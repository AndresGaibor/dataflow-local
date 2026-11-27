---
title: "Basic aggregation functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/AggregationFunctions/basic-aggregation-functions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions"]
---

# Basic aggregation functions

Expand/Collapse all

# Basic aggregation functions

Basic aggregation functions are a group of the most common aggregation functions.

Use the drop-down on each function to see a brief description and the syntax of each function. Click the function name in the syntax description for further details.

## Basic aggregation functions in the data load script

FirstSortedValue

FirstSortedValue() returns the value from the expression specified in value that corresponds to the result of sorting the sort\_weight argument, for example, the name of the product with the lowest unit price. The nth value in the sort order, can be specified in rank. If more than one resulting value shares the same sort\_weight for the specified rank, the function returns NULL. The sorted values are iterated over
a number of records, as defined by a group by clause, or aggregated across the full data set if no group by clause is defined.

[**firstsorted**](firstsorted.htm)([
distinct ] expression, sort\_weight
[, rank ])

Max

Max() finds the highest numeric value of the aggregated data in the expression, as defined by a group
by clause. By specifying a rank n, the nth highest value can be found.

[**max**](max.htm)( expression[, rank])

Min

Min() returns the lowest numeric value of the aggregated data in the expression, as defined by a group
by clause. By specifying a rank n, the nth lowest value can be found.

[**min**](min.htm)( expression[, rank])

Mode

Mode() returns the most commonly-occurring value, the mode value, of the aggregated data in the expression, as defined by a group by clause. The
Mode() function can return numeric values
as well as text values.

[**mode**](mode.htm)(expression
)

Only

Only() returns a value if there is one and only one possible result from the aggregated data. If records contain only one value then that value is returned, otherwise NULL is returned. Use the group by clause to evaluate over multiple records. The Only() function can return numeric and text values.

[**only**](only.htm)(expression
)

Sum

Sum() calculates the total of the values aggregated in the expression, as defined by a group
by clause.

[**sum**](sum.htm)([distinct]expression)

## Basic aggregation functions in chart expressions

Chart aggregation functions can only be used on fields in chart expressions. The argument expression of one aggregation function must not contain another aggregation function.

FirstSortedValue

FirstSortedValue() returns the value from the expression specified in value that corresponds to the result of sorting the sort\_weight argument, for example, the name of the product with the lowest unit price. The nth value in the sort order, can be specified in rank. If more than one resulting value shares the same sort\_weight for the specified rank, the function returns NULL.

[**firstsortedvalue**](../../ChartFunctions/BasicAggregationFunctions/firstsortedvalue.htm)([{SetExpression}] [DISTINCT] [TOTAL [<fld {,fld}>]] value, sort\_weight [,rank])

Max

Max() finds the highest value of the aggregated data. By specifying a rank n, the nth highest value can be found.

[**max**](../../ChartFunctions/BasicAggregationFunctions/max.htm)([{SetExpression}] [DISTINCT] [TOTAL [<fld {,fld}>]] expr [,rank])

Min

Min()
 finds the lowest value of the aggregated data. By specifying a rank n, the nth lowest value can be found.

[**min**](../../ChartFunctions/BasicAggregationFunctions/min.htm)([{SetExpression}] [DISTINCT] [TOTAL [<fld {,fld}>]] expr [,rank])

Mode

Mode()
 finds the most commonly occurring value, the mode value, in the aggregated data. The Mode() function
can process text values as well as numeric values.

[**mode**](../../ChartFunctions/BasicAggregationFunctions/mode.htm)
({[SetExpression] [TOTAL [<fld {,fld}>]]} expr)

Only

Only()
 returns a value if there is one and only one possible result from the aggregated data. For example, searching for the only product where the unit price =9 will return NULL if more than one product has a unit price of 9.

[**only**](../../ChartFunctions/BasicAggregationFunctions/only.htm)([{SetExpression}] [DISTINCT] [TOTAL [<fld {,fld}>]] expr)

Sum

Sum()
 calculates the total of the values given by the expression or field across the aggregated data.

[**sum**](../../ChartFunctions/BasicAggregationFunctions/sum.htm)([{SetExpression}] [DISTINCT] [TOTAL [<fld {,fld}>]] expr])
