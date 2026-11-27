---
title: "Managing your personal settings"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/profile-settings.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Introducing Qlik Cloud", "Qlik Cloud interface overview"]
---

# Managing your personal settings

On the Settings page in Qlik Cloud, you can manage personal settings, such as language, notifications, spaces, and the Qlik Analytics mobile app.

To open your personal settings, click your user profile in Qlik Cloud, then select Settings.

Information noteTo update your Qlik Account profile or security settings, click Account settings, or select Manage account from the profile menu. For more information, see [*Editing your user profile*](manage-user-profile.htm).

The personal settings page

![Personal settings page](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_personal-settings-rev.png "Click to view full size")

## Profile

Set your:

- Start location – Select the activity center that opens first when you sign in.
- Language
- Time zone
- Regional settings – Specify the region used for creating applications and preparing data.

You can also:

- View the roles that are assigned to you in the tenant.
- Clear your selected do not show again selections in dialogs, so you are offered the dialogs again.
- Activate and deactivate session replay. See [*Session replay in Qlik Cloud*](session-replay.htm).

## Notifications

Control when and how you're notified about activity in Qlik Cloud. Notifications help you stay informed about changes in spaces, notes, alerts, automations, data integration, glossaries, and more.

### Default notifications

You can configure notifications for the following areas:

- Spaces:

  - Notifications when you are added or removed from a space or when your space permissions are updated.
  - Notifications when a user requests access to content in a space.
  - You can customize notifications for a single space by going to Space settings > Notifications. For more information, see [*Managing space notifications*](../Spaces/notifications-space.htm).
- Apps:

  - Tenant admins and analytics admins can receive notifications when application reloads fail.
  - Any user can receive notifications if a scheduled reload for an application failed, stopped, or was disabled.
  - You must be the owner of the associated task to receive notifications for reload issues.
  - You can customize notifications for a single application by clicking ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on an individual application, then selecting Notifications.
  - For more information, see [*Applications (Insights and Analytics)*](../QlikCloudNavigation/navigating-activity-center-content.htm#Apps).
- Scripts: Notifications when reloads of a script failed. You can also receive a notification when an execution of a task for scheduled reloads has failed, stopped, or was deactivated, if you are the owner of that task. For more information, see [*Working with scripts in the catalog*](../ScriptEditor/using-the-script-editor.htm).
- Data flows: Notifications when runs of a data flow failed. You can also receive a notification when an execution of a task for scheduled runs has failed, stopped, or was deactivated, if you are the owner of that task. For more information, see [*Managing data flows*](../DataFlow/managing-data-flows.htm).
- Table recipes: Notifications when runs of a table recipe failed. You can also receive a notification when an execution of a task for scheduled runs has failed, stopped, or was deactivated, if you are the owner of that task. For more information, see [*Managing table recipes*](../TableRecipe/managing-table-recipes.htm).
- Notes: Notifications when you are invited to edit, or are mentioned in a note. For more information, see [*Notifications*](../Notes/notes-overview.htm#NotificationsNotes).
- Alerts: Notification when an alert is triggered, an alert stopped or failed to evaluate, or you are added to an alert. For more information, see [*Customizing alert notifications*](../Alerting/monitoring-changes-with-alerts.htm#Receivin).
- Automations: Notification when an automation fails to run.
- Qlik Predict: Notifications for Qlik Predict events. For more information, see [*Configuring notifications for Qlik Predict*](../AutoML/automl-customize-experience.htm#Configur).
- Glossaries: Notifications when a glossary term is created, deleted, or updated. For more information, see [*Working with business glossaries*](../Catalog/BusinessGlossary/Working-business-glossaries.htm).
- Data tasks: Notifications for operation of data tasks in Qlik Talend Data Integration. For more information, see [*Setting notifications for changes in operation*](../DataIntegration/Introduction/Notifications.htm#Setting).
- Data gateways: Notification for operation of data gateways. For more information, see [*Setting notifications for changes in operation*](../DataIntegration/Introduction/Notifications.htm#Setting).
- Sprints: Notifications about sprint role changes and record assignments. For more information, see [*Sprint notifications*](../DataIntegration/DataStewardship/Sprint-notifications.htm).

### Custom notifications

If you change notification settings at the space level for a specific item (such as an individual application or note), these custom settings override your default notifications for that space or item.

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

## Spaces

View lists of [shared](#glossary-0 "Glossary term") and [managed](#glossary-1 "Glossary term") spaces in the [tenant](#glossary-2 "Glossary term"). You can:

- View space details
- Delete spaces

## Qlik Analytics mobile app

Manage the devices being used for the Qlik Analytics mobile app or download the application.

For more information, see [*Managing push notifications*](../Mobile/qsmsaas-using.htm#Managing).

## API keys

Generate and manage API keys. You need the appropriate permissions to use this feature.

For more information, see [*Managing API keys*](../Admin/mc-generate-api-keys.htm).

## GitHub configuration

If you want to work with version control in Qlik Talend Data Integration, you must set up a personal connection to GitHub using a GitHub user account. For more information and details about requirements and preparation, see [*Manage your pipeline projects with version control*](../DataIntegration/VersionControl/Project-version-control.htm).

1. Set up authentication using a GitHub Personal access token and your Organization in GitHub.
2. Click Test connection to make sure authentication is correct.
3. Click Create.

Information noteA connection of the type GitHub - Version Control will be created in your personal space.

## Tools

You can download the following tools to be used with Qlik Cloud:

- Qlik Sense Mobile SaaS application.
- Qlik Sense Desktop: On-premises installation for analytics locally and offline. You can also authenticate your installation of Qlik Sense Desktop .
- Qlik DataTransfer: Upload on-premises data to the cloud.
- Qlik Lineage Connectors: Upload lineage and metadata from your on-premises BI tools and data sources to Qlik Cloud.

For an alternative way to download Qlik products, see [*Downloading tools and installation files*](Download_install_files.htm).

Related learning:

- [Getting Started with Qlik Cloud](/lnk/Getting_started_Qlik_Cloud)
