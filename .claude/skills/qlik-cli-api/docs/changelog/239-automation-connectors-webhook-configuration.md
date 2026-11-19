---
source: https://qlik.dev/changelog/239-automation-connectors-webhook-configuration/
last_updated: 2026-07-22T13:38:12+02:00
---

# New Automation Connectors API endpoint for webhook configuration

The [Automation Connectors API](https://qlik.dev/apis/rest/workflows/automation-connectors/) adds a new endpoint that returns the
webhook configuration for an automation connector, including its available events and event parameters.

Use this endpoint to discover which webhook events a connector supports and what parameters each event needs,
before you set up a webhook-triggered automation programmatically instead of through the Qlik Automate editor.

The new endpoint is:

- `GET /workflows/automation-connectors/{connectorId}/webhooks/configuration`: Retrieves the webhook
  configuration for an automation connector, including its events and event parameters.

The response includes the `events` available for a connector. Each event has a `name`, `role`, `description`,
`params` (with a `type`, whether the parameter is `required`, and any `options`), and an `exampleOutput` payload.
The `automatic` flag on the response shows whether the connector sets up the webhook automatically.

For more information, see the reference documentation for the
[Automation Connectors API](https://qlik.dev/apis/rest/workflows/automation-connectors/).
