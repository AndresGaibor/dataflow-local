---
title: "NumericCount Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/CounterAggregationFunctions/NumericCount.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Counter aggregation functions"]
---
# NumericCount Script function

NumericCount() returns the number of numeric values found in the expression,
as defined by a group by clause.

Syntax:

NumericCount ( [
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

Scripting example

| Example | Result |
| --- | --- |
| `LOAD NumericCount(OrderNumber) as TotalNumericCount Resident Temp;` | The second statement gives: TotalNumericCount 7 in a table with that [dimension](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/CounterAggregationFunctions/NumericCount.htm#glossary-0 "Glossary term"). |
| Given that the Temp table is loaded as in the previous example:  LOAD NumericCount(distinct OrderNumber) as TotalNumeriCCountDistinct Resident Temp; | TotalNumericCountDistinct  6 Because there is one OrderNumber that duplicates another, so the result is 6 that are not duplicates.. |

Example:

Temp:

LOAD \* inline [

Customer|Product|OrderNumber|UnitSales|UnitPrice

Astrida|AA|1|4|16

Astrida|AA|7|10|15

Astrida|BB|4|9|9

Betacab|CC|6|5|10

Betacab|AA|5|2|20

Betacab|BB||| 25

Canutility|AA|||15

Canutility|CC| ||19

Divadip|CC|2|4|16

Divadip|DD|7|1|25

] (delimiter is '|');

NumCount1:

LOAD Customer,NumericCount(OrderNumber) as NumericCountByCustomer Resident Temp Group By Customer;

Resulting table

| Customer | NumericCountByCustomer |
| --- | --- |
| Astrida | 3 |
| Betacab | 2 |
| Canutility | 0 |
| Divadip | 2 |
