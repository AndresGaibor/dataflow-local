---
title: "Field functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/FieldFunctions/field-functions-charts.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions"]
---

# Field functions

Expand/Collapse all

# Field functions

These functions can only be used in chart expressions.

[Field](#glossary-0 "Glossary term") functions either return integers or strings identifying different aspects of field [selections](#glossary-1 "Glossary term").

Use the drop-down on each function to see a brief description and the syntax of each function. Click the function name in the syntax description for further details.

## Count functions

GetAlternativeCount

GetAlternativeCount()
is used to find the number of alternative (light gray) values in the identified field.

[**getalternativecount**](getalternativecount.htm) (field\_name)

GetExcludedCount

GetExcludedCount() finds the number of excluded distinct values in the identified field. Only excluded (dark gray) fields are counted. Alternative (light gray) and selected excluded (dark gray with check mark) values are not counted.

[**getexcludedcount**](getexcludedcount.htm)(field\_name)

GetPossibleCount

GetPossibleCount() is used to find the number of possible values in the identified field. If the identified field includes selections, then the selected (green) fields are counted. Otherwise associated (white) values are counted.

[**getpossiblecount**](getpossiblecount.htm)(field\_name)

GetSelectedCount

GetSelectedCount() finds the number of selected (green) values in a field.

[**getselectedcount**](getselectedcount.htm) (field\_name
[, include\_excluded])

GetStateCounts

The
GetStateCounts() chart function is used to calculate the total number of unique values matching the specified selection states.

[**getstatecounts**](getstatecounts.htm) (field\_name, state\_name [, state\_type1,...state\_typeN])

## Field and selection functions

GetCurrentSelections

GetCurrentSelections() returns a list of the current selections in the application. If the selections are instead made using a search string in a search box, GetCurrentSelections() returns the search string.

[**getcurrentselections**](getcurrentselections.htm)([record\_sep [,tag\_sep [,value\_sep [,max\_values]]]])

GetFieldSelections

GetFieldSelections() returns a string with the current selections in a field.

[**getfieldselections**](getfieldselections.htm) (
field\_name [, value\_sep [, max\_values]])

GetObjectDimension

GetObjectDimension() returns the name of the dimension. Index is an optional integer denoting the dimension that should be returned.

[**getobjectdimension**](getobjectdimension.htm) ([index])

GetObjectField

GetObjectField() returns the field expression of the dimension. Index is an optional integer denoting the dimension that should be returned.

[**GetObjectField**](../../Scripting/SystemFunctions/GetObjectField.htm) ([index])

GetObjectMeasure

GetObjectMeasure() returns the name of the measure. Index is an optional integer denoting the measure that should be returned.

[**getobjectmeasure**](getobjectmeasure.htm) ([index])
