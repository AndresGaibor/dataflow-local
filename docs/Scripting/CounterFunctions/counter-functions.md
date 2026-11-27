---
title: "Counter functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/CounterFunctions/counter-functions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions"]
---

# Counter functions

Expand/Collapse all

# Counter functions

This section describes functions related to record counters during LOAD statement evaluation in the data [load script](#glossary-0 "Glossary term"). The only function that can be used in chart expressions is RowNo().

Some counter functions do not have any parameters, but the trailing parentheses are however
still required.

Use the drop-down on each function to see a brief description and the syntax of each function. Click the function name in the syntax description for further details.

autonumber

This script function returns a unique integer value for each distinct evaluated value of
expression encountered during
the script execution. This function can be used e.g. for creating a compact
memory representation of a complex key.

[**autonumber**](autonumber.htm)(expression[ , AutoID])

autonumberhash128

This script function calculates
a 128-bit hash of the combined input expression values and the returns
a unique integer value for each distinct hash value encountered during
the script execution. This function can be used for example for creating a compact
memory representation of a complex key.

[**autonumberhash128**](autonumberhash128.htm)(expression
{, expression})

autonumberhash256

This script function calculates
a 256-bit hash of the combined input expression values and returns a unique
integer value for each distinct hash value encountered during the script
execution. This function can be used e.g. for creating a compact memory
representation of a complex key.

[**autonumberhash256**](autonumberhash256.htm)(expression
{, expression})

IterNo

This script function returns an integer indicating for which time one single record
is evaluated in a LOAD statement
with a while clause. The first
iteration has number 1. The IterNo function is only meaningful if used together with a while clause.

[**IterNo**](IterNo.htm)( )

RecNo

This script function returns an integer for the number
of the currently read row of the current table. The first record is number
1.

[**RecNo**](RecNo.htm)( )

RowNo - script function

This function returns an integer for the position of the current row in the resulting
Qlik Sense internal table. The first row is number 1.

[**RowNo**](RowNo.htm)( )

RowNo - chart function

RowNo() returns the number of the current row within the current column segment
in a table. For bitmap charts, RowNo() returns the number of the current row within the chart's straight table equivalent.

[**rowno**](../../ChartFunctions/InterRecordFunctions/rowno.htm)([TOTAL])
