---
title: "Homogeneous replication"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/SQLServer/sqlserver-source-homog.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "Microsoft SQL Server (log based)"]
---

# Homogeneous replication

The following section describes how Qlik Talend Data Integration handles replication from Microsoft SQL Server to Microsoft SQL Server-based targets. Note that homogeneous replication is only relevant with Replication data projects.

In homogeneous replication, source column and table collations will be replicated to the target as described in [*Column and table collation*](#ar_sqlserverds_1727505754_1659775).

Information note

To prevent data truncation when replicating columns with an **XML** data type, it is strongly recommended to enable the Replicate unlimited LOB columns option in the task settings' [*Metadata*](../../Replicating/replicating-settings-metadata.htm) tab.

## Data type exceptions

When replicating from Microsoft SQL Server database to an SQL Server-based target, source and target data types are identical for all supported Microsoft SQL Server versions, with the following exceptions:

Data type exceptions in homogeneous replication

| Microsoft SQL Server Source | SQL Server-based Target |
| --- | --- |
| VARCHAR | VARCHAR (x)  (when x=0 or x>8000)  else VARCHAR (max) |
| NVARCHAR (length) | NVARCHAR (x)  (when x=0 or x>8000)  else NVARCHAR (max) |
| VARBINARY | VARBINARY (x)  (when x=0 or x>8000)  else VARBINARY (max) |
| HIERARCHYID | VARCHAR (x) |
| TIMESTAMP | VARBINARY |

## Column and table collation

When replicating from Microsoft SQL Server to an SQL Server-based target, column and table collations will be replicated to the target.

Information note

To support collation replication, the DBA must ensure that the collations defined for the source Microsoft SQL Server database are the same as those defined for the SQL Server-based target database.

### Non-nullable columns and primary/unique index names

Primary/Unique Index names are preserved during homogeneous replication. Non-nullable columns are also preserved during homogeneous replication, with the exception of the following data types:

- text
- ntext1
- varchar(max)
- nvarchar(max)
- varbinary(max)
- image
- xml
