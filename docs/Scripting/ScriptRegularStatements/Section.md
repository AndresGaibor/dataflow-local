---
title: "Section"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Section.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements"]
---
# Section

With the section statement,
it is possible to define whether the subsequent LOAD and SELECT statements should be considered
as data or as a definition of the access rights.

Syntax:

Section (access | application | directquery)

If nothing is specified, section
application is assumed. The section
definition is valid until a new section statement is made.

If you specify **section directquery**, the application will becomes a Direct Query application when the load script is run. For more information, see [*Creating a Direct Query application with custom SQL*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DirectQuery/create-data-model-custom-sql.htm).

Example:

Section
access;

Section
application;
