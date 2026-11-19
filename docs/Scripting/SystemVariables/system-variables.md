---
title: "System variables"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemVariables/system-variables.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Working with variables in the data load editor"]
---
Expand/Collapse all

# System variables

System variables, some of which are system-defined, provide information about the system and the Qlik Sense application.

Use the drop-down on each function to see a brief description and the syntax of each function. For some of the functions, you can get further details about that specific function by clicking the function name in the syntax description.

CreateSearchIndexOnReload

This
variable defines if search index files should be created during data reload.

[**CreateSearchIndexOnReload**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemVariables/CreateSearchIndexOnReload.htm)

HidePrefix

All field names beginning with this text string will be hidden in the
same manner as the system fields. This is a user-defined variable.

[**HidePrefix**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemVariables/HidePrefix.htm)

HideSuffix

All field names ending with this text string will be hidden in the same
manner as the system fields. This is a user-defined variable.

[**HideSuffix**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemVariables/HideSuffix.htm)

Include

The Include/Must\_Include variable specifies
a script that contains text that should be included in the script and evaluated as script code. It is not used to add data. You can store parts of your script code in a separate text file and reuse it in several applications. This is a user-defined variable.

$([**Include**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemVariables/Include.htm)=filename)

$(Must\_Include=filename)

OpenUrlTimeout

This
variable defines the timeout in seconds that Qlik Sense should respect when
getting data from URL sources (e.g. HTML pages). If omitted, the timeout
is about 20 minutes.

[**OpenUrlTimeout**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemVariables/OpenUrlTimeout.htm)

QlikCloudGroupMode

This variable controls the groups that are used in Section Access and returned with the GetUserAttr function (`'userGroups'` attribute).

[**QlikCloudGroupMode**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemVariables/QlikCloudGroupMode.htm)

ScriptOnlyVariables

The ScriptOnlyVariables system variable is used to define script-only variables. This variable specifies whether a script variable will be available only in the script, or whether it will also be available (and visible) outside the script—for example, in sheet view in an application.

[**ScriptOnlyVariables**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemVariables/ScriptOnlyVariables.htm)

StripComments

If this variable is set to 0, stripping of /\*..\*/ and // comments in the
script will be inhibited. If this variable is not defined, stripping of comments will always
be performed.

[**StripComments**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemVariables/StripComments.htm)

Verbatim

Normally all field values are automatically stripped of leading and
trailing blanks (ASCII 32) before being loaded into the Qlik Sense
database. Setting this variable to 1 suspends the stripping of blanks. Tab (ASCII 9) and hard space (ANSI 160) characters are never stripped.

[**Verbatim**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemVariables/Verbatim.htm)
