from opentrons import protocol_api
import csv
import os
import sys
from opentrons import protocol_api
import random

RANDOM_SEED = 513

class PlateTracker(protocol_api.Labware):
    """
    Extension of an Opentrons Labware object that tracks usage and sample labels

    A "plate" can be things like a 96 well plate or reagent reservoir that has wells to access
    This holds memory of sample locations on the plate and provides easy ways to update information
    A plate has the following components: TODO: update this list
    - label (str)- the name of plate we want.
    - plate (Obj) - the OpenTron labware object that has wells to access
    - num_wells_used (int) - the number of wells that have been used up
    - well_tracker(dict) - keys are labels regarding what is in the particular well.
                            values are the well locations on the plate pertaining to those samples
    """

    def __init__(self, module, plate_type='biorad_96_wellplate_200ul_pcr',
                 location=1, label='', is_checkerboard=False, randomize_wells=False):
        """
        Initiates information that is useful for a plate
        :param name: labwares name
        :param module: can be either a opentrons Labware OR a ProtocolContext object
        :param location: where labware will be
        :param plate_type: type of plate to be loaded
        :param is_checkerboard: well layout will be every other spacing
        """
        # Initialize LabWare
        if isinstance(module, protocol_api.protocol_context.ProtocolContext): # check if "protocol"
            plate = module.load_labware(plate_type, location=location, label=label)
        # check if labware module (i.e. temp_deck, mag_deck, tc_mod...)
        elif isinstance(module, protocol_api.labware.Labware) \
                or isinstance(module, protocol_api.module_contexts.MagneticModuleContext) \
                or isinstance(module, protocol_api.module_contexts.ThermocyclerContext) \
                or isinstance(module, protocol_api.module_contexts.TemperatureModuleContext):
            plate = module.load_labware(plate_type, label=label)
        else:  # you input something unexpected.
            raise AssertionError(
                f'Incorrect module type. Insert either a ProtocolContext or Labware: %s' % type(module))

        # initialize base Labware class with the *real* labware attributes
        super().__init__(
            plate._core,   # internal core object from Opentrons
            plate._api_version,
            plate._protocol_core,
            plate._core_map
        )

        # custom
        self.label = label # Redundant since inheriting Labware
        self.num_wells_used = 0
        self.well_tracker = {}
        self.is_checkerboard = is_checkerboard
        self.randomize_wells = randomize_wells
        self.available_wells  = self.wells()

        if is_checkerboard:
            self._get_checkerboard_indices()
        if randomize_wells:
            self._randomize_wells()

    def _randomize_wells(self):
        random.seed(RANDOM_SEED)
        random.shuffle(self.available_wells)

    def _get_checkerboard_indices(self):
        """
        Return the flat indices of cells that would be blank in a checkerboard pattern.
        Matrix is flattened column-major: [*col1, *col2, ...].
        """
        available_wells = []
        wells = self.wells()
        nrows = len(self.rows())
        ncols = len(self.columns())
        for r in range(nrows): ## Change order of this
            for c in range(ncols):
                if (r + c) % 2 == 0:  # checkerboard condition
                    idx = c * nrows + r  # column-major flattening
                    available_wells.append(wells[idx])
        self.available_wells = available_wells

    def reset_tracking(self):
        """
        Reset tracked well usage.
        Useful after user swaps in new physical plates at the same deck slots.
        """
        self.num_wells_used = 0
        self.well_tracker = {}
        self.available_wells = self.wells()
        if self.is_checkerboard:
            self._get_checkerboard_indices()
        if self.randomize_wells:
            self._randomize_wells()

    def get_sample_wells(self, label):
        """
        Get the wells that are used for the label
        :param label:
        :return:
        """
        if label in self.well_tracker.keys():
            print(f'Current wells used: %s' % self.well_tracker[label])
            return self.well_tracker[label]
        raise AssertionError(
            f"incorrect key provided ('{label}'). "
            f"Available keys are: {list(self.well_tracker.keys())}"
        )

    def show_well_status(self, ):
        """
        Check what is in the wells
        """
        print(f'Number of wells used: %s' % self.num_wells_used)
        print(f'Wells: %s' % self.well_tracker)

        # return ''

    def _get_used_wells_flat(self):
        """

        :return: flatted list of all the wells on a plate [A1 ... H12]
        """
        flat_list = []
        for cur_wells in self.well_tracker.values():
            if isinstance(cur_wells, list):
                flat_list.extend(cur_wells)
            else:
                flat_list.append(cur_wells)
        return flat_list

    def _update_label_if_repeat(self, label):
        """

        :param label: desired label to name well
        :return: Updated label with label_1 or next numeric iteration of the name
        """
        if label in self.well_tracker.keys():
            suffix = 1
            new_string = f"{label}_{suffix}"
            while new_string in self.well_tracker.keys():
                suffix += 1
                new_string = f"{label}_{suffix}"
            print(f'NEW LABEL CREATED %s' % new_string)
            return new_string
        return label

    def initiate_next_wells(self, sample_number, label, from_bottom_right = False):
        """
        Assigns the next available wells on the plate and updates the well_tracker
        :return: Available wells
        """
        # cur_wells_flat = self._get_used_wells_flat()
        # available_wells = [well for well in self.plate.wells() if well not in cur_wells_flat]
        available_wells = self.available_wells

        # print(f'available wells {available_wells}')
        label = self._update_label_if_repeat(label)

        if from_bottom_right:
            available_wells = available_wells[::-1]
        if len(available_wells) >= sample_number:
            self.well_tracker[label] = available_wells[:sample_number] #add to used

            #Update the wells that are still free
            updated_wells = available_wells[sample_number:]
            if from_bottom_right:
                updated_wells = updated_wells[::-1] # kind of redundant...
            self.available_wells = updated_wells #rm from available
        else:
            raise AssertionError(f'No more wells in %s left!' % self.label)

        self.num_wells_used += sample_number
        return self.well_tracker[label]

    def assign_wells(self, well_ids, label):
        """
        Assign specific wells by ID (e.g., ['E18', 'J8', 'F7']) to a label.
        Unlike initiate_next_wells which picks the next available wells sequentially,
        this method assigns the exact wells specified.

        :param well_ids: List of well ID strings (e.g., ['A1', 'B2', 'C3'])
        :param label: Label to track these wells under
        :return: List of assigned well objects
        """
        wells_by_name = self.wells_by_name()
        assigned = []
        for wid in well_ids:
            well = wells_by_name.get(wid)
            if well is None:
                raise ValueError(f"Well '{wid}' not found on plate '{self.label}'")
            assigned.append(well)
            if well in self.available_wells:
                self.available_wells.remove(well)

        label = self._update_label_if_repeat(label)
        self.well_tracker[label] = assigned
        self.num_wells_used += len(assigned)
        return assigned

    def assign_well(self, label, well_id=None,
                    liquid_params=None, protocol=None):
        """
        Assigns a specific well to a label and updates the well_tracker
        :param label:
        :param well_id:
        :return: the well for that sample
        """
        # 1) Source well_id from liquid_params if provided
        if liquid_params is not None:
            well_id = liquid_params.get("well_id", well_id)

        wells = self.wells_by_name()
        # 2) Try to resolve the requested well (if any)
        well = None
        if well_id is not None:
            well = wells.get(well_id, None)

        # 3) If well is None (no ID or invalid), allocate a new one
        if well is None:
            self.well_tracker[label] = self.initiate_next_wells(1, label)
            well_id = self.well_tracker[label][0]
            well = self.well_tracker[label]

        # 4) If this well is already tracked, allocate a fresh one for this label
        elif well in self.well_tracker.values():
            self.well_tracker[label] = self.initiate_next_wells(1, label)
            well_id = self.well_tracker[label][0]
            # well = self.well_tracker[label]

        # 5) Otherwise, first time using this existing well
        else:
            self.well_tracker[label] = well
            if well in self.available_wells:
                self.available_wells.remove(well)

        # if self.wells_by_name()[well_id] in self.well_tracker.values():
        #     # Well already exists! Assign a new name.
        #     self.well_tracker[label] = self.initiate_next_wells(1, label)
        #     well_id = self.well_tracker[label][0]
        # else:
        #     self.well_tracker[label] = self.wells_by_name()[well_id]
        #     self.available_wells.remove(self.well_tracker[label]) #rm from available
        self.num_wells_used += 1

        if liquid_params is not None:
            assert protocol is not None, "protocol is not provided. To assign a specific liquid, add protocol"
            liquid_definition = protocol.define_liquid(name=label,
                                                       description=liquid_params['description'],
                                                       display_color=liquid_params['display_color'])
            self.load_liquid(wells = [well_id],
                             volume = liquid_params['volume'],
                             liquid = liquid_definition)
            if isinstance(self.well_tracker[label], list):
                return LiquidTracker(label, self.well_tracker[label][0], liquid_params)
            return LiquidTracker(label, self.well_tracker[label], liquid_params)

        return self.well_tracker[label]

    def save_tracked_wells(self, file_path, log):
        """Save wells to CSV if local, otherwise log to comments on robot."""

        if os.environ.get("OT_SIMULATE_CSV"):
            log(f'PlateMap saved to {file_path}')
            with open(file_path, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Well", "Name"])  # header

                for key, wells in self.well_tracker.items():
                    for well in wells:
                        writer.writerow([well.well_name, key])
        else:
            log(f'Attempted to save plate map to {file_path},'
                f'But the environment variable "OT_SIMULATE_CSV" is not set.'                
                f'To save the plate map on this machine, run: export OT_SIMULATE_CSV=1'
                f'Do not set on OT since it is a write only machine')



class LiquidTracker(protocol_api.Well):
    def __init__(self, name, well: protocol_api.Well, liquid_params):
        """
        Inherit protocol_api.Well and track liquids
        """
        # Initialize parent Well with internal attributes of the provided well
        super().__init__(
            well._parent,    # labware
            well._core,      # internal core object
            well._api_version
        )

        # Liquid tracking dictionary
        self.name = name
        self.stock_conc = liquid_params['stock_conc']
        self.units = liquid_params['units']
        self.liquid_type = liquid_params['liquid_type']
        self.liquids = {}
        self.params = liquid_params

    def __call__(self):
        """
        When called, behave like a normal well
        """
        return self

    def __repr__(self):
        return f"<LiquidTracker {self.well_name}>"

from dataclasses import dataclass, field
from collections.abc import MutableMapping

@dataclass
class Reagent(MutableMapping):
    reservoir: str
    well_id: str
    volume: float = 100 #default volume
    display_color: str | None = None
    stock_conc: float | None = None
    final_pure_conc: float | None = None
    units: str | None = None
    liquid_type: str = "water_mix"
    description: str = ""
    artifact_num: str | None = None
    # internal dict to store key-value pairs
    _dict: dict = field(init=False, repr=False)

    def __post_init__(self):
        # generate random color if not provided
        if self.display_color is None:
            self.display_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        self._dict = {
            "reservoir": self.reservoir,
            "well_id": self.well_id,
            "volume": self.volume,
            "display_color": self.display_color,
            "stock_conc": self.stock_conc,
            "final_pure_conc": self.final_pure_conc, #TODO: remove, but check that no where else uses it
            "units": self.units,
            "liquid_type": self.liquid_type,
            "description": self.description,
            "artifact_num": self.artifact_num,
        }

    # --- Required methods for MutableMapping ---
    def __getitem__(self, key):
        return self._dict[key]

    def __setitem__(self, key, value):
        self._dict[key] = value

    def __delitem__(self, key):
        del self._dict[key]

    def __iter__(self):
        return iter(self._dict)

    def __len__(self):
        return len(self._dict)

# Metadata for pure

requirements = {"robotType": "Flex", "apiLevel": "2.24"}

PARAMETERS = [
    {
        "method": "add_float",
        "variable_name": "scalar_for_pipette_error",
        "display_name": "Scalar For Pipette Error",
        "description": "",
        "minimum": 1,
        "maximum": 2,
        "default": 1.2,
    },
]
# smix_final_volume = 200
reaction_volume = 10


# Helper file for loading labware, hardware, and liquids for OT
# Created By Sharon Newman

import math
import copy
import pandas as pd
from opentrons.protocol_api import SINGLE

DEFAULT_DEST_PLATE_SLOT_PRIORITY = [
    "D2", "B2", "A2", "A3", "C3"
]


def _replace_liquid_meniscus_reference(obj):
    if isinstance(obj, dict):
        updated = {}
        for key, value in obj.items():
            if key in {"position_reference", "positionReference"} and value == "liquid-meniscus":
                updated[key] = "well-bottom"
            else:
                updated[key] = _replace_liquid_meniscus_reference(value)
        return updated
    if isinstance(obj, list):
        return [_replace_liquid_meniscus_reference(item) for item in obj]
    return obj


def _replace_dispense_reference_with_top_offset(obj, z_offset=-3):
    if isinstance(obj, dict):
        updated = {}
        for key, value in obj.items():
            if key == "dispense_position" and isinstance(value, dict):
                cur_offset = value.get("offset", {})
                updated[key] = {
                    "offset": {
                        "x": cur_offset.get("x", 0),
                        "y": cur_offset.get("y", 0),
                        "z": z_offset,
                    },
                    "position_reference": "well-top",
                }
            elif key == "dispensePosition" and isinstance(value, dict):
                cur_offset = value.get("offset", {})
                updated[key] = {
                    "offset": {
                        "x": cur_offset.get("x", 0),
                        "y": cur_offset.get("y", 0),
                        "z": z_offset,
                    },
                    "positionReference": "well-top",
                }
            else:
                updated[key] = _replace_dispense_reference_with_top_offset(value, z_offset=z_offset)
        return updated
    if isinstance(obj, list):
        return [_replace_dispense_reference_with_top_offset(item, z_offset=z_offset) for item in obj]
    return obj


def _ensure_flex_8channel_1000_properties(props):
    updated = copy.deepcopy(props)
    if "flex_8channel_1000" not in updated and "flex_1channel_1000" in updated:
        updated["flex_8channel_1000"] = copy.deepcopy(updated["flex_1channel_1000"])
    return updated


def _resolve_dest_plate_slots(num_dest_plates, dest_plate_slots, blocked_slots, allow_partial=False):
    if num_dest_plates < 1:
        raise ValueError(f"num_dest_plates must be >= 1, got {num_dest_plates}")

    if dest_plate_slots is not None:
        if len(dest_plate_slots) < num_dest_plates and not allow_partial:
            raise ValueError(
                f"Not enough dest_plate_slots provided for num_dest_plates={num_dest_plates}. "
                f"Got {len(dest_plate_slots)} slots."
            )
        selected_slots = dest_plate_slots[:num_dest_plates] if len(dest_plate_slots) >= num_dest_plates else list(dest_plate_slots)
    else:
        selected_slots = []
        for slot in DEFAULT_DEST_PLATE_SLOT_PRIORITY:
            if slot in blocked_slots:
                continue
            selected_slots.append(slot)
            if len(selected_slots) == num_dest_plates:
                break
        if len(selected_slots) < num_dest_plates and not allow_partial:
            raise ValueError(
                f"Not enough free deck slots to place {num_dest_plates} destination plates."
            )

    if len(selected_slots) == 0:
        raise ValueError("No destination plate slots available to load.")

    duplicate_slots = {slot for slot in selected_slots if selected_slots.count(slot) > 1}
    if duplicate_slots:
        raise ValueError(f"Duplicate destination plate slots are not allowed: {sorted(duplicate_slots)}")
    overlaps = [slot for slot in selected_slots if slot in blocked_slots]
    if overlaps:
        raise ValueError(f"Destination plate slots conflict with occupied slots: {overlaps}")

    return selected_slots


def get_custom_pure_liquids(
    protocol, p50, p50_tips, reaction_volume, scalar=1.1, num_reps=3,
    use_well_bottom_reference=False, use_pcr_tube_top_offset=False
):
    custom = _ensure_flex_8channel_1000_properties(custom_water_no_mix_properties_v1)
    if use_pcr_tube_top_offset:
        custom = _replace_dispense_reference_with_top_offset(custom, z_offset=-3)
    target = custom['flex_1channel_50']["opentrons/opentrons_flex_96_filtertiprack_50ul/1"]
    water_liquid_no_mix = protocol.define_liquid_class(
        name="custom_water_push_no_mix",
        properties=custom,
        display_name="Custom water"
    )

    target['aspirate']['mix'] = {"enabled": True, "params": {"repetitions": 3, "volume": reaction_volume}}
    water_liquid_mix = protocol.define_liquid_class(
        name="custom_water_push_mix",
        properties=custom,
        display_name="Custom water with mixing before aspiration"
    )

    custom = _ensure_flex_8channel_1000_properties(custom_water_no_mix_properties_v1)
    if use_pcr_tube_top_offset:
        custom = _replace_dispense_reference_with_top_offset(custom, z_offset=-3)
    target = custom['flex_1channel_50']["opentrons/opentrons_flex_96_filtertiprack_50ul/1"]
    no_push_params = [(1.0, 0), (4.999, 0), (5.0, 0), (50.0, 0)]
    target['dispense']['push_out_by_volume'] = no_push_params
    target['aspirate']["delay"]["params"]["duration"] = 0.1
    target['dispense']["delay"]["params"]["duration"] = 0.1
    water_liquid_no_mix_no_push = protocol.define_liquid_class(
        name="custom_water_no_push_no_mix",
        properties=custom,
        display_name="Custom water with no mixing after dispensing"
    )

    target['dispense']['mix'] = {"enabled": True, "params": {"repetitions": 3, "volume": reaction_volume}}
    water_no_push_props = _ensure_flex_8channel_1000_properties(custom_water_no_mix_properties_v1)
    if use_pcr_tube_top_offset:
        water_no_push_props = _replace_dispense_reference_with_top_offset(
            water_no_push_props,
            z_offset=-3,
        )
    water_liquid_no_push = protocol.define_liquid_class(
        name="custom_water_no_push_w_mix",
        properties=water_no_push_props,
        display_name="Custom water with mixing after dispensing and no pushout"
    )

    final_liquid_nopush = protocol.define_liquid_class(
        name="custom_viscous_no_push_no_mix",
        properties=custom_viscous_no_mix_class_properties_v1,
        display_name="Custom Viscous with NO mixing after dispensing and no pushing"
    )

    cur_property = custom_final_dispense.copy()
    target = cur_property['flex_1channel_50']["opentrons/opentrons_flex_96_filtertiprack_50ul/1"]
    # target['aspirate']['pre_wet'] = False
    # target['aspirate']['mix'] = {"enabled": True, "params": {"repetitions": 3, "volume": reaction_volume * 0.8}}
    # target['aspirate']["delay"]["params"]["duration"] =  0.05
    # target['dispense']["delay"]["params"]["duration"] = 0.05
    # target['aspirate']['retract']['speed'] = 10
    # target['aspirate']['retract']['end_position']['position_reference'] = "liquid-meniscus"
    final_liquid_fast_props = _ensure_flex_8channel_1000_properties(custom_viscous_4C_aliquot)
    if use_well_bottom_reference:
        final_liquid_fast_props = _replace_liquid_meniscus_reference(
            final_liquid_fast_props
        )
    if use_pcr_tube_top_offset:
        final_liquid_fast_props = _replace_dispense_reference_with_top_offset(
            final_liquid_fast_props,
            z_offset=-3,
        )
    final_liquid_fast = protocol.define_liquid_class(
        name="final_liquid_fast",
        properties=final_liquid_fast_props,
        display_name="Custom Viscous with mixing before aspiration. No pushout"
    )

    cur_property = custom_final_dispense.copy()
    target = cur_property['flex_1channel_50']["opentrons/opentrons_flex_96_filtertiprack_50ul/1"]
    target['aspirate']['mix'] = {"enabled": True, "params": {"repetitions": 3, "volume": reaction_volume}}
    # target['dispense']['flow_rate_by_volume'] = [(1.0, 35.0), (10.0, 24.0), (50.0, 35.0)]
    # target['aspirate']["delay"]["params"]["duration"] =  0.25
    # target['dispense']["delay"]["params"]["duration"] = 0.25
    # target['dispense']['dispense_position']['offset'] = {"x": 0.5, "y": 0, "z": 2}
    # target['aspirate']['retract']['end_position']['position_reference'] = "well-top"
    final_liquid_asp_mix = protocol.define_liquid_class(
        name="custom_viscous_no_push_no_mix",
        properties=cur_property,
        display_name="Custom Viscous with mixing before aspiration. No pushout"
    )

    custom_properties = custom_viscous_no_mix_class_properties_v1.copy()
    target = custom_properties['flex_1channel_50']["opentrons/opentrons_flex_96_filtertiprack_50ul/1"]
    target['dispense']['mix'] = {"enabled": True, "params": {"repetitions": 3, "volume": reaction_volume}}
    viscous_liquid_nopush = protocol.define_liquid_class(
        name="custom_viscous_no_push_w_mix",
        properties=custom_properties,
        display_name="Custom Viscous WITH mixing after dispensing and no pushing"
    )

    target['aspirate']['mix'] = {"enabled": True, "params": {"repetitions": 3, "volume": reaction_volume*2}}
    viscous_liquid_asp_mix = protocol.define_liquid_class(
        name = "custom_viscous_no_push_aspirate_mix",
        properties = custom_properties,
        display_name = "Custom Viscous with mixing before aspiration"
    )
    fast_multidispense_props = _ensure_flex_8channel_1000_properties(
        fast_multidispense_liquid
    )
    if use_well_bottom_reference:
        fast_multidispense_props = _replace_liquid_meniscus_reference(
            fast_multidispense_props
        )
    if use_pcr_tube_top_offset:
        fast_multidispense_props = _replace_dispense_reference_with_top_offset(
            fast_multidispense_props,
            z_offset=-3,
        )

    fast_default_liquid = protocol.define_liquid_class(
        name = "fast_multidispense_liquid",
        properties = fast_multidispense_props,
        display_name = "Default viscous"
    )


    return  {"viscous": viscous_liquid_nopush, "water": water_liquid_no_mix,
             "water_mix":water_liquid_mix,
             "viscous_asp_mix": viscous_liquid_asp_mix,
             "final":final_liquid_nopush,
             "final_asp_mix":final_liquid_asp_mix,
             "final_liquid_fast":final_liquid_fast,
             "water_no_push":water_liquid_no_push,
             "water_no_push_no_mix": water_liquid_no_mix_no_push,
             "glycerol_50": fast_default_liquid}

#TODO: Deprecate this
def get_custom_pure_liquids_old(protocol, p50, p50_tips, reaction_volume):
    # water_RT_well = pcr_tubes.assign_well("water_RT", "H6")
    # select liquid class to use in your protocol
    # viscous_liquid = protocol.get_liquid_class(name="glycerol_50")
    # water_liquid = protocol.get_liquid_class(name="water")
    water_liquid_no_mix = make_custom_liquid(protocol, p50, p50_tips[0],
                                             custom_properties=custom_glycerol_class_properties_old,
                                             speed=20, asp_delay=0.5,
                                             aspirate_flow_rate=[(1.0, 35.0), (10.0, 24.0), (50.0, 35.0)],
                                             dispense_flow_rate=[(1.0, 3.5), (10.0, 5.0), (50.0, 50.0)],
                                             pre_wet=True,
                                             # correction_by_volume=[(0.0, 0.0), (1.0, -1.9), (3.0, -2.5), (5.0, -1.7),
                                             #                       (10.0, -3.0), (50.0, +2.5)]
                                             # push_out_by_volume=[[1.0, 7.0], [4.999, 7.0], [5.0, 2.0], [10.0, 2.0], [50.0, 2.0]],
                                             )
    water_liquid = make_custom_liquid(protocol, p50, p50_tips[0],
                                      custom_properties=custom_glycerol_class_properties_old,
                                      speed=20, asp_delay=0.5,
                                      aspirate_flow_rate=[(1.0, 35.0), (10.0, 24.0), (50.0, 35.0)],
                                      dispense_flow_rate=[(1.0, 3.5), (10.0, 5.0), (50.0, 50.0)],
                                      pre_wet=True,
                                      # correction_by_volume=[(0.0, 0.0), (1.0, -1.9), (3.0, -2.5), (5.0, -1.7),
                                      #                       (10.0, -3.0), (50.0, +2.5)],
                                      mix={"enabled": True, "params": {"repetitions": 1, "volume": 10}},
                                      push_out_by_volume=[(1.0, 5), (4.999, 5), (5.0, 3.9), (50.0, 3.9)]
                                      )

    viscous_liquid_no_mix = make_custom_liquid(protocol, p50, p50_tips[0],
                                               custom_properties=custom_glycerol_class_properties,
                                               speed=4, asp_delay=1,
                                               aspirate_flow_rate=[(1.0, 35.0), (10.0, 24.0), (50.0, 35.0)],
                                               dispense_flow_rate=[(1.0, 3.5), (10.0, 5.0), (50.0, 50.0)],
                                               pre_wet=True,
                                               # push_out_by_volume=[[1.0, 7.0], [4.999, 7.0], [5.0, 2.0], [10.0, 2.0], [50.0, 2.0]],
                                               # mix={"enabled": True, "params": {"repetitions": 1, "volume": 3}}
                                               # correction_by_volume = [(0.0, 0.0), (1.0, -.41), (3.0, -0.6), (5.0, -0.5), (10.0, -1.2), (50.0, +2.5)]
                                               )

    viscous_liquid = make_custom_liquid(protocol, p50, p50_tips[0],
                                        custom_properties=custom_glycerol_class_properties,
                                        speed=4, asp_delay=1,
                                        aspirate_flow_rate=[(1.0, 35.0), (10.0, 24.0), (50.0, 35.0)],
                                        dispense_flow_rate=[(1.0, 3.5), (10.0, 5.0), (50.0, 50.0)],
                                        pre_wet=True,
                                        mix={"enabled": True, "params": {"repetitions": 1, "volume": 10}},
                                        # correction_by_volume = [(0.0, 0.0), (1.0, -.41), (3.0, -0.6), (5.0, -0.5), (10.0, -1.2), (50.0, +2.5)]
                                        push_out_by_volume=[(1.0, 5), (4.999, 5), (5.0, 3.9), (50.0, 3.9)]
                                        # [[1.0, 7.0], [4.999, 7.0], [5.0, 2.0], [10.0, 2.0], [50.0, 2.0]],
                                        )

    final_liquid_nopush = make_custom_liquid(protocol, p50, p50_tips[0],
                                             custom_properties=custom_glycerol_class_properties,
                                             speed=4, asp_delay=1,
                                             aspirate_flow_rate=[(1.0, 35.0), (10.0, 24.0), (50.0, 35.0)],
                                             dispense_flow_rate=[(1.0, 3.5), (10.0, 5.0), (50.0, 50.0)],
                                             pre_wet=True,
                                             # mix={"enabled": True, "params": {"repetitions": 3, "volume": reaction_volume}},
                                             push_out_by_volume=[(1.0, 0), (4.999, 0), (5.0, 0), (50.0, 0)]
                                             # [[1.0, 7.0], [4.999, 7.0], [5.0, 2.0], [10.0, 2.0], [50.0, 2.0]],
                                             )
    viscous_liquid_nopush = make_custom_liquid(protocol, p50, p50_tips[0],
                                               custom_properties=custom_glycerol_class_properties,
                                               speed=4, asp_delay=1,
                                               aspirate_flow_rate=[(1.0, 35.0), (10.0, 24.0), (50.0, 35.0)],
                                               dispense_flow_rate=[(1.0, 3.5), (10.0, 5.0), (50.0, 50.0)],
                                               pre_wet=True,
                                               mix={"enabled": True,
                                                    "params": {"repetitions": 3, "volume": reaction_volume}},
                                               push_out_by_volume=[(1.0, 0), (4.999, 0), (5.0, 0), (50.0, 0)]
                                               # [[1.0, 7.0], [4.999, 7.0], [5.0, 2.0], [10.0, 2.0], [50.0, 2.0]],
                                               )

    water_liquid_nopush = make_custom_liquid(protocol, p50, p50_tips[0],
                                             custom_properties=custom_glycerol_class_properties_old,
                                             speed=20, asp_delay=0.5,
                                             aspirate_flow_rate=[(1.0, 35.0), (10.0, 24.0), (50.0, 35.0)],
                                             dispense_flow_rate=[(1.0, 3.5), (10.0, 5.0), (50.0, 50.0)],
                                             pre_wet=True,
                                             # correction_by_volume=[(0.0, 0.0), (1.0, -1.9), (3.0, -2.5), (5.0, -1.7),
                                             #                       (10.0, -3.0), (50.0, +2.5)],
                                             mix={"enabled": True, "params": {"repetitions": 3, "volume": 5}},
                                             push_out_by_volume=[(1.0, 0), (4.999, 0), (5.0, 0), (50.0, 0)]
                                             )
    return {"viscous": viscous_liquid_nopush, "water": water_liquid_no_mix, "final":final_liquid_nopush}
    # return water_liquid_no_mix, viscous_liquid_nopush, final_liquid_nopush

def setup_labware(protocol, pipette_name = "flex_1channel_50", side="right",
                  reagent_plate_name="generic_96_aluminumblock_200ul", #"opentrons_96_aluminumblock_generic_pcr_strip_200ul",
                  dest_plate="greiner_384_sv_hibase", num_dest_plates=1, dest_plate_slots=None,
                  allow_partial_dest_plates=False):
    """
    Load all labware and modules
    """
    # Set up deck
    chute = protocol.load_waste_chute()  # Looks like not used, but is! and also will throw generic error if removed
    tip_type = "opentrons_flex_96_filtertiprack_50ul"
    if pipette_name in {'flex_1channel_1000', 'flex_8channel_1000'}:
        tip_type = "opentrons_flex_96_filtertiprack_1000ul"

    pipette_tips = [protocol.load_labware(tip_type, "B3")]
    # p50 = protocol.load_instrument("flex_1channel_50", "left", tip_racks=p50_tips)
    # p50.configure_nozzle_layout(style=SINGLE, start="H1", tip_racks=p50_tips)

    pipette = protocol.load_instrument(pipette_name, side, tip_racks=pipette_tips)
    pipette._nominal_max_volume = pipette.max_volume
    pipette._nominal_min_volume = pipette.min_volume

    temp_module = protocol.load_module(
        module_name="temperature module gen2", location="D1"
    )

    if reagent_plate_name in {"opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical", "bnext_10ml_trough_holder"}:
        reagent_plate = PlateTracker(protocol, reagent_plate_name, "C2", label="reagent_plate")
    else:
        reagent_plate = PlateTracker(temp_module, reagent_plate_name, label="reagent_plate")

    # reagent_plate = PlateTracker(temp_module, "opentrons_24_aluminumblock_nest_1.5ml_snapcap",
    #                              label="reagent_plate")
    # pcr_tubes = PlateTracker(protocol, "bnext_pcr_6_strip_rack", "B2",
    #                          label="pcr_tubes")

    blocked_slots = {"B3", "D1", "C2"}
    dest_slots = _resolve_dest_plate_slots(
        num_dest_plates=num_dest_plates,
        dest_plate_slots=dest_plate_slots,
        blocked_slots=blocked_slots,
        allow_partial=allow_partial_dest_plates,
    )

    dest_plate_trackers = []
    for i, slot in enumerate(dest_slots):
        label = "dest_plate" if i == 0 else f"dest_plate_{i+1}"
        tracker = PlateTracker(
            protocol, dest_plate, slot, label=label,
            is_checkerboard=False, randomize_wells=False
        )
        dest_plate_trackers.append(tracker)

    plates = {
        "reagent_plate": reagent_plate,
        # "pcr_tubes": pcr_tubes,
        "dest_plate": dest_plate_trackers[0],
        "dest_plates": dest_plate_trackers,
        "dest_plate_slots": dest_slots,
    }

    for i, tracker in enumerate(dest_plate_trackers[1:], start=2):
        plates[f"dest_plate_{i}"] = tracker

    return chute, pipette, pipette_tips, temp_module, plates

def load_liquids(reagent_info, plates, protocol):
    """
    Load reagents into labware wells and return a dictionary of LiquidTracker objects.

    This function assigns wells to reagents according to the provided `reagent_info`.
    Each reagent is loaded into the corresponding labware (`PlateTracker`) and a
    LiquidTracker object is returned that tracks the well and metadata such as
    stock concentration, units, liquid type, etc.

    Args:
        reagent_info (dict): Dictionary of reagent definitions, typically using Reagent objects.
        plates (dict): Dictionary mapping plate names to PlateTracker objects.
        protocol (ProtocolContext): Opentrons protocol context, required for defining liquids.

    Returns:
        dict: Dictionary mapping reagent names to LiquidTracker objects.
              Each LiquidTracker contains metadata from the original Reagent object.

    Raises:
        ValueError: If a plate specified in `reagent_info` is not found in `plates`.
    """
    # Load assigned wells to reagents
    reagents = {}
    for reagent_name, params in reagent_info.items():
        plate_name = params["reservoir"]
        plate_obj = plates.get(plate_name)

        if plate_obj is None:
            raise ValueError(f"Plate '{plate_name}' not found for reagent '{reagent_name}'")

        reagents[reagent_name] = plate_obj.assign_well(
            reagent_name,
            liquid_params=params,
            protocol=protocol
        )
    return reagents


def reagents_from_df(REAGENTS):
    reagents: dict[str, Reagent] = {}

    for row in REAGENTS:
        name = row["reagent"]

        r = Reagent(
            reservoir=row["reservoir"],
            well_id=row["well"],
            volume=row.get("volume") or 100,  # default if None
            display_color=None,               # let __post_init__ assign
            stock_conc=row.get("stock_conc"),
            final_pure_conc=None,             # not in CSV; keep default
            units=row.get("units"),
            liquid_type=row.get("liquid_type") or "water_mix",
            description=row.get("description") or "",
            artifact_num=row.get("artifact_num"),
        )

        reagents[name] = r

    return reagents

# Helper files for common protocol movements
# Created By Sharon Newman

from opentrons import protocol_api
import time
import numpy as np
import math

import logging

log = logging.getLogger(__name__)
MIN_PIPETTE_VOl = 2.0 #ul

def add_parameters(parameters: protocol_api.ParameterContext):
    for param in PARAMETERS:
        add_fn = getattr(parameters, param["method"])
        if param["method"] in ["add_int", "add_float"]:
            add_fn(
                variable_name=param["variable_name"],
                display_name=param["display_name"],
                description=param["description"],
                minimum=param["minimum"],
                maximum=param["maximum"],
                default=param["default"],
            )
        elif param["method"] == "add_bool":
            add_fn(
                variable_name=param["variable_name"],
                display_name=param["display_name"],
                description=param["description"],
                default=param["default"],
            )
        else:
            add_fn(
                variable_name=param["variable_name"],
                display_name=param["display_name"],
                description=param["description"],
                choices=param["choices"],
                default=param["default"],
            )
#
def get_logger(protocol: protocol_api.ProtocolContext):
    def log_comment(msg, **kwargs):
        structured_log = " ".join([f"{k}={v}" for k, v in kwargs.items()])

        log.info(f"msg={msg} {structured_log}")
        protocol.comment(
            f"> {msg} {f'({structured_log})' if structured_log != '' else ''}"
        )

    return log_comment

def dilute_reagents(protocol, pipette, child, parent, reagents, log):
    diluent = reagents['water']
    min_total_volume = 12  # make sure we're not making ridiculously small volumes
    volume_parent = child.stock_conc * min_total_volume / parent.stock_conc

    # make sure we're not making ridiculously small volumes
    if volume_parent < MIN_PIPETTE_VOl*2:
        volume_parent = MIN_PIPETTE_VOl*2
        min_total_volume = volume_parent*parent.stock_conc / child.stock_conc

    log(min_total_volume)
    # assert np.all(min_total_volume < volume_parent), f"Impossible mixture for concs {child.stock_conc}"
    pipette.configure_for_volume(min_total_volume-volume_parent)

    # TODO: update this do take the parent.liquid type, but ensure no push so no air gaps are formed
    pipette.distribute_with_liquid_class(CUSTOM_PURE_LIQUIDS['water_no_push_no_mix'], min_total_volume-volume_parent,
                                         diluent, child, new_tip="always")
    pipette.configure_for_volume(volume_parent)

    pipette.pick_up_tip()
    pipette.distribute_with_liquid_class(CUSTOM_PURE_LIQUIDS["water_no_push"], volume_parent, parent, child, new_tip="never")
    vol_to_mix = min(min_total_volume / 3, pipette.max_volume)
    pipette.configure_for_volume(min_total_volume/3)
    pipette.mix(repetitions=20, volume=vol_to_mix,
            location=child, aspirate_flow_rate=10, dispense_flow_rate=10)
    pipette.drop_tip()

def create_and_register_diluted_reagent(reagents, parent_name, dilution_factor, protocol, log, pipette):
    """Register a new diluted reagent aliquot in reagents dict."""

    parent_reagent = reagents[parent_name]
    assert dilution_factor>1, f"No concentrated stock available for dilution factor of {dilution_factor} from {parent_reagent.stock_conc}"

    child_name = f"{parent_name}_aliquot_{int(dilution_factor)}x"
    child_params = parent_reagent.params
    child_params['description'] = f"Child of {parent_name}:  {child_params['description']} w/ dilution of {int(dilution_factor)}x"
    child_params['stock_conc'] = parent_reagent.stock_conc / dilution_factor
    child_params['volume'] = 0
    # update stock vol
    if child_name not in reagents:
        reagents[child_name] = parent_reagent.parent.assign_well(
            child_name,
            liquid_params = child_params,
            protocol = protocol
        )

    dilute_reagents(protocol,pipette, reagents[child_name], parent_reagent, reagents, log)
    log(f"Created new reagent: {child_name} of {reagents[child_name].stock_conc} {reagents[child_name].units}  from parent stock at location {reagents[child_name]}")

    return reagents[child_name]

def find_suitable_reagent(base_name, reagents, target_conc, reaction_volume, min_vol,
                          used_volume, protocol, log, pipette):
    """
    Given a sweep reagent, find the best stock (original or diluted)
    that gives >= min_vol. Creates a new aliquot if none exist.
    """
    # if sweep_reagent is not None:
    #     base_name = sweep_reagent["name"]

    # Gather all available versions of this reagent (base + aliquots)
    candidate_names = [r for r in reagents if r.startswith(base_name)]
    candidates = [(name, reagents[name]) for name in candidate_names]
    # log(f"{base_name} has {candidates} candidates")
    # Try each candidate stock concentration
    for name, reagent in sorted(candidates, key=lambda x: -x[1].stock_conc):
        vol = (reaction_volume * target_conc) / reagent.stock_conc
        water_to_add = reaction_volume - used_volume - vol
        log(f'If using stock name {name}: vol {vol} water {water_to_add}')
        if (vol >= min_vol) and (water_to_add >= 0):
            return reagent, vol  # found a usable stock

    # If none suitable, determine and create a new suitable diluted stock
    parent = reagents[base_name] #TODO: choose most appropriate concentration dont just take base
    # Dilute just enough so the required volume is >= min_vol
    child_conc = np.ceil(reaction_volume * target_conc) / min_vol
    dilution_factor = parent.stock_conc / child_conc
    assert dilution_factor > 1, f"No available stock to be made from {parent.stock_conc} {parent.units} for {target_conc} {parent.units}"

    log(f'Making a diluted stock of {child_conc} {parent.units} with dilution_factor: {dilution_factor} for {target_conc} {parent.units}')

    new_reagent = create_and_register_diluted_reagent(reagents, base_name, dilution_factor, protocol, log, pipette)
    vol = (reaction_volume * target_conc) / new_reagent.stock_conc
    assert np.all(vol > 0), f"Impossible mixture for concs {target_conc} vol is {vol}"

    return new_reagent, vol

def calculate_sweep_volumes(sweep, reaction_volume, fixed_volumes, reagents,
                            protocol, log, pipette, min_vol = MIN_PIPETTE_VOl):
    """Calculate sweep volumes w/ aliquot reuse"""
    sweep_steps = {}

    used_volume = sum(fixed_volumes.values())
    sweep_vol = (sweep['target_concs'] * reaction_volume) / reagents[sweep['name']].stock_conc
    log(f"Default sweep volume: {sweep_vol}, water_vol: {reaction_volume - sweep_vol - used_volume}")
    final_reagents = []

    # create two lists of volumes that correspond to the final reagents to be using
    for i, target_conc, v in zip( range(len(sweep_vol)), sweep['target_concs'], sweep_vol):
        cur_reagent, v = find_suitable_reagent(sweep['name'], reagents, target_conc, reaction_volume,
                                               min_vol, used_volume, protocol, log, pipette)
        sweep_vol[i] = v
        final_reagents.append(cur_reagent)

    sweep_steps[sweep['name']] = {
        "volume": sweep_vol,
        "reagent": final_reagents,
    }

    # Compute water filler
    water_vol = reaction_volume - used_volume - sweep_vol

    assert np.all(water_vol >= 0), f"Impossible mixture for concs {sweep['target_concs'][water_vol < 0]}, "
    sweep_steps["water"] = {"volume": water_vol, "reagent": reagents["water"]}

    return sweep_steps


def configure_then_transfer_to_well(vol, name, well, mm, p50, log, num_replicates=1, volume_scalar=1, new_tip = "always"):
    vol_to_transfer = vol * num_replicates * volume_scalar
    log(f'Transferring {vol_to_transfer} ul of {name}')
    p50.configure_for_volume(vol_to_transfer)
    p50.distribute_with_liquid_class(well.liquid_type, vol_to_transfer, well, mm, new_tip=new_tip)


def mix_wells(wells, p50, reaction_volume, num_replicates=1, volume_scalar=1, mix_reps = 10,
        flow_rate=50):

    # TODO: make this faster for emix (replace w/ configure_then_transfer?)
    if mix_reps:
        nominal_max_volume = getattr(p50, "_nominal_max_volume", p50.max_volume)
        p50.pick_up_tip()
        vol_to_mix = min((reaction_volume * num_replicates * volume_scalar) * 0.8, nominal_max_volume)
        p50.configure_for_volume(vol_to_mix)
        p50.mix(repetitions=mix_reps, volume=vol_to_mix,
                location=wells, aspirate_flow_rate=flow_rate, dispense_flow_rate=flow_rate)
        p50.drop_tip()

## Generically follow steps to add to a master mix
def make_master_mixes_old(steps, reagents, volumes_to_add, num_replicates, reaction_volume,
            volume_scalar, mm_plate, p50, log, num_mms=1, mix_reps = 15, mm_label = "master_mixes",
                      flow_rate=35):
    master_mixes = mm_plate.initiate_next_wells(num_mms, mm_label, from_bottom_right=True)
    for i, mm in enumerate(master_mixes):
        log(f"********master mixes {mm}")
        for name in steps:
            vol = volumes_to_add[name]
            well = reagents[name]
            configure_then_transfer_to_well(vol, name, well, mm, p50, log, num_replicates, volume_scalar)

        mix_wells(mm, p50, reaction_volume, num_replicates=num_replicates, volume_scalar=volume_scalar,
            mix_reps = mix_reps, flow_rate=flow_rate)

    return master_mixes


def make_master_mixes(steps, reagents, mm_plate, p50, log, well_volume=None, num_mms=1, mix_reps=20,
                      mm_label="master_mixes", flow_rate=35, num_replicates=1, volume_scalar=1):
    """
    Makes OT follow the steps in order given to make a master mix
    :param steps: a pd.df with column of vol_to_pipette, reagent
    :param reagents: Reagents class matching "reagent" names in steps
    :param mm_plate:
    :param p50:
    :param log:
    :param well_volume: Volume expected in total well TODO: rename to reaction_volume?
    :param num_mms:
    :param mix_reps:
    :param mm_label:
    :param flow_rate:
    :param num_replicates:
    :param volume_scalar:
    :return:
    """
    try:
        master_mixes = mm_plate.get_sample_wells(mm_label)
        log(f"Using existing master mix wells: {mm_label}")
    except AssertionError:
        master_mixes = mm_plate.initiate_next_wells(num_mms, mm_label, from_bottom_right=True)
        log(f"Created new master mix wells: {mm_label}")

    for i, mm in enumerate(master_mixes):
        log(f"********master mixes {mm}")
        for i, row in steps.iterrows():
            vol = row['vol_to_pipette_ul']
            name = row['reagent']
            well = reagents[name]
            configure_then_transfer_to_well(vol, name, well, mm, p50, log, num_replicates, volume_scalar)

        mix_wells(mm, p50, well_volume, num_replicates, volume_scalar,
                  mix_reps=mix_reps, flow_rate=flow_rate)
    return master_mixes


def distribute_mms(master_mixes, distribution_liquid_type,
                   p50, plates, reaction_volume,
                   log,num_replicates=1, dest_wells=None, dest_label="dest_wells"):
    # distribution_liquid_type= CUSTOM_PURE_LIQUIDS["final"]
    if dest_wells is None:
        dest_wells = plates['dest_plate'].initiate_next_wells(num_replicates, dest_label)
    log(f'destination wells: {dest_wells}')
    p50.distribute_with_liquid_class(distribution_liquid_type, reaction_volume, master_mixes, dest_wells)
    return dest_wells

custom_viscous_no_mix_class_properties_v1 = {
    "flex_1channel_50": {
        "opentrons/opentrons_flex_96_filtertiprack_50ul/1": {
            "aspirate": {
                "aspirate_position": {
                    "offset": {"x": 0, "y": 0, "z": 2},
                    "position_reference": "well-bottom",
                },
                # "correction_by_volume":  [(0.0, 0.0), (1.0, -0.2), (10.0,1), (50.0, -0.2)],
                "correction_by_volume":  [(0.0, 0.0), (1.0, -0.2), (10.0,1), (50.0, -0.2)],
                "delay": {"enabled": True, "params": {"duration": 1}},
                "flow_rate_by_volume":[(1.0, 35.0), (10.0, 24.0), (50.0, 35.0)],
                "mix": {"enabled": False},
                "pre_wet": True,
                "retract": {
                    "air_gap_by_volume": [[0.0, 0.0]],
                    "delay": {"enabled": False},
                    "end_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-top",
                    },
                    "speed": 4,
                    "touch_tip": {
                        "enabled": False,
                        "params":{"zOffset": -1, "mmFromEdge": 0.5, "speed": 30}
                    },
                },
                "submerge": {
                    "delay": {"enabled": False},
                    "speed": 50,
                    "start_position": {
                       "offset": {"x": 0, "y": 0, "z": 2},
                       "position_reference": "well-top",
                    },
                },
            },
            "dispense": {
                "correction_by_volume": [(0.0, 0.0), (1.0, -0.2), (10.0,1), (50.0, -0.2)],
                "delay": {"enabled": True, "params": {"duration": 0.5}},
                "dispense_position": {
                    "offset": {"x": 0, "y": 0, "z": 2},
                    "position_reference": "well-bottom",
                },
                "flow_rate_by_volume": [(1.0, 3.5), (10.0, 5.0), (50.0, 50.0)],
                "mix": {"enabled": False}, #{"enabled": True, "params": {"repetitions": 1, "volume": 10}},
                "push_out_by_volume": [(1.0, 0), (4.999, 0), (5.0, 0), (50.0, 0)],
                "retract": {
                    "air_gap_by_volume": [[0.0, 0.0]],
                    "blowout": {"enabled": False},
                    "delay": {"enabled": False},
                    "end_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-top",
                    },
                    "speed": 50,
                    "touch_tip": {
                        "enabled": False,
                        "params":{"zOffset": -1, "mmFromEdge": 0.5, "speed": 30}
                    },
                },
                "submerge": {
                    "delay": {"enabled": False},
                    "speed": 50,
                    "start_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-top",
                    },
                },
            },
        }
    }
}

