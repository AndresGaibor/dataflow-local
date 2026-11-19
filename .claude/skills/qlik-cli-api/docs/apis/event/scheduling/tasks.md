---
source: https://qlik.dev/apis/event/scheduling/tasks/
last_updated: 2026-10-14T18:08:44+02:00
---

# Tasks

## Table of Contents

### system-events.task

- [com.qlik.scheduling.task.created](#comqlikschedulingtaskcreated)
- [com.qlik.scheduling.task.deleted](#comqlikschedulingtaskdeleted)
- [com.qlik.scheduling.task.updated](#comqlikschedulingtaskupdated)

## Events published on the `system-events.task` channel

### com.qlik.scheduling.task.created

**Title:** Task created

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a new task is created. The event includes the task ID, owner, associated resource, and the scheduled action.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | The specific event type for this message. Allowed values: com.qlik.scheduling.task.created. Metadata: default = "com.qlik.scheduling.task.created". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1, default = "application/json". |
| `userid` | `string` | No | Unique identifier of the user related to the event. |
| `ownerid` | `string` | No | Unique identifier of the task owner. Falls back to the task creator when no distinct owner is set. |
| `tenantid` | `string` | No | Unique identifier of the tenant related to the event. |
| `toplevelresourceid` | `string` | No | Identifier of the top-level resource that triggered the event. |
| `data` | `taskEntryObject` | No | Represents the full state of a task resource at the time the event was published. All lifecycle events carry this object as their `data` payload, capturing the task's configuration, ownership, and execution status. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The unique identifier of the task. |
| `name` | `string` | Yes | The name of the task. |
| `_meta` | `taskMetadata` | No | Internal task metadata, emitted as-is. Not part of the stable public contract for other properties in this document; fields may be added. |
| `usage` | `string` | No | The product domain in which the associated resource is used. Always present on the wire; empty when not specified (the product treats a missing value as `ANALYTICS`, but this event does not apply that default itself). Allowed values:  \| ANALYTICS \| DATA_PREPARATION \| DATAFLOW_PREP \| SINGLE_TABLE_PREP. |
| `action` | `string` | Yes | The action performed on the target resource. |
| `status` | `string` | No | The outcome of the operation this event reports, not a run's final status specifically. Set by the publisher for every event type, not only `task.run.finished`. Allowed values: SUCCEEDED \| FAILED \| ABORTED. |
| `enabled` | `boolean` | No | Whether the task is enabled. When `true`, the task is active and eligible to run. |
| `ownerId` | `string` | Yes | The unique identifier of the user that owns the task. Only applicable for user-level tasks. |
| `spaceId` | `string` | No | The unique identifier of the space the task operates in. |
| `createdAt` | `string` | No | The UTC timestamp when the task was created. Always present; carries the zero timestamp `0001-01-01T00:00:00Z` when the task has no recorded creation time. Metadata: format = "date-time". |
| `createdBy` | `string` | Yes | The unique identifier of the user that created the task. |
| `updatedAt` | `string` | No | The UTC timestamp when the task was last updated. Always present; carries the zero timestamp `0001-01-01T00:00:00Z` when the task has no recorded update time. Metadata: format = "date-time". |
| `resourceId` | `string` | Yes | The unique identifier of the target resource associated with the task's action. |
| `description` | `string` | No | A user-provided description of the task. |
| `actionParams` | `object` | No | The parameters for the action, as an object of arbitrary JSON-valued properties (strings, numbers, booleans, nested objects/arrays, or null). Metadata: additionalProperties = true. |
| `disabledCode` | `string` | No | The reason the task was disabled. Always present; empty when the task is not disabled. Allowed values:  \| MANUALLY \| CONSECUTIVE-FAILURES \| APP-SCRIPT-UPDATED \| OWNER-DELETED \| OWNER-DISABLED. |
| `migratedFrom` | `string` | No | The identifier of the original reload task from which this task was migrated. Empty if the task was not migrated. |
| `resourceType` | `string` | Yes | The type of resource the task operates on. Allowed values: app. |
| `statusDetails` | `string` | No | Additional details about the final status, such as the failure reason, automation ID, or reload ID. |

<details>
<summary>Properties of `_meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `usage` | `string` | No | The product domain in which the resource is used. |
| `ownerId` | `string` | No | The user ID of the task owner. |
| `spaceId` | `string` | No | The unique identifier of the space the task operates in. |
| `trigger` | `taskMetadataTrigger` | No |  |
| `tenantId` | `string` | No | The unique identifier of the tenant the task operates in. |
| `topology` | `taskMetadataTopology` | No | Indicates the task's position in a dependency graph. |
| `createdAt` | `string` | No | The UTC timestamp when the task was created. Metadata: format = "date-time". |
| `createdBy` | `string` | No | The user ID of the user who created the task. |
| `deletedAt` | `string` | No | The UTC timestamp when the task was deleted. Metadata: format = "date-time". |
| `spaceType` | `string` | No | The type of space the task operates in. |
| `updatedAt` | `string` | No | The UTC timestamp when the task was last updated. Metadata: format = "date-time". |
| `disabledCode` | `string` | No | The reason the task is currently disabled. |
| `migratedFrom` | `string` | No | The unique identifier of the legacy reload task this task was migrated from, if applicable. |
| `resourceName` | `string` | No | The name of the resource on which the task was created. |
| `resourceType` | `string` | No | The type of resource on which the task was created. |
| `orchestration` | `taskMetadataOrchestration` | No |  |
| `scriptOwnerId` | `string` | No | The user ID of the owner whose script context is used when running the task. |
| `resourceSubType` | `string` | No | The subtype of resource on which the task was created. |

<details>
<summary>Properties of `trigger`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `topology`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `orchestration`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2018-10-30T07:06:22Z",
  "type": "com.qlik.scheduling.task.created",
  "source": "com.qlik/choreographer",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "ad378d54-3e97-47c0-bc57-cd84dbb93fa2",
  "ownerid": "22222222-2222-2222-2222-222222222222",
  "tenantid": "103359ca-3579-4125-a0dc-d19531b53186",
  "toplevelresourceid": "11111111-1111-1111-1111-111111111111",
  "data": {
    "id": "00000000-0000-0000-0000-000000000000",
    "name": "My task",
    "_meta": {
      "usage": "string",
      "ownerId": "string",
      "spaceId": "string",
      "trigger": {
        "id": "string",
        "type": 42
      },
      "tenantId": "string",
      "topology": {
        "isChild": true,
        "isParent": true
      },
      "createdAt": "2018-10-30T07:06:22Z",
      "createdBy": "string",
      "deletedAt": "2018-10-30T07:06:22Z",
      "spaceType": "string",
      "updatedAt": "2018-10-30T07:06:22Z",
      "disabledCode": "string",
      "migratedFrom": "string",
      "resourceName": "string",
      "resourceType": "string",
      "orchestration": {
        "id": "string",
        "type": 42,
        "attrs": {},
        "lastRun": {
          "id": "string",
          "status": "string",
          "endedAt": "2018-10-30T07:06:22Z",
          "workerId": "string",
          "startedAt": "2018-10-30T07:06:22Z",
          "executedAs": "string",
          "workerType": "string",
          "triggeredBy": "string"
        }
      },
      "scriptOwnerId": "string",
      "resourceSubType": "string"
    },
    "usage": "",
    "action": "string",
    "status": "SUCCEEDED",
    "enabled": true,
    "ownerId": "00000000-0000-0000-0000-000000000000",
    "spaceId": "string",
    "createdAt": "2018-10-30T07:06:22Z",
    "createdBy": "00000000-0000-0000-0000-000000000000",
    "updatedAt": "2018-10-30T07:06:22Z",
    "resourceId": "string",
    "description": "This is my task",
    "actionParams": {},
    "disabledCode": "",
    "migratedFrom": "string",
    "resourceType": "app",
    "statusDetails": "string"
  }
}
```


### com.qlik.scheduling.task.deleted

**Title:** Task deleted

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a task is deleted. The event includes the task state at the time of deletion, including the task ID and owner.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | The specific event type for this message. Allowed values: com.qlik.scheduling.task.deleted. Metadata: default = "com.qlik.scheduling.task.deleted". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1, default = "application/json". |
| `userid` | `string` | No | Unique identifier of the user related to the event. |
| `ownerid` | `string` | No | Unique identifier of the task owner. Falls back to the task creator when no distinct owner is set. |
| `tenantid` | `string` | No | Unique identifier of the tenant related to the event. |
| `toplevelresourceid` | `string` | No | Identifier of the top-level resource that triggered the event. |
| `data` | `taskEntryObject` | No | Represents the full state of a task resource at the time the event was published. All lifecycle events carry this object as their `data` payload, capturing the task's configuration, ownership, and execution status. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The unique identifier of the task. |
| `name` | `string` | Yes | The name of the task. |
| `_meta` | `taskMetadata` | No | Internal task metadata, emitted as-is. Not part of the stable public contract for other properties in this document; fields may be added. |
| `usage` | `string` | No | The product domain in which the associated resource is used. Always present on the wire; empty when not specified (the product treats a missing value as `ANALYTICS`, but this event does not apply that default itself). Allowed values:  \| ANALYTICS \| DATA_PREPARATION \| DATAFLOW_PREP \| SINGLE_TABLE_PREP. |
| `action` | `string` | Yes | The action performed on the target resource. |
| `status` | `string` | No | The outcome of the operation this event reports, not a run's final status specifically. Set by the publisher for every event type, not only `task.run.finished`. Allowed values: SUCCEEDED \| FAILED \| ABORTED. |
| `enabled` | `boolean` | No | Whether the task is enabled. When `true`, the task is active and eligible to run. |
| `ownerId` | `string` | Yes | The unique identifier of the user that owns the task. Only applicable for user-level tasks. |
| `spaceId` | `string` | No | The unique identifier of the space the task operates in. |
| `createdAt` | `string` | No | The UTC timestamp when the task was created. Always present; carries the zero timestamp `0001-01-01T00:00:00Z` when the task has no recorded creation time. Metadata: format = "date-time". |
| `createdBy` | `string` | Yes | The unique identifier of the user that created the task. |
| `updatedAt` | `string` | No | The UTC timestamp when the task was last updated. Always present; carries the zero timestamp `0001-01-01T00:00:00Z` when the task has no recorded update time. Metadata: format = "date-time". |
| `resourceId` | `string` | Yes | The unique identifier of the target resource associated with the task's action. |
| `description` | `string` | No | A user-provided description of the task. |
| `actionParams` | `object` | No | The parameters for the action, as an object of arbitrary JSON-valued properties (strings, numbers, booleans, nested objects/arrays, or null). Metadata: additionalProperties = true. |
| `disabledCode` | `string` | No | The reason the task was disabled. Always present; empty when the task is not disabled. Allowed values:  \| MANUALLY \| CONSECUTIVE-FAILURES \| APP-SCRIPT-UPDATED \| OWNER-DELETED \| OWNER-DISABLED. |
| `migratedFrom` | `string` | No | The identifier of the original reload task from which this task was migrated. Empty if the task was not migrated. |
| `resourceType` | `string` | Yes | The type of resource the task operates on. Allowed values: app. |
| `statusDetails` | `string` | No | Additional details about the final status, such as the failure reason, automation ID, or reload ID. |

<details>
<summary>Properties of `_meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `usage` | `string` | No | The product domain in which the resource is used. |
| `ownerId` | `string` | No | The user ID of the task owner. |
| `spaceId` | `string` | No | The unique identifier of the space the task operates in. |
| `trigger` | `taskMetadataTrigger` | No |  |
| `tenantId` | `string` | No | The unique identifier of the tenant the task operates in. |
| `topology` | `taskMetadataTopology` | No | Indicates the task's position in a dependency graph. |
| `createdAt` | `string` | No | The UTC timestamp when the task was created. Metadata: format = "date-time". |
| `createdBy` | `string` | No | The user ID of the user who created the task. |
| `deletedAt` | `string` | No | The UTC timestamp when the task was deleted. Metadata: format = "date-time". |
| `spaceType` | `string` | No | The type of space the task operates in. |
| `updatedAt` | `string` | No | The UTC timestamp when the task was last updated. Metadata: format = "date-time". |
| `disabledCode` | `string` | No | The reason the task is currently disabled. |
| `migratedFrom` | `string` | No | The unique identifier of the legacy reload task this task was migrated from, if applicable. |
| `resourceName` | `string` | No | The name of the resource on which the task was created. |
| `resourceType` | `string` | No | The type of resource on which the task was created. |
| `orchestration` | `taskMetadataOrchestration` | No |  |
| `scriptOwnerId` | `string` | No | The user ID of the owner whose script context is used when running the task. |
| `resourceSubType` | `string` | No | The subtype of resource on which the task was created. |

<details>
<summary>Properties of `trigger`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `topology`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `orchestration`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2018-10-30T07:06:22Z",
  "type": "com.qlik.scheduling.task.deleted",
  "source": "com.qlik/choreographer",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "ad378d54-3e97-47c0-bc57-cd84dbb93fa2",
  "ownerid": "22222222-2222-2222-2222-222222222222",
  "tenantid": "103359ca-3579-4125-a0dc-d19531b53186",
  "toplevelresourceid": "11111111-1111-1111-1111-111111111111",
  "data": {
    "id": "00000000-0000-0000-0000-000000000000",
    "name": "My task",
    "_meta": {
      "usage": "string",
      "ownerId": "string",
      "spaceId": "string",
      "trigger": {
        "id": "string",
        "type": 42
      },
      "tenantId": "string",
      "topology": {
        "isChild": true,
        "isParent": true
      },
      "createdAt": "2018-10-30T07:06:22Z",
      "createdBy": "string",
      "deletedAt": "2018-10-30T07:06:22Z",
      "spaceType": "string",
      "updatedAt": "2018-10-30T07:06:22Z",
      "disabledCode": "string",
      "migratedFrom": "string",
      "resourceName": "string",
      "resourceType": "string",
      "orchestration": {
        "id": "string",
        "type": 42,
        "attrs": {},
        "lastRun": {
          "id": "string",
          "status": "string",
          "endedAt": "2018-10-30T07:06:22Z",
          "workerId": "string",
          "startedAt": "2018-10-30T07:06:22Z",
          "executedAs": "string",
          "workerType": "string",
          "triggeredBy": "string"
        }
      },
      "scriptOwnerId": "string",
      "resourceSubType": "string"
    },
    "usage": "",
    "action": "string",
    "status": "SUCCEEDED",
    "enabled": true,
    "ownerId": "00000000-0000-0000-0000-000000000000",
    "spaceId": "string",
    "createdAt": "2018-10-30T07:06:22Z",
    "createdBy": "00000000-0000-0000-0000-000000000000",
    "updatedAt": "2018-10-30T07:06:22Z",
    "resourceId": "string",
    "description": "This is my task",
    "actionParams": {},
    "disabledCode": "",
    "migratedFrom": "string",
    "resourceType": "app",
    "statusDetails": "string"
  }
}
```


### com.qlik.scheduling.task.updated

**Title:** Task updated

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a task's configuration or properties are updated. The event includes the updated task state along with a list of changed fields in `_updates`, identifying what was modified and the old and new values. Use this to detect configuration drift or audit changes to scheduled tasks.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | The specific event type for this message. Allowed values: com.qlik.scheduling.task.updated. Metadata: default = "com.qlik.scheduling.task.updated". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1, default = "application/json". |
| `userid` | `string` | No | Unique identifier of the user related to the event. |
| `ownerid` | `string` | No | Unique identifier of the task owner. Falls back to the task creator when no distinct owner is set. |
| `tenantid` | `string` | No | Unique identifier of the tenant related to the event. |
| `toplevelresourceid` | `string` | No | Identifier of the top-level resource that triggered the event. |
| `data` | `taskEntryObject` | No | Represents the full state of a task resource at the time the event was published. All lifecycle events carry this object as their `data` payload, capturing the task's configuration, ownership, and execution status. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The unique identifier of the task. |
| `name` | `string` | Yes | The name of the task. |
| `_meta` | `taskMetadata` | No | Internal task metadata, emitted as-is. Not part of the stable public contract for other properties in this document; fields may be added. |
| `usage` | `string` | No | The product domain in which the associated resource is used. Always present on the wire; empty when not specified (the product treats a missing value as `ANALYTICS`, but this event does not apply that default itself). Allowed values:  \| ANALYTICS \| DATA_PREPARATION \| DATAFLOW_PREP \| SINGLE_TABLE_PREP. |
| `action` | `string` | Yes | The action performed on the target resource. |
| `status` | `string` | No | The outcome of the operation this event reports, not a run's final status specifically. Set by the publisher for every event type, not only `task.run.finished`. Allowed values: SUCCEEDED \| FAILED \| ABORTED. |
| `enabled` | `boolean` | No | Whether the task is enabled. When `true`, the task is active and eligible to run. |
| `ownerId` | `string` | Yes | The unique identifier of the user that owns the task. Only applicable for user-level tasks. |
| `spaceId` | `string` | No | The unique identifier of the space the task operates in. |
| `createdAt` | `string` | No | The UTC timestamp when the task was created. Always present; carries the zero timestamp `0001-01-01T00:00:00Z` when the task has no recorded creation time. Metadata: format = "date-time". |
| `createdBy` | `string` | Yes | The unique identifier of the user that created the task. |
| `updatedAt` | `string` | No | The UTC timestamp when the task was last updated. Always present; carries the zero timestamp `0001-01-01T00:00:00Z` when the task has no recorded update time. Metadata: format = "date-time". |
| `resourceId` | `string` | Yes | The unique identifier of the target resource associated with the task's action. |
| `description` | `string` | No | A user-provided description of the task. |
| `actionParams` | `object` | No | The parameters for the action, as an object of arbitrary JSON-valued properties (strings, numbers, booleans, nested objects/arrays, or null). Metadata: additionalProperties = true. |
| `disabledCode` | `string` | No | The reason the task was disabled. Always present; empty when the task is not disabled. Allowed values:  \| MANUALLY \| CONSECUTIVE-FAILURES \| APP-SCRIPT-UPDATED \| OWNER-DELETED \| OWNER-DISABLED. |
| `migratedFrom` | `string` | No | The identifier of the original reload task from which this task was migrated. Empty if the task was not migrated. |
| `resourceType` | `string` | Yes | The type of resource the task operates on. Allowed values: app. |
| `statusDetails` | `string` | No | Additional details about the final status, such as the failure reason, automation ID, or reload ID. |
| `_updates` | `object[]` | No | The list of fields updated in this task, with the old and new values for each changed field. |

<details>
<summary>Properties of `_meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `usage` | `string` | No | The product domain in which the resource is used. |
| `ownerId` | `string` | No | The user ID of the task owner. |
| `spaceId` | `string` | No | The unique identifier of the space the task operates in. |
| `trigger` | `taskMetadataTrigger` | No |  |
| `tenantId` | `string` | No | The unique identifier of the tenant the task operates in. |
| `topology` | `taskMetadataTopology` | No | Indicates the task's position in a dependency graph. |
| `createdAt` | `string` | No | The UTC timestamp when the task was created. Metadata: format = "date-time". |
| `createdBy` | `string` | No | The user ID of the user who created the task. |
| `deletedAt` | `string` | No | The UTC timestamp when the task was deleted. Metadata: format = "date-time". |
| `spaceType` | `string` | No | The type of space the task operates in. |
| `updatedAt` | `string` | No | The UTC timestamp when the task was last updated. Metadata: format = "date-time". |
| `disabledCode` | `string` | No | The reason the task is currently disabled. |
| `migratedFrom` | `string` | No | The unique identifier of the legacy reload task this task was migrated from, if applicable. |
| `resourceName` | `string` | No | The name of the resource on which the task was created. |
| `resourceType` | `string` | No | The type of resource on which the task was created. |
| `orchestration` | `taskMetadataOrchestration` | No |  |
| `scriptOwnerId` | `string` | No | The user ID of the owner whose script context is used when running the task. |
| `resourceSubType` | `string` | No | The subtype of resource on which the task was created. |

<details>
<summary>Properties of `trigger`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `topology`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `orchestration`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `_updates`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `path` | `string` | No | The name of the top-level task field that changed, as produced by a JSON merge-patch diff between the previous and updated task. Not a JSON Pointer or a recursive path expression. |
| `newValue` | `` | No | The new value of the field after the update. Any JSON value, including null. |
| `oldValue` | `` | No | The previous value of the field before the update. Any JSON value, including null. |

</details>

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2018-10-30T07:06:22Z",
  "type": "com.qlik.scheduling.task.updated",
  "source": "com.qlik/choreographer",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "ad378d54-3e97-47c0-bc57-cd84dbb93fa2",
  "ownerid": "22222222-2222-2222-2222-222222222222",
  "tenantid": "103359ca-3579-4125-a0dc-d19531b53186",
  "toplevelresourceid": "11111111-1111-1111-1111-111111111111",
  "data": {
    "id": "00000000-0000-0000-0000-000000000000",
    "name": "My task",
    "_meta": {
      "usage": "string",
      "ownerId": "string",
      "spaceId": "string",
      "trigger": {
        "id": "string",
        "type": 42
      },
      "tenantId": "string",
      "topology": {
        "isChild": true,
        "isParent": true
      },
      "createdAt": "2018-10-30T07:06:22Z",
      "createdBy": "string",
      "deletedAt": "2018-10-30T07:06:22Z",
      "spaceType": "string",
      "updatedAt": "2018-10-30T07:06:22Z",
      "disabledCode": "string",
      "migratedFrom": "string",
      "resourceName": "string",
      "resourceType": "string",
      "orchestration": {
        "id": "string",
        "type": 42,
        "attrs": {},
        "lastRun": {
          "id": "string",
          "status": "string",
          "endedAt": "2018-10-30T07:06:22Z",
          "workerId": "string",
          "startedAt": "2018-10-30T07:06:22Z",
          "executedAs": "string",
          "workerType": "string",
          "triggeredBy": "string"
        }
      },
      "scriptOwnerId": "string",
      "resourceSubType": "string"
    },
    "usage": "",
    "action": "string",
    "status": "SUCCEEDED",
    "enabled": true,
    "ownerId": "00000000-0000-0000-0000-000000000000",
    "spaceId": "string",
    "createdAt": "2018-10-30T07:06:22Z",
    "createdBy": "00000000-0000-0000-0000-000000000000",
    "updatedAt": "2018-10-30T07:06:22Z",
    "resourceId": "string",
    "description": "This is my task",
    "actionParams": {},
    "disabledCode": "",
    "migratedFrom": "string",
    "resourceType": "app",
    "statusDetails": "string",
    "_updates": [
      {
        "path": "string"
      }
    ]
  }
}
```


## Schemas

### cloudEventsContextAttributes

CloudEvents Specification JSON Schema

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Classifies the kind of event (for example, a task being created). Shared by every occurrence of that event type; it does not identify this specific occurrence — `id` does that. Metadata: minLength = 1. |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1, default = "application/json". |



### cloudEventsQlikExtensionsAttributes

Additional event metadata.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `userid` | `string` | No | Unique identifier of the user related to the event. |
| `ownerid` | `string` | No | Unique identifier of the task owner. Falls back to the task creator when no distinct owner is set. |
| `tenantid` | `string` | No | Unique identifier of the tenant related to the event. |
| `toplevelresourceid` | `string` | No | Identifier of the top-level resource that triggered the event. |



### taskEntryObject

Represents the full state of a task resource at the time the event was published. All lifecycle events carry this object as their `data` payload, capturing the task's configuration, ownership, and execution status.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The unique identifier of the task. |
| `name` | `string` | Yes | The name of the task. |
| `_meta` | `taskMetadata` | No | Internal task metadata, emitted as-is. Not part of the stable public contract for other properties in this document; fields may be added. |
| `usage` | `string` | No | The product domain in which the associated resource is used. Always present on the wire; empty when not specified (the product treats a missing value as `ANALYTICS`, but this event does not apply that default itself). Allowed values:  \| ANALYTICS \| DATA_PREPARATION \| DATAFLOW_PREP \| SINGLE_TABLE_PREP. |
| `action` | `string` | Yes | The action performed on the target resource. |
| `status` | `string` | No | The outcome of the operation this event reports, not a run's final status specifically. Set by the publisher for every event type, not only `task.run.finished`. Allowed values: SUCCEEDED \| FAILED \| ABORTED. |
| `enabled` | `boolean` | No | Whether the task is enabled. When `true`, the task is active and eligible to run. |
| `ownerId` | `string` | Yes | The unique identifier of the user that owns the task. Only applicable for user-level tasks. |
| `spaceId` | `string` | No | The unique identifier of the space the task operates in. |
| `createdAt` | `string` | No | The UTC timestamp when the task was created. Always present; carries the zero timestamp `0001-01-01T00:00:00Z` when the task has no recorded creation time. Metadata: format = "date-time". |
| `createdBy` | `string` | Yes | The unique identifier of the user that created the task. |
| `updatedAt` | `string` | No | The UTC timestamp when the task was last updated. Always present; carries the zero timestamp `0001-01-01T00:00:00Z` when the task has no recorded update time. Metadata: format = "date-time". |
| `resourceId` | `string` | Yes | The unique identifier of the target resource associated with the task's action. |
| `description` | `string` | No | A user-provided description of the task. |
| `actionParams` | `object` | No | The parameters for the action, as an object of arbitrary JSON-valued properties (strings, numbers, booleans, nested objects/arrays, or null). Metadata: additionalProperties = true. |
| `disabledCode` | `string` | No | The reason the task was disabled. Always present; empty when the task is not disabled. Allowed values:  \| MANUALLY \| CONSECUTIVE-FAILURES \| APP-SCRIPT-UPDATED \| OWNER-DELETED \| OWNER-DISABLED. |
| `migratedFrom` | `string` | No | The identifier of the original reload task from which this task was migrated. Empty if the task was not migrated. |
| `resourceType` | `string` | Yes | The type of resource the task operates on. Allowed values: app. |
| `statusDetails` | `string` | No | Additional details about the final status, such as the failure reason, automation ID, or reload ID. |

<details>
<summary>Properties of `_meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `usage` | `string` | No | The product domain in which the resource is used. |
| `ownerId` | `string` | No | The user ID of the task owner. |
| `spaceId` | `string` | No | The unique identifier of the space the task operates in. |
| `trigger` | `taskMetadataTrigger` | No |  |
| `tenantId` | `string` | No | The unique identifier of the tenant the task operates in. |
| `topology` | `taskMetadataTopology` | No | Indicates the task's position in a dependency graph. |
| `createdAt` | `string` | No | The UTC timestamp when the task was created. Metadata: format = "date-time". |
| `createdBy` | `string` | No | The user ID of the user who created the task. |
| `deletedAt` | `string` | No | The UTC timestamp when the task was deleted. Metadata: format = "date-time". |
| `spaceType` | `string` | No | The type of space the task operates in. |
| `updatedAt` | `string` | No | The UTC timestamp when the task was last updated. Metadata: format = "date-time". |
| `disabledCode` | `string` | No | The reason the task is currently disabled. |
| `migratedFrom` | `string` | No | The unique identifier of the legacy reload task this task was migrated from, if applicable. |
| `resourceName` | `string` | No | The name of the resource on which the task was created. |
| `resourceType` | `string` | No | The type of resource on which the task was created. |
| `orchestration` | `taskMetadataOrchestration` | No |  |
| `scriptOwnerId` | `string` | No | The user ID of the owner whose script context is used when running the task. |
| `resourceSubType` | `string` | No | The subtype of resource on which the task was created. |

<details>
<summary>Properties of `trigger`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | The unique identifier of the trigger associated with this task. |
| `type` | `integer` | No | The type identifier of the trigger associated with this task. |

</details>

<details>
<summary>Properties of `topology`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `isChild` | `boolean` | No | When `true`, this task is triggered by one or more parent tasks. |
| `isParent` | `boolean` | No | When `true`, this task has one or more downstream dependent tasks. |

</details>

<details>
<summary>Properties of `orchestration`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | The unique identifier of the orchestration instance associated with this task in the scheduling service. |
| `type` | `integer` | No | The type identifier of the orchestration system handling this task. |
| `attrs` | `object` | No | Additional attributes of the orchestration instance associated with this task in the scheduling service. |
| `lastRun` | `taskMetadataOrchestrationLastRun` | No |  |

<details>
<summary>Properties of `lastRun`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>



### taskMetadata

Internal task metadata, emitted as-is. Not part of the stable public contract for other properties in this document; fields may be added.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `usage` | `string` | No | The product domain in which the resource is used. |
| `ownerId` | `string` | No | The user ID of the task owner. |
| `spaceId` | `string` | No | The unique identifier of the space the task operates in. |
| `trigger` | `taskMetadataTrigger` | No |  |
| `tenantId` | `string` | No | The unique identifier of the tenant the task operates in. |
| `topology` | `taskMetadataTopology` | No | Indicates the task's position in a dependency graph. |
| `createdAt` | `string` | No | The UTC timestamp when the task was created. Metadata: format = "date-time". |
| `createdBy` | `string` | No | The user ID of the user who created the task. |
| `deletedAt` | `string` | No | The UTC timestamp when the task was deleted. Metadata: format = "date-time". |
| `spaceType` | `string` | No | The type of space the task operates in. |
| `updatedAt` | `string` | No | The UTC timestamp when the task was last updated. Metadata: format = "date-time". |
| `disabledCode` | `string` | No | The reason the task is currently disabled. |
| `migratedFrom` | `string` | No | The unique identifier of the legacy reload task this task was migrated from, if applicable. |
| `resourceName` | `string` | No | The name of the resource on which the task was created. |
| `resourceType` | `string` | No | The type of resource on which the task was created. |
| `orchestration` | `taskMetadataOrchestration` | No |  |
| `scriptOwnerId` | `string` | No | The user ID of the owner whose script context is used when running the task. |
| `resourceSubType` | `string` | No | The subtype of resource on which the task was created. |

<details>
<summary>Properties of `trigger`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | The unique identifier of the trigger associated with this task. |
| `type` | `integer` | No | The type identifier of the trigger associated with this task. |

</details>

<details>
<summary>Properties of `topology`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `isChild` | `boolean` | No | When `true`, this task is triggered by one or more parent tasks. |
| `isParent` | `boolean` | No | When `true`, this task has one or more downstream dependent tasks. |

</details>

<details>
<summary>Properties of `orchestration`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | The unique identifier of the orchestration instance associated with this task in the scheduling service. |
| `type` | `integer` | No | The type identifier of the orchestration system handling this task. |
| `attrs` | `object` | No | Additional attributes of the orchestration instance associated with this task in the scheduling service. |
| `lastRun` | `taskMetadataOrchestrationLastRun` | No |  |

<details>
<summary>Properties of `lastRun`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | The unique identifier of the task run. |
| `status` | `string` | No | The current status of the task run. |
| `endedAt` | `string` | No | The UTC timestamp when the task run ended. Metadata: format = "date-time". |
| `workerId` | `string` | No | The unique identifier of the worker that executed the job. |
| `startedAt` | `string` | No | The UTC timestamp when the task run started. Metadata: format = "date-time". |
| `executedAs` | `string` | No | The user ID of the user on whose behalf the task was executed. |
| `workerType` | `string` | No | The type or name of the target system that executed the run. |
| `triggeredBy` | `string` | No | The identity or event that triggered the task run. |

</details>

</details>



### taskMetadataOrchestration

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | The unique identifier of the orchestration instance associated with this task in the scheduling service. |
| `type` | `integer` | No | The type identifier of the orchestration system handling this task. |
| `attrs` | `object` | No | Additional attributes of the orchestration instance associated with this task in the scheduling service. |
| `lastRun` | `taskMetadataOrchestrationLastRun` | No |  |

<details>
<summary>Properties of `lastRun`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | The unique identifier of the task run. |
| `status` | `string` | No | The current status of the task run. |
| `endedAt` | `string` | No | The UTC timestamp when the task run ended. Metadata: format = "date-time". |
| `workerId` | `string` | No | The unique identifier of the worker that executed the job. |
| `startedAt` | `string` | No | The UTC timestamp when the task run started. Metadata: format = "date-time". |
| `executedAs` | `string` | No | The user ID of the user on whose behalf the task was executed. |
| `workerType` | `string` | No | The type or name of the target system that executed the run. |
| `triggeredBy` | `string` | No | The identity or event that triggered the task run. |

</details>



### taskMetadataOrchestrationLastRun

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | The unique identifier of the task run. |
| `status` | `string` | No | The current status of the task run. |
| `endedAt` | `string` | No | The UTC timestamp when the task run ended. Metadata: format = "date-time". |
| `workerId` | `string` | No | The unique identifier of the worker that executed the job. |
| `startedAt` | `string` | No | The UTC timestamp when the task run started. Metadata: format = "date-time". |
| `executedAs` | `string` | No | The user ID of the user on whose behalf the task was executed. |
| `workerType` | `string` | No | The type or name of the target system that executed the run. |
| `triggeredBy` | `string` | No | The identity or event that triggered the task run. |



### taskMetadataTopology

Indicates the task's position in a dependency graph.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `isChild` | `boolean` | No | When `true`, this task is triggered by one or more parent tasks. |
| `isParent` | `boolean` | No | When `true`, this task has one or more downstream dependent tasks. |



### taskMetadataTrigger

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No | The unique identifier of the trigger associated with this task. |
| `type` | `integer` | No | The type identifier of the trigger associated with this task. |


