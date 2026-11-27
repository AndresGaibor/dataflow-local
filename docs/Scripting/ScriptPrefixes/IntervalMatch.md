---
title: "IntervalMatch"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/IntervalMatch.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script prefixes"]
---

# IntervalMatch

The IntervalMatch prefix is used to create a table matching discrete numeric values to one or more numeric intervals, and optionally matching the values of one or several additional keys.

Syntax:

IntervalMatch (matchfield)(loadstatement | selectstatement )

IntervalMatch (matchfield,keyfield1
[ , keyfield2,
... keyfield5 ] ) (loadstatement
| selectstatement )

The IntervalMatch prefix must be placed before a LOAD or a SELECT statement that loads the intervals. The [field](#glossary-0 "Glossary term") containing the discrete data points (Time in the example below) and additional keys must already have been loaded into Qlik Sense before the statement with the IntervalMatch prefix. The prefix does not by itself read this field from the database table. The prefix transforms the loaded table of intervals and keys to a table that contains an additional column: the discrete numeric data points. It also expands the number of records so that the new table has one record per possible combination of discrete data point, interval and value of the key field(s).

The intervals may be overlapping and the discrete values will be linked to all matching intervals.

When the IntervalMatch prefix is extended with key fields, it is used to create a table matching discrete numeric values to one or more numeric intervals, while at the same time matching the values of one or several additional keys.

In order to avoid undefined interval limits being disregarded, it may be necessary to allow NULL values to map to other fields that constitute the lower or upper limits to the interval. This can be handled by the NullAsValue statement or by an explicit test that replaces NULL values with a numeric value well before or after any of the discrete numeric data points.

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| matchfield | The field containing the discrete numeric values to be linked to intervals. |
| keyfield | Fields that contain the additional attributes that are to be matched in the transformation. |
| loadstatement or selectstatement | Must result in a table, where the first field contains the lower limit of each interval, the second field contains the upper limit of each interval, and in the case of using key matching, the third and any subsequent fields contain the keyfield(s) present in the IntervalMatch statement. The intervals are always closed, i.e. the end points are included in the interval. Non-numeric limits render the interval to be disregarded (undefined). |

Example 1:

In the two tables below, the first one lists a number of discrete events and the second one defines the start and end times for the production of different orders. By means of the IntervalMatch prefix it is possible to logically connect the two tables in order to find out e.g. which orders were affected by disturbances and which orders were processed by which shifts.

EventLog:
LOAD \* Inline [
Time, Event, Comment
00:00, 0, Start of shift 1
01:18, 1, Line stop
02:23, 2, Line restart 50%
04:15, 3, Line speed 100%
08:00, 4, Start of shift 2
11:43, 5, End of production
];
OrderLog:
LOAD \* INLINE [
Start, End, Order
01:00, 03:35, A
02:30, 07:58, B
03:04, 10:27, C
07:23, 11:43, D
];
//Link the field Time to the time intervals defined by the fields Start and End.
Inner Join IntervalMatch ( Time )
LOAD Start, End
Resident OrderLog;

The table OrderLog contains now an additional column: Time. The number of records is also expanded.

Table with additional column

| Time | Start | End | Order |
| --- | --- | --- | --- |
| 00:00 | - | - | - |
| 01:18 | 01:00 | 03:35 | A |
| 02:23 | 01:00 | 03:35 | A |
| 04:15 | 02:30 | 07:58 | B |
| 04:15 | 03:04 | 10:27 | C |
| 08:00 | 03:04 | 10:27 | C |
| 08:00 | 07:23 | 11:43 | D |
| 11:43 | 07:23 | 11:43 | D |

Example 2: (using keyfield)

Same example than above, adding ProductionLine as a key field.

EventLog:

LOAD \* Inline [

Time, Event, Comment, ProductionLine

00:00, 0, Start of shift 1, P1

01:00, 0, Start of shift 1, P2

01:18, 1, Line stop, P1

02:23, 2, Line restart 50%, P1

04:15, 3, Line speed 100%, P1

08:00, 4, Start of shift 2, P1

09:00, 4, Start of shift 2, P2

11:43, 5, End of production, P1

11:43, 5, End of production, P2

];

OrderLog:

LOAD \* INLINE [

Start, End, Order, ProductionLine

01:00, 03:35, A, P1

02:30, 07:58, B, P1

03:04, 10:27, C, P1

07:23, 11:43, D, P2

];

//Link the field Time to the time intervals defined by the fields Start and End and match the values

// to the key ProductionLine.

Inner Join

IntervalMatch ( Time, ProductionLine )

LOAD Start, End, ProductionLine

Resident OrderLog;

A table box could now be created as below:

Tablebox example

| ProductionLine | Time | Event | Comment | Order | Start | End |
| --- | --- | --- | --- | --- | --- | --- |
| P1 | 00:00 | 0 | Start of shift 1 | - | - | - |
| P2 | 01:00 | 0 | Start of shift 1 | - | - | - |
| P1 | 01:18 | 1 | Line stop | A | 01:00 | 03:35 |
| P1 | 02:23 | 2 | Line restart 50% | A | 01:00 | 03:35 |
| P1 | 04:15 | 3 | Line speed 100% | B | 02:30 | 07:58 |
| P1 | 04:15 | 3 | Line speed 100% | C | 03:04 | 10:27 |
| P1 | 08:00 | 4 | Start of shift 2 | C | 03:04 | 10:27 |
| P2 | 09:00 | 4 | Start of shift 2 | D | 07:23 | 11:43 |
| P1 | 11:43 | 5 | End of production | - | - | - |
| P2 | 11:43 | 5 | End of production | D | 07:23 | 11:43 |
