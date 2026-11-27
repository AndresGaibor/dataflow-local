---
title: "Adding data connections"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataSource/add-data-connections.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Adding and managing your analytics data"]
---

# Adding data connections

Add connections to data sources that can be used in data analytics. There are a number of ways in which you can create data connections in Qlik Cloud Analytics.

## Adding new connections

For information about supported connections, see [*Loading analytics data*](../LoadData/connect-data-sources.htm).

Do the following:

1. Go to the Create page of the Analytics activity center and select Data connection.

   You can also add datasets from your mini-homes and by clicking Create new > Data connection in Catalog.
2. Select a destination space for the connection.
3. Select a data connector.

   The settings dialog, specific for the type of data source you selected, opens.
4. Enter the connection settings for the data source.
5. Optionally, click Test connection to confirm your settings.
6. Click Create.

## Other ways to add data connections

There are many other ways in which you can create connections in Qlik Cloud Analytics. For example, it is often possible to add a connection as you build specific analytics resources.

Common methods include:

- When managing a space.

  [*Adding data connections to spaces*](../Spaces/manage-data-connections-spaces.htm#AddDataConnection)
- When building applications and scripts. You can use Data load editor, Data manager, or the Script interface to create connections.
- When you build a [knowledge base](#glossary-0 "Glossary term") in Qlik Answers.

## Managing data connections in spaces

For more information about managing the data files within a space, see [*Managing data connections*](../Spaces/manage-data-connections-spaces.htm).

## Permissions

Whether you can create data connections is determined by the following permissions:

- Permissions assigned to you by an administrator.

  [*Assigning permissions for users to work with data connections*](../Admin/mc-administer-data-connections.htm#Permissions)
- Space permissions: Control access to data connections in specific spaces. See below for more information.

In addition to administrator-assigned permissions, space permissions further control your access to data connections in shared, managed, and data spaces. You still need the administrator-assigned permissions before you can add data connections to a space.

Shared space members with any of the following roles can create data connections in that space:

- Owner (of the space)
- Can manage
- Can edit data in applications
- Can edit

Managed space members with any of the following roles can create data connections in that space:

- Owner (of the space)
- Can manage

Space members with the Can consume data role can view data connections in the space, and they can consume the data connections where they have permission to create applications.

Information noteThe Can consume data role is a space-level role that gives members of a space permission to view and consume the data sources stored in that space. The benefit of this role is that you can allow users to access data files and data connections in your space, without giving them the elevated permissions they would normally require to access data sources inside a space.

For more information about the space role requirements for data source actions, see:

- [*Shared space permissions for Professional and capacity-based subscription users*](../Spaces/permissions-shared-space-prof-full.htm)
- [*Shared space permissions for users with Analyzer entitlement*](../Spaces/permissions-shared-space-analyzer.htm)
- [*Shared space permissions for administrators*](../Spaces/permissions-shared-space-admin.htm)
- [*Managed space permissions for Professional and capacity-based subscription users*](../Spaces/permissions-managed-space-prof-full.htm)
- [*Managed space permissions for users with Analyzer entitlement*](../Spaces/permissions-managed-space-analyzer.htm)
- [*Managed space permissions for administrators*](../Spaces/permissions-managed-space-admin.htm)

For information about required space roles for working with data connections in data spaces, see [*Data space roles and permissions*](../DataIntegration/DataSpaces/permissions-data-space.htm).
