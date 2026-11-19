---
title: "FileExtension Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FileFunctions/FileExtension.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "File functions"]
---
# FileExtension Script function

The FileExtension function returns a string containing the extension of the table file currently
being read.

Syntax:

FileExtension()

Examples and results:

Scripting examples

| Example | Result |
| --- | --- |
| LOAD \*, FileExtension( ) as X from  C:\UserFiles\abc.txt | Will return 'txt' in [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FileFunctions/FileExtension.htm#glossary-0 "Glossary term") X in each record read. |
