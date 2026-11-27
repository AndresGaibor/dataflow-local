---
title: "SAP (Application)"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/SAP-Application-DB/sap-application-source.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SAP sources"]
---

# SAP (Application)

This section explains how to set up a SAP (Application) source in a data task. Before you start the data task, make sure that you have fulfilled the [*Prerequisites*](../../../../Global_Common/Content/SharedReplicateHDD/SAP-Application-DB/native_Prerequisites.htm) and familiarized yourself with the [*Limitations and considerations*](../../../../Global_Common/Content/SharedReplicateHDD/SAP-Application-DB/native_Limitations_SAP_app.htm).

Information noteThis connector is supported with a Qlik Talend Cloud Enterprise subscription only.

## Setting connection properties

This section describes the available connection properties. All properties are required unless otherwise indicated.

To open the connector, do the following:

1. In Connections, click Create connection.
2. Select the SAP (Application) source connector and then provide the following settings:

### Data source

- Data gateway

  Select a Data Movement gateway to use for moving your data.

  For information on Data Movement gateway, see [*Qlik Data Gateway - Data Movement*](../../../Gateways/replication-gateway.htm).
- Client identifier: The client number of the SAP (Application) source you want to move data from.

### Database properties

- SAP schema:  The name of the relevant SAP schema.
- Backend database: Click the Browse button and then select the name of the data source connector you configured earlier.

  See also: [*Set up a source connector for SAP (Application)*](../../../../Global_Common/Content/SharedReplicateHDD/SAP-Application-DB/native_Set_up_a_Source_Endpoint_for_your_SAP_Application.htm).
- Non-Unicode SAP system: Select this option if your backend database is non-unicode.

### Internal properties

Internal properties are for special use cases and are therefore not exposed in the dialog. You should only use them if instructed by Qlik Support.

Use the ![Create new](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) and ![Cancel](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin.svg) buttons to the right of the fields to add or remove properties as needed.

### Name

The display name for the source connection.