custom_final_dispense = {
    "flex_1channel_50": {
        "opentrons/opentrons_flex_96_filtertiprack_50ul/1": {
            "aspirate": {
                "aspirate_position": {
                    "offset": {"x": 0, "y": 0, "z": 2},
                    "position_reference": "well-bottom",
                },
                "correction_by_volume":  [(0.0, 0.0), (1.0, -0.2), (10.0,1), (50.0, -0.2)],
                "delay": {"enabled": True, "params": {"duration": 1}},
                "flow_rate_by_volume":[(1.0, 35.0), (10.0, 24.0), (50.0, 35.0)],
                "mix": {"enabled": False},
                "pre_wet": True,
                "retract": {
                    "air_gap_by_volume": [[0.0, 0.0]],
                    "delay": {"enabled": False},
                    "end_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-top", #"liquid-meniscus",
                    },
                    "speed": 4,
                    "touch_tip": {
                        "enabled": False,
                        "params":{"zOffset": -1, "mmFromEdge": 0.5, "speed": 30}
                    },
                },
                "submerge": {
                    "delay": {"enabled": False},
                    "speed": 50,
                    "start_position": {
                       "offset": {"x": 0, "y": 0, "z": 2},
                       "position_reference": "well-top", #"liquid-meniscus",
                    },
                },
            },
            "dispense": {
                "correction_by_volume": [(0.0, 0.0), (1.0, -0.2), (10.0,1), (50.0, -0.2)],
                "delay": {"enabled": True, "params": {"duration": 0.5}},
                "dispense_position": {
                    "offset": {"x": 0, "y": 0, "z": 2},
                    "position_reference": "well-bottom",
                },
                "flow_rate_by_volume": [(1.0, 3.5), (10.0, 5.0), (50.0, 50.0)],
                "mix": {"enabled": False}, #{"enabled": True, "params": {"repetitions": 1, "volume": 10}},
                "push_out_by_volume": [(1.0, 0), (4.999, 0), (5.0, 0), (50.0, 0)],
                "retract": {
                    "air_gap_by_volume": [[0.0, 0.0]],
                    "blowout": {"enabled": False},
                    "delay": {"enabled": False},
                    "end_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-top",
                    },
                    "speed": 50,
                    "touch_tip": {
                        "enabled": False,
                        "params":{"zOffset": -1, "mmFromEdge": 0.5, "speed": 30}
                    },
                },
                "submerge": {
                    "delay": {"enabled": False},
                    "speed": 50,
                    "start_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-top",
                    },
                },
            },
        }
    },
    "flex_1channel_1000": {
        "opentrons/opentrons_flex_96_filtertiprack_1000ul/1": {
            "aspirate": {
                "aspirate_position": {
                    "offset": {"x": 0, "y": 0, "z": -10},
                    "position_reference": "liquid-meniscus",
                },
                "correction_by_volume":  [(0.0, 0.0), (10.0, -0.2), (100.0,-0.1), (1000.0, 12)],
                "delay": {"enabled": True, "params": {"duration": 0.05}},
                "flow_rate_by_volume":[(10.0, 10.0),(100.0, 100.0),(1000.0, 800.0)],
                "mix": {"enabled": False},
                "pre_wet": True,
                "retract": {
                    "air_gap_by_volume": [[0.0, 0.0]],
                    "delay": {"enabled": False},
                    "end_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "liquid-meniscus",
                    },
                    "speed": 20,
                    "touch_tip": {
                        "enabled": False,
                        "params":{"zOffset": -1, "mmFromEdge": 0.5, "speed": 30}
                    },
                },
                "submerge": {
                    "delay": {"enabled": False},
                    "speed": 100,
                    "start_position": {
                       "offset": {"x": 0, "y": 0, "z": 2},
                       "position_reference": "liquid-meniscus",
                    },
                },
            },
            "dispense": {
                "correction_by_volume": [(0.0, 0.0), (10.0, -0.2), (100.0,-.1), (1000.0, 12)],
                "delay": {"enabled": True, "params": {"duration": 0.05}},
                "dispense_position": {
                    "offset": {"x": 0, "y": 0, "z": 4},
                    "position_reference": "well-bottom",
                },
                "flow_rate_by_volume": [(1.0, 3.5), (10.0, 5.0), (50.0, 50.0)],
                "mix": {"enabled": False}, #{"enabled": True, "params": {"repetitions": 1, "volume": 10}},
                "push_out_by_volume": [[0,35.0]],
                "retract": {
                    "air_gap_by_volume": [[0.0, 0.0]],
                    "blowout": {"enabled": False},
                    "delay": {"enabled": False},
                    "end_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "speed": 20,
                    "touch_tip": {
                        "enabled": False,
                        "params":{"zOffset": -1, "mmFromEdge": 0.5, "speed": 30}
                    },
                },
                "submerge": {
                    "delay": {"enabled": False},
                    "speed": 50,
                    "start_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-top",
                    },
                },
            },
        }
    }
}

