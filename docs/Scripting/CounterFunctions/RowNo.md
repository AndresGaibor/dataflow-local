---
title: "RowNo Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/CounterFunctions/RowNo.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Counter functions"]
---

# RowNo Script function

This function returns an integer for the position of the current row in the resulting
Qlik Sense internal table. The first row is number 1.

Syntax:

RowNo( [TOTAL])

In contrast to RecNo(
), which counts the records in the raw data table, the RowNo(
) function does not count records that are excluded by where
clauses and is not reset when a raw data table is concatenated
to another.

Information noteIf you use [preceding load](#glossary-0 "Glossary term"), that is, a number of stacked LOAD  statements reading from the same table, you can only use RowNo(
) in the top LOAD  statement. If you use RowNo(
) in subsequent LOAD  statements, 0 is returned.

Example: Data load script

Raw data table load:

Tab1:
LOAD \* INLINE
[A, B
1, aa
2,cc
3,ee];
Tab2:
LOAD \* INLINE
[C, D
5, xx
4,yy
6,zz];

Loading record and row numbers for selected rows:

QTab:

LOAD \*,

RecNo( ),

RowNo( )

resident Tab1 where A<>2;

LOAD

C as A,

D as B,

RecNo( ),

RowNo( )

resident Tab2 where A<>5;

//We don't need the source tables anymore, so we drop them

Drop tables Tab1, Tab2;

The
resulting Qlik Sense internal table:

Results table

| A | B | RecNo( ) | RowNo( ) |
| --- | --- | --- | --- |
| 1 | aa | 1 | 1 |
| 3 | ee | 3 | 2 |
| 4 | yy | 2 | 3 |
| 6 | zz | 3 | 4 |
