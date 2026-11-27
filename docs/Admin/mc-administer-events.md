---
title: "Monitoring system events"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-events.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Monitoring system and resources"]
---

# Monitoring system events

Monitor and access detailed information about system events, including the event type, source, and the user who triggered the event.

## Viewing events

You can review system events on the Events page in the Administration activity center. This page provides details including:

- User session data
- Application creation data
- Event type
- Source
- The user who initiated the event. If the user name is unavailable, the user ID is shown instead.

You can filter the events table by event type. To view more details about a specific event, click ![Arrow down](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_down.svg) next to it.

### Data retention

Events are archived after 90 days but remain accessible via the [Audits API](https://qlik.dev/apis/rest/audits/#get-api-v1-audits-archive) for the lifetime of the tenant.

### Examples of sources and events

Examples of sources:

- com.qlik/licenses
- com.qlik/engine
- com.qlik/edge-auth

Examples of events:

- app.created
- user-session.begin
- assignment.added
- assignment.revoked

For more information, see [Qlik Developer Portal: Events API](https://qlik.dev/apis#event).

## Retrieving archived events using the Audit API and Postman

This example shows how retrieve archived events using Postman. For more information about the Audits API, see [Qlik Developer Portal: Audits API](https://qlik.dev/apis/rest/audits).

### Preparation

Before sending a request, ensure you have the following:

- Tenant URL: This is the base URL for your Qlik Cloud tenant, for example, https://your-tenant.us.qlikcloud.com/.
- API key for authorized requests: You can generate an API key by following the instructions in [*Managing API keys*](mc-generate-api-keys.htm).

### Retrieving archived events

Do the following:

1. Start Postman.
2. Set the HTTP method to GET.
3. Enter the API URL endpoint with the appended date parameter to filter archived events:

   {tenant-url}/api/v1/audits/archive?date=yyyy-mm-dd

   Example URL:

   https://your-tenant.us.qlikcloud.com/api/v1/audits/archive?date=2019-11-16
4. On the Auth tab, choose Bearer Token as the Auth Type.
5. Enter your API key in the Token [field](#glossary-0 "Glossary term").
6. Click Send.

If the request is successful, the API will return a JSON response with the archived events matching the specified date.

Example JSON response

Here’s an example of the JSON response from the API:

{
"data": [
{
"source": "com.qlik/edge-auth",
"contentType": "application/json",
"eventType": "com.qlik.user-session.begin",
"eventId": "ykaaY1j2yZvClvwN6pmbO\_3tjZeoVoBb",
"eventTime": "2019-11-16T17:29:50.273Z",
"tenantId": "bOowHi6pxn0GaUcXIna4oFco62ag9uoH",
"userId": "fSuVsk3HjaeBeiSoyNWdbwH6zwr4T-Jq",
"data": {
"subject": "okta\\00ukoxpallpY4QRs70x7"
}
},
{
…
}
]
}

## Learn more

- [*Finding deprecated charts*](../Visualizations/find-deprecated-charts.htm)
