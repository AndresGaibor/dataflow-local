---
source: https://qlik.dev/changelog/141-api-updates-direct-access-agents/
last_updated: 2025-06-03T11:03:41+02:00
---

# Updated API - The Direct Access Agents API now supports connector-specific configuration files

The [Direct Access Agents API](https://qlik.dev/apis/rest/direct-access-agents/) has been updated with new endpoints that allow you to
retrieve and update configuration files for individual connectors, including the File connector and the REST connector.

Configuration files must use a plain text format: flat, newline-delimited, and unescaped.

The following new endpoints give you more control over connector behavior on Direct Access gateways:

- `GET /v1/direct-access-agents/{agentId}/connectors/{connectorType}/files` - Retrieve configuration files for the
  specified connector.
- `GET /v1/direct-access-agents/{agentId}/connectors/{connectorType}/files/{fileType}` - Retrieve the configuration
  values from the flat file for the specified connector.
- `PUT /v1/direct-access-agents/{agentId}/connectors/{connectorType}/files/{fileType}` - Replace the contents of the
  flat file for the specified connector. Partial updates are not supported.

These new endpoints are supported from Direct Access Gateway 1.7.4 onward and are available only to users with the
Tenant Admin role.

To use these endpoints, you need the Direct Access Gateway agent ID (`agentId`).
This ID appears in the `connector-agent` logs as the `agent-gateway-id` after submitting a metadata request or reload,
for example:

`[INFO ] DAG - ... Message=agent-gateway-id: llaIfam89pGBzccYd9R1W4S4wee-S1FH`

For more information, refer to:

- [Viewing and downloading log files](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/direct-access-gateway-troubleshooting.htm)
  on help.qlik.com.
- The [API reference documentation](https://qlik.dev/apis/rest/direct-access-agents/).
