---
source: https://qlik.dev/apis/event/di-projects/
last_updated: 2026-09-29T07:26:55Z
---

# Data integration projects

Monitor data integration pipeline task execution and track project events.

## Table of Contents

### system-events.di-projects.di-tasks

- [com.qlik.v1.di-projects.di-tasks.completed](#comqlikv1di-projectsdi-taskscompleted)
- [com.qlik.v1.di-projects.di-tasks.failed](#comqlikv1di-projectsdi-tasksfailed)
- [com.qlik.v1.di-projects.di-tasks.started](#comqlikv1di-projectsdi-tasksstarted)
- [com.qlik.v1.di-projects.di-tasks.stopped](#comqlikv1di-projectsdi-tasksstopped)

## Events published on the `system-events.di-projects.di-tasks` channel

### com.qlik.v1.di-projects.di-tasks.completed

**Title:** Data task completed

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Event published when a data task completes successfully

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Event type. Allowed values: com.qlik.v1.di-projects.di-tasks.completed. Metadata: default = "com.qlik.v1.di-projects.di-tasks.completed". |
| `source` | `string` | Yes | Event source. Metadata: default = "com.qlik/data-app-design". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the event payload. Metadata: default = "application/json". |
| `userid` | `string` | Yes | Unique identifier of the user related to the event. |
| `ownerid` | `string` | Yes | Unique identifier of the owner related to the event. |
| `spaceid` | `string` | Yes | Unique identifier of the space related to the event. |
| `authtype` | `string` | No | Type of authentication principal that triggered the occurrence. |
| `tenantid` | `string` | Yes | Unique identifier of the tenant related to the event. |
| `authclaims` | `string` | No | JSON string representing claims of the principal that triggered the event. |
| `extensions` | `object` | No | Legacy duplicate extension metadata also emitted by the current SuperEvent serializer. |
| `data` | `TaskCompletedDataPayload` | Yes | The event-specific data payload for a completed task. |
| `subject` | `string` | No | Subject of the event in the context of the event producer. |
| `dataschema` | `string` | No | URI to the schema for the data attribute. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `endTime` | `string` | Yes | Timestamp when the task ended. Metadata: format = "date-time". |
| `dataTask` | `DataTaskInfo` | Yes |  |
| `startTime` | `string` | Yes | Timestamp when the task started. Metadata: format = "date-time". |
| `startedBy` | `string` | Yes | Identifier of the user who started the task. |
| `startMethod` | `string` | No | Method by which the task was started Allowed values: USER \| SCHEDULER. |

<details>
<summary>Properties of `dataTask`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique identifier for the data task. |
| `name` | `string` | Yes | Name of the data task. |
| `type` | `string` | Yes | Type of the data task. Allowed values: LANDING \| STORAGE \| QVD_STORAGE \| TRANSFORM \| DATAMART \| REGISTERED_DATA \| REPLICATION \| LAKE_LANDING \| KNOWLEDGE_MART \| FILE_BASED_KNOWLEDGE_MART \| FILE_LANDING \| LAKEHOUSE_STORAGE \| LAKEHOUSE_MIRROR \| STREAMING_LAKE_LANDING \| STREAMING_TRANSFORM \| REPLICATE_LANDING. |
| `ownerId` | `string` | Yes | Identifier of the owner of the data task. |
| `spaceId` | `string` | Yes | Identifier of the space containing the data task. |
| `projectId` | `string` | Yes | Identifier of the project containing the data task. |
| `description` | `string` | No | Optional description of the data task. |

</details>

</details>


**Example**

```json
{
  "id": "8b6adb1b-d6dd-47bd-ab3d-17d231166ba7",
  "time": "2025-05-26T11:48:15.004Z",
  "type": "com.qlik.v1.di-projects.di-tasks.completed",
  "source": "com.qlik/data-app-design",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "6819cec4fb2b973f77b77383",
  "ownerid": "68064bc230525613f366b4f1",
  "spaceid": "68079b4004d7603de4991dcc",
  "authtype": "string",
  "tenantid": "dpmeH_c0vkwEzct90sXfcDSXBXRmRuU5",
  "authclaims": "string",
  "extensions": {},
  "data": {
    "endTime": "2025-05-26T11:47:17.893Z",
    "dataTask": {
      "id": "bad_storage-lbx4",
      "name": "Bad Storage",
      "type": "string",
      "ownerId": "68064bc230525613f366b4f1",
      "spaceId": "68079b4004d7603de4991dcc",
      "projectId": "68172bbc045ae3756c1ae309",
      "description": "this storage has bad connection"
    },
    "startTime": "2025-05-26T11:47:17.425Z",
    "startedBy": "6819cec4fb2b973f77b77383",
    "startMethod": "USER"
  },
  "subject": "some-subject",
  "dataschema": "https://example.com/schema"
}
```


### com.qlik.v1.di-projects.di-tasks.failed

**Title:** Data task failed

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Event published when a data task fails

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Event type. Allowed values: com.qlik.v1.di-projects.di-tasks.failed. Metadata: default = "com.qlik.v1.di-projects.di-tasks.failed". |
| `source` | `string` | Yes | Event source. Metadata: default = "com.qlik/data-app-design". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the event payload. Metadata: default = "application/json". |
| `userid` | `string` | Yes | Unique identifier of the user related to the event. |
| `ownerid` | `string` | Yes | Unique identifier of the owner related to the event. |
| `spaceid` | `string` | Yes | Unique identifier of the space related to the event. |
| `authtype` | `string` | No | Type of authentication principal that triggered the occurrence. |
| `tenantid` | `string` | Yes | Unique identifier of the tenant related to the event. |
| `authclaims` | `string` | No | JSON string representing claims of the principal that triggered the event. |
| `extensions` | `object` | No | Legacy duplicate extension metadata also emitted by the current SuperEvent serializer. |
| `data` | `TaskFailedDataPayload` | Yes | The event-specific data payload for a failed task. |
| `subject` | `string` | No | Subject of the event in the context of the event producer. |
| `dataschema` | `string` | No | URI to the schema for the data attribute. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `endTime` | `string` | Yes | Timestamp when the task ended (failed). Metadata: format = "date-time". |
| `dataTask` | `DataTaskInfo` | Yes |  |
| `startTime` | `string` | Yes | Timestamp when the task started. Metadata: format = "date-time". |
| `startedBy` | `string` | Yes | Identifier of the user who started the task. |
| `startMethod` | `string` | No | Method by which the task was started Allowed values: USER \| SCHEDULER. |
| `errorDetails` | `ErrorDetails` | Yes | Detailed information about an error. |
| `errorMessage` | `string` | Yes | Summary of the error. |

<details>
<summary>Properties of `dataTask`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique identifier for the data task. |
| `name` | `string` | Yes | Name of the data task. |
| `type` | `string` | Yes | Type of the data task. Allowed values: LANDING \| STORAGE \| QVD_STORAGE \| TRANSFORM \| DATAMART \| REGISTERED_DATA \| REPLICATION \| LAKE_LANDING \| KNOWLEDGE_MART \| FILE_BASED_KNOWLEDGE_MART \| FILE_LANDING \| LAKEHOUSE_STORAGE \| LAKEHOUSE_MIRROR \| STREAMING_LAKE_LANDING \| STREAMING_TRANSFORM \| REPLICATE_LANDING. |
| `ownerId` | `string` | Yes | Identifier of the owner of the data task. |
| `spaceId` | `string` | Yes | Identifier of the space containing the data task. |
| `projectId` | `string` | Yes | Identifier of the project containing the data task. |
| `description` | `string` | No | Optional description of the data task. |

</details>

<details>
<summary>Properties of `errorDetails`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Machine-readable code identifying the type of error. |
| `title` | `string` | Yes | Human-readable summary of the error. |
| `detail` | `string` | No | Additional detail about the error. |
| `source` | `string` | Yes | Source component or service that produced the error. |
| `status` | `integer` | Yes | HTTP status code associated with the error. |

</details>

</details>


**Example**

```json
{
  "id": "8b6adb1b-d6dd-47bd-ab3d-17d231166ba7",
  "time": "2025-05-26T11:48:15.004Z",
  "type": "com.qlik.v1.di-projects.di-tasks.failed",
  "source": "com.qlik/data-app-design",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "6819cec4fb2b973f77b77383",
  "ownerid": "68064bc230525613f366b4f1",
  "spaceid": "68079b4004d7603de4991dcc",
  "authtype": "string",
  "tenantid": "dpmeH_c0vkwEzct90sXfcDSXBXRmRuU5",
  "authclaims": "string",
  "extensions": {},
  "data": {
    "endTime": "2025-05-26T11:48:22.025Z",
    "dataTask": {
      "id": "bad_storage-lbx4",
      "name": "Bad Storage",
      "type": "string",
      "ownerId": "68064bc230525613f366b4f1",
      "spaceId": "68079b4004d7603de4991dcc",
      "projectId": "68172bbc045ae3756c1ae309",
      "description": "this storage has bad connection"
    },
    "startTime": "2025-05-26T11:48:14.890Z",
    "startedBy": "6819cec4fb2b973f77b77383",
    "startMethod": "USER",
    "errorDetails": {
      "code": "QDI-DW-STORAGE-TABLE-IN-BATCH-ERROR",
      "title": "The batch run failed due to one or more tables that failed to load",
      "detail": "The batch run failed due to one or more tables that failed to load.",
      "source": "com.qlik/qdi-app-manager",
      "status": 500
    },
    "errorMessage": "The following tables failed to load: 'Order Details, Customers, Orders, Employees, Products, Categories, Region, Territories, Suppliers, Shippers'"
  },
  "subject": "some-subject",
  "dataschema": "https://example.com/schema"
}
```


### com.qlik.v1.di-projects.di-tasks.started

**Title:** Data task started

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Event published when a data task starts

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Event type. Allowed values: com.qlik.v1.di-projects.di-tasks.started. Metadata: default = "com.qlik.v1.di-projects.di-tasks.started". |
| `source` | `string` | Yes | Event source. Metadata: default = "com.qlik/data-app-design". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the event payload. Metadata: default = "application/json". |
| `userid` | `string` | Yes | Unique identifier of the user related to the event. |
| `ownerid` | `string` | Yes | Unique identifier of the owner related to the event. |
| `spaceid` | `string` | Yes | Unique identifier of the space related to the event. |
| `authtype` | `string` | No | Type of authentication principal that triggered the occurrence. |
| `tenantid` | `string` | Yes | Unique identifier of the tenant related to the event. |
| `authclaims` | `string` | No | JSON string representing claims of the principal that triggered the event. |
| `extensions` | `object` | No | Legacy duplicate extension metadata also emitted by the current SuperEvent serializer. |
| `data` | `TaskStartedDataPayload` | Yes | The event-specific data payload for a started task. |
| `subject` | `string` | No | Subject of the event in the context of the event producer. |
| `dataschema` | `string` | No | URI to the schema for the data attribute. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `dataTask` | `DataTaskInfo` | Yes |  |
| `startTime` | `string` | Yes | Timestamp when the task started. Metadata: format = "date-time". |
| `startedBy` | `string` | Yes | Identifier of the user who started the task. |
| `startMethod` | `string` | No | Method by which the task was started Allowed values: USER \| SCHEDULER. |

<details>
<summary>Properties of `dataTask`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique identifier for the data task. |
| `name` | `string` | Yes | Name of the data task. |
| `type` | `string` | Yes | Type of the data task. Allowed values: LANDING \| STORAGE \| QVD_STORAGE \| TRANSFORM \| DATAMART \| REGISTERED_DATA \| REPLICATION \| LAKE_LANDING \| KNOWLEDGE_MART \| FILE_BASED_KNOWLEDGE_MART \| FILE_LANDING \| LAKEHOUSE_STORAGE \| LAKEHOUSE_MIRROR \| STREAMING_LAKE_LANDING \| STREAMING_TRANSFORM \| REPLICATE_LANDING. |
| `ownerId` | `string` | Yes | Identifier of the owner of the data task. |
| `spaceId` | `string` | Yes | Identifier of the space containing the data task. |
| `projectId` | `string` | Yes | Identifier of the project containing the data task. |
| `description` | `string` | No | Optional description of the data task. |

</details>

</details>


**Example**

```json
{
  "id": "8b6adb1b-d6dd-47bd-ab3d-17d231166ba7",
  "time": "2025-05-26T11:48:15.004Z",
  "type": "com.qlik.v1.di-projects.di-tasks.started",
  "source": "com.qlik/data-app-design",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "6819cec4fb2b973f77b77383",
  "ownerid": "68064bc230525613f366b4f1",
  "spaceid": "68079b4004d7603de4991dcc",
  "authtype": "string",
  "tenantid": "dpmeH_c0vkwEzct90sXfcDSXBXRmRuU5",
  "authclaims": "string",
  "extensions": {},
  "data": {
    "dataTask": {
      "id": "bad_storage-lbx4",
      "name": "Bad Storage",
      "type": "string",
      "ownerId": "68064bc230525613f366b4f1",
      "spaceId": "68079b4004d7603de4991dcc",
      "projectId": "68172bbc045ae3756c1ae309",
      "description": "this storage has bad connection"
    },
    "startTime": "2025-05-26T11:48:14.890Z",
    "startedBy": "6819cec4fb2b973f77b77383",
    "startMethod": "USER"
  },
  "subject": "some-subject",
  "dataschema": "https://example.com/schema"
}
```


### com.qlik.v1.di-projects.di-tasks.stopped

**Title:** Data task stopped

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Event published when a data task is stopped

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Event type. Allowed values: com.qlik.v1.di-projects.di-tasks.stopped. Metadata: default = "com.qlik.v1.di-projects.di-tasks.stopped". |
| `source` | `string` | Yes | Event source. Metadata: default = "com.qlik/data-app-design". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the event payload. Metadata: default = "application/json". |
| `userid` | `string` | Yes | Unique identifier of the user related to the event. |
| `ownerid` | `string` | Yes | Unique identifier of the owner related to the event. |
| `spaceid` | `string` | Yes | Unique identifier of the space related to the event. |
| `authtype` | `string` | No | Type of authentication principal that triggered the occurrence. |
| `tenantid` | `string` | Yes | Unique identifier of the tenant related to the event. |
| `authclaims` | `string` | No | JSON string representing claims of the principal that triggered the event. |
| `extensions` | `object` | No | Legacy duplicate extension metadata also emitted by the current SuperEvent serializer. |
| `data` | `TaskStoppedDataPayload` | Yes | The event-specific data payload for a stopped task. |
| `subject` | `string` | No | Subject of the event in the context of the event producer. |
| `dataschema` | `string` | No | URI to the schema for the data attribute. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `endTime` | `string` | Yes | Timestamp when the task was stopped. Metadata: format = "date-time". |
| `dataTask` | `DataTaskInfo` | Yes |  |
| `startTime` | `string` | Yes | Timestamp when the task was originally started. Metadata: format = "date-time". |
| `stoppedBy` | `string` | Yes | Identifier of the user who stopped the task. |
| `startMethod` | `string` | No | Method by which the task was started Allowed values: USER \| SCHEDULER. |

<details>
<summary>Properties of `dataTask`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique identifier for the data task. |
| `name` | `string` | Yes | Name of the data task. |
| `type` | `string` | Yes | Type of the data task. Allowed values: LANDING \| STORAGE \| QVD_STORAGE \| TRANSFORM \| DATAMART \| REGISTERED_DATA \| REPLICATION \| LAKE_LANDING \| KNOWLEDGE_MART \| FILE_BASED_KNOWLEDGE_MART \| FILE_LANDING \| LAKEHOUSE_STORAGE \| LAKEHOUSE_MIRROR \| STREAMING_LAKE_LANDING \| STREAMING_TRANSFORM \| REPLICATE_LANDING. |
| `ownerId` | `string` | Yes | Identifier of the owner of the data task. |
| `spaceId` | `string` | Yes | Identifier of the space containing the data task. |
| `projectId` | `string` | Yes | Identifier of the project containing the data task. |
| `description` | `string` | No | Optional description of the data task. |

</details>

</details>


**Example**

```json
{
  "id": "8b6adb1b-d6dd-47bd-ab3d-17d231166ba7",
  "time": "2025-05-26T11:48:15.004Z",
  "type": "com.qlik.v1.di-projects.di-tasks.stopped",
  "source": "com.qlik/data-app-design",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "6819cec4fb2b973f77b77383",
  "ownerid": "68064bc230525613f366b4f1",
  "spaceid": "68079b4004d7603de4991dcc",
  "authtype": "string",
  "tenantid": "dpmeH_c0vkwEzct90sXfcDSXBXRmRuU5",
  "authclaims": "string",
  "extensions": {},
  "data": {
    "endTime": "2025-05-26T11:49:59.000Z",
    "dataTask": {
      "id": "bad_storage-lbx4",
      "name": "Bad Storage",
      "type": "string",
      "ownerId": "68064bc230525613f366b4f1",
      "spaceId": "68079b4004d7603de4991dcc",
      "projectId": "68172bbc045ae3756c1ae309",
      "description": "this storage has bad connection"
    },
    "startTime": "2025-05-26T11:48:14.890Z",
    "stoppedBy": "6819cec4fb2b973f77b77383",
    "startMethod": "USER"
  },
  "subject": "some-subject",
  "dataschema": "https://example.com/schema"
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
| `type` | `string` | Yes | Describes the type of event related to the originating occurrence. Metadata: minLength = 1. |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |



### cloudEventsQlikExtensionsAttributes

Qlik-specific CloudEvents extension attributes.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `userid` | `string` | Yes | Unique identifier of the user related to the event. |
| `ownerid` | `string` | Yes | Unique identifier of the owner related to the event. |
| `spaceid` | `string` | Yes | Unique identifier of the space related to the event. |
| `authtype` | `string` | No | Type of authentication principal that triggered the occurrence. |
| `tenantid` | `string` | Yes | Unique identifier of the tenant related to the event. |
| `authclaims` | `string` | No | JSON string representing claims of the principal that triggered the event. |
| `extensions` | `object` | No | Legacy duplicate extension metadata also emitted by the current SuperEvent serializer. |



### DataTaskInfo

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique identifier for the data task. |
| `name` | `string` | Yes | Name of the data task. |
| `type` | `string` | Yes | Type of the data task. Allowed values: LANDING \| STORAGE \| QVD_STORAGE \| TRANSFORM \| DATAMART \| REGISTERED_DATA \| REPLICATION \| LAKE_LANDING \| KNOWLEDGE_MART \| FILE_BASED_KNOWLEDGE_MART \| FILE_LANDING \| LAKEHOUSE_STORAGE \| LAKEHOUSE_MIRROR \| STREAMING_LAKE_LANDING \| STREAMING_TRANSFORM \| REPLICATE_LANDING. |
| `ownerId` | `string` | Yes | Identifier of the owner of the data task. |
| `spaceId` | `string` | Yes | Identifier of the space containing the data task. |
| `projectId` | `string` | Yes | Identifier of the project containing the data task. |
| `description` | `string` | No | Optional description of the data task. |



### datatasktype

Type of the data task.

**Type:** `string`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `datatasktype` | `string` | No | Type of the data task. Allowed values: LANDING \| STORAGE \| QVD_STORAGE \| TRANSFORM \| DATAMART \| REGISTERED_DATA \| REPLICATION \| LAKE_LANDING \| KNOWLEDGE_MART \| FILE_BASED_KNOWLEDGE_MART \| FILE_LANDING \| LAKEHOUSE_STORAGE \| LAKEHOUSE_MIRROR \| STREAMING_LAKE_LANDING \| STREAMING_TRANSFORM \| REPLICATE_LANDING. |



### ErrorDetails

Detailed information about an error.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Machine-readable code identifying the type of error. |
| `title` | `string` | Yes | Human-readable summary of the error. |
| `detail` | `string` | No | Additional detail about the error. |
| `source` | `string` | Yes | Source component or service that produced the error. |
| `status` | `integer` | Yes | HTTP status code associated with the error. |



### StartMethod

Method by which the task was started

**Type:** `string`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `StartMethod` | `string` | No | Method by which the task was started Allowed values: USER \| SCHEDULER. |



### TaskCompletedDataPayload

Payload for data task completed event.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `endTime` | `string` | Yes | Timestamp when the task ended. Metadata: format = "date-time". |
| `dataTask` | `DataTaskInfo` | Yes |  |
| `startTime` | `string` | Yes | Timestamp when the task started. Metadata: format = "date-time". |
| `startedBy` | `string` | Yes | Identifier of the user who started the task. |
| `startMethod` | `string` | No | Method by which the task was started Allowed values: USER \| SCHEDULER. |

<details>
<summary>Properties of `dataTask`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique identifier for the data task. |
| `name` | `string` | Yes | Name of the data task. |
| `type` | `string` | Yes | Type of the data task. Allowed values: LANDING \| STORAGE \| QVD_STORAGE \| TRANSFORM \| DATAMART \| REGISTERED_DATA \| REPLICATION \| LAKE_LANDING \| KNOWLEDGE_MART \| FILE_BASED_KNOWLEDGE_MART \| FILE_LANDING \| LAKEHOUSE_STORAGE \| LAKEHOUSE_MIRROR \| STREAMING_LAKE_LANDING \| STREAMING_TRANSFORM \| REPLICATE_LANDING. |
| `ownerId` | `string` | Yes | Identifier of the owner of the data task. |
| `spaceId` | `string` | Yes | Identifier of the space containing the data task. |
| `projectId` | `string` | Yes | Identifier of the project containing the data task. |
| `description` | `string` | No | Optional description of the data task. |

</details>



### TaskFailedDataPayload

Payload for data task failed event.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `endTime` | `string` | Yes | Timestamp when the task ended (failed). Metadata: format = "date-time". |
| `dataTask` | `DataTaskInfo` | Yes |  |
| `startTime` | `string` | Yes | Timestamp when the task started. Metadata: format = "date-time". |
| `startedBy` | `string` | Yes | Identifier of the user who started the task. |
| `startMethod` | `string` | No | Method by which the task was started Allowed values: USER \| SCHEDULER. |
| `errorDetails` | `ErrorDetails` | Yes | Detailed information about an error. |
| `errorMessage` | `string` | Yes | Summary of the error. |

<details>
<summary>Properties of `dataTask`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique identifier for the data task. |
| `name` | `string` | Yes | Name of the data task. |
| `type` | `string` | Yes | Type of the data task. Allowed values: LANDING \| STORAGE \| QVD_STORAGE \| TRANSFORM \| DATAMART \| REGISTERED_DATA \| REPLICATION \| LAKE_LANDING \| KNOWLEDGE_MART \| FILE_BASED_KNOWLEDGE_MART \| FILE_LANDING \| LAKEHOUSE_STORAGE \| LAKEHOUSE_MIRROR \| STREAMING_LAKE_LANDING \| STREAMING_TRANSFORM \| REPLICATE_LANDING. |
| `ownerId` | `string` | Yes | Identifier of the owner of the data task. |
| `spaceId` | `string` | Yes | Identifier of the space containing the data task. |
| `projectId` | `string` | Yes | Identifier of the project containing the data task. |
| `description` | `string` | No | Optional description of the data task. |

</details>

<details>
<summary>Properties of `errorDetails`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Machine-readable code identifying the type of error. |
| `title` | `string` | Yes | Human-readable summary of the error. |
| `detail` | `string` | No | Additional detail about the error. |
| `source` | `string` | Yes | Source component or service that produced the error. |
| `status` | `integer` | Yes | HTTP status code associated with the error. |

</details>



### TaskStartedDataPayload

Payload for data task started event.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `dataTask` | `DataTaskInfo` | Yes |  |
| `startTime` | `string` | Yes | Timestamp when the task started. Metadata: format = "date-time". |
| `startedBy` | `string` | Yes | Identifier of the user who started the task. |
| `startMethod` | `string` | No | Method by which the task was started Allowed values: USER \| SCHEDULER. |

<details>
<summary>Properties of `dataTask`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique identifier for the data task. |
| `name` | `string` | Yes | Name of the data task. |
| `type` | `string` | Yes | Type of the data task. Allowed values: LANDING \| STORAGE \| QVD_STORAGE \| TRANSFORM \| DATAMART \| REGISTERED_DATA \| REPLICATION \| LAKE_LANDING \| KNOWLEDGE_MART \| FILE_BASED_KNOWLEDGE_MART \| FILE_LANDING \| LAKEHOUSE_STORAGE \| LAKEHOUSE_MIRROR \| STREAMING_LAKE_LANDING \| STREAMING_TRANSFORM \| REPLICATE_LANDING. |
| `ownerId` | `string` | Yes | Identifier of the owner of the data task. |
| `spaceId` | `string` | Yes | Identifier of the space containing the data task. |
| `projectId` | `string` | Yes | Identifier of the project containing the data task. |
| `description` | `string` | No | Optional description of the data task. |

</details>



### TaskStoppedDataPayload

Payload for data task stopped event.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `endTime` | `string` | Yes | Timestamp when the task was stopped. Metadata: format = "date-time". |
| `dataTask` | `DataTaskInfo` | Yes |  |
| `startTime` | `string` | Yes | Timestamp when the task was originally started. Metadata: format = "date-time". |
| `stoppedBy` | `string` | Yes | Identifier of the user who stopped the task. |
| `startMethod` | `string` | No | Method by which the task was started Allowed values: USER \| SCHEDULER. |

<details>
<summary>Properties of `dataTask`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Unique identifier for the data task. |
| `name` | `string` | Yes | Name of the data task. |
| `type` | `string` | Yes | Type of the data task. Allowed values: LANDING \| STORAGE \| QVD_STORAGE \| TRANSFORM \| DATAMART \| REGISTERED_DATA \| REPLICATION \| LAKE_LANDING \| KNOWLEDGE_MART \| FILE_BASED_KNOWLEDGE_MART \| FILE_LANDING \| LAKEHOUSE_STORAGE \| LAKEHOUSE_MIRROR \| STREAMING_LAKE_LANDING \| STREAMING_TRANSFORM \| REPLICATE_LANDING. |
| `ownerId` | `string` | Yes | Identifier of the owner of the data task. |
| `spaceId` | `string` | Yes | Identifier of the space containing the data task. |
| `projectId` | `string` | Yes | Identifier of the project containing the data task. |
| `description` | `string` | No | Optional description of the data task. |

</details>


