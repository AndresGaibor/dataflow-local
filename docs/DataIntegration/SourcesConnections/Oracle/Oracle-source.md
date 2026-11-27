---
title: "Oracle"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/Oracle/Oracle-source.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases"]
---

# Oracle

This section explains how to set up an Oracle source in a data task. Before you start the data task, make sure that you have fulfilled the [*Prerequisites*](oracle-prerequisites-server.htm), set up the [*Required permissions*](../../../../Global_Common/Content/SharedReplicateHDD/Oracle/OracleDBSource_Security.htm), and familiarized yourself with the [*Limitations and considerations*](../../../../Global_Common/Content/SharedReplicateHDD/Oracle/OracleDB_source_limitations.htm).

Information noteThis connector is not supported with the Qlik Talend Cloud Starter subscription.

You need to configure connectivity to Oracle when landing data from any of the following databases:

- Oracle on-premises
- Amazon RDS for Oracle
- Oracle Cloud

## Setting connection properties

This section describes the available connection properties. All properties are required unless otherwise indicated.

To open the connector, do the following:

1. In Connections, click Create connection.
2. Select the Oracle source connector and then provide the following settings:

### Data source

- Data gateway

Select a Data Movement gateway to use for moving your data.

For information on Data Movement gateway, see [*Qlik Data Gateway - Data Movement*](../../../Gateways/replication-gateway.htm).

- Cloud provider: If your Oracle database is located in the cloud, select the provider:

  - None (default)
  - Amazon RDS
  - Oracle Cloud
- Connection string: The Oracle connection string for the source database. You can type the connect string in any Oracle format, for example:

  `//host:port/service name`

  Where:

  - `host`: This is the name or IP address for the computer with the Oracle database that you are using. For example, `johnboy_W7` or `255.255.255.0`.
  - `port`: (optional) This is the TNS Listener Port number for the computer with the Oracle database that you are using. If you do not enter a port number the default Oracle TNS Listener port is used.
  - `service name`: (optional) This is the service name for the computer with the Oracle database you are using. If you do not enter a service name the default service name is used.

  You can also enter an Oracle Net keyword-value pair. For example:

  "(DESCRIPTION=(ADDRESS=(PROTOCOL=tcp) (HOST=dlsun242) (PORT=5521))

  (CONNECT\_DATA=(SERVICE\_NAME=bjava21)))"

  Information note

  When working with a Multitenant environment, the connection string should specify a specific PDB.

### Account properties

User Name and Password: The user name and password of a user authorized to access the Oracle database.

### Database properties

- Expose number as: Select one of the following:

  - A precision-scale combination
  - FLOAT
  - VARCHAR

  Information note
  - If precision is 39 or greater, select VARCHAR
  - By default, the NUMBER data type is converted to precision 38, scale 10
  - The "Expose NUMBER" definition in the Oracle database is used for the NUMBER data type only (without the explicit precision and scale definition)

- Support nested tables: Select this option if you need to land Oracle tables containing columns that are nested tables or defined types. For more information on this feature and its prerequisites, see [*Moving nested tables*](../../../../Global_Common/Content/SharedReplicateHDD/Oracle/nested_tables.htm).
- Support invisible columns: Select this option to land invisible columns.

### CDC properties

- Retry interval: Use the counter or type the number of seconds that the system waits before resending a query.
- Archived redo logs destination ID: The destination of the archived redo logs. The value should be the same as the DEST\_ID number in the V$archived\_log table.

  When working with multiple log destinations (DEST\_ID), you should specify an Archived redo logs location identifier that represents archived logs that can be accessed by the Qlik replication server. If the Archived redo logs location identifier is not specified, the Qlik replication server will use the ID specified in the Alternate archived redo logs destination ID field. If no alternate ID is specified, then the Qlik replication server will use the minimal existing DEST\_ID.
