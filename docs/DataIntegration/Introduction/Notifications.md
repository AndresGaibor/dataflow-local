---
title: "Setting notifications for changes in operation"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Introduction/Notifications.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Monitoring and operating your data tasks"]
---

# Setting notifications for changes in operation

You can set notifications to be alerted at changes in the operation of your data pipeline. You can get a notification in your browser, by email, or a push message to the Qlik Analytics mobile app.

You can set notifications on different levels:

- Default notifications

  This setting provides notifications for all data tasks and data gateways.
- All data tasks and data gateways in a data space.

  This setting will override default notification settings.
- Individual data tasks and data gateways.

  This setting will override default notification settings and data space settings.

Notifications are available for the following events:

- Data task has stopped due to an error
- Data task status has changed to Stopped
- Data task status has changed to Started
- Table processing was suspended due to errors
- Data gateway state has changed
- Data gateway version requires update
- New data gateway version is available
- DDL changes handled by schema evolution

Information noteTo get notifications about a data gateway or data task, you must be a member of the space where it resides.

Information note

Web notifications are available for 90 days, after which they are deleted.

## Setting default notification settings

You can manage default notification settings in your personal settings.

1. Open your user profile menu and click Settings.
2. Click Notifications.
3. You can change default notification settings for Data gateways and Data tasks under Notifications.

   Set one or more delivery methods for the events that you want be notified for.

Information noteSetting default notifications affect all items. This can result in a large number of notifications in a large deployment.

For more information about setting default notifications in profile settings, see [*Notifications*](../../Introduction/profile-settings.htm#Notifica).

## Setting notifications for a data space

This setting is used for all data gateways and data tasks in the data space, where notifications are not set specifically.

You can set data space notifications in two different ways:

- In Administration > Spaces, click ![More icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on a space, and select Notifications.
- In Space settings for a data space in the Data Integration home, click Notifications.

You can view and edit your data space notifications in Notifications in your personal settings. You find them under Custom notifications> Spaces.

## Setting notifications for a data task

When you set a notification for a data task, this overrides the notification setting for the data space, as well as the default notification setting.

You can set data task notifications in two different ways:

- Click ![More icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on a data task in the data pipeline view, and select Notifications.
- Click ![More icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on a data task in a monitor view, and select Notifications.

You can view and edit your data space notifications in Notifications in your personal settings. You find them under Custom notifications> Data tasks.

Tip noteEmail notifications contain extended error information.

## Setting notifications for a data gateway

You can set notifications to be alerted at changes in the operation of your data gateways.

You can set data gateway notifications in two different ways:

- In Administration > Data gateways, click ![More icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on a gateway, and select Notifications.
- In Space settings for a data space in the Data Integration home, select a data gateway in Gateway agents, and click Notifications.

You can view and edit your data space notifications in Notifications in your personal settings. You find them under Custom notifications> Data gateways.
