---
title: "Sleep"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Sleep.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements"]
---

# Sleep

The sleep statement pauses script
execution for a specified time.

Syntax:

Sleep n

Arguments:

| Argument | Description |
| --- | --- |
| n | Stated in milliseconds, where n is a positive integer no larger than 3600000 (i.e. 1 hour). The value may be an expression. |

Example 1:

Sleep 10000;

Example 2:

Sleep
t\*1000;
