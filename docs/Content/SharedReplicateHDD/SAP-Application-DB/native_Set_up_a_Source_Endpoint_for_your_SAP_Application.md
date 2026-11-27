---
title: "Set up a source connector for SAP (Application)"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/Content/SharedReplicateHDD/SAP-Application-DB/native_Set_up_a_Source_Endpoint_for_your_SAP_Application.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SAP sources", "SAP (Application)", "Prerequisites"]
---

# Set up a source connector for SAP (Application)

Before you can configure the SAP (Application) connector, you first need to configure one of the following backend source connectors, according to your SAP Package type:

Information note

Moving from an STXL table is not supported. If you need to Move from an STXL table, use the [SAP Extractor connector](../../../../Sense_Hub/DataIntegration/SourcesConnections/SAP-Extractor/SAP-Extractor-source.htm) instead.

- Oracle

  Information note

  When using Oracle as the backend database, any tables you want to capture must be defined with ALL COLUMN SUPPLEMENTAL LOGGING.

  See also: [*Oracle*](../../../../Sense_Hub/DataIntegration/SourcesConnections/Oracle/Oracle-source.htm)
- Microsoft SQL Server

  Information note

  When using Microsoft SQL Server as the backend database, transparent table fields defined as STRING or BINARY STRING are not supported.

  See also: [*Microsoft SQL Server (log based)*](../../../../Sense_Hub/DataIntegration/SourcesConnections/SQLServer/sqlserver-source.htm)
- IBM DB2 for LUW

  See also: [*IBM DB2 for LUW*](../../../../Sense_Hub/DataIntegration/SourcesConnections/IBM4DB2-luw/IBM4DB2-luw-source.htm)
- IBM DB2 for z/OS

  See also: [*IBM DB2 for z/OS*](../../../../Sense_Hub/DataIntegration/SourcesConnections/IBM4DB2-zos/IBM4DB2-zos-source.htm)
- SAP HANA

  See also: [*SAP HANA (Database)*](../../../../Sense_Hub/DataIntegration/SourcesConnections/SAP-HANA/SAP-HANA-source.htm)

For information about general limitations when using the SAP (Application) connector, see [*Limitations and considerations*](native_Limitations_SAP_app.htm).

## Backend Source Endpoint Permissions

The user specified in the underlying source connector settings must have SELECT permission on the following objects:

- DD02L
- DD03L
- DD02T
- DD03T
- T000
- /HTG/GC\_HEAD
- /HTG/GC\_TABLES1
- /HTG/GC4R\_BUSGRP
- /HTG/GC4R\_TABLES
