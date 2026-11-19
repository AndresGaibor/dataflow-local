---
source: https://qlik.dev/changelog/190-api-updates-di-projects-resume-replication-tasks/
last_updated: 2025-12-16T15:58:21Z
---

# Updated API - Resume Replication tasks using the Data integration projects API

The Data Integration projects API has been updated to support resuming a Replication task from a certain timestamp,
position, or locally stored checkpoint.

The `POST /api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/actions/start` endpoint now includes the
following optional request body parameters (valid for Replication tasks only):

- `option` - Specifies the change tracking mode as an enum with the following values:
  - `PROCESS_CHANGES_FROM_TIMESTAMP` - Resume processing changes from a specific timestamp
  - `PROCESS_CHANGES_FROM_POSITION` - Resume change processing from a source change position
  - `RECOVER_USING_LOCALLY_STORED_CHECKPOINT` - Resume processing using the locally stored checkpoint

- `processChangesFrom` - The corresponding value based on the selected `option`:
  - For `PROCESS_CHANGES_FROM_TIMESTAMP`: ISO 8601 timestamp (for example, `"2017-03-07T11:19:03"`)
  - For `PROCESS_CHANGES_FROM_POSITION`: Source change position value (for example, `"15000000040000037"`)

**Example request:**

```json
{
  "option": "PROCESS_CHANGES_FROM_TIMESTAMP",
  "processChangesFrom": "2017-03-07T11:19:03"
}
```

For more information, refer to the [Data integration project API reference documentation](https://qlik.dev/apis/rest/di-projects/#post-api-v1-di-projects-projectId-di-tasks-dataTaskId-runtime-actions-start).
