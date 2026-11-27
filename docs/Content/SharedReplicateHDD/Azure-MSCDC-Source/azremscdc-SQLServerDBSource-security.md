---
title: "Required permissions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/Content/SharedReplicateHDD/Azure-MSCDC-Source/azremscdc-SQLServerDBSource-security.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "Microsoft SQL Server (Microsoft CDC based)"]
---

# Required permissions

This topic describes the permissions the user specified in the connector settings must be granted on the source database.

## Running with the db\_owner role on Azure SQL Managed Instance

Information noteThese permissions are relevant for Azure SQL Managed Instance only. When running with the db\_owner role on Azure SQL Database, no other permissions are required.

If the user is a member of the db\_owner database role, the following permissions must be granted:

- On the master database:

  - grant VIEW ANY DEFINITION
  - grant VIEW SERVER STATE
- On the MSDB database:

  - grant SELECT ON SYSJOBACTIVITY
  - grant SELECT ON SYSJOBS

## Running without the db\_owner role

If the user is not a member of the db\_owner database role, the following permissions must be granted on the source database:

- grant VIEW DATABASE STATE
- grant SELECT

Information noteWhen running without the db\_owner role, MS-CDC cannot be enabled automatically and must therefore be enabled manually. To prevent moving errors, you must also clear the Enable MS-CDC on all captured tables check box in the connection properties before running the task. For more information, see [*Microsoft SQL Server (Microsoft CDC based)*](../../../../Sense_Hub/DataIntegration/SourcesConnections/AzureSQLMSCDC/SQLServer-DB-source.htm)
