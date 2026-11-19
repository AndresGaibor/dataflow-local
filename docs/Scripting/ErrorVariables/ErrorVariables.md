---
title: "Error variables"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ErrorVariables/ErrorVariables.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Working with variables in the data load editor"]
---
Expand/Collapse all

# Error variables

The values of all error [variables](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ErrorVariables/ErrorVariables.htm#glossary-0 "Glossary term") will exist after the script execution. The first variable, ErrorMode, is input from the user, and the last three are output from Qlik Sense with information on errors in the script.

Use the drop-down on each variable to see a brief description and the syntax of each variable. Click the variable name in the syntax description for further details.

ErrorMode

This error variable determines what action is to be taken by Qlik Sense when
an error is encountered during script execution.

[**ErrorMode**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ErrorVariables/ErrorMode.htm)

ScriptError

This error variable returns the error code of the last executed script statement.

[**ScriptError**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ErrorVariables/ScriptError.htm)

ScriptErrorCount

This error variable returns the total number of statements that have caused errors during
the current script execution. This variable is always reset to 0 at the
start of script execution.

[**ScriptErrorCount**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ErrorVariables/ScriptErrorCount.htm)

ScriptErrorList

This error variable will contain a concatenated
list of all script errors that have occurred during the last script execution.
Each error is separated by a line feed.

[**ScriptErrorList**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ErrorVariables/ScriptErrorList.htm)
