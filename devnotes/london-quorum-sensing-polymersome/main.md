---
# Ensure that this title is the same as the one in `myst.yml`
title: "[Title]"
---

# Overview

Quorum sensing polymersomes' membranes will be made out of diblock copolymers which self-assemble to form a bilayer, similarly to lipids. These polymersomes will be a chassis for genetic circuits responsive to quorum sensing molecules (acyl-homoserine lactone) produced by biofilms and will contain PURE to express these circuits. The polymersomes will also contain X-gal which will be cleaved by beta-galactosidase when AHL is present to produce a visible indigo dye. The polymersomes will be integrated into hydrogel via 3D printing.

## How The Module Works
Polymersomes will be made by phase transfer and will encapsulate PURE and LuxR inducible circuits that express beta-galactosidase. LuxR will activate expression of beta-galactosidase when AHL is present. The polymersomes will also contain X-gal which will be cleaved by beta-galactosidase when expression is activated. These polymersomes will be intergrated into an agarose hydrogel patch that can be placed on a AHL producing biofilm.


:::{figure} ./Gemini_Generated_Image_es1k8oes1k8oes1k.png
:label: fig:module-diagram
:width: 110%
:::

## Milestones


- Create polymersomes encapsulating PURE and compare to lipid GUVs
    - **Risk**: Osmolarity imbalance from PURE causing membrane instability
    - **Success Criteria**: GFP expressing in stable polymersomes
- Integrate polymersomes into hydrogel that is stable for 3-4 hours. Outperforming DOPC standard GUVs in terms of time remaining stable.
    - **Risk**: Polymersomes unstable in hydrogel
    - **Mitigation**: Test different concentrations of hydrogel to assess optimal concentration for polymersome stability
- Insert alpha-hemolysin into polymersome membranes
    - **Risk**: Alpha-hemolysin not inserting
    - **Mitigation**: Test insertion in different polymer compositions
    - **Success Criteria**: Successful calcein leakage assay
- Expressing beta-galactosidase from quorum sensing circuits
    - **Risk**: AHL not diffusing sufficiently through hydrogel into polymersome
    - **Mitigation**: Permeability tests in different polymer compositions
    - **Success Criteria**: Produce X-gal/CPRG color change in polymersomes integrated in hydrogel


:::{table} Components
:label: table-experimental-params
:align: center

| Component | Description |
| --- | --- |
| Diblock copolymer | Energy mix made without folinic acid. |
| PURE  | B.next cytosol |
| Ultra low gelling agarose  | Gels at 8-17C  |
| X-gal | Cleaved by beta-galactosidase into indigo dye |
| LuxR genetic circuits | Provided by Elani lab |

:::



## Experiments
1. Create polymer GUVs using phase transfer and load into agarose hydrogel
2. Polymer screening for best stability in hydrogel
3. Load GUVs with PURE and test polymer stability during expression of GFP control.
4. Assess permeability of quorum sensing molecules in polymer GUVs 
5. Test beta-galactosidase reaction within polymersomes
6. Alpha-hemolysin insertion into polymer membranes to export cleaved X-gal. 
7. Add quorum sensing circuits to GUVs and test with bacterial biofilms.


## References
- Contini, C., Hu, W. & Elani, Y. (2022) Manufacturing polymeric porous capsules. Chemical Communications. 58 (28), 4409–4419. doi:10.1039/D1CC06565C.
- Ioannou, I.A., Monck, C., Ceroni, F., Brooks, N.J., Kuimova, M.K. & Elani, Y. (2024) Nucleated synthetic cells with genetically driven intercompartment communication. Proceedings of the National Academy of Sciences. 121 (36), e2404790121. doi:10.1073/pnas.2404790121.
- Jacobs, M.L., Boyd, M.A. & Kamat, N.P. (2019) Diblock copolymers enhance folding of a mechanosensitive membrane protein during cell-free expression. Proceedings of the National Academy of Sciences. 116 (10), 4031–4036. doi:10.1073/pnas.1814775116.

