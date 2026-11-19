---
source: https://qlik.dev/changelog/231-scheduling-tasks-api-and-reload-tasks-deprecation/
last_updated: 2026-09-28T11:33:43+02:00
---

# New Scheduling Tasks API and Reload Tasks API deprecation

> **Note:** This changelog entry was updated on September 28, 2026, to reflect the revised Reload Tasks API deprecation timeline.

The [Reload Tasks API](https://qlik.dev/apis/rest/reload-tasks/) is deprecated.

Starting **November 26, 2026**, you will no longer be able to create new reload tasks using `POST /api/v1/reload-tasks`.

Existing reload tasks will continue to run while they are migrated to the Scheduling Tasks service in the background.
Existing tasks can still be updated or deleted until they have been migrated.
After a task has been migrated, it can no longer be updated or deleted through the Reload Tasks API.
`GET` operations remain available during the migration.

Use the new [Scheduling Tasks API](https://qlik.dev/apis/rest/scheduling/tasks/) for new integrations.
It replaces the Reload Tasks API and supersedes the existing [Tasks API](https://qlik.dev/apis/rest/tasks/), providing capabilities
including scheduled execution, event-based triggers, task orchestration, dependency graphs, and task run history.

Any UI created events since April 2025 already use the new scheduling service and do not need to be migrated.

Migration guidance will be updated when the migration endpoint is publicly available.
