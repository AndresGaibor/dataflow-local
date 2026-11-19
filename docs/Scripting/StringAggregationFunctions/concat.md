---
title: "Concat Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringAggregationFunctions/concat.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "String aggregation functions"]
---
# Concat Script function

Concat() is used to combine string values. The script function returns the
aggregated string concatenation of all values of the expression iterated over
a number of records as defined by a group by clause.

Syntax:

Concat ([ distinct
] string [, delimiter [, sort\_weight]])

Return data type: string

Arguments:

The expression or field containing the string to be processed.

Arguments

| Argument | Description |
| --- | --- |
| string | The expression or field containing the string to be processed. |
| delimiter | Each value may be separated by the string found in delimiter. |
| sort\_weight | The order of concatenation may be determined by the value of the dimension sort\_weight, if present, with the string corresponding to the lowest value appearing first in the concatenation. When 0 is used as the sort\_weight argument value, sorting is not applied to the output. If the sort\_weight argument is omitted, the function defaults to alphanumeric sorting. |
| distinct | If the word distinct occurs before the expression, all duplicates are disregarded. |

Examples and results:

Add the example script to your application and run it. To see the result, add the fields listed in the results column to a sheet in your application.

Examples and results

| Example | Result | Results once added to a sheet |
| --- | --- | --- |
| TeamData:  LOAD \* inline [  SalesGroup|Team|Date|Amount  East|Gamma|01/05/2013|20000  East|Gamma|02/05/2013|20000  West|Zeta|01/06/2013|19000  East|Alpha|01/07/2013|25000  East|Delta|01/08/2013|14000  West|Epsilon|01/09/2013|17000  West|Eta|01/10/2013|14000  East|Beta|01/11/2013|20000  West|Theta|01/12/2013|23000  ] (delimiter is '|');    Concat1:  LOAD SalesGroup,Concat(Team) as TeamConcat1 Resident TeamData Group By SalesGroup; | SalesGroup  East  West | TeamConcat1  AlphaBetaDeltaGammaGamma  EpsilonEtaThetaZeta |
| Given that the TeamData table is loaded as in the previous example:  LOAD SalesGroup,Concat(distinct Team,'-') as TeamConcat2 Resident TeamData Group By SalesGroup; | SalesGroup  East  West | TeamConcat2  Alpha-Beta-Delta-Gamma  Epsilon-Eta-Theta-Zeta |
| Given that the TeamData table is loaded as in the previous example. Because the argument for sort\_weight is added, the results are ordered by the value of the [dimension](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringAggregationFunctions/concat.htm#glossary-0 "Glossary term") Amount:  LOAD SalesGroup,Concat(distinct Team,'-',Amount) as TeamConcat2 Resident TeamData Group By SalesGroup; | SalesGroup  East  West | TeamConcat3  Delta-Beta-Gamma-Alpha  Eta-Epsilon-Zeta-Theta |
| Given that the TeamData table is loaded as in the previous example. Because the argument for sort\_weight is 0, the results are not sorted:  ConcatNoSort:  LOAD SalesGroup,Concat(Team,'-',0) as TeamConcat4 Resident TeamData Group By SalesGroup; | SalesGroup  East  West | TeamConcat4  Gamma-Gamma-Alpha-Delta-Beta  Zeta-Epsilon-Eta-Theta |
