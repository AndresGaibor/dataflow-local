---
title: "Azure Data Lake Storage"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/TargetConnections/adls-target.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to targets", "Connecting to cloud storage"]
---

# Azure Data Lake Storage

Azure Data Lake Storage can be used as:

- A cloud staging area when using Databricks, Microsoft Fabric or Azure Synapse Analytics as a data pipeline target. The cloud staging area is where data and changes are staged before being applied and stored.
- A target in a replication task.

  - For an explanation of how to replicate data to Azure Data Lake Storage with Standard, Premium, and Enterprise subscriptions, see [*Landing data in a data lake with a Standard, Premium, or Enterprise subscription*](../Replicating/landing-datalakes.htm).
  - For an explanation of how to replicate data to Azure Data Lake Storage with the Starter subscription, see [*Replicating data with a Qlik Talend Cloud Starter subscription*](../Replicating/replicating-starter-subscription.htm).

## Limitations and considerations

The following limitations apply:

- Full LOB Mode is not supported.
- Database names, schema names, or table names containing slash (/) or backslash (\) characters are not supported.

## Storage permissions

The Azure Active Directory tenant specified in the connector settings must be granted the following ADLS Gen2 storage permissions.

- On the storage container: LIST
- On the storage directory: READ, WRITE and DELETE
- In the Access Control (IAM) settings for the ADLS Gen2 file system, assign the “Storage Blob Data Contributor” role to Replicate (AD App ID). It may take a few minutes for the role to take effect.

## Setting Azure Data Lake Storage connection properties

To configure the connector, do the following:

1. In Connections, click Create connection.
2. Select the Azure Data Lake Storage  target connector and then provide the following settings:

### Data Target

Data gateway: Select the Data Movement gateway that will be used to test the connection to ADLS. This should be the same Data Movement gateway deployed to land data from the data source.

### Connection properties

- Storage Account

  Name of the storage account.
- Container name

  Name of the container to use as cloud staging area.
- Azure Active Directory Tenant ID

  Tenant ID of the subscription in Azure Active Directory.
- Azure Application Registration Client ID

  Client ID of the application in Azure Active Directory.
- Azure Application Registration Secret

  Secret of the application in Azure Active Directory

### Name

The display name for the connection.

## Data type mapping

The following table shows the default mapping from Qlik Cloud data types to Azure Data Lake Storage data types.

Information noteThe data type mappings are only relevant if the [Create metadata files in the target folder](../Replicating/landing-datalakes-settings.htm#Metadata) option in the "Land data in data lake" task settings is enabled.

### Mapping from Qlik Cloud data types to Azure Data Lake Storage

Qlik Cloud and Azure Data Lake Storage data types

| Qlik Cloud data types | Azure Data Lake Storage Target data types |
| --- | --- |
| DATE | DATE |
| TIME | TIME |
| DATETIME | DATETIME |
| BYTES | BYTES (length) |
| BLOB | BLOB |
| REAL4 | REAL4 (7) |
| REAL8 | REAL8 (14) |
| INT1 | INT1 (3) |
| INT2 | INT2 (5) |
| INT4 | INT4 (10) |
| INT8 | INT8 (19) |
| UINT1 | UINT1 (3) |
| UINT2 | UINT2 (5) |
| UINT4 | UINT4 (10) |
| UINT8 | UINT8 (20) |
| NUMERIC | NUMERIC (p,s) |
| STRING | STRING (Length) |
| WSTRING | WSTRING (Length) |
| CLOB | CLOB |
| NCLOB | NCLOB |
| BOOLEAN | BOOLEAN (1) |

### Mapping from Qlik Cloud data types to Parquet

When Parquet is set as the file format, due to the limited number of data types supported by Parquet, the data type mappings will be as follows:

Parquet data type mappings

| Qlik Cloud Data Type | Parquet Primitive Type | Logical Type |
| --- | --- | --- |
| BOOLEAN | BOOLEAN |  |
| INT1 | INT32 | INT(8, true) |
| INT2 | INT32 | INT(16, true) |
| INT4 | INT32 |  |
| INT8 | INT64 |  |
| UINT1 | INT32 | INT(8, false) |
| UINT2 | INT32 | INT(16, false) |
| UINT4 | INT64 |  |
| UINT8 | INT64 | INT(64, false) |
| REAL4 | FLOAT |  |
| REAL8 | DOUBLE |  |
| NUMERIC | FIXED\_LEN\_BYTE\_ARRAY (16) | DECIMAL (precision, scale) |
| STRING | BYTE\_ARRAY | STRING |
| WSTRING | BYTE\_ARRAY | STRING |
| BYTES | BYTE\_ARRAY |  |
| BLOB | BYTE\_ARRAY |  |
| CLOB | BYTE\_ARRAY | STRING |
| NCLOB | BYTE\_ARRAY | STRING |
| DATE | INT32 | DATE |
| TIME | INT32 | TIME (UTC=true, unit=MILLIS) |
| DATETIME | INT64 | TIMESTAMP (UTC=true, unit=MICROS) |

## Learn more

- [Landing data in a data lake](../Replicating/landing-datalakes.htm)
- [Microsoft Fabric target](fabric-target.htm)
- [Azure Synapse Analytics target](azure-target.htm)
- [Databricks target](databricks-target.htm)
