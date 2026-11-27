---
title: "Supported compression methods"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/Content/SharedReplicateHDD/Oracle/Supported_Compression_Methods.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "Oracle"]
---

# Supported compression methods

The table below lists which compression methods Qlik Talend Data Integration supports when working with an Oracle source database. As the table shows, compression support depends on whether Qlik Talend Data Integration is configured to use Oracle LogMiner to access the redo logs.

Supported compression methods

| Redo log access method | Basic | OLTP | HCC | Others |
| --- | --- | --- | --- | --- |
| Log Reader | Yes | Yes | Yes  Information note When the Oracle source connector is configured to use Log Reader, the Query Low level of the HCC compression method is only supported in the Full Load task mode. | No |
| Oracle LogMiner | Yes | Yes | Yes | Yes (Any compression method supported by Oracle LogMiner) |
