---
title: "FileTime Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FileFunctions/FileTime.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "File functions"]
---

# FileTime Script function

The FileTime function returns a timestamp in UTC format of the last modification of a specified file. If a file is not specified, the function returns a timestamp in UTC of the last modification of the currently read table file.

Syntax:

FileTime([ filename ])

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| filename | The name of a file, if necessary including path, as a folder or web file [data connection](#glossary-0 "Glossary term")  Example: 'lib://Table Files/' |

Examples and results:

Script examples

| Example | Result |
| --- | --- |
| LOAD \*, FileTime( ) as X from abc.txt; | Will return the timestamp of the last modification of the file (abc.txt) in [field](#glossary-1 "Glossary term") X in each record read. |
| FileTime( 'xyz.xls' ) | Will return the timestamp of the last modification of the file xyz.xls. |
