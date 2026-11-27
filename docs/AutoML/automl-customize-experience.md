---
title: "Customizing your Qlik Predict experience"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/automl-customize-experience.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict"]
---

# Customizing your Qlik Predict experience

Your Qlik Cloud experience can be customized to improve your interactions with Qlik Predict.

## Customizing your activity center

You can improve your Qlik Predict experience by customizing what appears in the Analytics [activity center](#glossary-0 "Glossary term") when you log into a tenant.

You can add or remove items from your Home by clicking Customize your home. Add or remove favorites, specific collections, data, ML experiments, and ML deployments to allow a smoother interaction with the activity center.

Add Qlik Predict items to your Favorites by clicking ![Add to favorites](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_star_2.svg) on the item in the Analytics activity center.
Click ![Remove from favorites](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_star.svg) to remove the item from Favorites.

You can add a Qlik Predict item to a collection by right-clicking it and selecting Manage > Add to collection.

For more information, see [*Analytics activity center*](../QlikCloudNavigation/Analytics-activity-center.htm).

## Configuring notifications for Qlik Predict

As a user in the Qlik Cloud tenant, you can customize your Qlik Predict notifications to meet your preferences. Each individual user's notification settings are unique to that user. Notifications can be adjusted for the entire tenant (global) or for a particular shared or managed space. Notification settings applied at the space level override the global notification settings for that space.

The following notifications can be adjusted at both the tenant and space level:

- An ML deployment is created
- An experiment version is ready
- A model completed training
- A prediction is created from an ML deployment
- The ability to use predictions has changed for a deployed model

### Notification delivery options

Choose how you want to receive notifications. You can select one or more delivery methods:

- Web notifications: In the browser when you are using Qlik Cloud.

  Information note

  Web notifications are available for 90 days, after which they are deleted.
- Push notifications: To your mobile if you have the Qlik Analytics mobile application installed. For more information, see [*Managing push notifications*](../Mobile/qsmsaas-using.htm#Managing).
- Email: Notifications are sent to the email address registered for the account.
- Email digest: Selected notifications are gathered in a single email, which is sent daily to the email address registered for the account. You can set the starting time for your daily digest.

To temporarily stop receiving notifications via push, email, and email digest, click Pause notifications in the upper-right corner. Web notifications will continue during this time.

Notifications remain paused until you manually resume them by clicking Resume notifications. You can do this on:

- The personal settings page
- Notification settings for a space
- Notification settings for an individual resource (such as a note)

Information noteWhen you resume notifications, you will not receive any notifications that were triggered while notifications were paused.

### Global notifications

Global notification settings are configured to manage an individual user's notifications for the entire tenant.

Do the following:

1. Open your user profile menu and click Settings.
2. Click Notifications.
3. Expand the menu for Qlik Predict.
4. Click the checkboxes for each notification event and delivery option to meet your preferences.

For more information, see [*Notifications*](../Introduction/profile-settings.htm#Notifica).

### Space-level notifications

You can configure notification settings to override your global settings for a particular space.

Do the following:

1. Open a shared or managed space in the catalog and click Space settings.
2. Click Notifications.
3. Expand the menu for Qlik Predict.
4. Click the checkboxes for each notification event and delivery option to meet your preferences.

Any differences between global and space-level notification settings will be listed in your Settings under Custom notifications. From here, you can edit delete notification settings configured at the space level.

Do the following:

1. Open your user profile menu and click Settings.
2. Click Notifications.
3. Under Custom notifications, expand the desired tab.
4. Click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) to edit the setting, or click ![Remove](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cross.svg) to reset it to the default.

For more information, see [*Managing space notifications*](../Spaces/notifications-space.htm).
