"""
Refined variant of sample_gen with improved net->elementary reaction mapping.

This module reuses the existing sampling and kinetic-parameter code from
sample_gen, but replaces the mapping logic with a stricter, structure-aware
matcher.
"""
from math import nan
import biocrnpyler as bcp
# from biocrnpyler.core import Mixture
# from biocrnpyler.components import Enzyme
# from biocrnpyler.core.parameter import ParameterKey
# from biocrnpyler.mechanisms import MichaelisMenten
# import csv
import pandas as pd
import numpy as np
import crnsemble.build.generate_crn as gen_crn
import crnsemble.simulation.kinetic_sim as kinetic_sim
import numpy
import math
from collections import Counter
# import sample_gen as _base
# from sample_gen import *  # noqa: F401,F403


def _is_missing(value):
    # This function returns True if `value` is either:
    # - None (i.e., missing or not set)
    # - a float which is NaN (Not a Number, i.e., a missing or undefined numerical value)
    return value is None or (isinstance(value, float) and math.isnan(value))


def _safe_get(row, *col_names):
    for name in col_names:
        if name in row.index:
            val = row[name]

            if pd.isna(val) or not isinstance(val, str):
                value = val
            else:
                parts = val.split()
                value = parts if len(parts) >= 2 else val
            # value = row[name]
            if not _is_missing(value):
                return value
    return None


def _net_rxn_id(net_reaction_id):
    """
    Canonical identifier for net reactions.
    Uses only the row index/id from crn.input_data.
    """
    return net_reaction_id


def _reaction_side_names(reaction):
    lhs = {sp.name for cx in reaction._input_complexes for sp in [cx.species]}
    rhs = {sp.name for cx in reaction._output_complexes for sp in [cx.species]}
    return lhs, rhs


def _reaction_constituent_names(reaction):
    """
    Names of species involved directly OR as constituents of complexes.
    This allows matching steps where only complexes appear, but those complexes
    contain the substrate/product/enzyme.
    """
    names = set()
    for sp in reaction.species:
        names.add(sp.name)
        if sp.material_type == "complex":
            for sub_sp in sp.species:
                names.add(sub_sp.name)
    return names


def _reaction_contains_enzyme(reaction, enzyme_name):
    if enzyme_name is None:
        return False
    enzyme_name = str(enzyme_name)

    for sp in reaction.species:
        if sp.material_type == "protein" and sp.name == enzyme_name:
            return True
        if sp.material_type == "complex":
            # Complex species carry the component species list in .species.
            if any(sub_sp.name == enzyme_name for sub_sp in sp.species):
                return True
    return False


def _row_matches_reaction(row, reaction):
    rxn_type = str(_safe_get(row, "Rxn_Type", "Type") or "")
    substrate = _safe_get(row, "Substrates")
    product = _safe_get(row, "Products")
    enzyme_name = _safe_get(row, "Enzyme")
    lhs, rhs = _reaction_side_names(reaction)
    all_names = lhs | rhs

    if rxn_type == "Enzymatic":
        if not _reaction_contains_enzyme(reaction, enzyme_name):
            return False
        # Elementary enzymatic steps may contain only complexes (e.g., ES -> EP),
        # where the substrate/product doesn't appear as a free species. We therefore
        # match against both direct species names and complex constituents.
        participating = _reaction_constituent_names(reaction)

        if isinstance(product, list):
            prod_match = any(p in participating for p in product)
        else:
            prod_match = product is not None and product in participating
        if isinstance(substrate, list):
            sub_match = any(p in participating for p in substrate)
        else:
            sub_match = substrate is not None and substrate in participating
        # sub_match = substrate is not None and substrate in participating
        # prod_match = product is not None and product in participating
        return sub_match or prod_match

    if rxn_type == "Non-Enzymatic":
        sub_ok = substrate is None or str(substrate) in lhs
        prod_ok = product is None or str(product) in rhs
        return sub_ok and prod_ok

    if rxn_type == "input":

        metab = str(product)
        intermediate = f"input_{metab}"
        return intermediate in all_names

    if rxn_type == "output":
        # For an output of metabolite X, OneStepPathway yields:
        #   1) X -> output_X
        #   2) output_X ->
        # So we match reactions containing either X or the generated intermediate output_X.
        if substrate is None:
            return False
        metab = str(substrate)
        intermediate = f"output_{metab}"
        return intermediate in all_names

    # Fallback to directional exact-name matching for unknown types.
    sub_ok = substrate is None or str(substrate) in lhs
    prod_ok = product is None or str(product) in rhs
    return sub_ok and prod_ok


