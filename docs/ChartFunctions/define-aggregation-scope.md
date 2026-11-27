---
title: "Defining the aggregation scope"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/define-aggregation-scope.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Chart expressions"]
---

# Defining the aggregation scope

There are usually two factors that together determine which records are used to define the value of [aggregation](#glossary-0 "Glossary term") in an expression. When working in [visualizations](#glossary-1 "Glossary term") these factors are:

- Dimensional value (of the aggregation in a chart expression)
- Selections

Together, these factors define the scope of the aggregation. You may come across situations where you want your calculation to disregard the selection, the [dimension](#glossary-2 "Glossary term"), or both. In [chart](#glossary-3 "Glossary term") functions, you can achieve this by using the TOTAL qualifier, [set analysis](#glossary-4 "Glossary term") or a combination of the two. In summary:

- To disregard or adjust the dimensional grouping: Use the TOTAL qualifier
- To disregard or adjust the selection: Use set analysis

Aggregation: Method and description

| Method | Description |
| --- | --- |
| TOTAL qualifier | Using the total qualifier inside your aggregation function disregards the dimensional value.  The total qualifier may be used inside an aggregation in order to redefine the aggregation scope by disregarding the dimensional values. The aggregation will instead be performed on all possible [field](#glossary-5 "Glossary term") values.  The TOTAL qualifier may be followed by a list of one or more field names within angle brackets.  For example:  Sum(TOTAL <Quarter> {<Year={2013}, Quarter={'Q2'}>} Amount)  These field names should be a subset of the chart dimensions. In this case, the calculation is made disregarding all chart dimensions except those listed, that is, one value is returned for each combination of field values in the listed dimension fields. Also, fields that are not currently a dimension in a chart may be included in the list. This may be useful in the case of group dimensions, where the dimension fields are not fixed. Listing all of the dimensions in the group causes the function to give consistent aggregation results when the drill-down level changes.  For an example of adding exceptions in angle brackets, see  [*Example: TOTAL qualifier with exception, and set analysis*](#Examples). |
| Set analysis | Using set analysis inside your aggregation overrides the selection. The aggregation will be performed on all values split across the dimensions. |
| TOTAL qualifier and set analysis | Using the TOTAL qualifier and set analysis inside your aggregation overrides the selection and disregards all dimensions, except those listed within angle brackets after the TOTAL  qualifier. |
| ALL qualifier | Using the ALL qualifier inside your aggregation disregards the selection and the dimensions. The equivalent can be achieved with the {1} set analysis statement and the TOTAL qualifier:  =sum(All Sales)  =sum({1} Total Sales) |

## Example: TOTAL qualifier

The following example shows how TOTAL can be used to calculate a relative share. Assuming that Q2 has been selected, using TOTAL calculates the sum of all values disregarding the dimensions.

Example: Total qualifier

| Year | Quarter | Sum(Amount) | Sum(TOTAL Amount) | Sum(Amount)/Sum(TOTAL Amount) |
| --- | --- | --- | --- | --- |
|  |  | 3000 | 3000 | 100% |
| 2012 | Q2 | 1700 | 3000 | 56,7% |
| 2013 | Q2 | 1300 | 3000 | 43,3% |

Tip noteTo show the numbers as a percentage, in the [properties](#glossary-6 "Glossary term") panel, for the [measure](#glossary-7 "Glossary term") you want to show as a percentage value, under Number formatting, select Number, and from Formatting, choose Simple and one of the % formats.

## Example: Set analysis

The following example shows how set analysis can be used to make a comparison between data sets before any selection was made. Assuming that Q2 has been selected, using set analysis with the set definition {1} calculates the sum of all values disregarding any [selections](#glossary-8 "Glossary term") but split by the dimensions.

Example: Set analysis

| Year | Quarter | Sum(Amount) | Sum({1} Amount) | Sum(Amount)/Sum({1} Amount) |
| --- | --- | --- | --- | --- |
|  |  | 3000 | 10800 | 27,8% |
| 2012 | Q1 | 0 | 1100 | 0% |
| 2012 | Q3 | 0 | 1400 | 0% |
| 2012 | Q4 | 0 | 1800 | 0% |
| 2012 | Q2 | 1700 | 1700 | 100% |
| 2013 | Q1 | 0 | 1000 | 0% |
| 2013 | Q3 | 0 | 1100 | 0% |
| 2013 | Q4 | 0 | 1400 | 0% |
| 2013 | Q2 | 1300 | 1300 | 100% |

## Example: TOTAL qualifier and set analysis ({1} identifier)

The following example shows how set analysis and the TOTAL qualifier can be combined to make a comparison between data sets before any selection was made and across all dimensions. Assuming that Q2 has been selected, using set analysis with the set definition {1} and the TOTAL qualifier calculates the sum of all values disregarding any selections and disregarding the dimensions.

Example: TOTAL qualifier and set analysis

| Year | Quarter | Sum(Amount) | Sum({1} TOTAL Amount) | Sum(Amount)/Sum({1} TOTAL Amount) |
| --- | --- | --- | --- | --- |
|  |  | 3000 | 10800 | 27,8% |
| 2012 | Q2 | 1700 | 10800 | 15,7% |
| 2013 | Q2 | 1300 | 10800 | 12% |

## Example: TOTAL qualifier and set analysis (comparing data against a reference value)

The following example shows how you can use set analysis and the TOTAL qualifier to create a reference columns in your table for easy row-level comparison of metrics. To make the data easier to understand and consume, we label the measure columns.

The data from the second quarter of 2013 is used as a reference to compare against all other values in the table.

Do the following:

1. Add a table to your sheet.
2. Add the following fields as dimensions:

   - Year
   - Quarter
3. Add the following measure:

   ```
   Sum(Amount)
   ```
4. In the properties for the measure you just added, give the measure the following label: Total Sales
5. Add the following measure:

   ```
   Sum(TOTAL {<Year={2013}, Quarter={'Q2'}>} Amount)
   ```
6. In the properties for the measure you just added, give the measure the following label: Reference Quarter (2013-Q2) Total Sales
7. Add the following measure:

   ```
   round((sum(Amount) / sum(total {<Year={2013}, Quarter={'Q2'}>} Amount))*100,'0.01') & '%'
   ```
8. In the properties for the measure you just added, give the measure the following label: Rounded Quotient - Total Sales Compared to Reference Quarter (2013-Q2)

With no selections applied, your table should look like the following:

Example: TOTAL qualifier and set analysis (reference column)

| Year | Quarter | Total Sales | Reference Quarter (2013-Q2) Total Sales | Rounded Quotient - Total Sales Compared to Reference Quarter (2013-Q2) |
| --- | --- | --- | --- | --- |
| 2012 | Q1 | 1100 | 1300 | 84.62% |
| 2012 | Q2 | 1700 | 1300 | 130.77% |
| 2012 | Q3 | 1400 | 1300 | 107.69% |
| 2012 | Q4 | 1800 | 1300 | 138.46% |
| 2013 | Q1 | 1000 | 1300 | 76.92% |
| 2013 | Q2 | 1300 | 1300 | 100.00% |
| 2013 | Q3 | 1100 | 1300 | 84.62% |
| 2013 | Q4 | 1400 | 1300 | 107.69% |

## Example: TOTAL qualifier with exception, and set analysis

The following example shows how to use the TOTAL qualifier, but with an exception to this qualifier noted in angle brackets. The example expressions also uses set analysis.

Do the following:

1. Add a table to your sheet.
2. Add the following fields as dimensions:

   - Year
   - Quarter
3. Add the following measure:

   ```
   Sum(Amount)
   ```
4. In the properties for the measure you just added, give the measure the following label: Total Sales
5. Add the following measure:

   ```
   Sum(TOTAL <Quarter> {<Year={2013}, Quarter={'Q2'}>} Amount)
   ```
6. In the properties for the measure you just added, give the measure the following label: Reference Quarter (2013-Q2) Total Sales

Examples: TOTAL qualifier with exception, and set analysis

| Year | Quarter | Total Sales | Reference Quarter (2013-Q2) Total Sales |
| --- | --- | --- | --- |
| 2012 | Q1 | 1100 | 0 |
| 2012 | Q2 | 1700 | 1300 |
| 2012 | Q3 | 1400 | 0 |
| 2012 | Q4 | 1800 | 0 |
| 2013 | Q1 | 1000 | 0 |
| 2013 | Q2 | 1300 | 1300 |
| 2013 | Q3 | 1100 | 0 |
| 2013 | Q4 | 1400 | 0 |

The reference column expression is interpreted as follows:

- The set expression {<Year={2013}, Quarter={'Q2'}>} restricts input data to records with a Year of 2013 and a Quarter of Q2.
- The TOTAL qualifier ensures all dimensions in the table are disregarded. However, with the <Quarter> specifier, an exception is made for the Quarter dimension.

## Data used in examples on this page

Data used in examples:

```
AggregationScope:
LOAD * inline [
Year Quarter Amount
2012 Q1 1100
2012 Q2 1700
2012 Q3 1400
2012 Q4 1800
2013 Q1 1000
2013 Q2 1300
2013 Q3 1100
2013 Q4 1400] (delimiter is ' ');
```

## Learn more

- [*Set analysis*](SetAnalysis/set-analysis-expressions.htm)
- [Qlik Community: The Aggregation Scope](https://community.qlik.com/t5/Qlik-Design-Blog/The-Aggregation-Scope/ba-p/1467321)
