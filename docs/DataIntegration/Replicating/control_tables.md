---
title: "Control tables"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Replicating/control_tables.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Monitoring and operating your data tasks"]
---

# Control tables

Control tables store metadata and configuration information that can be used for auditing purposes, or leveraged for downstream processing. For example, the attrep\_cdc\_partitions control table contains records of partitions created on the target platform. These records can be used to identify partitioned data that requires further processing.

Control tables are supported in both Data pipeline and Replication use cases. This topic describes the control tables that are created on the target platform any of the control tables is selected in the task settings.

Information note

- All control table timestamps are in UTC format.

- Control tables are not created in Full Load only replication tasks.

- Setting the replication task to DROP and CREATE the table if the target table already exists does not apply to control tables.

- The data task automatically creates the control tables on the target during runtime. If you prefer to manually create the tables, make sure that all column names and table names are lower case, apart from the Apply Exceptions table (`attrep_apply_exceptions`), which should be upper case.

The available control tables are as follows:

- [*Apply exceptions*](apply_exceptions.htm)
- [*Replication status*](replication_status.htm)
- [*Suspended Tables*](suspended_tables.htm)
- [*Replication history*](replication_history.htm)
- [*Change data partitions*](CDC_Partition.htm)
- [*DDL history*](ddl_history.htm)
