---
title: "Mode Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/AggregationFunctions/mode.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Basic aggregation functions"]
---

# Mode Script function

Mode() returns the most commonly-occurring value, the mode value, of the aggregated data in the expression, as defined by a group by clause. The
Mode() function can return numeric values
as well as text values.

Syntax:

Mode ( expr)

Return data type: dual

Arguments

| Argument | Description |
| --- | --- |
| expr Expression | The expression or field containing the data to be measured. |

Limitations:

If more than one value is equally commonly occurring, NULL is returned.

Examples and results:

Add the example script to your application and run it. Then add, at least, the fields listed in the results column to a sheet in our application to see the result.

To get the same look as in the result column below, in the properties panel, under Sorting, switch from Auto to Custom, then deselect numerical and alphabetical sorting.

Scripting examples

| Example | Result |
| --- | --- |
| Temp:  LOAD \* inline [  Customer|Product|OrderNumber|UnitSales|CustomerID  Astrida|AA|1|10|1  Astrida|AA|7|18|1  Astrida|BB|4|9|1  Astrida|CC|6|2|1  Betacab|AA|5|4|2  Betacab|BB|2|5|2  Betacab|DD  Canutility|DD|3|8  Canutility|CC  ] (delimiter is '|');    Mode:  LOAD Customer, Mode(Product) as MyMostOftenSoldProduct Resident Temp Group By Customer; | MyMostOftenSoldProduct  AA  because AA is the only product sold more than once. |
