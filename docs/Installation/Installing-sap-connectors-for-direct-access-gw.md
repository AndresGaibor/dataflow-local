---
title: "Installing SAP NetWeaver RFC SDK for Qlik Data Gateway - Direct Access"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Connectors_SAP/Installation/Installing-sap-connectors-for-direct-access-gw.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "SAP NetWeaver", "SAP Connectors installation"]
---

# Installing SAP NetWeaver RFC SDK for Qlik Data Gateway - Direct Access

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
