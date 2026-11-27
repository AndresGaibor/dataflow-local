---
title: "Monitoring data with alerts"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Alerting/monitoring-changes-with-alerts.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Using analytics to explore data"]
---

# Monitoring data with alerts

Detect outliers and anomalies in your data quickly with alerts, without the need to open the application. You define conditions based on [measures](#glossary-1 "Glossary term") or [dimensions](#glossary-2 "Glossary term") of the data that you want to monitor. When the conditions are met, a notification with a preview of the data is sent to you.

## When to use alerts

The two main things to consider when setting up an alert are:

- Which data do I want to monitor?

  - You can monitor any measure, including measures used in a visualization and master measures. If you want to reuse measures, you can create master measures before setting up the alert. For more information, see [*Reusing measures with master measures*](../Measures/create-master-measure.htm).
  - You can also split up the data with a dimension to see more detailed data.
  - You can filter the data using selections. You can either use current selections, or selections from a bookmark. For more information, see [*Creating bookmarks*](../Bookmarks/create-bookmark.htm).
- When do I want the alert to be triggered?

  - You can set up multiple conditions that need to be fulfilled to trigger the alert. Each condition compares one of the measures or dimensions in the alert with a value, another measure, the last evaluation, or the current set.
  - For information on conditions, see [*Conditions*](#More).

You can evaluate the alert every time application data has changed, or set a fixed time schedule. You can also set a snooze to stop [notifications](#glossary-3 "Glossary term") for a limited time.

You can share the alert with other users that have access to the application. They will get the same notification, but they cannot edit the alert.

Information noteThe alert that you create is not connected to the [visualization](#glossary-4 "Glossary term") or master items that you use when creating the alert. If you make changes to the visualization, the alert data or conditions are not updated. If you delete the visualization, you will still be able to evaluate and edit the alert.

### Other ways to share data insights

- If you want to receive regular chart or sheet updates based solely on a schedule, you can create a subscription. For more information, see [*Scheduling reports with subscriptions*](../Reporting/Subscriptions/Subscription-reports.htm). You can add Qlik users to a subscription.
- If you want to generate customizable reports based on an entire application and send them to recipients outside of your Qlik Sense environment, see [*Reporting from Qlik Cloud Analytics with Qlik Automate*](../Reporting/Automations/Reports-with-application-automations.htm).
- The Discovery Agent offers AI-assisted anomaly and outlier detection. With this service, insights are generated and presented to users in a scrollable feed, making it easier to detect when your data has changed over time.

## Prerequisites

There are some prerequisites for creating an alert:

- Data alerts must be enabled on the tenant. A tenant admin can enable data alerts in the Settings page in Administration. For more information, see [*Enabling and managing data alerts*](../Admin/mc-managing-alerts.htm).
- You need to have view permissions for the application in which you want to create an alert.
- If you want to share an alert that you created with other recipients:

  - The sheet must be public if you want the recipients to be able to go to the sheet from the notification.
  - All recipients must have view permissions for the application. Alerts can be shared with recipients who do not have view permissions, but in this case the evaluation of the alert will fail.
  - If the application data is reduced with [section access](#glossary-5 "Glossary term") the recipients must have access to data used in [selections](#glossary-6 "Glossary term") in the alert. Alerts can be shared with recipients who are not defined in the section access, but in this case the evaluation of the alert will fail.

## Creating an alert

You can create an alert based on a visualization that you want to monitor, or any master measure or dimension in your application.

Do the following on the [sheet](#glossary-7 "Glossary term") in analysis mode:

1. Right-click on a visualization, and select Alerts and then Create new alert.
2. Enter a title and description for the alert.

   The title is copied from the title of the [chart](#glossary-8 "Glossary term") but you can change it.
3. The measures in the chart are automatically added to Add data to the alert. You can drag the measures to reorder them. You can also expand the measure to edit the name and expression, or delete the measure from the alert.

   You can see the result in Preview data.
4. Click Add additional measure to add one or more additional measures to display in the notification.

   You can use master measures, and measures based on an expression.

   Tip noteLater when you define the conditions for the alert, you can only use measures that are defined in the alert, so you should add them now.
5. You can get more specific results by splitting up the measure values by a dimension. The first dimension in the chart is selected by default, but you can select another dimension in Show by dimension.
6. If you want to show more detailed data, expand Selections.

   You can show the result using the current selections in the application, with no selections or with selections from a [bookmark](#glossary-9 "Glossary term"). You can also click Edit to make a custom selection.

   The selections are stored in the alert. This means that they are not affected if you delete the bookmark.
7. When the result displayed in Preview data meets your expectations, click Next.
8. Add the conditions that you want to use to trigger the alerts. You can compare a measure with a value, another measure, the last evaluation, or the current set. You can also define an offset when comparing the values. You can combine multiple conditions with AND and OR.

   [*Setting conditions for alerts*](setting-conditions-for-alerts.htm#More)
9. When you have defined the conditions, you can check under Preview to see if the alert would trigger with the current data. If Preview shows that the alert would not trigger when you expect it to, see [*Troubleshooting alerts*](troubleshooting-alerts.htm). When you are done, click Next.
10. You can schedule when to evaluate the alert. The following options are available:

    - When data changes: Evaluate the alert only when application data has changed. Changes in application data are recognized as either of the following:

      - Data values in the application change after a reload.
      - Data values change in a source application, and then the application is republished to a managed space using the Include data option (given that the alert is configured for the published application).
    - Fixed time schedule: You can create a Daily, Weekly, Monthly, or Yearly schedule. The scheduled interval can be widely customized regarding times, dates, and months. You can also set when to start and stop evaluating the alert.
11. You can stop notifications by the alert for a limited time with Snooze notifications. If you keep the setting Off, you will be notified every time the alert is triggered. If the alert is shared, notifications for this alert stop for a limited time for all recipients as well.
12. You can share the alert with other recipients. Make sure that all recipients have access to the application. Recipients can turn off notifications about alerts at any time.
13. Click Create to finish.

The alert is now created, and when it is triggered by the conditions you receive a notification. For more information about notifications, see [*Customizing alert notifications*](#Receivin) and [*Managing space notifications*](../Spaces/notifications-space.htm).

Warning noteA user may have access to visibility of all other users within the same tenant - such visibility may include (but may not be limited to): user names, email addresses and the user’s subject, which is a unique string used to identify the user that is provided to Qlik Cloud by the configured Identity Provider.

## Editing an alert

You can edit alerts that you own. There are two ways you can edit an alert.

- You can edit an alert in the Alerts page. To open the Alerts page, click Alerts from the Analytics [activity center](#glossary-10 "Glossary term") or click Alerts from the user profile menu. In the list of alerts, select Edit from the action menu of the alert that you want to edit.

  Tip noteYou can also click an alert to open it, and then click Edit.
- You can also right-click on any visualization in the application, select Alerts, and then select the name of the alert.

The alert is opened in the application and the sheet where it was created, with the selections used in the alert. You can edit the alert, and then save it.

## Conditions

You can set up multiple conditions that need to be fulfilled to trigger the alert. Each condition compares one of the measures or dimensions in the alert with:

- Another value that can be fixed, or calculated by an expression.
- Another measure.
- An [aggregation](#glossary-11 "Glossary term") of the current data set.

You can combine multiple conditions with AND and OR. You can also create multi-step conditions by grouping conditions and applying them in order.

You can also compare using an offset, a value that you want to offset the returned value by.

For more information about how to set conditions for alerts, see [*Setting conditions for alerts*](setting-conditions-for-alerts.htm).

## Customizing alert notifications

By default, you will receive notifications when:

- An alert you own or subscribe to is triggered.
- You are added to an alert.
- An alert you own or subscribe to stops or fails.

You can receive notifications in several ways:

- Web: In the browser when you are using Qlik Sense.
- Push: On your mobile if you have the Qlik Analytics mobile application installed.

  Qlik Cloud Government noteThe Qlik Analytics mobile application is not supported in a Qlik Cloud Government [subscription](#glossary-12 "Glossary term").
- Email: Notifications are sent to the email address registered for the account.
- Daily email digest: Selected notifications are gathered in a single email, which is sent daily to the email address registered for the account.

You can manage notifications in your personal settings. From your user profile menu, go to Settings > Notifications to change your global alert settings. To edit the settings for a specific alert, open Alerts in the Analytics activity center, find the alert, click the ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) menu, and select Notifications.

## Learn more

- [*Managing your alerts*](managing-your-alerts.htm)
- [*Troubleshooting alerts*](troubleshooting-alerts.htm)
- [*Tutorial - Alerts*](../Tutorials/alerting-example.htm)
- [How do I create a data alert in Qlik Cloud?](/lnk/How_create_data_alert_qlikcloud)

Related learning:

- [How do I create a data alert in Qlik Cloud?](/lnk/How_create_data_alert_qlikcloud)
