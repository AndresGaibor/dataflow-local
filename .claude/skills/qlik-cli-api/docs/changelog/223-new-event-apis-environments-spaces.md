---
source: https://qlik.dev/changelog/223-new-event-apis-environments-spaces/
last_updated: 2026-06-02T14:25:27+02:00
---

# New system events for environments and spaces

Qlik Cloud system events now include two new event APIs, enabling you to build
integrations that track environment lifecycle, respond to space configuration
changes, and automate tenant management workflows.

### Environments \{#220-environments}

The [Environments event API](https://qlik.dev/apis/event/environments/) publishes events related to environment management:

- `com.qlik.v1.environment.created`: Triggered when an environment is created
- `com.qlik.v1.environment.deleted`: Triggered when an environment is deleted
- `com.qlik.v1.environment.updated`: Triggered when an environment configuration is updated

Use these events to track environment lifecycle, maintain audit logs of environment
changes, automatically provision related resources, or trigger cleanup workflows when
environments are removed.

### Spaces \{#220-spaces}

The [Spaces event API](https://qlik.dev/apis/event/spaces/) covers the complete lifecycle of space
management:

- `com.qlik.v1.space.created`: Triggered when a space is created
- `com.qlik.v1.space.deleted`: Triggered when a space is deleted
- `com.qlik.v1.space.updated`: Triggered when space metadata is updated
- `com.qlik.v1.space.assignment.created`: Triggered when a space assignment is created
- `com.qlik.v1.space.assignment.deleted`: Triggered when a space assignment is deleted
- `com.qlik.v1.space.assignment.updated`: Triggered when a space assignment is updated
- `com.qlik.v1.space.share.created`: Triggered when a space is shared
- `com.qlik.v1.space.share.deleted`: Triggered when a space share is revoked
- `com.qlik.v1.space.share.updated`: Triggered when space share settings are modified
- `com.qlik.v1.space.share.session.attached`: Triggered when a user's session is attached
  to a space share
- `com.qlik.v1.space.settings.updated`: Triggered when space settings are changed
- `com.qlik.v1.space.groups-cache.invalidated`: Triggered when the groups cache for a
  space is invalidated

Use these events to track space operations, automate space provisioning workflows,
monitor access control changes, respond to sharing events, and maintain consistency
across your tenant.
