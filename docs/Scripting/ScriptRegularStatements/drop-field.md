---
title: "Drop field"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/drop-field.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements", "Drop"]
---
# Drop field

One or several Qlik Sense fields can be dropped from the data model, and thus from memory, at any time
during script execution, by means of a drop
field statement. The "distinct" property of a table is removed after a drop field statement.

> **Note:** Both drop field and drop fields are allowed forms with
> no difference in effect. If no table is specified, the field will be dropped from all tables where
> it occurs.

Syntax:

Drop field fieldname { , fieldname2 ...} [from tablename1 { , tablename2 ...}]

Drop fields fieldname { , fieldname2 ...} [from tablename1 { , tablename2 ...}]

Examples:

Drop
field A;

Drop
fields A,B;

Drop
field A from X;

Drop
fields A,B from X,Y;

## Learn more

- [*Drop table*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/drop-table.htm)
- [*Drop*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Drop.htm)
- [*Field/Fields*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Field.htm)
