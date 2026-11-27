---
title: "Supported data types"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/SQLServer/sqlserver-source-datatypes.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "Microsoft SQL Server (log based)"]
---

# Supported data types

The following table shows the supported Microsoft SQL Server source data types and their default mapping to Qlik Talend Data Integration data types.

When moving to a Microsoft SQL Server-based target, the source and target data types are the same, apart from the exceptions described in [*Homogeneous replication*](sqlserver-source-homog.htm).

For information on how to view the data type that is mapped in the target, see the section for the target connector you are using.

Information note

Collatable data types are indicated by an asterisk (\*).

Supported source data types

| Microsoft SQL Server data types | Qlik Talend Data Integration data types |
| --- | --- |
| BIGINT | INT8 |
| BIT | BOOLEAN |
| DECIMAL | NUMERIC |
| INT | INT4 |
| MONEY | NUMERIC (19,4) |
| NUMERIC (p,s) | NUMERIC |
| SMALLINT | INT2 |
| SMALLMONEY | NUMERIC (10,4) |
| TINYINT | UINT1 |
| REAL | REAL4 |
| FLOAT | REAL8 |
| DOUBLE | REAL8 |
| DATETIME | DATETIME |
| DATETIME2 | DATETIME |
| SMALLDATETIME | DATETIME |
| DATE | DATE |
| TIME | STRING (16) |
| DATETIMEOFFSET | STRING |
| \*CHAR | STRING |
| \*VARCHAR | STRING |
| \*VARCHAR (max)  \*TEXT  To use this data type with Qlik Talend Data Integration, you must enable the use of CLOBs for a specific task.  LOB columns for Microsoft SQL Server tables are updated in the target even for UPDATE statements that did not change the value of the LOB column in Microsoft SQL Server. | CLOB |
| \*NCHAR | WSTRING |
| \*NVARCHAR (length) | WSTRING |
| \*NVARCHAR (max)  \*NTEXT  To use this data type with Qlik Talend Data Integration, you must enable the use of NCLOBs for a specific task.  LOB columns for Microsoft SQL Server tables are updated in the target even for UPDATE statements that did not change the value of the LOB column in Microsoft SQL Server. | NCLOB |
| BINARY | BYTES |
| VARBINARY | BYTES |
| VARBINARY (max)  IMAGE  To use this data type with Qlik Talend Data Integration, you must enable the use of BLOBs for a specific task.  LOB columns for Microsoft SQL Server tables are updated in the target even for UPDATE statements that did not change the value of the LOB column in Microsoft SQL Server. | BLOB |
| TIMESTAMP | BYTES |
| UNIQUEIDENTIFIER | STRING |
| HIERARCHYID | VARCHAR (x) |
| XML  LOB columns for Microsoft SQL Server tables are updated in the target even for UPDATE statements that did not change the value of the LOB column in Microsoft SQL Server.  To use this data type with Qlik Talend Data Integration, you must enable the use of NCLOBs for a specific task. | CLOB |
| GEOMETRY | NCLOB |
| GEOGRAPHY | NCLOB |
| JSON | NCLOB with JSON subtype |

## Unsupported data types

The following data types are not supported:

- CURSOR
- SQL\_VARIANT
- TABLE

Information note

User-defined data types are supported according to their base-type. For example a user-defined data type based on DATETIME is handled as a DATETIME data type.
