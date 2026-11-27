---
title: "Exit error"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartLevelScripting/ControlStatements/exit-error.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Chart level scripting", "Control statements"]
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

- [*Using chart level scripting in visualizations*](../chart-level-scripting.htm)
- [*Exit*](Exit.htm)
- [*Exit script*](exit-script.htm)
- [*Control statements*](../modifier-control-statements.htm)
