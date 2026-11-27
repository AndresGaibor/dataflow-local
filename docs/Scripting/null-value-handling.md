---
title: "NULL value handling"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/null-value-handling.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Understanding script syntax and data structures"]
---

# NULL value handling

When no data can be produced for a certain [field](#glossary-0 "Glossary term") as a result of a database
query and/or a join between tables, the result is normally a NULL value.

## Overview

The Qlik Sense logic treats the following as real NULL values:

- NULL values returned from an ODBC [connection](#glossary-1 "Glossary term").
- NULL values created as a result of a forced concatenation
  of tables in the [data load script](#glossary-2 "Glossary term").
- NULL values created as a result of a join made in the
  data load script
- NULL values created as a result of the generation of
  field value combinations to be displayed in a table

Information noteIt is generally impossible to use these NULL values for associations
and selections except
when the NullAsValue
statement is being employed.

For more information about NullAsValue, see [*NullAsValue*](ScriptRegularStatements/NullAsValue.htm).

Text files per definition cannot
contain NULL values.

## Associating/selecting NULL values from ODBC

It is possible to associate and/or select NULL values from an ODBC
data source. For this purpose a script variable has been defined.
The following syntax can be used:

SET NULLDISPLAY=<sym>;

The symbol <sym> will substitute all NULL values from the ODBC data source on the lowest level of data input. <sym> may be any
string.

In order to reset this functionality to the default interpretation,
use the following syntax:

SET NULLDISPLAY=;

Information noteThe use of NULLDISPLAY only affects data from an ODBC data source.

If you wish to have the Qlik Sense logic interpret NULL values returned
from an ODBC connection as an empty string, add the following to your
script before any SELECT statement:

SET NULLDISPLAY=";

Information noteHere '' is actually two single quotation marks without anything in between.

For more information about NullDisplay, see [*NullDisplay*](ValueHandlingVariables/NullDisplay.htm) .

## Creating NULL values from text files

It is possible to define a symbol, which when it occurs in a text file
or an inline clause will be interpreted
as a real NULL value. Use the following statement:

SET NULLINTERPRET=<sym>;

The symbol <sym> is to be interpreted as NULL. <sym> may
be any string.

In order to reset this functionality to the default interpretation,
use:

SET NULLINTERPRET=;

Information note The use of NULLINTERPRET
only affects data from text files and inline clauses.

For more information about NullInterpret, see [*NullInterpret*](ValueHandlingVariables/NullInterpret.htm) .

## Propagation of NULL values in expressions

NULL values will propagate through an expression according to a few
logical and quite reasonable rules.

### Functions

The general rule is that functions return NULL when the parameters fall
outside the range for which the function is defined.

Examples

| Expression | Result |
| --- | --- |
| asin(2) | returns NULL |
| log(-5) | returns NULL |
| round(A,0) | returns NULL |

As a result of the above follows that functions generally return NULL
when any of the parameters necessary for the evaluation are NULL.

Examples

| Expression | Result |
| --- | --- |
| sin(NULL) | returns NULL |
| chr(NULL) | returns NULL |
| if(NULL, A, B) | returns B |
| if(True, NULL, A) | returns NULL |
| if(True, A, NULL) | returns A |

The exception to the second rule are logical functions testing for type.

Examples

| Expression | Result |
| --- | --- |
| isnull(NULL) | returns True (-1) |
| isnum(NULL) | returns False (0) |

### Arithmetic and string operators

If NULL is encountered on any side of these operators NULL is returned.

Examples

| Expression | Result |
| --- | --- |
| A + NULL | returns NULL |
| A - NULL | returns NULL |
| A / NULL | returns NULL |
| A \* NULL | returns NULL |
| NULL  / A | returns NULL |
| 0 / NULL | returns NULL |
| 0 \* NULL | returns NULL |
| A & NULL | returns A |

### Relational operators

If NULL is encountered on any side of relational operators special rules
apply.

Examples

| Expression | Result |
| --- | --- |
| NULL  (any relation operator) NULL | returns NULL |
| A <> NULL | returns True (-1) |
| A < NULL | returns False (0) |
| A <= NULL | returns False (0) |
| A = NULL | returns False (0) |
| A >= NULL | returns False (0) |
| A > NULL | returns False (0) |
