---
title: "Correl - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/StatisticalAggregationFunctionsinCharts/correl.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Statistical aggregation functions"]
---

# Correl - chart function

Correl() returns the aggregated correlation coefficient for two data sets. The correlation function is a measure of the relationship between the data sets and is aggregated for (x,y) value pairs iterated over the chart dimensions.

Syntax:

Correl([{SetExpression}] [DISTINCT] [TOTAL [<fld{, fld}>]] value1, value2 )

Return data type:  numeric

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| value1, value2 | The expressions or fields containing the two sample sets for which the correlation coefficient is to be measured. |
| SetExpression | By default, the aggregation function will aggregate over the set of possible records defined by the selection. An alternative set of records can be defined by a set analysis expression. |
| DISTINCT | If the word DISTINCT occurs before the function arguments, duplicates resulting from the evaluation of the function arguments are disregarded. |
| TOTAL | If the word TOTAL occurs before the function arguments, the calculation is made over all possible values given the current selections, and not just those that pertain to the current dimensional value, that is, it disregards the chart dimensions.  By using TOTAL [<fld {.fld}>], where the TOTAL qualifier is followed by a list of one or more field names as a subset of the chart dimension variables, you create a subset of the total possible values.  [*Defining the aggregation scope*](../define-aggregation-scope.htm) |

Limitations:

The parameter of the aggregation function must not contain other aggregation functions, unless these inner aggregations contain the TOTAL qualifier. For
more advanced nested aggregations, use the advanced function Aggr, in combination with a specified dimension.

Text values, NULL values and missing values in any or both pieces of a data-pair result in the entire data-pair being disregarded.

Examples and results:

Function examples

| Example | Result |
| --- | --- |
| Correl(Age, Salary) | For a table including the [dimension](#glossary-0 "Glossary term") `Employee name` and the [measure](#glossary-1 "Glossary term") Correl(Age, Salary), the result is 0.9270611. The result is only displayed for the totals cell. |
| Correl(TOTAL Age, Salary)) | 0.927. This and the following results are shown to three decimal places for readability.  If you create a filter pane with the dimension Gender, and make [selections](#glossary-2 "Glossary term") from it, you see the result 0.951 when Female is selected and 0.939 if Male is selected. This is because the selection excludes all results that do not belong to the other value of Gender. |
| Correl({1} TOTAL Age, Salary)) | 0.927. Independent of selections. This is because the set expression {1} disregards all selections and dimensions. |
| Correl(TOTAL <Gender> Age, Salary)) | 0.927 in the total cell, 0.939 for all values of Male, and 0.951 for all values of Female. This corresponds to the results from making the selections in a filter pane based on Gender. |

Data used in examples:

Salary:

LOAD \* inline [

"Employee name"|Gender|Age|Salary

Aiden Charles|Male|20|25000

Brenda Davies|Male|25|32000

Charlotte Edberg|Female|45|56000

Daroush Ferrara|Male|31|29000

Eunice Goldblum|Female|31|32000

Freddy Halvorsen|Male|25|26000

Gauri Indu|Female|36|46000

Harry Jones|Male|38|40000

Ian Underwood|Male|40|45000

Jackie Kingsley|Female|23|28000

] (delimiter is '|');

## Learn more

- [*Aggr - chart function*](../aggr.htm)
- [*Avg - chart function*](avg.htm)
- [*RangeCorrel Script and chart function*](../RangeFunctions/rangecorrel.htm)
- [*Set analysis*](../SetAnalysis/set-analysis-expressions.htm)
