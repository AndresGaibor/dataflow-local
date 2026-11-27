---
title: "Required permissions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/Content/SharedReplicateHDD/Oracle/OracleDBSource_Security.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "Oracle"]
---

# Required permissions

This section describes the permissions that are required for working with an Oracle source.

Information note

When moving from Oracle for Amazon RDS, see [*Required Amazon RDS for Oracle permissions*](oracle_rds_prerequisites.htm#Required) instead.

## General permissions

To use an Oracle source in a Data Movement gateway task, the user specified in the Data Movement gateway Oracle connector connection settings must be granted the following privileges in the Oracle database:

Information note

If any of the required privileges cannot be granted to a V$xxx, then grant them to the V\_$xxx.

- SELECT on V\_$ARCHIVED\_LOG
- SELECT on V\_$LOG
- SELECT on V\_$LOGFILE
- SELECT on V\_$DATABASE
- SELECT on V\_$THREAD
- SELECT on V\_$PARAMETER
- SELECT on V\_$NLS\_PARAMETERS
- SELECT on V\_$TIMEZONE\_NAMES
- In a RAC environment, grant:

  SELECT on GV\_$TRANSACTION

  Otherwise, grant:

  SELECT on V\_$TRANSACTION
- SELECT on V\_$CONTAINERS
- SELECT on ALL\_INDEXES
- SELECT on ALL\_OBJECTS
- SELECT on DBA\_OBJECTS - Required if the Oracle version is earlier than 11.2.0.3.
- SELECT on ALL\_TABLES
- SELECT on ALL\_USERS
- SELECT on ALL\_CATALOG
- SELECT on ALL\_CONSTRAINTS
- SELECT on ALL\_CONS\_COLUMNS
- SELECT on ALL\_TAB\_COLS
- SELECT on ALL\_IND\_COLUMNS
- SELECT on ALL\_LOG\_GROUPS
- SELECT on SYS.DBA\_REGISTRY
- SELECT on SYS.OBJ$
- SELECT on SYS.ENC$
- SELECT on DBA\_TABLESPACES
- SELECT on ALL\_TAB\_PARTITIONS
- SELECT on ALL\_ENCRYPTED\_COLUMNS
- If views are exposed: SELECT on ALL\_VIEWS

Grant the following additional privilege (for each source table) when you are using a specific table list:

- SELECT on <any-source-table>;

Grant the following additional privilege when using a pattern for the table list:

- SELECT ANY TABLE;

Grant the following additional privilege (for each source table) when Data Movement gateway adds supplemental logging automatically (the default behavior) and you are using a specific table list.

- ALTER on <any-source-table>;

Grant the following additional privilege when Data Movement gateway adds supplemental logging automatically (the default behavior) and you are using a pattern for the table list.

- ALTER ANY TABLE;
- When accessing an Oracle standby database, the following privilege must be granted:

  SELECT on V$STANDBY\_LOG

- When accessing nested tables, the following privileges must be granted:

  SELECT on all\_nested\_tables

  SELECT on all\_nested\_table\_cols

## Access privileges when using Oracle LogMiner to access the redo logs

If you are using Oracle LogMiner to access the Redo logs, grant the following privileges.

- CREATE SESSION
- EXECUTE on DBMS\_LOGMNR
- SELECT on V\_$LOGMNR\_LOGS
- SELECT on V\_$LOGMNR\_CONTENTS
- LOGMINING

  Information note

  This privilege is only required for Oracle 12c or later.

## Access privileges when using Log Reader to access the redo logs

When using Log Reader to access the Redo logs, the following privileges should be granted to the user specified in the Oracle connector settings:

- CREATE SESSION
- SELECT on v\_$transportable\_platform

  Grant the SELECT on v\_$transportable\_platform privilege if the Redo logs are stored in ASM and accessed by Qlik Talend Data Integration from ASM.
- SELECT ON V\_$DATABASE\_INCARNATION
- CREATE ANY DIRECTORY

  Qlik Talend Data Integration uses following Oracle file access features:
- BFILE read - Used when Qlik Talend Data Integration does not have file-level access to the Redo logs, and the Redo logs are not accessed from ASM.
- DBMS\_FILE\_TRANSFER package - Used to copy the Redo log files to a temporary folder (in which case the EXECUTE ON DBMS\_FILE\_TRANSFER privilege needs to be granted as well)
- DBMS\_FILE\_GROUP package - Used to delete the Redo log files from a temporary/alternate folder (in which case the EXECUTE ON DBMS\_FILE\_GROUP privilege needs to be granted as well).

Oracle file features work together with Oracle directories. Each Oracle directory object includes the name of the folder containing the files which need to be processed.

If you want Qlik Talend Data Integration to create and manage the Oracle directories, you need to grant the CREATE ANY DIRECTORY privilege specified above. Note that the directory names will be prefixed with attrep`_`. If you do not grant this privilege, you need to create the corresponding directories manually. The names of directories that are created manually must not be prefixed with ATTUREP\_, ATTUTMP\_, or ATTUGRP\_. If you create the directories manually and the Oracle user specified in the Oracle Source connector is not the user that created the Oracle Directories, grant the READ on DIRECTORY privilege as well.

If the Oracle source connector is configured to copy the Redo log files to a temporary folder, and the Oracle user specified in the Oracle source connector is not the user that created the Oracle directories, the following additional privileges are required:

- READ on the Oracle directory object specified as the source directory
- WRITE on the directory object specified as the destination directory in the copy process

## Required ASM privileges

The following section describes the additional permissions that are required when the redo logs are stored in ASM.

Grant the following read privilege:

SELECT ON v\_$transportable\_platform

From Oracle 11g Release 2 (11.2.0.2), Data Movement gateway must be granted the SYSASM privilege in order to access the ASM account. For older supported versions, granting Data Movement gateway the SYSDBA privilege should be sufficient.

Information note

When connecting to ASM, Data Movement gateway will first try to log in as SYSDBA and, if unsuccessful, will try to log in as SYSASM.

You can validate ASM account access by opening a command prompt and issuing the following statements:

sqlplus asmuser/asmpassword@+asmserver as sysdba

-OR-

sqlplus asmuser/asmpassword@+asmserver as sysasm
