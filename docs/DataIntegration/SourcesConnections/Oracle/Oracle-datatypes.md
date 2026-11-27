---
title: "Supported data types"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/Oracle/Oracle-datatypes.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "Oracle"]
---

# Supported data types

The following table shows the supported Oracle source data types and their default mapping to Qlik Talend Data Integration data types.

When moving to an Oracle -based target, the source and target data types are the same, apart from the exceptions described in [*Homogeneous replication*](oracle-source-homog.htm).

For information on how to view the data type that is mapped in the target, see the section for the target connector you are using.

Supported data types

| Oracle data types | Qlik Talend Data Integration data types |
| --- | --- |
| BINARY\_FLOAT | REAL4 |
| BINARY\_DOUBLE | REAL8 |
| BOOLEAN (Introduced in Oracle AI Database 26ai) | BOOLEAN |
| FLOAT (P) | REAL8 |
| NUMBER  Without defined precision or scale | Expose NUMBER as:  The mapping follows the selected setting in the Qlik Talend Data Integration Oracle source database settings. |
| NUMBER(P,S) | When scale is < 0:  REAL8  When scale is 0:  Precision = 0: REAL8  Precision > 0 and <= 2: INT1  Precision > 2 and <= 4: INT2  Precision > 4 and <= 9: INT4  Precision > 9: NUMERIC(P,S)  When scale is > 0 and precision >= scale:  NUMERIC(P,S)  When scale is greater than precision:  NUMERIC(S,S)  Information note Starting with Qlik Talend Data Integration November 2026 (2026.11), the `NumberFixPrecisionLessThanScale-OracleSource` feature flag is enabled by default.  The mapped precision equals the source scale, and the scale remains unchanged. For example, NUMBER(3,4) maps to NUMERIC(4,4).  Previously, both precision and scale were reported as 38. To restore this legacy behavior by disabling the feature flag, contact Qlik Support. |
| DATE | DATETIME |
| INTERVAL\_YEAR TO MONTH | STRING (with interval year\_to\_month indication) |
| INTERVAL\_DAY TO SECOND | STRING (with interval day\_to\_second indication) |
| TIMESTAMP | DATETIME |
| TIMESTAMP WITH TIME ZONE | STRING (with timestamp\_with\_timezone indication) |
| TIMESTAMP WITH LOCAL TIME ZONE | STRING (with timestamp\_with\_local\_timezone indication) |
| CHAR | STRING |
| VARCHAR2 | Length <= 4000 bytes:  STRING  Length > 4000 bytes:  CLOB |
| NCHAR | Length <= 2000 bytes:  WSTRING  Length > 2000 bytes:  NCLOB |
| NVARCHAR2 | Length <= 4000 bytes:  WSTRING  Length > 4000 bytes:  NCLOB |
| RAW | Length <= 2000 bytes:  BYTES  Length > 2000 bytes:  BLOB |
| REAL | REAL8 |
| BLOB  To use this data type with Qlik Talend Data Integration, you must enable the use of BLOBs for a specific task. | BLOB |
| CLOB  To use this data type with Qlik Talend Data Integration, you must enable the use of CLOBs for a specific task. | CLOB |
| NCLOB  To use this data type with Qlik Talend Data Integration, you must enable the use of NCLOBs for a specific task. | NCLOB |
| LONG  The LONG data type is not supported in Batch optimized apply mode.  To use this data type with Qlik Talend Data Integration, you must enable the use of LOBs for a specific task. | CLOB |
| LONG RAW  The LONG RAW data type is not supported in Batch optimized apply mode.  To use this data type with Qlik Talend Data Integration, you must enable the use of LOBs for a specific task. | BLOB |
| XMLTYPE  Information note  - When moving XML columns, performance can be improved by *not* using the Oracle 12 client. - Support for the XMLTYPE data type requires the full Oracle Client (as opposed to the Oracle Instant Client).  When the target column is a CLOB, both full LOB mode and limited LOB mode are supported (depending on the target).  For more information, see LOB support see [*Metadata*](../../Replicating/replicating-settings-metadata.htm). | CLOB with XML subtype |
| JSON  Information note  - You need to obtain a license from Oracle to use Oracle GoldenGate.   After obtaining the license, enable GoldenGate replication as described in the Oracle [Database Reference](https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ENABLE_GOLDENGATE_REPLICATION.html). - Support for the JSON data type requires Oracle Client version 21 or later. | CLOB with JSON subtype |

# Unsupported data types

The following data types are not supported:

- BFILE
- ROWID
- REF
- UROWID
- ANYDATA
- SDO\_GEOMETRY
- User-defined data types

Information note

- Virtual columns are not supported.
- As the ROWID data type is not supported, materialized views based on a ROWID column are also not supported.
