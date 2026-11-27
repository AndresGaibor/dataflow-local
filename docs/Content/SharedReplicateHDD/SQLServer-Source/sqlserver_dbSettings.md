---
title: "Defining Microsoft SQL Server database settings"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/Content/SharedReplicateHDD/SQLServer-Source/sqlserver_dbSettings.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "Microsoft SQL Server (log based)", "Preparing the Microsoft SQL Server database for CDC"]
---

# Defining Microsoft SQL Server database settings

Set the following for the Microsoft SQL Server database(s) you are using as a source:

- From the Object Explorer in the Microsoft SQL Server Management Studio, right click the database and select Properties. In the Options tab, set the Recovery model to Bulk logged or Full. In this mode, the transaction Log is more durable and truncation occurs less frequently.
- Ensure that there is a full database backup for each Microsoft SQL Server database that you are using as a source.
- When creating a connection string, it is possible to use any parameter supported by Microsoft SQL Server. The Microsoft SQL Server system administrator must ensure that the Microsoft SQL Server instance is configured correctly so that the proper authentication credentials are accepted.
- To be able to work with MS-REPLICATION, each of the source tables must have a primary key.
