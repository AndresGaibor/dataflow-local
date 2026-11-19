---
source: https://qlik.dev/changelog/26-api-deprecation-evaluations/
last_updated: 2025-07-08T16:09:30Z
---

# Deprecation of the evaluations API

The `/evaluations` API, used to queue evaluations of Sense apps and retrieve
various performance metrics, is being deprecated in favor of new API endpoints
more consistent with the rest of the Qlik Cloud platform. The affected API endpoints are:

- POST `/v1/evaluations`
- GET `/v1/evaluations`
- GET `/v1/evaluations/{id}`
- GET `/v1/evaluations/{id}/download`
- GET `/v1/evaluations/{baseid}/compare/{comparisonid}`
- GET `/v1/evaluations/{baseid}/compare/{comparisonid}/download`

### Migrating to the new endpoints

The capability is not being removed, and the full list of new endpoints can be found
on the [API reference page for apps](https://qlik.dev/apis/rest/apps).

In summary, the notable changes to the capability except for new paths are:

- The response body for listing evaluations now uses `response.data` like other REST APIs,
  instead of `response.evaluations`
- The response body `links` field is now aligned with other REST APIs,
  `links.next` is renamed to `links.next.href`, `links.prev` is renamed to `links.prev.href`
- The download endpoints are now action endpoints; GET `/v1/evaluations/{id}/download`
  is replaced by [GET `/v1/apps/{id}/actions/download`](https://qlik.dev/apis/rest/apps/#%23%2Fentries%2Fv1%2Fapps%2Fevaluations%2F-id%2Factions%2Fdownload-get)
  and GET `/v1/evaluations/{id}/compare/{comparisonid}/download` is replaced by
  [GET `/v1/apps/{id}/actions/compare/{comparisonid}/actions/download`](https://qlik.dev/apis/rest/apps/#%23%2Fentries%2Fv1%2Fapps%2Fevaluations%2F-baseid%2Factions%2Fcompare%2F-comparisonid%2Factions%2Fdownload-get)
- A few fields were dropped as they were either deemed redundant, (technically) unused,
  or may cause confusion:
  - `spaceId`
  - `userId`
  - `maxMemoryMiB`
  - `appOpenTimeSeconds`
  - `dataModelSizeMiB`
  - `sheetTitle`
  - `responseTimeSeconds2`
  - `cardinal`
  - `total_count`
  - `no_of_rows`
  - `fileSizeMiB`

More information regarding how Qlik deprecates APIs can be found
in the [API policy](https://qlik.dev/apis/api-policy).
