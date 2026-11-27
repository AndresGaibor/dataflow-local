---
title: "Prerequisites"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/SAP-ODATA/sap-odata-prereq.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SAP sources", "SAP OData"]
---

# Prerequisites

The following section describes the prerequisites for working with the SAP OData source connector.

## SAP NetWeaver and SAP BW supported versions

The following SAP NetWeaver and SAP BW versions contain components required for working with OData:

- SAP Gateway Foundation (SAP\_GWFND) in SAP NetWeaver 7.52, 7.51, and 7.50 (>= SP03) and in ABAP Platform 1809, 1909, 2020, 2021, 2022, 2023, and 2025.
- ODP-Based Data Extraction via OData is supported from SAP BW 750.

For more information, see SAP notes 3058404 and 2512479.

## Prerequisites for generating and using an OData service

For ODP-based data distribution via OData, the SAP Gateway Foundation should either exist locally in the SAP NetWeaver system of the ODP provider, or in a separate SAP NetWeaver instance. To generate the OData service, the system must contain the functional scope of the software component IW\_BEP.

To extract data via the OData service BW InfoProvider (ODP context BW), you need an open hub license.

For more information, see [ODP-Based Data Extraction via OData](https://help.sap.com/doc/saphelp_nw75/7.5.5/en-US/11/853413cf124dde91925284133c007d/frameset.htm).

## Check SAP Gateway activation

To check the status of the SAP Gateway, do the following:

1. Open transaction SPRO.
2. Navigate to: SAP NetWeaver > SAP Gateway > OData Channel > Configuration > Activate or Deactivate SAP Gateway.
3. Click the Activity icon.

   A message shows the current status: Active or Not Active.
4. If the SAP Gateway status is inactive, click Activate.

## Check services in transaction SICF

The SICF transaction ensures the activation of required HTTP services for OData functionality. To check the node service status, do the following:

1. Open transaction SICF.
2. Navigate to the following service path: /sap/opu/odata/SAP/.
3. Check the node is active.
4. If the required OData service is inactive, right click and select Activate Service.
5. Repeat for all services under the service path: /sap/opu/odata/iwfnd.
