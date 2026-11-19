---
source: https://qlik.dev/changelog/153-api-updates-sharing-tasks/
last_updated: 2025-07-11T16:40:35+01:00
---

# Updated API - Next execution endpoints for the Sharing Tasks API

You can now programmatically monitor and retrieve results from executions of the
[Sharing Tasks API](https://qlik.dev/apis/rest/sharing-tasks/). These new endpoints provide visibility
into past task runs and support retrieval of output files generated during each execution.

New endpoints:

- `GET /api/v1/sharing-tasks/{taskId}/executions` - Lists all executions of a sharing task.
- `GET /api/v1/sharing-tasks/{taskId}/executions/{executionId}` - Retrieves metadata
  for a specific execution. Use "latest" as the executionId to get the most recent run.
- `GET /api/v1/sharing-tasks/{taskId}/executions/{executionId}/files/{fileAlias}` - Downloads
  a specific file output from an execution (data or visualization image snapshot).

For more information, refer to the [Sharing Tasks API reference documentation](https://qlik.dev/apis/rest/sharing-tasks/).
