---
title: "System fields"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/system-fields.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Understanding script syntax and data structures", "Fields"]
---

# System fields

In
addition to the fields extracted from the data source, system fields are also produced by Qlik Sense. These all begin with "$" and can be displayed like ordinary fields in a [visualization](#glossary-0 "Glossary term"), such as a filter pane or a table. System fields are created automatically when you load data, and are primarily used as an aid in application design.

## Available system fields

The following system fields are available:

Available system fields

| System [field](#glossary-2 "Glossary term") | Description |
| --- | --- |
| $Table | Contains all tables that are loaded. |
| $Field | Contains all fields in the tables that are loaded. |
| $Fields | Contains the number of fields in each table. |
| $FieldNo | Contains the position of the fields in the tables. |
| $Rows | Contains the number of rows in the tables |

None of the system fields can be manipulated in the script.

## Using system fields in a visualization

System field data is associated. For example, if you add two filter panes, one with $Table and one with $Field, if you select a table, the $Field filter pane will show the fields in the selected table as possible values.

System fields are not included in field lists in the assets panel when you edit a sheet. They are included in the expression editor. If you want to use a system field in the assets panel, you need to reference it by typing it manually.

Example: In a dimension in the assets panel

=$Field
