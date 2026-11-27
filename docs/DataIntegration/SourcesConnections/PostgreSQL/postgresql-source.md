---
title: "PostgreSQL"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/PostgreSQL/postgresql-source.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases"]
---

# PostgreSQL

This section explains how to set up a PostgreSQL source in a data task. Before you start the data task, make sure that you have fulfilled the [*Prerequisites*](prereq-postgresql-source-dmgateway.htm), set up the [*Limitations and considerations*](postgresql-source-limitations.htm), and familiarized yourself with the [*Required permissions*](../../../../Global_Common/Content/SharedReplicateHDD/PostgreSQL-Source/security_req_postgresql.htm).

You need to configure connectivity to PostgreSQL when landing data from any of the following databases:

- On-premises:

  - PostgreSQL

    Information noteThe PostgreSQL on-premises source also supports moving from Azure Database for PostgreSQL - Flexible Server.
- Cloud-based:

  - Amazon Aurora
  - Amazon RDS for PostgreSQL
  - Microsoft Azure Database for PostgreSQL

    Information noteMicrosoft Azure Database for PostgreSQL is no longer supported by Microsoft. Consequently, support for Microsoft Azure Database for PostgreSQL as a data source has been discontinued from Data Movement gateway version 2025.5.22.
  - Google Cloud SQL for PostgreSQL: Requires Data Movement gateway 2022.11.42 or later
  - Google Cloud AlloyDB for PostgreSQL: Requires Data Movement gateway 2023.5.10 or later.

## Setting connection properties

This section describes the available connection properties. All properties are required unless otherwise indicated.

To open the connector, do the following:

1. In Connections, click Create connection.
2. Select the PostgreSQL source connector and then provide the following settings:

### Data source

- Data gateway

  Select a Data Movement gateway if required by your use case.

  Information note

  This field is not available with the Qlik Talend Cloud Starter subscription, as it does not support Data Movement gateway. If you have another subscription tier and do not want to use Data Movement gateway, select None.

  For information on the benefits of Data Movement gateway and use cases that require it, see [*Qlik Data Gateway - Data Movement*](../../../Gateways/replication-gateway.htm).
- Cloud provider: If your PostgreSQL database is located in the cloud, select the provider:

  - None (select if your PostgreSQL database is on-premises)
  - Amazon Aurora
  - Amazon RDS
  - Microsoft Azure
  - Google Cloud - Requires Data Movement gateway 2022.11.42 or later.
- Server: The host name or IP address of the computer on which the PostgreSQL database is installed.
- Port: The port through which the Data Movement gateway will access the PostgreSQL database. The default is 5432.

### Account properties

- User Name and Password

  The user name and password of a user authorized to access the PostgreSQL database.
- SSH tunnel

  Information note
  - This option is only available when Data gateway is set to None.
  - To use this option, you first need to define at least one SSH tunnel connector. For more information, see [*SSH tunnel*](../SSH-tunnel.htm).

  Select this if you want to connect to the data source via an SSH tunnel and then select the SSH tunnel connector from the SSH connection drop-down list.

### Database properties

Database name: There are two methods you can use to specify a database:

- Method 1 - Select from a list: Click Load databases and then select a database.
- Method 2 - Manually: Select Enter database name manually and then enter the database name.

### SSL options

You can configure to connect to the data source using SSL.

- SSL Mode:
  Select one of the following:
  - None - Connect with a surname and password only.
  - Preferred
    - Establishes an encrypted connection if the server supports encrypted connections, falling back to an unencrypted connection if an encrypted connection cannot be established.
  - Required - Establishes an encrypted connection if the server supports encrypted connections. The connection attempt fails if an encrypted connection cannot be established.
  - Verify CA - Similar to Required, but also verifies the server Certificate Authority (CA) certificate against the configured CA certificates. The connection attempt fails if no valid matching CA certificates are found.
  - Verify Full - Similar to Verify CA, but also performs host name identity verification by checking the host name the client (i.e. ) uses for connecting to the server against the identity in the certificate that the server sends to the client. The client checks whether the host name that it uses for connecting matches the Common Name value in the server certificate.
    The connection fails if there is a mismatch.
- Trusted certificate: The Certificate Authority (CA) that issued the client certificate file in PEM format.
- Client certificate: The client certificate requested by the server.
- Client certificate key: The client private key file in PEM format.
- CRL: The CRL certificate. This file contains certificates revoked by certificate authorities. If the server certificate appears in this list, the connection will fail.
- SSL compression: Select this option to compress the data before it is encrypted.

### CDC properties

WAL heartbeat - A CDC task that is running but not capturing changes (due to source table inactivity) will continue to occupy the LSN position in the slot allocated to the task, thereby preventing truncation of the WAL. Since the WAL is a server-wide resource used by all PostgreSQL processes, it may grow extremely large if no changes are captured for an extended period.

To prevent this from happening, enable the WAL heartbeat option. When this option is enabled, the PostgreSQL source connector mimics task activity by periodically committing pseudo transactions (referred to as "Heartbeats") to the heartbeat table, thereby advancing the task slot’s LSN position.

- Schema for heartbeat artifacts: The schema in which the WAL heartbeat table (attrep\_wal\_heartbeat) will be created. The default value is "public".
- Heartbeat frequency (minutes): The frequency with which to commit transactions to the heartbeat table.

### DDL properties

Information noteThese options are not supported when replicating to cloud storage targets.

- Capture DDL events: When this option is selected, the following operations occur:
  - To facilitate capture of DDL events, Data Movement gateway creates triggers and other operational artifacts in the PostgreSQL database when the task starts. You can later remove these artifacts as described in Removing artifacts from the source database below.
  - Streamed DDL events are captured.
- Create DDL artifacts in schema: The schema in which the operational DDL database artifacts will be created. The default value is "Public".

#### Removing artifacts from the source database

In order to capture DDLs, Data Movement gateway creates various artifacts in the PostgreSQL database when the task starts. You can remove these artifacts if you decide to delete the task at some point in the future.

To remove the artifacts, execute the following statements (in the order they appear below), where `public` is the default schema in which the artifacts were created:

- drop event trigger attrep\_intercept\_ddl

  Information noteThe `event` `trigger` does not belong to a specific schema.
- drop function public.attrep\_intercept\_ddl()
- drop table public.attrep\_ddl\_audit
- drop schema public
- drop table schema.attrep\_wal\_heartbeat

  where schema is the Schema for heartbeat artifacts specified in the connector settings.

Warning note

Dropping a schema should be done with extreme caution, if at all. Never drop an operational schema, especially not `public`.

### Internal properties

Internal properties are for special use cases and are therefore not exposed in the dialog. You should only use them if instructed by Qlik Support.

Use the ![Create new](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) and ![Cancel](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin.svg) buttons to the right of the fields to add or remove properties as needed.

### Miscellaneous

Map the BOOLEAN data type to BOOLEAN (instead of STRING (5)): Select this option if you want BOOLEAN columns to be mapped to the BOOLEAN data type in Qlik Cloud instead of STRING (5), which is the default.

### Name

The display name for the source connection.
