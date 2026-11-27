---
title: "Freshdesk"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Freshdesk.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Freshdesk

Freshdesk is an online cloud-based customer support software providing help desk support.

Freshdesk integration replicates data using the [Freshdesk REST API](https://developer.freshdesk.com/api/).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

You need administrator permissions in Freshdesk.

To find your API key:

1. Log into your [Freshdesk](https://support.freshdesk.com/support/login) account.
2. Click your profile icon in the upper-right corner.
3. Go to Profile settings > View API Key.
4. Copy and paste your API key into a secured file.

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
| Subdomain | You can find your subdomain in the URL of your Freshdesk account. If the URL is your-org-name.freshdesk.com, the subdomain is your-org-name. |
| API Key | API key. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### agents

The `agents` table contains info about the agents in your Freshdesk account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Freshdesk documentation](https://developers.freshdesk.com/api/#agents)  [Freshdesk API method](https://developers.freshdesk.com/api/#list_all_agents "Opens in new tab: Freshdesk API method") |

agents table foreign keys

| Join agents with | on |
| --- | --- |
| [groups](#groups) | ``` agents.id = groups.agent_ids ```  ``` agents.group_ids.type = groups.id ``` |
| [satisfaction\_ratings](#satisfaction-ratings) | ``` agents.id = satisfaction_ratings.agent_id ```  ``` agents.group_ids.type = satisfaction_ratings.group_id ``` |
| [tickets](#tickets) | ``` agents.id = tickets.responder_id ```  ``` agents.group_ids.type = tickets.group_id ``` |
| [time\_entries](#time-entries) | ``` agents.id = time_entries.agent_id ``` |
| [roles](#roles) | ``` agents.role_ids.type = roles.id ``` |

agents table schema

|  |
| --- |
| **available**  BOOLEAN |
| **available\_since**  DATE-TIME |
| **contact**  OBJECT This is a nested data structure:   - active: BOOLEAN - created\_at: DATE-TIME - email: STRING - job\_title: STRING - language: STRING - last\_login\_at: DATE-TIME - mobile: STRING - name: STRING - phone: STRING - time\_zone: STRING - updated\_at: DATE-TIME |
| **created\_at**  DATE-TIME |
| **group\_ids**  ARRAY This is a nested data structure. |
| **id**  INTEGER |
| **occasional**  BOOLEAN |
| **role\_ids**  ARRAY This is a nested data structure. |
| **signature**  STRING |
| **ticket\_scope**  INTEGER |
| **updated\_at**  DATE-TIME |

### companies

The `companies` table contains info about the companies your various customers and contacts belong to.

#### Custom Fields

If applicable, Stitch will replicate custom fields related to `companies` in Freshdesk.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Freshdesk documentation](https://developers.freshdesk.com/api/#companies)  [Freshdesk API method](https://developers.freshdesk.com/api/#list_all_companies "Opens in new tab: Freshdesk API method") |

companies table foreign keys

| Join companies with | on |
| --- | --- |
| [tickets](#tickets) | ``` companies.id = tickets.company_id ``` |

companies table schema

|  |
| --- |
| **created\_at**  DATE-TIME |
| **custom\_fields**  ARRAY This is a nested data structure:   - name: STRING - value: STRING |
| **description**  STRING |
| **domains**  ARRAY This is a nested data structure. |
| **id**  INTEGER |
| **name**  STRING |
| **note**  STRING |
| **updated\_at**  DATE-TIME |

### conversations

The `conversations` table contains info about replies and public/private notes added to the tickets in your Freshdesk account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Freshdesk documentation](https://developers.freshdesk.com/api/#conversations)  [Freshdesk API method](https://developers.freshdesk.com/api/#list_all_ticket_notes "Opens in new tab: Freshdesk API method") |

conversations table foreign keys

| Join conversations with | on |
| --- | --- |
| [tickets](#tickets) | ``` conversations.ticket_id = tickets.id ``` |
| [satisfaction\_ratings](#satisfaction-ratings) | ``` conversations.ticket_id = satisfaction_ratings.ticket_id ``` |

conversations table schema

|  |
| --- |
| **bcc\_emails**  ARRAY This is a nested data structure. |
| **body\_text**  STRING |
| **cc\_emails**  ARRAY This is a nested data structure. |
| **created\_at**  DATE-TIME |
| **from\_email**  STRING |
| **id**  INTEGER |
| **incoming**  BOOLEAN |
| **private**  BOOLEAN |
| **source**  INTEGER |
| **support\_email**  STRING |
| **ticket\_id**  INTEGER |
| **to\_emails**  ARRAY This is a nested data structure. |
| **updated\_at**  DATE-TIME |
| **user\_id**  INTEGER |

### groups

The `groups` table contains info about the groups your agents belong to.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Freshdesk documentation](https://developers.freshdesk.com/api/#groups)  [Freshdesk API method](https://developers.freshdesk.com/api/#list_all_groups "Opens in new tab: Freshdesk API method") |

groups table foreign keys

| Join groups with | on |
| --- | --- |
| [agents](#agents) | ``` groups.agent_ids = agents.id ```  ``` groups.id = agents.group_ids.type ``` |
| [satisfaction\_ratings](#satisfaction-ratings) | ``` groups.agent_ids = satisfaction_ratings.agent_id ```  ``` groups.id = satisfaction_ratings.group_id ``` |
| [tickets](#tickets) | ``` groups.agent_ids = tickets.responder_id ```  ``` groups.id = tickets.group_id ``` |
| [time\_entries](#time-entries) | ``` groups.agent_ids = time_entries.agent_id ``` |

groups table schema

|  |
| --- |
| **agent\_ids**  ARRAY This is a nested data structure. |
| **auto\_ticket\_assign**  INTEGER, BOOLEAN |
| **business\_hour\_id**  INTEGER |
| **created\_at**  DATE-TIME |
| **description**  STRING |
| **escalate\_to**  INTEGER |
| **id**  INTEGER |
| **name**  STRING |
| **unassigned\_for**  STRING |
| **updated\_at**  DATE-TIME |

### roles

The `roles` table contains info about the various roles that can be assigned to team members in your Freshdesk account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Freshdesk documentation](https://developers.freshdesk.com/api/#roles)  [Freshdesk API method](https://developers.freshdesk.com/api/#list_all_roles "Opens in new tab: Freshdesk API method") |

roles table foreign keys

| Join roles with | on |
| --- | --- |
| [agents](#agents) | ``` roles.id = agents.role_ids.type ``` |

roles table schema

|  |
| --- |
| **created\_at**  DATE-TIME |
| **default**  BOOLEAN |
| **description**  STRING |
| **id**  INTEGER |
| **name**  STRING |
| **updated\_at**  DATE-TIME |

### satisfaction\_ratings

The `satisfaction_ratings` table contains info about customer satisfaction survey responses, or satisfaction ratings.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Freshdesk documentation](https://developers.freshdesk.com/api/#satisfaction-ratings)  [Freshdesk API method](https://developers.freshdesk.com/api/#view_all_satisfaction_ratings "Opens in new tab: Freshdesk API method") |

satisfaction\_ratings table foreign keys

| Join satisfaction\_ratings with | on |
| --- | --- |
| [agents](#agents) | ``` satisfaction_ratings.agent_id = agents.id ```  ``` satisfaction_ratings.group_id = agents.group_ids.type ``` |
| [groups](#groups) | ``` satisfaction_ratings.agent_id = groups.agent_ids ```  ``` satisfaction_ratings.group_id = groups.id ``` |
| [tickets](#tickets) | ``` satisfaction_ratings.agent_id = tickets.responder_id ```  ``` satisfaction_ratings.group_id = tickets.group_id ```  ``` satisfaction_ratings.ticket_id = tickets.id ``` |
| [time\_entries](#time-entries) | ``` satisfaction_ratings.agent_id = time_entries.agent_id ``` |
| [conversations](#conversations) | ``` satisfaction_ratings.ticket_id = conversations.ticket_id ``` |

satisfaction\_ratings table schema

|  |
| --- |
| **agent\_id**  INTEGER |
| **created\_at**  DATE-TIME |
| **feedback**  STRING |
| **group\_id**  INTEGER |
| **id**  INTEGER |
| **ratings**  ARRAY This is a nested data structure:   - question: STRING - value: INTEGER |
| **survey\_id**  INTEGER |
| **ticket\_id**  INTEGER |
| **updated\_at**  DATE-TIME |
| **user\_id**  INTEGER |

### tickets

The `tickets` table contains info about the tickets in your Freshdesk account.

#### Custom Fields

If applicable, Stitch will replicate custom fields related to `tickets` in Freshdesk.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Freshdesk API method](https://developers.freshdesk.com/api/#tickets "Opens in new tab: Freshdesk API method") |

tickets table foreign keys

| Join tickets with | on |
| --- | --- |
| [agents](#agents) | ``` tickets.responder_id = agents.id ```  ``` tickets.group_id = agents.group_ids.type ``` |
| [groups](#groups) | ``` tickets.responder_id = groups.agent_ids ```  ``` tickets.group_id = groups.id ``` |
| [satisfaction\_ratings](#satisfaction-ratings) | ``` tickets.responder_id = satisfaction_ratings.agent_id ```  ``` tickets.group_id = satisfaction_ratings.group_id ```  ``` tickets.id = satisfaction_ratings.ticket_id ``` |
| [time\_entries](#time-entries) | ``` tickets.responder_id = time_entries.agent_id ``` |
| [companies](#companies) | ``` tickets.company_id = companies.id ``` |
| [conversations](#conversations) | ``` tickets.id = conversations.ticket_id ``` |

tickets table schema

|  |
| --- |
| **cc\_emails**  ARRAY This is a nested data structure. |
| **company**  OBJECT This is a nested data structure:   - id: INTEGER - name: STRING |
| **company\_id**  INTEGER |
| **created\_at**  DATE-TIME |
| **custom\_fields**  ARRAY This is a nested data structure:   - name: STRING - value: STRING |
| **deleted**  BOOLEAN |
| **description**  STRING |
| **description\_text**  STRING |
| **due\_by**  DATE-TIME |
| **email**  STRING |
| **email\_config\_id**  INTEGER |
| **facebook\_id**  STRING |
| **fr\_due\_by**  DATE-TIME |
| **fr\_escalated**  BOOLEAN |
| **fwd\_emails**  ARRAY This is a nested data structure. |
| **group\_id**  INTEGER |
| **id**  INTEGER |
| **is\_escalated**  BOOLEAN |
| **name**  STRING |
| **phone**  STRING |
| **priority**  NUMBER |
| **product\_id**  INTEGER |
| **reply\_cc\_emails**  ARRAY This is a nested data structure. |
| **requester**  OBJECT This is a nested data structure:   - email: STRING - id: INTEGER - mobile: STRING - name: STRING - phone: STRING |
| **requester\_id**  INTEGER |
| **responder\_id**  INTEGER |
| **source**  NUMBER |
| **spam**  BOOLEAN |
| **stats**  OBJECT This is a nested data structure:   - closed\_at: DATE-TIME - first\_responded\_at: DATE-TIME - resolved\_at: DATE-TIME |
| **status**  NUMBER |
| **subject**  STRING |
| **tags**  ARRAY This is a nested data structure. |
| **to\_emails**  ARRAY This is a nested data structure. |
| **twitter\_id**  STRING |
| **type**  STRING |
| **updated\_at**  DATE-TIME |

### time\_entries

The `time_entries` table contains info about the time entries entered by agents working on tickets.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Freshdesk API method](https://developers.freshdesk.com/api/#time-entries "Opens in new tab: Freshdesk API method") |

time\_entries table foreign keys

| Join time\_entries with | on |
| --- | --- |
| [agents](#agents) | ``` time_entries.agent_id = agents.id ``` |
| [groups](#groups) | ``` time_entries.agent_id = groups.agent_ids ``` |
| [satisfaction\_ratings](#satisfaction-ratings) | ``` time_entries.agent_id = satisfaction_ratings.agent_id ``` |
| [tickets](#tickets) | ``` time_entries.agent_id = tickets.responder_id ``` |

time\_entries table schema

|  |
| --- |
| **agent\_id**  INTEGER |
| **billable**  BOOLEAN |
| **created\_at**  DATE-TIME |
| **executed\_at**  DATE-TIME |
| **id**  INTEGER |
| **note**  STRING |
| **start\_time**  DATE-TIME |
| **ticket\_id**  INTEGER |
| **time\_spent**  STRING |
| **timer\_running**  BOOLEAN |
| **updated\_at**  DATE-TIME |
