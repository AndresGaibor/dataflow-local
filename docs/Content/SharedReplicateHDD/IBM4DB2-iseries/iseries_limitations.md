---
title: "Limitations and considerations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/Content/SharedReplicateHDD/IBM4DB2-iseries/iseries_limitations.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "IBM DB2 for iSeries"]
---

# Limitations and considerations

You should be aware of the following limitations and considerations when using an IBM DB2 for iSeries source.

## Limitations and considerations for all data tasks

- Multi-member (partitioned) tables are supported for Full Load and CDC when Replicate all members of the table is enabled in the endpoint's Advanced tab.
- Field level encryption is not supported
- Journal receivers must be System Managed rather than User Managed.
- Journals containing minimized data are not supported.

  The MINENTDTA parameter should be set to: MINENTDTA(\*NONE)
- All tables must be in the same journal
- The XML data type is not supported
- The DBCLOB data type is not supported
- Row size, excluding LOBs, cannot exceed 32740 bytes
- Usually, Qlik Talend Data Integration only applies source database changes to the target if the transactions with the changes were committed before the Full Load started. However, records that were deleted from the source as part of an uncommitted transaction will not be moved to the target during Full Load.
- DELETE operations in auto-commit mode will be ignored for tables journaled with \*AFTER images. In such cases, DELETE operations will only be captured if one of the Add RRN column options is enabled and is set as the only Primary Key.
- When auto-commit=ON, the timestamp of the last committed transactions will be displayed as "01-01-1970 00:00" in the SOURCE\_CURRENT\_TIMESTAMP column of the attrep\_status Control table.
- Moving columns, tables, and libraries with special characters in their name is not supported.
- Tables created by DDS: If you need to replicate tables created by DDS, please seek guidance from Qlik Support or your Qlik Customer Success Manager.
- Moving data with 4-byte emoji characters is not supported.
- Table and columns names that include non-Latin characters (NLS) are not supported.
- When the Use table and schema system names option is enabled (in the connector settings), only table/schema names that contain uppercase letters, digits, and underscores (\_) are supported.
- Remote journals are not supported.
- Table or columns names that include NLS (non-Latin) characters are not supported.

## Limitations and considerations for replication and landing tasks

- The DROP TABLE DDL is not supported
- The RENAME TABLE DDL is not supported
- In Batch Optimized Apply mode, when a table that matches the task's table capture pattern is created in the source database (CREATE TABLE), the table will not be created in the target database until a transaction occurs in any of the captured tables.
