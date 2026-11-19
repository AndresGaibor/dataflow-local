---
source: https://qlik.dev/changelog/123-platform-ops-connector/
last_updated: 2025-06-19T11:53:14Z
---

# Block updates - Qlik Platform Operations & Qlik Cloud Services connectors

The [Qlik Platform Operations](https://qlik.dev/manage/platform-operations/no-code/overview)
and Qlik Cloud Services connectors for [Qlik Automate](https://qlik.dev/toolkits/no-code/)
enable the deployment and management of Qlik Cloud tenants without any code.

New blocks in the **Qlik Platform Operations** connector:

- `Create Group`: A replacement for the renamed `Create Multiple IdP Groups` block.
  Supports creation of either IdP or custom groups.
- `Update Group`: Updates existing IdP or custom groups.
- `Add Or Remove User From Custom Group`: Adds or removes the specified user from the
  provided custom group.
- `Create Multiple Pinned Links`: Permits bulk creation of pinned links.
- `Create Pinned Link`: Creates a pinned link.
- `List Pinned Links`: Retrieves a list of all pinned links.
- `Get Pinned Link`: Retrieves a pinned link.
- `Update Pinned Link`: Updates a pinned link.
- `Delete All Pinned Links`: Bulk deletes all pinned links.
- `Delete Pinned Link`: Deletes a pinned link.
- `List Analytics App Media Files`: Retrieves a list of media files from a Analytics app.
- `Get Analytics App Media File`: Retrieves the specified media file from a Analytics app.
- `Get Analytics App Thumbnail Media File`: Retrieves the thumbnail image for a Analytics app.
- `Upload Analytics App Media File`: Uploads a media file to a Analytics app.
- `Delete Analytics App Media File`: Deletes the specified media file from a Analytics app.

Updated blocks in the **Qlik Platform Operations** connector:

- `List Members From Space`: Added new inputs to filter directly on the ID of a
  user or group, assignee type, and querystring.
- `Create Group` has been renamed to `Create Multiple IdP Groups` following the
  launch of custom groups.
  Use the replacement `Create Group` block if you wish to leverage custom groups.
- `Update Group` has been renamed to `Update Group Roles` following the launch of
  custom groups. Use the replacement `Update Group` block if you wish to update
  properties of custom groups.
- `Add Role To Group By Name`: has been updated to support custom groups. Note
  that the default behavior is to add roles to IdP groups. If you wish to add
  roles to custom groups, you must specify the group type as `custom` in the block
  configuration.
- `Remove Role From Group By Name`: has been updated to support custom groups.
  Note that the default behavior is to add roles to IdP groups. If you wish to add
  roles to custom groups, you must specify the group type as `custom` in the block
  configuration.

New blocks in the **Qlik Cloud Services** connector:

- `Copy Data File`: Duplicates the specified data file.
- `Get Analytics App Media File`: Retrieves the specified media file from a Analytics app.
- `Get Analytics App Thumbnail Media File`: Retrieves the thumbnail image for a
  Analytics app.
- `Upload Analytics App Media File`: Uploads a media file to a Analytics app.
- `Delete Analytics App Media File`: Deletes the specified media file from a Analytics
  app.

Updated blocks in the **Qlik Cloud Services** connector:

- `List Members From Space`: Added new inputs to filter directly on the ID of a
  user or group, assignee type, and querystring.
- `List Analytics App Media Files`: Renamed from `List Media Files In App` to align
  with naming of new media file handling blocks.
