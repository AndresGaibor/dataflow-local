---
title: "Supported data types"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DirectQuery/data_type_direct_query.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Accessing cloud databases directly with Direct Query"]
---

# Supported data types

The following tables show the database SQL data types that are supported when using Direct Query.

## Supported Amazon Redshift SQL data types

Supported Amazon Redshift SQL data types

| Data types | Viewable | Selectable |
| --- | --- | --- |
| BIGINT | Yes | Yes |
| INTEGER | Yes | Yes |
| SMALLINT | Yes | Yes |
| DECIMAL (p,s) | Yes | Yes |
| NUMERIC (p,s) | Yes | Yes |
| DOUBLE | Yes | Yes |
| DOUBLE PRECISION | Yes | Yes |
| REAL | Yes | Yes |
| FLOAT | Yes | Yes |
| FLOAT4 | Yes | Yes |
| FLOAT8 | Yes | Yes |
| TIME | Yes | Yes |
| DATE | Yes | Yes |
| TIME WITH TIME ZONE | Yes | Yes |
| TIMESTAMP | Yes | Yes |
| TIMESTAMPTZ | Yes | Yes |
| BOOLEAN | Yes | Yes |
| TEXT | Yes | Yes |
| CHARACTER (n) | Yes | Yes |
| VARCHAR (n) | Yes | Yes |
| HLLSKETCH | No | No |
| SUPER | Yes | Yes |
| GEOMETRY | Yes | Yes |
| GEOGRAPHY | Yes | Yes |

## Supported Azure SQL data types

Supported Azure SQL data types

| Data types | Viewable | Selectable |
| --- | --- | --- |
| BIGINT | Yes | Yes |
| BIT | Yes | Yes |
| CHAR  Maximum size is 4096 bytes. | Yes | Yes |
| DATE | Yes | Yes |
| DATETIME | Yes | Yes |
| DATETIME2 | Yes | Yes |
| DATETIMEOFFSET | Yes | Yes |
| DECIMAL | Yes | Yes |
| FLOAT | Yes | Yes |
| GUID | Yes | Yes |
| INT | Yes | Yes |
| MONEY | Yes | Yes |
| NCHAR  Maximum size is 4096 characters. | Yes | Yes |
| NUMERIC | Yes | Yes |
| NVARCHAR  Maximum size is 4096 characters. | Yes | Yes |
| REAL | Yes | Yes |
| ROWVERSION | Yes | Yes |
| SMALLDATETIME | Yes | Yes |
| SMALLINT | Yes | Yes |
| SMALLMONEY | Yes | Yes |
| TIME | Yes | Yes |
| TINYINT | Yes | Yes |
| VARCHAR  Maximum size is 4096 characters. | Yes | Yes |
| XML | Yes | Yes |

## Supported Azure Synapse Analytics data types

Supported Azure Synapse Analytics data types

| Data types | Viewable | Selectable |
| --- | --- | --- |
| BIGINT | Yes | Yes |
| BIT | Yes | Yes |
| CHAR  Maximum size is 4096 bytes. | Yes | Yes |
| DATE | Yes | Yes |
| DATETIME | Yes | Yes |
| DATETIME2 | Yes | Yes |
| DATETIMEOFFSET | Yes | Yes |
| DECIMAL | Yes | Yes |
| FLOAT | Yes | Yes |
| INT | Yes | Yes |
| MONEY | Yes | Yes |
| NCHAR  Maximum size is 4096 characters. | Yes | Yes |
| NUMERIC | Yes | Yes |
| NVARCHAR  Maximum size is 4096 characters. | Yes | Yes |
| REAL | Yes | Yes |
| SMALLDATETIME | Yes | Yes |
| SMALLINT | Yes | Yes |
| SMALLMONEY | Yes | Yes |
| TIME | Yes | Yes |
| TINYINT | Yes | Yes |
| VARCHAR  Maximum size is 4096 characters. | Yes | Yes |

## Supported Databricks SQL data types

