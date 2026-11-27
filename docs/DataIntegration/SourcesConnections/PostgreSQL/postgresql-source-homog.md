---
title: "Homogeneous replication"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/PostgreSQL/postgresql-source-homog.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "PostgreSQL"]
---

# Homogeneous replication

The following section describes how Qlik Talend Data Integration handles replication from PostgreSQL to PostgreSQL-based targets. Note that homogeneous replication is only relevant with Replication data projects.

In homogeneous replication, source column and table collations will be replicated to the target as described in [*Column and table collation*](#ar_sqlserverds_1727505754_1659775).

## Limitations and considerations

Homogeneous replication is not supported with the following Qlik Talend Data Integration configurations or operations:

- Apply Changes only tasks
- Stopping and resuming a task
- Starting a task from a timestamp
- When the If target table already exists in the task settings' Full Load Settings tab is set to Do nothing

## Data type considerations and exceptions

When replicating from PostgreSQL to a PostgreSQL-based target, source and target data types are identical for all supported PostgreSQL versions, with the following exceptions:

Data type exceptions in homogeneous replication

| PostgreSQL source | PostgreSQL target |
| --- | --- |
| ENUM | STRING |
| COMPOSITE | STRING |
| NUMERIC | NUMERIC (28,6) |
| NUMERIC (p,s)  A numeric array with precision and scale. | NUMERIC  A numeric array without precision and scale. |
| TINTERVAL | Information note As PostgreSQL have discontinued support for the TINTERVAL data type, tables with this data type will not be created on the target if the target database version does not support it. |
| INT4MULTIRANGE | STRING (255) |
| INT8MULTIRANGE | STRING (255) |
| NUMMULTIRANGE | STRING (255) |
| TSMULTIRANGE | STRING (255) |

See also the note about JSON data type replication in Supported data types.

## Column and table collation

When replicating from PostgreSQL to a PostgreSQL-based target, column and table collations will be replicated to the target.

Information note

To support collation replication, the DBA must ensure that the collations defined for the source PostgreSQL database are the same as those defined for the PostgreSQL-based target database.

### Non-nullable columns and primary/unique index names

Non-nullable columns and Primary/Unique Index names are preserved during homogeneous replication.

## Replication of Partitioned Tables

In order to replicate partitioned tables from PostgreSQL to a PostgreSQL-based target, you need to do the following:

1. Manually create the parent and child tables in the target database.
2. Define a separate task to replicate to those tables.
3. Set the Truncate before loading option in the [*Full load*](../../Replicating/replicating-settings-fullload.htm).
