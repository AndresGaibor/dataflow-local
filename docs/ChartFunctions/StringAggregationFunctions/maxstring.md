---
title: "MaxString - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/StringAggregationFunctions/maxstring.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "String aggregation functions"]
---

# MaxString - chart function

MaxString() finds string values in the expression or field and returns the last text value in alphabetical sort order.

Syntax:

MaxString({[SetExpression] [TOTAL [<fld{, fld}>]]} expr)

Return data type:  dual

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| expr | The expression or field containing the data to be measured. |
| SetExpression | By default, the aggregation function will aggregate over the set of possible records defined by the selection. An alternative set of records can be defined by a set analysis expression. |
| TOTAL | If the word TOTAL occurs before the function arguments, the calculation is made over all possible values given the current selections, and not just those that pertain to the current dimensional value, that is, it disregards the chart dimensions.  By using TOTAL [<fld {.fld}>], where the TOTAL qualifier is followed by a list of one or more field names as a subset of the chart dimension variables, you create a subset of the total possible values.  [*Defining the aggregation scope*](../define-aggregation-scope.htm) |

Limitations:

If the expression contains no values with a string representation NULL is returned.

Examples and results:

Results table

| SalesGroup | Amount | MaxString(Team) | MaxString(Date) |
| --- | --- | --- | --- |
| East | 14000 | Delta | 2013/08/01 |
| East | 20000 | Gamma | 2013/11/01 |
| East | 25000 | Alpha | 2013/07/01 |
| West | 14000 | Eta | 2013/10/01 |
| West | 17000 | Epsilon | 2013/09/01 |
| West | 19000 | Zeta | 2013/06/01 |
| West | 23000 | Theta | 2013/12/01 |

Function examples

| Example | Result |
| --- | --- |
| MaxString(Team) | There are three values of 20000 for the [dimension](#glossary-0 "Glossary term") Amount: two of Gamma (on different dates), and one of Beta. The result of the [measure](#glossary-1 "Glossary term") MaxString (Team) is therefore Gamma, because this is the highest value in the sorted strings. |
| MaxString(Date) | 2013/11/01 is the greatest Date value of the three associated with the dimension Amount. This assumes your script has the SET statement `SET DateFormat='YYYY-MM-DD';`' |

Data used in example:

TeamData:

LOAD \* inline [

SalesGroup|Team|Date|Amount

East|Gamma|01/05/2013|20000

East|Gamma|02/05/2013|20000

West|Zeta|01/06/2013|19000

East|Alpha|01/07/2013|25000

East|Delta|01/08/2013|14000

West|Epsilon|01/09/2013|17000

West|Eta|01/10/2013|14000

East|Beta|01/11/2013|20000

West|Theta|01/12/2013|23000

] (delimiter is '|');
