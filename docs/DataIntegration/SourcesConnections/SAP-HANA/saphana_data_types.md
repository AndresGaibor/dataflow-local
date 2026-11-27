---
title: "Supported data types"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/SAP-HANA/saphana_data_types.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SAP sources", "SAP HANA (Database)"]
---

# Supported data types

The following table shows the supported SAP HANA source data types and their default mapping to Qlik Talend Data Integration data types.

For information on how to view the data type that is mapped in the target, see the section for the target connector you are using.

Supported data types

| SAP HANA data types | Qlik Talend Data Integration data types |
| --- | --- |
| DATE | DATE |
| TIME | TIME |
| SECONDDATE | DATETIME |
| TIMESTAMP | DATETIME |
| TINYINT | UINT1 |
| SMALLINT | INT2 |
| INTEGER | INT4 |
| BIGINT | INT8 |
| DECIMAL (p,s) | NUMERIC |
| DECIMAL | STRING |
| SMALLDECIMAL | STRING |
| REAL | REAL4 |
| DOUBLE | REAL8 |
| VARCHAR | STRING |
| NVARCHAR | WSTRING |
| ALPHANUM | STRING |
| SHORTTEXT | WSTRING |
| VARBINARY | BYTES |
| BLOB | BLOB |
| CLOB | CLOB |
| NCLOB | NCLOB |
| TEXT | NCLOB |
| BOOLEAN | UINT1 |

## Unsupported data types

The following data types are not supported:

- ARRAY
- ST\_GEOMETRY
- ST\_POINT