custom_water_no_mix_properties_v1= {
    "flex_1channel_50": {
        "opentrons/opentrons_flex_96_filtertiprack_50ul/1": {
            "aspirate": {
                "aspirate_position": {
                    "offset": {"x": 0, "y": 0, "z": 2},
                    "position_reference": "well-bottom",
                },
                "correction_by_volume": [(0.0, 0.0), (1.0, -0.2), (10.0,1), (50.0, -0.2)],
                "delay": {"enabled": True, "params": {"duration": 0.5}},
                "flow_rate_by_volume": [(1.0, 35.0), (10.0, 24.0), (50.0, 35.0)], #weird that flow rate is so fast for 1ul
                "mix": {"enabled": False},
                "pre_wet": True,
                "retract": {
                    "air_gap_by_volume": [[0.0, 0.0]],
                    "delay": {"enabled": False},
                    "end_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-top", #"liquid-meniscus",
                    },
                    "speed": 20,
                    "touch_tip": {
                        "enabled": False,
                        "params":{"zOffset": -1, "mmFromEdge": 0.5, "speed": 30}
                    },
                },
                "submerge": {
                    "delay": {"enabled": False},
                    "speed": 50,
                    "start_position": {
                       "offset": {"x": 0, "y": 0, "z": 2},
                       "position_reference":"well-top", # "liquid-meniscus",
                    },
                },
            },
            "dispense": {
                # "correction_by_volume":  [(0.0, 0.0), (1.0, -0.2), (10.0,1), (50.0, -0.2)],
                "correction_by_volume":  [(0.0, 0.0), (1.0, -0.2), (10.0,1), (50.0, -0.2)],
                "delay": {"enabled": True, "params": {"duration": 0.5}},
                "dispense_position": {
                    "offset": {"x": 0, "y": 0, "z": 2},
                    "position_reference": "well-bottom",
                },
                "flow_rate_by_volume": [(1.0, 3.5), (10.0, 5.0), (50.0, 50.0)],
                "mix":{"enabled": False},
                "push_out_by_volume": [(1.0, 5), (4.999, 5), (5.0, 3.9), (50.0, 3.9)],
                "retract": {
                    "air_gap_by_volume": [[0.0, 0.0]],
                    "blowout": {"enabled": False},
                    "delay": {"enabled": False},
                    "end_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-top",
                    },
                    "speed": 50,
                    "touch_tip": {
                        "enabled": False,
                        "params":{"zOffset": -1, "mmFromEdge": 0.5, "speed": 30}
                    },
                },
                "submerge": {
                    "delay": {"enabled": False},
                    "speed": 50,
                    "start_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-top",
                    },
                },
            },
        }
    }
}
custom_viscous_4C_aliquot = {
    "flex_1channel_50": {
        "opentrons/opentrons_flex_96_filtertiprack_50ul/1": {
            "aspirate": {
                "aspirate_position": {
                    "offset": {"x": 0, "y": 0, "z": 2},
                    "position_reference": "well-bottom",
                },
                "correction_by_volume":  [(0.0, 0.0), (1.0, -0.2), (10.0,1), (50.0, -0.2)],
                "delay": {"enabled": True, "params": {"duration": 0.05}},
                "flow_rate_by_volume":[(1.0, 35.0), (10.0, 24.0), (50.0, 35.0)],
                "mix": {"enabled": False},
                "pre_wet": True,
                "retract": {
                    "air_gap_by_volume": [[0.0, 0.0]],
                    "delay": {"enabled": False},
                    "end_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "liquid-meniscus",
                    },
                    "speed": 10,
                    "touch_tip": {
                        "enabled": False,
                        "params":{"zOffset": -1, "mmFromEdge": 0.5, "speed": 30}
                    },
                },
                "submerge": {
                    "delay": {"enabled": False},
                    "speed": 50,
                    "start_position": {
                       "offset": {"x": 0, "y": 0, "z": 2},
                       "position_reference": "liquid-meniscus",
                    },
                },
            },
            "dispense": {
                "correction_by_volume": [(0.0, 0.0), (1.0, -0.2), (10.0,1), (50.0, -0.2)],
                "delay": {"enabled": True, "params": {"duration": 0.05}},
                "dispense_position": {
                    "offset": {"x": 0, "y": 0, "z": 2},
                    "position_reference": "well-bottom",
                },
                "flow_rate_by_volume": [(1.0, 3.5), (10.0, 5.0), (50.0, 50.0)],
                "mix": {"enabled": False}, #{"enabled": True, "params": {"repetitions": 1, "volume": 10}},
                "push_out_by_volume": [(1.0, 0), (4.999, 0), (5.0, 0), (50.0, 0)],
                "retract": {
                    "air_gap_by_volume": [[0.0, 0.0]],
                    "blowout": {"enabled": False},
                    "delay": {"enabled": False},
                    "end_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-top",
                    },
                    "speed": 50,
                    "touch_tip": {
                        "enabled": False,
                        "params":{"zOffset": -1, "mmFromEdge": 0.5, "speed": 30}
                    },
                },
                "submerge": {
                    "delay": {"enabled": False},
                    "speed": 50,
                    "start_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-top",
                    },
                },
            },
        }
    },
    "flex_1channel_1000": {
        "opentrons/opentrons_flex_96_filtertiprack_1000ul/1": {
            "aspirate": {
                "aspirate_position": {
                    "offset": {"x": 0, "y": 0, "z": -10},
                    "position_reference": "liquid-meniscus",
                },
                "correction_by_volume":  [(0.0, 0.0), (10.0, -0.2), (100.0,-0.1), (1000.0, 12)],
                "delay": {"enabled": True, "params": {"duration": 0.05}},
                "flow_rate_by_volume":[(10.0, 10.0),(100.0, 100.0),(1000.0, 800.0)],
                "mix": {"enabled": False},
                "pre_wet": True,
                "retract": {
                    "air_gap_by_volume": [[0.0, 0.0]],
                    "delay": {"enabled": False},
                    "end_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "liquid-meniscus",
                    },
                    "speed": 20,
                    "touch_tip": {
                        "enabled": False,
                        "params":{"zOffset": -1, "mmFromEdge": 0.5, "speed": 30}
                    },
                },
                "submerge": {
                    "delay": {"enabled": False},
                    "speed": 100,
                    "start_position": {
                       "offset": {"x": 0, "y": 0, "z": 2},
                       "position_reference": "liquid-meniscus",
                    },
                },
            },
            "dispense": {
                "correction_by_volume": [(0.0, 0.0), (10.0, -0.2), (100.0,-.1), (1000.0, 12)],
                "delay": {"enabled": True, "params": {"duration": 0.05}},
                "dispense_position": {
                    "offset": {"x": 0, "y": 0, "z": 4},
                    "position_reference": "well-bottom",
                },
                "flow_rate_by_volume": [(1.0, 3.5), (10.0, 5.0), (50.0, 50.0)],
                "mix": {"enabled": False}, #{"enabled": True, "params": {"repetitions": 1, "volume": 10}},
                "push_out_by_volume": [[0,35.0]],
                "retract": {
                    "air_gap_by_volume": [[0.0, 0.0]],
                    "blowout": {"enabled": False},
                    "delay": {"enabled": False},
                    "end_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-bottom",
                    },
                    "speed": 20,
                    "touch_tip": {
                        "enabled": False,
                        "params":{"zOffset": -1, "mmFromEdge": 0.5, "speed": 30}
                    },
                },
                "submerge": {
                    "delay": {"enabled": False},
                    "speed": 50,
                    "start_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-top",
                    },
                },
            },
        }
    }
}

