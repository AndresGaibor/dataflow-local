---
source: https://qlik.dev/changelog/205-in-app-reporting-toggle-deprecation/
last_updated: 2026-03-23T10:04:39Z
---

# Deprecation - Reporting template subscription toggle in the Sharing tasks API

The **reporting template subscription toggle** (`enable-reporting-template-subscription`) in the
[Sharing tasks API](https://qlik.dev/apis/rest/sharing-tasks/) is being deprecated and will be removed on or after April 28, 2026.

Review your tenant permissions and update any API calls that use the `enable-reporting-template-subscription` property.
For guidance, see [Configure tabular reporting](https://qlik.dev/manage/tenants/tenant-features/#configure-tabular-reporting).

After removal, template reporting access will be controlled exclusively by permissions.
Most users will experience no functional change since this permission was enabled by default.

For more information, see [Setting permissions for metered reporting features](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-permissions-reporting.htm)
on Qlik Help.
