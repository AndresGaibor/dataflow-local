---
title: "FileDir Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FileFunctions/FileDir.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "File functions"]
---

# FileDir Script function

The FileDir function returns a string containing the path to the directory of the table file
currently being read.

Syntax:

FileDir()

Examples and results:

Scripting examples

| Example | Result |
| --- | --- |
| Load \*, FileDir( ) as X from [lib://DataFiles/Region.txt] | Will return 'lib://DataFiles' in [field](#glossary-0 "Glossary term") X in each record read. |
