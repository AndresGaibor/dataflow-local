---
title: "Keep"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Keep.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script prefixes"]
---

# Keep

The keep prefix is similar to the join prefix. Just as the join prefix, it compares the loaded table with an existing named table or the last previously created data table, but instead of joining the loaded table with an existing table, it has the effect of reducing one or both of the two tables before they are stored in Qlik Sense, based on the intersection of table data. The comparison made is equivalent to a natural join made over all the common fields, i.e. the same way as in a corresponding join. However, the two tables are not joined and will be kept in Qlik Sense as two separately named tables.

Syntax:

(inner | left | right) keep [(tablename ) ]( loadstatement | selectstatement )

The keep prefix must be preceded by one of the prefixes inner, left or right.

The explicit join prefix in Qlik Sense script language performs a full join of the two tables. The result is one table. In many cases such joins will result in very large tables. One of the main features of Qlik Sense is its ability to make associations between multiple tables instead of joining them, which greatly reduces memory usage, increases processing speed and offers enormous flexibility. Explicit joins should therefore generally be avoided in Qlik Sense scripts. The keep functionality was designed to reduce the number of cases where explicit joins needs to be used.

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| tablename | The named table to be compared to the loaded table. |
| loadstatement or selectstatement | The LOAD or SELECT statement for the loaded table. |

Example:

Inner Keep LOAD \* from abc.csv;

Left Keep SELECT \* from table1;

tab1:

LOAD \* from file1.csv;

tab2:

LOAD \* from file2.csv;

.. .. ..

Left Keep (tab1) LOAD \* from file3.csv;

## Learn more

- [*Join*](Join.htm)
- [*Load*](../ScriptRegularStatements/Load.htm)
- [*Inner*](Inner.htm)
- [*Select*](../ScriptRegularStatements/Select.htm)
- [*Left*](Left.htm)
- [*Right*](Right.htm)