fast_multidispense_liquid = {
    "flex_1channel_50": {
        "opentrons/opentrons_flex_96_filtertiprack_50ul/1": {
            "aspirate": {
                "aspirate_position": {
                    "offset": {"x": 0, "y": 0, "z": 2},
                    "position_reference": "well-bottom",
                },
                "correction_by_volume":  [(0.0, 0.0), (1.0, -0.2), (10.0,1), (50.0, -0.2)],
                "delay": {"enabled": True, "params": {"duration": 0.05}},
                "flow_rate_by_volume":[(1.0, 35.0), (10.0, 24.0), (50.0, 35.0)],
                "mix": {"enabled": False},
                "pre_wet": True,
                "retract": {
                    "air_gap_by_volume": [[0.0, 0.0]],
                    "delay": {"enabled": False},
                    "end_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "liquid-meniscus",
                    },
                    "speed": 10,
                    "touch_tip": {
                        "enabled": False,
                        "params":{"zOffset": -1, "mmFromEdge": 0.5, "speed": 30}
                    },
                },
                "submerge": {
                    "delay": {"enabled": False},
                    "speed": 50,
                    "start_position": {
                       "offset": {"x": 0, "y": 0, "z": 2},
                       "position_reference": "liquid-meniscus",
                    },
                },
            },
            "singleDispense": {
                "correction_by_volume": [(0.0, 0.0), (1.0, -0.2), (10.0,1), (50.0, -0.2)],
                "delay": {"enabled": True, "params": {"duration": 0.05}},
                "dispense_position": {
                    "offset": {"x": 0, "y": 0, "z": 2},
                    "position_reference": "well-bottom",
                },
                "flow_rate_by_volume": [(1.0, 3.5), (10.0, 5.0), (50.0, 50.0)],
                "mix": {"enabled": False}, #{"enabled": True, "params": {"repetitions": 1, "volume": 10}},
                "push_out_by_volume": [(1.0, 0), (4.999, 0), (5.0, 0), (50.0, 0)],
                "retract": {
                    "air_gap_by_volume": [[0.0, 0.0]],
                    "blowout": {"enabled": False},
                    "delay": {"enabled": False},
                    "end_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-top",
                    },
                    "speed": 50,
                    "touch_tip": {
                        "enabled": False,
                        "params":{"zOffset": -1, "mmFromEdge": 0.5, "speed": 30}
                    },
                },
                "submerge": {
                    "delay": {"enabled": False},
                    "speed": 50,
                    "start_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-top",
                    },
                },
            },
            "multiDispense": {
                "submerge": {
                  "startPosition": {
                    "positionReference": "well-top",
                    "offset": {
                      "x": 0,
                      "y": 0,
                      "z": 2
                    }
                  },
                  "speed": 25,
                  "delay": {
                    "enable": False,
                    "params": {
                      "duration": 0.0
                    }
                  }
                },
                "retract": {
                  "endPosition": {
                    "positionReference": "well-top",
                    "offset": {
                      "x": 0,
                      "y": 0,
                      "z": 2
                    }
                  },
                  "speed": 4,
                  "airGapByVolume": [[0.0, 0.0]],
                  "blowout": {
                    "enable": True,
                    "params": {
                      "location": "source",
                      "flowRate": 25.0
                    }
                  },
                  "touchTip": {
                    "enable": False,
                    "params": {
                      "zOffset": -1,
                      "mmFromEdge": 0.5,
                      "speed": 30
                    }
                  },
                  "delay": {
                    "enable": False,
                    "params": {
                      "duration": 0
                    }
                  }
                },
                "dispensePosition": {
                  "positionReference": "well-bottom",
                  "offset": {
                    "x": 0,
                    "y": 0,
                    "z": 2
                  }
                },
                "flowRateByVolume": [[0.0, 25.0]],
                "correctionByVolume": [
                  [0.0, 0.0],
                  [1.0, -0.2],
                  [10.0, 0.1],
                  [50.0, -0.2]
                ],
                "conditioningByVolume": [
                  [1.0, 5.0],
                  [40.0, 5.0],
                  [45.0, 0.0],
                  [50.0, 0.0]
                ],
                "disposalByVolume": [
                  [1.0, 5.0],
                  [40.0, 5.0],
                  [45.0, 0.0],
                  [50.0, 0.0]
                ],
                "delay": {
                  "enable": True,
                  "params": {
                    "duration": 0.5
                  }
                }
              }
            }
    },
    "flex_1channel_1000": {
        "opentrons/opentrons_flex_96_filtertiprack_1000ul/1": {
            "aspirate": {
                "aspirate_position": {
                    "offset": {"x": 0, "y": 0, "z": 1},
                    "position_reference": "well-bottom",
                },
                "correction_by_volume":  [(0.0, 0.0), (10.0, -0.2), (100.0,-0.1), (1000.0, 12)],
                "delay": {"enabled": True, "params": {"duration": 0.05}},
                "flow_rate_by_volume":[(10.0, 10.0),(100.0, 100.0),(1000.0, 800.0)],
                "mix": {"enabled": False},
                "pre_wet": True,
                "retract": {
                    "air_gap_by_volume": [[0.0, 0.0]],
                    "delay": {"enabled": False},
                    "end_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "liquid-meniscus",
                    },
                    "speed": 20,
                    "touch_tip": {
                        "enabled": False,
                        "params":{"zOffset": -1, "mmFromEdge": 0.5, "speed": 30}
                    },
                },
                "submerge": {
                    "delay": {"enabled": False},
                    "speed": 100,
                    "start_position": {
                       "offset": {"x": 0, "y": 0, "z": 2},
                       "position_reference": "liquid-meniscus",
                    },
                },
            },
            "singleDispense": {
                "correction_by_volume": [(0.0, 0.0), (10.0, -0.2), (100.0,-.1), (1000.0, 12)],
                "delay": {"enabled": True, "params": {"duration": 0.05}},
                "dispense_position": {
                    "offset": {"x": 0, "y": 0, "z": 4},
                    "position_reference": "well-bottom",
                },
                "flow_rate_by_volume": [(1.0, 3.5), (10.0, 5.0), (50.0, 50.0)],
                "mix": {"enabled": False}, #{"enabled": True, "params": {"repetitions": 1, "volume": 10}},
                "push_out_by_volume": [[0,35.0]],
                "retract": {
                    "air_gap_by_volume": [[0.0, 0.0]],
                    "blowout": {"enabled": False},
                    "delay": {"enabled": False},
                    "end_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-top",
                    },
                    "speed": 20,
                    "touch_tip": {
                        "enabled": False,
                        "params":{"zOffset": -1, "mmFromEdge": 0.5, "speed": 30}
                    },
                },
                "submerge": {
                    "delay": {"enabled": False},
                    "speed": 50,
                    "start_position": {
                        "offset": {"x": 0, "y": 0, "z": 2},
                        "position_reference": "well-top",
                    },
                },
            },
            "multiDispense": {
                "submerge": {
                  "startPosition": {
                    "positionReference": "well-top",
                    "offset": {
                      "x": 0,
                      "y": 0,
                      "z": 2
                    }
                  },
                  "speed": 35,
                  "delay": {
                    "enable": False,
                    "params": {
                      "duration": 0.0
                    }
                  }
                },
                "retract": {
                  "endPosition": {
                    "positionReference": "well-top",
                    "offset": {
                      "x": 0,
                      "y": 0,
                      "z": 2
                    }
                  },
                  "speed": 35,
                  "airGapByVolume": [[0.0, 0.0]],
                  "blowout": {
                    "enable": True,
                    "params": {
                      "location": "source",
                      "flowRate": 250.0
                    }
                  },
                  "touchTip": {
                    "enable": False,
                    "params": {
                      "zOffset": -1,
                      "mmFromEdge": 0.5,
                      "speed": 30
                    }
                  },
                  "delay": {
                    "enable": False,
                    "params": {
                      "duration": 0
                    }
                  }
                },
                "dispensePosition": {
                  "positionReference": "well-bottom",
                  "offset": {
                    "x": 0,
                    "y": 0,
                    "z": 2
                  }
                },
                "flowRateByVolume": [[0.0, 250.0]],
                "correctionByVolume": [
                  [0.0, 0.0],
                  [10.0, -0.2],
                  [100.0, -0.1],
                  [1000.0, 12]
                ],
                "conditioningByVolume": [
                  [1.0, 5.0],
                  [990.0, 5.0],
                  [995.0, 0.0],
                  [1000.0, 0.0]
                ],
                "disposalByVolume": [
                  [1.0, 0.0],
                  [990.0, 0.0],
                  [995.0, 0.0],
                  [1000.0, 0.0]
                ],
                "delay": {
                  "enable": True,
                  "params": {
                    "duration": 0.5
                  }
                }
              }
            }
    }
}
from collections import namedtuple
import pandas as pd
import itertools
import os
import csv
import sys
import numpy as np

