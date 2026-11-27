---
title: "Min Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/AggregationFunctions/min.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Basic aggregation functions"]
---

# Min Script function

Min() returns the lowest numeric value of the aggregated data in the expression, as defined by a group
by clause. By specifying a rank n, the nth lowest value can be found.

Syntax:

Min ( expr [, rank])

Return data type:  numeric

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| expr Expression | The expression or field containing the data to be measured. |
| rank Expression | The default value of rank is 1, which corresponds to the lowest value. By specifying rank as 2, the second lowest value is returned. If rank is 3, the third lowest value is returned, and so on. |

Examples and results:

Add the example script to your application and run it. Then add, at least, the fields listed in the results column to a sheet in our application to see the result.

To get the same look as in the result column below, in the properties panel, under Sorting, switch from Auto to Custom, then deselect numerical and alphabetical sorting.

Example:

Temp:

LOAD \* inline [

Customer|Product|OrderNumber|UnitSales|CustomerID

Astrida|AA|1|10|1

Astrida|AA|7|18|1

Astrida|BB|4|9|1

Astrida|CC|6|2|1

Betacab|AA|5|4|2

Betacab|BB|2|5|2

Betacab|DD

Canutility|DD|3|8

Canutility|CC

] (delimiter is '|');

Min:

LOAD Customer, Min(UnitSales) as MyMin Resident Temp Group By Customer;

Resulting table

| Customer | MyMin |
| --- | --- |
| Astrida | 2 |
| Betacab | 4 |
| Canutility | 8 |

Example:

Given that the Temp table is loaded as in the previous example:

LOAD Customer, Min(UnitSales,2) as MyMinRank2 Resident Temp Group By Customer;

Resulting table

| Customer | MyMinRank2 |
| --- | --- |
| Astrida | 9 |
| Betacab | 5 |
| Canutility | - |
