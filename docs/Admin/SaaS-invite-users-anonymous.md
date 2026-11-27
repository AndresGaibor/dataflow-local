---
title: "Adding users to a Qlik Anonymous Access tenant"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/SaaS-invite-users-anonymous.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Managing users - Qlik Anonymous Access subscriptions"]
---

# Adding users to a Qlik Anonymous Access tenant

The individual who creates the [tenant](#glossary-0 "Glossary term") is the [service account owner](#glossary-1 "Glossary term"). If you are the service account owner, you are also the first [tenant administrator](#glossary-2 "Glossary term") and the only tenant user with access to the tenant. Add more tenant users by sending email invitations or configure an identity provider. Anonymous users are not added to the tenant, but instead access public content as an external user with minimal, view-only permissions.

Information note

This topic is applicable to Qlik Anonymous Access subscriptions. For other Qlik Cloud subscriptions, see:

- Standard, Premium, or Enterprise edition of Qlik Cloud Analytics or Qlik Cloud Data Integration: [*Managing users - Capacity-based subscriptions*](SaaS-user-management-capacity-model.htm)
- Qlik Sense Enterprise SaaS, Qlik Sense Business, or Qlik Cloud Government: [*Managing users - User-based subscriptions*](SaaS-user-management.htm)

You can add tenant users by configuring an identity provider (IdP), or by sending individual email invitations, but not both. However, when you switch from using the invite option to using an identity provider configuration, the invite option will remain available until the identity provider has been activated.

Ensure that tenant users can meet the Qlik Cloud requirements. For more information, see [*System requirements and supported browsers*](../Introduction/qcs-supported-browsers.htm).

## Terminology on this page

The following terminology is used in content about anonymous access:

- Anonymous users: Users who are accessing application content without signing in, either through anonymous access links to an application or by consuming embedded analytics anonymously. These users are not members of the Qlik Cloud tenant, and also do not require Qlik accounts.
- Tenant users: Users who are members of the tenant and manage the tenant or develop analytics for consumption by anonymous users. Tenant users may have administrator privileges in the tenant.

## Adding users with an identity provider

If you have an identity provider (IdP), you can create an IdP configuration under Identity provider in the Administration activity center.

For more information, see [*Identity providers in Qlik Cloud*](mc-create-idp-configuration.htm).

## Adding users by email invitations

To send an email invitation, you must be a tenant administrator. You can invite users to join the tenant from the Manage users pane in the Administration activity center or from your user profile menu.

- In the invitation window, enter one or more email addresses separated by commas or spaces.
- When the user receives the email invitation, they can join the tenant by clicking the link in the email. The link is valid for a limited period and redirects the user to a registration page.

You can view invitation status under Manage users > All users in the Administration activity center:

- Select Pending invites from the dropdown list or from the Status column.
- Hover over an invite to see the expiry date. Expired invites appear in red.
- When a user registers, the status changes to Active.

If needed, you can resend or delete invitations. Deleting an invitation prevents the user from registering, even if the link has not expired.

### Steps to invite a user

Do the following:

1. In the Administration activity center, go to Manage users and click Invite.
2. Enter the email addresses of the users that you want to invite, and then click Invite.
3. The invited users are listed in the table in the Manage users pane.

## Managing users in the Administration activity center

When users are added to the tenant, they are listed under Manage users > All users in the Administration activity center.

You can search for users by name, email, user ID, or IdP subject. The search on user ID and IdP subject must be an exact match. Hover over the information icon ![Information](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_info_outline.svg "Information") in the Name column to see user ID and IdP subject. The IdP subject field can be used for distinguishing one user from another if the names are identical.

For each user in the table, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) to open a menu where you can assign and remove security roles, activate or disable users, revoke mobile access if it has been granted, and delete users.

### User statuses

Each user has a status depending on whether they are a fully registered user, a user who has been invited but not yet registered, or a user who has been disabled. You can select a status to filter by in the dropdown list.

User status dropdown list

![Dropdown list with statuses in User pane](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_user-pane-statuses.png "Click to view full size")

User statuses

| Status | Description |
| --- | --- |
| Active | The user is fully registered. They can user the product according to their assigned roles. For more information about roles and permissions, see [*Assigning security roles and custom roles*](SaaS-roles-anonymous.htm). |
| Disabled | The user cannot access their account or use the product. All alerts owned by the user will be disabled. |
| Provisioned | The user is provisioned by the SCIM connector but has not yet registered. For more information, see [*Provisioning users and groups using SCIM*](auto-provisioning-using-SCIM.htm). |
| Pending invites | The user is invited but has not yet registered. A user ID is created but no entitlement has been assigned. |
| Orphans | The user has been assigned an entitlement to their IdP subject from the license service. The user has not yet registered, and no user ID has been created. |
| Requested | The user is invited to the tenant, but the number of users exceeds the subscription limit. Users with this status cannot access activity centers or open applications. They remain in this status until you add more entitlements or free up existing ones. |
