---
title: "Managing permissions in shared spaces"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/managing-shared-spaces.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Collaborating with other users", "Working in spaces", "Working in shared spaces"]
---

# Managing permissions in shared spaces

Permissions in spaces are controlled by space roles assigned to members when they are added to a space. A role gives the member a set of permissions in the space and on resources in the space.

Members of a shared space can have multiple roles applied to them. This enables customized access to the space for each member. If groups are allowed in the tenant, groups of users can be added to a space with the same role. If a space member has different individual permission and group permission in a space, the highest permission level is applied.

When you create a space, you are assigned the Owner space role. Owners can then add new members to the space. Users with the Owner and Can manage space roles can assign permissions. Space permissions are managed in Space settings > Members.

Tip note

You can check your permissions in a shared space by clicking Space settings > Members. If you do not see Members, you have Can view, Can edit, Can edit data in applications, or Can consume data permission for the space.

Applications can be shared with non-space members. For more information, see [*Sharing applications with users who are not space members*](sharing-content-with-non-space-members.htm).

For details about the actions permitted by each available space role, see:

- [*Shared space permissions for Professional and capacity-based subscription users*](permissions-shared-space-prof-full.htm)
- [*Shared space permissions for users with Analyzer entitlement*](permissions-shared-space-analyzer.htm)
- [*Shared space permissions for administrators*](permissions-shared-space-admin.htm)

## Available roles in shared spaces

The following space roles are available in shared spaces:

- Owner: You are the first administrator that can manage the space and its members as well as create content in the space. You cannot edit load scripts of applications and scripts that you do not own—to do this, you need the Can edit data in applications space role.

  This role cannot be assigned to other members of the space unless you are an administrator. This space role also cannot be removed from the space member without administrator action. It is not possible to remove a member with the Owner role from the space, unless you have access to the Administration activity center as an administrator.
