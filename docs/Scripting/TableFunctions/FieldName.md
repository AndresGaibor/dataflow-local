---
title: "FieldName Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/TableFunctions/FieldName.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Table functions"]
---
# FieldName Script function

The FieldName script function returns the name of the field with the specified number within a previously
loaded table. If the function is used within a LOAD statement, it
must not reference the table currently being loaded.

Syntax:

FieldName(field\_number ,table\_name)

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| field\_number | The field number of the field you want to reference. |
| table\_name | The table containing the field you want to reference. |

Example:

LET a =
FieldName(4,'tab1');
