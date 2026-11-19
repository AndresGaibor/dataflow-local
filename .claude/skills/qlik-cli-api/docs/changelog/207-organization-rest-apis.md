---
source: https://qlik.dev/changelog/207-organization-rest-apis/
last_updated: 2026-04-10T12:26:08+01:00
---

# Organization APIs for cross-tenant access

The [Organization REST APIs](https://qlik.dev/apis/org-rest/) provide organization-level
access to your Qlik Cloud environment.

With these APIs, you can list tenants across your subscriptions and regions,
retrieve tenant data, and manage organization-level OAuth clients required
to access organization resources.

This enables integration scenarios such as OEM deployments and large-scale
operations that require visibility across multiple tenants.

## Key capabilities

The Organization APIs support the following operations:

- **List and query tenants**: Retrieve tenants in your organization with
  filtering and pagination
- **Get tenant details**: Access metadata such as region, status, and
  subscription identifiers
- **Manage organization-level OAuth clients**: Create and manage credentials
  for organization API access
- **Organization-scope authentication**: Exchange OAuth client credentials for
  access tokens scoped to organization resources

## Tenant list page

A new **Tenants list** page is available in My Qlik, where you can view,
search, filter, and sort tenants. This complements the programmatic API
approach.

For more information, see:

- the [Organization APIs documentation](https://qlik.dev/apis/org-rest/)
- the [Create organization-level OAuth client guide](https://qlik.dev/authenticate/oauth/create/create-organization-level-oauth-client/)
- the [Viewing all tenants across your subscriptions](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/view-all-tenants.htm)
  page on Qlik Help
