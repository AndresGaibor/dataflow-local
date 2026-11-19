---
source: https://qlik.dev/changelog/204-new-events/
last_updated: 2026-03-12T08:03:42+01:00
---

# New Qlik Cloud system events for identity, security, and tenant management

Qlik Cloud system events now include new event types covering identity management,
security, and multi-tenant operations. These events enable you to automate access
provisioning, audit compliance, synchronize with external identity systems, and monitor
your Qlik Cloud infrastructure in real time.

All new events are available for consumption via [Audits (Events)](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-events.htm).

## New event types \{#204-new-event-types}

- [**API keys**](https://qlik.dev/apis/event/api-keys/): Track API key lifecycle for security and
  access management
- [**API key configs**](https://qlik.dev/apis/event/api-keys-configs/): Monitor API key config changes for
  compliance and security
- [**OAuth clients**](https://qlik.dev/apis/event/oauth-clients/): Monitor OAuth client lifecycle and
  security configurations
- [**OAuth tokens**](https://qlik.dev/apis/event/oauth-tokens/): Track token issuance and revocation for
  security and auditing
- [**User identities**](https://qlik.dev/apis/event/user-identities/): Track identity management and
  conflict resolution
- [**User sessions**](https://qlik.dev/apis/event/user-sessions/): Monitor user authentication events for
  security and audit
- [**Groups**](https://qlik.dev/apis/event/groups/): Track group lifecycle and user assignment changes in
  real time
- [**Group settings**](https://qlik.dev/apis/event/group-settings/): Monitor group configuration changes
- [**Tenants**](https://qlik.dev/apis/event/tenants/): Monitor tenant lifecycle and status changes
- [**Rate limits**](https://qlik.dev/apis/event/rate-limits/): Monitor rate limit violations for
  performance optimization

## Why this matters \{#204-why-this-matters}

- **Compliance**: Emit audit-trail events for access control changes, role assignments,
  and credential lifecycle
- **Automation**: React instantly to changes and synchronize downstream systems without
  polling
- **Security**: Detect and respond to suspicious patterns in tokens, sessions, and
  configuration changes
- **Multi-tenant operations**: Coordinate workflows across tenants with tenant lifecycle
  events