- Can manage: You can manage the space and its members as well as create content in the space. You cannot edit load scripts of applications and scripts that you do not own—to do this, you need the Can edit data in applications space role.
- Can edit: You can add and edit content in applications. You cannot manage the space and its membership.
- Can edit data in applications: You can add and edit content in applications, as well as edit the load script and business logic of applications in the shared space. You cannot manage the space and its membership.
- Can view: You can view applications in the space, but cannot create content or manage the space.
- Can consume data: You can consume data sources, but cannot create or edit data sources. They cannot create content or manage the space. See [*Adding and managing your analytics data*](managing-data-resources-spaces.htm#Managing) to learn about data sources inside a space.

## Changing permissions for members in shared spaces

Member permissions can be changed to give the user a new role in a space. A user with the Can view role might be changed to an application developer by changing their role to Can edit.

The space owner and members with the Can manage role can change members' permissions.

Information note

When you make any changes to user's permissions for applications or scripts, these changes are not instantly reflected in actively opened applications and scripts. To ensure that the changes to the user's permissions are updated, the user must close all browser tabs belonging to the affected application or script and wait at least two minutes (application session's Time To Live), then re-open the application. This applies to application and script permissions in personal, shared, and managed spaces. Changes in permissions for newly opened applications are reflected instantly.

Do the following:

1. In the space, click Space settings and select Members.
2. Click the arrow ![Arrow down](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_down.svg) in the Role column for the member.
3. Select the appropriate roles for the member.

## Common use cases

The following sections outline some common approaches you might want to follow when assigning roles to space members.

### I want to allow certain space members to develop analytics for consumption by others

To achieve this result, assign Can edit (or higher) permissions to content developers, and Can view permissions to content consumers.

With this configuration, content consumers are limited to what they can see and create in the space. They can create bookmarks, stories, notes, and other assets, but they will not be able to create their own applications and sheets.

### I want to allow space members to edit the data of other users' applications and scripts

To achieve this result, assign the Can edit data in applications role to specific users in the space. Users with this role are granted access to editing the data loaded by applications and scripts. They also have the ability to manage [business logic](#glossary-2 "Glossary term") and [distribution lists](#glossary-3 "Glossary term") in an application.

This role allows collaborative development of data models. It can also be used to allow other users to make changes to the source data of an application or script, in the event of its owner leaving the space or tenant, without the need for intervention by a tenant admin.

The owners of application and scripts also have these permissions.

### I want to allow space data to be used without giving users full access to the space

You might want data sources within the space to be accessible by certain users, without access to other space assets such as applications. Another requirement might be that you want to limit certain users' ability to manage data sources in a space, while still being able to use the existing data sources.

For either of these purposes, you can assign the Can consume data permission to specific data consumers.

For example, you could have a space dedicated to storing data sources. You could create a separate space for the development of applications using these data sources. You can assign Can consume data to users in the data source space, and then provide these users with application developer (Can edit) permissions in the development space. With this setup, the users are free to use the data sources to build analytics content, while allowing centralized data management.

## Space permissions and application ownership

Roles in a shared space give users permissions and access rules. Whether or not you are the owner of the application you are working with determines additional permissions.

The application owner is the user who has created the application. Only application owners and users with Can edit data in applications can edit data in Data model viewer, Data load editor, or Data manager. Application owners and users with Can edit data in applications are also the only users who can edit the application [business logic](#glossary-4 "Glossary term").

Space permissions override application ownership. If an application is moved to a space that the application owner does not have permission to access, then the application owner cannot access the application. If the application owner's role in a space is changed to Can view or Can consume data, they will lose the ability to add data to the application and reload the application. If an application owner does not have the Can edit data in applications role, they can edit their own applications' load scripts but not the load scripts of other applications in the space. When moving an application between spaces, ensure the application owner has the Can edit, Can edit data in applications, Can manage, or Owner role in the destination space, if you want the application owner to still manage reloading the application and the data model.

If your application has tasks for refreshing data, and you move it between spaces (personal or shared spaces), these tasks are deactivated. You can reactivate them when ready to resume the scheduled refreshes. See [*Activating and deactivating a task*](../Refresh/refresh-manage-tasks.htm#Activating).

## Space permissions and data sources

A data source in one space can be used in another space. For example, a user can create an application in a shared space using a data connection from their personal space. Certain space actions, however, require space members other than the resource owner to have access to the data source. In the previous example, other space members would not be able to reload the application as it uses a data connection from a personal space. Depending on your use case, this access control may or may not be desirable.

Generally, the owner of a data source is not granted any exemptions to the permissions governed by space roles. The only exception to this is the action of editing a data connection. Only the data connection owner can edit a connection. Each time a connection is edited, the user must re-authenticate themselves on the connection.

If the owner of a data connection loses the required access to the space or leaves the tenant, entities that rely on the connection will no longer be able to fetch new data from that connection. If the connection owner leaves the tenant, contact a tenant administrator to reassign connection ownership and move it to a new space as needed. If the connection owner is simply no longer a space member, another space member can re-create the connection.

The creator of a data file is assigned as its owner. The owner of a data file can be changed by an administrator. Ownership of data files does not affect access controls unless the data file is in a user's personal space. For more information about expected behavior, see [*Data file ownership*](../Admin/mc-administer-data-files.htm#DataFileOwnership).

The owner of a data file can leave the space and tenant, and other space members will continue to be able to view and use the file.

## Space permissions and automation ownership

The automation owner is the user who has created the automation, but other users may be able to see or run the automation. Only the automation owner can edit the automation.

Users with Can edit can see, run, and see the automation run history of automations in that space.

Users with Can manage can see, run, see the automation run history, manage the space and its membership, and additionally, can create content in that space.

Users with Can consume data can use automation connections. This means that a user can create an automation in space A and use a connection residing in space B if the user has been assigned the Can consume data role in space B.

## Space permissions and user entitlement

In user-based subscriptions (Qlik Sense Enterprise SaaS or Qlik Sense Business), what you can do depends on both your space roles and your user entitlement—Professional or Analyzer. Users with Analyzer entitlement have more limited permissions. We recommend that the space owner and members with the Can manage role have Professional entitlement.

In capacity-based subscriptions, only your assigned space roles determine what you can do in the space.

## Space permissions and global tenant roles

This section outlines how global tenant roles (assigned by an administrator) affect space permissions.

### Administrator roles

If you are assigned an administrator role in the Qlik Cloud tenant, your space permissions will be different from user permissions in the same spaces. The following general rules apply:

- An administrator will generally be able to view the resources in a space, manage space membership, and delete certain resources. They can create shared and managed spaces, and do not need the Shared Space Creator and Managed Space Creator security roles to do so. Administrators can also add themselves to spaces if needed.
- For other actions (for example, creating and editing content), the administrator role does not override space permissions, and the administrator needs to have sufficient roles in the space.

For more information, see:

- [*Assigning security roles and custom roles*](../Admin/SaaS-roles-capacity-model.htm) (capacity-based subscriptions)
- [*Assigning security roles and custom roles*](../Admin/SaaS-roles.htm) (user-based subscriptions)
- [*Assigning security roles and custom roles*](../Admin/SaaS-roles-anonymous.htm) (Qlik Anonymous Access subscriptions)

### Security roles

Certain actions require additional security roles to be assigned to you by an administrator. You might need the security role only, or a combination of security roles and space roles.

For example, to have full access to working with business glossaries, you need the Steward role, in addition to the required space roles.

For more information, see:

- [*Assigning security roles and custom roles*](../Admin/SaaS-roles-capacity-model.htm) (capacity-based subscriptions)
- [*Assigning security roles and custom roles*](../Admin/SaaS-roles.htm) (user-based subscriptions)
- [*Assigning security roles and custom roles*](../Admin/SaaS-roles-anonymous.htm) (Qlik Anonymous Access subscriptions)

## Troubleshooting

For solutions to common issues you might encounter when working in spaces, see [*Troubleshooting - Working in spaces*](../Troubleshooting/troubleshooting-spaces.htm).

Related learning:

- [Differentiate and manage Qlik Cloud spaces](/lnk/Differentiate_manage_spaces)
- [Administer and allocate space roles in Qlik Cloud](/lnk/Administer_allocate_space_roles)
