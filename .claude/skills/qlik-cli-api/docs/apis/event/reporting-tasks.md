---
source: https://qlik.dev/apis/event/reporting-tasks/
last_updated: 2026-11-12T18:22:49+01:00
---

# Reporting tasks

Events emitted for scheduled report generation and delivery tasks.

## Table of Contents

### system-events.sharing

- [com.qlik.reporting-task.summary.created](#comqlikreporting-tasksummarycreated)

## Events published on the `system-events.sharing` channel

### com.qlik.reporting-task.summary.created

**Title:** Reporting task summary created

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a summary is generated for a reporting task execution. Includes task metadata and execution statistics. Use this to track reporting outcomes.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | The unique identifier for the event type. Metadata: default = "com.qlik.reporting-task.summary.created". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | The unique identifier for the user triggering the event. |
| `authtype` | `string` | No | The type of principal that triggered the occurrence. |
| `tenantid` | `string` | Yes | The unique identifier for the tenant related to the event. |
| `authclaims` | `string` | No | A JSON string representing claims of the principal that triggered the event. |
| `tracestate` | `string` | No | A comma-delimited list of key-value pairs. |
| `traceparent` | `string` | No | Contains a version, trace ID, span ID, and trace options. |
| `data` | `reportingTaskSummaryCreatedData` | No | Contains the event-specific attributes of the payload. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The identifier of the reporting task. Has the same value as `resourceId`. |
| `name` | `string` | Yes | The name of the reporting task. |
| `appId` | `string` | Yes | The identifier of the app. |
| `error` | `string` | No | Currently empty for reporting task events. |
| `expiry` | `string` | No | The expiration date. |
| `status` | `string` | Yes | The status of the reporting task. This does not necessarily represent the outcome of an individual execution. |
| `enabled` | `boolean` | Yes | Indicates whether the reporting task is enabled, both by the user and by the system. |
| `ownerId` | `string` | Yes | The identifier of the reporting task owner. |
| `spaceId` | `string` | No | The identifier of the space. |
| `traceId` | `string` | No | The identifier used for tracing the reporting task summary event. |
| `creatorId` | `string` | Yes | The identifier of the user who created the reporting task. |
| `thumbnail` | `string` | Yes | The link to the thumbnail image. |
| `resourceId` | `string` | Yes | The resource identifier of the reporting task. |
| `transports` | `array` | Yes | The transport channels of the reporting task, for example `email` and `sharepoint`. When `hassectionaccess` is true, `sharepoint` is omitted from this list. Use `distributionchannels` for the channels as configured on the task. |
| `workflowId` | `string` | Yes | Currently empty for reporting task events. |
| `createdDate` | `string` | Yes | The date when the reporting task was created. |
| `description` | `string` | Yes | The description of the reporting task. |
| `insightLink` | `string` | Yes | An insight link to open the app from the email. |
| `typeOfSpace` | `string` | No | The type of space. |
| `resourceLink` | `string` | Yes | Currently empty for reporting task events. |
| `resourceType` | `string` | Yes | The resource type of the reporting task. |
| `sharingTaskType` | `string` | Yes | The type of sharing task. |
| `hassectionaccess` | `boolean` | Yes | Whether the associated app has section access enabled. |
| `sharingTaskOwnerId` | `string` | Yes | The identifier of the sharing task owner. |
| `distributionchannels` | `array` | Yes | The transport channels as configured on the reporting task, for example `email` and `sharepoint`. Unlike `transports`, this list still includes `sharepoint` when `hassectionaccess` is true. |
| `sharingTaskExecutionId` | `string` | No | The identifier of the sharing task execution, which covers the whole run of the reporting task. In `reporting-task.executed`, several events can carry the same value, for example one for each recipient or filter group execution. |
| `reportingServiceEventId` | `string` | Yes | The identifier of the reporting service event, when available. |
| `failedReports` | `integer` | Yes | The count of reports that failed to generate. |
| `taskExecutionId` | `string` | Yes | The identifier of the reporting task execution this summary pertains to. |
| `failedExecutions` | `integer` | Yes | The count of failed executions for the reporting task. |
| `successfulReports` | `integer` | Yes | The count of successfully generated reports. |
| `emailRecipientsCount` | `integer` | No | The total count of sharing email recipients. |
| `successfulExecutions` | `integer` | Yes | The count of successful executions for the reporting task. |
| `emailRecipientEnabledExternalCount` | `integer` | No | The count of external enabled sharing email recipients. |
| `emailRecipientEnabledInternalCount` | `integer` | No | The count of internal enabled sharing email recipients. |
| `emailRecipientDisabledExternalCount` | `integer` | No | The count of external disabled sharing email recipients. |
| `emailRecipientDisabledInternalCount` | `integer` | No | The count of internal disabled sharing email recipients. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2025-01-15T10:43:17Z",
  "type": "com.qlik.reporting-task.summary.created",
  "source": "com.qlik/my-service",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "authtype": "User",
  "tenantid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "authclaims": "{\n  \"sub\": \"VZhiEfgW2bLd7HgR-jjzAh6VnicipweT\",\n  \"email\": \"user@example.com\",\n  \"roles\": [\"admin\", \"editor\"]\n}\n",
  "tracestate": "rojo=00f067aa0ba902b7,congo=t61rcWkgMzE",
  "traceparent": "00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01",
  "data": {
    "id": "64b6d2e7a9f211331271421e",
    "name": "test",
    "appId": "9c6b39c8-4624-4b2c-8c7b-bb91b919a421",
    "error": "string",
    "expiry": "",
    "status": "VALID",
    "enabled": true,
    "ownerId": "63f622472ef44d955d3442a2",
    "spaceId": "63f622472ef44d955d3442a2",
    "traceId": "64b6d2e7a9f211331271421e",
    "creatorId": "63f622472ef44d955d3442a2",
    "thumbnail": "/api/v1/sharing-tasks/64b6d2e7a9f211331271421e/executions/latest/files/",
    "resourceId": "64b6d2e7a9f211331271421e",
    "transports": [
      "email"
    ],
    "workflowId": "string",
    "createdDate": "2023-07-18T17:59:03Z",
    "description": "Weekly sales report for the EMEA region",
    "insightLink": "string",
    "typeOfSpace": "managed",
    "resourceLink": "string",
    "resourceType": "reporting-task",
    "sharingTaskType": "template-sharing",
    "hassectionaccess": true,
    "sharingTaskOwnerId": "63f622472ef44d955d3442a2",
    "distributionchannels": [
      "email",
      "sharepoint"
    ],
    "sharingTaskExecutionId": "64b6d2e7a9f211331271421e",
    "reportingServiceEventId": "64b6d2e7a9f211331271421e",
    "failedReports": 0,
    "taskExecutionId": "64b6d2e7a9f211331271421e",
    "failedExecutions": 0,
    "successfulReports": 1,
    "emailRecipientsCount": 1,
    "successfulExecutions": 1,
    "emailRecipientEnabledExternalCount": 1,
    "emailRecipientEnabledInternalCount": 1,
    "emailRecipientDisabledExternalCount": 0,
    "emailRecipientDisabledInternalCount": 0
  }
}
```


## Schemas

### cloudEventsContextAttributes

CloudEvents Specification JSON Schema.

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

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `userid` | `string` | No | The unique identifier for the user triggering the event. |
| `authtype` | `string` | No | The type of principal that triggered the occurrence. |
| `tenantid` | `string` | Yes | The unique identifier for the tenant related to the event. |
| `authclaims` | `string` | No | A JSON string representing claims of the principal that triggered the event. |
| `tracestate` | `string` | No | A comma-delimited list of key-value pairs. |
| `traceparent` | `string` | No | Contains a version, trace ID, span ID, and trace options. |



### reportingTaskExecutedData

Contains the event-specific attributes of the payload.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The identifier of the reporting task. Has the same value as `resourceId`. |
| `name` | `string` | Yes | The name of the reporting task. |
| `appId` | `string` | Yes | The identifier of the app. |
| `error` | `string` | No | Currently empty for reporting task events. |
| `expiry` | `string` | No | The expiration date. |
| `status` | `string` | Yes | The status of the reporting task. This does not necessarily represent the outcome of an individual execution. |
| `enabled` | `boolean` | Yes | Indicates whether the reporting task is enabled, both by the user and by the system. |
| `ownerId` | `string` | Yes | The identifier of the reporting task owner. |
| `spaceId` | `string` | No | The identifier of the space. |
| `traceId` | `string` | No | The identifier used to trace the reporting task execution processing. |
| `creatorId` | `string` | Yes | The identifier of the user who created the reporting task. |
| `thumbnail` | `string` | Yes | The link to the thumbnail image. |
| `resourceId` | `string` | Yes | The resource identifier of the reporting task. |
| `transports` | `array` | Yes | The transport channels of the reporting task, for example `email` and `sharepoint`. When `hassectionaccess` is true, `sharepoint` is omitted from this list. Use `distributionchannels` for the channels as configured on the task. |
| `workflowId` | `string` | Yes | Currently empty for reporting task events. |
| `createdDate` | `string` | Yes | The date when the reporting task was created. |
| `description` | `string` | Yes | The description of the reporting task. |
| `insightLink` | `string` | Yes | An insight link to open the app from the email. |
| `typeOfSpace` | `string` | No | The type of space. |
| `resourceLink` | `string` | Yes | Currently empty for reporting task events. |
| `resourceType` | `string` | Yes | The resource type of the reporting task. |
| `sharingTaskType` | `string` | Yes | The type of sharing task. |
| `hassectionaccess` | `boolean` | Yes | Whether the associated app has section access enabled. |
| `sharingTaskOwnerId` | `string` | Yes | The identifier of the sharing task owner. |
| `distributionchannels` | `array` | Yes | The transport channels as configured on the reporting task, for example `email` and `sharepoint`. Unlike `transports`, this list still includes `sharepoint` when `hassectionaccess` is true. |
| `sharingTaskExecutionId` | `string` | No | The identifier of the sharing task execution, which covers the whole run of the reporting task. In `reporting-task.executed`, several events can carry the same value, for example one for each recipient or filter group execution. |
| `reportingServiceEventId` | `string` | Yes | The identifier of the reporting service event, when available. |



### reportingTaskSummaryCreatedData

Contains the event-specific attributes of the payload.

**Type:** `reportingTaskExecutedData`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The identifier of the reporting task. Has the same value as `resourceId`. |
| `name` | `string` | Yes | The name of the reporting task. |
| `appId` | `string` | Yes | The identifier of the app. |
| `error` | `string` | No | Currently empty for reporting task events. |
| `expiry` | `string` | No | The expiration date. |
| `status` | `string` | Yes | The status of the reporting task. This does not necessarily represent the outcome of an individual execution. |
| `enabled` | `boolean` | Yes | Indicates whether the reporting task is enabled, both by the user and by the system. |
| `ownerId` | `string` | Yes | The identifier of the reporting task owner. |
| `spaceId` | `string` | No | The identifier of the space. |
| `traceId` | `string` | No | The identifier used for tracing the reporting task summary event. |
| `creatorId` | `string` | Yes | The identifier of the user who created the reporting task. |
| `thumbnail` | `string` | Yes | The link to the thumbnail image. |
| `resourceId` | `string` | Yes | The resource identifier of the reporting task. |
| `transports` | `array` | Yes | The transport channels of the reporting task, for example `email` and `sharepoint`. When `hassectionaccess` is true, `sharepoint` is omitted from this list. Use `distributionchannels` for the channels as configured on the task. |
| `workflowId` | `string` | Yes | Currently empty for reporting task events. |
| `createdDate` | `string` | Yes | The date when the reporting task was created. |
| `description` | `string` | Yes | The description of the reporting task. |
| `insightLink` | `string` | Yes | An insight link to open the app from the email. |
| `typeOfSpace` | `string` | No | The type of space. |
| `resourceLink` | `string` | Yes | Currently empty for reporting task events. |
| `resourceType` | `string` | Yes | The resource type of the reporting task. |
| `sharingTaskType` | `string` | Yes | The type of sharing task. |
| `hassectionaccess` | `boolean` | Yes | Whether the associated app has section access enabled. |
| `sharingTaskOwnerId` | `string` | Yes | The identifier of the sharing task owner. |
| `distributionchannels` | `array` | Yes | The transport channels as configured on the reporting task, for example `email` and `sharepoint`. Unlike `transports`, this list still includes `sharepoint` when `hassectionaccess` is true. |
| `sharingTaskExecutionId` | `string` | No | The identifier of the sharing task execution, which covers the whole run of the reporting task. In `reporting-task.executed`, several events can carry the same value, for example one for each recipient or filter group execution. |
| `reportingServiceEventId` | `string` | Yes | The identifier of the reporting service event, when available. |
| `failedReports` | `integer` | Yes | The count of reports that failed to generate. |
| `taskExecutionId` | `string` | Yes | The identifier of the reporting task execution this summary pertains to. |
| `failedExecutions` | `integer` | Yes | The count of failed executions for the reporting task. |
| `successfulReports` | `integer` | Yes | The count of successfully generated reports. |
| `emailRecipientsCount` | `integer` | No | The total count of sharing email recipients. |
| `successfulExecutions` | `integer` | Yes | The count of successful executions for the reporting task. |
| `emailRecipientEnabledExternalCount` | `integer` | No | The count of external enabled sharing email recipients. |
| `emailRecipientEnabledInternalCount` | `integer` | No | The count of internal enabled sharing email recipients. |
| `emailRecipientDisabledExternalCount` | `integer` | No | The count of external disabled sharing email recipients. |
| `emailRecipientDisabledInternalCount` | `integer` | No | The count of internal disabled sharing email recipients. |


