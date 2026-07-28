import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.inspection import PartialDependenceDisplay
import matplotlib.pyplot as plt
import shap


def fit_RF(X, y):
    rf = RandomForestRegressor(n_estimators=500, random_state=42)
    rf.fit(X, y)
    return rf

def plot_importances(rf, factors):
    imp = pd.Series(rf.feature_importances_, index=factors).sort_values(ascending=True)

    fig, ax = plt.subplots(figsize=(6, 4))
    imp.plot.barh(ax=ax, color='steelblue')
    ax.axvline(1/len(factors), color='red', linestyle='--', label='random baseline')
    ax.set_xlabel("Feature importance")
    ax.set_title("Which factors drive response?")
    ax.legend()
    plt.tight_layout()
    plt.show()

def plot_pdd(rf, X, factors):
    fig, axes = plt.subplots(1, len(factors), figsize=(16, 4), sharey=True)
    PartialDependenceDisplay.from_estimator(
        rf, X,
        features=list(range(len(factors))),
        feature_names=factors,
        ax=axes,
        line_kw={'color': 'steelblue', 'linewidth': 2},
    )
    for ax, f in zip(axes, factors):
        ax.set_title(f, fontsize=9)
        ax.set_xlabel('')
    axes[0].set_ylabel(response_col)
    fig.suptitle("Partial Dependence — marginal effect of each factor")
    plt.tight_layout()
    plt.show()

def get_shap(rf, X, y, factors, factor_labels=None, well_labels=None,
             response_col='response', waterfall_well=None,
             figsize_summary=(10, 5), figsize_waterfall=(8, 5)):
    """
    Parameters
    ----------
    waterfall_well : str or None
        Well ID to show in the waterfall plot (e.g. "G12").
        If None, defaults to the top-scoring well.
    factor_labels : list of str or None
        Short display names for factors, same order as `factors`.
        E.g. ["PMix (mg/mL)", "DNA (nM)", "Mg (mM)", "K (mM)", "CP (mM)"]
        If None, `factors` column names are used as-is.
    """
    display_names = factor_labels if factor_labels is not None else factors

    explainer = shap.TreeExplainer(rf)
    shap_values = explainer.shap_values(X)

    shap_df = pd.DataFrame(shap_values, columns=display_names)
    if well_labels is not None:
        shap_df['Well'] = well_labels
    shap_df[response_col] = y

    # Summary plot
    shap.summary_plot(shap_values, X, feature_names=display_names, show=False)
    plt.gcf().set_size_inches(*figsize_summary)
    plt.tight_layout()
    plt.show()

    # Waterfall — pick well by ID or fall back to top scorer
    if waterfall_well is not None and well_labels is not None:
        well_arr = list(well_labels)
        if waterfall_well not in well_arr:
            raise ValueError(
                f"Well '{waterfall_well}' not found. "
                f"Available: {well_arr}"
            )
        idx = well_arr.index(waterfall_well)
    else:
        idx = int(y.argmax())
        if well_labels is not None:
            print(f"Showing waterfall for top well: {list(well_labels)[idx]}")

    well_name = list(well_labels)[idx] if well_labels is not None else f"index {idx}"
    shap.waterfall_plot(
        shap.Explanation(
            values=shap_values[idx],
            base_values=explainer.expected_value,
            data=X[idx],
            feature_names=display_names,
        ),
        show=False,
    )
    plt.gca().set_title(
        f"SHAP Waterfall — Well {well_name}  "
        f"({response_col} = {y[idx]:.3f})",
        fontsize=11, pad=10,
    )
    plt.gcf().set_size_inches(*figsize_waterfall)
    plt.tight_layout()
    plt.show()

    return shap_df

if __name__ == "__main__":
    kin = pd.read_csv("kinetic_fits.csv")
    factors = ['[PMix]_(mg/mL)','[DNA]_(nM)','[Magnesium_acetate]_(mM)','[Potassium_glutamate]_(mM)','[Creatine_phosphate]_(mM)']
    factor_labels = ['PMix (mg/mL)', 'DNA (nM)', 'Mg (mM)', 'K (mM)', 'CP (mM)']
    response_col = 'Steady_State_data_normalized'

    good = kin.dropna(subset=factors + [response_col])
    X = good[factors].values
    y = good[response_col].values

    rf = fit_RF(X, y)
    # plot_importances(rf, factors)
    # plot_pdd(rf, X, factors)
    get_shap(rf, X, y, factors,
             factor_labels=factor_labels,
             well_labels=good['Well'].values if 'Well' in good.columns else None,
             response_col=response_col,
             waterfall_well=None,   # e.g. "G12" to inspect a specific well
             )
