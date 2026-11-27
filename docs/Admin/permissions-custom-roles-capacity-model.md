---
title: "Managing custom roles"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/permissions-custom-roles-capacity-model.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Managing users - Capacity-based subscriptions", "Roles and permissions for users and administrators"]
---

# Managing custom roles

Create custom roles in Qlik Cloud with specific permissions for individuals or groups. Custom roles can be assigned in the same way as built-in security roles and extend default permissions.

Information note

This topic is applicable to the Standard, Premium, and Enterprise editions of Qlik Cloud Analytics and Qlik Talend Data Integration. If you have a Qlik Sense Enterprise SaaS, Qlik Sense Business, or Qlik Cloud Government subscription, see [*Managing users - User-based subscriptions*](SaaS-user-management.htm).

Custom roles extend default permissions. When assigning a custom role to users, permissions can only be added, not removed. A custom role cannot restrict a permission that is allowed by default. The permission remains allowed for everyone.

For each permission, the custom role shows the default setting, for example, (Default) Not allowed. This indicates the permission level that applies when the custom role does not override the default setting.

For more information about how default permissions interact with custom roles, see [*Roles and permissions for users and administrators*](permissions-admins-users-capacity-model.htm).

Information noteRoles and permissions apply to both UI and API access. When designing roles for API integrations, consider that API access may support operations beyond those visible in the UI. For more information, see [API access control and trust boundaries](https://qlik.dev/manage/access-control/api-trust-boundaries/).

## Creating custom roles

Tenant administrators can create new roles and configure permissions using the options described in [*Default permissions and custom roles*](permissions-scopes-capacity-model.htm).

Do the following:

1. In the Administration activity center, go to Manage users.
2. On the Permissions tab, click Create new.
3. In the Create new role dialog, enter a name and description for the role.
4. Use the search to find specific permissions.

   Tip noteYou can use the List all and Selected buttons to show all available permissions or only the selected ones.
5. Each permission shows its default setting, such as (Default) Allowed or (Default) Not allowed. Choose the desired access level for the permissions you want to add.
6. Click Create.

You can now assign your role to users or groups in the system. For more information, see [*Assigning security roles and custom roles*](SaaS-roles-capacity-model.htm).

## Editing custom roles

Tenant administrators can edit custom roles.

Do the following:

1. In the Administration activity center, go to Manage users.
2. On the Permissions tab, find the role you want to edit.
3. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg), then select Edit.
4. In the Edit role dialog, update the name or description and add or remove permissions as needed.
5. Click Save changes.

## Deleting custom roles

Tenant administrators can delete custom roles. Before deletion, make sure to unassign any users or groups associated with the role.

Do the following:

1. In the Administration activity center, go to Manage users.
2. On the Permissions tab, find the role that you want to delete.
3. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg), then select Delete.
4. Select the checkbox to confirm the deletion, and then click Delete role.

## Learn more

- [Creating custom roles in Qlik Cloud](https://share.vidyard.com/watch/RvVi46XWMzbCVZnrBFCyUU)
