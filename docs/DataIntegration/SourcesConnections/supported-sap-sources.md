---
title: "Supported SAP sources"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/supported-sap-sources.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SAP sources"]
---

# Supported SAP sources

The table below lists which SAP sources are supported by Data Movement gateway and also specifies which connectors need to be configured to connect to the application.

Information noteThe supported database versions always reflect the capabilities of the latest Data Movement gateway version, regardless of whether or not you are using Data Movement gateway to access your data source(s). For information on the versions supported (or no longer supported) with the latest Data Movement gateway version ,see [*Upgrading and uninstalling Data Movement gateway*](../../Gateways/dm-gateway-upgrading.htm)

Supported data sources

| Connector | Supported Qlik subscription | Supported without Data Movement gateway | Supported versions | Source type |
| --- | --- | --- | --- | --- |
| SAP HANA (Database)  For more information, see [*SAP HANA (Database)*](SAP-HANA/SAP-HANA-source.htm) | Enterprise | No | 2.0 | Application |
| SAP ODP  For more information, see [*SAP ODP*](SAP-ODP/sap-odp-properties.htm) | Enterprise | No | The SAP ODP endpoint uses ODP API 2.0 which is available from the following SAP basis levels and above:   - PI\_BASIS 730 SP 14 (part of SAP NetWeaver 7.30 SP 14) - PI\_BASIS 731 SP 16 (part of SAP NetWeaver 7.03 SP 16 and 7.31 SP 16) - PI\_BASIS 740 SP 11 (part of SAP NetWeaver 7.40 SP 11) - SAP\_BW 750 SP 0 (incl. former PI\_BASIS packages)   Information noteSAP\_BASIS and PI\_BASIS are interchangeable. In newer systems, the component name is SAP\_BASIS.  For more information, see SAP Note 1931427.  For information on how to release extractors so that they are available for the ODP API, see SAP Note 2232584. | Application |
| SAP HANA RFC  For more information, see [*SAP HANA RFC*](SAP-HANA-RFC/sap-hana-rfc-source.htm). | Early Access program | No | Early Access | Application |
| SAP OData  For more information, see [*SAP OData*](SAP-ODATA/sap-odata-properties.htm) | Enterprise | No | The following SAP NetWeaver and SAP BW versions contain components required for working with OData:   - SAP Gateway Foundation (SAP\_GWFND) in SAP NetWeaver 7.52, 7.51, and 7.50 (>= SP03) and in ABAP Platform 1809, 1909, 2020, 2021, 2022, 2023, and 2025. - ODP-Based Data Extraction via OData is supported from SAP BW 750.   For more information, see SAP notes 3058404 and 2512479. | Application |
| SAP Extractor  For more information, see [*SAP Extractor*](SAP-Extractor/SAP-Extractor-source.htm) | Enterprise | No | N/A | Application |
| SAP (Application)  For SAP configurations using any of the following backend databases: Oracle, Microsoft SQL Server, IBM DB2 for LUW, IBM DB2 for z/OS, and SAP HANA.  For more information, see[*SAP (Application)*](SAP-Application-DB/sap-application-source.htm) | Enterprise | No | N/A | Application |
| SAP Cloud for Customers | All | Yes | N/A | SaaS application |
| SAP Concur | All | Yes | N/A | SaaS application |
| SAP SuccessFactors | All | Yes | N/A | SaaS application |
