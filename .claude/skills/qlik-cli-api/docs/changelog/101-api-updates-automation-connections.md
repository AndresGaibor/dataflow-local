---
source: https://qlik.dev/changelog/101-api-updates-automation-connections/
last_updated: 2025-07-08T16:09:30Z
---

# Updated API - Automation Connections breaking change

Qlik is making changes to the recently updated [Automation Connections](https://qlik.dev/changelog/97-api-updates-automation-connections/)
API to improve developer experience on this API. The change is being made to the response
from three endpoints, to return all attributes at the root object, rather than
in the data object. No changes are being made to payloads or parameters.

This change will take effect no sooner than sixty days from the date on this changelog entry.

Endpoints affected:

- [GET `/v1/automation-connections/{id}`](https://qlik.dev/apis/rest/automation-connections/#get-v1-automation-connections-id)
- [PUT `/v1/automation-connections/{id}`](https://qlik.dev/apis/rest/automation-connections/#put-v1-automation-connections-id)
- [POST `/v1/automation-connections`](https://qlik.dev/apis/rest/automation-connections/#post-v1-automation-connections)

Current response, with data returned in `data` object:

```json
{
    "data": {
        "id": "bf96da21-b36f-40d0-ad36-3322e95d218f",
        "name": "Qlik Cloud Services",
        "spaceId": "",
        "ownerId": "645a73ad73599192614c03c3",
        "isConnected": true,
        "connectorId": "61a87510-c7a3-11ea-95da-0fb0c241e75c",
        "oauthAccountName": null,
        "redirect": null,
        "params": [],
        "createdAt": "2024-07-09T08:42:43.000000Z",
        "updatedAt": "2024-07-09T08:42:43.000000Z"
    }
}
```

From today through to the removal date in 60 days, the API will return both
the new and old structures:

```json
{
    "id": "bf96da21-b36f-40d0-ad36-3322e95d218f",
    "name": "Qlik Cloud Services",
    "spaceId": "",
    "ownerId": "645a73ad73599192614c03c3",
    "isConnected": true,
    "connectorId": "61a87510-c7a3-11ea-95da-0fb0c241e75c",
    "oauthAccountName": null,
    "redirect": null,
    "params": [],
    "createdAt": "2024-07-09T08:42:43.000000Z",
    "updatedAt": "2024-07-09T08:42:43.000000Z",
    "data": {
        "id": "bf96da21-b36f-40d0-ad36-3322e95d218f",
        "name": "Qlik Cloud Services",
        "spaceId": "",
        "ownerId": "645a73ad73599192614c03c3",
        "isConnected": true,
        "connectorId": "61a87510-c7a3-11ea-95da-0fb0c241e75c",
        "oauthAccountName": null,
        "redirect": null,
        "params": [],
        "createdAt": "2024-07-09T08:42:43.000000Z",
        "updatedAt": "2024-07-09T08:42:43.000000Z"
    }
}
```

After the removal date in 60 days, the API will return:

```json
{
    "id": "bf96da21-b36f-40d0-ad36-3322e95d218f",
    "name": "Qlik Cloud Services",
    "spaceId": "",
    "ownerId": "645a73ad73599192614c03c3",
    "isConnected": true,
    "connectorId": "61a87510-c7a3-11ea-95da-0fb0c241e75c",
    "oauthAccountName": null,
    "redirect": null,
    "params": [],
    "createdAt": "2024-07-09T08:42:43.000000Z",
    "updatedAt": "2024-07-09T08:42:43.000000Z"
}
```

Review the [Automation Connections API specification](https://qlik.dev/apis/rest/automation-connections)
for more information about this API.
