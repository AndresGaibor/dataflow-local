---
title: "SAP Connector configuration"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Connectors_SAP/Configuration/Connector-configuration.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "SAP NetWeaver"]
---

# SAP Connector configuration

Each of the connectors that comprise the Qlik Connector for use with SAP NetWeaver must be configured separately. Prior to configuring individual connectors, set the port, if necessary, and consider whether the connector will pass through a Message server or a firewall.

## Passing through a Message server

### Direct setting of the message server port

When creating a new connection through a message server, you can set the port directly through the connection dialog using the System ID / Port parameter. The Port number is of the form 36nn where nn is the system number.

See [*Using the SAP SQL Connector*](../Clients/Using-SAP-SQL-connection.htm)

## Passing through a firewall

If there is a firewall between the connector and the SAP system, port 33nn has to be open (where nn = system number of the SAP system).

After the transports have been installed in the system, configuration of the SAP system must be completed for each of the installed connectors.

Predefined roles are included in the user profile transports. The roles can be adjusted to fit specific purposes and needs.

[*Access authorization*](Access-authorization.htm)
