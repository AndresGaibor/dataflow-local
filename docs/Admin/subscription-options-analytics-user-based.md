---
title: "Qlik Cloud user-based subscriptions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/subscription-options-analytics-user-based.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Planning your Qlik Cloud deployment"]
---

# Qlik Cloud user-based subscriptions

Qlik Sense Enterprise SaaS and Qlik Sense Business are user-based analytics subscription, with pricing based on the number of users.

## Subscription details

For details on subscription specifications and license metrics, see [Qlik Product Terms](https://www.qlik.com/us/legal/product-terms) (Qlik Cloud® Subscriptions).

To check system requirements, see [*System requirements and supported browsers*](../Introduction/qcs-supported-browsers.htm).

If you are transitioning from a user-based subscription to the capacity-based subscription model, see [*Differences between the Qlik Cloud Analytics subscription models*](comparing-subscriptions.htm) for key differences.

## Monitoring resource usage

Administrators can view license information and track resource consumption in the Administration activity center.

For more information, see:

- [*Monitoring resource consumption*](mc-monitor-consumption.htm)
- [*Managing your Qlik Cloud subscription*](../Introduction/my-qlik.htm)

## Platform guardrails

To maintain performance and stability, Qlik Cloud enforces guardrails—fixed limits that help prevent resource overuse. These guardrails apply to all tenants.

Qlik Cloud Analytics platform guardrails

| Limit | Value |
| --- | --- |
| Data file size: upload to spaces (manual, Qlik DataTransfer, API) | 100 GB |
| Variables in exported application content (see [*Working with sheets*](../Sheets/working-with-sheets.htm)) | 1,100 |
| File size: export to Microsoft Excel (see [*Downloading application content*](../Download/downloading-visualization.htm)) | 100 MB |
| Tasks for scheduled data refreshes per application, script, data flow, or table recipe | 10 |
| Reload runtime limit (see [*Reloading application data*](../Apps/reloading-apps-cloud-hub.htm)) | 3 hours |
| Rows in data alerts (see [*Troubleshooting alerts*](../Alerting/troubleshooting-alerts.htm)) | 100,000 |
| Rows in email notifications (see [*Troubleshooting alerts*](../Alerting/troubleshooting-alerts.htm)) | 10 |
| Data alerts per user (see [*Troubleshooting alerts*](../Alerting/troubleshooting-alerts.htm)) | 50 |
| Webhooks per user | 150 |
| Subscriptions per user (see [*Scheduling reports with subscriptions*](../Reporting/Subscriptions/Subscription-reports.htm)) | 100 |
| Recipients per subscriptions (see [*Scheduling reports with subscriptions*](../Reporting/Subscriptions/Subscription-reports.htm)) | 100 |
| Users per tenant | 100,000 |
| IdP groups per tenant | 10,000 |
| Custom groups per tenant | 20,000 |
| Group membership per user | 1,000 |
| Combined users and groups per space | 50,000 |
| Group name length (max characters) | 256 |
| Session inactivity timeout | See [*Configuring session timeouts*](configure-session-timeout.htm) for defaults and ranges |
| Maximum session duration | See [*Configuring session timeouts*](configure-session-timeout.htm) for defaults and ranges |
| Application timeout (starts after session timeout + 120 seconds) | 60 seconds |

## Subscription-based limits

Some limits and features depend on your subscription and may change when you upgrade. For details, see [Qlik Product Terms](https://www.qlik.com/us/legal/product-terms) (Qlik Cloud® Subscriptions).

The following subscription-based limits are not listed in the Qlik Product Terms.

Additional subscription-based limits

| Limit | Value |
| --- | --- |
| Reloads per month | 1,000,000 |
| Concurrent application evaluations | 2 |

These values apply to Qlik Sense Enterprise SaaS and Qlik Sense Business. Other subscriptions may have different limits.

## Limits with large application support

Large application support increases some limits. The table below compares limits with and without large application support.

Large application support availability depends on your subscription and is not available with Qlik Sense Business. For details, see [Qlik Product Terms](https://www.qlik.com/us/legal/product-terms) (Qlik Cloud® Subscriptions). For more information, see [*Large application support*](large-app-support.htm).

Information note

The Application file size limit below is an approximate guideline, not a strict upload limit. Whether an upload succeeds depends on the application's loaded (in-memory) size, not the file size on disk. Compressed files, embedded images, or content-library media can result in a file exceeding the stated size while still loading within the in-memory limit.

Limits with large application support

| Limit | With large application support | Without large application support |
| --- | --- | --- |
| Application size: in-memory | Up to 50 GB | 1.25–5 GB[1 The limit is 1.25 GB for Qlik Sense Business and 5 GB for Qlik Sense Enterprise SaaS.](javascript:void(0)) |
| Application file size: upload from other Qlik Sense versions via activity center | 10 GB | 250 MB–1 GB[2 The limit is 250 MB for Qlik Sense Business and 1GB for Qlik Sense Enterprise SaaS.](javascript:void(0)) |
| Reload size limit[3 Without large application support, the largest reload engine is 40 GB (up to 34 GB usable capacity, the remainder reserved for system tasks). Plan data reloads accordingly.](javascript:void(0)) | 3x purchased capacity (max 240 GB) | Up to 34 GB[4 10 GB for button object reloads.](javascript:void(0)) |
| Engine hypercube memory limit | Approx. 3x application size (max 200 GB)[5 Based on application size.](javascript:void(0)) | 10 GB |

## Additional capabilities

The following capabilities vary in availability and capacity depending on the subscription tier.

For details on pricing and upgrade options, see [Qlik Product Terms](https://www.qlik.com/us/legal/product-terms) (Qlik Cloud® Subscriptions).

### Qlik Automate

The basic tier of Qlik Automate is included with Qlik Sense Enterprise SaaS.

For more information on limits, see [*Qlik Automate limitations*](../../Sense_QlikAutomation/introduction/platform-limitations.htm).

### Qlik Predict

The basic tier of Qlik Predict is included with Qlik Sense Enterprise SaaS.

For more information on limits, see [*Introducing automated machine learning*](../AutoML/introduction.htm#AutoML).

### Reporting Service

The included tier of Qlik Reporting Service comes with Qlik Sense Enterprise SaaS.

For more information on limits, see [*Qlik Reporting Service specifications and limitations*](../Reporting/Reporting-service-specifications-limitations.htm).
