---
title: "Scheduling reports with subscriptions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Subscriptions/Subscription-reports.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Using analytics to explore data"]
---

# Scheduling reports with subscriptions

Subscription reports let you schedule recurring emails containing your preferred [sheets](#glossary-0 "Glossary term") or [chart](#glossary-1 "Glossary term"). You can set your desired filters and have a report with the newest data delivered to your inbox at a scheduled time. For example, you could receive overnight order information in an email every morning. You can edit subscriptions you own at any time.

Subscription report delivered via email

![A subscription report email with image and PDF attachment.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_Subscription_email.png "Click to view full size")

Subscriptions follow the same access rules as applications, data, and spaces. Owners and recipients are restricted according to [section access](#glossary-2 "Glossary term"), permissions, and user entitlements (Professional and Analyzer). Recipients will only receive data they have access to.

A subscription report email contains:

- A PDF or PowerPoint file of the subscribed visualization or sheets as an attachment. Image resolution will be 300 DPI.
- An image of the visualization. There is no image if you subscribe to sheets.
- A link to the application, so you can see the original point of analysis. If the subscription includes more than one sheet, the first sheet in the list is opened.
- A link to your subscription management page.

## When to use subscriptions

Subscriptions are generated based on the schedule you set. You should create a subscription if:

- You want regular updates on a chart or up to 10 sheets.
- You do not need to set up something as mathematically complex as an alert.
- You want to produce an export of up to 10 sheets or a chart on a schedule.
- Your recipients have access to Qlik Cloud.
- Your recipients want to be able to add sheets or [charts](#glossary-4 "Glossary term") to PowerPoint files.

### Other ways to share data insights

If you want to receive notifications when certain conditions are met in your data, see [*Monitoring data with alerts*](../../Alerting/monitoring-changes-with-alerts.htm). Alerts are evaluated based on data reloads and are sent based on data exceptions. Alerts can also trigger on a schedule, but you still need to create a condition or target to save an alert. You can add Qlik users to an alert.

If you want to generate customizable reports based on an entire application and send them to any recipient, consider using the value-add Qlik Reporting Service capabilities. These include:

- In-application reporting. Control report generation with task-based or on-demand workflows, available from directly inside your application. For more information, see [*In-application reporting with Qlik Cloud Analytics*](../InAppGeneral/cloud-in-app-reports-intro.htm).
- Reporting with Qlik Automate. Create dynamic reports using the no-code automation building blocks. For more information, see [*Reporting from Qlik Cloud Analytics with Qlik Automate*](../Automations/Reports-with-application-automations.htm).
- Direct use of the Qlik Reporting Service API. For more information, see the [Developer Portal documentation](https://qlik.dev/apis/rest/reports).

## Prerequisites

Subscriptions have the following prerequisites:

- Subscriptions must be turned on by a Qlik Cloud admin. For more information, see [*Enabling and disabling reporting, subscriptions, and sharing features*](../../Admin/mc-enable-reporting-features.htm).
- You need a valid email address configured in Qlik Cloud.
- You need to have view permissions for the application in which you are creating subscriptions.

Information note Portrait layout is not supported for sheets that will be outputted to subscriptions or automations in PowerPoint format. Sheets set to portrait layout will be converted to landscape. However, you can use portrait layout if you are using the Qlik Reporting Service API. For more information about using the API to create reports, see the [Developer Portal documentation](https://qlik.dev/apis/rest/reports).

Information note If the application is deleted, any subscriptions related to it will still exist. However, they will fail to generate.

## Application settings saved in subscriptions

When you create a subscription, the following settings are saved:

- Selections
- Visualization properties: layout, colors, legend, labels, and more. For information on applying these properties, see [*Visual exploration*](../../UserInterface/visual-exploration-menu.htm).
- JavaScript options: languages, themes, [variables](#glossary-5 "Glossary term"), or deviceTypes

  DeviceType might be auto, touch, or desktop. The value depends on the touch screen mode toggle in your Qlik Sense application. If touch screen mode is on, the deviceType will be touch. Otherwise it will be auto or desktop.

### Handling of selections

Selections saved in your subscription are calculated based on their current value at time of report generation. This allows you to apply expression-based selections for subscriptions that dynamically adjust to current data. For example, you can apply a selection using the expression search =Year=year(now()) so that reports always filter data for the current year.

### Handling of other settings

Other saved settings are applied each time the report is generated. For example: you create a subscription in an application that uses Theme1. The application is later changed to Theme2. The subscription report will continue to use Theme1.

## Creating a subscription

You can create a subscription based on a visualization or a sheet. When you create a subscription, you become the owner. If you own a subscription, you can add recipients to it. For more information, see [*Sharing a subscription*](#Sharing). If you create a subscription based on a sheet, you can add up to 10 sheets to the subscription.

Do the following:

1. Open the sheet in analysis mode. Do one of the following:

   - Right-click on a visualization, and select Subscribe.
   - On the top bar, click ![Navigation](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg), and select Subscribe to sheet.
2. Title

   Enter a Title for the subscription. This will be used as the email subject.
3. Description

   This [field](#glossary-6 "Glossary term") is optional. This will appear in the body of the email. This section can be used to differentiate between subscriptions that are similar.

   For example: Weekly sales - East coast and Weekly Sales - West coast.
4. Format

   Choose between PDF or Microsoft PowerPoint. If your reports are distributed as PowerPoint files, they can be edited by your recipients.
5. Data

   Configure the data used by the subscription. [Variables](#glossary-7 "Glossary term") in the subscription are handled with bookmark capabilities. Control variable data with the Use variable state setting, which is equivalent to the  Save all variable states setting in [bookmarks](#glossary-8 "Glossary term").

   Variable states may still be included if the application creator set Include in bookmarks on any variables in their application. For more information, see [*Including variable states in bookmarks and reports*](../../Variables/using-variables-with-bookmarks.htm) and [*Creating bookmarks*](../../Bookmarks/create-bookmark.htm).

   By turning the Use variable state setting on, variable values will be included in the bookmark that will be applied when generating reports.
6. Sheets

   If you based the subscription on a sheet, you can add more sheets to the subscription. The maximum number of sheets is 10.

   You can sort the sheets to change the order they are displayed in the email.
7. Send email

   Choose how often the subscription will generate a report. The time you set is when report generation will start, not when the report will be received:

   - Daily: choose what time the report will be generated each day.
   - Weekly: choose which days of the week the report will be sent. You can select as many days as you want.
   - Monthly: choose which days of the month the report will be sent. You can select as many days as you want.
8. Time

   Choose the time of day the subscription will send a report.

   This is the time the report will be added to the queue for generation. It is not the time you will receive the report. To learn about report generation times, see [*Report emails not arriving when scheduled*](#Report).
9. Turn on Add users to subscription to add recipients to the subscription.
10. Click Preview to download a copy of the report as a preview. Your current selections in the application are applied in the preview.
11. Click Subscribe.

Warning noteA user may have access to visibility of all other users within the same tenant - such visibility may include (but may not be limited to): user names, email addresses and the user’s subject, which is a unique string used to identify the user that is provided to Qlik Cloud by the configured Identity Provider.

## Sharing a subscription

You can add recipients to a subscription if:

- You own the subscription.
- The sheets are public.
- The recipient has access to the application. If they do not have access, they will be added to the subscription, but they will not receive reports. Once they get permission to access the application, you can edit the subscription and add them.

Recipients do not receive a notification when they are added or removed from a subscription.

## Managing your subscriptions

Click Subscriptions in the Analytics [activity center](#glossary-9 "Glossary term") to see a list of subscriptions owned by you, as well as subscriptions to which you have been added as a recipient.
You can also access Subscriptions from the user profile menu in the upper right-hand corner of the application.

You can filter and sort the subscriptions on the Subscriptions page. You can refine your list by owner (anyone, you, or others), or search for subscriptions owned by a specific user. The subscriptions in the list can be sorted by time last sent, time they are next scheduled to be sent, or alphabetically by name.

Click a subscription to see more details. The ![action](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) menu to the right of each subscription has several actions.

If you receive a subscription, but do not own it, you will have the following options:

- Details: View subscription details such as last sent, scheduled, and created. You can also view a list of all sheets that are included in the subscription and open them in the application.
- View in app: Open the sheet or chart in the application. If the subscription includes more than one sheet, the first sheet in the list is opened.
- Unsubscribe: Remove yourself from a subscription.

If you are the subscription owner, you will have the following options:

- Details: View subscription details such as last sent, scheduled, and created. Owners can also use this section to edit, send, enable/disable, or delete the subscription.
- Recipients: View and edit the recipients list.
- Edit: Change subscription details or schedule.
- Send now: Send the report immediately.
- View in app: Open the sheet or chart in the application. If the subscription includes more than one sheet, the first sheet in the list is opened.
- Enable/Disable: Turn scheduled emails on and off. You can still send a report using Send now.
- Delete: Delete the subscription. This cannot be undone.

### How timezones are displayed for alerts and subscriptions with recurring schedules

In Qlik Cloud activity centers, the time or timezone displayed will usually match the timezone you have set in your personal settings.
One exception is the recurring interval schedule for alerts and subscriptions.

If you look at the Details page for an alert or subscription, you can see the next scheduled run-time under Scheduled. The time under Scheduled will reflect your timezone. If you hover over the ![Info](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_info_outline.svg), a tooltip will appear showing how often the subscription or alert is sent.

This image shows what it looks like when the creator and recipient live in the same timezone:

- The next scheduled run-time is: April 3, 2023 at 2:15 PM.
- The dark grey tooltip shows how often the subscription is sent: Every week, Monday and Wednesday, at 2:15 PM.

A subscription details page, as seen by a recipient who is in the same timezone as the creator.

![A subscription details page, showing a tooltip with the subscription schedule.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_subscription_details_timezone_same.png "Click to view full size")

However, the tooltip will show a ![Warning](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_warning_triangle_2.svg) if the alert or subscription was created in a different timezone than the recipient. In this case, the schedule will be shown in the timezone the alert or subscription was created.

For example, a user in Toronto, Canada (GMT-4) creates a subscription. They add a recipient who lives in Stockholm, Sweden (GMT+2). There is a 6-hour time difference between them. The Swedish recipient checks the details page to find out how often they will receive this subscription. Under Scheduled, the time displayed is in the correct timezone: Stockholm, Sweden. However, if the recipient hovers over the ![Info](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_info_outline.svg), the tooltip shows the entire subscription schedule in the Canadian timezone:

- The next scheduled run-time is March 13, 2023, 3:30 PM.
- The dark grey tooltip shows the subscription schedule, but in the Canadian timezone: ![Warning](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_warning_triangle_2.svg) Created in (GMT -4:00) America/Toronto: Every week, Monday, Wednesday, Friday 9:30 AM.

The schedule of a subscription created in Canada, as seen by a recipient in Sweden.

![The difference between the scheduled timezone and the time the user will receive a subscription email.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_subscription_details_timezone_difference.png "Click to view full size")

## Limitations

- You can create up to 100 subscriptions.
- You can include up to 10 sheets.
- A subscription can have up to 100 recipients.
- If a subscription fails to generate three times, it will be turned off.
- If export fails for one or more sheets in the subscription, the report will not be generated. Possible causes:

  - The recipient does not have access to all sheets in the subscription.
  - A sheet has been deleted.
- You cannot subscribe to:

  - [*Filter pane*](../../Visualizations/FilterPane/filter-pane.htm) objects
  - [*Tab container*](../../Visualizations/Container/container-object.htm) objects. You can subscribe to objects inside a tab container.
  - [*Navigation menu*](../../Visualizations/Navigation-menu/navigation-menu.htm) objects
  - [*Animator*](../../Visualizations/DashboardBundle/animator.htm) objects
  - [*Date range picker*](../../Visualizations/DashboardBundle/date-range-picker.htm)  objects
  - [*Variable input control*](../../Visualizations/DashboardBundle/variable-input.htm) objects
  - [*Video player*](../../Visualizations/DashboardBundle/video-player.htm) objects
  - Existing instances of the legacy [*Container*](../../Visualizations/DashboardBundle/dashboard-bundle.htm#Containe) object. Existing subscriptions to objects inside these containers are still supported.
  - [*Trellis container*](../../Visualizations/VisualizationBundle/trellis-container.htm) objects
  - [*Dynamic charts*](../../DynamicViews/dynamic-views.htm#Dynamic2)
  - Third-party extensions and action buttons
- When using a custom font in your application, it is assumed you have the required license to use that font in output from Qlik Sense. To ensure your fonts are licensed, make use of the multiple open-source fonts available in Qlik Sense for styling application content.

  If you have the required licenses for a font that is not available in the default Qlik Sense themes, see [Create themes with custom fonts](https://qlik.dev/extend/create-custom-themes/custom-themes-fontfamily-examples) to learn about adding the font to a custom theme.
- When characters that are unsupported in the selected font are used in application content, these characters will be rendered in output with a font in which they are supported. Different behavior might be noticed if a custom font is used.
- If you use a custom theme in your application to define font use (for example, adding a font file directly to the theme), fonts rendered in various outputs might not be the same fonts you have used in your application.
- Shadows applied to chart objects in the application are not shown in the generated subscription report.
- The maximum execution time for a subscription is two hours.

Consider the following limitations that apply to subscribing to application content. These limits are checked when you click Subscribe. If these limits are exceeded, you will see an error message. If this issue occurs, contact a user with Can edit permission in the application.

The specific limitations are listed below:

- Maximum number of sheets in the subscription: 10
- Maximum image size: 4,000 x 4,000 pixels
- Minimum image size: 5 x 5 pixels for charts and 20 x 20 pixels for sheets

## Troubleshooting

### Report emails not arriving when scheduled

A report subscription is set to start at a specific time, but does not arrive in your email inbox until hours later.

Possible cause

The time set in the subscription is the time report generation starts, not the time it arrives in your inbox. The time it takes for a report to generate depends on several factors. Most notably:

- Number of active Qlik Cloud users
- Number of active or queued processes: alerts, data reloads, subscriptions

Proposed action

Set your subscription to run at a non-peak time. If you and your recipients start work at 9 AM, set your subscriptions to run at 6 AM.

Related learning:

- [How do I subscribe to an email report in Qlik Cloud?](/lnk/How_subscribe_email_report_qlikcloud)
