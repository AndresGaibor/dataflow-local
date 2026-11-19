---
source: https://qlik.dev/changelog/21-api-updates-automations/
last_updated: 2025-06-26T10:42:10Z
---

# New API - Qlik Automate

> Updated on June 16, 2025:  Qlik Application Automation  has been renamed to Qlik Automate.

## Introducing Qlik Automate

Happy to announce the release of a new API: Qlik Automate.

Qlik Automate is a visual no-code approach to connecting applications.
The API helps you easily build automated analytics and data workflows.

### Examples

Here are a few examples of what you can expect to do with the Qlik Automate API:

- Create an automation.

```shell
curl "https://your-tenant.us.qlikcloud.com/api/v1/automations" \
 -X POST \
 -H "Authorization: Bearer <API-key>" \
 -H "Content-type: application/json" \
 -d '{
     "name":"string",
     "description":"string",
     "workspace":{},
     "state":"available",
     "schedules":[
         {
             "startAt":"2022-01-01 00:00:00",
             "stopAt":"2022-12-01 00:00:00",
             "interval":30,
             "timezone":"Europe/Stockholm"
         }
         ]
    }'
```

- Enable an automation.
- Retrieve and update automation settings.
- Copy an automation.
- Create a run.

```shell
curl "https://your-tenant.us.qlikcloud.com/api/v1/automations/{id}/runs" \
 -X POST \
 -H "Authorization: Bearer <API-key>" \
 -H "Content-type: application/json" \
 -d '{
     "id":"automationID",
     "context":"editor",
     "inputs":{}
     }'
```

- Retrieves a run.
- Retry a run
- Stop running an automation
- Export a run
- Move automation to another user

For more information you can see API reference
