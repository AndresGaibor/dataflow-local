---
title: "Format specification items"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptSpecifiers/format-specification-items.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements", "Load"]
---
Expand/Collapse all

# Format specification items

Each format specification item defines a certain property of the table
file:

fspec-item ::=
[ ansi | oem | mac | UTF-8 | Unicode | txt | fix | dif | biff | ooxml |
html | xml | kml | qvd | qvx | parquet | json | delimiter is char | no
eof | embedded labels | explicit labels | no labels | table is [tablename] | header is n | header is line | header is n lines | comment is string | record
is n | record is line | record is n lines
| no quotes |msq | URL is string | userAgent is string]

Use the drop-down on each function to see a brief description and the syntax of each function. Click the function name in the syntax description for further details.

Character set

Character set is a file specifier for the LOAD statement that defines the character set used in the file.

ansi | oem | mac | UTF-8 | Unicode | codepage is |

[*Character set*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptSpecifiers/character-set.htm)

Table format

The table format is a file specifier for the LOAD statement that defines the file type. If nothing is specified, a .txt
file is assumed.

txt | fix | dif | biff |
ooxml |
html | xml | qvd | qvx | parquet | json |

[*Table format*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptSpecifiers/table-format.htm)

Delimiter is

For delimited table files, an arbitrary
delimiter can be specified through the delimiter
is specifier. This specifier is relevant only for delimited .txt
files.

[**delimiter**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptSpecifiers/delimiter.htm) char

Table is

For XML, Excel, JSON, or nested Parquet files, Table is specifies the table to load from the file.

[**table-is**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptSpecifiers/table-is.htm) char

Header is

Specifies the header size in table files. An arbitrary header length can be specified
through the header is specifier. A header is a text section not used by Qlik Sense.

[**header-is**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptSpecifiers/header-is.htm) n

Header is line

Header is n lines

Comment is

If you have lines in your source data file that are comments, you can define a comment prefix with Comment is. Set commentprefix to the character or string that comment lines start with, and these lines will be ignored when you load data.

Comment is commentprefix

labels

Labels is a file specifier for the LOAD statement that defines where in a file the field names can be found.

embedded
[**labels**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptSpecifiers/labels.htm) | explicit
labels|no labels

no eof

The no eof specifier is used to disregard end-of-file character when loading delimited .txt
files.

[**no-eof**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptSpecifiers/no-eof.htm)

quotes

Quotes is a file specifier for the LOAD statement that defines whether quotes can be used and the precedence between quotes and separators. For text files only.

no [**quotes**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptSpecifiers/quotes.htm)

msq

Record is

For fixed record length files, the record
length must be specified through the record
is specifier.

[**record-is**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptSpecifiers/record-is.htm) n

Record is line

Record is n lines

XML

This script specifier is used when loading xml files. Valid options for the XML specifier are listed in syntax.

xmlsimple

[*XML*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptSpecifiers/XML.htm)

KML

This script specifier is used when loading KML files to use in a map visualization.

[**KML**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptSpecifiers/KML.htm)

## Learn more

- [*Load*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Load.htm)
- [*Select*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Select.htm)
