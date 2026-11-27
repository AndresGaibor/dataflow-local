---
title: "Using an account without the superuser role"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/PostgreSQL/postgresql-source-nonsu.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "PostgreSQL"]
---

# Using an account without the superuser role

If you are not using an account with the superuser role (or the rds\_superuser role when working with Amazon Aurora or Amazon RDS), you need to create several objects to capture Data Definition Language (DDL) events. Create these objects in the selected account and then create a trigger in the master user account.

Information noteUsing an account with the superuser role with Google Cloud SQL for PostgreSQL requires Data Movement gateway 2024.11.14 or later.

To do this:

1. Choose a schema where you want the objects to be created. The default schema is public. Ensure that the schema exists and is accessible by the non-privileged account.
2. Create the table attrep\_ddl\_audit by running the following command:

   ```
   create table <objects_schema>.attrep_ddl_audit
   (
   c_key    bigserial primary key,
   c_time   timestamp,    -- Informational
   c_user   varchar(64),  -- Informational: Current_user
   c_txn    varchar(16),  -- Informational: Current transaction
   c_tag    varchar(24),  -- Either 'CREATE TABLE' or 'ALTER TABLE' or 'DROP TABLE'
   c_oid    integer,      -- For future use - TG_OBJECTID
   c_name   varchar(64),  -- For future use - TG_OBJECTNAME
   c_schema varchar(64),  -- For future use - TG_SCHEMANAME. For now, holds the current_schema
   c_ddlqry  text         -- The DDL query associated with the current DDL event
   );
   ```
3. Create the function attrep\_intercept\_ddl by running the following command:

   ```
   CREATE OR REPLACE FUNCTION <objects_schema>.attrep_intercept_ddl()
     RETURNS event_trigger
   LANGUAGE plpgsql
     AS $$
     declare _qry text;
   BEGIN
     if (tg_tag='CREATE TABLE' or tg_tag='ALTER TABLE' or tg_tag='DROP TABLE') then
            SELECT current_query() into _qry;
            insert into <objects_schema>.attrep_ddl_audit
            values
            (
            default,current_timestamp,current_user,cast(TXID_CURRENT()as varchar(16)),tg_tag,0,'',current_schema,_qry
            );
            delete from <objects_schema>.attrep_ddl_audit;
   end if;
   END;
   $$;
   ```
4. If you are logged in with a non-privileged account, log out of the non-privileged account and log in with an account that has the superuser role (or the rds\_superuser role when working with Amazon Aurora or Amazon RDS) assigned to it.

   Information note

   If the attrep\_intercept\_ddl stored procedure is not being created in the default schema, you need to specify the schema name in the Create DDL artifacts in schema field in the PostgreSQL connector settings.

   For more information on the replication configuration parameters, see the PostgreSQL Help.
5. Create the event trigger attrep\_intercept\_ddl by running the following command:

   CREATE EVENT TRIGGER attrep\_intercept\_ddl ON ddl\_command\_end

   EXECUTE PROCEDURE <objects\_schema>.attrep\_intercept\_ddl();
6. Grant the following permissions to the non-privileged account:

   - GRANT INSERT ON attrep\_ddl\_audit to <non-privileged-user>;
   - GRANT DELETE ON attrep\_ddl\_audit to <non-privileged-user>;
   - GRANT USAGE ON attrep\_ddl\_audit\_c\_key\_seq TO <non-privileged-user>;
   - When working with PostgreSQL on-premises, Microsoft Azure Database for PostgreSQL, Google Cloud SQL for PostgreSQL, or Google Cloud AlloyDB for PostgreSQL, grant the following permission:

     ALTER ROLE <non-privileged-user> WITH REPLICATION;
   - When working with Amazon RDS for PostgreSQL or Amazon Aurora, grant the following permission:

     GRANT rds\_replication to <non-privileged-user>;
7. Grant SELECT permission to the user:

   GRANT SELECT ON ALL TABLES IN SCHEMA <SCHEMA \_NAME> TO <non-privileged-user>;
8. Grant usage on the schema to the user:

   GRANT USAGE ON SCHEMA <SCHEMA\_NAME> TO <non-privileged-user>;
