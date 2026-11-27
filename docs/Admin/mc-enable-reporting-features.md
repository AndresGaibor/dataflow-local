---
title: "Enabling and disabling reporting, subscriptions, and sharing features"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-enable-reporting-features.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Configuring features and integrations", "Administering reporting and subscriptions"]
---

# Enabling and disabling reporting, subscriptions, and sharing features

[Tenant admins](#glossary-0 "Glossary term") can turn subscriptions and chart sharing on or off in the Administration activity center. Access to in-application reporting can also be controlled by tenant admins by configuring default permissions and custom roles.

## Toggling availability of chart sharing

When the chart sharing feature is turned on in the Administration activity center, users can share a chart by right-clicking it and selecting Share.
When this feature is turned off, the option is not visible to application users.

Do the following:

1. In the Administration activity center, go to the Settings page, then select the Email and reports tab.
2. In the Sharing and reports section, toggle Chart sharing via email on or off.

## Toggling availability of subscriptions

Users can subscribe to a chart or sheet in a Qlik Sense application, and configure the output to be emailed to one or multiple recipients. You can turn this feature off in the Administration activity center.

Do the following:

1. In the Administration activity center, go to the Settings page, then select the Email and reports tab.
2. In the Sharing and reports section, toggle Subscriptions - charts and sheets on or off.

## Setting access to in-application reporting

Tenant administrators can set access to in-application reporting by configuring the Generate all reports permission in the default permissions and custom roles. With these options, you can turn off in-application reporting globally, customize access for specific users as needed, or provide full access to all users. For more information, see [*Setting permissions for metered reporting features*](mc-permissions-reporting.htm).

Information noteThe tenant-level feature control for In-application reporting has been removed. To replace this feature control setting, configure default permissions and custom roles to control access to in-application reporting. For more information, see [*Setting permissions for metered reporting features*](mc-permissions-reporting.htm).

## Learn more

- [*Administering reporting and subscriptions*](mc-administer-subscriptions.htm)
