"""
DOE (Design of Experiments) QC & Analysis
==========================================
Quality control and diagnostic tools for LHC / DOE
discovery plate experiments.

Functions
---------
qc_summary
    Print data quality overview; return clean/failed splits.
plot_replicate_agreement
    Assess replicate consistency via CV per condition.
plot_plate_heatmap
    384-well plate layout heatmap for any metric.
plot_qc_overview
    Multi-panel QC dashboard.
"""

import math
import re
import string
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import pandas as pd
import seaborn as sns


# ── Well ID parsing ─────────────────────────────────────


_ROW_LABELS = list(string.ascii_uppercase[:16])  # A-P
_COL_LABELS = list(range(1, 25))  # 1-24
_ROW_MAP = {letter: i for i, letter in enumerate(_ROW_LABELS)}


def _parse_well(well_id: str) -> tuple[int, int]:
    """Parse a well ID like 'E5' into (row_idx, col_idx).

    Returns
    -------
    tuple of (int, int)
        Zero-based (row, col) indices for a 384-well plate.
    """
    match = re.match(
        r"^([A-P])(\d{1,2})$", str(well_id).strip()
    )
    if match is None:
        raise ValueError(f"Cannot parse well ID: {well_id!r}")
    row = _ROW_MAP[match.group(1)]
    col = int(match.group(2))
    if col < 1 or col > 24:
        raise ValueError(f"Column out of range: {well_id!r}")
    return row, col - 1  # zero-based


# ── QC Summary ───────────────────────────────────────────


