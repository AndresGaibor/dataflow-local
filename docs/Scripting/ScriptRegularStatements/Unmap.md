---
title: "Unmap"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Unmap.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements"]
---

# Unmap

The Unmap statement disables field value
mapping specified by a previous Map … Using statement for subsequently loaded fields.

Syntax:

Unmap \*fieldlist

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| \*fieldlist | a comma separated list of the fields that should no longer be mapped from this point in the script. Using \* as field list indicates all fields. The wildcard characters \* and ? are allowed in field names. Quoting of field names may be necessary when wildcards are used. |

Examples and results:

| Example | Result |
| --- | --- |
| Unmap Country; | Disables mapping of [field](#glossary-0 "Glossary term") Country. |
| Unmap A, B, C; | Disables mapping of fields A, B and C. |
| Unmap \* ; | Disables mapping of all fields. |

## Learn more

- [*Map*](Map.htm)
