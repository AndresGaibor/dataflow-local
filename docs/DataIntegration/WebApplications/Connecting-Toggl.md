---
title: "Toggl"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Toggl.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Toggl

Toggl is a cloud-based time-tracking platform.

Toggl integration replicates data using the [Toggl API v8](https://github.com/toggl/toggl_api_docs/blob/master/toggl_api.md).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To set up your Toggl account, you need:

- Your Toggl API token is specific to your user. When replicating data, Qlik Talend Cloud is only able to access the same data as your user in Toggl.
- To replicate time entry data from multiple workspaces, you must be an Admin in the workspace from which you want to replicate data. Verify that you have this permission in Toggl before proceeding.

To retrieve your API token:

1. Log into your [Toggl](https://accounts.toggl.com/track/login/) account.
2. Click the Workspace menu in the lower left corner.
3. Click Profile settings.
4. Locate the API token field.
5. Copy the API token.

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
| Trailing Days | Enter the number of days to be used as an attribution window when replicating time entry data. This is only applicable to the `time_entries` table.  If the value is 5, Toggle replicates the past five days’ worth of data for the `time_entries` table during every replication job. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### clients

The `clients` table contains info about the clients in your Toggl account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | at |
| **Useful links** | [Toggl documentation](https://github.com/toggl/toggl_api_docs/blob/master/chapters/clients.md)  [Toggl API method](https://github.com/toggl/toggl_api_docs/blob/master/chapters/workspaces.md#get-workspace-clients "Opens in new tab: Toggl API method") |

clients table foreign keys

| Join clients with | on |
| --- | --- |
| [workspaces](#workspaces) | ``` clients.wid = workspaces.id ``` |
| [groups](#groups) | ``` clients.wid = groups.wid ``` |
| [projects](#projects) | ``` clients.wid = projects.wid ```  ``` clients.id = projects.cid ``` |
| [tags](#tags) | ``` clients.wid = tags.wid ``` |
| [tasks](#tasks) | ``` clients.wid = tasks.wid ``` |
| [users](#users) | ``` clients.wid = users.default_wid ``` |
| [workspace\_users](#workspace-users) | ``` clients.wid = workspace_users.wid ``` |

clients table schema

|  |
| --- |
| **at**  DATE-TIME |
| **cur**  STRING |
| **hrate**  INTEGER |
| **id**  INTEGER |
| **name**  STRING |
| **notes**  STRING |
| **wid**  INTEGER |

### groups

The `groups` table contains info about the groups in your Toggl account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | at |
| **Useful links** | [Toggl documentation](https://github.com/toggl/toggl_api_docs/blob/master/chapters/groups.md)  [Toggl API method](https://github.com/toggl/toggl_api_docs/blob/master/chapters/workspaces.md#get-workspace-groups "Opens in new tab: Toggl API method") |

groups table foreign keys

| Join groups with | on |
| --- | --- |
| [workspaces](#workspaces) | ``` groups.wid = workspaces.id ``` |
| [clients](#clients) | ``` groups.wid = clients.wid ``` |
| [projects](#projects) | ``` groups.wid = projects.wid ``` |
| [tags](#tags) | ``` groups.wid = tags.wid ``` |
| [tasks](#tasks) | ``` groups.wid = tasks.wid ``` |
| [users](#users) | ``` groups.wid = users.default_wid ``` |
| [workspace\_users](#workspace-users) | ``` groups.wid = workspace_users.wid ``` |

groups table schema

|  |
| --- |
| **at**  DATE-TIME |
| **id**  INTEGER |
| **name**  STRING |
| **wid**  INTEGER |

### projects

The `projects` table contains info about the projects in your Toggl account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | at |
| **Useful links** | [Toggl documentation](https://github.com/toggl/toggl_api_docs/blob/master/chapters/projects.md)  [Toggl API method](https://github.com/toggl/toggl_api_docs/blob/master/chapters/workspaces.md#get-workspace-projects "Opens in new tab: Toggl API method") |

projects table foreign keys

| Join projects with | on |
| --- | --- |
| [workspaces](#workspaces) | ``` projects.wid = workspaces.id ``` |
| [clients](#clients) | ``` projects.wid = clients.wid ```  ``` projects.cid = clients.id ``` |
| [groups](#groups) | ``` projects.wid = groups.wid ``` |
| [tags](#tags) | ``` projects.wid = tags.wid ``` |
| [tasks](#tasks) | ``` projects.wid = tasks.wid ``` |
| [users](#users) | ``` projects.wid = users.default_wid ``` |
| [workspace\_users](#workspace-users) | ``` projects.wid = workspace_users.wid ``` |

projects table schema

|  |
| --- |
| **active**  BOOLEAN |
| **at**  DATE-TIME |
| **billable**  BOOLEAN |
| **cid**  INTEGER |
| **id**  INTEGER |
| **is\_private**  BOOLEAN |
| **name**  STRING |
| **wid**  INTEGER |

### tags

The `tags` table contains info about the tags in your Toggl account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Toggl documentation](https://github.com/toggl/toggl_api_docs/blob/master/chapters/tags.md)  [Toggl API method](https://github.com/toggl/toggl_api_docs/blob/master/chapters/workspaces.md#get-workspace-tags "Opens in new tab: Toggl API method") |

tags table foreign keys

| Join tags with | on |
| --- | --- |
| [workspaces](#workspaces) | ``` tags.wid = workspaces.id ``` |
| [clients](#clients) | ``` tags.wid = clients.wid ``` |
| [groups](#groups) | ``` tags.wid = groups.wid ``` |
| [projects](#projects) | ``` tags.wid = projects.wid ``` |
| [tasks](#tasks) | ``` tags.wid = tasks.wid ``` |
| [users](#users) | ``` tags.wid = users.default_wid ``` |
| [workspace\_users](#workspace-users) | ``` tags.wid = workspace_users.wid ``` |

tags table schema

|  |
| --- |
| **id**  INTEGER |
| **name**  STRING |
| **wid**  INTEGER |

### tasks

The `tasks` table contains info about the tasks in your Toggl account.

**Note**: Tasks are only available for Toggl starter and other paid workspaces.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | at |
| **Useful links** | [Toggl documentation](https://github.com/toggl/toggl_api_docs/blob/master/chapters/tasks.md)  [Toggl API method](https://github.com/toggl/toggl_api_docs/blob/master/chapters/workspaces.md#get-workspace-tasks "Opens in new tab: Toggl API method") |

tasks table foreign keys

| Join tasks with | on |
| --- | --- |
| [workspaces](#workspaces) | ``` tasks.wid = workspaces.id ``` |
| [clients](#clients) | ``` tasks.wid = clients.wid ``` |
| [groups](#groups) | ``` tasks.wid = groups.wid ``` |
| [projects](#projects) | ``` tasks.wid = projects.wid ``` |
| [tags](#tags) | ``` tasks.wid = tags.wid ``` |
| [users](#users) | ``` tasks.wid = users.default_wid ```  ``` tasks.uid = users.id ``` |
| [workspace\_users](#workspace-users) | ``` tasks.wid = workspace_users.wid ``` |
| [time\_entries](#time-entries) | ``` tasks.id = time_entries.tid ```  ``` tasks.uid = time_entries.uid ``` |

tasks table schema

|  |
| --- |
| **active**  BOOLEAN |
| **at**  DATE-TIME |
| **estimated\_seconds**  INTEGER |
| **id**  INTEGER |
| **name**  STRING |
| **pid**  INTEGER |
| **uid**  INTEGER |
| **wid**  INTEGER |

### time\_entries

The `time_entries` table contains info about time entries. **Note**: This table uses an attribution window to replicate data. Refer to the [Replicating time entry data](#replicating-time-entry-data) section for more info.

#### Time entries and user permissions

The time entries Stitch replicates are dependent upon the user whose API token is used to create the integration in Stitch. Stitch is only able to access the same data as the user whose token is used.

For example: If the user is unable to access a workspace, or is not an Admin in that workspace, Stitch will not be able to replicate time entry data for those workspaces. In this case, only the user’s own time entries will be accessible by Stitch.

If data from a workspace is missing, verify that the user whose API token is being used in Stitch has Admin permissions in that workspace.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated |
| **Useful links** | [Toggl API method](https://github.com/toggl/toggl_api_docs/blob/master/reports/detailed.md "Opens in new tab: Toggl API method") |

time\_entries table foreign keys

| Join time\_entries with | on |
| --- | --- |
| [tasks](#tasks) | ``` time_entries.tid = tasks.id ```  ``` time_entries.uid = tasks.uid ``` |
| [users](#users) | ``` time_entries.uid = users.id ``` |

time\_entries table schema

|  |
| --- |
| **billable**  NUMBER |
| **client**  STRING |
| **cur**  STRING |
| **description**  STRING |
| **dur**  INTEGER |
| **end**  DATE-TIME |
| **id**  INTEGER |
| **is\_billable**  BOOLEAN |
| **pid**  INTEGER |
| **project**  STRING |
| **start**  DATE-TIME |
| **tags**  ARRAY |
| **task**  STRING |
| **tid**  INTEGER |
| **uid**  INTEGER |
| **updated**  DATE-TIME |
| **use\_stop**  BOOLEAN |
| **user**  STRING |

### users

The `users` table contains info about the users in your Toggl account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | at |
| **Useful links** | [Toggl documentation](https://github.com/toggl/toggl_api_docs/blob/master/chapters/users.md)  [Toggl API method](https://github.com/toggl/toggl_api_docs/blob/master/chapters/workspaces.md#get-workspace-users "Opens in new tab: Toggl API method") |

users table foreign keys

| Join users with | on |
| --- | --- |
| [workspaces](#workspaces) | ``` users.default_wid = workspaces.id ``` |
| [clients](#clients) | ``` users.default_wid = clients.wid ``` |
| [groups](#groups) | ``` users.default_wid = groups.wid ``` |
| [projects](#projects) | ``` users.default_wid = projects.wid ``` |
| [tags](#tags) | ``` users.default_wid = tags.wid ``` |
| [tasks](#tasks) | ``` users.default_wid = tasks.wid ```  ``` users.id = tasks.uid ``` |
| [workspace\_users](#workspace-users) | ``` users.default_wid = workspace_users.wid ``` |
| [time\_entries](#time-entries) | ``` users.id = time_entries.uid ``` |

users table schema

|  |
| --- |
| **at**  DATE-TIME |
| **beginning\_of\_week**  INTEGER |
| **date\_format**  STRING |
| **default\_wid**  INTEGER |
| **email**  STRING |
| **fullname**  STRING |
| **id**  INTEGER |
| **image\_url**  STRING |
| **invitation**  STRING |
| **jquery\_date\_format**  STRING |
| **jquery\_timeofday\_format**  STRING |
| **language**  STRING |
| **new\_blog\_post**  STRING |
| **record\_timeline**  BOOLEAN |
| **render\_timeline**  BOOLEAN |
| **retention**  INTEGER |
| **should\_upgrade**  BOOLEAN |
| **sidebar\_piechart**  BOOLEAN |
| **store\_start\_and\_stop\_time**  BOOLEAN |
| **timeline\_enabled**  BOOLEAN |
| **timeline\_experiment**  BOOLEAN |
| **timeofday\_format**  STRING |

### workspace\_users

The `workspace_users` table contains info about the users in a workspace.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | at |
| **Useful links** | [Toggl documentation](https://github.com/toggl/toggl_api_docs/blob/master/chapters/workspace_users.md)  [Toggl API method](https://github.com/toggl/toggl_api_docs/blob/master/chapters/workspace_users.md#get-workspace-users "Opens in new tab: Toggl API method") |

workspace\_users table foreign keys

| Join workspace\_users with | on |
| --- | --- |
| [workspaces](#workspaces) | ``` workspace_users.wid = workspaces.id ``` |
| [clients](#clients) | ``` workspace_users.wid = clients.wid ``` |
| [groups](#groups) | ``` workspace_users.wid = groups.wid ``` |
| [projects](#projects) | ``` workspace_users.wid = projects.wid ``` |
| [tags](#tags) | ``` workspace_users.wid = tags.wid ``` |
| [tasks](#tasks) | ``` workspace_users.wid = tasks.wid ``` |
| [users](#users) | ``` workspace_users.wid = users.default_wid ``` |

workspace\_users table schema

|  |
| --- |
| **active**  BOOLEAN |
| **admin**  BOOLEAN |
| **at**  DATE-TIME |
| **email**  STRING |
| **id**  INTEGER |
| **invite\_url**  STRING |
| **name**  STRING |
| **uid**  INTEGER |
| **wid**  INTEGER |

### workspaces

The `workspaces` table contains info about the workspaces in your Toggl account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | at |
| **Useful links** | [Toggl documentation](https://github.com/toggl/toggl_api_docs/blob/master/chapters/workspaces.md)  [Toggl API method](https://github.com/toggl/toggl_api_docs/blob/master/chapters/workspaces.md#get-workspaces "Opens in new tab: Toggl API method") |

workspaces table foreign keys

| Join workspaces with | on |
| --- | --- |
| [clients](#clients) | ``` workspaces.id = clients.wid ``` |
| [groups](#groups) | ``` workspaces.id = groups.wid ``` |
| [projects](#projects) | ``` workspaces.id = projects.wid ``` |
| [tags](#tags) | ``` workspaces.id = tags.wid ``` |
| [tasks](#tasks) | ``` workspaces.id = tasks.wid ``` |
| [users](#users) | ``` workspaces.id = users.default_wid ``` |
| [workspace\_users](#workspace-users) | ``` workspaces.id = workspace_users.wid ``` |

workspaces table schema

|  |
| --- |
| **admin**  BOOLEAN |
| **at**  DATE-TIME |
| **default\_currency**  STRING |
| **default\_hourly\_rate**  INTEGER |
| **id**  INTEGER |
| **logo\_url**  STRING |
| **name**  STRING |
| **only\_admins\_may\_create\_projects**  BOOLEAN |
| **only\_admins\_see\_billable\_rates**  BOOLEAN |
| **premium**  BOOLEAN |
| **rounding**  INTEGER |
| **rounding\_minutes**  INTEGER |
