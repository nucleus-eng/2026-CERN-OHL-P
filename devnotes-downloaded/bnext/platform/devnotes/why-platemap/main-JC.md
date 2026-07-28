---
abstract: |
  How do you join experimental variables and measurements together in a reliable way for sharing and analysis? In this DevNote we'll discuss a common format for sharing data and introduce the concept of a _platemap_ for building these datasets: a table that indicates all relevant metadata for wells in a multiwell plate. We'll show how easy it is to build a platemap and how the metadata can be useful in your analysis.
---


<!-- 
- Sharing data -- we need a standard 
- Long vs wide data format
-->

# Parable of the data
Here's a common enough scenario: you've collected some data from an experiment, and you want to analyze it. 

First, you have to associate the measurements with the variables or experimental conditions. Maybe you store the results in a spreadsheet, with one row or column according for each condition. Or, maybe you have a data file from an instrument, which you load into a Jupyter notebook, and you save the condition information into another variable.


Now you want to compare the results to data you collected previously, maybe on a different instrument, or to data a collaborator has collected. In order to do that, you want to understand when the experimental conditions were the same or different. The different datasets are all stored in files in different formats, and in order to join them all together, you end up having to come up with some specialized workflow for each one separately. Only after many hours of agonizing wrangling are you ready to start the actual analysis. 

One step we can take to make our lives a little easier is to use common standards in formatting data. With predictable structure, it becomes much easier to handle datasets.


In this DevNote, we'll introduce the _platemap_ for annotating multiwell plate data, and show you how you can use it to improve your analysis workflow.

(representation)=
# Representing experimental data

At the end of the day, experimental results are _measurements_ or _observations_ that are associated with experimental _variables_ or _conditions_. So, a natural way to represent results is to put them in a table. A common convention is to have each result be a _row_ in the table and to indicate all of the experimental conditions in the columns. When there are many observations from the same experimental condition—for example, time series data or different modalities of measurement—then we can list each of those as a separate row, noting that the values in the columns representing shared conditions between the observations will be duplicated. 

