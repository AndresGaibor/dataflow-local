---
title: "Slack"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Slack.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Slack

Slack is a cloud-based team communication platform.

Slack integration replicates data from a single Slack workspace using the [Slack Web API](https://api.slack.com/web). To replicate data from multiple workspaces, create an additional Slack integration for each workspace.

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

Qlik Talend Cloud supports data replication from one Slack workspace per connection. To replicate data from multiple workspaces, set up a separate Slack connection for each workspace in Qlik Talend Cloud, using a unique OAuth token for every connection.

To retrieve your token:

1. Navigate to the [Slack App site](https://api.slack.com/apps).
2. Click Create an App.
3. Enter a name for the app and select the workspace you want to replicate data from.
4. Click Create App.
5. Once your app is created, select it and navigate to Features > OAuth & Permissions.
6. Scroll to the Scopes section.
7. In the Bot Token Scopes section, click Add an OAuth Scope.
8. In the field that appears, search for the following scopes:
   - `channels:history`
   - `channels:join`
   - `channels:read`
   - `files:read`
   - `groups:read`
   - `links:read`
   - `reactions:read`
   - `remote_files:read`
   - `remote_files:write`
   - `team:read`
   - `useergroups:read`
   - `users.profile:read`
   - `users:read`
   - `users:read.email`

   After the required scopes are added to the app, you need to install it to your Slack workspace. If you do not have the required permissions to install apps, you may need Workspace Owner approval. See [Slack's documentation](https://www.stitchdata.com/docs/integrations/saas/slack) for app installation requirements.
9. Scroll up to the OAuth Tokens & Redirect URLs section of the OAuth & Permissions page.
10. In this section, click Install App to Workspace.
11. Complete the steps that follow to install the app or submit a request to your Workspace Owner for approval.

    Result: Once the app is installed in your workspace, a Tokens for Your Workspace section containing a Bot User OAuth Access Token field is displayed.
12. Copy and paste your token into a secured file.

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
| Token | Token. |
| Join Public Channels | Select the check box to replicate data for all public channels in the workspace you are connecting. |
| Include Private Channels | Select the check box to include data from private channels. |
| Exclude Archived Channels | Select the check box to exclude data from archived channels. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### channel\_members

The `channel_members` table contain info about members of channels in your Slack workspace. Channels include conversations, channels, and direct messages in your Slack workspace.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | channel\_id  user\_id |
| **Useful links** | [Slack documentation](https://api.slack.com/Content/conversations-api)  [Slack API method](https://api.slack.com/methods/conversations.members "Opens in new tab: Slack API method") |

channel\_members table foreign keys

| Join channel\_members with | on |
| --- | --- |
| [channels](#channels) | ``` channel_members.channel_id = channels.id ```  ``` channel_members.user_id = channels.creator ```  ``` channel_members.user_id = channels.members ``` |
| [files](#files) | ``` channel_members.channel_id = files.channels ```  ``` channel_members.channel_id = files.pinned_to ```  ``` channel_members.user_id = files.user ``` |
| [messages](#messages) | ``` channel_members.channel_id = messages.channel_id ```  ``` channel_members.channel_id = messages.pinned_to ```  ``` channel_members.user_id = messages.reply_users ```  ``` channel_members.user_id = messages.reactions.users ```  ``` channel_members.user_id = messages.user ``` |
| [remote\_files](#remote-files) | ``` channel_members.channel_id = remote_files.channels ```  ``` channel_members.channel_id = remote_files.pinned_to ```  ``` channel_members.user_id = remote_files.user ``` |
| [threads](#threads) | ``` channel_members.channel_id = threads.channel_id ```  ``` channel_members.user_id = threads.user ```  ``` channel_members.user_id = threads.reply_users ``` |
| [user\_groups](#user-groups) | ``` channel_members.user_id = user_groups.members ```  ``` channel_members.user_id = user_groups.purpose.creator ```  ``` channel_members.user_id = user_groups.topic.creator ``` |
| [users](#users) | ``` channel_members.user_id = users.id ``` |

channel\_members table schema

|  |
| --- |
| **channel\_id**  STRING |
| **user\_id**  STRING |

### channels

The `channels` table contains info about the channels in your Slack workspace. This includes conversations, channels, and direct messages.

Information noteSome types of channels - for example, private or archived channels - will be replicated only if the appropriate settings are configured in the integration’s settings. Refer to the Slack [setup steps](#add-integration) for more info.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Slack documentation](https://api.slack.com/types/channel)  [Slack API method](https://api.slack.com/methods/conversations.list "Opens in new tab: Slack API method") |

channels table foreign keys

| Join channels with | on |
| --- | --- |
| [channel\_members](#channel-members) | ``` channels.id = channel_members.channel_id ```  ``` channels.creator = channel_members.user_id ```  ``` channels.members = channel_members.user_id ``` |
| [files](#files) | ``` channels.id = files.channels ```  ``` channels.id = files.pinned_to ```  ``` channels.pending_connected_team_ids = files.source_team ```  ``` channels.pending_connected_team_ids = files.user_team ```  ``` channels.creator = files.user ```  ``` channels.members = files.user ``` |
| [messages](#messages) | ``` channels.id = messages.channel_id ```  ``` channels.id = messages.pinned_to ```  ``` channels.pending_connected_team_ids = messages.bot_profile.team_id ```  ``` channels.pending_connected_team_ids = messages.team ```  ``` channels.pending_connected_team_ids = messages.source_team ```  ``` channels.pending_connected_team_ids = messages.user_team ```  ``` channels.creator = messages.reply_users ```  ``` channels.members = messages.reply_users ```  ``` channels.creator = messages.reactions.users ```  ``` channels.members = messages.reactions.users ```  ``` channels.creator = messages.user ```  ``` channels.members = messages.user ``` |
| [remote\_files](#remote-files) | ``` channels.id = remote_files.channels ```  ``` channels.id = remote_files.pinned_to ```  ``` channels.pending_connected_team_ids = remote_files.source_team ```  ``` channels.pending_connected_team_ids = remote_files.user_team ```  ``` channels.creator = remote_files.user ```  ``` channels.members = remote_files.user ``` |
| [threads](#threads) | ``` channels.id = threads.channel_id ```  ``` channels.pending_connected_team_ids = threads.team ```  ``` channels.creator = threads.user ```  ``` channels.members = threads.user ```  ``` channels.creator = threads.reply_users ```  ``` channels.members = threads.reply_users ``` |
| [teams](#teams) | ``` channels.pending_connected_team_ids = teams.id ``` |
| [users](#users) | ``` channels.pending_connected_team_ids = users.team_id ```  ``` channels.creator = users.id ```  ``` channels.members = users.id ``` |
| [user\_groups](#user-groups) | ``` channels.creator = user_groups.members ```  ``` channels.members = user_groups.members ```  ``` channels.creator = user_groups.purpose.creator ```  ``` channels.members = user_groups.purpose.creator ```  ``` channels.creator = user_groups.topic.creator ```  ``` channels.members = user_groups.topic.creator ``` |

channels table schema

|  |
| --- |
| **channel\_id**  STRING |
| **created**  DATE-TIME |
| **creator**  STRING |
| **id**  STRING |
| **is\_archived**  BOOLEAN |
| **is\_channel**  BOOLEAN |
| **is\_ext\_shared**  BOOLEAN |
| **is\_general**  BOOLEAN |
| **is\_group**  BOOLEAN |
| **is\_im**  BOOLEAN |
| **is\_member**  BOOLEAN |
| **is\_mpim**  BOOLEAN |
| **is\_org\_shared**  BOOLEAN |
| **is\_pending\_ext\_shared**  BOOLEAN |
| **is\_private**  BOOLEAN |
| **is\_shared**  BOOLEAN |
| **members**  ARRAY This is a nested data structure. |
| **name**  STRING |
| **name\_normalized**  STRING |
| **num\_members**  INTEGER |
| **parent\_conversation**  STRING |
| **pending\_connected\_team\_ids**  ARRAY This is a nested data structure. |
| **pending\_shared**  ARRAY This is a nested data structure. |
| **previous\_names**  ARRAY This is a nested data structure. |
| **purpose**  OBJECT This is a nested data structure:   - creator: STRING - last\_set: DATE-TIME - value: STRING |
| **shared\_team\_ids**  ARRAY This is a nested data structure. |
| **topic**  OBJECT This is a nested data structure:   - creator: STRING - last\_set: DATE-TIME - value: STRING |
| **unlinked**  DATE-TIME |

### files

The `files` table contains info about Slack team files.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated |
| **Useful links** | [Slack documentation](https://api.slack.com/types/file)  [Slack API method](https://api.slack.com/methods/files.list "Opens in new tab: Slack API method") |

files table foreign keys

| Join files with | on |
| --- | --- |
| [channels](#channels) | ``` files.channels = channels.id ```  ``` files.pinned_to = channels.id ```  ``` files.source_team = channels.pending_connected_team_ids ```  ``` files.user_team = channels.pending_connected_team_ids ```  ``` files.user = channels.creator ```  ``` files.user = channels.members ``` |
| [channel\_members](#channel-members) | ``` files.channels = channel_members.channel_id ```  ``` files.pinned_to = channel_members.channel_id ```  ``` files.user = channel_members.user_id ``` |
| [messages](#messages) | ``` files.channels = messages.channel_id ```  ``` files.pinned_to = messages.channel_id ```  ``` files.channels = messages.pinned_to ```  ``` files.pinned_to = messages.pinned_to ```  ``` files.id = messages.file_ids ```  ``` files.source_team = messages.bot_profile.team_id ```  ``` files.user_team = messages.bot_profile.team_id ```  ``` files.source_team = messages.team ```  ``` files.user_team = messages.team ```  ``` files.source_team = messages.source_team ```  ``` files.user_team = messages.source_team ```  ``` files.source_team = messages.user_team ```  ``` files.user_team = messages.user_team ```  ``` files.user = messages.reply_users ```  ``` files.user = messages.reactions.users ```  ``` files.user = messages.user ``` |
| [remote\_files](#remote-files) | ``` files.channels = remote_files.channels ```  ``` files.pinned_to = remote_files.channels ```  ``` files.channels = remote_files.pinned_to ```  ``` files.pinned_to = remote_files.pinned_to ```  ``` files.groups = remote_files.groups ```  ``` files.source_team = remote_files.source_team ```  ``` files.user_team = remote_files.source_team ```  ``` files.source_team = remote_files.user_team ```  ``` files.user_team = remote_files.user_team ```  ``` files.user = remote_files.user ``` |
| [threads](#threads) | ``` files.channels = threads.channel_id ```  ``` files.pinned_to = threads.channel_id ```  ``` files.source_team = threads.team ```  ``` files.user_team = threads.team ```  ``` files.user = threads.user ```  ``` files.user = threads.reply_users ``` |
| [user\_groups](#user-groups) | ``` files.groups = user_groups.id ```  ``` files.groups = user_groups.parent_group ```  ``` files.user = user_groups.members ```  ``` files.user = user_groups.purpose.creator ```  ``` files.user = user_groups.topic.creator ``` |
| [teams](#teams) | ``` files.source_team = teams.id ```  ``` files.user_team = teams.id ``` |
| [users](#users) | ``` files.source_team = users.team_id ```  ``` files.user_team = users.team_id ```  ``` files.user = users.id ``` |

files table schema

|  |
| --- |
| **channels**  ARRAY This is a nested data structure. |
| **comments\_count**  INTEGER |
| **created**  DATE-TIME |
| **date\_delete**  DATE-TIME |
| **display\_as\_bot**  BOOLEAN |
| **editable**  BOOLEAN |
| **editor**  STRING |
| **external\_id**  STRING |
| **external\_type**  STRING |
| **external\_url**  STRING |
| **filetype**  STRING |
| **groups**  ARRAY This is a nested data structure. |
| **has\_rich\_preview**  BOOLEAN |
| **id**  STRING |
| **image\_exif\_rotation**  INTEGER |
| **ims**  ARRAY This is a nested data structure. |
| **is\_external**  BOOLEAN |
| **is\_public**  BOOLEAN |
| **is\_starred**  BOOLEAN |
| **is\_tombstoned**  BOOLEAN |
| **last\_editor**  STRING |
| **mimetype**  STRING |
| **mode**  STRING |
| **name**  STRING |
| **non\_owner\_editable**  BOOLEAN |
| **num\_stars**  INTEGER |
| **original\_h**  INTEGER |
| **original\_w**  INTEGER |
| **permalink**  STRING |
| **permalink\_public**  STRING |
| **pinned\_info**  OBJECT This is a nested data structure. |
| **pinned\_to**  ARRAY This is a nested data structure. |
| **pretty\_type**  STRING |
| **preview**  STRING |
| **public\_url\_shared**  BOOLEAN |
| **size**  INTEGER |
| **source\_team**  STRING |
| **state**  STRING |
| **thumb\_1024**  STRING |
| **thumb\_1024\_h**  INTEGER |
| **thumb\_1024\_w**  INTEGER |
| **thumb\_160**  STRING |
| **thumb\_360**  STRING |
| **thumb\_360\_h**  INTEGER |
| **thumb\_360\_w**  INTEGER |
| **thumb\_480**  STRING |
| **thumb\_480\_h**  INTEGER |
| **thumb\_480\_w**  INTEGER |
| **thumb\_64**  STRING |
| **thumb\_720**  STRING |
| **thumb\_720\_h**  INTEGER |
| **thumb\_720\_w**  INTEGER |
| **thumb\_80**  STRING |
| **thumb\_800**  STRING |
| **thumb\_800\_h**  INTEGER |
| **thumb\_800\_w**  INTEGER |
| **thumb\_960**  STRING |
| **thumb\_960\_h**  INTEGER |
| **thumb\_960\_w**  INTEGER |
| **thumb\_tiny**  STRING |
| **timestamp**  DATE-TIME |
| **title**  STRING |
| **updated**  DATE-TIME |
| **url\_private**  STRING |
| **url\_private\_download**  STRING |
| **user**  STRING |
| **user\_team**  STRING |
| **username**  STRING |

### messages

The `messages` table contains the history of messages and events in conversations in your Slack workspace.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | channel\_id  ts |
| **Replication Key** | ts |
| **Useful links** | [Slack documentation](https://api.slack.com/types/conversation)  [Slack API method](https://api.slack.com/methods/conversations.history "Opens in new tab: Slack API method") |

messages table foreign keys

| Join messages with | on |
| --- | --- |
| [channels](#channels) | ``` messages.channel_id = channels.id ```  ``` messages.pinned_to = channels.id ```  ``` messages.bot_profile.team_id = channels.pending_connected_team_ids ```  ``` messages.team = channels.pending_connected_team_ids ```  ``` messages.source_team = channels.pending_connected_team_ids ```  ``` messages.user_team = channels.pending_connected_team_ids ```  ``` messages.reply_users = channels.creator ```  ``` messages.reactions.users = channels.creator ```  ``` messages.user = channels.creator ```  ``` messages.reply_users = channels.members ```  ``` messages.reactions.users = channels.members ```  ``` messages.user = channels.members ``` |
| [channel\_members](#channel-members) | ``` messages.channel_id = channel_members.channel_id ```  ``` messages.pinned_to = channel_members.channel_id ```  ``` messages.reply_users = channel_members.user_id ```  ``` messages.reactions.users = channel_members.user_id ```  ``` messages.user = channel_members.user_id ``` |
| [files](#files) | ``` messages.channel_id = files.channels ```  ``` messages.pinned_to = files.channels ```  ``` messages.channel_id = files.pinned_to ```  ``` messages.pinned_to = files.pinned_to ```  ``` messages.file_ids = files.id ```  ``` messages.bot_profile.team_id = files.source_team ```  ``` messages.team = files.source_team ```  ``` messages.source_team = files.source_team ```  ``` messages.user_team = files.source_team ```  ``` messages.bot_profile.team_id = files.user_team ```  ``` messages.team = files.user_team ```  ``` messages.source_team = files.user_team ```  ``` messages.user_team = files.user_team ```  ``` messages.reply_users = files.user ```  ``` messages.reactions.users = files.user ```  ``` messages.user = files.user ``` |
| [remote\_files](#remote-files) | ``` messages.channel_id = remote_files.channels ```  ``` messages.pinned_to = remote_files.channels ```  ``` messages.channel_id = remote_files.pinned_to ```  ``` messages.pinned_to = remote_files.pinned_to ```  ``` messages.bot_profile.team_id = remote_files.source_team ```  ``` messages.team = remote_files.source_team ```  ``` messages.source_team = remote_files.source_team ```  ``` messages.user_team = remote_files.source_team ```  ``` messages.bot_profile.team_id = remote_files.user_team ```  ``` messages.team = remote_files.user_team ```  ``` messages.source_team = remote_files.user_team ```  ``` messages.user_team = remote_files.user_team ```  ``` messages.reply_users = remote_files.user ```  ``` messages.reactions.users = remote_files.user ```  ``` messages.user = remote_files.user ``` |
| [threads](#threads) | ``` messages.channel_id = threads.channel_id ```  ``` messages.pinned_to = threads.channel_id ```  ``` messages.bot_profile.team_id = threads.team ```  ``` messages.team = threads.team ```  ``` messages.source_team = threads.team ```  ``` messages.user_team = threads.team ```  ``` messages.reply_users = threads.user ```  ``` messages.reactions.users = threads.user ```  ``` messages.user = threads.user ```  ``` messages.reply_users = threads.reply_users ```  ``` messages.reactions.users = threads.reply_users ```  ``` messages.user = threads.reply_users ``` |
| [teams](#teams) | ``` messages.bot_profile.team_id = teams.id ```  ``` messages.team = teams.id ```  ``` messages.source_team = teams.id ```  ``` messages.user_team = teams.id ``` |
| [users](#users) | ``` messages.bot_profile.team_id = users.team_id ```  ``` messages.team = users.team_id ```  ``` messages.source_team = users.team_id ```  ``` messages.user_team = users.team_id ```  ``` messages.reply_users = users.id ```  ``` messages.reactions.users = users.id ```  ``` messages.user = users.id ``` |
| [user\_groups](#user-groups) | ``` messages.reply_users = user_groups.members ```  ``` messages.reactions.users = user_groups.members ```  ``` messages.user = user_groups.members ```  ``` messages.reply_users = user_groups.purpose.creator ```  ``` messages.reactions.users = user_groups.purpose.creator ```  ``` messages.user = user_groups.purpose.creator ```  ``` messages.reply_users = user_groups.topic.creator ```  ``` messages.reactions.users = user_groups.topic.creator ```  ``` messages.user = user_groups.topic.creator ``` |

messages table schema

|  |
| --- |
| **blocks**  ARRAY This is a nested data structure:   - type: STRING |
| **bot\_id**  STRING |
| **bot\_profile**  OBJECT This is a nested data structure:   - app\_id: STRING - deleted: BOOLEAN - id: STRING - name: STRING - team\_id: STRING - updated: DATE-TIME |
| **channel\_id**  STRING |
| **client\_msg\_id**  STRING |
| **display\_as\_bot**  BOOLEAN |
| **file\_id**  STRING |
| **file\_ids**  ARRAY This is a nested data structure. |
| **icons**  OBJECT This is a nested data structure:   - emoji: STRING |
| **inviter**  STRING |
| **is\_delayed\_message**  BOOLEAN |
| **is\_intro**  BOOLEAN |
| **is\_starred**  BOOLEAN |
| **last\_read**  DATE-TIME |
| **latest\_reply**  STRING |
| **name**  STRING |
| **old\_name**  STRING |
| **parent\_user\_id**  STRING |
| **permalink**  STRING |
| **pinned\_to**  ARRAY This is a nested data structure. |
| **purpose**  STRING |
| **reactions**  ARRAY This is a nested data structure:   - count: INTEGER - name: STRING - users: ARRAY, which is also a nested data structure. |
| **reply\_count**  INTEGER |
| **reply\_users**  ARRAY This is a nested data structure. |
| **reply\_users\_count**  INTEGER |
| **source\_team**  STRING |
| **subscribed**  BOOLEAN |
| **subtype**  STRING |
| **team**  STRING |
| **text**  STRING |
| **thread\_ts**  STRING |
| **topic**  STRING |
| **ts**  DATE-TIME |
| **type**  STRING |
| **unread\_count**  INTEGER |
| **upload**  BOOLEAN |
| **user**  STRING |
| **user\_team**  STRING |
| **username**  STRING |

### remote\_files

The `remote_files` table contains info about remote files added to Slack.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated |
| **Useful links** | [Slack API method](https://api.slack.com/methods/files.remote.list "Opens in new tab: Slack API method") |

remote\_files table foreign keys

| Join remote\_files with | on |
| --- | --- |
| [channels](#channels) | ``` remote_files.channels = channels.id ```  ``` remote_files.pinned_to = channels.id ```  ``` remote_files.source_team = channels.pending_connected_team_ids ```  ``` remote_files.user_team = channels.pending_connected_team_ids ```  ``` remote_files.user = channels.creator ```  ``` remote_files.user = channels.members ``` |
| [channel\_members](#channel-members) | ``` remote_files.channels = channel_members.channel_id ```  ``` remote_files.pinned_to = channel_members.channel_id ```  ``` remote_files.user = channel_members.user_id ``` |
| [files](#files) | ``` remote_files.channels = files.channels ```  ``` remote_files.pinned_to = files.channels ```  ``` remote_files.channels = files.pinned_to ```  ``` remote_files.pinned_to = files.pinned_to ```  ``` remote_files.groups = files.groups ```  ``` remote_files.source_team = files.source_team ```  ``` remote_files.user_team = files.source_team ```  ``` remote_files.source_team = files.user_team ```  ``` remote_files.user_team = files.user_team ```  ``` remote_files.user = files.user ``` |
| [messages](#messages) | ``` remote_files.channels = messages.channel_id ```  ``` remote_files.pinned_to = messages.channel_id ```  ``` remote_files.channels = messages.pinned_to ```  ``` remote_files.pinned_to = messages.pinned_to ```  ``` remote_files.source_team = messages.bot_profile.team_id ```  ``` remote_files.user_team = messages.bot_profile.team_id ```  ``` remote_files.source_team = messages.team ```  ``` remote_files.user_team = messages.team ```  ``` remote_files.source_team = messages.source_team ```  ``` remote_files.user_team = messages.source_team ```  ``` remote_files.source_team = messages.user_team ```  ``` remote_files.user_team = messages.user_team ```  ``` remote_files.user = messages.reply_users ```  ``` remote_files.user = messages.reactions.users ```  ``` remote_files.user = messages.user ``` |
| [threads](#threads) | ``` remote_files.channels = threads.channel_id ```  ``` remote_files.pinned_to = threads.channel_id ```  ``` remote_files.source_team = threads.team ```  ``` remote_files.user_team = threads.team ```  ``` remote_files.user = threads.user ```  ``` remote_files.user = threads.reply_users ``` |
| [user\_groups](#user-groups) | ``` remote_files.groups = user_groups.id ```  ``` remote_files.groups = user_groups.parent_group ```  ``` remote_files.user = user_groups.members ```  ``` remote_files.user = user_groups.purpose.creator ```  ``` remote_files.user = user_groups.topic.creator ``` |
| [teams](#teams) | ``` remote_files.source_team = teams.id ```  ``` remote_files.user_team = teams.id ``` |
| [users](#users) | ``` remote_files.source_team = users.team_id ```  ``` remote_files.user_team = users.team_id ```  ``` remote_files.user = users.id ``` |

remote\_files table schema

|  |
| --- |
| **channels**  ARRAY This is a nested data structure. |
| **comments\_count**  INTEGER |
| **created**  DATE-TIME |
| **date\_delete**  DATE-TIME |
| **display\_as\_bot**  BOOLEAN |
| **editable**  BOOLEAN |
| **editor**  STRING |
| **external\_id**  STRING |
| **external\_type**  STRING |
| **external\_url**  STRING |
| **filetype**  STRING |
| **groups**  ARRAY This is a nested data structure. |
| **has\_rich\_preview**  BOOLEAN |
| **id**  STRING |
| **image\_exif\_rotation**  INTEGER |
| **ims**  ARRAY This is a nested data structure. |
| **is\_external**  BOOLEAN |
| **is\_public**  BOOLEAN |
| **is\_starred**  BOOLEAN |
| **is\_tombstoned**  BOOLEAN |
| **last\_editor**  STRING |
| **mimetype**  STRING |
| **mode**  STRING |
| **name**  STRING |
| **non\_owner\_editable**  BOOLEAN |
| **num\_stars**  INTEGER |
| **original\_h**  INTEGER |
| **original\_w**  INTEGER |
| **permalink**  STRING |
| **permalink\_public**  STRING |
| **pinned\_info**  OBJECT This is a nested data structure. |
| **pinned\_to**  ARRAY This is a nested data structure. |
| **pretty\_type**  STRING |
| **preview**  STRING |
| **public\_url\_shared**  BOOLEAN |
| **size**  INTEGER |
| **source\_team**  STRING |
| **state**  STRING |
| **thumb\_1024**  STRING |
| **thumb\_1024\_h**  INTEGER |
| **thumb\_1024\_w**  INTEGER |
| **thumb\_160**  STRING |
| **thumb\_360**  STRING |
| **thumb\_360\_h**  INTEGER |
| **thumb\_360\_w**  INTEGER |
| **thumb\_480**  STRING |
| **thumb\_480\_h**  INTEGER |
| **thumb\_480\_w**  INTEGER |
| **thumb\_64**  STRING |
| **thumb\_720**  STRING |
| **thumb\_720\_h**  INTEGER |
| **thumb\_720\_w**  INTEGER |
| **thumb\_80**  STRING |
| **thumb\_800**  STRING |
| **thumb\_800\_h**  INTEGER |
| **thumb\_800\_w**  INTEGER |
| **thumb\_960**  STRING |
| **thumb\_960\_h**  INTEGER |
| **thumb\_960\_w**  INTEGER |
| **thumb\_tiny**  STRING |
| **timestamp**  DATE-TIME |
| **title**  STRING |
| **updated**  DATE-TIME |
| **url\_private**  STRING |
| **url\_private\_download**  STRING |
| **user**  STRING |
| **user\_team**  STRING |
| **username**  STRING |

### teams

The `teams` table contains info about teams in your Slack workspace.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Useful links** | [Slack API method](https://api.slack.com/methods/team.info "Opens in new tab: Slack API method") |

teams table foreign keys

| Join teams with | on |
| --- | --- |
| [channels](#channels) | ``` teams.id = channels.pending_connected_team_ids ``` |
| [files](#files) | ``` teams.id = files.source_team ```  ``` teams.id = files.user_team ``` |
| [messages](#messages) | ``` teams.id = messages.bot_profile.team_id ```  ``` teams.id = messages.team ```  ``` teams.id = messages.source_team ```  ``` teams.id = messages.user_team ``` |
| [remote\_files](#remote-files) | ``` teams.id = remote_files.source_team ```  ``` teams.id = remote_files.user_team ``` |
| [threads](#threads) | ``` teams.id = threads.team ``` |
| [users](#users) | ``` teams.id = users.team_id ``` |

teams table schema

|  |
| --- |
| **archived**  BOOLEAN |
| **avatar\_base\_url**  STRING |
| **created**  DATE-TIME |
| **date\_create**  DATE-TIME |
| **deleted**  DATE-TIME |
| **description**  STRING |
| **discoverable**  STRING |
| **domain**  STRING |
| **email\_domain**  STRING |
| **enterprise\_id**  STRING |
| **enterprise\_name**  STRING |
| **has\_compliance\_export**  BOOLEAN |
| **icon**  OBJECT This is a nested data structure:   - image\_102: STRING - image\_132: STRING - image\_230: STRING - image\_34: STRING - image\_44: STRING - image\_68: STRING - image\_88: STRING - image\_default: BOOLEAN |
| **id**  STRING |
| **is\_assigned**  BOOLEAN |
| **is\_enterprise**  INTEGER |
| **messages\_count**  INTEGER |
| **msg\_edit\_window\_mins**  INTEGER |
| **name**  STRING |
| **over\_integrations\_limit**  BOOLEAN |
| **over\_storage\_limit**  BOOLEAN |
| **plan**  STRING |

### threads

The `threads` table contains info about conversation threads in your Slack team.

Information noteWhile this table uses Full Table, it’s not truly replicated in full during each replication job. Each time a message in a thread is updated, the entire thread and all the messages it contains will be replicated in full. This means that while only updated threads are replicated, they are replicated in full whenever they’re updated.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | channel\_id  thread\_ts |
| **Useful links** | [Slack documentation](https://api.slack.com/Content/conversations-api)  [Slack API method](https://api.slack.com/methods/conversations.replies "Opens in new tab: Slack API method") |

threads table foreign keys

| Join threads with | on |
| --- | --- |
| [channels](#channels) | ``` threads.channel_id = channels.id ```  ``` threads.team = channels.pending_connected_team_ids ```  ``` threads.user = channels.creator ```  ``` threads.reply_users = channels.creator ```  ``` threads.user = channels.members ```  ``` threads.reply_users = channels.members ``` |
| [channel\_members](#channel-members) | ``` threads.channel_id = channel_members.channel_id ```  ``` threads.user = channel_members.user_id ```  ``` threads.reply_users = channel_members.user_id ``` |
| [files](#files) | ``` threads.channel_id = files.channels ```  ``` threads.channel_id = files.pinned_to ```  ``` threads.team = files.source_team ```  ``` threads.team = files.user_team ```  ``` threads.user = files.user ```  ``` threads.reply_users = files.user ``` |
| [messages](#messages) | ``` threads.channel_id = messages.channel_id ```  ``` threads.channel_id = messages.pinned_to ```  ``` threads.team = messages.bot_profile.team_id ```  ``` threads.team = messages.team ```  ``` threads.team = messages.source_team ```  ``` threads.team = messages.user_team ```  ``` threads.user = messages.reply_users ```  ``` threads.reply_users = messages.reply_users ```  ``` threads.user = messages.reactions.users ```  ``` threads.reply_users = messages.reactions.users ```  ``` threads.user = messages.user ```  ``` threads.reply_users = messages.user ``` |
| [remote\_files](#remote-files) | ``` threads.channel_id = remote_files.channels ```  ``` threads.channel_id = remote_files.pinned_to ```  ``` threads.team = remote_files.source_team ```  ``` threads.team = remote_files.user_team ```  ``` threads.user = remote_files.user ```  ``` threads.reply_users = remote_files.user ``` |
| [teams](#teams) | ``` threads.team = teams.id ``` |
| [users](#users) | ``` threads.team = users.team_id ```  ``` threads.user = users.id ```  ``` threads.reply_users = users.id ``` |
| [user\_groups](#user-groups) | ``` threads.user = user_groups.members ```  ``` threads.reply_users = user_groups.members ```  ``` threads.user = user_groups.purpose.creator ```  ``` threads.reply_users = user_groups.purpose.creator ```  ``` threads.user = user_groups.topic.creator ```  ``` threads.reply_users = user_groups.topic.creator ``` |

threads table schema

|  |
| --- |
| **blocks**  ARRAY This is a nested data structure:   - type: STRING |
| **channel\_id**  STRING |
| **client\_msg\_id**  STRING |
| **latest\_reply**  STRING |
| **reply\_count**  INTEGER |
| **reply\_users**  ARRAY This is a nested data structure. |
| **reply\_users\_count**  NUMBER |
| **subscribed**  BOOLEAN |
| **team**  STRING |
| **text**  STRING |
| **thread\_ts**  STRING |
| **ts**  DATE-TIME |
| **type**  STRING |
| **user**  STRING |

### user\_groups

The `user_groups` table contains info about user groups from your Slack team.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Slack API method](https://api.slack.com/methods/usergroups.list "Opens in new tab: Slack API method") |

user\_groups table foreign keys

| Join user\_groups with | on |
| --- | --- |
| [files](#files) | ``` user_groups.id = files.groups ```  ``` user_groups.parent_group = files.groups ```  ``` user_groups.members = files.user ```  ``` user_groups.purpose.creator = files.user ```  ``` user_groups.topic.creator = files.user ``` |
| [remote\_files](#remote-files) | ``` user_groups.id = remote_files.groups ```  ``` user_groups.parent_group = remote_files.groups ```  ``` user_groups.members = remote_files.user ```  ``` user_groups.purpose.creator = remote_files.user ```  ``` user_groups.topic.creator = remote_files.user ``` |
| [channel\_members](#channel-members) | ``` user_groups.members = channel_members.user_id ```  ``` user_groups.purpose.creator = channel_members.user_id ```  ``` user_groups.topic.creator = channel_members.user_id ``` |
| [channels](#channels) | ``` user_groups.members = channels.creator ```  ``` user_groups.purpose.creator = channels.creator ```  ``` user_groups.topic.creator = channels.creator ```  ``` user_groups.members = channels.members ```  ``` user_groups.purpose.creator = channels.members ```  ``` user_groups.topic.creator = channels.members ``` |
| [messages](#messages) | ``` user_groups.members = messages.reply_users ```  ``` user_groups.purpose.creator = messages.reply_users ```  ``` user_groups.topic.creator = messages.reply_users ```  ``` user_groups.members = messages.reactions.users ```  ``` user_groups.purpose.creator = messages.reactions.users ```  ``` user_groups.topic.creator = messages.reactions.users ```  ``` user_groups.members = messages.user ```  ``` user_groups.purpose.creator = messages.user ```  ``` user_groups.topic.creator = messages.user ``` |
| [threads](#threads) | ``` user_groups.members = threads.user ```  ``` user_groups.purpose.creator = threads.user ```  ``` user_groups.topic.creator = threads.user ```  ``` user_groups.members = threads.reply_users ```  ``` user_groups.purpose.creator = threads.reply_users ```  ``` user_groups.topic.creator = threads.reply_users ``` |
| [users](#users) | ``` user_groups.members = users.id ```  ``` user_groups.purpose.creator = users.id ```  ``` user_groups.topic.creator = users.id ``` |

user\_groups table schema

|  |
| --- |
| **created**  DATE-TIME |
| **creator**  STRING |
| **id**  STRING |
| **is\_archived**  BOOLEAN |
| **is\_deleted**  BOOLEAN |
| **is\_group**  BOOLEAN |
| **is\_moved**  INTEGER |
| **is\_mpim**  BOOLEAN |
| **is\_open**  BOOLEAN |
| **is\_pending\_ext\_shared**  BOOLEAN |
| **is\_read\_only**  BOOLEAN |
| **is\_thread\_only**  BOOLEAN |
| **last\_read**  DATE-TIME |
| **members**  ARRAY This is a nested data structure. |
| **name**  STRING |
| **name\_normalized**  STRING |
| **num\_members**  INTEGER |
| **parent\_group**  STRING |
| **priority**  NUMBER |
| **purpose**  OBJECT This is a nested data structure:   - creator: STRING - last\_set: INTEGER - value: STRING |
| **topic**  OBJECT This is a nested data structure:   - creator: STRING - last\_set: INTEGER - value: STRING |
| **unread\_count**  INTEGER |
| **unread\_count\_display**  INTEGER |

### users

The `users` table lists contains info about the users in your Slack team. This includes deactivated and deleted users.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated |
| **Useful links** | [Slack API method](https://api.slack.com/methods/users.list "Opens in new tab: Slack API method") |

users table foreign keys

| Join users with | on |
| --- | --- |
| [channels](#channels) | ``` users.team_id = channels.pending_connected_team_ids ```  ``` users.id = channels.creator ```  ``` users.id = channels.members ``` |
| [files](#files) | ``` users.team_id = files.source_team ```  ``` users.team_id = files.user_team ```  ``` users.id = files.user ``` |
| [messages](#messages) | ``` users.team_id = messages.bot_profile.team_id ```  ``` users.team_id = messages.team ```  ``` users.team_id = messages.source_team ```  ``` users.team_id = messages.user_team ```  ``` users.id = messages.reply_users ```  ``` users.id = messages.reactions.users ```  ``` users.id = messages.user ``` |
| [remote\_files](#remote-files) | ``` users.team_id = remote_files.source_team ```  ``` users.team_id = remote_files.user_team ```  ``` users.id = remote_files.user ``` |
| [teams](#teams) | ``` users.team_id = teams.id ``` |
| [threads](#threads) | ``` users.team_id = threads.team ```  ``` users.id = threads.user ```  ``` users.id = threads.reply_users ``` |
| [channel\_members](#channel-members) | ``` users.id = channel_members.user_id ``` |
| [user\_groups](#user-groups) | ``` users.id = user_groups.members ```  ``` users.id = user_groups.purpose.creator ```  ``` users.id = user_groups.topic.creator ``` |

users table schema

|  |
| --- |
| **color**  STRING |
| **deleted**  BOOLEAN |
| **has\_2fa**  BOOLEAN |
| **id**  STRING |
| **is\_admin**  BOOLEAN |
| **is\_app\_user**  BOOLEAN |
| **is\_bot**  BOOLEAN |
| **is\_owner**  BOOLEAN |
| **is\_primary\_owner**  BOOLEAN |
| **is\_restricted**  BOOLEAN |
| **is\_ultra\_restricted**  BOOLEAN |
| **name**  STRING |
| **profile**  OBJECT This is a nested data structure:   - email: STRING |
| **real\_name**  STRING |
| **team\_id**  STRING |
| **tz**  STRING |
| **tz\_label**  STRING |
| **tz\_offset**  INTEGER |
| **updated**  DATE-TIME |
