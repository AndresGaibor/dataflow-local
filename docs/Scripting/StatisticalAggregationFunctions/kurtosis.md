---
title: "Kurtosis Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalAggregationFunctions/kurtosis.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Statistical aggregation functions"]
---
# Kurtosis Script function

Kurtosis() returns
the kurtosis of the data in the expression over
a number of records as defined by a group by clause.

Syntax:

Kurtosis([distinct ] expr
)

Return data type: numeric

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| expr | The expression or field containing the data to be measured. |
| distinct | If the word distinct occurs before the expression, all duplicates will be disregarded. |

Examples and results:

Add the example script to your application and run it. To see the result, add the fields listed in the results column to a sheet in your application.

Resulting data

| Example | Result |
| --- | --- |
| ``` Table1: Crosstable (Type, Value) Load recno() as ID, * inline [ Observation|Comparison 35|2 40|27 12|38 15|31 21|1 14|19 46|1 10|34 28|3 48|1 16|2 30|3 32|2 48|1 31|2 22|1 12|3 39|29 19|37 25|2 ] (delimiter is '|'); ```  Kurtosis1:  LOAD Type,  Kurtosis(Value) as MyKurtosis1,  Kurtosis(DISTINCT Value) as MyKurtosis2  Resident Table1 Group By Type; | In a table with the [dimensions](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalAggregationFunctions/kurtosis.htm#glossary-0 "Glossary term") `Type`, `MyKurtosis1`,and `MyKurtosis2`, the results of the Kurtosis() calculations in the [data load script](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalAggregationFunctions/kurtosis.htm#glossary-1 "Glossary term") are:  Type MyKurtosis1 MyKurtosis2  Comparison -1.1612957 -1.4982366  Observation -1.1148768 -0.93540144 |