# Reagent = namedtuple('Reagent', ['plate', 'well', 'stock_conc', 'units', 'description', 'artifact_num'])
#
# REAGENT_INFO = {
#     "hepes": Reagent("reagent_plate", "A1", 1000, "mM", "HEPES", "AR-148"),
#     "potassium_glutamate": Reagent("reagent_plate", "A2", 2500, "mM", "Potassium glutamate", "AR-145"),
#     "magnesium_acetate": Reagent("reagent_plate", "A3", 1000, "mM", "Magnesium acetate", "AR-146"),
#     "ntp": Reagent("reagent_plate", "A4", 100, "mM", "NTP", "AR-728"),
#     "creatine_phosphate": Reagent("reagent_plate", "A5", 1000, "mM", "Creatine phosphate", "AR-702"),
#     "tcep": Reagent("reagent_plate", "A6", 500, "mM", "TCEP", "-"),
#     "folinic_acid": Reagent("reagent_plate", "A7", 5, "mM", "Folinic acid", "AR-161"),
#     "spermidine": Reagent("reagent_plate", "A8", 200, "mM", "Spermidine", "AR-159"),
#     "amino_acid_solution": Reagent("reagent_plate", "A9", 3.25, "mM", "Amino Acid solution", "AR-684"),
#     "trna": Reagent("reagent_plate", "A10", 35, "ug/ul", "tRNA", "AR-730"),
#     "water": Reagent("reagent_plate", "A11", None, "-", "Water", None),
# }
#
# smix_reagents_to_mix = [
#     "hepes", "potassium_glutamate", "magnesium_acetate", "ntp",
#     "creatine_phosphate", "tcep", "folinic_acid", "spermidine",
#     "amino_acid_solution", "water"
# ]
# smix_final_volume = 200  # ul
# smix_fold = 3.3
# final_pure_concs = {
#     'hepes': 50,
#     'potassium_glutamate': 100,
#     'magnesium_acetate': [7.5, 10, 12.5],  # Example sweep
#     'ntp': [1.5, 2, 2.5],                  # Example sweep
#     'creatine_phosphate': 20,
#     'tcep': 1,
#     'folinic_acid': 0.02,
#     'spermidine': 2,
#     'amino_acid_solution': 0.3,
#     'trna': 3.5,
#     'water': None,
#     'neb_sol_a': 1,
#     'neb_sol_b': 1, 'dna': 5, 'rnas_inh': 1,
# }
# reaction_volume = 10  # ul
def check_valid_input_params(REAGENT_INFO, final_pure_concs):
    # TODO: This isnt amenable to dfs
    # ============================================================================
    # ASSERTION 1: All stock concentrations must be positive
    # ============================================================================
    print("\n[1] Checking stock concentrations are positive...")
    for reagent_name, reagent_info in REAGENT_INFO.items():
        if reagent_info.stock_conc is not None:
            assert reagent_info.stock_conc > 0, \
                f"ERROR: {reagent_name} has non-positive stock concentration: {reagent_info.stock_conc}"
    print("✓ All stock concentrations are positive")

    # ============================================================================
    # ASSERTION 2: All target concentrations must be positive (if specified)
    # ============================================================================
    print("\n[2] Checking target concentrations are positive...")
    for reagent, conc in final_pure_concs.items():
        if conc is not None:
            if isinstance(conc, list):
                for c in conc:
                    assert c > 0, f"ERROR: {reagent} has non-positive target concentration: {c}"
            else:
                assert conc > 0, f"ERROR: {reagent} has non-positive target concentration: {conc}"
    print("✓ All target concentrations are positive")

