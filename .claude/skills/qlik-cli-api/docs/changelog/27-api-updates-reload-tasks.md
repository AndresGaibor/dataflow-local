---
source: https://qlik.dev/changelog/27-api-updates-reload-tasks/
last_updated: 2025-07-08T16:09:30Z
---

# New API - Reload tasks

### Reload tasks

Reload-tasks are the resources of reload tasks. With this API you can:

- `GET/v1/reload-tasks`: Find and return the tasks that the user can access.

```bash
curl "https://your-tenant.us.qlikcloud.com/api/v1/reload-tasks" \
 -H "Authorization: Bearer <API-key>"
```

- `POST/v1/reload-tasks` : Create a task for a specified app.

```bash
curl "https://your-tenant.us.qlikcloud.com/api/v1/reload-tasks" \
 -X POST \
 -H "Authorization: Bearer <API-key>" \
 -H "Content-type: application/json" \
 -d '{
  "appId": "116dbfae-7fb9-4983-8e23-5ccd8c508722",
  "partial": true,
  "timeZone": "string",
  "autoReload": true,
  "recurrence":
  [
    "FREQ=DAILY;BYHOUR=8;BYMINUTE=0;BYSECOND=0",
    "FREQ=WEEKLY;BYHOUR=10;BYMINUTE=0;BYSECOND=0"
  ],
  "endDateTime": "2018-11-09 14:46:07.697 +0000 UTC",
  "startDateTime": "2018-11-09 14:46:07.697 +0000 UTC",
  "autoReloadPartial": true,
  "type": "scheduled_reload"
}'
```

- `PUT/v1/reload-tasks/{taskId}`: Update an existing task.

```bash
curl "https://your-tenant.us.qlikcloud.com/api/v1/reload-tasks/{taskId}" \
 -X PUT \
 -H "Authorization: Bearer <API-key>" \
 -H "Content-type: application/json" \
 -d '{
  "appId": "116dbfae-7fb9-4983-8e23-5ccd8c508722",
  "partial": true,
  "timeZone": "string",
  "autoReload": true,
  "recurrence":
  [
    "FREQ=DAILY;BYHOUR=8;BYMINUTE=0;BYSECOND=0",
    "FREQ=WEEKLY;BYHOUR=10;BYMINUTE=0;BYSECOND=0"
  ],
  "endDateTime": "2018-11-09 14:46:07.697 +0000 UTC",
  "startDateTime": "2018-11-09 14:46:07.697 +0000 UTC",
  "autoReloadPartial": true,
  "state": "Disabled"
}'
```

See full API reference [here](https://qlik.dev/apis/rest/reload-tasks).
