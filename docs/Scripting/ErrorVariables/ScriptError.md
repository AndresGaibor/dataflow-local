---
title: "ScriptError"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ErrorVariables/ScriptError.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Working with variables in the data load editor", "Error variables"]
---
# ScriptError

This error variable returns the error code of the last executed script statement.

Syntax:

ScriptError

This [variable](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ErrorVariables/ScriptError.htm#glossary-0 "Glossary term")
will be reset to 0 after each successfully executed script statement.
If an error occurs it will be set to an internal Qlik Sense error code.
Error codes are dual values with a numeric and a text component. The following
error codes exist:

Script error codes

| Error code | Description |
| --- | --- |
| 0 | No error. Dual value text is empty. |
| 1 | General error. |
| 2 | Syntax error. |
| 3 | General ODBC error. |
| 4 | General OLE DB error. |
| 5 | General custom database error. |
| 6 | General XML error. |
| 7 | General HTML error. |
| 8 | File not found. |
| 9 | Database not found. |
| 10 | Table not found. |
| 11 | Field not found. |
| 12 | File has wrong format. |
| 16 | Semantic error. |

Example:

set ErrorMode=0;

LOAD \* from
abc.qvf;

if ScriptError=8
then

exit script;

//no file;

end if

## Learn more

- [*Error variables*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ErrorVariables/ErrorVariables.htm)
