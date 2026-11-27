---
title: "Limitations and considerations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/AzureSQLMSCDC/azuremscdc-source-limitations.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "Microsoft SQL Server (Microsoft CDC based)"]
---

# Limitations and considerations

You should be aware of the following limitations and considerations when using a Microsoft SQL Server (Microsoft CDC based) source:

## Limitations and considerations for all data tasks

- A Secondary Microsoft Azure SQL Managed Instance is not supported as a source database.
- Moving data from indexed views is not supported.
- When replicating a subset of columns, Data Movement gateway uses the @captured\_column\_list parameter to enable CDC only on the included columns. You can set the parameter manually before starting the task. Column names listed with the parameter cannot exceed 127 characters.
- Limitations due to the requirement to have MS-CDC enabled on all source tables include:
  - Truncate table is not supported
  - WRITETEXT and UPDATETEXT utilities are not supported

  For more information on MS-CDC limitations, see the Microsoft Help.
- When running without the db\_owner role, the following limitations apply:

  - Capture of DDLs is not supported. To prevent moving errors, you must clear the Capture DDL events check box in connection settings before running the task.
  - MS-CDC cannot be enabled automatically and should therefore be enabled manually. To prevent moving errors, you must clear the Enable MS-CDC on all captured tables check box in the connection settings before running the task.

  Information noteSpecial permissions are required for running without the db\_owner role. For more information, see [*Required permissions*](../../../../Global_Common/Content/SharedReplicateHDD/Azure-MSCDC-Source/azremscdc-SQLServerDBSource-security.htm).
- Moving of computed columns is supported in Full Load moving tasks only. During CDC, INSERTs to computed columns will appear as NULL on the target and UPDATEs will be ignored.
- Partition switching is not supported.
- The following DML pattern is not supported:

  select <\*> into <new\_table> from <existing\_table>
- Column-level encryption is not supported. Such tables will be written to the target without the encrypted columns.
- ADD COLUMN DDL is not supported. When an ADD COLUMN DDL is performed, the table will be replicated to the target without the newly added column(s) and a warning will be presented.
- When inserting a value into Microsoft Azure SQL Managed Instance spatial data types (GEOGRAPHY and GEOMETRY), one can either ignore the SRID (Spatial Reference System Identifier) property - in which case the default SRID will be used (0 for GEOMETRY and 4326 for GEOGRAPHY) - or specify a different number. When moving tables with spatial data types, Data Movement gateway replaces the SRID that was inserted by user with the default SRID.
- Columnstore indexes are not supported.
- Memory-optimized tables (using In-Memory OLTP) are not supported.
- Temporal databases are not supported
- Delayed durability is not supported
- Due to an ODBC limitation, no more than 16 columns can be part of a Primary Key.
- Masked data will be created in the target without masking.
- OpenLDAP is not supported
- Moving from databases configured to use ADR (Accelerated Database Recovery) is not supported.
- Moving a table or schema with an apostrophe (') in its name is not supported.
- Changes applied to the database using DACPAC will not be captured.
- MS-CDC Change Tables with fixed size columns (including NCHAR and CHAR data), the sum of which exceeds 8060 bytes, are not supported.
- System tables and views are not supported.

## Limitations and considerations for replication and landing tasks

- Due to the requirement to have MS-CDC enabled on all source tables, renamed columns will not be captured during CDC.

  For more information on MS-CDC limitations, see the Microsoft Help.
- Limitations when capturing DDL operations are as follows:

  - RENAME TABLE will not be captured. When a RENAME TABLE DDL is encountered, the task will continue capturing the changes without renaming the target table. If the task is stopped and resumed or if there is a recoverable error, the table will be suspended to allow the CT table to be manually aligned.
  - ADD COLUMN DDL is not supported. When an ADD COLUMN DDL is performed, the table will be replicated to the target without the newly added column(s) and a warning will be presented.
- When running without the db\_owner role, capture of DDLs is not supported.

  Information noteSpecial permissions are required for running without the db\_owner role. For more information, see [*Running without the db\_owner role*](../../../../Global_Common/Content/SharedReplicateHDD/Azure-MSCDC-Source/azremscdc-SQLServerDBSource-security.htm#Running).
- When running without the db\_owner role, MS-CDC cannot be enabled automatically and should therefore be enabled manually. To prevent moving errors, you must also clear the Enable MS-CDC on all captured tables check box in the connection properties before running the task.
- Capturing DDL and DML statements within a single transaction is not supported.

## Non-supported security features

Tables that use the following security features are not supported:

- Always Encrypted
- Row-Level Security

## Unsupported data types

The following data types are not supported:

- CURSOR
- SQL\_VARIANT
- TABLE

Information note

User-defined data types are supported according to their base-type. For example a user-defined data type based on DATETIME is handled as a DATETIME data type.
