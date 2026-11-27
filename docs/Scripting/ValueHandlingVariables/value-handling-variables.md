---
title: "Value handling variables"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ValueHandlingVariables/value-handling-variables.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Working with variables in the data load editor"]
---

# Value handling variables

Expand/Collapse all

# Value handling variables

This section describes variables that are used for handling NULL and other values.

Use the drop-down on each function to see a brief description and the syntax of each function. Click the function name in the syntax description for further details.

NullDisplay

The defined symbol will substitute all NULL values from ODBC, and connectors,
on the lowest level of data. This is a user-defined variable.

[**NullDisplay**](NullDisplay.htm)

NullInterpret

The defined symbol will
be interpreted as NULL when it occurs in a text file, CSV file, or an inline statement. This is a user-defined variable.

[**NullInterpret**](NullInterpret.htm)

NullValue

If the NullAsValue statement is used, the defined symbol will substitute all NULL values in the NullAsValue specified fields with the specified string.

[**NullValue**](NullValue.htm)

OtherSymbol

Defines a symbol to be treated as 'all other values' before a LOAD/SELECT
statement. This is a user-defined variable.

[**OtherSymbol**](OtherSymbol.htm)
