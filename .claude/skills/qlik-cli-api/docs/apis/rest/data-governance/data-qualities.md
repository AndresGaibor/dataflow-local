# Data qualities

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

The Data qualities API enables you to assess the quality of your datasets through asynchronous computations.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/data-governance/data-qualities/batch-computations/{batchComputationId}`](#get-apidata-governancedata-qualitiesbatch-computationsbatchcomputationid) | Retrieves the status of a batch computation, including per-dataset statuses. |
| `POST` | [`/api/data-governance/data-qualities/computations`](#post-apidata-governancedata-qualitiescomputations) | Triggers a full data quality computation for a dataset, running profile calculation followed by data quality |
| `GET` | [`/api/data-governance/data-qualities/computations/{computationId}`](#get-apidata-governancedata-qualitiescomputationscomputationid) | Retrieves the current execution status of a data quality computation. Poll this endpoint after triggering a |
| `POST` | [`/api/data-governance/data-qualities/field-qualities/actions/filter`](#post-apidata-governancedata-qualitiesfield-qualitiesactionsfilter) | Retrieves the latest computed field quality metrics for a list of datasets. The maximum number of datasets is 100. |
| `PUT` | [`/api/data-governance/data-qualities/fields-structures`](#put-apidata-governancedata-qualitiesfields-structures) | Assigns a standard or semantic type to one or more fields in a dataset. This is a partial update: |
| `GET` | [`/api/data-governance/data-qualities/global-results`](#get-apidata-governancedata-qualitiesglobal-results) | Retrieves the global quality results for a dataset, showing counts of valid, invalid, empty, and total |
| `POST` | [`/api/data-governance/data-qualities/global-results/actions/filter`](#post-apidata-governancedata-qualitiesglobal-resultsactionsfilter) | Retrieves the latest computed global quality metrics for a list of datasets. The maximum number of datasets is 100. |
| `POST` | [`/api/data-governance/data-qualities/global-results/data-quality-rules/actions/filter`](#post-apidata-governancedata-qualitiesglobal-resultsdata-quality-rulesactionsfilter) | Retrieves the dataset-level rule-quality outcomes for a rule, plus the aggregate outcome across the included |

## API Reference

### GET /api/data-governance/data-qualities/batch-computations/{batchComputationId}

Retrieves the status of a batch computation, including per-dataset statuses.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `batchComputationId` | string | Yes | Batch computation ID for tracking progress of the overall data quality computations. |

#### Responses

##### 200

Batch computation status retrieved successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | string | Yes | Overall status aggregated across all datasets in the batch. Enum: "IN_PROGRESS", "FINISHED" |
| `batchComputationId` | string | Yes | The unique identifier of the batch computation. |
| `computationStatuses` | object[] | Yes | Status of each individual dataset computation within the batch. |

<details>
<summary>Properties of `computationStatuses`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | string | Yes | Status of a data quality computation. Enum: "PROFILE_REQUESTED", "PROFILE_FAILED", "REQUESTED", "SUBMITTED", "SUCCEEDED", "FAILED" |
| `datasetId` | string | Yes | The ID of the dataset |
| `errorCode` | string | No | Error code indicating the reason for failure. Enum: "DQ-100", "DQ-110", "DQ-120", "DQ-121", "DQ-130", "DQ-140", "DQ-150", "DQ-200", "DQ-300", "DQ-310", "DQ-320", "DQ-400", "DQ-500", "DQ-160", "DQ-330", "DQ-170", "DQ-171" |
| `computationId` | string | Yes | The unique identifier of the individual computation for this dataset. |

</details>

##### 400

The request is in incorrect format.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors that occurred. |
| `traceId` | string | No | Trace identifier for debugging purposes. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code identifying the type of error. |
| `title` | string | Yes | A short summary of the error. |
| `detail` | string | No | A human-readable explanation of the error. |

</details>

##### 401

User does not have valid authentication credentials.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors that occurred. |
| `traceId` | string | No | Trace identifier for debugging purposes. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code identifying the type of error. |
| `title` | string | Yes | A short summary of the error. |
| `detail` | string | No | A human-readable explanation of the error. |

</details>

##### 403

User does not have access to the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors that occurred. |
| `traceId` | string | No | Trace identifier for debugging purposes. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code identifying the type of error. |
| `title` | string | Yes | A short summary of the error. |
| `detail` | string | No | A human-readable explanation of the error. |

</details>

##### 404

Batch computation not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors that occurred. |
| `traceId` | string | No | Trace identifier for debugging purposes. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code identifying the type of error. |
| `title` | string | Yes | A short summary of the error. |
| `detail` | string | No | A human-readable explanation of the error. |

</details>

##### 500

Internal Server Error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors that occurred. |
| `traceId` | string | No | Trace identifier for debugging purposes. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code identifying the type of error. |
| `title` | string | Yes | A short summary of the error. |
| `detail` | string | No | A human-readable explanation of the error. |

</details>

##### 503

Requested service is not available.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors that occurred. |
| `traceId` | string | No | Trace identifier for debugging purposes. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code identifying the type of error. |
| `title` | string | Yes | A short summary of the error. |
| `detail` | string | No | A human-readable explanation of the error. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/data-governance/data-qualities/batch-computations/{batchComputationId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/data-governance/data-qualities/batch-computations/{batchComputationId}',
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
# qlik-cli has not implemented support for GET /api/data-governance/data-qualities/batch-computations/{batchComputationId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/data-governance/data-qualities/batch-computations/{batchComputationId}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "status": "IN_PROGRESS",
  "batchComputationId": "string",
  "computationStatuses": [
    {
      "status": "SUCCEEDED",
      "datasetId": "669144f5aa2d642638ef1dd0",
      "errorCode": "DQ-100",
      "computationId": "string"
    }
  ]
}
```

