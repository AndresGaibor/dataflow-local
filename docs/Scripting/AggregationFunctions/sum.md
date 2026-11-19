---
title: "Sum Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/AggregationFunctions/sum.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Basic aggregation functions"]
---
# Sum Script function

Sum() calculates the total of the values aggregated in the expression, as defined by a group
by clause.

Syntax:

sum ( [ distinct] expr)

Return data type: numeric

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| distinct | If the word distinct occurs before the expression, all duplicates will be disregarded. |
| expr Expression | The expression or field containing the data to be measured. |

Examples and results:

Add the example script to your application and run it. Then add, at least, the fields listed in the results column to a sheet in our application to see the result.

To get the same look as in the result column below, in the properties panel, under Sorting, switch from Auto to Custom, then deselect numerical and alphabetical sorting.

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

Sum:

LOAD Customer, Sum(UnitSales) as MySum Resident Temp Group By Customer;

Resulting table

| Customer | MySum |
| --- | --- |
| Astrida | 39 |
| Betacab | 9 |
| Canutility | 8 |
