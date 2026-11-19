# Webhooks

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Webhooks are a way for Qlik Cloud to provide other applications with real-time information.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/core/webhooks`](#get-apicorewebhooks) | Retrieves all webhook entries for a tenant that the user has access to. Users assigned the `TenantAdmin` role can retrieve all webhooks of the tenant; other users only retrieve the webhooks they own. Values of `encryptedHeaders` are never returned, only their header names. |
| `POST` | [`/api/core/webhooks`](#post-apicorewebhooks) | Creates a new webhook. User must be assigned the `TenantAdmin` role to create `tenant` level webhooks. Each user can own up to 150 webhooks per tenant; creating a webhook beyond that quota is rejected with `403`. |
| `GET` | [`/api/core/webhooks/{id}`](#get-apicorewebhooksid) | Returns details for a specific webhook. |
| `PATCH` | [`/api/core/webhooks/{id}`](#patch-apicorewebhooksid) | Updates one or more individual properties of a webhook using a JSON Patch document, leaving all other properties unchanged. The patch is applied to the stored webhook and the result is validated as a whole, so a patch that produces an invalid webhook is rejected. When `/url` is changed on a webhook that has encrypted headers, every existing encrypted header must also be replaced or removed in the same patch, otherwise the request is rejected with `400`. Changing read-only properties is rejected with `409`, and changing `/ownerId` requires permission to transfer ownership. |
| `PUT` | [`/api/core/webhooks/{id}`](#put-apicorewebhooksid) | Replaces all writable properties of a webhook and returns the updated webhook. This is a full replacement: every writable property that is omitted from the request body is reset to its default, so omitting `secret`, `encryptedHeaders`, `headers` or `filter` clears them, and omitting `enabled` disables the webhook. Because `secret` is never returned and `encryptedHeaders` is returned as a list of header names, a `GET` response cannot be sent back unchanged as a `PUT` request body; re-send those values explicitly, and use `PATCH` to change individual properties. Read-only properties such as `id`, `createdAt`, `createdByUserId` and `origin` cannot be changed and are rejected with `409`. |
| `DELETE` | [`/api/core/webhooks/{id}`](#delete-apicorewebhooksid) | Deletes a specific webhook. |
| `GET` | [`/api/core/webhooks/{id}/deliveries`](#get-apicorewebhooksiddeliveries) | Returns deliveries for a specific webhook. Delivery history is stored for 1 week. |
| `GET` | [`/api/core/webhooks/{id}/deliveries/{deliveryId}`](#get-apicorewebhooksiddeliveriesdeliveryid) | Returns details for a specific delivery. |
| `POST` | [`/api/core/webhooks/{id}/deliveries/{deliveryId}/actions/resend`](#post-apicorewebhooksiddeliveriesdeliveryidactionsresend) | Resends the event payload of an existing delivery and returns the new delivery. The event payload is taken from the original delivery, but the webhook's current configuration (URL, headers, secret and certificate settings) is used to send it. The resend is attempted synchronously and a new delivery record is always created, so a `201` response can contain a delivery with status `fail`. A resend is subject to the same validation and failure handling as an automatic delivery, so a webhook that is no longer valid or that exceeds the delivery failure threshold can be disabled as a result. |
| `GET` | [`/api/core/webhooks/event-types`](#get-apicorewebhooksevent-types) | Lists event-types that are possible to subscribe to. |

## API Reference

### GET /api/core/webhooks

Retrieves all webhook entries for a tenant that the user has access to. Users assigned the `TenantAdmin` role can retrieve all webhooks of the tenant; other users only retrieve the webhooks they own. Values of `encryptedHeaders` are never returned, only their header names.

- **Replaces:** "GET:/v1/webhooks"
- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `createdByUserId` | string | No | Filter resources by user that created it |
| `enabled` | boolean | No | Filter resources by enabled true/false |
| `eventTypes` | string | No | Filter resources by event-type. Accepts a comma-separated list, and a webhook must subscribe to every listed event-type to match (AND semantics). A single webhook can subscribe to multiple event-types. Values must be event-types returned by `GET /core/webhooks/event-types`. |
| `level` | string | No | Filter resources by the level the webhook operates at: `tenant` for all resources of the tenant, or `user` for only the resources accessible to the webhook owner. |
| `limit` | number | No | Maximum number of webhooks to retrieve |
| `name` | string | No | Filter resources by name. The value is matched as a case-insensitive substring, not as a glob pattern, so `prod` matches `Production webhook`. |
| `next` | string | No | Cursor to the next page |
| `origins` | string | No | Filter resources by origin. The implementation also accepts a comma-separated list, in which case a webhook matches if its origin is any of the listed values (OR semantics). Enum: "api", "automations", "management-console" |
| `ownerId` | string | No | Filter resources by user that owns it, only applicable for user level webhooks |
| `prev` | string | No | Cursor to the previous page. |
| `sort` | string | No | Field to sort by, prefix with -/+ to indicate order Enum: "name", "+name", "-name", "url", "+url", "-url", "createdAt", "+createdAt", "-createdAt", "updatedAt", "+updatedAt", "-updatedAt" |
| `updatedByUserId` | string | No | Filter resources by user that last updated the webhook |
| `url` | string | No | Filter resources by URL. The value is matched as a case-insensitive substring, not as a glob pattern, so `example.com` matches `https://example.com/hook`. |

#### Responses

##### 200