---

### POST /api/data-governance/data-qualities/computations

Triggers a full data quality computation for a dataset, running profile calculation followed by data quality
assessment. Returns a `computationId` that can be used to track progress via the computation status endpoint
(`GET /data-governance/data-qualities/computations/{computationId}`). The computation runs asynchronously.
Poll the status endpoint until `status` is `SUCCEEDED` or `FAILED`.


- **Replaces:** "POST:/v1/data-qualities/computations"
- **Rate Limit:** Special (10 requests per minute)

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `datasetId` | string | Yes | The ID of the dataset |
| `connectionId` | string | No | The ID of the connection |
| `sampleMode` | string | No | Specifies how the dataset is sampled. `ABSOLUTE` represents a fixed number of rows, while `RELATIVE` refers to a percentage of the total dataset rows. Enum: "ABSOLUTE", "RELATIVE" |
| `sampleSize` | integer | No | The actual value of the selected sampling method size (either a fixed number for `ABSOLUTE` mode or a percentage for `RELATIVE` mode). Maximum allowed value for `ABSOLUTE` mode is `100000`. |
| `sampleMethod` | string | No | Specifies how rows are selected from the dataset. `HEAD` reads the first rows, while `RANDOM` reads a random selection of rows. If omitted, defaults to `HEAD` when `executionMode` is `PULLUP`, or `RANDOM` when `executionMode` is `PUSHDOWN`. Selecting `RANDOM` while `executionMode` is `PULLUP` is currently only supported for QVD datasets.  Enum: "HEAD", "RANDOM" |
| `executionMode` | string | No | Specifies where the data quality computation takes place. In `PUSHDOWN` mode, it runs within the Cloud Data Warehouse (e.g., Snowflake, Databricks), whereas in `PULLUP` mode, it runs in Qlik Cloud. Enum: "PUSHDOWN", "PULLUP" |

#### Responses

##### 202

Computation triggered. The response body contains the `computationId` for tracking progress.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `computationId` | string | Yes | The unique identifier of the triggered computation. Use this value to poll for status. |

##### 400

The request is in incorrect format.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors that occurred. |
| `traceId` | string | No | Trace identifier for debugging purposes. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code identifying the type of error. |
| `title` | string | Yes | A short summary of the error. |
| `detail` | string | No | A human-readable explanation of the error. |

</details>

##### 401

User does not have valid authentication credentials.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors that occurred. |
| `traceId` | string | No | Trace identifier for debugging purposes. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code identifying the type of error. |
| `title` | string | Yes | A short summary of the error. |
| `detail` | string | No | A human-readable explanation of the error. |

</details>

##### 403

User does not have access to the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors that occurred. |
| `traceId` | string | No | Trace identifier for debugging purposes. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code identifying the type of error. |
| `title` | string | Yes | A short summary of the error. |
| `detail` | string | No | A human-readable explanation of the error. |

</details>

##### 500

