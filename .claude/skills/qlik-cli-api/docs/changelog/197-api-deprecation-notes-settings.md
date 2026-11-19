---
source: https://qlik.dev/changelog/197-api-deprecation-notes-settings/
last_updated: 2026-02-16T11:36:38+01:00
---

# Deprecation notice - Settings endpoint in the Notes API

The `/api/v1/notes/settings` endpoint is being deprecated in favor of permissions-based configuration.

The endpoint will be removed on or after **March 31, 2026**.

To configure note settings, use the permissions-based approach through user default permissions instead of the
`/api/v1/notes/settings` endpoint.

For more information about configuring permissions, see [Controlling user access to Notes](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/permissions-scopes-notes.htm)
on help.qlik.com.

> **Important:** Once the Qlik Cloud user interface removes support for these settings, values configured through the
> `/api/v1/notes/settings` endpoint will no longer be applied.
