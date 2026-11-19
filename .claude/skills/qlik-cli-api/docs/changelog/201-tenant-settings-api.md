---
source: https://qlik.dev/changelog/201-tenant-settings-api/
last_updated: 2026-03-25T16:41:23+01:00
---

# New REST API - Tenant Settings API for managing tenant-level configuration in Qlik Cloud

The [Tenant Settings API](https://qlik.dev/apis/rest/tenant-settings/) allows tenant administrators to
programmatically manage cross-region inference for AI capabilities, like
Qlik Answers and Qlik MCP Server, and manage tenant start page settings.

## Cross-region inference

Some Qlik Cloud AI features require access to services in other regions.
Enabling cross-region inference allows Qlik Cloud to temporarily send the data required for processing to the AWS
region where the service is available, process the request there, and return the results.

By opting in, you confirm that you are authorized to enable this feature and agree to have your data processed in
other regions.

For more information on cross-region inference and its implications, see
[Enabling cross-region data processing](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/cross-region-data-processing.htm)
on Qlik Help and the [Qlik Cross Region Inference article](https://community.qlik.com/t5/Official-Support-Articles/Qlik-Cross-Region-Inference/ta-p/2541184)
in Qlik Community.

## API operations

The API supports the following operations:

- `POST /tenant-settings`: Create initial tenant settings configuration.
- `GET /tenant-settings`: Retrieve current tenant settings.
- `PATCH /tenant-settings`: Update existing tenant settings using JSON Patch operations.
- `DELETE /tenant-settings`: Delete tenant settings and revert to defaults.
- `GET /tenant-settings/start-pages`: Retrieve configured start pages.
- `POST /tenant-settings/actions/toggle-cross-region-data-processing`: Enable or disable cross-region inference for AI
  capabilities.

For more information, see the [reference documentation for the Tenant Settings API](https://qlik.dev/apis/rest/tenant-settings/).
