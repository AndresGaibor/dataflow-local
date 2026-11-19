---
title: "MaxString Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringAggregationFunctions/MaxString.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "String aggregation functions"]
---
# MaxString Script function

MaxString() finds string values in the expression and returns the last text value sorted
alphabetically over a number of records, as defined by a group
by clause.

Syntax:

MaxString ( expr
)

Return data type: dual

Arguments:

| Argument | Description |
| --- | --- |
| expr | The expression or field containing the data to be measured. |

Limitations:

If no text value is found, NULL is returned.

Examples and results:

Add the example script to your application and run it. To see the result, add the fields listed in the results column to a sheet in your application.

| Example | Result |  |
| --- | --- | --- |
| TeamData:  LOAD \* inline [  SalesGroup|Team|Date|Amount  East|Gamma|01/05/2013|20000  East|Gamma|02/05/2013|20000  West|Zeta|01/06/2013|19000  East|Alpha|01/07/2013|25000  East|Delta|01/08/2013|14000  West|Epsilon|01/09/2013|17000  West|Eta|01/10/2013|14000  East|Beta|01/11/2013|20000  West|Theta|01/12/2013|23000  ] (delimiter is '|');    Concat1:  LOAD SalesGroup,MaxString(Team) as MaxString1 Resident TeamData Group By SalesGroup; | SalesGroup  East  West | MaxString1  Gamma  Zeta |
| Given that the TeamData table is loaded as in the previous example, and your [data load script](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringAggregationFunctions/MaxString.htm#glossary-0 "Glossary term")has the SET statement: `SET DateFormat='DD/MM/YYYY';`':  LOAD SalesGroup,MaxString(Date) as MaxString2 Resident TeamData Group By SalesGroup; | SalesGroup  East  West | MaxString2  01/11/2013  01/12/2013 |
