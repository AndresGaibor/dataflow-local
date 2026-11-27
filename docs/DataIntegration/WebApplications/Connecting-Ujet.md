---
title: "Ujet"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Ujet.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Ujet

Ujet is a cloud-based contact center platform that provides mobile and AI-powered solutions for managing customer service operations.

Ujet integration replicates data using the [UJET API](https://support.ujet.co/hc/en-us/articles/115006908127-UJET-Data-API#h_7d95eafc-6c02-446b-bcc6-b733f4e1143e).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

You need administrator permissions in your Ujet account.

To retrieve your company key and company secret:

1. Log into your [Ujet](https://turo.ujet.co/sign-in) account.
2. Navigate to Settings > Developer Settings.
3. In the Agent Platform section, click UJET.
4. Click Save Changes.
5. Copy and paste your company key and company secret into a secured file.

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
| Company Key | Company key. |
| Company Secret | Company secret. |
| Domain | Enter your Ujet domain. You can find this value in your Ujet welcome email. |
| Subdomain | You can find your subdomain in your Ujet URL. If the URL is https://myujet.ujet.com, the subdomain is myujet. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### agent\_activity\_logs

The `agent_activity_logs` table contains info about agent activity logs.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | started\_at |

agent\_activity\_logs table foreign keys

| Join agent\_activity\_logs with | on |
| --- | --- |
| [agents](#agents) | ``` agent_activity_logs.agent_id = agents.id ``` |
| [calls](#calls) | ``` agent_activity_logs.agent_id = calls.agent_info.id ```  ``` agent_activity_logs.agent_id = calls.transfers.from_agent.id ```  ``` agent_activity_logs.agent_id = calls.transfers.to_agent.id ```  ``` agent_activity_logs.call_id = calls.id ```  ``` agent_activity_logs.call_id = calls.participants.call_id ``` |
| [chats](#chats) | ``` agent_activity_logs.agent_id = chats.transfers.from_agent.id ```  ``` agent_activity_logs.agent_id = chats.transfers.to_agent.id ```  ``` agent_activity_logs.chat_id = chats.id ```  ``` agent_activity_logs.chat_id = chats.participants.chat_id ``` |
| [menus](#menus) | ``` agent_activity_logs.agent_id = menus.agent_assignments.assignee.id ```  ``` agent_activity_logs.agent_id = menus.team_assignments.team.assignees.id ``` |

agent\_activity\_logs table schema

|  |
| --- |
| **activity**  STRING |
| **agent\_id**  INTEGER |
| **call\_id**  INTEGER |
| **chat\_id**  INTEGER |
| **duration**  INTEGER |
| **ended\_at**  DATE-TIME |
| **id**  INTEGER |
| **started\_at**  DATE-TIME |
| **status**  OBJECT This is a nested data structure:   - color: STRING - id: INTEGER - name: STRING - wfm\_id: INTEGER |
| **whodunnit**  OBJECT This is a nested data structure:   - agent\_number: STRING - avatar\_url: STRING - first\_name: STRING - id: INTEGER - last\_name: STRING - name: STRING |

### agents

The `agents` table contains info about agents.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | status\_updated\_at |

agents table foreign keys

| Join agents with | on |
| --- | --- |
| [agent\_activity\_logs](#agent-activity-logs) | ``` agents.id = agent_activity_logs.agent_id ``` |
| [calls](#calls) | ``` agents.id = calls.agent_info.id ```  ``` agents.id = calls.transfers.from_agent.id ```  ``` agents.id = calls.transfers.to_agent.id ``` |
| [chats](#chats) | ``` agents.id = chats.transfers.from_agent.id ```  ``` agents.id = chats.transfers.to_agent.id ``` |
| [menus](#menus) | ``` agents.id = menus.agent_assignments.assignee.id ```  ``` agents.id = menus.team_assignments.team.assignees.id ```  ``` agents.teams.id = menus.team_assignments.team.id ``` |
| [teams](#teams) | ``` agents.teams.id = teams.id ``` |

agents table schema

|  |
| --- |
| **agent\_number**  STRING |
| **avatar\_url**  STRING |
| **call\_count**  INTEGER |
| **channels**  ARRAY This is a nested data structure:   - channel\_type: STRING - menu: OBJECT, which is also a nested data structure.   - deleted: BOOLEAN   - hidden: BOOLEAN   - id: INTEGER   - menu\_type: STRING   - name: STRING   - output\_msg: STRING   - parent\_id: INTEGER   - position: INTEGER |
| **chat\_count**  INTEGER |
| **created\_at**  DATE-TIME |
| **crm\_authenticated**  BOOLEAN |
| **email**  STRING |
| **first\_name**  STRING |
| **id**  INTEGER |
| **last\_login\_time**  DATE-TIME |
| **last\_name**  STRING |
| **location**  STRING |
| **middle\_name**  STRING |
| **online**  BOOLEAN |
| **roles**  ARRAY This is a nested data structure. |
| **status**  OBJECT This is a nested data structure:   - color: STRING - id: INTEGER - name: STRING - wfm\_id: INTEGER |
| **status\_updated\_at**  DATE-TIME |
| **teams**  ARRAY This is a nested data structure:   - agents\_count: INTEGER - deleted: BOOLEAN - id: INTEGER - name: STRING - parent\_id: INTEGER - position: INTEGER |
| **wrap\_up**  BOOLEAN |

### calls

The `calls` table contains info about calls.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |

calls table foreign keys

| Join calls with | on |
| --- | --- |
| [agents](#agents) | ``` calls.agent_info.id = agents.id ```  ``` calls.transfers.from_agent.id = agents.id ```  ``` calls.transfers.to_agent.id = agents.id ``` |
| [agent\_activity\_logs](#agent-activity-logs) | ``` calls.agent_info.id = agent_activity_logs.agent_id ```  ``` calls.transfers.from_agent.id = agent_activity_logs.agent_id ```  ``` calls.transfers.to_agent.id = agent_activity_logs.agent_id ```  ``` calls.id = agent_activity_logs.call_id ```  ``` calls.participants.call_id = agent_activity_logs.call_id ``` |
| [chats](#chats) | ``` calls.agent_info.id = chats.transfers.from_agent.id ```  ``` calls.transfers.from_agent.id = chats.transfers.from_agent.id ```  ``` calls.transfers.to_agent.id = chats.transfers.from_agent.id ```  ``` calls.agent_info.id = chats.transfers.to_agent.id ```  ``` calls.transfers.from_agent.id = chats.transfers.to_agent.id ```  ``` calls.transfers.to_agent.id = chats.transfers.to_agent.id ``` |
| [menus](#menus) | ``` calls.agent_info.id = menus.agent_assignments.assignee.id ```  ``` calls.transfers.from_agent.id = menus.agent_assignments.assignee.id ```  ``` calls.transfers.to_agent.id = menus.agent_assignments.assignee.id ```  ``` calls.agent_info.id = menus.team_assignments.team.assignees.id ```  ``` calls.transfers.from_agent.id = menus.team_assignments.team.assignees.id ```  ``` calls.transfers.to_agent.id = menus.team_assignments.team.assignees.id ``` |

calls table schema

|  |
| --- |
| **agent\_info**  OBJECT This is a nested data structure:   - agent\_number: INTEGER - avatar\_url: STRING - first\_name: STRING - id: INTEGER - last\_name: STRING - name: STRING |
| **answer\_type**  STRING |
| **assigned\_at**  DATE-TIME |
| **call\_duration**  INTEGER |
| **call\_type**  STRING |
| **connected\_at**  DATE-TIME |
| **created\_at**  DATE-TIME |
| **deflection**  STRING |
| **deflection\_details**  ARRAY This is a nested data structure:   - call\_id: INTEGER - deflection: STRING - from\_menu\_path: OBJECT, which is also a nested data structure.   - items\_count: INTEGER   - materialized\_path: STRING   - name: STRING - id: INTEGER - transfer\_id: INTEGER |
| **disconnected\_by**  STRING |
| **end\_user**  OBJECT This is a nested data structure:   - id: INTEGER - identifier: STRING - out\_contact\_id: STRING |
| **ends\_at**  DATE-TIME |
| **fail\_details**  STRING |
| **fail\_reason**  STRING |
| **has\_feedback**  BOOLEAN |
| **hold\_duration**  INTEGER |
| **id**  INTEGER |
| **lang**  STRING |
| **menu\_path**  OBJECT This is a nested data structure:   - items\_count: INTEGER - materialized\_path: STRING - name: STRING |
| **offer\_events**  ARRAY This is a nested data structure:   - casting\_time: DATE-TIME - group: STRING |
| **offer\_type**  STRING |
| **out\_ticket\_id**  STRING |
| **out\_ticket\_url**  STRING |
| **outbound\_number**  STRING |
| **participants**  ARRAY This is a nested data structure:   - call\_duration: INTEGER - call\_id: INTEGER - connected\_at: DATE-TIME - end\_user\_id: INTEGER - ended\_at: DATE-TIME - fail\_reason: STRING - hold\_duration: INTEGER - id: INTEGER - status: STRING - type: STRING - user\_id: INTEGER |
| **photos**  ARRAY This is a nested data structure:   - id: INTEGER - photo\_type: STRING - url: STRING |
| **queued\_at**  DATE-TIME |
| **rating**  STRING |
| **recording\_url**  STRING |
| **scheduled\_at**  DATE-TIME |
| **selected\_menu**  OBJECT This is a nested data structure:   - deleted: BOOLEAN - hidden: BOOLEAN - id: INTEGER - menu\_type: STRING - name: STRING - output\_msg: STRING - parent\_id: INTEGER - position: INTEGER |
| **status**  STRING |
| **support\_number**  STRING |
| **transfers**  ARRAY This is a nested data structure:   - answer\_type\_path: STRING - assigned\_at: DATE-TIME - call\_duration: INTEGER - connected\_at: DATE-TIME - created\_at: DATE-TIME - deflection: STRING - fail\_reason: STRING - from\_agent: OBJECT, which is also a nested data structure.   - agent\_number: INTEGER   - avatar\_url: STRING   - first\_name: STRING   - id: INTEGER   - last\_name: STRING   - name: STRING - from\_menu\_path: OBJECT, which is also a nested data structure.   - items\_count: INTEGER   - materialized\_path: STRING   - name: STRING - from\_queue\_priority\_level: INTEGER - id: INTEGER - status: STRING - to\_agent: OBJECT, which is also a nested data structure.   - agent\_number: INTEGER   - avatar\_url: STRING   - first\_name: STRING   - id: INTEGER   - last\_name: STRING   - name: STRING - to\_menu\_path: STRING - to\_queue\_priority\_level: STRING - updated\_at: DATE-TIME - wait\_duration: INTEGER |
| **updated\_at**  DATE-TIME |
| **verified**  BOOLEAN |
| **videos**  ARRAY This is a nested data structure:   - id: INTEGER - url: STRING |
| **voicemail\_reason**  STRING |
| **voip\_provider**  STRING |
| **wait\_duration**  INTEGER |

### chats

The `chats` table contains info about chats.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |

chats table foreign keys

| Join chats with | on |
| --- | --- |
| [agents](#agents) | ``` chats.transfers.from_agent.id = agents.id ```  ``` chats.transfers.to_agent.id = agents.id ``` |
| [agent\_activity\_logs](#agent-activity-logs) | ``` chats.transfers.from_agent.id = agent_activity_logs.agent_id ```  ``` chats.transfers.to_agent.id = agent_activity_logs.agent_id ```  ``` chats.id = agent_activity_logs.chat_id ```  ``` chats.participants.chat_id = agent_activity_logs.chat_id ``` |
| [calls](#calls) | ``` chats.transfers.from_agent.id = calls.agent_info.id ```  ``` chats.transfers.to_agent.id = calls.agent_info.id ```  ``` chats.transfers.from_agent.id = calls.transfers.from_agent.id ```  ``` chats.transfers.to_agent.id = calls.transfers.from_agent.id ```  ``` chats.transfers.from_agent.id = calls.transfers.to_agent.id ```  ``` chats.transfers.to_agent.id = calls.transfers.to_agent.id ``` |
| [menus](#menus) | ``` chats.transfers.from_agent.id = menus.agent_assignments.assignee.id ```  ``` chats.transfers.to_agent.id = menus.agent_assignments.assignee.id ```  ``` chats.transfers.from_agent.id = menus.team_assignments.team.assignees.id ```  ``` chats.transfers.to_agent.id = menus.team_assignments.team.assignees.id ``` |

chats table schema

|  |
| --- |
| **agent\_info**  STRING |
| **assigned\_at**  DATE-TIME |
| **average\_response\_time**  INTEGER |
| **chat\_duration**  INTEGER |
| **chat\_type**  STRING |
| **created\_at**  DATE-TIME |
| **end\_user**  OBJECT This is a nested data structure:   - id: INTEGER - identifier: STRING - out\_contact\_id: STRING |
| **ends\_at**  DATE-TIME |
| **fail\_reason**  STRING |
| **first\_msg\_sent\_at**  DATE-TIME |
| **has\_feedback**  BOOLEAN |
| **id**  INTEGER |
| **lang**  STRING |
| **last\_msg\_sent\_at**  DATE-TIME |
| **longest\_response\_time**  INTEGER |
| **menu\_path**  OBJECT This is a nested data structure:   - items\_count: INTEGER - materialized\_path: STRING - name: STRING |
| **message\_count**  INTEGER |
| **offer\_events**  ARRAY This is a nested data structure. |
| **offer\_type**  STRING |
| **out\_ticket\_id**  STRING |
| **out\_ticket\_url**  STRING |
| **participants**  ARRAY This is a nested data structure:   - chat\_duration: INTEGER - chat\_id: INTEGER - connected\_at: DATE-TIME - end\_user\_id: INTEGER - fail\_reason: STRING - finished\_at: DATE-TIME - id: INTEGER - status: STRING - type: STRING - user\_id: STRING |
| **photos**  ARRAY This is a nested data structure:   - id: INTEGER - photo\_type: STRING - url: STRING |
| **rating**  STRING |
| **selected\_menu**  OBJECT This is a nested data structure:   - deleted: BOOLEAN - hidden: BOOLEAN - id: INTEGER - menu\_type: STRING - name: STRING - output\_msg: STRING - parent\_id: INTEGER - position: INTEGER |
| **status**  STRING |
| **transcript**  BOOLEAN |
| **transfers**  ARRAY This is a nested data structure:   - answer\_type\_path: STRING - assigned\_at: DATE-TIME - call\_duration: INTEGER - connected\_at: DATE-TIME - created\_at: DATE-TIME - deflection: STRING - fail\_reason: STRING - from\_agent: OBJECT, which is also a nested data structure.   - agent\_number: INTEGER   - avatar\_url: STRING   - first\_name: STRING   - id: INTEGER   - last\_name: STRING   - name: STRING - from\_menu\_path: OBJECT, which is also a nested data structure.   - items\_count: INTEGER   - materialized\_path: STRING   - name: STRING - from\_queue\_priority\_level: INTEGER - id: INTEGER - status: STRING - to\_agent: OBJECT, which is also a nested data structure.   - agent\_number: INTEGER   - avatar\_url: STRING   - first\_name: STRING   - id: INTEGER   - last\_name: STRING   - name: STRING - to\_menu\_path: STRING - to\_queue\_priority\_level: STRING - updated\_at: DATE-TIME - wait\_duration: INTEGER |
| **updated\_at**  DATE-TIME |
| **verified**  BOOLEAN |
| **videos**  ARRAY This is a nested data structure:   - id: INTEGER - url: STRING |
| **wait\_duration**  INTEGER |

### menu\_tree

The `menu_tree` table contains info about menu trees.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |

menu\_tree table schema

|  |
| --- |
| **agents\_count**  INTEGER |
| **deleted**  BOOLEAN |
| **id**  INTEGER |
| **name**  STRING |
| **parent\_id**  INTEGER |
| **position**  INTEGER |

### menus

The `menus` table contains info about menus.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |

menus table foreign keys

| Join menus with | on |
| --- | --- |
| [agents](#agents) | ``` menus.agent_assignments.assignee.id = agents.id ```  ``` menus.team_assignments.team.assignees.id = agents.id ```  ``` menus.team_assignments.team.id = agents.teams.id ``` |
| [agent\_activity\_logs](#agent-activity-logs) | ``` menus.agent_assignments.assignee.id = agent_activity_logs.agent_id ```  ``` menus.team_assignments.team.assignees.id = agent_activity_logs.agent_id ``` |
| [calls](#calls) | ``` menus.agent_assignments.assignee.id = calls.agent_info.id ```  ``` menus.team_assignments.team.assignees.id = calls.agent_info.id ```  ``` menus.agent_assignments.assignee.id = calls.transfers.from_agent.id ```  ``` menus.team_assignments.team.assignees.id = calls.transfers.from_agent.id ```  ``` menus.agent_assignments.assignee.id = calls.transfers.to_agent.id ```  ``` menus.team_assignments.team.assignees.id = calls.transfers.to_agent.id ``` |
| [chats](#chats) | ``` menus.agent_assignments.assignee.id = chats.transfers.from_agent.id ```  ``` menus.team_assignments.team.assignees.id = chats.transfers.from_agent.id ```  ``` menus.agent_assignments.assignee.id = chats.transfers.to_agent.id ```  ``` menus.team_assignments.team.assignees.id = chats.transfers.to_agent.id ``` |
| [teams](#teams) | ``` menus.team_assignments.team.id = teams.id ``` |

menus table schema

|  |
| --- |
| **agent\_assignments**  ARRAY This is a nested data structure:   - assignee: OBJECT, which is also a nested data structure.   - agent\_number: STRING   - avatar\_url: STRING   - first\_name: STRING   - id: INTEGER   - last\_name: STRING   - name: STRING - channel\_type: STRING - group\_type: STRING - lang: STRING - queue\_level: STRING |
| **deleted**  BOOLEAN |
| **hidden**  BOOLEAN |
| **id**  INTEGER |
| **menu\_type**  STRING |
| **name**  STRING |
| **output\_msg**  STRING |
| **parent\_id**  INTEGER |
| **position**  INTEGER |
| **team\_assignments**  ARRAY This is a nested data structure:   - channel\_type: STRING - group\_type: STRING - lang: STRING - queue\_level: STRING - team: OBJECT, which is also a nested data structure.   - agents\_count: INTEGER   - assignees: ARRAY, which is also a nested data structure.     - agent\_number: STRING     - avatar\_url: STRING     - first\_name: STRING     - id: INTEGER     - last\_name: STRING     - name: STRING   - deleted: BOOLEAN   - id: INTEGER   - name: STRING   - parent\_id: INTEGER   - position: INTEGER |

### team\_tree

The `team_tree` table contains info about team trees.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |

team\_tree table schema

|  |
| --- |
| **agents\_count**  INTEGER |
| **deleted**  BOOLEAN |
| **id**  INTEGER |
| **name**  STRING |
| **parent\_id**  INTEGER |
| **position**  INTEGER |

### teams

The `teams` table contains info about teams.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |

teams table foreign keys

| Join teams with | on |
| --- | --- |
| [agents](#agents) | ``` teams.id = agents.teams.id ``` |
| [menus](#menus) | ``` teams.id = menus.team_assignments.team.id ``` |

teams table schema

|  |
| --- |
| **agents\_count**  INTEGER |
| **assignees**  ARRAY This is a nested data structure:   - agent\_number: STRING - avatar\_url: STRING - first\_name: STRING - id: INTEGER - last\_name: STRING - name: STRING |
| **deleted**  BOOLEAN |
| **id**  INTEGER |
| **name**  STRING |
| **parent\_id**  INTEGER |
| **position**  INTEGER |

### user\_statuses

The `user_statuses` table contains info about user statuses.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |

user\_statuses table schema

|  |
| --- |
| **color**  STRING |
| **id**  INTEGER |
| **name**  STRING |
| **wfm\_id**  INTEGER |
