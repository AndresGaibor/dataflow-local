---
source: https://qlik.dev/changelog/68-api-updates-automation-connections/
last_updated: 2025-07-08T16:09:30Z
---

# New API - Automation Connections

Qlik Automate provides you with the ability to create workflows in a no-code
interface. Most [Qlik Automate connectors](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/connector-blocks/connectors-list.htm)
require a connection to a data source, containing information on where the data
source is, connection credentials, and more.

The `automation-connections` API provides a way of returning the list of connections
that the user has access to. This is useful for audits, and also when programmatically
deploying, backing up, and restoring automations.

To retrieve a list of connections:

```bash
curl "https://your-tenant.us.qlikcloud.com/api/v1/automation-connections" \
 -H "Authorization: Bearer <API-key>"
```

An example response, returning a single connection for the Qlik Cloud Services connector.

```json
{
    "links": {
        "prev": {
            "href": null
        },
        "next": {
            "href": null
        }
    },
    "data": [
        {
            "id": "78dc7c00-7af0-11ed-bb39-bd3b23861504",
            "name": "Qlik Cloud Services",
            "isConnected": true,
            "connectorId": "61a87510-c7a3-11ea-95da-0fb0c241e75c",
            "createdAt": "2022-12-13T14:14:35.000000Z",
            "updatedAt": "2022-12-13T14:14:35.000000Z",
            "ownerId": "637390ec6541614d3a88d6c1"
        }
    ]
}
```

Note that some connections returned via this API will not be visible in the user
interface. In this example, the Qlik Cloud Services connector automatically generates
and manages its connection on behalf of any user who uses
the connector. This means that the API will return the connection, but users will
not be able to manage it. Review the documentation
for each [connector](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/connector-blocks/connectors-list.htm)
for connection details.

Review the [Automation Connections](https://qlik.dev/apis/rest/automation-connections)
API specification for more information about this API.
