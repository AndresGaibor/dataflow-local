---
source: https://qlik.dev/changelog/184-api-updates-di-projects-request-reload/
last_updated: 2025-11-27T14:53:57Z
---

# Updated API - Request dataset reloads using the Data integration projects API

The Data Integration Projects API now includes a new endpoint to request
dataset reloads directly through the API.

The following new endpoint provides control over dataset reloading:

- `POST /di-projects/{projectId}/di-tasks/{dataTaskId}/actions/request-reload` - Request a reload of one or multiple
  datasets within a data integration task. You can reload all datasets (default behavior) or specific datasets by
  providing their dataset IDs.

For transform tasks, you can also specify a reload strategy:

- `NONE` - Standard reload
- `TRUNCATE` - Clears the output table before reloading
- `COMPARE_AND_APPLY` - Compares source and target to apply only incremental differences

The actual reload takes place the next time the task runs, consistent with the behavior in the user interface.
This enhancement provides greater control and automation for dataset maintenance within your data integration workflows.

For more information, refer to the [Data integration projects API reference documentation](https://qlik.dev/apis/rest/di-projects/).
