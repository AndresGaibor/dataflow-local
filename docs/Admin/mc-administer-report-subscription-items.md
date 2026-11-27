---
title: "Administering report tasks and subscriptions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-report-subscription-items.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Configuring features and integrations", "Administering reporting and subscriptions"]
---

# Administering report tasks and subscriptions

Tenant admins and analytics admins can edit user [subscriptions](#glossary-0 "Glossary term") and in-application [report tasks](#glossary-1 "Glossary term") in the Administration activity center.

Do the following:

1. In the Administration activity center, open Subscriptions.
2. In the leftmost column, select one or more report tasks or subscriptions.
3. Use the buttons to delete, disable, or enable the items.

Tip noteTo edit a single report task or subscription, you can use the ![Navigation](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) menu. You can use this menu to change the owner.

## Item status

In the Sent column, the status of the latest delivery is displayed. The following table shows the different statuses.

Latest delivery status

| Status in Sent | Description |
| --- | --- |
| Creating... | When creation is not immediate, a spinner is shown. |
| Sent by email | Date and time refer to when file generation started, not when the email was sent.  Information noteIn addition to scheduling a delivery, users have the option Send now to immediately start file generation and mail delivery, independent of any scheduled delivery. |
| Failed to send | Error message when the application, chart, or sheet is missing. Date and time refer to when file generation started. |
| Deleting... | When deletion is not immediate, a spinner is shown. |
| Never sent | If the applicable reporting feature is turned on, output is sent according to schedule, or when a user uses the Send now option. |

Information noteDate and time in the Scheduled column refer to when file generation starts, not when the email is sent.

## User self-management of subscriptions

Users are not dependent on admins to manage report tasks they can access, or to subscribe to reports about [charts](#glossary-2 "Glossary term") and [sheets](#glossary-3 "Glossary term").

For information about managing report tasks, see [*Working with report tasks*](../Reporting/Generate/cloud-in-app-reports-tasks.htm).

In the profile menu, under Subscriptions, users can see an overview of their subscriptions with different actions available. When a user creates a subscription, they become the owner. A subscription owner can add recipients. For more information about creating and managing subscriptions, see [*Scheduling reports with subscriptions*](../Reporting/Subscriptions/Subscription-reports.htm).

## Learn more

- [*Administering reporting and subscriptions*](mc-administer-subscriptions.htm)
