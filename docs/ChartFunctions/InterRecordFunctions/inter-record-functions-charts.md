---
title: "Inter-record functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/InterRecordFunctions/inter-record-functions-charts.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions"]
---

# Inter-record functions

Expand/Collapse all

# Inter-record functions

Inter-record functions are used:

- In the data load script, when a value from previously loaded records
  of data is needed for the evaluation of the current record.
- In a chart expression, when another value from the data set of a visualization is needed.

Information note

Sorting on y-values in charts or sorting by expression columns in tables is not allowed when an inter-record chart function is used in any of the chart's expressions. These sort alternatives are therefore automatically disabled. When you use an inter-record chart function in a visualization or table, the sorting of the visualization will revert back to the sorted input to the inter-record function. This limitation does not apply to the equivalent script function, if there is one.

Information noteSelf-referencing expression definitions can only reliably be made in tables with fewer than 100 rows, but this may vary depending on the hardware that the Qlik engine is running on.

Use the drop-down on each function to see a brief description and the syntax of each function. Click the function name in the syntax description for further details.

## Row functions

These functions can only be used in chart expressions.

Above

Above() evaluates an expression at a row above the current row within a column segment in a table. The row for which it is calculated depends on the value of offset, if present, the default being the row directly above. For charts other than tables, Above() evaluates for the row above the current row in the chart's straight table equivalent.

[**above**](above.htm)([TOTAL [<fld{,fld}>]] expr
[ , offset [,count]])

Below

Below() evaluates an expression at a row below the current row within a column segment in a table. The row for which it is calculated depends on the value of offset, if present, the default being the row directly below. For charts other than tables, Below() evaluates for the row below the current column in the chart's straight table equivalent.

[**below**](below.htm)([TOTAL[<fld{,fld}>]] expression
[ , offset [,count
]])

Bottom

Bottom() evaluates an expression at the last (bottom) row of a column segment in a table. The row for which it is calculated depends on the value of offset, if present, the default being the bottom row. For
charts other than tables, the evaluation is made on the last row of the current column in the chart's straight table equivalent.

[**bottom**](bottom.htm)([TOTAL[<fld{,fld}>]] expr
[ , offset [,count
]])

Top

Top() evaluates an expression at the first (top) row of a column segment in a table. The row for which it is calculated depends on the value of offset, if present, the default being the top row. For charts other than tables, theTop() evaluation is made on the first row of the current column in the chart's straight table equivalent.

[**top**](top.htm)([TOTAL [<fld{,fld}>]] expr [ , offset [,count
]])

NoOfRows

NoOfRows() returns the number of rows in the current column segment in a table. For bitmap charts, NoOfRows() returns the number of rows in the chart's straight table equivalent.

[**noofrows**](noofrows.htm)([TOTAL])

## Column functions

These functions can only be used in chart expressions.

Column

Column() returns the value found in the column corresponding to ColumnNo in a straight table, disregarding dimensions. For example Column(2) returns the value of the second measure column.

[**column**](column.htm)(ColumnNo)

Dimensionality

Dimensionality() returns the number of dimensions for the current row. In the case of pivot tables, the function returns the total number of dimension columns that have non-aggregation content, that is, do not contain partial
sums or collapsed aggregates.

[**dimensionality**](dimensionality.htm) ( )

Secondarydimensionality

SecondaryDimensionality() returns the number of dimension
pivot table rows that have non-aggregation content, that is, do not contain
partial sums or collapsed aggregates. This function is the equivalent
of the dimensionality() function for horizontal pivot table dimensions.

[**secondarydimensionality**](secondarydimensionality.htm) ( )

## Field functions

FieldIndex

FieldIndex() returns the position of the field value value in the field field\_name (by load
order).

[**fieldindex**](fieldindex.htm)(field\_name ,
value)

FieldValue

FieldValue() returns the value found in position elem\_no of the field field\_name (by load
order).

[**fieldvalue**](fieldvalue.htm)(field\_name , elem\_no)

FieldValueCount

FieldValueCount() is an integer function that returns
the number of distinct values in a field.

[**fieldvaluecount**](fieldvaluecount.htm)(field\_name)

## Pivot table functions

These functions can only be used in chart expressions.

After

After() returns the value of an expression
evaluated with a pivot table's dimension values as they appear in the
column after the current column within a row segment in the pivot table.

[**after**](after.htm)([TOTAL] expression
[ , offset [,n]])

Before

Before() returns the value of an expression
evaluated with a pivot table's dimension values as they appear in the
column before the current column within a row segment in the pivot table.

[**before**](before.htm)([TOTAL] expression
[ , offset [,n]])

First

First() returns the value of an expression
evaluated with a pivot table's dimension values as they appear in the
first column of the current row segment in the pivot table. This function
returns NULL in all chart types except pivot tables.

[**first**](first.htm)([TOTAL] expression
[ , offset [,n]])

Last

Last() returns the value of
an expression evaluated with a pivot table's dimension values as they appear in the
last column of the current row segment in the pivot table. This function
returns NULL in all chart types except pivot tables.

[**last**](last.htm)([TOTAL] expression
[ , offset [,n]])

ColumnNo

ColumnNo() returns the number of the current column within the current row segment
in a pivot table. The first column is number 1.

[**columnno**](columnno.htm)([TOTAL])

NoOfColumns

NoOfColumns() returns the number of columns in the current row segment in a pivot
table.

[**noofcolumns**](noofcolumns.htm)([TOTAL])

## Inter-record functions in the data load script

Exists

Exists() determines whether a specific field
value has already been loaded into the field in the data load script. The function returns TRUE or FALSE, so it can be used in the where clause of a LOAD statement or an IF statement.

[**Exists**](../../Scripting/InterRecordFunctions/Exists.htm)(field\_name
[, expr])

LookUp

LookUp() looks into a table that is already loaded and returns the value of field\_name corresponding to the first
occurrence of the value match\_field\_value
in the field match\_field\_name.
The table can be the current table or another table previously loaded.

[**LookUp**](../../Scripting/InterRecordFunctions/LookUp.htm)(field\_name,
match\_field\_name, match\_field\_value [, table\_name])

Peek

Peek() returns the value of a field in a table for a row that has already been loaded. The row number can be specified, as can the table. If no row number is specified, the last previously loaded record will be used.

[**Peek**](../../Scripting/InterRecordFunctions/Peek.htm)(field\_name[, row\_no[, table\_name ] ])

Previous

Previous() finds the value of the expr expression using data from the previous input record that has not been discarded because of
a where clause. In the first record
of an internal table, the function will return NULL.

[**Previous**](../../Scripting/InterRecordFunctions/Previous.htm)(expr)

## Learn more

- [*Range functions*](../RangeFunctions/RangeFunctionsInCharts.htm)
