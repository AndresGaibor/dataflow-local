---
title: "Drop variable"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Drop-Variable.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements", "Drop"]
---

# Drop variable

Use the Drop variable statement to drop a script variable during script execution. When a variable is dropped, it is not available or visible, for example, in sheet view.

Information note

Both drop variable and drop variables are allowed forms with
no difference in effect.

Syntax:

Drop variable variablename {, variablename2 ...}

Drop variables variablename {, variablename2 ...}

Examples:

```
Drop variable MyVarToDrop1;
```

```
Drop variables MyVarToDrop2, MyVarToDrop3;
```

## When to use a Drop variable statement

Drop variable statements are useful for separating script development from sheet development. You can use a variable to perform calculations or for loading specific data only, without adding clutter to the sheet-building experience. If you have many variables and a large volume of data to load with the script, dropping variables early in the script can help reduce memory usage and increase performance.

## Learn more

- [*Drop*](Drop.htm)
- [*Working with variables in the data load editor*](../work-with-variables-in-data-load-editor.htm)
