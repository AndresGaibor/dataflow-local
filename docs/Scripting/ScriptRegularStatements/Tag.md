---
title: "Tag"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Tag.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements"]
---
# Tag

This script statement provides a way to assign tags to one or more fields or tables. If an attempt to tag a field or table not present in the application is made, the tagging will be ignored. If conflicting occurrences of a field or tag name are found, the last value is used.

Syntax:

Tag [field|fields] fieldlist with tagname

  

Tag [field|fields] fieldlist using mapname

  

Tag table tablelist with tagname

Arguments

| Argument | Description |
| --- | --- |
| fieldlist | One or several fields that should be tagged, in a comma separated list. |
| mapname | The name of a mapping table previously loaded in a mapping Load or mapping Select statement. |
| tablelist | A comma separated list of the tables that should be tagged. |
| tagname | The name of the tag that should be applied to the field. |

Example 1:

tagmap:

mapping LOAD \* inline [

a,b

Alpha,MyTag

Num,MyTag

];

tag fields using tagmap;

Example 2:

tag field Alpha with 'MyTag2';

## Learn more

- [*Untag*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Untag.htm)
- [*Field tags*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/field-tags.htm)
- [*Mapping*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Mapping.htm)
- [*Field/Fields*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Field.htm)
