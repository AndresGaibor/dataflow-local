---
title: "Onfleet"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Onfleet.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Onfleet

Onfleet is a cloud-based fleet management solution that offers route optimization, auto-dispatching, delivery analytics and customer communications.

Onfleet integration replicates data using the [Onfleet REST API](https://docs.onfleet.com/reference/introduction).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

You must have administrative privileges to create a user in your Onfleet account.

To create an API key:

1. Log into your [Onfleet](https://onfleet.com/login) account.
2. Go to the API & Webhooks tab.
3. In the API Keys section, click +.
4. In the Name field, enter a name for the API key.
5. Click Create Key.
6. Copy and paste your API key into a secured file.

If you restrict an API key’s scopes, Qlik Talend Cloud can replicate only the scopes defined for that key.

## Creating the connection

For more information, see [*Connecting to SaaS applications*](../Landing/connecting-web-applications.htm).

1. Fill in the required connection properties.
2. Provide a name for the connection in Connection name.
3. Select Open connection metadata to define metadata for the connection when it has been created.
4. Click Create.

Connection settings

| Setting | Description |
| --- | --- |
| Data gateway | Select a Data Movement gateway if required by your use case.  Information note This field is not available with the Qlik Talend Cloud Starter subscription, as it does not support Data Movement gateway. If you have another subscription tier and do not want to use Data Movement gateway, select None.  For information on the benefits of Data Movement gateway and use cases that require it, see [*Qlik Data Gateway - Data Movement*](../../Gateways/replication-gateway.htm). |
| Start Date | Enter the date, in the format `MM/DD/YYYY`, from which the data must be replicated from your source to your target. |
| API Key | API key. |
| Quota Limit | Enter the percentage of the Onfleet API quota that is allowed to use. For example, entering 10 would allow Qlik Talend Cloud to use 10% of the API quota. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### administrators

The `administrators` table contains info about the administrators in your Onfleet account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | timeLastModified |
| **Useful links** | [Onfleet API method](http://docs.onfleet.com/Content/administrators#list-administrators "Opens in new tab: Onfleet API method") |

administrators table foreign keys

| Join administrators with | on |
| --- | --- |
| [tasks](#tasks) | ``` administrators.id = tasks.creator ```  ``` administrators.organization = tasks.organization ``` |
| [teams](#teams) | ``` administrators.id = teams.managers ``` |
| [organizations](#organizations) | ``` administrators.organization = organizations.id ```  ``` administrators.organization = organizations.delegatees ``` |
| [workers](#workers) | ``` administrators.organization = workers.organization ``` |

administrators table schema

|  |
| --- |
| **email**  STRING |
| **id**  STRING |
| **isActive**  BOOLEAN |
| **metadata**  ARRAY This is a nested data structure. |
| **name**  STRING |
| **organization**  STRING |
| **phone**  STRING |
| **timeCreated**  DATE-TIME |
| **timeLastModified**  DATE-TIME |
| **type**  STRING |

### hubs

The `hubs` table contains info about the hubs, or depots, for teams in your Onfleet account. A hub is the location from which all deliveries for a team’s workers start.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Onfleet documentation](http://docs.onfleet.com/Content/hubs)  [Onfleet API method](http://docs.onfleet.com/Content/hubs#list-hubs "Opens in new tab: Onfleet API method") |

hubs table foreign keys

| Join hubs with | on |
| --- | --- |
| [teams](#teams) | ``` hubs.id = teams.hub ```  ``` hubs.teams = teams.id ``` |
| [workers](#workers) | ``` hubs.teams = workers.teams ``` |

hubs table schema

|  |
| --- |
| **address**  OBJECT This is a nested data structure:   - apartment: STRING - city: STRING - country: STRING - number: STRING - postalCode: STRING - state: STRING - street: STRING |
| **id**  STRING |
| **location**  ARRAY |
| **name**  STRING |
| **teams**  ARRAY This is a nested data structure. |

### organizations

The `organizations` table contains info about the organizations in your Onfleet account. In Onfleet, an organization is the top-most entity - it contains administrators, teams, works, and tasks, all of which belong to the organization.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | timeLastModified |
| **Useful links** | [Onfleet documentation](http://docs.onfleet.com/Content/organizations)  [Onfleet API method](http://docs.onfleet.com/Content/organizations#get-details "Opens in new tab: Onfleet API method") |

organizations table foreign keys

| Join organizations with | on |
| --- | --- |
| [administrators](#administrators) | ``` organizations.id = administrators.organization ```  ``` organizations.delegatees = administrators.organization ``` |
| [tasks](#tasks) | ``` organizations.id = tasks.organization ```  ``` organizations.delegatees = tasks.organization ``` |
| [workers](#workers) | ``` organizations.id = workers.organization ```  ``` organizations.delegatees = workers.organization ``` |

organizations table schema

|  |
| --- |
| **country**  STRING |
| **delegatees**  ARRAY This is a nested data structure. |
| **email**  STRING |
| **id**  STRING |
| **image**  STRING |
| **name**  STRING |
| **timeCreated**  DATE-TIME |
| **timeLastModified**  DATE-TIME |
| **timezone**  STRING |

### tasks

The `tasks` table contains info about the tasks in your Onfleet account. Tasks are units of work that [`administrators`](#administrators) create and assign to [`workers`](#workers) for completion.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | timeLastModified |
| **Useful links** | [Onfleet documentation](http://docs.onfleet.com/Content/tasks)  [Onfleet API method](http://docs.onfleet.com/Content/tasks#list-tasks "Opens in new tab: Onfleet API method") |

tasks table foreign keys

| Join tasks with | on |
| --- | --- |
| [administrators](#administrators) | ``` tasks.creator = administrators.id ```  ``` tasks.organization = administrators.organization ``` |
| [teams](#teams) | ``` tasks.creator = teams.managers ```  ``` tasks.id = teams.tasks ```  ``` tasks.worker = teams.workers ``` |
| [organizations](#organizations) | ``` tasks.organization = organizations.id ```  ``` tasks.organization = organizations.delegatees ``` |
| [workers](#workers) | ``` tasks.organization = workers.organization ```  ``` tasks.id = workers.activeTask ```  ``` tasks.id = workers.tasks ```  ``` tasks.worker = workers.id ``` |

tasks table schema

|  |
| --- |
| **completeAfter**  NUMBER |
| **completeBefore**  NUMBER |
| **completionDetails**  OBJECT This is a nested data structure:   - events: ARRAY, which is also a nested data structure. - failureReason: STRING - firstLocation: ARRAY, which is also a nested data structure. - lastLocation: ARRAY, which is also a nested data structure. - time: DATE-TIME - unavailableAttachments: ARRAY, which is also a nested data structure. |
| **creator**  STRING |
| **delayTime**  NUMBER |
| **dependencies**  ARRAY This is a nested data structure. |
| **destination**  OBJECT This is a nested data structure:   - address: OBJECT, which is also a nested data structure.   - apartment: STRING   - city: STRING   - country: STRING   - number: STRING   - postalCode: STRING   - state: STRING   - street: STRING - id: STRING - location: ARRAY, which is also a nested data structure. - metadata: ARRAY, which is also a nested data structure. - notes: STRING - timeCreated: DATE-TIME - timeLastModified: DATE-TIME |
| **estimatedCompletionTime**  NUMBER |
| **executor**  STRING |
| **feedback**  ARRAY This is a nested data structure. |
| **id**  STRING |
| **identity**  OBJECT This is a nested data structure:   - checksum: STRING - failedScanCount: NUMBER |
| **merchant**  STRING |
| **metadata**  ARRAY This is a nested data structure. |
| **notes**  STRING |
| **organization**  STRING |
| **overrides**  OBJECT This is a nested data structure. |
| **pickupTask**  BOOLEAN |
| **quantity**  NUMBER |
| **recipients**  ARRAY This is a nested data structure:   - id: STRING - metadata: ARRAY, which is also a nested data structure. - name: STRING - notes: STRING - organization: STRING - phone: STRING - skipSMSNotifications: BOOLEAN - timeCreated: DATE-TIME - timeLastModified: DATE-TIME |
| **serviceTime**  NUMBER |
| **shortId**  STRING |
| **sourceTaskId**  STRING |
| **state**  NUMBER |
| **timeCreated**  DATE-TIME |
| **timeLastModified**  DATE-TIME |
| **trackingURL**  STRING |
| **trackingViewed**  BOOLEAN |
| **worker**  STRING |

### teams

The `teams` table contains info about the teams in your Onfleet account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | timeLastModified |
| **Useful links** | [Onfleet documentation](http://docs.onfleet.com/Content/teams)  [Onfleet API method](http://docs.onfleet.com/Content/teams#list-teams "Opens in new tab: Onfleet API method") |

teams table foreign keys

| Join teams with | on |
| --- | --- |
| [administrators](#administrators) | ``` teams.managers = administrators.id ``` |
| [tasks](#tasks) | ``` teams.managers = tasks.creator ```  ``` teams.tasks = tasks.id ```  ``` teams.workers = tasks.worker ``` |
| [hubs](#hubs) | ``` teams.hub = hubs.id ```  ``` teams.id = hubs.teams ``` |
| [workers](#workers) | ``` teams.tasks = workers.activeTask ```  ``` teams.tasks = workers.tasks ```  ``` teams.id = workers.teams ```  ``` teams.workers = workers.id ``` |

teams table schema

|  |
| --- |
| **hub**  STRING |
| **id**  STRING |
| **managers**  ARRAY This is a nested data structure. |
| **name**  STRING |
| **tasks**  ARRAY This is a nested data structure. |
| **timeCreated**  DATE-TIME |
| **timeLastModified**  DATE-TIME |
| **workers**  ARRAY This is a nested data structure. |

### workers

The `workers` table contains info about the workers (or drivers) in your Onfleet account. Workers are organization members who complete tasks.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | timeLastModified |
| **Useful links** | [Onfleet documentation](http://docs.onfleet.com/Content/workers)  [Onfleet API method](http://docs.onfleet.com/Content/workers#list-workers "Opens in new tab: Onfleet API method") |

workers table foreign keys

| Join workers with | on |
| --- | --- |
| [administrators](#administrators) | ``` workers.organization = administrators.organization ``` |
| [organizations](#organizations) | ``` workers.organization = organizations.id ```  ``` workers.organization = organizations.delegatees ``` |
| [tasks](#tasks) | ``` workers.organization = tasks.organization ```  ``` workers.activeTask = tasks.id ```  ``` workers.tasks = tasks.id ```  ``` workers.id = tasks.worker ``` |
| [teams](#teams) | ``` workers.activeTask = teams.tasks ```  ``` workers.tasks = teams.tasks ```  ``` workers.teams = teams.id ```  ``` workers.id = teams.workers ``` |
| [hubs](#hubs) | ``` workers.teams = hubs.teams ``` |

workers table schema

|  |
| --- |
| **accountStatus**  STRING |
| **activeTask**  STRING |
| **capacity**  NUMBER |
| **delayTime**  NUMBER |
| **displayName**  STRING |
| **id**  STRING |
| **imageUrl**  STRING |
| **location**  STRING |
| **metadata**  ARRAY This is a nested data structure. |
| **name**  STRING |
| **onDuty**  BOOLEAN |
| **organization**  STRING |
| **phone**  STRING |
| **tasks**  ARRAY This is a nested data structure. |
| **teams**  ARRAY This is a nested data structure. |
| **timeCreated**  DATE-TIME |
| **timeLastModified**  DATE-TIME |
| **timeLastSeen**  DATE-TIME |
| **userData**  OBJECT This is a nested data structure:   - appVersion: STRING - batteryLevel: NUMBER - deviceDescription: STRING - platform: STRING |
| **vehicle**  OBJECT This is a nested data structure:   - color: STRING - description: STRING - id: STRING - licensePlate: STRING - timeLastModified: DATE-TIME - type: STRING |
