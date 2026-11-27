---
title: "Managing custom roles"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/permissions-custom-roles.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Managing users - User-based subscriptions", "Roles and permissions for users and administrators"]
---

# Managing custom roles

Create custom roles in Qlik Cloud with specific permissions for individuals or groups. Custom roles can be assigned in the same way as built-in security roles and extend default permissions.

Information note

This topic is applicable to Qlik Sense Enterprise SaaS, Qlik Sense Business, and Qlik Cloud Government. If you have a subscription for the Standard, Premium, or Enterprise edition of Qlik Cloud Analytics or Qlik Talend Data Integration, see [*Managing users - Capacity-based subscriptions*](SaaS-user-management-capacity-model.htm).

Custom roles extend default permissions. When assigning a custom role to users, permissions can only be added, not removed. A custom role cannot restrict a permission that is allowed by default. The permission remains allowed for everyone.

For each permission, the custom role shows the default setting, for example, (Default) Not allowed. This indicates the permission level that applies when the custom role does not override the default setting.

For more information about how default permissions interact with custom roles, see [*Roles and permissions for users and administrators*](permissions-admins-users.htm).

Information noteRoles and permissions apply to both UI and API access. When designing roles for API integrations, consider that API access may support operations beyond those visible in the UI. For more information, see [API access control and trust boundaries](https://qlik.dev/manage/access-control/api-trust-boundaries/).

## Creating custom roles

Tenant administrators can create new roles and configure permissions using the options described in [*Default permissions and custom roles*](permissions-scopes.htm).

Do the following:

1. In the Administration activity center, go to Manage users.
2. On the Permissions tab, click Create new.
3. In the Create new role dialog, enter a name and description for the role.
4. Use the search to find specific permissions.

   Tip noteYou can use the List all and Selected buttons to show all available permissions or only the selected ones.
5. Each permission shows its default setting, such as (Default) Allowed or (Default) Not allowed. Choose the desired access level for the permissions you want to add.
6. Click Create.

You can now assign your role to users or groups in the system. For more information, see [*Assigning security roles and custom roles*](SaaS-roles.htm).

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

## Replacing deprecated built-in roles

Some built-in roles are being deprecated and will be removed in a future release. To avoid losing access to features, you must replace these roles with custom roles that include the same permissions. In some cases, you can use the default permissions to make specific permissions available to all users.

### Permissions required for replacements roles

Use the following table to identify which permissions to include in the custom role.

Deprecated roles and their required permissions

| Deprecated built-in role | Required permissions | Available in default permissions |
| --- | --- | --- |
| Automation Creator | Private Automations (set to Allowed) | Yes |

Tip noteYou can combine multiple permissions in a single custom role or create separate roles for each permission—depending on how you want to manage access.

### Creating a replacement role

To create and assign a replacement custom role:

1. In the Administration activity center, go to Manage users.
2. On the Permissions tab, select Create new.
3. Name the role using your organization's naming convention.
4. Add the permissions listed in the table above.
5. Assign the role to users or groups who previously had the deprecated role.
6. Remove the deprecated role from those user or groups.

### Finding users and groups with deprecated roles

To identify users or groups assigned to deprecated roles, see [*Auditing user roles and access*](permissions-auditing-capacity-model.htm).

### Best practices for role replacement

- Migrate all users and groups before the deprecated role is removed to avoid disruptions in access.
- Review custom roles regularly to ensure they follow your organization’s security and access policies.

## Learn more

- [Creating custom roles in Qlik Cloud](https://share.vidyard.com/watch/RvVi46XWMzbCVZnrBFCyUU)
