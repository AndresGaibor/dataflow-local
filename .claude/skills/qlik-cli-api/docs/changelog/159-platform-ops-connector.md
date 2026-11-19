---
source: https://qlik.dev/changelog/159-platform-ops-connector/
last_updated: 2025-08-13T13:20:14+01:00
---

# Block updates - Qlik Platform Operations & Qlik Cloud Services connectors

The [Qlik Platform Operations](https://qlik.dev/manage/platform-operations/no-code/overview)
and Qlik Cloud Services connectors for [Qlik Automate](https://qlik.dev/toolkits/no-code/)
enable the deployment and management of Qlik Cloud tenants without writing any code.

### Qlik Platform Operations connector

**New block**:

- `Change Automation Space`: Moves an automation between shared spaces or into the
  user's private space.

**Updated block**:

- `Create Automation`: Added support for creating the automation in a shared space.

### Qlik Cloud Services connector

**New blocks**:

- `Change Automation Space`: Moves an automation between shared spaces or into the
  user's private space.
- `Export App`: Exports a Qlik Sense app. Can be used with other
  native file blocks.
- `Import App`: Imports a Qlik Sense app. Can be used with other
  native file blocks.

**Updated blocks**:

- `Create Automation`: Added support for creating the automation in a shared space.
- `Raw API Request`: Added support for calls to `/api/v1/glossaries/*`.
- `Raw API List Request`: Added support for calls to `/api/v1/glossaries/*`.
- `Export App`: Renamed to `Export App To Temporary Contents` to better reflect the
  way the blocks works.
- `Import App`: Renamed to `Import App From Temporary Contents` to better reflect the
  way the blocks works.
