---
source: https://qlik.dev/changelog/71-platform-ops-update/
last_updated: 2025-07-08T16:09:30Z
---

# Connector updates - Qlik Platform Operations connector

The [Platform Operations connector](https://qlik.dev/manage/platform-operations/no-code/overview)
is a connector
for [Qlik Automate](https://qlik.dev/toolkits/no-code/) that
makes deploying and managing tenants in Qlik Cloud possible without code.

Previously, the Qlik Platform Operations connector supported cross-tenant API calls
only to the domain `*.qlikcloud.com`.

This update brings support for calling any Qlik Cloud tenant, including those in
Qlik Cloud Government regions. Due to differences in Qlik Cloud Government, it is
not yet possible to use the tenant create, deactivate, or reactivate blocks on Qlik
Cloud Government tenants.

Additionally, the connector now supports passing a full tenant hostname. This means that you
can now use either of these formats to connect to a tenant:

- `tenantname.region.qlikcloud.com` - the full tenant hostname **(recommended)**
- `tenantname.region` - the legacy, reduced path

It is now recommended that you use the full tenant hostname on all blocks for any
new automations you create with the Platform Operations connector, by using
the generic *Variable* block to define the hostname at the automation level.

Review how to [get started with the Platform Operations connector](https://qlik.dev/manage/platform-operations/no-code/overview).
