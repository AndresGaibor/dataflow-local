---
title: "Untag"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Untag.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements"]
---

# Untag

This script statement provides a way to remove tags from fields or tables. If an attempt to untag a field or table not present in the application is made, the untagging will be ignored.

Syntax:

Untag [field|fields] fieldlist with tagname

Untag [field|fields] fieldlist using mapname

Untag table tablelist with tagname

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| fieldlist | One or several fields which tags should be removed, in a comma separated list. |
| mapname | The name of a mapping table previously loaded in a mapping LOAD or mapping SELECT statement. |
| tablelist | A comma separated list of the tables that should be untagged. |
| tagname | The name of the tag that should be removed from the field. |

Example 1:

tagmap:

mapping LOAD \* inline [

a,b

Alpha,MyTag

Num,MyTag

];

Untag fields using tagmap;

Example 2:

Untag field Alpha with MyTag2;

## Learn more

- [*Tag*](Tag.htm)
- [*Mapping*](../ScriptPrefixes/Mapping.htm)
- [*Field/Fields*](Field.htm)
