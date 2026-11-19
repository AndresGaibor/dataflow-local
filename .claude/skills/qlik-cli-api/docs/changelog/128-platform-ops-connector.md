---
source: https://qlik.dev/changelog/128-platform-ops-connector/
last_updated: 2025-06-19T11:53:14Z
---

# Block updates - Qlik Platform Operations & Qlik Cloud Services connectors

The [Qlik Platform Operations](https://qlik.dev/manage/platform-operations/no-code/overview)
and Qlik Cloud Services connectors for [Qlik Automate](https://qlik.dev/toolkits/no-code/)
enable the deployment and management of Qlik Cloud tenants without any code.

New blocks in the **Qlik Platform Operations** connector:

- `Create Space Share`: Creates a space share to share a resource to a specific user,
  group, or link.
- `List Space Shares`: Lists all space shares for a space.
- `Get Space Share`: Retrieves a specific space share.
- `Update Space Share`: Updates an existing space share.
- `Delete Space Share`: Removes a specific space share.

No blocks were updated in the **Qlik Platform Operations** connector this release.

New blocks in the **Qlik Cloud Services** connector:

- `Create Group`: Supports creation of either IdP or custom groups.
- `Update Group`: Updates existing IdP or custom groups.
- `Add Or Remove User From Custom Group`: Adds or removes the specified user from the
  provided custom group.
- `Add Role To Group By Name`: Adds a role to a group using the role and group name.
- `Remove Role From Group By Name`: Removes a role from a group using the role and
  group name.
- `Create Multiple Pinned Links`: Permits bulk creation of pinned links.
- `Create Pinned Link`: Creates a pinned link.
- `List Pinned Links`: Retrieves a list of all pinned links.
- `Get Pinned Link`: Retrieves a pinned link.
- `Update Pinned Link`: Updates a pinned link.
- `Delete All Pinned Links`: Bulk deletes all pinned links.
- `Delete Pinned Link`: Deletes a pinned link.

Updated blocks in the **Qlik Cloud Services** connector:

- `List Groups`: Added filter on provider type to select from IdP or custom groups.
- `List Data Assets By Data Store`: Pagination bug has been fixed.
- `List Data Stores`: Pagination bug has been fixed.
- `List Datasets By Data Asset`: Pagination bug has been fixed.
- `Raw API Request`: Added support for `ui-config` API.
- `Raw API List Request`: Added support for `ui-config` API.