OK Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No |  |
| `links` | object | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The webhook's unique identifier |
| `url` | string | Yes | Target URL for webhook HTTPS requests |
| `name` | string | Yes | The name for the webhook |
| `level` | string | No | Defines at what level the webhook should operate: for all resources belonging to a tenant or restricted to only those accessible by the webhook-creator. Enum: "tenant", "user" |
| `filter` | string | No | Filter that should match for a webhook to be triggered. Supported common attribute names are 'id', 'spaceId' and 'topLevelResourceId'. Individual event-types can support additional event-specific attributes, which cannot be combined with other event-types in the same webhook. For example "com.qlik.v1.app.reload.finished" supports "data.status" with the allowed values "SUCCEEDED", "FAILED", "CANCELED" and "EXCEEDED_LIMIT". The authoritative set of filterable attributes and their allowed values for each event-type is returned in the `allowedFilters` property of `GET /core/webhooks/event-types`. Supported attribute operators are 'eq' and 'ne'. Supported logical operators are 'and' and 'or'. Note that attribute values must be valid JSON strings, hence they're enclosed with double quotes. For more detailed information regarding the SCIM filter syntax (RFC7644) used please follow the link to external documentation. |
| `enabled` | boolean | No | Whether the webhook is active and sending requests |
| `headers` | object | No | Additional headers in the post request. Maximum combined size: 2048 bytes (total of all header names and values). |
| `ownerId` | string | No | The id of the user that owns the webhook, only applicable for user level webhooks |
| `createdAt` | string | No | The UTC timestamp when the webhook was created |
| `updatedAt` | string | No | The UTC timestamp when the webhook was last updated |
| `eventTypes` | string[] | No | Types of events for which the webhook should trigger. Retrieve available types from `/core/webhooks/event-types`. |
| `description` | string | No | The reason for creating the webhook |
| `disabledReason` | string | No | The reason for the webhook to be disabled |
| `secretKeyAdded` | boolean | No | Whether a signing secret is currently stored for this webhook. The secret itself is never returned. |
| `createdByUserId` | string | No | The id of the user that created the webhook |
| `updatedByUserId` | string | No | The id of the user that last updated the webhook |
| `encryptedHeaders` | string[] | No | Names of the encrypted headers that are sent with the post request. Only the header names are returned; the values are never disclosed. Maximum combined size: 2048 bytes (total of all encrypted header names and values). |
| `disabledReasonCode` | string | No | The unique code for the reason |
| `enableCloudEventDelivery` | boolean | No | Whether this webhook delivers events as CloudEvents. Once enabled, it cannot be disabled. |
| `checkCertificateRevocation` | boolean | No | If enabled the certificate chain of the configured URL will be checked for revocation before sending the webhook. |
| `origin` | string | No | Indicates from where the webhook was created and its purpose Enum: "api", "automations", "management-console" |

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `next` | object | No |  |
| `prev` | object | No |  |
| `self` | object | No |  |

<details>
<summary>Properties of `next`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL to a resource request |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL to a resource request |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL to a resource request |

</details>

</details>

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/core/webhooks` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/core/webhooks',
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
# qlik-cli has not implemented support for GET /api/core/webhooks yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/core/webhooks" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "string",
      "url": "string",
      "name": "string",
      "level": "tenant",
      "filter": "id eq \"id123\" or spaceId eq \"spaceId123\" or spaceId eq \"spaceId456\" or topLevelResourceId eq \"id789\"",
      "enabled": false,
      "headers": {
        "headerName": "headerValue"
      },
      "ownerId": "string",
      "createdAt": "2025-07-02T08:20:35.49Z",
      "updatedAt": "2025-07-02T08:20:35.49Z",
      "eventTypes": [
        "string"
      ],
      "description": "string",
      "disabledReason": "string",
      "secretKeyAdded": true,
      "createdByUserId": "string",
      "updatedByUserId": "string",
      "encryptedHeaders": [
        "header1",
        "header2"
      ],
      "disabledReasonCode": "string",
      "enableCloudEventDelivery": true,
      "checkCertificateRevocation": false,
      "origin": "api"
    }
  ],
  "links": {
    "next": {
      "href": "string"
    },
    "prev": {
      "href": "string"
    },
    "self": {
      "href": "string"
    }
  }
}
```

---

### POST /api/core/webhooks

Creates a new webhook. User must be assigned the `TenantAdmin` role to create `tenant` level webhooks. Each user can own up to 150 webhooks per tenant; creating a webhook beyond that quota is rejected with `403`.

