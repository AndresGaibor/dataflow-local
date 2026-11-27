---
title: "FieldValueCount Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/InterRecordFunctions/fieldvaluecount.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Inter-record functions"]
---

# FieldValueCount Script and chart function

FieldValueCount() is an integer function that returns
the number of distinct values in a field.

A partial reload can remove values from the data, which will not be reflected in the number returned. The returned number will correspond to all distinct values that were loaded in either the initial reload or any subsequent partial reload.

Information noteSorting on y-values in charts or sorting by expression columns in tables is not allowed when this chart function is used in any of the chart's expressions. These sort alternatives are therefore automatically disabled. When you use this chart function in a visualization or table, the sorting of the visualization will revert back to the sorted input to this function. This limitation does not apply to the equivalent script function.

Syntax:

FieldValueCount(field\_name)

Return data type:  integer

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| field\_name | Name of the field for which the value is required. For example, the column in a table. Must be given as a string value. This means that the field name must be enclosed by single quotes. |

Examples and results:

The following examples use the [field](#glossary-0 "Glossary term") First name from the table Names.

Examples and results

| Examples | Results |
| --- | --- |
| Add the example data to your app and run it. | The table Names is loaded, as in the sample data. |
| Chart function: In a table containing the [dimension](#glossary-2 "Glossary term") First name, add as a [measure](#glossary-3 "Glossary term"). |  |
| FieldValueCount('First name') | 5 as Peter appears twice. |
| FieldValueCount('Initials') | 6 as Initials only has distinct values. |
| Script function: Given the table Names is loaded, as in the example data: |  |
| FieldCount1:  Load FieldValueCount('First name') as MyFieldCount1  Resident Names; | MyFieldCount1=5, because 'Peter' appears twice. |
| FieldCount2:  Load FieldValueCount('Initials') as MyInitialsCount1  Resident Names; | MyFieldCount1=6, because 'Initials' only has distinct values. |

Data used in examples:

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

FieldCount1:
Load FieldValueCount('First name') as MyFieldCount1
Resident Names;
 
FieldCount2:
Load FieldValueCount('Initials') as MyInitialsCount1
Resident Names;
```
