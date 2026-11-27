---
title: "Matching intervals to discrete data"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/matching-intervals-to-discrete-data.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Modeling your data", "Best practices for data modeling"]
---

# Matching intervals to discrete data

The intervalmatch prefix to a LOAD or SELECT statement is used to link discrete numeric values to one or more numeric intervals. This is a very powerful feature which can be used, for example, in production environments.

## Intervalmatch example

Look at the two tables below. The first table shows the start and end of production of different orders. The second table shows some discrete events. How can we associate the discrete events with the orders, so that we know, for example, which orders were affected by the disturbances and which orders were processed by which shifts?

Table OrderLog

| Start | End | Order |
| --- | --- | --- |
| 01:00 | 03:35 | A |
| 02:30 | 07:58 | B |
| 03:04 | 10:27 | C |
| 07:23 | 11:43 | D |

Table EventLog

| Time | Event | Comment |
| --- | --- | --- |
| 00:00 | 0 | Start of shift 1 |
| 01:18 | 1 | Line stop |
| 02:23 | 2 | Line restart 50% |
| 04:15 | 3 | Line speed 100% |
| 08:00 | 4 | Start of shift 2 |
| 11:43 | 5 | End of production |

First, load the two tables as usual and then link the field Time to the intervals defined by the fields Start and End:

SELECT \* from OrderLog;

SELECT \* from EventLog;

Intervalmatch (Time) SELECT Start,End from OrderLog;

You can now create a table in Qlik Sense as below:

Table with Time field linked to the intervals defined by the Start and End

| Time | Event | Comment | Order | Start | End |
| --- | --- | --- | --- | --- | --- |
| 0:00 | 0 | Start of shift 1 | - | - | - |
| 1:18 | 1 | Line stop | A | 1:00 | 3:35 |
| 2:23 | 2 | Line restart 50% | A | 1:00 | 3:35 |
| 4:15 | 3 | Line speed 100% | B | 2:30 | 7:58 |
| 4:15 | 3 | Line speed 100% | C | 3:04 | 10:.... |
| 8:00 | 4 | Start of shift 2 | C | 3:04 | 10:.... |
| 8:00 | 4 | Start of shift 2 | D | 7:23 | 11:.... |
| 11:43 | 5 | End of production | E | 7:23 | 11:..... |

We can now easily see that mainly order A was affected by the line stop but that the reduced line speed affected also orders B and C. Only the orders C and D were partly handled by Shift 2.

Note the following points when using intervalmatch:

- Before the intervalmatch statement, the field containing the discrete data points (Time in the example above) must already have been read into Qlik Sense. The intervalmatch statement does not read this field from the database table.
- The table read in the intervalmatch LOAD or SELECT statement must always contain exactly two fields (Start and End in the example above). In order to establish a link to other fields you must read the interval fields together with additional fields in a separate LOAD or SELECT statement (the first SELECT statement in the example above).
- The intervals are always closed. That is, the end points are included in the interval. Non-numeric limits render the interval to be disregarded (undefined)
  while NULL limits extend the interval indefinitely (unlimited).
- The intervals may be overlapping and the discrete values will be linked to all matching intervals.

## Using the extended intervalmatch syntax to resolve slowly changing dimension problems

The extended intervalmatch syntax can be used for handling of the well-known problem of slowly changing dimensions in source data.

### Sample script:

SET NullInterpret='';

IntervalTable:

LOAD
Key,
ValidFrom,
Team

FROM 'lib://dataqv/intervalmatch.xlsx'
(ooxml, embedded labels, table is IntervalTable);

Key:

LOAD

Key,

ValidFrom as FirstDate,

date(if(Key=previous(Key),

previous(ValidFrom) - 1)) as LastDate,

Team

RESIDENT IntervalTable order by Key, ValidFrom desc;

drop table IntervalTable;

Transact:

LOAD Key, Name, Date, Sales

FROM 'lib://dataqv/intervalmatch.xlsx' (ooxml, embedded labels, table is Transact);

INNER JOIN intervalmatch (Date,Key) LOAD FirstDate, LastDate, Key RESIDENT Key;

The nullinterpret statement is only required when reading data from a table file since missing values are defined as empty strings instead of NULL values.

Loading the data from IntervalTable would result in the following table:

Table with data loaded from IntervalTable

| Key | FirstDate | Team |
| --- | --- | --- |
| 000110 | 2011-01-21 | Southwest |
| 000110 | - | Northwest |
| 000120 | - | Northwest |
| 000120 | 2013-03-05 | Southwest |
| 000120 | 2013-03-05 | Northwest |
| 000120 | 2013-03-05 | Southwest |

The nullasvalue statement allows NULL values to map to the listed fields.

Create Key, FirstDate, LastDate, (attribute fields) by using previous and order by and thereafter the IntervalTable is dropped having been replaced by this key table.

Loading the data from Transact would result in the following table:

Table with data loaded from Transact

| Key | Name | Date | Sales |
| --- | --- | --- | --- |
| 000110 | Spengler Aaron | 2009-08-18 | 100 |
| 000110 | Spengler Aaron | 2009-12-25 | 200 |
| 000110 | Spengler Aaron | 2011-02-03 | 300 |
| 000110 | Spengler Aaron | 2011-05-05 | 400 |
| 000120 | Ballard John | 2011-06-04 | 500 |
| 000120 | Ballard John | 2013-01-20 | 600 |
| 000120 | Ballard John | 2013-03-10 | 700 |
| 000120 | Ballard John | 2013-03-13 | 800 |
| 000120 | Ballard John | 2013-09-21 | 900 |

The intervalmatch statement preceded by the inner join replaces the key above with a synthetic key that connects to the Transact table resulting in the following table:

Table with the intervalmatch statement preceded by the inner join

| Key | Team | Name | FirstDate | LastDate | Date | Sales |
| --- | --- | --- | --- | --- | --- | --- |
| 000110 | Northwest | Spengler Aaron | - | 2011-01-20 | 2009-08-18 | 100 |
| 000110 | Northwest | Spengler Aaron | - | 2011-01-20 | 2009-12-25 | 200 |
| 000110 | Southwest | Spengler Aaron | 2011-01-21 |  | 2011-02-03 | 300 |
| 000110 | Southwest | Spengler Aaron | 2011-01-21 |  | 2011-05-05 | 400 |
| 000120 | Northwest | Ballard John |  | 2013-01-05 | 2011-06-04 | 500 |
| 000120 | Southwest | Ballard John | 2013-01-06 | 2013-03-04 | 2013-01-20 | 600 |
| 000120 | Southwest | Ballard John | 2013-03-05 |  | 2013-03-10 | 700 |
| 000120 | Southwest | Ballard John | 2013-03-05 |  | 2013-03-13 | 800 |
| 000120 | Southwest | Ballard John | 2013-03-05 |  | 2013-09-21 | 900 |
