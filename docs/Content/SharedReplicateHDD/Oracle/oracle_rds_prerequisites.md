---
title: "Working with Amazon RDS for Oracle"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/Content/SharedReplicateHDD/Oracle/oracle_rds_prerequisites.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "Oracle"]
---

# Working with Amazon RDS for Oracle

Before you can land data from Amazon RDS for Oracle, make sure to fulfill the prerequisites described below.

Information noteOracle databases with Multi-AZ enabled are supported.

## Amazon RDS for Oracle considerations and limitations

When moving from Amazon RDS for Oracle, TDE is supported only with encrypted tablespace and only when using Oracle LogMiner.

## Required Amazon RDS for Oracle permissions

This topic describes the permissions required when moving from Amazon RDS for Oracle.

Grant the following privileges:

- GRANT SELECT ANY TABLE
- GRANT SELECT on ALL\_VIEWS to user;
- GRANT SELECT ANY TRANSACTION to user;
- GRANT SELECT on DBA\_TABLESPACES to user;
- GRANT SELECT on ALL\_TAB\_PARTITIONS to user;
- GRANT SELECT on ALL\_INDEXES to user;
- GRANT SELECT on ALL\_OBJECTS to user;
- GRANT SELECT on ALL\_TABLES to user;
- GRANT SELECT on ALL\_USERS to user;
- GRANT SELECT on ALL\_CATALOG to user;
- GRANT SELECT on ALL\_CONSTRAINTS to user;
- GRANT SELECT on ALL\_CONS\_COLUMNS to user;
- GRANT SELECT on ALL\_TAB\_COLS to user;
- GRANT SELECT on ALL\_IND\_COLUMNS to user;
- GRANT SELECT on ALL\_LOG\_GROUPS to user;
- GRANT LOGMINING TO user;

In addition, execute the following statements:

```
exec rdsadmin.rdsadmin_util.grant_sys_object('V_$ARCHIVED_LOG','user','SELECT');
exec rdsadmin.rdsadmin_util.grant_sys_object('V_$LOG','user','SELECT');
exec rdsadmin.rdsadmin_util.grant_sys_object('V_$LOGFILE','user','SELECT');
exec rdsadmin.rdsadmin_util.grant_sys_object('V_$DATABASE','user','SELECT');
exec rdsadmin.rdsadmin_util.grant_sys_object('V_$THREAD','user','SELECT');
exec rdsadmin.rdsadmin_util.grant_sys_object('V_$PARAMETER','user','SELECT');
exec rdsadmin.rdsadmin_util.grant_sys_object('V_$NLS_PARAMETERS','user','SELECT');
exec rdsadmin.rdsadmin_util.grant_sys_object('V_$TIMEZONE_NAMES','user','SELECT');
exec rdsadmin.rdsadmin_util.grant_sys_object('V_$TRANSACTION','user','SELECT');
exec rdsadmin.rdsadmin_util.grant_sys_object('V_$CONTAINERS','user','SELECT');
exec rdsadmin.rdsadmin_util.grant_sys_object('DBA_REGISTRY','user','SELECT');
exec rdsadmin.rdsadmin_util.grant_sys_object('OBJ$','user','SELECT');
exec rdsadmin.rdsadmin_util.grant_sys_object('ALL_ENCRYPTED_COLUMNS','user','SELECT');
exec rdsadmin.rdsadmin_util.grant_sys_object('V_$LOGMNR_LOGS','user','SELECT');
exec rdsadmin.rdsadmin_util.grant_sys_object('V_$LOGMNR_CONTENTS','user','SELECT');
exec rdsadmin.rdsadmin_util.grant_sys_object('DBMS_LOGMNR','user','EXECUTE');
```

## Preparing Moving from Amazon RDS for Oracle

This section details the requirements for working with Oracle on Amazon RDS.

### Set up supplemental logging

Qlik Talend Data Integration requires database-level supplemental logging to be enabled. To enable database-level supplemental logging, execute the following command:

exec rdsadmin.rdsadmin\_util.alter\_supplemental\_logging('ADD');

Although not required, examples of additional commands that you can execute to change the supplemental logging attributes include:

exec rdsadmin.rdsadmin\_util.alter\_supplemental\_logging('ADD','ALL');

exec rdsadmin.rdsadmin\_util.alter\_supplemental\_logging('DROP','PRIMARY KEY');

### Enabling automatic backups

In Step 5: Management Options of setting up your Oracle database instance, set the Enabled Automatic Backups option to Yes.

### Setting up archiving

To retain archived redo logs of your Oracle database instance (which will allow Qlik Talend Data Integration to retrieve the log information using Oracle LogMiner), execute the following command (example 24 hours):

exec rdsadmin.rdsadmin\_util.set\_configuration('archivelog retention hours',24);

Make sure that your storage has sufficient space for the archived redo logs during the specified period.

### Using Log Reader to access the redo logs

The following steps are relevant only when using Log Reader to access the redo logs.

#### Create directories for online and archived logs

Before you can use Log Reader, you need to create directories for the online and archived logs.

To create the directories, run the following commands:

exec rdsadmin.rdsadmin\_master\_util.create\_archivelog\_dir;

exec rdsadmin.rdsadmin\_master\_util.create\_onlinelog\_dir;

To remove the directories (if there are no ongoing moving tasks), run the following commands:

exec rdsadmin.rdsadmin\_master\_util.drop\_archivelog\_dir;

exec rdsadmin.rdsadmin\_master\_util.drop\_onlinelog\_dir;

#### Limitations and considerations

The following Oracle features are not supported when using Log Reader with Amazon RDS for Oracle:

- ASM
- TDE
