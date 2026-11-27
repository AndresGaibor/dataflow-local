---
title: "Inner"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Inner.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script prefixes"]
---

# Inner

The join and keep prefixes can be preceded by the prefix inner. If used before join it specifies
that an inner join should be used. The resulting table will thus only
contain combinations of field values from the raw data tables where the linking field values are represented in both tables. If used before keep, it specifies
that both raw data tables should be reduced to their common intersection
before being stored in Qlik Sense.

Syntax:

Inner ( Join | Keep)
[ (tablename) ](loadstatement |selectstatement )

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| tablename | The named table to be compared to the loaded table. |
| loadstatement or selectstatement | The LOAD or SELECT statement for the loaded table. |

Example

### Load script

Add the example script to your application and run it. To see the result, add the fields listed in the results column to a sheet in your application.

```
Table1:
Load * inline [
Column1, Column2
A, B
1, aa
2, cc
3, ee ];

Table2:
Inner Join Load * inline [
Column1, Column3
A, C
1, xx
4, yy ];
```

For more information about using inline loads, see [*Using inline loads to load data*](../inline-loads-qs.htm).

### Result

Resulting table

| Column1 | Column2 | Column3 |
| --- | --- | --- |
| A | B | C |
| 1 | aa | xx |

### Explanation

This example demonstrates the Inner Join output where only values present in both the first (left) and the second (right) tables are joined.

## Learn more

- [*Join*](Join.htm)
- [*Keep*](Keep.htm)
- [*Outer*](Outer.htm)
- [*Left*](Left.htm)
- [*Right*](Right.htm)
