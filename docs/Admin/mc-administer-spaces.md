---
title: "Managing spaces"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-spaces.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Managing data governance and transfers"]
---

# Managing spaces

Spaces in Qlik Cloud are designated areas for organizing and collaborating on applications and data. You can manage spaces from the Spaces page in the Administration activity center.

## Overview of spaces in Qlik Cloud

On the Spaces page, you can view all spaces in the tenant and perform the following actions:

- Create a new space
- Change a space owner
- Manage space members
- Edit a space
- Delete a space

If your subscription includes large application support, you can configure spaces to work with applications that exceed the standard application size. For more information, see [*Large application support*](large-app-support.htm).

## Space types

Qlik Cloud supports four types of spaces:

### Personal spaces

- Only the space owner can edit applications in a personal space.
- Co-development of applications is not possible in personal spaces.
- Applications can be shared for viewing outside the space.
- Users with the Private Analytics Content Creator role can create analytics content in personal spaces.

### Shared space

- Shared spaces enable collaboration and application co-development within a closed group of users.
- The available actions for applications depend on the users space permissions.
- Tenant admins, analytics admins, and users with the Shared Space Creator role can create shared spaces.
- The space creator can add members and assign permissions.

For more information, see [Working in shared spaces](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/working-in-shared-spaces.htm).

### Managed spaces

- Managed spaces provide governed access to applications, ensuring restricted access for members.
- Permissions are assigned to members when they are added to a managed space, defining what they can access within the space.
- Applications developed in personal or shared spaces can be published to a managed space.
- Only space owners and target application consumers can open applications in a managed space, unless users have viewing permissions.
- Tenant admins, analytics admins, and users with the Managed Space Creator role can create managed spaces.

For more information, see [Working in managed spaces](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/working-in-managed-spaces.htm).

### Data spaces

- Data spaces are governed areas of your Qlik Cloud tenant that are used to create and store data projects in Qlik Talend Data Integration.

Information noteIf your organization has a Qlik Talend Cloud Premium or Enterprise subscription, you can organize data spaces into environments and synchronize them with Talend Cloud. For more information, see [*Synchronization between Qlik and Talend - Qlik Talend Cloud subscriptions*](synchronized-resources.htm).

Related learning:

- [Differentiate and manage Qlik Cloud spaces](/lnk/Differentiate_manage_spaces)
- [Administer and allocate space roles in Qlik Cloud](/lnk/Administer_allocate_space_roles)
