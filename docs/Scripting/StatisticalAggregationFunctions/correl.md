---
title: "Correl Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalAggregationFunctions/correl.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Statistical aggregation functions"]
---

# Correl Script function

Correl() returns
the aggregated correlation coefficient for a series of coordinates represented
by paired numbers in x-expression and y-expression iterated over a number
of records as defined by a group by
clause.

Syntax:

Correl(value1, value2)

Return data type: numeric

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| value1, value2 | The expressions or fields containing the two sample sets for which the correlation coefficient is to be measured. |

Limitations:

Text values, NULL values and missing values in any or both pieces of a data-pair result in the entire data-pair being disregarded.

Examples and results:

Add the example script to your application and run it. To see the result, add the fields listed in the results column to a sheet in your application.

Resulting data

| Example | Result |
| --- | --- |
| Salary:  Load \*, 1 as Grp;  LOAD \* inline [  "Employee name"|Gender|Age|Salary  Aiden Charles|Male|20|25000  Brenda Davies|Male|25|32000  Charlotte Edberg|Female|45|56000  Daroush Ferrara|Male|31|29000  Eunice Goldblum|Female|31|32000  Freddy Halvorsen|Male|25|26000  Gauri Indu|Female|36|46000  Harry Jones|Male|38|40000  Ian Underwood|Male|40|45000  Jackie Kingsley|Female|23|28000  ] (delimiter is '|');  Correl1:  LOAD Grp,  Correl(Age,Salary) as Correl\_Salary Resident Salary Group By Grp; | In a table with the [dimension](#glossary-0 "Glossary term") Correl\_Salary, the result of the Correl() calculation in the data [load script](#glossary-1 "Glossary term") will be shown: 0.9270611 |
