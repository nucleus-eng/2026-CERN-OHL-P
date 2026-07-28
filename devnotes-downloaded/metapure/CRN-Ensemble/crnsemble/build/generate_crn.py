"""
Utilities to generate a Chemical Reaction Network (CRN) from a tabular
reaction-network description.

Given a CSV file specifying substrates, products, enzymes and mechanisms,
this module constructs biocrnpyler species, enzymes and reactions and
compiles them into a CRN object that can be simulated or analysed.
"""

import biocrnpyler as bcp
from biocrnpyler.core import Mixture
from biocrnpyler.components import Enzyme
from biocrnpyler.core.parameter import ParameterKey
from biocrnpyler.mechanisms import MichaelisMenten
import csv
import pandas as pd
import numpy as np
import math
import numpy
import crnsemble.mechanisms.new_reactions as new_reactions

def get_mechanism_dict(mechanism):

    """
    This function is used for the initiation of the parameters used for each mechanisms. In the specific parameters, the key values are use, the methods are used for
    for add_mechanism, and the parameters are used for the initiation of the CRN.
    """

    mechanism_dict = {
    "michaelis_menten_reverse_binding": 
        {
         'method' : bcp.mechanisms.MichaelisMentenReversible(),
         'n_elem_rxn': 3,
         'parameters': {
                "kcat": 1,
                "kcat_rev": 1,
                "kb1": 1,
                "ku1": 1,
                "kb2": 1,
                "ku2": 1
                        }
        },
    "elementary_rxns": 
        {
         'method' : new_reactions.MichaelisMentenReversibleMod(),
         'n_elem_rxn': 3,
         'parameters': {
                "kcat": 1,
                "kcat_rev": 1,
                "kb1": 1,
                "ku1": 1,
                "kb2": 1,
                "ku2": 1
                        }
        },
    "michalis_menten": 
      {
        'method': bcp.mechanisms.MichaelisMenten(), # This is a function so calling it will return the mechanism object not the function itself
        'n_elem_rxn': 3,
        'parameters': {                
                "kcat": 1,
                "kb": 1,
                "ku": 1
                       }
      },
    "mass_action":
     {
        'method': bcp.MassAction(k_forward = 1, k_reverse = 1.0),
        'n_elem_rxn': 2,
        'parameters':
        {
            'k_forward' : 1.0,
            'k_reverse' : 1.0
        }

    },
    "inlet/outlet":
     {
        'method': bcp.OneStepPathway(),
        'n_elem_rxn': 2,
        'parameters':
        {
                'k_prod' : 1,
                'k_deg' : 1
        }

    }


    }
    return mechanism_dict[mechanism]
    


# def get_enzyme_rxn_params (reactions, rxn_iter, react_mechanism,  params = None):
def get_enzyme_rxn_params (comp_object, react_mechanism):

    # if "parameters" in enzyme_def:
    # react_mechanism = reactions.loc[rxn_iter, 'Mechanism']

    mechanism_key = getattr(get_mechanism_dict(react_mechanism)['method'], "name")

    specific_parameters = {}

    # if not params:   

    for param_name, param_value in get_mechanism_dict(react_mechanism)["parameters"].items():

        # if reactions.loc[rxn_iter, 'Type'] == 'Enzymatic':
        if isinstance(comp_object, bcp.components.Enzyme):

            # param_key = ParameterKey(mechanism=react_mechanism, part_id = reactions.loc[rxn_iter,'Enzyme'], name=param_name)
            

            param_key = ParameterKey(mechanism=mechanism_key, part_id = comp_object.name, name=param_name)
            
        # elif reactions.loc[rxn_iter, 'Type'] in ['inlet', 'outlet']:
        
        elif isinstance(comp_object, bcp.components.Metabolite):
            
            if param_name == 'k_prod':
                # param_id =  f'{reactions.loc[rxn_iter,'Type']}_production'
                param_id =  f'{comp_object.name}_production'
            else:
                # param_id =  f'{reactions.loc[rxn_iter,'Type']}_degredation'
                param_id =  f'{comp_object.name}_degradation'
            k_param = 'k'
            print(f"{mechanism_key} - {param_id} - {k_param}")
            param_key = ParameterKey(mechanism=mechanism_key, part_id = param_id, name=k_param)

        key_val_pair = {param_key: param_value}

        specific_parameters.update(key_val_pair)


    return specific_parameters

