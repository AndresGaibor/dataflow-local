---
title: "Managing user entitlements"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/SaaS-user-allocations.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Managing users - User-based subscriptions"]
---

# Managing user entitlements

User entitlements determine the areas of the [tenant](#glossary-0 "Glossary term") each user can access, and the actions they can do in these areas. [Tenant administrators](#glossary-1 "Glossary term") can assign or remove a user entitlement from the Administration activity center.

Information note

This topic is applicable to Qlik Sense Enterprise SaaS, Qlik Sense Business, and Qlik Cloud Government. If you have a subscription for the Standard, Premium, or Enterprise edition of Qlik Cloud Analytics or Qlik Talend Data Integration, see [*Managing users - Capacity-based subscriptions*](SaaS-user-management-capacity-model.htm).

## What are user entitlements

When users join the tenant, you assign them Professional entitlement or Analyzer entitlement. The number of user entitlements is based on your Qlik Cloud subscription. You can see the number of available users entitlements and how many users you have consumed in the Administration activity center Home. For more information, see [*Monitoring resource consumption*](mc-monitor-consumption.htm).

- Professional entitlement is intended for users who will create content in Qlik Sense. A user with Professional entitlement can create shared spaces, create, edit, and publish sheets or applications, and can create and edit alerts.
- Analyzer entitlement is intended for users who consume sheets and applications created by others. Users with Analyzer entitlement cannot create or edit applications in shared spaces. They can, however, create personal sheets, stories, bookmarks, and snapshots in applications that are shared with them, depending on their assigned space roles. They can also generate on-demand applications, print objects, stories, and sheets, and export data from an object to Microsoft Excel.
- Analyzer capacity (minutes) is intended for providing time-based Analyzer access. You can see the total amount of minutes available per month and the consumed minutes in the Administration activity center Home.

Information noteAll users can have unlimited parallel user connections.

## Monitoring consumption of user entitlements

Monitoring consumption of user entitlements and Analyzer capacity is essential for effective resource management. You can track usage through the Administration activity or the Entitlement Analyzer monitoring application.

### Administration activity center

The Administration Home provides a summary of available and consumed user entitlements. It also shows the total and used Analyzer capacity minutes.

For more information, see [*Monitoring resource consumption*](mc-monitor-consumption.htm).

### Entitlement Analyzer monitoring application

The Entitlement Analyzer application allows you to monitor entitlement usage across the tenant and track Analyzer capacity consumption.

This application is part of the Qlik Cloud Monitoring Apps, which are community-supported. It is not officially supported by Qlik. To quickly install and update these applications, use the Qlik Cloud Monitoring Apps Installer with Qlik Automate. For details on installation and support, see [*App Installers*](../../Sense_QlikAutomation/introduction/template-list.htm#App).

For more information about the Entitlement Analyzer application, see:

- [Qlik Community: Entitlement Analyzer for Qlik Sense Enterprise SaaS (Cloud only)](https://community.qlik.com/t5/Support-Updates/Entitlement-Analyzer-for-Qlik-Sense-Enterprise-SaaS-Cloud-only/ba-p/1817404)
- [GitHub: Qlik Cloud Entitlement Analyzer](https://github.com/qlik-oss/qlik-cloud-entitlement-analyzer)

## Assigning and managing user entitlements

Information noteAs per the [Qlik® Customer Agreement](https://www.qlik.com/us/legal/legal-agreements), you are not allowed to reallocate user entitlements or let multiple users share entitlements to exceed your purchased quantity.

Tenant admins can manage the user entitlements under Manage users in the Administration activity center.

### Assigning user entitlements

Do the following:

1. In the Administration activity center, go to Manage users, and then select the All users tab.
2. Select one or more users from the list.
3. Click Change entitlements.
4. Select the checkbox for the entitlement you want to assign, and then click Save.

Information noteYou can automatically assign user entitlements. See [*Enabling automatic assignment of entitlements*](#Enable).

### Removing user entitlements

If dynamic assignment of entitlements is enabled in your tenant, an active user will be reassigned an entitlement at their next login. To prevent this, you can disable the user.

Removing a user's entitlement does not affect any resources owned by the user.

Do the following:

1. In the Administration activity center, go to Manage users, and then select the All users tab.
2. Select one or more users from the list.
3. Click Change entitlements.
4. Clear the checkbox for the assigned entitlement, and then click Save.

### Changing user entitlement from Analyzer to Professional

Do the following:

1. In the Administration activity center, go to Manage users, and then select the All users tab.
2. Select one or more users from the list.
3. Click Change entitlements.
4. Select Professional, and then click Save.

## Enabling automatic assignment of entitlements

You can enable automatic assignment of Professional entitlement or Analyzer entitlement to users upon login to Qlik Cloud.

There are two toggles for dynamic entitlement assignment: Enable dynamic assignment of professional users and Enable dynamic assignment of analyzer users. Depending on which toggles you turn on, there are four options:

- Both enabled: Professional entitlement is assigned, if available, otherwise Analyzer entitlement. If neither of those are available, Analyzer capacity is assigned, if available.
- Only enabled for Professional: Professional entitlement is assigned, if available, otherwise Analyzer capacity is assigned, if available.
- Only enabled for Analyzer: Analyzer entitlement is assigned, if available, otherwise Analyzer capacity is assigned, if available.
- Both turned off: Analyzer capacity access is assigned, if available.

Do the following:

1. In the Administration activity center, go to the Settings page, then select the Entitlements tab.
2. Turn on the Enable dynamic assignment of professional users option to assign Professional entitlement automatically.
3. Turn on the Enable dynamic assignment of analyzer users option to assign Analyzer entitlement automatically.

If you change to a new license key, all your assignments are removed, because they are associated with the license, not the tenant. However, if you start using the old license key again, the assignments will be present.

## How user entitlements interact with roles

Users who join the tenant are assigned a user entitlement, either Professional entitlement or Analyzer entitlement. User entitlements divide users into content consumers and content creators. The user entitlement also determines which areas of the tenant are visible to a user. For more information, see [*Managing user entitlements*](#).

- Users with Professional entitlement are both content consumers and content creators, which means they have access to the Add New button. This lets them create new resources like applications and spaces.
- Users with Analyzer entitlement are strictly content consumers, as a result, the Add New button is hidden from their view.

Administrator roles and user roles offer additional permissions beyond those granted by user entitlements. For example, a user with Analyzer entitlement who is assigned a space creator role will gain access to the Add New button to create new spaces.

Information noteWhen designing your permission structure, provide Professional entitlement to any user who will be assigned a specific security role.

### Automatic role assignment

By default, all users with Professional entitlement are automatically assigned the following roles:

- Shared Space Creator
- Private Analytics Content Creator
- Data Services Contributor

Tenant administrators turn off this automatic role assignment if needed.

#### Turning off automatic role assignment

Do the following:

1. In the Administration activity center, go to the Settings page, then select the Entitlements tab.
2. Turn off the following settings:

   - Professional entitlements can create shared spaces
   - Professional entitlements can create private analytics content
   - Professional entitlements can access Data Integration

#### Key points about automatic role assignment

- Role assignments take effect the next time a user logs in after the setting has been enabled.
- New users receive only the Professional entitlement at first. Roles are assigned on their second login, provided both the Professional entitlement and role assignment settings are enabled.

  - If a new user was manually assigned the Professional entitlement and only the role assignment settings are enabled, roles will be assigned after a single login.
- If the role assignment setting is turned on while users are logged in, they must log out and log back in for the changes to apply.
- Users who were assigned roles before the setting was turned off will keep them until an administrator manually removes them.
