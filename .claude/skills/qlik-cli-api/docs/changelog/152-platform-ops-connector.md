---
source: https://qlik.dev/changelog/152-platform-ops-connector/
last_updated: 2025-07-09T21:18:10Z
---

# Block updates - Qlik Platform Operations & Qlik Cloud Services connectors

The [Qlik Platform Operations](https://qlik.dev/manage/platform-operations/no-code/overview)
and Qlik Cloud Services connectors for [Qlik Automate](https://qlik.dev/toolkits/no-code/)
enable the deployment and management of Qlik Cloud tenants without any code.

Updated blocks in the **Qlik Platform Operations** connector:

- `Update API Key Settings`: Removed `api_keys_enabled` input
  following the [deprecation notice](https://qlik.dev/changelog/146-developer-role-deprecation/).
- All `Reload Task` blocks have been marked as deprecated following the release of the
  replacement [Tasks API](https://qlik.dev/changelog/135-tasks-api/).

New blocks in the **Qlik Cloud Services** connector:

- `Create Data File`: Creates a data file using provided base64 encoded content.
- `Create Data File In Space`: Creates a data file in a space using provided base64
  encoded content.
- `Copy Data File In Space`: Duplicates an existing data file.
- `Create Folder In Space`: Creates a new folder in the specified space.
- `List Data Files From Space`: Lists all data files in the specified space.
- `Get Data File`: Retrieves metadata for a data file.
- `List Data File Connections`: Retrieves a list of metadata for data file connections.

Updated blocks in the **Qlik Cloud Services** connector:

- `Copy Data File`: Added folder support.
- `List Data Files`: Added folder support.
- `Create Folder`: Added support for creating folders in spaces.
