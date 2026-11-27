---
title: "ConnectString Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FileFunctions/ConnectString.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "File functions"]
---

# ConnectString Script function

The ConnectString() function returns the name of the active data connection for ODBC or OLE DB connections. The function returns an empty string if no connect statement has been executed, or after a disconnect statement.

Syntax:

ConnectString()

Examples and results:

Scripting examples

| Example | Result |
| --- | --- |
| LIB CONNECT TO 'Tutorial ODBC';  ConnectString:  Load ConnectString() as ConnectString AutoGenerate 1; | Returns 'Tutorial ODBC' in [field](#glossary-0 "Glossary term") ConnectString.  This example assumes that you have an available [data connection](#glossary-1 "Glossary term") called Tutorial ODBC. |
