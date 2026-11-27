---
title: "QlikView"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikLineageConnectors/connectors/qlikview.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Delivering data and lineage for analytics", "Extracting lineage data with Qlik Lineage Connectors", "Qlik Lineage Connectors"]
---

# QlikView

Expand/Collapse all

# QlikView

QlikView connectors are used to connect a QlikView environment.

Session Log Paths: The UNC Path for the QlikView Server Session logs. By default, it is located under:

\\QLIKVIEW-SERVER\c$\ProgramData\QlikTech\QlikView

Load session data: Check when using the session log path. Activates reading of the log path.

Create user nodes: When checked, it extracts user information from the session logs and binds them to each published application.

User session days back: How many days back to look for content.

Max parallel workers: This is the maximum number of folders that can be simultaneously scanned. It is recommended best practice to keep the default value. You can increase this number depending on the processing capabilities of your network. A higher number provided better sync performance if reading from disk is slow. However, this can increase memory usage.

Full list of connector fields

Add QlikView connector

| Field | Default or example input |
| --- | --- |
| System ID | ID |
| System name | Name |
| Description | Description (optional) |
| Maximum parallel workers | 1 |
| Connector Server Aliases | |
| System | ID |
| Server Name | mssql01-prod |
| Fully Qualified Domain Name | mssql01-prod.company.com |
| IP | 123.456.789.123 |
| DNS Name | mssql01-prod.company.com;mssql02-prod.company.com; |

## QlikView rules

There are two rule categories for QlikView: Directory rules and Folder alias references.

### Directory Rules

Path: Locate the files that you would like to associate with this rule. UNC is recommended. You can enter a wildcard in the path, ex. c:\qlikview\data\\*\qvw

Scan subfolders: By selecting this option, Qlik Lineage Connectors will include subfolders in the given path.

Include filter: You can use a fully qualified name like sales.qvw or a wildcard like \*.qvw, \*.xlsx, etc.

Exclude filter: You can use a fully qualified name like data.qvd or a wildcard like \*.qvd. If you want to exclude more than one file or folder, use ; to separate them.

Create link in Qlik Cloud: By selecting this option, a link to lineage data will populate into the specified managed space in the target tenant.

Full list of rule fields

Add a QlikView application rule

| Field | Default or example input |
| --- | --- |
| Select rule type | QlikView application rule |
| Name | Enter a name for this rule |
| Description | Description (optional) |
| Path | Enter a path for this rule |
| Include filter | \*.qvw; ... |
| Exclude filter | old\_report.qvw; se\_\*.qvw |
| Rule priority | Enter a processing priority for this rule |

## Folder Alias

A folder alias will synchronize the different references that a connector may read from. For example, an application may refer to a folder as \\qlik-sense\QVD but in a script it is referred to as \\qlik-sense.local.corp\QVD. In this case, the two different references point to the same folder, but it will not appear like that in the lineage graphs. By adding the alias, the resource name will be synchronized, and the graphs will reconcile.
