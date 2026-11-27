---
title: "Supported data types"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/IBM4DB2-zos/db2_db_data_types_source.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "IBM DB2 for z/OS"]
---

# Supported data types

The following table shows the supported IBM DB2 for z/OS source data types and their default mapping to Qlik Talend Data Integration data types.

For information on how to view the data type that is mapped in the target, see the section for the target connector you are using.

Supported data types

| IBM DB2 for z/OS Source Data Types | Qlik Talend Data Integration Data Types |
| --- | --- |
| INTEGER | INT4 |
| SMALLINT | INT2 |
| BIGINT | INT8 |
| DECIMAL (p,s) | NUMERIC (p,s)  Information note If a decimal point is set to a comma (,) in the DB2 configuration, you will need to configure Qlik Talend Data Integration to support the DB2 setting.   For information on how to configure Qlik Talend Data Integration, see [*R4Z configuration dependency on host*](IBM4DB2-zos-source.htm#R4Z). |
| FLOAT (8) | REAL8 |
| DOUBLE | REAL8 |
| REAL | REAL4 |
| DECFLOAT (p) | If precision = 16, then:  REAL8  If precision = 34, then:  STRING |
| GRAPHIC | If n<=127, then:  WSTRING |
| VARGRAPHIC | If n<=16k double byte chars, then:  WSTRING |
| LONG VARGRAPHIC | CLOB |
| CHAR (n) | STRING  n<=255 |
| VARCHAR (n) | STRING  n<=32k |
| LONG VARCHAR (n) | CLOB  n<=32k |
| CHAR (n) FOR BIT DATA | BYTES |
| VARCHAR (n) FOR BIT DATA | CLOB |
| LONG VARCHAR FOR BIT DATA | BLOB |
| DATE | DATE |
| TIME | TIME |
| TIMESTAMP | DATETIME (6) |
| BLOB | BLOB |
| CLOB | CLOB  Maximum size: 2 GB |
| DBCLOB | CLOB  Maximum size: 1 G double byte chars |
| XML | CLOB |
| BINARY | BYTES |
| VARBINARY | BYTES |
| ROWID | IGNORED |
| TIMESTAMP WITH TIME ZONE | NOT SUPPORTED |
