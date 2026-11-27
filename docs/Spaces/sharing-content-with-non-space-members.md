---
title: "Sharing applications with users who are not space members"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/sharing-content-with-non-space-members.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Using analytics to explore data", "Sharing and downloading application content"]
---

# Sharing applications with users who are not space members

With fine-grained access control, you can share an application from a [shared](#glossary-0 "Glossary term") or [managed](#glossary-1 "Glossary term") space with users or user groups without making them members of the space. This reduces administration and simplifies space management, because users only get access to the shared application—not the whole space.

Information noteFine-grained access control is not available in Qlik Cloud Analytics Standard or Qlik Sense Business.

## Permissions needed for fine-grained sharing

Access to fine-grained sharing is controlled by permissions. If you only see options to share the entire space and not just a single application, contact your administrator. Administrators can find more information in [*Default permissions and custom roles*](../Admin/permissions-scopes-capacity-model.htm).

## Sharing an application with non-space members

Space owners and users with the Can manage role in a space can share applications from a shared or managed space. You cannot share applications from a personal space.

When you share an application, you assign roles that determine what the user can do with the application:

- Shared space: Can view
- Managed space: Can view, Can contribute, or Has restricted view

If your tenant supports groups, you can share applications with user groups. When a user has both individual and group permissions on an application, the higher permission level applies.

Information noteA [tenant admin](#glossary-2 "Glossary term") or analytics admin can assign themselves a Can manage role in a space to be able to share applications. A tenant admin can also take ownership of the space to share applications.

### Sharing with individual users or groups

Do the following:

1. In a shared or managed space, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) in the application to be shared and select Share.
2. Search for user name or email address of the user or user group.
3. Select permissions for the user.
4. Click Share.

### Sharing with everyone in your tenant

Do the following:

1. In a shared or managed space, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) in the application to be shared and select Share > Invite.
2. Select permissions in the dropdown list next to Anyone at <your tenant name>.
3. Click Done.

### Permission details

If the sharing roles don't meet your needs, consider making the user a space member. More roles are available for space members.

For detailed descriptions of the space roles, see:

- [*Managing permissions in shared spaces*](managing-shared-spaces.htm)
- [*Managing permissions in managed spaces*](managing-managed-spaces.htm)

## Managing shared application users in a space

You manage shared application users in the Members section of the space. Shared application users are not space members, but have access to one or more applications in the space.

You can access an application in three ways:

- as a member of the space
- as a user with whom the application has been shared
- as part of a group with which the application has been shared

Normally, you don't want a user to have access to an application in several different ways. However, these options offer flexibility and simplify management.

What a user can do with an application depends on:

- The role you assign when sharing the application
- The user's entitlement (Professional or Analyzer)
- Any existing space permissions

The highest application permission level always applies. For example, if you share an application with Can view permission, but the user already has Can contribute, the user retains the higher-level permission. Application sharing never overrides higher-level permission.

A shared application user can open the space and see only the shared applications, not all applications in the space. They can also view the space details, but not the members section.

### Opening the members list

Do the following:

1. Click ![Qlik Sense SaaS navigation menu. ](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_grid_menu.svg) and select Analytics Services.
2. Open Catalog.
3. In the Spaces list, select the space you want to manage.
4. Click Space settings and select Members.

The members list shows both space members and shared application users. Members are presented with a space icon, shared application users with an application icon. In the following image, you can see that Anna is a space member, but she also has two applications that have been shared with her. She has multiple roles, which are displayed when her profile is expanded (see image Anna's expanded profile).

Ali is a space member with Can manage permissions on the space and no shared applications. When a user has different permissions, the highest one is displayed.

Anna 2 is not a space member, and only has Can view access to "Demo App - Beginner's tutorial". She cannot open any other applications in the space.

Members list in a shared space

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_SpaceMembersList.png "Click to view full size")

In Anna's expanded profile you can see that she is the space owner and as such she can share applications from this space with non-space members. Two applications have been shared with her, and even if the role assigned to her is only Can view, she can, as space owner, perform many more actions than open the applications and see content.

A shared application user can perform the same actions in the application as a member of the space with the corresponding permissions. The only exception is notes, which shared application users can only create in [personal spaces](#glossary-3 "Glossary term").

Anna's expanded profile

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_SpaceMembersListExpanded.png "Click to view full size")

### Editing the members list

Space owners and users with Can manage permissions can edit the members list. In addition to the search, the filtering options by role and access make it easy to find users or groups for editing.

#### Actions that will impact shared application users

In the More actions menu (![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg)), you can make edits to shared application users.

In a shared space, you can add the user as a space member or remove the user's access to the application. You cannot edit the role Can view.

In a managed space, you can add the user as a space member or remove the user's access to the application. You can edit the roles, but the user must have at least one role.

For users who are both space members and have shared applications, you can remove them as space members but keep them as shared application users, or the other way around. You can also remove their access to only some of the shared applications.

A shared application will become inaccessible for users with whom the application has been shared when:

- the application is deleted
- the application is moved to another space
- the application is duplicated and the original application deleted

Information noteAn application will still be available after it's been republished.

## Limitations

### General limitations

- You cannot share QlikView applications.
- You can share Direct Query applications only by inviting users to the space where the application and its data connections are stored. Users need access to both the application and the underlying data sources. If a user doesn’t have permission for a required data source, they won’t be able to load data in the application. For more information, see [*Direct Query applications*](../DirectQuery/direct-query-apps.htm).
- The [write table](#glossary-4 "Glossary term") does not support fine-grained access control. If a user has access to an application without being a member of the space, they cannot view, edit, analyze, or create write tables on sheets in the application.

### Sharing limitations per space

The following limits exist per space for application sharing. If the limit is reached for individual users, consider making them a members of a user group or the space.

|  |  |
| --- | --- |
| Max number of shares per application | 400 |
| Max number of shares per user/user group | 200 |
| Max number of shares per space | 400 |
