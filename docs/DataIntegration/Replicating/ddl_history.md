---
title: "DDL history"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Replicating/ddl_history.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Monitoring and operating your data tasks", "Control tables"]
---

# DDL history

The attrep\_ddl\_history table contains a history of DDL changes that occurred during CDC.

The DDL History table is supported with the following target platforms only:

- Databricks
- Microsoft Fabric
- Amazon Redshift
- If you are using Data Movement gateway, the following targets need version 2024.11.14 or later:
  - Amazon S3
  - Google Cloud Storage
  - Snowflake
- Kafka - If you are using Data Movement gateway, version 2025.5.42 or later is required.
- If you are using Data Movement gateway, the following targets need version 2025.11.1 or later:
  - Google BigQuery
  - Google Cloud Alloy DB for PostgreSQL
    (via the PostgreSQL connector)
  - Google Cloud SQL for PostgreSQL
    (via the PostgreSQL connector)
  - Microsoft Azure Database for PostgreSQL
    (via the PostgreSQL connector)
  - PostgreSQL

A new record is inserted into the table whenever a supported DDL change occurs in the source. Multiple ALTER TABLE statements that occur during a task may be represented as a single row in the control table. The
JSON buffer (see below) describes all the changes that occurred (e.g. ADD COLUMN A, DROP COLUMN B, ALTER COLUMN C).

For information on enabling the DDL History Control Tables, see [*Control tables*](../Landing/Landing-settings.htm#Control).

Column descriptions

| Column | Type | Description |
| --- | --- | --- |
| SERVER\_NAME | STRING | The name of the machine on which the Qlik replication server is installed. |
| TASK\_NAME | STRING | The name of the data task. |
| TABLE\_OWNER | STRING | The source table schema or owner. |
| TABLE\_NAME | STRING | The source table name. If the table was renamed, this will be the table name before the change. |
| CHANGE\_SEQ | STRING | See Change\_Seq in [*Using Change Tables*](use_change_tables.htm). |
| TIMESTAMP | TIMESTAMP | When the change occurred. |
| TABLE\_VERSION | INTEGER | An internal version number is assigned to the table. The version number increases whenever a DDL change occurs in the source table. |
| DDL\_TYPE | STRING | CREATE\_TABLE, DROP\_TABLE, ALTER\_TABLE, TRUNCATE\_TABLE |
| DETAILS | CLOB | JSON document describing the change(s)  Example:  ``` { 	"owner": "string", 	"table": "string", 	"tableNewName": "string",    	"version": number, 	"columns": 	{ 		"col1":            		{ 			"columnNewName": "string",   			"action": "string",             			"type":" string",                			"length": number, 			"precision": number, 			"scale": number, 			"primaryKeyPosition": number,     			"nullable": boolean,  			"ordinal": number  		}, 		"col2": 		{ 			… 		} 	} } ```  where:   - `tableNewName` is NULL if the table was not renamed - `col1` and `col2` are the original column names (or the *only* column names if the columns were not renamed) - `columnNewName` is the new column name or NULL if the column was not renamed - `action` is ADD (also for CREATE TABLE), DROP, or ALTER - `type` is the Qlik Cloud data type - `primaryKeyPosition` is ZERO if the column is not part of the primary key |
