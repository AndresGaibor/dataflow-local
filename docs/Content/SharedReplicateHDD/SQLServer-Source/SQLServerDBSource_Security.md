---
title: "Required permissions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/Content/SharedReplicateHDD/SQLServer-Source/SQLServerDBSource_Security.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "Microsoft SQL Server (log based)"]
---

# Required permissions

To use Microsoft SQL Server (Log-Based) as a source in a landing task, the user specified in the Microsoft SQL Server (Log-Based) connection properties must be one of the following:

- A member of both the `db_owner` database role and the `sysAdmin` fixed server role.
- A member of the `db_owner` database role but not a member of sysAdmin fixed server role. This also requires you to perform the procedures described in Setting up a non-sysadmin user in a standalone environment below.

## Setting up a non-sysadmin user in a standalone environment

The following section describes how to set up Microsoft SQL Server when a non-sysadmin user is specified in the connector connection settings.

Information note

If you want to set up a non-sysadmin user in an AlwaysOn environment, see [*Setting up a non-sysadmin user when working with AlwaysOn availability groups*](work_with_sql_server_alwayson_availability_groups.htm#Setting).

## Setup procedure

To support a non-sysadmin user:

1. Set up Microsoft SQL Server for Replication as described in [*Setting up Microsoft SQL Server for replication*](sqlserver_replication.htm).
2. Enable MS-REPLICATION on the source database. This can either be done manually or by running the task once using a sysadmin user.

   Information note

   MS-REPLICATION distributor should either be configured as local or in a way that allows access to non-sysadmin users via the associated linked server.
3. Create schema `[attrep]` in the Master DB.
4. Create the table valued function `[attrep].[split_partition_list]` on the Master database:

   ```
   USE [master]
   GO

   set ansi_nulls on
   go

   set quoted_identifier on
   go

   if (object_id('[attrep].[split_partition_list]','TF')) is not null
   drop  function [attrep].[split_partition_list];
   go

   create function [attrep].[split_partition_list]
   (
   @plist varchar(8000),	--A delimited list of partitions
   @dlm nvarchar(1)	--Delimiting character
   )
   returns @partitionsTable table --Table holding the BIGINT values of the string fragments
   (
   pid bigint primary key
   )
   as
   begin
   declare @partition_id bigint;
   declare @dlm_pos integer;
   declare @dlm_len integer;

   set @dlm_len = len(@dlm);

   while (charindex(@dlm,@plist)>0)
   begin
   set @dlm_pos = charindex(@dlm,@plist);
   set @partition_id = cast( ltrim(rtrim(substring(@plist,1,@dlm_pos-1))) as bigint);
   insert into @partitionsTable (pid) values (@partition_id)
   set @plist = substring(@plist,@dlm_pos+@dlm_len,len(@plist));
   end
   set @partition_id = cast (ltrim(rtrim(@plist)) as bigint);
   insert into @partitionsTable (pid) values (  @partition_id  );
   return
   end
   GO
   ```
5. Create procedure `[attrep].[rtm_dump_dblog]` on the Master database:

   ```
   use [MASTER]
   go

   if (object_id('[attrep].[rtm_dump_dblog]','P')) is not null
   drop procedure [attrep].[rtm_dump_dblog];
   go

   set ansi_nulls on
   go

   set quoted_identifier on
   go

   create procedure [attrep].[rtm_dump_dblog]
   (
   @start_lsn        varchar(32),
   @seqno            integer,
   @filename         varchar(260),
   @partition_list        varchar(8000), -- A comma delimited list: P1,P2,... Pn
   @programmed_filtering integer,
   @minPartition     bigint,
   @maxPartition     bigint
   )
   as begin

           declare @start_lsn_cmp varchar(32); -- Stands against the GT comparator

           SET NOCOUNT ON  -- Disable "rows affected display"

           set @start_lsn_cmp = @start_lsn;
           if (@start_lsn_cmp) is null
                   set @start_lsn_cmp = '00000000:00000000:0000';

           if (@partition_list is null)
           begin
                   RAISERROR ('Null partition list waspassed',16,1);
                   return
                   --set @partition_list = '0,';    -- A dummy which is never matched
           end

           if (@start_lsn) is not null
                   set @start_lsn = '0x'+@start_lsn;

   if (@programmed_filtering=0)
           SELECT
                   [Current LSN],
                   [operation],
                   [Context],
                   [Transaction ID],
                   [Transaction Name],
                   [Begin Time],
                   [End Time],
                   [Flag Bits],
                   [PartitionID],
                   [Page ID],
                   [Slot ID],
                   [RowLog Contents 0],
                   [Log Record],
                   [RowLog Contents 1], -- After Image
   		 [Xact Id] -- Only needed if you are using the AR_H_XACT_ID custom header
           FROM
                   fn_dump_dblog (
                           @start_lsn, NULL, N'DISK', @seqno, @filename,
                           default, default, default, default, default, default, default,
                           default, default, default, default, default, default, default,
                           default, default, default, default, default, default, default,
                           default, default, default, default, default, default, default,
                           default, default, default, default, default, default, default,
                           default, default, default, default, default, default, default,
                           default, default, default, default, default, default, default,
                           default, default, default, default, default, default, default,
                           default, default, default, default, default, default, default)
           where [Current LSN] collate SQL_Latin1_General_CP1_CI_AS >= @start_lsn_cmp collate SQL_Latin1_General_CP1_CI_AS -- This aims for implementing FN_DBLOG based on GT comparator.
           and
           (
             (  [operation] in ('LOP_BEGIN_XACT','LOP_COMMIT_XACT','LOP_ABORT_XACT') )
             or
             (  [operation] in ('LOP_INSERT_ROWS','LOP_DELETE_ROWS','LOP_MODIFY_ROW')
                   and
                   ( ( [context]   in ('LCX_HEAP','LCX_CLUSTERED','LCX_MARK_AS_GHOST') ) or ([context] = 'LCX_TEXT_MIX' and  (datalength([RowLog Contents 0]) in (0,14,28))) )   -- This one filters only TEXT_MIX of interest.\
                   and       [PartitionID] in ( select * from master.attrep.split_partition_list (@partition_list,','))
             )
             or
             ([operation] = 'LOP_HOBT_DDL')
           )
   else
           SELECT
                   [Current LSN],
                   [operation],
                   [Context],
                   [Transaction ID],
                   [Transaction Name],
                   [Begin Time],
                   [End Time],
                   [Flag Bits],
                   [PartitionID],
                   [Page ID],
                   [Slot ID],
                   [RowLog Contents 0],
                   [Log Record],
                   [RowLog Contents 1], -- After Image
   		 [Xact Id] -- Only needed if you are using the AR_H_XACT_ID custom header
   	FROM
                   fn_dump_dblog (
                           @start_lsn, NULL, N'DISK', @seqno, @filename,
                           default, default, default, default, default, default, default,
                           default, default, default, default, default, default, default,
                           default, default, default, default, default, default, default,
                           default, default, default, default, default, default, default,
                           default, default, default, default, default, default, default,
                           default, default, default, default, default, default, default,
                           default, default, default, default, default, default, default,
                           default, default, default, default, default, default, default,
                           default, default, default, default, default, default, default)
           where [Current LSN] collate SQL_Latin1_General_CP1_CI_AS >= @start_lsn_cmp collate SQL_Latin1_General_CP1_CI_AS
           and
           (
             (  [operation] in ('LOP_BEGIN_XACT','LOP_COMMIT_XACT','LOP_ABORT_XACT') )
             or
             (  [operation] in ('LOP_INSERT_ROWS','LOP_DELETE_ROWS','LOP_MODIFY_ROW')
                   and
                   ( ( [context]   in ('LCX_HEAP','LCX_CLUSTERED','LCX_MARK_AS_GHOST') ) or ([context] = 'LCX_TEXT_MIX' and  (datalength([RowLog Contents 0]) in (0,14,28))) )   -- This one filters only TEXT_MIX of interest.\
                   and           ([PartitionID] is not null) and ([PartitionID] >= @minPartition and [PartitionID]<=@maxPartition)
             )
             or
             ([operation] = 'LOP_HOBT_DDL')
           )
           SET NOCOUNT OFF -- Re-enable "rows affected display"

   end
   GO
   ```
6. Create certificate on Master DB:

   ```
   Use [master]
   Go
   CREATE CERTIFICATE [attrep_rtm_dump_dblog_cert]
   ENCRYPTION BY PASSWORD = N'choose_your_own_pwd'
   WITH SUBJECT = N'Certificate for FN_DUMP_DBLOG Permissions';
   ```
7. Create login from the certificate:

   ```
   Use [master]
   Go
   CREATE LOGIN attrep_rtm_dump_dblog_login FROM CERTIFICATE
   [attrep_rtm_dump_dblog_cert];
   ```
8. Add the login to the sysadmin server role:

   ```
   ALTER SERVER ROLE [sysadmin] ADD MEMBER [attrep_rtm_dump_dblog_login];
   ```
9. Add the certificate signature to `[master].[attrep].[rtm_dump_dblog]:`

   ```
   Use [master]
   GO
   ADD SIGNATURE
   TO [master].[attrep].[rtm_dump_dblog]
   BY CERTIFICATE [attrep_rtm_dump_dblog_cert]
   WITH PASSWORD = 'choose_your_own_pwd';
   ```

   Information note

   If the stored procedure is recreated, you need to add the signature again.
10. Create procedure `[attrep].[rtm_position_1st_timestamp]` on the Master database:

    ```
    use [master]
    if object_id('[attrep].[rtm_position_1st_timestamp]','P') is not null
    DROP PROCEDURE [attrep].[rtm_position_1st_timestamp];
    go
    create procedure [attrep].[rtm_position_1st_timestamp]
    (
    @dbname                sysname,      -- Database name
    @seqno                 integer,      -- Backup set sequence/position number within file
    @filename              varchar(260), -- The backup filename
    @1stTimeStamp          varchar(40)   -- The timestamp to position by
    )
    as begin

    SET NOCOUNT ON       -- Disable "rows affected display"

    declare @firstMatching table
    (
    cLsn varchar(32),
    bTim datetime
    )

    declare @sql nvarchar(4000)
    declare @nl                       char(2)
    declare @tb                       char(2)
    declare @fnameVar                 nvarchar(254) = 'NULL'

    set @nl  = char(10); -- New line
    set @tb  = char(9)   -- Tab separator

    if (@filename is not null)
    set @fnameVar = ''''+@filename +''''

    set @sql='use ['+@dbname+'];'+@nl+
    'select top 1 [Current LSN],[Begin Time]'+@nl+
    'FROM fn_dump_dblog (NULL, NULL, NULL, '+ cast(@seqno as varchar(10))+','+ @fnameVar+','+@nl+
    @tb+'default, default, default, default, default, default, default,'+@nl+
    @tb+'default, default, default, default, default, default, default,'+@nl+
    @tb+'default, default, default, default, default, default, default,'+@nl+
    @tb+'default, default, default, default, default, default, default,'+@nl+
    @tb+'default, default, default, default, default, default, default,'+@nl+
    @tb+'default, default, default, default, default, default, default,'+@nl+
    @tb+'default, default, default, default, default, default, default,'+@nl+
    @tb+'default, default, default, default, default, default, default,'+@nl+
    @tb+'default, default, default, default, default, default, default)'+@nl+
    'where operation=''LOP_BEGIN_XACT''' +@nl+
    'and [Begin Time]>= cast('+''''+@1stTimeStamp+''''+' as datetime)'+@nl

    --print @sql
    delete from  @firstMatching
    insert into @firstMatching  exec sp_executesql @sql    -- Get them all

    select top 1 cLsn as [matching LSN],convert(varchar,bTim,121) as [matching Timestamp] from @firstMatching;

    SET NOCOUNT OFF      -- Re-enable "rows affected display"

    end
    GO
    ```
11. Create certificate on Master DB:

    ```
    Use [master]
    Go
    CREATE CERTIFICATE [attrep_rtm_position_1st_timestamp_cert]
    ENCRYPTION BY PASSWORD = N'choose_your_own_pwd'
    WITH SUBJECT = N'Certificate for FN_POSITION_1st_TIMESTAMP Permissions';
    ```
12. Create login from the certificate:

    ```
    Use [master]
    Go
    CREATE LOGIN attrep_rtm_position_1st_timestamp_login FROM CERTIFICATE
    [attrep_rtm_position_1st_timestamp_cert];
    ```
13. Add the login to the sysadmin server role:

    ```
    ALTER SERVER ROLE [sysadmin] ADD MEMBER [attrep_rtm_position_1st_timestamp_login];
    ```
14. Add the signature to `[master].[attrep].[rtm_position_1st_timestamp]` by the certificate:

    ```
    Use [master]
    GO
    ADD SIGNATURE
    TO [master].[attrep].[rtm_position_1st_timestamp]
    BY CERTIFICATE [attrep_rtm_position_1st_timestamp_cert]
    WITH PASSWORD = 'choose_your_own_pwd';
    ```

    Information note

    If the stored procedure is recreated, you need to add the signature again.
15. Create function [attrep].[rtm\_check\_file\_exists] on the Master DB:

    USE [master]

    GO

    IF object\_id('[attrep].[rtm\_check\_file\_exists]','FN') IS NOT NULL

    DROP FUNCTION [attrep].[rtm\_check\_file\_exists];

    GO

    CREATE FUNCTION [attrep].[rtm\_check\_file\_exists]

    (

    @filename varchar(260)

    )
    returns int

    as

    begin

    declare @exists int = 0;

    exec master.dbo.xp\_fileexist @filename, @exists OUT;

    return @exists;

    end

    GO
16. Create attrep\_rtm\_check\_file\_exists certificate on the Master DB:

    CREATE CERTIFICATE [attrep\_rtm\_check\_file\_exists\_cert]

    ENCRYPTION BY PASSWORD = N'choose\_your\_own\_pwd'

    WITH SUBJECT = N'Certificate for rtm\_check\_file\_exists Permissions';
17. Create attrep\_rtm\_check\_file\_exists\_login from the certificate:

    CREATE LOGIN attrep\_rtm\_check\_file\_exists\_login

    FROM CERTIFICATE [attrep\_rtm\_check\_file\_exists\_cert];
18. Add the login to the sysadmin server role:

    ALTER SERVER ROLE [sysadmin] ADD MEMBER attrep\_rtm\_check\_file\_exists\_login;
19. Add the signature to function [rtm\_check\_file\_exists] by the certificate:

    ADD SIGNATURE TO [master].[attrep].[rtm\_check\_file\_exists]

    BY CERTIFICATE [attrep\_rtm\_check\_file\_exists\_cert]

    WITH PASSWORD = N'choose\_your\_own\_pwd';

    Information noteIf the stored procedure is recreated, you need to add the signature again.
20. Create procedure `[attrep].[rtm_dbcc_page]` on the Master database:

    ```
    use [MASTER]
    go
    if (object_id('[attrep].[rtm_dbcc_page]','P')) is not null
    drop procedure [attrep].[rtm_dbcc_page];
    go

    CREATE PROCEDURE [attrep].[rtm_dbcc_page]
        @DBName NVARCHAR(128),
        @FileId INT,
        @PageId INT,
        @PrintMode INT = 1
    AS
    BEGIN
        SET NOCOUNT ON;

    CREATE TABLE #DbccPageOutput (
        [ParentObject] VARCHAR(255),
        [Object]       VARCHAR(255),
        [Field]        VARCHAR(255),
        [Value]        VARCHAR(255)
    );

    DECLARE @Sql NVARCHAR(MAX) =
                 N'DBCC PAGE (' + QUOTENAME(@DBName, '''') + N', '
               + CAST(@FileId AS NVARCHAR(10)) + N', '
               + CAST(@PageId AS NVARCHAR(10)) + N', '
               + CAST(@PrintMode AS NVARCHAR(10)) + N') WITH TABLERESULTS;';

    INSERT INTO #DbccPageOutput (ParentObject, Object, Field, Value)
    EXECUTE (@Sql);

    SELECT [ParentObject], [Object], [Field], [Value]
    FROM #DbccPageOutput;

    DROP TABLE #DbccPageOutput;
    END;
    GO
    ```
21. Create the certificate on the Master database:

    ```
    CREATE CERTIFICATE [attrep_rtm_dbcc_page_cert]
    ENCRYPTION BY PASSWORD = N'choose_your_own_pwd'
    WITH SUBJECT = N'Certificate for rtm_dbcc_page Permissions';
    ```
22. Create a login from the certificate:

    ```
    CREATE LOGIN [attrep_rtm_dbcc_page_login]
    FROM CERTIFICATE [attrep_rtm_dbcc_page_cert];
    ```
23. Add the login to the sysadmin server role:

    ```
    ALTER SERVER ROLE [sysadmin] ADD MEMBER [attrep_rtm_dbcc_page_login];
    ```
24. Add the certificate signature to `[master].[attrep].[rtm_dbcc_page]`:

    ```
    ADD SIGNATURE TO [master].[attrep].[rtm_dbcc_page]
    BY CERTIFICATE [attrep_rtm_dbcc_page_cert]
    WITH PASSWORD = N'choose_your_own_pwd';
    ```

    Information note

    If the stored procedure is recreated, you need to add the signature again.
25. Use an existing login user or create a login user:

    ```
    CREATE LOGIN [username] WITH PASSWORD='password';
    ```
26. Create a user in the master and MSDB databases for the login user:

    `USE master`

    `GO`

    `CREATE USER [username] FOR LOGIN [username];`

    `GO`

    `USE msdb`

    `GO`

    `CREATE USER [username] FOR LOGIN [username];`

    `GO`

    Repeat this step for each database that you want to access with a non sysadmin user.
27. Grant the user the following permissions and roles (in each of the following databases):

    - Master DB:
      - select on sys.fn\_dblog
      - view any definition
      - view server state (should be granted to the login).
      - execute on sp\_repldone
      - execute on sp\_replincrementlsn
      - execute on sp\_addpublication
      - execute on sp\_addarticle
      - execute on sp\_articlefilter
      - select on [attrep].[split\_partition\_list]
      - execute on [attrep].[rtm\_dump\_dblog]
      - execute on [attrep].[rtm\_position\_1st\_timestamp]
      - execute on [attrep].[rtm\_dbcc\_page]
      - execute on [attrep].[rtm\_check\_file\_exists]

        Information noteThis permission is only required if you performed steps 16-20 above.
    - MSDB DB:
      - select on msdb.dbo.backupset
      - select on msdb.dbo.backupmediafamily
      - select on msdb.dbo.backupfile
    - For the source database:
      - db\_owner ROLE
28. To enable Qlik Talend Data Integration to create the publication without sysadmin authority, set the publish flag and pre-create the log reader job:

    USE master

    EXEC sp\_replicationdboption @dbname = '<databaseName>', @optname = 'publish', @value = 'true'

    EXEC <databaseName>.sys.sp\_addlogreader\_agent
