---
title: "Working in managed spaces"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/working-in-managed-spaces.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Collaborating with other users", "Working in spaces"]
---

# Working in managed spaces

A [managed space](#glossary-0 "Glossary term") is a governed section of Qlik Cloud Analytics.
You can find your managed spaces using the spaces drop-down in Catalog.

Information noteManaged spaces are not available in Qlik Cloud Analytics Starter or Qlik Sense Business.

Applications can be published to a managed space from [personal spaces](#glossary-1 "Glossary term") and [shared spaces](#glossary-2 "Glossary term"). Publishing creates a copy of the application in the managed space. Published applications maintain a relationship to the original application for republishing.

Data products can also be published to managed spaces when activated on the data marketplace. Publishing creates a copy of the data product in the managed space.

Managed spaces are restricted to members. When you add a member to a space, you assign them a space role. The role is a set of [permissions](#glossary-4 "Glossary term") that they have on that space and objects contained inside the space.

The following space roles are available in managed spaces:

- Owner: Can manage the space and its members, as well as open applications in the space. This is not a role you can assign to other members of the space unless you are an administrator. This space role also cannot be removed from the space member without administrator action. It is not possible to remove a member with the Owner role from the space, unless you have access to the Administration activity center as an administrator.
- Can manage: Can manage the space and its members.
- Can publish: Can publish applications to the space. They cannot open applications in the space.
- Can contribute: Can view and open applications in the space. Contributors can create private content in the application and make that content public.
- Can view: Can view and open applications in the space.
- Has restricted view: Can view and open applications in the space.
- Can consume data: Can consume data sources, but cannot create or edit data sources. They cannot create content or manage the space. See [*Adding and managing your analytics data*](managing-data-resources-spaces.htm#Managing) to learn about data sources inside a space.
- Can operate: Can reload applications and create scheduled reloads.

Members can have multiple roles assigned to them. Applications in the space can be opened by space members with Owner, Can manage, Can contribute, or Can view space role. For a detailed look at the permissions granted with each role, see [*Managing permissions in managed spaces*](managing-managed-spaces.htm).

Applications in a managed space can also be opened by non-space members with whom the applications have been shared, see:[*Sharing applications with users who are not space members*](sharing-content-with-non-space-members.htm).

Applications published to a managed space keep the data loaded in the application, but do not include their data files or data connections. To keep data current, data sources should be added to the managed space. For more information, see [*Data sources for applications in managed spaces*](app-data-managed-spaces.htm).

All actions in a managed space, such as opening an application, are logged in the Administration activity center.

## Creating managed spaces

Tenant admins, analytics admins, and users with the Managed Space Creator user role can create managed spaces. For more information, see [Assigning security roles.](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/SaaS-roles.htm)

Space owners can be changed in the Administration activity center by [tenant administrators](#glossary-5 "Glossary term") or analytics administrators.

Do the following:

1. Go to the Create page of the Analytics [activity center](#glossary-6 "Glossary term") and select Space.
2. Select Managed space.
3. Enter a name and a description for the space. The name must be unique.
4. Click Create.

## Adding members to managed spaces

Members can be added to the space by the tenant administrator, analytics administrator, or members with Can manage role.

If groups are allowed in the tenant, you can add groups of members to your space. If a space member has individual permissions and group permissions in a space, the highest permission level is applied.

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

## Removing members from managed spaces

You can remove members from a space.

Do the following:

1. In the space, click Space settings and select Members.
2. Under Role, click ![Arrow down](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_down.svg) next to the member to remove.
3. Click Remove.

Tip note

Click Undo in the pop-up that appears if you want to re-add the member to the space.

## Deleting managed spaces

The tenant administrator, analytics administrator, or a user with the Owner or Can manage role can delete a space.

Do the following:

1. In the space, click Space settings and select Delete space.
2. Click Delete.

## Developing and publishing applications for managed spaces

This is a sample workflow for using managed spaces.

1. Create an application with mock data

   Application developers create an application using mock data, either in a personal space or in a shared space. They add data sources and create a data model.

   [*Creating applications and adding data*](../Apps/create-app-cloud-hub.htm)

   [*Data sources for applications in managed spaces*](app-data-managed-spaces.htm)
2. Create a managed space

   The tenant administrator, analytics administrator, or a user with the Managed Space Creator user role creates a managed space.
3. Add administrators to the managed space

   Tenant or analytics administrator transfers ownership of the space to a user who will have full access to applications in the space and can add members with the Can manage role to the space. These users will have administrator privileges in the space.
4. Add publishers to the space

   The space owner or members with the Can manage role can add members with the Can publish role to the space. If members need access to the space, additional permissions can be granted.
5. Publish the application to the managed space

   Once the application is ready for consumption, members with the Can publish role can publish their applications to the managed space. The managed space owner or members with the Can manage role add the data sources referenced in the application load script to the space.

   Different copies of an application can be used to republish an application in a managed space. For example, in workflows with separate development and verification shared spaces, an application might be published from the development space. Later, updates made to the copy in the verification space can be republished from that space to the managed space.

   [*Publishing applications to managed spaces*](managing-apps-in-managed-spaces.htm#Publishi)
6. Add viewers and contributors to the managed space

   The space owner and members with the Can manage role can add the space's target audience with Can view, Can contribute, or Can consume data roles.
7. Create a reload schedule for the application

   The space owner can schedule reloads for the application in the managed space.
8. Publish updates to the application

   As updates are made to the application or data in the application, publishers can republish the updated application to the managed space.

   [*Publishing applications to managed spaces*](managing-apps-in-managed-spaces.htm#Publishi)
9. Retire an application from the managed spaces

   When the application is no longer required, administrators can delete it from the managed space.
10. Retire the space

    When the space is no longer required, you can delete it.

Related learning:

- [Differentiate and manage Qlik Cloud spaces](/lnk/Differentiate_manage_spaces)
