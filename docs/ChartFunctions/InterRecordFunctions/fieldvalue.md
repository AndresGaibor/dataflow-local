---
title: "FieldValue Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/InterRecordFunctions/fieldvalue.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Inter-record functions"]
---

# FieldValue Script and chart function

FieldValue() returns the value found in position elem\_no of the field field\_name (by load
order).

Syntax:

FieldValue(field\_name , elem\_no)

Return data type:  dual

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| field\_name | Name of the field for which the value is required. For example, the column in a table. Must be given as a string value. This means that the field name must be enclosed by single quotes. |
| elem\_no | The position (element) number of the [field](#glossary-0 "Glossary term") following the load order, that the value is returned for. This could correspond to the row in a table, but it depends on the order in which the elements (rows) are loaded. |

Limitations:

- If elem\_no is larger than the number
  of field values, NULL is returned.
- Sorting on y-values in charts or sorting by expression columns in tables is not allowed when this chart function is used in any of the chart's expressions. These sort alternatives are therefore automatically disabled. When you use this chart function in a visualization or table, the sorting of the visualization will revert back to the sorted input to this function. This limitation does not apply to the equivalent script function.

Example

### Load script

Load the following data as an inline load in the data load editor to create the example below.

```
Names:

LOAD * inline [
First name|Last name|Initials|Has cellphone
John|Anderson|JA|Yes
Sue|Brown|SB|Yes
Mark|Carr|MC |No
Peter|Devonshire|PD|No
Jane|Elliot|JE|Yes
Peter|Franc|PF|Yes ] (delimiter is '|');

John1:

Load FieldValue('First name',1) as MyPos1
Resident Names;

Peter1:

Load FieldValue('First name',5) as MyPos2
Resident Names;
```

For more information about using inline loads, see [*Using inline loads to load data*](../../Scripting/inline-loads-qs.htm).

### Create a visualization

Create a table [visualization](#glossary-1 "Glossary term") in a Qlik Sense [sheet](#glossary-2 "Glossary term"). Add fields First name, MyPos1, and MyPos2 to the table.

### Result

| First name | MyPos1 | MyPos2 |
| --- | --- | --- |
| Jane | John | Jane |
| John | John | Jane |
| Mark | John | Jane |
| Peter | John | Jane |
| Sue | John | Jane |

### Explanation

FieldValue('First name','1') results in John as the value for MyPos1 for all first names because John appears first in the load order of the First name field. Note that in a filter pane John would appear as number 2 from the top, after Jane, as it's sorted alphabetically and not as in the load order.

FieldValue('First name','5') results in Jane as the value for MyPos2 for all first names because Jane appears fifth in the load order of the First name field.