def get_sweep_reagents(final_pure_concs):
    # Identify sweep reagents
    sweep_reagents = []
    sweep_values = []
    for reagent, conc in final_pure_concs.items():
        if isinstance(conc, list) and len(conc) > 1:
            sweep_reagents.append(reagent)
            sweep_values.append(conc)
    return sweep_reagents, sweep_values

def calc_base_conc_for_sweep(smix_reagents_to_mix, final_pure_concs):
    # Determine minimal concentration for each sweep reagent (for smix)
    smix_base_concs = {}
    for r in smix_reagents_to_mix:
        if r in final_pure_concs:
            conc = final_pure_concs[r]
            if isinstance(conc, list):
                smix_base_concs[r] = min(conc)  # Use minimal concentration for smix
            else:
                smix_base_concs[r] = conc
        else:
            smix_base_concs[r] = None
    return smix_base_concs

def calc_smix_conc(smix_base_concs, smix_reagents_to_mix, smix_fold, reagents, smix_final_volume, reaction_volume):
    # Calculate smix composition at 3.3x concentration (using minimal values)
    smix_target_conc = {}
    smix_vols_needed = {}

    for r in smix_reagents_to_mix:
        pure_conc = smix_base_concs[r]
        if pure_conc is not None:
            smix_target_conc[r] = pure_conc * smix_fold
            stock = reagents[r].stock_conc
            smix_vols_needed[r] = round((smix_target_conc[r] * smix_final_volume) / stock, 3)
        else:
            smix_target_conc[r] = None
            smix_vols_needed[r] = None

    # ============================================================================
    # ASSERTION 4: All smix volumes must be positive
    # ============================================================================
    print("\n[4] Checking all smix volumes are positive...")
    for reagent, vol in smix_vols_needed.items():
        if vol is not None:
            assert vol > 0, f"ERROR: {reagent} has non-positive smix volume: {vol} ul"
    print("✓ All smix volumes are positive")

    # Calculate water volume
    total_non_water_vol = sum(v for r, v in smix_vols_needed.items() if r != 'water' and v is not None)
    water_vol = round(smix_final_volume - total_non_water_vol, 3)
    smix_vols_needed['water'] = water_vol

    # ============================================================================
    # ASSERTION 5: Smix total volume must equal target volume
    # ============================================================================
    print("\n[5] Checking smix total volume equals target...")
    smix_total = sum(v for v in smix_vols_needed.values() if v is not None)
    assert abs(smix_total - smix_final_volume) < 0.01, \
        f"ERROR: Smix total volume ({smix_total} ul) != target volume ({smix_final_volume} ul)"
    print(f"✓ Smix total volume = {smix_total:.3f} ul (target: {smix_final_volume} ul)")

    # ============================================================================
    # ASSERTION 6: Water volume must be positive
    # ============================================================================
    print("\n[6] Checking water volume is positive...")
    assert water_vol > 0, f"ERROR: Water volume is non-positive: {water_vol} ul (reagents overfilled!)"
    print(f"✓ Water volume = {water_vol:.3f} ul")

    # Calculate smix volume needed per reaction
    smix_vol_per_reaction = round(reaction_volume / smix_fold, 3)  # ul
    return smix_target_conc, smix_vols_needed, smix_vol_per_reaction

def check_reaction_conditions(reaction_rows, sweep_reagents,reaction_volume, smix_vol_per_reaction,
                              final_pure_concs, reagents, warnings=[]):
    # ============================================================================
    # ASSERTION 7: All extra volumes must be non-negative
    # ============================================================================
    # print("\n[7] Checking all extra volumes are non-negative...")
    # for row in reaction_rows:
    #     for reagent in sweep_reagents:
    #         extra_vol = row[f'{reagent}_extra_ul']
    #         assert extra_vol >= 0, \
    #             f"ERROR: {row['condition']} has negative extra volume for {reagent}: {extra_vol} ul"
    # print("✓ All extra volumes are non-negative")

    # ============================================================================
    # ASSERTION 8: Total volume (smix + extras) must not exceed reaction volume
    # ============================================================================
    # print("\n[8] Checking total volumes don't exceed reaction volume...")
    # max_extra_vol_allowed = reaction_volume - smix_vol_per_reaction
    # for row in reaction_rows:
    #     total_check = row['total_vol_check']
    #     if total_check > reaction_volume:
    #         warnings.append(
    #             f"WARNING: {row['condition']} total volume ({total_check} ul) exceeds reaction volume ({reaction_volume} ul)")
    #     assert row['total_extra_vol'] <= max_extra_vol_allowed, \
    #         f"ERROR: {row['condition']} extra volumes ({row['total_extra_vol']} ul) exceed available space ({max_extra_vol_allowed} ul)"
    # print(f"✓ All extra volumes fit within reaction volume (max allowed: {max_extra_vol_allowed:.3f} ul)")

    # ============================================================================
    # ASSERTION 9: Smix volume must be less than reaction volume
    # ============================================================================
    print("\n[9] Checking smix volume leaves room for titrations...")
    assert smix_vol_per_reaction < reaction_volume, \
        f"ERROR: Smix volume ({smix_vol_per_reaction} ul) >= reaction volume ({reaction_volume} ul)"
    print(f"✓ Smix volume ({smix_vol_per_reaction} ul) < reaction volume ({reaction_volume} ul)")

    # ============================================================================
    # ASSERTION 10: Target concentrations achievable with stock concentrations
    # ============================================================================
    print("\n[10] Checking target concentrations are achievable...")
    for reagent, conc in final_pure_concs.items():
        if conc is not None and reagent in reagents:
            stock_conc = reagents[reagent].stock_conc
            if stock_conc is not None:
                if isinstance(conc, list):
                    max_target = max(conc)
                else:
                    max_target = conc
                max_achievable = stock_conc
                assert max_target <= max_achievable, \
                    f"ERROR: {reagent} target ({max_target} mM) exceeds stock concentration ({stock_conc} mM)"
    print("✓ All target concentrations are achievable with available stocks")

    # Display warnings if any
    if warnings:
        print("\n" + "!" * 60)
        print("WARNINGS:")
        for warning in warnings:
            print(f"  {warning}")
        print("!" * 60)

    # return warnings
def add_fixed_volumes_to_df(reaction_rows, sweep_reagents, smix_reagents_to_mix, final_pure_concs, reagents,
                            reaction_volume):
    # Build main reaction conditions DataFrame
    reaction_conditions = pd.DataFrame(reaction_rows)

    non_smix_reagents = [
        r for r in final_pure_concs.keys()
        if r not in smix_reagents_to_mix and r != 'water'
    ]
    # Add vectorized columns for all fixed reagents (NOT in smix, NOT sweep)
    fixed_reagents = [r for r in non_smix_reagents if
                      not (r in sweep_reagents and r in smix_reagents_to_mix) and r != 'water' and r in reagents]

    for reagent in fixed_reagents:
        conc = final_pure_concs[reagent]
        stock_conc = reagents[reagent].stock_conc
        if stock_conc and conc is not None:
            vol_needed = round((conc * reaction_volume) / stock_conc, 4)
            reaction_conditions[f'{reagent}_vol_ul'] = vol_needed


    # After all reagent columns are added, compute the sum of fixed additions for each row
    reaction_conditions['fixed_total_ul'] = reaction_conditions[[f'{r}_vol_ul' for r in fixed_reagents]].sum(axis=1)

    # Now calculate water column in vectorized fashion
    # For each row: water = reaction_volume - (smix + all titrations + all fixed)
    tit_columns = [col for col in reaction_conditions.columns if col.endswith('_extra_ul')]
    reaction_conditions['titration_sum_ul'] = reaction_conditions[tit_columns].sum(axis=1) if tit_columns else 0
    reaction_conditions['water_vol_ul'] = (
            reaction_volume
            - reaction_conditions['bnext_sms_vol_ul']
            - reaction_conditions['titration_sum_ul']
            - reaction_conditions['fixed_total_ul']
    ).round(4).clip(lower=0.0)

    # Optionally compute final volume check
    reaction_conditions['final_vol_check'] = (
            reaction_conditions['bnext_sms_vol_ul']
            + reaction_conditions['titration_sum_ul']
            + reaction_conditions['fixed_total_ul']
            + reaction_conditions['water_vol_ul']
    ).round(4)
    assert reaction_conditions['final_vol_check'].any() < reaction_volume, 'OT appropriate print statement. Uncomment next line instead'
    # assert reaction_conditions['final_vol_check'].any() < reaction_volume, f'Lower sweep reagent concentrations -- not enough dead volume for reaction condition {reaction_conditions[reaction_conditions['final_vol_check'] > reaction_volume]}'
    return reaction_conditions

def find_suitable_reagent(base_name, reagents, target_conc, reaction_volume, min_vol,
                          used_volume):
    """
    Given a sweep reagent, find the best stock (original or diluted)
    that gives >= min_vol. Creates a new aliquot if none exist.
    """
    # if sweep_reagent is not None:
    #     base_name = sweep_reagent["name"]
    print(f'Finding suitable available concentrations of {base_name} for {target_conc} conc with minimum pipetting volume of {min_vol}ul')
    # Gather all available versions of this reagent (base + aliquots)
    candidate_names = [r for r in reagents if r.startswith(base_name)]
    candidates = [(name, reagents[name]) for name in candidate_names]
    # log(f"{base_name} has {candidates} candidates")
    # Try each candidate stock concentration
    for name, reagent in sorted(candidates, key=lambda x: -x[1].stock_conc):
        vol = (reaction_volume * target_conc) / reagent.stock_conc
        water_to_add = reaction_volume - used_volume - vol
        print(f'    If using {name} will need vol {vol} + water {water_to_add}')
        if (vol >= min_vol) and (water_to_add >= 0):
            return reagent, vol, name  # found a usable stock

    # If none suitable, determine a suitable diluted stock factor
    parent = reagents[base_name] #TODO: choose most appropriate concentration dont just take base
    # Dilute just enough so the required volume is >= min_vol
    child_conc = np.ceil(reaction_volume * target_conc) / min_vol
    dilution_factor = parent.stock_conc / child_conc
    assert dilution_factor > 1, f"No available stock to be made from {parent.stock_conc} {parent.units} for {target_conc} {parent.units}"

    # new_reagent = create_and_register_diluted_reagent(reagents, base_name, dilution_factor, protocol, log, pipette)
    vol = (reaction_volume * target_conc) / child_conc
    assert False, (f'Failed to find a suitable reagent for {target_conc} {parent.units} within minimum pipetting bounds'
                   f'\n Suggest adding a {base_name} reagent w/ dilution factor {dilution_factor} for {child_conc} {parent.units}')
    # return reagent, vol
    # assert np.all(vol > 0), f"Impossible mixture for concs {target_conc} vol is {vol}"
    # print(f'Make a diluted stock of {child_conc} {parent.units} with dilution_factor: {dilution_factor} for {target_conc} {parent.units}')


def generate_sweep_combinations(sweep_reagents, sweep_values, smix_vol_per_reaction, smix_base_concs,
                                reagents, reaction_volume):
    # Generate all combinations of sweep reagents
    if sweep_reagents:
        combinations = list(itertools.product(*sweep_values))
    else:
        combinations = [tuple()]

    # For each combination, calculate extra volumes needed
    reaction_rows = []

    for combo_idx, combo in enumerate(combinations):
        row = {'condition': f'Condition_{combo_idx + 1}', 'bnext_sms_vol_ul': smix_vol_per_reaction}
        # Add target concentrations for sweep reagents
        for i, reagent in enumerate(sweep_reagents):
            row[f'{reagent}_target_mM'] = combo[i]
        # Calculate extra volume needed for each sweep reagent
        for i, reagent in enumerate(sweep_reagents):
            target_conc = combo[i]
            base_conc = smix_base_concs[reagent]  # Concentration provided by smix
            extra_conc_needed = target_conc - base_conc
            if extra_conc_needed > 0:
                best_reagent, extra_vol, name = (
                    find_suitable_reagent(reagent, reagents, extra_conc_needed,
                                          reaction_volume, min_vol=0.3, used_volume=0)) #currently not tracking everything in well yet
                # stock_conc = reagents[reagent].stock_conc
                # extra_vol = round((extra_conc_needed * reaction_volume) / stock_conc, 4)
                row[f'{name}_extra_ul'] = extra_vol
            else:
                row[f'{reagent}_extra_ul'] = 0.0
        reaction_rows.append(row)
        print(f'Sucessfully generated {combo} concs for {sweep_reagents} sweep reagents')
    return reaction_rows

def save_table(table, file_path):
    # def save_tracked_wells(self, file_path, log):
    """Save wells to CSV if local, otherwise log to comments on robot."""
    if os.environ.get("OT_SIMULATE_CSV"):
        print(f'Tables saved to {file_path}')
        table.to_csv(file_path, index=False)
    else:
        print(f'Attempted to save to {file_path},'
            f'But the environment variable "OT_SIMULATE_CSV" is not set.'                
            f'To save the file on this machine, run: export OT_SIMULATE_CSV=1'
            f'Do not set on OT since it is a write only machine')

