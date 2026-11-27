---
title: "HRank - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/RelationalFunctions/HRank.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Relational functions"]
---

# HRank - chart function

HRank() evaluates the expression, and compares the result with the result of the other columns containing the current row segment of a pivot table. The function then returns the ranking of the current column
within the segment.

Syntax:

HRank([ TOTAL ] expr
[ , mode [, fmt
] ])

Return data type:  dual

Information noteThis function only works in pivot tables. In all other chart types it returns NULL.

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| expr | The expression or field containing the data to be measured. |
| mode | Specifies the number representation of the function result. |
| fmt | Specifies the text representation of the function result. |
| TOTAL | If the chart is one-dimensional, or if the expression is preceded by the TOTAL qualifier, the function is evaluated along the entire column. If the table or table equivalent has multiple vertical dimensions, the current column segment will include only rows with the same values as the current row in all [dimension](#glossary-0 "Glossary term") columns except for the column showing the last dimension in the inter-field sort order.  [*Defining the aggregation scope*](../define-aggregation-scope.htm) |

If the pivot table is one-dimensional or if the expression is preceded by the total qualifier, the current row segment is always equal to the entire row. If the pivot table has multiple horizontal dimensions, the current row segment will include
only columns with the same values as the current column in all dimension rows except for the row showing the last horizontal dimension of the inter-field sort order.

The ranking is returned as a dual value, which in the case when each
column has a unique ranking will be an integer between 1 and the number
of columns in the current row segment.

In the case where several columns share the same ranking, the text and number representation can be controlled with the mode and format arguments.

The second argument, mode, specifies the number representation of the function result:

mode examples

| Value | Description |
| --- | --- |
| 0 (default) | If all ranks within the sharing group fall on the low side of the middle value of the entire ranking, all columns get the lowest rank within the sharing group.  If all ranks within the sharing group fall on the high side of the middle value of the entire ranking, all columns get the highest rank within the sharing group.  If ranks within the sharing group span over the middle value of the entire ranking, all rows get the value corresponding to the average of the top and bottom ranking in the entire column segment. |
| 1 | Lowest rank on all columns in the group. |
| 2 | Average rank on all columns in the group. |
| 3 | Highest rank on all columns in the group. |
| 4 | Lowest rank on first column, then incremented by one for each column in the group. |

The third argument, format,
specifies the text representation of the function result:

format examples

 | Value | Description |
| --- | --- |
| 0 (default) | Low value&' - '&high value on all columns in the group (for example 3 - 4). |
| 1 | Low value on all columns in the group. |
| 2 | Low value on first column, blank on the following columns in the group. |

The order of columns for mode 4 and format 2 is determined by the sort order of the chart dimensions.

Examples:

HRank( sum(
Sales ))

HRank( sum(
Sales ), 2 )

HRank( sum(
Sales ), 0, 1 )
