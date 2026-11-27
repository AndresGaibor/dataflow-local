---
title: "NullAsValue"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/NullAsValue.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements"]
---

# NullAsValue

The NullAsValue statement specifies for which fields that NULL should be converted to a value.

Syntax:

NullAsValue \*fieldlist

By default, Qlik Sense considers NULL values to be missing or undefined
entities. However, certain database contexts imply that NULL values are
to be considered as special values rather than simply missing values.
The fact that NULL values are normally not allowed to link to other NULL
values can be suspended by means of the NullAsValue
statement.

The NullAsValue statement operates
as a switch and will operate on subsequent loading statements. It can be switched off again by means of the NullAsNull statement.

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| \*fieldlist | A comma separated list of the fields for which NullAsValue should be turned on. Using \* as field list indicates all fields. The wildcard characters \* and ? are allowed in field names. Quoting of field names may be necessary when wildcards are used. |

Example:

NullAsValue A,B;

Set NullValue = 'NULL';

LOAD A,B from x.csv;

## Learn more

- [*NULL value handling*](../null-value-handling.htm)
- [*NullAsNull*](NullAsNull.htm)
