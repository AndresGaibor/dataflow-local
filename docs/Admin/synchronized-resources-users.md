---
title: "Synchronizing users"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/synchronized-resources-users.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Synchronization between Qlik and Talend - Qlik Talend Cloud subscriptions"]
---

# Synchronizing users

With a Qlik Talend Cloud subscription, users are automatically synchronized between Qlik Cloud and Talend Cloud. Synchronization helps administrators manage users and permissions consistently across both systems.

Information noteThis topic applies only to customers with a Qlik Talend Cloud subscription.

In a synchronized setup, Qlik Cloud displays all users from both Qlik Cloud and Talend Cloud. The Talend Management Console shows only the subset of users required for Talend services.

## How user accounts are synchronized

Synchronization of user accounts follows specific rules to keep users and their roles aligned between Qlik Cloud and Talend Cloud.

- A user in Qlik Cloud is synchronized to Talend Cloud only if they have at least one Talend role or a custom role with Talend permissions.
- Assigning a Talend role or permission to a user in Qlik Cloud triggers synchronization.

  Information noteRole assignments made through groups or the Auto assign option are not synchronized to Talend Cloud. For more information, see [*Synchronizing roles and permissions*](synchronized-resources-roles.htm).
- Once synchronized, users remain in both systems even if their assigned permissions are later removed.
- When you invite a user to Talend Cloud, the user appears in Qlik Cloud with only their email address until they sign in for the first time.
- If a user with the same email address exists in both systems, the accounts are automatically linked.
- Role assignments are synchronized.
- Changes to user status are synchronized.
- Users created in Talend Cloud consume a Qlik Cloud user entitlement.
- User groups are not synchronized.

For more information, see:

- [*Synchronization between Qlik and Talend - Qlik Talend Cloud subscriptions*](synchronized-resources.htm)
- [*Managing users - Capacity-based subscriptions*](SaaS-user-management-capacity-model.htm)
- [Managing users](https://help.qlik.com/talend/en-US/management-console-user-guide/Cloud/tmc-user-management) (Talend Help)

## Deleting users

When you delete a user who has been synchronized between Qlik Cloud and Talend Cloud, the following applies:

### Deleting users in Qlik Cloud

Deleting a user in the Qlik Cloud Administration activity center removes the user from both systems.

### Deleting users in Talend Cloud

Deleting a user in Talend Management Console removes the user only from Talend Cloud. The user account remains active in Qlik Cloud, with all previously assigned roles and space permissions. The user can continue to access Qlik Cloud and work in their spaces, but can no longer access Talend Cloud.

If an administrator later assigns a role to the user that includes Talend permissions, the user is synchronized again. This restores their access to Talend Cloud, along with any previous roles and space permissions.

To prevent restoring access, administrators should remove any roles containing Talend permissions after deleting the user from Talend Management Console.

## Editing user profile details

Users can edit their profile information, such as name, job title, and phone number, and on the shared Account page. This page is accessible from the profile menu in both Qlik Cloud and Talend Cloud.

For more information, see [*Editing your user profile*](../Introduction/manage-user-profile.htm).
