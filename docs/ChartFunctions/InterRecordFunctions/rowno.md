---
title: "RowNo - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/InterRecordFunctions/rowno.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Counter functions"]
---

# RowNo - chart function

RowNo() returns the number of the current row within the current column segment
in a table. For bitmap charts, RowNo() returns the number of the current row within the chart's straight table equivalent.

If the table or table equivalent has multiple vertical dimensions, the
current column segment will include only rows with the same values as
the current row in all dimension columns, except for the column showing the last dimension in the inter-field sort order.

Column segments

![A table showing column segments](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/table_column_segments.png)

Information noteSorting on y-values in charts or sorting by expression columns in tables is not allowed when this chart function is used in any of the chart's expressions. These sort alternatives are therefore automatically disabled. When you use this chart function in a visualization or table, the sorting of the visualization will revert back to the sorted input to this function.

Syntax:

RowNo([TOTAL])

Return data type:  integer

Arguments:

| Argument | Description |
| --- | --- |
| TOTAL | If the table is one-dimensional or if the qualifier TOTAL is used as argument, the current column segment is always equal to the entire column.  [*Defining the aggregation scope*](../define-aggregation-scope.htm) |

## Example: Chart expression using RowNo

Example - chart expression

### Load script

Load the following data as an inline load in the data load editor to create the chart expression examples below.

```
Temp:
LOAD * inline [
Customer|Product|OrderNumber|UnitSales|UnitPrice
Astrida|AA|1|4|16
Astrida|AA|7|10|15
Astrida|BB|4|9|9
Betacab|CC|6|5|10
Betacab|AA|5|2|20
Betacab|BB|1|25| 25
Canutility|AA|3|8|15
Canutility|CC|5|4|19
Divadip|CC|2|4|16
Divadip|DD|3|1|25
] (delimiter is '|');
```

For more information about using inline loads, see [*Using inline loads to load data*](../../Scripting/inline-loads-qs.htm).

### Chart expression

Create a table [visualization](#glossary-0 "Glossary term") in a Qlik Sense [sheet](#glossary-1 "Glossary term") with Customer and UnitSales as [dimensions](#glossary-2 "Glossary term"). Add RowNo( ) and RowNo(TOTAL) as [measures](#glossary-3 "Glossary term") labeled Row in Segment and Row Number, respectively.
Add the following expression to the table as a measure.

If( RowNo( )=1, 0, UnitSales / Above( UnitSales ))

### Result

| Customer | UnitSales | Row in Segment | Row Number | If( RowNo( )=1, 0, UnitSales / Above( UnitSales )) |
| --- | --- | --- | --- | --- |
| Astrida | 4 | 1 | 1 | 0 |
| Astrida | 9 | 2 | 2 | 2.25 |
| Astrida | 10 | 3 | 3 | 1.1111111111111 |
| Betacab | 2 | 1 | 4 | 0 |
| Betacab | 5 | 2 | 5 | 2.5 |
| Betacab | 25 | 3 | 6 | 5 |
| Canutility | 4 | 1 | 7 | 0 |
| Canutility | 8 | 2 | 8 | 2 |
| Divadip | 1 | 1 | 9 | 0 |
| Divadip | 4 | 2 | 10 | 4 |

### Explanation

The Row in Segment column shows the results 1,2,3 for the column segment containing the values of UnitSales for customer Astrida. The row numbering then begins at 1 again for the next column segment, which is Betacab.

The Row Number column disregards the dimensions because of the TOTAL argument for RowNo() and counts the rows in the table.

This expression returns 0 for the first row in each column segment, so the column shows:

0, 2.25, 1.1111111, 0, 2.5, 5, 0, 2, 0, and 4.

For more information about expressions, see [*Using expressions in visualizations*](../use-expressions-in-visualizations.htm).

## Learn more

- [*Above - chart function*](above.htm)