def data_to_species (data):

    # Collect all species names from both columns, supporting entries
    # with multiple species separated by spaces (e.g. "x1 x2").
    species_names = []
    for col in ["Substrates", "Products"]:
        for val in data[col]:
            if pd.isna(val):
                continue
            species_names.extend(str(val).split())

    unique_species = sorted(set(species_names))

    speicies_object_vec = {}
    for species in unique_species:
        speicies_object_vec[species] = bcp.Species(species, material_type=f'm{species}')

    return speicies_object_vec



def gen_CRN_components(rxn_data, species_data):

    # enzyme_obj_dict =  {'enzyme_list': [], 'enzym_rxn_params' : {}}

    mixture_data  =  {'comp_list': [], 'comp_params': {}}

    rxn_obj_list = []

    # inlet_obj_list = []

    # enzyme_obj_list = []

    for rxn_iter in rxn_data.index:

        reaction = rxn_data.loc[rxn_iter]

        if pd.isna(reaction['Substrates']):
            substrate_species = []
        else:
            substrate_species = [
                    species_data[k] for k in str(reaction['Substrates']).split()
                ]


        if pd.isna(reaction['Products']):
            products_species = []
        else:
            products_species = [
                    species_data[k] for k in str(reaction['Products']).split()
                ]
            
        
        if reaction['Type'] in ['input', 'output']:

            mixture_data = _update_inlet_coms(reaction, substrate_species , products_species, mixture_data)


        elif rxn_data.loc[rxn_iter, 'Type'] == 'Enzymatic':

            mixture_data = _update_enzyme_comps(reaction, substrate_species, products_species , mixture_data)
            
        elif rxn_data.loc[rxn_iter, 'Type'] == 'Non-Enzymatic':

            rxn_obj_list = _update_rxn_coms(reaction, substrate_species, products_species, rxn_obj_list)
            

    
    return mixture_data, rxn_obj_list
            

def _update_enzyme_comps(reaction, substrate_species, products_species, mixture_data):


    enzyme_name = reaction["Enzyme"]

    # substrate_species = [species_data[k] for k in substrates]

    # products_species = [species_data[k] for k in products]


        # # Handle substrates (can be single string or list)
    enzyme = Enzyme(enzyme_name, substrates = substrate_species, products = products_species)

    # if enzymatic_reactions[rxn_iter]['mechanism'['method']] != 'michalis_menten':
    react_mechanism = get_mechanism_dict(reaction['Mechanism'])
    # custom_mechanisms = {react_mechanism.mechanism_type:react_mechanism}
    enzyme.add_mechanism(react_mechanism['method'])


    mixture_data['comp_list'].append(enzyme)

    # mechanism_key = getattr(react_mechanism['method'], "name", reaction['Mechanism'])
    rxn_params = get_enzyme_rxn_params(enzyme,  reaction['Mechanism'])

    mixture_data['comp_params'].update(rxn_params)

    return mixture_data



def _update_rxn_coms(reaction, substrate_species, products_species, rxn_obj_list):

    propensity = get_mechanism_dict(reaction['Mechanism'])['method']

    R1 = bcp.Reaction(substrate_species, products_species, propensity)

    rxn_obj_list.append(R1)

    return rxn_obj_list