def map_net_to_crn_rxn(mapping, net_reaction_id, crn):
    row = crn.input_data.loc[net_reaction_id]
    net_id = _net_rxn_id(net_reaction_id)

    excl_rxn_id = []
    for rxn_id, reaction in enumerate(crn.reactions):

        if len(mapping[net_id]) == gen_crn.get_mechanism_dict(row['Mechanism'])['n_elem_rxn']:
            break
        if _row_matches_reaction(row, reaction):

            if rxn_id in excl_rxn_id:
                continue


            mapping[net_id].append(rxn_id)
            excl_rxn_id.append(rxn_id)

    return mapping


def get_elementary_indicex_dict(crn):
    """
    Build net-reaction -> elementary reaction indices mapping.
    """
    mapping = {}
    for net_reaction_id in crn.input_data.index:
        net_id = _net_rxn_id(net_reaction_id)
        mapping.setdefault(net_id, [])
        map_net_to_crn_rxn(mapping, net_reaction_id, crn)

    # keep deterministic ordering and remove accidental duplicates
    for key, ids in mapping.items():
        mapping[key] = sorted(set(ids))
    return mapping

def _rev_vals_in_dG_range(crn, rev_vals, net_reaction_id):
    """
    Return True iff (ΔG_i/RT)_lower ≤ sign(V_{i,net}^ref) Σ_j ln(R_{i,j}^ref) ≤ (ΔG_i/RT)_upper.

    Parameters
    ----------
    rev_vals : array_like
        Sampled reference reversibilities R_{i,j}^ref (strictly positive).
    v_net_ref : float
        Reference net flux V_{i,net}^ref for the net reaction (same sign as crn.net_fluxes).
    dg_rt_lower, dg_rt_upper : float or None
        Dimensionless Gibbs bounds (ΔG/RT); if either is missing, the check is skipped (returns True).
    """

    dg_rt_lower, dg_rt_upper = crn.input_data.loc[net_reaction_id, ['dGlow','dGhigh']].astype(float).values

    v_net = crn.net_fluxes[net_reaction_id]

    RT = 0.592 # kcal / mol
    lhs = float(np.sign(v_net)) * float(np.sum(np.log(rev_vals)))
    lo = float(dg_rt_lower / RT)
    hi = float(dg_rt_upper / RT)
    return lo <= lhs <= hi

    
def _sample_reversibility(crn, net_reaction_id, mapping):
    elem_rxn = mapping[_net_rxn_id(net_reaction_id)]
    rxn_type = str(_safe_get(crn.input_data.loc[net_reaction_id], "Rxn_Type", "Type") or "")
    
    if rxn_type == "Enzymatic":
        rev_vals = np.random.rand(len(elem_rxn))

    #     while not _rev_vals_in_dG_range(crn, rev_vals, net_reaction_id):
    #         rev_vals = np.random.rand(len(elem_rxn))
        

    # # if len(elem_rxn) == 0:
    # #     rev_vals = np.array([])

    # # if crn.reactions[elem_rxn[0]].is_reversible:
    # #     rev_vals = np.random.rand(len(elem_rxn))
    else: 
        rev_vals = np.zeros(len(elem_rxn))
    return rev_vals


def sample_reversibilities(crn, mapping):
    revers = {}
    for net_reaction_id in crn.input_data.index:
        revers[_net_rxn_id(net_reaction_id)] = _sample_reversibility(crn, net_reaction_id, mapping)
    return revers


def _sample_enzyme_fracs():


    # elm_rxn = mapping[rxn
    # if crn.input_data.loc[rxn, 'Rxn_Type'] == 'Enzymatic':

    r1 = np.round(np.random.uniform(0,1), 3)
    r2 = np.round(np.random.uniform(0, 1 - r1), 3)
    r3 = np.round(1 - r1 - r2, 3)
    r3 += 1 - (r1 + r2 + r3)

    fracs = [r1, r2, r3]
    
    # else:
    #     fracs = np.zeros(1)

    return fracs


