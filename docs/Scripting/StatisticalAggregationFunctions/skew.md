---
title: "Skew Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalAggregationFunctions/skew.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Statistical aggregation functions"]
---
# Skew Script function

Skew() returns
the skewness of expression over
a number of records as defined by a group by clause.

Syntax:

Skew([ distinct] expr)

Return data type:  numeric

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| expr | The expression or field containing the data to be measured. |
| DISTINCT | If the word distinct occurs before the expression, all duplicates will be disregarded. |

Examples and results:

Add the example script to your application and run it. Then build a straight table with `Type` and MySkew as [dimensions](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalAggregationFunctions/skew.htm#glossary-1 "Glossary term").

Resulting data

| Example | Result |
| --- | --- |
| ``` Table1: Crosstable (Type, Value) Load recno() as ID, * inline [ Observation|Comparison 35|2 40|27 12|38 15|31 21|1 14|19 46|1 10|34 28|3 48|1 16|2 30|3 32|2 48|1 31|2 22|1 12|3 39|29 19|37 25|2 ] (delimiter is '|'); ```  Skew1:  LOAD Type,  Skew(Value) as MySkew  Resident Table1 Group By Type; | The results of the Skew() calculation are:   - `Type`  is `MySkew` - `Comparison`  is 0.86414768 - `Observation` is 0.32625351 |
