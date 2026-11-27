---
title: "Limitations and considerations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/Content/SharedReplicateHDD/SAP-Application-DB/native_Limitations_SAP_app.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SAP sources", "SAP (Application)"]
---

# Limitations and considerations

When using SAP (Application) as a source connector in a Qlik Talend Data Integration task, the following limitations apply.

## Limitations and considerations for all data tasks

- When using the HR module as a source, only transparent tables are supported.
- The STXL table is not supported.
- As the SAP HANA endpoint can be configured to connect to one instance only, in the event of failover in a HA environment, the endpoint must be manually reconfigured to point to the new instance. Then reload all associated tasks.
- Cluster tables are not supported when SAP uses an Oracle backend database, and the VARDATA column is defined as LONG RAW.
- Moving data with 4-byte emoji characters is not supported.

## Limitations and considerations for replication and landing tasks

- The DROP TABLE DDL is not supported. In order to stop capturing a captured table, you need to stop the task, remove the table from the task table list (or exclude it if it is defined as a pattern), and then resume the task. When you remove the table from the task table list, you also have the option to remove it from the corresponding Business Group.
- The CREATE TABLE DDL is not supported. When you add a new table to a Business group during a task run, and the table name corresponds to the task table list definition, the table replication will not start automatically. To ensure that the table is replicated, you need to stop the task and then resume it.

For information about limitations according to backend database type, see [*Set up a source connector for SAP (Application)*](native_Set_up_a_Source_Endpoint_for_your_SAP_Application.htm).