def qc_summary(
    df: pd.DataFrame,
    factors: list[str],
    responses: list[str],
    fit_col: str = "Fit_R^2",
    good_fit_col: str = "Fit_good_fit",
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Print data quality overview and split into clean/failed.

    Parameters
    ----------
    df : pd.DataFrame
        Per-well DOE results with factor concentrations,
        response metrics, and fit quality columns.
    factors : list of str
        Column names of DOE factor variables.
    responses : list of str
        Column names of response metrics.
    fit_col : str, default "r_squared"
        Column containing the goodness-of-fit metric.
    good_fit_col : str, default "good_fit"
        Boolean column indicating whether a fit passed QC.

    Returns
    -------
    clean_df : pd.DataFrame
        Rows where ``good_fit_col`` is True.
    failed_df : pd.DataFrame
        Rows where ``good_fit_col`` is False.
    """
    total = len(df)
    good = df[good_fit_col].sum()
    bad = total - good

    print("=" * 50)
    print("DOE QC Summary")
    print("=" * 50)
    print(f"  Total wells:  {total}")
    print(f"  Good fits:    {good} ({100 * good / total:.1f}%)")
    print(f"  Failed fits:  {bad} ({100 * bad / total:.1f}%)")

    # Fit quality details
    if fit_col in df.columns:
        neg_r2 = (df[fit_col] < 0).sum()
        low_r2 = ((df[fit_col] >= 0) & (df[fit_col] < 0.9)).sum()
        print(f"\n  R² < 0:       {neg_r2}")
        print(f"  0 ≤ R² < 0.9: {low_r2}")

    # Per-response summary (good fits only)
    clean = df[df[good_fit_col]].copy()
    failed = df[~df[good_fit_col]].copy()

    print("\n  Response metrics (good fits only):")
    for resp in responses:
        if resp in clean.columns and len(clean) > 0:
            vals = clean[resp]
            print(
                f"    {resp:30s}  "
                f"min={vals.min():.4f}  "
                f"median={vals.median():.4f}  "
                f"max={vals.max():.4f}"
            )

    # Check if failures cluster in factor space
    if len(failed) > 0:
        print(f"\n  Factor ranges for FAILED wells:")
        for f in factors:
            if f in failed.columns:
                print(
                    f"    {f:30s}  "
                    f"[{failed[f].min():.3f} – "
                    f"{failed[f].max():.3f}]"
                )

    print("=" * 50)
    return clean, failed


# ── Replicate Agreement ──────────────────────────────────


def plot_replicate_agreement(
    df: pd.DataFrame,
    condition_col: str,
    responses: list[str],
    cv_threshold: float = 0.5,
    save_path: str | Path | None = None,
    show: bool = True,
    hue = None
) -> plt.Figure:
    """Assess replicate consistency via CV per condition.

    For each response, shows:
    - Left: strip plot of individual replicates per condition,
      ordered by condition mean.
    - Right: histogram of CV across conditions, with a
      threshold line highlighting poor reproducibility.

    Parameters
    ----------
    df : pd.DataFrame
        Per-well data with a condition identifier column
        and response metric columns.
    condition_col : str
        Column grouping replicates (e.g. "conditions").
    responses : list of str
        Response metric columns to assess.
    cv_threshold : float, default 0.5
        CV values above this are flagged as high-variance.

    Returns
    -------
    matplotlib.figure.Figure
    """
    n = len(responses)
    fig, axes = plt.subplots(
        n, 2, figsize=(14, 3.5 * n), squeeze=False
    )

    for row, resp in enumerate(responses):
        # -- Compute stats per condition --
        stats = (
            df.groupby(condition_col)[resp]
            .agg(["mean", "std", "count"])
            .reset_index()
        )
        stats["cv"] = stats["std"] / stats["mean"].abs()
        stats["cv"] = stats["cv"].replace(
            [np.inf, -np.inf], np.nan
        )

        # -- Left panel: strip plot --
        ax_strip = axes[row, 0]
        order = stats.sort_values("mean")[condition_col].values
        sns.stripplot(
            data=df,
            x=condition_col,
            y=resp,
            order=order,
            size=4,
            alpha=0.7,
            jitter=True,
            ax=ax_strip,
            hue=hue
        )
        ax_strip.set_title(f"{resp} — replicates per condition")
        ax_strip.set_xlabel("condition (ordered by mean)")
        ax_strip.tick_params(
            axis="x", labelbottom=False, bottom=False
        )

        # -- Right panel: CV histogram --
        ax_cv = axes[row, 1]
        cv_vals = stats["cv"].dropna()
        n_high = (cv_vals > cv_threshold).sum()
        n_total = len(cv_vals)

        ax_cv.hist(
            cv_vals, bins=20, color="steelblue",
            edgecolor="white", alpha=0.8,
        )
        ax_cv.axvline(
            cv_threshold, color="red", linestyle="--",
            label=f"threshold={cv_threshold}",
        )
        ax_cv.set_title(
            f"{resp} — CV distribution "
            f"({n_high}/{n_total} above threshold)"
        )
        ax_cv.set_xlabel("Coefficient of Variation")
        ax_cv.set_ylabel("# conditions")
        ax_cv.legend(fontsize=8)

    fig.tight_layout()
    if save_path is not None:
        fig.savefig(
            save_path, dpi=150, bbox_inches="tight"
        )
    if show:
        plt.show()
    return fig


# ── Plate Heatmap ────────────────────────────────────────


def plot_plate_heatmap(
    df: pd.DataFrame,
    well_col: str,
    value_col: str,
    plate_rows: int = 16,
    plate_cols: int = 24,
    cmap: str = "viridis",
    title: str | None = None,
    ax: plt.Axes | None = None,
    save_path: str | Path | None = None,
    show: bool = True,
) -> plt.Figure:
    """Render a 384-well plate layout heatmap.

    Parameters
    ----------
    df : pd.DataFrame
        Must contain ``well_col`` (e.g. "E5") and
        ``value_col`` (numeric metric to visualize).
    well_col : str
        Column with well IDs (e.g. "Well").
    value_col : str
        Column with numeric values to color-map.
    plate_rows : int, default 16
        Number of plate rows (A-P for 384).
    plate_cols : int, default 24
        Number of plate columns (1-24 for 384).
    cmap : str, default "viridis"
        Matplotlib colormap name.
    title : str or None
        Figure title. Defaults to ``value_col``.
    ax : matplotlib.axes.Axes or None
        Axes to draw on. If None, creates a new figure.

    Returns
    -------
    matplotlib.figure.Figure
    """
    # Build the plate grid (NaN = empty)
    plate = np.full((plate_rows, plate_cols), np.nan)
    for _, row in df.iterrows():
        try:
            r, c = _parse_well(row[well_col])
            plate[r, c] = row[value_col]
        except (ValueError, KeyError):
            continue

    _standalone = ax is None  # capture before ax is reassigned
    if _standalone:
        fig, ax = plt.subplots(figsize=(14, 6))
    else:
        fig = ax.get_figure()

    # Mask NaN for distinct empty-well color
    masked = np.ma.masked_invalid(plate)
    cmap_obj = plt.colormaps[cmap].copy() if hasattr(plt, 'colormaps') else plt.get_cmap(cmap).copy()
    cmap_obj.set_bad(color="0.90")

    im = ax.imshow(
        masked, cmap=cmap_obj, aspect="auto",
        interpolation="nearest",
    )
    # Pin axis limits so the full plate grid always shows,
    # regardless of colorbar creation or tight_layout shifts.
    ax.set_xlim(-0.5, plate_cols - 0.5)
    ax.set_ylim(plate_rows - 0.5, -0.5)  # inverted: row A at top

    fig.colorbar(im, ax=ax, shrink=0.7, label=value_col)
    # Re-assert after colorbar creation, which can reset aspect in newer matplotlib
    ax.set_aspect('auto')
    ax.set_xlim(-0.5, plate_cols - 0.5)
    ax.set_ylim(plate_rows - 0.5, -0.5)

    # Axis labels
    row_labels = _ROW_LABELS[:plate_rows]
    col_labels = [str(c) for c in _COL_LABELS[:plate_cols]]
    ax.set_xticks(range(plate_cols))
    ax.set_xticklabels(col_labels, fontsize=7)
    ax.set_yticks(range(plate_rows))
    ax.set_yticklabels(row_labels, fontsize=8)
    ax.set_xlabel("Column")
    ax.set_ylabel("Row")
    ax.set_title(title or value_col)

    if _standalone:
        fig.tight_layout()
    if save_path is not None:
        fig.savefig(
            save_path, dpi=150, bbox_inches="tight"
        )
    if show and _standalone:
        plt.show()

    return fig


# ── QC Overview ──────────────────────────────────────────


def plot_qc_overview(
    df: pd.DataFrame,
    factors: list[str],
    responses: list[str],
    # good_fit_col: str = "good_fit",
    # fit_col: str = "r_squared",
    fit_col: str = "Fit_R^2",
    good_fit_col: str = "Fit_good_fit",
    well_col: str = "Well",
    save_path: str | Path | None = None,
    show: bool = True,
) -> plt.Figure:
    """Multi-panel QC dashboard.

    Panel layout:
    - Top-left: R² histogram with threshold line.
    - Top-right: plate heatmap of the first response.
    - Bottom: factor pairplot colored by good_fit flag
      (where in factor space do failures cluster?).

    Parameters
    ----------
    df : pd.DataFrame
        Per-well DOE results.
    factors : list of str
        DOE factor column names.
    responses : list of str
        Response metric column names.
    good_fit_col : str, default "good_fit"
        Boolean fit-quality column.
    fit_col : str, default "r_squared"
        Goodness-of-fit metric column.
    well_col : str, default "Well"
        Well identifier column for plate heatmap.

    Returns
    -------
    matplotlib.figure.Figure
    """
    # -- Top row: R² histogram + plate heatmap --
    fig_top, (ax_r2, ax_plate) = plt.subplots(
        1, 2, figsize=(16, 5)
    )

    # R² histogram
    if fit_col in df.columns:
        r2_clean = df[fit_col].clip(lower=-1)
        ax_r2.hist(
            r2_clean, bins=30, color="steelblue",
            edgecolor="white", alpha=0.8,
        )
        ax_r2.axvline(
            0.95, color="green", linestyle="--",
            label="R²=0.95",
        )
        ax_r2.axvline(
            0, color="red", linestyle="--",
            label="R²=0",
        )
        ax_r2.set_xlabel("R²")
        ax_r2.set_ylabel("# wells")
        ax_r2.set_title("Fit Quality (R² distribution)")
        ax_r2.legend(fontsize=8)

    # Plate heatmap of first response
    primary = responses[0] if responses else None
    if primary and well_col in df.columns:
        plot_plate_heatmap(
            df, well_col, primary,
            title=f"Plate: {primary}", ax=ax_plate,
        )
    else:
        ax_plate.set_visible(False)

    fig_top.tight_layout()

    # Resolve save paths for two-figure output
    _sp = Path(save_path) if save_path is not None else None
    if _sp is not None:
        fig_top.savefig(
            _sp.with_name(f"{_sp.stem}_summary{_sp.suffix}"),
            dpi=150,
            bbox_inches="tight",
        )
    if show:
        plt.show()
    
    # -- Bottom: factor scatter matrix colored by fit --
    if good_fit_col in df.columns and len(factors) >= 2:
        plot_df = df[factors + [good_fit_col]].copy()
        # plot_df["fit_quality"] = plot_df[good_fit_col].map(
        #     {True: "good", False: "FAILED"}
        # )
        # palette = {"good": "steelblue", "FAILED": "red"}
        g = sns.pairplot(
            plot_df,
            hue="Steady_State_data_normalized",
            palette="viridis", #palette,
            vars=factors,
            diag_kind="hist",
            plot_kws={"alpha": 0.6, "s": 30},
            height=2.5,
        )
        g.figure.suptitle(
            "Factor Space — Failures in Red", y=1.02
        )
        if _sp is not None:
            g.figure.savefig(
                _sp.with_name(
                    f"{_sp.stem}_factors{_sp.suffix}"
                ),
                dpi=150,
                bbox_inches="tight",
            )
        if show:
            plt.show()
        return g.figure

    return fig_top
