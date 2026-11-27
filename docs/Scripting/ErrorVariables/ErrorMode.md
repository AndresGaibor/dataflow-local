---
title: "ErrorMode"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ErrorVariables/ErrorMode.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Working with variables in the data load editor", "Error variables"]
---

# ErrorMode

This error variable determines what action is to be taken by Qlik Sense when
an error is encountered during script execution.

Syntax:

ErrorMode

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| ErrorMode=1 | The default setting. The script execution will halt and the user will be prompted for action (non-batch mode). |
| ErrorMode =0 | Qlik Sense will simply ignore the failure and continue script execution at the next script statement. |
| ErrorMode =2 | Qlik Sense will trigger an "Execution of script failed..." error message immediately on failure, without prompting the user for action beforehand. |

Example:

set
ErrorMode=0;

## Learn more

- [*Error variables*](ErrorVariables.htm)
