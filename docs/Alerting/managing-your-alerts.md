---
title: "Managing your alerts"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Alerting/managing-your-alerts.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Using analytics to explore data", "Monitoring data with alerts"]
---

# Managing your alerts

Click Alerts in the Analytics [activity center](#glossary-0 "Glossary term") to see a list of alerts owned by you, as well as alerts that have been shared with you.

You can click on an alert to see more details, or you can use the action menu to the right of each alert.

You can filter and sort the alerts on the Alerts page. You can refine your list by alert owner (anyone, you, or others), or search for alerts owned by a specific user. The alerts in the list can be sorted by time of last evaluation, the last time triggered, or alphabetically by name.

## Managing alerts that you own

If you are the owner of the alert, you can perform the following actions:

- Details

  View details, history, recipients, and notification preferences.
- Notification settings

  Manage how you want to receive [notifications](#glossary-1 "Glossary term") sent by this alert.

  If you go to Settings > Notifications you can change global alert settings. To change the settings for a specific alert, click Alerts in the Analytics activity center. Find the alert, click the ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) menu, and select Notifications settings.

  Information note

  Web notifications are available for 90 days, after which they are deleted.
- Edit

  Edit the alert in the application with the [selections](#glossary-2 "Glossary term") used to create the alert.
- Evaluate now

  Evaluate the alert manually.
- Enable / Disable

  Turn scheduled evaluation on and off.
- Recipients

  View the recipients of the alert. If you are the owner of the alert, you can remove recipients.
- Delete

  Delete the alert. This deletes the alert for all recipients as well.
- Data & conditions

  View [measures](#glossary-3 "Glossary term"), [dimensions](#glossary-4 "Glossary term"), selections, and conditions used in the alert.
- History

  View the history of when the alert was triggered.

  Information note

  Alert executions are available in History for 90 days, after which they are deleted. If fewer than 10 executions happen within this 90-day period, up to 10 executions older than 90 days are kept in History.

## Managing alerts that have been shared with you

The following actions are available for alerts that have been shared with you.

- Details

  View details, history, recipients, and notification preferences.
- Notifications

  Manage how you want to receive notifications sent by this alert.

  If you go to Settings > Notifications you can change global alert settings. To change the settings for a specific alert, click Alerts in the Analytics activity center. Find the alert, click the ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) menu, and select Notifications settings.

  Information note

  Web notifications are available for 90 days, after which they are deleted.
- Data & conditions

  View measures, dimensions, selections, and conditions used in the alert.
- History

  View the history of when the alert was triggered.

  Information note

  Alert executions are available in History for 90 days, after which they are deleted. If fewer than 10 executions happen within this 90-day period, up to 10 executions older than 90 days are kept in History.
- Unsubscribe

  Unsubscribe from the alert.

### How timezones are displayed for alerts and subscriptions with recurring schedules

In Qlik Cloud activity centers, the time or timezone displayed will usually match the timezone you have set in your personal settings.
One exception is the recurring interval schedule for alerts and subscriptions.

If you look at the Details page for an alert or subscription, you can see the next scheduled run-time under Scheduled. The time under Scheduled will reflect your timezone. If you hover over the ![Info](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_info_outline.svg), a tooltip will appear showing how often the subscription or alert is sent.

This image shows what it looks like when the creator and recipient live in the same timezone:

- The next scheduled run-time is: April 3, 2023 at 2:15 PM.
- The dark grey tooltip shows how often the subscription is sent: Every week, Monday and Wednesday, at 2:15 PM.

A subscription details page, as seen by a recipient who is in the same timezone as the creator.

![A subscription details page, showing a tooltip with the subscription schedule.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_subscription_details_timezone_same.png "Click to view full size")

However, the tooltip will show a ![Warning](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_warning_triangle_2.svg) if the alert or subscription was created in a different timezone than the recipient. In this case, the schedule will be shown in the timezone the alert or subscription was created.

For example, a user in Toronto, Canada (GMT-4) creates a subscription. They add a recipient who lives in Stockholm, Sweden (GMT+2). There is a 6-hour time difference between them. The Swedish recipient checks the details page to find out how often they will receive this subscription. Under Scheduled, the time displayed is in the correct timezone: Stockholm, Sweden. However, if the recipient hovers over the ![Info](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_info_outline.svg), the tooltip shows the entire subscription schedule in the Canadian timezone:

- The next scheduled run-time is March 13, 2023, 3:30 PM.
- The dark grey tooltip shows the subscription schedule, but in the Canadian timezone: ![Warning](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_warning_triangle_2.svg) Created in (GMT -4:00) America/Toronto: Every week, Monday, Wednesday, Friday 9:30 AM.

The schedule of a subscription created in Canada, as seen by a recipient in Sweden.

![The difference between the scheduled timezone and the time the user will receive a subscription email.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_subscription_details_timezone_difference.png "Click to view full size")

## Managing alerts as an admin

Tenant and analytics admins can manage all alerts in the Administration activity center.

- Delete alerts.
- Enable and disable alerts.
- Change the owner of an alert.
- Edit alert schedules.

For admin information, see [*Enabling and managing data alerts*](../Admin/mc-managing-alerts.htm)