Supported Databricks SQL data types

| Data types | Viewable | Selectable |
| --- | --- | --- |
| BIGINT | Yes | Yes |
| INTEGER | Yes | Yes |
| TINYINT | Yes | Yes |
| SMALLINT | Yes | Yes |
| DECIMAL (p,s) | Yes | Yes |
| NUMERIC (p,s) | Yes | Yes |
| DOUBLE | Yes | Yes |
| FLOAT | Yes | Yes |
| TIMESTAMP | Yes | Yes |
| DATE | Yes | Yes |
| BINARY | Yes | Yes |
| BOOLEAN | Yes | Yes |
| STRING | Yes | Yes |
| CHAR | Yes | Yes |
| VARCHAR | Yes | Yes |
| ARRAY | Yes | No |
| MAP | No | No |
| STRUCT | No | No |

## Supported Google BigQuery SQL data types

Supported Google BigQuery SQL data types

| Data types | Viewable | Selectable |
| --- | --- | --- |
| INT64 | Yes | Yes |
| INTEGER | Yes | Yes |
| SMALLINT | Yes | Yes |
| BIGINT | Yes | Yes |
| TINYINT | Yes | Yes |
| BYTEINT | Yes | Yes |
| DECIMAL (p,s) | Yes | Yes |
| NUMERIC (p,s) | Yes | Yes |
| BIGDECIMAL | Yes | Yes |
| BIGNUMERIC | Yes | Yes |
| FLOAT64 | Yes | Yes |
| STRING | Yes | Yes |
| DATE | Yes | Yes |
| DATETIME | Yes | Yes |
| TIME | Yes | Yes |
| TIMESTAMP | Yes | Yes |
| INTERVAL | Yes | No |
| BOOL | Yes | Yes |
| BYTES | Yes | Yes |
| ARRAY | No | No |
| STRUCT | No | No |
| GEOGRAPHY | No | No |
| JSON | No | No |

## Supported Microsoft SQL Server data types

Supported Microsoft SQL Server data types

| Data types | Viewable | Selectable |
| --- | --- | --- |
| BIGINT | Yes | Yes |
| BIT | Yes | Yes |
| CHAR  Maximum size is 4096 bytes. | Yes | Yes |
| DATE | Yes | Yes |
| DATETIME | Yes | Yes |
| DATETIME2 | Yes | Yes |
| DATETIMEOFFSET | Yes | Yes |
| DECIMAL | Yes | Yes |
| FLOAT | Yes | Yes |
| GUID | Yes | Yes |
| INT | Yes | Yes |
| MONEY | Yes | Yes |
| NCHAR  Maximum size is 4096 characters. | Yes | Yes |
| NUMERIC | Yes | Yes |
| NVARCHAR  Maximum size is 4096 characters. | Yes | Yes |
| REAL | Yes | Yes |
| ROWVERSION | Yes | Yes |
| SMALLDATETIME | Yes | Yes |
| SMALLINT | Yes | Yes |
| SMALLMONEY | Yes | Yes |
| TIME | Yes | Yes |
| TINYINT | Yes | Yes |
| VARCHAR  Maximum size is 4096 characters. | Yes | Yes |
| XML | Yes | Yes |

## Supported PostgreSQL data types

Supported PostgreSQL data types

