---
title: "Comment table"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/comment-table.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements"]
---
# Comment table

Provides a way of displaying the table comments (metadata) from databases or spreadsheets.

Table names not present in the application are ignored. If multiple occurrences of a table name are found, the last value is used. The keyword can be used to read comments from a data source.

Syntax:

comment [tables] tablelist using mapname

comment [table] tablename with comment

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| tablelist | (table{,table}) |
| mapname | The name of a mapping table previously read in a mapping LOAD or mapping SELECT statement. |
| tablename | The name of the table that should be commented. |
| comment | The comment that should be added to the table. |

Example 1:

Commentmap:

mapping LOAD \* inline [

a,b

Main,This is the fact table

Currencies, Currency helper table

];

comment tables using Commentmap;

Example 2:

comment table Main with 'Main fact table';

## Learn more

- [*Comment field*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/comment.htm)
- [*Table/Tables*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Table.htm)