def get_list_elem(crn, protein_species, enzyme_fracs_dict, mapping):
    """
    Assign sampled fractions to a protein and its complexes by exploring
    all elementary reactions connected to net reactions catalyzed by protein.
    """
    enzyme_fracs = _sample_enzyme_fracs()
    protein_name = protein_species.name

    protein_net_ids = [
        rid for rid in crn.input_data.index
        if str(_safe_get(crn.input_data.loc[rid], "Enzyme") or "") == protein_name
    ]
    explore_rxns = sorted({rxn_id for rid in protein_net_ids for rxn_id in mapping.get(rid, [])})

    enzyme_comp_id = 0
    for elem_rxn_id in explore_rxns:
        for species in crn.reactions[elem_rxn_id].species:
            if enzyme_comp_id >= len(enzyme_fracs):
                break

            if species.material_type not in ["protein", "complex"]:
                continue

            if enzyme_fracs_dict[species] is nan:
                if species.material_type == "protein" and species.name == protein_name:
                    enzyme_fracs_dict[species] = enzyme_fracs[enzyme_comp_id]
                    enzyme_comp_id += 1
                elif species.material_type == "complex" and protein_species in species.species:
                    enzyme_fracs_dict[species] = enzyme_fracs[enzyme_comp_id]
                    enzyme_comp_id += 1

        if enzyme_comp_id >= len(enzyme_fracs):
            break

    return enzyme_fracs_dict


def sample_enzyme_fracs(crn, mapping):
    enzyme_fracs_dict = {k: nan for k in crn.species}

    for species in crn.species:
        if enzyme_fracs_dict[species] is nan:
            if species.material_type == "protein":
                enzyme_fracs_dict = get_list_elem(crn, species, enzyme_fracs_dict, mapping)
            else:
                enzyme_fracs_dict[species] = 1

    return enzyme_fracs_dict


def build_elementary_fluxes(crn, mapping, reverse_map):
    records = []

    for net_idx, row in crn.input_data.iterrows():
        net_id = _net_rxn_id(net_idx)
        v_net = crn.net_fluxes[net_idx]
        elem_ids = mapping[net_id]
        r = np.asarray(reverse_map[net_id])
        if len(elem_ids) == 0:
            continue

        direction = np.sign(v_net)
        v_forward = v_net / (1.0 - r**direction)
        v_reverse = v_forward * r**direction

        for elem_idx, vf, vr, ri in zip(elem_ids, v_forward, v_reverse, r):
            records.append({
                "elem_rxn_id": elem_idx,
                "net_rxn_idx": net_idx,
                "net_rxn_name": net_id,
                "Rxn_Type": row["Type"] if "Type" in row.index else row["Rxn_Type"],
                "v_net": v_net,
                "reversibility": ri,
                "v_forward": vf,
                "v_reverse": vr,
            })

    elem_df = pd.DataFrame.from_records(records).set_index("elem_rxn_id").sort_index()
    crn.all_fluxes = elem_df
    return crn

def get_kinetic_params(crn, init_dict):


    for elem_rxn_id in crn.all_fluxes.index:


        rxn_name = crn.all_fluxes.loc[elem_rxn_id, 'net_rxn_name']



        substrates = [x.species for x in crn.reactions[elem_rxn_id]._input_complexes]

        products = [x.species for x in crn.reactions[elem_rxn_id]._output_complexes]

        forward_conc_multi = math.prod([init_dict[x] for x in substrates])
        
        backward_conc_multi = math.prod([init_dict[x] for x in products])

        if crn.reactions[elem_rxn_id].is_reversible:

            k_forward, k_reverse = crn.all_fluxes.loc[elem_rxn_id,['v_forward','v_reverse']]/[forward_conc_multi, backward_conc_multi]
            
            crn._reactions[elem_rxn_id]._propensity_type._k_forward._value = k_forward
            crn._reactions[elem_rxn_id]._propensity_type._k_reverse._value = k_reverse
        else: 
            k_forward = crn.all_fluxes.loc[elem_rxn_id,'v_forward']/forward_conc_multi
            crn._reactions[elem_rxn_id].propensity_type._k_forward= float(k_forward)

    return crn


