---
title: "Microsoft Teams"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Microsoft-Teams.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Microsoft Teams

Microsoft Teams is Microsoft's cloud-based team collaboration platform, part of the Microsoft 365 suite. It provides persistent chat channels, video conferencing, file storage, and integration with other Microsoft 365 services.

Microsoft Teams integration replicates data using the [Microsoft Graph API](https://learn.microsoft.com/en-us/graph/api/overview).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To set up your Microsoft Teams account, you need:

- A Microsoft 365 account with Microsoft Teams deployed in your organization.
- An Azure subscription with access to the Azure portal ([portal.azure.com](https://portal.azure.com)) or Entra Admin Center ([entra.microsoft.com](https://entra.microsoft.com)).
- Permission to register applications and grant admin consent in your Microsoft Entra ID tenant (Global Administrator or Application Administrator role).

To register a Microsoft Entra ID application and grant API permissions:

1. Log into your [Microsoft Entra admin center](https://entra.microsoft.com/) account.
2. Navigate to Entra ID > App registrations.
3. Click New registration.
4. Enter a name for the application (for example, QlikDataIntegration), select Accounts in this organizational directory only, and click Register.
5. On the application's Overview page, copy the Application (client) ID and the Directory (tenant) ID and paste them into a secured file.
6. Navigate to Certificates & secrets > Client secrets > New client secret.
7. Enter a description and expiration date, and click Add.

   Copy and paste the secret Value into a secured file.
8. Navigate to API permissions > Add a permission > Microsoft Graph > Application permissions.
9. Add the following permissions:
   - `User.Read.All` — required for the `users` stream.
   - `Group.Read.All` — required for the `groups`, `group_members`, `group_owners`, `channels`, `channel_members`, `channel_tabs`, `channel_messages`, `channel_message_replies`, `conversations`, `conversation_threads`, and `conversation_posts` streams.
   - `Files.Read.All` — required for the `team_drives` stream.
   - `Reports.Read.All` — required for the `team_device_usage_report` stream.
10. Click Grant admin consent for [your organization] and confirm.

    All permissions must show a green “Granted” status before the connector will work.

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
| Tenant ID | Directory (tenant) ID. |
| OAuth Application ID | Application (client) ID. |
| Application Secret | Client secret. |

## Limitations and considerations

- Authentication uses application (client credentials) permissions. A Global Administrator or Application Administrator must grant admin consent for all required API permissions.
- The `team_device_usage_report` stream calls the Microsoft Graph reports endpoint, which returns data for the past 28 days only. By default, Microsoft 365 anonymizes user identity columns (`user_principal_name`, `user_id`) in usage reports. To retrieve actual user identities, a tenant admin can enable Display concealed user, group, and site names in all reports in the Microsoft 365 admin center under Settings > Org settings > Services > Reports.
- Incremental streams use a mix of server-side and client-side bookmark filtering. The `channel_messages` stream uses the Graph `/messages/delta` endpoint with a `$filter` query. The `team_device_usage_report` stream iterates day-by-day using a date URL parameter. The `channel_message_replies`, `conversations`, `conversation_threads`, `conversation_posts`, and `team_drives` streams retrieve all records and filter client-side because the underlying endpoints do not support `$filter` on the bookmark field.
- Groups without "Team" in the `resourceProvisioningOptions` property are excluded from Teams-specific stream queries (such as `channels`, `channel_messages`, `channel_members`, and so on).
- Field names are normalized from camelCase to snake\_case during extraction.
- Microsoft Graph API throttling limits apply. The connector handles rate limiting automatically with retry logic.

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### channel\_members

The `channel_members` table contains information about conversation members within a chat or channel in your Microsoft account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | id  group\_id  channel\_id |
| **Useful links** | [Microsoft Teams API method](https://docs.microsoft.com/en-us/graph/api/conversationmember-list?view=graph-rest-beta&tabs=http "Opens in new tab: Microsoft Teams API method") |

channel\_members table foreign keys

| Join channel\_members with | on |
| --- | --- |
| [channels](#channels) | ``` channel_members.channel_id = channels.id ``` |
| [channel\_tabs](#channel-tabs) | ``` channel_members.channel_id = channel_tabs.channel_id ``` |
| [channel\_messages](#channel-messages) | ``` channel_members.channel_id = channel_messages.channel_identity.channel_id ```  ``` channel_members.user_id = channel_messages.from.user.id ```  ``` channel_members.user_id = channel_messages.mentions.mentioned.user.id ```  ``` channel_members.user_id = channel_messages.reactions.user.user.id ``` |
| [channel\_message\_replies](#channel-message-replies) | ``` channel_members.channel_id = channel_message_replies.channel_identity.channel_id ```  ``` channel_members.user_id = channel_message_replies.from.user.id ```  ``` channel_members.user_id = channel_message_replies.mentions.mentioned.user.id ```  ``` channel_members.user_id = channel_message_replies.reactions.user.user.id ``` |
| [users](#users) | ``` channel_members.user_id = users.id ``` |

channel\_members table schema

|  |
| --- |
| **channel\_id**  STRING |
| **display\_name**  STRING |
| **email**  STRING |
| **id**  STRING |
| **roles**  ARRAY This is a nested data structure. |
| **user\_id**  STRING |

### channel\_message\_replies

The `channel_message_replies` table contains information about message replies within a channel in one of your Microsoft teams.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | id  group\_id  channel\_id  message\_id |
| **Replication Key** | created\_date\_time |
| **Useful links** | [Microsoft Teams API method](https://docs.microsoft.com/en-us/graph/api/channel-list-messagereplies?view=graph-rest-beta&tabs=http "Opens in new tab: Microsoft Teams API method") |

channel\_message\_replies table foreign keys

| Join channel\_message\_replies with | on |
| --- | --- |
| [channels](#channels) | ``` channel_message_replies.channel_identity.channel_id = channels.id ``` |
| [channel\_members](#channel-members) | ``` channel_message_replies.channel_identity.channel_id = channel_members.channel_id ```  ``` channel_message_replies.from.user.id = channel_members.user_id ```  ``` channel_message_replies.mentions.mentioned.user.id = channel_members.user_id ```  ``` channel_message_replies.reactions.user.user.id = channel_members.user_id ``` |
| [channel\_tabs](#channel-tabs) | ``` channel_message_replies.channel_identity.channel_id = channel_tabs.channel_id ``` |
| [channel\_messages](#channel-messages) | ``` channel_message_replies.channel_identity.channel_id = channel_messages.channel_identity.channel_id ```  ``` channel_message_replies.from.user.id = channel_messages.from.user.id ```  ``` channel_message_replies.mentions.mentioned.user.id = channel_messages.from.user.id ```  ``` channel_message_replies.reactions.user.user.id = channel_messages.from.user.id ```  ``` channel_message_replies.from.user.id = channel_messages.mentions.mentioned.user.id ```  ``` channel_message_replies.mentions.mentioned.user.id = channel_messages.mentions.mentioned.user.id ```  ``` channel_message_replies.reactions.user.user.id = channel_messages.mentions.mentioned.user.id ```  ``` channel_message_replies.from.user.id = channel_messages.reactions.user.user.id ```  ``` channel_message_replies.mentions.mentioned.user.id = channel_messages.reactions.user.user.id ```  ``` channel_message_replies.reactions.user.user.id = channel_messages.reactions.user.user.id ``` |
| [users](#users) | ``` channel_message_replies.from.user.id = users.id ```  ``` channel_message_replies.mentions.mentioned.user.id = users.id ```  ``` channel_message_replies.reactions.user.user.id = users.id ``` |

channel\_message\_replies table schema

|  |
| --- |
| **attachments**  ARRAY This is a nested data structure:   - content: STRING - content\_type: STRING - content\_url: STRING - id: STRING - name: STRING - thumbnail\_url: STRING |
| **body**  OBJECT This is a nested data structure:   - content: STRING - content\_type: STRING |
| **channel\_identity**  OBJECT This is a nested data structure:   - channel\_id: STRING - teamId: STRING |
| **chat\_id**  STRING |
| **created\_date\_time**  DATE-TIME |
| **deleted\_date\_time**  DATE-TIME |
| **etag**  STRING |
| **from**  OBJECT This is a nested data structure:   - application: STRING - conversation: STRING - device: STRING - user: OBJECT, which is also a nested data structure.   - display\_name: STRING   - id: STRING   - user\_identity\_type: STRING |
| **id**  STRING |
| **importance**  STRING |
| **last\_modified\_date\_time**  DATE-TIME |
| **locale**  STRING |
| **mentions**  ARRAY This is a nested data structure:   - id: INTEGER - mention\_text: STRING - mentioned: OBJECT, which is also a nested data structure.   - application: STRING   - conversation: STRING   - device: STRING   - user: OBJECT, which is also a nested data structure.     - display\_name: STRING     - id: STRING     - user\_identity\_type: STRING |
| **message\_type**  STRING |
| **policy\_violation**  STRING |
| **reactions**  ARRAY This is a nested data structure:   - created\_date\_time: DATE-TIME - reaction\_type: STRING - user: OBJECT, which is also a nested data structure.   - application: STRING   - conversation: STRING   - device: STRING   - user: OBJECT, which is also a nested data structure.     - display\_name: STRING     - id: STRING     - user\_identity\_type: STRING |
| **reply\_to\_id**  STRING |
| **subject**  STRING |
| **summary**  STRING |
| **web\_url**  STRING |

### channel\_messages

The `channel_messages` table contains information about messages in a channel, without replies, in your Microsoft account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | id  group\_id  channel\_id |
| **Replication Key** | last\_modified\_date\_time |
| **Useful links** | [Microsoft Teams API method](https://docs.microsoft.com/en-us/graph/api/chatmessage-delta?view=graph-rest-beta&tabs=http "Opens in new tab: Microsoft Teams API method") |

channel\_messages table foreign keys

| Join channel\_messages with | on |
| --- | --- |
| [channels](#channels) | ``` channel_messages.channel_identity.channel_id = channels.id ``` |
| [channel\_members](#channel-members) | ``` channel_messages.channel_identity.channel_id = channel_members.channel_id ```  ``` channel_messages.from.user.id = channel_members.user_id ```  ``` channel_messages.mentions.mentioned.user.id = channel_members.user_id ```  ``` channel_messages.reactions.user.user.id = channel_members.user_id ``` |
| [channel\_tabs](#channel-tabs) | ``` channel_messages.channel_identity.channel_id = channel_tabs.channel_id ``` |
| [channel\_message\_replies](#channel-message-replies) | ``` channel_messages.channel_identity.channel_id = channel_message_replies.channel_identity.channel_id ```  ``` channel_messages.from.user.id = channel_message_replies.from.user.id ```  ``` channel_messages.mentions.mentioned.user.id = channel_message_replies.from.user.id ```  ``` channel_messages.reactions.user.user.id = channel_message_replies.from.user.id ```  ``` channel_messages.from.user.id = channel_message_replies.mentions.mentioned.user.id ```  ``` channel_messages.mentions.mentioned.user.id = channel_message_replies.mentions.mentioned.user.id ```  ``` channel_messages.reactions.user.user.id = channel_message_replies.mentions.mentioned.user.id ```  ``` channel_messages.from.user.id = channel_message_replies.reactions.user.user.id ```  ``` channel_messages.mentions.mentioned.user.id = channel_message_replies.reactions.user.user.id ```  ``` channel_messages.reactions.user.user.id = channel_message_replies.reactions.user.user.id ``` |
| [users](#users) | ``` channel_messages.from.user.id = users.id ```  ``` channel_messages.mentions.mentioned.user.id = users.id ```  ``` channel_messages.reactions.user.user.id = users.id ``` |

channel\_messages table schema

|  |
| --- |
| **attachments**  ARRAY This is a nested data structure:   - content: STRING - content\_type: STRING - content\_url: STRING - id: STRING - name: STRING - thumbnail\_url: STRING |
| **body**  OBJECT This is a nested data structure:   - content: STRING - content\_type: STRING |
| **channel\_identity**  OBJECT This is a nested data structure:   - channel\_id: STRING - teamId: STRING |
| **chat\_id**  STRING |
| **created\_date\_time**  DATE-TIME |
| **deleted\_date\_time**  DATE-TIME |
| **etag**  STRING |
| **from**  OBJECT This is a nested data structure:   - application: STRING - conversation: STRING - device: STRING - user: OBJECT, which is also a nested data structure.   - display\_name: STRING   - id: STRING   - user\_identity\_type: STRING |
| **id**  STRING |
| **importance**  STRING |
| **lastModified\_date\_time**  DATE-TIME |
| **locale**  STRING |
| **mentions**  ARRAY This is a nested data structure:   - id: INTEGER - mention\_text: STRING - mentioned: OBJECT, which is also a nested data structure.   - application: STRING   - conversation: STRING   - device: STRING   - user: OBJECT, which is also a nested data structure.     - display\_name: STRING     - id: STRING     - userIdentity\_type: STRING |
| **message\_type**  STRING |
| **policy\_violation**  STRING |
| **reactions**  ARRAY This is a nested data structure:   - created\_date\_time: DATE-TIME - reaction\_type: STRING - user: OBJECT, which is also a nested data structure.   - application: STRING   - conversation: STRING   - device: STRING   - user: OBJECT, which is also a nested data structure.     - display\_name: STRING     - id: STRING     - user\_identity\_type: STRING |
| **reply\_to\_id**  STRING |
| **subject**  STRING |
| **summary**  STRING |
| **web\_url**  STRING |

### channel\_tabs

The `channel_tabs` table contains information about tabs within a channel in one of your Microsoft teams.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | id  group\_id  channel\_id |
| **Useful links** | [Microsoft Teams documentation](https://docs.microsoft.com/en-us/graph/api/teamstab-list?view=graph-rest-beta)  [Microsoft Teams API method](https://docs.microsoft.com/en-us/graph/api/teamstab-list?view=graph-rest-1.0 "Opens in new tab: Microsoft Teams API method") |

channel\_tabs table foreign keys

| Join channel\_tabs with | on |
| --- | --- |
| [channels](#channels) | ``` channel_tabs.channel_id = channels.id ``` |
| [channel\_members](#channel-members) | ``` channel_tabs.channel_id = channel_members.channel_id ``` |
| [channel\_messages](#channel-messages) | ``` channel_tabs.channel_id = channel_messages.channel_identity.channel_id ``` |
| [channel\_message\_replies](#channel-message-replies) | ``` channel_tabs.channel_id = channel_message_replies.channel_identity.channel_id ``` |
| [groups](#groups) | ``` channel_tabs.group_id = groups.id ``` |
| [group\_owners](#group-owners) | ``` channel_tabs.group_id = group_owners.group_id ``` |
| [conversations](#conversations) | ``` channel_tabs.group_id = conversations.group_id ``` |
| [conversation\_threads](#conversation-threads) | ``` channel_tabs.group_id = conversation_threads.group_id ``` |
| [team\_drives](#team-drives) | ``` channel_tabs.group_id = team_drives.owner.group.id ``` |

channel\_tabs table schema

|  |
| --- |
| **channel\_id**  STRING |
| **configuration**  OBJECT This is a nested data structure:   - content\_url: STRING - entity\_id: STRING - has\_content: BOOLEAN - remove\_url: STRING - website\_url: STRING - wiki\_default\_tab: BOOLEAN - wiki\_tab\_id: INTEGER |
| **display\_name**  STRING |
| **group\_id**  STRING |
| **id**  STRING |
| **sort\_order\_index**  STRING |
| **teams\_app**  OBJECT This is a nested data structure:   - display\_name: STRING - distribution\_method: STRING - id: STRING |
| **web\_url**  STRING |

### channels

The `channels` table contains information about the channels within a team in your Microsoft account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | id  group\_id |
| **Useful links** | [Microsoft Teams API method](https://docs.microsoft.com/en-us/graph/api/channel-list?view=graph-rest-1.0&tabs=http "Opens in new tab: Microsoft Teams API method") |

channels table foreign keys

| Join channels with | on |
| --- | --- |
| [channel\_members](#channel-members) | ``` channels.id = channel_members.channel_id ``` |
| [channel\_tabs](#channel-tabs) | ``` channels.id = channel_tabs.channel_id ``` |
| [channel\_messages](#channel-messages) | ``` channels.id = channel_messages.channel_identity.channel_id ``` |
| [channel\_message\_replies](#channel-message-replies) | ``` channels.id = channel_message_replies.channel_identity.channel_id ``` |

channels table schema

|  |
| --- |
| **description**  STRING |
| **display\_name**  STRING |
| **email**  STRING |
| **id**  STRING |
| **web\_url**  STRING |

### conversation\_posts

The `conversation_posts` table contains information about the posts within a conversation thread in your Microsoft account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | id  change\_key  group\_id  conversation\_id  thread\_id |
| **Replication Key** | last\_modified\_date\_time |
| **Useful links** | [Microsoft Teams documentation](https://docs.microsoft.com/en-us/graph/api/conversationthread-list-posts?view=graph-rest-beta&tabs=http)  [Microsoft Teams API method](https://docs.microsoft.com/en-us/graph/api/conversationthread-list-posts?view=graph-rest-1.0&tabs=http "Opens in new tab: Microsoft Teams API method") |

conversation\_posts table foreign keys

| Join conversation\_posts with | on |
| --- | --- |
| [conversations](#conversations) | ``` conversation_posts.conversation_id = conversations.id ``` |
| [conversation\_threads](#conversation-threads) | ``` conversation_posts.conversation_id = conversation_threads.conversation_id ```  ``` conversation_posts.thread_id = conversation_threads.id ``` |

conversation\_posts table schema

|  |
| --- |
| **body**  OBJECT This is a nested data structure:   - content: STRING - content\_type: STRING |
| **categories**  ARRAY This is a nested data structure. |
| **change\_key**  STRING |
| **conversation\_id**  STRING |
| **created\_date\_time**  DATE-TIME |
| **from**  OBJECT This is a nested data structure:   - emailAddress: OBJECT, which is also a nested data structure.   - address: STRING   - name: STRING |
| **has\_attachments**  BOOLEAN |
| **id**  STRING |
| **last\_modified\_date\_time**  DATE-TIME |
| **received\_date\_time**  DATE-TIME |
| **sender**  OBJECT This is a nested data structure:   - emailAddress: OBJECT, which is also a nested data structure.   - address: STRING   - name: STRING |
| **thread\_id**  STRING |

### conversation\_threads

The `conversation_threads` table contains information about threads in a group conversation in your Microsoft account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | id  conversation\_id  group\_id |
| **Replication Key** | last\_delivered\_date\_time |
| **Useful links** | [Microsoft Teams documentation](https://docs.microsoft.com/en-us/graph/api/conversation-list-threads?view=graph-rest-beta&tabs=http)  [Microsoft Teams API method](https://docs.microsoft.com/en-us/graph/api/group-list-threads?view=graph-rest-1.0&tabs=http "Opens in new tab: Microsoft Teams API method") |

conversation\_threads table foreign keys

| Join conversation\_threads with | on |
| --- | --- |
| [conversations](#conversations) | ``` conversation_threads.conversation_id = conversations.id ```  ``` conversation_threads.group_id = conversations.group_id ``` |
| [conversation\_posts](#conversation-posts) | ``` conversation_threads.conversation_id = conversation_posts.conversation_id ```  ``` conversation_threads.id = conversation_posts.thread_id ``` |
| [groups](#groups) | ``` conversation_threads.group_id = groups.id ``` |
| [group\_owners](#group-owners) | ``` conversation_threads.group_id = group_owners.group_id ``` |
| [channel\_tabs](#channel-tabs) | ``` conversation_threads.group_id = channel_tabs.group_id ``` |
| [team\_drives](#team-drives) | ``` conversation_threads.group_id = team_drives.owner.group.id ``` |

conversation\_threads table schema

|  |
| --- |
| **conversation\_id**  STRING |
| **group\_id**  STRING |
| **has\_attachments**  BOOLEAN |
| **id**  STRING |
| **is\_locked**  BOOLEAN |
| **last\_delivered\_date\_time**  DATE-TIME |
| **preview**  STRING |
| **topic**  STRING |
| **unique\_senders**  STRING |

### conversations

The `conversations` table contains information about conversations within a group in your Microsoft account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | id  group\_id |
| **Replication Key** | last\_delivered\_date\_time |
| **Useful links** | [Microsoft Teams documentation](https://docs.microsoft.com/en-us/graph/api/group-list-conversations?view=graph-rest-beta&tabs=http)  [Microsoft Teams API method](https://docs.microsoft.com/en-us/graph/api/group-list-conversations?view=graph-rest-1.0&tabs=http "Opens in new tab: Microsoft Teams API method") |

conversations table foreign keys

| Join conversations with | on |
| --- | --- |
| [conversation\_threads](#conversation-threads) | ``` conversations.id = conversation_threads.conversation_id ```  ``` conversations.group_id = conversation_threads.group_id ``` |
| [conversation\_posts](#conversation-posts) | ``` conversations.id = conversation_posts.conversation_id ``` |
| [groups](#groups) | ``` conversations.group_id = groups.id ``` |
| [group\_owners](#group-owners) | ``` conversations.group_id = group_owners.group_id ``` |
| [channel\_tabs](#channel-tabs) | ``` conversations.group_id = channel_tabs.group_id ``` |
| [team\_drives](#team-drives) | ``` conversations.group_id = team_drives.owner.group.id ``` |

conversations table schema

|  |
| --- |
| **group\_id**  STRING |
| **has\_attachments**  BOOLEAN |
| **id**  STRING |
| **last\_delivered\_date\_time**  DATE-TIME |
| **preview**  STRING |
| **topic**  STRING |
| **unique\_senders**  ARRAY This is a nested data structure. |

### group\_members

The `group_members` table contains information about group members in your Microsoft account. Members can be users, organizational contacts, devices, service principals, and other groups.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | id  group\_id |
| **Useful links** | [Microsoft Teams API method](https://docs.microsoft.com/en-us/graph/api/group-list-members?view=graph-rest-1.0&tabs=http "Opens in new tab: Microsoft Teams API method") |

group\_members table schema

|  |
| --- |
| **business\_phones**  ARRAY This is a nested data structure. |
| **display\_name**  STRING |
| **given\_name**  STRING |
| **id**  STRING |
| **job\_title**  STRING |
| **mail**  STRING |
| **mobile\_phone**  STRING |
| **office\_location**  STRING |
| **preferred\_language**  STRING |
| **surname**  STRING |
| **user\_principal\_name**  STRING |

### group\_owners

The `group_owners` table contains information about groups’ owners in your Microsoft account. The owners can be a set of users or service principals that have modifying priviliges.

**Note**: Groups created in Microsoft Exchange will not be available in this table.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | id  group\_id |
| **Useful links** | [Microsoft Teams API method](https://docs.microsoft.com/en-us/graph/api/group-list-owners?view=graph-rest-1.0&tabs=http "Opens in new tab: Microsoft Teams API method") |

group\_owners table foreign keys

| Join group\_owners with | on |
| --- | --- |
| [groups](#groups) | ``` group_owners.group_id = groups.id ``` |
| [channel\_tabs](#channel-tabs) | ``` group_owners.group_id = channel_tabs.group_id ``` |
| [conversations](#conversations) | ``` group_owners.group_id = conversations.group_id ``` |
| [conversation\_threads](#conversation-threads) | ``` group_owners.group_id = conversation_threads.group_id ``` |
| [team\_drives](#team-drives) | ``` group_owners.group_id = team_drives.owner.group.id ``` |

group\_owners table schema

|  |
| --- |
| **business\_phones**  ARRAY This is a nested data structure. |
| **display\_name**  STRING |
| **given\_name**  STRING |
| **group\_id**  STRING |
| **id**  STRING |
| **job\_title**  STRING |
| **mail**  STRING |
| **mobile\_phone**  STRING |
| **office\_location**  STRING |
| **preferred\_language**  STRING |
| **surname**  STRING |
| **user\_principal\_name**  STRING |

### groups

The `groups` table contains information about groups in your organization within your Microsoft account. Some old teams in your account will not have a `resource_provisioning_options` value. For more information, refer to [Microsoft’s docs](https://docs.microsoft.com/en-us/graph/known-issues#missing-teams-in-list-all-teams).

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Microsoft Teams API method](https://docs.microsoft.com/en-us/graph/teams-list-all-teams?context=graph%2Fapi%2Fbeta&view=graph-rest-beta "Opens in new tab: Microsoft Teams API method") |

groups table foreign keys

| Join groups with | on |
| --- | --- |
| [group\_owners](#group-owners) | ``` groups.id = group_owners.group_id ``` |
| [channel\_tabs](#channel-tabs) | ``` groups.id = channel_tabs.group_id ``` |
| [conversations](#conversations) | ``` groups.id = conversations.group_id ``` |
| [conversation\_threads](#conversation-threads) | ``` groups.id = conversation_threads.group_id ``` |
| [team\_drives](#team-drives) | ``` groups.id = team_drives.owner.group.id ``` |

groups table schema

|  |
| --- |
| **classification**  STRING |
| **created\_date\_time**  DATE-TIME |
| **creation\_options**  ARRAY This is a nested data structure. |
| **deleted\_date\_time**  DATE-TIME |
| **description**  STRING |
| **display\_name**  STRING |
| **expiration\_date\_time**  DATE-TIME |
| **group\_types**  ARRAY This is a nested data structure. |
| **id**  STRING |
| **is\_assignable\_to\_role**  BOOLEAN |
| **mail**  STRING |
| **mail\_enabled**  BOOLEAN |
| **mail\_nickname**  STRING |
| **membership\_rule**  STRING |
| **membership\_rule\_processing\_state**  STRING |
| **onPremises\_domain\_name**  STRING |
| **on\_premises\_last\_sync\_date\_time**  DATE-TIME |
| **on\_premises\_net\_bios\_name**  STRING |
| **on\_premises\_provisioning\_errors**  ARRAY This is a nested data structure. |
| **on\_premises\_sam\_account\_name**  STRING |
| **on\_premises\_security\_identifier**  STRING |
| **on\_premises\_sync\_enabled**  BOOLEAN |
| **preferred\_data\_location**  STRING |
| **preferred\_language**  STRING |
| **proxy\_addresses**  ARRAY This is a nested data structure. |
| **renewed\_date\_time**  DATE-TIME |
| **resource\_behavior\_options**  ARRAY This is a nested data structure. |
| **resource\_provisioning\_options**  ARRAY This is a nested data structure. |
| **security\_edentifier**  STRING |
| **security\_enabled**  BOOLEAN |
| **theme**  STRING |
| **visibility**  STRING |

### team\_device\_usage\_report

The `team_device_usage_report` table contains information about a group’s device usage in Microsoft Teams.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | user\_principal\_name  report\_refresh\_date |
| **Replication Key** | report\_refresh\_date |
| **Useful links** | [Microsoft Teams API method](https://docs.microsoft.com/en-us/graph/api/reportroot-getteamsdeviceusageuserdetail?view=graph-rest-beta "Opens in new tab: Microsoft Teams API method") |

team\_device\_usage\_report table schema

|  |
| --- |
| **deleted\_date**  STRING |
| **is\_deleted**  STRING |
| **last\_activity\_date**  STRING |
| **report\_period**  STRING |
| **report\_refresh\_date**  STRING |
| **used\_android\_phone**  STRING |
| **used\_i\_os**  STRING |
| **used\_mac**  STRING |
| **used\_web**  STRING |
| **used\_windows**  STRING |
| **used\_windows\_phone**  STRING |
| **user\_principal\_name**  STRING |

### team\_drives

The `team_drives` table contains information about the drive that your team is on in your Microsoft account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | id  group\_id |
| **Replication Key** | last\_modified\_date\_time |
| **Useful links** | [Microsoft Teams API method](https://docs.microsoft.com/en-us/graph/api/drive-get?view=graph-rest-beta&tabs=http#get-the-document-library-associated-with-a-group "Opens in new tab: Microsoft Teams API method") |

team\_drives table foreign keys

| Join team\_drives with | on |
| --- | --- |
| [groups](#groups) | ``` team_drives.owner.group.id = groups.id ``` |
| [group\_owners](#group-owners) | ``` team_drives.owner.group.id = group_owners.group_id ``` |
| [channel\_tabs](#channel-tabs) | ``` team_drives.owner.group.id = channel_tabs.group_id ``` |
| [conversations](#conversations) | ``` team_drives.owner.group.id = conversations.group_id ``` |
| [conversation\_threads](#conversation-threads) | ``` team_drives.owner.group.id = conversation_threads.group_id ``` |

team\_drives table schema

|  |
| --- |
| **created\_by**  OBJECT This is a nested data structure:   - user: OBJECT, which is also a nested data structure.   - display\_name: STRING |
| **drive\_type**  STRING |
| **id**  STRING |
| **last\_modified\_date\_time**  STRING |
| **name**  STRING |
| **owner**  OBJECT This is a nested data structure:   - group: OBJECT, which is also a nested data structure.   - display\_name: STRING   - email: STRING   - id: STRING |
| **quota**  OBJECT This is a nested data structure:   - deleted: INTEGER - remaining: NUMBER - state: STRING - total: NUMBER - used: INTEGER |
| **web\_url**  STRING |

### users

The `users` table contains information about users in your Microsoft account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Microsoft Teams documentation](https://docs.microsoft.com/en-us/graph/api/resources/user?view=graph-rest-beta.htm)  [Microsoft Teams API method](https://docs.microsoft.com/en-us/graph/api/user-list?view=graph-rest-1.0&tabs=http "Opens in new tab: Microsoft Teams API method") |

users table foreign keys

| Join users with | on |
| --- | --- |
| [channel\_members](#channel-members) | ``` users.id = channel_members.user_id ``` |
| [channel\_message\_replies](#channel-message-replies) | ``` users.id = channel_message_replies.from.user.id ```  ``` users.id = channel_message_replies.mentions.mentioned.user.id ```  ``` users.id = channel_message_replies.reactions.user.user.id ``` |
| [channel\_messages](#channel-messages) | ``` users.id = channel_messages.from.user.id ```  ``` users.id = channel_messages.mentions.mentioned.user.id ```  ``` users.id = channel_messages.reactions.user.user.id ``` |

users table schema

|  |
| --- |
| **business\_phones**  ARRAY This is a nested data structure. |
| **display\_name**  STRING |
| **given\_name**  STRING |
| **id**  STRING |
| **job\_title**  STRING |
| **mail**  STRING |
| **mobile\_phone**  STRING |
| **office\_location**  STRING |
| **preferred\_language**  STRING |
| **surname**  STRING |
| **user\_principal\_name**  STRING |
