---
title: "Setting up Microsoft SQL Server for replication"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/Content/SharedReplicateHDD/SQLServer-Source/sqlserver_replication.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "Microsoft SQL Server (log based)", "Preparing the Microsoft SQL Server database for CDC"]
---

# Setting up Microsoft SQL Server for replication

You need to enable your Microsoft SQL Server database for MS-REPLICATION.

In the Microsoft SQL Server’s Management Studio, follow the instructions provided by the Configure Distribution wizard to set up replication or see the Microsoft SQL Server documentation.

To open the wizard from Microsoft SQL Server:

1. In the Microsoft SQL Server Management Studio, right-click the Replication folder and select Configure Distribution.

   The Configure Distribution wizard opens.
2. Make the following selections:

   In the Distributor step, select <Microsoft SQL Server Name> will act as its own distributor; Microsoft SQL Server will create a distribution database and log.
