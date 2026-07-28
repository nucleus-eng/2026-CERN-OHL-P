import csv
import crnsemble.build.generate_crn as gen_crn
import pandas as pd

def get_species_name_mapping(crn):
    """
    Build a mapping from species names used in the CSV file
    to the corresponding Species objects in the compiled CRN.
    """
    name_mapping = {}
    for species in crn.species:
        # species.name matches the label used in the CSV (e.g. "x1", "E1")
        name_mapping[species.name] = species
    return name_mapping

def _get_init_conc(species, cond_pd_data, enz_fracs = 1):
    """
    Retrieves the initial concentration for a given species from the provided DataFrame.
    For complex species (e.g., enzyme-substrate complexes), the initial concentration is
    calculated based on the corresponding parent's initial concentration and enzyme fractions.

    Args:
        species: The species object whose initial concentration is desired.
        cond_pd_data (pandas.DataFrame): DataFrame containing 'Species' and 'InitialConcentration' columns.
        enz_fracs (float or int, optional): Fraction for adjusting complexes, defaults to 1.

    Returns:
        float: The initial concentration for the given species.
    """
    if species.material_type == 'complex':
        parent_protein = next(x for x in species.species if x.material_type == 'protein')
        # Use .at for clean, efficient lookup by index after boolean indexing
        try:
            init_conc = cond_pd_data.loc[parent_protein.name, 'InitialConcentration'] 
        except KeyError:
            raise KeyError(f"Parent protein '{parent_protein.name}' not found in initial concentrations DataFrame.")
    else:
        try:
            init_conc = cond_pd_data.loc[species.name, 'InitialConcentration']
        except KeyError:
            init_conc = 0.0

    return float(init_conc) * enz_fracs



def _get_nondim_ss_conc(species, enz_fracs = 1):
    """
    Retrieves the initial concentration for a given species from the provided DataFrame.
    For complex species (e.g., enzyme-substrate complexes), the initial concentration is
    calculated based on the corresponding parent's initial concentration and enzyme fractions.

    Args:
        species: The species object whose initial concentration is desired.
        cond_pd_data (pandas.DataFrame): DataFrame containing 'Species' and 'InitialConcentration' columns.
        enz_fracs (float or int, optional): Fraction for adjusting complexes, defaults to 1.

    Returns:
        float: The initial concentration for the given species.
    """
    if species.material_type == 'complex':
        parent_protein = next(x for x in species.species if x.material_type == 'protein')
        # Use .at for clean, efficient lookup by index after boolean indexing
        try:
            init_conc = 1.0 
        except KeyError:
            raise KeyError(f"Parent protein '{parent_protein.name}' not found in initial concentrations DataFrame.")
    else:
        try:
            init_conc = 1
        except KeyError:
            raise KeyError(f"Parent protein '{species.name}' not found in initial concentrations DataFrame.")

    return float(init_conc) * enz_fracs



    # return init_conc
def get_init_dict(crn, enzyme_frac_dict):

    # cond_pd_data = pd.read_csv(conc_data_file).set_index('Species')

    init_cont_dict = {}
    # init_conc = csv.
    
    # conc_data_file = pd.read_csv('species_initial_concentrations.csv')
    # conc_map = dict(zip(conc_data['Species'], conc_data['InitialConcentration']))
    for species in crn.species:
        # if species.material_type == 'complex':
        #     parent_protein = [species_name_dict[x.name] for x in species.species if x.material_type == 'protein'][0]

        # init_cont_dict[species] = conc_map.get(species.name, 1)

        enz_frac = enzyme_frac_dict[species]

        init_cont_dict[species] = _get_nondim_ss_conc(species,  enz_frac)
    
    return init_cont_dict

def get_init_conc(crn, conc_data_file): # It will be removed

    cond_pd_data = pd.read_csv(conc_data_file).set_index('Species')

    

    init_cont_dict = {}
    # init_conc = csv.
    
    # conc_data_file = pd.read_csv('species_initial_concentrations.csv')
    # conc_map = dict(zip(conc_data['Species'], conc_data['InitialConcentration']))
    for species in crn.species:
        # if species.material_type == 'complex':
        #     parent_protein = [species_name_dict[x.name] for x in species.species if x.material_type == 'protein'][0]

        # init_cont_dict[species] = conc_map.get(species.name, 1)

        # enz_frac = enzyme_frac_dict[species]
        if species.name in cond_pd_data.index:
            init_cont_dict[species] = cond_pd_data.loc[species.name, 'InitialConcentration']
    
    return init_cont_dict

if __name__ == "__main__":
    # Define species

    reaction_net_data = 'Reaction-network.csv'

    conc_data_file = 'species_initial_concentrations.csv'

    # reaction_mat_data = csv_to_components(reaction_net_data)

    crn = gen_crn.generate_crn(reaction_net_data, conc_data_file)

    get_init_conc = get_init_conc(crn, conc_data_file)

    print(crn.pretty_print(show_material=True, show_rates=True, show_attributes=True))