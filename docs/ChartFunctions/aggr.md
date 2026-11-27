---
title: "Aggr - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/aggr.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions"]
---

# Aggr - chart function

Aggr() returns an array of values for the expression
calculated over the stated dimension or dimensions. For example, the maximum value of sales, per customer, per region.

The Aggr function is used for nested aggregations, in which its first parameter (the inner aggregation) is calculated once per dimensional value. The dimensions are specified in the second parameter (and subsequent parameters).

In addition, the Aggr function should be enclosed in an outer aggregation function, using the array of results from the Aggr function as input to the aggregation in which it is nested.

Syntax:

Aggr({SetExpression}[DISTINCT] [NODISTINCT
] expr, StructuredParameter{, StructuredParameter})

Return data type:  dual

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| expr | An expression consisting of an [aggregation](#glossary-0 "Glossary term") function. By default, the aggregation function will aggregate over the set of possible records defined by the selection. |
| StructuredParameter | StructuredParameter consists of a [dimension](#glossary-1 "Glossary term") and optionally, sorting criteria in the format: (Dimension(Sort-type, Ordering))  The dimension is a single [field](#glossary-2 "Glossary term") and cannot be an expression. The dimension is used to determine the array of values the Aggr expression is calculated for.  If sorting criteria are included, the array of values created by the Aggr function, calculated for the dimension, is sorted. This is important when the sort order affects the result of the expression the Aggr function is enclosed in.  For details of how to use sorting criteria, see [Adding sorting criteria to the dimension in the structured parameter](#Sorting). |
| SetExpression | By default, the aggregation function will aggregate over the set of possible records defined by the selection. An alternative set of records can be defined by a set analysis expression. |
| DISTINCT | If the expression argument is preceded by the distinct qualifier or if no qualifier is used at all, each distinct combination of dimension values will generate only one return value. This is the normal way aggregations are made – each distinct combination of dimension values will render one line in the [chart](#glossary-3 "Glossary term"). |
| NODISTINCT | If the expression argument is preceded by the nodistinct qualifier, each combination of dimension values may generate more than one return value, depending on underlying data structure. If there is only one dimension, the aggr function will return an array with the same number of elements as there are rows in the source data. |

Basic aggregation functions, such as Sum, Min, and Avg, return a single numerical value, whereas the Aggr() function can be compared to creating a temporary staged result set (a virtual table), over which another aggregation can be made. For example, by computing an average sales value by summing the sales by customer in an Aggr() statement, and then calculating the average of the summed results: Avg(TOTAL Aggr(Sum(Sales),Customer)).

Tip noteUse the Aggr() function in calculated dimensions
if you want to create nested chart aggregations on multiple levels.

Limitations:

Each dimension in an Aggr() function
must be a single field, and cannot be an expression (calculated dimension).

Adding sorting criteria to the dimension in the structured parameter

In its basic form, the argument StructuredParameter in the Aggr function syntax is a single dimension. The expression: Aggr(Sum(Sales, Month)) finds the total value of sales for each month. However, when enclosed in another aggregation function, there can be unexpected results unless sorting criteria are used. This is because some dimensions can be sorted numerically or alphabetically, and so on.

In the StructuredParameter argument in the Aggr function, you can specify sorting criteria on the dimension in your expression. This way, you impose a sort order on the virtual table that is produced by the Aggr function.

The argument StructuredParameter has the following syntax:

(FieldName, (Sort-type, Ordering))

Structured parameters can be nested:

(FieldName, (FieldName2, (Sort-type, Ordering)))

Sort-type can be: NUMERIC, TEXT, FREQUENCY, or LOAD\_ORDER.

The Ordering types associated with each Sort-type are as follows:

Allowed ordering types

| Sort-type | Allowed Ordering types |
| --- | --- |
| NUMERIC | ASCENDING, DESCENDING, or REVERSE |
| TEXT | ASCENDING, A2Z, DESCENDING, REVERSE, or Z2A |
| FREQUENCY | DESCENDING, REVERSE or ASCENDING |
| LOAD\_ORDER | ASCENDING, ORIGINAL, DESCENDING, or REVERSE |

The ordering types REVERSE and DESCENDING are equivalent.

For Sort-type TEXT, the ordering types ASCENDING and A2Z are equivalent, and DESCENDING, REVERSE, and Z2A are equivalent.

For Sort-type LOAD\_ORDER, the ordering types ASCENDING and ORIGINAL are equivalent.

## Examples: Chart expressions using Aggr

Examples - chart expressions

### Chart expression example 1

#### Load script

Load the following data as an inline load in the data load editor to create the chart expression example below.

```
ProductData:

LOAD * inline [
Customer|Product|UnitSales|UnitPrice
Astrida|AA|4|16
Astrida|AA|10|15
Astrida|BB|9|9
Betacab|BB|5|10
Betacab|CC|2|20
Betacab|DD|25|25
Canutility|AA|8|15
Canutility|CC|0|19
] (delimiter is '|');
```

For more information about using inline loads, see [*Using inline loads to load data*](../Scripting/inline-loads-qs.htm).

#### Chart expression

Create a KPI [visualization](#glossary-4 "Glossary term") in a Qlik Sense [sheet](#glossary-5 "Glossary term"). Add the following expression to the KPI, as a [measure](#glossary-6 "Glossary term"):

Avg(Aggr(Sum(UnitSales\*UnitPrice), Customer))

#### Result

376.7

#### Explanation

The expression Aggr(Sum(UnitSales\*UnitPrice), Customer) finds the total value of sales by Customer, and returns an array of values: 295, 715, and 120 for the three Customer values.

Effectively, we have built a temporary list of values without having to create an explicit table or column containing those values.

These values are used as input to the Avg() function to find the average value of sales, 376.7.

For more information about expressions, see [*Using expressions in visualizations*](use-expressions-in-visualizations.htm).

### Chart expression example 2

#### Load script

Load the following data as an inline load in the data load editor to create the chart expression example below.

```
ProductData:

LOAD * inline [
Customer|Product|UnitSales|UnitPrice
Astrida|AA|4|16
Astrida|AA|10|15
Astrida|BB|10|15
Astrida|BB|9|9
Betacab|BB|5|10
Betacab|BB|7|12
Betacab|CC|2|22
Betacab|CC|4|20
Betacab|DD|25|25
Canutility|AA|8|15
Canutility|AA|5|11
Canutility|CC|0|19
] (delimiter is '|');
```

For more information about using inline loads, see [*Using inline loads to load data*](../Scripting/inline-loads-qs.htm).

#### Chart expression

Create a table visualization in a Qlik Sense sheet with  Customer, Product, UnitPrice, and UnitSales as dimensions. Add the following expression to the table, as a measure:

Aggr(NODISTINCT Max(UnitPrice), Customer, Product)

#### Result

| Customer | Product | UnitPrice | UnitSales | Aggr(NODISTINCT Max(UnitPrice), Customer, Product) |
| --- | --- | --- | --- | --- |
| Astrida | AA | 15 | 10 | 16 |
| Astrida | AA | 16 | 4 | 16 |
| Astrida | BB | 9 | 9 | 15 |
| Astrida | BB | 15 | 10 | 15 |
| Betacab | BB | 10 | 5 | 12 |
| Betacab | BB | 12 | 7 | 12 |
| Betacab | CC | 20 | 4 | 22 |
| Betacab | CC | 22 | 2 | 22 |
| Betacab | DD | 25 | 25 | 25 |
| Canutility | AA | 11 | 5 | 15 |
| Canutility | AA | 15 | 8 | 15 |
| Canutility | CC | 19 | 0 | 19 |

#### Explanation

An array of values: 16, 16, 15, 15, 12, 12, 22, 22, 25, 15, 15, and 19. The nodistinct qualifier means that the array contains one element for each row in the source data: each is the maximum UnitPrice for each Customer and Product.

### Chart expression example 3

#### Load script

Load the following data as an inline load in the data load editor to create the chart expression example below.

```
Set vNumberOfOrders = 1000;

OrderLines:
Load
	RowNo() as OrderLineID,
	OrderID,
	OrderDate,
	Round((Year(OrderDate)-2005)*1000*Rand()*Rand()*Rand1) as Sales
	While Rand()<=0.5 or IterNo()=1;
Load * Where OrderDate<=Today();
Load
	Rand() as Rand1,
	Date(MakeDate(2013)+Floor((365*4+1)*Rand())) as OrderDate,
	RecNo() as OrderID
	Autogenerate vNumberOfOrders;

Calendar:
Load distinct
	Year(OrderDate) as Year,
	Month(OrderDate) as Month,
	OrderDate
	Resident OrderLines;
```

#### Chart expressions

Create a table visualization in a Qlik Sense sheet with Year and Month as dimensions. Add the following expressions to the table as measures:

- Sum(Sales)
- Sum(Aggr( Rangesum(Above(Sum(Sales),0,12)), (Year, (Numeric, Ascending)), (Month, (Numeric, Ascending)) )) labeled as Structured Aggr() in the table.

#### Result

| Year | Month | Sum(Sales) | Structured Aggr() |
| --- | --- | --- | --- |
| 2013 | Jan | 53495 | 53495 |
| 2013 | Feb | 48580 | 102075 |
| 2013 | Mar | 25651 | 127726 |
| 2013 | Apr | 36585 | 164311 |
| 2013 | May | 61211 | 225522 |
| 2013 | Jun | 23689 | 249211 |
| 2013 | Jul | 42311 | 291522 |
| 2013 | Aug | 41913 | 333435 |
| 2013 | Sep | 28886 | 362361 |
| 2013 | Oct | 25977 | 388298 |
| 2013 | Nov | 44455 | 432753 |
| 2013 | Dec | 64144 | 496897 |
| 2014 | Jan | 67775 | 67775 |

#### Explanation

This example displays the aggregated values over a twelve month period for each year in chronological ascending order, hence the structured parameters (Numeric, Ascending) part of the Aggr() expression. Two specific dimensions are required as structured parameters: Year and Month, sorted (1) Year (numeric) and (2) Month (numeric). These two dimensions must be used in the table or chart visualization. This is necessary for the dimension list of the Aggr() function to correspond with the dimensions of the object used in the visualization.

You can compare the difference between these measures in a table or in separate line [charts](#glossary-7 "Glossary term"):

- Sum(Aggr(
  Rangesum(Above(Sum(Sales),0,12)),
  (Year),
  (Month)
  ))
- Sum(Aggr(
  Rangesum(Above(Sum(Sales),0,12)),
  (Year, (Numeric, Ascending)),
  (Month, (Numeric, Ascending))
  ))

It should be clear to see that only the latter expression performs the desired accumulation of aggregated values.

## Learn more

- [*Basic aggregation functions*](../Scripting/AggregationFunctions/basic-aggregation-functions.htm)
- [*Set analysis*](SetAnalysis/set-analysis-expressions.htm)
