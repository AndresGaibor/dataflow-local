---
source: https://qlik.dev/changelog/77-api-deprecation-sharing-tasks/
last_updated: 2025-07-08T16:09:30Z
---

# API Updates - Deprecation of app and template name attributes in POST /v1/sharing-tasks

This changelog provides 30 days' notice of the deprecation and removal of two attributes
in the `POST /v1/sharing-tasks` endpoint. This endpoint is used to create new sharing
tasks. Other methods are not affected.

Previously, the attributes allowed you to provide a different name for an asset than the system name.
With the upcoming changes, the service will no longer apply user-provided values,
instead, it will use the system name of the asset.

The attributes are:

- `root>appName` - the name of the source Qlik Sense application
- `root>excelData>name` - the name of the report template used to generate output

No changes are needed to your code, as the API will continue to accept payloads with
these attributes, but it will ignore any provided values.

Changes will be made no fewer than 30 days from the date of this notice.

For more information on Qlik's API policies, please refer to
the [API policy](https://qlik.dev/apis/api-policy) page.

For more information on this API, please review
the [Sharing tasks API specification](https://qlik.dev/apis/rest/sharing-tasks/).
