---
title: "HideSuffix"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemVariables/HideSuffix.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Working with variables in the data load editor", "System variables"]
---

# HideSuffix

All field names ending with this text string will be hidden in the same
manner as the system fields. This is a user-defined variable.

Syntax:

HideSuffix

Example:

set HideSuffix='%';

If this statement is used, the field names ending with a percentage
sign will not be shown in the field name lists when the system fields
are hidden.

## Learn more

- [*System variables*](system-variables.htm)
