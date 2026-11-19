# Sharing tasks

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Sharing tasks define when scheduled reports, data alerts, subscriptions, and other tasks execute, and associate each task with its execution conditions.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/alerting/sharing-tasks/{taskId}/task-executions`](#get-apialertingsharing-taskstaskidtask-executions) | Returns the execution history of a sharing task. Executions that are in progress are not included. |
| `GET` | [`/api/alerting/sharing-tasks/{taskId}/task-executions/{taskExecutionId}`](#get-apialertingsharing-taskstaskidtask-executionstaskexecutionid) |  |

## API Reference

### GET /api/alerting/sharing-tasks/{taskId}/task-executions

Returns the execution history of a sharing task. Executions that are in progress are not included.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `taskId` | string | Yes | The sharing task identifier. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `filter` | string | No | The filter for finding entries. |
| `limit` | integer | No | The maximum number of entries to return. |
| `offset` | integer | No | The number of elements to skip for pagination. |
| `page` | string | No | The cursor to the page of data. |
| `sort` | string[] | No | Sort the returned result set by the specified field Enum: "status", "-status", "+status", "startedAt", "-startedAt", "+startedAt" |

#### Responses

##### 200

The task executions list has been successfully returned.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `totalCount` | integer | Yes | total count of entries in the collection as a whole |
| `currentPageCount` | integer | Yes | count of entries on the currently shown page |
| `data` | object[] | No | The list of task executions. |
| `links` | object | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The task execution ID. |
| `errors` | object[] | No | The errors that occurred during the task execution. |
| `status` | string | No | The status of the task execution. |
| `eventId` | string | No | The event ID. |
| `tenantId` | string | No | The tenant ID. |
| `createdBy` | string | No | The creator of the task, represented by user ID. |
| `startedAt` | string | No | The start timestamp. |
| `updatedAt` | string | No | The update timestamp. |
| `finishedAt` | string | No | The finish timestamp. |
| `triggerType` | string | No | The type of trigger. Enum: "manual", "onSchedule", "onReload" |
| `sharingTaskId` | string | No | The sharing task ID. |
| `eventTimestamp` | string | No | The event timestamp. |
| `recipientsCount` | integer | No | The number of recipients. |
| `templateMetadata` | object | No | A map of template metadata, where the key is the task template ID. |
| `failedReportCount` | integer | No | The number of failed reports. |
| `transportChannels` | string[] | No | A list of transport channels. Enum: "email", "sharepoint" |
| `successReportCount` | integer | No | The number of successful reports. |
| `recurrenceFrequency` | string | No | The 'FREQ' component of the RRULE at execution time, empty when triggered by a non-scheduled execution. Enum: "SECONDLY", "MINUTELY", "HOURLY", "DAILY", "WEEKLY", "MONTHLY", "YEARLY" |
| `cancelledReportCount` | integer | No | The number of cancelled reports. |
| `reportOnSharePointCount` | integer | No | The number of reports on SharePoint. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code. |
| `title` | string | No | The title of the error. |
| `detail` | string | No | The details about the error. |

</details>

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `next` | object | No |  |
| `prev` | object | No |  |
| `self` | object | No | Object with Href to a particular element or set of elements |

<details>
<summary>Properties of `next`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | URL to particular set of elements |
| `type` | string | No | Page type, can be next or prev Enum: "prev", "next" |
| `token` | string | No | Page unique token |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | URL to particular set of elements |
| `type` | string | No | Page type, can be next or prev Enum: "prev", "next" |
| `token` | string | No | Page unique token |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

</details>

##### 400

Bad request, malformed syntax or errors in parameters.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

</details>

##### 404

Resource does not exist.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

</details>

##### default

Error response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/alerting/sharing-tasks/{taskId}/task-executions` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/alerting/sharing-tasks/{taskId}/task-executions',
  {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    },
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for GET /api/alerting/sharing-tasks/{taskId}/task-executions yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/alerting/sharing-tasks/{taskId}/task-executions" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "totalCount": 42,
  "currentPageCount": 42,
  "data": [
    {
      "id": "string",
      "errors": [
        {
          "code": "string",
          "title": "string",
          "detail": "string"
        }
      ],
      "status": "string",
      "eventId": "string",
      "tenantId": "string",
      "createdBy": "string",
      "startedAt": "string",
      "updatedAt": "string",
      "finishedAt": "string",
      "triggerType": "manual",
      "sharingTaskId": "string",
      "eventTimestamp": "string",
      "recipientsCount": 42,
      "templateMetadata": {},
      "failedReportCount": 42,
      "transportChannels": [
        "email",
        "sharepoint"
      ],
      "successReportCount": 42,
      "recurrenceFrequency": "SECONDLY",
      "cancelledReportCount": 42,
      "reportOnSharePointCount": 42
    }
  ],
  "links": {
    "next": {
      "href": "http://localhost:8787/v1/items?limit=12",
      "type": "next",
      "token": "JwAAAAJfaWQAGQAAADVjZjUwM2NjMjVkYzlhMTM1MzYwZTVjZAAA"
    },
    "prev": {
      "href": "http://localhost:8787/v1/items?limit=12",
      "type": "next",
      "token": "JwAAAAJfaWQAGQAAADVjZjUwM2NjMjVkYzlhMTM1MzYwZTVjZAAA"
    },
    "self": {
      "href": "http://localhost:8787/v1/items/5da5825325dc9a0dd0260af9"
    }
  }
}
```

---

### GET /api/alerting/sharing-tasks/{taskId}/task-executions/{taskExecutionId}

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `taskExecutionId` | string | Yes | The task execution identifier. |
| `taskId` | string | Yes | The sharing task identifier. |

#### Responses

##### 200

The task execution has been successfully returned.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The task execution ID. |
| `errors` | object[] | No | The errors that occurred during the task execution. |
| `status` | string | No | The status of the task execution. |
| `eventId` | string | No | The event ID. |
| `tenantId` | string | No | The tenant ID. |
| `createdBy` | string | No | The creator of the task, represented by user ID. |
| `startedAt` | string | No | The start timestamp. |
| `updatedAt` | string | No | The update timestamp. |
| `finishedAt` | string | No | The finish timestamp. |
| `triggerType` | string | No | The type of trigger. Enum: "manual", "onSchedule", "onReload" |
| `sharingTaskId` | string | No | The sharing task ID. |
| `eventTimestamp` | string | No | The event timestamp. |
| `recipientsCount` | integer | No | The number of recipients. |
| `templateMetadata` | object | No | A map of template metadata, where the key is the task template ID. |
| `failedReportCount` | integer | No | The number of failed reports. |
| `transportChannels` | string[] | No | A list of transport channels. Enum: "email", "sharepoint" |
| `successReportCount` | integer | No | The number of successful reports. |
| `recurrenceFrequency` | string | No | The 'FREQ' component of the RRULE at execution time, empty when triggered by a non-scheduled execution. Enum: "SECONDLY", "MINUTELY", "HOURLY", "DAILY", "WEEKLY", "MONTHLY", "YEARLY" |
| `cancelledReportCount` | integer | No | The number of cancelled reports. |
| `reportOnSharePointCount` | integer | No | The number of reports on SharePoint. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code. |
| `title` | string | No | The title of the error. |
| `detail` | string | No | The details about the error. |

</details>

##### 400

Bad request, malformed syntax or errors in parameters.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

</details>

##### 404

Resource does not exist.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

</details>

##### default

Error response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Error code specific to sharing service. |
| `meta` | object | No |  |
| `title` | string | No | Error title. |
| `detail` | string | No | Error cause. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpCode` | integer | No | HTTP error code. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/alerting/sharing-tasks/{taskId}/task-executions/{taskExecutionId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/alerting/sharing-tasks/{taskId}/task-executions/{taskExecutionId}',
  {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    },
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for GET /api/alerting/sharing-tasks/{taskId}/task-executions/{taskExecutionId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/alerting/sharing-tasks/{taskId}/task-executions/{taskExecutionId}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "string",
  "errors": [
    {
      "code": "string",
      "title": "string",
      "detail": "string"
    }
  ],
  "status": "string",
  "eventId": "string",
  "tenantId": "string",
  "createdBy": "string",
  "startedAt": "string",
  "updatedAt": "string",
  "finishedAt": "string",
  "triggerType": "manual",
  "sharingTaskId": "string",
  "eventTimestamp": "string",
  "recipientsCount": 42,
  "templateMetadata": {},
  "failedReportCount": 42,
  "transportChannels": [
    "email",
    "sharepoint"
  ],
  "successReportCount": 42,
  "recurrenceFrequency": "SECONDLY",
  "cancelledReportCount": 42,
  "reportOnSharePointCount": 42
}
```

---
