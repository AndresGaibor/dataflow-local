---
title: "Secure network communication"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Connectors_SAP/Secure-network-communication.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "SAP NetWeaver"]
---

# Secure network communication

Secure Network Communication (SNC) is the SAP technology used for safe communication between SAP components. If the customer has SNC installed, this can also be used for the RFC communication between the connector and the SAP system.

A cryptographic library must be installed on the connector machine. This is not supplied by Qlik. The technology is used between SAP components only. For technical details, see the SAP Help Portal: [http://help.sap.com](http://help.sap.com/).

## Using SNC

Do the following:

1. Open Control Panel > System>Advanced.
2. Create a system variable, SNC\_Lib, to hold the path to a local cryptography library. The environment variable SECUDIR must already be set.

   ![Windows System Properties menu, Advanced tab, with Environment Variables dialog opened and SECUDIR variable set to library path](_images/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Resources/Images/ui_system-variable.png)

   When using the SAP SQL Connector, SAP InfoProvider Connector, and the BEx Connector, you can override the system variable SNC\_Lib by adding the environment variable QLIK\_SNC\_LIB to specify the full path and name of a cryptographic library.
3. Specify the SNC Name in the connection dialog, p:sncname. In addition, specify the quality of the protection. The available values are specific to the library used.

The parameter SNC Lib is used to specify the full path and name of a 64 bit cryptographic library. This parameter is optional.

Information noteThe parameter overrides the environment variable SNC\_Lib, allowing the variable to hold the path to a 32 bit library for use with the SAP GUI.

The Quality parameter defaults to the highest available security.
