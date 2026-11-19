---
source: https://qlik.dev/changelog/247-semantic-types-api/
last_updated: 2026-10-01T15:03:30+02:00
---

# New REST API - Semantic types API for exporting and importing semantic types

The new [Semantic types API](https://qlik.dev/apis/rest/data-governance/semantic-types/) lets you export and import semantic type
definitions programmatically. Reuse semantic types across tenants, or migrate them from a legacy Talend environment
into Qlik Cloud. For more information about semantic types, see [Managing semantic types](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataProducts/Managing-semantic-types.htm)
on Qlik Help.

The API supports the following operations:

- `POST /api/data-governance/semantic-types/actions/export`: Export semantic types from a tenant as a JSON file,
  optionally filtered by ID, type, creator, or a search string.
- `POST /api/data-governance/semantic-types/actions/import`: Preview an import to see which semantic types are new,
  conflicting, or have errors, then resolve conflicts and apply the import. Supports both the Qlik Cloud export
  format and the Talend legacy format.

For more information, see the [Semantic types API reference](https://qlik.dev/apis/rest/data-governance/semantic-types/) and
[Import and export semantic types](https://qlik.dev/manage/data-governance/import-export-semantic-types/) for a full walkthrough of
the export and import workflow, including conflict resolution.
