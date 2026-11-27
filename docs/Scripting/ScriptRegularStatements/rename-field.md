---
title: "Rename field"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/rename-field.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements", "Rename"]
---

# Rename field

This script function renames one or more existing Qlik Sense field(s) after they have been loaded.

Information noteIt is not recommended to name a variable identically to a field or a function in Qlik Sense.

Either syntax: rename [field](#glossary-0 "Glossary term")
or rename fields can be used.

Syntax:

Rename Field (using mapname
| oldname to newname{ , oldname to newname })

Rename Fields (using mapname
| oldname to newname{ , oldname to newname })

Arguments:

| Argument | Description |
| --- | --- |
| mapname | The name of a previously loaded mapping table containing one or more pairs of old and new field names. |
| oldname | The old field name. |
| newname | The new field name. |

Limitations:

You cannot rename two fields to having the same name.

Example 1:

Rename Field
XAZ0007 to Sales;

Example 2:

FieldMap:

Mapping
SQL SELECT oldnames, newnames from datadictionary;

Rename Fields
using FieldMap;

## Learn more

- [*Rename table*](rename-table.htm)
- [*Rename*](Rename.htm)
- [*Field/Fields*](Field.htm)
- [*To*](../ScriptControlStatements/To.htm)
