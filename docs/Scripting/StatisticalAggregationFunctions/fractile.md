---
title: "Fractile Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalAggregationFunctions/fractile.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Statistical aggregation functions"]
---
# Fractile Script function

Fractile()
finds the value that corresponds to the inclusive fractile (quantile) of the aggregated data in the expression over
a number of records as defined by a group by clause.

> **Tip:** You can use [*FractileExc Script function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalAggregationFunctions/fractileexc.htm) to calculate the exclusive fractile.

Syntax:

Fractile(expr, fraction)

Return data type: numeric

The function returns the value corresponding to the rank as defined by `rank = fraction * (N-1) + 1` where `N` is the number of values in `expr`. If `rank` is a non-integer number, an interpolation is made between the two closest values.

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| expr | The expression or [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalAggregationFunctions/fractile.htm#glossary-0 "Glossary term") containing the data to use when calculating the fractile. |
| fraction | A number between 0 and 1 corresponding to the fractile (quantile expressed as a fraction) to be calculated. |

Examples and results:

Add the example script to your application and run it. To see the result, add the fields listed in the results column to a sheet in your application.

Resulting data

| Example | Result |
| --- | --- |
| ``` Table1: Crosstable (Type, Value) Load recno() as ID, * inline [ Observation|Comparison 35|2 40|27 12|38 15|31 21|1 14|19 46|1 10|34 28|3 48|1 16|2 30|3 32|2 48|1 31|2 22|1 12|3 39|29 19|37 25|2 ] (delimiter is '|'); ```  Fractile1:  LOAD Type,  Fractile(Value,0.75) as MyFractile Resident Table1 Group By Type; | In a table with the [dimensions](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalAggregationFunctions/fractile.htm#glossary-1 "Glossary term") `Type` and `MyFractile`, the results of the Fractile() calculations in the [data load script](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalAggregationFunctions/fractile.htm#glossary-2 "Glossary term") are:  Type MyFractile  Comparison 27.5  Observation 36 |
