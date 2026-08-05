---
abstract: |
  We optimized the inner solution, lipid concentration, and lipid composition to identify conditions that achieved the highest yield of giant unilamellar vesicles (GUVs) using an inverted emulsion method. Our results indicate that higher sucrose concentrations, increased lipid concentration, and the incorporation of cholesterol enhance GUV yield.
---

# Overview

To achieve bulk material production, it is necessary to optimize GUV formation using the double emulsion method to minimize waste of cell-free components during encapsulation. In this protocol, we investigate inner solutions supplemented with OptiPrep, 200 mM sucrose, and 400 mM sucrose; lipid concentrations of 1 mM, 10 mM, and 20 mM; and GUV compositions of 100% POPC, 90:10 POPC:cholesterol, and 2:1 cholesterol:POPC.

:::{figure} ./double-emulsion.jpg
:label: double-emulsion-method
:width: 20%

Double emulsion method: "Double emulsion method [](10.1126/sciadv.add6605)"
:::


# Results

## Inner solution optimization

The following lipids in chloroform were used to prepare films:

:::{table}
:label: lipid-stocks
:align: center

Lipids for thin film preparation

| Ampiphile | MW (g/mol)| Stock (mg/mL) | Stock (mM) |
| --- | --- | --- | --- |
| POPC | 760.091 | 25 | 32.9 |
| Cholesterol (ovine)  | 386.7 | 19.3 | 50 |
| 18:1 Liss Rhod PE | 1301.7 | 1 | 0.77 |

:::

These lipids were added in chloroform to the bottom of a glass vial (one per reaction condition).

:::{table}
:label: lipid-films
:align: center

Film Preparation

| Name | Mole Ratio | | | Conditions | | Volume (uL) | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| | POPC | Chol | Rhod | Volume (uL) | Molarity (mM) | POPC | Chol | Rhod |
| 100% POPC | 99.9 | 0 | 0.1 | 200 | 20 | 121.5 | 0 | 5.2 |
| 9:1 POPC:Chol | 89.9 | 10 | 0.1 | 200 | 20 | 109.3| 8 | 5.2 |
| 2:1 Chol:POPC | 33.3 | 66.6 | 0.1 | 200 | 20 | 40.5 | 53.3 | 5.2 |

:::

Steps for oil/lipid mixture preparation are as follows:
1)	Dry down under nitrogen gas until a thin film has formed across the bottom. Place in vacuum oven overnight (or at least a few hours). 
2)	Add 200 uL of BioUltra mineral oil on top of the film. Vortex mixture briefly, then heat for 30 min at 80 C using a hot plate. 
3)	Vortex ~5-10 seconds. If lipid has not dissolved into the oil keep on heat plate for another 10 minutes. Repeat until no film is visible on the vial.
4)	Cool lipid/oil mixture on ice.

For this initial experiment changing the inner solution, we used 3 100% POPC films. We varied the inner solution in the double emulsion protocol as follows:

:::{table}
:label: inner-solution
:align: center

Inner solution formulation

| Stock Solution | Optiprep (uL)| 200 mM Sucrose (uL) | 400 mM Sucrose (uL) |
| --- | --- | --- | --- |
| B.Next Pure | 16.2 | 16.2 | 16.2 |
| Optiprep  | 0.67 | 0 | 0 |
| Sucrose (2M) | 0 | 2 | 3.8 |
| H2O  | 3.14 | 1.8 | 0 |
| Total  | 20 | 20 | 20 |

:::

The corresponding outer solution for each condition was prepared as follows:

:::{table}
:label: outer-solution
:align: center

Outer solution formulation

| Stock Solution | Optiprep (uL)| 200 mM Sucrose (uL) | 400 mM Sucrose (uL) |
| --- | --- | --- | --- |
| Glucose (2M) | 550 | 100 | 200 |
| HEPES (1M)  | 0 | 900 | 800 |
| H2O | 450 | 0 | 0 |
| Total  | 1000 | 1000 | 1000 |

:::

The double emulsion was assembled and imaged as follows:
1)	Add 20 uL of inner solution to cold lipid/oil mixture
2)	Vortex for 30 seconds. Incubate on ice for 5 minutes to stabilize.
3)	Carefully layer emulsion on top of 100 uL outer solution.
4)	Incubate on ice 5 minutes to allow interface to stabilize.
5)	Block glass slides with 2 w/v% BSA for at least 20 min.
6)	Centrifuge at 18,000 rcf at 4C for 15 minutes
7)  Remove as much mineral oil from the top as possible. Using a fresh pipette tip, collect the vesicle pellet from the bottom of the tube. 
    Note: Optiprep and 200 mM sucrose conditions did not have a visible pellet. 400mM sucrose had a visible pellet.
8)	Resuspend liposomes in 100 uL of outer solution.
9)	Remove BSA from all wells and image the liposomes on glass slides.

:::{figure} ./GUVs-Inner-solution.jpg
:label: GUVs-inner-solution
:width: 75%

Representative images of vesicles prepared using Optiprep (left), 200 mM Sucrose (middle), and 400 mM Sucrose (right). Highest yield of GUVs occurred using an inner solution containing 400 mM Sucrose.
:::

## Comparision of lipid concentrations and compositions

For this section, we prepared varying lipid concentrations and compositions and compared the resulting GUV yield and size. GUVs were prepared with lipid compositions described in {numref}`lipid-films` with the 400 mOsm inner solution and outer solution previously described in {numref}`inner-solution` and {numref}`outer-solution`.

:::{figure} ./Composition-concentration-images.jpg
:label: Composition-concentration-images
:width: 75%

Representative images of GUV 10 mM lipid in oil (top row) and 20 mM lipid in oil (bottom row). GUVs with 1 mM lipid concentration in oil did not form.
:::

Images were manually quantified to determine count and GUV size.

:::{figure} ./GUV-count.jpg
:label: GUV-count
:width: 50%

Quantification of the number of GUVs per ROI using varying lipid concentration and compoition. Increasing lipid concentration increased the number of GUVs and addition of cholesterol seemed to increase number of GUVs. 2:1 Chol:POPC GUVs had increased variability compared to other compositions.
:::

:::{figure} ./GUV-diameter.jpg
:label: GUV-diameter
:width: 50%

Quantification of the diameter of GUVs using varying lipid concentration and compoition. Increasing lipid concentration increases GUV diameter.
:::

# Conclusions

In this Developer Note we've discussed a few important points for optimizing GUV production:

- 400 mOsm inner solution increased vesicle yield
- Cholesterol was beneficial for vesicle yield and increased lipid concentration increased GUV size and yield 