- **Replaces:** "POST:/v1/webhooks"
- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `url` | string | Yes | Target URL for webhook HTTPS requests |
| `name` | string | Yes | The name for the webhook |
| `level` | string | No | Defines at what level the webhook should operate: for all resources belonging to a tenant or restricted to only those accessible by the webhook-creator. Enum: "tenant", "user" |
| `filter` | string | No | Filter that should match for a webhook to be triggered. Supported common attribute names are 'id', 'spaceId' and 'topLevelResourceId'. Individual event-types can support additional event-specific attributes, which cannot be combined with other event-types in the same webhook. For example "com.qlik.v1.app.reload.finished" supports "data.status" with the allowed values "SUCCEEDED", "FAILED", "CANCELED" and "EXCEEDED_LIMIT". The authoritative set of filterable attributes and their allowed values for each event-type is returned in the `allowedFilters` property of `GET /core/webhooks/event-types`. Supported attribute operators are 'eq' and 'ne'. Supported logical operators are 'and' and 'or'. Note that attribute values must be valid JSON strings, hence they're enclosed with double quotes. For more detailed information regarding the SCIM filter syntax (RFC7644) used please follow the link to external documentation. |
| `secret` | string | No | Shared secret used to sign the webhook delivery. Each delivery is sent with a `Qlik-Signature` header containing the hex-encoded HMAC-SHA256 of the raw request body, computed with this secret, so the receiver can verify that the payload is genuine and unmodified. The secret is stored encrypted and is never returned by the API; responses report only `secretKeyAdded`. |
| `enabled` | boolean | No | Whether the webhook is active and sending requests |
| `headers` | object | No | Additional headers in the post request (webhook delivery). Note: duplicate headers are not allowed and are case-insensitive. Maximum combined size: 2048 bytes (total of all header names and values). |
| `ownerId` | string | No | The id of the user that owns the webhook, only applicable for user level webhooks |
| `eventTypes` | string[] | No | Types of events for which the webhook should trigger. Retrieve available types from `/core/webhooks/event-types`. |
| `description` | string | No | The reason for creating the webhook |
| `encryptedHeaders` | object | No | Headers that are persisted encrypted and decrypted again to be sent as normal headers in the post request (webhook delivery). In requests they are supplied as name/value pairs, but responses return only the header names as a list of strings, because the values are never disclosed. If the URL changes, these headers must be re-entered. Note: duplicate headers are not allowed and are case-insensitive. Maximum combined size: 2048 bytes (total of all encrypted header names and values). |
| `enableCloudEventDelivery` | boolean | No | Whether this webhook delivers events as CloudEvents. On creation, the service determines the effective value from tenant feature flags and webhook origin; the supplied value is not authoritative. On PUT, omission is treated as false. When feature flags are enabled, the service may automatically enable this for exclusive Data Integration webhooks. Once enabled, it cannot be disabled; omitting it when replacing an enabled webhook therefore returns `403`. |
| `checkCertificateRevocation` | boolean | No | If enabled the certificate chain of the configured URL will be checked for revocation before sending the webhook. |
| `origin` | string | No | Indicates from where the webhook was created and its purpose Enum: "api", "automations", "management-console" |

#### Responses

##### 201

The webhook was created. The response contains the stored webhook, where `secret` is replaced by `secretKeyAdded` and `encryptedHeaders` is returned as a list of header names.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The webhook's unique identifier |
| `url` | string | Yes | Target URL for webhook HTTPS requests |
| `name` | string | Yes | The name for the webhook |
| `level` | string | No | Defines at what level the webhook should operate: for all resources belonging to a tenant or restricted to only those accessible by the webhook-creator. Enum: "tenant", "user" |
| `filter` | string | No | Filter that should match for a webhook to be triggered. Supported common attribute names are 'id', 'spaceId' and 'topLevelResourceId'. Individual event-types can support additional event-specific attributes, which cannot be combined with other event-types in the same webhook. For example "com.qlik.v1.app.reload.finished" supports "data.status" with the allowed values "SUCCEEDED", "FAILED", "CANCELED" and "EXCEEDED_LIMIT". The authoritative set of filterable attributes and their allowed values for each event-type is returned in the `allowedFilters` property of `GET /core/webhooks/event-types`. Supported attribute operators are 'eq' and 'ne'. Supported logical operators are 'and' and 'or'. Note that attribute values must be valid JSON strings, hence they're enclosed with double quotes. For more detailed information regarding the SCIM filter syntax (RFC7644) used please follow the link to external documentation. |
| `enabled` | boolean | No | Whether the webhook is active and sending requests |
| `headers` | object | No | Additional headers in the post request. Maximum combined size: 2048 bytes (total of all header names and values). |
| `ownerId` | string | No | The id of the user that owns the webhook, only applicable for user level webhooks |
| `createdAt` | string | No | The UTC timestamp when the webhook was created |
| `updatedAt` | string | No | The UTC timestamp when the webhook was last updated |
| `eventTypes` | string[] | No | Types of events for which the webhook should trigger. Retrieve available types from `/core/webhooks/event-types`. |
| `description` | string | No | The reason for creating the webhook |
| `disabledReason` | string | No | The reason for the webhook to be disabled |
| `secretKeyAdded` | boolean | No | Whether a signing secret is currently stored for this webhook. The secret itself is never returned. |
| `createdByUserId` | string | No | The id of the user that created the webhook |
| `updatedByUserId` | string | No | The id of the user that last updated the webhook |
| `encryptedHeaders` | string[] | No | Names of the encrypted headers that are sent with the post request. Only the header names are returned; the values are never disclosed. Maximum combined size: 2048 bytes (total of all encrypted header names and values). |
| `disabledReasonCode` | string | No | The unique code for the reason |
| `enableCloudEventDelivery` | boolean | No | Whether this webhook delivers events as CloudEvents. Once enabled, it cannot be disabled. |
| `checkCertificateRevocation` | boolean | No | If enabled the certificate chain of the configured URL will be checked for revocation before sending the webhook. |
| `origin` | string | No | Indicates from where the webhook was created and its purpose Enum: "api", "automations", "management-console" |

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 403

The request is not allowed, for example because the user lacks the required permissions, the target URL is forbidden, the event-type is not enabled for the tenant, or the user's 150-webhook quota is reached.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/core/webhooks` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/core/webhooks',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      url: 'https://www.valid-url.com',
      name: 'Apps-Webhook',
      level: 'tenant',
      filter:
        'id eq "id123" or spaceId eq "spaceId123" or spaceId eq "spaceId456" or topLevelResourceId eq "id789"',
      secret:
        'ItsA32To64BitLongSecretForQlikSignature',
      enabled: false,
      headers: { headerName: 'headerValue' },
      ownerId: '6863a23242ecf6179670ee97',
      eventTypes: [
        'com.qlik.v1.reload.finished',
        'com.qlik.v1.app.created',
      ],
      description:
        'this webhook provides a real time update of an action occurred by delivering an event through a post call',
      encryptedHeaders: {
        headerName: 'sensitiveHeaderValue',
      },
      enableCloudEventDelivery: true,
      checkCertificateRevocation: false,
      origin: 'api',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/core/webhooks yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/core/webhooks" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"url":"https://www.valid-url.com","name":"Apps-Webhook","level":"tenant","filter":"id eq \"id123\" or spaceId eq \"spaceId123\" or spaceId eq \"spaceId456\" or topLevelResourceId eq \"id789\"","secret":"ItsA32To64BitLongSecretForQlikSignature","enabled":false,"headers":{"headerName":"headerValue"},"ownerId":"6863a23242ecf6179670ee97","eventTypes":["com.qlik.v1.reload.finished","com.qlik.v1.app.created"],"description":"this webhook provides a real time update of an action occurred by delivering an event through a post call","encryptedHeaders":{"headerName":"sensitiveHeaderValue"},"enableCloudEventDelivery":true,"checkCertificateRevocation":false,"origin":"api"}'
