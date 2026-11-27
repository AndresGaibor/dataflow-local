---
title: "Homogeneous replication"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/Oracle/oracle-source-homog.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "Oracle"]
---

# Homogeneous replication

With the exception of the data types listed in the table below, when replicating from an Oracle source to an Oracle target, all of the source and target data types will be identical. Note that homogeneous replication is only relevant with Replication data projects.

Information note

- As of Oracle 9.0, the LONG and LONG RAW data types are no longer supported by Oracle.
- Primary/Unique Index names are preserved during homogeneous replication.

Non-identical data types in homogeneous replication

| Oracle data types | Qlik Talend Data Integration data types |
| --- | --- |
| VARCHAR2 | Length > 4000 bytes:  CLOB |
| NVARCHAR2 | Length > 4000 bytes:  NCLOB |
| RAW | Length > 2000 bytes:  BLOB |
| LONG  The LONG data type is not supported in Batch optimized Apply Mode.  To use this data type with Qlik Talend Data Integration, you must enable the use of LOBs for a specific task. | **CLOB** |
| LONG RAW  The LONG RAW data type is not supported in Batch optimized Apply Mode.  To use this data type with Qlik Talend Data Integration, you must enable the use of LOBs for a specific task. | **BLOB** |
