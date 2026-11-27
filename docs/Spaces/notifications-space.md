---
title: "Managing space notifications"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/notifications-space.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Collaborating with other users", "Working in spaces"]
---

# Managing space notifications

You can receive [notifications](#glossary-0 "Glossary term") for activities and events in [shared](#glossary-1 "Glossary term") and [managed](#glossary-2 "Glossary term") spaces.

Your notifications can be managed from Settings in the profile menu for all your space-related notifications, or from Notifications in an individual space. In Notifications, you can subscribe to events and actions by selecting the method of notification you would like to receive.

For information about setting default notification settings, see [*Managing your personal settings*](../Introduction/profile-settings.htm).

Information note

Groups cannot receive notifications. If you have been added to a space as a part of a group, you cannot receive notifications from that space.

Information note

Email notifications require an email server configured for your tenant. If email notifications cannot be selected in Notifications, your tenant administrator may not have configured an email server.

Information note

Web notifications are available for 90 days, after which they are deleted.

## Changing notification settings for all spaces

You can configure the default ([tenant](#glossary-3 "Glossary term")-level) settings for all spaces you can access in the Qlik Cloud tenant. Default notification settings are configured in Settings.

The default notification settings apply to all spaces you can access, unless a custom notification has been created for an individual space or resource within it.

When custom notifications are set for an individual space or resource (example: an application), the order of priority outlined at [*Custom notifications*](#Notification) is applied to evaluate whether the notification will still be sent.

Do the following:

1. Go to your personal settings by opening your user profile menu in Qlik Cloud and clicking Settings.
2. Under Default notifications, expand notification categories as needed.
3. Check or clear the checkboxes for each notification and delivery preference.

## Changing notification settings for an individual space

When you change the notification settings for a single space, you are setting custom notifications. Custom notification settings applied to an individual space override the default settings that are configured in Settings.

When custom notifications are set for an individual space or resource (example: an application), the order of priority outlined at [*Custom notifications*](#Notification) is applied to evaluate whether the notification will still be sent.

Do the following:

1. In the Analytics activity center, open Catalog.
2. Select a space using the filter options.
3. Click Space settings, and then select Notifications.
4. Expand notification categories as needed.
5. Check or clear the checkboxes for each notification and delivery preference.

Existing custom notifications can also be changed or removed from your Settings.

## Custom notifications

There are three levels of notification settings in Qlik Cloud: default ([tenant](#glossary-4 "Glossary term")-level), space-level, and resource-level. Space-level and resource-level notification settings are custom notifications. They are organized in the following structure, from most global to most granular:

- Default notifications (Added in Settings)

  - Space-level (Added in Catalog)

    - Resource-level (for example, an individual application)

With custom notifications, default and space-level notifications can be overridden by configuring custom settings for entities (spaces or resources) located within that specific entity.

When evaluating whether or not to send notifications for a resource, the setting on the most granular (deeply nested) item in the structure takes priority. In other words, the following order of priority applies (with item 1 being of highest priority, and so on):

1. Resource-level (for example, an individual application)
2. Space-level (Added in Catalog)
3. Default notifications (Added in Settings)

### Example

Suppose these are all the settings that have been configured by a user for failed reloads:

- A default (tenant-level) notification setting to only send web notifications.
- A space named ExampleSpace has a notification setting to send all types of notifications, including web notifications.
- An application in ExampleSpace, named ExampleApp, has a notification setting to not receive any type of notification.

In this example, all applications in the tenant except those in ExampleSpace will generate web notifications only. All applications in ExampleSpace except ExampleApp will generate all types of notifications, including web notifications. ExampleApp will not generate any notifications.

## Learn more

- [*Managing your personal settings*](../Introduction/profile-settings.htm)
- [Getting Started with Qlik Cloud](/lnk/Getting_started_Qlik_Cloud)

Related learning:

- [Getting Started with Qlik Cloud](/lnk/Getting_started_Qlik_Cloud)
