---
title: "Google Cloud Storage"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/TargetConnections/google-storage-target.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to targets", "Connecting to cloud storage"]
---

# Google Cloud Storage

Google Cloud Storage can be used as:

- A cloud staging area when using Databricks as a data pipeline target. The cloud staging area is where data and changes are staged before being applied and stored.
- A target in a replication task.

  - For an explanation of how to replicate data to Google Cloud Storage with Standard, Premium, and Enterprise subscriptions, see [*Landing data in a data lake with a Standard, Premium, or Enterprise subscription*](../Replicating/landing-datalakes.htm).
  - For an explanation of how to replicate data to Google Cloud Storage with the Starter subscription, see [*Replicating data with a Qlik Talend Cloud Starter subscription*](../Replicating/replicating-starter-subscription.htm).

## Limitations and considerations

The following limitations apply:

- Full LOB Mode is not supported.
- Database names, schema names, or table names containing slash (/) or backslash (\) characters are not supported.

## Prerequisites

The JSON credentials specified in the connector settings must be for an account that has read and write access to the specified bucket.

## Setting Google Cloud Storage connection properties

To configure the connector, do the following:

1. In Connections, click Create connection.
2. Select the Google Cloud Storage  target connector and then provide the following settings:

#### Data target

Data gateway: Select the Data Movement gateway that will be used to test the connection to Google Cloud Storage. This should be the same Data Movement gateway deployed to land data from the data source.

#### Connection properties

- Service account key:
  The JSON credentials for the service account key with read and write access to the Google Cloud Storage bucket. Click Upload and select the JSON file with the service account key.

  Information noteThe specified account key must have read and write access to the specified bucket and folder.
- Bucket name: The Google Cloud Storage bucket.

#### Internal properties

Internal properties are for special use cases and are therefore not exposed in the dialog. You should only use them if instructed by Qlik Support.

Use the ![Create new](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) and ![Cancel](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin.svg) buttons to the right of the fields to add or remove properties as needed.

#### Name

The display name for the connection.

## Data type mapping

The following table shows the default mapping from Qlik Cloud data types to Google Cloud Storage data types.

Information noteThe data type mappings are only relevant if the [Create metadata files in the target folder](../Replicating/landing-datalakes-settings.htm#Metadata) option in the "Land data in data lake" task settings is enabled.

### Mapping from Qlik Cloud data types to Google Cloud Storage

Qlik Cloud and Google Cloud Storage data types

| Data Movement gateway data types | Google Cloud Storage Target data types |
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
- [Databricks target](databricks-target.htm)
