---
title: "NULL functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NULLFunctions/null-functions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions"]
---

# NULL functions

Expand/Collapse all

# NULL functions

This section describes functions for returning or detecting NULL values.

All functions can be used in both the [data load script](#glossary-0 "Glossary term") and in chart expressions.

Use the drop-down on each function to see a brief description and the syntax of each function. Click the function name in the syntax description for further details.

EmptyIsNull

The EmptyIsNull function converts empty strings to NULL. Hence, it returns NULL if the parameter is an empty string, otherwise it returns the parameter.

[**EmptyIsNull**](EmptyIsNull.htm)(expr
)

IsNull

The IsNull function tests if the value of an expression is NULL and if so, returns -1 (True), otherwise 0 (False).

[**IsNull**](IsNull.htm)(expr
)

Null

The Null function returns a null value.

[**Null**](Null.htm)( )
