---
title: "Setting permissions for users who can configure anonymous access"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/permissions-anonymous-access.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Managing users - Qlik Anonymous Access subscriptions", "Roles and permissions for users and administrators", "Default permissions and custom roles"]
---

# Setting permissions for users who can configure anonymous access

Tenant administrators control the ability of each user in the tenant to configure [anonymous access](#glossary-0 "Glossary term") for applications. They do this in the Administration [activity center](#glossary-1 "Glossary term").

To allow a user in the tenant to generate application links that can be accessed by people outside the tenant, the Anonymous access link permission must be configured to Allowed for the tenant user. This procedure is performed by a [tenant administrator](#glossary-2 "Glossary term").

This permission can be assigned in either of the following ways:

- Assigning the permission in the default permissions (affects all tenant users)
- Assigning the permission as a custom role (only affects tenant users with the custom role)

For more information about default permissions and custom roles, see [*Roles and permissions for users and administrators*](permissions-admins-users-anonymous.htm).

For more information about all available default permissions and custom roles, see [*Default permissions and custom roles*](permissions-scopes-anonymous.htm).

Information note
This functionality is only available with a Qlik Anonymous Access subscription. For more information, see [*Qlik Anonymous Access subscriptions*](subscription-options-anonymous.htm).

## Default permissions

Tenant administrators can adjust default permissions. By default, these permissions prevent all users, including [tenant administrators](#glossary-3 "Glossary term"), from configuring anonymous access for applications. You can change the setting to Allowed to let all users configure anonymous access.

Do the following:

1. In the Administration activity center, go to Manage users.
2. Select the Permissions tab.
3. Click Manage default permissions.
4. Expand Content types > Applications.
5. For Anonymous access link, select Allowed from the dropdown list.
6. Click Confirm.

## Custom roles

Tenant administrators can create custom roles to grant specific users higher permissions than the default permissions. You might want to restrict anonymous access in the default permissions, then create a custom role to allow it for selected users.

Do the following:

1. Create a custom role

   1. In the Administration activity center, go to Manage users.
   2. Select the Permissions tab, then click Create new.
   3. Enter a Name and, optionally, a Description for the role.
   4. Under Permissions, expand Content types > Applications.
   5. For Anonymous access link, select Allowed from the dropdown list.
   6. Click Confirm.
2. Assign the custom role to users

   1. Go to the All users tab.
   2. Select the checkboxes for the users you want to assign the role to.
   3. Click Manage roles.
   4. Select your new custom role and click Save.
