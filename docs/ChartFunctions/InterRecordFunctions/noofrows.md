---
title: "NoOfRows Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/InterRecordFunctions/noofrows.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Inter-record functions"]
---

# NoOfRows Script and chart function

NoOfRows() returns the number of rows in the current column segment in a table. For bitmap charts, NoOfRows() returns the number of rows in the chart's straight table equivalent.

If the table or table equivalent has multiple vertical dimensions, the
current column segment will include only rows with the same values as
the current row in all dimension columns, except for the column showing the last dimension in the inter-field sort order.

Information noteSorting on y-values in charts or sorting by expression columns in tables is not allowed when this chart function is used in any of the chart's expressions. These sort alternatives are therefore automatically disabled. When you use this chart function in a visualization or table, the sorting of the visualization will revert back to the sorted input to this function.

Syntax:

NoOfRows([TOTAL])

Return data type:  integer

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| TOTAL | If the table is one-dimensional or if the qualifier TOTAL is used as argument, the current column segment is always equal to the entire column.  [*Defining the aggregation scope*](../define-aggregation-scope.htm) |

## Example: Chart expression using NoOfRows

Example - chart expression

### Load script

Load the following data as an inline load in the data load editor to create the chart expression examples below.

```
	Temp:
LOAD * inline [
Region|SubRegion|RowNo()|NoOfRows()
Africa|Eastern
Africa|Western
Americas|Central
Americas|Northern
Asia|Eastern
Europe|Eastern
Europe|Northern
Europe|Western
Oceania|Australia
] (delimiter is '|');
```

For more information about using inline loads, see [*Using inline loads to load data*](../../Scripting/inline-loads-qs.htm).

### Chart expression

Create a table [visualization](#glossary-0 "Glossary term") in a Qlik Sense [sheet](#glossary-1 "Glossary term") with Region and SubRegion as [dimensions](#glossary-2 "Glossary term"). Add RowNo( ),  NoOfRows(), and NoOfRows(Total) as [measures](#glossary-3 "Glossary term").

### Result

| Region | SubRegion | RowNo() | NoOfRows() | NoOfRows(Total) |
| --- | --- | --- | --- | --- |
| Africa | Eastern | 1 | 2 | 9 |
| Africa | Western | 2 | 2 | 9 |
| Americas | Central | 1 | 2 | 9 |
| Americas | Northern | 2 | 2 | 9 |
| Asia | Eastern | 1 | 1 | 9 |
| Europe | Eastern | 1 | 3 | 9 |
| Europe | Northern | 2 | 3 | 9 |
| Eurrope | Western | 3 | 3 | 9 |
| Oceania | Australia | 1 | 1 | 9 |

### Explanation

In this example, the sort order is by the first dimension Region. As a result, each column segment is made up of a group of regions that has the same value, for example, Africa.

The RowNo() column shows the row numbers for each column segment, for example, there are two rows for the Africa region. The row numbering then begins at 1 again for the next column segment, which is Americas.

The  NoOfRows() column counts the number of rows in each column segment, for example, Europe has three rows in the column segment.

The NoOfRows(Total) column disregards the dimensions because of the TOTAL argument for NoOfRows() and counts the rows in the table.

If the table was sorted on the second dimension, SubRegion, the column segments would be based on that dimension so the row numbering would change for each SubRegion.

For more information about expressions, see [*Using expressions in visualizations*](../use-expressions-in-visualizations.htm).

## Learn more

- [*RowNo - chart function*](rowno.htm)
