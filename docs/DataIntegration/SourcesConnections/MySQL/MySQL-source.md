---
title: "MySQL"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/MySQL/MySQL-source.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases"]
---

# MySQL

This section explains how to set up a MySQL source in a data task. Before you start the data task, make sure that you have fulfilled the [*Prerequisites*](prereq-mysql-source.htm), set up the [*Required permissions*](security-req-mysql-source.htm), and familiarized yourself with the [*Limitations and considerations*](limitations-mysql-source.htm).

You need to configure connectivity to MySQL when landing data from any of the following databases:

- On-premises:

  - MySQL
  - Percona

    Information note

    When using Percona as a source, the CDC prerequisites described in [*Capturing changes from a customer-installed MySQL database*](prereq-mysql-source.htm#ar_mysql_902766750_1418057) are not relevant.
  - MariaDB
- Cloud-based:

  - Amazon Aurora
  - Amazon RDS for MySQL
  - Amazon RDS for MariaDB
  - Google Cloud SQL for MySQL
  - Microsoft Azure Database for MySQL

    Information noteMicrosoft Azure Database for MySQL is no longer supported by Microsoft. Consequently, support for Microsoft Azure Database for MySQL as a data source has been discontinued from Data Movement gateway version 2025.5.22.

## Setting connection properties

This section describes the available connection properties. All properties are required unless otherwise indicated.

To open the connector, do the following:

1. In Connections, click Create connection.
2. Select the MySQL source connector and then provide the following settings:

### Data source

- Data gateway

  Select a Data Movement gateway if required by your use case.

  Information note

  This field is not available with the Qlik Talend Cloud Starter subscription, as it does not support Data Movement gateway. If you have another subscription tier and do not want to use Data Movement gateway, select None.

  For information on the benefits of Data Movement gateway and use cases that require it, see [*Qlik Data Gateway - Data Movement*](../../../Gateways/replication-gateway.htm).
- Cloud provider: If your MySQL database is located in the cloud, select the provider:

  - None (for on-premises)
  - Amazon Aurora
  - Amazon RDS
  - Google Cloud
  - Microsoft Azure
- Server: The host name or IP address of the computer on which the MySQL database is installed.
- Port: The port through which Qlik Cloud services will access the MySQL database. The default is 3306.

### Account properties

- User Name and Password

  The user name and password of a user authorized to access the MySQL database.
- SSH tunnel

  Information note
  - This option is only available when Data gateway is set to None.
  - To use this option, you first need to define at least one SSH tunnel connector. For more information, see [*SSH tunnel*](../SSH-tunnel.htm).

  Select this if you want to connect to the data source via an SSH tunnel and then select the SSH tunnel connector from the SSH connection drop-down list.

### SSL options

You can configure Qlik Data Gateway - Data Movement to connect to the data source using SSL.

- SSL Mode:
  Select one of the following:
  - None - Connect with a surname and password only.
  - Preferred
    - Establishes an encrypted connection if the server supports encrypted connections, falling back to an unencrypted connection if an encrypted connection cannot be established.
  - Required - Establishes an encrypted connection if the server supports encrypted connections. The connection attempt fails if an encrypted connection cannot be established.
  - Verify CA - Similar to Required, but also verifies the server Certificate Authority (CA) certificate against the configured CA certificates. The connection attempt fails if no valid matching CA certificates are found.
  - Verify Full - Similar to Verify CA, but also performs host name identity verification by checking the host name the client (i.e. Qlik Data Gateway - Data Movement) uses for connecting to the server against the identity in the certificate that the server sends to the client. The client checks whether the host name that it uses for connecting matches the Common Name value in the server certificate.
    The connection fails if there is a mismatch.
- Trusted certificate: The Certificate Authority (CA) that issued the client certificate file in PEM format.
- Client certificate: The client certificate requested by the server.
- Client certificate key: The client private key file in PEM format.

### Database properties

Database timezone: The timezone where the source database is located.

### CDC properties

Check binary log for changes every - How often to check the binary log for changes when the database is idle (i.e. when no changes are done to the source tables). The default is five seconds. Usually there is no reason to change the interval. However, to reduce the load on the system, you might want to increase the interval in the following scenarios:

- The database is updated infrequently
- Polling the system for changes slows down the system
- Changes are not required in real time

### Internal properties

Internal properties are for special use cases and are therefore not exposed in the dialog. You should only use them if instructed by Qlik Support.

Use the ![Create new](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) and ![Cancel](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin.svg) buttons to the right of the fields to add or remove properties as needed.

### Name

The display name for the source connection.
