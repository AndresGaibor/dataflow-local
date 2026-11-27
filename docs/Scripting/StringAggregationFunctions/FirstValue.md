---
title: "FirstValue Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringAggregationFunctions/FirstValue.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "String aggregation functions"]
---

# FirstValue Script function

FirstValue() returns the value that was loaded first from the
records defined by the expression, sorted by a group by clause.

Information noteThis function is only available as a script function.

Syntax:

FirstValue ( expr)

Return data type: dual

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| expr | The expression or field containing the data to be measured. |

Limitations:

If no text value is found, NULL is returned.

Examples and results:

Add the example script to your application and run it. To see the result, add the fields listed in the results column to a sheet in your application.

Resulting data

| Example | Result | Results on a sheet |
| --- | --- | --- |
| TeamData:  LOAD \* inline [  SalesGroup|Team|Date|Amount  East|Gamma|01/05/2013|20000  East|Gamma|02/05/2013|20000  West|Zeta|01/06/2013|19000  East|Alpha|01/07/2013|25000  East|Delta|01/08/2013|14000  West|Epsilon|01/09/2013|17000  West|Eta|01/10/2013|14000  East|Beta|01/11/2013|20000  West|Theta|01/12/2013|23000  ] (delimiter is '|');    FirstValue1:  LOAD SalesGroup,FirstValue(Team) as FirstTeamLoaded Resident TeamData Group By SalesGroup; | SalesGroup  East  West | FirstTeamLoaded  Gamma  Zeta |
