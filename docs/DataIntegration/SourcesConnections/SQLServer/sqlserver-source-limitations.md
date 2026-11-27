---
title: "Limitations and considerations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/SQLServer/sqlserver-source-limitations.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "Microsoft SQL Server (log based)"]
---

# Limitations and considerations

You should be aware of the following limitations and considerations when using a Microsoft SQL Server (Log-Based) source:

## Limitations and considerations for all data tasks

- The Microsoft SQL Server Replication Publisher definitions for the database that was used in the task are not removed if you delete the task. A Microsoft SQL Server system administrator must delete these definitions from Microsoft SQL Server.
- Landing of Sparse tables is supported in "Full Load" only landing mode.
- Landing of data from indexed views is not supported.
- TRUNCATE events will not be captured.
- Landing of computed columns is supported in Full Load landing tasks only. During CDC, INSERTs to computed columns will appear as NULL on the target and UPDATEs will be ignored.
- Microsoft SQL Server partition switching is not supported.
- When using the WRITETEXT and UPDATETEXT utilities, events applied to the source database will not be captured.
- The following DML pattern is not supported:

  `select <*> into <new_table> from <existing_table>`
- Column-level encryption is not supported.
- The following limitations apply when accessing the backup transaction logs:
  - Encrypted backups are not supported.
  - Backups stored at a URL or on Windows Azure are not supported.
- Microsoft SQL Server backup to multiple disks (i.e. MIRROR TO DISK) is not supported.
- When inserting a value into SQL Server spatial data types (GEOGRAPHY and GEOMETRY), one can either ignore the SRID (Spatial Reference System Identifier) property - in which case the default SRID will be used (0 for GEOMETRY and 4326 for GEOGRAPHY), or specify a different number. When landing tables with spatial data types, the SRID that was inserted by user will be replaced with the default SRID.
- Columnstore indexes are not supported.
- Memory-optimized tables (using In-Memory OLTP) are not supported.
- Temporal tables are not supported
- Delayed durability is not supported
- Table change tracking is not supported
- Masked data will be created in the target without masking.
- OpenLDAP is not supported
- Landing directly from a secondary Microsoft SQL Server database is not supported. Consequently, the Microsoft SQL Server connector must be configured to connect to the primary database or the AlwaysOn Listener.
- Landing from databases configured to use ADR (Accelerated Database Recovery) is not supported.
- Landing a table or schema with an apostrophe (') in its name is not supported.
- Changes applied to the database using DACPAC will not be captured.
- CDC is not supported from tables which have both compressed and uncompressed partitions.
- System tables and views are not supported.

## Limitations and considerations for replication and landing tasks

- Renaming tables using `sp_rename` is not supported (e.g. `sp_rename 'Sales.SalesRegion', 'SalesReg;`)
- Renaming columns using `sp_rename` is not supported (e.g. `sp_rename 'Sales.Sales.Region', 'RegID', 'COLUMN';`)
- The following limitations apply when accessing the backup transaction logs *at file level*:

  - The backup transaction logs must reside in a shared folder with the appropriate permissions and access rights.
  - Active transaction logs are accessed through the Microsoft SQL Server API (and not at file-level).
  - The Qlik Talend Data Integration and Microsoft SQL Server machines must reside in the same domain.
  - Transparent Data Encryption (TDE) is not supported. Note that when accessing the backup transaction logs using SQL Server’s native functionality (i.e. not using file-level access), TDE encryption is supported.
  - Unix platforms are not supported.
  - Reading the backup logs from multiple stripes is not supported.
- Replicating GEOGRAPHY and GEOMETRY data types is only supported in limited LOB mode.
- If your database is not set up for MS-REPLICATION or MS-CDC, you can still capture tables that do not have a Primary Key, but bear in mind that in such a setup only INSERT/DELETE DML events will be captured. UPDATE events will be ignored.
- Capturing DDL and DML statements within a single transaction is not supported.
- UPDATEs to a Primary Key/Unique Index that affect multiple rows may cause conflicts
  when applying the changes to the target. This may occur, for example, if the UPDATEs
  are applied to the target as INSERT/DELETE operations rather than a single UPDATE
  operation. In such a scenario (where UPDATEs to a Primary Key/Unique Index affect
  multiple rows), working in Batch optimized apply Change Processing mode is not
  supported as it may result in the table being ignored. Working in Transactional
  Apply Change Processing mode however, may result in constraint violations.

  If this
  happens, you either need to reload the relevant table or locate the problematic
  records in the [*Apply exceptions*](../../Replicating/apply_exceptions.htm#ar_control_tables_553656663_1108409) Control Table and edit them manually in the
  target database.See also: [*Change processing tuning*](../../Replicating/replicating-settings-cptuning.htm).

## Unsupported Microsoft SQL Server security features

Tables that use the following Microsoft SQL Server security features are not supported:

- Always Encrypted
- Row-Level Security

## Unsupported data types

The following data types are not supported:

- CURSOR
- SQL\_VARIANT
- TABLE

Information note

User-defined data types are supported according to their base-type. For example a user-defined data type based on DATETIME is handled as a DATETIME data type.