Internal Server Error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors that occurred. |
| `traceId` | string | No | Trace identifier for debugging purposes. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code identifying the type of error. |
| `title` | string | Yes | A short summary of the error. |
| `detail` | string | No | A human-readable explanation of the error. |

</details>

##### 503

Requested service is not available.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors that occurred. |
| `traceId` | string | No | Trace identifier for debugging purposes. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code identifying the type of error. |
| `title` | string | Yes | A short summary of the error. |
| `detail` | string | No | A human-readable explanation of the error. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/data-governance/data-qualities/computations` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/data-governance/data-qualities/computations',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      datasetId: '669144f5aa2d642638ef1dd0',
      sampleMode: 'ABSOLUTE',
      sampleSize: 10000,
      connectionId:
        '2b855c3d-426c-4aac-90cf-0edf9fc294d3',
      sampleMethod: 'HEAD',
      executionMode: 'PULLUP',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/data-governance/data-qualities/computations yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/data-governance/data-qualities/computations" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"datasetId":"669144f5aa2d642638ef1dd0","sampleMode":"ABSOLUTE","sampleSize":10000,"connectionId":"2b855c3d-426c-4aac-90cf-0edf9fc294d3","sampleMethod":"HEAD","executionMode":"PULLUP"}'
```

**Example Response:**

```json
{
  "computationId": "string"
}
```

---

### GET /api/data-governance/data-qualities/computations/{computationId}

Retrieves the current execution status of a data quality computation. Poll this endpoint after triggering a
computation to determine when results are available. The `status` field returns one of `REQUESTED`,
`SUBMITTED`, `PROFILE_REQUESTED`, `SUCCEEDED`, `FAILED`, or `PROFILE_FAILED`.


- **Replaces:** "GET:/v1/data-qualities/computations/{computationId}"
- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `computationId` | string | Yes | The unique identifier of the computation, as returned by `POST /data-governance/data-qualities/computations`. |

#### Responses

##### 200

Current execution status of the computation.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | string | Yes | Status of a data quality computation. Enum: "PROFILE_REQUESTED", "PROFILE_FAILED", "REQUESTED", "SUBMITTED", "SUCCEEDED", "FAILED" |

##### 400

The request is in incorrect format.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors that occurred. |
| `traceId` | string | No | Trace identifier for debugging purposes. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code identifying the type of error. |
| `title` | string | Yes | A short summary of the error. |
| `detail` | string | No | A human-readable explanation of the error. |

</details>

##### 401

User does not have valid authentication credentials.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors that occurred. |
| `traceId` | string | No | Trace identifier for debugging purposes. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code identifying the type of error. |
| `title` | string | Yes | A short summary of the error. |
| `detail` | string | No | A human-readable explanation of the error. |

</details>

##### 403

User does not have access to the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors that occurred. |
| `traceId` | string | No | Trace identifier for debugging purposes. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code identifying the type of error. |
| `title` | string | Yes | A short summary of the error. |
| `detail` | string | No | A human-readable explanation of the error. |

</details>

##### 404

No computation found with the specified `computationId`.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors that occurred. |
| `traceId` | string | No | Trace identifier for debugging purposes. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code identifying the type of error. |
| `title` | string | Yes | A short summary of the error. |
| `detail` | string | No | A human-readable explanation of the error. |

</details>

##### 500

Internal Server Error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors that occurred. |
| `traceId` | string | No | Trace identifier for debugging purposes. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code identifying the type of error. |
| `title` | string | Yes | A short summary of the error. |
| `detail` | string | No | A human-readable explanation of the error. |

</details>

##### 503

Requested service is not available.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors that occurred. |
| `traceId` | string | No | Trace identifier for debugging purposes. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code identifying the type of error. |
| `title` | string | Yes | A short summary of the error. |
| `detail` | string | No | A human-readable explanation of the error. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/data-governance/data-qualities/computations/{computationId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/data-governance/data-qualities/computations/{computationId}',
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
# qlik-cli has not implemented support for GET /api/data-governance/data-qualities/computations/{computationId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/data-governance/data-qualities/computations/{computationId}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "status": "SUCCEEDED"
}
```

---

### POST /api/data-governance/data-qualities/field-qualities/actions/filter

Retrieves the latest computed field quality metrics for a list of datasets. The maximum number of datasets is 100.
When a dataset has been analyzed through multiple connections, the response returns the result from the most recently computed connection.


- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `datasets` | object[] | Yes | List of datasets to retrieve field qualities for. |

<details>
<summary>Properties of `datasets`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `datasetId` | string | Yes | The ID of the dataset |

</details>

#### Responses

##### 200

Field qualities retrieved successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fieldQualities` | object[] | Yes | List of field quality results per dataset. |

