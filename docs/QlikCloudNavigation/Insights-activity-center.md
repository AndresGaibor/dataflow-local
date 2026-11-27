---
title: "Insights activity center"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikCloudNavigation/Insights-activity-center.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Cloud Analytics activity centers"]
---

# Insights activity center

The Insights activity center provides options for consuming applications and other analytic content. Insights offers a focused and curated experience for analysts exploring analytic content.

Insights activity center

![Insights activity center](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Navigation/ui_activity-center-Insights-rev.png "Click to view full size")

Insights contains the following sections:

- Home
- Feed
- Favorites
- Collections
- Browse

Previously, the Insights activity center was part of the Qlik Cloud Analytics hub. Insights offers no options for creation.

## Home

After your first login, you will start in Home when you log into Qlik Cloud. Here, you can view various content, including your applications, scripts, charts, and notes. You can easily customize what collections of content appear in your home.

### Customizing Home

Click Add widgets to customize your personal Home. Choose from favorites, collections, applications, data, charts, notes, ML experiments, automations and scripts. You can also show content that has been recently used, created, or updated.

Click a widget to add or remove it from your home page.

Customize the widgets shown on your home page.

![The Add widgets dialog.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_add_widgets.png "Click to view full size")

You can also rearrange or remove sections directly on the home page:

- To move a widget vertically, click and hold ![drag handle](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_draggable.svg) next to the widget and move it into place.
- To remove a widget, hover to the right of the widget and click the More actions menu (![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg)) that appears. Then select Remove.

#### Tenant-wide custom home pages

Administrators can add tenant-wide customized home pages for Insights, allowing the promotion of specific content to all users in the tenant. The custom page appears as a tab in Home, next to your Personal page. For more information, see [*Customizing the Insights activity center Home*](../Admin/mc-administer-customized-home.htm).

## Feed

The Feed section is a curated, scrollable collection of insights from applications for which you have access. The feed is available with the Discovery Agent.

The feed is available from both the Insights and Analytics activity center.

For more information, see [*Analyzing Discovery Agent feeds*](../DiscoveryAgent/feeds.htm).

## Favorites

The Favorites section contains all content you have favorited. Your favorites are not shared with other users. Favorite content in your activity centers by clicking ![Favorite](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_star_2.svg).

## Collections

Collections enable you to group content such as applications, charts, notes, and links.

To add content to a collection, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) > Manage > Add to collection on any content type.

If you are using the Qlik Analytics mobile app, you also have a Mobile Content collection. Applications that you have opened in the Qlik Analytics mobile app are automatically added to Mobile Content.

By default, collections are private. Tenant admins, analytics admins, and other designated users can make collections public to share them with all other members of the tenant. Public collections do not change members' access to content in spaces. Members will only be able to see content in public collections to which they already have access.

To make a collection public, click ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the collection, select Make public, and click Make public. To make a public collection private again, click ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg), select Make private, and click Make private.

Tip noteYou can also set the visibility of a collection when creating it. Use the Visibility drop down menu and select Private or Public.

For more information, see [*Managing public collections*](../Admin/public-collections.htm).

## Browse

Browse offers access to the content available to the user from the Qlik Cloud Analytics catalog. In Browse, you can view the applications and spaces to which you have access, as well as other analytic content. Browse allows you to filter by:

- Spaces
- Search terms
- Content types:

  - Charts
  - Applications
  - Notes
  - Links
  - Assistants
- Owners
- Creators
- Tags

You can select individual spaces from the spaces drop-down to view content from that space. Select All filters to display the filter pane. When the filter pane is active the All filters box is grayed out. The box displays the number of active filters.

You can view content in either the Tile ![Select tile icon for tile view](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ic_profile_tile.svg) or List ![Select list icon for list view](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ic_profile_list.svg) view.

Applications and other content can be sorted alphabetically, by creation date, by modification date, or recently used. You can filter content by those you own or by those others own.

Browse section

![Browse section of the Insights activity center ](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Navigation/ui_activity-center-Insights-browse-rev.png "Click to view full size")

### Spaces

Spaces are areas where applications and other content are stored. Spaces can be personal, shared, or managed.

All users have a [personal space](#glossary-0 "Glossary term") where applications they create are stored by default. Personal spaces are private. You can share your personal content by moving them to a shared space.

Users with the Shared Space Creator role can create shared spaces.
Shared spaces are private when first created. Shared spaces allow collaborative development of applications and other content. Spaces also limit access to applications in the space. Access to applications in the space is granted by adding members to the space.

Managed spaces can be created by [tenant](#glossary-1 "Glossary term") or analytics administrators, or users with the Managed Space Creator role.
Managed spaces are used to provide strictly controlled access to applications that might have sensitive data. Applications are developed in other spaces and then published to the managed space.

You can select spaces to which you have access from the drop-down in Browse.

For information on spaces, see:

- [*Navigating spaces*](../Spaces/navigating-spaces.htm)
- [*Working in spaces*](../Spaces/Spaces.htm)

## Alerts

In Alerts, you can view a list of all alerts owned by you, as well as alerts to which you have been added as a recipient. The Alerts page contains details about each alert, including its name, owner, associated application, and whether it is being evaluated on a schedule.

In the Insights activity center, Alerts becomes available after you create your first alert.

You can filter and sort the alerts on the Alerts page. You can refine your list by alert owner (anyone, you, or others), or search for alerts owned by a specific user. The alerts in the list can be sorted by time of last evaluation, the last time triggered, or alphabetically by name.

## Subscriptions

In Subscriptions, you can view and modify subscriptions you own, as well as subscriptions to which you have been added as a recipient. The Subscriptions page contains details about each subscription, including its name, owner, associated application, and schedule.

You can filter and sort the subscriptions on the Subscriptions page. You can refine your list by owner (anyone, you, or others), or search for subscriptions owned by a specific user. The subscriptions in the list can be sorted by time last sent, time they are next scheduled to be sent, or alphabetically by name.

For more information about creating and managing subscriptions, see [*Scheduling reports with subscriptions*](../Reporting/Subscriptions/Subscription-reports.htm).

## Learn

Learn contains videos, courses, and more to help you get started with analytics in Qlik Cloud. Learn provides both learning paths and learning resources for users new to Qlik Cloud.

Learning paths are courses designed to help you get started in your activity center. Each activity center has its own learning path. When you open Learn, your activity center's learning path will be selected. You can switch between learning paths by selecting them from the learning path menu.

Learning resources are other helpful content relevant to your learning path. These resources include:

- Videos: Helpful videos showing tasks and features in Qlik Cloud.
- Guided tours: Product tours that guide you through different sections and tasks in Qlik Cloud.
- Links: Links to useful resources and help content.

The learning resources displayed are initially filtered to your current learning path. You can filter the content by type. You can also filter it by activity centers.

Learn also includes links to Qlik Community, Qlik Continuous Classroom, and Qlik Support.
