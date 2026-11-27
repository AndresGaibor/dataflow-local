---
title: "Date and time functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/date-and-time/date-and-time.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions"]
---

# Date and time functions

Date and time functions perform operations on date and time values to calculate, extract, or format temporal information and return a result.

The following functions are available in Qlik Open Lakehouse:

| Function | Description |
| --- | --- |
| [ADD\_TIME\_ZONE\_OFFSET](add_time_zone_offset.htm) | Add a timezone offset to a date. The timezone offset can be in any of the standard formats accepted by Java's ZoneId.of method (America/New\_York, +0200, etc.) |
| [DATE](date.htm) | Casts string to date |
| [DATE\_ADD](date_add.htm) | Adds an interval value of type unit to timestamp. Subtraction can be performed by using a negative value |
| [DATE\_DIFF](date_diff.htm) | Returns timestamp2 - timestamp1 expressed in terms of unit |
| [DATE\_TRUNC](date_trunc.htm) | Truncate a date to a given unit |
| [DAY](day.htm) | Returns the day of the month from the timestamp |
| [DAY\_OF\_WEEK](day_of_week.htm) | Returns the ISO day of the week from the timestamp. values range from 1 (Monday) to 7 (Sunday) |
| [DAY\_OF\_YEAR](day_of_year.htm) | Returns the day of the year from timestamp. values range from 1 to 366 |
| [EXTRACT\_TIMESTAMP](extract_timestamp.htm) | Convert a date or timestamp string to a date or timestamp, autodetecting the date format |
| [FORMAT\_DATETIME](format_datetime.htm) | Convert a datetime into a string |
| [FROM\_ISO8601\_DATE](from_iso8601_date.htm) | Parses the ISO 8601 formatted string into a date |
| [FROM\_UNIXTIME](from_unixtime.htm) | Convert epoch seconds to a timestamp |
| [HOUR](hour.htm) | Returns the hour of the day from a timestamp. Values range from 0 to 23 |
| [MILLISECOND](millisecond.htm) | Returns the millisecond of the second from the timestamp |
| [MINUTE](minute.htm) | Returns the minute of the hour from the timestamp |
| [MONTH](month.htm) | Returns the month of the year from the timestamp |
| [QUARTER](quarter.htm) | Returns the quarter of the year from the timestamp. Values range from 1 to 4 |
| [RUN\_END\_TIME](run_end_time.htm) | Returns the job execution end time |
| [RUN\_START\_TIME](run_start_time.htm) | Returns the job execution start time |
| [SECOND](second.htm) | Returns the second of the minute from the timestamp |
| [SUBTRACT\_TIME\_ZONE\_OFFSET](subtract_time_zone_offset.htm) | Subtract a timezone offset from a date. The timezone offset can be in any of the standard formats accepted by Java's `ZoneId.of` method (America/New\_York, +0200, etc) |
| [TO\_UNIXTIME](to_unixtime.htm) | Convert a date to its Epoch (Unix) seconds representation, with fractional milliseconds |
| [TO\_UNIX\_EPOCH\_MILLIS](to_unix_epoch_millis.htm) | Convert a date to its Epoch (Unix) seconds representation |
| [TO\_UNIX\_EPOCH\_SECONDS](to_unix_epoch_seconds.htm) | Convert a date to its Epoch (Unix) seconds representation |
| [WEEK](week.htm) | Returns the ISO week of the year from the timestamp. Values range from 1 to 53 |
| [YEAR](year.htm) | Returns the year from the timestamp |
| [YEAR\_OF\_WEEK](year_of_week.htm) | Returns the year of ISO week from the timestamp |
