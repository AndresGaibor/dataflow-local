# Direct Access Agents

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

API for remotely managing configuration settings of Direct Access Gateway agents.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `POST` | [`/api/v1/direct-access-agents/{agentId}/actions/{agentAction}`](#post-apiv1direct-access-agentsagentidactionsagentaction) | Restarts the specified agent. The `restart` action is rejected with `409` while a reload is in `RELOADING` status. The `force-restart` action cancels the active reloads and restarts the agent. The requestor must have the `TenantAdmin` role and be either the gateway's space owner or a member of the gateway's space with the `Can Consume Data` role. Available in Direct Access Gateway V1.7.2+. |
| `POST` | [`/api/v1/direct-access-agents/{agentId}/benchmarks`](#post-apiv1direct-access-agentsagentidbenchmarks) | Starts a background benchmark task that measures the throughput and latency of a Direct Access agent. Use the returned `benchmarkId` to monitor progress and retrieve performance metrics for capacity planning or performance optimization. The requestor must have the `TenantAdmin` role and be either the gateway's space owner or a member of the gateway's space with the `Can Consume Data` role. Available in Direct Access Gateway V1.7.8+. |
| `GET` | [`/api/v1/direct-access-agents/{agentId}/benchmarks/{benchmarkId}`](#get-apiv1direct-access-agentsagentidbenchmarksbenchmarkid) | Retrieves the current status, progress, and performance metrics for a benchmark task. Use this operation to monitor a running benchmark or inspect its completed results. The requestor must have the `TenantAdmin` role and be either the gateway's space owner or a member of the gateway's space with the `Can Consume Data` role. Available in Direct Access Gateway V1.7.8+. |
| `POST` | [`/api/v1/direct-access-agents/{agentId}/benchmarks/{benchmarkId}/cancel`](#post-apiv1direct-access-agentsagentidbenchmarksbenchmarkidcancel) | Requests cancellation of a running benchmark for the specified agent. The request is asynchronous. Use the returned status URL to monitor when cancellation completes. The requestor must have the `TenantAdmin` role and be either the gateway's space owner or a member of the gateway's space with the `Can Consume Data` role. Available in Direct Access Gateway V1.7.8+. |
| `GET` | [`/api/v1/direct-access-agents/{agentId}/configurations`](#get-apiv1direct-access-agentsagentidconfigurations) | Retrieves the connector agent configuration from the specified agent. The requestor must have the `TenantAdmin` role and be either the gateway's space owner or a member of the gateway's space with the `Can Consume Data` role. Available in Direct Access Gateway V1.7.2+. |
| `PATCH` | [`/api/v1/direct-access-agents/{agentId}/configurations`](#patch-apiv1direct-access-agentsagentidconfigurations) | Makes changes to the local agent configuration using JSON Patch. The requestor must have the `TenantAdmin` role and be either the gateway's space owner or a member of the gateway's space with the `Can Consume Data` role. Available in Direct Access Gateway V1.7.2+. |
| `GET` | [`/api/v1/direct-access-agents/{agentId}/connectors/{connectorType}/files`](#get-apiv1direct-access-agentsagentidconnectorsconnectortypefiles) | Lists the configuration files of the connector: `file-connector`: `plain-text-configuration`, `allowed-paths`, `custom-allowed-extensions`; `rest-connector`: `plain-text-configuration`; `odbc-connector`: `allowed-drivers`, `allowed-dsns`, `custom-data-type-mappings`. `plain-text-configuration` and `custom-allowed-extensions` are read and written as raw lines through `connectors/{connectorType}/files/{fileType}`; the other files have dedicated typed operations. The requestor must have the `TenantAdmin` role and be either the gateway's space owner or a member of the gateway's space with the `Can Consume Data` role. Available in Direct Access Gateway V1.7.4+. |
| `GET` | [`/api/v1/direct-access-agents/{agentId}/connectors/{connectorType}/files/{fileType}`](#get-apiv1direct-access-agentsagentidconnectorsconnectortypefilesfiletype) | Retrieves the configuration items in the flat file for the specified connector, as raw lines. Raw-lines files per connector: `file-connector`: `plain-text-configuration`, `custom-allowed-extensions`; `rest-connector`: `plain-text-configuration`. The other files listed by `connectors/{connectorType}/files` (`custom-data-type-mappings`, `allowed-paths`, `allowed-dsns` and `allowed-drivers`) are typed and have dedicated operations. The requestor must have the `TenantAdmin` role and be either the gateway's space owner or a member of the gateway's space with the `Can Consume Data` role. Available in Direct Access Gateway V1.7.4+. |
| `PUT` | [`/api/v1/direct-access-agents/{agentId}/connectors/{connectorType}/files/{fileType}`](#put-apiv1direct-access-agentsagentidconnectorsconnectortypefilesfiletype) | Completely replaces the contents of the connector's configuration file with the given raw lines. Partial updates are not supported. Omitting `contentsToSave` or sending `null` is treated as an empty list and clears the file. Raw-lines files per connector: `file-connector`: `plain-text-configuration`, `custom-allowed-extensions`; `rest-connector`: `plain-text-configuration`. The other files listed by `connectors/{connectorType}/files` (`custom-data-type-mappings`, `allowed-paths`, `allowed-dsns` and `allowed-drivers`) are typed and have dedicated operations. The requestor must have the `TenantAdmin` role and be either the gateway's space owner or a member of the gateway's space with the `Can Consume Data` role. Available in Direct Access Gateway V1.7.4+. |
| `GET` | [`/api/v1/direct-access-agents/{agentId}/connectors/file-connector/files/allowed-paths`](#get-apiv1direct-access-agentsagentidconnectorsfile-connectorfilesallowed-paths) | Retrieves the allowed paths settings for the File Connector. The requestor must have the `TenantAdmin` role and be either the gateway's space owner or a member of the gateway's space with the `Can Consume Data` role. Available in Direct Access Gateway V1.7.6+. |
| `PUT` | [`/api/v1/direct-access-agents/{agentId}/connectors/file-connector/files/allowed-paths`](#put-apiv1direct-access-agentsagentidconnectorsfile-connectorfilesallowed-paths) | Completely replaces the contents of the allowed paths configuration file for the File Connector. Partial updates are not supported. Omitting `fileConnectorAllowedPaths` or sending `null` is treated as an empty list and clears the file. The requestor must have the `TenantAdmin` role and be either the gateway's space owner or a member of the gateway's space with the `Can Consume Data` role. Available in Direct Access Gateway V1.7.6+. |
| `GET` | [`/api/v1/direct-access-agents/{agentId}/connectors/odbc-connector/files/custom-data-type-mappings`](#get-apiv1direct-access-agentsagentidconnectorsodbc-connectorfilescustom-data-type-mappings) | Retrieves the custom data type mapping settings for the Generic ODBC Connector. The requestor must have the `TenantAdmin` role and be either the gateway's space owner or a member of the gateway's space with the `Can Consume Data` role. Available in Direct Access Gateway V1.7.5+. |
| `PUT` | [`/api/v1/direct-access-agents/{agentId}/connectors/odbc-connector/files/custom-data-type-mappings`](#put-apiv1direct-access-agentsagentidconnectorsodbc-connectorfilescustom-data-type-mappings) | Completely replaces the contents of the custom data type mapping configuration file for the Generic ODBC connector. Partial updates are not supported. Omitting `odbcCustomDataTypes` or sending `null` is treated as an empty list and clears the file. There are property naming differences between the API and the file contents. Use the API property format when making changes. The requestor must have the `TenantAdmin` role and be either the gateway's space owner or a member of the gateway's space with the `Can Consume Data` role. Available in Direct Access Gateway V1.7.5+. |
| `GET` | [`/api/v1/direct-access-agents/{agentId}/tools/metrics-collector/configuration`](#get-apiv1direct-access-agentsagentidtoolsmetrics-collectorconfiguration) | Retrieves the settings for the metrics collector. The requestor must have the `TenantAdmin` role and be either the gateway's space owner or a member of the gateway's space with the `Can Consume Data` role. Available in Direct Access Gateway V1.7.9+. |
| `PUT` | [`/api/v1/direct-access-agents/{agentId}/tools/metrics-collector/configuration`](#put-apiv1direct-access-agentsagentidtoolsmetrics-collectorconfiguration) | Completely replaces the contents of the metrics collector settings configuration file. Partial updates are not supported. The requestor must have the `TenantAdmin` role and be either the gateway's space owner or a member of the gateway's space with the `Can Consume Data` role. Available in Direct Access Gateway V1.7.9+. |

## API Reference

### POST /api/v1/direct-access-agents/{agentId}/actions/{agentAction} _(deprecated)_

Restarts the specified agent. The `restart` action is rejected with `409` while a reload is in `RELOADING` status. The `force-restart` action cancels the active reloads and restarts the agent. The requestor must have the `TenantAdmin` role and be either the gateway's space owner or a member of the gateway's space with the `Can Consume Data` role. Available in Direct Access Gateway V1.7.2+.

- **Replaced by:** "POST:/connectivity/direct-access-agents/{agentId}/actions/{agentAction}"
- **Rate Limit:** Tier 2 (100 requests per minute)
- **Deprecated:** This endpoint is deprecated. Sunset date: 2027-11. Deprecated: replaced by the namespaced Direct Access Agents API under /api/connectivity/direct-access-agents, which exposes the same operations. See https://qlik.dev/apis/rest/connectivity/direct-access-agents/.

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `agentAction` | string | Yes | The type of action to perform. Permitted values are `restart` (rejected with `409` while a reload is in `RELOADING` status) and `force-restart` (cancels the active reloads and restarts the agent). |
| `agentId` | string | Yes | The ID of the Direct Access gateway, as shown in the gateway's settings dialog in the Management Console. |

#### Responses

##### 204

Service restarted successfully.

##### 400

The gateway version does not support this operation, or the request was invalid.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 403

The requestor does not have the required `TenantAdmin` role or the required permissions for the gateway's space.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 404

The gateway was not found, or the agent's Windows service does not exist.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 405

The agent runs on an operating system other than Windows or Linux, where restarting is not supported.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 409

A reload is in `RELOADING` status. Use `force-restart` to restart anyway.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 500

There was an error processing the request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/direct-access-agents/{agentId}/actions/{agentAction}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/direct-access-agents/{agentId}/actions/{agentAction}',
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
# qlik-cli has not implemented support for POST /api/v1/direct-access-agents/{agentId}/actions/{agentAction} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/direct-access-agents/{agentId}/actions/{agentAction}" \
-X POST \
-H "Authorization: Bearer <access_token>"
```

---

### POST /api/v1/direct-access-agents/{agentId}/benchmarks _(deprecated)_

Starts a background benchmark task that measures the throughput and latency of a Direct Access agent. Use the returned `benchmarkId` to monitor progress and retrieve performance metrics for capacity planning or performance optimization. The requestor must have the `TenantAdmin` role and be either the gateway's space owner or a member of the gateway's space with the `Can Consume Data` role. Available in Direct Access Gateway V1.7.8+.

- **Replaced by:** "POST:/connectivity/direct-access-agents/{agentId}/benchmarks"
- **Rate Limit:** Tier 2 (100 requests per minute)
- **Deprecated:** This endpoint is deprecated. Sunset date: 2027-11. Deprecated: replaced by the namespaced Direct Access Agents API under /api/connectivity/direct-access-agents, which exposes the same operations. See https://qlik.dev/apis/rest/connectivity/direct-access-agents/.

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `agentId` | string | Yes | The ID of the Direct Access gateway, as shown in the gateway's settings dialog in the Management Console. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `description` | string | No | The description for the benchmark task. |
| `force` | boolean | No | Forces the benchmark to start regardless of the state of the agent. Does not override QCS resource limits. Use with caution. |
| `gigaBytesToTransfer` | integer | No | The volume of data in GB to transfer during the throughput measurement part of the benchmark. Must be between 1 and 20. |
| `name` | string | No | The name to assign to the benchmark task. |

#### Responses

##### 201

Benchmark task created successfully with a unique identifier.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `benchmarkId` | string | No | The ID of the benchmark run, for the status and cancel operations. |

##### 400

Bad request, for example `gigaBytesToTransfer` outside 1 to 20.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 403

The requestor does not have the required `TenantAdmin` role or the required permissions for the gateway's space.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 404

The agent was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 500

There was an error processing the request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 501

Reserved; not returned by the current version of the service.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 503

Service is unavailable.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/direct-access-agents/{agentId}/benchmarks` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/direct-access-agents/{agentId}/benchmarks',
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
# qlik-cli has not implemented support for POST /api/v1/direct-access-agents/{agentId}/benchmarks yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/direct-access-agents/{agentId}/benchmarks" \
-X POST \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "benchmarkId": "string"
}
```

---

### GET /api/v1/direct-access-agents/{agentId}/benchmarks/{benchmarkId} _(deprecated)_

Retrieves the current status, progress, and performance metrics for a benchmark task. Use this operation to monitor a running benchmark or inspect its completed results. The requestor must have the `TenantAdmin` role and be either the gateway's space owner or a member of the gateway's space with the `Can Consume Data` role. Available in Direct Access Gateway V1.7.8+.

- **Replaced by:** "GET:/connectivity/direct-access-agents/{agentId}/benchmarks/{benchmarkId}"
- **Rate Limit:** Tier 1 (1000 requests per minute)
- **Deprecated:** This endpoint is deprecated. Sunset date: 2027-11. Deprecated: replaced by the namespaced Direct Access Agents API under /api/connectivity/direct-access-agents, which exposes the same operations. See https://qlik.dev/apis/rest/connectivity/direct-access-agents/.

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `agentId` | string | Yes | The ID of the Direct Access gateway, as shown in the gateway's settings dialog in the Management Console. |
| `benchmarkId` | string | Yes | The benchmark ID |

#### Responses

##### 200

Benchmark status and performance metrics retrieved successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No | The benchmark name |
| `status` | string | No | The benchmark status |
| `results` | object | No | Contains throughput, latency, transfer volume, and transmission timing for a benchmark. Present only when the benchmark status is `Completed`; `null` before that. |
| `benchmarkId` | string | No | The benchmark ID |
| `description` | string | No | The benchmark description |
| `statusMessage` | string | No | Additional details about the benchmark status |
| `benchmarkEndTime` | string | No | The ISO 8601 formatted timestamp when the benchmark task completed or was cancelled |
| `concurrentReloads` | integer | No | Number of concurrent benchmarks/reloads observed when this benchmark was started |
| `benchmarkStartTime` | string | No | The ISO 8601 formatted timestamp when the benchmark task started execution |
| `totalBytesRequested` | integer | No | The total bytes requested to be transferred during the benchmark |
| `getReloadSlotEndTime` | string | No | The ISO 8601 formatted timestamp when get reload slot completed |
| `dataGenerationEndTime` | string | No | The ISO 8601 formatted timestamp when data generation completed |
| `getReloadSlotStartTime` | string | No | The ISO 8601 formatted timestamp when get reload slot started |
| `dataGenerationStartTime` | string | No | The ISO 8601 formatted timestamp when data generation started |

<details>
<summary>Properties of `results`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `latency` | integer | No | The latency in ms measured during data transmission |
| `throughput` | integer | No | The data throughput in KB/s measured during data transmission |
| `connectorLatency` | integer | No | The average latency in ms measured on the connector side during data transmission. Null if no connector benchmark data is available. |
| `totalBytesTransferred` | integer | No | The total number of bytes successfully transferred during data transmission |
| `dataTransmissionEndTime` | string | No | The ISO 8601 formatted timestamp when data transmission completed |
| `dataTransmissionStartTime` | string | No | The ISO 8601 formatted timestamp when data transmission started |

</details>

##### 400

The gateway version does not support this operation, or the request was invalid.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 403

The requestor does not have the required `TenantAdmin` role or the required permissions for the gateway's space.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 404

The benchmark was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 500

There was an error processing the request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 503

Service is unavailable.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/direct-access-agents/{agentId}/benchmarks/{benchmarkId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/direct-access-agents/{agentId}/benchmarks/{benchmarkId}',
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
# qlik-cli has not implemented support for GET /api/v1/direct-access-agents/{agentId}/benchmarks/{benchmarkId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/direct-access-agents/{agentId}/benchmarks/{benchmarkId}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "name": "string",
  "status": "string",
  "results": {
    "latency": 42,
    "throughput": 42,
    "connectorLatency": 42,
    "totalBytesTransferred": 42,
    "dataTransmissionEndTime": "2026-03-11T20:54:34.437Z",
    "dataTransmissionStartTime": "2026-03-11T20:52:05.308Z"
  },
  "benchmarkId": "string",
  "description": "string",
  "statusMessage": "string",
  "benchmarkEndTime": "2026-03-11T20:54:34.438Z",
  "concurrentReloads": 42,
  "benchmarkStartTime": "2026-03-11T20:51:15.927Z",
  "totalBytesRequested": 42,
  "getReloadSlotEndTime": "2026-03-11T20:51:22.000Z",
  "dataGenerationEndTime": "2026-03-11T20:51:40.000Z",
  "getReloadSlotStartTime": "2026-03-11T20:51:20.000Z",
  "dataGenerationStartTime": "2026-03-11T20:51:23.000Z"
}
```

---

### POST /api/v1/direct-access-agents/{agentId}/benchmarks/{benchmarkId}/cancel _(deprecated)_

Requests cancellation of a running benchmark for the specified agent. The request is asynchronous. Use the returned status URL to monitor when cancellation completes. The requestor must have the `TenantAdmin` role and be either the gateway's space owner or a member of the gateway's space with the `Can Consume Data` role. Available in Direct Access Gateway V1.7.8+.

- **Replaced by:** "POST:/connectivity/direct-access-agents/{agentId}/benchmarks/{benchmarkId}/cancel"
- **Rate Limit:** Tier 2 (100 requests per minute)
- **Deprecated:** This endpoint is deprecated. Sunset date: 2027-11. Deprecated: replaced by the namespaced Direct Access Agents API under /api/connectivity/direct-access-agents, which exposes the same operations. See https://qlik.dev/apis/rest/connectivity/direct-access-agents/.

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `agentId` | string | Yes | The ID of the Direct Access gateway, as shown in the gateway's settings dialog in the Management Console. |
| `benchmarkId` | string | Yes | The benchmark ID |

#### Responses

##### 202

The cancellation was requested successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `message` | string | No | Confirmation text for the cancellation request. |
| `statusUrl` | object | No |  |

<details>
<summary>Properties of `statusUrl`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | The URL to the related resource |

</details>

##### 400

The gateway version does not support this operation, or the request was invalid.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 403

The requestor does not have the required `TenantAdmin` role or the required permissions for the gateway's space.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 404

The benchmark was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 500

There was an error processing the request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 503

Service is unavailable.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/direct-access-agents/{agentId}/benchmarks/{benchmarkId}/cancel` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/direct-access-agents/{agentId}/benchmarks/{benchmarkId}/cancel',
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
# qlik-cli has not implemented support for POST /api/v1/direct-access-agents/{agentId}/benchmarks/{benchmarkId}/cancel yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/direct-access-agents/{agentId}/benchmarks/{benchmarkId}/cancel" \
-X POST \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "message": "string",
  "statusUrl": {
    "href": "string"
  }
}
```

---

### GET /api/v1/direct-access-agents/{agentId}/configurations _(deprecated)_

Retrieves the connector agent configuration from the specified agent. The requestor must have the `TenantAdmin` role and be either the gateway's space owner or a member of the gateway's space with the `Can Consume Data` role. Available in Direct Access Gateway V1.7.2+.

- **Replaced by:** "GET:/connectivity/direct-access-agents/{agentId}/configurations"
- **Rate Limit:** Tier 1 (1000 requests per minute)
- **Deprecated:** This endpoint is deprecated. Sunset date: 2027-11. Deprecated: replaced by the namespaced Direct Access Agents API under /api/connectivity/direct-access-agents, which exposes the same operations. See https://qlik.dev/apis/rest/connectivity/direct-access-agents/.

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `agentId` | string | Yes | The ID of the Direct Access gateway, as shown in the gateway's settings dialog in the Management Console. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `queryProperties` | string[] | No | Individual properties within the agent configuration |

#### Responses

##### 200

The dictionary of key/value pairs retrieved from the configuration file.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `connectors` | object[] | No | The configuration settings of one connector. |
| `environment` | string | No | The environment the gateway reports it runs in. |
| `dcaasSettings` | object[] | No |  |
| `productVersion` | string | No | The Direct Access gateway product version. |
| `connectorAgentSettings` | object[] | No |  |

<details>
<summary>Properties of `connectors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `settings` | object[] | No | The connector's configuration settings. |
| `connectorName` | string | No | The connector name. |

<details>
<summary>Properties of `settings`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `ConfigurationLineNumeric` | object | No | A configuration setting with a numeric value. |

<details>
<summary>Properties of `ConfigurationLineNumeric`</summary>

_Properties truncated due to depth limit._

</details>

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `ConfigurationLineString` | object | No | A configuration setting with a string value. |

<details>
<summary>Properties of `ConfigurationLineString`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `dcaasSettings`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `ConfigurationLineNumeric` | object | No | A configuration setting with a numeric value. |

<details>
<summary>Properties of `ConfigurationLineNumeric`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No | The configuration key. |
| `value` | string | No | The current value, as a string. |
| `connector` | string | No | The connector or component the setting belongs to. |
| `uiActions` | string[] | No | The operations allowed on the setting in the gateway UI: `Read`, `Write`. Enum: "Read", "Write" |
| `apiActions` | string[] | No | The operations allowed on the setting through this API: `Read`, `Write`. Enum: "Read", "Write" |
| `description` | string | No | What the setting controls. |
| `displayName` | string | No | The human-readable name of the setting. |
| `defaultValue` | string | No | The default value, as a string. |
| `pendingValue` | string | No | The value that applies after the restart, when `pendingApplication` is `true`. |
| `skipValidation` | boolean | No | `true` when values are written without being validated against the permitted values. |
| `permittedRangeEnd` | integer | No | The highest permitted value. |
| `pendingApplication` | boolean | No | `true` when a new value was written but only applies after the agent restarts. |
| `allowMultipleValues` | boolean | No | `true` when the value is a list of values. |
| `applyWithoutRestart` | boolean | No | `true` when a change takes effect without restarting the agent. |
| `permittedRangeStart` | integer | No | The lowest permitted value. |

</details>

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `ConfigurationLineString` | object | No | A configuration setting with a string value. |

<details>
<summary>Properties of `ConfigurationLineString`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No | The configuration key. |
| `value` | string | No | The current value, as a string. |
| `connector` | string | No | The connector or component the setting belongs to. |
| `uiActions` | string[] | No | The operations allowed on the setting in the gateway UI: `Read`, `Write`. Enum: "Read", "Write" |
| `apiActions` | string[] | No | The operations allowed on the setting through this API: `Read`, `Write`. Enum: "Read", "Write" |
| `description` | string | No | What the setting controls. |
| `displayName` | string | No | The human-readable name of the setting. |
| `defaultValue` | string | No | The default value, as a string. |
| `pendingValue` | string | No | The value that applies after the restart, when `pendingApplication` is `true`. |
| `skipValidation` | boolean | No | `true` when values are written without being validated against the permitted values. |
| `permittedValues` | string[] | No | The permitted values; empty when any value is accepted. |
| `pendingApplication` | boolean | No | `true` when a new value was written but only applies after the agent restarts. |
| `allowMultipleValues` | boolean | No | `true` when the value is a list of values. |
| `applyWithoutRestart` | boolean | No | `true` when a change takes effect without restarting the agent. |

</details>

</details>

<details>
<summary>Properties of `connectorAgentSettings`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `ConfigurationLineNumeric` | object | No | A configuration setting with a numeric value. |

<details>
<summary>Properties of `ConfigurationLineNumeric`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No | The configuration key. |
| `value` | string | No | The current value, as a string. |
| `connector` | string | No | The connector or component the setting belongs to. |
| `uiActions` | string[] | No | The operations allowed on the setting in the gateway UI: `Read`, `Write`. Enum: "Read", "Write" |
| `apiActions` | string[] | No | The operations allowed on the setting through this API: `Read`, `Write`. Enum: "Read", "Write" |
| `description` | string | No | What the setting controls. |
| `displayName` | string | No | The human-readable name of the setting. |
| `defaultValue` | string | No | The default value, as a string. |
| `pendingValue` | string | No | The value that applies after the restart, when `pendingApplication` is `true`. |
| `skipValidation` | boolean | No | `true` when values are written without being validated against the permitted values. |
| `permittedRangeEnd` | integer | No | The highest permitted value. |
| `pendingApplication` | boolean | No | `true` when a new value was written but only applies after the agent restarts. |
| `allowMultipleValues` | boolean | No | `true` when the value is a list of values. |
| `applyWithoutRestart` | boolean | No | `true` when a change takes effect without restarting the agent. |
| `permittedRangeStart` | integer | No | The lowest permitted value. |

</details>

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `ConfigurationLineString` | object | No | A configuration setting with a string value. |

<details>
<summary>Properties of `ConfigurationLineString`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No | The configuration key. |
| `value` | string | No | The current value, as a string. |
| `connector` | string | No | The connector or component the setting belongs to. |
| `uiActions` | string[] | No | The operations allowed on the setting in the gateway UI: `Read`, `Write`. Enum: "Read", "Write" |
| `apiActions` | string[] | No | The operations allowed on the setting through this API: `Read`, `Write`. Enum: "Read", "Write" |
| `description` | string | No | What the setting controls. |
| `displayName` | string | No | The human-readable name of the setting. |
| `defaultValue` | string | No | The default value, as a string. |
| `pendingValue` | string | No | The value that applies after the restart, when `pendingApplication` is `true`. |
| `skipValidation` | boolean | No | `true` when values are written without being validated against the permitted values. |
| `permittedValues` | string[] | No | The permitted values; empty when any value is accepted. |
| `pendingApplication` | boolean | No | `true` when a new value was written but only applies after the agent restarts. |
| `allowMultipleValues` | boolean | No | `true` when the value is a list of values. |
| `applyWithoutRestart` | boolean | No | `true` when a change takes effect without restarting the agent. |

</details>

</details>

##### 400

The gateway version does not support this operation, or the request was invalid.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 403

The requestor does not have the required `TenantAdmin` role or the required permissions for the gateway's space.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 404

The gateway was not found, or the configuration file does not exist on the agent.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 500

There was an error processing the request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/direct-access-agents/{agentId}/configurations` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/direct-access-agents/{agentId}/configurations',
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
# qlik-cli has not implemented support for GET /api/v1/direct-access-agents/{agentId}/configurations yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/direct-access-agents/{agentId}/configurations" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "connectors": [
    {
      "settings": [
        {
          "name": "string",
          "value": "string",
          "connector": "string",
          "uiActions": [
            "Read"
          ],
          "apiActions": [
            "Read"
          ],
          "description": "string",
          "displayName": "string",
          "defaultValue": "string",
          "pendingValue": "string",
          "skipValidation": true,
          "permittedRangeEnd": 42,
          "pendingApplication": true,
          "allowMultipleValues": true,
          "applyWithoutRestart": true,
          "permittedRangeStart": 42
        }
      ],
      "connectorName": "string"
    }
  ],
  "environment": "string",
  "dcaasSettings": [
    {
      "name": "string",
      "value": "string",
      "connector": "string",
      "uiActions": [
        "Read"
      ],
      "apiActions": [
        "Read"
      ],
      "description": "string",
      "displayName": "string",
      "defaultValue": "string",
      "pendingValue": "string",
      "skipValidation": true,
      "permittedRangeEnd": 42,
      "pendingApplication": true,
      "allowMultipleValues": true,
      "applyWithoutRestart": true,
      "permittedRangeStart": 42
    }
  ],
  "productVersion": "string",
  "connectorAgentSettings": [
    {
      "name": "string",
      "value": "string",
      "connector": "string",
      "uiActions": [
        "Read"
      ],
      "apiActions": [
        "Read"
      ],
      "description": "string",
      "displayName": "string",
      "defaultValue": "string",
      "pendingValue": "string",
      "skipValidation": true,
      "permittedRangeEnd": 42,
      "pendingApplication": true,
      "allowMultipleValues": true,
      "applyWithoutRestart": true,
      "permittedRangeStart": 42
    }
  ]
}
```

---

### PATCH /api/v1/direct-access-agents/{agentId}/configurations _(deprecated)_

Makes changes to the local agent configuration using JSON Patch. The requestor must have the `TenantAdmin` role and be either the gateway's space owner or a member of the gateway's space with the `Can Consume Data` role. Available in Direct Access Gateway V1.7.2+.

- **Replaced by:** "PATCH:/connectivity/direct-access-agents/{agentId}/configurations"
- **Rate Limit:** Tier 2 (100 requests per minute)
- **Deprecated:** This endpoint is deprecated. Sunset date: 2027-11. Deprecated: replaced by the namespaced Direct Access Agents API under /api/connectivity/direct-access-agents, which exposes the same operations. See https://qlik.dev/apis/rest/connectivity/direct-access-agents/.

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `agentId` | string | Yes | The ID of the Direct Access gateway, as shown in the gateway's settings dialog in the Management Console. |

#### Request Body

The JSON Patch document

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | The operation. `remove` resets the property to its default value, or removes it when it has none. Enum: "add", "replace", "remove" |
| `path` | string | Yes | The configuration property to change. Enum: "AGENT_LOG_LEVEL", "AGENT_HEALTH_FAIL_MINUTES_LIMIT", "AGENT_LOG_OPTIONS", "EXTEND_FIRST_REQUEST_TIMEOUT", "RELOAD_CACHE_MEMORY_MB", "DCAAS_LOG_LEVEL", "ODBC_LOG_LEVEL", "ODBC_MAX_PROCESS_COUNT", "ODBC_PROCESS_ISOLATION_MODE", "ODBC_RELOAD_SESSION_LIFE", "SAPBW_LOG_LEVEL", "SAPBW_MAX_PROCESS_COUNT", "SAPBW_PROCESS_ISOLATION_MODE", "SAPSQL_LOG_LEVEL", "SAPSQL_MAX_PROCESS_COUNT", "SAPSQL_PROCESS_ISOLATION_MODE", "SAPPACKAGE_LOG_LEVEL", "SAPPACKAGE_MAX_PROCESS_COUNT", "SAPPACKAGE_PROCESS_ISOLATION_MODE", "FILE_LOG_LEVEL", "FILE_MAX_PROCESS_COUNT", "FILE_PROCESS_ISOLATION_MODE", "REST_LOG_LEVEL", "REST_MAX_PROCESS_COUNT", "REST_PROCESS_ISOLATION_MODE", "ODBC_TABLES_LIMIT_FOR_GENERICODBC", "OVERRIDE_CHUNKS_CACHE_DIR", "CHUNK_RECOVERY_RESUME_THRESHOLD_MINUTES", "REST_ALLOW_LOCALHOST_CONNECTION", "OPTIONAL_CAPABILITIES", "AGENT_LOG_MAX_FILE_SIZE_MB", "AGENT_LOG_RETENTION_DAYS", "METRICS_LOG_MAX_FILE_SIZE_MB", "METRICS_LOG_RETENTION_DAYS", "DCAAS_LOG_RETENTION_DAYS", "ODBC_LOG_RETENTION_DAYS", "SAPBW_LOG_RETENTION_DAYS", "SAPSQL_LOG_RETENTION_DAYS", "SAPPACKAGE_LOG_RETENTION_DAYS", "REST_LOG_RETENTION_DAYS", "FILE_LOG_RETENTION_DAYS", "BENCHMARK_LOAD_PERFORMANCE_METRICS_RECORDING_ENABLED", "BENCHMARK_RETENTION_CLEANUP_ENABLED", "BENCHMARK_RETENTION_DAYS", "BENCHMARK_RETENTION_CHECK_INTERVAL_MINUTES", "BENCHMARK_RETENTION_DB_SIZE_MB", "BENCHMARK_RETENTION_CLEANUP_BATCH_SIZE" |
| `value` | string | No | The new value. Required for `add` and `replace`; ignored for `remove`. |

**Content-Type:** `application/json-patch+json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | The operation. `remove` resets the property to its default value, or removes it when it has none. Enum: "add", "replace", "remove" |
| `path` | string | Yes | The configuration property to change. Enum: "AGENT_LOG_LEVEL", "AGENT_HEALTH_FAIL_MINUTES_LIMIT", "AGENT_LOG_OPTIONS", "EXTEND_FIRST_REQUEST_TIMEOUT", "RELOAD_CACHE_MEMORY_MB", "DCAAS_LOG_LEVEL", "ODBC_LOG_LEVEL", "ODBC_MAX_PROCESS_COUNT", "ODBC_PROCESS_ISOLATION_MODE", "ODBC_RELOAD_SESSION_LIFE", "SAPBW_LOG_LEVEL", "SAPBW_MAX_PROCESS_COUNT", "SAPBW_PROCESS_ISOLATION_MODE", "SAPSQL_LOG_LEVEL", "SAPSQL_MAX_PROCESS_COUNT", "SAPSQL_PROCESS_ISOLATION_MODE", "SAPPACKAGE_LOG_LEVEL", "SAPPACKAGE_MAX_PROCESS_COUNT", "SAPPACKAGE_PROCESS_ISOLATION_MODE", "FILE_LOG_LEVEL", "FILE_MAX_PROCESS_COUNT", "FILE_PROCESS_ISOLATION_MODE", "REST_LOG_LEVEL", "REST_MAX_PROCESS_COUNT", "REST_PROCESS_ISOLATION_MODE", "ODBC_TABLES_LIMIT_FOR_GENERICODBC", "OVERRIDE_CHUNKS_CACHE_DIR", "CHUNK_RECOVERY_RESUME_THRESHOLD_MINUTES", "REST_ALLOW_LOCALHOST_CONNECTION", "OPTIONAL_CAPABILITIES", "AGENT_LOG_MAX_FILE_SIZE_MB", "AGENT_LOG_RETENTION_DAYS", "METRICS_LOG_MAX_FILE_SIZE_MB", "METRICS_LOG_RETENTION_DAYS", "DCAAS_LOG_RETENTION_DAYS", "ODBC_LOG_RETENTION_DAYS", "SAPBW_LOG_RETENTION_DAYS", "SAPSQL_LOG_RETENTION_DAYS", "SAPPACKAGE_LOG_RETENTION_DAYS", "REST_LOG_RETENTION_DAYS", "FILE_LOG_RETENTION_DAYS", "BENCHMARK_LOAD_PERFORMANCE_METRICS_RECORDING_ENABLED", "BENCHMARK_RETENTION_CLEANUP_ENABLED", "BENCHMARK_RETENTION_DAYS", "BENCHMARK_RETENTION_CHECK_INTERVAL_MINUTES", "BENCHMARK_RETENTION_DB_SIZE_MB", "BENCHMARK_RETENTION_CLEANUP_BATCH_SIZE" |
| `value` | string | No | The new value. Required for `add` and `replace`; ignored for `remove`. |

#### Responses

##### 204

All operations were valid and applied.

##### 207

Some operations failed validation. The valid operations were applied; `data` lists every operation with its validation result.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | No | One entry per operation of the request, in request order. |
| `errorMessage` | string | No | The error text from the agent when the patch could not be processed; `null` otherwise. |
| `httpStatusCode` | integer | No | The status the agent reported for the patch: `204` all operations applied, `207` some applied, `400` none applied. |
| `failedPatchError` | object | No | The error structure of this API. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `valid` | boolean | No | `true` when the operation passed validation and was applied. |
| `operation` | object | No | A JSON Patch operation on one configuration property. |
| `validationResult` | string | No | Why the operation was rejected; `null` when it is valid. |

<details>
<summary>Properties of `operation`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | string | Yes | The operation. `remove` resets the property to its default value, or removes it when it has none. Enum: "add", "replace", "remove" |
| `path` | string | Yes | The configuration property to change. Enum: "AGENT_LOG_LEVEL", "AGENT_HEALTH_FAIL_MINUTES_LIMIT", "AGENT_LOG_OPTIONS", "EXTEND_FIRST_REQUEST_TIMEOUT", "RELOAD_CACHE_MEMORY_MB", "DCAAS_LOG_LEVEL", "ODBC_LOG_LEVEL", "ODBC_MAX_PROCESS_COUNT", "ODBC_PROCESS_ISOLATION_MODE", "ODBC_RELOAD_SESSION_LIFE", "SAPBW_LOG_LEVEL", "SAPBW_MAX_PROCESS_COUNT", "SAPBW_PROCESS_ISOLATION_MODE", "SAPSQL_LOG_LEVEL", "SAPSQL_MAX_PROCESS_COUNT", "SAPSQL_PROCESS_ISOLATION_MODE", "SAPPACKAGE_LOG_LEVEL", "SAPPACKAGE_MAX_PROCESS_COUNT", "SAPPACKAGE_PROCESS_ISOLATION_MODE", "FILE_LOG_LEVEL", "FILE_MAX_PROCESS_COUNT", "FILE_PROCESS_ISOLATION_MODE", "REST_LOG_LEVEL", "REST_MAX_PROCESS_COUNT", "REST_PROCESS_ISOLATION_MODE", "ODBC_TABLES_LIMIT_FOR_GENERICODBC", "OVERRIDE_CHUNKS_CACHE_DIR", "CHUNK_RECOVERY_RESUME_THRESHOLD_MINUTES", "REST_ALLOW_LOCALHOST_CONNECTION", "OPTIONAL_CAPABILITIES", "AGENT_LOG_MAX_FILE_SIZE_MB", "AGENT_LOG_RETENTION_DAYS", "METRICS_LOG_MAX_FILE_SIZE_MB", "METRICS_LOG_RETENTION_DAYS", "DCAAS_LOG_RETENTION_DAYS", "ODBC_LOG_RETENTION_DAYS", "SAPBW_LOG_RETENTION_DAYS", "SAPSQL_LOG_RETENTION_DAYS", "SAPPACKAGE_LOG_RETENTION_DAYS", "REST_LOG_RETENTION_DAYS", "FILE_LOG_RETENTION_DAYS", "BENCHMARK_LOAD_PERFORMANCE_METRICS_RECORDING_ENABLED", "BENCHMARK_RETENTION_CLEANUP_ENABLED", "BENCHMARK_RETENTION_DAYS", "BENCHMARK_RETENTION_CHECK_INTERVAL_MINUTES", "BENCHMARK_RETENTION_DB_SIZE_MB", "BENCHMARK_RETENTION_CLEANUP_BATCH_SIZE" |
| `value` | string | No | The new value. Required for `add` and `replace`; ignored for `remove`. |

</details>

</details>

<details>
<summary>Properties of `failedPatchError`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

</details>

##### 400

Bad request, or no operation passed validation (nothing was applied).

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 403

The requestor does not have the required `TenantAdmin` role or the required permissions for the gateway's space.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 404

The gateway was not found, or the configuration file does not exist on the agent.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 415

Unsupported content type. Send the JSON Patch document as `application/json-patch+json`; `application/json` is listed for API compliance only and is rejected.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 500

There was an error processing the request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PATCH /api/v1/direct-access-agents/{agentId}/configurations` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/direct-access-agents/{agentId}/configurations',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify([
      {
        op: 'add',
        path: 'AGENT_LOG_LEVEL',
        value: 'string',
      },
    ]),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/v1/direct-access-agents/{agentId}/configurations yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/direct-access-agents/{agentId}/configurations" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '[{"op":"add","path":"AGENT_LOG_LEVEL","value":"string"}]'
```

**Example Response:**

```json
{
  "data": [
    {
      "valid": true,
      "operation": {
        "op": "add",
        "path": "AGENT_LOG_LEVEL",
        "value": "string"
      },
      "validationResult": "string"
    }
  ],
  "errorMessage": "string",
  "httpStatusCode": 42,
  "failedPatchError": {
    "errors": [
      {
        "code": "string",
        "title": "string",
        "detail": "string"
      }
    ],
    "traceId": "string",
    "hasErrors": true
  }
}
```

---

### GET /api/v1/direct-access-agents/{agentId}/connectors/{connectorType}/files _(deprecated)_

Lists the configuration files of the connector: `file-connector`: `plain-text-configuration`, `allowed-paths`, `custom-allowed-extensions`; `rest-connector`: `plain-text-configuration`; `odbc-connector`: `allowed-drivers`, `allowed-dsns`, `custom-data-type-mappings`. `plain-text-configuration` and `custom-allowed-extensions` are read and written as raw lines through `connectors/{connectorType}/files/{fileType}`; the other files have dedicated typed operations. The requestor must have the `TenantAdmin` role and be either the gateway's space owner or a member of the gateway's space with the `Can Consume Data` role. Available in Direct Access Gateway V1.7.4+.

- **Replaced by:** "GET:/connectivity/direct-access-agents/{agentId}/connectors/{connectorType}/files"
- **Rate Limit:** Tier 1 (1000 requests per minute)
- **Deprecated:** This endpoint is deprecated. Sunset date: 2027-11. Deprecated: replaced by the namespaced Direct Access Agents API under /api/connectivity/direct-access-agents, which exposes the same operations. See https://qlik.dev/apis/rest/connectivity/direct-access-agents/.

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `agentId` | string | Yes | The ID of the Direct Access gateway, as shown in the gateway's settings dialog in the Management Console. |
| `connectorType` | string | Yes | The connector to retrieve the list of files for Enum: "file-connector", "rest-connector", "odbc-connector" |

#### Responses

##### 200

The list of files for the specified connector.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `result` | string[] | No | The file contents. |
| `errorMessage` | object | No | The error structure of this API. |

<details>
<summary>Properties of `errorMessage`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

</details>

##### 400

The gateway version does not support this operation, or the request was invalid.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 403

The requestor does not have the required `TenantAdmin` role or the required permissions for the gateway's space.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 404

The gateway was not found, or the configuration file does not exist on the agent.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 500

There was an error processing the request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/direct-access-agents/{agentId}/connectors/{connectorType}/files` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/direct-access-agents/{agentId}/connectors/{connectorType}/files',
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
# qlik-cli has not implemented support for GET /api/v1/direct-access-agents/{agentId}/connectors/{connectorType}/files yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/direct-access-agents/{agentId}/connectors/{connectorType}/files" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "result": [
    "string"
  ],
  "errorMessage": {
    "errors": [
      {
        "code": "string",
        "title": "string",
        "detail": "string"
      }
    ],
    "traceId": "string",
    "hasErrors": true
  }
}
```

---

### GET /api/v1/direct-access-agents/{agentId}/connectors/{connectorType}/files/{fileType} _(deprecated)_

Retrieves the configuration items in the flat file for the specified connector, as raw lines. Raw-lines files per connector: `file-connector`: `plain-text-configuration`, `custom-allowed-extensions`; `rest-connector`: `plain-text-configuration`. The other files listed by `connectors/{connectorType}/files` (`custom-data-type-mappings`, `allowed-paths`, `allowed-dsns` and `allowed-drivers`) are typed and have dedicated operations. The requestor must have the `TenantAdmin` role and be either the gateway's space owner or a member of the gateway's space with the `Can Consume Data` role. Available in Direct Access Gateway V1.7.4+.

- **Replaced by:** "GET:/connectivity/direct-access-agents/{agentId}/connectors/{connectorType}/files/{fileType}"
- **Rate Limit:** Tier 1 (1000 requests per minute)
- **Deprecated:** This endpoint is deprecated. Sunset date: 2027-11. Deprecated: replaced by the namespaced Direct Access Agents API under /api/connectivity/direct-access-agents, which exposes the same operations. See https://qlik.dev/apis/rest/connectivity/direct-access-agents/.

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `agentId` | string | Yes | The ID of the Direct Access gateway, as shown in the gateway's settings dialog in the Management Console. |
| `connectorType` | string | Yes | The connector type to retrieve Enum: "file-connector", "rest-connector", "odbc-connector" |
| `fileType` | string | Yes | The type of file to retrieve. Case-insensitive; the file names returned by `connectors/{connectorType}/files` (for example `plain-text-configuration`) are accepted as well. `custom-data-type-mappings`, `allowed-paths`, `allowed-dsns` and `allowed-drivers` are managed through their dedicated operations and are rejected here with `400`. Enum: "CustomTypesMapping", "PlainTextConfiguration", "AllowedPaths", "AllowedDrivers", "AllowedDsns", "CustomAllowedExtensions" |

#### Responses

##### 200

The lines of the file.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `result` | string[] | No | The file contents. |
| `errorMessage` | object | No | The error structure of this API. |

<details>
<summary>Properties of `errorMessage`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

</details>

##### 400

Unknown `fileType`, or a file type with a dedicated operation (`custom-data-type-mappings`, `allowed-paths`, `allowed-dsns` and `allowed-drivers`); use that operation instead.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 403

The requestor does not have the required `TenantAdmin` role or the required permissions for the gateway's space.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 404

The gateway was not found, or the configuration file does not exist on the agent.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 500

There was an error processing the request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/direct-access-agents/{agentId}/connectors/{connectorType}/files/{fileType}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/direct-access-agents/{agentId}/connectors/{connectorType}/files/{fileType}',
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
# qlik-cli has not implemented support for GET /api/v1/direct-access-agents/{agentId}/connectors/{connectorType}/files/{fileType} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/direct-access-agents/{agentId}/connectors/{connectorType}/files/{fileType}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "result": [
    "string"
  ],
  "errorMessage": {
    "errors": [
      {
        "code": "string",
        "title": "string",
        "detail": "string"
      }
    ],
    "traceId": "string",
    "hasErrors": true
  }
}
```

---

### PUT /api/v1/direct-access-agents/{agentId}/connectors/{connectorType}/files/{fileType} _(deprecated)_

Completely replaces the contents of the connector's configuration file with the given raw lines. Partial updates are not supported. Omitting `contentsToSave` or sending `null` is treated as an empty list and clears the file. Raw-lines files per connector: `file-connector`: `plain-text-configuration`, `custom-allowed-extensions`; `rest-connector`: `plain-text-configuration`. The other files listed by `connectors/{connectorType}/files` (`custom-data-type-mappings`, `allowed-paths`, `allowed-dsns` and `allowed-drivers`) are typed and have dedicated operations. The requestor must have the `TenantAdmin` role and be either the gateway's space owner or a member of the gateway's space with the `Can Consume Data` role. Available in Direct Access Gateway V1.7.4+.

- **Replaced by:** "PUT:/connectivity/direct-access-agents/{agentId}/connectors/{connectorType}/files/{fileType}"
- **Rate Limit:** Tier 2 (100 requests per minute)
- **Deprecated:** This endpoint is deprecated. Sunset date: 2027-11. Deprecated: replaced by the namespaced Direct Access Agents API under /api/connectivity/direct-access-agents, which exposes the same operations. See https://qlik.dev/apis/rest/connectivity/direct-access-agents/.

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `agentId` | string | Yes | The ID of the Direct Access gateway, as shown in the gateway's settings dialog in the Management Console. |
| `connectorType` | string | Yes | The connector type to update Enum: "file-connector", "rest-connector", "odbc-connector" |
| `fileType` | string | Yes | The file type to update. Case-insensitive; the file names returned by `connectors/{connectorType}/files` (for example `plain-text-configuration`) are accepted as well. `custom-data-type-mappings`, `allowed-paths`, `allowed-dsns` and `allowed-drivers` are managed through their dedicated operations and are rejected here with `400`. Enum: "CustomTypesMapping", "PlainTextConfiguration", "AllowedPaths", "AllowedDrivers", "AllowedDsns", "CustomAllowedExtensions" |

#### Request Body

The contents of the file to be updated

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `contentsToSave` | string[] | No | The lines to write, in order; they replace the whole file. |

#### Responses

##### 204

The file was replaced.

##### 400

Bad request, unknown `fileType`, or a file type with a dedicated operation (`custom-data-type-mappings`, `allowed-paths`, `allowed-dsns` and `allowed-drivers`); use that operation instead.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 403

The requestor does not have the required `TenantAdmin` role or the required permissions for the gateway's space.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 404

The gateway was not found, or the configuration file does not exist on the agent.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 409

A reload is in progress on the agent and the file was not changed; retry when the reload completes.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 500

There was an error processing the request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PUT /api/v1/direct-access-agents/{agentId}/connectors/{connectorType}/files/{fileType}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/direct-access-agents/{agentId}/connectors/{connectorType}/files/{fileType}',
  {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      contentsToSave: ['C:\\\\filepath'],
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PUT /api/v1/direct-access-agents/{agentId}/connectors/{connectorType}/files/{fileType} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/direct-access-agents/{agentId}/connectors/{connectorType}/files/{fileType}" \
-X PUT \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"contentsToSave":["C:\\\\filepath"]}'
```

---

### GET /api/v1/direct-access-agents/{agentId}/connectors/file-connector/files/allowed-paths _(deprecated)_

Retrieves the allowed paths settings for the File Connector. The requestor must have the `TenantAdmin` role and be either the gateway's space owner or a member of the gateway's space with the `Can Consume Data` role. Available in Direct Access Gateway V1.7.6+.

- **Replaced by:** "GET:/connectivity/direct-access-agents/{agentId}/connectors/file-connector/files/allowed-paths"
- **Rate Limit:** Tier 1 (1000 requests per minute)
- **Deprecated:** This endpoint is deprecated. Sunset date: 2027-11. Deprecated: replaced by the namespaced Direct Access Agents API under /api/connectivity/direct-access-agents, which exposes the same operations. See https://qlik.dev/apis/rest/connectivity/direct-access-agents/.

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `agentId` | string | Yes | The ID of the Direct Access gateway, as shown in the gateway's settings dialog in the Management Console. |

#### Responses

##### 200

The allowed paths.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `result` | object[] | No | The file contents. |
| `errorMessage` | object | No | The error structure of this API. |

<details>
<summary>Properties of `result`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `path` | string | Yes | The Path property in the File connector allowed paths file. |
| `spaces` | string[] | No | The Spaces property in the File connector allowed paths file. |

</details>

<details>
<summary>Properties of `errorMessage`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

</details>

##### 400

The gateway version does not support this operation, or the request was invalid.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 403

The requestor does not have the required `TenantAdmin` role or the required permissions for the gateway's space.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 404

The gateway was not found, or the configuration file does not exist on the agent.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 500

There was an error processing the request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/direct-access-agents/{agentId}/connectors/file-connector/files/allowed-paths` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/direct-access-agents/{agentId}/connectors/file-connector/files/allowed-paths',
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
# qlik-cli has not implemented support for GET /api/v1/direct-access-agents/{agentId}/connectors/file-connector/files/allowed-paths yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/direct-access-agents/{agentId}/connectors/file-connector/files/allowed-paths" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "result": [
    {
      "path": "\\\\\\\\Server\\\\Share\\\\example",
      "spaces": [
        "Foo",
        "Bar"
      ]
    }
  ],
  "errorMessage": {
    "errors": [
      {
        "code": "string",
        "title": "string",
        "detail": "string"
      }
    ],
    "traceId": "string",
    "hasErrors": true
  }
}
```

---

### PUT /api/v1/direct-access-agents/{agentId}/connectors/file-connector/files/allowed-paths _(deprecated)_

Completely replaces the contents of the allowed paths configuration file for the File Connector. Partial updates are not supported. Omitting `fileConnectorAllowedPaths` or sending `null` is treated as an empty list and clears the file. The requestor must have the `TenantAdmin` role and be either the gateway's space owner or a member of the gateway's space with the `Can Consume Data` role. Available in Direct Access Gateway V1.7.6+.

- **Replaced by:** "PUT:/connectivity/direct-access-agents/{agentId}/connectors/file-connector/files/allowed-paths"
- **Rate Limit:** Tier 2 (100 requests per minute)
- **Deprecated:** This endpoint is deprecated. Sunset date: 2027-11. Deprecated: replaced by the namespaced Direct Access Agents API under /api/connectivity/direct-access-agents, which exposes the same operations. See https://qlik.dev/apis/rest/connectivity/direct-access-agents/.

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `agentId` | string | Yes | The ID of the Direct Access gateway, as shown in the gateway's settings dialog in the Management Console. |

#### Request Body

The contents of the file to be updated

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fileConnectorAllowedPaths` | object[] | No | The allowed paths; they replace the whole file. |

<details>
<summary>Properties of `fileConnectorAllowedPaths`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `path` | string | Yes | The Path property in the File connector allowed paths file. |
| `spaces` | string[] | No | The Spaces property in the File connector allowed paths file. |

</details>

#### Responses

##### 204

The file was replaced.

##### 400

Invalid request body, or the gateway version does not support this operation.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 403

The requestor does not have the required `TenantAdmin` role or the required permissions for the gateway's space.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 404

The gateway was not found, or the configuration file does not exist on the agent.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 409

A reload is in progress on the agent and the file was not changed; retry when the reload completes.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 500

There was an error processing the request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PUT /api/v1/direct-access-agents/{agentId}/connectors/file-connector/files/allowed-paths` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/direct-access-agents/{agentId}/connectors/file-connector/files/allowed-paths',
  {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      fileConnectorAllowedPaths: [
        {
          path: '\\\\\\\\Server\\\\Share\\\\example',
          spaces: ['Foo', 'Bar'],
        },
      ],
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PUT /api/v1/direct-access-agents/{agentId}/connectors/file-connector/files/allowed-paths yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/direct-access-agents/{agentId}/connectors/file-connector/files/allowed-paths" \
-X PUT \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"fileConnectorAllowedPaths":[{"path":"\\\\\\\\Server\\\\Share\\\\example","spaces":["Foo","Bar"]}]}'
```

---

### GET /api/v1/direct-access-agents/{agentId}/connectors/odbc-connector/files/custom-data-type-mappings _(deprecated)_

Retrieves the custom data type mapping settings for the Generic ODBC Connector. The requestor must have the `TenantAdmin` role and be either the gateway's space owner or a member of the gateway's space with the `Can Consume Data` role. Available in Direct Access Gateway V1.7.5+.

- **Replaced by:** "GET:/connectivity/direct-access-agents/{agentId}/connectors/odbc-connector/files/custom-data-type-mappings"
- **Rate Limit:** Tier 1 (1000 requests per minute)
- **Deprecated:** This endpoint is deprecated. Sunset date: 2027-11. Deprecated: replaced by the namespaced Direct Access Agents API under /api/connectivity/direct-access-agents, which exposes the same operations. See https://qlik.dev/apis/rest/connectivity/direct-access-agents/.

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `agentId` | string | Yes | The ID of the Direct Access gateway, as shown in the gateway's settings dialog in the Management Console. |

#### Responses

##### 200

The custom data type mappings.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `result` | object[] | No | The file contents. |
| `errorMessage` | object | No | The error structure of this API. |

<details>
<summary>Properties of `result`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The Identifier property in the ODBC custom data type mapping file. |
| `bit` | boolean | No | The IsBit property in the ODBC custom data type mapping file. |
| `size` | integer | No | The Size property in the ODBC custom data type mapping file. |
| `qlikDataType` | string | Yes | The QlikDataType property in the ODBC custom data type mapping file. |
| `nativeDataType` | string | Yes | The NativeDataType property in the ODBC custom data type mapping file. |

</details>

<details>
<summary>Properties of `errorMessage`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

</details>

##### 400

The gateway version does not support this operation, or the request was invalid.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 403

The requestor does not have the required `TenantAdmin` role or the required permissions for the gateway's space.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 404

The gateway was not found, or the configuration file does not exist on the agent.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 500

There was an error processing the request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/direct-access-agents/{agentId}/connectors/odbc-connector/files/custom-data-type-mappings` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/direct-access-agents/{agentId}/connectors/odbc-connector/files/custom-data-type-mappings',
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
# qlik-cli has not implemented support for GET /api/v1/direct-access-agents/{agentId}/connectors/odbc-connector/files/custom-data-type-mappings yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/direct-access-agents/{agentId}/connectors/odbc-connector/files/custom-data-type-mappings" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "result": [
    {
      "id": "Amazon Athena ODBC (x64)",
      "bit": true,
      "size": 0,
      "qlikDataType": "String",
      "nativeDataType": "varchar"
    }
  ],
  "errorMessage": {
    "errors": [
      {
        "code": "string",
        "title": "string",
        "detail": "string"
      }
    ],
    "traceId": "string",
    "hasErrors": true
  }
}
```

---

### PUT /api/v1/direct-access-agents/{agentId}/connectors/odbc-connector/files/custom-data-type-mappings _(deprecated)_

Completely replaces the contents of the custom data type mapping configuration file for the Generic ODBC connector. Partial updates are not supported. Omitting `odbcCustomDataTypes` or sending `null` is treated as an empty list and clears the file. There are property naming differences between the API and the file contents. Use the API property format when making changes. The requestor must have the `TenantAdmin` role and be either the gateway's space owner or a member of the gateway's space with the `Can Consume Data` role. Available in Direct Access Gateway V1.7.5+.

- **Replaced by:** "PUT:/connectivity/direct-access-agents/{agentId}/connectors/odbc-connector/files/custom-data-type-mappings"
- **Rate Limit:** Tier 2 (100 requests per minute)
- **Deprecated:** This endpoint is deprecated. Sunset date: 2027-11. Deprecated: replaced by the namespaced Direct Access Agents API under /api/connectivity/direct-access-agents, which exposes the same operations. See https://qlik.dev/apis/rest/connectivity/direct-access-agents/.

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `agentId` | string | Yes | The ID of the Direct Access gateway, as shown in the gateway's settings dialog in the Management Console. |

#### Request Body

The contents of the file to be updated.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `odbcCustomDataTypes` | object[] | No | The custom data type mappings; they replace the whole file. |

<details>
<summary>Properties of `odbcCustomDataTypes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The Identifier property in the ODBC custom data type mapping file. |
| `bit` | boolean | No | The IsBit property in the ODBC custom data type mapping file. |
| `size` | integer | No | The Size property in the ODBC custom data type mapping file. |
| `qlikDataType` | string | Yes | The QlikDataType property in the ODBC custom data type mapping file. |
| `nativeDataType` | string | Yes | The NativeDataType property in the ODBC custom data type mapping file. |

</details>

#### Responses

##### 204

The file was replaced.

##### 400

Invalid request body, or the gateway version does not support this operation.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 403

The requestor does not have the required `TenantAdmin` role or the required permissions for the gateway's space.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 404

The gateway was not found, or the configuration file does not exist on the agent.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 409

A reload is in progress on the agent and the file was not changed; retry when the reload completes.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 500

There was an error processing the request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PUT /api/v1/direct-access-agents/{agentId}/connectors/odbc-connector/files/custom-data-type-mappings` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/direct-access-agents/{agentId}/connectors/odbc-connector/files/custom-data-type-mappings',
  {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      odbcCustomDataTypes: [
        {
          id: 'Amazon Athena ODBC (x64)',
          bit: true,
          size: 0,
          qlikDataType: 'String',
          nativeDataType: 'varchar',
        },
      ],
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PUT /api/v1/direct-access-agents/{agentId}/connectors/odbc-connector/files/custom-data-type-mappings yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/direct-access-agents/{agentId}/connectors/odbc-connector/files/custom-data-type-mappings" \
-X PUT \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"odbcCustomDataTypes":[{"id":"Amazon Athena ODBC (x64)","bit":true,"size":0,"qlikDataType":"String","nativeDataType":"varchar"}]}'
```

---

### GET /api/v1/direct-access-agents/{agentId}/tools/metrics-collector/configuration _(deprecated)_

Retrieves the settings for the metrics collector. The requestor must have the `TenantAdmin` role and be either the gateway's space owner or a member of the gateway's space with the `Can Consume Data` role. Available in Direct Access Gateway V1.7.9+.

- **Replaced by:** "GET:/connectivity/direct-access-agents/{agentId}/tools/metrics-collector/configuration"
- **Rate Limit:** Tier 1 (1000 requests per minute)
- **Deprecated:** This endpoint is deprecated. Sunset date: 2027-11. Deprecated: replaced by the namespaced Direct Access Agents API under /api/connectivity/direct-access-agents, which exposes the same operations. See https://qlik.dev/apis/rest/connectivity/direct-access-agents/.

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `agentId` | string | Yes | The ID of the Direct Access gateway, as shown in the gateway's settings dialog in the Management Console. |

#### Responses

##### 200

The metrics collector settings and the per-connector scrape configurations.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `result` | object | No | The metrics collector configuration of the gateway. |
| `errorMessage` | object | No | The error structure of this API. |

<details>
<summary>Properties of `result`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `connectorConfigurations` | object | No | The scrape configuration per connector. |
| `metricsCollectorSettings` | object | No |  |

<details>
<summary>Properties of `connectorConfigurations`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fileConnector` | object | No |  |
| `odbcConnector` | object | No |  |
| `restConnector` | object | No |  |
| `systemMetrics` | object | No |  |
| `connectorAgent` | object | No |  |
| `sapBwConnector` | object | No |  |
| `sapSqlConnector` | object | No |  |
| `sapPackageConnector` | object | No |  |

<details>
<summary>Properties of `fileConnector`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `odbcConnector`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `restConnector`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `systemMetrics`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `connectorAgent`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `sapBwConnector`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `sapSqlConnector`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `sapPackageConnector`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `metricsCollectorSettings`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `port` | integer | Yes | The port number that the metrics collector API will run on. This must match the port that the SYSTEM connector runs on to enable network metrics collection. |
| `enabled` | boolean | Yes | Indicates whether the metrics collector is enabled. |
| `localDataRetentionDays` | integer | Yes | The number of days to retain local data. |
| `baseScrapeIntervalSeconds` | integer | Yes | The base interval in seconds for the metrics collection loop. This defines how frequently the collector checks whether to scrape each connector, not the interval at which each connector is scraped. Must be equal to or less than the lowest individual connector scrape interval. |
| `localDatabaseFileLocation` | string | No | The file location for the local metrics database. When empty, the default applies: `%ProgramData%\Qlik\Gateway\tmp` on Windows, `/usr/share/Qlik/Gateway/tmp` in the containerized gateway. |
| `dataRetentionCheckIntervalMinutes` | integer | Yes | The interval in minutes the metrics collector checks for and deletes old data. |
| `localDataRetentionDatabaseSizeInMb` | integer | No | The maximum size of the local database in megabytes. |

</details>

</details>

<details>
<summary>Properties of `errorMessage`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

</details>

##### 400

The gateway version does not support this operation, or the request was invalid.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 403

The requestor does not have the required `TenantAdmin` role or the required permissions for the gateway's space.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 404

The gateway was not found, or the configuration file does not exist on the agent.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 500

There was an error processing the request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/direct-access-agents/{agentId}/tools/metrics-collector/configuration` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/direct-access-agents/{agentId}/tools/metrics-collector/configuration',
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
# qlik-cli has not implemented support for GET /api/v1/direct-access-agents/{agentId}/tools/metrics-collector/configuration yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/direct-access-agents/{agentId}/tools/metrics-collector/configuration" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "result": {
    "connectorConfigurations": {
      "fileConnector": {
        "scrapeIntervalSeconds": 30,
        "metricsCollectionEnabled": false
      },
      "odbcConnector": {
        "scrapeIntervalSeconds": 30,
        "metricsCollectionEnabled": false
      },
      "restConnector": {
        "scrapeIntervalSeconds": 30,
        "metricsCollectionEnabled": false
      },
      "systemMetrics": {
        "scrapeIntervalSeconds": 30,
        "metricsCollectionEnabled": false
      },
      "connectorAgent": {
        "scrapeIntervalSeconds": 30,
        "metricsCollectionEnabled": false
      },
      "sapBwConnector": {
        "scrapeIntervalSeconds": 30,
        "metricsCollectionEnabled": false
      },
      "sapSqlConnector": {
        "scrapeIntervalSeconds": 30,
        "metricsCollectionEnabled": false
      },
      "sapPackageConnector": {
        "scrapeIntervalSeconds": 30,
        "metricsCollectionEnabled": false
      }
    },
    "metricsCollectorSettings": {
      "port": 5052,
      "enabled": false,
      "localDataRetentionDays": 30,
      "baseScrapeIntervalSeconds": 1,
      "localDatabaseFileLocation": "",
      "dataRetentionCheckIntervalMinutes": 60,
      "localDataRetentionDatabaseSizeInMb": 500
    }
  },
  "errorMessage": {
    "errors": [
      {
        "code": "string",
        "title": "string",
        "detail": "string"
      }
    ],
    "traceId": "string",
    "hasErrors": true
  }
}
```

---

### PUT /api/v1/direct-access-agents/{agentId}/tools/metrics-collector/configuration _(deprecated)_

Completely replaces the contents of the metrics collector settings configuration file. Partial updates are not supported. The requestor must have the `TenantAdmin` role and be either the gateway's space owner or a member of the gateway's space with the `Can Consume Data` role. Available in Direct Access Gateway V1.7.9+.

- **Replaced by:** "PUT:/connectivity/direct-access-agents/{agentId}/tools/metrics-collector/configuration"
- **Rate Limit:** Tier 2 (100 requests per minute)
- **Deprecated:** This endpoint is deprecated. Sunset date: 2027-11. Deprecated: replaced by the namespaced Direct Access Agents API under /api/connectivity/direct-access-agents, which exposes the same operations. See https://qlik.dev/apis/rest/connectivity/direct-access-agents/.

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `agentId` | string | Yes | The ID of the Direct Access gateway, as shown in the gateway's settings dialog in the Management Console. |

#### Request Body

The contents of the file to be updated.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `connectorConfigurations` | object | Yes |  |
| `metricsCollectorSettings` | object | Yes |  |

<details>
<summary>Properties of `connectorConfigurations`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fileConnector` | object | Yes |  |
| `odbcConnector` | object | Yes |  |
| `restConnector` | object | Yes |  |
| `systemMetrics` | object | Yes |  |
| `connectorAgent` | object | Yes |  |
| `sapBwConnector` | object | Yes |  |
| `sapSqlConnector` | object | Yes |  |
| `sapPackageConnector` | object | Yes |  |

<details>
<summary>Properties of `fileConnector`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scrapeIntervalSeconds` | integer | Yes | Frequency in seconds at which metrics are collected from this connector. |
| `metricsCollectionEnabled` | boolean | Yes | Indicates whether metrics collection is enabled for this connector. |

</details>

<details>
<summary>Properties of `odbcConnector`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scrapeIntervalSeconds` | integer | Yes | Frequency in seconds at which metrics are collected from this connector. |
| `metricsCollectionEnabled` | boolean | Yes | Indicates whether metrics collection is enabled for this connector. |

</details>

<details>
<summary>Properties of `restConnector`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scrapeIntervalSeconds` | integer | Yes | Frequency in seconds at which metrics are collected from this connector. |
| `metricsCollectionEnabled` | boolean | Yes | Indicates whether metrics collection is enabled for this connector. |

</details>

<details>
<summary>Properties of `systemMetrics`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scrapeIntervalSeconds` | integer | Yes | Frequency in seconds at which metrics are collected from this connector. |
| `metricsCollectionEnabled` | boolean | Yes | Indicates whether metrics collection is enabled for this connector. |

</details>

<details>
<summary>Properties of `connectorAgent`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scrapeIntervalSeconds` | integer | Yes | Frequency in seconds at which metrics are collected from this connector. |
| `metricsCollectionEnabled` | boolean | Yes | Indicates whether metrics collection is enabled for this connector. |

</details>

<details>
<summary>Properties of `sapBwConnector`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scrapeIntervalSeconds` | integer | Yes | Frequency in seconds at which metrics are collected from this connector. |
| `metricsCollectionEnabled` | boolean | Yes | Indicates whether metrics collection is enabled for this connector. |

</details>

<details>
<summary>Properties of `sapSqlConnector`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scrapeIntervalSeconds` | integer | Yes | Frequency in seconds at which metrics are collected from this connector. |
| `metricsCollectionEnabled` | boolean | Yes | Indicates whether metrics collection is enabled for this connector. |

</details>

<details>
<summary>Properties of `sapPackageConnector`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scrapeIntervalSeconds` | integer | Yes | Frequency in seconds at which metrics are collected from this connector. |
| `metricsCollectionEnabled` | boolean | Yes | Indicates whether metrics collection is enabled for this connector. |

</details>

</details>

<details>
<summary>Properties of `metricsCollectorSettings`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `port` | integer | Yes | The port number that the metrics collector API will run on. This must match the port that the SYSTEM connector runs on to enable network metrics collection. |
| `enabled` | boolean | Yes | Indicates whether the metrics collector is enabled. Required; a request without it is rejected with `400`. |
| `localDataRetentionDays` | integer | Yes | The number of days to retain local data. |
| `baseScrapeIntervalSeconds` | integer | Yes | The base interval in seconds for the metrics collection loop. This defines how frequently the collector checks whether to scrape each connector, not the interval at which each connector is scraped. Must be equal to or less than the lowest individual connector scrape interval. |
| `localDatabaseFileLocation` | string | Yes | The file location for the local metrics database. Required; an empty string keeps the default location: `%ProgramData%\Qlik\Gateway\tmp` on Windows, `/usr/share/Qlik/Gateway/tmp` in the containerized gateway. |
| `dataRetentionCheckIntervalMinutes` | integer | Yes | The interval in minutes the metrics collector checks for and deletes old data. |
| `localDataRetentionDatabaseSizeInMb` | integer | No | The maximum size of the local database in megabytes. Optional; 500 MB when omitted. |

</details>

#### Responses

##### 204

The settings were replaced.

##### 400

Invalid request body, or the gateway version does not support this operation.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 403

The requestor does not have the required `TenantAdmin` role or the required permissions for the gateway's space.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 404

The gateway was not found, or the configuration file does not exist on the agent.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 409

The agent rejected the update because of a conflicting state, such as a reload in progress.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

##### 500

There was an error processing the request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | The errors. |
| `traceId` | string | No | The trace ID of the request, when available. |
| `hasErrors` | boolean | No | `true` when `errors` is not empty. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | The error code, for example `HTTP-400` for a plain HTTP error or a `DirectAccess-<number>` code. |
| `title` | string | No | A short description of the error. |
| `detail` | string | No | Additional detail, when available. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PUT /api/v1/direct-access-agents/{agentId}/tools/metrics-collector/configuration` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/direct-access-agents/{agentId}/tools/metrics-collector/configuration',
  {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      connectorConfigurations: {
        fileConnector: {
          scrapeIntervalSeconds: 30,
          metricsCollectionEnabled: false,
        },
        odbcConnector: {
          scrapeIntervalSeconds: 30,
          metricsCollectionEnabled: false,
        },
        restConnector: {
          scrapeIntervalSeconds: 30,
          metricsCollectionEnabled: false,
        },
        systemMetrics: {
          scrapeIntervalSeconds: 30,
          metricsCollectionEnabled: false,
        },
        connectorAgent: {
          scrapeIntervalSeconds: 30,
          metricsCollectionEnabled: false,
        },
        sapBwConnector: {
          scrapeIntervalSeconds: 30,
          metricsCollectionEnabled: false,
        },
        sapSqlConnector: {
          scrapeIntervalSeconds: 30,
          metricsCollectionEnabled: false,
        },
        sapPackageConnector: {
          scrapeIntervalSeconds: 30,
          metricsCollectionEnabled: false,
        },
      },
      metricsCollectorSettings: {
        port: 5052,
        enabled: false,
        localDataRetentionDays: 30,
        baseScrapeIntervalSeconds: 1,
        localDatabaseFileLocation: '',
        dataRetentionCheckIntervalMinutes: 60,
        localDataRetentionDatabaseSizeInMb: 500,
      },
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PUT /api/v1/direct-access-agents/{agentId}/tools/metrics-collector/configuration yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/direct-access-agents/{agentId}/tools/metrics-collector/configuration" \
-X PUT \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"connectorConfigurations":{"fileConnector":{"scrapeIntervalSeconds":30,"metricsCollectionEnabled":false},"odbcConnector":{"scrapeIntervalSeconds":30,"metricsCollectionEnabled":false},"restConnector":{"scrapeIntervalSeconds":30,"metricsCollectionEnabled":false},"systemMetrics":{"scrapeIntervalSeconds":30,"metricsCollectionEnabled":false},"connectorAgent":{"scrapeIntervalSeconds":30,"metricsCollectionEnabled":false},"sapBwConnector":{"scrapeIntervalSeconds":30,"metricsCollectionEnabled":false},"sapSqlConnector":{"scrapeIntervalSeconds":30,"metricsCollectionEnabled":false},"sapPackageConnector":{"scrapeIntervalSeconds":30,"metricsCollectionEnabled":false}},"metricsCollectorSettings":{"port":5052,"enabled":false,"localDataRetentionDays":30,"baseScrapeIntervalSeconds":1,"localDatabaseFileLocation":"","dataRetentionCheckIntervalMinutes":60,"localDataRetentionDatabaseSizeInMb":500}}'
```

---
