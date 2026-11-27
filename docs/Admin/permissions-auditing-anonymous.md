---
title: "Auditing user roles and access"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/permissions-auditing-anonymous.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Managing users - Qlik Anonymous Access subscriptions", "Roles and permissions for users and administrators"]
---

# Auditing user roles and access

Regularly reviewing user permissions is essential for maintaining security and ensuring users have appropriate access within your tenant. Auditing permissions helps ensure that only authorized users have access to sensitive resources.

## Checking assigned roles for users

Tenant administrators can check the roles assigned to any user in the tenant from the Administration activity center.

Do the following:

1. In the Administration activity center, go to Manage users > All users.
2. In the Roles column, hover over ![Information](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_info_outline.svg) to see a tooltip that lists all roles assigned to the user.

Tooltip in the Roles column.

![Tooltip showing user roles.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_audit_roles_administration.png "Click to view full size")

## Viewing your own roles

You can view your own assigned roles in the tenant using one of the following methods:

- From your user profile menu:

  1. Click your profile icon in the upper-right corner.
  2. Hover over the role name displayed below the tenant name.

     A tooltip will display a list of your roles.

  Tooltip on the user profile menu.

  ![Tooltip showing user roles.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_audit_roles_profile_menu.png "Click to view full size")
- From your personal settings page:

  1. Click your profile icon in the upper-right corner.
  2. Select Settings.
  3. Hover over ![Information](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_info_outline.svg) next to the role name below the tenant name.

     A tooltip will display a list of your roles.

  Tooltip on the Settings page.

  ![Tooltip showing user roles.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_audit_roles_profile_page.png "Click to view full size")

## Using the Access Evaluator application to analyze user permissions

You can use the Access Evaluator application to analyze roles, access, and permissions across the tenant. This application provides insights such as:

- User and group access to spaces
- User, group, and sharing access to applications
- User roles and associated role permissions
- Group assignments to roles

The Access Evaluator is part of the Qlik Cloud Monitoring Apps, which are community-supported. This means that they are not supported by Qlik. To quickly install and update these applications, use the Qlik Cloud Monitoring Apps Installer with Qlik Automate. For details on installation and support, see [*App Installers*](../../Sense_QlikAutomation/introduction/template-list.htm#App).

For more information about the Access Evaluator, see:

- [Qlik Community: Access Evaluator - Monitoring App for Qlik Cloud](https://community.qlik.com/t5/Support-Updates/Access-Evaluator-Monitoring-App-for-Qlik-Cloud/ba-p/1954291)
- [GitHub: Qlik Cloud Access Evaluator](https://github.com/qlik-oss/qlik-cloud-access-evaluator)