```

**Example Response:**

```json
{
  "id": "string",
  "url": "string",
  "name": "string",
  "level": "tenant",
  "filter": "id eq \"id123\" or spaceId eq \"spaceId123\" or spaceId eq \"spaceId456\" or topLevelResourceId eq \"id789\"",
  "enabled": false,
  "headers": {
    "headerName": "headerValue"
  },
  "ownerId": "string",
  "createdAt": "2025-07-02T08:20:35.49Z",
  "updatedAt": "2025-07-02T08:20:35.49Z",
  "eventTypes": [
    "string"
  ],
  "description": "string",
  "disabledReason": "string",
  "secretKeyAdded": true,
  "createdByUserId": "string",
  "updatedByUserId": "string",
  "encryptedHeaders": [
    "header1",
    "header2"
  ],
  "disabledReasonCode": "string",
  "enableCloudEventDelivery": true,
  "checkCertificateRevocation": false,
  "origin": "api"
}
```

---

### GET /api/core/webhooks/{id}

Returns details for a specific webhook.

- **Replaces:** "GET:/v1/webhooks/{id}"
- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The webhook's unique identifier. |

#### Responses

##### 200

OK Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The webhook's unique identifier |
| `url` | string | Yes | Target URL for webhook HTTPS requests |
| `name` | string | Yes | The name for the webhook |
| `level` | string | No | Defines at what level the webhook should operate: for all resources belonging to a tenant or restricted to only those accessible by the webhook-creator. Enum: "tenant", "user" |
| `filter` | string | No | Filter that should match for a webhook to be triggered. Supported common attribute names are 'id', 'spaceId' and 'topLevelResourceId'. Individual event-types can support additional event-specific attributes, which cannot be combined with other event-types in the same webhook. For example "com.qlik.v1.app.reload.finished" supports "data.status" with the allowed values "SUCCEEDED", "FAILED", "CANCELED" and "EXCEEDED_LIMIT". The authoritative set of filterable attributes and their allowed values for each event-type is returned in the `allowedFilters` property of `GET /core/webhooks/event-types`. Supported attribute operators are 'eq' and 'ne'. Supported logical operators are 'and' and 'or'. Note that attribute values must be valid JSON strings, hence they're enclosed with double quotes. For more detailed information regarding the SCIM filter syntax (RFC7644) used please follow the link to external documentation. |
| `enabled` | boolean | No | Whether the webhook is active and sending requests |
| `headers` | object | No | Additional headers in the post request. Maximum combined size: 2048 bytes (total of all header names and values). |
| `ownerId` | string | No | The id of the user that owns the webhook, only applicable for user level webhooks |
| `createdAt` | string | No | The UTC timestamp when the webhook was created |
| `updatedAt` | string | No | The UTC timestamp when the webhook was last updated |
| `eventTypes` | string[] | No | Types of events for which the webhook should trigger. Retrieve available types from `/core/webhooks/event-types`. |
| `description` | string | No | The reason for creating the webhook |
| `disabledReason` | string | No | The reason for the webhook to be disabled |
| `secretKeyAdded` | boolean | No | Whether a signing secret is currently stored for this webhook. The secret itself is never returned. |
| `createdByUserId` | string | No | The id of the user that created the webhook |
| `updatedByUserId` | string | No | The id of the user that last updated the webhook |
| `encryptedHeaders` | string[] | No | Names of the encrypted headers that are sent with the post request. Only the header names are returned; the values are never disclosed. Maximum combined size: 2048 bytes (total of all encrypted header names and values). |
| `disabledReasonCode` | string | No | The unique code for the reason |
| `enableCloudEventDelivery` | boolean | No | Whether this webhook delivers events as CloudEvents. Once enabled, it cannot be disabled. |
| `checkCertificateRevocation` | boolean | No | If enabled the certificate chain of the configured URL will be checked for revocation before sending the webhook. |
| `origin` | string | No | Indicates from where the webhook was created and its purpose Enum: "api", "automations", "management-console" |

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/core/webhooks/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/core/webhooks/{id}',
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
# qlik-cli has not implemented support for GET /api/core/webhooks/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/core/webhooks/{id}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "string",
  "url": "string",
  "name": "string",
  "level": "tenant",
  "filter": "id eq \"id123\" or spaceId eq \"spaceId123\" or spaceId eq \"spaceId456\" or topLevelResourceId eq \"id789\"",
  "enabled": false,
  "headers": {
    "headerName": "headerValue"
  },
  "ownerId": "string",
  "createdAt": "2025-07-02T08:20:35.49Z",
  "updatedAt": "2025-07-02T08:20:35.49Z",
  "eventTypes": [
    "string"
  ],
  "description": "string",
  "disabledReason": "string",
  "secretKeyAdded": true,
  "createdByUserId": "string",
  "updatedByUserId": "string",
  "encryptedHeaders": [
    "header1",
    "header2"
  ],
  "disabledReasonCode": "string",
  "enableCloudEventDelivery": true,
  "checkCertificateRevocation": false,
  "origin": "api"
}
```