def _get_kval_input(crn, elem_rxn_id, substrates, products, init_dict):

    if substrates == []:

        k_forward = crn.all_fluxes.loc[elem_rxn_id,'v_forward']
    
    else: 
        
        k_forward = np.random.uniform(0, 10)

        # init_dict [substrates[0]] = crn.all_fluxes.loc[elem_rxn_id,'v_forward'] / k_forward
        # conc_term_forw = np.sum([np.log(init_dict[x]) for x in substrates])
        # log_k_forward = np.log(crn.all_fluxes.loc[elem_rxn_id,'v_forward']) - conc_term_forw

        # k_forward = np.exp(log_k_forward)

    crn._reactions[elem_rxn_id].propensity_type._k_forward.value= float(k_forward)

    return crn, init_dict


def _get_kval_output(crn, elem_rxn_id, substrates, products, init_dict):

    if products == []:

        k_forward = np.random.uniform(0, 50)

        init_dict [substrates[0]] = crn.all_fluxes.loc[elem_rxn_id,'v_forward'] / k_forward
    
    else: 
        
        conc_term_forw = np.sum([np.log(init_dict[x]) for x in substrates])

        log_k_forward = np.log(float(crn.all_fluxes.loc[elem_rxn_id, "v_forward"])) - conc_term_forw

        k_forward = np.exp(log_k_forward)
        # conc_term_forw = np.sum([np.log(init_dict[x]) for x in substrates])
        # log_k_forward = np.log(crn.all_fluxes.loc[elem_rxn_id,'v_forward']) - conc_term_forw

        # k_forward = np.exp(log_k_forward)

    crn._reactions[elem_rxn_id].propensity_type._k_forward.value = float(k_forward)

    return crn, init_dict

def _get_k_val_reversible(crn, elem_rxn_id, substrates, products, init_dict):

    conc_term_forw = np.sum([np.log(init_dict[x]) for x in substrates])
    conc_term_back = np.sum([np.log(init_dict[x]) for x in products])

    v_forward = float(crn.all_fluxes.loc[elem_rxn_id, "v_forward"])
    v_reverse = float(crn.all_fluxes.loc[elem_rxn_id, "v_reverse"])
    log_k_forward = np.log(v_forward) - conc_term_forw
    log_k_reverse = np.log(v_reverse) - conc_term_back

    k_forward, k_reverse = np.exp([log_k_forward, log_k_reverse])
    
    crn._reactions[elem_rxn_id]._propensity_type._k_forward._value = k_forward
    crn._reactions[elem_rxn_id]._propensity_type._k_reverse._value = k_reverse

    return crn

def _get_kval_enzymes(crn, elem_rxn_id, substrates, products, init_dict):


    crn = _get_k_val_reversible(crn, elem_rxn_id, substrates, products, init_dict)

    return crn


def _get_kval_rxn(crn, elem_rxn_id, substrates, products, init_dict):

    if crn._reactions[elem_rxn_id].is_reversible:
        crn = _get_k_val_reversible(crn, elem_rxn_id, substrates, products, init_dict)
    else:

        conc_term_forw = np.sum([np.log(init_dict[x]) for x in substrates])

        log_k_forward = np.log(float(crn.all_fluxes.loc[elem_rxn_id, "v_forward"])) - conc_term_forw

        k_forward = np.exp(log_k_forward)
        # conc_term_forw = np.sum([np.log(init_dict[x]) for x in substrates])
        # log_k_forward = np.log(crn.all_fluxes.loc[elem_rxn_id,'v_forward']) - conc_term_forw

        # k_forward = np.exp(log_k_forward)

        crn._reactions[elem_rxn_id].propensity_type._k_forward = float(k_forward)
    
    return crn

