---
title: "Managing data connections"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/manage-data-connections-spaces.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Adding and managing your analytics data"]
---

# Managing data connections

In Qlik Cloud Analytics, you can manage the data connections in spaces from Space settings > Connections. Manage data connections in the Data connections tab.

This help topic focuses on managing data connections. For information about managing automation connections, see [*Connections*](navigating-spaces.htm#Connecti) and [Automation connections](/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/introduction/navigating-UI.htm#connections).

## Adding data connections to spaces

You can add connections to data sources while managing a space. Network File System (NFS) connections cannot be added directly in a space and must be added in an application.

For information about supported connections, see [*Loading analytics data*](../LoadData/connect-data-sources.htm).

Do the following:

1. In a space, click Space settings and select Connections.

   The Data connections tab is open by default.
2. Click Add connection.
3. By default, the data connection is set to be created in the current space, but you can change this to a different space if needed.
4. Select a data connector.

   The settings dialog, specific for the type of data source you selected, opens.
5. Enter the connection settings for the data source.
6. Optionally, click Test connection to check your settings.
7. Click Create.

## Editing data connections

You can edit existing data connections. User credentials are cleared each time you edit a connection.

To edit a data connection, you need the space permissions to manage data sources in the space (see [*Managing data connections*](#SpacePermissions)). You also need to be the connection owner.

Do the following:

1. In a space, click Space settings and select Connections.

   The Data connections tab is open by default.
2. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to the data connection you want to edit, and select Edit.

   The settings dialog, specific for this type of data connection, opens.
3. Edit the connection settings for the data source.
4. Click Save.

## Editing connection credentials

Some data connectors support User defined credentials. With proper permissions, you can add, edit, and remove your own sets of credentials for a data connection, including for connections you do not own.

For more information, see the connectors documentation at [Data sources in Qlik Cloud Analytics](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Helpsites/Connectors_SaaS.htm).

Do the following:

1. In a space, click Space settings and select Connections.

   The Data connections tab is open by default.
2. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to a data connection that has User defined credentials turned on, and select Edit credentials.

   A dialog opens.
3. In the drop down menu, select an existing credentials set to edit, or create new credentials.

   You can also delete existing credentials.
4. Edit the credential settings.
5. Click Save.

Connection credentials can also be edited in the Data load editor and Script interface, including by users with only Can consume data access to the space.

## Deleting data connections

Do the following:

1. In a space, click Space settings and select Connections.

   The Data connections tab is open by default.
2. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to the data connection you want to delete, and select Delete.
3. In the dialog, click Delete to confirm the deletion.

## Moving data connections

Once a data connection has been created in a space, it is not possible to move the connection to another space unless you have access to the Administration activity center as a tenant admin, analytics admin, or data admin.
To move an existing data connection to another space, contact an administrator or create a new connection in the desired space with the same settings as the existing connection.

For documentation about how an administrator can move a connection, see [*Moving data connections*](../Admin/mc-administer-data-connections.htm#Moving).

## Permissions

Whether you can manage data connections is determined by the following permissions:

- Permissions assigned to you by an administrator: Control whether you can view or manage data connections across the tenant.

  [*Assigning permissions for users to work with data connections*](../Admin/mc-administer-data-connections.htm#Permissions)
- Space permissions: Control access to data connections in specific spaces. See below for more information.

In addition to administrator-assigned permissions, space permissions further control your access to data connections in shared, managed, and data spaces. You still need the administrator-assigned permissions before you can manage data connections in a space.

Data connections are a type of data source in Qlik Cloud Analytics.

Shared space members with any of the following roles can manage data sources in that space:

- Owner
- Can manage
- Can edit
- Can edit data in applications

Managed space members with any of the following roles can manage data sources in that space:

- Owner
- Can manage
- Can operate

Information noteFor user-based subscriptions, the Can operate role also requires a Professional user entitlement.

Space members with the Can consume data role can view data sources in the space, and they can consume the data sources where they have permission to create applications They can also edit user credentials for certain connections from the Data load editor or Script interface.

Information noteThe Can consume data role is a space-level role that gives members of a space permission to view and consume the data sources stored in that space. The benefit of this role is that you can allow users to access data files and data connections in your space, without giving them the elevated permissions they would normally require to access data sources inside a space.

For more information about the space role requirements for data source actions, see:

- [*Shared space permissions for Professional and capacity-based subscription users*](permissions-shared-space-prof-full.htm)
- [*Shared space permissions for users with Analyzer entitlement*](permissions-shared-space-analyzer.htm)
- [*Shared space permissions for administrators*](permissions-shared-space-admin.htm)
- [*Managed space permissions for Professional and capacity-based subscription users*](permissions-managed-space-prof-full.htm)
- [*Managed space permissions for users with Analyzer entitlement*](permissions-managed-space-analyzer.htm)
- [*Managed space permissions for administrators*](permissions-managed-space-admin.htm)

For information about required space roles for working with data connections in data spaces, see [*Data space roles and permissions*](../DataIntegration/DataSpaces/permissions-data-space.htm).

## Administering data connections

Tenant administrators and analytics administrators can manage all data connections in the space from the Administration [activity center](#glossary-0 "Glossary term"). For more information, see [*Managing data connections for administrators*](../Admin/mc-administer-data-connections.htm).
