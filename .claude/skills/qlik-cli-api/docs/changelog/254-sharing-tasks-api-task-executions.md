---
source: https://qlik.dev/changelog/254-sharing-tasks-api-task-executions/
last_updated: 2026-10-06T14:14:34+02:00
---

# New Sharing tasks API endpoints in the Alerting namespace

The [Sharing tasks API](https://qlik.dev/apis/rest/alerting/sharing-tasks/) is now available in the Alerting namespace with two
endpoints for retrieving the execution history of a sharing task:

- `GET /api/alerting/sharing-tasks/{taskId}/task-executions`: Lists the executions of a sharing task. Executions that
  are in progress aren't included.
- `GET /api/alerting/sharing-tasks/{taskId}/task-executions/{taskExecutionId}`: Retrieves the details of a single
  execution of a sharing task.

Use these endpoints to check whether sharing tasks ran as expected and to monitor their execution status
programmatically.

For more information, see the [Sharing tasks API reference](https://qlik.dev/apis/rest/alerting/sharing-tasks/).
