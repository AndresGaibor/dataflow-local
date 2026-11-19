---
source: https://qlik.dev/changelog/83-platform-ops-connector/
last_updated: 2025-07-08T16:09:30Z
---

# Block updates - Qlik Platform Operations connector

The [Qlik Platform Operations connector](https://qlik.dev/manage/platform-operations/no-code/overview)
is a connector
for [Qlik Automate](https://qlik.dev/toolkits/no-code/) that
enables deployment and management of Qlik Cloud tenants without coding.

> **Note:** Some of the block updates below feature *breaking changes*. Your existing automations will
> remain unaffected unless you choose to upgrade by clicking "Upgrade to latest version" on the block.

The following blocks have been added:

- `Get Analytics Data Connection`: retrieves the definition for a specific analytics
  data connection.
- `Create Analytics Data Connection`: enables creation of analytics data connections
  using the recently
  updated [data-connections API](https://qlik.dev/changelog/80-api-data-connections-dcaas/).
- `List Analytics Data Sources`: lists all data sources available on the tenant
  against which data connections can be created.
- `Get Analytics Data Source Properties`: retrieves the properties of a specific
  data source for use when determining which `connectionProperties` to pass into a
  `Create New Analytics Data Connection` block.
- `List Analytics Data Source Property Mapping`: similar to `Get Analytics Data Source Properties`
  but formats the possible `connectionProperties` for easier programmatic use.
- `List Analytics Data Source Gateways`: lists available Qlik Direct Access Data
  Gateways on the tenant for a specific data source.
- `Add Member To Space If Not Existing, Update If Existing`: adds a user or group to
  a space if they are not already a member, or updates their roles if they are a
  member. Does not update users who are owners of a space.
- `Count Remaining API Keys`: returns the number of API keys that the requesting user
  is able to create on the tenant. This is a function of the maximum number of API keys
  per user, minus the number of keys the user currently has.
- `Import Base 64 Encoded File To Temporary Contents`: supports importing a base64-encoded
  file to the temporary contents service for downstream consumption in another
  service, such as report-templates.
- `Export Base 64 Encoded File From Temporary Contents`: supports exporting a base64-encoded
  file from the temporary contents service.
- `Copy Analytics App`: copies an analytics app on the same tenant.
- `Generate Automation Schedule Definition`: helps to create a valid automation schedule for
  use in the `Create automation` or `Update automation` blocks.

The following blocks have been updated:

- `RAW API Request`: *breaking change* - removed the key value entry input mode for
  this block due to incorrect translation of certain data types, leading to API
  errors. If you are using this block, make sure to create a copy before
  upgrading its version to avoid corrupting the input.
- `RAW API Request With Headers`: *breaking change* - removed the key value entry input mode for
  this block due to incorrect translation of certain data types, leading to API
  errors. If you are using this block, make sure to create a copy before
  upgrading its version to avoid corrupting the input.
- `List Analytics Data Connections`: additional input parameters have been added
  to align with available options on the API.
- `List API Keys`: additional input parameters have been added to align with available
  options on the API.
- `Create API Keys`: an example output has been added.
- `List Collections`: a new enum has been added for collection type.
- `Create Collection If Not Existing`: a new enum has been added for collection type.
- `Create Automation`: an input for the automation schedule has been added to the block.
- `Update Automation`: an input for the automation schedule has been added to the block.
- `Create Group`: block output has been updated to return the created group or groups.
- `Update Roles Of Member From Space`: removed unused required input `assigneeId`.
- `Update User`: added enums for user status.
- `Publish App To Managed Space`: an example output has been added.
- `Republish App To Managed Space`: an example output has been added.
- `List Users`: added information on how to list non-active users.
- `List Collections`: added enum for public collections (`publicgoverned`).

The following blocks have been renamed to improve consistency:

- `List Data Connections`: renamed to `List Analytics Data Connections`.
- `Delete Data Connections`: renamed to `Delete Analytics Data Connections`.

Review [Qlik Platform Operations connector overview](https://qlik.dev/manage/platform-operations/no-code/overview)
for information on how to get started using the connector.