| Data types | Viewable | Selectable |
| --- | --- | --- |
| BIGINT | Yes | Yes |
| INTEGER | Yes | Yes |
| SMALLINT | Yes | Yes |
| DECIMAL (p,s) | Yes | Yes |
| NUMERIC (p,s) | Yes | Yes |
| DOUBLE PRECISION | Yes | Yes |
| REAL | Yes | Yes |
| BIGSERIAL | Yes | Yes |
| SERIAL | Yes | Yes |
| SMALLSERIAL | Yes | Yes |
| MONEY | Yes | Yes |
| TIME | Yes | Yes |
| DATE | Yes | Yes |
| TIME WITH TIME ZONE | Yes | Yes |
| TIMESTAMP | Yes | Yes |
| TIMESTAMPTZ | Yes | Yes |
| INTERVAL | Yes | Yes |
| INT4RANGE | Yes | Yes |
| INT8RANGE | Yes | Yes |
| NUMRANGE | Yes | Yes |
| TSRANGE | Yes | Yes |
| TSTZRANGE | Yes | Yes |
| DATERANGE | Yes | Yes |
| ENUMERATED (created by ENUM function) | Yes | No |
| BOOLEAN | Yes | Yes  (bool=NULL cannot be selected) |
| TEXT | Yes | Yes |
| CHARACTER (n) | Yes | Yes |
| VARCHAR (n) | Yes | Yes |
| POINT | No | Yes |
| LINE | Yes | Yes |
| LSEG | Yes | Yes |
| BOX | Yes | Yes |
| PATH | Yes | Yes |
| POLYGON | Yes | Yes |
| CIRCLE | Yes | Yes |
| CIDR | Yes | Yes |
| INET | Yes | Yes |
| MACADDR | Yes | Yes |
| BIT (n) | Yes | Yes |
| BIT VARYING (n) | Yes | Yes |
| TSVECTOR | Yes | Yes |
| TSQUERY | Yes | Yes |
| UUID | Yes | Yes |
| XML | Yes | Yes |
| JSON | Yes | Yes |
| JSONB | Yes | Yes |
| INTEGER[] | Yes | Yes |
| TEXT[][] | Yes | Yes |
| COMPOSITE (user defined) | Yes | No |
| DOMAIN (user defined) | Yes | Yes |
| PG\_LSN | Yes | Yes |

## Supported Snowflake SQL data types

Supported Snowflake SQL data types

| Data types | Viewable | Selectable |
| --- | --- | --- |
| NUMBER (p,s) | Yes | Yes |
| DECIMAL (p,s) | Yes | Yes |
| NUMERIC (p,s) | Yes | Yes |
| INTEGER | Yes | Yes |
| BIGINT | Yes | Yes |
| SMALLINT | Yes | Yes |
| TINYINT | Yes | Yes |
| BYTEINT | Yes | Yes |
| FLOAT | Yes | Yes |
| FLOAT4 | Yes | Yes |
| FLOAT8 | Yes | Yes |
| DOUBLE | Yes | Yes |
| DOUBLE PRECISION | Yes | Yes |
| REAL | Yes | Yes |
| VARCHAR (n) | Yes | Yes |
| CHAR (n) | Yes | Yes |
| STRING (n) | Yes | Yes |
| TEXT (n) | Yes | Yes |
| BINARY (n) | No | No |
| VARBINARY | No | No |
| BOOLEAN | No | No |
| TIMESTAMP (p) | Yes | Yes |
| TIMESTAMP\_NTZ (p) | Yes | Yes |
| TIMESTAMP\_TZ (p) | Yes | Yes |
| TIMESTAMP\_LTZ (p) | Yes | Yes |
| DATE | Yes | Yes |
| DATETIME | Yes | Yes |
| TIME (p) | Yes | Yes |
| VARIANT | Yes | Yes |
| OBJECT | Yes | No |
| ARRAY | Yes | No |
| GEOGRAPHY | No | No |

## Converting unsupported data types in Azure SQL, Azure Synapse Analytics, and Microsoft SQL Server

You can use the Microsoft database function CONVERT() to enable displaying unsupported data types where it is possible.

When you use CONVERT() in a chart expression, the first [field](#glossary-0 "Glossary term") (data type to convert to) must be enclosed in single quotes , for example, 'varchar'.

CONVERT('<to-datatype>[(length)]', <value> [,<style-number>])

For example, the following expression would not be supported as the result is a VARBINARY(MAX) which is not supported:

DECOMPRESS(COMPRESS('text'))

However, it is possible to use the following expression as it results in the VARCHAR value "text":

CONVERT('varchar', DECOMPRESS(COMPRESS('text')))
