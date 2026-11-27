---
title: "Managing users - Qlik Anonymous Access subscriptions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/SaaS-user-management-anonymous.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud"]
---

# Managing users - Qlik Anonymous Access subscriptions

With a Qlik Anonymous Access subscription, there are two types of users. Tenant users are members of the tenant who can be invited, assigned roles, and managed by administrators. Anonymous users, by contrast, are not members and do not need Qlik accounts—they can only view content through anonymous access links or embedded analytics. While anonymous users are not managed individually, administrators need to monitor overall capacity usage, including both tenant and anonymous sessions.

Information note

This topic is applicable to Qlik Anonymous Access subscriptions. For other Qlik Cloud subscriptions, see:

- Standard, Premium, or Enterprise edition of Qlik Cloud Analytics or Qlik Cloud Data Integration: [*Managing users - Capacity-based subscriptions*](SaaS-user-management-capacity-model.htm)
- Qlik Sense Enterprise SaaS, Qlik Sense Business, or Qlik Cloud Government: [*Managing users - User-based subscriptions*](SaaS-user-management.htm)

## Terminology on this page

The following terminology is used in content about anonymous access:

- Anonymous users: Users who are accessing application content without signing in, either through anonymous access links to an application or by consuming embedded analytics anonymously. These users are not members of the Qlik Cloud tenant, and also do not require Qlik accounts.
- Tenant users: Users who are members of the tenant and manage the tenant or develop analytics for consumption by anonymous users. Tenant users may have administrator privileges in the tenant.

## Managing tenant users and anonymous users

Add tenant users through an identity provider or send email invitations. Once added, you can assign permissions for specific actions in Qlik Cloud. Permissions are grouped into roles, which can be assigned to individual users or groups.

Anonymous users do not need to be added to the tenant to access content shared with them. They can only view limited versions of anonymously shared applications, and all other tenant content is unavailable to them.

## Monitoring entitlements and capacity

Tenant users consume user entitlements. Anonymous users do not consume entitlements but are counted towards Anonymous Capacity. Administrators can monitor both user entitlements and anonymous access usage, including sessions and purchased capacity, in the Administration Home to ensure it stays within subscription limits.

For more information, see:

- [*Anonymous access capacities*](mc-monitor-consumption.htm#AnonymousAccess).
- [*Monitoring resource consumption*](mc-monitor-consumption.htm).
