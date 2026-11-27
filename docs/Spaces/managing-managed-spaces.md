---
title: "Managing permissions in managed spaces"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/managing-managed-spaces.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Collaborating with other users", "Working in spaces", "Working in managed spaces"]
---

# Managing permissions in managed spaces

Permissions in spaces are controlled by roles assigned to members when they are added to a space. A role gives that member a set of permissions in the space and on resources in the space.

Information noteManaged spaces are not available in Qlik Cloud Analytics Starter or Qlik Sense Business.

Members of a [managed space](#glossary-0 "Glossary term") can have multiple roles applied to them. This enables customized access to the space for each member. If groups are allowed in the tenant, groups of users can be added to a space with the same role. If a space member has different individual permission and group permission in a space, the highest permission level is applied.

Tenant and analytics admins, space owners, and members with the Can manage space role can add new members to the space and assign them permissions. Space permissions are managed in Space settings > Members.

The space owner is assigned the Owner role. This space role cannot be removed from the space member without administrator action. It is not possible to remove space members with the Owner role from the space, unless you have access to the Administration activity center as an administrator.

Applications can be shared with non-space members. For more information, see [*Sharing applications with users who are not space members*](sharing-content-with-non-space-members.htm).

For details about the actions permitted by each available space role, see:

- [*Managed space permissions for Professional and capacity-based subscription users*](permissions-managed-space-prof-full.htm)
- [*Managed space permissions for users with Analyzer entitlement*](permissions-managed-space-analyzer.htm)
- [*Managed space permissions for administrators*](permissions-managed-space-admin.htm)
- [*Managed space permissions for anonymous users*](permissions-managed-space-anonymous.htm)

Information noteAPI-based workflows may support additional actions beyond what is available in the UI. Always review the latest API documentation when planning or updating integrations. For more information, see [API access control and trust boundaries](https://qlik.dev/manage/access-control/api-trust-boundaries/).

## Available roles in managed spaces

The following space roles are available in managed spaces:

- Owner: Can manage the space and its members, as well as open applications in the space. This is not a role you can assign to other members of the space unless you are an administrator. This space role also cannot be removed from the space member without administrator action. It is not possible to remove a member with the Owner role from the space, unless you have access to the Administration activity center as an administrator.
- Can manage: Can manage the space and its members.
- Can publish: Can publish applications to the space. They cannot open applications in the space.
- Can contribute: Can view and open applications in the space. Contributors can create private content in the application and make that content public.
- Can view: Can view and open applications in the space.
- Has restricted view: Can view and open applications in the space.
- Can consume data: Can consume data sources, but cannot create or edit data sources. They cannot create content or manage the space. See [*Adding and managing your analytics data*](managing-data-resources-spaces.htm#Managing) to learn about data sources inside a space.
- Can operate: Can reload applications and create scheduled reloads.

## Changing permissions for members in managed spaces

Member roles can be changed to give them new permissions in the space.

Tenant and analytics admins, space owners, and members with the Can manage role can change members' permissions.

Information note

When you make any changes to user's permissions for applications or scripts, these changes are not instantly reflected in actively opened applications and scripts. To ensure that the changes to the user's permissions are updated, the user must close all browser tabs belonging to the affected application or script and wait at least two minutes (application session's Time To Live), then re-open the application. This applies to application and script permissions in personal, shared, and managed spaces. Changes in permissions for newly opened applications are reflected instantly.

Do the following:

1. In the space, click Space settings and select Members.
2. Click the arrow ![Arrow down](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_down.svg) in the Role column for the member.
3. Select the appropriate roles for the member.

## Common use cases

The following sections outline some common approaches you might want to follow when assigning roles to space members.

### I want users to be able to create analytics without accessing data sources

To achieve this result, assign the Can contribute role to users in the managed space. These users will be able to create new sheets and visualizations in an application, but they cannot manage the data sources in the space.

### I want to allow a user to publish content to the space without having access to its data

A managed space typically contains data with higher security and governance requirements than the source space in which it is developed. You might have a team of application developers who are in charge of developing the application data model and base sheets, but are only given mock data to do this. The developers of the application might not necessarily be the same users as those who will be consuming and analyzing its production data.

You might want the application developers responsible for completing the application to be responsible for publishing it as well. To achieve this, assign the Can publish role to these users. The application developers can then publish the content to the managed space, but cannot access the data and content from the managed space.

## Space permissions and data sources

A data source in one space can be used in another space. For example, a user can create an application in a shared space using a data connection from their personal space. Certain space actions, however, require space members other than the resource owner to have access to the data source. In the previous example, other space members would not be able to reload the application as it uses a data connection from a personal space. Depending on your use case, this access control may or may not be desirable.

Generally, the owner of a data source is not granted any exemptions to the permissions governed by space roles. The only exception to this is the action of editing a data connection. Only the data connection owner can edit a connection. Each time a connection is edited, the user must re-authenticate themselves on the connection.

If the owner of a data connection loses the required access to the space or leaves the tenant, entities that rely on the connection will no longer be able to fetch new data from that connection. If the connection owner leaves the tenant, contact a tenant administrator to reassign connection ownership and move it to a new space as needed. If the connection owner is simply no longer a space member, another space member can re-create the connection.

The creator of a data file is assigned as its owner. The owner of a data file can be changed by an administrator. Ownership of data files does not affect access controls unless the data file is in a user's personal space. For more information about expected behavior, see [*Data file ownership*](../Admin/mc-administer-data-files.htm#DataFileOwnership).

The owner of a data file can leave the space and tenant, and other space members will continue to be able to view and use the file.

## Space permissions and user entitlement

In user-based subscriptions (Qlik Sense Enterprise SaaS or Qlik Sense Business), what you can do depends on both your space roles and your user entitlement—Professional or Analyzer. Users with Analyzer entitlement have more limited permissions. We recommend that the space owner and members with the Can manage role have Professional entitlement.

In capacity-based subscriptions, only your assigned space roles determine what you can do in the space.

### Assignment of roles by user entitlement

In capacity-based subscriptions, users can take on any of the roles listed below. The guidance that follows applies specifically to user-based subscriptions.

Users with Professional entitlement can be assigned roles that allow them to perform these types of actions:

- Space management: Owner or Can manage
- Creation of content and data sources: Owner or Can manage
- Reloads: Owner, Can manage, or Can operate
- Publishing: Can publish
- Consumption of content and/or data: Any role

Users with Analyzer entitlement should only be assigned roles for consumption of content. These roles include: Can contribute, Can view, Has restricted view, and Can consume data.

## Space permissions and global tenant roles

This section outlines how global tenant roles (assigned by an administrator) affect space permissions.

### Administrator roles

If you are assigned an administrator role in the Qlik Cloud tenant, your space permissions will be different from user permissions in the same spaces. The following general rules apply:

- An administrator will generally be able to view the resources in a space, manage space membership, and delete certain resources. They can create shared and managed spaces, and do not need the Shared Space Creator and Managed Space Creator security roles to do so. Administrators can also add themselves to spaces if needed.
- For other actions (for example, creating and editing content), the administrator role does not override space permissions, and the administrator needs to have sufficient roles in the space.

For more information, see:

- [*Assigning security roles and custom roles*](../Admin/SaaS-roles-capacity-model.htm) (capacity-based subscriptions)
- [*Assigning security roles and custom roles*](../Admin/SaaS-roles.htm) (user-based subscriptions)
- [*Assigning security roles and custom roles*](../Admin/SaaS-roles-anonymous.htm) (Qlik Anonymous Access subscriptions)

### Security roles

Certain actions require additional security roles to be assigned to you by an administrator. You might need the security role only, or a combination of security roles and space roles.

For example, to have full access to working with business glossaries, you need the Steward role, in addition to the required space roles.

For more information, see:

- [*Assigning security roles and custom roles*](../Admin/SaaS-roles-capacity-model.htm) (capacity-based subscriptions)
- [*Assigning security roles and custom roles*](../Admin/SaaS-roles.htm) (user-based subscriptions)
- [*Assigning security roles and custom roles*](../Admin/SaaS-roles-anonymous.htm) (Qlik Anonymous Access subscriptions)

## Troubleshooting

For solutions to common issues you might encounter when working in spaces, see [*Troubleshooting - Working in spaces*](../Troubleshooting/troubleshooting-spaces.htm).

Related learning:

- [Differentiate and manage Qlik Cloud spaces](/lnk/Differentiate_manage_spaces)
- [Administer and allocate space roles in Qlik Cloud](/lnk/Administer_allocate_space_roles)
