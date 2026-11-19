---
title: "ScriptOnlyVariables"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemVariables/ScriptOnlyVariables.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Working with variables in the data load editor", "System variables"]
---
# ScriptOnlyVariables

The ScriptOnlyVariables system variable is used to define script-only variables. This variable specifies whether a script variable will be available only in the script, or whether it will also be available (and visible) outside the script—for example, in sheet view in an application.

After a ScriptOnlyVariables value is defined —either explicitly, or implicitly via its default value of 0 — all variables defined in Let or Set statements after this definition will use the defined setting, unless the ScriptOnlyVariables value is changed later in the script. This means that you can define some variables as script-only and allow others to be surfaced outside of the script.

Syntax:

ScriptOnlyVariables

`ScriptOnlyVariables` values

| Value | Results |
| --- | --- |
| `0` | Variables are surfaced outside of the script, in addition to being available within the script itself.  This is the default value if the ScriptOnlyVariables variable value is not defined explicitly in the script. |
| `1` | Variables are not surfaced outside of the script. |

Example 1: Surfacing a variable outside of the script

In this example, the variable `vNotScriptOnly` is explicitly set to appear outside the script.

```
SET ScriptOnlyVariables = 0;
SET vNotScriptOnly = "example_text";
```

Example 2: Hiding a variable outside of the script

In this example, the variable `vScriptOnly` will only be available during script execution. It will not be shown elsewhere, such as sheet view.

```
SET ScriptOnlyVariables = 1;
SET vScriptOnly = "example_text";
```

Example 3: Hiding some variables and surfacing others

In this example, the ScriptOnlyVariables value is defined multiple times throughout the script to allow different variable settings. The variable `vHideOutsideScript` will only be available during script execution. The variable `vAllowInSheets` will be surfaced in sheet view.

```
SET ScriptOnlyVariables = 1;
SET vHideOutsideScript = "example_text";
SET ScriptOnlyVariables = 0;
SET vAllowInSheets = "example_text";
```

## When to use ScriptOnlyVariables

Script-only variables help you to:

- Use certain variables only for performing calculations and field definitions in the context of the data model.
- Remove variables that are not needed for the creation of sheets and charts, simplifying application development.

## Learn more

- [*System variables*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemVariables/system-variables.htm)
- [*Let*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Let.htm)
- [*Set*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Set.htm)
- [*Working with variables in the data load editor*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/work-with-variables-in-data-load-editor.htm)
