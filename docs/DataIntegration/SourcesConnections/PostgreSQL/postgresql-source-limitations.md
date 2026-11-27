---
title: "Limitations and considerations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/PostgreSQL/postgresql-source-limitations.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "PostgreSQL"]
---

# Limitations and considerations

You should be aware of the following limitations and considerations when using a PostgreSQL source:

## Limitations and considerations for all data tasks

- The database name cannot include a semi-colon (;).
- Capturing changes while the database is in Hot Standby mode is not supported.
- Moving of multiple tables with the same name but a different case (e.g. table1, TABLE1 and Table1) may cause unpredictable behavior and is therefore not supported.
- The PostgreSQL read replica (in a High Availability environment) is supported from PostgreSQL 16 only.
- Change processing of TRUNCATE operations is not supported.
- Deferred Constraints are not supported.
- Unique Indexes with CASE expressions are not supported.

## Limitations and considerations for landing tasks only

- Partitioned tables are not supported.
- Forced failover is a feature of Azure Database for PostgreSQL – Flexible Server. If forced failover occurs when moving data from Azure Database for PostgreSQL – Flexible Server, the task will stop and the datasets will need to be recreated.

## Limitations and considerations for replication and landing tasks

- REPLICA IDENTITY support:

  - If FULL is used, before-image values will be replicated for all table columns. Only when using this mode is it possible to redefine the target index.
  - If DEFAULT is used, replication is supported only when a table contains a Primary key. Additionally, only Primary Key columns of the before-image will be replicated.
  - USING INDEX is supported only when the specified Unique Index is the only unique constraint for the table (meaning that the table does not have a Primary Key or another Unique Index). In this case, it is supported exactly the same as the DEFAULT value described above.
  - As Qlik Talend Data Integration does not verify the REPLICA IDENTITY value, make sure you define the correct value.
- The “Start Process Changes from Timestamp” run option is not supported.
- Change processing of [CREATE | ALTER | DROP] table DDLs are supported unless they are held in an inner function/procedure body block or in other nested constructs.

  For example, the following change will not be captured:

  CREATE OR REPLACE FUNCTION attu.create\_distributors1() RETURNS void

  LANGUAGE plpgsql

  AS $$

  BEGIN

  create table attu.distributors1(did serial PRIMARY KEY,name varchar(40) NOT NULL);

  END;

  $$;
- An UPDATE operation that involves two partitions (moving a record between partitions) will be replicated to the target table using DELETE and INSERT operations. If the Store Changes replication mode is enabled, the UPDATE will appear as separate INSERT and DELETE operations in the corresponding Change Table.
- When using the [Parallel Load](../../Replicating/Table-settings-replication.htm) feature, table segmentation according to partitions or sub-partitions is not supported.
- When capturing changes to source tables, a RENAME TABLE operation will be captured only if it is preceded by a DML operation.
- PostGIS data types are not supported.
- Forced failover is a feature of Azure Database for PostgreSQL – Flexible Server. If forced failover occurs when moving data from Azure Database for PostgreSQL – Flexible Server, the task will stop and will need to be reloaded.
- The SQL MERGE command introduced in PostgreSQL 15.x has not been certified.

## Unsupported data types

The following data types are not supported:

- PostGIS
- INT4MULTIRANGE
- INT8MULTIRANGE
- NUMMULTIRANGE
- TSMULTIRANGE
