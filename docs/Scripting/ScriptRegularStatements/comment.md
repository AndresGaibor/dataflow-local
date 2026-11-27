---
title: "Comment field"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/comment.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements"]
---

# Comment field

Provides a way of displaying the field comments (metadata) from databases and spreadsheets. Field names not present in the application will be ignored. If multiple occurrences of a field name are found, the last value is used.

Syntax:

comment [fields] \*fieldlist using mapname

comment [field] fieldname with comment

The map table used should have two columns, the first containing field names and the second the comments.

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| \*fieldlist | A comma separated list of the fields to be commented. Using \* as field list indicates all fields. The wildcard characters \* and ? are allowed in field names. Quoting of field names may be necessary when wildcards are used. |
| mapname | The name of a mapping table previously read in a mapping LOAD or mapping SELECT statement. |
| fieldname | The name of the field that should be commented. |
| comment | The comment that should be added to the field. |

Example 1:

commentmap:

mapping LOAD \* inline [

a,b

Alpha,This field contains text values

Num,This field contains numeric values

];

comment fields using commentmap;

Example 2:

comment field Alpha with AFieldContainingCharacters;

comment field Num with '\*A field containing numbers';

comment Gamma with 'Mickey Mouse field';

## Learn more

- [*Mapping*](../ScriptPrefixes/Mapping.htm)
- [*Field/Fields*](Field.htm)
