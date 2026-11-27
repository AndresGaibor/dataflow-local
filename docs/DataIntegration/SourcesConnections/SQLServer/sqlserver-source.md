---
title: "Microsoft SQL Server (log based)"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/SQLServer/sqlserver-source.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases"]
---

# Microsoft SQL Server (log based)

This section explains how to set up a Microsoft SQL Server (log based) on-premises source in a data task. Before you start the data task, make sure that you have fulfilled the [*Prerequisites*](sqlserver-prerequisites.htm), set up the [*Required permissions*](../../../../Global_Common/Content/SharedReplicateHDD/SQLServer-Source/SQLServerDBSource_Security.htm#ar_sqlserverds_1727505754_1656303), and familiarized yourself with the [*Limitations and considerations*](sqlserver-source-limitations.htm).

Information noteThis connector is not supported with the Qlik Talend Cloud Starter subscription.

## Setting connection properties

This section describes the available connection properties. All properties are required unless otherwise indicated.

To open the connector, do the following:

1. In Connections, click Create connection.
2. Select the Microsoft SQL Server (log based) source connector and then provide the following settings:

### Data source

- Data gateway

  Select a Data Movement gateway if required by your use case.

  Information note

  This field is not available with the Qlik Talend Cloud Starter subscription, as it does not support Data Movement gateway. If you have another subscription tier and do not want to use Data Movement gateway, select None.

  For information on the benefits of Data Movement gateway and use cases that require it, see [*Qlik Data Gateway - Data Movement*](../../../Gateways/replication-gateway.htm).
- Cloud provider: None
- Server: The host name or IP address of the computer on which the Microsoft SQL Server database is installed.

  Information note

  To override the default port, add the port to the server name, separated by a comma. For example, if the server name is `myserver.company.local` and the port is `3333`, then the server name should be:

  `myserver.company.local,3333`

### Account properties

User Name and Password: The user name and password of a user authorized to access the Microsoft SQL Server database.

### Database properties

- Database name: There are two methods you can use to specify a database:

  - Method 1 - Select from a list: This method requires the user to be [created on the master database](sqlserver-prerequisites.htm#Database). Click Load databases and then select a database.
  - Method 2 - Manually: Select Enter database name manually and then enter the database name.
- Encrypt (Trust server certificate): Select to encrypt the communication between the database server and Data Movement gateway or between the database server and Qlik Cloud when Data gateway is set to None. When selected, the server certificate will be automatically trusted.
  - Host name in certificate: To only trust the sever certificate if its host name matches the value specified in this field, enter the server certificate's host name.

### CDC properties

- Safeguard policy: For optimal performance, Data Movement gateway will try to capture all unread changes from the active transaction log (TLOG). However, sometimes due to truncation, the active TLOG may not contain all of the unread changes. When this occurs, Data Movement gateway accesses the backup log to capture the missing changes. To minimize the need to access the backup log, Data Movement gateway prevents truncation using one of the following methods:

  - Rely on SQL Server replication agent: This is the default method. When this method is used, Data Movement gateway prevents TLOG truncation by mimicking a transaction in the database. As long as such a transaction is open, changes that appear after the transaction started will not be truncated. If you need Microsoft Replication to be enabled in your database, then you must choose this method.
  - Exclusive automatic truncation: When this method is used, the landing task reads the changes and then uses `sp_repldone` to mark the TLOG transactions as ready for truncation. Although this method does not involve any transactional activities, it can only be used when Microsoft Replication is not running. Also, using this method, only one landing task can access the database at any given time. Therefore, if you need to run parallel landing tasks against the same database, use the default method.

    Information note
    - This method requires the Log Reader Agent to be stopped in the database. If the Log Reader Agent is running when the task starts, Data Movement gateway will forcibly stop it. Alternatively, you can stop the Log Reader Agent manually, before starting the landing task. For instructions on how to do this, refer to the Microsoft SQL Server Management Studio help.
    - When using this method with MS-CDC, the CDC Capture and CDC Cleanup jobs should be stopped and disabled.
    - This method is not available when the Microsoft SQL Server Replication job resides on a remote Distributor machine as Data Movement gateway does not have access to the remote machine.
  - Apply TLOG truncation prevention policy every (seconds):Specify how often to prevent TLOG truncation using one of the methods describes above. Factors that you should consider when determining the policy frequency include storage availability, backup and log routines, and the rate at which Data Movement gateway processes events.

    Information note

    If Exclusive automatic truncation is selected, setting a very short interval (e.g. 1) may adversely affect task processing, and possibly even result in an error.
- Change processing mode (Read changes from): Choose one of the following change processing modes:

  - Prioritize Online Logs - This is the default. Data Movement gateway will first look for the changes in the online transaction logs. If the changes cannot be found in the online transaction logs, it will look for them in the backup transaction logs instead.
  - Prioritize Backup Logs - When this option is enabled, Data Movement gateway will first look for the changes in the backup transaction logs. This can improve performance when reading from the online transaction log is slow (e.g due to lock contention) or when using file-level access to access the backup transaction logs.

    If the changes cannot be found in the backup transaction logs, it will look for them in the online transaction logs instead.
  - Backup Logs Only - When this option is selected, ensure the changes reside in the backup transaction logs only. Selecting this method results in increased latency due to the interval between backups. The actual latency time will remain constant, but will vary according to the backup schedule.
  - Online Logs Only - When this option is selected, ensure the changes reside in the online transaction logs only.
- Alternate backup folder: The location of the backup logs when using a third-party utility to back up the transaction logs (i.e. instead of Microsoft SQL Server’s own backup mechanism). Note that the backup files must be exported to the specified location in standard Microsoft SQL Server format.
- Select virtual backup device types: When this option is selected, changes will be read from the specified virtual device(s). Usually, this option only needs to be enabled when using a third-party backup utility (which will be recorded as a virtual device).

### Internal properties

Internal properties are for special use cases and are therefore not exposed in the dialog. You should only use them if instructed by Qlik Support.

Use the ![Create new](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) and ![Cancel](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin.svg) buttons to the right of the fields to add or remove properties as needed.

### Name

The display name for the source connection.
