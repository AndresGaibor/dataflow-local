---
title: "Working with webhooks"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/working-with-automations/working-with-webhooks.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Working with automations"]
---

# Working with webhooks

An automation can be triggered by using the webhook URL of the automation or by native webhooks. To trigger an automation using its webhook URL, set the start block run mode to Triggered. To trigger an automation using a webhook connector, set the start block run mode to Webhook.

- [Triggered webhooks](#triggered-webhooks)
- [Native webhooks](#native-webhooks)

## Required webhooks permissions

When creating or managing webhooks, you must be a tenant admin or request either of the permissions below:

- Use webhooks: Required to create, view, update, and delete webhooks owned by the user. Available via [*Managing users - Capacity-based subscriptions*](../../Sense_Hub/Admin/SaaS-user-management-capacity-model.htm) and [*Creating and managing OAuth clients*](../../Sense_Hub/Admin/mc-create-oauth-client.htm)[*Creating and managing OAuth clients*](../../Sense_Hub/Admin/mc-create-oauth-client.htm)
- Manage Webhooks: Required to manage all webhooks in the tenant, including those created by other users. This is only available via [*Creating and managing OAuth clients*](../../Sense_Hub/Admin/mc-create-oauth-client.htm).

## Triggered webhooks

Triggered webhooks make API calls to the Qlik Cloud service from another platform through its webhook URL.

Information note

For triggered automations, the Run asynchronously setting in the Start block determines the maximum execution time for all triggered runs.

When this setting is cleared (`async = false`), the maximum execution time is configurable from 10 seconds up to 5 minutes (default: 55 seconds). When selected (`async = true`), the maximum execution time is 4 hours. The setting is configured per automation and is not selected per trigger request.

Information note

If the service is temporarily unavailable during an outage, migration, or upgrade, a triggered webhook request can be accepted for later processing instead of being run immediately.

Warning note

A `202` response means the request was accepted for later processing. It does not confirm that the automation has completed or that the target data is up to date.

When using the execution token, the run mode in the Start block must be set to Triggered. Any other run mode will cause the execution to fail and generate the following error message:

"The requested automation has an invalid run mode. Please check your automation run mode to be set as triggered."

Information note

Refer to [platform limitations](../introduction/platform-limitations.htm) to see API call and execution time limits.

For a visual demo about how to set up triggered webhooks, see:

[Triggered Webhooks](https://share.vidyard.com/watch/L7rmNJUjRcz39tHZ8Vthfg)

### Getting the automation URL

Automations are exposed through a REST API endpoint, which means they can be called with a webhook URL to trigger the automation. To get the webhook URL, set the start block run mode to Triggered. The block configuration pane displays a `GET` and `POST` curl command with the webhook URL.

Warning note

The automation webhook URL contains a token that should be kept secret. Do not share it publicly and do not store it on public version control repositories.

Warning note

Renewing the execution token will immediately break any reference to the automation via API or button object. Token renewal cannot be undone.

Triggered start block inputs

![webhook url from a start block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/webhook-url.png)

### Viewing the webhook payload

When you call the automation with a webhook URL, the start block receives input from the webhook. To view the payload, use an output block and set the start block as the input.

Mapping start block to output block

![start block as the input for an output block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/start-output.png)

Information note

You can change the input field to retrieve a specific part of the JSON payload, for example `{$.Start.name}`. Alternatively, you can use input blocks to specify part of the JSON payload.

### Defining input parameters

You can add an input block below the start block to receive the payload from the webhook URL. Below the input block, you can add other blocks that retrieves part of the data.

For example, you could use the input block to receive the full payload, which is a JSON array, and select only the required field from the input block output.

Input parameters

![Automation showing input from payload and posting a message to Slack](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/webhook-slack.png)

## Native webhooks

Native webhooks use an API call to create an event in the platform you select under Connector. Native webhooks include preconfigured connectors, like the Qlik Cloud connector.

For a visual demo about how to set up native webhooks, see:

[Working with native webhooks](https://share.vidyard.com/watch/6EoibjSsKdTvoWZBWzCtj1)

Set the start block run mode to Webhook to use native webhooks.

Webhook run mode

![Webhook start block option](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/start-block-webhook.png)

You must authenticate the data connector of the selected webhook. Once it is authenticated, select which event triggers the automation. In the image below, the automation runs whenever a Qlik Cloud app is created.

Information note

Tenant admins have access to all events, while other security roles only have access to a subset of the events.

[Native Webhooks](https://share.vidyard.com/watch/6EoibjSsKdTvoWZBWzCtj1)

Start block as a webhook

![Webhook start block with event app created](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/webhook-app-createdNew.png)

### Filtering

By using filters, you can limit the webhook to trigger only on specific apps or apps in specific spaces. The filter can include multiple apps and spaces. Use the do lookup function to easily add the ID of an app or a space.

The events App Created and App Published can only be filtered by space ID because the app ID is not known before these events have occurred.

Webhook for the App Reload Finished event filtered by space ID

![Webhook with a filter specifying a space ID](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/webhook-filter.png)

### Modifying the test payload

You can modify the test payload to include objects that you want to retrieve during a test run. The actual payload can be different from the test payload.

For example, here is a simple automation that outputs the name of the app when that app is reloaded. The start block is set to Webhook and the event that triggers the automation is an app reload.

App reload automation with webhook start block

![A simple automation with two blocks showing the start block configured as a webhook](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/webhook-modify-payload-new.png)

The test payload field is edited to only include the `data` object.

```
{
  "data": {
    "id": "94a789ad-d967-4049-8aaf-9abac267c222",
    "name": "MyApp"
   }
}
```

When you run this automation and look at the start block output, it shows only the test payload. When the automation is triggered through the Qlik Cloud webhook, the start block output shows the actual payload.

```
{
  ...
  },
  "data": {
    "duration": 1345,
    "endTime": "2021-09-14T18:30:06.288Z",
    "errors": [],
    "id": "ff241d45-6605-432d-9ec5-8cf4e9a64807",
    "name": "JIRA app",
    "peakMemoryBytes": 4985984,
    "reloadId": "6140ea2554b901cc5a122461",
    "size": {
      "memory": 16845
    },
    "status": "ok",
    "warnings": []
  }
}
```

### Managing webhooks as an administrator

Automations with a webhook in the start block are listed under Webhooks in the Administration activity center. Only tenant administrators can access this section.

Webhooks table in the Administration activity center.

![The management console webhooks table showing a webhook and the expanded view](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/mc-webhook.png)

To learn how to manage webhooks from the Administration activity center, see [Webhooks](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-webhooks.htm).
