---
title: "Exit script"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartLevelScripting/ControlStatements/exit-script.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Chart level scripting", "Control statements"]
---

# Exit script

This control statement stops script execution. It may be inserted anywhere in the script.

Syntax:

Exit Script [ (when | unless)
condition ]

Since the exit script statement is a control statement and as such is ended with either a semicolon or
end-of-line, it must not cross a line boundary.

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| condition | A logical expression evaluating to True or False. |
| when / unless | An exit script statement can be made conditional by the optional use of when or unless clause. |

Examples:

//Exit script
Exit Script;
 
//Exit script when a condition is fulfilled
Exit Script when a=1

## Learn more

- [*Exit*](Exit.htm)
