---
title: "Search"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Search.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements"]
---

# Search

The Search statement is used for including or excluding fields in smart search.

Syntax:

Search Include \*fieldlist

Search Exclude \*fieldlist

You can use several Search statements to refine your selection of fields to include. The statements are evaluated from top to bottom.

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| \*fieldlist | A comma separated list of the fields to include or exclude from searches in smart search. Using \* as field list indicates all fields. The wildcard characters \* and ? are allowed in field names. Quoting of field names may be necessary when wildcards are used. |

Example:

Search examples

| Statement | Description |
| --- | --- |
| Search Include \*; | Include all fields in searches in smart search. |
| Search Exclude [\*ID]; | Exclude all fields ending with ID from searches in smart search. |
| Search Exclude '\*ID'; | Exclude all fields ending with ID from searches in smart search. |
| Search Include ProductID; | Include the field ProductID in searches in smart search. |

The combined result of these three statements, in this sequence, is that all fields ending with ID except ProductID are excluded from searches in smart search.

## Learn more

- [*Using smart search*](../../Search/use-smart-search-tool.htm)
