---
source: https://qlik.dev/changelog/211-new-system-events/
last_updated: 2026-04-22T10:13:33Z
---

# New system events for automations, licenses, roles, web integrations, and IP policies

Qlik Cloud system events now cover five additional resource domains, giving you more
options to build reactive integrations and audit workflows.

All new events follow the CloudEvents 3.0 specification and are available via the
[Audits API](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-events.htm).

## New event types \{#211-new-event-types}

### Automations \{#211-automations}

- [`com.qlik.v1.automation.run.ended`](https://qlik.dev/apis/event/automations/): Published when an
  automation execution ends. The payload includes run status, execution context, block-level
  metrics (duration, API calls, bytes sent and received), and billing information.

### Licenses \{#211-licenses}

Ten new events track the full lifecycle of license resources:

- `com.qlik.license.assignment.deleted`: license assignment deleted
- `com.qlik.license.assignment.rejected`: license assignment rejected
- `com.qlik.license.assignment.updated`: license assignment updated
- `com.qlik.license.definition.updated`: license definition updated
- `com.qlik.v1.license.lease.created`: capacity lease created
- `com.qlik.v1.license.lease.deleted`: capacity lease deleted
- `com.qlik.v1.license.lease.updated`: capacity lease updated
- `com.qlik.v1.licenses.purged`: tenant license resources purged
- `com.qlik.v1.license.tenant.associated`: tenant associated to a license
- `com.qlik.license.data.volume.consumption.aggregated` *(deprecated)*: data volume consumption aggregated

For full event reference details, see the [licenses events API](https://qlik.dev/apis/event/licenses/).

### Roles \{#211-roles}

Four new events track role changes across the tenant:

- `com.qlik.v1.role.created`: role created (includes assigned scopes for custom roles)
- `com.qlik.v1.role.deleted`: role deleted
- `com.qlik.v1.role.updated`: role updated by an admin
- `com.qlik.v1.role.synced`: role definitions synchronized across the platform

Note: Permission lists are not included in role event payloads due to payload size limits.

For full event reference details, see the [roles events API](https://qlik.dev/apis/event/roles/).

### Web integrations \{#211-web-integrations}

Three new events track web integration lifecycle:

- `com.qlik.web-integration.created`: web integration created
- `com.qlik.web-integration.deleted`: web integration deleted
- `com.qlik.web-integration.updated`: web integration updated

For full event reference details, see the [web-integrations events API](https://qlik.dev/apis/event/web-integrations/).

### IP policies \{#211-ip-policies}

Three new events track IP policy changes in the tenant:

- `com.qlik.core.ip-policy.created`: IP policy created
- `com.qlik.core.ip-policy.deleted`: IP policy deleted
- `com.qlik.core.ip-policy.updated`: IP policy updated (payload includes an
  `_updates` array listing changed attribute paths with old and new values)

For full event reference details, see the [IP policies events API](https://qlik.dev/apis/event/core/ip-policies/).
