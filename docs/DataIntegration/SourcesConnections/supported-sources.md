---
title: "Supported source databases and versions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/supported-sources.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases"]
---

# Supported source databases and versions

The table below lists which source database versions are supported by Data Movement gateway and also specifies which connectors need to be configured to connect to the database.

Information noteThe supported database versions always reflect the capabilities of the latest Data Movement gateway version, regardless of whether or not you are using Data Movement gateway to access your data source(s). For information on the versions supported (or no longer supported) with the latest Data Movement gateway version ,see [*Upgrading and uninstalling Data Movement gateway*](../../Gateways/dm-gateway-upgrading.htm)

Supported data sources

| Connector | Supported subscription | Supported without Data Movement gateway | Data source | Supported versions | Source type |
| --- | --- | --- | --- | --- | --- |
| IBM DB2 for iSeries  For more information, see [*IBM DB2 for iSeries*](IBM4DB2-iseries/IBM4DB2-iseries-source.htm). | Standard, Premium, and Enterprise | No | IBM DB2 for iSeries | 7.3, 7.4, 7.5 | Relational database |
| IBM DB2 for LUW  For more information, see [*IBM DB2 for LUW*](IBM4DB2-luw/IBM4DB2-luw-source.htm). | Standard, Premium, and Enterprise | No | IBM DB2 for LUW | 11.1, 11.5 | Relational database |
| IBM DB2 for z/OS  For more information, see [*IBM DB2 for z/OS*](IBM4DB2-zos/IBM4DB2-zos-source.htm). | Enterprise | No | IBM DB2 for z/OS | **DB2:**  12, 12.1, 13.1  **IBM z/OS:**  2.5, 3.2 | Mainframe |
| Microsoft SQL Server (log based)  For more information, see [*Microsoft SQL Server (log based)*](SQLServer/sqlserver-source.htm). | Standard, Enterprise, and Premium | No | Microsoft SQL Server | 2016, 2017, 2019, 2022, 2025 | Relational database |
| Microsoft SQL Server (Microsoft CDC based)  For more information, see [*Microsoft SQL Server (Microsoft CDC based)*](AzureSQLMSCDC/SQLServer-DB-source.htm). | All | Yes | - Microsoft SQL Server - Microsoft Azure SQL Managed Instance - Microsoft Azure SQL Database - Amazon RDS for SQL Server | 2016, 2017, 2019, 2022, 2025 | Relational database |
| MySQL  For more information, see [*MySQL*](MySQL/MySQL-source.htm). | All | Yes | - MySQL - Amazon Aurora for MySQL - Amazon RDS for MySQL - Google Cloud SQL for MySQL - Percona | 8.0, 8.4 | Relational database |
|  | - MariaDB | 10.6 to 10.11, 11.4, 11.8 | Relational database |
|  | - Amazon RDS for MariaDB | 10.6 to 10.11, 11.4, 11.8 | Relational database |
| Oracle  For more information, see [*Oracle*](Oracle/Oracle-source.htm). | Standard, Enterprise, and Premium | No | - Oracle - Oracle Amazon RDS for Oracle - Oracle on Oracle Cloud | 19.x, 21c, 23ai  Information note Oracle 23ai is certified with Oracle Standard Edition and TDE encryption only.  Warning noteIf you set the Oracle compatibility parameter, make sure you specify a version supported by Data Movement gateway. For example, if you are working with version 21c, you cannot set an earlier version as the compatibility version. | Relational database |
| PostgreSQL  For more information, see [*PostgreSQL*](PostgreSQL/postgresql-source.htm). | All | Yes | - PostgreSQL - Amazon RDS for PostgreSQL - Google Cloud SQL for PostgreSQL - Google Cloud AlloyDB for PostgreSQL | 14.x, 15.x, 16.x, 17.x | Relational database |
|  | - Amazon Aurora Cloud for PostgreSQL | 14.x, 15.x, 16.x, 17.x | Relational database |
|  | - Microsoft Azure Database for PostgreSQL - Flexible Server | N/A | Relational database |
| Teradata  For more information, see [*Teradata*](Teradata/Teradata-source.htm). | All | No | Teradata Vantage | 17.x, 20.x | Relational database |
