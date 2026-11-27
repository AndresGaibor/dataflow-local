---
title: "Change data partitions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Replicating/CDC_Partition.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Monitoring and operating your data tasks", "Control tables"]
---

# Change data partitions

This Control table is supported in the following cases:

- When the landing task in your data pipeline uses an Amazon S3 (for Qlik Cloud) target
- All tasks replicating to cloud storage

The attrep\_cdc\_partitions table contains records of partitions created on the target database. You can use this information to identify partitioned data that needs to be further processed.

attrep\_cdc\_partitions table fields

| Column | Type | Description |
| --- | --- | --- |
| SERVER\_NAME | STRING | The name of the machine on which the Qlik replication server is installed. |
| TASK\_NAME | STRING | The name of the data task. |
| PARTITION\_NAME | STRING | The partition name consists of the partition start and end time.  Example:  20170313T123000\_20170313T170000 |
| PARTITION\_START\_TIME | TIMESTAMP | When the partition was opened:  Example:  2017-03-13 12:30:00.000 |
| PARTITION\_END\_TIME | TIMESTAMP | When the partition was closed:  Example:  2017-03-13 17:00:00.000 |
| TABLE\_OWNER | STRING | The table schema or owner. |
| TABLE\_NAME | STRING | The table name. |
