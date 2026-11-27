---
title: "Deleting users"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/SaaS-delete-users.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Managing users - User-based subscriptions"]
---

# Deleting users

You can delete users from the Manage users section of the Administration activity center.
Deleting an active or disabled user frees up a user entitlement that can be assigned to another user. Deleting a pending user removes the user record from the system, and they won't be able to register through the email invitation.

Information note

This topic is applicable to Qlik Sense Enterprise SaaS, Qlik Sense Business, and Qlik Cloud Government. If you have a subscription for the Standard, Premium, or Enterprise edition of Qlik Cloud Analytics or Qlik Talend Data Integration, see [*Managing users - Capacity-based subscriptions*](SaaS-user-management-capacity-model.htm).

When a user is deleted from Qlik Cloud, such as when they leave an organization, any assets they own will no longer have an owner. This can lead to application and script reload failures and other access issues. Make sure to reassign ownership of spaces, applications, scripts, and data connections that the deleted user owned to resolve these issues.

## What happens when you delete a user

Deleting a registered tenant user—a user with status Active or Disabled—has several implications beyond simply removing their entry from the Administration activity center. This section outlines the various aspects affected by the deletion, including their personal information, account status, and data ownership.

### User information of deleted users

When a user is deleted, all personally identifiable information is removed. If a user is deleted while logged in to the tenant, their session is invalidated.

### Deleted users who are part of an identity provider

When using your own identity provider, invalidating the user session doesn't prevent a deleted user from logging in again. If they attempt to log in after deletion, a new tenant user record is created, possibly leading to an automatic license assignment. To prevent this, remove the user from the identity provider. If you have configured your own identity provider, you can remove the user yourself.

### Qlik Account of deleted users

Users with a Qlik Account cannot log in after deletion from the tenant unless they are invited again. Deleting a user from the tenant does not remove them from Qlik Account.

### Consequences of deleting a user

- The user is no longer available in the tenant.
- API keys associated with the user are revoked.
- User entitlement becomes available for reassignment.
- Spaces, applications, scripts, and data connections must be reassigned to a new owner.
- If the user is the owner of a reload schedule, ownership must be reassigned or a new schedule created to prevent scheduled reload failures.
- Audit logs in the Administration activity center contain details of the deleted user event.
- Notifications and alerts owned by the user are deleted from the system.
- Automations and automation connections owned by the user are deleted from the system.

## Reassigning ownership of spaces and resources

When a user is deleted, any spaces, applications, scripts, and data connections they owned will remain in the tenant without an owner. To prevent orphaned records, reassign ownership of these assets before deleting the user. Additionally, ensure that reload schedules have a new owner, or the reloads will fail.

Tenant admins can change space ownership, reassign ownership of applications, scripts, and data connections, and move these resources to other spaces. Analytics admins can perform these actions in shared and managed spaces, and data admins in data spaces.

Do the following:

1. In the Administration activity center, go to Spaces.
2. Use the filter to locate spaces owned by the deleted user.
3. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to a space and select Change owner.
4. Specify a new owner of the space and click Apply.

Repeat the process for applications, scripts, or data connections in the Content page. For more detailed instructions on changing ownership and managing reload schedules, see the following topics:

- [*Managing applications for tenant and analytics administrators*](mc-administer-apps.htm)
- [*Managing scripts for tenant and analytics administrators*](mc-administer-scripts.htm)
- [*Managing data connections for administrators*](mc-administer-data-connections.htm)

Tip noteTo change the owner of a published application, you need to change the owner of the source application and then republish it. The published copy of the application will inherit the owner of the source application. If the source application has been deleted, see [*The source application for a published application was deleted*](../Troubleshooting/troubleshooting-spaces.htm#The) for more information.

## Deleting a user from the tenant

As a tenant admin, you can delete users from the tenant. You can only delete one user at a time, and you cannot delete yourself as a user. Make sure to remove the user from your identity provider, if applicable, and reassign any resources owned by the user before deletion.

Do the following:

1. In the Administration activity center, open Manage users.
2. In the row for the user to be deleted, click the ![Three dot icon](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) button to the far right.
3. Select Delete to delete an existing user or Delete invitation to delete an invitee.
4. Confirm the deletion.
