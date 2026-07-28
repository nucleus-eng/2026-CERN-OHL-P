from opentrons import protocol_api
import logging
import pandas as pd
import numpy as np

from bnext_local.instrument.opentrons.helper.file_merger import reaction_name
from bnext_local.instrument.opentrons.helper.labware_module_helpers import get_custom_pure_liquids, setup_labware, load_liquids, reagents_from_df
import sys

log = logging.getLogger(__name__)
from energy_mix_params import PARAMETERS, requirements, smix_final_volume, smix_reagents_to_mix, pure_master_mix_reagents, reaction_volume
from bnext_local.instrument.opentrons.helper.custom_classes import PlateTracker
from bnext_local.instrument.opentrons.helper.protocol_helpers import get_logger, make_master_mixes, make_master_mixes_old, distribute_mms, configure_then_transfer_to_well, mix_wells
from bnext_local.cdk.src.cdk.calculators.sweep_calculator import generate_smix_and_sweep_tables, check_valid_input_params
from bnext_local.instrument.opentrons.helper.custom_classes import Reagent

metadata = {
    "protocolName": "Small Molecule Mix Assembly - For Lab Craft",
    "description": "Assemble Energy Mix solution from standard components",
    "author": "Sharon Newman <sharon@bnext.bio>",
}

CUSTOM_PURE_LIQUIDS = [] #TODO currently global...maybe not great as we scale this up?

def run(protocol: protocol_api.ProtocolContext):
    log = get_logger(protocol)
    log("########################### STARTING PROTOCOL ###########################")
    # Set up params
    # reaction_volume = protocol.params.reaction_volume #should this be import csv?
    scalar_for_pipette_error = protocol.params.scalar_for_pipette_error

    chute, p50, p50_tips, temp_module, plates  = setup_labware(protocol)
    plates["master_mix_plate"] = PlateTracker(protocol, "opentrons_24_aluminumblock_nest_1.5ml_snapcap"
                                        , "C2", label="master_mix")
    temp_module.set_temperature(4)

    global CUSTOM_PURE_LIQUIDS
    CUSTOM_PURE_LIQUIDS = get_custom_pure_liquids(protocol, p50, p50_tips, reaction_volume)

    reagent_info = reagents_from_df(REAGENTS)
    reagent_info['master_mix']["reservoir"] = "master_mix_plate"

    # Update REAGENT_INFO with custom pure liquid definitions
    def update_reagents_with_liquid_class(reagent_info):
        for reagent_name, reagent in reagent_info.items():
            if reagent["liquid_type"] in CUSTOM_PURE_LIQUIDS:
                reagent["liquid_type"] = CUSTOM_PURE_LIQUIDS[reagent["liquid_type"]]

    update_reagents_with_liquid_class(reagent_info)
    reagents = load_liquids(reagent_info, plates, protocol)

    log("Begin Making Energy Mix")

    smix_table = pd.DataFrame(BASE_MASTER_MIX)
    smix_final_volume = smix_table['total_master_mix_volume_ul'][0]
    smix_vol_to_distribue = smix_table['base_master_mix_vol_to_add_ul'][0]


    mms = make_master_mixes(smix_table, reagents, plates['master_mix_plate'],
                                         p50, log, well_volume=smix_final_volume, num_mms=1, mix_reps=25,
                                         mm_label="master_mix", flow_rate=35, volume_scalar=1)[0]

    log("Distributing PURE Master Mix")
    # Assign specific destination wells from discovery plate pipeline CSV
    sample_well_ids = [row["well_id"] for row in SAMPLES_TITRATION_LABCRAFT]
    dest_wells = plates['dest_plate'].assign_wells(sample_well_ids, "ot_mm")
    
    dest_wells = distribute_mms(mms, CUSTOM_PURE_LIQUIDS['final_asp_mix'], p50, plates=plates,
                                reaction_volume=smix_vol_to_distribue, log=log, dest_wells=dest_wells, dest_label="ot_mm")

    # _ = plates['dest_plate'].initiate_next_wells(3, "Standard")

    platemap_file_path = f'/Volumes/bnext/experiments/ot_platemaps/{sys.argv[1].split(".")[0].split("/")[-1]}_platemap.csv'
    plates['dest_plate'].save_tracked_wells(platemap_file_path, log)

    # log(f'******* MMs at:  \n {mms} ')
    log("Protocol Complete")