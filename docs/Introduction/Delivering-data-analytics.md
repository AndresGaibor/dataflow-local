---
title: "Delivering data and lineage for analytics"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/Delivering-data-analytics.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data"]
---

# Delivering data and lineage for analytics

Qlik also provides options to load lineage and on-premises data into your Qlik Cloud tenant.

## Uploading on-premises data

Qlik DataTransfer is a departmental utility that enables you to upload data from on-premises data sources to Qlik Cloud. You can manually upload files or schedule data for updates.

Tip noteQlik recommends using the Qlik Data Gateway - Direct Access to load data from on premises into a Qlik Cloud tenant. The supported databases and the Generic ODBC Connector Package, together with the support for loading on premises files, can allow you to decommission Qlik DataTransfer servers (and potentially repurpose them for gateways).

New users are encouraged to use the File connector via Direct Access gateway and only use Qlik DataTransfer if absolutely necessary. For more information, see [Qlik Data Gateway - Direct Access](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/direct-access-gateway.htm) and [File (via Direct Access gateway)](/en-US/cloud-services/Subsystems/Web_Storage_Provider_Connectors_help/Content/Connectors_StorageProvider/Storage%20provider%20connectors/File-DG-storage-provider-connector.htm).

The following data sources are supported:

- [Data connections](#glossary-0 "Glossary term") from your QlikView or Qlik Sense Enterprise on Windows deployment.
- Qlik Sense or QlikView applications.
- Data files from local folders or network shared folders.

[*Uploading on-premises data with Qlik DataTransfer*](../QlikDataTransfer/qlik-datatransfer.htm)

## Extracting lineage data

Qlik Lineage Connectors expand Qlik's lineage capabilities to include lineage information from BI tools and data sources— increasing data trust and improving operational continuity and efficiency. These tools can eliminate time-consuming processes to manually document the data journey across multiple systems.

Qlik Lineage Connectors extract lineage and metadata from Qlik sources, relational databases, and BI solutions:

- Microsoft Power BI
- Tableau
- Snowflake
- Azure SQL database
- MS SQL Server
- MS SQL Server Integration Services
- Oracle database

[*Extracting lineage data with Qlik Lineage Connectors*](../QlikLineageConnectors/qlik-lineageconnectors.htm)
