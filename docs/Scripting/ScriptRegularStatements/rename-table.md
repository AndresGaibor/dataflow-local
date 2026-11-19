---
title: "Rename table"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/rename-table.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements", "Rename"]
---
# Rename table

This script function renames one or more existing Qlik Sense internal table(s) after they have been loaded.

Either syntax: rename table
or rename tables can be used.

Syntax:

Rename Table (using mapname
| oldname to newname{ , oldname to newname })

Rename Tables (using mapname
| oldname to newname{ , oldname to newname })

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| mapname | The name of a previously loaded mapping table containing one or more pairs of old and new table names. |
| oldname | The old table name. |
| newname | The new table name. |

Limitations:

Two differently named tables cannot be renamed to having the same name. The script will generate an error if you try to rename a table to the same name as an existing table.

Example 1:

Tab1:

SELECT \*
from Trans;

Rename Table Tab1 to Xyz;

Example 2:

TabMap:

Mapping
LOAD oldnames, newnames from tabnames.csv;

Rename
Tables using TabMap;

## Learn more

- [*Rename field*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/rename-field.htm)
- [*Rename*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Rename.htm)
- [*To*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptControlStatements/To.htm)
- [*Table/Tables*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Table.htm)
