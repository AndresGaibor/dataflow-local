---
source: https://qlik.dev/changelog/221-change-stores-api-editable-columns/
last_updated: 2026-05-28T17:20:56+02:00
---

# Updated API - Change stores API adds editable-columns endpoint

The [Change stores API](https://qlik.dev/apis/rest/analytics/change-stores/) now includes a new endpoint for retrieving editable
columns associated with a change store.

The API now supports the following additional operation:

- `GET /api/analytics/change-stores/{storeId}/editable-columns`: Returns a paginated list of editable columns that
  belong to the specified change store, with support for filtering and sorting by column name, creation date, and
  other attributes.

This endpoint enables you to programmatically discover and manage the editable columns available in a change store,
supporting use cases that require querying column metadata and configuration details.

For more information, see the
[reference documentation for the Change stores API](https://qlik.dev/apis/rest/analytics/change-stores/).
