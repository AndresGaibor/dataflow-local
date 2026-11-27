---
title: "Setting permissions for metered reporting features"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-permissions-reporting.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Configuring features and integrations", "Administering reporting and subscriptions"]
---

# Setting permissions for metered reporting features

[Tenant administrators](#glossary-0 "Glossary term") configure permissions to control whether users have full, partial, or no access to the value-add capabilities of the Qlik Reporting Service. If a user is granted access to the functionality, their access to reporting resources — applications with report tasks, reporting automations, and so on — is further managed by built-in security roles assigned by administrators, as well as their roles in the associated spaces.

## What are metered reporting features?

Metered reporting features are the value-add capabilities of the Qlik Reporting Service, which are available within Qlik Cloud subscriptions. They are:

- In-application reporting, including on-demand reporting
- Reporting with Qlik Automate
- Usage of the Qlik Reporting Service API for metered operations. This excludes using the API for other functionality, such as [subscriptions](#glossary-1 "Glossary term") and downloads of application content.

## About the Generate all reports permission

The Generate all reports permission controls whether a user has full, partial, or no access to the value-add capabilities of the Qlik Reporting Service. The Generate all reports permission is used in conjunction with space roles and built-in security roles to control user access to reporting functionality. See [*Other permission interactions*](#Other).

Information noteThe Generate all reports permission does not control user access to subscriptions. You can turn subscriptions off for the entire tenant in the Administration activity center, in the Settings section. See [*Toggling availability of subscriptions*](mc-enable-reporting-features.htm#Toggling).

The Generate all reports permission is configured in the baseline permissions that apply to all users in the tenant (default permissions), as well as custom security roles. To learn how to assign permissions via the default permissions and custom roles, see:

- [*Roles and permissions for users and administrators*](permissions-admins-users-capacity-model.htm) (capacity-based subscriptions)
- [*Roles and permissions for users and administrators*](permissions-admins-users.htm) (user-based subscriptions)

For information about the permissions available through default permissions and custom roles, see:

- [*Default permissions and custom roles*](permissions-scopes-capacity-model.htm) (capacity-based subscriptions)
- [*Default permissions and custom roles*](permissions-scopes.htm) (user-based subscriptions)

Options for the Generate all reports permission are described below.

### Allowed

Users can configure and generate all types of reports available with value-add capabilities of the Qlik Reporting Service. This includes:

- In-application reporting, including on-demand reporting. This includes:

  - Viewing and using the Reporting section in analytics applications.
  - Connecting to analytics applications in Qlik add-ins for Microsoft Office.
  - Generating on-demand reports in analytics applications.
- Reporting with Qlik Automate.
- Usage of the Qlik Reporting Service API for metered operations.

### On-demand reports

Users can only configure and generate reports using on-demand reporting and the Qlik Reporting Service API. They are blocked from:

- Viewing and using the Reporting section in analytics applications.
- Connecting to analytics applications in Qlik add-ins for Microsoft Office.
- Executing automations that use the Qlik Reporting Service.

### Not allowed

Users cannot work with any value-add capabilities of the Qlik Reporting Service.

In other words, these users are blocked from:

- Viewing and using the Reporting section in analytics applications.
- Connecting to analytics applications in Qlik add-ins for Microsoft Office.
- Executing automations that use the Qlik Reporting Service.

### Effect on tenant administrators

The access controls provided by the Generate all reports permission also apply to tenant administrators. In other words, to use a metered reporting feature, a tenant administrator also needs the appropriate Generate all reports permission level. Tenant administrators can administer user report tasks and subscriptions in the Subscriptions section of the Administration activity center without any Generate all reports permissions.

## Use cases

Administrators can use the Generate all reports permission to achieve granular access control based on different user scenarios. The following workflow can be used:

1. Set the default permission level to On-demand reports. This allows all users to generate on-demand reports while analyzing applications, but restricts access to report development features.
2. For report developers, raise the permission level to Allowed by creating a custom role and assigning it to these users. This gives these users full access to report development features.
3. For most reporting features, space roles provide an additional layer of control to specific content. Access to specific content — in particular, applications used for reporting — can be managed both by users and administrators.

## Other permission interactions

### Built-in security roles

The Private Analytics Content Creator role is a built-in security role. This role is assigned by tenant administrators. Users working with reporting in their personal spaces will need this role. See:

- [*Assigning security roles and custom roles*](SaaS-roles-capacity-model.htm) (capacity-based subscriptions)
- [*Assigning security roles and custom roles*](SaaS-roles.htm) (user-based subscriptions)

### Space roles

In addition to permissions configured through default permissions and custom roles, user access to reporting is further controlled by the user's role in the space containing the analytics content. See [*Space permissions for in-application reporting*](../Reporting/reporting-permissions.htm#Space) and [*Space permissions for reporting with Qlik Automate*](../Reporting/reporting-permissions.htm#Space2).
