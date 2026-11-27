---
title: "Supported dat a types"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/PostgreSQL/postgresql-data-types-source.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "PostgreSQL"]
---

# Supported data types

The following table shows the supported PostgreSQL source data types and their default mapping to Qlik Talend Data Integration data types.

When replicating to a PostgreSQL-based target, the source and target data types are the same, apart from the exceptions described in [*Homogeneous replication*](postgresql-source-homog.htm).

For information on how to view the data type that is mapped in the target, see the section for the target connector you are using.

Supported data types

| PostgreSQL data types | Qlik Talend Data Integration data types |
| --- | --- |
| INTEGER | INT4 |
| SMALLINT | INT2 |
| BIGINT | INT8 |
| NUMERIC | NUMERIC(28,6) |
| NUMERIC(p,s) | If precision is =< 38, then:  NUMERIC(p,s)  If precision is => 39, then:  STRING |
| DECIMAL | NUMERIC(28,6) |
| DECIMAL(p,s) | If precision is =< 38, then:  NUMERIC(p,s)  If precision is => 39, then:  STRING |
| REAL | REAL4 |
| DOUBLE | REAL8 |
| SMALLSERIAL | INT2 |
| SERIAL | INT4 |
| BIGSERIAL | INT8 |
| MONEY | NUMERIC(38,4)  Information note The MONEY data type is mapped to FLOAT in Microsoft SQL Server. |
| CHAR | WSTRING (1) |
| CHAR(n) | WSTRING (n) |
| VARCHAR(n)  Information note VARCHAR without a length (n) is not recognized as a valid data type by target endpoints. Consequently, if a source column data type is set to VARCHAR without an explicit length, Qlik Talend Data Integration will set a default length of 8000 bytes.  You can change the default by setting the following internal parameter to the required length:  unboundedVarcharMaxSize  For information on setting internal parameters, see [*PostgreSQL*](postgresql-source.htm). | WSTRING (n) |
| TEXT | NCLOB |
| BYTEA | BLOB |
| TIMESTAMP | DATETIME |
| TIMESTAMP (z)  Information noteThis data type will always be presented in UTC. | DATETIME |
| DATE  Information noteQlik Talend Data Integration only supports ISO formatted textual DATE formats (the default). If other formats are used, an error will be generated. You can change the date format in the postgresql.conf file or using the PGDATESTYLE environment variable. You can also change the date format at database level. | DATE |
| TIME | TIME |
| TIME (z) | TIME |
| INTERVAL | STRING (128) - 1 YEAR, 2 MONTHS, 3 DAYS, 4 HOURS, 5 MINUTES, 6 SECONDS |
| BOOLEAN | BOOLEAN |
| ENUM | STRING (64) |
| CIDR | STRING (50) |
| INET | STRING (50) |
| MACADDR | STRING (18) |
| BIT (n) | STRING (n) |
| BIT VARYING (n) | STRING (n) |
| UUID | STRING |
| TSVECTOR | CLOB |
| TSQUERY | CLOB |
| XML | CLOB |
| POINT | STRING (255) "(x,y)" |
| LINE | STRING (255) "(x,y,z)" |
| LSEG | STRING (255) "((x1,y1),(x2,y2))" |
| BOX | STRING (255) "((x1,y1),(x2,y2))" |
| PATH | CLOB "((x1,y1),(xn,yn))" |
| POLYGON | CLOB "((x1,y1),(xn,yn))" |
| CIRCLE | STRING (255) "(x,y),r" |
| JSON  Information noteReading and writing JSON data is performed using wide string (where each character occupies 2 bytes). Therefore, when replicating JSON columns to a PostgreSQL target, set the limited LOB size in the task settings to twice the maximum JSON length. So, for example, if the JSON data is 4 KB, set the limited LOB size value to 8 KB. | NCLOB  NCLOB with JSON subtype |
| JSONB  Information noteReading and writing JSONB data is performed using wide string (where each character occupies 2 bytes). Therefore, when replicating JSONB columns to a PostgreSQL target, set the limited LOB size value in the task settings to twice the maximum JSONB length. So, for example, if the JSONB data is 4 KB, set the limited LOB size value to 8 KB. | NCLOB  NCLOB with JSON subtype |
| ARRAY | NCLOB |
| COMPOSITE | NCLOB |
| INT4RANGE | STRING (255) |
| INT8RANGE | STRING (255) |
| NUMRANGE | STRING (255) |
| TSRANGE | STRING (255) |
| INT4MULTIRANGE | STRING (255) |
| INT8MULTIRANGE | STRING (255) |
| NUMMULTIRANGE | STRING (255) |
| TSMULTIRANGE | STRING (255) |
| CHARACTER VARYING | If length is specified:  WSTRING (LENGTH)  If no length is specified:  WSTRING (8000) |
| OID (Object Identifier)  Information noteQlik Talend Data Integration will replicate the object ID, and not the actual value. | UINT4 |

Information noteThe PostGIS data type is not supported.
