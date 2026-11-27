---
title: "Homogeneous replication"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/MySQL/homogeneous_replication.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "MySQL"]
---

# Homogeneous replication

The following section describes how Qlik Talend Data Integration handles replication from MySQL to MySQL-based targets. Note that homogeneous replication is only relevant with Replication data projects.

Information note

When replicating a TIMESTAMP column, the time is converted to UTC on the target.

## Limitations and considerations

Homogeneous replication is not supported with the following Qlik Talend Data Integration configurations or operations:

- Apply Changes only tasks
- Stopping and resuming a task
- Starting a task from a timestamp
- When the If target table already exists in the task settings' Full Load Settings tab is set to Do nothing

## Data types

The data types will be identical with the following exceptions:

Exceptions

| MySQL source data types | MySQL-based target data types |
| --- | --- |
| JSON | LONGTEXT |

Information note

When using data types from other database engines, the data type on the target will be the corresponding MySQL data type. For more information on using non-native data types, refer to the MySQL online Help.

## Collation

Table and column collations will be replicated to the target. Collatable data types are indicated in the Collatable column of the Supported data types table.

To support collation replication, the DBA must ensure that the collations defined for the source MySQL database are the same as those defined for the MySQL-based target database.

## Non-nullable columns and primary/unique index names

Non-nullable columns and Primary/Unique Index names are preserved during homogeneous replication.
