---
title: "FirstSortedValue Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/AggregationFunctions/firstsorted.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Basic aggregation functions"]
---

# FirstSortedValue Script function

FirstSortedValue() returns the value from the expression specified in value that corresponds to the result of sorting the sort\_weight argument, for example, the name of the product with the lowest unit price. The nth value in the sort order, can be specified in rank. If more than one resulting value shares the same sort\_weight for the specified rank, the function returns NULL. The sorted values are iterated over
a number of records, as defined by a group by clause, or aggregated across the full data set if no group by clause is defined.

Syntax:

FirstSortedValue ([
distinct ] value, sort-weight
[, rank ])

Return data type:  dual

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| value Expression | The function finds the value of the expression value that corresponds to the result of sorting sort\_weight. |
| sort-weight Expression | The expression containing the data to be sorted. The first (lowest) value of sort\_weight is found, from which the corresponding value of the value expression is determined. If you place a minus sign in front of sort\_weight, the function returns the last (highest) sorted value instead. |
| rank Expression | By stating a rank "n" larger than 1, you get the nth sorted value. |
| distinct | If the word DISTINCT occurs before the function arguments, duplicates resulting from the evaluation of the function arguments are disregarded. |

Examples and results:

Add the example script to your application and run it. Then add, at least, the fields listed in the results column to a sheet in our application to see the result.

To get the same look as in the result column below, in the properties panel, under Sorting, switch from Auto to Custom, then deselect numerical and alphabetical sorting.

Scripting examples

| Example | Result |
| --- | --- |
| Temp:  LOAD \* inline [  Customer|Product|OrderNumber|UnitSales|CustomerID  Astrida|AA|1|10|1  Astrida|AA|7|18|1  Astrida|BB|4|9|1  Astrida|CC|6|2|1  Betacab|AA|5|4|2  Betacab|BB|2|5|2  Betacab|DD|12|25|2  Canutility|AA|3|8|3  Canutility|CC|13|19|3  Divadip|AA|9|16|4  Divadip|AA|10|16|4  Divadip|DD|11|10|4  ] (delimiter is '|');    FirstSortedValue:  LOAD Customer,FirstSortedValue(Product, UnitSales) as MyProductWithSmallestOrderByCustomer Resident Temp Group By Customer; | Customer MyProductWithSmallestOrderByCustomer  Astrida CC  Betacab AA  Canutility AA  Divadip DD  The function sorts UnitSales from smallest to largest, looking for the value of Customer with the smallest value of UnitSales, the smallest order.  Because CC corresponds to the smallest order (value of UnitSales=2) for customer Astrida. AA corresponds to the smallest order (4) for customer Betacab, AA corresponds to the smallest order (8) for customer Canutility, and DD corresponds to the smallest order (10) for customer Divadip.. |
| Given that the Temp table is loaded as in the previous example:  LOAD Customer,FirstSortedValue(Product, -UnitSales) as MyProductWithLargestOrderByCustomer Resident Temp Group By Customer; | Customer MyProductWithLargestOrderByCustomer  Astrida AA  Betacab DD  Canutility CC  Divadip -  A minus sign precedes the sort\_weight argument, so the function sorts the largest first.  Because AA corresponds to the largest order (value of UnitSales:18) for customer Astrida, DD corresponds to the largest order (12) for customer Betacab, and CC corresponds to the largest order (13) for customer Canutility. There are two identical values for the largest order (16) for customer Divadip, therefore this produces a null result. |
| Given that the Temp table is loaded as in the previous example:  LOAD Customer,FirstSortedValue(distinct Product, -UnitSales) as MyProductWithSmallestOrderByCustomer Resident Temp Group By Customer; | Customer MyProductWithLargestOrderByCustomer  Astrida AA  Betacab DD  Canutility CC  Divadip AA  This is the same as the previous example, except the distinct qualifier is used. This causes the duplicate result for Divadip to be disregarded, allowing a non-null value to be returned. |
