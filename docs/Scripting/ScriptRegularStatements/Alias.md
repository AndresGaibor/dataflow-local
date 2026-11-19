---
title: "Alias"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Alias.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements"]
---
# Alias

The alias statement is used
for setting an alias according to which a field will be renamed whenever
it occurs in the script that follows.

Syntax:

alias fieldname as aliasname {,fieldname as aliasname}

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| fieldname | The name of the [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Alias.htm#glossary-0 "Glossary term") in your source data |
| aliasname | An alias name you want to use instead |

## Examples with results

For the examples in the table below, the defined field name changes will be applied to references of the original field name on all subsequent SELECT and LOAD statements.
A new alias can be defined for a field name by a new alias statement at any subsequent position in the script.

The field is also referenced with the alias name in the data model and application content.

Examples and results

| Example | Result |
| --- | --- |
| Alias ID\_N as NameID; | Field ID\_N is renamed to NameID. |
| Alias A as Name, B as Number, C as Date; | Fields A, B, and C are renamed to Name, Number, and Date respectively. |

Long-form example

Overview

Open the Data load editor and add the load script below to a new section.

Load script

```
alias [A] as [AAA];
T1:
Load 'string 1' as A autogenerate 1;
T2:
Load 'string 2' as B autogenerate 1;
T3:
Load 'string 3' as A autogenerate 1;
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- `AAA`

Results table

| AAA |
| --- |
| string 1 |
| string 3 |

## Learn more

- [*Load*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Load.htm)
- [*Select*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Select.htm)
