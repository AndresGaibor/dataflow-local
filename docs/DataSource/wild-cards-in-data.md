---
title: "Wild cards in the data"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataSource/wild-cards-in-data.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Understanding script syntax and data structures"]
---

# Wild cards in the data

You can use wild cards in the data. Two different wild cards exist: the star symbol, interpreted as all values of this [field](#glossary-0 "Glossary term"), and an optional symbol, interpreted as all remaining values of this field.

## The star symbol

The star symbol is interpreted as all (listed) values of this field, that is, a value listed elsewhere in this table. If used in one of the system fields (USERID, PASSWORD, NTNAME or SERIAL) in a table loaded in the access section of the script, it is interpreted as all (also not listed) possible values of this field.

There is no star symbol available unless explicitly specified. For information on how to make a star statement in the script, see [*Star*](../Scripting/ScriptRegularStatements/Star.htm).

## OtherSymbol

In many cases a way to represent all other values in a table is needed, that is, all values that were not explicitly found in the loaded data. This is done with a special [variable](#glossary-1 "Glossary term") called OtherSymbol. To define the OtherSymbol to be treated as "all other values", use the following syntax:

SET OTHERSYMBOL=<sym>;

before a LOAD or SELECT statement. <sym> may be any string.

The appearance of the defined symbol in an internal table will cause Qlik Sense to define it as all values not previously loaded in the field where it is found. Values found in the field after the appearance of the OtherSymbol will thus be disregarded.

In order to reset this functionality use:

SET OTHERSYMBOL=;

Example:

Table Customers

| CustomerID | Name |
| --- | --- |
| 1 | ABC Inc. |
| 2 | XYZ Inc. |
| 3 | ACME INC |
| + | Undefined |

Table Orders

| CustomerID | OrderID |
| --- | --- |
| 1 | 1234 |
| 3 | 1243 |
| 5 | 1248 |
| 7 | 1299 |

Insert the following statement in the script before the point where the first table above is loaded:

SET OTHERSYMBOL=+;

Any reference to a CustomerID other than 1, 2 or 3, e.g. as when clicking on OrderID 1299 will result in Undefined under Name.

Information noteOtherSymbol is not intended to be used for creating outer joins between tables.