def get_nondim_kin_params(crn, init_dict):


    for elem_rxn_id in crn.all_fluxes.index:





        substrates = [x.species for x in crn.reactions[elem_rxn_id]._input_complexes]

        products = [x.species for x in crn.reactions[elem_rxn_id]._output_complexes]

        # forward_conc_multi = math.prod([init_dict[x] for x in substrates])
        
        # backward_conc_multi = math.prod([init_dict[x] for x in products])

        if crn.all_fluxes.loc[elem_rxn_id, 'Rxn_Type'] == 'input':

            crn, init_dict = _get_kval_input(crn, elem_rxn_id, substrates, products, init_dict)
        
        if crn.all_fluxes.loc[elem_rxn_id, 'Rxn_Type'] == 'output':

            crn, init_dict =_get_kval_output(crn, elem_rxn_id, substrates, products, init_dict)
        
        if crn.all_fluxes.loc[elem_rxn_id, 'Rxn_Type'] == 'Enzymatic':
            crn = _get_kval_enzymes(crn, elem_rxn_id, substrates, products, init_dict)
        
        if crn.all_fluxes.loc[elem_rxn_id, 'Rxn_Type'] == 'Non-Enzymatic':
            crn = _get_kval_rxn(crn, elem_rxn_id, substrates, products, init_dict)

        # if crn.reactions[elem_rxn_id].is_reversible:

        #     conc_term_forw = np.sum([np.log(init_dict[x]) for x in substrates])
        #     conc_term_back = np.sum([np.log(init_dict[x]) for x in products])

            

        #     log_k_forward, log_k_reverse = np.log(crn.all_fluxes.loc[elem_rxn_id,['v_forward','v_reverse']])/[conc_term_forw, conc_term_back]

        #     k_forward, k_reverse = np.exp([log_k_forward, log_k_reverse])
            
        #     crn._reactions[elem_rxn_id]._propensity_type._k_forward._value = k_forward
        #     crn._reactions[elem_rxn_id]._propensity_type._k_reverse._value = k_reverse
        # # else: 
        #     if substrates == []:
        #         crn._reactions[elem_rxn_id].propensity_type._k_forward= float(crn.all_fluxes.loc[elem_rxn_id,'v_forward'])
        #         continue

        #     conc_term_forw = np.sum([np.log(init_dict[x]) for x in substrates])
        #     log_k_forward = np.log(crn.all_fluxes.loc[elem_rxn_id,['v_forward']])/[conc_term_forw]

        #     k_forward = np.exp([log_k_forward])
        #     crn._reactions[elem_rxn_id].propensity_type._k_forward= float(k_forward)

    crn.initial_concentration_dict = init_dict
    return crn

def sample_crn(crn):
    

    mapping = get_elementary_indicex_dict(crn)

    # Sample the enzyme fractions and use that to calculate the initial concentration values
    enzyme_frac_dict = sample_enzyme_fracs(crn, mapping)

    init_dict = kinetic_sim.get_init_dict(crn, enzyme_frac_dict)

    # Sample the mapping     
    reverse_map = sample_reversibilities(crn, mapping)


    # Generate the elemntary flux values
    crn = build_elementary_fluxes(crn, mapping, reverse_map)


    crn = get_nondim_kin_params(crn, init_dict)

    return crn


def gen_esemble(reaction_net_data, ensem_size):

    crn_vec = []

    for ensem_id in range(ensem_size):

    # Create the chemical reaction network object
        crn = gen_crn.generate_crn(reaction_net_data)

        crn = sample_crn(crn)

        crn_vec.append(crn)

    return crn_vec
if __name__ == "__main__":
    # import generate_crn as gen_crn
    # import kinetic_sim

    # import mass_balance

    reaction_net_data = "Reaction-network2.csv"
    conc_data_file = "species_initial_concentrations.csv"

    crn = gen_crn.generate_crn(reaction_net_data, conc_data_file)
    mapping = get_elementary_indicex_dict(crn)

    enzyme_frac_dict = sample_enzyme_fracs(crn, mapping)
    ss_conc_dict = kinetic_sim.get_init_dict(crn,  enzyme_frac_dict)

    reverse_map = sample_reversibilities(crn, mapping)
    crn = build_elementary_fluxes(crn, mapping, reverse_map)

    # mass_balance.assert_mass_balance(crn)
    crn = get_nondim_kin_params(crn, ss_conc_dict)
