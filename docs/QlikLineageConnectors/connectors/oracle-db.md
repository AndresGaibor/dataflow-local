---
title: "Oracle DB"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikLineageConnectors/connectors/oracle-db.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Delivering data and lineage for analytics", "Extracting lineage data with Qlik Lineage Connectors", "Qlik Lineage Connectors"]
---

# Oracle DB

Expand/Collapse all

# Oracle DB

Used to connect to Oracle Database Services.

Connection string: Enter the parts of your connection string. Use the Add new button to create an additional entry to the connection string.

Connector Server Aliases: Used to fully inform Qlik Lineage Connectors of the different ways of referring to the data source.

Test: Performs a control of the connection string and verifies the ability to connect to Oracle.

Full list of connector fields

Add an Oracle DB connector

| Field | Default or example input |
| --- | --- |
| System ID | Id |
| System name | Name |
| Description | Description (optional) |
| Connection string | Data Source=(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=10.76.135.70)(PORT=1539))(CONNECT\_DATA=(SERVER=DEDICATED)(SERVICE\_NAME=XE)));User Id=SYSTEM;Password=password; |
| Connector Server Aliases | |
| System | ID |
| Server Name | mssql01-prod |
| Fully Qualified Domain Name | mssql01-prod.company.com |
| IP | 123.456.789.123 |
| DNS Nane | mssql01-prod.company.com;mssql02-prod.company.com; |

## Oracle DB rules

Extract Tables: When enabled, Qlik Lineage Connectors gathers tables and fields definitions from the system table, together with some metadata surrounding them.

- Include System Tables: Add Oracle-specific system tables to the overview.

Extract Views: When enabled, Qlik Lineage Connectors goes through the defined views in the database, and parses the definitions.

- Include System Views: Include Oracle-specific system views in the overview.
- Create view dependencies: If enabled, extract views not only gather the output from said views, but also the internal lineage and creates connections to the raw tables used in each view.

Extract Materialized Views: When enabled, Qlik Lineage Connectors goes through the defined materialized views in the database and parses the definitions.

- Create materialized view dependencies: If enabled, Qlik Lineage Connectors parses the internal lineage and creates connections to the raw tables used in each view.

Schema Filter: The schema filter is used to decide what schemas to include. Star selection is allowed for wildcard support.

Full list of rule fields

Add an Oracle DB rule

| Field | Default or example input |
| --- | --- |
| Select rule type | Database rule |
| Name | Enter a name for this rule |
| Description | Description (optional) |
| Schema filter | SYSTEM.\*; ... |
| Rule priority | Enter a processing priority for this rule |

## Folder Alias

A folder alias will synchronize the different references that a connector may read from. For example, an application may refer to a folder as \\mssql01-prod\sources but in a script it is referred to as \\mssql01-prod.company.com\sources. In this case, the two different references point to the same folder, but it will not appear like that in the lineage graphs. By adding the alias, the resource name will be synchronized, and the graphs will reconcile.
