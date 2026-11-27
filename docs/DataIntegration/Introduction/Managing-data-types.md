---
title: "Managing data types"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Introduction/Managing-data-types.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Managing datasets"]
---

# Managing data types

When you change the data type or the data type size of a column, this may have implications on the tasks using the dataset.

Supported data types and conversions vary by target platform. For specific documentation for your target platform , see [*Setting up connections to targets*](../TargetConnections/data-project-connections.htm).

## Understanding the impact of changing a data type

There are two common use cases for changing data type size or switching to a different data type:

- Ingesting data that will not fit into the current data type.
- A requirement for greater numerical accuracy. For example, changing SMALLINT to DECIMAL (p,s).

In most cases, changing a data type will result in an ALTER TABLE operation, thereby preventing data loss. For example, if the previous data type was STRING (25) and the new data type is STRING (50), the data in the column with the new data type will be updated without any issue. However, in some cases, changing a data type will result in the table being dropped and recreated. For example, if the previous column data type is NUMBER and you change it to DATE, the table will be dropped and recreated as converting numbers to dates is not possible. Likewise, if the target platform does not support ALTER table operations (such as Databricks), the table will be dropped and recreated.

There are some cases where it is theoretically possible to alter a table, but because of the underlying complexity, the data task will drop and recreate the table. Finally, there are cases where potential data loss rather than actual data loss will trigger a drop and recreate operation. For example, if you change STRING(25) to STRING(1), data loss will occur if the ingested data does not fit into STRING(1). However, it's possible that STRING(25) will always contain only one character, so in practice no data loss will occur, but the table will still be dropped and recreated due to potential data loss.

## Changes to data types that require the table to be dropped and recreated, regardless of target platform

Changing the following data types will result in the table being dropped and recreated:

- BYTES
- BLOB
- CLOB
- NCLOB

## Target platforms that support changes to data type size without dropping and recreating the table

When working with Snowflake, Google BigQuery, Amazon Redshift, Microsoft SQL Server, and Azure Synapse Analytics, you can change the size of certain data types without the table being dropped and recreated. The following table lists which data types are supported for each of the aforementioned platforms.

| Data type | Snowflake | Google BigQuery | Azure Synapse Analytics | Microsoft SQL Server | Amazon Redshift |
| --- | --- | --- | --- | --- | --- |
| INT1 | No | Yes | Yes | Yes | No |
| INT2 | No | Yes | Yes | Yes | No |
| INT4 | No | Yes | Yes | Yes | No |
| INT8 | No | Yes | Yes | Yes | No |
| REAL4 | No | No | Yes | Yes | No |
| REAL8 | No | No | Yes | Yes | No |
| UINT1 | No | Yes | Yes | Yes | No |
| UINT2 | No | Yes | Yes | Yes | No |
| UNIT4 | No | Yes | Yes | Yes | No |
| UNIT8 | No | Yes | Yes | Yes | No |
| NUMERIC | Yes | Yes | Yes | Yes | No |
| STRING | Yes | Yes | Yes | Yes | Yes |
| WSTRING | No | Yes | Yes | Yes | No |

## Target platforms that support changing data types to STRING without the table being dropped and recreated

When moving data to Microsoft SQL Server and Azure Synapse Analytics, you can change the following data types to STRING, without the table being dropped and recreated:

- BOOLEAN
- DATE
- TIME
- DATETIME
- INT1
- INT2
- INT4
- INT8
- REAL4
- REAL8
- UINT1
- UINT2
- UNIT4
- UNIT8
- NUMERIC
- WSTRING (Supported with Azure Synapse Analytics only)

## Managing JSON data

Qlik introduced support for the JSON data type in 2025. JSON data type support is not available in tasks created before the introduction. In new tasks, columns with JSON data will be converted to the data type specified for the target platform. Data Movement gateway 2024.11.78 or higher is required to discover JSON data type in landing tasks if you are using a client-managed gateway.

When JSON data is converted, these new global transformation rules may be created.

- QLIK\_\_PARSE\_TO\_JSON

  This rule is created in Snowflake projects where landing is loading data to lake landing. The rule is added in the storage task after the landing to parse all JSON columns to JSON in Snowflake.
- QLIK\_\_JSON\_AS\_VARCHAR

  This rule is created in Snowflake projects where the data is landed to Snowflake, and the storage creates Snowflake managed Iceberg tables. The rule converts JSON to Varchar as Iceberg does not support the Variant type.

### Managing existing JSON data in tasks created before JSON data type support was introduced

- If you have existing tasks with JSON, VARIANT or SUPER data in the data platform converted to another data type, for example BLOB, you may want to consider converting columns to the data type used for JSON in the target platform. You can perform this with a transformation rule. This may be required if you need to use new columns together with existing columns in downstream tasks.
- Another option is to convert the columns in the new task to the same data type used in existing data types to maintain backward compatibility.

## Data types in SaaS application sources

When moving data from a SaaS application source, all VARCHAR columns except primary keys are initially created as VARCHAR (1). When the task starts to run, the column length is automatically expanded (to VARCHAR (15), for example) to accommodate the data, eliminating the need for manual intervention.

## Data types in non-materialized datasets

For non-materialized datasets, the data platform determines the column types at runtime. The logical type is only informational and may differ from the actual type.

- To see the final type, check the generated database artifacts.
- To force a type, add an explicit cast in the column expression.
