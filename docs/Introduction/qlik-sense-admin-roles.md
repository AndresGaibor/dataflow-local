---
title: "Understanding administrator roles and responsibilities"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/qlik-sense-admin-roles.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Deploying Qlik Cloud"]
---

# Understanding administrator roles and responsibilities

Administrators manage and maintain the Qlik Cloud tenant. An individual can hold more than one administrator role, each with specific permissions and responsibilities.

## Service account owner

The first user to access the [tenant](#glossary-0 "Glossary term") becomes the service account owner (SAO) and the initial tenant administrator. The SAO is responsible for:

- Creating and configuring the [tenant](#glossary-1 "Glossary term").
- Inviting users to join the tenant.
- Managing the subscription.

For more information, see [*Managing your Qlik Cloud subscription*](my-qlik.htm)

### Identity provider (IdP) configuration:

The SAO plays a critical role in IdP management. If the SAO is removed as a tenant admin, it may not be possible to repair or modify the IdP configuration in Qlik Cloud.

If the IdP stops functioning, the original SAO must access the Administration activity center via the recovery URL. However, this recovery will fail if the original SAO is no longer a tenant admin.

For more information, see [Known limitation in Qlik Cloud Services: Account Owner should not be removed as tenant admin](https://community.qlik.com/t5/Knowledge-Base/Known-limitation-in-Qlik-Cloud-Services-Account-Owner-should-not/ta-p/1717890).

### Subscription management:

Only the SAO can manage the subscription. To change the SAO, contact [Qlik Support](https://community.qlik.com/t5/Support/ct-p/qlikSupport) or create a support case from the [Support Case Portal](https://community.qlik.com/t5/forums/postpage/board-id/@support).

For more information, see [Qlik Cloud Services: Service Account Owner and Tenant Admin FAQ](https://community.qlik.com/t5/Knowledge/Qlik-Cloud-Services-Service-Account-Owner-and-Tenant-Admin-FAQ/ta-p/1799811).

## Tenant administrator

The tenant administrator is responsible for managing the organization’s Qlik Cloud environment. This role provides full administrative capabilities, such as:

- Managing users.
- Configuring system settings.
- Customizing and extending the tenant.
- Accessing all features of the Administration activity center.

Key details about the Tenant Admin role:

- At least one tenant admin is required at all times.
- You cannot remove the Tenant Admin role from yourself to prevent accidental removal of the last tenant admin.
- Tenant admins can assign the Tenant Admin role to other users.

Warning note

Anyone assigned the Tenant Admin role may be granted access to content, including personal content, relating to all users within the tenant to which the Tenant Admin role is assigned.

## Specialized administrator roles

In addition to tenant admins, there are administrator roles with more focused responsibilities and limited access:

### Analytics administrator

The analytics administrator manages user resources related to analytics services within shared and managed spaces. Their responsibilities include managing:

- Applications
- Scripts
- Data files
- Data connections

Analytics Admins cannot access content in other users' personal spaces.

### Data administrator

The data administrator manages resources for data integration services within data spaces. Their responsibilities include:

- Managing data spaces from the Administration activity center.
- Managing data resources in Data Integration Home.

Data Admins cannot access content in other users' personal spaces.

### Audit administrator

Audit administrators with the Manage API keys permission can access application feedback and usage metrics captured by the Natural Language API.

## Permissions granted by administrator roles

For details about the permissions associated with each administrator role, see:

- [*Permissions granted by security roles*](../Admin/SaaS-user-permissions-capacity-model.htm) (capacity-based subscriptions)
- [*Permissions granted by security roles*](../Admin/SaaS-user-permissions.htm) (user-based subscriptions)
- [*Permissions granted by security roles*](../Admin/SaaS-user-permissions-anonymous.htm) (Qlik Anonymous Access subscriptions)
