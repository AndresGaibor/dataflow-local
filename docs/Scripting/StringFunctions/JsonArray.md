---
title: "JsonArray Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/JsonArray.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "String functions"]
---
# JsonArray Script and chart function

JsonArray aggregates and concatenates JSON data.

Syntax:

JsonArray([DISTINCT][TOTAL] value [, sort\_weight])

Return data type: dual

Arguments

| Argument | Description |
| --- | --- |
| DISTINCT | If the word DISTINCT occurs before the function arguments, duplicates resulting from the evaluation of the function arguments are disregarded. |
| TOTAL | If the word TOTAL occurs before the function arguments, the calculation is made over all possible values given the current selections, and not just those that pertain to the current dimensional value, that is, it disregards the chart dimensions. |
| value | Input field. The expression containing the data to be sorted. The first (lowest) value of sort\_weight is found, from which the corresponding value of the value expression is determined. If you place a minus sign in front of sort\_weight, the function returns the last (highest) sorted value instead. |
| sort\_weight | Input field. The expression containing the data to be sorted. The first (lowest) value of sort\_weight is found, from which the corresponding value of the value expression is determined. If you place a minus sign in front of sort\_weight, the function returns the last (highest) sorted value instead. |

Example:

The following load script loads and aggregates data with **JsonArray**.

Data:
LOAD Id,
JsonArray(ValueOrNull) AS Json,
JsonArray(DISTINCT ValueOrNull) AS JsonDistinct,
JsonArray(ValueOrNull, Order) AS JsonSorted
GROUP BY Id;
LOAD \*, If(Value='-',Null(),Value) AS ValueOrNull;
LOAD \* INLINE '
Id | Value | Order
1 | 123 | 1
2 | "json text" | 2
2 | normal text | 1
3 | [1,2,3] | 3
3 | {"name":"abc"} | 2
3 | [1,2,3] | 1
4 | 1 | 1
4 | 2 and text | 2
4 | | 3
4 | - | 4
' (delimiter is '|');

This results in the following table of data:

Results

| Id | Json | JsonDistinct | JsonSorted |
| --- | --- | --- | --- |
| 1 | [123] | [123] | [123] |
| 2 | ["json text","normal text"] | ["json text","normal text"] | ["normal text","json text"] |
| 3 | [[1,2,3],[1,2,3],{"name":"abc"}] | [[1,2,3],{"name":"abc"}] | [[1,2,3],{"name":"abc"},[1,2,3]] |
| 4 | [1,"2 and text",""] | [1,"2 and text",""] | [1,"2 and text",""] |
