---
title: "Tableau"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikLineageConnectors/connectors/tableau.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Delivering data and lineage for analytics", "Extracting lineage data with Qlik Lineage Connectors", "Qlik Lineage Connectors"]
---

# Tableau

Expand/Collapse all

# Tableau

The Tableau connector is used to connect to sites on Tableau Server and Tableau Online.

The connector will use the REST and Metadata APIs to extract lineage details on field level per workbook.

Server URL: URL including protocol to Tableau Server or Online.

Qlik Lineage Connectors
 use both the REST APIs and MetaData APIs. Verify that the MetaData API is enabled if connecting to Tableau Server.

Enable Metadata API on server by running the following command:

```
tsm maintenance metadata-services enable
```

Enabling Metadata API on server

![The result of enabling metadata API on the server. It reads: When enabling this option, some services used by Tableau Server must be restarted. This will make some functionality on Tableau Server temporarily unavailable. Do you want to continue?](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/NodeGraph/ui-NodeGraphTD-27.png "Click to view full size")

Site Content URL: List all sites' content URL to include, separated by a semicolon. Can be left empty for Tableau Server to include all sites but must include at least one site for Tableau Online. To include only the Tableau Server default site, which has an empty content URL, type only a semicolon.

Information noteContent URL is the sub path of a Tableau site's full URL. In the server environment, it is referred to as the Site ID. When you sign in to Tableau Server or Tableau Online manually, the content URL is the value that appears after /site/ in the Browser address bar.

For example, in the following URLs, the content URL is Sales:

- (Tableau Server) http://MyServer/#/site/Sales/projects
- (Tableau Online) https://10ax.online.tableau.com/#/site/Sales/workbooks

Authentication Method: Needs to be an existing user with permissions to read all metadata to extract, e.g. Server Administrator.

- Username and Password

  Specify an existing Tableau user credentials.
- PAT (Personal access token)

  Create a valid PAT for an existing user and enter name and secret.

Information notePAT is the recommended authentication method from a security perspective. Keep in mind, however, that the token needs to be renewed on a regular basis.

Full list of connector fields

Add a Tableau connector

| Field | Default or example input |
| --- | --- |
| System ID | ID |
| System name | Name |
| Description | Description (optional) |
| Server URL | https://nnxx.online.tableau.com |
| Site Content URLs | ;NA;EMEA (will include Default, NA, EMEA) |
| Authentication method | Username and Password |
| Connector Server Aliases | |
| System | ID |
| Server Name | mssql01-prod |
| Fully Qualified Domain Name | mssql01-prod.company.com |
| IP | 123.456.789.123 |
| DNS Name | mssql01-prod.company.com;mssql02-prod.company.com; |

## Tableau rules

Include Sites Filter: In case of multiple sites on a Tableau Server specify the sites to include in current rule.

Include Projects Filter: Specify specific projects to include in current rule.

Include Workbooks Filter: Specify specific workbooks to include in current rule.

Exclude Filter: Specify specific keywords used to exclude Sites/Projects/Workbooks.

Extract and show flows: When enabled, any published Flow metadata is extracted.

Information noteInclude filters are treated with a logical AND. For example, if a site and project filter is used, only the matching projects within the matching sites are included. If an include filter is left empty, all matches will be included. All filters can be typed as specific strings or as wildcard patterns. If multiple filters are wanted, they can be separated by a semicolon.

Full list of rule fields

Add a Tableau rule

| Field | Default or example input |
| --- | --- |
| Select rule type | Tableau Server/Online |
| Name | Enter a name for this rule |
| Description | Description (optional) |
| Include sites filter | NA; EMEA |
| Include projects filter | Sales; Marketing\* |
| Include workbooks filter | Sales; Marketing\* |
| Exclude filter | Dev; Test\* |
| Rule priority | Enter a processing priority for this rule |

## Folder Alias

A folder alias will synchronize the different references that a connector may read from. For example, an application may refer to a folder as \\mssql01-prod\sources but in a script it is referred to as \\mssql01-prod.company.com\sources. In this case, the two different references point to the same folder, but it will not appear like that in the lineage graphs. By adding the alias, the resource name will be synchronized, and the graphs will reconcile.
