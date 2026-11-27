---
title: "Analyzer capacity license"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/analyzer-capacity-consumption.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Managing users - User-based subscriptions", "Managing user entitlements"]
---

# Analyzer capacity license

The Analyzer capacity license provides access to applications and data with usage measured in six-minute increments during active sessions.

## Overview of Analyzer capacity licensing

Analyzer capacity is a consumption-based license type that gives users access to the same features as the Analyzer entitlement. Users with this license can access applications created by others in their activity centers. They can also create personal sheets, stories, bookmarks, and snapshots based on their assigned space roles. However, they cannot create or edit applications in shared spaces.

With an Analyzer capacity license, you subscribe to a defined amount of analyzer time, measured in minutes per calendar month. These minutes are shared across users and can be consumed by anyone in the user group, including anonymous users.

Consumption is measured in six-minute units, with each new six-minute period consuming one unit.

## Analyzer capacity consumption

Analyzer capacity consumption begins when there is active engagement between the user and the Qlik Sense application. Idle time—when an application is visible but not used—does not consume any additional minutes.

### Examples of active engagement

- Opening an application.
- Making selections in the application. For example, using Insight Advisor Chat or data profiling in the Data Catalog.
- Navigating to a new sheet.
- Reloading the application or during scheduled reloads.

### How units are consumed

- One unit of consumption is six minutes.
- If there is user activity within the first six minutes, another unit is consumed.
- If the user remains idle for six minutes, no additional units are consumed.
- Units continue to be added based on user activity. For example, if you are active for 26 minutes, five units (30 minutes) are consumed.

### Background services

Analyzer capacity can also be consumed during background services. If a scheduled reload occurs in an application to which a user is connected, an additional unit will be consumed unless there is already an ongoing unit consumption.

### Consumption calculation

The following diagrams show how consumption of Analyzer capacity is measured and when units are consumed.

Diagram of capacity consumption using one unit.

![Diagram that shows how capacity consumption is measured in six minute blocks. Diagram has four examples of when one unit of capacity is consumed and how activity is registered. ](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/dr_UnderstandingMinuteUsage1.png "Click to view full size")

Diagram of capacity consumption using multiple units.

![Diagram that shows how capacity consumption is measured in six minute blocks and how activity is registered over multiple units of consumption. Diagram has four examples of when multiple units of capacity are consumed with activity registered at different times. ](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/dr_UnderstandingMinuteUsage2.png "Click to view full size")

There is a key difference in how Qlik Sense Enterprise on Windows and Qlik Cloud calculate Analyzer capacity usage:

- Qlik Sense Enterprise on Windows uses the number of devices as part of the calculation.
- Qlik Cloud uses the number of open applications as part of the calculation.

The following tables illustrate how these calculations are made:

Units consumed by device

| Examples - applications and devices | Qlik Cloud |
| --- | --- |
| 1 Qlik Sense application - 1 device | 1 unit |
| 2 Qlik Sense applications - 1 device | 2 units |
| 3 Qlik Sense applications - 2 devices | 3 units |
| 5 Qlik Sense applications - 2 devices | 5 units |

Information noteA device is defined as a separate device such as a laptop or mobile device. This could also include a second browser.

Units consumed by time

| Example - applications and time | Qlik Cloud |
| --- | --- |
| 1 Qlik Sense application - 6 minutes of activity | 1 unit |
| 1 Qlik Sense applications - 14 minutes of activity | 3 units |
| 2 Qlik Sense applications - 6 minutes of activity | 2 units |
| 2 Qlik Sense applications - 14 minutes of activity | 6 units |

### Analyzer capacity overage

When all of your Analyzer capacity for the month has been consumed, users will be denied access to Qlik Sense. The consumption resets at the beginning of each month.

To avoid disruption due to unexpectedly high usage, you can enable Analyzer capacity overage by adding it to your subscription. Overage packs can be adjusted to match the number of Analyzer capacity packs as needed.

## Monitoring Analyzer capacity consumption

Monitoring Analyzer capacity consumption is essential for managing resource usage in Qlik Cloud. You can track your capacity consumption through two primary tools: the Administration activity center and the Entitlement Analyzer monitoring application.

### Administration activity center

The Administration Home provides a summary of the Analyzer capacity consumption, detailing the total minutes available per month and the consumed minutes.

For more information, see [*Monitoring resource consumption*](../Admin/mc-monitor-consumption.htm).

### Entitlement Analyzer monitoring application

The Entitlement Analyzer provides detailed insights into Analyzer capacity usage in your tenant.

This application is part of the Qlik Cloud Monitoring Apps, which are community-supported. As such, they are not officially supported by Qlik. To quickly install and update these applications, use the Qlik Cloud Monitoring Apps Installer with Qlik Automate. For details on installation and support, see [*App Installers*](../../Sense_QlikAutomation/introduction/template-list.htm#App).

For more information about the Entitlement Analyzer application, see:

- [Qlik Community: Entitlement Analyzer for Qlik Sense Enterprise SaaS (Cloud only)](https://community.qlik.com/t5/Support-Updates/Entitlement-Analyzer-for-Qlik-Sense-Enterprise-SaaS-Cloud-only/ba-p/1817404)
- [GitHub: Qlik Cloud Entitlement Analyzer](https://github.com/qlik-oss/qlik-cloud-entitlement-analyzer)
