---
source: https://qlik.dev/changelog/76-api-updates-di-projects/
last_updated: 2025-07-08T16:09:30Z
---

# New API - Qlik Cloud Data Integration APIs

Qlik Cloud Data Integration is a powerful data integration fabric that helps
data engineers deliver, transform, and unify enterprise data in real-time via
automated, governed, and reusable data pipelines.

The new `di-projects` APIs can be leveraged by your usual API tooling, or via Qlik
Automate, providing a way to:

- List Projects: Retrieves a list of data projects which belong to a given data space
- List Data Tasks: Retrieves a list of data tasks that belong to a given data project
- Get Project: retrieves a data project's information using its ID
- Get Data Task: Retrieves a single data task, using the project and task IDs
- Start Data Task: Starts a data task run, using the project and task IDs
- Stop Data Task: Stops a data task run, using the project and task IDs
- Get Data Task Runtime State: Retrieves the runtime state of a data task,
  using the project and task Ids returning the list of data integration

With this first iteration, users are able to create workflows that run Qlik Cloud
Data Integration tasks, such as:

- Starting a data task, waiting for it to finish, and proceeding to start another
  data task.
- Implementing conditions in an automation which are not implemented yet in Qlik
  Cloud Data Integration,
  like running a task only after all the sources have been updated.
- Building a workflow that stops CDC tasks before running some backend maintenance
  and then starting the CDC task again.

You can leverage Qlik Automate to do this without code:

![Qlik Cloud Data Integration connector in Qlik Automate](https://qlik.dev/_astro/connectors.iuJnV7jh.png)

![Qlik Cloud Data Integration connector blocks in Qlik Automate](https://qlik.dev/_astro/blocks.CeMD8wz6.png)

Example API call to retrieve tasks for a project via your own API tooling:

```bash
curl "https://your-tenant.us.qlikcloud.com/api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}" \
 -H "Authorization: Bearer <API-key>"
```

If the task exists, and you have access to it, you will receive a `200` response
with details of the task:

```json
{
 "id": "sqlserver_data_landing-5h5M",
 "name": "SQLServer-data_Landing",
 "type": "LANDING",
 "ownerId": "64ff3381259ad349da2046a9",
 "spaceId": "6502c7c2562be31c8343bbd4",
 "description": "This is the landing task for SQL server"
}
```

Now that you have the task, you can start it:

```bash
curl "https://your-tenant.us.qlikcloud.com/api/v1/di-projects/{projectId}/di-tasks/{dataTaskId}/runtime/actions/start" \
-X POST \
-H "Authorization: Bearer <API-key>"
```

If successful, you will receive a `204` response with no body.

Review the [DI projects](https://qlik.dev/apis/rest/di-projects/)
API specification for more information about this API.
