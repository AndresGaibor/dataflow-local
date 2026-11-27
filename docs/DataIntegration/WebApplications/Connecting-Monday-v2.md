---
title: "Monday.com"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Monday-v2.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Monday.com

Monday.com is a powerhouse for project management.

Monday.com integration replicates data using the [Monday.com API](https://developer.monday.com/api-reference/reference/about-the-api-reference).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

Depending on your role in the app, the steps to retrieve the API token may vary.

For account admin users:

1. Log into your [Monday.com](https://auth.monday.com/users/sign_up_new?developer=true) account.
2. Click your profile picture in the top right corner.
3. Click Administration > Connections > Personal API token.
4. Copy and paste your API token into a secured file.

For other users:

1. Log into your [Monday.com](https://auth.monday.com/users/sign_up_new?developer=true) account.
2. Click your profile picture in the top right corner.
3. Select Developers.
4. Click API token > Show.
5. Copy and paste your API token into a secured file.

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

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### account

The `account` table contains info about the account data in your Monday.com account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Monday.com documentation](https://developer.monday.com/api-reference/reference/account#queries) |

### assets

The `assets` table contains info about the assets in your Monday.com account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Monday.com documentation](https://developer.monday.com/api-reference/reference/assets-1#queries) |

### audit\_event\_catalogue

The `audit_event_catalogue` table contains info about the supported audit log events in your Monday.com account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | name |
| **Useful links** | [Monday.com documentation](https://developer.monday.com/api-reference/reference/audit-event-catalogue#queries) |

### boards

The `boards` table contains info about the board data in your Monday.com account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Monday.com documentation](https://developer.monday.com/api-reference/reference/boards#queries) |

### board\_activity\_logs

The `board_activity_logs` table contains info about the activity log data in your Monday.com account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Monday.com documentation](https://developer.monday.com/api-reference/reference/activity-logs#queries) |

### board\_columns

The `board_columns` table contains info about the column data in your Monday.com account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id  board\_id |
| **Useful links** | [Monday.com documentation](https://developer.monday.com/api-reference/reference/columns#queries) |

### board\_groups

The `board_groups` table contains info about the group data in your Monday.com account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id  board\_id |
| **Useful links** | [Monday.com documentation](https://developer.monday.com/api-reference/reference/groups#queries) |

### board\_items

The `board_items` table contains info about the item data in your Monday.com account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Monday.com documentation](https://developer.monday.com/api-reference/reference/items#queries) |

### board\_views

The `board_views` table contains info about the board view data in your Monday.com account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Monday.com documentation](https://developer.monday.com/api-reference/reference/board-views#queries) |

### column\_values

The `column_values` table contains info about the column value data in your Monday.com account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id  item\_id |
| **Useful links** | [Monday.com documentation](https://developer.monday.com/api-reference/reference/column-values-v2#queries) |

### docs

The `docs` table contains info about the monday doc data in your Monday.com account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Monday.com documentation](https://developer.monday.com/api-reference/reference/docs#queries) |

### folders

The `folders` table contains info about the folder data in your Monday.com account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Monday.com documentation](https://developer.monday.com/api-reference/reference/folders#queries) |

### platform\_api

The `platform_api` table contains info about the API usage data in your Monday.com account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | daily\_analytics.last\_update |
| **Useful links** | [Monday.com documentation](https://developer.monday.com/api-reference/reference/platform-api#queries) |

### reply

The `reply` table contains info about other types supported by the monday platform API in your Monday.com account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Monday.com documentation](https://developer.monday.com/api-reference/reference/other-types#reply) |

### tags

The `tags` table contains info about the tag data in your Monday.com account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Monday.com documentation](https://developer.monday.com/api-reference/reference/tags-1#queries) |

### teams

The `teams` table contains info about the team data in your Monday.com account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Monday.com documentation](https://developer.monday.com/api-reference/reference/teams#queries) |

### updates

The `updates` table contains info about the updates data in your Monday.com account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Monday.com documentation](https://developer.monday.com/api-reference/reference/updates#queries) |

### users

The `users` table contains info about the user data in your Monday.com account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Monday.com documentation](https://developer.monday.com/api-reference/reference/users#queries) |

### workspaces

The `workspaces` table contains info about the workspace data in your Monday.com account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Monday.com documentation](https://developer.monday.com/api-reference/reference/workspaces#queries) |
