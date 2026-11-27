---
title: "FieldIndex Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/InterRecordFunctions/fieldindex.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Inter-record functions"]
---

# FieldIndex Script and chart function

FieldIndex() returns the position of the field value value in the field field\_name (by load
order).

Syntax:

FieldIndex(field\_name ,
value)

Return data type:  integer

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| field\_name | Name of the field for which the index is required. For example, the column in a table. Must be given as a string value. This means that the field name must be enclosed by single quotes. |
| value | The value of the [field](#glossary-0 "Glossary term") field\_name. |

Limitations:

- If value cannot be found
  among the field values of the field field\_name, 0 is returned.
- Sorting on y-values in charts or sorting by expression columns in tables is not allowed when this chart function is used in any of the chart's expressions. These sort alternatives are therefore automatically disabled. When you use this chart function in a visualization or table, the sorting of the visualization will revert back to the sorted input to this function. This limitation does not apply to the equivalent script function.

Examples and results:

The following examples use the field: First name from the tableNames.

Examples and results

| Examples | Results |
| --- | --- |
| Add the example data to your app and run it. | The table Names is loaded, as in the sample data. |
| Chart function: In a table containing the [dimension](#glossary-2 "Glossary term") First name, add as a [measure](#glossary-3 "Glossary term"). |  |
| FieldIndex ('First name','John') | 1, because 'John' appears first in the load order of the First name field. Note that in a filter pane John would appear as number 2 from the top as it's sorted alphabetically and not as in the load order. |
| FieldIndex ('First name','Peter') | 4, because FieldIndex() returns only one value, that is the first occurrence in the load order. |
| Script function: Given the table Names is loaded, as in the example data: |  |
| John1:  Load FieldIndex('First name','John') as MyJohnPos  Resident Names; | MyJohnPos=1, because 'John' appears first in the load order of the First name field. Note that in a filter pane John would appear as number 2 from the top as it's sorted alphabetically and not as in the load order. |
| Peter1:  Load FieldIndex('First name','Peter') as MyPeterPos  Resident Names; | MyPeterPos=4, because FieldIndex() returns only one value, that is the first occurrence in the load order. |

Data used in example:

```
Names:
LOAD * inline [
First name|Last name|Initials|Has cellphone
John|Anderson|JA|Yes
Sue|Brown|SB|Yes
Mark|Carr|MC|No
Peter|Devonshire|PD|No
Jane|Elliot|JE|Yes
Peter|Franc|PF|Yes ] (delimiter is '|');

John1:
Load FieldIndex('First name','John') as MyJohnPos
Resident Names;
 
Peter1:
Load FieldIndex('First name','Peter') as MyPeterPos
Resident Names;
```