---

### PATCH /api/core/webhooks/{id}

Updates one or more individual properties of a webhook using a JSON Patch document, leaving all other properties unchanged. The patch is applied to the stored webhook and the result is validated as a whole, so a patch that produces an invalid webhook is rejected. When `/url` is changed on a webhook that has encrypted headers, every existing encrypted header must also be replaced or removed in the same patch, otherwise the request is rejected with `400`. Changing read-only properties is rejected with `409`, and changing `/ownerId` requires permission to transfer ownership.

- **Replaces:** "PATCH:/v1/webhooks/{id}"
- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The webhook's unique identifier. |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | The operation to be performed Enum: "add", "remove", "replace" |
| `path` | string | Yes | The path of the webhook property to patch. Only writable properties can be patched; read-only properties such as `/id`, `/createdAt`, `/createdByUserId` and `/origin` are rejected. Individual members of `/headers` and `/encryptedHeaders` can also be addressed directly, for example `/encryptedHeaders/myHeader`. Enum: "/name", "/description", "/url", "/eventTypes", "/headers", "/enabled", "/secret", "/encryptedHeaders", "/enableCloudEventDelivery", "/filter", "/level", "/ownerId", "/checkCertificateRevocation" |
| `value` | boolean \| integer \| object \| string \| array | No | The value to be used for this operation. The type must match the patched property, for example an array of event-type names for `/eventTypes` or an object of header name/value pairs for `/headers`. Not used by the `remove` operation. |

<details>
<summary>Properties of `value`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | boolean | No |  |

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | integer | No |  |

**Option 3:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | object | No |  |

**Option 4:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | string | No |  |

**Option 5:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `` | array | No |  |

</details>

#### Responses

##### 204

No Content response.

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 409