:::{note}
This is known as the ["long"](https://data.europa.eu/apps/data-visualisation-guide/wide-versus-long-data) data format.
:::

When you are recording data from an experiment, typically you don't need to include _all_ of the information about experimental conditions, but a smaller subset of _identifiers_ that you can pair up with the full set of conditions later. If you are using an instrument to make measurements, there may even be no way to include all of the condition information! 

So, to aid us in correctly associating the full set of experimental conditions with the data (and to make the full "long" data table), we can make a smaller table that just pairs the identifiers with the experimental conditions. Since many biological experiments are conducted using multiwell plates, we call this smaller table a _platemap_.

<!-- Logic: Okay this answers why to use a common standard, but why should you have a platemap?

- Data come from an instrument
- You want to do analysis, and maybe you want to compare different experiments, how?
- Platemap tells you what's in what well, and you can associate that easily with the data
- Platemap combines unique experiment information (Well, Date, Experiment) with your relevant metadata (Conditions)
- For analysis, if you want to understand the differences between experiment, then you need to know what makes the experiments different!! -->

# How to make a platemap

Simply put, a platemap tells you what's in a multiwell plate. <!-- A platemap is a table—it has rows and columns.[^confusion]--> Each row represents one well of the plate, and the columns represent different types of data that describe what's in the wells. 

A properly formatted platemap has **five** _required_ columns that identify each well so that it can be associated with experimental measurements, which can then also be compared to past and future measurements: `Well`, `Date`, `Experiment`, `Name` and `Type`. 

It may have an additional, unrestricted number of optional columns that provide information about the experimental conditions.

See the box below for an example.

:::{tip} Tips
- The relative ordering of rows and columns is not important.
- For ease of use, platemaps should be saved in a common table format like a `*.csv` (comma-separated) or `*.tsv` (tab-separated) file.
- The simplest way to make a platemap is in a spreadsheet editor, like Google Sheets, Microsoft Excel or Numbers for Mac, and exporting the file as a `*.csv` or `*.tsv`.
:::


:::::{important} Example
:label: platemap-example

Here is a simple example for a small plate with 6 wells:

```{figure} assets/simple-plate.svg
:label: simple_plate
:alt: Schematic of a plate with 6 wells
:align: center

A very simple 6 well plate with 3 samples of Cytosol (expressing deGFP; green circles) and 3 replicates of a fluorescein standard (white circles), which can be described by the platemap in @simple_platemap.
```

::::{table} An example platemap corresponding to @simple_plate. In addition to the five required columns, we have added some informative optional columns that indicate the concentration of standard, the reporter type, and the total volume in each well.
:label: simple_platemap

:::{include} assets/simple-platemap.txt
:::

::::
:::::

## Required columns
Four of the required columns serve to uniquely identify the contents of each well across experiments in a dataset:
- `Well`: the alphanumeric coordinate of the well (e.g., A1, B2)
- `Date`: the date the experiment was conducted

:::{caution} Formatting dates
:class: dropdown
Use a (human- and) machine-readable format that at the minimum includes month, day and year, like `yyyy-mm-dd`. Avoid formats like `mm/dd/yy` or `dd/mm/yy` that can cause confusion due to differences in use by country.
:::

- `Experiment`: a name briefly describing the experiment <!--, which can be used as a cross-reference for more metadata-->
- `Name`: a brief description of the contents of the well

:::{tip}
For performing statistics, it's useful to have all replicates have _identical_ `Name`s.
:::

The fifth required column, `Type`, is not an identifier but indicates the role of this well in this experiment. `Type` should be one of
   - `Sample`
   - `Standard` or `Blank`
   - `Control`, `Positive Control` or `Negative Control`

When using the CDK, `Type` indicates what kinds of analyses are relevant to each well.

:::{seealso} Designing your experiment
See our forthcoming DevNotes on (i) why you need standards for your plate reader experiments; and (ii) adding proper controls.
:::

## Optional columns
A platemap may also have any number of additional, optional columns that provide useful metadata about the contents of the wells. For example:
- ID or lot number
- Concentration
- Volume
  
Other columns you might want to add include useful categories for filtering results, such as fluorophore/reporter type, or information about experimental conditions or design that would be informative when sharing your data. See @column-example below for an example.

<!-- :::{aside} The Developer Cell
You may recall that as part of our developer cell project we wanted to collect a bunch of data on PURE. Check out the first cut of that data, using platemaps such as this!
::: -->

# Using platemaps

Once your platemap has been made, it can support the analysis and sharing of your experimental data. In this section, we'll see some example applications.

## Associating experimental conditions with measurements

When using an instrument like a microplate reader to make fluorescence measurements, the data files generated are instrument-specific and likely do not allow you to include many kinds of information that are necessary for making your data legible to collaborators, or for performing analyses. Typically you'll just have the measurement information and the wells on the plate they correspond to. 

To format your data for sharing or analysis, you will need to read your instrument data into a table with one row per  measurement. Then you can simply "join" or "merge" your table with the platemap along the `Well` column. In Python, if your data are loaded into a Pandas `DataFrame` called `data`, this can be done in a fairly straightforward way:

```python
import pandas as pd
platemap = pd.read_csv('path/to/platemap.csv')
data = data.merge(platemap, how='left', 
                  left_on = '<Well column in data>',
                  right_on = 'Well')
```

<!--:::{tip} Using the CDK to load microplate reader data-->
For \[BioTek\] microplate readers, this functionality is implemented in the CDK directly into the function that loads plate reader data:
```python
from cdk.analysis.cytosol import platereader as pr

data, platemap = pr.load_platereader_data(
    data_file='path/to/datafile.txt',
    platemap_file='path/to/platemap.csv',
    platereader="biotek-cdk"
)
```

<!-- :::{aside}
Currently, primarily Agilent (BioTek) plate readers are supported. 
::: -->

The function takes as input the data file from a plate reader, and combines it in this way with a provided platemap. The resulting `data` object is a Pandas `DataFrame` that contains the data in full "long" format, suitable for sharing or further analysis.

(column-example)=
## Using optional platemap columns for analysis
By including information about experimental variables and conditions into the platemap, we can easily separate data based on different conditions or variables to understand how they affect the results. 
Information about measurement conditions, like different modalities or read types, can be used the same way.

As a simple example, when visualizing data using Seaborn, a column can be used as a facet when plotting data:
```python
sns.relplot(data, x = 'Time', y = 'data_normalized', 
            hue = 'tRNA ID')
```

:::{figure} #fig:column_facet
:name: fig-column-facet
:align: center

Using an optional platemap column to visualize differences due to experimental conditions. Here, the time course of (normalized) fluorescence of GFP produced in a PURE reaction is shown for two different tRNA stocks (colors). This plot was generated by faceting on the `tRNA ID` column that was included in the platemap.
:::


<!-- When performing more quantitative analyses of data, like fitting a regression model, the optional columns will also contain the relevant "features" or "regressor" variables of interest. -->

[^long]: This is known as the ["long"](https://data.europa.eu/apps/data-visualisation-guide/wide-versus-long-data) data format. As we'll see later, this format has advantages for data processing.
[^confusion]: Note: the rows and columns are not the same as the rows and columns of your plate!