---
title: "Qlik Sense"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikLineageConnectors/connectors/qliksense.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Delivering data and lineage for analytics", "Extracting lineage data with Qlik Lineage Connectors", "Qlik Lineage Connectors"]
---

# Qlik Sense

Expand/Collapse all

# Qlik Sense

Qlik Sense connectors are used to connect a Qlik Sense Enterprise on Windows environment.

QRS Location: QRS URL to repository service. Ex. https://servername:4242/qrs

Engine Location: URL to Qlik Sense engine. Ex. https://servername:4747

Server name: In Sense QMC, go to Configure System > Nodes and double click on central/main node to edit. Check that hostname from QMC matches the folder under: C:\Program Data\Qlik\Sense\Repository\Archived Logs. If the server names are different, then you should use the one under the path above.

Data Path: The location of your Qlik Share (UNC Location). This is by default \\SERVER-NAME\QlikShare. It should match the configuration in your QMC.

Use client certificate from certificate store: An alternative way of referring to your Qlik Sense Certificate. Requires thumbprint.

Client Certificate: Export the certificate and place it on the disk. Enter the full path to the file.

Certificate password: If you export your certificate with a password, enter the password here.

Use Qlik Core Metadata API (experimental): Connects to the Core Metadata. Used to get distinct values / number of values per field from your datasets.

Qlik Engine API Directory and Qlik Engine API User: The credentials for the user used to connect to the APIs. As we use the certificate to talk to Qlik Sense, this is the user we identify ourselves as.

Session log paths: The UNC Path for the Engine Session logs. By default, it is located under:

\\QLIK-SENSE-SERVER\QlikShare\ArchivedLogs\QLIK-SENSE-SERVER\Engine\Trace

Load session data: Check when using the session log path. Activates reading of the log path.

Create user nodes: Extract user information from the session logs and bind them to each published application.

User session days back: How many days back to look for content.

Max parallel workers: This is the maximum number of folders that can be simultaneously scanned. It is recommended best practice to keep the default value. You can increase this number depending on the processing capabilities of your network. A higher number provided better sync performance if reading from disk is slow. However, this can increase memory usage.

Test: Controls access to DataPath, QRS, Engine and verifies the configuration.

Full list of connector fields

Add qlik\_sense connector

| Field | Default or example input |
| --- | --- |
| System ID | ID |
| System name | Name |
| Description | Description (optional) |
| QRS location | https://servername:4242/qrs |
| Qlik Sense Engine Location | https://servername:4747 |
| Server name | None |
| Data path | C:\Qlikshare |
| Client certificate | C:\ProgramData\Qlik\Sense\Repository\Exported Certificates\<servername>\Client.pfx |
| Certificate password | None |
| Qlik Engine API Directory | INTERNAL |
| Qlik Engine API User | sa\_reporting |
| Maximum parallel workers | 1 |
| Connector Server Aliases | |
| System | ID |
| Server Name | mssql01-prod |
| Fully Qualified Domain Name | mssql01-prod.company.com |
| MAX PARALLEL WORKERS | 1 |
| IP | 123.456.789.123 |
| DNS Name | mssql01-prod.company.com;mssql02-prod.company.com; |

## Qlik Sense application rules

Streams: Name of the stream. Can be “;”-separated and wild-carded.

Tags: Name of the tag. Can be “;”-separated and wild-carded.

Applications: Must be the exact AppID. These can be “;”-separated and wild-carded.

Exclude Applications: Must be the exact AppID. These can be “;”-separated and wild-carded.

Create link in Qlik Cloud: By selecting this option, a link to lineage data will populate into the specified managed space in the target tenant.

Information noteA note about Streams, Tags and Applications: these are treated as logically OR. For example, if Streams is \*Sales\* and Tags is \*Europe\*, all applications in Sales\_NorthAmerica, Sales, Purchase\_Europe, and Europe will be matched.

Full list of rule fields

Add a Qlik Sense Application rule

| Field | Default or example input |
| --- | --- |
| Select rule type | Qlik Sense application rule |
| Name | Enter a name for this rule |
| Description | Description (optional) |
| Streams | Stream1; Stream2; ... |
| Tags | Tag1; Tag2; ... |
| Applications | Id1; Id2; ... |
| Exclude applications | Id1; Id2; ... |
| Rule priority | Enter a processing priority for this rule |

## Folder Alias

A folder alias will synchronize the different references that a connector may read from. For example, an application may refer to a folder as \\qlik-sense\QVD but in a script it is referred to as \\qlik-sense.local.corp\QVD. In this case, the two different references point to the same folder, but it will not appear like that in the lineage graphs. By adding the alias, the resource name will be synchronized, and the graphs will reconcile.
