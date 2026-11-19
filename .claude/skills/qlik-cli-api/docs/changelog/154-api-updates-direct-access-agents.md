---
source: https://qlik.dev/changelog/154-api-updates-direct-access-agents/
last_updated: 2025-07-11T16:40:21+01:00
---

# Updated API - The Direct Access Agents API now supports custom data type mappings for ODBC connectors

The [Direct Access Agents API](https://qlik.dev/apis/rest/direct-access-agents/) has been updated with
new endpoints that allow you to manage the custom data type mapping configuration file
for the Generic ODBC Connector.

The following new endpoints give you more control over connector behavior on Direct Access gateways:

- `GET /api/v1/direct-access-agents/{agentId}/connectors/{connectorType}/files/custom-data-type-mappings` -
  Retrieves the contents of the custom mapping configuration file for the specified connector type.
- `PUT /api/v1/direct-access-agents/{agentId}/connectors/{connectorType}/files/custom-data-type-mappings` -
  Replace the custom mapping configuration for the specified connector type.

These new endpoints are available in Direct Access Gateway v1.7.5 and later, and
currently support only the `odbc-connector` type. The caller must be
assigned the `TenantAdmin` role.

For API information, refer to the [Direct Access Gateway API reference](https://qlik.dev/apis/rest/direct-access-agents/),
and for configuration examples see [Configuring Direct Access Gateways](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/direct-access-gateway-troubleshooting.htm)
on Qlik Help.
