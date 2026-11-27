---
title: "IBM DB2 for LUW"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/IBM4DB2-luw/IBM4DB2-luw-source.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases"]
---

# IBM DB2 for LUW

This section explains how to set up an IBM DB2 for LUW source in a data task. Before you start the data task, make sure that you have fulfilled the [*Prerequisites*](luw-prerequisites.htm), and familiarized yourself with the [*Limitations and considerations*](../../../../Global_Common/Content/SharedReplicateHDD/IBM4DB2-luw/limitations_db2.htm).

## Setting connection properties

This section describes the available connection properties. All properties are required unless otherwise indicated.

To open the connector, do the following:

1. In Connections, click Create connection.
2. Select the IBM DB2 for LUW source connector and then provide the following settings:

### Data source

- Data gateway

Select a Data Movement gateway to use for moving your data.

For information on Data Movement gateway, see [*Qlik Data Gateway - Data Movement*](../../../Gateways/replication-gateway.htm).

- Server: The IP address or host name of the IBM DB2 for LUW server.
- Port: The port through which to access the IBM DB2 for LUW server.

### Account properties

- User name: The user name required to access the IBM DB2 for LUW server.
- Password: The password required to access the IBM DB2 for LUW server.

### Database properties

- Database: The IBM DB2 for LUW
  source database.
- Maximum buffer size for read (KB): The maximum number of kilobytes to read each time the log is accessed during CDC. If you encounter performance issues, adjusting this number may help.

### SSL options

- Enable SSL: Select to enable SSL
- Keystore database file: (Optional) The keystore database file (containing your private key) on the Data Movement gateway machine. The file must be in CMS format (<filename>.kdb), which is usually the default.
- Stash file: (Optional) A file with an encrypted version of the keystore database password.
- Keystore database password: (Optional) The Keystore database file can be access using either the password that is set here or the stash file that is specified in the Stash file field.

Warning note

KDB and stash files need to be generated using a GSKit version that is compatible with the DB2 driver supported by Data Movement gateway.

For information on which GSKit version is shipped with a particular driver version, see [GSKit Versions Shipped with DB2](https://www.ibm.com/support/pages/node/484539)

### CDC properties

- To enable data capture from IBM DB2 for LUW, the source tables need to be created as follows:

  CREATE / ALTER TABLE table-name …. DATA CAPTURE CHANGES [INCLUDE LONGVAR COLUMNS];

  You can either configure Data Movement gateway to perform this operation by selecting Automatically enable DATA CAPTURE CHANGES (requires admin privilege) in the connector settings or you can do this manually.

- Check for changes every (sec): How often to check the source database for changes.

### Internal properties

Internal properties are for special use cases and are therefore not exposed in the dialog. You should only use them if instructed by Qlik Support.

Use the ![Create new](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) and ![Cancel](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin.svg) buttons to the right of the fields to add or remove properties as needed.

### Name

The display name for the source connection.

## Resuming or starting a task from LRI in a pureScale environment

To resume or start a task from LRI in a pureScale environment:

1. Run the db2pd DB2 command line to determine the Current Log Number:

   $ db2pd -log -db database\_name

   where database\_name is the name of your database.

   The output will be similar to the following:

   ```
   Database Member 0 -- Database SAMPLE -- Active -- Up 0 days 00:27:02 -- Date 2018-05-23-14.49.45.515600
   Logs:
   Current Log Number            2
   Pages Written                 19
   Cur Commit Disk Log Reads     0
   Cur Commit Total Log Reads    0
   Method 1 Archive Status       n/a
   Method 1 Next Log to Archive  n/a
   Method 1 First Failure        n/a
   Method 2 Archive Status       n/a
   Method 2 Next Log to Archive  n/a
   Method 2 First Failure        n/a
   Log Chain ID                  0
   Current LSO                   57142478
   Current LSN                   0x000000000004FB14
    
   Address            StartLSN         StartLSO    State Size       	Pages      Filename
   0x00007F164E99F090 00000000000429EC 48912001    0x00000000 1000       1000       S0000000.LOG
   0x00007F16511319F0 000000000004901E 52988001    0x00000000 1000       1000       S0000001.LOG
   0x00007F1651132350 000000000004F9A6 57064001    0x00000000 1000       1000       S0000002.LOG
   ```

   Information note

   The most recent (current) log is number 2.
2. Run the db2flsn command to determine the LRI/ LSN range of that log file:

   $ db2flsn -db SAMPLE -lrirange **2**

   The output will be similar to the following:

   ```
   S0000002.LOG: has LRI range
   00000000000000010000000000002254000000000004F9A6 to
   000000000000000100000000000022CC000000000004FB13
   ```

   In the above output, the task "Start From" LRI value would be:

   0100000000000022CC000000000004FB13 (i.e. the 34 bytes at the end of the range).

### Unable to retrieve the current LSN?

If you are unable to retrieve the current LSN, you can instruct Qlik Talend Data Integration to scan the log by specifying CurrentLSN=scan (as described in Internal properties above) instead of the current LSN.

Information note

When CurrentLSN=scan, Qlik Talend Data Integration will search the log from the start until it finds the current LSN. This may take some time depending on the size of the log.
