---
title: "NullAsNull"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/NullAsNull.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements"]
---

# NullAsNull

The NullAsNull statement turns
off the conversion of NULL values to string values previously set by a NullAsValue statement.

Syntax:

NullAsNull \*fieldlist

The NullAsValue statement operates as a switch and can be turned on or off several times in the script, using either a NullAsValue or a NullAsNull statement.

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| \*fieldlist | A comma separated list of the fields for which NullAsNull should be turned on. Using \* as field list indicates all fields. The wildcard characters \* and ? are allowed in field names. Quoting of field names may be necessary when wildcards are used. |

Example:

NullAsNull A,B;

LOAD A,B from x.csv;

## Learn more

- [*NullAsValue*](NullAsValue.htm)
