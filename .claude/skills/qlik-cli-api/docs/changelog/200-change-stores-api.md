---
source: https://qlik.dev/changelog/200-change-stores-api/
last_updated: 2026-01-29T17:25:57+01:00
---

# New REST API - Change stores API for managing editable datasets

The new [Change stores](https://qlik.dev/apis/rest/analytics/change-stores/) API lets you programmatically access and manage
change stores in Qlik Cloud. Change stores are primarily designed to support the [Write table](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/WriteTable/Analyze/write-table.htm)
visualization.

A change store is a structured dataset that tracks modifications to cell values, providing
an audit trail of all changes.

With this API, you can retrieve change stores, access their modification history, and integrate change data into
downstream systems.

The API supports the following operations:

- `GET /api/analytics/change-stores`: List all change stores accessible to the user.
- `GET /api/analytics/change-stores/{storeId}`: Retrieve details about a specific change store.
- `GET /api/analytics/change-stores/{storeId}/changes`: List changes within a change store.
- `GET /api/analytics/change-stores/{storeId}/changes/tabular-views`: Retrieve changes in tabular format with optional
  row expansion.

For more information, see the
[reference documentation for the Change stores API](https://qlik.dev/apis/rest/analytics/change-stores/).
