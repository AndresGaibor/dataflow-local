---
title: "Replication history"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Replicating/replication_history.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Monitoring and operating your data tasks", "Control tables"]
---

# Replication history

The `attrep_history` table provides statistics about each task, such as the number and volume of records processed during a particular timeslot.

A new record is appended to the table at the end of each [*TIMESLOT\_DURATION*](#TIMESLOT). In other words, the data in this table is never deleted.

Column descriptions

| Column | Type | Description |
| --- | --- | --- |
| SERVER\_NAME | nvchar | The name of the machine on which the Qlik replication server is installed. |
| TASK\_NAME | nvchar | The name of the data task. |
| TIMESLOT\_TYPE | varchar | One of the following:   - FULL LOAD - CHANGE PROCESSING (CDC)   When FULL LOAD and CHANGE PROCESSING are running in parallel (some tables in full load, some in CDC), two history records will occupy the same time slot. |
| TIMESLOT | timestamp | The end timestamp of the time slot. |
| TIMESLOT\_DURATION | int | The duration of each history record in minutes. |
| TIMESLOT\_LATENCY | int | The latency at the end of the time slot in seconds. This is only applicable to CDC time slots. Note that this value contains the value of the *target* latency only. |
| TIMESLOT\_RECORDS | int | The number of records processed during the time slot. |
| TIMESLOT\_VOLUME | int | The volume of data processed in MB. |
