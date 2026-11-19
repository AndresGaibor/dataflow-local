---
source: https://qlik.dev/changelog/78-platform-ops-connector/
last_updated: 2025-07-08T16:09:30Z
---

# Block updates - Qlik Platform Operations connector

The [Platform Operations connector](https://qlik.dev/manage/platform-operations/no-code/overview)
is a connector
for [Qlik Automate](https://qlik.dev/toolkits/no-code/) that
makes deploying and managing tenants in Qlik Cloud possible without code.

The following blocks have been added:

- `Get Current Tenant Hostname`: returns the hostname for the tenant the automation
  is running on.
- `List Analytics Reloads`: returns results from the Reloads API to list analytics
  reload information.
- `Add Role To User By Name`: supports addition of individual
  roles to users by the name of the role.
- `Remove Role From User By Name`: supports removal of individual
  roles from users by the name of the role.
- `Create collection If Not Existing`: checks to see if a collection exists, if so,
  returns the collection, if not, creates the collection.
- `Get Sharing Settings`: retrieves the current configuration of the sharing service for
  various reporting and sharing features in the tenant.
- `Update Sharing Settings`: changes the configuration of the sharing service to
  turn on or off various reporting and sharing features in the tenant.
- `RAW API Request With Headers`: similar to the `RAW API Request` block, but appends
  the response headers to the response body, since some Qlik Cloud APIs
  return information in the header.

The following blocks have been updated:

- `Get API Key Settings`: removed the need to pass the `tenantId` as a block
  input, since you can only make requests for the tenant you pass the request to.
- `Update API Key Settings`: removed the need to pass the `tenantId` as a block
  input, since you can only make requests for the tenant you pass the request to.
- `Update Collection`: added support for changing collection type from `private` to
  `publicgoverned` to support managing public collections.

The following blocks have been renamed to improve consistency:

- `Enable Data Alerts`: renamed to `Update Data Alert Settings`.
- `Get Auto Create Group Setting`: renamed to `Get Auto Create Group Settings`.
- `Update Auto Create Group Setting`: renamed to `Update Auto Create Group Settings`.
- `Trigger Enable Notes Settings`: renamed to `Update Notes Settings`.

Review how to [get started with the Platform Operations connector](https://qlik.dev/manage/platform-operations/no-code/overview).
