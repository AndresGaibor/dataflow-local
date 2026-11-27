---
title: "MapSubstring Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/MappingFunctions/MapSubstring.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Mapping functions"]
---

# MapSubstring Script function

The MapSubstring script function is
used to map parts of any expression to a previously loaded mapping table.
The mapping is case sensitive and non-iterative, and substrings are mapped
from left to right.

Syntax:

MapSubstring('map\_name',
expression)

Return data type: string

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| map\_name | The name of a mapping table previously read by a mapping load or a mapping select statement. The name must be enclosed by single straight quotation marks.  Warning noteIf you use this function in a macro expanded [variable](#glossary-0 "Glossary term") and refer to a mapping table that does not exist, the function call fails and a [field](#glossary-1 "Glossary term") is not created. |
| expression | The expression whose result is to be mapped by substrings. |

Example:

In this example we load a list of product models. Each model has a set of attributes that are described by a composite code. Using the mapping table with MapSubstring, we can expand the attribute codes to a description.

map2:
mapping LOAD \*
Inline [
AttCode, Attribute
R, Red
Y, Yellow
B, Blue
C, Cotton
P, Polyester
S, Small
M, Medium
L, Large
] ;
Productmodels:
LOAD \*,
MapSubString('map2', AttCode) as Description
Inline [
Model, AttCode
Twixie, R C S
Boomer, B P L
Raven, Y P M
Seedling, R C L
SeedlingPlus, R C L with hood
Younger, B C with patch
MultiStripe, R Y B C S/M/L
] ;
// We don't need the AttCode anymore
Drop Field 'AttCode';

The resulting table looks like this:

Resulting table

| Model | Description |
| --- | --- |
| Twixie | Red Cotton Small |
| Boomer | Blue Polyester Large |
| Raven | Yellow Polyester Medium |
| Seedling | Red Cotton Large |
| SeedlingPlus | Red Cotton Large with hood |
| Younger | Blue Cotton with patch |
| MultiStripe | Red Yellow Blue Cotton Small/Medium/Large |

## Learn more

- [[*Mapping*](../ScriptPrefixes/Mapping.htm)](../ScriptPrefixes/Mapping.htm)
- [*Using quotation marks in the script*](../use-quotes-in-script.htm)
