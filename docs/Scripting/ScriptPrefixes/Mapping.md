---
title: "Mapping"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Mapping.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script prefixes"]
---

# Mapping

The mapping prefix is used to create a mapping table that can be used to, for example, replace field values and field names during script execution.

Syntax:

Mapping(
loadstatement | selectstatement
)

The mapping prefix can be put in front of a LOAD or a SELECT statement and will store the result of the loading statement as a mapping table. Mapping provides an efficient way to substitute [field](#glossary-0 "Glossary term") values during script execution, e.g. replacing US, U.S. or America with USA. A mapping table consists of two columns, the first containing comparison values and the second containing the desired mapping values. Mapping tables are stored temporarily in memory and dropped automatically after script execution. Alternatively, you can drop mapping tables earlier in the script execution using the Drop mapping table variant of the [*Drop table*](../ScriptRegularStatements/drop-table.htm) statement.

The content of the mapping table can be accessed using e.g. the Map … Using statement, the Rename Field statement, the Applymap() function or the Mapsubstring() function.

Example:

In this example we load a list of salespersons with a country code representing their country of residence. We use a table mapping a country code to a country to replace the country code with the country name. Only three countries are defined in the mapping table, other country codes are mapped to 'Rest of the world'.

```
// Load mapping table of country codes:
map1:
mapping LOAD *
Inline [
CCode, Country
Sw, Sweden
Dk, Denmark
No, Norway
] ;
// Load list of salesmen, mapping country code to country
// If the country code is not in the mapping table, put Rest of the world
Salespersons:
LOAD *,
ApplyMap('map1', CCode,'Rest of the world') As Country
Inline [
CCode, Salesperson
Sw, John
Sw, Mary
Sw, Per
Dk, Preben
Dk, Olle
No, Ole
Sf, Risttu] ;
// We don't need the CCode anymore
Drop Field 'CCode';
```

The resulting table looks like this:

Mapping table

| Salesperson | Country |
| --- | --- |
| John | Sweden |
| Mary | Sweden |
| Per | Sweden |
| Preben | Denmark |
| Olle | Denmark |
| Ole | Norway |
| Risttu | Rest of the world |

## Learn more

- [*Load*](../ScriptRegularStatements/Load.htm)
- [*Select*](../ScriptRegularStatements/Select.htm)
- [*Map*](../ScriptRegularStatements/Map.htm)
- [*Unmap*](../ScriptRegularStatements/Unmap.htm)
- [*ApplyMap Script function*](../MappingFunctions/ApplyMap.htm)
- [*MapSubstring Script function*](../MappingFunctions/MapSubstring.htm)
- [*Mapping functions*](../MappingFunctions/mapping-functions.htm)
- [*Drop table*](../ScriptRegularStatements/drop-table.htm)
