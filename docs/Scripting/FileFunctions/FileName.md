---
title: "FileName Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FileFunctions/FileName.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "File functions"]
---

# FileName Script function

The FileName function returns a string containing the name of the table file currently being
read, without path but including the extension.

Syntax:

FileName()

Examples and results:

Scripting examples

| Example | Result |
| --- | --- |
| LOAD \*, FileName( ) as X from  lib://DataFiles/abc.txt | Will return  'abc.txt' in [field](#glossary-0 "Glossary term") X in each record read. |
