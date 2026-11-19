---
title: "HidePrefix"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemVariables/HidePrefix.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Working with variables in the data load editor", "System variables"]
---
# HidePrefix

All field names beginning with this text string will be hidden in the
same manner as the system fields. This is a user-defined variable.

Syntax:

HidePrefix

Example:

set HidePrefix='\_' ;

If this statement is used, the field names beginning with an underscore
will not be shown in the field name lists when the system fields are hidden.

## Learn more

- [*System variables*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemVariables/system-variables.htm)
