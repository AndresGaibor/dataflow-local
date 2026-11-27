---
title: "Adding Qlik Connector for use with SAP NetWeaver to Qlik DataTransfer"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikDataTransfer/sap-qlik-datatransfer.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Managing data governance and transfers", "Installing Qlik DataTransfer"]
---

# Adding Qlik Connector for use with SAP NetWeaver to Qlik DataTransfer

By default, the Qlik Connector for use with SAP NetWeaver is not available as a [data connection](#glossary-0 "Glossary term") in Qlik DataTransfer. You can, however, upload data from an application that already has a connection to SAP NetWeaver.

The Qlik Connector for SAP NetWeaver must be installed on the same machine as Qlik DataTransfer. For installation instructions for the QlikConnector for use with SAP NetWeaver, see [SAP Connector installation](/en-US/connectors/Subsystems/SAP_Connectors_Help/Content/Connectors_SAP/Installation/Connector-installation.htm). Once the connector is installed, you can then configure Qlik DataTransfer to support uploading data from an application with a SAP NetWeaver connection.

Do the following:

1. After installing the Qlik Connector for use with SAP NetWeaver, navigate to C:\Program Files\Common Files\Qlik\Custom Data\.
2. Copy the following folders:
   - QvSAPBAPIConnector
   - QvSAPBExConnector
   - QvSAPExtractorConnector
   - QvSAPInfoProviderConnector
   - QvSAPSqlConnector
3. Navigate to C:\Program Files\Qlik\DataTransfer\Connectors\.
4. Paste the copied folders.
5. Restart the Qlik DataTransfer service.
6. In Qlik DataTransfer, add an existing application that contains a SAP connection in Qlik apps.
7. Reload the Qlik application.

You can now load data from that application with Qlik DataTransfer.

Information note

SAP will be listed in Data connections in Qlik DataTransfer, but it will not function. You must use SAP NetWeaver inside an existing application containing a SAP connection for Qlik DataTransfer.
