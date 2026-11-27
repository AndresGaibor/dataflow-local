---
title: "Conditional functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ConditionalFunctions/conditional-functions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions"]
---

# Conditional functions

Expand/Collapse all

# Conditional functions

The conditional functions all evaluate a condition and then return different answers depending on the condition value. The functions can be used in the data [load script](#glossary-0 "Glossary term") and in chart expressions.

Use the drop-down on each function to see a brief description and the syntax of each function. Click the function name in the syntax description for further details.

alt

The alt function returns the
first of the parameters that has a valid number representation. If no
such match is found, the last parameter will be returned. Any number of
parameters can be used.

[**alt**](alt.htm)(expr1[ , expr2
, expr3 , ...]
, else)

class

The class function assigns the first parameter to a class interval.
The result is a dual value with a<=x<b as the textual value, where a and b are the upper and lower
limits of the bin, and the lower bound as numeric value.

[**class**](class.htm)(expression, interval [ , label [ , offset ]])

coalesce

The coalesce function returns the first of the parameters that has a valid non-NULL representation. Any number of parameters can be used.

[**coalesce**](coalesce.htm)(expr1[ , expr2
, expr3 , ...])

if

The if function returns a value depending on whether the condition provided with the function evaluates as True or False.

[**if**](if.htm)(condition , then , else)

match

The match function compares the first parameter with all the following ones and returns the numeric location of the expressions that match. The comparison is case sensitive.

[**match**](match.htm)( str, expr1
[ , expr2,...exprN ])

mixmatch

The mixmatch function compares the first parameter with all the following ones and returns the numeric location of the expressions that match. The comparison is case insensitive and insensitive to the Japanese Hiragana and Katakana character systems.

[**mixmatch**](mixmatch.htm)( str, expr1
[ , expr2,...exprN ])

pick

The pick function returns the n:th expression
in the list.

[**pick**](pick.htm)(n, expr1[ , expr2,...exprN])

wildmatch

The wildmatch function compares the first parameter with all the following ones and returns the number of the expression that matches. It permits the use of wildcard characters
( \* and ?)
in the comparison strings.  \* matches any sequence of characters. ? matches any single character. The comparison is case insensitive and insensitive to the Japanese Hiragana and Katakana character systems.

[**wildmatch**](wildmatch.htm)( str, expr1 [ , expr2,...exprN ])
