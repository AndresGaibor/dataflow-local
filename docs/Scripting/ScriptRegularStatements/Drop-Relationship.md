---
title: "Drop relationship"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Drop-Relationship.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements", "Drop"]
---

# Drop relationship

One or several Direct Query relationships can be dropped from the data model in the section directquery section of a load script by means of a DROP RELATIONSHIP statement.

DROP RELATIONSHIP is useful if there is a previous IMPORT LIVE <datamodelobject> in your load script that contains a Data model manager-defined relationship you want to remove.

Syntax:

DROP RELATIONSHIP BETWEEN tablename {, tablename2 ...}

Information noteFor TableName, you can use quoted name name references. For example, ( IDENTIFIER | LITERAL\_STRING | LITERAL\_FIELD | LITERAL\_NUMBER)).

Example:

DROP RELATIONSHIP BETWEEN Table1, Table2
