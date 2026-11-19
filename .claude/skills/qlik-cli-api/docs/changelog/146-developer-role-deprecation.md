---
source: https://qlik.dev/changelog/146-developer-role-deprecation/
last_updated: 2025-06-16T14:59:09Z
---

# Developer role and Enable API keys toggle deprecated

The **Developer** role in **Administration > Manage users > Permissions** is deprecated and will be removed before the
end of 2025.

To avoid disruptions, migrate affected users and groups to a custom role that includes the Manage API keys permission or
enable this permission in the User Default settings.
For more information about creating a replacement role, see [Managing custom roles](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/permissions-custom-roles-capacity-model.htm)
on help.qlik.com.

The **Enable API keys** toggle in **Administration > Settings** and the `api_keys_enabled` option in the [API keys API](https://qlik.dev/apis/rest/api-keys/)
are also deprecated and will be removed before the end of 2025.

After removal, API key creation will be controlled exclusively by the Manage API keys permission.
Users with this permission can create API keys from **Profile settings > API keys**.
For more information, see [Generate your first API key](https://qlik.dev/authenticate/api-key/generate-your-first-api-key).
