---
source: https://qlik.dev/changelog/258-workflows-automations-interval-deprecation/
last_updated: 2026-11-12T11:04:27Z
---

# schedules\[].interval property deprecated in Workflows Automations API

> **Note:** Updated on November 12, 2026: Corrected the earliest removal date from November 30 to November 1, 2027.

The `schedules[].interval` property in the [Workflows Automations API](https://qlik.dev/apis/rest/workflows/automations/) is deprecated
and will be removed on or after November 1, 2027.

The deprecation applies to the `schedules` objects used by the following operations:

- `POST /api/workflows/automations`
- `PUT /api/workflows/automations/{id}`
- `GET /api/workflows/automations/{id}`

Replace `schedules[].interval`, which specifies an interval in seconds, with `schedules[].recurrence`, which uses an
RRULE to define the automation schedule.

For example:

```json
{
  "schedules": [
    {
      "recurrence": "RRULE:FREQ=DAILY;BYHOUR=9;BYMINUTE=0;BYSECOND=0"
    }
  ]
}
```
