---
title: "NullValue"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ValueHandlingVariables/NullValue.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Working with variables in the data load editor", "Value handling variables"]
---
# NullValue

If the NullAsValue statement is used, the defined symbol will substitute all NULL values in the NullAsValue specified fields with the specified string.

Syntax:

NullValue

Example:

NullAsValue Field1, Field2;

set NullValue='<NULL>';
