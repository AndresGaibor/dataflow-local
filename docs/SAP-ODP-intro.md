---
title: "SAP ODP Connector"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/SAP_ODP_Connectors_Help/Content/Connectors_SAP_ODP/SAP-ODP-intro.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics"]
---

# SAP ODP Connector

The ODP Connector provides connectivity to the SAP ODP framework, exposing data artifacts such as Extractors, CDS views and SAP HANA Information views.

## Prerequisites

The following section describes the prerequisites for working with the SAP ODP connector.

### General prerequisites

#### ODP API

The SAP ODP connector uses ODP API 2.0 which is available from the following SAP basis levels and above:

- PI\_BASIS 730 SP 14 (part of SAP NetWeaver 7.30 SP 14)
- PI\_BASIS 731 SP 16 (part of SAP NetWeaver 7.03 SP 16 and 7.31 SP 16)
- PI\_BASIS 740 SP 11 (part of SAP NetWeaver 7.40 SP 11)
- SAP\_BW 750 SP 0 (incl. former PI\_BASIS packages)

Information noteSAP\_BASIS and PI\_BASIS are interchangeable. In newer systems, the component name is SAP\_BASIS.

For more information, see SAP Note 1931427.

For information on how to release extractors so that they are available for the ODP API, see SAP Note 2232584.

#### STXL Table support

To expose the table STXL for extraction using the SAP ODP connector, a custom extractor needs to be created in transaction RSO2 in SAP GUI. This extractor can then be called by the SAP ODP connector.

#### Setting up SLT on SAP

In order to replicate data, you must first define the parameters that SAP Landscape Transformation Replication Server will use to replicate data from a source system to a target system. You specify this information in a configuration. A configuration contains information about the source system, the target system, and the relevant connections.

You create a configuration in SAP Landscape Transformation Replication Server system. To create a configuration, open the SAP LT Replication Server Cockpit (transaction LTRC) and choose Create Configuration.

Creating a configuration involves the following steps:

1. In the Specify General Data tab, provide the following information:

   - Configuration Name: You must specify a name for the configuration. This name is used for the schema that is created automatically in the target system.
   - Description (Optional): Optionally, specify a description for the configuration.
2. In the Specify Source System tab, select the RFC Connection option and provide the following information:

   - RFC Destination: Enter NONE.
   - Allow Multiple Usage: Select this option.
3. In the Specify Target System tab, select the Other option and provide the following information:

   - Scenario: Select Operational Data Provisioning (ODP) from the drop-down list.
   - Queue Alias: Specify a name.
4. In the Specify Transfer Settings tab, specify transfer settings appropriate for your environment. Under Job Options, we recommend setting at least five Data Transfer, Initial Load, and Calculation Jobs.
5. In the Review and Create tab, review your settings and create the configuration.
6. Grant the [*SAP ODP Connector user configuration*](SAP-ODP-user-configuration.htm).

### Prerequisites when working with Qlik Data Gateway - Direct Access

When working with Qlik Data Gateway - Direct Access, make sure to fulfill the following prerequisites:

#### Ports and Microsoft Visual C++

- These ports are used for communication by internal data gateway processes. If any of these ports is being used by another application, either reconfigure the other application or uninstall it.
  - 3007 (SAP BW Connector REST API)
  - 3008 (SAP SQL Connector REST API)
  - 3009 (SAP ODP Connector REST API)
  - 50070 (SAP BW Connector gRPC)
  - 50080 (SAP SQL Connector gRPC)
  - 50090 (SAP ODP Connector gRPC)
- Microsoft Visual C++ 2013 Redistributable (x64) must be installed on the Qlik Data Gateway - Direct Access machine.

#### SAP NetWeaver RFC SDK for Qlik Data Gateway - Direct Access

When using Qlik Data Gateway - Direct Access to access SAP, you need to install the SAP NetWeaver RFC SDK on the Qlik Data Gateway - Direct Access machine. The library is used by the Qlik SAP Connectors to communicate with the SAP Systems.

To do this:

1. Download SAP NetWeaver RFC SDK 7.50 Patch Level 8 or later from [SAP NetWeaver Remote Function Call (RFC) Software Development Kit (SDK)](https://support.sap.com/en/product/connectors/nwrfcsdk.html).
2. Unzip the library. The Windows (sapnwrfc\_win64) library contains the following files:

   - icudt50.dll
   - icuin50.dll
   - icuuc50.dll
   - libsapucum.dll
   - libsapucum.lib
   - sapnwrfc.dll
   - sapnwrfc.lib
   - sapnwrfc.pdb
3. Copy the files to the Direct Access gateway installation folder. This process is performed differently depending on your installation:

   - Windows server installations:

     Copy the files to the following folder on the Qlik Data Gateway - Direct Access machine:

     C:\Program Files\Qlik\ConnectorAgent\runSapConnectors
   - Containerized installations:

     Run this command from the SAP RFC SDK folder that contains both Linux and Windows folders of the SDK binaries (for example, Users/abc/…/sap-7.50.8):

     docker cp . direct-access-agent-1:/usr/share/Qlik/Gateway/sap-sdk
4. For Windows server installations only: Install Microsoft Visual C++ 2013 Redistributable (x64) on the Qlik Data Gateway - Direct Access machine.

For more information on Qlik Data Gateway - Direct Access, see [Setting up Qlik Data Gateway - Direct Access](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/direct-access-gateway.htm).

## Supported objects

The SAP ODP connector supports the following Contexts:

- ABAP Core Data Services (CDS) views: The context of the CDS views. This is the default ODP context.
- SAP NetWeaver Business Warehouse: The context of the BW

  Information noteHierarchies are not supported.
- SAP DataSources / Extractors: The context of data sources and extractors.
- SAP HANA Information Views: The context of HANA views.
- SAP LT Replication (SLT): Required to work with a SAP Landscape Transformation Replication Server.
