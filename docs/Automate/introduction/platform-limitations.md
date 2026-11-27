---
title: "Qlik Automate limitations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/introduction/platform-limitations.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate"]
---

# Qlik Automate limitations

This page describes platform limitations for Qlik Automate.

## General limitations

The following limitations apply to all automations.

### Notifications

A failed automation run will only generate a notification once every hour.

### Screen width

The recommended minimum width for working with Qlik Automate is 640px.

### Tenant limit

There is a limit of 10,000 automations per tenant

### User limits

Platform limitations for user limits

| Metric | Limitation | Notes |
| --- | --- | --- |
| Maximum number of owned automations per user | 500 | Each user can own up to 500 automations. Once 500 automations are reached, to create a new automation, the user will first need to delete an existing automation. |
| Maximum number of automation connections per user | The lesser of 250, or the value specified in your subscription. | Each user can maintain up to 250 connections, across all connectors, unless a lower value is specified for your contract. For detailed information about the maximum number of connections permitted by subscription type, see the [Qlik Cloud® Subscriptions](https://www.qlik.com/us/legal/product-terms) product description. |

### Special characters

The formula parser cannot process curly brackets { } within a string. If your data contains this type of bracket, use the [Custom code block](../advanced/custom-code.htm) to remove them.

### Automation executions (runs)

Platform limitations for automation executions

| Metric | Limitation | Notes |
| --- | --- | --- |
| Maximum runs per month | Determined by Qlik license | For detailed information about your license metrics, see the [Qlik Cloud® Subscriptions](https://www.qlik.com/us/legal/product-terms) product description. Administrators can view license information and monitor the number of automation runs in Administration. For more information, see [*Monitoring resource consumption*](../../Sense_Hub/Admin/mc-monitor-consumption.htm). |
| Maximum runs for automations with third-party blocks | Determined by Qlik license | For detailed information about your license metrics, see the [Qlik Cloud® Subscriptions](https://www.qlik.com/us/legal/product-terms) product description. Administrators can view license information and monitor the number of automation runs in Administration. For more information, see [*Monitoring resource consumption*](../../Sense_Hub/Admin/mc-monitor-consumption.htm). |
| Maximum number of concurrent runs | Determined by Qlik license.  A tenant admin, analytics admin, or a user with Tenant Admin Automations permissions can set a limit that is lower to the maximum number allowed by the license. | When concurrent limits are reached, new runs are queued. After 14 days, automations that are still in the queue are marked as failed.   Information noteThe total maximum concurrency per license is capped at 110 runs for all automations and tenants for that license.  Information noteWhen multiple runs are queued, the order in which they are executed may not always be guaranteed. |
| Maximum run duration | Determined by block limitations | - |
| Maximum memory consumption during run | 256 MB | Memory limitation mostly affected only when processing very large data sets. |
| API call timeout | 5 minutes | API pagination is used to reduce API query timeout. |
| Call URL timeout | Configured by the user | Configured on the block with the Max automation execution time setting. |
| Custom code block maximum execution time | 3,600 seconds | Because the custom code block is optimized for security, it cannot access the internet, leverage third-party modules and packages, or make direct external calls. Since version upgrades may occasionally break customer code we recommend using native blocks and functions where possible. |
| Maximum API calls | Rate limit of 300 calls per minute | API calls include triggered automations. |

### Automation execution time

Platform limitations for automation execution time

| Automation run type | Default maximum execution time | Configurable values |
| --- | --- | --- |
| Manual (including test runs) | 4 hours | 10 seconds - 4 hours |
| Scheduled | 4 hours | 10 seconds - 4 hours |
| Triggered (async = false) | 55 seconds | 10 seconds - 5 minutes |
| Triggered (async = true) | 4 hours | 10 seconds - 4 hours |
| Webhooks | 4 hours | 10 seconds - 4 hours |

Information note

For triggered automations, the values `async = false` and `async = true` refer to the Run asynchronously setting in the Start block.

This setting is configured at the automation level and applies to all triggered runs of that automation. It cannot be changed per incoming trigger request.

### Automation history

Platform limitations for automation history

| Metric | Limitation | Notes |
| --- | --- | --- |
| Maximum number of automation logs | 5000 per automation 500 MB per automation | Oldest logs are deleted when limits reached. |
| Automation history retention | 30 days | - |
| Maximum size for each run log | 100 MB | Log is truncated if limit exceeded. |
| Maximum size of state for each run log | 1 MB per block 5 MB per block across all block executions Maximum 200 list items. | State is truncated if limit exceeded. |

### Automation blocks

Platform limitations for specific automation blocks

| Metric | Limitation | Notes |
| --- | --- | --- |
| Custom code block | Python, JavaScript, and PHP supported | The custom code block does not support including libraries. See [Custom code block](../advanced/custom-code.htm) for more information. |
| Variable block | Variables stored in memory | To persist data or process large datasets, use a database or cloud storage. |
| List blocks | Full list loaded in memory | Use loops to process large lists. Use iterators to avoid loading everything into memory. |
| Qlik Reporting blocks | Limitations are imposed by the Reporting Service API | [Qlik APIs](https://qlik.dev/apis) |
| Qlik Reporting blocks | Sheet titles are not included in report exports | By design, sheet titles are not exported in XLSX, PPTX, HTML, and PixelPerfect templates. |

### Per-user limitations

Platform limitations per user

| Metric | Limitation |
| --- | --- |
| Maximum number of automations per user | 500 |
| Maximum number of templates per user | 100 |

### AI description generation limitations

- Not available for tenants in the `il-central-1` (Israel) region.
- Not supported for automations with more than 500 blocks.
- Not supported for automations that contain only a START block.
- Rate limit: 20 calls per minute per tenant.

## Additional Limitations

In addition to the limitations listed above, the following limitations apply to specific types of automations.

### Scheduled automations

Platform limitations for scheduled automations

| Metric | Limitation |
| --- | --- |
| Minimum schedule interval | 1 minute |
| Maximum schedule interval | 30 days |

### Triggered automations

Platform limitations for triggered automations

| Metric | Limitation | Notes |
| --- | --- | --- |
| Maximum payload size `POST` to the automation | 1 MB | - |
| Maximum incoming triggers | Maximum rate limit 300 triggers per second Maximum 200 queued triggers | Response code `429` = rate limit exceeded Response code `400` = queue is full |
| Deferred processing during service downtime | Triggered requests can be accepted and queued for later execution | Response code `202` = accepted for later processing, not completed The execution can be delayed until the service is available again |

### Native webhook automations

Platform limitations for native webhook automations

| Metric | Limitation |
| --- | --- |
| Maximum payload size `POST` to the automation | 1 MB |
| Maximum incoming events | Maximum rate limit 20 events per second Maximum 1,000 queued events |
