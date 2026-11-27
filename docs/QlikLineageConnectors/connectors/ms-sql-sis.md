---
title: "Microsoft SQL Server Integration Services (SSIS)"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikLineageConnectors/connectors/ms-sql-sis.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Delivering data and lineage for analytics", "Extracting lineage data with Qlik Lineage Connectors", "Qlik Lineage Connectors"]
---

# Microsoft SQL Server Integration Services (SSIS)

Expand/Collapse all

# Microsoft SQL Server Integration Services (SSIS)

The Microsoft SSIS connector is used to connect data sources and transformations on field level found within SSIS packages. This can be both how they are used internally within the connector, as well as externally to data from other connectors in the Qlik Lineage Connectors container.

Package Deployment Model

There are two kinds of deployment model:

- Project Deployment Model

  When a project, containing packages and parameters, is deployed to the SSISDB catalog on an instance of SQL Server. Default deployment model since MS SQL Server 2012.
- Directory

  When projects and packages are not accessible from the server of deployment, a directory holding either entire projects (\*.Ispac) or separate packages (\*.Dtsx) can be used.

Information noteNote: There is also Legacy Project Deployment Model (Not supported). This is the default deployment model before MS SQL Server 2012.

Connection string:

Required when using Project Deployment Model. This is the connection string used to connect to the MS SQL Server where the projects are deployed. Use integrated security only if the Qlik Lineage Connectors service account has sufficient permissions. User needs to be member of either 'ssis\_admin' on SSISDB or have the role 'sysadmin'.

Project/Package Storage Path:

Required when using Directory Deployment Model. All project files (\*.Ispac) and separate package files (\*.Dtsx) found in directory, or any of its subdirectories, will be included.

Test: Depending on Deployment Model the test will do one of the following:

- When using Project Deployment Model, a control of the connection string is performed and verifies the ability to connect to SSIS on MS SWL Server to read and extract projects and packages.

Project Deployment Model Test status

![The status of items in the Project Deployment Model.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/NodeGraph/ui-NodeGraphTD-24.png "Click to view full size")

- When using Directory, a control is performed to ensure read access to path specified.

Figure 25 - Directory test status

![The status of items in the Directory.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/NodeGraph/ui-NodeGraphTD-25.png "Click to view full size")

Full list of connector fields

Add an SSIS connector

| Field | Default or example input |
| --- | --- |
| System ID | ID |
| System name | Name |
| Description | Description (optional) |
| Deployment model | Select category |
| Connection string | data source=localhost; initial catalog=AdventureWorks;Integrated Security=SSPI; |
| Connector Server Aliases | |
| System | ID |
| Server Name | mssql01-prod |
| Fully Qualified Domain Name | mssql01-prod.company.com |
| IP | 123.456.789.123 |
| DNS Name | mssql01-prod.company.com;mssql02-prod.company.com; |

## Microsoft SSIS rules

Include Folders Filter: Specify specific folders to include in current rule.

Include Projects Filter: Specify specific projects to include in current rule.

Include Packages Filter: Specify specific packages to include in current rule.

Exclude Filter: Specify specific keywords used to exclude Folders/Projects/Packages.

Information noteInclude filters are treated with a logical AND. For example, if a site and project filter is used, only the matching projects within the matching sites are included. If an include filter is left empty, all matches will be included. All filters can be typed as specific strings or as wildcard patterns. If multiple filters are wanted, they can be separated by a semicolon.

Full list of rule fields

Add an SSIS rule

| Field | Default or example input |
| --- | --- |
| Select rule type | SSIS rule |
| Name | Enter a name for this rule |
| Description | Description (optional) |
| Include folders filter | ETL; Extract\*; Transform\* |
| Include projects filter | ETL; Extract\*; Transform\* |
| Include packages filter | ETL; Extract\*; Transform\* |
| Exclude filter | Archive; Test\* |
| Rule priority | Enter a processing priority for this rule |

## Folder Alias

A folder alias will synchronize the different references that a connector may read from. For example, an application may refer to a folder as \\mssql01-prod\sources but in a script it is referred to as \\mssql01-prod.company.com\sources. In this case, the two different references point to the same folder, but it will not appear like that in the lineage graphs. By adding the alias, the resource name will be synchronized, and the graphs will reconcile.
