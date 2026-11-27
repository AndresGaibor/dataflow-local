---
title: "Disconnect"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Disconnect.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements"]
---

# Disconnect

The Disconnect statement terminates the current ODBC/OLE DB/Custom connection. This statement is optional.

Syntax:

Disconnect

The connection will be automatically terminated
when a new connect statement is
executed or when the script execution is finished.

Example:

Disconnect;