<details>
<summary>Properties of `fieldQualities`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fields` | object[] | Yes | List of fields and their quality metrics. |
| `computed` | object | Yes | Metadata about the computation. |
| `datasetId` | string | Yes | The ID of the dataset |

<details>
<summary>Properties of `fields`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes | The name of the field. |
| `type` | object | Yes | Information about the type of the field. |
| `quality` | object | Yes | Quality metrics for the field. |

<details>
<summary>Properties of `type`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `quality`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `computed`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `at` | string | Yes | When the computation occurred. |
| `by` | object | Yes | Details about the user who computed the quality. |

<details>
<summary>Properties of `by`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 400

The request is in incorrect format.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors that occurred. |
| `traceId` | string | No | Trace identifier for debugging purposes. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code identifying the type of error. |
| `title` | string | Yes | A short summary of the error. |
| `detail` | string | No | A human-readable explanation of the error. |

</details>

##### 401

User does not have valid authentication credentials.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors that occurred. |
| `traceId` | string | No | Trace identifier for debugging purposes. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code identifying the type of error. |
| `title` | string | Yes | A short summary of the error. |
| `detail` | string | No | A human-readable explanation of the error. |

</details>

##### 403

User does not have access to the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors that occurred. |
| `traceId` | string | No | Trace identifier for debugging purposes. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code identifying the type of error. |
| `title` | string | Yes | A short summary of the error. |
| `detail` | string | No | A human-readable explanation of the error. |

</details>

##### 500

Internal Server Error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors that occurred. |
| `traceId` | string | No | Trace identifier for debugging purposes. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code identifying the type of error. |
| `title` | string | Yes | A short summary of the error. |
| `detail` | string | No | A human-readable explanation of the error. |

</details>

##### 503

Requested service is not available.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors that occurred. |
| `traceId` | string | No | Trace identifier for debugging purposes. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code identifying the type of error. |
| `title` | string | Yes | A short summary of the error. |
| `detail` | string | No | A human-readable explanation of the error. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/data-governance/data-qualities/field-qualities/actions/filter` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/data-governance/data-qualities/field-qualities/actions/filter',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      datasets: [
        { datasetId: '669144f5aa2d642638ef1dd0' },
      ],
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/data-governance/data-qualities/field-qualities/actions/filter yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/data-governance/data-qualities/field-qualities/actions/filter" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"datasets":[{"datasetId":"669144f5aa2d642638ef1dd0"}]}'
```

**Example Response:**

```json
{
  "fieldQualities": [
    {
      "fields": [
        {
          "name": "string",
          "type": {
            "kind": "STANDARD",
            "name": "customer_id",
            "precision": "timestamp-millis",
            "semanticTypeId": "9996fbb942b02a6987534999"
          },
          "quality": {
            "type": {
              "empty": 42,
              "total": 42,
              "valid": 42,
              "invalid": 42
            },
            "rules": [
              {
                "ruleId": "string",
                "quality": {
                  "total": 42,
                  "valid": 42,
                  "errors": [
                    "DISABLED_SEMANTIC_TYPE"
                  ],
                  "invalid": 42,
                  "notApplicable": 42,
                  "notExecutable": 42
                },
                "ruleMappingId": "string"
              }
            ],
            "aggregated": {
              "empty": 42,
              "total": 42,
              "valid": 42,
              "invalid": 42
            }
          }
        }
      ],
      "computed": {
        "at": "2023-10-01T12:00:00Z",
        "by": {
          "id": "string"
        }
      },
      "datasetId": "669144f5aa2d642638ef1dd0"
    }
  ]
}
```

---

### PUT /api/data-governance/data-qualities/fields-structures

Assigns a standard or semantic type to one or more fields in a dataset. This is a partial update:
only the fields included in the request are modified; any field not included in the request keeps
its current assigned structure unchanged.


- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

The `datasetId` of the target dataset and the list of fields to update, each with the standard or
semantic type to assign. Only the fields present in this list are affected.


**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fields` | object[] | Yes | List of fields to update with their assigned types. |
| `datasetId` | string | Yes | The ID of the dataset |

