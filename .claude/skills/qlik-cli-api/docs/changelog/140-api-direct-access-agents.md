---
source: https://qlik.dev/changelog/140-api-direct-access-agents/
last_updated: 2025-05-12T16:48:26+02:00
---

# New API - Direct Access Agents API

The new Direct Access Agents API is now available for remotely managing Direct Access Gateway agents.

This API allows you to programmatically retrieve and update configuration settings, as well as restart Direct Access
Gateway agents.

This API is supported from Direct Access Gateway 1.7.2 onward and is available only to users with the Tenant Admin
role.

With the Direct Access Agents API, you can:

- Retrieve configuration settings via `GET /direct-access-agents/{agentId}/configurations`.
- Update configuration settings using JSON Patch via `PATCH /direct-access-agents/{agentId}/configurations`.
- Restart the agent via `POST /direct-access-agents/{agentId}/actions/{agentAction}`.

To use this API, you need the Direct Access Gateway agent ID (`agentId`).
This ID appears in the `connector-agent` logs as the `agent-gateway-id` after submitting a metadata request or reload,
for example:

`[INFO ] DAG - ... Message=agent-gateway-id: llaIfam89pGBzccYd9R1W4S4wee-S1FH`

For more information, refer to:

- [Viewing and downloading log files](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/direct-access-gateway-troubleshooting.htm)
  on help.qlik.com.
- The [API reference documentation](https://qlik.dev/apis/rest/direct-access-agents/).
