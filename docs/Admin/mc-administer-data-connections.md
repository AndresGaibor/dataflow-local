---
title: "Managing data connections for administrators"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-data-connections.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Managing resources"]
---

# Managing data connections for administrators

If you are [tenant admin](#glossary-0 "Glossary term"), analytics admin, or [data admin](#glossary-1 "Glossary term"), you can manage [data connections](#glossary-2 "Glossary term") in the Administration activity center, under Content > Data connections.

## Administrator access levels for managing data connections

Tenant, analytics, and data administrators have different levels of access to data connections:

- Tenant administrators: Can manage all data connections in managed, shared, data, and personal spaces.
- Analytics administrators: Can manage data connections in managed and shared spaces. Cannot manage data connections in other users' personal spaces.
- Data administrators: Can manage data connections in data spaces. Cannot manage data connections in other users' personal spaces.

## Data connections

The Data connections tab on the Content page displays data connections in the tenant, including name, owner, space, type, and dates for creation and update.

- Hover over ![Information](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_info_outline.svg) in the Owner column to see owner details. This can be useful for distinguishing between two owners with the same name.
- You can filter by name, owner, space, and dates for creation and update. To filter by date, click ![Filter](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_filter2.svg) in the Date created or Last updated columns and set a start and end date in the date picker.

If a data connection type no longer is supported, its type is presented as Obsolete and it cannot be used.

Information noteData connections for Automations are not present in the Data connections table.

## Moving data connections

A tenant admin, analytics admin, or data admin can move data connections in the Administration activity center.

A typical case where you would want to move a data connection is when the owner of a data connection has quit and someone else needs to take ownership of the data connection.

Moving a data connection will affect applications that use the data connection and the application users. It is important to ensure that application users can continue working with the applications after a move. Reloads might need to be recreated and data connection credentials reinstated. When you move a data connection, both you (the admin) and the data connection owner must both have, at minimum, edit permissions on the space to which you are moving the data connection.

Data connections can be moved between shared, managed, and data spaces. A tenant admin, analytics admin, or data admin can move a data connection, from any of the space types to which they have access, to their personal space.

Do the following:

1. In the Administration activity center, go to Content > Data connections.
2. Select one or more data connections.
3. Note the users who are the owners of the connections.
4. In the upper-right corner, click Move.
5. Click the search box and select or search for the target space for the data connection.
6. Click Move.

   - If the move is successful, you are ready.
   - If an error occurs, ensure the requirements are met for moving the data connection to the target space:

     - [*Requirements for moving a data connection to a shared space*](#RequirementsSharedMove)
     - [*Requirements for moving a data connection to a managed space*](#RequirementsManagedMove)

### Requirements for moving a data connection to a shared space

- You must have a value of Allowed for the Data connections permission. This is assigned in the Users section of the Administration activity center.

  [*The Data connections permission*](#TenantWide)
- You and the data connection owner must have one of the following space roles in the target shared space:

  - Owner
  - Can manage
  - Can edit
  - Can edit data in applications

  For information about how to manage members in spaces, see [*Managing spaces*](mc-administer-spaces.htm).

### Requirements for moving a data connection to a managed space

- You must have a value of Allowed for the Data connections permission. This is assigned in the Users section of the Administration activity center.

  [*The Data connections permission*](#TenantWide)
- You and the data connection owner must have one of the following space roles in the target managed space:

  - Owner
  - Can manage

  For information about how to manage members in spaces, see [*Managing spaces*](mc-administer-spaces.htm).

## Changing the owner of a data connection

You can change the owner of a data connection in the Administration activity center. Changing the data connection owner can only be done by an admin in the Administration activity center.

Only the owner of a data connection can edit that connection. Therefore, if a user who owns a data connection leaves or is removed from the tenant, the only way to modify this data connection is by changing its ownership.

To use the connection for loading or selecting data, the new connection owner must authenticate the connection by entering credentials.

Do the following:

1. In the Administration activity center, go to Content > Data connections.
2. Select one or more data connections.
3. In the top right corner, click Change owner.
4. Click the search box and start typing the name or email of the user who you want to make the new connection owner. Select their name when it appears.
5. Click the checkbox to acknowledge the warning regarding possible consequences of changing the ownership of the connection.
6. Click Apply.

   - If the action is successful, the ownership has been changed. If needed, the new connection owner can now edit the data connection in the catalog.
   - If an error occurs, ensure the requirements are met:

     - [*Requirements for connections in shared spaces*](#RequirementsSharedOwnership)
     - [*Requirements for connections in managed spaces*](#RequirementsManagedOwnership)

### Requirements for connections in shared spaces

To change the owner of a data connection in a shared space, you must have one of the following space roles in the space:

- Owner (of the space)
- Can manage
- Can edit
- Can edit data in applications

For information about how to manage members in spaces, see [*Managing spaces*](mc-administer-spaces.htm).

### Requirements for connections in managed spaces

To change the owner of a data connection in a shared space, you must have one of the following space roles in the space:

- Owner (of the space)
- Can manage

For information about how to manage members in spaces, see [*Managing spaces*](mc-administer-spaces.htm).

## Ownership when moving data connections

What happens with the ownership of a data connection depends on whether you move the data connection to your personal space or to another space.

### Moving the data connection to your personal space

When you move a data connection to your personal space, you will become the new owner of the data connection. User defined credentials for the data connections are kept, other credentials are reset and need to be re-authenticated.

### Moving the data connection to a space different from your personal space

When you move a data connection to a space which isn't your personal space, no ownership changes will occur. The previous owner remains as owner and credentials are intact. However, when you move a data connection where the owner has been deleted, you will always become the new owner, regardless of where you move the data connection. Credentials are reset.

Information noteYou cannot move a data connection to another user's personal space.

## Deleting data connections

Deleting a data connection will affect applications that use the data connection and the application users. It is important to ensure that application users are informed and can take necessary actions.

Do the following:

1. In the Administration activity center, go to Content > Data connections.
2. Select one or more data connections.
3. In the top right corner, click Delete.
4. In the Delete data connection window, acknowledge the deletion.
5. Click Delete.

Tip noteYou can also use the context menu to delete a single data connection.

## Assigning permissions for users to work with data connections

Tenant administrators configure the Data connections permission to control which users can work with data connections. See [*The Data connections permission*](#TenantWide).

For users to work with data connections in their personal spaces, tenant administrators need to assign them Data connections permissions and a security role. See [*Personal spaces*](#PersonalSpace).

### The Data connections permission

The Data connections permission controls which users can work with data connections. You can configure whether each user in the tenant has full, partial, or no access to working with data connections.

For the Data connections permission, the following options are available:

- Allowed: Users can list, create, view, update, and delete data connections. Users can also read data from, and store data to, these connections.

  With Allowed, users can also edit data connections that they own. For data connections they do not own but that have User defined credentials, they can manage their own credentials.
- Read: Users can view data connections, select and load data from connections, and store data to data connections.

  With Read, users cannot create or edit connections, but they can manage their own credentials for connections that have User defined credentials.
- Not allowed: Users cannot create, view, update, or delete data connections. Users also cannot read data from, or store data to, these connections.

Information noteThe Data connections permission requirements apply to all users in the tenant, including tenant, analytics, and data administrators.

The Data connections permission is configured in the Administration activity center through two processes:

- Creating custom roles. See:

  - [*Creating custom roles*](permissions-custom-roles-capacity-model.htm#Creating) (capacity-based subscriptions)
  - [*Creating custom roles*](permissions-custom-roles.htm#Creating) (user-based subscriptions)
  - [*Creating custom roles*](permissions-custom-roles-anonymous.htm#Creating) (Qlik Anonymous Access subscriptions)
- Configuring the default permissions. See:

  - [*Default permissions*](permissions-admins-users-capacity-model.htm#UserDefault) (capacity-based subscriptions)
  - [*Default permissions*](permissions-admins-users.htm#UserDefault) (user-based subscriptions)
  - [*Default permissions*](permissions-admins-users-anonymous.htm#UserDefault) (Qlik Anonymous Access subscriptions)

For information about the available permissions, see:

- [*Default permissions and custom roles*](permissions-scopes-capacity-model.htm) (capacity-based subscriptions)
- [*Default permissions and custom roles*](permissions-scopes.htm) (user-based subscriptions)
- [*Default permissions and custom roles*](permissions-scopes-anonymous.htm) (Qlik Anonymous Access subscriptions)

### Personal spaces

For users to work with data connections in their personal spaces, a tenant administrator needs to assign them the following:

- The required value for the Data connections permission. See [*The Data connections permission*](#TenantWide).
- The Private Analytics Content Creator security role. See:

  - [*Assigning security roles and custom roles*](SaaS-roles-capacity-model.htm) (capacity-based subscriptions)
  - [*Assigning security roles and custom roles*](SaaS-roles.htm) (user-based subscriptions)
  - [*Assigning security roles and custom roles*](SaaS-roles-anonymous.htm) (Qlik Anonymous Access subscriptions)

### Interaction with space permissions

User access to working with data connections in shared, managed, and data spaces is further controlled by their space roles in these spaces. For more information, see:

- [*Shared space permissions for Professional and capacity-based subscription users*](../Spaces/permissions-shared-space-prof-full.htm)
- [*Managed space permissions for Professional and capacity-based subscription users*](../Spaces/permissions-managed-space-prof-full.htm)
- [*Data space roles and permissions*](../DataIntegration/DataSpaces/permissions-data-space.htm)
