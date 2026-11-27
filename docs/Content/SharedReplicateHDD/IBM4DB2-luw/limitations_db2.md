---
title: "Limitations and considerations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/Content/SharedReplicateHDD/IBM4DB2-luw/limitations_db2.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "IBM DB2 for LUW"]
---

# Limitations and considerations

When using IBM DB2 for LUW as a data source, the following limitations currently apply.

## Limitations and considerations for all data tasks

- Clustered database is not supported

  Information note

  Users can define a separate IBM DB2 for LUW database for each of the connectors in the cluster.
- Changes to DECFLOAT columns will be ignored during CDC.
- The RENAME COLUMN statement is not supported.
- When performing updates on MDC (Multi-Dimensional Clustering) tables, each update is shown in the task monitor as INSERT + DELETE.
- Variable-length string columns with data that is stored out-of-row will be ignored.
  Note that this limitation is only applicable to tables created with extended row size.
- If you need to replicate 4-byte emoji characters, use a transformation to convert the data type from STRING(n ) to WSTRING ( n\*2 ).
- Read-enabled HADR standby databases are not supported.

## Limitations and considerations for landing tasks

- When the Include LOB columns landing task setting is disabled, any table that has LOB columns will be suspended during change processing.

## Limitations and considerations for replication and landing tasks

- When truncating a table with multiple partitions, the number of DDL events displayed in the Qlik Talend Data Integration console will be equal to the number of partitions. This is because IBM DB2 for LUW records a separate DDL for each partition.
- The following DDLs on partitioned tables are not supported:

  - ALTER TABLE ADD PARTITION
  - ALTER TABLE DETACH PARTITION
  - ALTER TABLE ATTACH PARTITION
- When the Do not replicate LOB columns task setting is enabled, any table that has LOB columns will be suspended during change processing.
- When the Audit table option is enabled in the Store Changes Settings tab, the first timestamp record in the audit table will be NULL.
- When the Change table option is enabled in the Store Changes Settings tab, the first timestamp record in the table may be Zero in some cases (i.e. 1970-01-01 00:00:00.000000).
- When capturing changes to source tables, a RENAME TABLE operation will be captured only if it is preceded by a DML operation.
