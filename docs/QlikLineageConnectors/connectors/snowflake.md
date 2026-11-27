---
title: "Snowflake"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikLineageConnectors/connectors/snowflake.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Delivering data and lineage for analytics", "Extracting lineage data with Qlik Lineage Connectors", "Qlik Lineage Connectors"]
---

# Snowflake

Expand/Collapse all

# Snowflake

This connector is used to connect to Snowflake databases.

The connector needs a running or an auto-starting Snowflake Virtual Warehouse. It uses ACCOUNT\_USAGE from the internal imported ‘SNOWFLAKE’ metadata database and INFORMATION\_SCHEMA from each database available.

For ease of setup, it is recommended to use the ACCOUNTADMIN role as this will provide access to all relevant tables, but a custom role can be created.

Account: Snowflake account name

Host: Full host name of the Snowflake instance

User: Snowflake username

Password: Snowflake password

Role: Queries will be executed by the user using this Snowflake role

Warehouse: Snowflake computing warehouse to use when running queries

Full list of connector fields

Add a Snowflake connector

| Field | Default or example input |
| --- | --- |
| System ID | ID |
| System name | Name |
| Description | Description (optional) |
| Account | account |
| Host | account.west-europe.azure.snowflakecomputing.com |
| User | user |
| Password | \*\*\*\* |
| Role | AccountAdmin |
| Warehouse | Default |
| Connector Server Aliases | |
| System | ID |
| Server Name | mssql01-prod |
| Fully Qualified Domain Name | mssql01-prod.company.com |
| IP | 123.456.789.123 |
| DNS Name | mssql01-prod.company.com;mssql02-prod.company.com; |

## Snowflake rules

Extract Tables: When enabled, Qlik Lineage Connectors gather tables and fields definitions from the system table, together with some metadata surrounding them.

Extract Views: When enabled, Qlik Lineage Connectors go through the defined views in the database, and parses the definitions.

- Create view dependencies: If enabled, extract views not only gather the output from said views, but also the internal lineage and creates connections to the raw tables used in each view.

Extract Procedures: When enabled, Qlik Lineage Connectors go through the defined procedures in the database, and parses the definitions.

- Create procedure dependencies: If enabled, Qlik Lineage Connectors analyse the SQL statements in the procedure definitions and generates lineage on field level to other database entities.

Extract Functions: When enabled, Qlik Lineage Connectors go through the defined functions in the database, and parses the definitions.

- Create function dependencies: If enabled, Qlik Lineage Connectors analyse the SQL statements in the function definitions and generates lineage on field level to other database entities.

Include Databases: A semicolon separated list of databases to act upon with the above ruleset. Does not support wildcard.

Schema Filter: The schema filter is used to decide what schemas to include. For example, you could use the definition \*.dbo.\* ; AdventureWorks.Sales.\* to gather all tables from the dbo schema of all your databases, but also the tables from the Sales schema on the AdventureWorks catalog.

Full list of rule fields

Add a Snowflake rule

| Field | Default or example input |
| --- | --- |
| Select rule type | Database rule |
| Name | Enter a name for this rule |
| Description | Description (optional) |
| Include databases | Db1; Db2; ... |
| Include filter | AdventureWorks.dbo.\*; ... |
| Exclude filter | AdventureWorks.dbo.\*; ... |
| Rule priority | Enter a processing priority for this rule |

## Folder Alias

A folder alias will synchronize the different references that a connector may read from. For example, an application may refer to a folder as \\mssql01-prod\sources but in a script it is referred to as \\mssql01-prod.company.com\sources. In this case, the two different references point to the same folder, but it will not appear like that in the lineage graphs. By adding the alias, the resource name will be synchronized, and the graphs will reconcile.