<details>
<summary>Properties of `fields`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes | The name of the field. |
| `type` | object | Yes | Information about the type of the field. |

<details>
<summary>Properties of `type`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `kind` | string | Yes | The kind of the field type. Enum: "STANDARD", "SEMANTIC" |
| `name` | string | No | The name of the standard type (if applicable). |
| `precision` | string | No | The precision of the type (e.g., for date/time fields). Enum: "timestamp-millis", "timestamp-micros", "time-millis", "time-micros", "date" |
| `semanticTypeId` | string | No | The ID of the semantic type (if applicable). |

</details>

</details>

#### Responses

##### 204

The requested field types were assigned successfully. The response body is empty.

##### 400

The request is in incorrect format.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors that occurred. |
| `traceId` | string | No | Trace identifier for debugging purposes. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code identifying the type of error. |
| `title` | string | Yes | A short summary of the error. |
| `detail` | string | No | A human-readable explanation of the error. |

</details>

##### 401

User does not have valid authentication credentials.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors that occurred. |
| `traceId` | string | No | Trace identifier for debugging purposes. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code identifying the type of error. |
| `title` | string | Yes | A short summary of the error. |
| `detail` | string | No | A human-readable explanation of the error. |

</details>

##### 403

User does not have access to the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors that occurred. |
| `traceId` | string | No | Trace identifier for debugging purposes. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code identifying the type of error. |
| `title` | string | Yes | A short summary of the error. |
| `detail` | string | No | A human-readable explanation of the error. |

</details>

##### 404

The dataset's field structure, or a referenced semantic type, was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors that occurred. |
| `traceId` | string | No | Trace identifier for debugging purposes. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code identifying the type of error. |
| `title` | string | Yes | A short summary of the error. |
| `detail` | string | No | A human-readable explanation of the error. |

</details>

##### 500

Internal Server Error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors that occurred. |
| `traceId` | string | No | Trace identifier for debugging purposes. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code identifying the type of error. |
| `title` | string | Yes | A short summary of the error. |
| `detail` | string | No | A human-readable explanation of the error. |

</details>

##### 503

Requested service is not available.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors that occurred. |
| `traceId` | string | No | Trace identifier for debugging purposes. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code identifying the type of error. |
| `title` | string | Yes | A short summary of the error. |
| `detail` | string | No | A human-readable explanation of the error. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PUT /api/data-governance/data-qualities/fields-structures` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/data-governance/data-qualities/fields-structures',
  {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      fields: [
        {
          name: 'customer_id',
          type: {
            kind: 'STANDARD',
            name: 'customer_id',
            precision: 'timestamp-millis',
            semanticTypeId:
              '9996fbb942b02a6987534999',
          },
        },
      ],
      datasetId: '669144f5aa2d642638ef1dd0',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PUT /api/data-governance/data-qualities/fields-structures yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/data-governance/data-qualities/fields-structures" \
-X PUT \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"fields":[{"name":"customer_id","type":{"kind":"STANDARD","name":"customer_id","precision":"timestamp-millis","semanticTypeId":"9996fbb942b02a6987534999"}}],"datasetId":"669144f5aa2d642638ef1dd0"}'
```

---

### GET /api/data-governance/data-qualities/global-results

Retrieves the global quality results for a dataset, showing counts of valid, invalid, empty, and total
sample cells.


- **Replaces:** "GET:/v1/data-qualities/global-results"
- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `datasetId` | string | Yes | The unique identifier of the dataset. |
| `connectionId` | string | No | The unique identifier of the connection. |

#### Responses

##### 200

Global quality results for the dataset, including counts of valid, invalid, empty, and total sample cells per connection.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `datasetId` | string | Yes | The unique identifier of the dataset. |
| `qualities` | object[] | Yes |  |

<details>
<summary>Properties of `qualities`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `quality` | object | No |  |
| `connectionId` | string | Yes | The unique identifier of the connection. |

<details>
<summary>Properties of `quality`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `empty` | integer | Yes | Number of empty sample cells. |
| `total` | integer | Yes | Total number of cells in the sample. |
| `valid` | integer | Yes | Number of valid sample cells. |
| `invalid` | integer | Yes | Number of invalid sample cells. |
| `updatedAt` | string | Yes | Timestamp of the most recent data quality computation for this dataset and connection. |

</details>

</details>

##### 400

