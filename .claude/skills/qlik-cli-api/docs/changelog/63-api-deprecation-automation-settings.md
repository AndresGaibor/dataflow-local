---
source: https://qlik.dev/changelog/63-api-deprecation-automation-settings/
last_updated: 2025-06-19T11:53:14Z
---

# API Updates - Deprecation of /v1/automations/settings

This changelog provides 60 days notice of deprecation and removal of
the `/v1/automations/settings` endpoints.

These endpoints turn on and off Qlik Automate on a tenant, and this
capability was superseded by the addition in July 2023 of a new role, `Automation Creator`.
This new role provides much greater flexibility in who can use automations, including
at tenant, group, and user level.

For more information on Qlik's API policies, please refer to
the API policy page.

### Migrating to use the automation creator role

To provide all users in the tenant with access to create and run automations,
you must add the `AutomationCreator` role to the `Everyone` group.

Assuming the `Everyone` group already had the `PrivateAnalyticsContentCreator` role
assigned, you would send a request to replace the `assignedRoles` with the new list
of `PrivateAnalyticsContentCreator` and `AutomationCreator`:

```bash
curl -L -X PATCH "https://<TENANT>/api/v1/groups/000000000000000000000001" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-type: application/json" ^
-H "Accept: application/json" ^
-d "[{\"op\": \"replace\", \"path\": \"/assignedRoles\", \"value\": [{\"name\": \"PrivateAnalyticsContentCreator\"}, {\"name\": \"SharedSpaceCreator\"}]}]"
```

If successful, an empty response with an `http 204` code is returned.

In a similar way, you can also assign access to groups from your Identity Provider,
or to individual users.

For more information, please review
the configure Qlik Automate
topic.
