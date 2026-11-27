---
title: "Dixa"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Dixa.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Dixa

Dixa is a customer service platform that unifies customer data and communication channels.

For more information about the API, see the [Dixa API](https://docs.dixa.io/openapi).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To generate the API token:

1. Log into your Dixa account.
2. Go to the Settings page.
3. Scroll to the Manage section and click Integrations.
4. In the API Tokens tab, click Add API token.
5. Give the API token a name, like `Qlik Integration`, to make it easy to find in your list of tokens.
6. Choose Dixa API as the API version.
7. Click Save changes
8. Copy the token.

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
| API Token | API token. |
| Interval | Select the granularity of report time intervals from the drop-down list. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### activity\_logs

The `activity_logs` lists all information from activity logs for an organization in your Dixa account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | activityTimestamp |
| **Useful links** | [Dixa API method](https://docs.dixa.io/openapi/dixa-api/v1/tag/Conversations/#tag/Conversations/operation/getConversationsConversationidActivitylog "Opens in new tab: Dixa API method") |

activity\_logs table foreign keys

| Join activity\_logs with | on |
| --- | --- |
| [conversations](#conversations) | ``` activity_logs.conversationId = conversations.id ``` |
| [messages](#messages) | ``` activity_logs.attributes.messageId = messages.id ``` |

activity\_logs table schema

|  |
| --- |
| **\_type**  STRING |
| **activityTimestamp**  DATE-TIME |
| **activityType**  STRING |
| **attributes**  OBJECT This is a nested data structure:   - **type**: STRING - **agent**: OBJECT, which is also a nested data structure.   - **email**: STRING   - **id**: STRING   - **name**: STRING   - **phoneNumber**: STRING - **agentid**: STRING - **agentName**: STRING - **agentNames**: ARRAY - **avatalUrl**: STRING - **avatarUrl**: STRING - **claimedFromLabel**: STRING - **claimedFromType**: STRING - **conversationSubject**: STRING - **destinationId**: STRING - **destinationLabel**: STRING - **destinationType**: STRING - **fromEndpoint**: STRING - **message**: STRING - **messageId**: STRING - **note**: STRING - **queueLabel**: STRING - **reason**: STRING - **subject**: STRING - **tag**: STRING - **tagAdded**: STRING - **templateName**: STRING - **transferType**: STRING |
| **author**  OBJECT This is a nested data structure:   - **email**: STRING - **id**: STRING - **name**: STRING - **phoneNumber**: STRING |
| **conversationId**  INTEGER |
| **id**  STRING |

### conversations

The `conversations` table lists information about conversations in your Dixa account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Dixa API method](https://docs.dixa.io/openapi/dixa-api/v1/tag/Conversations/ "Opens in new tab: Dixa API method") |

conversations table foreign keys

| Join conversations with | on |
| --- | --- |
| [activity\_logs](#activity-logs) | ``` conversations.id = activity_logs.conversationId ``` |

conversations table schema

|  |
| --- |
| **anonymized\_at**  INTEGER |
| **assigned\_at**  INTEGER |
| **assignee\_email**  STRING |
| **assignee\_id**  STRING |
| **assignee\_name**  STRING |
| **assignee\_phone\_number**  STRING |
| **closed\_at**  INTEGER |
| **conversation\_wrapup\_notes**  ARRAY |
| **created\_at**  INTEGER |
| **custom\_fields**  ARRAY This is a nested data structure:   - **archived**: BOOLEAN - **attribute\_id**: STRING - **data\_type**: STRING - **identifier**: STRING - **value**: STRING |
| **direction**  STRING |
| **dixa\_email\_integration\_id**  STRING |
| **dixa\_email\_integration\_sender\_name**  STRING |
| **facebook\_page\_id**  STRING |
| **facebook\_page\_name**  STRING |
| **forwarding\_email**  STRING |
| **from\_provisioned\_phone\_number\_id**  STRING |
| **from\_provisioned\_phone\_number\_name**  STRING |
| **handling\_duration**  INTEGER |
| **id**  INTEGER |
| **initial\_channel**  STRING |
| **last\_message\_created\_at**  INTEGER |
| **originating\_country**  STRING |
| **queue\_id**  STRING |
| **queue\_name**  STRING |
| **queued\_at**  INTEGER |
| **rating\_message**  STRING |
| **rating\_score**  INTEGER |
| **ratings**  ARRAY This is a nested data structure:   - **rating\_cancelled\_timestamp**: STRING - **rating\_created\_timestamp**: INTEGER - **rating\_language**: STRING - **rating\_message**: STRING - **rating\_modified\_timestamp**: INTEGER - **rating\_offered\_timestamp**: INTEGER - **rating\_rated\_timestamp**: INTEGER - **rating\_scheduled\_for\_timestamp**: INTEGER - **rating\_scheduled\_timestamp**: INTEGER - **rating\_score**: INTEGER - **rating\_status**: STRING - **rating\_type**: STRING - **rating\_unscheduled\_timestamp**: STRING |
| **requester\_email**  STRING |
| **requester\_id**  STRING |
| **requester\_name**  STRING |
| **requester\_phone\_number**  STRING |
| **status**  STRING |
| **subject**  STRING |
| **tags**  ARRAY |
| **tags\_info**  ARRAY This is a nested data structure:   - **id**: STRING - **is\_deactivated**: BOOLEAN - **name**: STRING |
| **to\_provisioned\_phone\_number\_id**  STRING |
| **to\_provisioned\_phone\_number\_name**  STRING |
| **total\_duration**  INTEGER |
| **transfer\_time**  INTEGER |
| **transferee\_name**  STRING |
| **transferee\_number**  STRING |
| **updated\_at**  INTEGER |
| **widget\_id**  STRING |
| **widget\_name**  STRING |

### messages

The `messages` table contains information about all messages in your Dixa account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | created\_at |
| **Useful links** | [Dixa API method](https://docs.dixa.io/openapi/dixa-api/v1/tag/Messages/ "Opens in new tab: Dixa API method") |

messages table foreign keys

| Join messages with | on |
| --- | --- |
| [activity\_logs](#activity-logs) | ``` messages.id = activity_logs.attributes.messageId ``` |

messages table schema

|  |
| --- |
| **attached\_files**  ARRAY |
| **author\_email**  STRING |
| **author\_name**  STRING |
| **bcc**  ARRAY |
| **cc**  ARRAY |
| **chat\_input\_answer**  STRING |
| **chat\_input\_question**  STRING |
| **chat\_menu\_text**  STRING |
| **created\_at**  INTEGER |
| **csid**  INTEGER |
| **direction**  STRING |
| **duration**  INTEGER |
| **from**  STRING |
| **from\_phone\_number**  STRING |
| **id**  STRING |
| **initial\_channel**  STRING |
| **is\_automated\_message**  BOOLEAN |
| **recording\_url**  STRING |
| **text**  STRING |
| **to**  ARRAY |
| **to\_phone\_number**  STRING |
| **voicemail\_url**  STRING |