The request is in incorrect format.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors that occurred. |
| `traceId` | string | No | Trace identifier for debugging purposes. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code identifying the type of error. |
| `title` | string | Yes | A short summary of the error. |
| `detail` | string | No | A human-readable explanation of the error. |

</details>

##### 401

User does not have valid authentication credentials.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors that occurred. |
| `traceId` | string | No | Trace identifier for debugging purposes. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code identifying the type of error. |
| `title` | string | Yes | A short summary of the error. |
| `detail` | string | No | A human-readable explanation of the error. |

</details>

##### 403

User does not have access to the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors that occurred. |
| `traceId` | string | No | Trace identifier for debugging purposes. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code identifying the type of error. |
| `title` | string | Yes | A short summary of the error. |
| `detail` | string | No | A human-readable explanation of the error. |

</details>

##### 404

No quality results found for the specified dataset.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors that occurred. |
| `traceId` | string | No | Trace identifier for debugging purposes. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code identifying the type of error. |
| `title` | string | Yes | A short summary of the error. |
| `detail` | string | No | A human-readable explanation of the error. |

</details>

##### 500

Internal Server Error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors that occurred. |
| `traceId` | string | No | Trace identifier for debugging purposes. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code identifying the type of error. |
| `title` | string | Yes | A short summary of the error. |
| `detail` | string | No | A human-readable explanation of the error. |

</details>

##### 503

Requested service is not available.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors that occurred. |
| `traceId` | string | No | Trace identifier for debugging purposes. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code identifying the type of error. |
| `title` | string | Yes | A short summary of the error. |
| `detail` | string | No | A human-readable explanation of the error. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/data-governance/data-qualities/global-results` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/data-governance/data-qualities/global-results',
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
# qlik-cli has not implemented support for GET /api/data-governance/data-qualities/global-results yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/data-governance/data-qualities/global-results" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "datasetId": "string",
  "qualities": [
    {
      "quality": {
        "empty": 42,
        "total": 42,
        "valid": 42,
        "invalid": 42,
        "updatedAt": "2023-10-01T12:00:00Z"
      },
      "connectionId": "string"
    }
  ]
}
```

---

### POST /api/data-governance/data-qualities/global-results/actions/filter

Retrieves the latest computed global quality metrics for a list of datasets. The maximum number of datasets is 100.
When a dataset has been analyzed through multiple connections, the response returns the result from the most recently computed connection.


- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `datasetIds` | string[] | Yes | List of dataset IDs to retrieve results for. |

#### Responses

##### 200

Data quality global results for the requested datasets.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `dataQualities` | object[] | Yes | List of data quality results, one per dataset and connection pair. |

<details>
<summary>Properties of `dataQualities`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `error` | object | No | Details of an execution failure. |
| `status` | string | Yes | Status of a data quality computation. Enum: "PROFILE_REQUESTED", "PROFILE_FAILED", "REQUESTED", "SUBMITTED", "SUCCEEDED", "FAILED" |
| `quality` | object | No |  |
| `datasetId` | string | Yes | The ID of the dataset |
| `connectionId` | string | Yes | The ID of the connection |

<details>
<summary>Properties of `error`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `reason` | string | No | A human-readable explanation of the failure. |
| `errorCode` | string | Yes | The error code identifying the failure reason. |
| `executedAt` | string | No | Timestamp when the execution failed. |

</details>

<details>
<summary>Properties of `quality`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `empty` | integer | Yes | Number of empty sample cells. |
| `total` | integer | Yes | Total number of cells in the sample. |
| `valid` | integer | Yes | Number of valid sample cells. |
| `invalid` | integer | Yes | Number of invalid sample cells. |
| `updatedAt` | string | Yes | Timestamp of the most recent data quality computation for this dataset and connection. |

</details>

</details>

##### 400

The request is in incorrect format.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors that occurred. |
| `traceId` | string | No | Trace identifier for debugging purposes. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code identifying the type of error. |
| `title` | string | Yes | A short summary of the error. |
| `detail` | string | No | A human-readable explanation of the error. |

</details>

##### 401

User does not have valid authentication credentials.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors that occurred. |
| `traceId` | string | No | Trace identifier for debugging purposes. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code identifying the type of error. |
| `title` | string | Yes | A short summary of the error. |
| `detail` | string | No | A human-readable explanation of the error. |

</details>

##### 403

User does not have access to the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors that occurred. |
| `traceId` | string | No | Trace identifier for debugging purposes. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code identifying the type of error. |
| `title` | string | Yes | A short summary of the error. |
| `detail` | string | No | A human-readable explanation of the error. |