def _update_inlet_coms(reaction, substrate_species, products_species, mixture_data):

    """

    Create inlet (or outlet) components for metabolite flows using OneStepPathway.

    For an 'Inlet' row whose Product is, say, 'A', we create a Metabolite
    component named 'input_A' which, when combined with the OneStepPathway
    mechanism, yields reactions like:

        -> metabolite[input_A]
        metabolite[input_A] -> mA[A]

    The actual kinetics (input_production / input_degredation) are provided
    via ParameterKey entries in the Mixture parameters.

    """


    if reaction['Type'] == 'input':

        metab_name = reaction["Products"]
        # product_species = species_data[product_name]
        precursors = [None]

        products = products_species

        # products=[species_data[metab_name]]


    elif reaction['Type'] == 'output':

        metab_name = reaction["Substrates"]
        # product_species = species_data[product_name]
        precursors = substrate_species

        products=[None]


    metab_object = bcp.Metabolite(

        f"{reaction['Type']}_{metab_name}",

        precursors=precursors,

        products=products,
    )


    flow_mechanism = get_mechanism_dict(reaction['Mechanism'])

    
    metab_object.add_mechanism(flow_mechanism['method'])


    mixture_data['comp_list'].append(metab_object)


    rxn_params = get_enzyme_rxn_params(metab_object, reaction['Mechanism'])

    
    mixture_data['comp_params'].update(rxn_params)


    return mixture_data

def build_CRN(input_pd_data, mixture_data, rxn_data,  flux_data):

    """
    This Module builds the CRN using Mixture and the reactions. The Mixture, contains the information of the inputs, outputs, and the enzymes. Using the mixtures,
    The CRN is built. Thereafter, the reactions are added to the CRN.
    """

    # This function builds the CRN 

    M = Mixture('Metabolic Network', components=mixture_data['comp_list'], 
            parameters=mixture_data['comp_params']
            # ,mechanisms=enzyme_mechanisms
            )
    CRN = M.compile_crn()

    CRN.net_fluxes = flux_data
    
    CRN.input_data = input_pd_data

    for rxn in rxn_data:

        CRN.add_reactions(rxn)

    return CRN


def generate_crn(metab_network, default_mechanism='michalis_menten', mixture_name="CRN Mixture",  output_file=None, return_crn=True):

    """
    Generate a Chemical Reaction Network (CRN) from a CSV reaction-network file.

    Parameters
    ----------

    metab_network : str or path-like
        Path to a CSV file describing the reaction network. The file is
        expected to contain at least the columns ``Substrates``, ``Type``, ``Products``,
        ``Enzyme`` and ``Mechanism``. Enzymatic reactions are converted into
        biocrnpyler `Enzyme` components with appropriate mechanisms and
        parameters; The Uptake, and degeneration reactions are added to the CRN as a mixture, and non-enzymatic reactions are added directly to the CRN.
    default_mechanism : str, optional
        Default mechanism label to use when constructing reactions. The
        current implementation infers mechanisms from the CSV ``Mechanism``
        column and does not explicitly use this argument, but it is kept
        for compatibility.
    mixture_name : str, optional
        Name for the underlying biocrnpyler `Mixture`. Reserved for future
        use; not currently used inside this helper.
    output_file : str or None, optional
        Reserved for future use. If implemented, this would allow writing a
        textual representation of the compiled CRN to disk.
    return_crn : bool, optional
        If True (default), the compiled CRN object is returned. At present the
        CRN is always returned regardless of this flag.

    Returns
    -------
    CRN : bcp.ChemicalReactionNetwork
        The compiled Chemical Reaction Network constructed from the CSV file.
    """
    # Generate compatible objects with biocrnpyler

    input_pd_data = pd.read_csv(metab_network)

    species_data = data_to_species(input_pd_data)

    mixture_data, rxn_obj_list = gen_CRN_components(input_pd_data, species_data)

    flux_data = {k: input_pd_data.loc[k,'Fluxes'] for k in input_pd_data.index}


    CRN = build_CRN(input_pd_data, mixture_data, rxn_obj_list, flux_data)
    
    return CRN


# Example usage
if __name__ == "__main__":
    # Define species

    reaction_net_data = 'Reaction-network2.csv'

    # reaction_net_data = 'RN_test.csv'

    # init_data = 'species_initial_concentrations.csv'

    # reaction_mat_data = csv_to_components(reaction_net_data)

    crn = generate_crn(reaction_net_data)

    print(crn.pretty_print(show_material=True, show_rates=True, show_attributes=True))
    
    # )

"""
The following must be changed in this module:

The _update_inlet_comps is not modular, and is solely based on the 

"""