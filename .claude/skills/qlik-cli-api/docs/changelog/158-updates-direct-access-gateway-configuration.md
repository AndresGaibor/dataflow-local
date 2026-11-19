---
source: https://qlik.dev/changelog/158-updates-direct-access-gateway-configuration/
last_updated: 2025-08-07T10:29:43+02:00
---

# Updated API - The Direct Access Agents API now supports remote configuration in the File Connector

The [Direct Access Agents API](https://qlik.dev/apis/rest/direct-access-agents/) has been updated with
two endpoints that enable you to remotely manage the File Connector's allowed paths,
without needing direct access to the gateway machine locally.

The following two endpoints give you more control over connector behavior on Direct Access gateways:

- `GET /api/v1/direct-access-agents/{agentId}/connectors/{connectorType}/files/allowed-paths` -
  Retrieves the allowed paths settings for the File Connector.
- `PUT /api/v1/direct-access-agents/{agentId}/connectors/{connectorType}/files/allowed-paths` -
  Replaces the content of the allowed paths configuration file for the File Connector.

These new endpoints are available in Direct Access Gateway v1.7.6 and later. The requestor must be
assigned the `TenantAdmin` role.

For more API information, see the [Direct Access Gateway API reference](https://qlik.dev/apis/rest/direct-access-agents/).
