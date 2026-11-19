---
source: https://qlik.dev/changelog/135-tasks-api/
last_updated: 2026-04-20T13:34:03+01:00
---

# New REST API - The Tasks API for managing tasks and task chains in Qlik Cloud

The new [Tasks](https://qlik.dev/apis/rest/tasks/) API allows you to manage tasks and task chains in Qlik Cloud.
This API adds support for more complex workflows, including scheduled execution, event-based triggers, and task
orchestration with up to 10 tasks per resource.

> **Warning:** Existing reload tasks can be migrated to the new tasks service.
> However, once a Qlik Sense app has one or more tasks, reload tasks are turned off for that resource.

The new endpoints are:

- `GET /v1/tasks`: List tasks the requesting user has access to
- `POST /v1/tasks`: Create a new task
- `GET /v1/tasks/{id}`: Get task details
- `PUT /v1/tasks/{id}`: Update a task
- `DELETE /v1/tasks/{id}`: Delete a task
- `POST /v1/tasks/{id}/actions/start`: Start a task
- `GET /v1/tasks/{id}/runs`: List task runs
- `GET /v1/tasks/resources/{id}/runs`: List runs for a resource
- `GET /v1/tasks/{id}/runs/last`: Get the most recent task run
- `GET /v1/tasks/{id}/runs/{runId}/log`: Get a specific task run log

These operations require `reload` permission on the target resource.
Tenant admins can call `GET /v1/tasks` and `DELETE /v1/tasks/{id}`, even without this permission.

For more information, see:

- The [reference documentation for the Tasks API](https://qlik.dev/apis/rest/tasks/).
- The [migration guide for your reload tasks](https://qlik.dev/manage/analytics-applications/migrate-reload-tasks-to-tasks).
