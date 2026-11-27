---
title: "Working in shared spaces"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/working-in-shared-spaces.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Collaborating with other users", "Working in spaces"]
---

# Working in shared spaces

A [shared space](#glossary-0 "Glossary term") is a section of Qlik Cloud Analytics used to develop applications collaboratively and control access to applications.
You can find your shared space using the spaces drop-down in Catalog.

Space roles are assigned to members when they are added to a shared space. Each space role is a set of [permissions](#glossary-1 "Glossary term") that define what members can do in the shared space.

The following space roles are available in shared spaces:

- Owner: You are the first administrator that can manage the space and its members as well as create content in the space. You cannot edit load scripts of applications and scripts that you do not own—to do this, you need the Can edit data in applications space role.

  This role cannot be assigned to other members of the space unless you are an administrator. This space role also cannot be removed from the space member without administrator action. It is not possible to remove a member with the Owner role from the space, unless you have access to the Administration activity center as an administrator.
- Can manage: You can manage the space and its members as well as create content in the space. You cannot edit load scripts of applications and scripts that you do not own—to do this, you need the Can edit data in applications space role.
- Can edit: You can add and edit content in applications. You cannot manage the space and its membership.
- Can edit data in applications: You can add and edit content in applications, as well as edit the load script and business logic of applications in the shared space. You cannot manage the space and its membership.
- Can view: You can view applications in the space, but cannot create content or manage the space.
- Can consume data: You can consume data sources, but cannot create or edit data sources. They cannot create content or manage the space. See [*Adding and managing your analytics data*](managing-data-resources-spaces.htm#Managing) to learn about data sources inside a space.

Members can be assigned different roles in a space. They can also be removed from spaces. For information on managing permissions in a shared space, see [*Managing permissions in shared spaces*](managing-shared-spaces.htm).

You can create new applications directly in a shared space. You can also move applications from your personal space to a shared space so other members can work on them. For more information on collaborating with users in a space, see [*Using applications in shared spaces*](managing-apps-in-spaces.htm).

You can share applications in a shared space with non-space members, see [*Sharing applications with users who are not space members*](sharing-content-with-non-space-members.htm).

## Creating shared spaces

A space's owner is the user who created the space. The owner of a space can only be changed in the Administration activity center.

Tenant admins, analytics admins, and users with the Shared Space Creator user role can create shared spaces.

By default, the Shared Space Creator role is automatically assigned to:

- All users in capacity-based subscriptions.
- All users with Professional entitlement in user-based subscriptions.

For more information, see [Assigning security roles](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/SaaS-roles.htm).

Do the following:

1. Go to the Create page of the Analytics [activity center](#glossary-2 "Glossary term") and select Space.
2. Enter a name and a description for the space. The name must be unique.
3. Click Create.

## Adding members to shared spaces

Members can be added to the space by the owner or members with the Can manage role.

If groups are allowed in the tenant, you can add groups of members to your space. If a space member has individual permission and group permission in a space, the highest permission level is applied.

Information note A [tenant admin](#glossary-3 "Glossary term") or analytics admin can assign themselves a Can manage role in a space to be able to share applications. A tenant admin can also take ownership of the space to share applications.

You can invite specific users or groups to the space, or add all users in the tenant. Adding all users is useful if you want applications or content to be generally available to everyone in your organization.

Do the following:

- In the space, open the invite dialog in one of the following ways:

  - Click Share.
  - Click Space settings > Members, and then select Add members.
- To invite specific users or groups:
  - Search for users or groups by name or email and select the members you want to invite.
  - Select permissions for the new members.
  - Click Send.
- To invite all users in your tenant:

  - Select permissions in the dropdown list next to Anyone at <your tenant name>.
  - Click Done.

## Removing members from shared spaces

You can remove members from a space.

Do the following:

1. In the space, click Space settings and select Members.
2. Under Role, click ![Arrow down](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_down.svg) next to the member to remove.
3. Click Remove.

Tip note

Click Undo in the pop-up that appears if you want to re-add the member to the space.

## Editing the names and descriptions of shared spaces

You can change the name and description of the space.

Do the following:

1. In the space, click Space settings and select Edit space.
2. Change the name and description and click Save.

## Deleting shared spaces

You can delete a space. Only the tenant administrator, analytics administrator, or a user with the Is owner or Can manage role can delete a space.

1. In the space, click Space settings and select Delete space.
2. Click Delete.

## Collaborating with others on application development

When collaborators are given sufficient permissions in a shared space, they are empowered to work together in the construction of an application, from start to finish. In the early stages of application development, users with the Can edit data in applications role can work together on the [load script](#glossary-5 "Glossary term"), allowing the collaborative creation of the application's underlying data architecture.

One of the main benefits of shared spaces is the ability to easily switch content between private and public access. For example, a user could start by developing a [sheet](#glossary-6 "Glossary term") privately, then making it public so others can try consuming it, editing it, and adding new content to it.

Space members can easily Duplicate public content, creating a private copy for themselves which they can then adjust and fine-tune. Revised copies of content can then be made public again so other collaborators can review the changes. Public sheets, [bookmarks](#glossary-7 "Glossary term"), and [stories](#glossary-8 "Glossary term") can also be made private by other users who didn’t necessarily create them. These features, including the variety of available space roles, allow teams to make decisions about who controls what content in the application and what content is considered finished and ready for its functional purpose.

For more information about private and public content in an application, see [*Granting access to sheets, sheet groups, bookmarks, and stories*](../Share/make-public-or-private.htm).

Additionally, users can create and edit notes in the space to make comments on specific parts of an application, such as a visualization or selection state. You can mention users directly in notes and track conversations between team members about application development specifics. For more information about the collaborative benefits of Notes, see [*Capturing and sharing insights using Notes*](../Notes/notes-overview.htm).

## Sample workflow: Developing and sharing applications with shared spaces

There are different ways of developing applications collaboratively and sharing them with other members.
Here is a sample workflow for using shared spaces:

1. Create an application

   Create an application in your personal space. Add data sources, create a data model, and create scheduled reloads for the application.

   [*Creating applications and adding data*](../Apps/create-app-cloud-hub.htm)
2. Create a shared space

   Add a shared space for collaborative development of your application.
3. Move your application to the space

   Once the application is ready for collaboration, move your application to your shared space.

   [*Moving applications between spaces*](managing-apps-in-spaces.htm#Moving)
4. Add users to the space

   Add collaborators to your space and assign them the Can edit or Can edit data in applications roles. In user-based subscriptions, collaborators must also have Professional entitlement.
5. Add data to the space

   Optionally, add additional data resources to the space for other collaborators to use.

   [*Adding and managing your analytics data*](managing-data-resources-spaces.htm)
6. Develop applications in the space collaboratively

   All users with the Can edit role can add sheets, stories, and bookmarks to the application. Their content is private until they chose to make it public in the application.

   Users with the Can edit data in applications role can collaboratively develop application load scripts with application owners.

   [*Using applications in shared spaces*](managing-apps-in-spaces.htm)

   [*Granting access to sheets, sheet groups, bookmarks, and stories*](../Share/make-public-or-private.htm)
7. Add the target audience for the application to the space

   When the application is ready for its target audience, you can add them to your space.

   If this space is used purely for development, you can move the application to another space to which the application audience has access.

   [*Managing permissions in shared spaces*](managing-shared-spaces.htm)

   [*Moving applications between spaces*](managing-apps-in-spaces.htm#Moving)
8. Update your application

   You may receive feedback from your application audience. An application in a space can be updated at any time with changes to the data model or content in the application.
9. Retire an application from the shared space

   When the application is no longer required, you can delete it.

   [*Deleting applications*](../Apps/delete-app-cloud-hub.htm)
10. Retire the space

    When the space is no longer required, you can delete it.

Related learning:

- [Getting Started with Qlik Cloud](/lnk/Getting_started_Qlik_Cloud)
- [How do I create spaces and organize applications in Qlik Cloud?](/lnk/How_create_spaces_organize_apps_Cloud)
- [Differentiate and manage Qlik Cloud spaces](/lnk/Differentiate_manage_spaces)
