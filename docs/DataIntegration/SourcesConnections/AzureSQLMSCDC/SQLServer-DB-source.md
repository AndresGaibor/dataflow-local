---
title: "Microsoft SQL Server (Microsoft CDC based)"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/AzureSQLMSCDC/SQLServer-DB-source.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases"]
---

# Microsoft SQL Server (Microsoft CDC based)

This section explains how to set up a Microsoft SQL Server (Microsoft CDC) source in a data task. Before you start the data task, make sure that you have fulfilled the [*Prerequisites*](Prereqs-sql-server-cdc.htm), set up the [*Required permissions*](../../../../Global_Common/Content/SharedReplicateHDD/Azure-MSCDC-Source/azremscdc-SQLServerDBSource-security.htm), and familiarized yourself with the [*Limitations and considerations*](azuremscdc-source-limitations.htm).

When moving data from a Microsoft SQL Server (Microsoft CDC based) source, changes are captured from Microsoft Change Tables as opposed to the SQL Server transaction log . Eliminating the need to rely on the transaction log minimizes the risk of data loss resulting from online transaction log retention time and backup transaction log inaccessibility.

Information noteMoving from a geo-replica database is also supported. For more information about geo-replication, see
<https://learn.microsoft.com/en-us/azure/azure-sql/database/active-geo-replication-configure-portal?view=azuresql&tabs=portal>

## Setting connection properties

This section describes the available connection properties. All properties are required unless otherwise indicated.

To open the connector, do the following:

1. In Connections, click Create connection.
2. Select the Microsoft SQL Server (Microsoft CDC based) source connector and then provide the following settings:

### Data source

- Data gateway

  Select a Data Movement gateway to use for moving your data or select None.

  For information on Data Movement gateway, see [*Qlik Data Gateway - Data Movement*](../../../Gateways/replication-gateway.htm).
- Cloud provider: Select one of the following:

  - None if your SQL Server is on-premises or Amazon RDS for SQL Server
  - Microsoft Azure if your data source is Azure (Azure SQL Managed Instance or Azure SQL Database)
  - Google Cloud if your data source is Google Cloud SQL for SQL Server.

    Information noteIf you are using Data Movement gateway, version 2025.5.22 or later is required for Google Cloud.
- Server: The host name or IP address of the computer on which the Microsoft Azure SQL Managed Instance database is installed.

  Information note

  To override the default port, add the port to the server name, separated by a comma. For example, if the server name is `myserver.company.local` and the port is `3333`, then the server name should be:

  `myserver.company.local,3333`

### Account properties

- User Name and Password

  The user name and password of a user authorized to access the Azure SQL Managed Instance database.
- SSH tunnel

  Information note
  - This option is only available when Data gateway is set to None.
  - To use this option, you first need to define at least one SSH tunnel connector. For more information, see [*SSH tunnel*](../SSH-tunnel.htm).

  Select this if you want to connect to the data source via an SSH tunnel and then select the SSH tunnel connector from the SSH connection drop-down list.

### Database properties

- Encrypt (Trust server certificate): Select to encrypt the communication between the database server and Data Movement gateway or between the database server and Qlik Cloud when Data gateway is set to None. When selected, the server certificate will be automatically trusted.
  - Host name in certificate: To only trust the sever certificate if its host name matches the value specified in this field, enter the server certificate's host name.
- Database name: There are two methods you can use to specify a database:

  - Method 1 - Select from a list: This method requires the user to be [created on the master database](Prereqs-sql-server-cdc.htm#Database). Click Load databases and then select a database.
  - Method 2 - Manually: Select Enter database name manually and then enter the database name.

### CDC properties

Enable MS-CDC on all captured tables - Select this option to automatically enable MS-CDC for all selected source tables (on all columns). When this option is selected, the MS-CDC tables will be created in the database's default filegroup.

Warning noteEnabling MS-CDC on all captured tables requires the user to be a member of the db\_owner database role.

### DDL properties

Information noteThese options are not supported when replicating to cloud storage targets.

- Capture DDL events: When this option is selected, the following operations occur:
  - To facilitate capture of DDL events, Data Movement gateway creates triggers and other operational artifacts in the Microsoft SQL Server database when the task starts. You can later remove these artifacts as described in Removing artifacts from the source database below.
  - Streamed DDL events are captured.
- Create DDL artifacts in schema: The schema in which the DDL database artifacts will be created. The default value is dbo.

#### Removing artifacts from the source database

In order to capture DDLs, Data Movement gateway creates various artifacts in the Microsoft SQL Server database when the task starts. You can remove these artifacts if you decide to delete the task at some point in the future.

To remove the artifacts, execute the following statements (in the order they appear below), where dbo is the default schema in which the artifacts were created:

DROP TRIGGER [attrep\_mscdc\_ddl\_catcher] ON DATABASE

DROP TABLE [dbo].[attrep\_mscdc\_ddl\_history]

### Internal properties

Internal properties are for special use cases and are therefore not exposed in the dialog. You should only use them if instructed by Qlik Support.

Use the ![Create new](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) and ![Cancel](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin.svg) buttons to the right of the fields to add or remove properties as needed.

### Name

The display name for the source connection.
