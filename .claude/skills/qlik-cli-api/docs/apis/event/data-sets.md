---
source: https://qlik.dev/apis/event/data-sets/
last_updated: 2026-10-19T15:45:25+02:00
---

# Data sets

## Table of Contents

### system-events.data-asset.data

- [com.qlik.v1.data-set.data.load.finished](#comqlikv1data-setdataloadfinished)

## Events published on the `system-events.data-asset.data` channel

### com.qlik.v1.data-set.data.load.finished

**Title:** Data set load finished

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a data set load operation finishes, whether it succeeded or failed.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Data set load operation finished. Metadata: default = "com.qlik.v1.data-set.data.load.finished". |
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
| `data` | `datasetLoadFinishedObject` | No |  |

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
| `dataSetId` | `string` | No | Unique identifier for the data set related to the event. |
| `firstLoad` | `boolean` | No | Indicates whether the load reported is the first time the data set is loaded (can be used by backend systems to aggregate/bill differently based on first time indication). |
| `consumption` | `dataLoadConsumptionObject` | No |  |
| `dataAssetId` | `string` | No | Unique identifier for the data asset related to the event. |
| `loadEndedAt` | `string` | No | Timestamp of when the data set load ended. Must adhere to RFC 3339. Metadata: format = "date-time". |
| `loadSuccess` | `boolean` | No | Indicates whether the load was successful (can be used by backend systems to aggregate/bill differently based on success criteria). |
| `errorMessage` | `string` | No | Error message describing why the load failed (only populated when loadSuccess is false) |
| `dataAssetType` | `string` | No | Type of the data asset the load belongs to (e.g. LANDING, STORAGE). |
| `loadStartedAt` | `string` | No | Timestamp of when the data set load started. Must adhere to RFC 3339. Metadata: format = "date-time". |
| `notChargeable` | `boolean` | No | When this field is set to true the event should be discarded from consumption metrics. |
| `recordsLoaded` | `integer` | No | Number of records loaded into the data set (only applicable on finished event). |
| `dataSetSecureQRI` | `string` | No | Secure QRI (Qlik resource identifier) of the data set related to the event. It identifies the data set's underlying resource without exposing connection details. |
| `notChargeableReason` | `string` | No | Description for why the event is set to notChargeable. |

<details>
<summary>Properties of `consumption`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `totalBytes` | `number` | No | Harmonized total bytes property, same value as totalBytesLoaded. |
| `totalBytesLoaded` | `number` | No | Total bytes loaded in a specific load operation. |

</details>

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2018-10-30T07:06:22Z",
  "type": "com.qlik.v1.data-set.data.load.finished",
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
    "dataSetId": "id123",
    "firstLoad": true,
    "consumption": {
      "totalBytes": 20000,
      "totalBytesLoaded": 20000
    },
    "dataAssetId": "id123",
    "loadEndedAt": "2018-10-30T07:06:22Z",
    "loadSuccess": true,
    "errorMessage": "Failed to connect to source",
    "dataAssetType": "LANDING",
    "loadStartedAt": "2018-10-30T07:06:22Z",
    "notChargeable": false,
    "recordsLoaded": 20,
    "dataSetSecureQRI": "qri:db:snowflake://Bh__CEOO2-D2Ty2f5egzjobOWnrxe6Cl8hHjJ6G08KE#w7OWgEHpy-iUi4EVNEGGQ6bJwU3FT6RdX38hbbrpJlM",
    "notChargeableReason": "Transform to QCS"
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



### dataLoadConsumptionObject

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `totalBytes` | `number` | No | Harmonized total bytes property, same value as totalBytesLoaded. |
| `totalBytesLoaded` | `number` | No | Total bytes loaded in a specific load operation. |



### datasetLoadFinishedObject

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | `string` | No | Unique identifier for the app related to the event. Metadata: format = "uid". |
| `dataSetId` | `string` | No | Unique identifier for the data set related to the event. |
| `firstLoad` | `boolean` | No | Indicates whether the load reported is the first time the data set is loaded (can be used by backend systems to aggregate/bill differently based on first time indication). |
| `consumption` | `dataLoadConsumptionObject` | No |  |
| `dataAssetId` | `string` | No | Unique identifier for the data asset related to the event. |
| `loadEndedAt` | `string` | No | Timestamp of when the data set load ended. Must adhere to RFC 3339. Metadata: format = "date-time". |
| `loadSuccess` | `boolean` | No | Indicates whether the load was successful (can be used by backend systems to aggregate/bill differently based on success criteria). |
| `errorMessage` | `string` | No | Error message describing why the load failed (only populated when loadSuccess is false) |
| `dataAssetType` | `string` | No | Type of the data asset the load belongs to (e.g. LANDING, STORAGE). |
| `loadStartedAt` | `string` | No | Timestamp of when the data set load started. Must adhere to RFC 3339. Metadata: format = "date-time". |
| `notChargeable` | `boolean` | No | When this field is set to true the event should be discarded from consumption metrics. |
| `recordsLoaded` | `integer` | No | Number of records loaded into the data set (only applicable on finished event). |
| `dataSetSecureQRI` | `string` | No | Secure QRI (Qlik resource identifier) of the data set related to the event. It identifies the data set's underlying resource without exposing connection details. |
| `notChargeableReason` | `string` | No | Description for why the event is set to notChargeable. |

<details>
<summary>Properties of `consumption`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `totalBytes` | `number` | No | Harmonized total bytes property, same value as totalBytesLoaded. |
| `totalBytesLoaded` | `number` | No | Total bytes loaded in a specific load operation. |

</details>



### updateItem

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `path` | `string` | No | updated item path |
| `newvalue` | `string` | No | new value at given path |
| `oldvalue` | `string` | No | original value at given path |


