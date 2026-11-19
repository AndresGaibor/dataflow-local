---
source: https://qlik.dev/changelog/106-api-updates-extensions-themes/
last_updated: 2024-08-22T08:20:07+01:00
---

# Updates to Extensions and Themes API permissions

Qlik is enhancing security and data protection for the [Extensions API](https://qlik.dev/apis/rest/extensions/)
and [Themes API](https://qlik.dev/apis/rest/themes/). These APIs allow customization of experiences in Qlik Sense
by adding custom visualization objects, colors, and styling.

Currently, any user in the tenant can download the full archive of an extension or
theme from the following endpoints:

- [GET `/v1/extensions/{id}/file`](https://qlik.dev/apis/rest/extensions/#get-v1-extensions-id-file) for extensions
- [GET `/v1/themes/{id}/file`](https://qlik.dev/apis/rest/themes/#get-v1-themes-id-file) for themes

To improve security, only users with the `TenantAdmin` or `AnalyticsAdmin`
roles will be allowed to download the full archive. This brings these endpoints
in line with the permissions for import endpoints.

This change will take effect no sooner than 60 days from the date on this changelog, on,
or after October 21, 2024.

Endpoints affected:

- GET `/v1/extensions/{id}/file`
- GET `/v1/themes/{id}/file`
