---
source: https://qlik.dev/apis/event/analytics/geocodings/
last_updated: 2026-11-06T17:29:42+01:00
---

# Geocodings

## Table of Contents

### system-events.analytics.geocoding

- [com.qlik.analytics.geocoding.executed](#comqlikanalyticsgeocodingexecuted)

## Events published on the `system-events.analytics.geocoding` channel

### com.qlik.analytics.geocoding.executed

**Title:** Geocoding performed

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a geocoding lookup is executed.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. Metadata: default = "com.qlik.analytics.geocoding.executed". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: default = "com.qlik/geo-operations". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1, default = "application/json". |
| `userid` | `string` | No | Unique identifier for the user that triggered the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `data` | `geocodingPayload` | No | Geocoding event payload |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | `string` | No | Unique identifier of the app that triggered the event. |
| `lookups` | `integer` | Yes | Number of rows sent for geocoding in this batch |
| `operation` | `string` | Yes | Type of operation of the original request Allowed values: pointtoaddresslookup \| addresspointlookup. |
| `requestId` | `string` | Yes | The unique identifier of the operation that did the geocoding. |

</details>


**Example**

```json
{
  "id": "5f17a489-01a7-410b-83a1-a2af1421cd46",
  "time": "2026-04-05T17:31:00Z",
  "type": "com.qlik.analytics.geocoding.executed",
  "source": "com.qlik/geo-operations",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "69a6a037a234a46a56167985",
  "tenantid": "5d9b462Bsc46ZP6zCouVwBzyyk4HSrzu",
  "data": {
    "appId": "feca8dc1-ae1d-4eef-a1ca-e0ed05fb9332",
    "lookups": 28,
    "operation": "pointtoaddresslookup",
    "requestId": "7304c306-71a4-4665-bd57-91ae52fb2c36"
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
| `userid` | `string` | No | Unique identifier for the user that triggered the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |



### geocodingPayload

Geocoding event payload

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | `string` | No | Unique identifier of the app that triggered the event. |
| `lookups` | `integer` | Yes | Number of rows sent for geocoding in this batch |
| `operation` | `string` | Yes | Type of operation of the original request Allowed values: pointtoaddresslookup \| addresspointlookup. |
| `requestId` | `string` | Yes | The unique identifier of the operation that did the geocoding. |


