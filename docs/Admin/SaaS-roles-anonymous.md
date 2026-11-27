---
title: "Assigning security roles and custom roles"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/SaaS-roles-anonymous.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Managing users - Qlik Anonymous Access subscriptions", "Roles and permissions for users and administrators"]
---

# Assigning security roles and custom roles

Security roles and custom roles provide a set of [tenant](#glossary-0 "Glossary term")-level permissions to users and administrators. As a [tenant administrator](#glossary-1 "Glossary term"), you can assign roles manually from the Administration activity center or set up automatic role assignment.

Information note

This topic is applicable to Qlik Anonymous Access subscriptions. For other Qlik Cloud subscriptions, see:

- Standard, Premium, or Enterprise edition of Qlik Cloud Analytics or Qlik Cloud Data Integration: [*Managing users - Capacity-based subscriptions*](SaaS-user-management-capacity-model.htm)
- Qlik Sense Enterprise SaaS, Qlik Sense Business, or Qlik Cloud Government: [*Managing users - User-based subscriptions*](SaaS-user-management.htm)

Security roles control actions and access rights for users and administrators in the tenant. In addition to the tenant-level roles, there are also space roles that control user actions on content within spaces. For more information about the different types of roles, see [*Roles and permissions for users and administrators*](permissions-admins-users-anonymous.htm).

You can assign roles to individual users or groups of users from the Administration activity center.

Information note If users are logged in when they are assigned a role, they must log out and log in again for the role to be applied.

## Assigning security roles and custom roles to users

Tenant administrators can assign security roles from the All users tab or the Permissions tab and custom roles from the Permissions tab on the Manage users pane in the Administration activity center.

### Assigning a role from the All users tab

The All users tab shows a list of users who have been added or invited to the tenant. You can select one or more users to see all roles assigned to them.

Do the following:

1. In the Administration activity center, go to Manage users > All users.
2. Select one or more users and click Manage roles.
3. In the Manage roles dialog, select the roles you want to assign from the tabs for user and admin roles.
4. Click Save.

   The users will be assigned the role at their next login.

In the Manage roles dialog, icons indicate if a role is already assigned to a user through:

- Group assignment: The role is assigned to a group that the user is a member of. Hover over the icon to view a tooltip showing the groups.

  Role assigned to a user through group membership.

  ![Icon for role assigned via a group with a tooltip with the group name shown in the Manage roles dialog.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_role_group_assigned.png "Click to view full size")
- Auto-assign: The role is automatically assigned to all users in the tenant.

  Role automatically assigned to all users in the tenant.

  ![Icon for role assigned to Everyone in the tenant shown in the Manage roles dialog.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_role_everyone_assigned.png "Click to view full size")

### Assigning a role from the Permissions tab

On the Permissions tab, you see all available security roles and custom roles. You can select a role to see all users assigned to this role.

Do the following:

1. In the Administration activity center, go to Manage users > Permissions.
2. Click the arrow ![Arrow down](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_down.svg) on the role you want to assign.

   Assigning a role from the Users tab.

   ![Permissions tab with expanded role showing the Users tab](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_assign_roles_users.png "Click to view full size")
3. On the Users tab, click Assign.
4. Search for users by name or email and add them to the list.
5. Click Assign.

   The users will be assigned the role at their next login.

## Assigning security roles and custom roles to groups

Groups are defined through your identity provider or created from the Administration activity center. Tenant administrators can assign security roles and custom roles to groups from the Permissions tab on the Manage users pane in the Administration activity center. When you assign a role to a group, every member of that group is granted the permissions defined by the role.

Do the following:

1. In the Administration activity center, go to Manage users > Permissions.
2. Click the arrow ![Arrow down](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_down.svg) on the role you want to assign.

   Assigning a role from the Groups tab.

   ![Permissions tab with expanded role showing the Groups tab](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_assign_roles_groups.png "Click to view full size")
3. On the Groups tab, click Assign.
4. Search for groups by name and add them to the list.
5. Click Assign.

   The group members will be assigned the role at their next login.

Information noteIf users have roles assigned both individually and through group memberships, they might end up with duplicate role assignments. To remove a role from users, ensure that you unassign it from both the Permissions > Users tab and the Permissions > Groups tab.

## Assigning security roles and custom roles to everyone in the tenant

Tenant administrators can assign security roles and custom roles to all users in the tenant from the Auto assign column on the Permissions tab in the Administration activity center. A role assigned to a user this way is removed from the user if you set the value in the column to Off.

Do the following:

1. In the Administration activity center, go to Manage users > Permissions.
2. Find the role you want to assign to everyone and select Anyone at <your tenant name> in the Auto assign column.

   Assigning a role to everyone with the Auto assign option.

   ![Permissions tab with expanded menu with Auto assign options.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_assign_roles_anyone.png "Click to view full size")

   All users will be assigned the role at their next login.

For new tenants, the following settings apply to all users by default:

Roles (auto-assigned on the Permissions tab):

- Data Services Contributor
- Steward
- Private Analytics Content Creator
- Shared Space Creator
- Automl Experiment Contributor
- Automl Deployment Contributor

Permissions set to Allowed in the default permissions:

- Private Automations
- Shared Automations
