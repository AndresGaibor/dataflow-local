---
title: "Setting permissions for write tables"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/write-table-permissions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Managing users - User-based subscriptions", "Roles and permissions for users and administrators", "Default permissions and custom roles"]
---

# Setting permissions for write tables

User access to [write tables](#glossary-0 "Glossary term") can be controlled by [tenant administrators](#glossary-1 "Glossary term"). As a tenant administrator, you can define the level of access that each user is granted for working with write tables and the change-stores API. These permissions are configured in the Administration activity center.

## About the Manage write table charts permission

The Manage write table charts permission controls user access to write tables. You can configure whether each user in the tenant has full, partial, or no access to working with write tables.

The Manage write table charts permission has the following options:

- Allowed: Users have full access to write table functionality, including chart configuration, making changes in editable columns, and access to the change-stores API.
- Read and write access only: Users can view and interact with write tables in applications. They can make changes in editable columns added to the write table. Users cannot create write table charts or edit existing write table chart configurations, and cannot use API keys to extract changes from the change-stores API.
- Not allowed: Users cannot view or make changes in editable columns within write tables. They also cannot create write tables or edit existing write table configurations, and they are not granted access to the change-stores API.

Information noteThe Manage write table charts permission requirements apply to all users in the tenant, including tenant, analytics, and data administrators.

The Manage write table charts permission is configured in the Administration activity center through two processes:

- Creating custom roles. See:

  - [*Creating custom roles*](permissions-custom-roles-capacity-model.htm#Creating) (capacity-based subscriptions)
  - [*Creating custom roles*](permissions-custom-roles.htm#Creating) (user-based subscriptions)
- Configuring the default permissions. See:

  - [*Default permissions*](permissions-admins-users-capacity-model.htm#UserDefault) (capacity-based subscriptions)
  - [*Default permissions*](permissions-admins-users.htm#UserDefault) (user-based subscriptions)

## Interaction with space permissions

In addition to the Manage write table charts permission, user access to write tables is further controlled by a user's role in the space where the application is located.

If a user has the required Manage write table charts permission level but does not have the required space role, they are not granted access to the functionality. Similarly, if a user has the required space role but lacks the required Manage write table charts permission level, they are not granted access to the functionality.

For more information, see [*Space permissions*](../Visualizations/WriteTable/Analyze/write-table.htm#Space).

## Learn more

- [*Write table*](../Visualizations/WriteTable/Analyze/write-table.htm)
- [*Creating write tables*](../Visualizations/WriteTable/Create/create.htm)
- [*Troubleshooting - Write table*](../Visualizations/WriteTable/Create/troubleshooting.htm)
