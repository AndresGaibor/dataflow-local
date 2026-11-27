---
title: "Concat - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/StringAggregationFunctions/concat.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "String aggregation functions"]
---

# Concat - chart function

Concat() is used to combine string values. The function returns the aggregated string concatenation of all the values of the expression evaluated over each dimension.

Syntax:

Concat({[SetExpression] [DISTINCT] [TOTAL [<fld{, fld}>]]} string[, delimiter[, sort\_weight]])

Return data type:  string

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| string | The expression or field containing the string to be processed. |
| delimiter | Each value may be separated by the string found in delimiter. |
| sort\_weight | The order of concatenation may be determined by the value of the dimension sort\_weight, if present, with the string corresponding to the lowest value appearing first in the concatenation. When 0 is used as the sort\_weight argument value, sorting is not applied to the output. If the sort\_weight argument is omitted, the function defaults to alphanumeric sorting. |
| SetExpression | By default, the aggregation function will aggregate over the set of possible records defined by the selection. An alternative set of records can be defined by a set analysis expression. |
| DISTINCT | If the word DISTINCT occurs before the function arguments, duplicates resulting from the evaluation of the function arguments are disregarded. |
| TOTAL | If the word TOTAL occurs before the function arguments, the calculation is made over all possible values given the current selections, and not just those that pertain to the current dimensional value, that is, it disregards the chart dimensions.  By using TOTAL [<fld {.fld}>], where the TOTAL qualifier is followed by a list of one or more field names as a subset of the chart dimension variables, you create a subset of the total possible values.  [*Defining the aggregation scope*](../define-aggregation-scope.htm) |

Examples and results:

Results table

| SalesGroup | Amount | Concat(Team) | Concat(TOTAL <SalesGroup> Team) | Concat(Team, ', ', 0) | Concat(TOTAL <SalesGroup> Team, '', 0) |
| --- | --- | --- | --- | --- | --- |
| East | 14000 | Delta | AlphaBetaDeltaGammaGamma | Delta | GammaGammaAlphaDeltaBeta |
| East | 20000 | BetaGammaGamma | AlphaBetaDeltaGammaGamma | GammaGammaBeta | GammaGammaAlphaDeltaBeta |
| East | 25000 | Alpha | AlphaBetaDeltaGammaGamma | Alpha | GammaGammaAlphaDeltaBeta |
| West | 14000 | Eta | EpsilonEtaThetaZeta | Eta | ZetaEpsilonEtaTheta |
| West | 17000 | Epsilon | EpsilonEtaThetaZeta | Epsilon | ZetaEpsilonEtaTheta |
| West | 19000 | Zeta | EpsilonEtaThetaZeta | Zeta | ZetaEpsilonEtaTheta |
| West | 23000 | Theta | EpsilonEtaThetaZeta | Theta | ZetaEpsilonEtaTheta |

Function examples

| Example | Result |
| --- | --- |
| Concat(Team) | The table is constructed from the [dimensions](#glossary-0 "Glossary term") SalesGroup and Amount, and variations on the [measure](#glossary-1 "Glossary term") Concat(Team). Ignoring the Totals result, note that even though there is data for eight values of Team spread across two values of SalesGroup, the only result of the measure Concat(Team) that concatenates more than one Team string value in the table is the row containing the dimension Amount 20000, which gives the result BetaGammaGamma. This is because there are three values for the Amount 20000 in the input data. All other results remain unconcatenated when the measure is spanned across the dimensions because there is only one value of Team for each combination of SalesGroup and Amount. |
| Concat(DISTINCT Team,', ') | Beta, Gamma. because the DISTINCT qualifier means the duplicate Gamma result is disregarded. Also, the delimiter argument is defined as a comma followed by a space. |
| Concat (TOTAL <SalesGroup> Team) | All the string values for all values of Team are concatenated if the TOTAL qualifier is used. With the [field](#glossary-2 "Glossary term") selection <SalesGroup> specified, this divides the results into the two values of the dimension SalesGroup. For the SalesGroupEast, the results are AlphaBetaDeltaGammaGamma. For the SalesGroupWest, the results are EpsilonEtaThetaZeta. |
| Concat (TOTAL <SalesGroup> Team,';', Amount) | By adding the argument for sort\_weight: Amount, the results are ordered by the value of the dimension Amount. The results becomes DeltaBetaGammaGammaAlpha and EtaEpsilonZEtaTheta. |
| Concat(Team, '', 0) | With sort\_weight set to 0, the results are not sorted. |
| Concat(TOTAL <SalesGroup> Team, '', 0) | With sort\_weight set to 0, the results are not sorted. Additionally, all the string values for all values of Team are concatenated because the TOTAL qualifier is used. |

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
