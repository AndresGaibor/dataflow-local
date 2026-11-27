---
title: "SAP OData"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/SAP-ODATA/sap-odata-properties.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SAP sources"]
---

# SAP OData

This topic explains how to set up a SAP OData source in a data task. Before you start the data task, make sure that you have fulfilled the [*Prerequisites*](sap-odata-prereq.htm), set the [*Required permissions*](sap-odata-permissions.htm), and familiarized yourself with the [*Limitations and considerations*](sap-odata-limitations.htm).

Information noteThis connector is supported with a Qlik Talend Cloud Enterprise subscription only.

## Setting connection properties

This section describes how to set up connection parameters to your SAP OData source.

To open the connector, do the following:

1. In Connections, click Create connection.
2. Select the SAP OData source connector and then provide the connection settings described below.

### Data source

- Data gateway

  Select a Data Movement gateway to use for moving your data.

  Information noteRequires Data Movement gateway 2025.5.22 or later.

  For information on Data Movement gateway, see [*Qlik Data Gateway - Data Movement*](../../../Gateways/replication-gateway.htm).
- Host

  The host name of the SAP Gateway on which the SAP OData source is located.

  Information noteTo use HTTPS, you must specify a host name, not an IP address.
- Port

  The port number for HTTPS protocol in the SAP Gateway.
- Client identifier

  The SAP client number used for the OData service call.

### Account properties

- User Name

  A user in the SAP system with the required permissions (type ‘Communications Data’).
- Password

  The password for the specified user.
- Certificate file

  The full path to the certificate file for connecting to the SAP Gateway server using SSL. If you don't have the certificate file, contact your SAP system administrator. Note that the file must be in .pem format.

### Source properties

- Max records per request

  The size of the data package in records. This value can be adjusted according to your network and system capabilities. A background job is started for paging, and the data is cached in the operational delta queue. Using the odata.maxpagesize value, you can specify the quantity of packages to be retrieved from the delta queue.

  For more information, see [Using the OData Service for Extracting ODP Data](https://help.sap.com/doc/saphelp_nw75/7.5.5/en-US/50/f4ee6253134d3cafa25b9444f0c5a9/frameset.htm).
- SAP services URI

  The URI for accessing your SAP services. The default value is /sap/opu/odata/SAP/.

### Internal properties

Internal properties are for special use cases and are therefore not exposed in the dialog. You should only use them if instructed by Qlik Support.

Use the ![Create new](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) and ![Cancel](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin.svg) buttons to the right of the fields to add or remove properties as needed.

### Name

The display name for the source connection.
