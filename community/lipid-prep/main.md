---
abstract: |
  Participants in the Developer Cell Project gathered at the London Exchange Meeting and compared liposome encapsulation protocols across labs, revealing significant variation. Discussions during this meeting will help establish the engineering practice for protocol development within Nucleus and build out a framework of co-existing, category-specific protocols for benchmarking synthetic cell systems.
---

:::{tip} Request for comment

This Developer Note (DevNote) is a work in progress. Please leave comments on the Nucleus Forum thread [here](https://forum.nucleus.engineering/t/london-exchange-liposome-encapsulation-protocol/49). Dialogue there will be used to update and upgrade this DevNote.

:::

# Overview

Participants in the [Developer Cell Project](https://syncellwiki.org/wiki/index.php/Schmidt_Sciences_DevCell_Project) gathered at Imperial College, London for the London Exchange Meeting. This DevNote captures key points that emerged during a discussion
on the usage of the [Base Cell Protocol](https://docs.nucleus.engineering/docs/processes/assemble-base-cell/main/). The Base Cell protocol is an evolution of an earlier effort to create alignment around a liposome preparation [protocol](https://github.com/BuildACell/liposome-kit/blob/master/txtl-liposome_water-in-oil.md) that emerged from the Build a Cell community in 2018. 

A key goal of the Developer cell program is to build an engineering practice that enables the integration of an increasing number of engineered components into synthetic cells. This requires not only the use of community accepted protocols with clearly defined interfaces but also a community practice for modifying and extending standard protocols that evolve as the field matures to address new and greater challenges. The London exchange meeting is an important step in establishing this practice. 

It is clear that advancing the field will require not a singular ideal protocol but rather category-specific protocols that enable benchmarking, along with a [framework](fig:flowchart) for their continued improvement.

# State of Affairs



As it stands, there is significant variation in the protocols used by the members of the collaboration. 

::::{card} Protocol Survey

```{include} highlight.md

```

:::{tip} Original Table
:icon: false
:class: dropdown

```{include} protocol-table.md
```
:::

::::

An ["idealized" protocol](tbl:idealized) was discussed that incorporated common features from the protocols in use following some discussion. 

:::{table} Idealized protocol.
:label: tbl:idealized

| Parameter | Idealized Protocol |
| --- | --- |
| Lipid preparation | Thin film |
| Lipid composition / concentration | POPC:Chol 70:30, 3 mg/mL |
| Oil phase | Bioultra (CAS 8042-47-5) |
| Outer solution | Glucose 0.5 M in DPBS 1X |
| Density medium | 5% Optiprep |
| W/O emulsions | TBD |
| Column conditions | TBD |
| Monolayer incubation | TBD |
| Centrifugation | TBD |
| Temperature | TBD |

:::

# Immediate next steps

We did not have enough time during the exchange meeting to finish defining an 'ideal' protocol. Instead it was agreed to capture the state of affairs and convert the ideas discussed into the present DevNote and continue the work asynchronously. As such the DevNote remains a work in progress. We expect and encourage comments on this DevNote on the associated [Nucleus Forum thread](https://forum.nucleus.engineering/t/london-exchange-liposome-encapsulation-protocol/49). 

## Distributed testing

We recognize that the current protocol may not be perfect but improvements must be rooted in data. DevNotes and the Nucleus Forum provide venues for sharing data that can inform improvements to the protocol - this is data that would normally fall outside of the scope of existing modes of scholarly communication and exists significantly as remembrances. 

An example of this kind of work can be found in a recent [DevNote](https://devnotes.nucleus.engineering/articles/bnext-devnotes-mk0407) by Mary Kelly.

What data would be most useful to share? What benchmarks should be used to compare liposomes across labs, yield or module functionality?

## Assistance from an Integration Node

As the integration node in the DevCells project and maintainers of Nucleus, b.next can play an important role in synthesizing insights from the project and broader community running controlled experiments across protocol variations using a single lab's hands. As a starting point, this may involve evaluating some of the suggestions embodied in the [idealized protocol](tbl:idealized).

What other roles can b.next play as an integration node to support protocol convergence across the project?

# Long term vision

One thing that is clear from discussion is that the solution is not a single protocol but rather a framework for deciding between protocols that are adapted to specific use cases. 

:::{figure} flowchart.svg
:label: fig:flowchart

:::

The base cell protocol is an important first step to enable benchmarking across labs. However, it may need to be adapted to produce liposomes that can be incorporated in a specific hydrogel. Since the [Chicago](https://devnotes.nucleus.engineering/articles/bnext-devnotes-chicago-demo-1) and [London](https://devnotes.nucleus.engineering/collections-devcell-node-london) Node demonstration projects both involve embedding synthetic cells into hydrogels, there is an opportunity to define the relevant benchmarking protocol.


Similarly, it may be the case that tweaking lipid composition is needed for incorporating different membrane proteins. In this case, it may be useful to define a panel of membrane specifications that are used representing specific physico-chemical properties such as charge, stiffness, or thickness that go beyond the existing [Base Membrane Specification](https://docs.nucleus.engineering/docs/modules/membrane-popc-chol/spec/) based on POPC and cholesterol used in the Base Cell Protocol. 

**Participants of the London Exchange Meeting**: Michael Booth (University College, London), Samuel Chen (University of Michigan), Oscar Cees (Imperial College, London), Claudia Contini (Imperial College, London), Yuval Elani (Imperial College, London), Sung-Won Hwang (University of Michigan), Anton Jackson-Smith (b.next), Mary Kelly (Northwestern University), Matthew Lucia (Northwestern University), Akshay Maheshwari (b.next), Jonah McDonald (King's College, London), Niall McIntyre (Imperial College, London), Anton Molina (b.next), Richard Murray (Schmidt Sciences), Charlie Newell (University College, London), Ojaswita Pant (Northwestern University), Julia Purrinos De Oliveira (Imperial College, London), Surendra Yadav (b.next)
