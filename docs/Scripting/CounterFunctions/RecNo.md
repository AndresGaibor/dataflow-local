---
title: "RecNo Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/CounterFunctions/RecNo.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Counter functions"]
---

# RecNo Script function

This script function returns an integer for the number
of the currently read row of the current table. The first record is number
1.

Syntax:

RecNo( )

In contrast to RowNo(
), which counts rows in the resulting Qlik Sense table, RecNo(
), counts the records in the raw data table and is reset when a raw data table is concatenated
to another.

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
