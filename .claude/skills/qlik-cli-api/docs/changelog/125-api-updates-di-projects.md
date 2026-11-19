---
source: https://qlik.dev/changelog/125-api-updates-di-projects/
last_updated: 2025-03-04T16:54:00+01:00
---

# Updated API - Data Integration Projects now includes validate and prepare endpoints

The [Data Integration Projects API](https://qlik.dev/apis/rest/di-projects/) has been updated with new endpoints that allow users to
validate and prepare their projects and tasks programmatically.

![Prepare dialog in the Qlik Talend Data Integration UI](https://qlik.dev/_astro/prepare-ui.X0u1woXF.png)

Using these new API endpoints, users can programmatically:

- Validate and prepare tasks at the project level, using the internal project orchestration
  logic:
  - Validate all tasks in a project: `POST /api/v1/di-projects/{ProjectID}/actions/validate`
  - Prepare all tasks in a project: `POST /api/v1/di-projects/{ProjectID}/actions/prepare`
- Validate and prepare tasks at the task level:
  - Validate a task: `POST /api/v1/di-projects/{ProjectID}/di-tasks/{dataTaskID}/actions/validate`
  - Prepare a task: `POST /api/v1/di-projects/{ProjectID}/di-tasks/{dataTaskID}/actions/prepare`
- Monitor the status of validate and prepare operations to ensure
  they are completed successfully before running tasks:
  - Get status: `GET /api/v1/di-projects/actions/{ActionID}`

These new endpoints can be leveraged alongside the existing [Export and Import endpoints](https://qlik.dev/changelog/76-api-updates-di-projects/)
to fully automate deployment use cases programmatically.

For more information, review the [reference documentation for the Data Integration Projects API](https://qlik.dev/apis/rest/di-projects/).
