---
source: https://qlik.dev/changelog/227-scheduling-tasks-events-api/
last_updated: 2026-06-26T10:33:08+02:00
---

# New Scheduling Tasks event API for monitoring task lifecycle

The Scheduling Tasks event API is now available, letting you react to task
changes in real time, audit modifications, and keep external systems in sync.
You can fetch those new events through the audits endpoint:

```console
GET /api/v1/audits?source=com.qlik/choreographer
```

- **Task created** (`com.qlik.scheduling.task.created`): Published when you
  create a new scheduling task. Includes the task ID, owner, associated
  resource, and scheduled action details.
- **Task updated** (`com.qlik.scheduling.task.updated`): Published when you
  modify an existing task. Includes the full task state and a change log with
  old and new values for each field. Also emitted when a task is disabled due to
  repeated failures.
- **Task deleted** (`com.qlik.scheduling.task.deleted`): Published when you
  delete a task. Includes the full task state at the moment of deletion.

For more information, see the [Scheduling Tasks API
reference](https://qlik.dev/apis/event/scheduling/tasks/).
