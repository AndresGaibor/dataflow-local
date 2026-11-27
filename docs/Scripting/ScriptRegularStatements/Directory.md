---
title: "Directory"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Directory.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements"]
---

# Directory

The Directory
statement defines which directory to look in for data files in subsequent LOAD statements,
until a new Directory statement is made.

Syntax:

Directory[path]

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| path | A text that can be interpreted as the path to the data file.  The path is the path to the file, either:   - Root folder of a [connection](#glossary-0 "Glossary term") library.  Example: Lib://SomeFolder/ - URL address (HTTP   or FTP), pointing to a location on the Internet or an intranet.  Example: http://www.qlik.com |

Examples:

Directory lib://DataFiles/;

Directory lib://OneDrive - dr.no@example.com/Data/;

## Learn more

- [*Load*](Load.htm)
