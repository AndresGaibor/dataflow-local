---
title: "Table functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/TableFunctions/table-functions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions"]
---
Expand/Collapse all

# Table functions

The table functions return information about the data table which is
currently being read. If no table name is specified and the function is
used within a LOAD statement,
the current table is assumed.

All functions can be used in the data load script, while only NoOfRows can be used in a chart expression.

Use the drop-down on each function to see a brief description and the syntax of each function. For some of the functions, you can get further details about that specific function by clicking the function name in the syntax description.

FieldName

The FieldName script function returns the name of the field with the specified number within a previously
loaded table. If the function is used within a LOAD statement, it
must not reference the table currently being loaded.

[**FieldName**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/TableFunctions/FieldName.htm)(field\_number ,table\_name)

FieldNumber

The FieldNumber script function returns the number of a specified field within a previously loaded
table. If the function is used within a LOAD statement, it must not reference
the table currently being loaded.

[**FieldNumber**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/TableFunctions/FieldNumber.htm)(field\_name ,table\_name)

NoOfFields

The NoOfFields script function returns the number of fields in a previously loaded table. If
the function is used within a LOAD statement, it must not reference the
table currently being loaded.

[**NoOfFields**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/TableFunctions/NoOfFields.htm)(table\_name)

NoOfRows

The NoOfRows function returns the number of rows (records) in a previously loaded table.
If the function is used within a LOAD statement, it must not reference
the table currently being loaded.

[**NoOfRows**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/TableFunctions/NoOfRows.htm)(table\_name)

NoOfTables

This script function returns
the number of tables previously loaded.

NoOfTables()

TableName

This script function returns the name of the table with the specified number.

TableName(table\_number)

TableNumber

This script function returns the number of the specified table. The first table has number 0.

If table\_name does not exist, NULL is returned.

TableNumber(table\_name)

Example:

In this example, we want to create a table with information about the tables and fields that have been loaded.

First we load some sample data. This creates the two tables that will be used to illustrate the table functions described in this section.

Characters:
Load Chr(RecNo()+Ord('A')-1) as Alpha, RecNo() as Num autogenerate 26;
ASCII:
Load
if(RecNo()>=65 and RecNo()<=90,RecNo()-64) as Num,
Chr(RecNo()) as AsciiAlpha,
RecNo() as AsciiNum
autogenerate 255
Where (RecNo()>=32 and RecNo()<=126) or RecNo()>=160 ;

Next, we iterate through the tables that have been loaded, using the NoOfTables function, and then through the fields of each table, using the NoOfFields function, and load information using the table functions.

//Iterate through the loaded tables
For t = 0 to NoOfTables() - 1
//Iterate through the fields of table
For f = 1 to NoOfFields(TableName($(t)))
Tables:
Load
TableName($(t)) as Table,
TableNumber(TableName($(t))) as TableNo,
NoOfRows(TableName($(t))) as TableRows,
FieldName($(f),TableName($(t))) as Field,
FieldNumber(FieldName($(f),TableName($(t))),TableName($(t))) as FieldNo
Autogenerate 1;
Next f
Next t;

The resulting table Tables will look like this:

Load table

| Table | TableNo | TableRows | Field | FieldNo |
| --- | --- | --- | --- | --- |
| Characters | 0 | 26 | Alpha | 1 |
| Characters | 0 | 26 | Num | 2 |
| ASCII | 1 | 191 | Num | 1 |
| ASCII | 1 | 191 | AsciiAlpha | 2 |
| ASCII | 1 | 191 | AsciiNum | 3 |
