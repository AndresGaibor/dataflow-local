---
title: "Supported data types"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/IBM4DB2-iseries/db2_db_data_types_source.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "IBM DB2 for iSeries"]
---

# Supported data types

The following table shows the supported IBM DB2 for iSeries source data types and their default mapping to Qlik Talend Data Integration data types.

For information on how to view the data type that is mapped in the target, see the section for the target connector you are using.

Supported data types

| IBM DB2 for iSeries data types | Qlik Talend Data Integration data types |
| --- | --- |
| INTEGER | INT4 |
| SMALLINT | INT2 |
| BIGINT | INT8 |
| DECIMAL (p,s) | NUMERIC (p,s) |
| FLOAT | REAL8 |
| DOUBLE | REAL8 |
| REAL | REAL4 |
| CHAR (n) | If n<=32 KB, then:  STRING |
| VARCHAR (n) | If n<=32 KB, then:  STRING |
| GRAPHIC (n) | If n<=16 KB, then:  STRING |
| VARGRAPHIC (n) | If n<=16 KB double byte chars, then:  STRING |
| DATE | DATE |
| TIME | TIME |
| TIMESTAMP | DATETIME (6) |
| BLOB | BLOB  Maximum size: 2 GB |
| CLOB | CLOB  Maximum size: 2 GB |
| ROWID | BYTES - This should be a user-defined column. |
| DATALINK | STRING |
| TIMESTAMP WITH TIME ZONE | NOT SUPPORTED |
| BOOLEAN  Information note The BOOLEAN data type is supported from iSeries 7.5. | BOOLEAN |
| BINARY-DECIMAL | NUMERIC  If BINARY-DECIMAL has a scale of 0:  INTEGER |
| ZONED-DECIMAL | NUMERIC |
