---
source: https://qlik.dev/changelog/222-data-qualities-api-data-governance/
last_updated: 2026-05-29T17:48:41+02:00
---

# New REST API - Data Governance data-qualities API replaces deprecated v1 endpoints

The new [Data Governance data-qualities API](https://qlik.dev/apis/rest/data-governance/data-qualities/) introduces namespaced
replacements for the deprecated `/api/v1/data-qualities/` endpoints.

### New namespaced endpoints \{#222-new-endpoints}

The new API includes the following endpoints:

- `POST /api/data-governance/data-qualities/computations`: Trigger a data quality computation for a dataset. Returns
  a `computationId` for tracking progress. Replaces `POST /api/v1/data-qualities/computations`.
- `GET /api/data-governance/data-qualities/computations/{computationId}`: Retrieve the execution status of a
  computation. Poll until `status` is `SUCCEEDED` or `FAILED`. Replaces
  `GET /api/v1/data-qualities/computations/{computationId}`.
- `GET /api/data-governance/data-qualities/global-results`: Retrieve global quality results for a dataset, including
  counts of valid, invalid, empty, and total sample cells. Replaces
  `GET /api/v1/data-qualities/global-results`.

### Migration path \{#222-migration-path}

The deprecated `/api/v1/data-qualities/` endpoints return `Deprecation: true` and a `Sunset` response header
indicating the removal date. Migrate to the new namespaced endpoints before that date.

**Request and response schemas are fully compatible.** Migration requires only a URL path update. Request bodies and
response parsing remain unchanged.

Update your endpoint paths:

| Deprecated                                                | Replacement                                                            |
| --------------------------------------------------------- | ---------------------------------------------------------------------- |
| `POST /api/v1/data-qualities/computations`                | `POST /api/data-governance/data-qualities/computations`                |
| `GET /api/v1/data-qualities/computations/{computationId}` | `GET /api/data-governance/data-qualities/computations/{computationId}` |
| `GET /api/v1/data-qualities/global-results`               | `GET /api/data-governance/data-qualities/global-results`               |

The new endpoints also include an improvement over the deprecated versions:

- **`POST /api/data-governance/data-qualities/computations`** returns a `location` response header containing the
  URL to poll for computation status. You can use this header directly instead of constructing the status URL from the
  `computationId`.

For more information, see the [Data Governance data-qualities API reference](https://qlik.dev/apis/rest/data-governance/data-qualities/)
and the [API namespaces overview](https://qlik.dev/apis/namespaces/).
