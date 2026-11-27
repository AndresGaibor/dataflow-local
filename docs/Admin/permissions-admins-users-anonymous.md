---
title: "Roles and permissions for users and administrators"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/permissions-admins-users-anonymous.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Managing users - Qlik Anonymous Access subscriptions"]
---

# Roles and permissions for users and administrators

Users’ permitted actions in Qlik Cloud are determined by their roles. A role is a set of permissions that can be assigned to individuals or groups of users. By assigning roles, you can better organize your users and what they can do in the tenant. The roles can be changed at any time. Anonymous users received limited permissions to view publicly shared application

Information note

This topic is applicable to Qlik Anonymous Access subscriptions. For other Qlik Cloud subscriptions, see:

- Standard, Premium, or Enterprise edition of Qlik Cloud Analytics or Qlik Cloud Data Integration: [*Managing users - Capacity-based subscriptions*](SaaS-user-management-capacity-model.htm)
- Qlik Sense Enterprise SaaS, Qlik Sense Business, or Qlik Cloud Government: [*Managing users - User-based subscriptions*](SaaS-user-management.htm)

Access control in Qlik Cloud is divided between tenant-wide roles and space roles. Understanding how they interact is essential for effectively managing user access. Tenant-wide roles authorize actions across the entire tenant, and space roles grant access to content in specific spaces. The roles on tenant level include built-in security roles and custom roles created by administrators. Additionally, all users have a set of universally applied default permissions.

## Security roles

Security roles provide access to different capabilities in Qlik Cloud. Security roles are divided into administrator roles and user roles.

- Administrator roles enable management of tenant-wide functions that affect governance, performance, and security.
- User roles enable access to features in the tenant and actions on resources, such as creating spaces or accessing personal content.

For more information about the permissions granted with each role, see [*Permissions granted by security roles*](SaaS-user-permissions-anonymous.htm).

## Default permissions

Default permissions grant baseline permissions to all users in the tenant. Tenant administrators configure them in the Manage default permissions dialog. Default permissions determine what users can do in Qlik Cloud. Custom roles can extend these permissions for specific users.

Tenant administrators need to decide what permissions everyone should have and assign additional permissions based on users' work requirements through roles. As a best practice, follow these steps to ensure secure access control for specific features:

1. Create a custom role tailored to users who require access to the feature, assigning them appropriate permissions.
2. In the default permissions settings, remove default access to the feature to prevent unintended users from accessing it.

This approach ensures users have the right permissions to do their job without granting unnecessary access, and reduces disruptions for users who need to use the feature.

### Managing default permissions

Tenant administrators can manage the default permission levels.

Do the following:

1. In the Administration activity center, go to Manage users > Permissions.
2. Click Manage default permissions above the table.
3. Add or remove permissions as needed.

   Tip noteYou can use the List all and Selected buttons to show all available permissions or only the selected ones.
4. Save the changes.

   Information note Users must log out and log in again for the changes to be applied.

The permission configuration options are described in [*Default permissions and custom roles*](permissions-scopes-anonymous.htm).

## Custom roles

Custom roles give administrators the flexibility to define roles tailored to specific needs, for example access to capabilities where special knowledge is required or where capacity is limited. These roles complement the built-in security roles, providing additional granularity in managing permissions on both tenant level and individual level.

Custom roles extend permissions beyond those granted by the default permissions. When assigning a custom role to users, permissions can only be added, not removed.

For more information on how to create custom roles, see [*Managing custom roles*](permissions-custom-roles-anonymous.htm).

## Space roles

Space roles determine what a user can do with the content in a specific space. Spaces are sections of Qlik Cloud used to collaboratively develop and control access to resources such as applications or automations. The roles are defined at the space level and apply only to content within that space.

For more information on space roles, see:

- [*Managing permissions in shared spaces*](../Spaces/managing-shared-spaces.htm)
- [*Managing permissions in managed spaces*](../Spaces/managing-managed-spaces.htm)
- [*Data space roles and permissions*](../DataIntegration/DataSpaces/permissions-data-space.htm)
- [Administer and allocate space roles in Qlik Cloud](/lnk/Administer_allocate_space_roles)

## How default permissions interact with custom roles

Custom roles add permissions beyond those allowed by default, but cannot revoke permissions. Attempting to restrict a permission that is allowed by default has no effect. The permission remains allowed for everyone.

The table shows the permission levels that a custom role can grant, based on the corresponding default permission. Each custom role permission also shows the default setting, for example, (Default) Allowed.

How custom role permissions align with default permissions

| Configured default permission level | Possible custom role permission level |
| --- | --- |
| Allowed | Allowed |
| Not allowed | Any available permission level |
| Other permission levels | The same or a higher permission level |

For details on the permission levels, see [*Default permissions and custom roles*](permissions-scopes-anonymous.htm).

As an example, suppose the default permissions allow all users to manage links. If you create a custom role, this permission appears as (Default) Allowed. You do not need to configure it in the custom role because it is already allowed by default.

Everyone can manage links.

![Illustration of how default permissions and custom role permissions interact](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_user_default_custom_role.png "Click to view full size")

If you want to restrict managing links to certain users, such as Lisa and Tom, first create a custom role with Manage links set to Allowed and assign the role to Lisa and Tom. Then, change the permission to Not allowed in the default permissions. With this configuration, the permission is no longer allowed by default, but Lisa and Tom retain the permission through their custom role.

Only Lisa and Tom can manage links.

![Illustration of how default permissions and custom role permissions interact](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_user_default_custom_role-2.png "Click to view full size")

## How security roles interact with the Data Integration subscription

The Data Integration subscription gives you access to the Data Integration home and to security roles specifically designed for data admins and [data spaces](#glossary-0 "Glossary term").
