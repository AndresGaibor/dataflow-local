---
title: "Limitations and considerations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/Content/SharedReplicateHDD/Oracle/OracleDB_source_limitations.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "Oracle"]
---

# Limitations and considerations

You should be aware of the following limitations and considerations when using an Oracle source.

## Limitations and considerations for all data tasks

- When moving from a CHAR column, any trailing spaces will be truncated.
- Function-based indexes are not supported.
- If you are managing supplemental logging and you carry out transformations on any of the columns, you must be sure that supplemental logging is activated for all fields and columns.
- Capturing changes from a pluggable Oracle database (PDB) requires the source endpoint to connect to that PDB instance. Capturing changes from multiple PDB instances by connecting to the container database (CDB) is not supported.
- Deferred Constraints are not supported.
- Changes made by the Oracle DBMS\_REDEFINITION package -( e.g. table metadata and the OBJECT\_ID) - will not be captured by the data task.
- During Change Processing, columns without supplemental logging (e.g. LOB columns) that are not updated will be inserted as NULL in the Change Table.
- During Change Processing, batch updates to numeric columns defined as a Primary Key are not supported.

  Example of an unsupported UPDATE command:

  UPDATE tableX set ID=ID+1;

  Where tableX is the table name and ID is a numeric column defined as a Primary Key.
- Data in LONG and LONG RAW columns cannot exceed 64k. Any data that exceeds 64k will be truncated.
- Tables whose names contain apostrophes cannot be supported.
- Change Data Capture (CDC) is not supported from dynamic views.
- Index-organized tables with an overflow segment are not supported in Change Processing (CDC) tasks.
- Changes to Index-organized tables with key compression are not supported.
- Moving of tables or views of type BIN$ or DR$ is not supported.
- Oracle Flashback Database and restore points are not supported as the related operations affect the consistency of Oracle redo log files.
- When using the escape character '\' to search for a table in the Select Tables window, you need to write '\\' (2 backslashes) instead of '\' (1 backslash). For example, to search for all tables that include '\_', you would need to enter %\\\_%.

Information note

- When adding a pattern for include or exclude, 2 backslashes are not required (for example, \*%\\_%).
- When using '$’ for the escape character, there is no limitation.

- When using Oracle 19.0 as the source, the following Oracle features are not supported:
  - Data-guard DML redirect
  - Schema-only Oracle accounts

- When moving from Oracle 21c, the following limitations apply:

  - Immutable tables are not supported
  - Blockchain tables are not supported

- CDC is not supported if the schema name, table name, or any column name exceeds 30 characters.
- Cascading standby database is not supported.
- Failover configuration is supported only when changes are captured from the primary node.
- RESETLOGS functionality is not supported by default. If RESETLOGS is used in your Oracle instance, contact [Qlik Support](https://community.qlik.com/t5/Support/ct-p/qlikSupport).
- Moving data from an Oracle Autonomous Data Warehouse is not supported.

## Limitations and considerations for replication and landing tasks

- The rename table <table name> to <new table name> syntax is supported by Qlik Talend Data Integration when using Oracle version 11 and higher.
- Data changes resulting from partition/sub-partition operations (ADD, DROP, EXCHANGE and TRUNCATE) will not be moved and may cause the following errors:
  - For ADD operations, updates and deletes on the added data may return a "0 rows affected" warning.
  - For DROP and TRUNCATE operations, new inserts may result in "duplicates" errors.
  - For EXCHANGE operations, both a "0 rows affected" warning and "duplicates" errors may be encountered.

  To Move changes resulting from partition/sub-partition operations, you need to reload the tables in question.
  When adding a new *empty* partition, operations on the newly added partition will be moved to the target as normal.
- When Replicate limited LOB columns (KB) is enabled, empty BLOB/CLOB columns on the Oracle source are moved as NULL values. For more information on Limited-size LOB mode, see [*Metadata*](../../../../Sense_Hub/DataIntegration/Replicating/replicating-settings-metadata.htm).
- The Allow unlimited LOB size option is not supported when loading LONG and LONG RAW columns into Oracle target.

  Workaround: Use the [Replicate limited LOB columns (KB)](../../../../Sense_Hub/DataIntegration/Replicating/replicating-settings-metadata.htm) option instead.

- Table clusters are not supported.
- Only table-level SHRINK SPACE operations are supported. These include the full table, partitions, and sub-partitions.
- Implementing online redo logs on raw devices is not supported.
- The following Oracle features are not supported when using Amazon RDS for Oracle:
  - ASM
  - TDE
- Direct-load INSERT procedure with the parallel execution option is not supported in the following cases:

  - Uncompressed tables with more than 255 columns
  - Row size exceeds 8K
  - Exadata HCC tables

## Limitations and considerations for Oracle Supplemental Logging

Qlik Talend Data Integration CDC functionality for Oracle relies on information Oracle writes to the Oracle redo logs. In the past, users could control what is written to the Oracle redo log by setting full supplemental logging. However, in recent years and in very specific scenarios, Oracle has started excluding certain metadata/data from the redo log that is not strictly needed for recovery. As noted earlier, data that is not in the Oracle redo logs will not be available to Qlik Talend Data Integration either. The only way to make this data available is to set the ENABLE\_GOLDENGATE\_REPLICATION=TRUE parameter in the Oracle database.

However, enabling the Golden Gate replication parameter has licensing implications, which are the sole responsibility of the customer according to their specific contracts with Oracle.

Some Qlik Talend Data Integration customers have negotiated for a license to use this parameter as part of a Unlimited License Agreement (ULA), or an Enterprise Agreement (EA), or via a Restricted Use Clause (typically associated with the use of the XStream feature). Qlik is not a party to these agreements.

When the ENABLE\_GOLDENGATE\_REPLICATION parameter is not enabled, the following known limitations apply:

- Full supplemental logging is not available for tables with column names longer than 30 characters.
- Changes to columns of type JSON, XMLType, UDTs and other complex types are either not extractable from the log, or the entire table cannot be enabled for full supplemental logging.
- Moving from Application Containers is not supported.
- Additional limitations might be unilaterally introduced by Oracle, especially for new functionality added with new database versions.

Information note

When the ENABLE\_GOLDENGATE\_REPLICATION parameter is enabled in the Oracle database, the following text will appear in the replication task log:

XStream is enabled in the Oracle source database.

## Unsupported data types

The following data types are not supported:

- BFILE
- ROWID
- REF
- UROWID
- ANYDATA
- SDO\_GEOMETRY
- User-defined data types

Information note

- Virtual columns are not supported.
- As the ROWID data type is not supported, materialized views based on a ROWID column are also not supported.
