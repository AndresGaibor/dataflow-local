---
title: "FieldNumber Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/TableFunctions/FieldNumber.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Table functions"]
---
# FieldNumber Script function

The FieldNumber script function returns the number of a specified field within a previously loaded
table. If the function is used within a LOAD statement, it must not reference
the table currently being loaded.

Syntax:

FieldNumber(field\_name ,table\_name)

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| field\_name | The name of the field. |
| table\_name | The name of the table containing the field. |

If the field field\_name does not exist in table\_name, or table\_name does not exist, the function returns 0.

Example:

LET a =
FieldNumber('Customer','tab1');
