---
title: "Count Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/CounterAggregationFunctions/count.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Counter aggregation functions"]
---

# Count Script function

Count() returns the number of values aggregated in expression, as defined by a group by clause.

Syntax:

Count( [distinct ] expr)

Return data type:  integer

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| expr | The expression or field containing the data to be measured. |
| distinct | If the word distinct occurs before the expression, all duplicates are disregarded. |

Examples and results:

Add the example script to your application and run it. Then add, at least, the fields listed in the results column to a sheet in our application to see the result.

To get the same look as in the result column below, in the properties panel, under Sorting, switch from Auto to Custom, then deselect numerical and alphabetical sorting.

Scripting examples

| Example | Result |
| --- | --- |
| Temp:  LOAD \* inline [  Customer|Product|OrderNumber|UnitSales|UnitPrice  Astrida|AA|1|4|16  Astrida|AA|7|10|15  Astrida|BB|4|9|9  Betacab|CC|6|5|10  Betacab|AA|5|2|20  Betacab|BB|1|25| 25  Canutility|AA|3|8|15  Canutility|CC|||19  Divadip|CC|2|4|16  Divadip|DD|3|1|25  ] (delimiter is '|');    Count1:  LOAD Customer,Count(OrderNumber) as OrdersByCustomer Resident Temp Group By Customer; | Customer OrdersByCustomer  Astrida 3  Betacab 3  Canutility 2  Divadip 2  As long as the [dimension](#glossary-0 "Glossary term") Customer is included in the table on the [sheet](#glossary-1 "Glossary term") otherwise the result for OrdersByCustomer is 3, 2. |
| Given that the Temp table is loaded as in the previous example:  LOAD Count(OrderNumber) as TotalOrderNumber Resident Temp; | TotalOrderNumber  10 |
| Given that the Temp table is loaded as in the first example:  LOAD Count(distinct OrderNumber) as TotalOrderNumber Resident Temp; | TotalOrderNumber  8  Because there are two values of OrderNumber with the same value, 1, and one null value. |
