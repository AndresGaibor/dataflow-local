---
title: "REST data sources"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/REST_Connector_help/Content/Connectors_REST/REST-connector.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics"]
---

# REST data sources

The Qlik REST Connector enables Qlik Cloud to efficiently load data into applications from a REST data source. Many web-based data sources expose data through a REST API. The Qlik REST Connector is a generic connector, that is, it is not tailored to a specific REST data source.

There are variations in the way the REST API is implemented by different data sources that use it. Users must learn the requirements of each data source. The Qlik REST Connector provides connection options to accommodate those varied requirements. To help understand how to use those options, documentation for the REST Connector includes use cases that illustrate how to load data from different REST sources.

[*Setting up selected REST sources for data loading*](Create-REST-connection/Connection-examples.htm)

[*Using pagination with selected REST sources*](Create-REST-connection/Pagination-scenarios.htm)

To access data, the user must have authorization with current access credentials to the data source. Once a connection to a REST data source has been created, data can be selected from tables available to the user’s account and then loaded into an application where it can be used in visualizations.

Information noteThis data source is not available in Qlik Sense Business or Qlik Cloud Analytics Standard.

## Accessing REST sources via Qlik Data Gateway - Direct Access

The REST connector appears twice in the Create data connection dialog. Once as REST and once as REST (via Direct Access gateway), which is the one you need to select. Qlik Data Gateway - Direct Access eliminates the need to open inbound firewall ports, allowing Qlik Cloud applications to securely access firewalled data. If your REST data sources are located behind a firewall and can be accessed via Qlik Data Gateway - Direct Access, it is strongly recommended to connect to them via the Direct Access gateway.

Information noteUsers that need to leverage gateway-enabled data connections must have the Can Consume Data permission for the space in which the gateway resides.

For more information on Qlik Data Gateway - Direct Access, see [Data gateways](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/direct-access-gateway.htm).

## Supported REST data types

The REST Connector supports the following data types:

- JSON data
- XML data
- CSV files

## Supported REST authentication methods

The REST Connector supports the following authentication methods:

- Windows authentication
- Basic and Digest authentication schema
- X509 certificates

The REST Connector does not support OAuth schema authentication.

## Supported REST Connector ciphers

When making use of the TLS Cipher Suite, only the following ciphers can be used with the REST Connector:

- ECDHE-ECDSA-AES256-GCM-SHA384
- ECDHE-ECDSA-AES128-GCM-SHA256
- ECDHE-RSA-AES256-GCM-SHA384
- ECDHE-RSA-AES128-GCM-SHA256
- ECDHE-ECDSA-AES256-SHA384
- ECDHE-ECDSA-AES128-SHA256
- ECDHE-RSA-AES256-SHA384
- ECDHE-RSA-AES128-SHA256
