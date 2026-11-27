---
title: "Data cleansing"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/data-cleansing.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Modeling your data", "Best practices for data modeling"]
---

# Data cleansing

When loading data from different tables, note that [field](#glossary-0 "Glossary term") values denoting the same thing are not always consistently named. Since this lack of consistency is not only annoying, but also hinders associations, the problem needs to be solved. This can be done in an elegant way by creating a mapping table for the comparison of field values.

## Mapping tables

Tables loaded via mapping load or mapping select are treated differently from other tables. They will be stored in a separate area of the memory and used only as mapping tables during script execution. After the script execution they will be automatically dropped.

### Rules:

- A mapping table must have two columns, the first one containing the comparison values and the second the desired mapping values.
- The two columns must be named, but the names have no relevance in themselves. The column names have no connection to field names in regular internal tables.

## Using a mapping table

When loading several tables listing countries, you may find that one and the same country has several different names. In this example, the U.S.A. are listed as US, U.S., and United States.

To avoid the occurrence of three different records denoting the United States in the concatenated table, create a table similar to that shown and load it as a mapping table.

The entire script should have the following appearance:

CountryMap:

Mapping LOAD x,y from MappingTable.txt

(ansi, txt, delimiter is ',', embedded

labels);

Map Country using CountryMap;

LOAD Country,City from CountryA.txt

(ansi, txt, delimiter is ',', embedded labels);

LOAD Country, City from CountryB.txt

(ansi, txt, delimiter is ',', embedded labels);

The mapping statement loads the file MappingTable.txt as a mapping table with the label CountryMap.

The map statement enables mapping of the field Country using the previously loaded mapping table CountryMap.

The LOAD statements load the tables CountryA and CountryB. These tables, which will be concatenated due to the [fact](#glossary-1 "Glossary term")that they have the same set of fields, include the field Country, whose field values will be compared with those of the first column of the mapping table. The field values US, U.S., and United States will be found and replaced by the values of the second column of the mapping table, i.e. USA.

The automatic mapping is done last in the chain of events that leads up to the field being stored in the Qlik Sense table. For a typical LOAD or SELECT statement the order of events is roughly as follows:

1. Evaluation of expressions
2. Renaming of fields by as
3. Renaming of fields by alias
4. Qualification of table name, if applicable
5. Mapping of data if field name matches

This means that the mapping is not done every time a field name is encountered as part of an expression but rather when the value is stored under the field name in the Qlik Sense table.

To disable mapping, use the unmap statement.

For mapping on expression level, use the applymap function.

For mapping on substring level, use the mapsubstring function.

## Learn more

- [*Mapping*](../Scripting/ScriptPrefixes/Mapping.htm)
- [*Map*](../Scripting/ScriptRegularStatements/Map.htm)
- [*Unmap*](../Scripting/ScriptRegularStatements/Unmap.htm)
- [*Mapping functions*](../Scripting/MappingFunctions/mapping-functions.htm)
