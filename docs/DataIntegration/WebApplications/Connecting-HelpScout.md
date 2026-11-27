---
title: "Help Scout"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-HelpScout.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Help Scout

Help Scout is an easy-to-use help desk software that enables small companies to provide their contacts with personalized support.

Help Scout integration replicates data using the [Help Scout Mailbox API 2.0](https://developer.helpscout.com/mailbox-api/).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

You must have administrative privileges to create an app in your Help Scout account.

To create your App ID and App secret:

1. Log into your [Help Scout](https://secure.helpscout.net/members/login/) account.
2. Navigate to User profile > My Apps.
3. Click Create My App.
4. In App Name, enter a name for the application.
5. In Redirection URL, make sure it is set to https://connector.qlik.com/auth/oauth/v3.htm.
6. Click Create.
7. Copy and paste your App ID and App secret into a secured file.

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
| App ID | App ID. |
| App Secret | App Secret. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### conversation\_threads

The `conversation_threads` table contains info about the threads that make up [`conversations`](#conversations).

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | created\_at |
| **Useful links** | [Help Scout API method](https://developer.helpscout.com/mailbox-api/endpoints/conversations/threads/list/ "Opens in new tab: Help Scout API method") |

conversation\_threads table foreign keys

| Join conversation\_threads with | on |
| --- | --- |
| [conversations](#conversations) | ``` conversation_threads.conversation_id = conversations.id ```  ``` conversation_threads.customer.id = conversations.primary_customer.id ```  ``` conversation_threads.assigned_to.id = conversations.assignee.id ```  ``` conversation_threads.created_by.id = conversations.assignee.id ```  ``` conversation_threads.assigned_to.id = conversations.closed_by ```  ``` conversation_threads.created_by.id = conversations.closed_by ```  ``` conversation_threads.assigned_to.id = conversations.created_by.id ```  ``` conversation_threads.created_by.id = conversations.created_by.id ``` |
| [customers](#customers) | ``` conversation_threads.customer.id = customers.id ``` |
| [users](#users) | ``` conversation_threads.assigned_to.id = users.id ```  ``` conversation_threads.created_by.id = users.id ``` |

conversation\_threads table schema

|  |
| --- |
| **action**  OBJECT This is a nested data structure:   - text: STRING - type: STRING |
| **assigned\_to**  OBJECT This is a nested data structure:   - email: STRING - first: STRING - id: INTEGER - last: STRING - photo\_url: STRING - type: STRING |
| **attachments**  ARRAY This is a nested data structure. |
| **bcc**  ARRAY This is a nested data structure. |
| **body**  STRING |
| **cc**  ARRAY This is a nested data structure. |
| **conversation\_id**  INTEGER |
| **created\_at**  DATE-TIME |
| **created\_by**  OBJECT This is a nested data structure:   - email: STRING - first: STRING - id: INTEGER - last: STRING - photo\_url: STRING - type: STRING |
| **customer**  OBJECT This is a nested data structure:   - email: STRING - first: STRING - id: INTEGER - last: STRING - photo\_url: STRING |
| **id**  INTEGER |
| **opened\_at**  DATE-TIME |
| **saved\_reply\_id**  INTEGER |
| **source**  OBJECT This is a nested data structure:   - type: STRING - via: STRING |
| **state**  STRING |
| **status**  STRING |
| **to**  ARRAY This is a nested data structure. |
| **type**  STRING |

### conversations

The `conversations` table contains info about the conversations in your Help Scout mailbox. Stitch will replicate all conversations, including active, closed, open, pending, and spam.

**Note**: If custom fields are available, Stitch will replicate them.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Help Scout API method](https://developer.helpscout.com/mailbox-api/endpoints/conversations/list/ "Opens in new tab: Help Scout API method") |

conversations table foreign keys

| Join conversations with | on |
| --- | --- |
| [conversation\_threads](#conversation-threads) | ``` conversations.id = conversation_threads.conversation_id ```  ``` conversations.primary_customer.id = conversation_threads.customer.id ```  ``` conversations.assignee.id = conversation_threads.assigned_to.id ```  ``` conversations.closed_by = conversation_threads.assigned_to.id ```  ``` conversations.created_by.id = conversation_threads.assigned_to.id ```  ``` conversations.assignee.id = conversation_threads.created_by.id ```  ``` conversations.closed_by = conversation_threads.created_by.id ```  ``` conversations.created_by.id = conversation_threads.created_by.id ``` |
| [customers](#customers) | ``` conversations.primary_customer.id = customers.id ``` |
| [mailbox\_folders](#mailbox-folders) | ``` conversations.folder_id = mailbox_folders.id ```  ``` conversations.mailbox_id = mailbox_folders.mailbox_id ``` |
| [mailbox\_fields](#mailbox-fields) | ``` conversations.mailbox_id = mailbox_fields.mailbox_id ``` |
| [mailboxes](#mailboxes) | ``` conversations.mailbox_id = mailboxes.id ``` |
| [workflows](#workflows) | ``` conversations.mailbox_id = workflows.mailbox_id ``` |
| [users](#users) | ``` conversations.assignee.id = users.id ```  ``` conversations.closed_by = users.id ```  ``` conversations.created_by.id = users.id ``` |

conversations table schema

|  |
| --- |
| **assignee**  OBJECT This is a nested data structure:   - email: STRING - first: STRING - id: INTEGER - last: STRING - photo\_url: STRING - type: STRING |
| **bcc**  ARRAY This is a nested data structure. |
| **cc**  ARRAY This is a nested data structure. |
| **closed\_at**  DATE-TIME |
| **closed\_by**  INTEGER |
| **created\_at**  DATE-TIME |
| **created\_by**  OBJECT This is a nested data structure:   - email: STRING - first: STRING - id: INTEGER - last: STRING - photo\_url: STRING - type: STRING |
| **custom\_fields**  ARRAY This is a nested data structure:   - id: INTEGER - name: STRING - text: STRING - value: STRING |
| **customer\_waiting\_since**  OBJECT This is a nested data structure:   - friendly: STRING - last\_reply\_from: STRING - time: DATE-TIME |
| **folder\_id**  INTEGER |
| **id**  INTEGER |
| **mailbox\_id**  INTEGER |
| **number**  INTEGER |
| **preview**  STRING |
| **primary\_customer**  OBJECT This is a nested data structure:   - email: STRING - first: STRING - id: INTEGER - last: STRING - photo\_url: STRING - type: STRING |
| **source**  OBJECT This is a nested data structure:   - type: STRING - via: STRING |
| **state**  STRING |
| **status**  STRING |
| **subject**  STRING |
| **tags**  ARRAY This is a nested data structure:   - color: STRING - id: INTEGER - tag: STRING |
| **threads**  INTEGER |
| **type**  STRING |
| **updated\_at**  DATE-TIME |
| **user\_updated\_at**  DATE-TIME |

### customers

The `customers` table contains info about the customers in your Help Scout account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Help Scout API method](https://developer.helpscout.com/mailbox-api/endpoints/customers/list/ "Opens in new tab: Help Scout API method") |

customers table foreign keys

| Join customers with | on |
| --- | --- |
| [conversation\_threads](#conversation-threads) | ``` customers.id = conversation_threads.customer.id ``` |
| [conversations](#conversations) | ``` customers.id = conversations.primary_customer.id ``` |

customers table schema

|  |
| --- |
| **address**  OBJECT This is a nested data structure:   - city: STRING - country: STRING - lines: ARRAY, which is also a nested data structure. - postal\_code: STRING - state: STRING |
| **age**  STRING |
| **background**  STRING |
| **chats**  ARRAY This is a nested data structure:   - id: INTEGER - type: STRING - value: STRING |
| **created\_at**  DATE-TIME |
| **emails**  ARRAY This is a nested data structure:   - id: INTEGER - type: STRING - value: STRING |
| **first\_name**  STRING |
| **gender**  STRING |
| **id**  INTEGER |
| **job\_title**  STRING |
| **last\_name**  STRING |
| **location**  STRING |
| **organization**  STRING |
| **phones**  ARRAY This is a nested data structure:   - id: INTEGER - type: STRING - value: STRING |
| **photo\_type**  STRING |
| **photo\_url**  STRING |
| **properties**  ARRAY This is a nested data structure:   - name: STRING - type: STRING - value: STRING |
| **social\_profiles**  ARRAY This is a nested data structure:   - id: INTEGER - type: STRING - value: STRING |
| **updated\_at**  DATE-TIME |
| **websites**  ARRAY This is a nested data structure:   - id: INTEGER - value: STRING  Click to expand websites |  | | --- | | **id**  INTEGER | | **value**  STRING | |

### happiness\_ratings\_report

The happiness ratings report provides a company’s ratings for a specified time range.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | conversation\_id  rating\_created\_at  rating\_customer\_id |
| **Useful links** | [Help Scout API method](https://developer.helpscout.com/mailbox-api/endpoints/reports/happiness/reports-happiness-ratings/ "Opens in new tab: Help Scout API method") |

happiness\_ratings\_report table schema

|  |
| --- |
| **conversation\_id**  INTEGER |
| **rating\_comments**  STRING |
| **rating\_created\_at**  DATE-TIME |
| **rating\_customer\_id**  INTEGER |
| **rating\_customer\_name**  STRING |
| **rating\_id**  INTEGER |
| **rating\_user\_id**  INTEGER |
| **rating\_user\_name**  STRING |
| **thread\_created\_at**  DATE-TIME |
| **thread\_id**  INTEGER |
| **type**  STRING |

### mailbox\_fields

The `mailbox_fields` table contains info about the custom fields associated with your Help Scout mailboxes.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Help Scout API method](https://developer.helpscout.com/mailbox-api/endpoints/mailboxes/mailbox-fields/ "Opens in new tab: Help Scout API method") |

mailbox\_fields table foreign keys

| Join mailbox\_fields with | on |
| --- | --- |
| [conversations](#conversations) | ``` mailbox_fields.mailbox_id = conversations.mailbox_id ``` |
| [mailbox\_folders](#mailbox-folders) | ``` mailbox_fields.mailbox_id = mailbox_folders.mailbox_id ``` |
| [mailboxes](#mailboxes) | ``` mailbox_fields.mailbox_id = mailboxes.id ``` |
| [workflows](#workflows) | ``` mailbox_fields.mailbox_id = workflows.mailbox_id ``` |

mailbox\_fields table schema

|  |
| --- |
| **id**  INTEGER |
| **mailbox\_id**  INTEGER |
| **name**  STRING |
| **options**  ARRAY This is a nested data structure:   - id: INTEGER - label: STRING - order: INTEGER |
| **order**  INTEGER |
| **required**  BOOLEAN |
| **type**  STRING |

### mailbox\_folders

The `mailbox_folders` table contains info about the mailbox folders in your Help Scout account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Help Scout API method](https://developer.helpscout.com/mailbox-api/endpoints/mailboxes/mailbox-folders/ "Opens in new tab: Help Scout API method") |

mailbox\_folders table foreign keys

| Join mailbox\_folders with | on |
| --- | --- |
| [conversations](#conversations) | ``` mailbox_folders.id = conversations.folder_id ```  ``` mailbox_folders.mailbox_id = conversations.mailbox_id ``` |
| [mailbox\_fields](#mailbox-fields) | ``` mailbox_folders.mailbox_id = mailbox_fields.mailbox_id ``` |
| [mailboxes](#mailboxes) | ``` mailbox_folders.mailbox_id = mailboxes.id ``` |
| [workflows](#workflows) | ``` mailbox_folders.mailbox_id = workflows.mailbox_id ``` |

mailbox\_folders table schema

|  |
| --- |
| **active\_count**  INTEGER |
| **id**  INTEGER |
| **mailbox\_id**  INTEGER |
| **name**  STRING |
| **total\_count**  INTEGER |
| **type**  STRING |
| **updated\_at**  DATE-TIME |
| **user\_id**  INTEGER |

### mailboxes

The `mailboxes` table contains info about the mailboxes in your Help Scout account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Help Scout API method](https://developer.helpscout.com/mailbox-api/endpoints/mailboxes/list/ "Opens in new tab: Help Scout API method") |

mailboxes table foreign keys

| Join mailboxes with | on |
| --- | --- |
| [conversations](#conversations) | ``` mailboxes.id = conversations.mailbox_id ``` |
| [mailbox\_fields](#mailbox-fields) | ``` mailboxes.id = mailbox_fields.mailbox_id ``` |
| [mailbox\_folders](#mailbox-folders) | ``` mailboxes.id = mailbox_folders.mailbox_id ``` |
| [workflows](#workflows) | ``` mailboxes.id = workflows.mailbox_id ``` |

mailboxes table schema

|  |
| --- |
| **created\_at**  DATE-TIME |
| **email**  STRING |
| **id**  INTEGER |
| **name**  STRING |
| **slug**  STRING |
| **updated\_at**  DATE-TIME |

### team\_members

This report contains information about team members.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | team\_id  user\_id |
| **Useful links** | [Help Scout API method](https://developer.helpscout.com/mailbox-api/endpoints/teams/list-team-members/ "Opens in new tab: Help Scout API method") |

team\_members table schema

|  |
| --- |
| **team\_id**  INTEGER |
| **user\_id**  INTEGER |

### teams

This report contains information about all the different teams in the company.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Help Scout API method](https://developer.helpscout.com/mailbox-api/endpoints/teams/list-teams/ "Opens in new tab: Help Scout API method") |

teams table schema

|  |
| --- |
| **created\_at**  DATE-TIME |
| **id**  INTEGER |
| **initials**  STRING |
| **mention**  STRING |
| **name**  STRING |
| **photo\_url**  STRING |
| **timezone**  STRING |
| **updated\_at**  DATE-TIME |

### users

The `users` table contains info about the users in your Help Scout account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Help Scout API method](https://developer.helpscout.com/mailbox-api/endpoints/users/list/ "Opens in new tab: Help Scout API method") |

users table foreign keys

| Join users with | on |
| --- | --- |
| [conversation\_threads](#conversation-threads) | ``` users.id = conversation_threads.assigned_to.id ```  ``` users.id = conversation_threads.created_by.id ``` |
| [conversations](#conversations) | ``` users.id = conversations.assignee.id ```  ``` users.id = conversations.closed_by ```  ``` users.id = conversations.created_by.id ``` |

users table schema

|  |
| --- |
| **created\_at**  DATE-TIME |
| **email**  STRING |
| **first\_name**  STRING |
| **id**  INTEGER |
| **last\_name**  STRING |
| **photo\_url**  STRING |
| **role**  STRING |
| **timezone**  STRING |
| **type**  STRING |
| **updated\_at**  DATE-TIME |

### workflows

The `workflows` table contains info about the workflows in your Help Scout account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | modified\_at |
| **Useful links** | [Help Scout API method](https://developer.helpscout.com/mailbox-api/endpoints/workflows/list/ "Opens in new tab: Help Scout API method") |

workflows table foreign keys

| Join workflows with | on |
| --- | --- |
| [conversations](#conversations) | ``` workflows.mailbox_id = conversations.mailbox_id ``` |
| [mailbox\_fields](#mailbox-fields) | ``` workflows.mailbox_id = mailbox_fields.mailbox_id ``` |
| [mailbox\_folders](#mailbox-folders) | ``` workflows.mailbox_id = mailbox_folders.mailbox_id ``` |
| [mailboxes](#mailboxes) | ``` workflows.mailbox_id = mailboxes.id ``` |

workflows table schema

|  |
| --- |
| **created\_at**  DATE-TIME |
| **id**  INTEGER |
| **mailbox\_id**  INTEGER |
| **modified\_at**  DATE-TIME |
| **name**  STRING |
| **order**  INTEGER |
| **status**  STRING |
| **type**  STRING |
