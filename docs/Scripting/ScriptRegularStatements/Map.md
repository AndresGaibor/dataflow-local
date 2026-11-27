---
title: "Map"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Map.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements"]
---

# Map

The map ... using statement is
used for mapping a certain field value or expression to the values of
a specific mapping table. The mapping table is created through the Mapping
statement.

Syntax:

Map fieldlist Using 
mapname

The automatic mapping is done for fields loaded after the Map … Using statement until the end of the script or until an Unmap statement is encountered.

The mapping is done last in the chain of events leading up to the [field](#glossary-0 "Glossary term") being stored in the internal table in Qlik Sense. This means that mapping is not done every time a field name is encountered as part of an expression, but rather when the value is stored under the field name in the internal table. If mapping on the expression level is required, the Applymap() function has to be used instead.

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| fieldlist | A comma separated list of the fields that should be mapped from this point in the script. Using \* as field list indicates all fields. The wildcard characters \* and ? are allowed in field names. Quoting of field names may be necessary when wildcards are used. |
| mapname | The name of a mapping table previously read in a mapping load or mapping select statement. |

Examples and results:

| Example | Result |
| --- | --- |
| Map Country Using Cmap; | Enables mapping of the field Country using the map Cmap. |
| Map A, B, C Using X; | Enables mapping of the fields A, B and C using the map X. |
| Map \* Using GenMap; | Enables mapping of all fields using GenMap. |

## Learn more

- [*Mapping*](../ScriptPrefixes/Mapping.htm)
- [*Unmap*](Unmap.htm)
- [*Mapping functions*](../MappingFunctions/mapping-functions.htm)
