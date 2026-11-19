---
source: https://qlik.dev/changelog/226-di-projects-api-task-run-endpoints/
last_updated: 2026-06-18T07:31:19Z
---

# New Data Integration Projects API endpoints for querying task run history

The Data Integration Projects APIs now include three new endpoints to search and
inspect historical run data for data tasks.

The following new endpoints provide visibility into task run history:

- `POST /di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/runs/actions/search`:
  Get a list of historical run instances for a given data task, with support for
  pagination to navigate large result sets.
- `GET /di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/runs/{runId}/state`:
  Retrieve the state of a specific run instance by its run ID, including the run
  start and end time, duration, state and more.
- `GET /di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/runs/{runId}/state/datasets`:
  Retrieve dataset-level state details for a specific run, providing granular
  visibility into individual dataset processing within that run.

These additions enable greater observability for data task executions, making it
easier to monitor run outcomes and troubleshoot issues programmatically.

For more information, refer to the [Data integration projects API reference
documentation](https://qlik.dev/apis/rest/di-projects/).
