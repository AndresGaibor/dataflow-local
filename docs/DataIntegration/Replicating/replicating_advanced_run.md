---
title: "Advanced run options"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Replicating/replicating_advanced_run.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating a replication project"]
---

# Advanced run options

In addition to the standard run, stop, and resume options, several other options for running tasks are available. You can open the Advanced run options dialog by doing any of the following:

- Select Advanced run options from the replication task's ![Menu button consisting of 3 vertical dots.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_vertical.svg) menu, either in pipeline view or in tile view.
- Open the replication task, and select Advanced run options from the ![More icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) menu in the top right.

## Processing changes

In the Advanced run options dialog, select Process changes. The following options are available:

- Tables are already loaded. Start processing changes from:

  Information noteMetadata changes performed on the source tables while a task is stopped (for example, DROP COLUMN) will not be captured when the task is resumed from an earlier time or position (SCN/LSN). In such a case, the metadata that exists when the task is resumed will be captured.

  - Date and Time: Set the date and time from where you want to start capturing changes.

    Information note
    - When logs are deleted from the database (e.g. due to a purge policy), a log matching the specified date and time may not exist. In this case, the data task will resume the task from the earliest point possible, after the specified date and time.
    - With the IBM DB2 for LUW source endpoint, this option cannot be used to start Apply Changes tasks from a point before the original start time of the Apply Changes task. Or, to put it another way, it can only be used to start tasks from any time after the original start time of the Apply Changes task.
    - The timestamp uses the local time of the browser machine.
  - Source change position (SCN or LSN): Specify the position in the log from where to resume change processing. The source change position format differs according to your data source. For more information, see [*How to Find the Source Change Position*](#How).

    Information note

    The Source change position option is supported with the following source endpoints only:

    - Oracle
    - Microsoft SQL Server
    - MySQL
    - PostgreSQL
    - IBM DB2 for z/OS
    - IBM DB2 for LUW

## Recovering tasks

In the Advanced run options dialog, select Recover. The following options are available:

- Recover using locally stored checkpoint: Use this option if recovery is not possible using the Tables are already loaded. Start processing changes from option (due to corrupt swap files, for example). When this option is selected, the replication task uses the checkpoint data stored in <Data\_Folder\_Path>/data/tasks/<task\_name>/StateManager to recover the task.

  Information note

  When using this option, be aware of the following limitations and considerations:

  - Supported in Transactional Apply changes mode only and only with data targets that support transactions.
  - The following data sources are supported only:
    - Oracle
    - Microsoft SQL Server
    - MySQL
    - PostgreSQL
    - IBM DB2 for z/OS
    - SAP HANA
  - Tasks can only be recovered during CDC (i.e. after Full Load Completes)
- Recover using checkpoint stored on target: Recover a task using the CHECKPOINT value from the attrep\_txn\_state table (created in the target database).

  Example checkpoint value:

  checkpoint:V1#15#0000038b:000033f1:0004#0#261#0000038b:0000348b:0009#0#273

  Select this option (as opposed to the Recover using locally stored checkpoint option) if the files in the data folder are corrupted or if the storage device containing the data folder has failed.

  For a detailed explanation of how to set up and implement recovery using the attrep\_txn\_state table, see [*Recovering from data folder loss or corruption*](#Recoveri).

## How to Find the Source Change Position

The following section explains how to locate the source change position for each of the supported databases.

#### MySQL

OPTION 1:

1. Execute:

   SHOW BINARY LOGS;
2. Choose a binlog file (e.g. log.000123).
3. Execute:

   SHOW BINLOG EVENTS IN 'binlog\_filename';

   Example:

   SHOW BINLOG EVENTS IN 'log.000123';
4. Locate the position of a BEGIN or DDL statement (e.g. 1777888).

   Information note

   MySQL does not support a "start from position" located in the middle of a transaction, which is why you must select either BEGIN or DDL.
5. Set the internal parameter:

   StartFromPosition = binlog\_filename:begin\_or\_ddl\_position

   Example:

   StartFromPosition = log.000123:1777888

OPTION 2:

1. Execute:

   SHOW MASTER STATUS;
2. Set the "Start from position" as:

   firstColumnValue:secondColumnValue

   Example:

   mysql.007472:775

#### Microsoft SQL Server

Execute:

SELECT MAX([Current LSN]) FROM fn\_dblog(null,null);

Example: 00002717:00000e08:0003

#### Oracle

Execute:

SELECT current\_scn FROM V$DATABASE;

Example: 1471212002

#### PostgreSQL

Note that the command differs according to your PostgreSQL version.

PostgreSQL 10 and later

Execute:

SELECT \* FROM pg\_current\_wal\_lsn();

#### IBM DB2 for z/OS

Specify the LSN, which is the RBA in a non data sharing environment, and the LRSN in a data sharing environment

#### IBM DB2 for LUW

1. Execute db2pd to find the correct log name.
2. Execute db2flsn with the returned log name and use the current LRI value.

   See also: [*Resuming or starting a task from LRI in a pureScale environment*](../SourcesConnections/IBM4DB2-luw/IBM4DB2-luw-source.htm#ar_ibm_db2_456845099_55844)

   For more information, refer to "Resuming or Starting a Task from LRI in a pureScale Environment" in the Replicate Help.

## Recovering from data folder loss or corruption

During normal operation, the moving state is stored in the following location:

<Data\_Folder\_Path>/data/tasks/<task\_name>/StateManager

This enables tasks that cannot be resumed normally (due to corrupt swap files, for example) to be recovered using the Recover using locally stored checkpoint option described above. However, if the files in the data folder become corrupted or if the storage device containing the data folder fails, tasks must be recovered using the Recover using checkpoint stored on target option instead.

### Considerations and limitations

When using this option, be aware of the following considerations and limitations:

- This option will only be available if the Store task recovery data in target database option was enabled in the Task Settings' *Change processing tuning* tab before CDC completed.
- The Apply changes mode must be set to Transactional.
- The following data source types are supported only:
  - Amazon RDS for MySQL
  - Amazon RDS for PostgreSQL
  - Amazon RDS for SQL
  - AWS Aurora Cloud for PostgreSQL
  - Google Cloud SQL for MySQL
  - Google Cloud SQL for PostgreSQL
  - IBM DB2 for z/OS
  - Microsoft Azure Database for MySQL
  - Microsoft Azure SQL Managed Instance
  - Microsoft SQL Server
  - MySQL
  - Oracle
  - PostrgreSQL
  - SAP HANA
- The Microsoft SQL Server target type is supported only.
- Tasks can only be recovered during CDC (after Full Load completes)

### Setting up and initiating task recovery

For recovery to be successful, the source database transaction logs must be available from the time the task failed.

To set up a task for recovery

1. Make sure to enable the Store task recovery data in target database option in the Task Settings' Change processing tuning tab. This option can be enabled at any time during CDC, although it must be enabled before CDC completes.
2. Run the task.

In addition to the selected source tables, the task will write the checkpoint data to the attrep\_txn\_state table in the target database (and automatically create the table if it has not already been created by another task).

To initiate recovery

1. Access the attrep\_txn\_state table in the target database and locate the failed task in the TASK\_NAME column. If there are tasks with the same name running on multiple Qlik Talend Data Integration Servers, you will also need to locate the appropriate server in the SERVER\_NAME column. After locating the relevant task, copy the value in the corresponding CHECKPOINT column.
2. Select the Recover using checkpoint stored on target option and then provide the CHECKPOINT value (preferably by pasting) as described above.
3. Click OK to start the recovery.

During recovery, the replication task does not write anything to the target database until it identifies the commit event corresponding to the CHECKPOINT value. Once it identifies the CHECKPOINT commit event, recovery is performed and the task reverts to standard operation.
