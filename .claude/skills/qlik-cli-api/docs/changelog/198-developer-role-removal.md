---
source: https://qlik.dev/changelog/198-developer-role-removal/
last_updated: 2026-01-26T15:49:02+01:00
---

# Developer role and Enable API keys toggle removed

> **Note:** This functionality is rolled out in phases and may not be immediately available in all regions.

The Developer role has now been removed, following the June 2025 deprecation announcement and the recent
[Qlik Community blog reminder](https://community.qlik.com/t5/Support-Updates/Qlik-Cloud-Removing-the-deprecated-Developer-role-and-Enable-API/ba-p/2535358).
The role has been removed from all users and groups. It's replaced by the Manage API keys permission, which you can
assign as part of a [custom roles](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/permissions-custom-roles-capacity-model.htm).

Users and groups that were not previously migrated to the Manage API keys permission may experience disruptions.
For guidance, see the supporting [Qlik Community migration steps article](https://community.qlik.com/t5/Official-Support-Articles/Qlik-Cloud-Removing-the-deprecated-Developer-role-and-Enable-API/ta-p/2534952).

The Enable API keys toggle in **Administration > Settings** and the `api_keys_enabled` option in the
[API keys API](https://qlik.dev/apis/rest/api-keys/) have also been removed.
API key creation is now fully controlled through the Manage API keys permission.
