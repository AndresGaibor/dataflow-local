---
source: https://qlik.dev/changelog/169-platform-ops-connector/
last_updated: 2025-09-25T10:25:44+02:00
---

# Block updates - Qlik Platform Operations & Qlik Cloud Services connectors

The [Qlik Platform Operations](https://qlik.dev/manage/platform-operations/no-code/overview)
and Qlik Cloud Services connectors for [Qlik Automate](https://qlik.dev/toolkits/no-code/)
enable the deployment and management of Qlik Cloud tenants without writing any code.

### Qlik Platform Operations connector \{#169-qlik-platform-ops-connector}

**New block**:

- No new blocks were added in this release.

**Updated block**:

- `Get Reload Status`: Renamed to `Get Analytics Reload Status`.
- `Reload App`: Renamed to `Reload Analytics App`. Added inputs for users to provide
  the reload weight and pass reload variables.

### Qlik Cloud Services connector \{#169-qlik-cloud-services-connector}

**New blocks**:

- `Import Consumption App`: Downloads a copy of the subscription's
  consumption report as a Qlik Sense application. Capacity subscriptions only.
- `Add Member To Space If Not Existing`: Adds a user to a space, or updates their
  membership if they are already a member.

**Updated blocks**:

- `Do Reload`: Added inputs for users to provide the reload weight and pass reload
  variables.
