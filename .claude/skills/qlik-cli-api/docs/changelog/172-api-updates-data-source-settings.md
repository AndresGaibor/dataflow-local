---
source: https://qlik.dev/changelog/172-api-updates-data-source-settings/
last_updated: 2025-10-09T16:16:49Z
---

# Updated API - Manage data source settings using the Data sources API

The Data sources API now includes a new endpoint that lets you manage configuration settings for each data source in
your tenant.

The following new operations are available:

- `GET /api/v1/data-sources/{dataSourceId}/settings` - Retrieves the settings for a data source.
- `PUT /api/v1/data-sources/{dataSourceId}/settings` - Updates the settings for a data source.

These operations give administrators and integrators more flexibility to manage data source settings through the API.

For more information, refer to the [Data sources API reference](https://qlik.dev/apis/rest/data-sources/).
