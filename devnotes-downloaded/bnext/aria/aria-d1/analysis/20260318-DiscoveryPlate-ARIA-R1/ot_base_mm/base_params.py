# Metadata for pure
from bnext_local.instrument.opentrons.helper.custom_classes import Reagent

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

