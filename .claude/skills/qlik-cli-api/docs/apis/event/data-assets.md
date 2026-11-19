---
source: https://qlik.dev/apis/event/data-assets/
last_updated: 2026-10-19T15:45:25+02:00
---

# Data assets

## Table of Contents

### system-events.data-asset.data

- [com.qlik.v1.data-asset.data.change-processing.progressed](#comqlikv1data-assetdatachange-processingprogressed)

## Events published on the `system-events.data-asset.data` channel

### com.qlik.v1.data-asset.data.change-processing.progressed

**Title:** Data asset change processing batch progressed

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a data asset change processing batch makes progress, before the batch finishes.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Data asset change processing batch progressed. Metadata: default = "com.qlik.v1.data-asset.data.change-processing.progressed". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1, default = "application/json". |
| `userid` | `string` | No | Unique identifier for the user related to the event. |
| `updates` | `object[]` | No | Updates of qemServer object |
| `authtype` | `string` | No | Representing the type of principal that triggered the occurrence. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `authclaims` | `string` | No | A JSON string representing claims of the principal that triggered the event |
| `tracestate` | `string` | No | A comma-delimited list of key-value pairs. |
| `traceparent` | `string` | No | Contains a version, trace ID, span ID, and trace options. |
| `toplevelresourceid` | `string` | No | Unique identifier referring to integration application related to the event. |
| `data` | `dataAssetChangeProcessingProgressedObject` | No |  |

<details>
<summary>Properties of `updates`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `path` | `string` | No | updated item path |
| `newvalue` | `string` | No | new value at given path |
| `oldvalue` | `string` | No | original value at given path |

</details>

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | `string` | No | Unique identifier for the app related to the event. Metadata: format = "uid". |
| `dataSets` | `object[]` | No |  |
| `consumption` | `changeProcessingConsumptionObject` | No |  |
| `dataAssetId` | `string` | No | Unique identifier for the data asset related to the event. |
| `dataAssetType` | `string` | No | Type of the data asset the change processing batch belongs to (e.g. STORAGE). |
| `notChargeable` | `boolean` | No | When this field is set to true the event should be discarded from consumption metrics. |
| `sourceDataProvider` | `string` | No | Identifies the source system that produced the data (one of STITCH, REPLICATE, QCDI, OTHER). |
| `notChargeableReason` | `string` | No | Description for why the event is set to notChargeable. |
| `changeProcessingEndedAt` | `string` | No | Timestamp of when the change processing batch ended. Must adhere to RFC 3339. Metadata: format = "date-time". |
| `changeProcessingStartedAt` | `string` | No | Timestamp of when the change processing batch started. Must adhere to RFC 3339. Metadata: format = "date-time". |
| `dataAssetChangeCountersDelta` | `changeProcessingOperationsObject` | No |  |

<details>
<summary>Properties of `dataSets`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `dataSetId` | `string` | No | Unique identifier for the data set related to the item. |
| `updateEndedAt` | `string` | No | Timestamp of when the change processing update for the data set ended. Must adhere to RFC 3339. Metadata: format = "date-time". |
| `updateSuccess` | `boolean` | No | Indicates whether the change processing update for this data set succeeded. |
| `updateStartedAt` | `string` | No | Timestamp of when the change processing update for the data set started. Must adhere to RFC 3339. Metadata: format = "date-time". |
| `dataSetSecureQRI` | `string` | No | Secure QRI (Qlik resource identifier) of the data set related to the item. It identifies the data set's underlying resource without exposing connection details. |
| `recordOperationCounters` | `changeProcessingOperationsObject` | No |  |

<details>
<summary>Properties of `recordOperationCounters`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `consumption`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `totalBytes` | `number` | No | Harmonized total bytes property, same value as totalBytesProcessed. |
| `totalBytesProcessed` | `number` | No | Total bytes in a specific change processing operation. |

</details>

<details>
<summary>Properties of `dataAssetChangeCountersDelta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `numberOfDeletes` | `number` | No | Number of rows deletions in the specific change processing batch. |
| `numberOfInserts` | `number` | No | Number of rows inserts in the specific change processing batch. |
| `numberOfUpdates` | `number` | No | Number of rows updates in the specific change processing batch. |

</details>

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2018-10-30T07:06:22Z",
  "type": "com.qlik.v1.data-asset.data.change-processing.progressed",
  "source": "com.qlik/my-service",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "id123",
  "updates": [
    {}
  ],
  "authtype": "string",
  "tenantid": "id123",
  "authclaims": "string",
  "tracestate": "string",
  "traceparent": "string",
  "toplevelresourceid": "id123",
  "data": {
    "appId": "id123",
    "dataSets": [
      {
        "dataSetId": "id123",
        "updateEndedAt": "2018-10-30T07:06:22Z",
        "updateSuccess": true,
        "updateStartedAt": "2018-10-30T07:06:22Z",
        "dataSetSecureQRI": "qri:db:snowflake://Bh__CEOO2-D2Ty2f5egzjobOWnrxe6Cl8hHjJ6G08KE#w7OWgEHpy-iUi4EVNEGGQ6bJwU3FT6RdX38hbbrpJlM",
        "recordOperationCounters": {
          "numberOfDeletes": 30,
          "numberOfInserts": 10,
          "numberOfUpdates": 20
        }
      }
    ],
    "consumption": {
      "totalBytes": 30000,
      "totalBytesProcessed": 30000
    },
    "dataAssetId": "id123",
    "dataAssetType": "STORAGE",
    "notChargeable": false,
    "sourceDataProvider": "STITCH",
    "notChargeableReason": "Transform to QCS",
    "changeProcessingEndedAt": "2018-10-30T07:06:22Z",
    "changeProcessingStartedAt": "2018-10-30T07:06:22Z",
    "dataAssetChangeCountersDelta": {
      "numberOfDeletes": 30,
      "numberOfInserts": 10,
      "numberOfUpdates": 20
    }
  }
}
```


## Schemas

### changeProcessingConsumptionObject

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `totalBytes` | `number` | No | Harmonized total bytes property, same value as totalBytesProcessed. |
| `totalBytesProcessed` | `number` | No | Total bytes in a specific change processing operation. |



### changeProcessingOperationsObject

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `numberOfDeletes` | `number` | No | Number of rows deletions in the specific change processing batch. |
| `numberOfInserts` | `number` | No | Number of rows inserts in the specific change processing batch. |
| `numberOfUpdates` | `number` | No | Number of rows updates in the specific change processing batch. |



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
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1, default = "application/json". |



### cloudEventsQlikExtensionsAttributes

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `userid` | `string` | No | Unique identifier for the user related to the event. |
| `updates` | `object[]` | No | Updates of qemServer object |
| `authtype` | `string` | No | Representing the type of principal that triggered the occurrence. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `authclaims` | `string` | No | A JSON string representing claims of the principal that triggered the event |
| `tracestate` | `string` | No | A comma-delimited list of key-value pairs. |
| `traceparent` | `string` | No | Contains a version, trace ID, span ID, and trace options. |
| `toplevelresourceid` | `string` | No | Unique identifier referring to integration application related to the event. |

<details>
<summary>Properties of `updates`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `path` | `string` | No | updated item path |
| `newvalue` | `string` | No | new value at given path |
| `oldvalue` | `string` | No | original value at given path |

</details>



### dataAssetChangeProcessingProgressedObject

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | `string` | No | Unique identifier for the app related to the event. Metadata: format = "uid". |
| `dataSets` | `object[]` | No |  |
| `consumption` | `changeProcessingConsumptionObject` | No |  |
| `dataAssetId` | `string` | No | Unique identifier for the data asset related to the event. |
| `dataAssetType` | `string` | No | Type of the data asset the change processing batch belongs to (e.g. STORAGE). |
| `notChargeable` | `boolean` | No | When this field is set to true the event should be discarded from consumption metrics. |
| `sourceDataProvider` | `string` | No | Identifies the source system that produced the data (one of STITCH, REPLICATE, QCDI, OTHER). |
| `notChargeableReason` | `string` | No | Description for why the event is set to notChargeable. |
| `changeProcessingEndedAt` | `string` | No | Timestamp of when the change processing batch ended. Must adhere to RFC 3339. Metadata: format = "date-time". |
| `changeProcessingStartedAt` | `string` | No | Timestamp of when the change processing batch started. Must adhere to RFC 3339. Metadata: format = "date-time". |
| `dataAssetChangeCountersDelta` | `changeProcessingOperationsObject` | No |  |

<details>
<summary>Properties of `dataSets`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `dataSetId` | `string` | No | Unique identifier for the data set related to the item. |
| `updateEndedAt` | `string` | No | Timestamp of when the change processing update for the data set ended. Must adhere to RFC 3339. Metadata: format = "date-time". |
| `updateSuccess` | `boolean` | No | Indicates whether the change processing update for this data set succeeded. |
| `updateStartedAt` | `string` | No | Timestamp of when the change processing update for the data set started. Must adhere to RFC 3339. Metadata: format = "date-time". |
| `dataSetSecureQRI` | `string` | No | Secure QRI (Qlik resource identifier) of the data set related to the item. It identifies the data set's underlying resource without exposing connection details. |
| `recordOperationCounters` | `changeProcessingOperationsObject` | No |  |

<details>
<summary>Properties of `recordOperationCounters`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `numberOfDeletes` | `number` | No | Number of rows deletions in the specific change processing batch. |
| `numberOfInserts` | `number` | No | Number of rows inserts in the specific change processing batch. |
| `numberOfUpdates` | `number` | No | Number of rows updates in the specific change processing batch. |

</details>

</details>

<details>
<summary>Properties of `consumption`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `totalBytes` | `number` | No | Harmonized total bytes property, same value as totalBytesProcessed. |
| `totalBytesProcessed` | `number` | No | Total bytes in a specific change processing operation. |

</details>

<details>
<summary>Properties of `dataAssetChangeCountersDelta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `numberOfDeletes` | `number` | No | Number of rows deletions in the specific change processing batch. |
| `numberOfInserts` | `number` | No | Number of rows inserts in the specific change processing batch. |
| `numberOfUpdates` | `number` | No | Number of rows updates in the specific change processing batch. |

</details>



### dataSetChangeProcessingObject

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `dataSetId` | `string` | No | Unique identifier for the data set related to the item. |
| `updateEndedAt` | `string` | No | Timestamp of when the change processing update for the data set ended. Must adhere to RFC 3339. Metadata: format = "date-time". |
| `updateSuccess` | `boolean` | No | Indicates whether the change processing update for this data set succeeded. |
| `updateStartedAt` | `string` | No | Timestamp of when the change processing update for the data set started. Must adhere to RFC 3339. Metadata: format = "date-time". |
| `dataSetSecureQRI` | `string` | No | Secure QRI (Qlik resource identifier) of the data set related to the item. It identifies the data set's underlying resource without exposing connection details. |
| `recordOperationCounters` | `changeProcessingOperationsObject` | No |  |

<details>
<summary>Properties of `recordOperationCounters`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `numberOfDeletes` | `number` | No | Number of rows deletions in the specific change processing batch. |
| `numberOfInserts` | `number` | No | Number of rows inserts in the specific change processing batch. |
| `numberOfUpdates` | `number` | No | Number of rows updates in the specific change processing batch. |

</details>



### updateItem

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `path` | `string` | No | updated item path |
| `newvalue` | `string` | No | new value at given path |
| `oldvalue` | `string` | No | original value at given path |


