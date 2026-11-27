---
title: "Qlik script trace hints"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikLineageConnectors/connectors/qlik-script-tracehints.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Delivering data and lineage for analytics", "Extracting lineage data with Qlik Lineage Connectors", "Qlik Lineage Connectors"]
---

# Qlik script trace hints

Expand/Collapse all

# Qlik script trace hints

When using theQlikView or Qlik Sense connectors to parse log files, Qlik Lineage Connectors will attempt to identify the database type when reading CONNECT TO statements in the Qlik script. Depending on the connection type, it may not be able to identify the database type, but you can add this information via a script.

All referenced resources that Qlik Lineage Connectors detects locally are sent to Qlik Cloud as a Qlik Resource Identifier (QRI). A QRI contains information about the data source type, format or platform the data is stored on, and its canonical path on the network and within that network node.

## Connect trace hint

Sending additional information to Qlik Lineage Connectors is done through a TRACE statement. This command will add a comment to the log file that will be read by Qlik Lineage Connectors. Adding this information will form a more accurate QRI that can be detected across different instance of Qlik Lineage Connectors and other resources accessed directly from Qlik Cloud.

### Trace hint example

The Qlik Lineage Connectors trace hint for additional connection information follows this format:

TRACE !!qlc "Connect" "connection\_name" "default\_database" "default\_schema" "database\_type";
LIB CONNECT TO 'Database\_tenant.region.provider.com';

The trace hint will be added as metadata to the connection and any query following the connect statement will use this hint to enhance the information on each resource.

The trace includes the following elements:

- !!qlc

  This is a flag that informs Qlik Lineage Connectors that the information following is important.
- "Connect"

  This keyword indicates to Qlik Lineage Connectors of additional information for the next CONNECT statement it processes.
- "connection\_name"

  This is the name of the connection. It can either be the machine's address or a descriptive name. This name will group all subsequent SQL queries and is crucial for forming the QRIs that address each resource in the lineage graph. It also helps align data accessed on-premises with Qlik Cloud-based queries, ensuring they refer to the same resources.

  Tip noteUse the database address and, if relevant, the port number.
- "default\_database" and "default\_schema"

  For queries executed after the connect statement, the database and schema details can often be omitted, depending on the database system. This omission is possible because the connection string already contains the necessary database and schema information. Qlik Lineage Connectors will automatically use the specified database and schema for queries that do not explicitly include this information.

  Query without database and schema

  ```
  LIB CONNECT TO ERP_Database';
  SQL SELECT Order, Product, Qty, Amount FROM SalesTable;
  ```

  The database and schema are not provided in the query as it is configured in the connection, or on the database side.

  Query with added trace hint

  ```
  TRACE !!qlc “erp_1.company.com” “PROD” “dbo” “sqlserver”;
  ```

  ```
  LIB CONNECT TO ERP_Database';
  SQL SELECT Order, Product, Qty, Amount FROM SalesTable;
  ```

  Queries that explicitly state the database and/or shcema will take precedence and will not rely on the default values.
- "database\_type"

  Depending on whether the library uses different connection types or relies solely on OLEDB/ODBC, Qlik Lineage Connectors might encounter challenges to correctly identify the database type. To address this, you can manually set the database type, overriding Qlik Lineage Connectors automatic detection.

  Supported value settings

  Athena

  Azure SQL

  Azure Synapse

  Cassandra

  Couchbase

  Databricks

  Drill

  DynamoDB

  GBQ

  Hive

  Impala

  Marketo

  MongoDB

  MySQL

  Oracle

  Phoenix

  PostgreSQL

  Presto

  Redshift

  Salesforce

  SAP BW

  SAP HANA

  SAP SQL

  Snowflake

  SQL Server

  Teradata

  Unknown
