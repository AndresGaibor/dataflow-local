---
title: "Asana"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Asana-v2.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Asana

Asana is a team communication manager.

Asana integration replicates data using the [Asana API](https://asana.com/developers/documentation/examples-tutorials/overview).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To retrieve your client ID and secret:

1. Log into your [Asana](https://app.asana.com/-/login?u=%2F0%2Fmy-apps) account.
2. In the My apps section, click Create new app.
3. Complete the required information, then click Create app.
4. Select the OAuth tab.
5. Make sure Redirect URLs is set to https://connector.qlik.com/auth/oauth/v3.htm.
6. In the Permission scopes section, select Full permissions.
7. Select the Manage distribution tab.
8. Click Add workspace.
9. From the dropdown menu, select the workspace you want to replicate data from, then click Add.
10. In the OAuth section, copy and paste your client secret and client ID into a secured file.

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
| Client ID | Client ID. |
| Client Secret | Client secret. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### portfolios

The `portfolios` table contains info about the portfolios in your Asana account.

#### Custom fields

To replicate task custom fields, select the `custom_fields` attribute in Stitch. If your destination doesn’t natively support nested data structures, two subtables (`tasks__custom_fields`, `tasks__custom_fields__enum_options`) will be created.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | gid |
| **Useful links** | [Asana documentation](https://developers.asana.com/Content/portfolios)  [Asana API method](https://developers.asana.com/Content/get-multiple-portfolios "Opens in new tab: Asana API method") |

portfolios table foreign keys

| Join portfolios with | on |
| --- | --- |
| [projects](#projects) | ``` portfolios.created_by.gid = projects.followers.gid ```  ``` portfolios.members.gid = projects.followers.gid ```  ``` portfolios.owner.gid = projects.followers.gid ```  ``` portfolios.created_by.gid = projects.members.gid ```  ``` portfolios.members.gid = projects.members.gid ```  ``` portfolios.owner.gid = projects.members.gid ```  ``` portfolios.created_by.gid = projects.owner.gid ```  ``` portfolios.members.gid = projects.owner.gid ```  ``` portfolios.owner.gid = projects.owner.gid ```  ``` portfolios.workspace.gid = projects.workspace.gid ``` |
| [tags](#tags) | ``` portfolios.created_by.gid = tags.followers.gid ```  ``` portfolios.members.gid = tags.followers.gid ```  ``` portfolios.owner.gid = tags.followers.gid ```  ``` portfolios.workspace.gid = tags.workspace.gid ``` |
| [tasks](#tasks) | ``` portfolios.created_by.gid = tasks.assignee.gid ```  ``` portfolios.members.gid = tasks.assignee.gid ```  ``` portfolios.owner.gid = tasks.assignee.gid ```  ``` portfolios.created_by.gid = tasks.followers.gid ```  ``` portfolios.members.gid = tasks.followers.gid ```  ``` portfolios.owner.gid = tasks.followers.gid ```  ``` portfolios.workspace.gid = tasks.workspace.gid ``` |
| [users](#users) | ``` portfolios.created_by.gid = users.gid ```  ``` portfolios.members.gid = users.gid ```  ``` portfolios.owner.gid = users.gid ```  ``` portfolios.workspace.gid = users.workspaces.gid ``` |
| [stories](#stories) | ``` portfolios.created_by.gid = stories.assignee.gid ```  ``` portfolios.members.gid = stories.assignee.gid ```  ``` portfolios.owner.gid = stories.assignee.gid ```  ``` portfolios.created_by.gid = stories.created_by.gid ```  ``` portfolios.members.gid = stories.created_by.gid ```  ``` portfolios.owner.gid = stories.created_by.gid ```  ``` portfolios.created_by.gid = stories.dependency.gid ```  ``` portfolios.members.gid = stories.dependency.gid ```  ``` portfolios.owner.gid = stories.dependency.gid ``` |
| [teams](#teams) | ``` portfolios.created_by.gid = teams.users.gid ```  ``` portfolios.members.gid = teams.users.gid ```  ``` portfolios.owner.gid = teams.users.gid ```  ``` portfolios.workspace.gid = teams.organization.gid ``` |
| [workspaces](#workspaces) | ``` portfolios.workspace.gid = workspaces.gid ``` |

portfolios table schema

|  |
| --- |
| **color**  STRING |
| **created\_at**  DATE-TIME |
| **created\_by**  OBJECT This is a nested data structure:   - gid: STRING - name: STRING - resource\_type: STRING |
| **current\_status\_update**  OBJECT \* This is a nested data structure:   - gid: STRING - resource\_subtype: STRING - resource\_type: STRING - title: STRING |
| **custom\_field\_settings**  ARRAY This is a nested data structure:   - custom\_field: OBJECT, which is also a nested data structure.   - created\_by: OBJECT, which is also a nested data structure.     - gid: STRING     - name: STRING     - resource\_type: STRING   - currency\_code: STRING   - custom\_label: STRING   - custom\_label\_position: STRING   - date\_value: OBJECT, which is also a nested data structure.     - date: STRING     - date\_time: DATE-TIME   - description: STRING   - display\_value: STRING   - enabled: BOOLEAN   - enum\_options: ARRAY, which is also a nested data structure.     - color: STRING     - enabled: BOOLEAN     - gid: STRING     - name: STRING     - resource\_type: STRING   - enum\_value: OBJECT, which is also a nested data structure.     - color: STRING     - enabled: BOOLEAN     - gid: STRING     - name: STRING     - resource\_type: STRING   - format: STRING   - gid: STRING   - has\_notifications\_enabled: BOOLEAN   - is\_global\_to\_workspace: BOOLEAN   - multi\_enum\_values: ARRAY, which is also a nested data structure.     - color: STRING     - enabled: BOOLEAN     - gid: STRING     - name: STRING     - resource\_type: STRING   - name: STRING   - number\_value: NUMBER   - people\_value: ARRAY, which is also a nested data structure.     - gid: STRING     - name: STRING     - resource\_type: STRING   - precision: INTEGER   - resource\_subtype: STRING   - resource\_type: STRING   - text\_value: STRING   - type: STRING - gid: STRING - is\_important: BOOLEAN - parent: OBJECT, which is also a nested data structure.   - gid: STRING   - name: STRING   - resource\_type: STRING - project: OBJECT, which is also a nested data structure.   - gid: STRING   - name: STRING   - resource\_type: STRING - resource\_type: STRING |
| **custom\_fields**  ARRAY This is a nested data structure:   - date\_value: OBJECT, which is also a nested data structure.   - date: STRING   - date\_time: DATE-TIME - display\_value: STRING - enabled: BOOLEAN - enum\_options: ARRAY, which is also a nested data structure.   - color: STRING   - enabled: BOOLEAN   - gid: STRING   - name: STRING   - resource\_type: STRING - enum\_value: OBJECT, which is also a nested data structure.   - color: STRING   - enabled: BOOLEAN   - gid: STRING   - name: STRING   - resource\_type: STRING - gid: STRING - multi\_enum\_values: ARRAY, which is also a nested data structure.   - color: STRING   - enabled: BOOLEAN   - gid: STRING   - name: STRING   - resource\_type: STRING - name: STRING - number\_value: NUMBER - resource\_subtype: STRING - resource\_type: STRING - text\_value: STRING - type: STRING |
| **due\_on**  STRING |
| **gid**  STRING |
| **is\_template**  BOOLEAN |
| **members**  ARRAY This is a nested data structure:   - gid: STRING - name: STRING - resource\_type: STRING |
| **name**  STRING |
| **owner**  OBJECT This is a nested data structure:   - gid: STRING - name: STRING - resource\_type: STRING |
| **permalink\_url**  STRING |
| **portfolio\_items**  ARRAY This is a nested data structure:   - gid: STRING - name: STRING - resource\_type: STRING |
| **public**  BOOLEAN |
| **resource\_type**  STRING |
| **start\_on**  STRING |
| **workspace**  OBJECT This is a nested data structure:   - gid: STRING - name: STRING - resource\_type: STRING |

### projects

The `projects` table contains info about the projects the user who authorized the Asana integration in Stitch has access to.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | gid |
| **Replication Key** | modified\_at |
| **Useful links** | [Asana documentation](https://asana.com/developers/api-reference/projects) |

projects table foreign keys

| Join projects with | on |
| --- | --- |
| [tasks](#tasks) | ``` projects.gid = tasks.projects.gid ```  ``` projects.followers.gid = tasks.assignee.gid ```  ``` projects.members.gid = tasks.assignee.gid ```  ``` projects.owner.gid = tasks.assignee.gid ```  ``` projects.followers.gid = tasks.followers.gid ```  ``` projects.members.gid = tasks.followers.gid ```  ``` projects.owner.gid = tasks.followers.gid ```  ``` projects.workspace.gid = tasks.workspace.gid ``` |
| [stories](#stories) | ``` projects.gid = stories.project.gid ```  ``` projects.followers.gid = stories.assignee.gid ```  ``` projects.members.gid = stories.assignee.gid ```  ``` projects.owner.gid = stories.assignee.gid ```  ``` projects.followers.gid = stories.created_by.gid ```  ``` projects.members.gid = stories.created_by.gid ```  ``` projects.owner.gid = stories.created_by.gid ```  ``` projects.followers.gid = stories.dependency.gid ```  ``` projects.members.gid = stories.dependency.gid ```  ``` projects.owner.gid = stories.dependency.gid ``` |
| [sections](#sections) | ``` projects.gid = sections.project.gid ```  ``` projects.gid = sections.projects.gid ``` |
| [tags](#tags) | ``` projects.followers.gid = tags.followers.gid ```  ``` projects.members.gid = tags.followers.gid ```  ``` projects.owner.gid = tags.followers.gid ```  ``` projects.workspace.gid = tags.workspace.gid ``` |
| [users](#users) | ``` projects.followers.gid = users.gid ```  ``` projects.members.gid = users.gid ```  ``` projects.owner.gid = users.gid ```  ``` projects.workspace.gid = users.workspaces.gid ``` |
| [portfolios](#portfolios) | ``` projects.followers.gid = portfolios.created_by.gid ```  ``` projects.members.gid = portfolios.created_by.gid ```  ``` projects.owner.gid = portfolios.created_by.gid ```  ``` projects.followers.gid = portfolios.members.gid ```  ``` projects.members.gid = portfolios.members.gid ```  ``` projects.owner.gid = portfolios.members.gid ```  ``` projects.followers.gid = portfolios.owner.gid ```  ``` projects.members.gid = portfolios.owner.gid ```  ``` projects.owner.gid = portfolios.owner.gid ```  ``` projects.workspace.gid = portfolios.workspace.gid ``` |
| [teams](#teams) | ``` projects.followers.gid = teams.users.gid ```  ``` projects.members.gid = teams.users.gid ```  ``` projects.owner.gid = teams.users.gid ```  ``` projects.workspace.gid = teams.organization.gid ``` |
| [workspaces](#workspaces) | ``` projects.workspace.gid = workspaces.gid ``` |

projects table schema

|  |
| --- |
| **archived**  BOOLEAN |
| **color**  STRING |
| **completed**  BOOLEAN |
| **completed\_at**  DATE-TIME |
| **completed\_by**  OBJECT This is a nested data structure:   - gid: STRING - name: STRING - resource\_type: STRING |
| **created\_at**  DATE-TIME |
| **created\_from\_template**  OBJECT This is a nested data structure:   - gid: STRING - name: STRING - resource\_type: STRING |
| **current\_status**  STRING |
| **current\_status\_update**  OBJECT This is a nested data structure:   - gid: STRING - resource\_subtype: STRING - resource\_type: STRING - title: STRING |
| **custom\_field\_settings**  ARRAY This is a nested data structure:   - custom\_field: OBJECT, which is also a nested data structure.   - created\_by: OBJECT, which is also a nested data structure.     - gid: STRING     - name: STRING     - resource\_type: STRING   - currency\_code: STRING   - custom\_label: STRING   - custom\_label\_position: STRING   - date\_value: OBJECT, which is also a nested data structure.     - date: STRING     - date\_time: DATE-TIME   - description: STRING   - display\_value: STRING   - enabled: BOOLEAN   - enum\_options: ARRAY, which is also a nested data structure.     - color: STRING     - enabled: BOOLEAN     - gid: STRING     - name: STRING     - resource\_type: STRING   - enum\_value: OBJECT, which is also a nested data structure.     - color: STRING     - enabled: BOOLEAN     - gid: STRING     - name: STRING     - resource\_type: STRING   - format: STRING   - gid: STRING   - has\_notifications\_enabled: BOOLEAN   - is\_global\_to\_workspace: BOOLEAN   - multi\_enum\_values: ARRAY, which is also a nested data structure.     - color: STRING     - enabled: BOOLEAN     - gid: STRING     - name: STRING     - resource\_type: STRING   - name: STRING   - number\_value: NUMBER   - people\_value: ARRAY, which is also a nested data structure.     - gid: STRING     - name: STRING     - resource\_type: STRING   - precision: INTEGER   - resource\_subtype: STRING   - resource\_type: STRING   - text\_value: STRING   - type: STRING - gid: STRING - is\_important: BOOLEAN - parent: OBJECT, which is also a nested data structure.   - gid: STRING   - name: STRING   - resource\_type: STRING - project: OBJECT, which is also a nested data structure.   - gid: STRING   - name: STRING   - resource\_type: STRING - resource\_type: STRING |
| **custom\_fields**  ARRAY This is a nested data structure:   - date\_value: OBJECT, which is also a nested data structure.   - date: STRING   - date\_time: DATE-TIME - description: STRING - display\_value: STRING - enabled: BOOLEAN - enum\_options: ARRAY, which is also a nested data structure.   - color: STRING   - enabled: BOOLEAN   - gid: STRING   - name: STRING   - resource\_type: STRING - enum\_value: OBJECT, which is also a nested data structure.   - color: STRING   - enabled: BOOLEAN   - gid: STRING   - name: STRING   - resource\_type: STRING - gid: STRING - has\_notifications\_enabled: BOOLEAN - is\_global\_to\_workspace: BOOLEAN - multi\_enum\_values: ARRAY, which is also a nested data structure.   - color: STRING   - enabled: BOOLEAN   - gid: STRING   - name: STRING   - resource\_type: STRING - name: STRING - number\_value: NUMBER - precision: INTEGER - resource\_subtype: STRING - resource\_type: STRING - text\_value: STRING - type: STRING |
| **default\_view**  STRING |
| **due\_date**  STRING |
| **due\_on**  STRING |
| **followers**  ARRAY This is a nested data structure:   - gid: STRING - name: STRING - resource\_type: STRING |
| **gid**  STRING |
| **html\_notes**  STRING |
| **icon**  STRING |
| **is\_template**  BOOLEAN |
| **members**  ARRAY This is a nested data structure:   - gid: STRING - name: STRING - resource\_type: STRING |
| **modified\_at**  DATE-TIME |
| **name**  STRING |
| **notes**  STRING |
| **owner**  OBJECT This is a nested data structure:   - gid: STRING - name: STRING - resource\_type: STRING |
| **permalink\_url**  STRING |
| **project\_brief**  OBJECT This is a nested data structure:   - gid: STRING - resource\_type: STRING |
| **public**  BOOLEAN |
| **resource\_type**  STRING |
| **start\_on**  STRING |
| **team**  OBJECT This is a nested data structure:   - gid: STRING - name: STRING - resource\_type: STRING |
| **workspace**  OBJECT This is a nested data structure:   - gid: STRING - name: STRING - resource\_type: STRING |

### sections

The `sections` table contains info about sections within specified projects in your Asana account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | gid |
| **Useful links** | [Asana documentation](https://developers.asana.com/Content/sections)  [Asana API method](https://developers.asana.com/Content/get-sections-in-a-project "Opens in new tab: Asana API method") |

sections table foreign keys

| Join sections with | on |
| --- | --- |
| [projects](#projects) | ``` sections.project.gid = projects.gid ```  ``` sections.projects.gid = projects.gid ``` |
| [tasks](#tasks) | ``` sections.project.gid = tasks.projects.gid ```  ``` sections.projects.gid = tasks.projects.gid ``` |
| [stories](#stories) | ``` sections.project.gid = stories.project.gid ```  ``` sections.projects.gid = stories.project.gid ```  ``` sections.gid = stories.new_section.gid ```  ``` sections.gid = stories.old_section.gid ``` |

sections table schema

|  |
| --- |
| **created\_at**  DATE-TIME |
| **gid**  STRING |
| **name**  STRING |
| **project**  OBJECT This is a nested data structure:   - gid: STRING - name: STRING - resource\_type: STRING |
| **projects**  ARRAY This is a nested data structure:   - gid: STRING - name: STRING - resource\_type: STRING |
| **resource\_type**  STRING |

### stories

The `stories` table contains info about all stories within specified tasks in your Asana account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | gid |
| **Replication Key** | created\_at |
| **Useful links** | [Asana documentation](https://developers.asana.com/Content/stories)  [Asana API method](https://developers.asana.com/Content/get-stories-from-a-task "Opens in new tab: Asana API method") |

stories table foreign keys

| Join stories with | on |
| --- | --- |
| [projects](#projects) | ``` stories.project.gid = projects.gid ```  ``` stories.assignee.gid = projects.followers.gid ```  ``` stories.created_by.gid = projects.followers.gid ```  ``` stories.dependency.gid = projects.followers.gid ```  ``` stories.assignee.gid = projects.members.gid ```  ``` stories.created_by.gid = projects.members.gid ```  ``` stories.dependency.gid = projects.members.gid ```  ``` stories.assignee.gid = projects.owner.gid ```  ``` stories.created_by.gid = projects.owner.gid ```  ``` stories.dependency.gid = projects.owner.gid ``` |
| [tasks](#tasks) | ``` stories.project.gid = tasks.projects.gid ```  ``` stories.task.gid = tasks.gid ```  ``` stories.assignee.gid = tasks.assignee.gid ```  ``` stories.created_by.gid = tasks.assignee.gid ```  ``` stories.dependency.gid = tasks.assignee.gid ```  ``` stories.assignee.gid = tasks.followers.gid ```  ``` stories.created_by.gid = tasks.followers.gid ```  ``` stories.dependency.gid = tasks.followers.gid ``` |
| [sections](#sections) | ``` stories.project.gid = sections.project.gid ```  ``` stories.project.gid = sections.projects.gid ```  ``` stories.new_section.gid = sections.gid ```  ``` stories.old_section.gid = sections.gid ``` |
| [tags](#tags) | ``` stories.tag.gid = tags.gid ```  ``` stories.assignee.gid = tags.followers.gid ```  ``` stories.created_by.gid = tags.followers.gid ```  ``` stories.dependency.gid = tags.followers.gid ``` |
| [users](#users) | ``` stories.assignee.gid = users.gid ```  ``` stories.created_by.gid = users.gid ```  ``` stories.dependency.gid = users.gid ``` |
| [portfolios](#portfolios) | ``` stories.assignee.gid = portfolios.created_by.gid ```  ``` stories.created_by.gid = portfolios.created_by.gid ```  ``` stories.dependency.gid = portfolios.created_by.gid ```  ``` stories.assignee.gid = portfolios.members.gid ```  ``` stories.created_by.gid = portfolios.members.gid ```  ``` stories.dependency.gid = portfolios.members.gid ```  ``` stories.assignee.gid = portfolios.owner.gid ```  ``` stories.created_by.gid = portfolios.owner.gid ```  ``` stories.dependency.gid = portfolios.owner.gid ``` |
| [teams](#teams) | ``` stories.assignee.gid = teams.users.gid ```  ``` stories.created_by.gid = teams.users.gid ```  ``` stories.dependency.gid = teams.users.gid ``` |

stories table schema

|  |
| --- |
| **assignee**  OBJECT This is a nested data structure:   - gid: STRING - name: STRING - resource\_type: STRING |
| **created\_at**  DATE-TIME |
| **created\_by**  OBJECT This is a nested data structure:   - gid: STRING - name: STRING - resource\_type: STRING |
| **custom\_field**  OBJECT This is a nested data structure:   - date\_value: OBJECT, which is also a nested data structure.   - date: STRING   - date\_time: DATE-TIME - display\_value: STRING - enabled: BOOLEAN - enum\_options: ARRAY, which is also a nested data structure.   - color: STRING   - enabled: BOOLEAN   - gid: STRING   - name: STRING   - resource\_type: STRING - enum\_value: OBJECT, which is also a nested data structure.   - color: STRING   - enabled: BOOLEAN   - gid: STRING   - name: STRING   - resource\_type: STRING - gid: STRING - multi\_enum\_values: ARRAY, which is also a nested data structure.   - color: STRING   - enabled: BOOLEAN   - gid: STRING   - name: STRING   - resource\_type: STRING - name: STRING - number\_value: NUMBER - resource\_subtype: STRING - resource\_type: STRING - text\_value: STRING - type: STRING |
| **dependency**  OBJECT This is a nested data structure:   - gid: STRING - name: STRING - resource\_subtype: STRING - resource\_type: STRING |
| **duplicate\_of**  OBJECT This is a nested data structure:   - gid: STRING - name: STRING - resource\_subtype: STRING - resource\_type: STRING |
| **duplicated\_from**  OBJECT This is a nested data structure:   - gid: STRING - name: STRING - resource\_subtype: STRING - resource\_type: STRING |
| **follower**  OBJECT This is a nested data structure:   - gid: STRING - name: STRING - resource\_type: STRING |
| **gid**  STRING |
| **hearted**  BOOLEAN |
| **hearts**  ARRAY This is a nested data structure:   - gid: STRING - user: OBJECT, which is also a nested data structure.   - gid: STRING   - name: STRING   - resource\_type: STRING |
| **html\_text**  STRING |
| **is\_editable**  BOOLEAN |
| **is\_edited**  BOOLEAN |
| **is\_pinned**  BOOLEAN |
| **liked**  BOOLEAN |
| **likes**  ARRAY This is a nested data structure:   - gid: STRING - user: OBJECT, which is also a nested data structure.   - gid: STRING   - name: STRING   - resource\_type: STRING |
| **new\_approval\_status**  BOOLEAN |
| **new\_date\_value**  OBJECT This is a nested data structure:   - due\_at: DATE-TIME - due\_on: STRING - start\_on: STRING |
| **new\_dates**  OBJECT This is a nested data structure:   - due\_at: DATE-TIME - due\_on: STRING - start\_on: STRING |
| **new\_enum\_value**  OBJECT This is a nested data structure:   - color: STRING - enabled: ENABLED - gid: STRING - name: STRING - resource\_type: STRING |
| **new\_multi\_enum\_values**  ARRAY This is a nested data structure:   - color: STRING - enabled: ENABLED - gid: STRING - name: STRING - resource\_type: STRING |
| **new\_name**  STRING |
| **new\_number\_value**  NUMBER |
| **new\_people\_value**  ARRAY This is a nested data structure:   - gid: STRING - name: STRING - resource\_type: STRING |
| **new\_resource\_subtype**  STRING |
| **new\_section**  OBJECT This is a nested data structure:   - gid: STRING - name: STRING - resource\_type: STRING |
| **new\_text\_value**  STRING |
| **num\_hearts**  INTEGER |
| **num\_likes**  INTEGER |
| **old\_approval\_status**  STRING |
| **old\_date\_value**  OBJECT This is a nested data structure:   - due\_at: DATE-TIME - due\_on: STRING - start\_on: STRING |
| **old\_dates**  OBJECT This is a nested data structure:   - due\_at: DATE-TIME - due\_on: STRING - start\_on: STRING |
| **old\_enum\_value**  OBJECT This is a nested data structure:   - color: STRING - enabled: ENABLED - gid: STRING - name: STRING - resource\_type: STRING |
| **old\_multi\_enum\_values**  ARRAY This is a nested data structure:   - color: STRING - enabled: ENABLED - gid: STRING - name: STRING - resource\_type: STRING |
| **old\_name**  STRING |
| **old\_number\_value**  NUMBER |
| **old\_people\_value**  ARRAY This is a nested data structure:   - gid: STRING - name: STRING - resource\_type: STRING |
| **old\_resource\_subtype**  STRING |
| **old\_section**  OBJECT This is a nested data structure:   - gid: STRING - name: STRING - resource\_type: STRING |
| **old\_text\_value**  STRING |
| **previews**  ARRAY This is a nested data structure:   - fallback: STRING - footer: STRING - header: STRING - header\_link: STRING - html\_text: STRING - text: STRING - title: STRING - title: STRING |
| **project**  OBJECT This is a nested data structure:   - gid: STRING - name: STRING - resource\_type: STRING |
| **resource\_subtype**  STRING |
| **resource\_type**  STRING |
| **source**  STRING |
| **sticker\_name**  STRING |
| **story**  OBJECT This is a nested data structure:   - created\_at: DATE-TIME - created\_by: OBJECT, which is also a nested data structure.   - gid: STRING   - name: STRING   - resource\_type: STRING - gid: STRING - name: STRING - resource\_subtype: STRING - resource\_type: STRING - text: STRING |
| **tag**  OBJECT This is a nested data structure:   - gid: STRING - name: STRING - resource\_type: STRING |
| **target**  OBJECT This is a nested data structure:   - gid: STRING - name: STRING - resource\_subtype: STRING - resource\_type: STRING |
| **task**  OBJECT This is a nested data structure:   - gid: STRING - name: STRING - resource\_subtype: STRING - resource\_type: STRING |
| **text**  STRING |
| **type**  STRING |

### subtasks

The `subtasks` table contains info about the subtasks associated with tasks in your Asana account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | gid |
| **Replication Key** | modified\_at |
| **Useful links** | [Asana API method](https://developers.asana.com/reference/getsubtasksfortask "Opens in new tab: Asana API method") |

subtasks table schema

|  |
| --- |
| **assignee**  OBJECT This is a nested data structure:   - gid: STRING - name: STRING - resource\_type: STRING |
| **assignee\_status**  STRING |
| **completed**  BOOLEAN |
| **completed\_at**  DATE-TIME |
| **completed\_by**  OBJECT This is a nested data structure:   - gid: STRING - name: STRING - resource\_type: STRING |
| **created\_at**  DATE-TIME |
| **custom\_fields**  ARRAY This is a nested data structure:   - created\_by: OBJECT, which is also a nested data structure.   - gid: STRING   - name: STRING   - resource\_type: STRING - currency\_code: STRING - custom\_label: STRING - custom\_label\_position: STRING - date\_value: OBJECT, which is also a nested data structure.   - date: STRING   - date\_time: DATE-TIME - description: STRING - display\_value: STRING - enabled: BOOLEAN - enum\_options: ARRAY, which is also a nested data structure.   - color: STRING   - enabled: BOOLEAN   - gid: STRING   - name: STRING   - resource\_type: STRING - enum\_value: OBJECT, which is also a nested data structure.   - color: STRING   - enabled: BOOLEAN   - gid: STRING   - name: STRING   - resource\_type: STRING - format: STRING - gid: STRING - has\_notifications\_enabled: BOOLEAN - is\_global\_to\_workspace: BOOLEAN - multi\_enum\_values: ARRAY, which is also a nested data structure.   - color: STRING   - enabled: BOOLEAN   - gid: STRING   - name: STRING   - resource\_type: STRING - name: STRING - number\_value: NUMBER - people\_value: ARRAY, which is also a nested data structure.   - gid: STRING   - name: STRING   - resource\_type: STRING - precision: INTEGER - resource\_subtype: STRING - resource\_type: STRING - text\_value: STRING - type: STRING |
| **dependencies**  ARRAY This is a nested data structure:   - gid: STRING - name: STRING - resource\_type: STRING |
| **dependents**  ARRAY This is a nested data structure:   - gid: STRING - name: STRING - resource\_type: STRING |
| **due\_at**  DATE-TIME |
| **due\_on**  DATE-TIME |
| **followers**  ARRAY This is a nested data structure:   - gid: STRING - name: STRING - resource\_type: STRING |
| **gid**  STRING |
| **hearted**  BOOLEAN |
| **hearts**  ARRAY This is a nested data structure:   - gid: STRING - user: OBJECT, which is also a nested data structure.   - gid: STRING   - name: STRING   - resource\_type: STRING |
| **html\_notes**  STRING |
| **is\_rendered\_as\_separator**  BOOLEAN |
| **liked**  BOOLEAN |
| **likes**  ARRAY This is a nested data structure:   - gid: STRING - user: OBJECT, which is also a nested data structure.   - gid: STRING   - name: STRING   - resource\_type: STRING |
| **memberships**  ARRAY This is a nested data structure:   - project: OBJECT, which is also a nested data structure.   - gid: STRING   - name: STRING   - resource\_type: STRING - section: OBJECT, which is also a nested data structure.   - gid: STRING   - name: STRING   - resource\_type: STRING |
| **modified\_at**  DATE-TIME |
| **name**  STRING |
| **notes**  STRING |
| **num\_hearts**  INTEGER |
| **num\_likes**  INTEGER |
| **num\_subtasks**  INTEGER |
| **parent**  OBJECT This is a nested data structure:   - gid: STRING - name: STRING - resource\_subtype: STRING - resource\_type: STRING |
| **permalink\_url**  STRING |
| **projects**  ARRAY This is a nested data structure:   - gid: STRING - name: STRING - resource\_type: STRING |
| **resource\_subtype**  STRING |
| **resource\_type**  STRING |
| **start\_at**  DATE-TIME |
| **start\_on**  STRING |
| **tags**  ARRAY This is a nested data structure:   - gid: STRING - name: STRING - resource\_type: STRING |
| **workspace**  OBJECT This is a nested data structure:   - gid: STRING - name: STRING - resource\_type: STRING |

### tags

The `tags` table contains info about the tags in your Asana account. A tag is a label that can be attached to any task in Asana.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | gid |
| **Replication Key** | created\_at |
| **Useful links** | [Asana documentation](https://asana.com/developers/api-reference/tags) |

tags table foreign keys

| Join tags with | on |
| --- | --- |
| [stories](#stories) | ``` tags.gid = stories.tag.gid ```  ``` tags.followers.gid = stories.assignee.gid ```  ``` tags.followers.gid = stories.created_by.gid ```  ``` tags.followers.gid = stories.dependency.gid ``` |
| [projects](#projects) | ``` tags.followers.gid = projects.followers.gid ```  ``` tags.followers.gid = projects.members.gid ```  ``` tags.followers.gid = projects.owner.gid ```  ``` tags.workspace.gid = projects.workspace.gid ``` |
| [tasks](#tasks) | ``` tags.followers.gid = tasks.assignee.gid ```  ``` tags.followers.gid = tasks.followers.gid ```  ``` tags.workspace.gid = tasks.workspace.gid ``` |
| [users](#users) | ``` tags.followers.gid = users.gid ```  ``` tags.workspace.gid = users.workspaces.gid ``` |
| [portfolios](#portfolios) | ``` tags.followers.gid = portfolios.created_by.gid ```  ``` tags.followers.gid = portfolios.members.gid ```  ``` tags.followers.gid = portfolios.owner.gid ```  ``` tags.workspace.gid = portfolios.workspace.gid ``` |
| [teams](#teams) | ``` tags.followers.gid = teams.users.gid ```  ``` tags.workspace.gid = teams.organization.gid ``` |
| [workspaces](#workspaces) | ``` tags.workspace.gid = workspaces.gid ``` |

tags table schema

|  |
| --- |
| **color**  STRING |
| **created\_at**  DATE-TIME |
| **followers**  ARRAY This is a nested data structure:   - gid: STRING - name: STRING - resource\_type: STRING |
| **gid**  STRING |
| **name**  STRING |
| **notes**  STRING |
| **permalink\_url**  STRING |
| **resource\_type**  STRING |
| **workspace**  OBJECT This is a nested data structure:   - gid: STRING - name: STRING - resource\_type: STRING |

### tasks

The `tasks` table contains info about the tasks in your Asana account.

#### Custom fields

To replicate task custom fields, select the `custom_fields` attribute in Stitch. If your destination doesn’t natively support nested data structures, two subtables (`tasks__custom_fields`, `tasks__custom_fields__enum_options`) will be created.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | gid |
| **Replication Key** | modified\_at |
| **Useful links** | [Asana documentation](https://asana.com/developers/api-reference/tasks) |

tasks table foreign keys

| Join tasks with | on |
| --- | --- |
| [projects](#projects) | ``` tasks.projects.gid = projects.gid ```  ``` tasks.assignee.gid = projects.followers.gid ```  ``` tasks.followers.gid = projects.followers.gid ```  ``` tasks.assignee.gid = projects.members.gid ```  ``` tasks.followers.gid = projects.members.gid ```  ``` tasks.assignee.gid = projects.owner.gid ```  ``` tasks.followers.gid = projects.owner.gid ```  ``` tasks.workspace.gid = projects.workspace.gid ``` |
| [stories](#stories) | ``` tasks.projects.gid = stories.project.gid ```  ``` tasks.gid = stories.task.gid ```  ``` tasks.assignee.gid = stories.assignee.gid ```  ``` tasks.followers.gid = stories.assignee.gid ```  ``` tasks.assignee.gid = stories.created_by.gid ```  ``` tasks.followers.gid = stories.created_by.gid ```  ``` tasks.assignee.gid = stories.dependency.gid ```  ``` tasks.followers.gid = stories.dependency.gid ``` |
| [sections](#sections) | ``` tasks.projects.gid = sections.project.gid ```  ``` tasks.projects.gid = sections.projects.gid ``` |
| [tags](#tags) | ``` tasks.assignee.gid = tags.followers.gid ```  ``` tasks.followers.gid = tags.followers.gid ```  ``` tasks.workspace.gid = tags.workspace.gid ``` |
| [users](#users) | ``` tasks.assignee.gid = users.gid ```  ``` tasks.followers.gid = users.gid ```  ``` tasks.workspace.gid = users.workspaces.gid ``` |
| [portfolios](#portfolios) | ``` tasks.assignee.gid = portfolios.created_by.gid ```  ``` tasks.followers.gid = portfolios.created_by.gid ```  ``` tasks.assignee.gid = portfolios.members.gid ```  ``` tasks.followers.gid = portfolios.members.gid ```  ``` tasks.assignee.gid = portfolios.owner.gid ```  ``` tasks.followers.gid = portfolios.owner.gid ```  ``` tasks.workspace.gid = portfolios.workspace.gid ``` |
| [teams](#teams) | ``` tasks.assignee.gid = teams.users.gid ```  ``` tasks.followers.gid = teams.users.gid ```  ``` tasks.workspace.gid = teams.organization.gid ``` |
| [workspaces](#workspaces) | ``` tasks.workspace.gid = workspaces.gid ``` |

tasks table schema

|  |
| --- |
| **approval\_status**  STRING |
| **assignee**  OBJECT This is a nested data structure:   - gid: STRING - name: STRING - resource\_type: STRING |
| **assignee\_section**  OBJECT This is a nested data structure:   - gid: STRING - name: STRING - resource\_type: STRING |
| **assignee\_status**  STRING |
| **completed**  BOOLEAN |
| **completed\_at**  DATE-TIME |
| **completed\_by**  OBJECT This is a nested data structure:   - gid: STRING - name: STRING - resource\_type: STRING |
| **created\_at**  DATE-TIME |
| **custom\_fields**  ARRAY This is a nested data structure:   - created\_by: OBJECT, which is also a nested data structure.   - gid: STRING   - name: STRING   - resource\_type: STRING - currency\_code: STRING - custom\_label: STRING - custom\_label\_position: STRING - date\_value: OBJECT, which is also a nested data structure.   - date: STRING   - date\_time: DATE-TIME - description: STRING - display\_value: STRING - enabled: BOOLEAN - enum\_options: ARRAY, which is also a nested data structure.   - color: STRING   - enabled: BOOLEAN   - gid: STRING   - name: STRING   - resource\_type: STRING - enum\_value: OBJECT, which is also a nested data structure.   - color: STRING   - enabled: BOOLEAN   - gid: STRING   - name: STRING   - resource\_type: STRING - format: STRING - gid: STRING - has\_notifications\_enabled: BOOLEAN - is\_global\_to\_workspace: BOOLEAN - multi\_enum\_values: ARRAY, which is also a nested data structure.   - color: STRING   - enabled: BOOLEAN   - gid: STRING   - name: STRING   - resource\_type: STRING - name: STRING - number\_value: NUMBER - people\_value: ARRAY, which is also a nested data structure.   - gid: STRING   - name: STRING   - resource\_type: STRING - precision: INTEGER - resource\_subtype: STRING - resource\_type: STRING - text\_value: STRING - type: STRING |
| **dependencies**  ARRAY This is a nested data structure:   - gid: STRING - name: STRING - resource\_type: STRING |
| **dependents**  ARRAY This is a nested data structure:   - gid: STRING - name: STRING - resource\_type: STRING |
| **due\_at**  DATE-TIME |
| **due\_on**  DATE-TIME |
| **external**  OBJECT This is a nested data structure:   - data: STRING - gid: STRING |
| **followers**  ARRAY This is a nested data structure:   - gid: STRING - name: STRING - resource\_type: STRING |
| **gid**  STRING |
| **hearted**  BOOLEAN |
| **hearts**  ARRAY This is a nested data structure:   - gid: STRING - user: OBJECT, which is also a nested data structure.   - gid: STRING   - name: STRING   - resource\_type: STRING |
| **html\_notes**  STRING |
| **is\_rendered\_as\_seperator**  BOOLEAN |
| **liked**  BOOLEAN |
| **likes**  ARRAY This is a nested data structure:   - gid: STRING - user: OBJECT, which is also a nested data structure.   - gid: STRING   - name: STRING   - resource\_type: STRING |
| **memberships**    ARRAY This is a nested data structure:   - project: OBJECT, which is also a nested data structure.   - gid: STRING   - name: STRING   - resource\_type: STRING - section: OBJECT, which is also a nested data structure.   - gid: STRING   - name: STRING   - resource\_type: STRING |
| **modified\_at**  DATE-TIME |
| **name**  STRING |
| **notes**  STRING |
| **num\_hearts**  INTEGER |
| **num\_likes**  INTEGER |
| **num\_subtasks**  INTEGER |
| **parent**  OBJECT This is a nested data structure:   - gid: STRING - name: STRING - resource\_subtype: STRING - resource\_type: STRING |
| **permalink\_url**  STRING |
| **projects**  ARRAY This is a nested data structure:   - gid: STRING - name: STRING - resource\_type: STRING |
| **resource\_subtype**  STRING |
| **resource\_type**  STRING |
| **start\_at**  DATE-TIME |
| **start\_on**  STRING |
| **tags**  ARRAY This is a nested data structure:   - gid: STRING - name: STRING - resource\_type: STRING |
| **workspace**  OBJECT This is a nested data structure:   - gid: STRING - name: STRING - resource\_type: STRING |

### teams

The `teams` table contains info about teams that belong to a specified user in your Asana account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | gid |
| **Useful links** | [Asana documentation](https://developers.asana.com/Content/teams)  [Asana API method](https://developers.asana.com/Content/get-teams-for-a-user "Opens in new tab: Asana API method") |

teams table foreign keys

| Join teams with | on |
| --- | --- |
| [projects](#projects) | ``` teams.users.gid = projects.followers.gid ```  ``` teams.users.gid = projects.members.gid ```  ``` teams.users.gid = projects.owner.gid ```  ``` teams.organization.gid = projects.workspace.gid ``` |
| [tags](#tags) | ``` teams.users.gid = tags.followers.gid ```  ``` teams.organization.gid = tags.workspace.gid ``` |
| [tasks](#tasks) | ``` teams.users.gid = tasks.assignee.gid ```  ``` teams.users.gid = tasks.followers.gid ```  ``` teams.organization.gid = tasks.workspace.gid ``` |
| [users](#users) | ``` teams.users.gid = users.gid ```  ``` teams.organization.gid = users.workspaces.gid ``` |
| [stories](#stories) | ``` teams.users.gid = stories.assignee.gid ```  ``` teams.users.gid = stories.created_by.gid ```  ``` teams.users.gid = stories.dependency.gid ``` |
| [portfolios](#portfolios) | ``` teams.users.gid = portfolios.created_by.gid ```  ``` teams.users.gid = portfolios.members.gid ```  ``` teams.users.gid = portfolios.owner.gid ```  ``` teams.organization.gid = portfolios.workspace.gid ``` |
| [workspaces](#workspaces) | ``` teams.organization.gid = workspaces.gid ``` |

teams table schema

|  |
| --- |
| **description**  STRING |
| **gid**  STRING |
| **html\_description**  STRING |
| **name**  STRING |
| **organization**  OBJECT This is a nested data structure:   - gid: STRING - name: STRING - resource\_type: STRING |
| **permalink\_url**  STRING |
| **resource\_type**  STRING |
| **users**  ARRAY This is a nested data structure:   - gid: STRING - name: STRING - resource\_type: STRING |
| **visibility**  STRING |

### users

The `users` table contains info about the users in your Asana account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | gid |
| **Useful links** | [Asana documentation](https://asana.com/developers/api-reference/users) |

users table foreign keys

| Join users with | on |
| --- | --- |
| [projects](#projects) | ``` users.gid = projects.followers.gid ```  ``` users.gid = projects.members.gid ```  ``` users.gid = projects.owner.gid ```  ``` users.workspaces.gid = projects.workspace.gid ``` |
| [tags](#tags) | ``` users.gid = tags.followers.gid ```  ``` users.workspaces.gid = tags.workspace.gid ``` |
| [tasks](#tasks) | ``` users.gid = tasks.assignee.gid ```  ``` users.gid = tasks.followers.gid ```  ``` users.workspaces.gid = tasks.workspace.gid ``` |
| [stories](#stories) | ``` users.gid = stories.assignee.gid ```  ``` users.gid = stories.created_by.gid ```  ``` users.gid = stories.dependency.gid ``` |
| [portfolios](#portfolios) | ``` users.gid = portfolios.created_by.gid ```  ``` users.gid = portfolios.members.gid ```  ``` users.gid = portfolios.owner.gid ```  ``` users.workspaces.gid = portfolios.workspace.gid ``` |
| [teams](#teams) | ``` users.gid = teams.users.gid ```  ``` users.workspaces.gid = teams.organization.gid ``` |
| [workspaces](#workspaces) | ``` users.workspaces.gid = workspaces.gid ``` |

users table schema

|  |
| --- |
| **email**  STRING |
| **gid**  STRING |
| **name**  STRING |
| **photo**  OBJECT This is a nested data structure:   - image\_1024x1024: STRING - image\_128x128: STRING - image\_21x21: STRING - image\_27x27: STRING - image\_36x36: STRING - image\_60x60: STRRING |
| **resource\_type**  STRING |
| **workspaces**  ARRAY This is a nested data structure:   - gid: STRING - name: STRING - resource\_type: STRING |

### workspaces

The `workspaces` table contains info about the workspaces associated with your Asana account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | gid |
| **Useful links** | [Asana documentation](https://asana.com/developers/api-reference/workspaces) |

workspaces table foreign keys

| Join workspaces with | on |
| --- | --- |
| [projects](#projects) | ``` workspaces.gid = projects.workspace.gid ``` |
| [tags](#tags) | ``` workspaces.gid = tags.workspace.gid ``` |
| [tasks](#tasks) | ``` workspaces.gid = tasks.workspace.gid ``` |
| [users](#users) | ``` workspaces.gid = users.workspaces.gid ``` |
| [portfolios](#portfolios) | ``` workspaces.gid = portfolios.workspace.gid ``` |
| [teams](#teams) | ``` workspaces.gid = teams.organization.gid ``` |

workspaces table schema

|  |
| --- |
| **email\_domains**  ARRAY This is a nested data structure. |
| **gid**  STRING |
| **is\_organization**  BOOLEAN |
| **name**  STRING |
| **resource\_type**  STRING |
