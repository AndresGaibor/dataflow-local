---
title: "Limitations and considerations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/MySQL/limitations-mysql-source.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "MySQL"]
---

# Limitations and considerations

You should be aware of the following limitations and considerations when using a MySQL source.

## Limitations and considerations for all data tasks

- When MySQL is installed on Windows, changes are not captured from tables whose names contain both upper and lower case characters.
- If the MySQL database is stopped during Full Load, the Full Load will end successfully, but the tables on the target might have less rows than the source tables. If this should happen, either restart the task or reload the tables with the missing rows.
- A Unique Index/Primary Key created on only part of the column data is not supported. If such a Unique Index/Primary Key is encountered, it will be created on the entire target column.

  The following is an example of a statement that creates a Unique Index/Primary Key using only part of the column data:

  CREATE INDEX partial\_name ON customer (name(10));
- Changes to computed (virtual) columns will not be captured.
- Binary log transaction compression is not supported.
- The MySQL primary-primary configuration is not supported.
- Failover of cluster nodes is not supported.
- Capturing changes from an encrypted binlog is not supported.
- Due to an issue with MySQL ODBC Driver 8.0.027 or later, empty TEXT columns may not be replicated correctly during Full Load. For example, if one table row contains a TEXT column with a value and the same column in the next row contains an empty value (but not NULL), both rows will display the value of the first row on the target.

## Limitations and considerations for landing tasks only

- Galera cluster is not supported.
- Zero dates are not supported.

## Limitations and considerations for replication and landing tasks

- Capture of the following DDLs is not supported:

  - All partition DDLs
  - Drop Table
  - Rename Table
- Changes that are older than one year will not be captured.
- Using the alter table <table\_name> add column <column\_name> statement to add columns to the beginning or to the middle of a table is not supported. When the alter table <table\_name> add column <column\_name> statement is used to add a column to the middle of a table, the column will be added to the end of the table instead.
- Zero dates are only supported if both the source and target MySQL-based databases are configured with the same "Strict Mode" (On or Off).
- The Transaction ID of XA transactions will not be displayed in the replication ChangeTable/Audit Table **transaction\_id** header.
- The AR\_H\_USER header column is currently not supported. For more information on header columns, see [*Change Tables*](../../Replicating/read_change_tables.htm).
- If a MySQL table contains LOBs and the task's Replicate Lob columns option is disabled, the table will be replicated without the LOB columns. Note that this only applies to MEDIUMBLOB, LONGBLOB, MEDIUMTEXT and LONGTEXT columns. This limitation does not apply to BLOB, TINYBLOB, TEXT and TINYTEXT columns.
