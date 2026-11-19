---
source: https://qlik.dev/changelog/257-direct-access-agents-api-connectivity-configuration-metadata/
last_updated: 2026-10-13T16:51:04+02:00
---

# Direct Access Agents API configuration endpoint now available

The Direct Access Agents API now includes the
`GET /api/connectivity/direct-access-agents/{agentId}/configurations` endpoint in the `connectivity` namespace.

The endpoint retrieves the Direct Access gateway configuration and includes gateway environment and product version
metadata when available.

The existing [Direct Access Agents API](https://qlik.dev/apis/rest/direct-access-agents/) at `/api/v1/direct-access-agents` continues
to work as documented.

This endpoint requires the `TenantAdmin` (Tenant Admin) role. The requester must also be either the gateway's space
owner or a member of the gateway's space with the `dataconsumer` (Can consume data) role.

For more information, see the
[reference documentation](https://qlik.dev/apis/rest/connectivity/direct-access-agents/).
