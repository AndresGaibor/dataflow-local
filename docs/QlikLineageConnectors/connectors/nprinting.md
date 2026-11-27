---
title: "Qlik NPrinting"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikLineageConnectors/connectors/nprinting.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Delivering data and lineage for analytics", "Extracting lineage data with Qlik Lineage Connectors", "Qlik Lineage Connectors"]
---

# Qlik NPrinting

Expand/Collapse all

# Qlik NPrinting

Qlik NPrinting connectors are used to connect a Qlik’s NPrinting reports.

Connection string: The connection string to connect to your NPrinting server. The connection string will look like this:

Host=10.0.1.4;Port=4992;Username=postgres;Password=NPprintingMasterPassword;Database=nprinting

To allow incoming calls, you need to configure the services on the NPrinting side as well. See Appendix 1 – Configuring NPrinting for more information.

Test: Verifies the connection string, and that it can connect to Qlik NPrinting Service.

Full list of connector fields

Add qlik\_nprinting connector

| Field | Default or example input |
| --- | --- |
| System ID | ID |
| System name | Name |
| Description | Description (optional) |
| Connection string | hOST=LOCALHOST;pORT=4992;uSERNAME=postgres;Password+;Database=nprinting |
| Connector Server Aliases | |
| System | ID |
| Server Name | mssql01-prod |
| Fully Qualified Domain Name | mssql01-prod.company.com |
| IP | 123.456.789.123 |
| DNS Name | mssql01-prod.company.com;mssql02-prod.company.com; |

## Qlik NPrinting rules

Full list of rule fields

Add a Qlik NPrinting rule

| Field | Default or example input |
| --- | --- |
| Select rule type | NPrinting Rule |
| Name | Enter a name for this rule |
| Description | Description (optional) |
| App filter | Filter on desired apps, \*AppName\* |
| Rule priority | Enter a processing priority for this rule |

## Folder Alias

A folder alias will synchronize the different references that a connector may read from. For example, an application may refer to a folder as \\qlik-sense\QVD but in a script it is referred to as \\qlik-sense.local.corp\QVD. In this case, the two different references point to the same folder, but it will not appear like that in the lineage graphs. By adding the alias, the resource name will be synchronized, and the graphs will reconcile.
