---
title: "Notion"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Notion-v2.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Notion

Notion is a collaborative environment where teams can organize work, manage projects, and store information in a customizable way.

Notion integration replicates data using the [Notion API](https://developers.notion.com/reference/intro).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To set up the integration:

1. Log into your [Notion](https://www.notion.so/profile/integrations) account.
2. Navigate to Profile > Integrations.
3. Click New Integration and specify the following properties:
   - In Integration Name, enter a name.
   - In Associated workspace, select a workspace to install the integration.
   - In Type, select Internal.
4. Click Save to generate your internal integration secret.

   Copy and paste your authorization token into a secured file.
5. In Capabilities, select the following capabilities:
   - Read content
   - Read comments
   - Read user information including email addresses
6. Go to Access tab and specify which pages or databases the integration can access.

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
| Authorization Token | Authorization token. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### pages

The `pages` table contains info about the page properties in your Notion account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Notion documentation](https://developers.notion.com/reference/retrieve-a-page) |

### data\_sources

The `data_sources` table contains info about the structure and columns of a data source in your Notion account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Notion documentation](https://developers.notion.com/reference/retrieve-a-data-source) |

### users

The `users` table contains info about the list of users in your Notion account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Notion documentation](https://developers.notion.com/reference/get-users) |

### blocks

The `blocks` table contains info about the block objects in your Notion account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Notion documentation](https://developers.notion.com/reference/retrieve-a-block) |

### block-children

The `block-children` table contains info about the child block objects in your Notion account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Notion documentation](https://developers.notion.com/reference/get-block-children) |

### page\_property

The `page_property` table contains info about the page properties in your Notion account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Notion documentation](https://developers.notion.com/reference/retrieve-a-page-property) |

### comments

The `comments` table contains info about the comment objects in your Notion account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Notion documentation](https://developers.notion.com/reference/list-comments) |

### file\_upload

The `file_upload` table contains info about the file upload objects in your Notion account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Notion documentation](https://developers.notion.com/reference/retrieve-a-file-upload) |

### file\_uploads\_list

The `file_uploads_list` table contains info about the file uploads in your Notion account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Notion documentation](https://developers.notion.com/reference/list-file-uploads) |

### user

The `user` table contains info about the users in your Notion account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Notion documentation](https://developers.notion.com/reference/get-user) |

### bot\_user

The `bot_user` table contains info about the bot users in your Notion account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Notion documentation](https://developers.notion.com/reference/get-self) |
