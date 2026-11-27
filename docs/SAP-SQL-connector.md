---
title: "SAP NetWeaver"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Connectors_SAP/SAP-SQL-connector.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics"]
---

# SAP NetWeaver

The Qlik SAP NetWeaver connector efficiently loads data into a Qlik Sense application from SAP NetWeaver. The information may be stored in a number of different repositories within the SAP architecture, such as SAP BI/BW, SAP ERP, or CRM system.

Information note

The Qlik SAP NetWeaver connector is available with Qlik Cloud Government. It’s available with Qlik Cloud with an additional license.

It is not available with Qlik Sense Business or Qlik Cloud Analytics Standard.

You must have a SAP NetWeaver account with current access credentials. Once a connection to a SAP NetWeaver account has been created, data can be selected from tables available to the user’s account. The data you select is then loaded into an application where it can be used in visualizations.

Information noteFor a complete history of changes, see [Qlik Connector for use with SAP NetWeaver release notes](https://community.qlik.com/t5/Search-the-Community/bd-p/qlikSearchUnify?searchString=sap&from=0&sortby=_score&orderBy=desc&pageNo=1&aggregations=%5B%7B%22type%22%3A%22_type%22%2C%22filter%22%3A%5B%22forum%22%2C%22tkb%22%2C%22blog%22%5D%7D%2C%7B%22type%22%3A%22boardName%22%2C%22filter%22%3A%5B%22Release%2520Notes%22%5D%7D%2C%7B%22type%22%3A%22Product_category_flat%22%2C%22filter%22%3A%5B%22Qlik+SAP+Connectors%22%5D%7D%5D&uid=cb43fd48-5178-11eb-8a9b-0242ac120002&resultsPerPage=10&exactPhrase=&withOneOrMore=&withoutTheWords=&pageSize=10&language=en&state=1&suCaseCreate=false) on Community.

## Prerequisites when working with Qlik Data Gateway - Direct Access

Information note

To use SAP NetWeaver with Qlik Data Gateway - Direct Access, an additional license is required, but does not need to be installed.

When working with Qlik Data Gateway - Direct Access, make sure to fulfill the following prerequisites:

- Install the SAP NetWeaver RFC SDK on the Qlik Data Gateway - Direct Access machine as described in [*Installing SAP NetWeaver RFC SDK for Qlik Data Gateway - Direct Access*](Installation/Installing-sap-connectors-for-direct-access-gw.htm).
- These ports are used for communication by internal data gateway processes. If any of these ports is being used by another application, either reconfigure the other application or uninstall it.
  - 3007 (SAP BW Connector REST API)
  - 3008 (SAP SQL Connector REST API)
  - 50070 (SAP BW Connector gRPC)
  - 50080 (SAP SQL Connector gRPC)
- Microsoft Visual C++ 2013 Redistributable (x64) must be installed on the Qlik Data Gateway - Direct Access machine.

For more information on Qlik Data Gateway - Direct Access, see [Setting up Qlik Data Gateway - Direct Access](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/direct-access-gateway.htm).

## Supported connectors

This section lists the supported connectors. For a list of objects supported by each connector, see the section for that connector.

Qlik Cloud supports the following connectors only:

- [SAP BW connector](Clients/SAP-BW-connection.htm)
- [SAP SQL connector](Clients/Using-SAP-SQL-connection.htm)
- [SAP Report connector](Clients/Using-SAP-Report-connection.htm)
