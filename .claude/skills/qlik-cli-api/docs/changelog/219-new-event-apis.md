---
source: https://qlik.dev/changelog/219-new-event-apis/
last_updated: 2026-05-12T16:24:53Z
---

# New system events for app usage tracking, notification digests, reloads, and hub dashboards

Qlik Cloud system events now include four new event APIs, enabling you to
build integrations that track application resource usage, respond to
notification configuration changes, react to app reload completions, and
monitor hub dashboard changes.

### App usages \{#218-app-usages}

The [App usages event API](https://qlik.dev/apis/event/app-usages/) publishes events when
application usage quota is consumed:

- `com.qlik.v1.app-usage.quota.consumed`: Triggered when an app consumes a unit
  of usage quota

Use this event to monitor per-app resource consumption, alert on quota
thresholds, or build dashboards that track usage patterns across your
tenant.

### Notification digests \{#218-notification-digests}

The [Notification digests event API](https://qlik.dev/apis/event/notification-digests/)
covers changes to notification digest configurations:

- `com.qlik.notification-digest.updated`: Triggered when a notification digest
  configuration is created, updated, or modified

Use this event to track notification digest lifecycle, clean up orphaned
digests, or audit changes to notification preferences.

### Reloads \{#218-reloads}

The [Reloads event API](https://qlik.dev/apis/event/reloads/) publishes reload task
completion events:

- `com.qlik.v1.reload.finished`: Triggered when an application reload task
  completes

Use this event to track reload completion status, trigger dependent
processing, send completion notifications to stakeholders, or implement
reload-driven workflows.

### Hub dashboards \{#218-hub-dashboards}

The [Hub dashboards event API](https://qlik.dev/apis/event/hub-dashboards/) publishes
events when hub dashboard configurations change:

- `com.qlik.v1.hub-dashboard.updated`: Triggered when a hub dashboard is
  created, updated, or modified

Use this event to audit dashboard changes, track dashboard creation and
deletion, trigger dependent content updates, or implement approval
workflows for dashboard modifications.
