---
title: "Exit error"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptControlStatements/exit error.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script control statements"]
---
# Exit error

The Exit error statement ends script execution and raises a user-defined script error.

Syntax:

Exit Error expression [(when | unless condition)]

Since Exit error is a control statement, it is ended by semicolon or end-of-line and must not cross a line boundary.

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| expression | A value that is evaluated and returned as the user-raised script error message. |
| when / unless condition | Optional condition. when raises the error when the condition is true. unless raises the error when the condition is false. |

Examples:

```
//Exit error
Exit Error 'Load validation failed';
```

```
//Exit error when a condition is fulfilled
Exit Error 'Source connection unavailable' when vConnectionOk=0;
```

```
//Exit error unless a condition is fulfilled
Exit Error 'Required variable is missing' unless len(trim(vRequiredVar))>0;
```

## Learn more

- [*Exit*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptControlStatements/Exit.htm)
- [*Exit script*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptControlStatements/exit%20script.htm)
- [*Script control statements*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptControlStatements/script-control-statements.htm)
