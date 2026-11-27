---
title: "Right"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Right.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script prefixes"]
---

# Right

The Join
and Keep
prefixes can be preceded by the prefix right.

If used before join it specifies
that a right join should be used. The resulting table will only contain
combinations of field values from the raw data tables where the linking field values are represented in the second table. If used before keep, it specifies
that the first raw data table should be reduced to its common intersection
with the second table, before being stored in Qlik Sense.

Information noteWere you looking for the string function by the same name? See: [*Right Script and chart function*](../StringFunctions/Right.htm)

Syntax:

Right (Join | Keep) [(tablename)](loadstatement
|selectstatement )

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
Right Join Load * inline [
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
| 4 | - | yy |

### Explanation

This example demonstrates the Right Join output where only values present in the second (right) table are joined.

## Learn more

- [*Join*](Join.htm)
- [*Keep*](Keep.htm)
- [*Inner*](Inner.htm)
- [*Outer*](Outer.htm)
- [*Left*](Left.htm)
