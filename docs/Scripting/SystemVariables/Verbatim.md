---
title: "Verbatim"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemVariables/Verbatim.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Working with variables in the data load editor", "System variables"]
---
# Verbatim

Normally all field values are automatically stripped of leading and
trailing blanks (ASCII 32) before being loaded into the Qlik Sense
database. Setting this variable to 1 suspends the stripping of blanks. Tab (ASCII 9) and hard space (ANSI 160) characters are never stripped.

Syntax:

Verbatim

Example:

set Verbatim = 1;

## Learn more

- [*System variables*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemVariables/system-variables.htm)
