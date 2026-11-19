---
title: "Qualify"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Qualify.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements"]
---
# Qualify

The Qualify statement is used for switching on the qualification of field names, i.e. field names will get the table name as a prefix.

Syntax:

Qualify \*fieldlist

The automatic join between fields with the same name in different tables can be
suspended by means of the qualify statement, which qualifies the [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Qualify.htm#glossary-0 "Glossary term") name with
its table name. If qualified, the field name(s) will be renamed when found in a
table. The new name will be in the form of tablename.fieldname. Tablename is
equivalent to the label of the current table, or, if no label exists, to the
name appearing after from in LOAD and SELECT statements.

The qualification will be made for all fields loaded after the qualify statement.

Qualification is always turned off by default at the beginning of script
execution. Qualification of a field name can be activated at any time using a
qualify statement. Qualification can be turned off at any time using an
Unqualify statement.

> **Note:** The qualify
> statement should not be used in conjunction with partial reload.

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| \*fieldlist | A comma separated list of the fields for which qualification should be turned on. Using \* as field list indicates all fields. The wildcard characters \* and ? are allowed in field names. Quoting of field names may be necessary when wildcards are used. |

Example 1:

Qualify B;

LOAD A,B
from x.csv;

LOAD A,B
from y.csv;

The two tables x.csv and y.csv are associated only through A.
Three fields will result: A, x.B, y.B.

Example 2:

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

Only TransID will be used for associations
between the tables tab1, tab2 and tab3.

## Learn more

- [*Unqualify*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Unqualify.htm)