def create_output_tables(smix_reagents_to_mix, smix_base_concs, smix_target_conc,
                         smix_vols_needed, reaction_conditions, save_tables=True):
    # Create output tables
    smix_table = pd.DataFrame({
        'reagent': smix_reagents_to_mix,
        'smix_base_conc_mM': [smix_base_concs[r] for r in smix_reagents_to_mix],
        'smix_target_conc_mM': [smix_target_conc[r] for r in smix_reagents_to_mix],
        'bnext_sms_vol_ul': [smix_vols_needed[r] for r in smix_reagents_to_mix],
    })

    # reaction_conditions = pd.DataFrame(reaction_rows)
    if save_tables:
        # Save outputs
        # smix_table.to_csv("smix_volumes_sweep.csv", index=False)
        # reaction_conditions.to_csv("reaction_conditions_sweep.csv", index=False)
        main_dir = f'/Volumes/bnext/experiments/ot_smix_params/energy_mix_'
        save_table(smix_table, main_dir + "smix_volumes_sweep.csv")
        save_table(reaction_conditions, main_dir + "reaction_conditions_sweep.csv")
    return smix_table, reaction_conditions

def generate_smix_and_sweep_tables(smix_reagents_to_mix, smix_fold, smix_final_volume,
                                   final_pure_concs, reagents, reaction_volume):
    smix_base_concs= calc_base_conc_for_sweep(smix_reagents_to_mix, final_pure_concs)
    smix_target_conc, smix_vols_needed, smix_vol_per_reaction = calc_smix_conc(smix_base_concs, smix_reagents_to_mix,
                                                                               smix_fold, reagents, smix_final_volume,
                                                                               reaction_volume)

    sweep_reagents, sweep_values = get_sweep_reagents(final_pure_concs)
    reaction_rows = generate_sweep_combinations(sweep_reagents, sweep_values, smix_vol_per_reaction, smix_base_concs,
                                                reagents, reaction_volume
                                                )
    reaction_conditions = add_fixed_volumes_to_df(reaction_rows, sweep_reagents, smix_reagents_to_mix, final_pure_concs, reagents,
                            reaction_volume)
    smix_table, reaction_conditions = create_output_tables(smix_reagents_to_mix, smix_base_concs, smix_target_conc,
                                                        smix_vols_needed, reaction_conditions, save_tables=True)
    check_reaction_conditions(reaction_rows, sweep_reagents, reaction_volume, smix_vol_per_reaction,
                              final_pure_concs, reagents, warnings=[])
    return smix_table, reaction_conditions


def calculate_vol_to_pipette(df, reaction_volume, buffer_name="water", final_conc_col = "final_conc"):
    """
       Calculate pipetting volumes for reaction components and assign remaining
       volume to a buffer reagent (e.g., water).

       Non-buffer volumes are calculated as:
           reaction_volume * final_conc / stock_conc

       The buffer row receives the remaining volume needed to reach the total
       reaction volume. Volumes are rounded to 0.01 µL and validated with safety
       assertions.

       Parameters
       ----------
       df : pandas.DataFrame
           Must contain columns: 'reagent', 'final_conc', 'stock_conc'.
       reaction_volume : float
           Total reaction volume in µL (> 0).
       buffer_name : str, optional
           Name of buffer reagent. Defaults to "water".

       Returns
       -------
       pandas.DataFrame
           DataFrame with 'vol_to_pipette' column (µL, rounded to 0.01).

       Raises
       ------
       AssertionError
           If inputs are invalid or calculated volumes are inconsistent.
       """
    REQUIRED_COLS = {final_conc_col, "stock_conc"}
    missing = REQUIRED_COLS - set(df.columns)
    assert not missing, f"Missing required columns: {missing}"
    assert reaction_volume > 0, "reaction_volume must be > 0 µL"
    # get reagent names from column or index
    if "reagent" in df.columns:
        reagents = df["reagent"]
    else:
        assert df.index.name == "reagent" or df.index.dtype == object, (
            "Expected 'reagent' column or reagent names as index"
        )
        reagents = df.index

    # ensure exactly one buffer row
    buffer_mask = reagents == buffer_name
    assert buffer_mask.sum() == 1, (
        f"Expected exactly one '{buffer_name}' row, found {buffer_mask.sum()}"
    )

    # calculate volumes for non-buffer reagents
    df["vol_to_pipette"] = reaction_volume * df[final_conc_col] / df["stock_conc"]

    non_buffer_mask = ~buffer_mask
    non_buffer_vol = df.loc[non_buffer_mask, "vol_to_pipette"].sum(skipna=True)

    # assign remaining volume to buffer
    buffer_vol = reaction_volume - non_buffer_vol
    assert buffer_vol >= 0, (
        f"Calculated {buffer_name} volume is negative ({buffer_vol:.3f} µL). "
        "Check concentrations or reaction_volume."
    )

    df.loc[buffer_mask, "vol_to_pipette"] = buffer_vol

    # round to 0.01 µL
    df["vol_to_pipette"] = df["vol_to_pipette"].round(3)

    # final safety check: total volume matches reaction_volume
    total_vol = df["vol_to_pipette"].sum()
    assert abs(total_vol - reaction_volume) <= 0.01, (
        f"Total volume {total_vol:.2f} µL does not match "
        f"reaction_volume {reaction_volume:.2f} µL"
    )

    return df
# smix_table, reaction_conditions  = generate_smix_and_sweep_tables(smix_reagents_to_mix, smix_fold, smix_final_volume, final_pure_concs, reagents, reaction_volume)
# AUTO-GENERATED FROM CSV – DO NOT EDIT MANUALLY

