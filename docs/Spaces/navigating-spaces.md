---
title: "Navigating spaces"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/navigating-spaces.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Cloud Analytics activity centers"]
---

# Navigating spaces

Spaces are areas in Qlik Cloud where applications, scripts, and other content are stored. This is where you manage content, members, data sources, connections, and [notifications](#glossary-0 "Glossary term") for spaces.

Shared and managed spaces are divided into the following sections:

- Details
- Notifications
- Members
- Data files
- Connections

You can access these sections by selecting Space settings in a shared or managed space.

In a personal space, you can only select Data files and Connections. Select your user profile menu to manage other personal space settings.

When you make any changes to user's permissions for applications or scripts, these changes are not instantly reflected in actively opened applications and scripts. To ensure that the changes to the user's permissions are updated, the user must close all browser tabs belonging to the affected application or script and wait at least two minutes (application session's Time To Live), then re-open the application. This applies to application and script permissions in personal, shared, and managed spaces. Changes in permissions for newly opened applications are reflected instantly.

## Details

You view space information in Details, including description, space owner, and space creator.

The Details section

![The Details section of a shared space](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_space_navi_details.png "Click to view full size")

## Notifications

You can manage your subscriptions for content in the space from Notifications. You can subscribe to events or actions in a space by selecting the event or action under the notification type.

[*Managing space notifications*](notifications-space.htm)

## Members

Space owners and users with the Can manage role can view all the members of a space in Members. They can do the following:

- Add members
- Change member permissions
- Remove members

[*Managing permissions in shared spaces*](managing-shared-spaces.htm)

[*Managing permissions in managed spaces*](managing-managed-spaces.htm)

Depending on the subscription and purchased features on it, additional actions might be available:

- View and manage applications that are shared with non-space members

  [*Sharing applications with users who are not space members*](sharing-content-with-non-space-members.htm)
- View and manage applications that have anonymous access activated (only applicable to Qlik Anonymous Access subscriptions, and in managed spaces)

  [*Sharing application content with anonymous access*](../Share/share-anonymous-access.htm)

The Members section of a shared space.

![The members section of a shared space.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_space_navi_members.png "Click to view full size")

## Data files

You can view all data files added to the space in Data files. If you have the permissions, you can also add data files to the space.

[*Managing data files*](manage-data-files-spaces.htm)

Information note

Users with Can view cannot view the data sources in a space.

The Data files section of a shared space

![Image showing the entire 'Data files' interface, including toolbar, path selector, and table](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_catalog_data-files-space.png "Click to view full size")

## Connections

You can view all data and automation connections added to the space in the respective tabs in Connections. If you have the permissions, you can also add connections to the space.

The Data Connections section of a shared space for data and automation connections

![The Data connections section of a shared space](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_space_navi_connections_data.png "Click to view full size")

The Automation Connections section of a shared space for data and automation connections

![The Automation connections section of a shared space](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_space_navi_connections_automation.png "Click to view full size")

Related learning:

- [How do I share my applications with Qlik Cloud?](/lnk/How_share_apps_Cloud)
