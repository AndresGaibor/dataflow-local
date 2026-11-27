---
title: "Script expressions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/script-expressions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions"]
---

# Script expressions

Expressions can be used in both LOAD
statements and SELECT
statements. The syntax and functions
described here apply to the LOAD statement, and not to the SELECT statement, since the latter is interpreted
by the ODBC driver and
not by Qlik Sense. However, most ODBC drivers are often capable of interpreting
a number of the functions described below.

Expressions consist of functions, fields and operators, combined in a syntax.

All expressions in a Qlik Sense script return a number and/or a string,
whichever is appropriate. Logical functions and operators return 0 for False
and -1 for True. Number to string conversions and vice versa are implicit.
Logical operators and functions interpret 0 as False and all else as True.

The general syntax for an expression is:

General syntax

| Expression | Fields | Operator |
| --- | --- | --- |
| expression ::= (constant | constant | | |
| expression ::= (constant | fieldref | | |
| expression ::= (constant | operator1 expression | | |
| expression ::= (constant | expression operator2 expression | | |
| expression ::= (constant | function | | |
| expression ::= (constant | ( expression ) | ) |

where:

- constant is a string (a text,
  a date or a time) enclosed by single straight quotation marks, or a number.
  Constants are written with no thousands separator and with a decimal point
  as the decimal separator.
- fieldref is a field name of
  the loaded table.
- operator1 is a unary operator
  (working on one expression, the one to the right).
- operator2 is a binary operator
  (working on two expressions, one on each side).
- function ::= functionname(
  parameters)
- parameters ::= expression { , expression
  }

The number and types of parameters are not arbitrary. They depend on the
function used.

Expressions and functions can thus be nested freely, and as long as
the expression returns an interpretable value, Qlik Sense will not give
any error messages.

## Learn more

- [*NULL value handling*](null-value-handling.htm)
- [*Dollar-sign expansions*](dollar-sign-expansions.htm)
- [*Using quotation marks in the script*](use-quotes-in-script.htm)
