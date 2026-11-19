---
title: "NullCount Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/CounterAggregationFunctions/NullCount.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Counter aggregation functions"]
---
# NullCount Script function

NullCount() returns the number of NULL values aggregated in the expression, as defined by a group by clause.

Syntax:

NullCount ( [
distinct ] expr)

Return data type:  integer

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| expr Expression | The expression or field containing the data to be measured. |
| distinct | If the word distinct occurs before the expression, all duplicates are disregarded. |

Examples and results:

Add the example script to your application and run it. Then add, at least, the fields listed in the results column to a sheet in our application to see the result.

To get the same look as in the result column below, in the properties panel, under Sorting, switch from Auto to Custom, then deselect numerical and alphabetical sorting.

Scripting examples

| Example | Result |
| --- | --- |
| Set NULLINTERPRET = NULL;  Temp:  LOAD \* inline [  Customer|Product|OrderNumber|UnitSales|CustomerID  Astrida|AA|1|10|1  Astrida|AA|7|18|1  Astrida|BB|4|9|1  Astrida|CC|6|2|1  Betacab|AA|5|4|2  Betacab|BB|2|5|2  Betacab|DD|||  Canutility|AA|3|8|  Canutility|CC|NULL||  ] (delimiter is '|');  Set NULLINTERPRET=;  NullCount1:  LOAD Customer,NullCount(OrderNumber) as NullOrdersByCustomer Resident Temp Group By Customer;    `LOAD NullCount(OrderNumber) as TotalNullCount Resident Temp;` | Customer NullOrdersByCustomer  Astrida 0  Betacab 0  Canutility 1    The second statement gives:  TotalNullCount  1  in a table with that [dimension](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/CounterAggregationFunctions/NullCount.htm#glossary-0 "Glossary term"), because only one record contains a null value. |
