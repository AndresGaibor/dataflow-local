---
title: "Replication  status"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Replicating/replication_status.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Monitoring and operating your data tasks", "Control tables"]
---

# Replication status

The `attrep_status` table contains the current status of each replication task and the target data. Although updates for the tasks in the `attrep_status` table are generated every few seconds, The attrep\_status table will only be updated *after* it has applied changes to the target tables. In some cases, this may take a few minutes.

Replication status

| Column | Type | Description |
| --- | --- | --- |
| SERVER\_NAME | nvchar | The name of the machine on which the Qlik replication server is installed. |
| TASK\_NAME | nvchar | The name of the Qlik data task. |
| TASK\_STATUS | varchar | One of the following:   - FULL LOAD - CHANGE PROCESSING   Task status is FULL LOAD as long as there is at least one table in full load. After all tables have been loaded, the task status changes to CHANGE PROCESSING. |
| STATUS\_TIME | timestamp | When the status was last updated. |
| PENDING\_CHANGES | int | The number of change records that were not yet applied to the target. |
| DISK\_SWAP\_SIZE | int | The amount of disk space that is occupied by old or offloaded transactions. |
| TASK\_MEMORY | int | Current memory consumption in MB. |
| SOURCE\_CURRENT\_POSITION | varchar | The POSITION in the source endpoint that the Qlik replication server is currently reading from. |
| SOURCE\_CURRENT\_TIMESTAMP | timestamp | The TIMESTAMP in the source from which the Qlik replication server is currently reading.  Information note The Qlik replication server aligns the timestamp read from the data source with the timestamp on the Qlik replication server machine (according to the source latency). So, for example, if the time on the source was 12:30 and the time on the Qlik replication server is 12:32, an extra two minutes will be added to the original source time. This will be the value in the SOURCE\_CURRENT\_TIMESTAMP column. |
| SOURCE\_TAIL\_POSITION | varchar | The POSITION of the oldest start transaction that is still not committed. This represents the newest position that you can revert to, without losing any changes. There may, of course, be duplicates. |
| SOURCE\_TAIL\_TIMESTAMP | timestamp | The TIMESTAMP of the oldest start transaction that is still not committed. This represents the newest TIMESTAMP that you can revert to, without losing any changes. There may, of course, be duplicates. |
| SOURCE\_TIMESTAMP\_APPLIED | timestamp | This is the timestamp of the last transaction committed. In a bulk apply this will be the timestamp for the commit of the last transaction in that batch. It will only be changed as part of the last transaction in the batch. |
