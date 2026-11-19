---
source: https://qlik.dev/changelog/215-tenant-settings-api-toggle-cross-region-endpoint-deprecation/
last_updated: 2026-04-27T12:27:23+02:00
---

# Deprecation notice - Tenant Settings API endpoint path updated to toggle-cross-region-data-inference

> **Note:** This changelog entry was updated on April 27, 2026.

The `POST /tenant-settings/actions/toggle-cross-region-data-processing` endpoint is deprecated. Use
`POST /tenant-settings/actions/toggle-cross-region-data-inference` instead.

Both endpoints are documented, but the `toggle-cross-region-data-processing` endpoint is deprecated and should not be
used for new integrations.

To migrate from the `toggle-cross-region-data-processing` endpoint to the new `toggle-cross-region-data-inference`
endpoint, update your API calls. The request body and response structure remain unchanged.

> **Warning:** The `toggle-cross-region-data-processing` endpoint will be removed after or on May 12, 2026.

For more information, see the [Tenant Settings API reference](https://qlik.dev/apis/rest/tenant-settings/).
