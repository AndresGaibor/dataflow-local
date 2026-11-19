---
source: https://qlik.dev/changelog/157-api-updates-data-connections/
last_updated: 2025-10-31T14:06:52+01:00
---

# Updated API - The Data connections API now supports updating credentials and properties

The Data connections API now makes it easier to update connection properties and credentials without needing to delete
and recreate connections.

You can use the `PATCH /v1/data-connections/{qId}` operation to update most fields returned by
`GET /v1/data-connections/{qId}`.
To identify which fields are supported for a given datasource, use `GET /v1/data-sources/{dataSourceId}/api-specs` and
review the `connectionProperties` object.

`PATCH` requests must include an array of operation objects. Each object should contain:

- `op`: The operation type (`add`, `replace`, or `remove`)
- `path`: The path to the field being updated (for example, `/qName`)
- `value`: The new value (required for `add` and `replace`), matching the type of the target field

When updating a connection that uses an OAuth-based datasource, include the `qlik-auth-code` header in the request with
a valid authorization code.

> **Important:** The `type` query parameter for `PATCH /v1/data-connections` now only accepts `connectionname`.
> The previously supported `credentialname` value has been removed.

For more information, see the [Data connections API reference](https://qlik.dev/apis/rest/data-connections/) and the [Data sources API reference](https://qlik.dev/apis/rest/data-sources/).