Conflict

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PATCH /api/core/webhooks/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/core/webhooks/{id}',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      {
        op: 'add',
        path: '/description',
        value: true,
      },
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/core/webhooks/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/core/webhooks/{id}" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"add","path":"/description","value":true}]'
```

---

### PUT /api/core/webhooks/{id}

Replaces all writable properties of a webhook and returns the updated webhook. This is a full replacement: every writable property that is omitted from the request body is reset to its default, so omitting `secret`, `encryptedHeaders`, `headers` or `filter` clears them, and omitting `enabled` disables the webhook. Because `secret` is never returned and `encryptedHeaders` is returned as a list of header names, a `GET` response cannot be sent back unchanged as a `PUT` request body; re-send those values explicitly, and use `PATCH` to change individual properties. Read-only properties such as `id`, `createdAt`, `createdByUserId` and `origin` cannot be changed and are rejected with `409`.

- **Replaces:** "PUT:/v1/webhooks/{id}"
- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The webhook's unique identifier. |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `url` | string | Yes | Target URL for webhook HTTPS requests |
| `name` | string | Yes | The name for the webhook |
| `level` | string | No | Defines at what level the webhook should operate: for all resources belonging to a tenant or restricted to only those accessible by the webhook-creator. Enum: "tenant", "user" |
| `filter` | string | No | Filter that should match for a webhook to be triggered. Supported common attribute names are 'id', 'spaceId' and 'topLevelResourceId'. Individual event-types can support additional event-specific attributes, which cannot be combined with other event-types in the same webhook. For example "com.qlik.v1.app.reload.finished" supports "data.status" with the allowed values "SUCCEEDED", "FAILED", "CANCELED" and "EXCEEDED_LIMIT". The authoritative set of filterable attributes and their allowed values for each event-type is returned in the `allowedFilters` property of `GET /core/webhooks/event-types`. Supported attribute operators are 'eq' and 'ne'. Supported logical operators are 'and' and 'or'. Note that attribute values must be valid JSON strings, hence they're enclosed with double quotes. For more detailed information regarding the SCIM filter syntax (RFC7644) used please follow the link to external documentation. |
| `secret` | string | No | Shared secret used to sign the webhook delivery. Each delivery is sent with a `Qlik-Signature` header containing the hex-encoded HMAC-SHA256 of the raw request body, computed with this secret, so the receiver can verify that the payload is genuine and unmodified. The secret is stored encrypted and is never returned by the API; responses report only `secretKeyAdded`. |
| `enabled` | boolean | No | Whether the webhook is active and sending requests |
| `headers` | object | No | Additional headers in the post request (webhook delivery). Note: duplicate headers are not allowed and are case-insensitive. Maximum combined size: 2048 bytes (total of all header names and values). |
| `ownerId` | string | No | The id of the user that owns the webhook, only applicable for user level webhooks |
| `eventTypes` | string[] | No | Types of events for which the webhook should trigger. Retrieve available types from `/core/webhooks/event-types`. |
| `description` | string | No | The reason for creating the webhook |
| `encryptedHeaders` | object | No | Headers that are persisted encrypted and decrypted again to be sent as normal headers in the post request (webhook delivery). In requests they are supplied as name/value pairs, but responses return only the header names as a list of strings, because the values are never disclosed. If the URL changes, these headers must be re-entered. Note: duplicate headers are not allowed and are case-insensitive. Maximum combined size: 2048 bytes (total of all encrypted header names and values). |
| `enableCloudEventDelivery` | boolean | No | Whether this webhook delivers events as CloudEvents. On creation, the service determines the effective value from tenant feature flags and webhook origin; the supplied value is not authoritative. On PUT, omission is treated as false. When feature flags are enabled, the service may automatically enable this for exclusive Data Integration webhooks. Once enabled, it cannot be disabled; omitting it when replacing an enabled webhook therefore returns `403`. |
| `checkCertificateRevocation` | boolean | No | If enabled the certificate chain of the configured URL will be checked for revocation before sending the webhook. |

#### Responses

##### 200

OK Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | No | The webhook's unique identifier |
| `url` | string | Yes | Target URL for webhook HTTPS requests |
| `name` | string | Yes | The name for the webhook |
| `level` | string | No | Defines at what level the webhook should operate: for all resources belonging to a tenant or restricted to only those accessible by the webhook-creator. Enum: "tenant", "user" |
| `filter` | string | No | Filter that should match for a webhook to be triggered. Supported common attribute names are 'id', 'spaceId' and 'topLevelResourceId'. Individual event-types can support additional event-specific attributes, which cannot be combined with other event-types in the same webhook. For example "com.qlik.v1.app.reload.finished" supports "data.status" with the allowed values "SUCCEEDED", "FAILED", "CANCELED" and "EXCEEDED_LIMIT". The authoritative set of filterable attributes and their allowed values for each event-type is returned in the `allowedFilters` property of `GET /core/webhooks/event-types`. Supported attribute operators are 'eq' and 'ne'. Supported logical operators are 'and' and 'or'. Note that attribute values must be valid JSON strings, hence they're enclosed with double quotes. For more detailed information regarding the SCIM filter syntax (RFC7644) used please follow the link to external documentation. |
| `enabled` | boolean | No | Whether the webhook is active and sending requests |
| `headers` | object | No | Additional headers in the post request. Maximum combined size: 2048 bytes (total of all header names and values). |
| `ownerId` | string | No | The id of the user that owns the webhook, only applicable for user level webhooks |
| `createdAt` | string | No | The UTC timestamp when the webhook was created |
| `updatedAt` | string | No | The UTC timestamp when the webhook was last updated |
| `eventTypes` | string[] | No | Types of events for which the webhook should trigger. Retrieve available types from `/core/webhooks/event-types`. |
| `description` | string | No | The reason for creating the webhook |
| `disabledReason` | string | No | The reason for the webhook to be disabled |
| `secretKeyAdded` | boolean | No | Whether a signing secret is currently stored for this webhook. The secret itself is never returned. |
| `createdByUserId` | string | No | The id of the user that created the webhook |
| `updatedByUserId` | string | No | The id of the user that last updated the webhook |
| `encryptedHeaders` | string[] | No | Names of the encrypted headers that are sent with the post request. Only the header names are returned; the values are never disclosed. Maximum combined size: 2048 bytes (total of all encrypted header names and values). |
| `disabledReasonCode` | string | No | The unique code for the reason |
| `enableCloudEventDelivery` | boolean | No | Whether this webhook delivers events as CloudEvents. Once enabled, it cannot be disabled. |
| `checkCertificateRevocation` | boolean | No | If enabled the certificate chain of the configured URL will be checked for revocation before sending the webhook. |
| `origin` | string | No | Indicates from where the webhook was created and its purpose Enum: "api", "automations", "management-console" |

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 409

Conflict

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PUT /api/core/webhooks/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/core/webhooks/{id}',
  {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      url: 'https://www.valid-url.com',
      name: 'Apps-Webhook',
      level: 'tenant',
      filter:
        'id eq "id123" or spaceId eq "spaceId123" or spaceId eq "spaceId456" or topLevelResourceId eq "id789"',
      secret:
        'ItsA32To64BitLongSecretForQlikSignature',
      enabled: false,
      headers: { headerName: 'headerValue' },
      ownerId: '6863a23242ecf6179670ee97',
      eventTypes: [
        'com.qlik.v1.reload.finished',
        'com.qlik.v1.app.created',
      ],
      description:
        'this webhook provides a real time update of an action occurred by delivering an event through a post call',
      encryptedHeaders: {
        headerName: 'sensitiveHeaderValue',
      },
      enableCloudEventDelivery: true,
      checkCertificateRevocation: false,
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PUT /api/core/webhooks/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/core/webhooks/{id}" \
-X PUT \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"url":"https://www.valid-url.com","name":"Apps-Webhook","level":"tenant","filter":"id eq \"id123\" or spaceId eq \"spaceId123\" or spaceId eq \"spaceId456\" or topLevelResourceId eq \"id789\"","secret":"ItsA32To64BitLongSecretForQlikSignature","enabled":false,"headers":{"headerName":"headerValue"},"ownerId":"6863a23242ecf6179670ee97","eventTypes":["com.qlik.v1.reload.finished","com.qlik.v1.app.created"],"description":"this webhook provides a real time update of an action occurred by delivering an event through a post call","encryptedHeaders":{"headerName":"sensitiveHeaderValue"},"enableCloudEventDelivery":true,"checkCertificateRevocation":false}'
```

**Example Response:**

```json
{
  "id": "string",
  "url": "string",
  "name": "string",
  "level": "tenant",
  "filter": "id eq \"id123\" or spaceId eq \"spaceId123\" or spaceId eq \"spaceId456\" or topLevelResourceId eq \"id789\"",
  "enabled": false,
  "headers": {
    "headerName": "headerValue"
  },
  "ownerId": "string",
  "createdAt": "2025-07-02T08:20:35.49Z",
  "updatedAt": "2025-07-02T08:20:35.49Z",
  "eventTypes": [
    "string"
  ],
  "description": "string",
  "disabledReason": "string",
  "secretKeyAdded": true,
  "createdByUserId": "string",
  "updatedByUserId": "string",
  "encryptedHeaders": [
    "header1",
    "header2"
  ],
  "disabledReasonCode": "string",
  "enableCloudEventDelivery": true,
  "checkCertificateRevocation": false,
  "origin": "api"
}
```

