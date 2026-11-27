---
title: "Zendesk Chat"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Zendesk-Chat.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Zendesk Chat

Zendesk Chat is a live chat software platform that allows businesses to provide real-time customer support directly on their website or app.

Zendesk Chat integration replicates data using the [Zendesk Chat API](https://developer.zendesk.com/api-reference/live-chat/introduction/).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To generate your client ID and secret:

1. Log into your Zendesk chat domain, for example: https://my-sub-domain.zendesk.com/chat.
2. Expand the Settings menu on the left of the page and click Account.
3. Select the API and SDKs tab at the top of the page.
4. Select or add an API Client. Your client ID is displayed on the page.
5. Copy and save the client secret in a secured file. You will need it to connect to the application.

## Creating the connection

For more information, see [*Connecting to SaaS applications*](../Landing/connecting-web-applications.htm).

1. Click Authenticate when you have filled in the required connection settings.

   You may be asked to log in to the source application.

   A window is displayed with an authentication code.
2. Copy the code to the clipboard and return to the connection dialog.
3. Paste the code in Complete authentication with the code provided by the source and click Verify.

   Tip noteYou may need to scroll down to see this field.

   When status is Verified, the authentication is verified.
4. Provide a name for the connection in Connection name.
5. Select Open connection metadata to define metadata for the connection when it has been created.

Connection settings

| Setting | Description |
| --- | --- |
| Data gateway | Select a Data Movement gateway if required by your use case.  Information note This field is not available with the Qlik Talend Cloud Starter subscription, as it does not support Data Movement gateway. If you have another subscription tier and do not want to use Data Movement gateway, select None.  For information on the benefits of Data Movement gateway and use cases that require it, see [*Qlik Data Gateway - Data Movement*](../../Gateways/replication-gateway.htm). |
| Start Date | Enter the date, in the format `MM/DD/YYYY`, from which the data must be replicated from your source to your target. |
| Zendesk Subdomain | The subdomain of your Zendesk site. For example, the subdomain of `qlik.zendesk.com` would be `qlik`. |
| Client ID | Client ID. |
| Client Secret | Client secret. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### account

The `account` table contains info about accounts within your Zendesk Chat account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | account\_key |
| **Useful links** | [Zendesk Chat API method](https://developer.zendesk.com/api-reference/live-chat/chat-api/accounts/ "Opens in new tab: Zendesk Chat API method") |

account table foreign keys

| Join account with | on |
| --- | --- |
| [goals](#goals) | ``` account.plan.goals = goals.id ``` |
| [chats](#chats) | ``` account.plan.goals = chats.conversions.goal_id ```  ``` account.plan.goals = chats.history.conversion.goal_id ``` |

account table schema

|  |
| --- |
| **account\_key**  STRING |
| **billing**  OBJECT This is a nested data structure:   - additional\_info: STRING - address1: STRING - address2: STRING - city: STRING - company: STRING - country\_code: STRING - email: STRING - first\_name: STRING - last\_name: STRING - postal\_code: STRING - state: STRING |
| **create\_date**  DATE-TIME |
| **plan**  OBJECT This is a nested data structure:   - agent\_leaderboard: BOOLEAN - agent\_reports: BOOLEAN - analytics: BOOLEAN - chat\_reports: BOOLEAN - daily\_reports: BOOLEAN - email\_reports: BOOLEAN - file\_upload: BOOLEAN - goals: INTEGER - high\_load: BOOLEAN - integrations: BOOLEAN - ip\_restriction: BOOLEAN - long\_desc: STRING - max\_advanced\_triggers: STRING - max\_agents: INTEGER - max\_basic\_triggers: STRING - max\_concurrent\_chats: STRING - max\_departments: STRING - max\_history\_search\_days: STRING - monitoring: BOOLEAN - name: STRING - operating\_hours: BOOLEAN - price: NUMBER - rest\_api: BOOLEAN - short\_desc: STRING - sla: BOOLEAN - support: BOOLEAN - unbranding: BOOLEAN - widget\_customization: STRING |
| **status**  STRING |

### agents

The `agents` table contains info about agents within your Zendesk Chat account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Zendesk Chat API method](https://developer.zendesk.com/api-reference/live-chat/chat-api/agents/ "Opens in new tab: Zendesk Chat API method") |

agents table foreign keys

| Join agents with | on |
| --- | --- |
| [chats](#chats) | ``` agents.id = chats.agent_ids ```  ``` agents.departments = chats.department_id ```  ``` agents.departments = chats.history.prev_department_id ``` |
| [departments](#departments) | ``` agents.departments = departments.id ``` |
| [shortcuts](#shortcuts) | ``` agents.departments = shortcuts.departments ``` |

agents table schema

|  |
| --- |
| **create\_date**  DATE-TIME |
| **departments**  ARRAY |
| **display\_name**  STRING |
| **email**  STRING |
| **enabled**  BOOLEAN |
| **enabled\_departments**  ARRAY |
| **first\_name**  STRING |
| **id**  INTEGER |
| **last\_login**  DATE-TIME |
| **last\_name**  STRING |
| **login\_count**  INTEGER |
| **role\_id**  INTEGER |
| **roles**  OBJECT This is a nested data structure:   - administrator: BOOLEAN - owner: BOOLEAN |
| **scope**  STRING |
| **skills**  ARRAY |

### bans

The `bans` table contains info about bans created in your Zendesk Chat account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Zendesk Chat API method](https://developer.zendesk.com/api-reference/live-chat/chat-api/bans/ "Opens in new tab: Zendesk Chat API method") |

bans table schema

|  |
| --- |
| **created\_at**  DATE-TIME |
| **id**  INTEGER |
| **ip\_address**  STRING |
| **reason**  STRING |
| **type**  STRING |
| **visitor\_id**  STRING |
| **visitor\_name**  STRING |

### chats

The `chats` table contains info about the chats within your Zendesk Chat account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | timestamp |
| **Useful links** | [Zendesk Chat API method](https://developer.zendesk.com/api-reference/live-chat/chat-api/chats/ "Opens in new tab: Zendesk Chat API method") |

chats table foreign keys

| Join chats with | on |
| --- | --- |
| [agents](#agents) | ``` chats.agent_ids = agents.id ```  ``` chats.department_id = agents.departments ```  ``` chats.history.prev_department_id = agents.departments ``` |
| [departments](#departments) | ``` chats.department_id = departments.id ```  ``` chats.history.prev_department_id = departments.id ``` |
| [shortcuts](#shortcuts) | ``` chats.department_id = shortcuts.departments ```  ``` chats.history.prev_department_id = shortcuts.departments ``` |
| [goals](#goals) | ``` chats.conversions.goal_id = goals.id ```  ``` chats.history.conversion.goal_id = goals.id ``` |
| [account](#account) | ``` chats.conversions.goal_id = account.plan.goals ```  ``` chats.history.conversion.goal_id = account.plan.goals ``` |

chats table schema

|  |
| --- |
| **agent\_ids**  ARRAY |
| **agent\_names**  ARRAY |
| **comment**  STRING |
| **conversions**  ARRAY This is a nested data structure:   - attribution: OBJECT, which is also a nested data structure.   - agent\_id: INTEGER   - agent\_name: STRING   - chat\_timestamp: DATE-TIME   - department\_id: INTEGER   - department\_name: STRING - goal\_id: INTEGER - goal\_name: STRING - id: STRING - timestamp: DATE-TIME |
| **count**  OBJECT This is a nested data structure:   - agent: INTEGER - total: INTEGER - visitor: INTEGER |
| **department\_id**  INTEGER |
| **department\_name**  STRING |
| **duration**  INTEGER |
| **end\_timestamp**  DATE-TIME |
| **history**  ARRAY This is a nested data structure:   - channel: STRING - conversion: OBJECT, which is also a nested data structure.   - attribution: OBJECT, which is also a nested data structure.     - agent\_id: INTEGER     - agent\_name: STRING     - chat\_timestamp: DATE-TIME     - department\_id: INTEGER     - department\_name: STRING   - goal\_id: INTEGER   - goal\_name: STRING   - id: STRING   - timestamp: DATE-TIME - department\_id: INTEGER, STRING - department\_name: STRING - msg: STRING - msg\_id: STRING, INTEGER - name: STRING - new\_rating: STRING - new\_tags: ARRAY - nick: STRING - options: STRING - prev\_department\_id: INTEGER, STRING - rating: STRING - skills\_name: ARRAY - tags: ARRAY - timestamp: DATE-TIME - type: STRING |
| **id**  STRING |
| **message**  STRING |
| **missed**  BOOLEAN |
| **rating**  STRING |
| **referrer\_search\_engine**  STRING |
| **referrer\_search\_terms**  STRING |
| **response\_time**  OBJECT This is a nested data structure:   - avg: NUMBER, INTEGER - first: INTEGER - max: INTEGER |
| **session**  OBJECT |
| **started\_by**  STRING |
| **tags**  ARRAY |
| **timestamp**  DATE-TIME |
| **triggered**  BOOLEAN |
| **triggered\_response**  BOOLEAN |
| **type**  STRING |
| **unread**  BOOLEAN, INTEGER |
| **visitor**  OBJECT This is a nested data structure:   - email: STRING - id: STRING - name: STRING - notes: STRING - phone: STRING |
| **webpath**  ARRAY |
| **zendesk\_ticket\_id**  INTEGER |

### departments

The `departments` table contains info about departments within your Zendesk Chat account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Zendesk Chat API method](https://developer.zendesk.com/api-reference/live-chat/chat-api/departments/ "Opens in new tab: Zendesk Chat API method") |

departments table foreign keys

| Join departments with | on |
| --- | --- |
| [shortcuts](#shortcuts) | ``` departments.id = shortcuts.departments ``` |
| [chats](#chats) | ``` departments.id = chats.department_id ```  ``` departments.id = chats.history.prev_department_id ``` |
| [agents](#agents) | ``` departments.id = agents.departments ``` |

departments table schema

|  |
| --- |
| **description**  STRING |
| **enabled**  BOOLEAN |
| **id**  INTEGER |
| **members**  ARRAY |
| **name**  STRING |
| **settings**  OBJECT |

### goals

The `goals` table contains info about URL-based goals set within your Zendesk Chat account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Useful links** | [Zendesk Chat API method](https://developer.zendesk.com/api-reference/live-chat/chat-api/goals/ "Opens in new tab: Zendesk Chat API method") |

goals table foreign keys

| Join goals with | on |
| --- | --- |
| [chats](#chats) | ``` goals.id = chats.conversions.goal_id ```  ``` goals.id = chats.history.conversion.goal_id ``` |
| [account](#account) | ``` goals.id = account.plan.goals ``` |

goals table schema

|  |
| --- |
| **attribution\_model**  STRING |
| **attribution\_period**  INTEGER |
| **description**  STRING |
| **enabled**  BOOLEAN |
| **id**  INTEGER |
| **name**  STRING |
| **settings**  OBJECT This is a nested data structure:   - conditions: ARRAY, which is also a nested data structure.   - operator: STRING   - type: STRING   - value: STRING |

### shortcuts

The `shortcuts` table contains info about shortcuts within your Zendesk Chat account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | name |
| **Useful links** | [Zendesk Chat API method](https://developer.zendesk.com/api-reference/live-chat/chat-api/shortcuts/ "Opens in new tab: Zendesk Chat API method") |

shortcuts table foreign keys

| Join shortcuts with | on |
| --- | --- |
| [departments](#departments) | ``` shortcuts.departments = departments.id ``` |
| [chats](#chats) | ``` shortcuts.departments = chats.department_id ```  ``` shortcuts.departments = chats.history.prev_department_id ``` |
| [agents](#agents) | ``` shortcuts.departments = agents.departments ``` |

shortcuts table schema

|  |
| --- |
| **agents**  ARRAY |
| **departments**  ARRAY |
| **id**  STRING |
| **message**  STRING |
| **name**  STRING |
| **options**  STRING |
| **scope**  STRING |
| **tags**  ARRAY |

### triggers

The `triggers` table contains info about triggers within your Zendesk Chat account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Zendesk Chat API method](https://developer.zendesk.com/api-reference/live-chat/chat-api/triggers/#list-triggers "Opens in new tab: Zendesk Chat API method") |

triggers table schema

|  |
| --- |
| **definition**  OBJECT This is a nested data structure:   - actions: STRING - condition: STRING - event: STRING - version: INTEGER |
| **description**  STRING |
| **enabled**  BOOLEAN |
| **id**  INTEGER |
| **name**  STRING |
