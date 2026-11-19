---
source: https://qlik.dev/changelog/210-apps-events-cloudevents/
last_updated: 2026-04-22T10:13:33Z
---

# Updated API - Apps events now use CloudEvents 1.0.2 format

The [Apps events API](https://qlik.dev/apis/event/apps/) has been updated to use the
[CloudEvents 1.0.2 specification](https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md)
envelope format.
If you consume app events, review the payload and event type changes below.

## New app.opened event \{#210-app-opened}

A new event type `com.qlik.v1.app.opened` is now available. It is published when an app is
opened in Qlik Cloud. You can use this event to track app engagement, audit access patterns, and
trigger downstream workflows on app open.

## Payload format changes \{#210-payload-format}

App event payloads now use the CloudEvents 1.0.2 envelope. The following fields replace the
legacy v0.1 envelope fields:

| Legacy field (CloudEvents v0.1) | New field (CloudEvents 1.0.2) |
| ------------------------------- | ----------------------------- |
| `cloudEventsVersion: "0.1"`     | `specversion: "1.0.2"`        |
| `eventId`                       | `id`                          |
| `eventTime`                     | `time`                        |
| `eventType`                     | `type`                        |
| `extensions.tenantId`           | `tenantid` (top-level)        |
| `extensions.userId`             | `userid` (top-level)          |
| `extensions.ownerId`            | `ownerid` (top-level)         |
| `extensions.spaceId`            | `spaceid` (top-level)         |

The `data` field containing the resource payload is unchanged in structure.

## Event type identifier changes \{#210-event-type-changes}

The `v1` version segment has been removed from most app lifecycle event type identifiers:

| Previous event type            | New event type              |
| ------------------------------ | --------------------------- |
| `com.qlik.v1.app.created`      | `com.qlik.app.created`      |
| `com.qlik.v1.app.deleted`      | `com.qlik.app.deleted`      |
| `com.qlik.v1.app.data.updated` | `com.qlik.app.data.updated` |
| `com.qlik.v1.app.exported`     | `com.qlik.app.exported`     |
| `com.qlik.v1.app.published`    | `com.qlik.app.published`    |

The `com.qlik.v1.app.reload.finished` event type identifier is unchanged.

Update any event subscriptions or filters that match on the `type` field to use the new identifiers.

For full API reference details, see the [Apps events API](https://qlik.dev/apis/event/apps/).
