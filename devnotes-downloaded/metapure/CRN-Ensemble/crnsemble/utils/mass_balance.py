"""
Stoichiometry matrix A and net flux vector v from a biocrnpyler CRN.

Uses crn.species for row ordering and crn.reactions for columns.
For each elementary reaction j, the net flux is v_j = v_forward - v_reverse from
crn.all_fluxes (reactions not listed there contribute zero flux).

Steady-state mass balance: A @ v ≈ 0 (species that are not true sources/sinks
should have negligible residuals if fluxes are consistent).
"""

from __future__ import annotations

from typing import Any, Optional, Tuple

import numpy as np

import crnsemble.build.generate_crn as generate_crn
try:
    import pandas as pd
except ImportError:  # pragma: no cover
    pd = None


def species_index_map(crn) -> Tuple[dict, list]:
    """Map each Species object to row index; return (idx_map, ordered species list)."""
    species_list = list(crn.species)
    idx_map = {sp: i for i, sp in enumerate(species_list)}
    return idx_map, species_list


def stoichiometry_matrix(crn) -> Tuple[np.ndarray, list]:
    """
    Build A with shape (n_species, n_reactions): d/dt x ≈ A @ v.

    Reactants (inputs) contribute negative stoichiometry; products positive.
    """
    idx_map, _ = species_index_map(crn)
    n_s = len(crn.species)
    n_r = len(crn.reactions)
    A = np.zeros((n_s, n_r), dtype=float)

    # for A_r in range(n_s):

    #     for A_c in range(n_r):

    #         rxn = crn.reactions[A_c]

    #         for w in rxn._input_complexes:
    #             sp = w.species

    #                 A[A_r, A_c] = sp.stoichiometry
                


    for j, rxn in enumerate(crn.reactions):

        if j == 14:
            print('stop')
        for w in rxn._input_complexes:
            sp = w.species
            # if sp not in idx_map:
            #     raise KeyError(f"Reactant species {getattr(sp, 'name', sp)} not in crn.species")
            A[idx_map[sp], j] -= float(w.stoichiometry)
        for w in rxn._output_complexes:
            sp = w.species
            # if sp not in idx_map:
            #     raise KeyError(f"Product species {getattr(sp, 'name', sp)} not in crn.species")
            A[idx_map[sp], j] += float(w.stoichiometry)

    names = [sp.name for sp in crn.species]
    return A, names


def net_flux_vector(
    crn,
    all_fluxes: Optional[Any] = None,
) -> np.ndarray:
    """
    Full-length net flux v (length n_reactions): v_j = v_forward - v_reverse.

    Uses crn.all_fluxes if all_fluxes is None. Index must be elementary
    reaction indices (same enumeration as crn.reactions).
    """
    if all_fluxes is None:
        all_fluxes = getattr(crn, "all_fluxes", None)
    if all_fluxes is None:
        raise AttributeError("crn.all_fluxes is missing; run build_elementary_fluxes first or pass a DataFrame.")

    n_r = len(crn.reactions)
    v = np.zeros(n_r, dtype=float)

    if pd is not None and isinstance(all_fluxes, pd.DataFrame):
        for elem_id, row in all_fluxes.iterrows():
            j = int(elem_id)
            if j < 0 or j >= n_r:
                raise IndexError(f"elem_rxn_id {j} out of range for crn.reactions (n={n_r})")
            vf = float(row["v_forward"])
            vr = float(row["v_reverse"])
            v[j] = vf - vr
    else:
        raise TypeError("all_fluxes must be a pandas DataFrame with v_forward and v_reverse columns")

    return v


def mass_balance_residual(
    crn,
    all_fluxes: Optional[Any] = None,
    atol: float = 1e-9,
    rtol: float = 1e-9,
) -> dict:
    """
    Compute r = A @ v and report whether |r| is small per entry (combined tolerance).

    Returns dict with keys: A, v, residual (r), species_names, max_abs_residual, ok
    """
    A, species_names = stoichiometry_matrix(crn)
    v = net_flux_vector(crn, all_fluxes=all_fluxes)
    r = A @ v
    max_abs = float(np.max(np.abs(r))) if r.size else 0.0
    ok = bool(np.allclose(r, 0.0, atol=atol, rtol=rtol))
    return {
        "A": A,
        "v": v,
        "residual": r,
        "species_names": species_names,
        "max_abs_residual": max_abs,
        "ok": ok,
    }


def assert_mass_balance(
    crn,
    all_fluxes: Optional[Any] = None,
    atol: float = 1e-9,
    rtol: float = 1e-9,
) -> None:
    """Raise AssertionError if A @ v is not near zero within tolerances."""
    out = mass_balance_residual(crn, all_fluxes=all_fluxes, atol=atol, rtol=rtol)
    if not out["ok"]:
        mask = ~np.isclose(out["residual"], 0.0, atol=atol, rtol=rtol)
        bad = np.where(mask)[0]
        lines = [
            f"{out['species_names'][i]}: residual={out['residual'][i]}"
            for i in bad[:20]
        ]
        extra = "" if len(bad) <= 20 else f" ... and {len(bad) - 20} more"
        raise AssertionError(
            f"Mass balance failed (max |A@v| = {out['max_abs_residual']}). "
            f"Examples: {'; '.join(lines)}{extra}"
        )
    else:
        print("Mass balance is conserved")

# Example usage
if __name__ == "__main__":
    # Define species

    reaction_net_data = 'Reaction-network2.csv'

    # reaction_net_data = 'RN_test.csv'

    init_data = 'species_initial_concentrations.csv'

    # reaction_mat_data = csv_to_components(reaction_net_data)

    crn = generate_crn.generate_crn(reaction_net_data, init_data)

    assert_mass_balance(crn)