BASE_MASTER_MIX = [
    {'reagent': 'dna', 'unit': 'nM', 'stock_conc': 92.0, 'base_conc': 1.0, 'vol_per_rxn_ul': 0.109, 'vol_to_pipette_ul': 4.696, 'below_min_pipetting_vol': False, 'base_master_mix_fold': 1.647773, 'base_master_mix_vol_to_add_ul': 6.069, 'effective_pipetting_scalar': 1.2, 'total_master_mix_volume_ul': 262.172},
    {'reagent': 'rnas_inh', 'unit': 'U/ml', 'stock_conc': 40000.0, 'base_conc': 2000.0, 'vol_per_rxn_ul': 0.5, 'vol_to_pipette_ul': 21.6, 'below_min_pipetting_vol': False, 'base_master_mix_fold': 1.647773, 'base_master_mix_vol_to_add_ul': 6.069, 'effective_pipetting_scalar': 1.2, 'total_master_mix_volume_ul': 262.172},
    {'reagent': 'ribosome', 'unit': 'uM', 'stock_conc': 10.0, 'base_conc': 1.799, 'vol_per_rxn_ul': 1.799, 'vol_to_pipette_ul': 77.717, 'below_min_pipetting_vol': False, 'base_master_mix_fold': 1.647773, 'base_master_mix_vol_to_add_ul': 6.069, 'effective_pipetting_scalar': 1.2, 'total_master_mix_volume_ul': 262.172},
    {'reagent': 'magnesium_acetate', 'unit': 'mM', 'stock_conc': 1000.0, 'base_conc': 2.469, 'vol_per_rxn_ul': 0.025, 'vol_to_pipette_ul': 1.067, 'below_min_pipetting_vol': False, 'base_master_mix_fold': 1.647773, 'base_master_mix_vol_to_add_ul': 6.069, 'effective_pipetting_scalar': 1.2, 'total_master_mix_volume_ul': 262.172},
    {'reagent': 'potassium_glutamate', 'unit': 'mM', 'stock_conc': 2500.0, 'base_conc': 60.0, 'vol_per_rxn_ul': 0.24, 'vol_to_pipette_ul': 10.368, 'below_min_pipetting_vol': False, 'base_master_mix_fold': 1.647773, 'base_master_mix_vol_to_add_ul': 6.069, 'effective_pipetting_scalar': 1.2, 'total_master_mix_volume_ul': 262.172},
    {'reagent': 'hepes', 'unit': 'mM', 'stock_conc': 1500.0, 'base_conc': 50.0, 'vol_per_rxn_ul': 0.333, 'vol_to_pipette_ul': 14.4, 'below_min_pipetting_vol': False, 'base_master_mix_fold': 1.647773, 'base_master_mix_vol_to_add_ul': 6.069, 'effective_pipetting_scalar': 1.2, 'total_master_mix_volume_ul': 262.172},
    {'reagent': 'atp', 'unit': 'mM', 'stock_conc': 100.0, 'base_conc': 2.0, 'vol_per_rxn_ul': 0.2, 'vol_to_pipette_ul': 8.64, 'below_min_pipetting_vol': False, 'base_master_mix_fold': 1.647773, 'base_master_mix_vol_to_add_ul': 6.069, 'effective_pipetting_scalar': 1.2, 'total_master_mix_volume_ul': 262.172},
    {'reagent': 'gtp', 'unit': 'mM', 'stock_conc': 100.0, 'base_conc': 2.0, 'vol_per_rxn_ul': 0.2, 'vol_to_pipette_ul': 8.64, 'below_min_pipetting_vol': False, 'base_master_mix_fold': 1.647773, 'base_master_mix_vol_to_add_ul': 6.069, 'effective_pipetting_scalar': 1.2, 'total_master_mix_volume_ul': 262.172},
    {'reagent': 'ctp', 'unit': 'mM', 'stock_conc': 50.0, 'base_conc': 1.0, 'vol_per_rxn_ul': 0.2, 'vol_to_pipette_ul': 8.64, 'below_min_pipetting_vol': False, 'base_master_mix_fold': 1.647773, 'base_master_mix_vol_to_add_ul': 6.069, 'effective_pipetting_scalar': 1.2, 'total_master_mix_volume_ul': 262.172},
    {'reagent': 'utp', 'unit': 'mM', 'stock_conc': 50.0, 'base_conc': 1.0, 'vol_per_rxn_ul': 0.2, 'vol_to_pipette_ul': 8.64, 'below_min_pipetting_vol': False, 'base_master_mix_fold': 1.647773, 'base_master_mix_vol_to_add_ul': 6.069, 'effective_pipetting_scalar': 1.2, 'total_master_mix_volume_ul': 262.172},
    {'reagent': 'tcep', 'unit': 'mM', 'stock_conc': 50.0, 'base_conc': 1.0, 'vol_per_rxn_ul': 0.2, 'vol_to_pipette_ul': 8.64, 'below_min_pipetting_vol': False, 'base_master_mix_fold': 1.647773, 'base_master_mix_vol_to_add_ul': 6.069, 'effective_pipetting_scalar': 1.2, 'total_master_mix_volume_ul': 262.172},
    {'reagent': 'folinic_acid', 'unit': 'mM', 'stock_conc': 5.0, 'base_conc': 0.02, 'vol_per_rxn_ul': 0.04, 'vol_to_pipette_ul': 1.728, 'below_min_pipetting_vol': False, 'base_master_mix_fold': 1.647773, 'base_master_mix_vol_to_add_ul': 6.069, 'effective_pipetting_scalar': 1.2, 'total_master_mix_volume_ul': 262.172},
    {'reagent': 'spermidine', 'unit': 'mM', 'stock_conc': 200.0, 'base_conc': 2.0, 'vol_per_rxn_ul': 0.1, 'vol_to_pipette_ul': 4.32, 'below_min_pipetting_vol': False, 'base_master_mix_fold': 1.647773, 'base_master_mix_vol_to_add_ul': 6.069, 'effective_pipetting_scalar': 1.2, 'total_master_mix_volume_ul': 262.172},
    {'reagent': 'aas', 'unit': 'mM', 'stock_conc': 3.25, 'base_conc': 0.3, 'vol_per_rxn_ul': 0.923, 'vol_to_pipette_ul': 39.877, 'below_min_pipetting_vol': False, 'base_master_mix_fold': 1.647773, 'base_master_mix_vol_to_add_ul': 6.069, 'effective_pipetting_scalar': 1.2, 'total_master_mix_volume_ul': 262.172},
    {'reagent': 'trna', 'unit': 'ug/ul', 'stock_conc': 35.0, 'base_conc': 3.5, 'vol_per_rxn_ul': 1.0, 'vol_to_pipette_ul': 43.2, 'below_min_pipetting_vol': False, 'base_master_mix_fold': 1.647773, 'base_master_mix_vol_to_add_ul': 6.069, 'effective_pipetting_scalar': 1.2, 'total_master_mix_volume_ul': 262.172},
]
REAGENTS = [
    {'reagent': 'hepes', 'reservoir': 'reagent_plate', 'well': 'A1', 'stock_conc': 1500.0, 'units': 'mM', 'description': 'HEPES', 'artifact_num': 'AR-977', 'liquid_type': None, 'volume': None, 'Unnamed: 9': None},
    {'reagent': 'potassium_glutamate', 'reservoir': 'reagent_plate', 'well': 'A2', 'stock_conc': 2500.0, 'units': 'mM', 'description': 'Potassium glutamate', 'artifact_num': 'AR-954', 'liquid_type': None, 'volume': None, 'Unnamed: 9': None},
    {'reagent': 'magnesium_acetate', 'reservoir': 'reagent_plate', 'well': 'A3', 'stock_conc': 1000.0, 'units': 'mM', 'description': 'Magnesium acetate', 'artifact_num': 'AR-953', 'liquid_type': None, 'volume': None, 'Unnamed: 9': None},
    {'reagent': 'atp', 'reservoir': 'reagent_plate', 'well': 'A4', 'stock_conc': 100.0, 'units': 'mM', 'description': 'ATP', 'artifact_num': 'AR-970', 'liquid_type': None, 'volume': None, 'Unnamed: 9': None},
    {'reagent': 'gtp', 'reservoir': 'reagent_plate', 'well': 'A5', 'stock_conc': 100.0, 'units': 'mM', 'description': 'GTP', 'artifact_num': 'AR-971', 'liquid_type': None, 'volume': None, 'Unnamed: 9': None},
    {'reagent': 'ctp', 'reservoir': 'reagent_plate', 'well': 'A6', 'stock_conc': 50.0, 'units': 'mM', 'description': 'CTP', 'artifact_num': 'AR-972', 'liquid_type': None, 'volume': None, 'Unnamed: 9': None},
    {'reagent': 'utp', 'reservoir': 'reagent_plate', 'well': 'A7', 'stock_conc': 50.0, 'units': 'mM', 'description': 'UTP', 'artifact_num': 'AR-973', 'liquid_type': None, 'volume': None, 'Unnamed: 9': None},
    {'reagent': 'creatine_phosphate', 'reservoir': 'reagent_plate', 'well': 'A8', 'stock_conc': 1000.0, 'units': 'mM', 'description': 'Creatine phosphate', 'artifact_num': 'AR-702', 'liquid_type': None, 'volume': None, 'Unnamed: 9': None},
    {'reagent': 'tcep', 'reservoir': 'reagent_plate', 'well': 'A9', 'stock_conc': 50.0, 'units': 'mM', 'description': 'TCEP', 'artifact_num': None, 'liquid_type': None, 'volume': None, 'Unnamed: 9': None},
    {'reagent': 'folinic_acid', 'reservoir': 'reagent_plate', 'well': 'A10', 'stock_conc': 5.0, 'units': 'mM', 'description': 'Folinic acid', 'artifact_num': 'AR-959', 'liquid_type': None, 'volume': None, 'Unnamed: 9': None},
    {'reagent': 'spermidine', 'reservoir': 'reagent_plate', 'well': 'A11', 'stock_conc': 200.0, 'units': 'mM', 'description': 'Spermidine', 'artifact_num': 'AR-967', 'liquid_type': None, 'volume': None, 'Unnamed: 9': None},
    {'reagent': 'aas', 'reservoir': 'reagent_plate', 'well': 'B1', 'stock_conc': 3.25, 'units': 'mM', 'description': 'Amino Acid solution', 'artifact_num': 'AR-969', 'liquid_type': None, 'volume': None, 'Unnamed: 9': None},
    {'reagent': 'trna', 'reservoir': 'reagent_plate', 'well': 'B2', 'stock_conc': 35.0, 'units': 'ug/ul', 'description': 'tRNA', 'artifact_num': 'AR-902', 'liquid_type': None, 'volume': None, 'Unnamed: 9': None},
    {'reagent': 'rnas_inh', 'reservoir': 'reagent_plate', 'well': 'B3', 'stock_conc': 40000.0, 'units': 'U/ml', 'description': 'RNAse Inhibitor', 'artifact_num': None, 'liquid_type': 'viscous_asp_mix', 'volume': None, 'Unnamed: 9': None},
    {'reagent': 'polyphosphate', 'reservoir': 'reagent_plate', 'well': 'B4', 'stock_conc': 500.0, 'units': 'mM', 'description': 'Polyphosphate', 'artifact_num': None, 'liquid_type': 'viscous_asp_mix', 'volume': None, 'Unnamed: 9': None},
    {'reagent': 'ppk', 'reservoir': 'reagent_plate', 'well': 'B5', 'stock_conc': 57.0, 'units': 'uM', 'description': 'PPK', 'artifact_num': None, 'liquid_type': 'viscous_asp_mix', 'volume': None, 'Unnamed: 9': None},
    {'reagent': 'dna', 'reservoir': 'reagent_plate', 'well': 'B6', 'stock_conc': 92.0, 'units': 'nM', 'description': 'pOpen-deGFP DNA', 'artifact_num': 'AR-854', 'liquid_type': None, 'volume': None, 'Unnamed: 9': None},
    {'reagent': 'ribosome', 'reservoir': 'reagent_plate', 'well': 'B7', 'stock_conc': 10.0, 'units': 'uM', 'description': 'nucleus ribosome', 'artifact_num': 'AR-905', 'liquid_type': 'viscous_asp_mix', 'volume': None, 'Unnamed: 9': None},
    {'reagent': 'pmix', 'reservoir': 'reagent_plate', 'well': 'B8', 'stock_conc': 15.0, 'units': 'mg/ml', 'description': 'nucleus pmix', 'artifact_num': 'AR-975', 'liquid_type': 'viscous_asp_mix', 'volume': None, 'Unnamed: 9': None},
    {'reagent': 'water', 'reservoir': 'reagent_plate', 'well': 'B9', 'stock_conc': None, 'units': None, 'description': 'Water', 'artifact_num': None, 'liquid_type': None, 'volume': None, 'Unnamed: 9': None},
    {'reagent': 'master_mix', 'reservoir': None, 'well': None, 'stock_conc': 1.647773, 'units': 'x', 'description': 'Auto-generated base master mix', 'artifact_num': None, 'liquid_type': None, 'volume': None, 'Unnamed: 9': None},
]
SAMPLES_TITRATION_LABCRAFT = [
    {'well_id': 'J16', '[DNA] (nM)': 1.996, '[PMix] (mg/mL)': 1.8, '[Magnesium acetate] (mM)': 17.531, '[Creatine phosphate] (mM)': 20.0, '[Potassium glutamate] (mM)': 40.0},
    {'well_id': 'H9', '[DNA] (nM)': 1.996, '[PMix] (mg/mL)': 1.8, '[Magnesium acetate] (mM)': 17.531, '[Creatine phosphate] (mM)': 20.0, '[Potassium glutamate] (mM)': 40.0},
    {'well_id': 'J10', '[DNA] (nM)': 1.996, '[PMix] (mg/mL)': 1.8, '[Magnesium acetate] (mM)': 17.531, '[Creatine phosphate] (mM)': 20.0, '[Potassium glutamate] (mM)': 40.0},
    {'well_id': 'G16', '[DNA] (nM)': 1.996, '[PMix] (mg/mL)': 1.95, '[Magnesium acetate] (mM)': 17.531, '[Creatine phosphate] (mM)': 20.0, '[Potassium glutamate] (mM)': 40.0},
    {'well_id': 'I14', '[DNA] (nM)': 1.996, '[PMix] (mg/mL)': 1.95, '[Magnesium acetate] (mM)': 17.531, '[Creatine phosphate] (mM)': 20.0, '[Potassium glutamate] (mM)': 40.0},
    {'well_id': 'G11', '[DNA] (nM)': 1.996, '[PMix] (mg/mL)': 1.95, '[Magnesium acetate] (mM)': 17.531, '[Creatine phosphate] (mM)': 20.0, '[Potassium glutamate] (mM)': 40.0},
    {'well_id': 'G12', '[DNA] (nM)': 1.996, '[PMix] (mg/mL)': 1.95, '[Magnesium acetate] (mM)': 3.531, '[Creatine phosphate] (mM)': 0.0, '[Potassium glutamate] (mM)': 80.0},
    {'well_id': 'G10', '[DNA] (nM)': 1.996, '[PMix] (mg/mL)': 1.95, '[Magnesium acetate] (mM)': 3.531, '[Creatine phosphate] (mM)': 0.0, '[Potassium glutamate] (mM)': 80.0},
    {'well_id': 'I15', '[DNA] (nM)': 1.996, '[PMix] (mg/mL)': 1.95, '[Magnesium acetate] (mM)': 3.531, '[Creatine phosphate] (mM)': 0.0, '[Potassium glutamate] (mM)': 80.0},
    {'well_id': 'I12', '[DNA] (nM)': 4.0, '[PMix] (mg/mL)': 1.8, '[Magnesium acetate] (mM)': 3.531, '[Creatine phosphate] (mM)': 0.0, '[Potassium glutamate] (mM)': 80.0},
    {'well_id': 'I10', '[DNA] (nM)': 4.0, '[PMix] (mg/mL)': 1.8, '[Magnesium acetate] (mM)': 3.531, '[Creatine phosphate] (mM)': 0.0, '[Potassium glutamate] (mM)': 80.0},
    {'well_id': 'I11', '[DNA] (nM)': 4.0, '[PMix] (mg/mL)': 1.8, '[Magnesium acetate] (mM)': 3.531, '[Creatine phosphate] (mM)': 0.0, '[Potassium glutamate] (mM)': 80.0},
    {'well_id': 'G8', '[DNA] (nM)': 1.996, '[PMix] (mg/mL)': 1.833, '[Magnesium acetate] (mM)': 10.74, '[Creatine phosphate] (mM)': 0.0, '[Potassium glutamate] (mM)': 40.0},
    {'well_id': 'J9', '[DNA] (nM)': 1.996, '[PMix] (mg/mL)': 1.833, '[Magnesium acetate] (mM)': 10.74, '[Creatine phosphate] (mM)': 0.0, '[Potassium glutamate] (mM)': 40.0},
    {'well_id': 'I8', '[DNA] (nM)': 1.996, '[PMix] (mg/mL)': 1.833, '[Magnesium acetate] (mM)': 10.74, '[Creatine phosphate] (mM)': 0.0, '[Potassium glutamate] (mM)': 40.0},
    {'well_id': 'H8', '[DNA] (nM)': 4.0, '[PMix] (mg/mL)': 1.828, '[Magnesium acetate] (mM)': 11.866, '[Creatine phosphate] (mM)': 20.0, '[Potassium glutamate] (mM)': 80.0},
    {'well_id': 'J13', '[DNA] (nM)': 4.0, '[PMix] (mg/mL)': 1.828, '[Magnesium acetate] (mM)': 11.866, '[Creatine phosphate] (mM)': 20.0, '[Potassium glutamate] (mM)': 80.0},
    {'well_id': 'G15', '[DNA] (nM)': 4.0, '[PMix] (mg/mL)': 1.828, '[Magnesium acetate] (mM)': 11.866, '[Creatine phosphate] (mM)': 20.0, '[Potassium glutamate] (mM)': 80.0},
    {'well_id': 'G14', '[DNA] (nM)': 0.0, '[PMix] (mg/mL)': 1.763, '[Magnesium acetate] (mM)': 21.274, '[Creatine phosphate] (mM)': 100.0, '[Potassium glutamate] (mM)': 0.0},
    {'well_id': 'H11', '[DNA] (nM)': 0.0, '[PMix] (mg/mL)': 1.763, '[Magnesium acetate] (mM)': 21.274, '[Creatine phosphate] (mM)': 100.0, '[Potassium glutamate] (mM)': 0.0},
    {'well_id': 'H15', '[DNA] (nM)': 0.0, '[PMix] (mg/mL)': 1.763, '[Magnesium acetate] (mM)': 21.274, '[Creatine phosphate] (mM)': 100.0, '[Potassium glutamate] (mM)': 0.0},
    {'well_id': 'J11', '[DNA] (nM)': 0.0, '[PMix] (mg/mL)': 1.555, '[Magnesium acetate] (mM)': 10.015, '[Creatine phosphate] (mM)': 49.321, '[Potassium glutamate] (mM)': 12.407},
    {'well_id': 'G13', '[DNA] (nM)': 0.0, '[PMix] (mg/mL)': 1.555, '[Magnesium acetate] (mM)': 10.015, '[Creatine phosphate] (mM)': 49.321, '[Potassium glutamate] (mM)': 12.407},
    {'well_id': 'G9', '[DNA] (nM)': 0.0, '[PMix] (mg/mL)': 1.555, '[Magnesium acetate] (mM)': 10.015, '[Creatine phosphate] (mM)': 49.321, '[Potassium glutamate] (mM)': 12.407},
    {'well_id': 'J12', '[DNA] (nM)': 0.0, '[PMix] (mg/mL)': 2.031, '[Magnesium acetate] (mM)': 22.531, '[Creatine phosphate] (mM)': 70.516, '[Potassium glutamate] (mM)': 63.735},
    {'well_id': 'H16', '[DNA] (nM)': 0.0, '[PMix] (mg/mL)': 2.031, '[Magnesium acetate] (mM)': 22.531, '[Creatine phosphate] (mM)': 70.516, '[Potassium glutamate] (mM)': 63.735},
    {'well_id': 'H12', '[DNA] (nM)': 0.0, '[PMix] (mg/mL)': 2.031, '[Magnesium acetate] (mM)': 22.531, '[Creatine phosphate] (mM)': 70.516, '[Potassium glutamate] (mM)': 63.735},
    {'well_id': 'I13', '[DNA] (nM)': 0.049, '[PMix] (mg/mL)': 1.976, '[Magnesium acetate] (mM)': 0.0, '[Creatine phosphate] (mM)': 67.201, '[Potassium glutamate] (mM)': 139.95},
    {'well_id': 'H14', '[DNA] (nM)': 0.049, '[PMix] (mg/mL)': 1.976, '[Magnesium acetate] (mM)': 0.0, '[Creatine phosphate] (mM)': 67.201, '[Potassium glutamate] (mM)': 139.95},
    {'well_id': 'H13', '[DNA] (nM)': 0.049, '[PMix] (mg/mL)': 1.976, '[Magnesium acetate] (mM)': 0.0, '[Creatine phosphate] (mM)': 67.201, '[Potassium glutamate] (mM)': 139.95},
    {'well_id': 'I9', '[DNA] (nM)': 19.0, '[PMix] (mg/mL)': 1.53, '[Magnesium acetate] (mM)': 2.006, '[Creatine phosphate] (mM)': 0.0, '[Potassium glutamate] (mM)': 1.367},
    {'well_id': 'J14', '[DNA] (nM)': 19.0, '[PMix] (mg/mL)': 1.53, '[Magnesium acetate] (mM)': 2.006, '[Creatine phosphate] (mM)': 0.0, '[Potassium glutamate] (mM)': 1.367},
    {'well_id': 'J15', '[DNA] (nM)': 19.0, '[PMix] (mg/mL)': 1.53, '[Magnesium acetate] (mM)': 2.006, '[Creatine phosphate] (mM)': 0.0, '[Potassium glutamate] (mM)': 1.367},
    {'well_id': 'I16', '[DNA] (nM)': 0.0, '[PMix] (mg/mL)': 1.839, '[Magnesium acetate] (mM)': 15.969, '[Creatine phosphate] (mM)': 100.0, '[Potassium glutamate] (mM)': 114.929},
    {'well_id': 'H10', '[DNA] (nM)': 0.0, '[PMix] (mg/mL)': 1.839, '[Magnesium acetate] (mM)': 15.969, '[Creatine phosphate] (mM)': 100.0, '[Potassium glutamate] (mM)': 114.929},
    {'well_id': 'J8', '[DNA] (nM)': 0.0, '[PMix] (mg/mL)': 1.839, '[Magnesium acetate] (mM)': 15.969, '[Creatine phosphate] (mM)': 100.0, '[Potassium glutamate] (mM)': 114.929},
]

from opentrons import protocol_api
import logging
import pandas as pd
import numpy as np

import sys

log = logging.getLogger(__name__)

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
                                         p50, log, well_volume=smix_final_volume, num_mms=1, mix_reps=15,
                                         mm_label="smix", flow_rate=35, volume_scalar=1)[0]

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
