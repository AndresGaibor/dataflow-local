---
source: https://qlik.dev/changelog/244-legacy-iam-system-events-deprecation/
last_updated: 2026-08-31T18:19:43+02:00
---

# Deprecation notice - Legacy identity and access management system events

> **Deprecation notice:** Legacy Qlik Cloud system events related to identity and access management are deprecated in favor of namespaced
> `com.qlik.core.*` events.
>
> Use the mappings in this notice to identify the correct replacements. Some replacement events also standardize
> resource or action naming, so the replacement value cannot always be derived by adding `core` to the legacy value.

Qlik Cloud system events related to identity and access management are being standardized using the
`com.qlik.core.<resource>.<event>` format.

If your integration processes one of the legacy events listed in this notice, replace its event type with the mapped
`com.qlik.core.*` event type before the planned removal date.

### Required customer action \{#244-required-customer-action}

If you don't consume Qlik Cloud system events through the Audits API or Qlik Cloud Webhooks, no action is required.

The required change depends on how you consume system events:

- **Audits API:** Update filters and application logic that match the `eventType` value. The Audits API response
  envelope does not change as part of this migration.
- **Qlik Cloud Webhooks:** Only `com.qlik.v1.user.created`, `com.qlik.v1.user.deleted`, and
  `com.qlik.v1.api-key.validation.failed` from this notice are available through the Webhooks feature. Update the event
  type selected in your webhook subscription and follow the separate
  [Qlik Cloud webhooks payload-format migration](https://qlik.dev/changelog/216-webhooks-legacy-fields-removal/) guidance.

### Deprecation timeline \{#244-deprecation-timeline}

The legacy events listed in this changelog entry are deprecated and will be removed on or after
**November 30, 2026**. After their removal, Qlik stops publishing them.

The removal of legacy Webhooks envelope fields follows the separate timeline described in the
[Webhooks payload-format migration notice](https://qlik.dev/changelog/216-webhooks-legacy-fields-removal/).

### Event mappings \{#244-event-mappings}

The following mappings include only publicly available events.

<details>
  <summary id="244-authentication-events">Authentication events</summary>

  | Legacy event type                   | Replacement event type                   | Migration note                                           |
  | ----------------------------------- | ---------------------------------------- | -------------------------------------------------------- |
  | `com.qlik.user-session.begin`       | `com.qlik.core.user-session.begun`       | The action name changes from `begin` to `begun`.         |
  | `com.qlik.user-session.end`         | `com.qlik.core.user-session.ended`       | The action name changes from `end` to `ended`.           |
  | `com.qlik.user-identity.conflict`   | `com.qlik.core.user-identity.conflicted` | The action name changes from `conflict` to `conflicted`. |
  | `com.qlik.user-identity.reassigned` | `com.qlik.core.user-identity.reassigned` |                                                          |
  | `com.qlik.oauth-token.issued`       | `com.qlik.core.oauth-token.issued`       |                                                          |
  | `com.qlik.oauth-token.revoked`      | `com.qlik.core.oauth-token.revoked`      |                                                          |

  For more information, see [User sessions events](/apis/event/user-sessions/),
  [User identities events](/apis/event/user-identities/), and
  [OAuth tokens events](/apis/event/oauth-tokens/).
</details>

<details>
  <summary id="244-api-keys-events">API keys events</summary>

  | Legacy event type                       | Replacement event type                    |
  | --------------------------------------- | ----------------------------------------- |
  | `com.qlik.api-key.created`              | `com.qlik.core.api-key.created`           |
  | `com.qlik.api-key.updated`              | `com.qlik.core.api-key.updated`           |
  | `com.qlik.api-key.deleted`              | `com.qlik.core.api-key.deleted`           |
  | `com.qlik.api-key.validated`            | No replacement available                  |
  | `com.qlik.v1.api-key.validation.failed` | `com.qlik.core.api-key.validation.failed` |
  | `com.qlik.api-keys-config.updated`      | `com.qlik.core.api-keys-config.updated`   |

  For more information, see [API keys events](/apis/event/api-keys/) and
  [API keys configuration events](/apis/event/api-keys-configs/).
</details>

<details>
  <summary id="244-users-events">Users events</summary>

  The legacy and `v1` user-deleted events map to the same replacement event.

  | Legacy event type              | Replacement event type           | Migration note                                                                  |
  | ------------------------------ | -------------------------------- | ------------------------------------------------------------------------------- |
  | `com.qlik.v1.user.created`     | `com.qlik.core.user.created`     |                                                                                 |
  | `com.qlik.user.deleted`        | `com.qlik.core.user.deleted`     |                                                                                 |
  | `com.qlik.v1.user.deleted`     | `com.qlik.core.user.deleted`     |                                                                                 |
  | `com.qlik.v1.user.updated`     | `com.qlik.core.user.updated`     | The field-level change list moves from `extensions.updates` to `data._updates`. |
  | `com.qlik.v1.user.provisioned` | `com.qlik.core.user.provisioned` |                                                                                 |
  | `com.qlik.v1.user.purged`      | `com.qlik.core.user.purged`      |                                                                                 |

  For more information, see [Users events](/apis/event/users/).
</details>

<details>
  <summary id="244-groups-events">Groups events</summary>

  | Legacy event type                         | Replacement event type                | Migration note                                                                                                                                                                                                                             |
  | ----------------------------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  | `com.qlik.group.config.updated`           | `com.qlik.core.group-setting.updated` | The resource name changes from `group.config` to `group-setting`.                                                                                                                                                                          |
  | `com.qlik.v1.group-setting.updated`       | `com.qlik.core.group-setting.updated` |                                                                                                                                                                                                                                            |
  | `com.qlik.v1.group-setting.purged`        | `com.qlik.core.group-setting.purged`  |                                                                                                                                                                                                                                            |
  | `com.qlik.v1.group.created`               | `com.qlik.core.group.created`         |                                                                                                                                                                                                                                            |
  | `com.qlik.v1.group.deleted`               | `com.qlik.core.group.deleted`         |                                                                                                                                                                                                                                            |
  | `com.qlik.v1.group.updated`               | `com.qlik.core.group.updated`         |                                                                                                                                                                                                                                            |
  | `com.qlik.v1.group.purged`                | `com.qlik.core.group.purged`          |                                                                                                                                                                                                                                            |
  | `com.qlik.v1.group.users.modified`        | `com.qlik.core.group.users.modified`  |                                                                                                                                                                                                                                            |
  | `com.qlik.group.user.group.claim.updated` | `com.qlik.core.user.updated`          | Identify group-claim changes in `data._updates` by checking for updates whose `path` is `/groups` or `/assignedGroups`. During the overlap period, deduplicate events using the CloudEvent `id` to avoid processing the same change twice. |

  For more information, see [Groups events](/apis/event/groups/) and
  [Group settings events](/apis/event/group-settings/).
</details>

<details>
  <summary id="244-roles-events">Roles events</summary>

  | Legacy event type                 | Replacement event type              | Migration note                                                                                                          |
  | --------------------------------- | ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
  | `com.qlik.v1.role.created`        | `com.qlik.core.role.created`        |                                                                                                                         |
  | `com.qlik.v1.role.deleted`        | `com.qlik.core.role.deleted`        |                                                                                                                         |
  | `com.qlik.v1.role.updated`        | `com.qlik.core.role.updated`        | The field-level change list is named `_updates` instead of `updates`, and each entry uses `path` instead of `property`. |
  | `com.qlik.v1.role.synced`         | `com.qlik.core.role.synced`         |                                                                                                                         |
  | `com.qlik.v1.role-setting.purged` | `com.qlik.core.role-setting.purged` |                                                                                                                         |

  For more information, see [Roles events](/apis/event/roles/).
</details>

<details>
  <summary id="244-tenants-events">Tenants events</summary>

  | Legacy event type                          | Replacement event type                       | Migration note                                                                                                          |
  | ------------------------------------------ | -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
  | `com.qlik.tenant.created`                  | `com.qlik.core.tenant.created`               |                                                                                                                         |
  | `com.qlik.tenant.updated`                  | `com.qlik.core.tenant.updated`               | The field-level change list is named `_updates` instead of `updates`, and each entry uses `path` instead of `property`. |
  | `com.qlik.tenant.deleted`                  | `com.qlik.core.tenant.deleted`               |                                                                                                                         |
  | `com.qlik.v1.tenant.deactivated`           | `com.qlik.core.tenant.deactivated`           |                                                                                                                         |
  | `com.qlik.v1.tenant.reactivated`           | `com.qlik.core.tenant.reactivated`           |                                                                                                                         |
  | `com.qlik.v1.tenant.allowed-deactivate`    | `com.qlik.core.tenant.allowed-deactivate`    |                                                                                                                         |
  | `com.qlik.v1.tenant.disallowed-deactivate` | `com.qlik.core.tenant.disallowed-deactivate` |                                                                                                                         |

  For more information, see [Tenants events](/apis/event/tenants/).
</details>

<details>
  <summary id="244-web-integrations-events">Web integrations events</summary>

  | Legacy event type                  | Replacement event type                  | Migration note                                                                                                          |
  | ---------------------------------- | --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
  | `com.qlik.web-integration.created` | `com.qlik.core.web-integration.created` |                                                                                                                         |
  | `com.qlik.web-integration.updated` | `com.qlik.core.web-integration.updated` | The field-level change list is named `_updates` instead of `updates`, and each entry uses `path` instead of `property`. |
  | `com.qlik.web-integration.deleted` | `com.qlik.core.web-integration.deleted` |                                                                                                                         |

  For more information, see [Web integrations events](/apis/event/web-integrations/).
</details>

<details>
  <summary id="244-spaces-events">Spaces events</summary>

  | Legacy event type                   | Replacement event type                   | Migration note                                               |
  | ----------------------------------- | ---------------------------------------- | ------------------------------------------------------------ |
  | `com.qlik.space.created`            | `com.qlik.core.space.created`            |                                                              |
  | `com.qlik.space.updated`            | `com.qlik.core.space.updated`            |                                                              |
  | `com.qlik.space.deleted`            | `com.qlik.core.space.deleted`            |                                                              |
  | `com.qlik.space.settings.updated`   | `com.qlik.core.space.settings.updated`   |                                                              |
  | `com.qlik.space.assignment.created` | `com.qlik.core.space.assignment.created` |                                                              |
  | `com.qlik.space.assignment.updated` | `com.qlik.core.space.assignment.updated` |                                                              |
  | `com.qlik.space.assignment.deleted` | `com.qlik.core.space.assignment.deleted` |                                                              |
  | `com.qlik.space.share.created`      | `com.qlik.core.space.share.created`      |                                                              |
  | `com.qlik.space.share.updated`      | `com.qlik.core.space.share.updated`      |                                                              |
  | `com.qlik.space.share.deleted`      | `com.qlik.core.space.share.deleted`      |                                                              |
  | `com.qlik.v1.environment.created`   | `com.qlik.core.environment.created`      |                                                              |
  | `com.qlik.v1.environment.updated`   | `com.qlik.core.environment.updated`      |                                                              |
  | `com.qlik.v1.environment.deleted`   | `com.qlik.core.environment.deleted`      |                                                              |
  | `com.qlik.v1.request.created`       | `com.qlik.core.space.request.created`    | The resource name changes from `request` to `space.request`. |
  | `com.qlik.v1.request.approved`      | `com.qlik.core.space.request.approved`   | The resource name changes from `request` to `space.request`. |
  | `com.qlik.v1.request.deleted`       | `com.qlik.core.space.request.deleted`    | The resource name changes from `request` to `space.request`. |
  | `com.qlik.v1.space.purged`          | `com.qlik.core.space.purged`             |                                                              |

  For more information, see [Spaces events](/apis/event/spaces/).
</details>

<details>
  <summary id="244-oauth-clients-events">OAuth clients events</summary>

  For OAuth clients events, the payload and envelope remain unchanged. Only the event type changes.

  | Legacy event type                                     | Replacement event type                                  |
  | ----------------------------------------------------- | ------------------------------------------------------- |
  | `com.qlik.v1.oauth-client.created`                    | `com.qlik.core.oauth-client.created`                    |
  | `com.qlik.v1.oauth-client.updated`                    | `com.qlik.core.oauth-client.updated`                    |
  | `com.qlik.v1.oauth-client.deleted`                    | `com.qlik.core.oauth-client.deleted`                    |
  | `com.qlik.v1.oauth-client.published`                  | `com.qlik.core.oauth-client.published`                  |
  | `com.qlik.v1.oauth-client.secret.created`             | `com.qlik.core.oauth-client.secret.created`             |
  | `com.qlik.v1.oauth-client.secret.deleted`             | `com.qlik.core.oauth-client.secret.deleted`             |
  | `com.qlik.v1.oauth-client.connection-config.approved` | `com.qlik.core.oauth-client.connection-config.approved` |
  | `com.qlik.v1.oauth-client.connection-config.updated`  | `com.qlik.core.oauth-client.connection-config.updated`  |
  | `com.qlik.v1.oauth-client.connection-config.deleted`  | `com.qlik.core.oauth-client.connection-config.deleted`  |

  For more information, see [OAuth clients events](/apis/event/oauth-clients/).
</details>

### Compatibility summary \{#244-compatibility-summary}

Most customers only need to replace the legacy event type with the mapped namespaced event type. The following events
require additional attention:

- **Users updated:** Read the field-level change list from `data._updates` instead of `extensions.updates`.
- **Group claim updates:** Replace `com.qlik.group.user.group.claim.updated` with
  `com.qlik.core.user.updated`. Identify group-claim changes by checking `data._updates` for entries whose `path` is
  `/groups` or `/assignedGroups`. During the overlap period, deduplicate events using the CloudEvent `id`.
- **Roles, tenants, and web integrations updated:** Read the field-level change list from `_updates` instead of
  `updates`. Each entry uses `path` instead of `property`.
- **Webhooks:** The user-created, user-deleted, and API-key-validation-failed events also follow the separate
  [Webhooks payload-format migration](https://qlik.dev/changelog/216-webhooks-legacy-fields-removal/).
- **OAuth clients:** Only the event type changes.

### New events in this namespace \{#244-new-events}

The following event is new and does not replace a legacy event:

- `com.qlik.core.auth-settings.updated`, published when the authentication settings of a tenant change.

For more information about namespaced system events, see
[Qlik Cloud system events](https://qlik.dev/apis/event/).
