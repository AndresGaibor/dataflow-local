---
title: "Supported data types"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/MySQL/mysql-source-data-types.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "MySQL"]
---

# Supported data types

The following table shows the supported MySQL source data types and their default mapping to Qlik Talend Data Integration data types.

When replicating data to a MySQL-based target, the source and target data types are the same, apart from the exceptions described in [*Homogeneous replication*](homogeneous_replication.htm).

For information on how to view the data type that is mapped in the target, see the section for the target connector you are using.

Supported data types

| MySQL data types | Collatable | Qlik Talend Data Integration data types |
| --- | --- | --- |
| INT | No | INT4 |
| BIGINT | No | INT8 |
| MEDIUMINT | No | INT4 |
| TINYINT | No | INT1 |
| SMALLINT | No | INT2 |
| UNSIGNED TINYINT | No | UINT1 |
| UNSIGNED SMALLINT | No | UINT2 |
| UNSIGNED MEDIUMINT | No | UINT4 |
| UNSIGNED INT | No | UINT4 |
| UNSIGNED BIGINT | No | UINT8 |
| DECIMAL (10) | No | NUMERIC (10,0) |
| BINARY | No | BYTES (1) |
| BIT | No | BOOLEAN |
| BIT (64) | No | BYTES (8) |
| BLOB | No | BYTES (65535) |
| LONGBLOB | No | BLOB |
| MEDIUMBLOB | No | BLOB |
| TINYBLOB | No | BYTES (255) |
| DATE | No | DATE |
| DATETIME  Information note DATETIME without a parenthetical value is replicated without milliseconds, whereas DATETIME with a value of 1-5 - e.g. DATETIME(5) - is replicated with milliseconds.  Information note When moving a DATETIME column, the time remains the same on the target (i.e. it is not converted to UTC). | No | DATETIME |
| TIME | No | STRING |
| TIMESTAMP  Information note When moving a TIMESTAMP column, the time is converted to UTC on the target. | No | DATETIME |
| YEAR | No | INT2 |
| DOUBLE | No | REAL8 |
| FLOAT  If the FLOAT values are not in the range specified below, use a transformation to map FLOAT to STRING. For an explanation of how to do this, see [*Creating rules to transform datasets*](../../Transformation/Transformation-rules.htm).  Supported FLOAT range:  - 1.79E+308 to -2.23E-308, 0  and  2.23E-308 to 1.79E+308 | No | REAL (DOUBLE) |
| VARCHAR (45) | Yes | WSTRING (45) |
| VARCHAR (2000) | Yes | WSTRING (2000) |
| VARCHAR (4000) | Yes | WSTRING (4000) |
| VARBINARY (4000) |  | BYTES (4000) |
| VARBINARY (2000) |  | BYTES (2000) |
| CHAR | Yes | WSTRING |
| TEXT | Yes | WSTRING (65535) |
| LONGTEXT | Yes | **NCLOB** |
| MEDIUMTEXT | Yes | **NCLOB** |
| TINYTEXT | Yes | WSTRING (255) |
| GEOMETRY | No | BLOB |
| POINT | No | BLOB |
| LINESTRING | No | BLOB |
| POLYGON | No | BLOB |
| MULTIPOINT | No | BLOB |
| MULTILINESTRING | No | BLOB |
| MULTIPOLYGON | No | BLOB |
| GEOMETRYCOLLECTION | No | BLOB |
| ENUM | No | WSTRING (Length)  Where "Length" is the longest value in the ENUM. |
| SET | No | WSTRING (Length)  Where "Length" is the total of all values in the SET, including commas. |
| JSON | No | CLOB |

Information note

If the DATETIME and TIMESTAMP data types are specified with a “zero” value (i.e. 0000-00-00), you need to make sure that the target database in the moving task supports "zero" values for the DATETIME and TIMESTAMP data types. If they are not supported, you can use a transformation to specify a supported value (e.g. 1970.) Otherwise, they will be recorded as null on the target.
