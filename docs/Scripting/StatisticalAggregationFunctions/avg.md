---
title: "Avg Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalAggregationFunctions/avg.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Statistical aggregation functions"]
---
# Avg Script function

Avg() finds the average value of the aggregated data in the expression over
a number of records as defined by a group by clause.

Syntax:

Avg([DISTINCT] expr)

Return data type: numeric

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| expr | The expression or field containing the data to be measured. |
| DISTINCT | If the word distinct occurs before the expression, all duplicates will be disregarded. |

Examples and results:

Add the example script to your application and run it. To see the result, add the fields listed in the results column to a sheet in your application.

Resulting data

| Example | Result |
| --- | --- |
| Temp:  crosstable (Month, Sales) load \* inline [  Customer|Jan|Feb|Mar||Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec  Astrida|46|60|70|13|78|20|45|65|78|12|78|22  Betacab|65|56|22|79|12|56|45|24|32|78|55|15  Canutility|77|68|34|91|24|68|57|36|44|90|67|27  Divadip|36|44|90|67|27|57|68|47|90|80|94  ] (delimiter is '|');    Avg1:  LOAD Customer, Avg(Sales) as MyAverageSalesByCustomer Resident Temp Group By Customer; | Customer MyAverageSalesByCustomer  Astrida 48.916667  Betacab 44.916667  Canutility 56.916667  Divadip 63.083333 This can be checked in the [sheet](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalAggregationFunctions/avg.htm#glossary-0 "Glossary term") by creating a table including the [measure](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalAggregationFunctions/avg.htm#glossary-1 "Glossary term") . `Sum(Sales)/12` |
| Given that the Temp table is loaded as in the previous example:  LOAD Customer,Avg(DISTINCT Sales) as MyAvgSalesDistinct Resident Temp Group By Customer; | Customer MyAverageSalesByCustomer  Astrida 43.1  Betacab 43.909091  Canutility 55.909091  Divadip 61 Only the distinct values are counted. Divide the total by the number of non-duplicate values. |
