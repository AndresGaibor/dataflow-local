---
source: https://qlik.dev/changelog/109-platform-ops-connector/
last_updated: 2025-07-08T16:09:30Z
---

# Block updates - Qlik Platform Operations connector

The [Qlik Platform Operations connector](https://qlik.dev/manage/platform-operations/no-code/overview)
for [Qlik Automate](https://qlik.dev/toolkits/no-code/) enables the deployment and
management of Qlik Cloud tenants without any code.

New blocks:

- `Create Webhook`: Creates a new webhook for the specified events and filters.
- `Update Webhook`: Updates an existing webhook.
- `List Webhooks`: Retrieves a list of all webhooks in the tenant accessible by the
  OAuth client.
- `Get Webhook`: Retrieves information about a specific webhook.
- `Delete Webhook`: Removes a specific webhook.
- `List Webhook Event Types`: Retrieves a list of all event types against which a webhook
  can be configured.
- `List Automation Connections`: Retrieves a list of all automation connections in
  the tenant accessible by the OAuth client.
- `Get Automation Connection`: Retrieves information about a specific automation connection.
- `Update Automation Connection Space`: Moves a specific automation connection to
  a new space.
- `Delete Automation Connection`: Removes a specific automation connection.

Updated blocks:

- `Create Reload Task`: Updated parameters to match the API specification for creating a reload task.
- `Update Reload Task`: Updated parameters to match the API specification for creating a reload task.

Review [Qlik Platform Operations connector overview](https://qlik.dev/manage/platform-operations/no-code/overview)
for information on how to get started using the connector.
