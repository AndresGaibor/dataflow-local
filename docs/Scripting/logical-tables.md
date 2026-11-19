---
title: "Logical tables"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/logical-tables.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Understanding script syntax and data structures"]
---
# Logical tables

Each LOAD or SELECT statement generates a table. Normally, Qlik Sense treats the result of each one of these as one logical table. However, there are a couple of exceptions from this rule:

- If two or more statements result in tables with identical field names, the tables are concatenated and treated as one logical table.
- If a LOAD or SELECT statement is preceded by any of the following qualifiers, data is altered or treated differently.

Logical tables

| Table | Description |
| --- | --- |
| concatenate | This table is concatenated with (added to) another named table or with the last previously created logical table.  For more information, see [*Concatenating tables*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/concatenate-tables.htm) and [*Concatenate*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/concatenate.htm). |
| crosstable | This table is unpivoted. That is, it is converted from crosstable format to column format.  For more information, see [*Working with crosstables in the data load script*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/work-with-cross-tables.htm) and [*Crosstable*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/crosstable.htm). |
| generic | This table is split into several other logical tables.  For more information, see [*Generic databases*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataSource/generic-databases.htm) and [*Generic*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Generic.htm). |
| info | This table is not loaded as a logical table, but as an information table containing links to external information such as files, sounds, URLs, etc. |
| intervalmatch | The table (which must contain exactly two columns) is interpreted as numeric intervals, which are associated with discrete numbers in a specified [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/logical-tables.htm#glossary-0 "Glossary term").  For more information, see [*Matching intervals to discrete data*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/matching-intervals-to-discrete-data.htm) and [*IntervalMatch*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/IntervalMatch.htm). |
| join | This table is joined by Qlik Sense with another named table or with the last previously created logical table, over the fields in common.  For more information, see [*Combining tables with Join and Keep*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/combine-tables-join-keep.htm) and [*Join*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Join.htm). |
| keep | This table is reduced to the fields in common with another named table or with the last previously created logical table.  For more information, see [*Combining tables with Join and Keep*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/combine-tables-join-keep.htm) and [*Keep*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Keep.htm). |
| mapping | This table (which must contain exactly two columns) is read as a mapping table, which is never associated with other tables.  For more information, see [*Using mapping as an alternative to joining*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/use-mapping-as-alternative-join.htm) and [*Mapping*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Mapping.htm) . |
| semantic | This table is not loaded as a logical table, but as a semantic table containing relationships that should not be joined, e.g. predecessor, successor and other references to other objects of the same type.  For more information, see [*Semantic*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Semantic.htm). |

When the data has been loaded, the logical tables are associated.
