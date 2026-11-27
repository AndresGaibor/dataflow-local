---
title: "Creating and managing webhooks for workflows"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-webhooks.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Extending Qlik Cloud"]
---

# Creating and managing webhooks for workflows

Webhooks are a simple way to automate communication between applications by sending event data automatically when certain actions occur. In Qlik Cloud, webhooks can trigger actions in other applications without manual intervention, making it easier to integrate Qlik Cloud into your workflows and automate tasks based on system events. Each time a defined event occurs, a JSON request is sent to the specified webhook endpoint, delivering the event data to your chosen application.

## Required webhooks permissions

When creating or managing webhooks using the Qlik Cloud [Webhooks API](https://qlik.dev/apis/rest/webhooks/) and automations UI, you must request one or both of these permissions:

- Use webhooks: Required to create, view, update, and delete webhooks owned by the user.
- Manage Webhooks: Required to manage all webhooks in the tenant, including those created by other users.

## Understanding webhooks

### How webhooks work

When an event happens in Qlik Cloud (for example, a new application is created or a user is deleted), a webhook sends information in JSON format to a specified external application using an HTTP callback. This external application can then use the event data to trigger further actions.

For example:

- Notify your team through Slack when a new application is created.
- Automatically send a welcome email when a new team member is added to a tenant.
- Update a spreadsheet when a user is deleted from the tenant.

### Benefits of using webhooks

Webhooks allow real-time integration with other systems, eliminating the need for constant manual checks or repetitive API requests. By listening for events and sending the relevant data immediately, webhooks reduce unnecessary work and enable smooth automation.

### Popular platforms for webhook integrations

To handle and respond to webhook data, you can build custom services or use third-party platforms like:

- [Qlik Automate](/en-US/cloud-services/Subsystems/ApplicationAutomation/Content/introduction/home-automation.htm)
- [Pipedream](https://pipedream.com/)
- [Zapier](https://zapier.com/)
- [Microsoft Power Automate](https://flow.microsoft.com/en-us/)

### Webhook limits

To maintain system performance and manage resources, the following limits apply:

- Webhook delivery history is retained for 7 days.
- Each user can own up to 150 webhooks.
- Total HTTP header size per webhook is limited to 2048 bytes for encrypted headers and 2048 bytes for non-encrypted headers. For each header type, the limit is the total byte size of all configured header names and values added together. There is no limit on the number of headers.

Information noteFrom November 3, 2025 the legacy event format was replaced with a new Qlik cloud event format. All legacy events use a temporary hybrid event containing both legacy and cloud event payloads. Data integration events are emitted as cloud events and will not need to be migrated in the future. For a complete list of supported events and event types in Qlik Cloud, see [*Supported event types for webhooks*](mc-administer-webhooks-supported-events.htm). For more details on new Qlik cloud events, see [Qlik Community: Migration to new event format](https://community.qlik.com/t5/Official-Support-Articles/Qlik-Cloud-Webhooks-Migration-to-new-event-formats-is-coming/ta-p/2528660) .

### Webhook request structure

When a webhook is triggered by an event, it sends an HTTP JSON request to the specified endpoint during webhooks creation. The structure of this request contains event metadata and payload details such as, the event type, timestamp, and object attributes.

#### Webhook request example: Application deleted event

Here’s an example of the JSON request sent when an application is deleted:

Request URL

```
https://<your-tenantURL>/api/v1/webhooks/{id}
```

Headers

```
{
    "Content-Type": "application/json",
    "X-Execution-Token: <your-execution-token>",
    "Qlik-Signature": "446bd5e3f5b635f491d17557e4bec6ebc61b7bd2bc9cc7b612e4e",
    "User-Agent": "Qlik Webhook"
}
```

Body

```
{
    "cloudEventsVersion": "0.1",
    "source": "com.qlik/engine",
    "contentType": "application/json",
    "eventId": "e65c1481-e8a-4be-a5ca-27dfcde077d7",
    "eventTime": "2021-03-08T14:51:29Z",
    "eventTypeVersion": "1.0.0",
    "eventType": "com.qlik.v1.app.deleted",
    "extensions": {
        "ownerId": "vNRGrDZIypJzauw59BbpvkRhqbmI",
        "tenantId": "oZcMPa_1PwH4FUdrh6839YHHdEJN",
        "userId": "vNRGrDZIypJtcGTzauw59BbpqbmI"
    },
    "data": {
        "attributes": {
            "id": "0984fec4-aa8c-4253-b1d1-4fd4f9c78",
            "name": "New App",
            "createdDate": "2021-03-08T14:51:28.888Z",
            "modifiedDate": "2021-03-08T14:51:29.316Z",
            "owner": "auth0|b62a17c577a4abe6e807b07d18c4d82286352542d633d120100b03fb11",
            "ownerId": "vNRGrDZIypJtcGTzauw59BbpvbmI",
            "published": false,
            "hasSectionAccess": false
        }
    }
}
```

This payload provides detailed information about the deleted application, such as its ID, name, owner, and deletion timestamp, helping the receiving system process the event. For more details on event payloads, see [Qlik Developer Portal: API events](https://qlik.dev/apis/event/).

#### Encrypted Headers

Qlik cloud supports encrypted HTTP headers. Encrypted headers allow you to further protect sensitive metadata. How it works:

- Encrypted Header Values: Header values configured for webhooks can be encrypted when configuring webhooks. This ensures credentials like bearer tokens or API keys are securely stored and handled. Webhook secrets are write-once. Once saved, secrets can not be viewed or retrieved to reduce the risk of accidental exposure.

Information noteHeaders are encrypted in storage, not during transmission.

## Creating webhooks

Webhooks can be created by:

- Tenant admins from the Administration activity center.
- All users from the Qlik Automate interface.

For more information on using webhooks with Qlik Automate, see [Working with webhooks](/en-US/cloud-services/Subsystems/Sense_QlikAutomation/Content/Sense_QlikAutomation/working-with-automations/working-with-webhooks.htm).

Do the following:

1. In the Administration activity center, go to Webhooks.
2. Click Create new.
3. Enter a name for the webhook, and optionally, add a description.
4. For URL (endpoint), enter the fully qualified domain name (FQDN) where the webhook will send JSON data.

   - This URL must use the HTTPS protocol (example: https://domain.com). IP addresses cannot be used as webhook endpoints.
5. Optionally, enter a secret for webhook authentication.

   - The secret must be between 32 and 64 characters.
   - If created, the secret will be included as part of a hash, appended to the HTTP request as a qlik-signature.
6. Cloud event The event payload emitted by Qlik Cloud Webhooks service. Once enabled and saved, the change cannot be undone.
7. Check certificate revocation when enabled verifies that the webhook certificates are valid and not revoked.
8. Optionally, add HTTP headers to append to the request. Select the checkbox to encrypt the header value

   Information noteFor security reasons you cannot edit encrypted headers. To delete the header, click the delete icon. To remove the value, click the remove icon and enter a new one.
9. Under Events, choose the system events that will trigger the webhook. To filter an event, see [*Adding filters to events*](#AddingFilters).

   Available events include:

   - Automation events
   - API events
   - Application events
   - Data-integration events
   - User events
10. Click Create.

Information noteIf you click Cancel while there are unsaved changes, a confirmation dialog appears. Click Discard to close without saving your changes.

### Adding filters to events

You can add a filter when you create or edit a webhook. A filter sends data only when the selected event matches the filter conditions.

A filter icon appears next to an event category when an event in that category has a filter.

Do the following:

1. In the Events section, select an event that supports filtering. The Add filter button appears when you select a supported event.
2. Click Add filter.

   Information noteA webhook with a filter can have only one event selected. Adding a filter disables any other selected events. If you have already selected other events, a confirmation dialog informs you that they will be unchecked.
3. In the filter builder, select a field, operator, and value.

   - Available fields depend on the selected event.
   - The available value control depends on the selected field. You can select a listed value, search for a resource, or enter a value manually.
4. To add a condition to the group, click Add condition. Select and or or to define how the conditions are combined.
5. To add a condition group, click Add group. Select and or or to define how the groups are combined.
6. Review the Filter expression preview.

   Information noteThe filter expression is shown for troubleshooting and validation and is not editable. To change the filter, use the filter builder. A filter expression can contain up to 512 characters.
7. Create or save the webhook.

#### Example

To receive events only when a reload completes successfully, create a filter for the Reload Task Completed event. The resulting filter expression is: `data.status eq "SUCCEEDED"`

Filter builder for the Reload Task Completed event.

![Filter builder with data.status set to equals SUCCEEDED and the generated filter expression.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_webhook-event-filter.png "Click to view full size")

#### Events that don't support filtering

Filtering isn't supported for the following events:

- App Data Model Updated
- API Key Validation Failed
- Automation Created
- Automation Deleted
- Automation Updated
- User Created
- User Deleted

## Managing webhooks

Information note

Webhooks created with Qlik Automate can only be viewed in the Administration activity center. They cannot be edited, deleted, enabled, or disabled.

To manage these webhooks, use the Qlik Automate interface.

### Sorting and searching webhooks

To sort and search webhooks in the table:

- Click ![Up-down arrow](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_up_down.svg) at the top a column to change the sort order.
- Click ![Filter](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_filter.svg) at the top of a column to search for a webhook. The search filter works for full and partial matches.

Webhooks table.

![Management console webhooks table](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/mc-webhooks.png "Click to view full size")

### Turning webhooks on or off

Do the following:

1. In the Administration activity center, go to Webhooks.
2. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to the webhook.
3. To turn on the webhook, select Enable.
4. To turn off the webhook, select Disable.

Newly created webhooks are enabled by default.

### Editing webhooks

Do the following:

1. In the Administration activity center, go to Webhooks.
2. For the webhook you want to edit, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg).
3. Select Edit.
4. Make your edits and click Save.

Information noteIf you click Cancel while there are unsaved changes, a confirmation dialog appears. Click Discard to close without saving your changes.

### Deleting webhooks

Do the following:

1. In the Administration activity center, go to Webhooks.
2. Select the webhook to delete.
3. Click Delete.
4. Confirm the deletion.

Information noteThe Delete button is unavailable until you select one or more webhooks. The action bar displays the number of selected webhooks.

### Viewing webhook history

Webhook event history is retained for 7 days.

Do the following:

1. In the Administration activity center, go to Webhooks.
2. Click ![Down arrow UI icon to expand the webhook menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_down.svg) next to a webhook to expand its event history.

   Webhook history.

   ![Management console webhook history](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/mc-webhook-history.png "Click to view full size")
3. To manually resend an event delivery, click ![The resend icon](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_reload.svg) on the event row.
4. To view the event response payload, click ![Down arrow](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_down.svg) on the event row.

   The payload shows details like application ID, name, and timestamp, which is useful for debugging or auditing past events.

   Event response payload.

   ![Management console webhook event type payload information](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/mc-webhook-payload.png "Click to view full size")
