---
title: "Left"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Left.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script prefixes"]
---
# Left

The Join
and Keep
prefixes can be preceded by the prefix left.

If used before join it specifies
that a left join should be used. The resulting table will only contain
combinations of field values from the raw data tables where the linking field values are represented in the first table. If used before keep, it specifies
that the second raw data table should be reduced to its common intersection
with the first table, before being stored in Qlik Sense.

> **Note:** Were you looking for the string function by the same name? See: [*Left Script and chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/Left.htm)

Syntax:

Left ( Join | Keep)
[ (tablename) ](loadstatement | selectstatement)

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
Left Join Load * inline [
Column1, Column3
A, C
1, xx
4, yy ];
```

For more information about using inline loads, see [*Using inline loads to load data*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/inline-loads-qs.htm).

### Result

Resulting table

| Column1 | Column2 | Column3 |
| --- | --- | --- |
| A | B | C |
| 1 | aa | xx |
| 2 | cc | - |
| 3 | ee | - |

### Explanation

This example demonstrates the Left Join output where only values present in the first (left) table are joined.

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
Left Join Load * inline [
Column1, Column3
A, C
1, xx
4, yy ];
```

For more information about using inline loads, see [*Using inline loads to load data*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/inline-loads-qs.htm).

### Result

Resulting table

| Column1 | Column2 | Column3 |
| --- | --- | --- |
| A | B | C |
| 1 | aa | xx |
| 2 | cc | - |
| 3 | ee | - |

### Explanation

This example demonstrates the Left Join output where only values present in the first (left) table are joined.

## Learn more

- [*Join*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Join.htm)
- [*Keep*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Keep.htm)
- [*Inner*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Inner.htm)
- [*Outer*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Outer.htm)
- [*Right*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Right.htm)
