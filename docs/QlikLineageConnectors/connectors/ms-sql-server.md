---
title: "Microsoft SQL server"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikLineageConnectors/connectors/ms-sql-server.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Delivering data and lineage for analytics", "Extracting lineage data with Qlik Lineage Connectors", "Qlik Lineage Connectors"]
---

# Microsoft SQL server

Expand/Collapse all

# Microsoft SQL server

MSSQL connectors are used to connect to Microsoft SQL server reports.

Connection string: The connection string to your SQL Database.

Connector Server Aliases: Used to fully inform Qlik Lineage Connectors of the different ways of referring to the data source.

Test: Performs a control of the connection string and verifies the ability to connect to SQL.

Full list of connector fields

Add a MSSQL connector

| Field | Default or example input |
| --- | --- |
| System ID | ID |
| System name | Name |
| Description | Description (optional) |
| Connection string | data source=rd-hwl-db-dev-1.rdspace.qliktech.com;initial catalog=AdventureWorks2017;User Id=db\_read;Password=password; |
| Connector Server Aliases |  |
| System | ID |
| Server Name | mssql01-prod |
| Fully Qualified Domain Name | mssql01-prod.company.com |
| IP | 123.456.789.123 |
| DNS Name | mssql01-prod.company.com;mssql02-prod.company.com; |

## Microsoft SQL Server rules

Extract Tables: When enabled, Qlik Lineage Connectors gather tables and fields definitions from the system table, together with some metadata surrounding them.

Extract Views: When enabled, Qlik Lineage Connectors go through the defined views in the database, and parses the definitions.

- Create view dependencies: If enabled, Qlik Lineage Connectors analyze the SQL statements in the view definitions and generates lineage on field level to other database entities.

Extract Procedures: When enabled, Qlik Lineage Connectors go through the defined procedures in the database, and parses the definitions.

- Create procedure dependencies: If enabled, Qlik Lineage Connectors analyzes the SQL statements in the procedure definitions and generates lineage on field level to other database entities.

Extract Functions: When enabled, Qlik Lineage Connectors go through the defined functions in the database, and parses the definitions.

- Create function dependencies: If enabled, Qlik Lineage Connectors analyze the SQL statements in the function definitions and generates lineage on field level to other database entities.

Include Databases: A semicolon separated list of databases to act upon with the above ruleset. Does not support wildcard.

Schema Filter: The schema filter is used to decide what schemas to include. For example, you could use the definition \*.dbo.\* ; AdventureWorks.Sales.\* to gather all tables from the dbo schema of all your databases, but also the tables from the Sales schema on the AdventureWorks catalog.

Full list of rule fields

Add a Microsoft SQL Server rule

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
