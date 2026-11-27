---
title: "Enabling and managing data alerts"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-managing-alerts.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Configuring features and integrations"]
---

# Enabling and managing data alerts

Data alerts in Qlik Cloud notify users when specific conditions or thresholds in their data are met, helping them stay informed about critical changes. Administrators can enable and manage alerts in the tenant.

## Enabling alerts

To allow users to create and manage data alerts, alerts must first be enabled in the tenant. Tenant admins can enable alerts.

Do the following:

1. In the Administration activity center, go to the Settings page, then select the Feature control tab.
2. Toggle Data alerts on.

To use email notifications, you must also configure an email server. For more information, see [*Configuring email for reports and notifications*](mc-configure-email-support.htm).

## Managing alerts

Tenant admins or analytics admin can manage all alerts in the tenant from the Alerts page in the Administration activity center. You can:

- Delete alerts.
- Disable alerts (turns off scheduled evaluation).
- Re-enable disabled alerts.
- Change the owner of an alert. The new owner must have access to the application. If the alert has multiple recipients, the new owner must have Professional user entitlement (applies only to user-based subscriptions).

  Information noteIf the application uses [section access](#glossary-1 "Glossary term") and the new owner lacks access to the data, the alert will not be evaluated for them. It will still be evaluated for other owners who have the necessary access.

## Managing your own alerts

You can change settings for alerts that you own or subscribe to from the Analytics [activity center](#glossary-2 "Glossary term"). For more information, see [*Managing your alerts*](../Alerting/managing-your-alerts.htm).
