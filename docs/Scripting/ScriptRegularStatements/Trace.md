---
title: "Trace"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Trace.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements"]
---

# Trace

The trace statement writes a string to the Script
Execution Progress window and to the script log file, when used. It is very useful for debugging purposes. Using $-expansions of variables that are calculated prior to the trace statement, you can customize the message.

Syntax:

Trace string

Example 1:

The following statement can be used right after the Load statement that loads the 'Main' table.

Trace Main
table loaded;

This will display the text ‘Main table loaded’ in the script execution dialog and in the log file.

Example 2:

The following statements can be used right after the Load statement that loads the 'Main' table.

Let MyMessage = NoOfRows('Main') & ' rows in Main table';

Trace $(MyMessage);

This will display a text showing the number of rows in the script execution dialog and in the log file, for example, ‘265,391 rows in Main table’ .
