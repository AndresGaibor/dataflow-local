---
source: https://qlik.dev/changelog/230-apps-evaluations-endpoints-deprecation/
last_updated: 2026-06-26T14:22:57+02:00
---

# Apps API evaluation endpoints replaced by Analytics Apps namespaced API

Six evaluation endpoints in the [Apps REST API](https://qlik.dev/apis/rest/apps/) are deprecated and will be removed on or after
September 24, 2026.

Direct replacements are available in the new [Analytics Apps API](https://qlik.dev/apis/rest/analytics/apps/).

### What's changing \{#230-whats-changing}

The evaluation sub-resources at `/api/v1/apps/...` are deprecated.
They will be removed on or after September 24, 2026.
Equivalent endpoints are now available under `/api/analytics/apps/...`.

The new endpoints include improved response schemas, a standardized `Accept` header
for format selection on download operations, and a clearer path naming convention
for comparison operations.

### Endpoint mapping \{#230-endpoint-mapping}

| Legacy endpoint                                                                         | Replacement endpoint                                                                       |
| --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| `GET /api/v1/apps/{guid}/evaluations`                                                   | `GET /api/analytics/apps/{guid}/evaluations`                                               |
| `POST /api/v1/apps/{guid}/evaluations`                                                  | `POST /api/analytics/apps/{guid}/evaluations`                                              |
| `GET /api/v1/apps/evaluations/{baseid}/actions/compare/{comparisonid}`                  | `GET /api/analytics/apps/evaluations/{baselineId}/compare/{comparisonId}`                  |
| `GET /api/v1/apps/evaluations/{baseid}/actions/compare/{comparisonid}/actions/download` | `GET /api/analytics/apps/evaluations/{baselineId}/compare/{comparisonId}/actions/download` |
| `GET /api/v1/apps/evaluations/{id}`                                                     | `GET /api/analytics/apps/evaluations/{id}`                                                 |
| `GET /api/v1/apps/evaluations/{id}/actions/download`                                    | `GET /api/analytics/apps/evaluations/{id}/actions/download`                                |

<details>
  <summary>
    ### Migration guide \{#230-migration-guide}
  </summary>

  Update your integrations for each change listed below.

  #### Update the base path \{#230-base-path}

  Replace `/api/v1/apps` with `/api/analytics/apps` in every evaluation request.

  ```bash
  # Before
  GET https://<TENANT>.us.qlikcloud.com/api/v1/apps/<GUID>/evaluations

  # After
  GET https://<TENANT>.us.qlikcloud.com/api/analytics/apps/<GUID>/evaluations
  ```

  #### Rename path parameters in comparison endpoints \{#230-path-params}

  The comparison endpoints rename their path parameters. Update your URL templates:

  | Parameter (legacy) | Parameter (new)  |
  | ------------------ | ---------------- |
  | `{baseid}`         | `{baselineId}`   |
  | `{comparisonid}`   | `{comparisonId}` |

  ```bash
  # Before
  GET /api/v1/apps/evaluations/{baseid}/actions/compare/{comparisonid}

  # After
  GET /api/analytics/apps/evaluations/{baselineId}/compare/{comparisonId}
  ```

  #### Use the Accept header to choose download format \{#230-accept-header}

  The legacy download endpoints had no format selection mechanism and always returned
  `application/xml`. The new download endpoints accept an `Accept` header:

  ```bash
  # Legacy: no format control, always returns XML
  GET /api/v1/apps/evaluations/{id}/actions/download

  # New: choose the format
  GET /api/analytics/apps/evaluations/{id}/actions/download
  Accept: application/json
  ```

  Accepted values are `application/xml` (default) and `application/json`. The same
  applies to the comparison download endpoint.

  <Aside type="info">
    The `?format=json|xml` query parameter on the non-download GET endpoints
    (`GET .../evaluations/{id}` and `GET .../evaluations/{baselineId}/compare/{comparisonId}`)
    is unchanged between the legacy and new endpoints.
  </Aside>

  #### Update code that reads evaluation response fields \{#230-evaluation-schema}

  **Update field references:**

  | Find                          | Replace with                                                          |
  | ----------------------------- | --------------------------------------------------------------------- |
  | `evaluation.metadata`         | `evaluation.reloadInformation`                                        |
  | `evaluation.events[].details` | `evaluation.events[].message`                                         |
  | `evaluation.result.sheets`    | `evaluation.result.sheetsCached` + `evaluation.result.sheetsUncached` |

  **Remove these fields since they're not included in the `analytics/apps` API responses:**

  - `evaluation.sheetId`, `evaluation.sheetTitle`: no direct replacement.
    Sheet context is available per-event via `events[].sheetId` and `.sheetTitle`
  - `evaluation.details.dedicated`

  **Handle these new fields:**

  - `evaluation.engine: { shortName: string }`: Engine version that ran the evaluation (e.g., `"OAPE-40"`)
  - `evaluation.openAppProgress: { messages: [{ message: string, timeSinceStartMilliseconds: string }] }`:
    Timestamped progress log of the app open phase
  - `evaluation.result.openApp: { steps: [{ name: string, durationMilliseconds: number }], totalDurationMilliseconds: number }`:
    Breakdown of app open timing by phase

  #### Update code that reads comparison response fields \{#230-comparison-schema}

  **Update field references:**

  | Find                         | Replace with                 |
  | ---------------------------- | ---------------------------- |
  | `comparison.documentSizeMib` | `comparison.documentSizeMiB` |

  **Remove these fields since they're not included in the `analytics/apps` API responses:**

  - `comparison.objHeavy`, `comparison.fileSizeMib`, `comparison.maxMemoryMib`, `comparison.dataModelSizeMib`,
    `comparison.appOpenTimeSeconds`

  **Handle this new field:**

  - `comparison.engine: { baseline: { shortName: string }, comparison: { shortName: string } }`: Engine versions used in
    each of the two evaluations
</details>

For more information, see the [Analytics Apps API reference](https://qlik.dev/apis/rest/analytics/apps/)
and the [Apps REST API reference](https://qlik.dev/apis/rest/apps/).
