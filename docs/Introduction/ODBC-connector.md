---
title: "ODBC databases"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/ODBC_Connector_help/Content/Connectors_ODBC/Introduction/ODBC-connector.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics"]
---

# ODBC databases

The Qlik ODBC Connector Package contains database connectors that enable Qlik Sense to efficiently load data into an application from databases accessed through supported ODBC (Open Database Connectivity) drivers.

Information noteIndustry-accepted best practices must be followed when using or allowing access through the ODBC Connector. Administrators must follow The Principle of Least Privilege when setting up source database privileges and permissions.

Information note

The ODBC Connector Package does not support single sign-on (SSO)

## Qlik Data Gateway - Direct Access

All supported ODBC data sources can be used with Direct Access gateway.

Connectors that support Direct Access gateway (ODBC-based and others) appear twice in the Create data connection dialog. Once with just the data source name and once with the data source name followed by (via Direct Access gateway). You can quickly filter the connectors list to show only connectors that support Direct Access gateway, by typing "Access" into the Data connectors search box.

Qlik Data Gateway - Direct Access eliminates the need to open inbound firewall ports, allowing Qlik Cloud applications to securely access firewalled data. If your enterprise data source is located behind a firewall and can be accessed via Qlik Data Gateway - Direct Access, it is strongly recommended to connect to it via the Direct Access gateway.

Information noteUsers that need to leverage gateway-enabled data connections must have the Can Consume Data permission for the space in which the gateway resides.

For more information on Qlik Data Gateway - Direct Access, see [Data gateways](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/direct-access-gateway.htm).

## Databases

The following databases are supported with ODBC drivers.

- [*Amazon Athena*](../Athena/Athena-connector.htm)
- [*Amazon Redshift*](../Redshift/Redshift-connector.htm)
- [*Apache Drill*](../ApacheDrill/ApacheDrill-connector.htm)
- [*Apache Hive*](../ApacheHive/Apache-hive-connector.htm)
- [*Apache Phoenix*](../ApachePhoenix/Apache-Phoenix-connector.htm)
- [*Apache Spark*](../ApacheSPARK/ApacheSPARK-connector.htm)
- [*Azure SQL Database*](../MS-Azure/MS-Azure-connector.htm)
- [*Azure Synapse Analytics*](../MS-AzureSynapse/MS-AzureSynapse-connector.htm)
- [*Cloudera Impala*](../ClouderaImpala/Cloudera-impala-connector.htm)
- [*Databricks*](../Databricks/Databricks-connector.htm)
- [*DynamoDB*](../DynamoDB/DynamoDB-connector.htm)
- [*Google BigQuery*](../GoogleBigQuery/Google-BigQuery-Connector.htm)
- [*Microsoft SQL Server*](../SQLServer/SQL-Server-connector.htm)
- [*MongoDB*](../Mongo/Mongo-connector.htm)
- [*MySQL Enterprise Edition*](../MySQL/MySQL-connector.htm)
- [*ODBC (via Direct Access gateway)*](../ODBC-DrectAccess/ODBC.htm)
- [*Oracle*](../Oracle/Oracle-connector.htm)
- [*PostgreSQL*](../PostgresSQL/PostgresSQL-connector.htm)
- [*Presto*](../Presto/Presto-connector.htm)
- [*ServiceNow*](../ServiceNow/ServiceNow-connector.htm)
- [*Snowflake*](../Snowflake/Snowflake-connector.htm)
- [*Teradata*](../Teradata/Teradata-connector.htm)

Related learning:

- [Loading Data from a Database](/lnk/Loading_data_from_database_QS)
