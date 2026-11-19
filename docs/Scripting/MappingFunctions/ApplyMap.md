---
title: "ApplyMap Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/MappingFunctions/ApplyMap.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Mapping functions"]
---
# ApplyMap Script function

The ApplyMap script function is used
for mapping the output of an expression to a previously loaded mapping table.

Syntax:

ApplyMap('map\_name',
expression [
, default\_mapping ] )

Return data type: dual

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| map\_name | The name of a mapping table that has previously been created through the mapping load or the mapping select statement. Its name must be enclosed by single, straight quotation marks.  **Warning:** If you use this function in a macro expanded [variable](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/MappingFunctions/ApplyMap.htm#glossary-0 "Glossary term") and refer to a mapping table that does not exist, the function call fails and a [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/MappingFunctions/ApplyMap.htm#glossary-1 "Glossary term") is not created. |
| expression | The expression, the result of which should be mapped. |
| default\_mapping | If stated, this value will be used as a default value if the mapping table does not contain a matching value for expression. If not stated, the value of expression will be returned as is. |

> **Warning:** The output field of ApplyMap should not have the same name as one of its input fields. This may cause unexpected results. Example not to use: ApplyMap('Map', A) as A.

Example:

In this example we load a list of salespersons with a country code representing their country of residence. We use a table mapping a country code to a country to replace the country code with the country name. Only three countries are defined in the mapping table, other country codes are mapped to 'Rest of the world'.

// Load mapping table of country codes:
map1:
mapping LOAD \*
Inline [
CCode, Country
Sw, Sweden
Dk, Denmark
No, Norway
] ;
// Load list of salesmen, mapping country code to country
// If the country code is not in the mapping table, put Rest of the world
Salespersons:
LOAD \*,
ApplyMap('map1', CCode,'Rest of the world') As Country
Inline [
CCode, Salesperson
Sw, John
Sw, Mary
Sw, Per
Dk, Preben
Dk, Olle
No, Ole
Sf, Risttu
] ;
// We don't need the CCode anymore
Drop Field 'CCode';

The resulting table (Salespersons) looks like this:

Resulting table

| Salesperson | Country |
| --- | --- |
|
|  |
| John | Sweden |
| Mary | Sweden |
| Per | Sweden |
| Preben | Denmark |
| Olle | Denmark |
| Ole | Norway |
| Risttu | Rest of the world |

## Learn more

- [*Mapping*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Mapping.htm)
- [*Using quotation marks in the script*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/use-quotes-in-script.htm)
