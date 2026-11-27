---
title: "FileBaseName Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FileFunctions/FileBaseName.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "File functions"]
---

# FileBaseName Script function

The FileBaseName function returns a string containing the name of the table file currently being
read, without path or extension.

Syntax:

FileBaseName()

Examples and results:

Scripting examples

| Example | Result |
| --- | --- |
| LOAD \*, filebasename( ) as X from  C:\UserFiles\abc.txt | Will return 'abc' in [field](#glossary-0 "Glossary term") X in each record read. |
