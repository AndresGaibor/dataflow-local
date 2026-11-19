---
source: https://qlik.dev/changelog/195-di-projects-api-breaking-change/
last_updated: 2026-01-21T15:39:25+01:00
---

# Updated API - New endpoint and breaking change on Data integration projects API

## What's changing

- **New endpoint:**
  The `POST /di-projects/{projectId}/di-tasks/{dataTaskId}/actions/recreate-datasets`
  endpoint has been added to the Data integration projects API. This enables users
  to recreate datasets for specific data tasks.

- **Breaking change:**
  A breaking change is introduced on the `POST /api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/actions/prepare`
  endpoint. This change aligns the behavior of the `allowRecreate` property with the project-level
  API and UI for consistency.

The `allowRecreate` property allows users to control if tables are recreated in instances
where a design change cannot be applied to the existing tables, for example when the primary key changes.

> **Note:** This change only impacts task-level prepare implementations. The project-level
> Prepare behavior remains unchanged.
>
> - With `allowRecreate=true`, the prepare operation will recreate tables if necessary.
> - With `allowRecreate=false`, the prepare operation will not recreate tables.

### Migration

To adapt to this breaking change, migration depends on your existing use of the task prepare endpoint:

- If you don't want the prepare operation to recreate tables under any circumstances, use `allowRecreate=false`.
- If you want the prepare operation to recreate tables if there is a change that cannot
  otherwise be applied, use `allowRecreate=true`.
- If you want to recreate all tables unconditionally, use the new
  `recreate-datasets`: `POST /di-projects/{projectId}/di-tasks/{dataTaskId}/actions/recreate-datasets`
  endpoint instead of prepare.

For more information, refer to the [Data integration project API reference documentation](https://qlik.dev/apis/rest/di-projects).
