---
source: https://qlik.dev/changelog/90-platform-ops-connector/
last_updated: 2025-07-08T16:09:30Z
---

# Block updates - Qlik Platform Operations connector

The [Qlik Platform Operations connector](https://qlik.dev/manage/platform-operations/no-code/overview)
is a connector
for [Qlik Automate](https://qlik.dev/toolkits/no-code/) that
enables deployment and management of Qlik Cloud tenants without coding.

The following blocks have been added:

- `Publish or Republish App to Managed Space`: a convenience block which
  rolls together the capabilities in `Publish App to Managed Space`
  and `Republish App to Managed Space` to automatically replace apps if they already
  exist with the same name in the managed space.
- `Allocate Or Update User License`: a convenience block for tenants on the user
  (professional/analyzer) license model, supporting automated assignment or update
  of user licenses in a single block.
- `RAW API List Request`: a block which supports list API calls to RAW endpoints, removing the
  requirement for handling looped calls when making RAW calls.

The following blocks have been renamed to improve consistency:

- `Create Interactive Identity Provider`: renamed to `Create Interactive OIDC Identity Provider`
  in preparation for updates to blocks for additional OIDC and SAML configuration
  options.
- `Update Interactive Identity Provider`: renamed to `Update Interactive OIDC Identity Provider`
  in preparation for updates to blocks for additional OIDC and SAML configuration
  options.

Review [Qlik Platform Operations connector overview](https://qlik.dev/manage/platform-operations/no-code/overview)
for information on how to get started using the connector.