---

### DELETE /api/core/webhooks/{id}

Deletes a specific webhook.

- **Replaces:** "DELETE:/v1/webhooks/{id}"
- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The webhook's unique identifier. |

#### Responses

##### 204

No Content response.

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `DELETE /api/core/webhooks/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/core/webhooks/{id}',
  {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
    },
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for DELETE /api/core/webhooks/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/core/webhooks/{id}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### GET /api/core/webhooks/{id}/deliveries

Returns deliveries for a specific webhook. Delivery history is stored for 1 week.

- **Replaces:** "GET:/v1/webhooks/{id}/deliveries"
- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The webhook's unique identifier. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `eventType` | string | No | Filter resources by event-type |
| `limit` | number | No | Maximum number of deliveries to retrieve |
| `next` | string | No | Cursor to the next page |
| `prev` | string | No | Cursor to the previous page. |
| `sort` | string | No | Field to sort by, prefix with -/+ to indicate order Enum: "status", "+status", "-status", "triggeredAt", "+triggeredAt", "-triggeredAt" |
| `status` | string | No | Filter resources by status (success or fail) Enum: "success", "fail" |

#### Responses

##### 200

OK Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No |  |
| `links` | object | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The delivery's unique identifier |
| `status` | string | Yes | The status of delivery Enum: "success", "fail" |
| `request` | object | No | The request that was sent to the webhook URL for this delivery. |
| `response` | object | No | The response that was received from the webhook URL for this delivery. Absent if no response was received. |
| `eventType` | string | Yes | The name of the triggering event-type |
| `webhookId` | string | Yes | The unique webhook identifier that the delivery is for |
| `triggeredAt` | string | Yes | The UTC timestamp when the delivery was triggered |
| `statusMessage` | string | No | The status message of the delivery |

<details>
<summary>Properties of `request`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `url` | string | No | URL used for this delivery |
| `body` | object | No | The sent body/payload of the delivery |
| `headers` | object | No | Headers sent for this delivery, values of encryptedHeaders are omitted as such "**OMITTED**". Maximum combined size: 2048 bytes for non-encrypted headers + 2048 bytes for encrypted headers. |

</details>

<details>
<summary>Properties of `response`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `body` | string | No | The received body of the delivery |
| `headers` | object | No | Headers received for this delivery, values of encryptedHeaders are omitted as such "**OMITTED**". Maximum combined size: 2048 bytes for non-encrypted headers + 2048 bytes for encrypted headers. |
| `statusCode` | number | No | The HTTP status code of the response |

</details>

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `next` | object | No |  |
| `prev` | object | No |  |
| `self` | object | No |  |

<details>
<summary>Properties of `next`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL to a resource request |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL to a resource request |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | Yes | URL to a resource request |

</details>

</details>

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/core/webhooks/{id}/deliveries` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/core/webhooks/{id}/deliveries',
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
# qlik-cli has not implemented support for GET /api/core/webhooks/{id}/deliveries yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/core/webhooks/{id}/deliveries" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "string",
      "status": "success",
      "request": {
        "url": "string",
        "body": {},
        "headers": {
          "headerName": "headerValue",
          "encryptedHeadersName": "**OMITTED**"
        }
      },
      "response": {
        "body": "string",
        "headers": {
          "headerName": "headerValue",
          "encryptedHeadersName": "**OMITTED**"
        },
        "statusCode": 42
      },
      "eventType": "string",
      "webhookId": "string",
      "triggeredAt": "2025-07-02T08:20:35.49Z",
      "statusMessage": "string"
    }
  ],
  "links": {
    "next": {
      "href": "string"
    },
    "prev": {
      "href": "string"
    },
    "self": {
      "href": "string"
    }
  }
}
```

---

### GET /api/core/webhooks/{id}/deliveries/{deliveryId}

Returns details for a specific delivery.

- **Replaces:** "GET:/v1/webhooks/{id}/deliveries/{deliveryId}"
- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `deliveryId` | string | Yes | The delivery's unique identifier. |
| `id` | string | Yes | The webhook's unique identifier. |

#### Responses

##### 200

OK Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The delivery's unique identifier |
| `status` | string | Yes | The status of delivery Enum: "success", "fail" |
| `request` | object | No | The request that was sent to the webhook URL for this delivery. |
| `response` | object | No | The response that was received from the webhook URL for this delivery. Absent if no response was received. |
| `eventType` | string | Yes | The name of the triggering event-type |
| `webhookId` | string | Yes | The unique webhook identifier that the delivery is for |
| `triggeredAt` | string | Yes | The UTC timestamp when the delivery was triggered |
| `statusMessage` | string | No | The status message of the delivery |

<details>
<summary>Properties of `request`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `url` | string | No | URL used for this delivery |
| `body` | object | No | The sent body/payload of the delivery |
| `headers` | object | No | Headers sent for this delivery, values of encryptedHeaders are omitted as such "**OMITTED**". Maximum combined size: 2048 bytes for non-encrypted headers + 2048 bytes for encrypted headers. |

</details>

<details>
<summary>Properties of `response`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `body` | string | No | The received body of the delivery |
| `headers` | object | No | Headers received for this delivery, values of encryptedHeaders are omitted as such "**OMITTED**". Maximum combined size: 2048 bytes for non-encrypted headers + 2048 bytes for encrypted headers. |
| `statusCode` | number | No | The HTTP status code of the response |

</details>

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/core/webhooks/{id}/deliveries/{deliveryId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/core/webhooks/{id}/deliveries/{deliveryId}',
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
# qlik-cli has not implemented support for GET /api/core/webhooks/{id}/deliveries/{deliveryId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/core/webhooks/{id}/deliveries/{deliveryId}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "string",
  "status": "success",
  "request": {
    "url": "string",
    "body": {},
    "headers": {
      "headerName": "headerValue",
      "encryptedHeadersName": "**OMITTED**"
    }
  },
  "response": {
    "body": "string",
    "headers": {
      "headerName": "headerValue",
      "encryptedHeadersName": "**OMITTED**"
    },
    "statusCode": 42
  },
  "eventType": "string",
  "webhookId": "string",
  "triggeredAt": "2025-07-02T08:20:35.49Z",
  "statusMessage": "string"
}
```

