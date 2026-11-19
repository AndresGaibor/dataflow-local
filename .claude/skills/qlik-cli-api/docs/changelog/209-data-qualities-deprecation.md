---
source: https://qlik.dev/changelog/209-data-qualities-deprecation/
last_updated: 2026-04-22T10:13:33Z
---

# Deprecation - Data Qualities API endpoints

Three endpoints in the [Data Qualities API](https://qlik.dev/apis/rest/data-qualities/) are now deprecated:

- `POST /api/v1/data-qualities/{qualityComputationId}/run-computation`
- `GET /api/v1/data-qualities/{qualityComputationId}`
- `GET /api/v1/data-qualities/{qualityComputationId}/global-results`

The endpoints will be removed on or after **December 31, 2026**.

Deprecated responses now include the following HTTP response headers to help you identify
affected calls and plan migrations:

- `Deprecation: true`: signals that the endpoint is deprecated
- `Sunset`: the date on or after which the endpoint is removed
- `Link`: a reference to replacement documentation

Review your integrations that call these endpoints and update them before the date
indicated in the `Sunset` response header (**December 31, 2026**).

For full API reference details, see the [Data Qualities API reference](https://qlik.dev/apis/rest/data-qualities/).
