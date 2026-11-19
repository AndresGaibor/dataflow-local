---
source: https://qlik.dev/apis/event/analytics/change-stores/
last_updated: 2026-09-25T18:11:55+02:00
---

# Change stores

Use change store events to react when users save changes to editable columns in write tables.

## Table of Contents

### system-events.analytics.change-store

- [com.qlik.analytics.change-store.changes.saved](#comqlikanalyticschange-storechangessaved)

## Events published on the `system-events.analytics.change-store` channel

### com.qlik.analytics.change-store.changes.saved

**Title:** Changes saved event for webhooks

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Changes have been saved.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | Unique identifier for the event. |
| `time` | `string` | No | Timestamp of when the event happened. Metadata: format = "date-time". |
| `type` | `string` | No | The event type Metadata: default = "com.qlik.analytics.change-store.changes.saved". |
| `source` | `string` | No | The source of the event. Metadata: default = "com.qlik/write-table". |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | No | Unique identifier for the tenant related to the event. |
| `specversion` | `string` | No | The event is compatible with the CloudEvents specification v1.0 Allowed values: 1.0. |
| `datacontenttype` | `string` | No | The content type of the event payload. Metadata: default = "application/json". |
| `data` | `object` | No | The data payload for changes saved event. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `ownerId` | `string` | No | The user that created the change-store. It is empty if the space is shared. |
| `spaceId` | `string` | No | The space that the change-store belongs to. It is empty if the space is personal. |
| `storeId` | `string` | No | The change-store unique identifier. |
| `tenantId` | `string` | No | The tenant where the change-store has been created. |
| `createdBy` | `string` | No | The user that saved the changes. |
| `committedAt` | `string` | No | The timestamp when the changes have been saved. Metadata: format = "date-time". |

</details>


**Example**

```json
{
  "id": "id123",
  "time": "2018-10-30T07:06:22Z",
  "type": "com.qlik.analytics.change-store.changes.saved",
  "source": "com.qlik/write-table",
  "userid": "id123",
  "tenantid": "id123",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "data": {
    "ownerId": "storeOwner1234",
    "spaceId": "space123",
    "storeId": "store012",
    "tenantId": "tenant123",
    "createdBy": "user345",
    "committedAt": "2024-01-01T12:20:00Z"
  }
}
```


## Schemas

### cloudEvents

CloudEvents schema v1.0

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | Unique identifier for the event. |
| `time` | `string` | No | Timestamp of when the event happened. Metadata: format = "date-time". |
| `type` | `string` | No | Content type |
| `source` | `string` | No | The source of the event. Metadata: default = "com.qlik/write-table". |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `tenantid` | `string` | No | Unique identifier for the tenant related to the event. |
| `specversion` | `string` | No | The event is compatible with the CloudEvents specification v1.0 Allowed values: 1.0. |
| `datacontenttype` | `string` | No | The content type of the event payload. Metadata: default = "application/json". |


