---
title: "Troubleshooting alerts"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Alerting/troubleshooting-alerts.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Using analytics to explore data", "Monitoring data with alerts"]
---

# Troubleshooting alerts

This section describes problems that can occur when using alerts.

## The preview could not be generated

You get a message The preview could not be generated when creating the alert.

Possible cause

You have access to the application as a [tenant](#glossary-1 "Glossary term") or analytics admin but you do not have access as a user.

Proposed action

You need to get at least viewing [permissions](#glossary-2 "Glossary term") to the application to be able to create alerts. Request viewing permissions from the application owner.

## No access to application

The message No access to app is displayed under Application in the alerts overview.

Possible cause 1

You do not have permission to view the application.

Proposed action

Contact the tenant or analytics admin to get at least view permission to the application.

Possible cause 2

The application has been deleted.

## This alert would not trigger with the current data

In Preview, you get the message This alert would not trigger with the current data when creating an alert.

Possible cause 1

The conditions are not met by the current data. This is expected behavior, not an error.

Proposed action

Check the conditions you defined and compare them with the values in Preview data. Adjust the conditions if the alert should trigger. For more information, see [*Setting conditions for alerts*](setting-conditions-for-alerts.htm).

Possible cause 2

The label of a measure is a text expression that contains two quoted segments, for example ='Total' & Chr(10) & 'Sales'.

Proposed action

Change the label expression so that it uses a single set of quotes, or simplify the label.

Possible cause 3

The community has published a workaround for chart labels that contain an equals sign (=): [Alerts in Qlik Cloud are not working as expected: this alert would not trigger with the current data](https://community.qlik.com/t5/Official-Support-Articles/Alerts-in-Qlik-Cloud-are-not-working-as-expected-this-alert/ta-p/2525739).

## Alert email notifications are not received

An alert is triggered, but you or the recipients do not receive the email notification.

Possible cause 1

The alert is disabled, or notifications for the alert are snoozed.

Proposed action

In the Alerts page, enable the alert if it is disabled, and check whether Snooze notifications is on. For more information about enabling and disabling alerts, see [*Managing your alerts*](managing-your-alerts.htm).

Possible cause 2

Email is not selected as a notification method for the alert or in your global notification settings. You might have selected Daily email digest instead.

Proposed action

Check the notification settings. For more information, see [*Customizing alert notifications*](monitoring-changes-with-alerts.htm#Receivin).

Possible cause 3

The alert evaluation fails if a recipient does not have view permission for the application. If the application uses [section access](#glossary-4 "Glossary term"), evaluation also fails if a recipient cannot access the data used in the alert [selections](#glossary-5 "Glossary term"). The [sheet](#glossary-6 "Glossary term") must be public for recipients to open it from the notification.

Proposed action

Give each recipient view permission for the application. If the application uses section access, make sure each recipient can access the data used in the alert selections. Make the sheet public if recipients need to open it from the notification. For more information, see [*Monitoring data with alerts*](monitoring-changes-with-alerts.htm).

Possible cause 4

Email support is not configured for the tenant, or data alerts are not enabled.

Proposed action

Ask a tenant admin to enable data alerts and configure an email server. For more information, see [*Enabling and managing data alerts*](../Admin/mc-managing-alerts.htm) and [*Configuring email for reports and notifications*](../Admin/mc-configure-email-support.htm).

## Limitations

### Data is limited to 100,000 rows

When the alert is evaluated the data set is limited to the first 100,000 rows of the returned hypercube. This means that it will not evaluate on the full data set or provide a complete result.

If you have a large data set, the workaround is to create multiple alerts with a filter to reduce the number of rows in the data set to evaluate.

### Email notifications are limited to 10 rows of data

If the result of the alert evaluation contains more than 10 rows of data, the email notification only shows the first 10 rows.

There is also a CSV file with all rows of data attached to the email. Do not open the CSV file directly in Excel. As the fields are delimited with Tab characters and Excel expect commas, it will not be correctly formatted. To open the CSV file:

1. Download the CSV file to your computer.
2. Open Excel with a blank workbook.
3. Import the CSV file using Tab as delimiter.

### You can have up to 50 alerts

The number of alerts that you own or subscribe to, is limited to 50. Disabled alerts also count towards the limit. If you have reached the limit you can reduce the number of alerts.

- Delete alerts that you own.
- Unsubscribe from alerts that have been shared with you.

### Sharing alerts based on applications with section access

If the alert is based on an application that uses [section access](#glossary-7 "Glossary term") to manage user access, you can share the alert with up to 100 recipients.
