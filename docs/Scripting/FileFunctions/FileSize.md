---
title: "FileSize Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FileFunctions/FileSize.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "File functions"]
---
# FileSize Script function

The FileSize function returns an integer containing the size in bytes of the file filename
or, if no filename is specified,
of the table file currently being read.

Syntax:

FileSize([filename])

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| filename | The name of a file, if necessary including path, as a folder or web file [data connection](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FileFunctions/FileSize.htm#glossary-0 "Glossary term") If you don't specify a file name, the table file currently being read is used.  Example: 'lib://Table Files/' |

Examples and results:

Scripting examples

| Example | Result |
| --- | --- |
| LOAD \*, FileSize( ) as X from abc.txt; | Will return the size of the specified file (abc.txt) as an integer in [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FileFunctions/FileSize.htm#glossary-1 "Glossary term") X in each record read. |
| `FileSize( 'lib://DataFiles/xyz.xls' )` | Will return the size of the file xyz.xls. |
