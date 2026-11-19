---
source: https://qlik.dev/apis/event/core/auth-settings/
last_updated: 2026-09-22T16:26:40+02:00
---

# Auth settings

## Table of Contents

### system-events.auth-settings

- [com.qlik.core.auth-settings.updated](#comqlikcoreauth-settingsupdated)

## Events published on the `system-events.auth-settings` channel

### com.qlik.core.auth-settings.updated

**Title:** Auth settings updated

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when auth settings are updated.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Describes the type of event related to the originating occurrence. Metadata: default = "com.qlik.core.auth-settings.updated". |
| `source` | `string` | Yes | Identifies the service that emitted this event. Metadata: default = "com.qlik/iam-resources". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `clientid` | `string` | No | Unique identifier for the OAuth client triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `sessionid` | `string` | No | Unique identifier for the session related to the event. |
| `data` | `authSettings` | No | Contains the updated authentication settings and field-level changes. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The ID of the Auth Settings. |
| `tenantId` | `string` | Yes | Unique identifier for the tenant the Auth Settings belongs to. |
| `isDefault` | `boolean` | No | Indicates whether these are the default Auth Settings for the tenant. |
| `maxUserSessionLifespanMinutes` | `integer` | Yes | Max session lifespan in minutes. Metadata: format = int64. |
| `dcrAllowedAuthenticationMethods` | `string[]` | No | The allowed authentication methods for dynamic client registration. Allowed values: none \| client_secret. |
| `dynamicClientRegistrationEnabled` | `boolean` | No | Indicates whether dynamic client registration is enabled. Only present when the dynamic client registration feature flag is enabled. |
| `userSessionInactivityTimeoutMinutes` | `integer` | Yes | Max session inactivity time in minutes. Metadata: format = int64. |
| `_meta` | `eventMeta` | No | Metadata about the actor that triggered the event. |
| `_updates` | `object[]` | No | An attribute update object that contains the change of an attribute. |

<details>
<summary>Properties of `_meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `userId` | `string` | Yes | The ID of the user that triggered the event. |
| `tenantId` | `string` | Yes | The ID of the tenant in which the event was triggered. |
| `sessionId` | `string` | Yes | The ID of the session in which the event was triggered. |

</details>

<details>
<summary>Properties of `_updates`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `path` | `string` | Yes | The updated attribute path. |
| `newValue` | `` | Yes | The new JSON value of the updated attribute. |
| `oldValue` | `` | Yes | The old JSON value of the updated attribute. |

</details>

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2026-04-05T17:31:00Z",
  "type": "com.qlik.core.auth-settings.updated",
  "source": "com.qlik/iam-resources",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "clientid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "tenantid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "sessionid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "data": {
    "id": "5be59decca62aa00097268a4",
    "tenantId": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
    "isDefault": false,
    "maxUserSessionLifespanMinutes": 1440,
    "dcrAllowedAuthenticationMethods": [
      "client_secret"
    ],
    "dynamicClientRegistrationEnabled": false,
    "userSessionInactivityTimeoutMinutes": 60,
    "_meta": {
      "userId": "5be59decca62aa00097268a4",
      "tenantId": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
      "sessionId": "5be59decca62aa00097268a4"
    },
    "_updates": [
      {
        "path": "/userSessionInactivityTimeoutMinutes",
        "newValue": 30,
        "oldValue": 60
      }
    ]
  }
}
```


## Schemas

### attributeUpdate

An attribute update object that contains the change of an attribute.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `path` | `string` | Yes | The updated attribute path. |
| `newValue` | `` | Yes | The new JSON value of the updated attribute. |
| `oldValue` | `` | Yes | The old JSON value of the updated attribute. |



### authSettings

Authentication Settings resource object.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The ID of the Auth Settings. |
| `tenantId` | `string` | Yes | Unique identifier for the tenant the Auth Settings belongs to. |
| `isDefault` | `boolean` | No | Indicates whether these are the default Auth Settings for the tenant. |
| `maxUserSessionLifespanMinutes` | `integer` | Yes | Max session lifespan in minutes. Metadata: format = int64. |
| `dcrAllowedAuthenticationMethods` | `string[]` | No | The allowed authentication methods for dynamic client registration. Allowed values: none \| client_secret. |
| `dynamicClientRegistrationEnabled` | `boolean` | No | Indicates whether dynamic client registration is enabled. Only present when the dynamic client registration feature flag is enabled. |
| `userSessionInactivityTimeoutMinutes` | `integer` | Yes | Max session inactivity time in minutes. Metadata: format = int64. |



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

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `userid` | `string` | No | Unique identifier for the user triggering the event. |
| `clientid` | `string` | No | Unique identifier for the OAuth client triggering the event. |
| `tenantid` | `string` | Yes | Unique identifier for the tenant related to the event. |
| `sessionid` | `string` | No | Unique identifier for the session related to the event. |



### eventMeta

Metadata about the actor that triggered the event.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `userId` | `string` | Yes | The ID of the user that triggered the event. |
| `tenantId` | `string` | Yes | The ID of the tenant in which the event was triggered. |
| `sessionId` | `string` | Yes | The ID of the session in which the event was triggered. |


