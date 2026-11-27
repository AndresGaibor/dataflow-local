---
title: "Supported data types"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/IBM4DB2-luw/luw-datatypes.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "IBM DB2 for LUW"]
---

# Supported data types

The following table shows the supported IBM DB2 for LUW source data types and their default mapping to Qlik Talend Data Integration data types.

For information on how to view the data type that is mapped in the target, see the section for the target connector you are using.

Supported data types

| IBM DB2 for LUW Source data types | Qlik Talend Data Integration data types |
| --- | --- |
| INTEGER | INT4 |
| SMALLINT | INT2 |
| BIGINT | INT8 |
| DECIMAL (p,s) | NUMERIC (p,s) |
| FLOAT | REAL8 |
| DOUBLE | REAL8 |
| REAL | REAL4 |
| DECFLOAT (p) | If precision = 16, then:  REAL8  If precision is = 34, then:  STRING |
| GRAPHIC (n) | If n<=127 KB, then:  WSTRING |
| VARGRAPHIC (n) | If n<=16k double byte chars, then:  WSTRING |
| LONG VARGRAPHIC | CLOB |
| CHAR (n) | STRING  n<=255 |
| VARCHAR (n) | STRING  n<=32k |
| LONG VARCHAR (n) | CLOB  n<=32k |
| CHAR (n) FOR BIT DATA | BYTES |
| VARCHAR (n) FOR BIT DATA | BYTES |
| LONG VARCHAR FOR BIT DATA | BYTES |
| DATE | DATE |
| TIME | TIME |
| TIMESTAMP | DATETIME |
| BLOB | BLOB |
| CLOB | CLOB  Maximum size: 2 GB |
| DBCLOB | CLOB  Maximum size: 1 G double byte chars |
| XML | CLOB |
| BOOLEAN | BOOLEAN |
