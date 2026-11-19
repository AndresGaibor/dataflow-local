---
title: "Unqualify"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Unqualify.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements"]
---
# Unqualify

The
Unqualify statement is used for
switching off the qualification of field names that has been previously
switched on by the Qualify statement.

Syntax:

Unqualify \*fieldlist

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| \*fieldlist | A comma separated list of the fields for which qualification should be turned on. Using \* as field list indicates all fields. The wildcard characters \* and ? are allowed in field names. Quoting of field names may be necessary when wildcards are used.  Refer to the documentation for the Qualify statement for further information. |

Example 1:

In an unfamiliar database, it is often useful to start out by making sure
that only one or a few fields are associated, as illustrated in this example:

qualify \*;

unqualify
TransID;

SQL SELECT \*
from tab1;

SQL SELECT \*
from tab2;

SQL SELECT \*
from tab3;

First, qualification is turned on for all fields.

Then qualification is turned off for TransID.

Only TransID will be used for associations
between the tables tab1, tab2 and tab3. All other fields will be qualified with the table name.

## Learn more

- [*Qualify*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Qualify.htm)
