---
title: "Connecting to databases"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Landing/connecting-data-source-dmg.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources"]
---

# Connecting to databases

The following database sources are supported in Qlik Talend Data Integration. Data moved to the target platform is kept up-to-date using CDC (Change Data Capture) technology, or with scheduled reloads of the entire source data. When working with Data Movement gateway, CDC occurs in real time. When working without Data Movement gateway, CDC occurs according to a user-defined schedule.

In certain use cases, when configuring the connection to your source database, you also need to select which Data Movement gateway to use to access the source. If your use case does require a Data Movement gateway, make sure that a Data Movement gateway has been set up for accessing the selected data source, and that the required driver is installed on the Data Movement gateway server. Note that Data Movement gateway is not supported with a Qlik Talend Cloud Starter subscription and might be optional with other subscriptions, depending on your use case and data source.

For information about when Data Movement gateway is required, see [*When is Data Movement gateway required?*](../../Gateways/replication-gateway.htm#top).

Information noteWhen you connect to data sources, you might need to add underlying Qlik Cloud IP addresses to your allowlist. For more information, see [*Allowlisting domains and IP addresses*](../../Introduction/qlik-cloud-dns-ip.htm).

## Connecting to a database

To connect to a database

1. Open the Create connection dialog by doing one of the following:

   - In Create, click Data connection.
   - In Connections, click Create connection.
   - In the Select source connection screen of the onboarding wizard, click Create connection.
2. Locate the database you want to connect to by doing one of the following:

   - Start typing the database name in the search box to show a list of matching connections.
   - Select Database in the Category list and Source from the Type list to shown only database sources.
   - Select from recently used connectors in the Recently used tab.
3. Click the connector name to open the connection settings.

For instructions on configuring your connector, find your connector in the list below and click the link.

1. The first step of connecting to a SaaS application is to add a connection to the data source. You can do this in several ways.

   - In Connections, click Create connection.
   - Click Create connection where source connections are listed (for example, in the data task setup wizard).

   Select Database in the Category list and Source in the Type list to filter the list of connectors to databases.

   You can also select from recently used connectors.
2. Select which database to connect to. For instructions on setting up your connector, find your connector in the list below and click the link.

![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/amazon-aurora.png)

### [Amazon Aurora MySQL](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/MySQL/MySQL-source.htm)

![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/amazon-aurora.png)

### [Amazon Aurora PostgreSQL](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/PostgreSQL/postgresql-source.htm)

![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/dynamo-square.png)

### [Amazon RDS for MySQL](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/MySQL/MySQL-source.htm)

![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/dynamo-square.png)

### [Amazon RDS for Oracle](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/Oracle/Oracle-source.htm)

![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/dynamo-square.png)

### [Amazon RDS for PostgreSQL](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/PostgreSQL/postgresql-source.htm)

![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/amazon-s3-square.png)

### [*Amazon S3*](../SourcesConnections/Connecting-Amazon-S3.htm)

![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/google_cloud_sql.png)

### [Google Cloud SQL for MySQL](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/MySQL/MySQL-source.htm)

![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/ibmdb2.png)

### [IBM DB2 for iSeries](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/IBM4DB2-iseries/IBM4DB2-iseries-source.htm)

![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/ibmdb2.png)

### [IBM DB2 for z/OS](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/IBM4DB2-zos/IBM4DB2-zos-source.htm)

![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/ibmdb2.png)

### [IBM DB2 for LUW](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/IBM4DB2-luw/IBM4DB2-luw-source.htm)

![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/mariadb.png)

### [MariaDB](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/MySQL/MySQL-source.htm)

![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/azure_sql-square.png)

### [Microsoft Azure for MySQL](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/MySQL/MySQL-source.htm)

![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/azure_sql-square.png)

### [Microsoft Azure for PostgreSQL](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/PostgreSQL/postgresql-source.htm)

![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/mssql-square.png)

### [Microsoft SQL Server (Microsoft CDC-based)](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/AzureSQLMSCDC/SQLServer-DB-source.htm)

![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/mssql-square.png)

### [Microsoft SQL Server (log-based)](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/SQLServer/sqlserver-source.htm)

![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/mysql-square.png)

### [MySQL](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/MySQL/MySQL-source.htm)

![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/oracle-square.png)

### [Oracle](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/Oracle/Oracle-source.htm)

![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/oracle-square.png)

### [Oracle Cloud](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/Oracle/Oracle-source.htm)

![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/percona-square.png)

### [Percona Server for MySQL](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/MySQL/MySQL-source.htm)

![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/postgres-square.png)

### [PostgreSQL](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/PostgreSQL/postgresql-source.htm)

![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/teradata-square.png)

### [Teradata](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/Teradata/Teradata-source.htm)
