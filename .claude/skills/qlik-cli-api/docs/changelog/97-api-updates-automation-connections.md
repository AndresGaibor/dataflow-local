---
source: https://qlik.dev/changelog/97-api-updates-automation-connections/
last_updated: 2025-07-08T16:09:30Z
---

# Updated API - Automation Connections

Qlik Automate provides you with the ability to create workflows in a no-code
interface. Most [Qlik Automate connectors](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/connector-blocks/connectors-list.htm)
require a connection to a data source, containing information on where the data
source is, connection credentials, and more.

The updated `automation-connections` API endpoints provide capabilities for users to manage automation connections
in personal and shared spaces, including, but not limited to, retrieving, creating, updating and deleting an
automation connection, as well as changing its owner and moving it to a different space.
This is useful for collaborations and administration, and also when programmatically deploying,
backing up, and restoring automations.

In the initial release, you could retrieve a list of connections:

```bash
curl "https://your-tenant.us.qlikcloud.com/api/v1/automation-connections" \
 -H "Authorization: Bearer <API-key>"
```

Now with the updated API, you could retrieve a single connection:

```bash
curl "https://your-tenant.us.qlikcloud.com/api/v1/automation-connections/{id}" \
 -H "Authorization: Bearer <API-key>"
```

An example response, returning a single connection for the Qlik Cloud Services connector.

```json
{
    "data": {
    "id": "1968b1a0-1a75-11ee-9e04-976916adf99b",
    "name": "Qlik Cloud Services",
    "spaceId": "",
    "ownerId": "64a428976c47a6c39e592159",
    "isConnected": true,
    "connectorId": "61a87510-c7a3-11ea-95da-0fb0c241e75c",
    "oauthAccountName": null,
    "redirect": null,
    "params": [],
    "createdAt": "2023-07-04T14:14:33.000000Z",
    "updatedAt": "2024-03-14T11:32:10.000000Z"
    }
}
```

The API now also supports connection creation and updates, for example, creating a new connection:

```bash
curl "https://your-tenant.us.qlikcloud.com/api/v1/automation-connections" \
 -X POST \
 -H "Authorization: Bearer <API-key>" \
 -H "Content-type: application/json" \
 -d '{"name":"connection","params":[{"name":"username","value":"string"}],"spaceId":"5f0f78b239ff4f0001234567","connectorId":"3004e850-1985-11ee-b6df-8d800b305320"}'
```

An example response, returning details of a created connection.

```json
{
  "id": "e0e720d0-4947-11ec-a1d2-9559fa35801d",
  "name": "connection",
  "params": [
    {
      "id": "39a90780-8874-11ee-b16c-89512345678",
      "meta": [],
      "name": "region",
      "order": 1,
      "value": "string",
      "fieldType": "enum",
      "isOptional": "false",
      "exampleValue": "string",
      "paramOptions": [
        {
          "id": "39a90780-8874-11ee-b16c-89512345678",
          "value": "string"
        }
      ],
      "documentation": "string"
    }
  ],
  "ownerId": "sWYAHxZxhtcmBT7Ptc5xJ5I6N7HxwnEy",
  "spaceId": "5f0f78b239ff4f0001234567",
  "redirect": "string",
  "createdAt": "2021-12-23T12:28:21.000000Z",
  "updatedAt": "2021-12-23T12:28:21.000000Z",
  "connectorId": "e0e720d0-4947-11ec-a1d2-9559fa35801d",
  "isConnected": "true",
  "oauthAccountName": "oauth"
}
```

Note that the `connectorId` value isn't currently available via published API. For now,
retrieve this value by viewing the ID of a previously created connection of the type you require.

Review the [Automation Connections](https://qlik.dev/apis/rest/automation-connections)
API specification for more information about this API.