---

### POST /api/core/webhooks/{id}/deliveries/{deliveryId}/actions/resend

Resends the event payload of an existing delivery and returns the new delivery. The event payload is taken from the original delivery, but the webhook's current configuration (URL, headers, secret and certificate settings) is used to send it. The resend is attempted synchronously and a new delivery record is always created, so a `201` response can contain a delivery with status `fail`. A resend is subject to the same validation and failure handling as an automatic delivery, so a webhook that is no longer valid or that exceeds the delivery failure threshold can be disabled as a result.

- **Replaces:** "POST:/v1/webhooks/{id}/deliveries/{deliveryId}/actions/resend"
- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `deliveryId` | string | Yes | The delivery's unique identifier. |
| `id` | string | Yes | The webhook's unique identifier. |

#### Responses

##### 201

A new delivery was created for the resend attempt. Check `status` to see whether the delivery itself succeeded or failed.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The delivery's unique identifier |
| `status` | string | Yes | The status of delivery Enum: "success", "fail" |
| `request` | object | No | The request that was sent to the webhook URL for this delivery. |
| `response` | object | No | The response that was received from the webhook URL for this delivery. Absent if no response was received. |
| `eventType` | string | Yes | The name of the triggering event-type |
| `webhookId` | string | Yes | The unique webhook identifier that the delivery is for |
| `triggeredAt` | string | Yes | The UTC timestamp when the delivery was triggered |
| `statusMessage` | string | No | The status message of the delivery |

<details>
<summary>Properties of `request`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `url` | string | No | URL used for this delivery |
| `body` | object | No | The sent body/payload of the delivery |
| `headers` | object | No | Headers sent for this delivery, values of encryptedHeaders are omitted as such "**OMITTED**". Maximum combined size: 2048 bytes for non-encrypted headers + 2048 bytes for encrypted headers. |

</details>

<details>
<summary>Properties of `response`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `body` | string | No | The received body of the delivery |
| `headers` | object | No | Headers received for this delivery, values of encryptedHeaders are omitted as such "**OMITTED**". Maximum combined size: 2048 bytes for non-encrypted headers + 2048 bytes for encrypted headers. |
| `statusCode` | number | No | The HTTP status code of the response |

</details>

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 403

The request is not allowed, for example because the user lacks the required permissions or the event-type of the delivery is not enabled for the tenant.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 404

Not found

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/core/webhooks/{id}/deliveries/{deliveryId}/actions/resend` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/core/webhooks/{id}/deliveries/{deliveryId}/actions/resend',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/core/webhooks/{id}/deliveries/{deliveryId}/actions/resend yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/core/webhooks/{id}/deliveries/{deliveryId}/actions/resend" \
-X POST \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "string",
  "status": "success",
  "request": {
    "url": "string",
    "body": {},
    "headers": {
      "headerName": "headerValue",
      "encryptedHeadersName": "**OMITTED**"
    }
  },
  "response": {
    "body": "string",
    "headers": {
      "headerName": "headerValue",
      "encryptedHeadersName": "**OMITTED**"
    },
    "statusCode": 42
  },
  "eventType": "string",
  "webhookId": "string",
  "triggeredAt": "2025-07-02T08:20:35.49Z",
  "statusMessage": "string"
}
```

---

### GET /api/core/webhooks/event-types

Lists event-types that are possible to subscribe to.

- **Replaces:** "GET:/v1/webhooks/event-types"
- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Responses

##### 200

OK Response

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No | Name of the event type |
| `title` | string | No | Title of the event type |
| `levels` | string[] | No | Specifies which levels that are supported for this event type |
| `category` | string | No | Category of the event type |
| `description` | string | No | Description of the event type |
| `allowedFilters` | object[] | No | The set of fields that can be used to filter this specific event type for webhook delivery. Different event types may support different filter paths. |

<details>
<summary>Properties of `allowedFilters`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `path` | string | Yes | The field name or path that can be used as a filter |
| `allowedValues` | string[] | No | Optional allowed values for this filter path. If omitted, the path is treated as free-form and clients are responsible for valid usage. |

</details>

</details>

##### 401

Unauthorized

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 500

Internal Server Error

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

##### 503

Service Unavailable

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | A way to trace the source of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error |
| `title` | string | Yes | A summary of what went wrong |
| `detail` | string | No | May be used to provide additional details |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/core/webhooks/event-types` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/core/webhooks/event-types',
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
# qlik-cli has not implemented support for GET /api/core/webhooks/event-types yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/core/webhooks/event-types" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "name": "string",
      "title": "string",
      "levels": [
        "string"
      ],
      "category": "string",
      "description": "string",
      "allowedFilters": [
        {
          "path": "data.status",
          "allowedValues": [
            "SUCCEEDED",
            "FAILED",
            "CANCELED",
            "EXCEEDED_LIMIT"
          ]
        }
      ]
    }
  ]
}
```

---
