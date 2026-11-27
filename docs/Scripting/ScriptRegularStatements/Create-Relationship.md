---
title: "Create relationship"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Create-Relationship.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements"]
---

# Create relationship

CREATE RELATIONSHIP specifies new tables and columns relationship in a Direct Query application data model.

CREATE RELATIONSHIP can only be used in a Direct Query application. It must be preceded by a section directquery section.

Syntax:

CREATE RELATIONSHIP (OUTER|INNER) JOINED] TableName, [(OUTER|INNER) JOINED] TableName ON ConditionExpression ;

Information note

If an outer|inner joined qualifier for a table is not specified then the default will be inner joined.

Information note

For TableName, you can use quoted name name references. For example, ( IDENTIFIER | LITERAL\_STRING | LITERAL\_FIELD | LITERAL\_NUMBER)).

Examples:

CREATE RELATIONSHIP BETWEEN T1,T2 ON A = C;

CREATE RELATIONSHIP
BETWEEN OUTER JOINED T2, INNER JOINED T3
ON (D = E or (D is null and E is null));
