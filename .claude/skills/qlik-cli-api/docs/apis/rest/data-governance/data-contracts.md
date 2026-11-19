# Data contracts

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Use the Data contracts API to manage data contracts for datasets in Qlik Cloud.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `DELETE` | [`/api/data-governance/data-contracts/datasets/{datasetId}`](#delete-apidata-governancedata-contractsdatasetsdatasetid) | Permanently deletes the data contract for the given dataset, along with every expectation and evaluation belonging to it. This is a hard delete: unlike deactivation, nothing is preserved and the operation cannot be undone. The schema expectation, its field expectations and all their evaluations are deleted too, whatever the schema flag. |
| `GET` | [`/api/data-governance/data-contracts/datasets/{datasetId}/expectations`](#get-apidata-governancedata-contractsdatasetsdatasetidexpectations) | Returns the list of all expectations of the global catalog, merged with the dataset's activated ones, with their current activation status, configured thresholds or bounds, latest actual value and last evaluation result. The catalog holds `trust_score` (8 dimensions: global, validity, completeness, accuracy, diversity, discoverability, usage, timeliness), `data_profile` (1 expectation: volume) and `schema` (1 expectation: structure, experimental). Each item has the four top-level fields `category`, `name`, `status`, `updatedAt` and exactly one category-specific details sub-object (`trustScore`, `dataProfile` or `schema`) holding every category-specific field. If the dataset has no data contract, the operation still returns 200 with the default, non-activated expectations. For non-activated expectations the actual value (Trust Score) or row count (volume) is fetched live while the response is built and is omitted if it cannot be retrieved. |
| `PATCH` | [`/api/data-governance/data-contracts/datasets/{datasetId}/expectations`](#patch-apidata-governancedata-contractsdatasetsdatasetidexpectations) | Updates, activates or deactivates the dataset's expectations in a single call. The request body groups update items by category key (`trustScore`, `dataProfile`, `schema`, `field`); items are processed independently (partial success): valid items are applied, failures are reported per item, and the response is 200. Activating at least one expectation creates the data contract when none exists. `schema` (structure) and `field` items are experimental and processed only while schema compliance is enabled for the tenant. Activation, re-evaluation and per-category rules are on `UpdateExpectationsByCategory` and its item schemas. |
| `POST` | [`/api/data-governance/data-contracts/datasets/actions/create`](#post-apidata-governancedata-contractsdatasetsactionscreate) | Creates a data contract for each listed dataset ID, notably to apply a contract to every dataset of a data product at once. The caller's "Compute data quality" write privilege is checked once for the whole request, before any dataset is processed, so a caller lacking it is rejected upfront with HTTP 403 rather than failing every entry individually. Each dataset is then processed independently and concurrently: a failure on one (no write permission on its space, dataset not found, or a contract already existing) does not block the others. Unlike PATCH /expectations, an existing contract is never overwritten: it is reported as a failure. The dataset-level write permission, which depends on each dataset's space/owner, is still checked per dataset. The request is capped at 100 datasets; a larger batch is rejected upfront with HTTP 400, before any contract is created. |

## API Reference

### DELETE /api/data-governance/data-contracts/datasets/{datasetId}

Permanently deletes the data contract for the given dataset, along with every expectation and evaluation belonging to it. This is a hard delete: unlike deactivation, nothing is preserved and the operation cannot be undone. The schema expectation, its field expectations and all their evaluations are deleted too, whatever the schema flag.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `datasetId` | string | Yes |  |

#### Responses

##### 204

The data contract, its expectations, and its evaluation history were deleted, with an empty body.

##### 400

The datasetId path parameter is malformed.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | Identifier of the request trace. Quote it when reporting a problem so the request can be located in the logs. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `meta` | object | No | Optional additional context for the error. Null when none is provided. |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 401

User does not have valid authentication credentials.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | Identifier of the request trace. Quote it when reporting a problem so the request can be located in the logs. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `meta` | object | No | Optional additional context for the error. Null when none is provided. |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 403

User does not have access to the resource, or the feature is not available for this tenant. DC-001: the feature is not available for this tenant (feature flag disabled). DC-004: the user lacks the 'Compute data quality' privilege. DC-007: the user can read the dataset but lacks update permission on its space.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | Identifier of the request trace. Quote it when reporting a problem so the request can be located in the logs. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `meta` | object | No | Optional additional context for the error. Null when none is provided. |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 404

Dataset or data contract not found. DC-006: the dataset was not found, or the user has no read access to the dataset's space. DC-003: no data contract exists for the dataset.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | Identifier of the request trace. Quote it when reporting a problem so the request can be located in the logs. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `meta` | object | No | Optional additional context for the error. Null when none is provided. |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 500

Internal Server Error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | Identifier of the request trace. Quote it when reporting a problem so the request can be located in the logs. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `meta` | object | No | Optional additional context for the error. Null when none is provided. |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 502

The Catalog service could not be reached to verify the dataset.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | Identifier of the request trace. Quote it when reporting a problem so the request can be located in the logs. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `meta` | object | No | Optional additional context for the error. Null when none is provided. |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `DELETE /api/data-governance/data-contracts/datasets/{datasetId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/data-governance/data-contracts/datasets/{datasetId}',
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
# qlik-cli has not implemented support for DELETE /api/data-governance/data-contracts/datasets/{datasetId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/data-governance/data-contracts/datasets/{datasetId}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### GET /api/data-governance/data-contracts/datasets/{datasetId}/expectations

Returns the list of all expectations of the global catalog, merged with the dataset's activated ones, with their current activation status, configured thresholds or bounds, latest actual value and last evaluation result. The catalog holds `trust_score` (8 dimensions: global, validity, completeness, accuracy, diversity, discoverability, usage, timeliness), `data_profile` (1 expectation: volume) and `schema` (1 expectation: structure, experimental). Each item has the four top-level fields `category`, `name`, `status`, `updatedAt` and exactly one category-specific details sub-object (`trustScore`, `dataProfile` or `schema`) holding every category-specific field. If the dataset has no data contract, the operation still returns 200 with the default, non-activated expectations. For non-activated expectations the actual value (Trust Score) or row count (volume) is fetched live while the response is built and is omitted if it cannot be retrieved.
When schema compliance is enabled for the tenant, the schema / structure expectation is listed too (experimental), with every non-deleted field of the activated schema nested under it in `schema.fields` (experimental), sorted by name in case-sensitive order — never as sibling items of their own: this response never has a `category: field` item. The schema expectation also stores the name of every field it knows, deleted ones included (`fieldNames`), for the drift detection of later tickets; no response exposes it.
Order, the same on every page: the top-level items, ACTIVATED ones before the others; the `schema` item is one of them. When schema compliance is disabled (or the flag service cannot answer), the schema entry, stored or NOT_ACTIVATED placeholder, is omitted from this response, from suggest and from lookup; a schema activated before the flag was turned off is kept, only hidden, and so are its fields, nested under it.
Pagination (experimental): at most `limit` items per page, in this order, which never changes from one page to the next. `links.next.href` leads to the next page and is null on the last one; a page that ends exactly on the last item also has `next: null`, so no next link ever leads to an empty page. `links.prev.href` leads to the previous page, which holds the `limit` items before the current one or fewer, and is null on the first. There is no page number: the Qlik pagination guidelines are cursor-based, so call the links as is. `meta.count` is the total number of top-level items over all pages, the same on every page of one pass. Only the top-level items are paged and counted: the fields nested under `schema.fields` are never paged nor counted, and the page that holds the schema item holds every one of its fields regardless of `limit` — a deliberate exception, since a cap would silently drop fields from the only API that lists them; a dataset with many fields can return 1,000 or more of them in that one schema item. When schema compliance is disabled there is no schema item, so every item comes on a single page with `links.prev` and `links.next` both null.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `datasetId` | string | Yes |  |

#### Responses

##### 200

Expectations retrieved successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `expectations` | undefined[] | Yes | One expectation of the dataset. The notes below apply to every item.  - `category`: one of `trust_score`, `data_profile` or `schema`. - `status`: `ACTIVATED` means the expectation is enforced and being evaluated, `DEACTIVATED`   means it was previously activated but is currently disabled (explicitly turned off), and   `NOT_ACTIVATED` means it exists in the catalog but has never been activated for this   dataset. - `activatable`: for `schema` it is true when Catalog reports at least one non-orphan field   for the dataset, false otherwise (no schema, no field, only orphan fields, or Catalog   unreachable). - `trustScore.dimensionStatus` is AVAILABLE or NOT_AVAILABLE, as recorded on the stored   expectation; absent for NOT_ACTIVATED items. `trustScore.threshold` and   `trustScore.warning` are absent for NOT_ACTIVATED. - `trustScore.actualValue`: the current score. ACTIVATED: the score recorded by the latest   evaluation (evaluations run on every incoming Trust Score event, so it is current),   omitted when that evaluation is an ERROR (dimension unavailable / service failure), as an   ERROR evaluation carries no real measurement. NOT_ACTIVATED and DEACTIVATED: fetched live   from the Trust Score service when the response is built, once per expectation category   per request, and never falling back to the stale stored value; evaluations only run   while an expectation is activated, so the stored value of a DEACTIVATED expectation   dates from the moment it was deactivated and drifts further from reality the longer it   stays off, and a NOT_ACTIVATED expectation has no evaluation record at all (the live   value lets a caller see the current score before activating). The field is always   omitted rather than defaulted to 0 whenever no actual value is available (a genuine   measured 0 is still reported as 0), notably when the external service is unreachable   (fail-open behavior): no error is returned to the client and the rest of the response is   unaffected. For an ACTIVATED item it normally agrees with `lastEvaluation.actualValue`;   for a DEACTIVATED item they usually differ, and that is expected. - `dataProfile.min` and `dataProfile.max`: ACTIVATED/DEACTIVATED: the stored bound (absent   if the bound was removed). NOT_ACTIVATED: a preview of the bound activation would apply   right now, `ceil(actualRowCount * 0.95)` for `min` (-5% baseline) and   `ceil(actualRowCount * 1.05)` for `max` (+5% baseline), present only when   `actualRowCount` is available and absent otherwise, so a caller can preview the default   bounds before activating. - `dataProfile.actualRowCount`: the current row count, with the same semantics as   `trustScore.actualValue` (recorded by the latest evaluation for ACTIVATED, omitted when   that evaluation is an ERROR, never 0; fetched live, once per expectation category per   request, for NOT_ACTIVATED and DEACTIVATED, never falling back to the stale stored   value; omitted rather than defaulted to 0 when unavailable) but taken from Catalog:   evaluations run on every incoming profile event, and when Catalog is unreachable the   field is omitted (fail-open behavior), with no error returned to the client and the rest   of the response unaffected. For an ACTIVATED item it normally agrees with   `lastEvaluation.actualRowCount`; for a DEACTIVATED item they usually differ, and that is   expected. - `lastEvaluation` is present for ACTIVATED/DEACTIVATED items with at least one   evaluation. `lastEvaluation.error`: human-readable error message, present when status is   ERROR. `lastEvaluation.actualValue`: the score recorded at evaluation time; for an   ACTIVATED item it normally agrees with the top-level `actualValue`, for a DEACTIVATED   item they usually differ, and that is expected. `lastEvaluation.expectedWarning`:   omitted when no warning was set. - `schema.fields`: every non-deleted field of the schema, nested here and never as a   sibling `category: field` item; always present, `[]` when the schema has no field or was   never activated. Not counted by `meta.count` and not paged: present in full whatever the   page `limit`. |

<details>
<summary>Properties of `expectations`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `GetTrustScoreExpectationItem` | object | No |  |

<details>
<summary>Properties of `GetTrustScoreExpectationItem`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes | The name of a trust score dimension. Enum: "global", "validity", "completeness", "accuracy", "diversity", "discoverability", "usage", "timeliness" |
| `status` | string | Yes | Activation status of an expectation. `ACTIVATED` means the expectation is enforced, `DEACTIVATED` means it was explicitly turned off, and `NOT_ACTIVATED` means it has never been activated. Enum: "ACTIVATED", "DEACTIVATED", "NOT_ACTIVATED" |
| `category` | string | Yes | The expectations category. |
| `updatedAt` | string | No | When the expectation was last updated. Absent for NOT_ACTIVATED items. |
| `activatable` | boolean | No | Whether the expectation can be activated right now. Present only for non-active items (NOT_ACTIVATED and DEACTIVATED); omitted for ACTIVATED items. For trust_score expectations it is true only when the dataset has a computed Trust Score and the dimension is available, and false otherwise (quality not computed, dimension disabled, or the Trust Score service is unreachable). Always true for data_profile expectations. |
| `trustScore` | object | Yes |  |

<details>
<summary>Properties of `trustScore`</summary>

_Properties truncated due to depth limit._

</details>

</details>

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `GetVolumeExpectationItem` | object | No |  |

<details>
<summary>Properties of `GetVolumeExpectationItem`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes | The name of a volume expectation. Enum: "volume" |
| `status` | string | Yes | Activation status of an expectation. `ACTIVATED` means the expectation is enforced, `DEACTIVATED` means it was explicitly turned off, and `NOT_ACTIVATED` means it has never been activated. Enum: "ACTIVATED", "DEACTIVATED", "NOT_ACTIVATED" |
| `category` | string | Yes | The expectations category. |
| `updatedAt` | string | No | When the expectation was last updated. Absent for NOT_ACTIVATED items. |
| `activatable` | boolean | No | Whether the expectation can be activated right now. Present only for non-active items (NOT_ACTIVATED and DEACTIVATED); omitted for ACTIVATED items. For trust_score expectations it is true only when the dataset has a computed Trust Score and the dimension is available, and false otherwise (quality not computed, dimension disabled, or the Trust Score service is unreachable). Always true for data_profile expectations. |
| `dataProfile` | object | Yes |  |

<details>
<summary>Properties of `dataProfile`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 400

The datasetId path parameter is malformed, the limit is outside 1..100, or the page cursor is not valid.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | Identifier of the request trace. Quote it when reporting a problem so the request can be located in the logs. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `meta` | object | No | Optional additional context for the error. Null when none is provided. |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 401

User does not have valid authentication credentials.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | Identifier of the request trace. Quote it when reporting a problem so the request can be located in the logs. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `meta` | object | No | Optional additional context for the error. Null when none is provided. |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 403

User does not have access to the resource, or the feature is not available for this tenant. DC-001: feature flag disabled. DC-004: can read the dataset but lacks the 'Compute data quality' read privilege.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | Identifier of the request trace. Quote it when reporting a problem so the request can be located in the logs. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `meta` | object | No | Optional additional context for the error. Null when none is provided. |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 404

Dataset not found, or the caller has no read access to the dataset's space.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | Identifier of the request trace. Quote it when reporting a problem so the request can be located in the logs. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `meta` | object | No | Optional additional context for the error. Null when none is provided. |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 500

Internal Server Error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | Identifier of the request trace. Quote it when reporting a problem so the request can be located in the logs. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `meta` | object | No | Optional additional context for the error. Null when none is provided. |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 502

The Catalog service could not be reached to verify the dataset.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | Identifier of the request trace. Quote it when reporting a problem so the request can be located in the logs. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `meta` | object | No | Optional additional context for the error. Null when none is provided. |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/data-governance/data-contracts/datasets/{datasetId}/expectations` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/data-governance/data-contracts/datasets/{datasetId}/expectations',
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
# qlik-cli has not implemented support for GET /api/data-governance/data-contracts/datasets/{datasetId}/expectations yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/data-governance/data-contracts/datasets/{datasetId}/expectations" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "expectations": [
    {
      "name": "validity",
      "status": "ACTIVATED",
      "category": "string",
      "updatedAt": "2024-01-15T10:30:00Z",
      "activatable": true,
      "trustScore": {
        "warning": 90,
        "threshold": 85,
        "actualValue": 85.1,
        "lastEvaluation": {
          "error": "Service unreachable",
          "status": "PASS",
          "trigger": "TRUST_SCORE_EVENT",
          "errorCode": "DCI-001",
          "actualValue": 85,
          "evaluatedAt": "2018-03-20T09:12:28Z",
          "expectedWarning": 90,
          "expectedThreshold": 85
        },
        "dimensionStatus": "AVAILABLE"
      }
    }
  ]
}
```

---

### PATCH /api/data-governance/data-contracts/datasets/{datasetId}/expectations

Updates, activates or deactivates the dataset's expectations in a single call. The request body groups update items by category key (`trustScore`, `dataProfile`, `schema`, `field`); items are processed independently (partial success): valid items are applied, failures are reported per item, and the response is 200. Activating at least one expectation creates the data contract when none exists. `schema` (structure) and `field` items are experimental and processed only while schema compliance is enabled for the tenant. Activation, re-evaluation and per-category rules are on `UpdateExpectationsByCategory` and its item schemas.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `datasetId` | string | Yes |  |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `expectations` | object | Yes | Object whose keys are category identifiers in camelCase (e.g. `trustScore` maps to the `trust_score` category), each containing an array of updates. Unknown keys are silently ignored. `name` is matched case-insensitively for `trustScore`, `dataProfile` and `schema` (e.g. `VAlidity` matches `validity`), and the response `name` is always the canonical stored name (e.g. `validity`; a per-item error result may carry the name as sent). A `field` name is matched exactly and case-sensitively: `City` and `city` are two fields. Each `status` accepts only ACTIVATED and DEACTIVATED, the lifecycle status of the expectation. Partial success: valid items are applied and invalid ones are reported per item. When no data contract exists, a batch with at least one activation of a NOT_ACTIVATED expectation creates (upserts) the contract instead of returning DC-008; a batch with no `status: ACTIVATED` item is rejected with 400 DC-008. A contract that exists but is not yet activated is activated in place before the batch is processed. For Trust Score items, threshold and warning must be within 0-100 and warning, when set, strictly greater than threshold. Activation. Routing depends only on the requested target status: any item carrying `status: ACTIVATED` goes through the full activation pipeline, whatever the current status (NOT_ACTIVATED or DEACTIVATED), instead of returning a per-item error, so a caller can activate and update expectations in a single request. First-time activation: if no threshold is provided, it is bootstrapped from the current actual value returned by the external service; a provided threshold (and optionally a warning) is used directly. Reactivation (DEACTIVATED to ACTIVATED) applies the same partial-override semantics. Trust Score: a `threshold` or `warning` in the request is applied; an absent one keeps the stored value, and an explicit `null` warning clears it. Data Profile: a `min` or `max` in the request is applied; an absent one keeps the stored value, and an explicit removal clears it. In both cases the external service (Trust Score service / Catalog dataset row count) is called for the current live value, and the evaluation is recorded with trigger `MANUAL` against that value and the resulting threshold/warning or bounds. Result items for activated expectations use the same `updateStatus: SUCCESS` / `ERROR` shape as regular update results. Trust Score activation failures. A Trust Score activation item is rejected with `updateStatus: ERROR`, never SUCCESS, regardless of any provided threshold, and no expectation and no evaluation are persisted for it (a failed reactivation leaves the existing expectation DEACTIVATED); the HTTP response is still 200 and other items are unaffected. `DCI-002`: the Trust Score service is unreachable (transient, retryable). `DCI-010`: no Trust Score has ever been computed for the dataset (profiling / Data Quality never ran; not retryable until quality is computed). `DCI-001`: the dataset has a computed Trust Score but this specific dimension is turned off in the Trust Score settings (the most common cause of a non-GLOBAL activation failure); activation or reactivation always requires the dimension to be available, and an explicit threshold does not bypass this check. Re-evaluation. A re-evaluation using the `actualValue` of the most recent evaluation is triggered when `threshold` or `warning` changes and the expectation is (or becomes) ACTIVATED, and when `status` changes from DEACTIVATED to ACTIVATED even if threshold/warning remain unchanged. An expectation that ends up DEACTIVATED is not re-evaluated automatically, although a manual evaluation via the evaluate API can still be triggered. When a re-evaluation fails, `lastEvaluation.status` is ERROR and the `lastEvaluation` block carries both `error` (human-readable message) and `errorCode` (machine-readable DCI-NNN code). |

<details>
<summary>Properties of `expectations`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `trustScore` | object[] | No | Array of trust score expectation update items. Must not be empty if present. |
| `dataProfile` | object[] | No | Array of data profile (volume) expectation update items. Must not be empty if present. |

<details>
<summary>Properties of `trustScore`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes | The name of the trust score dimension. One of: global, validity, completeness, accuracy, diversity, discoverability, usage, timeliness. Matched case-insensitively. Unknown names produce a per-item error in the response. |
| `status` | string | No | Activation status of an expectation. `ACTIVATED` means the expectation is enforced, `DEACTIVATED` means it was explicitly turned off, and `NOT_ACTIVATED` means it has never been activated. Enum: "ACTIVATED", "DEACTIVATED", "NOT_ACTIVATED" |
| `warning` | number | No | New warning range value (0-100 inclusive). Must be strictly greater than the effective threshold. Absent means no change. Set to null to remove. |
| `threshold` | number | No | New failure threshold value (0-100 inclusive). |

</details>

<details>
<summary>Properties of `dataProfile`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `max` | integer | No | New upper bound (inclusive). Absent = unchanged, null = remove the bound, value = set. |
| `min` | integer | No | New lower bound (inclusive). Absent = unchanged, null = remove the bound, value = set. |
| `name` | string | Yes | The name of the volume expectation. Currently only "volume" is supported (case-insensitive). Unknown names produce per-item errors (not 400). |
| `status` | string | No | Activation status of an expectation. `ACTIVATED` means the expectation is enforced, `DEACTIVATED` means it was explicitly turned off, and `NOT_ACTIVATED` means it has never been activated. Enum: "ACTIVATED", "DEACTIVATED", "NOT_ACTIVATED" |

</details>

</details>

#### Responses

##### 200

Per-item results are returned. Individual items may have succeeded or failed. Per-item error codes (`code`, with `updateStatus: ERROR`):

  - DCI-001: activation or reactivation of an unavailable Trust Score dimension; activation or reactivation of a `schema` when Catalog reports no non-orphan field (`Dataset schema not available`).
  - DCI-002: Trust Score service unavailable on activation.
  - DCI-003: unknown expectation name; a `schema` or `field` item while the schema flag is OFF; an update of an expectation that was never activated; a `field` item while the schema expectation is not ACTIVATED; a `field` item without `fieldStatus` on a deleted field.
  - DCI-009: Catalog service unavailable on a `dataProfile` or `schema` activation or reactivation, or on a `field` change that needs an evaluation (change on an activated field, reactivation); the field is left unchanged.
  - DCI-010: no Trust Score computed for the dataset on activation.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `expectations` | object | Yes |  |

<details>
<summary>Properties of `expectations`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `trustScore` | object[] | No |  |
| `dataProfile` | object[] | No |  |

<details>
<summary>Properties of `trustScore`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Diagnostic error code for the failure (only present when updateStatus is ERROR). The example values shown are not an exhaustive list of possible codes. |
| `name` | string | Yes | The name of the expectation. For trust score items, one of: global, validity, completeness, accuracy, diversity, discoverability, usage, timeliness. May also contain the raw input name for per-item error responses. |
| `reason` | string | No | The reason for failure (only present when updateStatus is ERROR). |
| `status` | string | No | Activation status of an expectation. `ACTIVATED` means the expectation is enforced, `DEACTIVATED` means it was explicitly turned off, and `NOT_ACTIVATED` means it has never been activated. Enum: "ACTIVATED", "DEACTIVATED", "NOT_ACTIVATED" |
| `warning` | number | No | The current warning range (only present when updateStatus is SUCCESS). |
| `category` | string | No | The expectation category (only present when updateStatus is SUCCESS). |
| `threshold` | number | No | The current threshold (only present when updateStatus is SUCCESS). |
| `updatedAt` | string | No | When the expectation was last updated (only present when updateStatus is SUCCESS). |
| `updateStatus` | string | Yes | Enum: "SUCCESS", "ERROR" |
| `lastEvaluation` | object | No | The last evaluation result (only present when updateStatus is SUCCESS). |
| `dimensionStatus` | string | No | The availability status of the trust score dimension. Enum: "AVAILABLE", "NOT_AVAILABLE" |

<details>
<summary>Properties of `lastEvaluation`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `dataProfile`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `max` | integer | No | The current upper bound (only present when updateStatus is SUCCESS). |
| `min` | integer | No | The current lower bound (only present when updateStatus is SUCCESS). |
| `code` | string | No | Diagnostic error code for the failure (only present when updateStatus is ERROR). The example values shown are not an exhaustive list of possible codes. |
| `name` | string | Yes | The name of the volume expectation. Currently only "volume" is supported. |
| `reason` | string | No | The reason for failure (only present when updateStatus is ERROR). |
| `status` | string | No | Activation status of an expectation. `ACTIVATED` means the expectation is enforced, `DEACTIVATED` means it was explicitly turned off, and `NOT_ACTIVATED` means it has never been activated. Enum: "ACTIVATED", "DEACTIVATED", "NOT_ACTIVATED" |
| `category` | string | No | The expectation category (only present when updateStatus is SUCCESS). |
| `updatedAt` | string | No | When the expectation was last updated (only present when updateStatus is SUCCESS). |
| `updateStatus` | string | Yes | Enum: "SUCCESS", "ERROR" |
| `lastEvaluation` | object | No | The last volume evaluation result (only present when updateStatus is SUCCESS). |

<details>
<summary>Properties of `lastEvaluation`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 400

Request-level validation failure. DC-002: the request is rejected when the `expectations` object is absent; none of `trustScore`, `dataProfile`, `schema` or `field` contains any item; a `name` is duplicated within a category array (compared case-insensitively for `trustScore`, `dataProfile` and `schema`, exactly for `field`: `City` twice is rejected, `City` and `city` are both processed); an item has no updatable field besides `name` (for `schema`, `status` or `additionalFieldsPolicy`, detail `At least one updatable field is required for expectation: structure`; for `field`, `status` or `fieldStatus`); only unknown category keys are present (no `trustScore`, `dataProfile`, `schema` or `field`); `additionalFieldsPolicy` is outside its enum; `fieldStatus` is other than EXPECTED, OPTIONAL, FORBIDDEN or DELETED; the JSON body is malformed. DC-008: no data contract exists for the dataset and the batch contains no item with `status: ACTIVATED`; include at least one ACTIVATED item to create the contract automatically.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | Identifier of the request trace. Quote it when reporting a problem so the request can be located in the logs. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `meta` | object | No | Optional additional context for the error. Null when none is provided. |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 401

User does not have valid authentication credentials.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | Identifier of the request trace. Quote it when reporting a problem so the request can be located in the logs. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `meta` | object | No | Optional additional context for the error. Null when none is provided. |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 403

User does not have access to the resource, or the feature is not available for this tenant. DC-001: the feature is not available for this tenant (feature flag disabled). DC-004: the user lacks the 'Compute data quality' privilege (checked independently of the dataset's space/owner, on every request regardless of what it contains). DC-007: the user can read the dataset but lacks update permission on its space.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | Identifier of the request trace. Quote it when reporting a problem so the request can be located in the logs. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `meta` | object | No | Optional additional context for the error. Null when none is provided. |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 404

Dataset not found (or the user has no read access to the dataset's space).

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | Identifier of the request trace. Quote it when reporting a problem so the request can be located in the logs. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `meta` | object | No | Optional additional context for the error. Null when none is provided. |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 500

Internal Server Error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | Identifier of the request trace. Quote it when reporting a problem so the request can be located in the logs. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `meta` | object | No | Optional additional context for the error. Null when none is provided. |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 502

The Catalog service could not be reached to verify the dataset.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | Identifier of the request trace. Quote it when reporting a problem so the request can be located in the logs. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `meta` | object | No | Optional additional context for the error. Null when none is provided. |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PATCH /api/data-governance/data-contracts/datasets/{datasetId}/expectations` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/data-governance/data-contracts/datasets/{datasetId}/expectations',
  {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      expectations: {
        trustScore: [
          {
            name: 'global',
            status: 'ACTIVATED',
            warning: 90,
            threshold: 85,
          },
        ],
        dataProfile: [
          {
            max: 10500,
            min: 9500,
            name: 'volume',
            status: 'ACTIVATED',
          },
        ],
      },
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PATCH /api/data-governance/data-contracts/datasets/{datasetId}/expectations yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/data-governance/data-contracts/datasets/{datasetId}/expectations" \
-X PATCH \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"expectations":{"trustScore":[{"name":"global","status":"ACTIVATED","warning":90,"threshold":85}],"dataProfile":[{"max":10500,"min":9500,"name":"volume","status":"ACTIVATED"}]}}'
```

**Example Response:**

```json
{
  "expectations": {
    "trustScore": [
      {
        "code": "DCI-001",
        "name": "string",
        "reason": "Unknown trust score dimension: Foo",
        "status": "ACTIVATED",
        "warning": 90,
        "category": "trust_score",
        "threshold": 85,
        "updatedAt": "2026-05-13T10:00:00Z",
        "updateStatus": "SUCCESS",
        "lastEvaluation": {
          "error": "Service unreachable",
          "status": "PASS",
          "trigger": "TRUST_SCORE_EVENT",
          "errorCode": "DCI-001",
          "actualValue": 92,
          "evaluatedAt": "2026-05-13T10:00:00Z",
          "expectedWarning": 90,
          "expectedThreshold": 85
        },
        "dimensionStatus": "AVAILABLE"
      }
    ],
    "dataProfile": [
      {
        "max": 10500,
        "min": 9500,
        "code": "DCI-008",
        "name": "string",
        "reason": "Invalid volume bounds: min must be less than or equal to max.",
        "status": "ACTIVATED",
        "category": "data_profile",
        "updatedAt": "2026-07-15T10:00:00Z",
        "updateStatus": "SUCCESS",
        "lastEvaluation": {
          "error": "string",
          "status": "PASS",
          "trigger": "TRUST_SCORE_EVENT",
          "errorCode": "DCI-005",
          "evaluatedAt": "2026-07-15T10:00:00Z",
          "expectedMax": 10500,
          "expectedMin": 9500,
          "actualRowCount": 10000
        }
      }
    ]
  }
}
```

---

### POST /api/data-governance/data-contracts/datasets/actions/create

Creates a data contract for each listed dataset ID, notably to apply a contract to every dataset of a data product at once. The caller's "Compute data quality" write privilege is checked once for the whole request, before any dataset is processed, so a caller lacking it is rejected upfront with HTTP 403 rather than failing every entry individually. Each dataset is then processed independently and concurrently: a failure on one (no write permission on its space, dataset not found, or a contract already existing) does not block the others. Unlike PATCH /expectations, an existing contract is never overwritten: it is reported as a failure. The dataset-level write permission, which depends on each dataset's space/owner, is still checked per dataset. The request is capped at 100 datasets; a larger batch is rejected upfront with HTTP 400, before any contract is created.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `datasets` | object[] | Yes | The batch of datasets to create contracts for. 1 to 100 entries, no duplicate `datasetId`. |

<details>
<summary>Properties of `datasets`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `datasetId` | string | Yes | Identifier of the dataset the data contract must be created for. |
| `expectations` | object | Yes | Object whose keys are category identifiers in camelCase (e.g. `trustScore` maps to the `trust_score` category), each containing an array of updates. Unknown keys are silently ignored. `name` is matched case-insensitively for `trustScore`, `dataProfile` and `schema` (e.g. `VAlidity` matches `validity`), and the response `name` is always the canonical stored name (e.g. `validity`; a per-item error result may carry the name as sent). A `field` name is matched exactly and case-sensitively: `City` and `city` are two fields. Each `status` accepts only ACTIVATED and DEACTIVATED, the lifecycle status of the expectation. Partial success: valid items are applied and invalid ones are reported per item. When no data contract exists, a batch with at least one activation of a NOT_ACTIVATED expectation creates (upserts) the contract instead of returning DC-008; a batch with no `status: ACTIVATED` item is rejected with 400 DC-008. A contract that exists but is not yet activated is activated in place before the batch is processed. For Trust Score items, threshold and warning must be within 0-100 and warning, when set, strictly greater than threshold. Activation. Routing depends only on the requested target status: any item carrying `status: ACTIVATED` goes through the full activation pipeline, whatever the current status (NOT_ACTIVATED or DEACTIVATED), instead of returning a per-item error, so a caller can activate and update expectations in a single request. First-time activation: if no threshold is provided, it is bootstrapped from the current actual value returned by the external service; a provided threshold (and optionally a warning) is used directly. Reactivation (DEACTIVATED to ACTIVATED) applies the same partial-override semantics. Trust Score: a `threshold` or `warning` in the request is applied; an absent one keeps the stored value, and an explicit `null` warning clears it. Data Profile: a `min` or `max` in the request is applied; an absent one keeps the stored value, and an explicit removal clears it. In both cases the external service (Trust Score service / Catalog dataset row count) is called for the current live value, and the evaluation is recorded with trigger `MANUAL` against that value and the resulting threshold/warning or bounds. Result items for activated expectations use the same `updateStatus: SUCCESS` / `ERROR` shape as regular update results. Trust Score activation failures. A Trust Score activation item is rejected with `updateStatus: ERROR`, never SUCCESS, regardless of any provided threshold, and no expectation and no evaluation are persisted for it (a failed reactivation leaves the existing expectation DEACTIVATED); the HTTP response is still 200 and other items are unaffected. `DCI-002`: the Trust Score service is unreachable (transient, retryable). `DCI-010`: no Trust Score has ever been computed for the dataset (profiling / Data Quality never ran; not retryable until quality is computed). `DCI-001`: the dataset has a computed Trust Score but this specific dimension is turned off in the Trust Score settings (the most common cause of a non-GLOBAL activation failure); activation or reactivation always requires the dimension to be available, and an explicit threshold does not bypass this check. Re-evaluation. A re-evaluation using the `actualValue` of the most recent evaluation is triggered when `threshold` or `warning` changes and the expectation is (or becomes) ACTIVATED, and when `status` changes from DEACTIVATED to ACTIVATED even if threshold/warning remain unchanged. An expectation that ends up DEACTIVATED is not re-evaluated automatically, although a manual evaluation via the evaluate API can still be triggered. When a re-evaluation fails, `lastEvaluation.status` is ERROR and the `lastEvaluation` block carries both `error` (human-readable message) and `errorCode` (machine-readable DCI-NNN code). |

<details>
<summary>Properties of `expectations`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `trustScore` | object[] | No | Array of trust score expectation update items. Must not be empty if present. |
| `dataProfile` | object[] | No | Array of data profile (volume) expectation update items. Must not be empty if present. |

<details>
<summary>Properties of `trustScore`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `dataProfile`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

#### Responses

##### 200

Per-dataset results are returned. Individual datasets may have succeeded or failed. Per-dataset failure codes (`code`):

  - DCI-011: dataset not found, or user has no read access to it. The user cannot even see the dataset, so its existence is not revealed.
  - DCI-012: user can read the dataset but lacks write/update permission on it. The caller already knows the dataset exists. Only for the dataset-scoped part of the check; a missing 'Compute data quality' privilege is rejected upfront for the whole request (DC-004) instead.
  - DCI-013: a data contract already exists for the dataset. The existing contract is left untouched.
  - DCI-014: no item with `status: ACTIVATED` in the dataset's expectations (the per-item counterpart of DC-008, so that it does not block other datasets).
  - DCI-015: no processable expectation in the dataset entry: every requested expectation name was unknown.
  - DCI-016: no expectation could be activated (every requested expectation failed, e.g. the Trust Score is not yet computed). No contract is persisted, so the call can be retried once the underlying indicators exist.
  - DCI-009: Catalog service unavailable.
  - DCI-005: unexpected error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `datasets` | object[] | Yes |  |

<details>
<summary>Properties of `datasets`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | Diagnostic error code for the failure (only present when updateStatus is ERROR). The example values shown are not an exhaustive list of possible codes. |
| `reason` | string | No | The reason for failure (only present when updateStatus is ERROR). |
| `datasetId` | string | Yes |  |
| `expectations` | object | No | Per-expectation results (only present when updateStatus is SUCCESS). |
| `updateStatus` | string | Yes | Enum: "SUCCESS", "ERROR" |

<details>
<summary>Properties of `expectations`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `trustScore` | object[] | No |  |
| `dataProfile` | object[] | No |  |

<details>
<summary>Properties of `trustScore`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `dataProfile`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 400

Request-level validation failure. No contract is created for any dataset. DC-002: `datasets` empty or has more than 100 entries; duplicate `datasetId`; malformed expectations for one of the entries.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | Identifier of the request trace. Quote it when reporting a problem so the request can be located in the logs. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `meta` | object | No | Optional additional context for the error. Null when none is provided. |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 401

User does not have valid authentication credentials.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | Identifier of the request trace. Quote it when reporting a problem so the request can be located in the logs. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `meta` | object | No | Optional additional context for the error. Null when none is provided. |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 403

The feature is not available for this tenant, or the caller lacks the "Compute data quality" privilege.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | Identifier of the request trace. Quote it when reporting a problem so the request can be located in the logs. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `meta` | object | No | Optional additional context for the error. Null when none is provided. |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 500

Internal Server Error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No | Identifier of the request trace. Quote it when reporting a problem so the request can be located in the logs. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `meta` | object | No | Optional additional context for the error. Null when none is provided. |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/data-governance/data-contracts/datasets/actions/create` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/data-governance/data-contracts/datasets/actions/create',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      datasets: [
        {
          datasetId: '66a3aa9800358457159ecd12',
          expectations: {
            trustScore: [
              {
                name: 'global',
                status: 'ACTIVATED',
                warning: 90,
                threshold: 85,
              },
            ],
            dataProfile: [
              {
                max: 10500,
                min: 9500,
                name: 'volume',
                status: 'ACTIVATED',
              },
            ],
          },
        },
      ],
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/data-governance/data-contracts/datasets/actions/create yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/data-governance/data-contracts/datasets/actions/create" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"datasets":[{"datasetId":"66a3aa9800358457159ecd12","expectations":{"trustScore":[{"name":"global","status":"ACTIVATED","warning":90,"threshold":85}],"dataProfile":[{"max":10500,"min":9500,"name":"volume","status":"ACTIVATED"}]}}]}'
```

**Example Response:**

```json
{
  "datasets": [
    {
      "code": "DCI-013",
      "reason": "Data contract already exists for dataset: 66a3aa9800358457159ecd12",
      "datasetId": "66a3aa9800358457159ecd12",
      "expectations": {
        "trustScore": [
          {
            "code": "DCI-001",
            "name": "string",
            "reason": "Unknown trust score dimension: Foo",
            "status": "ACTIVATED",
            "warning": 90,
            "category": "trust_score",
            "threshold": 85,
            "updatedAt": "2026-05-13T10:00:00Z",
            "updateStatus": "SUCCESS",
            "lastEvaluation": {
              "error": "Service unreachable",
              "status": "PASS",
              "trigger": "TRUST_SCORE_EVENT",
              "errorCode": "DCI-001",
              "actualValue": 92,
              "evaluatedAt": "2026-05-13T10:00:00Z",
              "expectedWarning": 90,
              "expectedThreshold": 85
            },
            "dimensionStatus": "AVAILABLE"
          }
        ],
        "dataProfile": [
          {
            "max": 10500,
            "min": 9500,
            "code": "DCI-008",
            "name": "string",
            "reason": "Invalid volume bounds: min must be less than or equal to max.",
            "status": "ACTIVATED",
            "category": "data_profile",
            "updatedAt": "2026-07-15T10:00:00Z",
            "updateStatus": "SUCCESS",
            "lastEvaluation": {
              "error": "string",
              "status": "PASS",
              "trigger": "TRUST_SCORE_EVENT",
              "errorCode": "DCI-005",
              "evaluatedAt": "2026-07-15T10:00:00Z",
              "expectedMax": 10500,
              "expectedMin": 9500,
              "actualRowCount": 10000
            }
          }
        ]
      },
      "updateStatus": "SUCCESS"
    }
  ]
}
```

---
