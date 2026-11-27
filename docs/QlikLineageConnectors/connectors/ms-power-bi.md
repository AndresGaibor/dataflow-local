---
title: "Microsoft Power BI Services"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikLineageConnectors/connectors/ms-power-bi.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Delivering data and lineage for analytics", "Extracting lineage data with Qlik Lineage Connectors", "Qlik Lineage Connectors"]
---

# Microsoft Power BI Services

Expand/Collapse all

# Microsoft Power BI Services

Power BI connectors are used to connect a Power BI environment.

Qlik Lineage Connectors support Power BI Cloud. It is important to install Power BI Desktop on the same machine as the Qlik Lineage Connectors service; this is required to parse reports. Power BI Desktop does not need to be licensed but it must be installed local to Qlik Lineage Connectors so that it can leverage the Microsoft framework in order to communicate with Power BI Cloud to extract required metadata. Typically, both applications are installed on a windows machine though both applications can also be installed on the same Windows server. Note the [*Microsoft Power BI Services*](#Prerequi) step where after install of Power BI Desktop, the location of Power BI must be entered in Qlik Lineage Connectors in General Settings > Service (tab) > Power BI.

## Prerequisites

Qlik Lineage Connectors
 uses a Master User to access Power BI resources. You will need to register a user in the Azure Active Directory, set it as Power BI service administrator and add access to all Power BI workspaces.

1. Install Power BI desktop locally. Go to General Settings in Qlik Lineage Connectors and locate the last setting in General Settings : POWER BI DESKTOP BINARY FOLDER. Enter the path where Power BI Desktop was installed: C:\Program Files\Microsoft Power BI Desktop\bin
2. Register Qlik Lineage Connectors in Azure Active Directory.
3. Apply permissions to your application within Azure AD.
4. Set up Power BI Connector in Qlik Lineage Connectors.

### Register Qlik Lineage Connectors in Azure Active Directory Using the Power BI Application Registration Tool:

1. Go to dev.powerbi.com/apps
2. Select Sign in with your existing account then select Next.
3. Provide an Application Name, i.e. Qlik Lineage Connectors
4. Select Native as Application Type.
5. API Access select all Read only APIs.
6. Click register.
7. Save the Application ID.

Power BI application ID

![Power BI registration success message](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_QLC_PowerBI_RegSucc.png "Click to view full size")

### Apply permissions to Qlik Lineage Connectors within Azure AD

1. Search or browse for App registrations within the [Azure portal](http://portal.azure.com/ "Azure portal") and select the app (ex., Qlik Lineage Connectors).
2. Select API permissions under Manage.
3. Within API permissions, select Add a permission, then select Power BI Service.

Power BI API Permissions

![Add a permission at the top left of the screen, and Power BI Service at the bottom right.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/NodeGraph/ui-NodeGraphTD-20.png "Click to view full size")

1. Add all Read.All APIs under Delegated Permissions. Select them one by one to save the selections. Select Save when done.
2. Select Grant Consent.

The Grant Consent action is needed for the master account to avoid being prompted for consent by Azure AD. If the account performing this action is a Global Admin, you grant permissions to all users within your organization for this application. If the account performing this action is the master account and is not a Global Admin, you grant permissions only to the master account for this application. Note: Grant Consent may take some time. Check permissions in Azure App Registration under API Permissions:

Power BI consent granted

![A list of all Power BI permissions and whether they require consent.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/NodeGraph/ui-NodeGraphTD-21.png "Click to view full size")

### Set up Power BI Connector in Qlik Lineage Connectors

Full list of connector fields

Add powerbi\_service connector

| Field | Default or example input |
| --- | --- |
| System ID | ID |
| System name | Name |
| Description | Description (optional) |
| Client ID | None |
| User | None |
| Password | None |
| Connector Server Aliases | |
| System | ID |
| Server Name | mssql01-prod |
| Fully Qualified Domain Name | mssql01-prod.company.com |
| IP | 123.456.789.123 |
| DNS Name | mssql01-prod.company.com;mssql02-prod.company.com; |

1. In Qlik Lineage Connectors, go to Connector Settings -> Connectors -> New Connector.
2. Add a new Microsoft Power BI Services Connector and add Client ID (Application ID), User and Password.
3. Click Test to test the connection.
4. Save.

#### Supported Power BI Environments

Qlik Lineage Connectors include support for three Microsoft cloud environments: Commercial, GCC (Government Community Cloud), and GCC High. You will need to change the default Power BI Authentication URIs to access the GCC/GCC High environments with Qlik Lineage Connectors.

##### Commercial

- Use the default settings
- Leave "Override Power BI Authentication URIs" cleared

##### GCC

- Select "Override Power BI Authentication URIs"
- Set "Authentication Authority" to: https://login.microsoftonline.com/organizations/
- Set "Authentication Resource" to: https://analysis.usgovcloudapi.net/powerbi/api
- Set "Base API URI" to: https://api.powerbigov.us

##### GCC High

- Select "Override Power BI Authentication URIs"
- Set "Authentication Authority" to: https://login.microsoftonline.com/organizations/
- Set "Authentication Resource" to: https://high.analysis.usgovcloudapi.net/powerbi/api
- Set "Base API URI" to: https://api.high.powerbigov.us

Power BI Authentication URIs

![Authentication settings for PowerBI.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/NodeGraph/ui-QLC_powerbi_auth_uri.png "Click to view full size")

## Microsoft Power BI rules

Workspaces: List of workspaces to extract.

Reports IDS: Individual report IDs to extract.

Full list of rule fields

Add a Power BI rule

| Field | Default or example input |
| --- | --- |
| Select rule type | Power BI Cloud rule |
| Name | Enter a name for this rule |
| Description | Description (optional) |
| Workspaces | WorkspaceGuid1; WorkspaceName\*; ... |
| Reports IDs | Id1; Id2; Id3... |
| Rule priority | Enter a processing priority for this rule |

## Folder Alias

A folder alias will synchronize the different references that a connector may read from. For example, an application may refer to a folder as \\mssql01-prod\sources but in a script it is referred to as \\mssql01-prod.company.com\sources. In this case, the two different references point to the same folder, but it will not appear like that in the lineage graphs. By adding the alias, the resource name will be synchronized, and the graphs will reconcile.