</details>

##### 500

Internal Server Error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors that occurred. |
| `traceId` | string | No | Trace identifier for debugging purposes. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code identifying the type of error. |
| `title` | string | Yes | A short summary of the error. |
| `detail` | string | No | A human-readable explanation of the error. |

</details>

##### 503

Requested service is not available.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors that occurred. |
| `traceId` | string | No | Trace identifier for debugging purposes. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code identifying the type of error. |
| `title` | string | Yes | A short summary of the error. |
| `detail` | string | No | A human-readable explanation of the error. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/data-governance/data-qualities/global-results/actions/filter` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/data-governance/data-qualities/global-results/actions/filter',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      datasetIds: ['669144f5aa2d642638ef1dd0'],
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/data-governance/data-qualities/global-results/actions/filter yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/data-governance/data-qualities/global-results/actions/filter" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"datasetIds":["669144f5aa2d642638ef1dd0"]}'
```

**Example Response:**

```json
{
  "dataQualities": [
    {
      "error": {
        "reason": "string",
        "errorCode": "string",
        "executedAt": "2023-10-01T12:00:00Z"
      },
      "status": "SUCCEEDED",
      "quality": {
        "empty": 42,
        "total": 42,
        "valid": 42,
        "invalid": 42,
        "updatedAt": "2023-10-01T12:00:00Z"
      },
      "datasetId": "string",
      "connectionId": "string"
    }
  ]
}
```

---

### POST /api/data-governance/data-qualities/global-results/data-quality-rules/actions/filter

Retrieves the dataset-level rule-quality outcomes for a rule, plus the aggregate outcome across the included
datasets. When `datasetIds` is provided (max 100), the result and aggregate are limited to those datasets
that are accessible to the caller. When `datasetIds` is absent or empty, the service determines all
accessible datasets where the rule is instantiated and returns the result and aggregate for that scope.

For each dataset in the resolved scope, the service selects the most recent data quality computation
across all connections. Only datasets whose latest computation contains a result for the requested rule
are included in `ruleQualities` and contribute to `ruleQualityAggregate`. Datasets without a computed
quality result, or whose latest computation has no result for the requested rule, are excluded; the
service does not fall back to an older computation. This behavior also applies when `datasetIds` is
absent or empty.

The `ruleQualities` list is sorted by `datasetId` and paginated using the `page` and `limit` query
parameters. Set `sortDescending` to `true` to sort in descending order (default is ascending).
`ruleQualityAggregate` always covers the full resolved scope, independently of sorting and pagination.


