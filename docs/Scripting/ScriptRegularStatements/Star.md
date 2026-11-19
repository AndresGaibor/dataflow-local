---
title: "Star"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Star.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements"]
---
# Star

The string used for representing the set of all the values of a field
in the database can be set through the star
statement. It affects the subsequent LOAD
and SELECT
statements.

Syntax:

Star is[
string ]

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| string | An arbitrary text. Note that the string must be enclosed by quotation marks if it contains blanks.  If nothing is specified, star is; is assumed, i.e. there is no star symbol available unless explicitly specified. This definition is valid until a new star statement is made. |

The Star is statement is not recommended for use in the data part of the script (under Section Application) if [section access](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Star.htm#glossary-0 "Glossary term") is used. The star character is however fully supported for the protected fields in the Section Access part of the script. In this case you do not need to use the explicit Star is statement since this is always implicit in section access.

## Limitations

- You cannot use the star character with key fields; that is, fields that link tables.
- You cannot use the star character with any fields affected by the Unqualify statement as this can affect fields that link tables.
- You cannot use the star character with non-logical tables, for example, info-load tables or mapping-load tables.
- When the star character is used in a reducing field (a field that links to the data) in section access , it represents the values listed in this field in section access. It does not represent other values that may exist in the data but are not listed in section access.
- You cannot use the star character with fields affected by any form of data reduction outside the Section Access area.

## Example

The example below is an extract of a data [load script](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Star.htm#glossary-1 "Glossary term") featuring section access.

Star is \*;

Section Access;

LOAD \* INLINE [

ACCESS, USERID, OMIT

ADMIN, ADMIN,

USER, USER1, SALES

USER, USER2, WAREHOUSE

USER, USER3, EMPLOYEES

USER, USER4, SALES

USER, USER4, WAREHOUSE

USER, USER5, \*

];

Section Application;

LOAD \* INLINE [

SALES, WAREHOUSE, EMPLOYEES, ORDERS

1, 2, 3, 4

];

The following applies:

- The Star sign is \*.
- The user ADMIN  sees all fields. Nothing is omitted.
- The user USER1 is not able to see the field SALES.
- The user USER2 is not able to see the field WAREHOUSE .
- The user USER3 cannot see the field EMPLOYEES.
- The user USER4 is added twice to the solution to OMIT two fields for this user, SALES and WAREHOUSE.
- The USER5 has a “\*” added which means that all listed fields in OMIT are unavailable, that is, user USER5 cannot see the fields SALES, WAREHOUSE and EMPLOYEES but this user can see the field ORDERS.
