---
title: "Supported data types"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/SAP-ODATA/sap-odata-datatypes.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SAP sources", "SAP OData"]
---

# Supported data types

The following table shows the supported SAP OData source data types (ABAP), the corresponding OData service data types, and the default mapping to Qlik Talend Data Integration data types.

For information on how the data type is mapped to the target, see the topic for the target connector you are using.

Supported data types

| ABAP data type | OData service data type | Qlik Talend Data Integration data type |
| --- | --- | --- |
| ACCP | EDM.STRING | WSTRING |
| CHAR | EDM.STRING | WSTRING |
| CLNT | EDM.STRING | WSTRING |
| CUKY | EDM.STRING | WSTRING |
| CURR | EDM.STRING | NUMERIC |
| DATS | EDM.DATETIME  Information noteThere is no EDM.DATE data type. Specify zeros for the time. | DATETIME |
| DATN | EDM.DATETIME  Information noteThere is no EDM.DATE data type. Specify zeros for the time. | DATETIME |
| DEC | EDM.DECIMAL | NUMERIC |
| FLTP | EDM.DOUBLE | REAL8 |
| INT1 | EDM.INT32 | INT4 |
| INT2 | EDM.INT32 | INT4 |
| INT4 | EDM.INT32 | INT4 |
| INT8 | EDM.INT64 | INT8 |
| LANG | EDM.STRING | WSTRING |
| NUMC | EDM.STRING | WSTRING |
| QUAN | EDM.DECIMAL | NUMERIC |
| RAW | EDM.STRING | WSTRING |
| SSTR | EDM.STRING | WSTRING |
| STRG | EDM.STRING | WSTRING |
| TIMS | EDM.TIME | TIME |
| TZNTSTMPL | EDM.DATETIMEOFFSET |  |
| UNIT | EDM.STRING | WSTRING |
| VARC | EDM.STRING | WSTRING |
