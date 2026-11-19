---
title: "FilePath Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FileFunctions/FilePath.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "File functions"]
---
# FilePath Script function

The FilePath function returns a string containing the full path to the table file currently
being read.

Syntax:

FilePath()

Examples and results:

Scripting examples

| Example | Result |
| --- | --- |
| Load \*, FilePath( ) as X from [lib://DataFiles/Region.txt] | Will return  'lib://DataFiles/Region.txt' in [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FileFunctions/FilePath.htm#glossary-0 "Glossary term") X in each record read. |
