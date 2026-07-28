# CRN Ensemble Software Layout

This package reorganizes the project into software-style modules for generating
an ensemble of converging CRN results from spreadsheet inputs.

## Goal

Given an input reaction table (CSV now, Excel-ready structure), build CRNs,
sample reversible/kinetic parameter sets, enforce mass balance, and evaluate
ensemble solutions.

## Package structure

- `build/`: CRN construction from tabular reaction definitions.
- `simulation/`: initial-condition and kinetic simulation helpers.
- `analysis/`: mass-balance and validation utilities.
- `mechanisms/`: mechanism customizations (e.g., reaction-direction changes).
- `ensemble/`: ensemble sampling and parameter generation.
- `inputs/`: place reaction/condition spreadsheet files.

## Notes

Current files are organized copies/shims of existing scripts to provide a clean
software structure without breaking your current top-level workflow.
