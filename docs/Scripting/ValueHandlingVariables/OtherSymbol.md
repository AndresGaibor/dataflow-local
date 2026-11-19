---
title: "OtherSymbol"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ValueHandlingVariables/OtherSymbol.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Working with variables in the data load editor", "Value handling variables"]
---
# OtherSymbol

Defines a symbol to be treated as 'all other values' before a LOAD/SELECT
statement. This is a user-defined variable.

Syntax:

OtherSymbol

Example:

set
OtherSymbol='+';

LOAD \* inline

[X, Y

a, a

b, b];

LOAD \* inline

[X, Z

a, a

+, c];

The field value Y='b' will now link to Z='c' through the other symbol.
