---
source: https://qlik.dev/changelog/262-scheduling-tasks-api-reload-task-endpoints/
last_updated: 2026-10-28T19:20:17+01:00
---

# New Scheduling Tasks API endpoints for creating reload tasks

The [Scheduling Tasks API](https://qlik.dev/apis/rest/scheduling/tasks/) now includes three endpoints for creating reload tasks with a
single request. These endpoints simplify creating reload tasks when moving from the deprecated
[Reload Tasks API](https://qlik.dev/apis/rest/reload-tasks/). The service generates the task definition, so you don't need to construct
it yourself.

The following endpoints are available:

- `POST /api/scheduling/tasks/resources/{id}/actions/reload/on-time-schedule`: Creates a reload task that runs on a
  recurring schedule defined by an RFC 5545 recurrence rule.
- `POST /api/scheduling/tasks/resources/{id}/actions/reload/on-task-event`: Creates a reload task triggered when another
  task finishes with the specified status (`succeeded`, `failed`, or `any`).
- `POST /api/scheduling/tasks/resources/{id}/actions/reload/on-dataset-updated`: Creates a reload task triggered when a
  Qlik Talend Cloud pipeline updates a dataset used by the app. An app can have only one task of this type.

In each endpoint, `{id}` is the ID of the app to reload. Tasks are disabled by default. Set enabled to true when
creating a task to enable it. You need the `app:reload` permission on the app.

For advanced configurations, use `POST /api/scheduling/tasks`.

For more information, see the [Scheduling Tasks API reference](https://qlik.dev/apis/rest/scheduling/tasks/).
