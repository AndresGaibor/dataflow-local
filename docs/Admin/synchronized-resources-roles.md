---
title: "Synchronizing roles and permissions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/synchronized-resources-roles.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Synchronization between Qlik and Talend - Qlik Talend Cloud subscriptions"]
---

# Synchronizing roles and permissions

With a Qlik Talend Cloud subscription, Talend user roles and permissions are synchronized between Qlik Cloud and Talend Cloud. Synchronization helps administrators manage permissions consistently across both systems.

Information noteThis topic applies only to customers with a Qlik Talend Cloud subscription.

## Synchronization behavior

The following rules describe how roles and permissions are synchronized between Qlik Cloud and Talend Cloud:

- Custom roles are synchronized.

  - Both Qlik and Talend permissions can be assigned to custom roles.
  - Only Talend permissions are shown in Talend Management Console. Qlik permissions are visible only in Qlik Cloud.

  Information noteBe careful when adding users to roles synchronized from Qlik Cloud. These roles may include Qlik permissions that are not visible in Talend Management Console. Assigning users to such roles could unintentionally give them additional access in Qlik Cloud.
- Built-in Talend roles are synchronized.
- Built-in Qlik roles remain local.
- Roles assigned through groups or the Auto assign option in Qlik Cloud Administration are not synchronized to Talend Cloud. To synchronize users, assign the roles directly to individual users.
- Updating a role's name or changing which permissions are assigned to a role is reflected in both systems.
- Deleting a synchronized role in either system removes it from both.

  Information noteDeleting a synchronized role in Talend Management Console also deletes the corresponding role in Qlik Cloud. Because Qlik permissions are not visible in Talend Management Console, review the role in Qlik Cloud before deleting it to avoid removing permissions that are still in use.
- Adding a Talend permission to a role already assigned to many users (for example, more than 500) will create corresponding Talend Cloud accounts for those users. This may affect performance, so review the user impact before saving changes. Talend Management Console supports up to 999 users in total.

For more information, see:

- [*Synchronization between Qlik and Talend - Qlik Talend Cloud subscriptions*](synchronized-resources.htm)
- [*Roles and permissions for users and administrators*](permissions-admins-users-capacity-model.htm).

## How Talend roles appear in Qlik Cloud

In a synchronized setup, Qlik Cloud displays all roles from both Qlik Cloud and Talend Cloud.

- Talend roles appear as custom roles in the Administration activity center. These roles are labeled Role distributed from Talend.
- Talend permissions are grouped under the Talend Cloud permissions section in the custom roles settings. You can add these permissions to any custom role in Qlik Cloud.
- You can create, manage, and assign roles from both the Administration activity center and Talend Management Console.
- If two roles share the same name during the initial synchronization between Qlik Cloud and Talend Cloud, a number is appended to the Talend role in Qlik Cloud (for example, My user role 1). After initial synchronization, roles with the same name are automatically synchronized.

Information noteThe Security Administrator role in Talend Cloud is read-only. You cannot edit or delete this role in either system. To grant fewer permissions, create a custom role.

Tip noteUse a clear naming convention to help distinguish between local and synchronized roles.

## Example: Creating and assigning a synchronized role

This example shows what happens when a custom role with both Qlik and Talend permissions is created and assigned to a user.

1. An administrator creates a custom role in Qlik Cloud with Qlik and Talend permissions.
2. The role is assigned to a user in Qlik Cloud.
3. If the user does not exist in Talend Cloud, a Talend user account is created automatically.
4. In Talend Management Console, the user's Talend permissions are visible.
5. In Qlik Cloud, the user can perform actions allowed by Qlik permissions.
6. In Talend Cloud, the user can perform actions allowed by Talend permissions.