- **Rate Limit:** Tier 2 (100 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `sortDescending` | boolean | No | When true, sorts the `ruleQualities` list by `datasetId` in descending order. Defaults to false (ascending). |
| `page` | integer | No | Page number to retrieve (1-indexed). Defaults to 1. |
| `limit` | integer | No | Maximum number of datasets to return in the `ruleQualities` page. |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `ruleId` | string | Yes | The unique identifier of the rule to analyze, represented as a 24-character hexadecimal MongoDB ObjectId. |
| `datasetIds` | string[] | No | Optional selection of datasets. When non-empty, only these datasets are considered (filtered to those accessible to the caller); the maximum number of dataset IDs is 100. When absent or empty, the service determines all accessible datasets where the rule is instantiated. |

#### Responses

##### 200

Rule-quality aggregation for the requested rule.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `ruleId` | string | Yes | The unique identifier of the analyzed rule. |
| `ruleQualities` | object[] | Yes | Rule-quality outcomes, one entry per dataset in the current page. |
| `ruleQualityAggregate` | object | Yes | Summed quality counts across one or more field/rule-mapping entries. |

<details>
<summary>Properties of `ruleQualities`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fields` | object[] | Yes | Rule-quality outcome for each field of this dataset where the rule is mapped. |
| `datasetId` | string | Yes | The ID of the dataset |
| `datasetAggregate` | object | Yes | Summed quality counts across one or more field/rule-mapping entries. |

<details>
<summary>Properties of `fields`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `quality` | object | Yes | Detailed quality counts for a rule applied to a single field, plus computation metadata. |
| `fieldName` | string | Yes | The name of the field the rule is mapped to. |
| `ruleMappingId` | string | Yes | The unique identifier of the rule mapping. |

<details>
<summary>Properties of `quality`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `datasetAggregate`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `total` | integer | Yes | Sum of the total cell counts across the included field/rule-mapping entries. |
| `valid` | integer | Yes | Sum of the numbers of cells that passed the rule across the included field/rule-mapping entries. |
| `invalid` | integer | Yes | Sum of the numbers of cells that failed the rule across the included field/rule-mapping entries. |
| `notApplicable` | integer | Yes | Sum of the numbers of cells where the rule does not apply across the included field/rule-mapping entries. |
| `notExecutable` | integer | Yes | Sum of the numbers of cells where the rule could not be executed across the included field/rule-mapping entries. |

</details>

</details>

<details>
<summary>Properties of `ruleQualityAggregate`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `total` | integer | Yes | Sum of the total cell counts across the included field/rule-mapping entries. |
| `valid` | integer | Yes | Sum of the numbers of cells that passed the rule across the included field/rule-mapping entries. |
| `invalid` | integer | Yes | Sum of the numbers of cells that failed the rule across the included field/rule-mapping entries. |
| `notApplicable` | integer | Yes | Sum of the numbers of cells where the rule does not apply across the included field/rule-mapping entries. |
| `notExecutable` | integer | Yes | Sum of the numbers of cells where the rule could not be executed across the included field/rule-mapping entries. |

</details>

##### 400

The request is in incorrect format.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors that occurred. |
| `traceId` | string | No | Trace identifier for debugging purposes. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code identifying the type of error. |
| `title` | string | Yes | A short summary of the error. |
| `detail` | string | No | A human-readable explanation of the error. |

</details>

##### 401

User does not have valid authentication credentials.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors that occurred. |
| `traceId` | string | No | Trace identifier for debugging purposes. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code identifying the type of error. |
| `title` | string | Yes | A short summary of the error. |
| `detail` | string | No | A human-readable explanation of the error. |

</details>

##### 403

User does not have access to the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors that occurred. |
| `traceId` | string | No | Trace identifier for debugging purposes. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code identifying the type of error. |
| `title` | string | Yes | A short summary of the error. |
| `detail` | string | No | A human-readable explanation of the error. |

</details>

##### 404

No rule found with the specified `ruleId`.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors that occurred. |
| `traceId` | string | No | Trace identifier for debugging purposes. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code identifying the type of error. |
| `title` | string | Yes | A short summary of the error. |
| `detail` | string | No | A human-readable explanation of the error. |

</details>

##### 500

Internal Server Error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors that occurred. |
| `traceId` | string | No | Trace identifier for debugging purposes. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code identifying the type of error. |
| `title` | string | Yes | A short summary of the error. |
| `detail` | string | No | A human-readable explanation of the error. |

</details>

##### 503

Requested service is not available.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors that occurred. |
| `traceId` | string | No | Trace identifier for debugging purposes. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code identifying the type of error. |
| `title` | string | Yes | A short summary of the error. |
| `detail` | string | No | A human-readable explanation of the error. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/data-governance/data-qualities/global-results/data-quality-rules/actions/filter` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/data-governance/data-qualities/global-results/data-quality-rules/actions/filter',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      ruleId: '9996fbb942b02a6987534999',
      datasetIds: ['669144f5aa2d642638ef1dd0'],
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/data-governance/data-qualities/global-results/data-quality-rules/actions/filter yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/data-governance/data-qualities/global-results/data-quality-rules/actions/filter" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"ruleId":"9996fbb942b02a6987534999","datasetIds":["669144f5aa2d642638ef1dd0"]}'
```

**Example Response:**

```json
{
  "ruleId": "string",
  "ruleQualities": [
    {
      "fields": [
        {
          "quality": {
            "total": 42,
            "valid": 42,
            "errors": [
              "string"
            ],
            "invalid": 42,
            "updatedAt": "2023-10-01T12:00:00Z",
            "notApplicable": 42,
            "notExecutable": 42
          },
          "fieldName": "string",
          "ruleMappingId": "string"
        }
      ],
      "datasetId": "669144f5aa2d642638ef1dd0",
      "datasetAggregate": {
        "total": 42,
        "valid": 42,
        "invalid": 42,
        "notApplicable": 42,
        "notExecutable": 42
      }
    }
  ],
  "ruleQualityAggregate": {
    "total": 42,
    "valid": 42,
    "invalid": 42,
    "notApplicable": 42,
    "notExecutable": 42
  }
}
```

---
