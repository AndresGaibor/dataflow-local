---
title: "Character set"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptSpecifiers/character-set.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements", "Load"]
---
# Character set

Character set is a file specifier for the LOAD statement that defines the character set used in the file.

The ansi, oem and mac specifiers were used in QlikView and will still work. However, they will not be generated when creating the LOAD statement with Qlik Sense.

Syntax:

utf8 | unicode | ansi | oem | mac | codepage is

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| utf8 | UTF-8 character set |
| unicode | Unicode character set |
| ansi | Windows, codepage 1252 |
| oem | DOS, OS/2, AS400 and others |
| mac | Codepage 10000 |
| codepage is | With the codepage specifier, it is possible to use any Windows codepage as  N . |

Limitations:

Conversion
from the oem character set is
not implemented for macOS. If nothing is specified, codepage 1252 is assumed under Windows.

Example:

LOAD \* from a.txt (utf8, txt, delimiter is ',' , embedded labels)

LOAD \* from a.txt (unicode, txt, delimiter is ',' , embedded labels)

LOAD \* from
a.txt (codepage is 10000, txt, delimiter is ',' , no labels)

## Learn more

- [*Load*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Load.htm)
