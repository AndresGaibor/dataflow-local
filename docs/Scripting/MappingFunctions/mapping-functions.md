---
title: "Mapping functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/MappingFunctions/mapping-functions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions"]
---

# Mapping functions

Expand/Collapse all

# Mapping functions

This section describes functions for handling mapping tables. A mapping table can be used to replace [field](#glossary-0 "Glossary term") values or field names during script execution.

Mapping functions can only be used in the [data load script](#glossary-1 "Glossary term")

Use the drop-down on each function to see a brief description and the syntax of each function. Click the function name in the syntax description for further details.

ApplyMap

The ApplyMap script function is used
for mapping the output of an expression to a previously loaded mapping table.

[**ApplyMap**](ApplyMap.htm)('mapname',
expr [
, defaultexpr ] )

MapSubstring

The MapSubstring script function is
used to map parts of any expression to a previously loaded mapping table.
The mapping is case sensitive and non-iterative, and substrings are mapped
from left to right.

[**MapSubstring**](MapSubstring.htm)('mapname',
expr)