- Alternate archived redo logs destination ID: The archive destination in the event of a failure to read from the primary destination.
- Use archived redo logs only: When this option is selected, the Qlik replication server will only access the archived redo logs. If the archived redo logs ares stored on ASM only, the user specified in the connectorsettings needs to be granted the ASM privileges described in [*Required ASM privileges*](../../../../Global_Common/Content/SharedReplicateHDD/Oracle/OracleDBSource_Security.htm#ar_oracleds_385117211_beijchii).
- Access redo logs via: Select whether to access the redo logs using Log Reader (the default) or LogMiner. When the Cloud provider is Oracle Cloud, the redo logs will always be accessed using Log Reader. When not selected, the redo logs will be accessed using LogMiner. For guidelines about when LogMiner should be used instead of Log Reader, see [*Redo log files - access method guidelines*](../../../../Global_Common/Content/SharedReplicateHDD/Oracle/Redo_Log_Files_Access_Method_Guidelines.htm).

### ASM properties

- If the Oracle redo logs you are using are stored using Automated Storage Management (ASM), enter the required access information in the designated fields.

  Information note
  - These options are only available when Access redo logs via Log Reader is selected.
  - To access the redo logs in ASM, you also need to grant the additional privileges described in [*Required ASM privileges*](../../../../Global_Common/Content/SharedReplicateHDD/Oracle/OracleDBSource_Security.htm#ar_oracleds_385117211_beijchii)

- ASM Connection String: The connection string to the ASM instance if your Oracle database is using ASM.
- ASM user name: The user name for the ASM user.
- ASM password: The password for the ASM user.
- Number of concurrent ASM Read threads: The number of threads to use when reading the redo logs from ASM. Increasing this number may improve performance when there is a large volume of changes.

### Secret store encryption entries for CDC

When some of the source table columns are encrypted you need to specify the Oracle Wallet encryption Names and Values. For more information, see Finding the wallet entries below.

### Internal properties

Internal properties are for special use cases and are therefore not exposed in the dialog. You should only use them if instructed by Qlik Support.

Use the ![Create new](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) and ![Cancel](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin.svg) buttons to the right of the fields to add or remove properties as needed.

### Name

The display name for the source connection.

## Finding the wallet entries

### Finding the wallet entry used for TDE column encryption

In order to specify the correct encryption key(s) used for TDE tablespace encryption or TDE column encryption, you first need to find the relevant entry (or entries in the case of multiple keys) in the Oracle Wallet containing the encryption key(s). After you find the relevant entry or entries, copy the entry and its value (or entries and values if more than one) into the Names and Values fields respectively.

Information note

To enter multiple values, first copy each entry into a text editor such as Notepad making sure to separate the values with a comma. Then, copy the string containing the values and commas from the text editor and paste it into the **Values** field. There is no need to do this for entries. You can paste the entries directly into the Entries field, remembering to separate each entry with a comma.

To find the Oracle Wallet entries:

1. If the ENCRYPTION\_WALLET\_LOCATION parameter is defined in the sqlnet.ora file, use the wallet from the directory defined by this parameter.
2. If the WALLET\_LOCATION parameter is defined in the sqlnet.ora file, use the wallet from the directory defined by this parameter.
3. In other cases, use the wallet in the default database location.

   Information note

   The name of the wallet should be ewallet.p12
4. Use the “list” option in the Oracle mkstore utility to determine the ORACLE.SECURITY.DB/TS.ENCRYPTION.<SUFFIX> entry name(s), as follows:

   mkstore –wrl <full wallet name> -list
5. If you know which entry/entries is/are used to encrypt the Redo logs, select the entry name(s) and use the “viewEntry” option in the Oracle mkstore utility to determine the entry value, as follows:

   `mkstore –wrl <full wallet name> -viewEntry <entry name>`

   Information note

   If you do not know which entry is used to encrypt the Redo logs, you can select multiple DB or TS entries and determine their values as described above (and then copy and paste the entry names and values into the Names and Values fields). If the specified entries are not correct, the task will fail and the error message will contain the correct entry name.

   Information note

   If the DBA changes the entry while the task is running, the task will fail and the error message will contain the new entry name. Add the new entry (name and value) to the already specified entries and then resume the task.

### Finding the wallet entry used for TDE column encryption in a specific table

This section describes how to find the correct encryption key used for TDE column encryption in a specific table.

To find the Oracle Wallet entry:

1. On the Oracle database, run the following query to return the object\_id (e.g. the. table ID) according to a given owner and table name:

   Select object\_id from all\_objects where owner='<table owner>' and object\_name='<table name>' and object\_type='TABLE';
2. Use the retrieved object\_id in the following query to return the relevant master key:

   select mkeyid from sys.enc$ where obj#=OBJECT\_ID;
3. Select the key value from the Oracle Wallet as follows:

   mkstore –wrl <full\_wallet\_name> -viewEntry <entry\_name>
4. Copy the master key entry and its value into the Names and Values fields respectively.
