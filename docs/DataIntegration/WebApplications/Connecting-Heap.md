---
title: "Heap"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Heap.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Heap

Heap is an analytics platform that automatically tracks and analyzes all user interactions on a website or app.

Heap integration replicates data from Avro files published to Amazon S3 via Heap’s **Connect** for Amazon S3 feature.

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To obtain your account ID:

1. Log into your Amazon Web Services (AWS) account.
2. Click the **user menu**, located between the **bell** and **Global** menus in the top-right corner of the page.
3. Click **My Account**.
4. In the **Account Settings** section of the page, locate the **Account Id** field:

   ![An AWS account ID, highlighted in the AWS Account Settings page](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/s3-csv-account-id.png)
5. Copy the ID.

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
| S3 Bucket | The name of the S3 bucket. |
| AWS Account ID | AWS account ID. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

### Custom attributes

Heap’s data model is dynamic, meaning it changes as custom attributes are added to object types in your account. For example: Adding new user attributes to the [`user`](#users) object.

This means that the Heap schema in your destination may also change over time as you add new attributes in Heap.

When a new attribute is added to an object in Heap, it will display as a selectable field in the Stitch app. **Note**: To include the field in replication, you’ll need to select it in Stitch. Stitch will not automatically select new fields.

The schema documentation following this section outlines the default attributes for each object type according to Heap’s documentation.

### Event tables

For each event type you define in Heap, a table for that event will be available for selection in Stitch.

For example: If there’s a `Sign up - Click button` event, there will be a table named `sign_up_click_button`.

Refer to the [`[event_type]`](#event_type) schema documentation for a list of default event attributes.

**Note**: When new event types are added in Heap, you will need to select the table and fields in Stitch to include it in replication.

Depending on your destination, table and column names may not appear as they are outlined below.

### event\_tables

For every event type defined in Heap, a table will display in the Stitch app. The name of the table will be the event name, which Heap will first strip the non-alphanumeric characters from. For example: The table name for `Sign Up - Click Link` will be transformed into `sign_up_click_link` by Heap.

**Note**: Custom attributes are supported b for this table. As Heap schemas are dynamic, `event_tables` documentation will only list the non-custom attributes outlined in Heap’s documentation.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | event\_id |
| **Useful links** | [Heap documentation](https://help.heap.io/heap-connect/heap-connect-guide/data-schema/#event-tables) |

event\_tables table foreign keys

| Join event\_tables with | on |
| --- | --- |
| [pageviews](#pageviews) | ``` event_tables.event_id = pageviews.event_id ```  ``` event_tables.session_id = pageviews.session_id ```  ``` event_tables.user_id = pageviews.user_id ``` |
| [sessions](#sessions) | ``` event_tables.event_id = sessions.event_id ```  ``` event_tables.session_id = sessions.session_id ```  ``` event_tables.user_id = sessions.user_id ``` |
| [user\_migrations](#user-migrations) | ``` event_tables.user_id = user_migrations.to_user_id ``` |
| [users](#users) | ``` event_tables.user_id = users.user_id ``` |

event\_tables table schema

|  |
| --- |
| **IP**  STRING |
| **action\_method**  STRING |
| **app\_name**  STRING |
| **app\_version**  STRING |
| **browser**  STRING |
| **carrier**  STRING |
| **city**  STRING |
| **country**  STRING |
| **device**  STRING |
| **device\_type**  STRING |
| **event\_id**  STRING |
| **hash**  STRING |
| **href**  STRING |
| **landing\_page**  STRING |
| **library**  STRING |
| **path**  STRING |
| **platform**  STRING |
| **query**  STRING |
| **referrer**  STRING |
| **region**  STRING |
| **screen\_ally\_id**  STRING |
| **screen\_ally\_label**  STRING |
| **search\_keyword**  STRING |
| **session\_id**  INTEGER |
| **session\_time**  STRING |
| **target\_ally\_id**  STRING |
| **target\_ally\_label**  STRING |
| **target\_text**  STRING |
| **target\_view\_class**  STRING |
| **target\_view\_name**  STRING |
| **time**  STRING |
| **title**  STRING |
| **type**  STRING |
| **user\_id**  INTEGER |
| **utm\_campaign**  STRING |
| **utm\_content**  STRING |
| **utm\_medium**  STRING |
| **utm\_source**  STRING |
| **utm\_term**  STRING |
| **view\_controller**  STRING |

### pageviews

The `pageviews` table contains info about pageviews.

**Note**: Custom attributes are supported for this table. As Heap schemas are dynamic, `pageviews` documentation will only list the non-custom attributes outlined in Heap’s documentation.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | event\_id |
| **Useful links** | [Heap documentation](https://help.heap.io/heap-connect/heap-connect-guide/data-schema/#pageviews-table) |

pageviews table foreign keys

| Join pageviews with | on |
| --- | --- |
| [event\_tables](#event-tables) | ``` pageviews.event_id = event_tables.event_id ```  ``` pageviews.session_id = event_tables.session_id ```  ``` pageviews.user_id = event_tables.user_id ``` |
| [sessions](#sessions) | ``` pageviews.event_id = sessions.event_id ```  ``` pageviews.session_id = sessions.session_id ```  ``` pageviews.user_id = sessions.user_id ``` |
| [user\_migrations](#user-migrations) | ``` pageviews.user_id = user_migrations.to_user_id ``` |
| [users](#users) | ``` pageviews.user_id = users.user_id ``` |

pageviews table schema

|  |
| --- |
| **IP**  STRING |
| **app\_name**  STRING |
| **app\_version**  STRING |
| **browser**  STRING |
| **carrier**  STRING |
| **city**  STRING |
| **country**  STRING |
| **device**  STRING |
| **device\_type**  STRING |
| **event\_id**  STRING |
| **hash**  STRING |
| **landing\_page**  STRING |
| **library**  STRING |
| **path**  STRING |
| **platform**  STRING |
| **query**  STRING |
| **referrer**  STRING |
| **region**  STRING |
| **screen\_ally\_id**  STRING |
| **screen\_ally\_label**  STRING |
| **search\_keyword**  STRING |
| **session\_id**  INTEGER |
| **session\_time**  STRING |
| **time**  STRING |
| **title**  STRING |
| **user\_id**  INTEGER |
| **utm\_campaign**  STRING |
| **utm\_content**  STRING |
| **utm\_medium**  STRING |
| **utm\_source**  STRING |
| **utm\_term**  STRING |
| **view\_controller**  STRING |

### sessions

The `sessions` table contains info about sessions. In Heap, a web session ends after 30 minutes of user inactivity, while in iOS, a session ends after the app has entered the background.

**Note**: Custom attributes are supported for this table. As Heap schemas are dynamic, `sessions` documentation will only list the non-custom attributes outlined in Heap’s documentation.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | event\_id |
| **Useful links** | [Heap documentation](https://help.heap.io/heap-connect/heap-connect-guide/data-schema/#sessions-table) |

sessions table foreign keys

| Join sessions with | on |
| --- | --- |
| [event\_tables](#event-tables) | ``` sessions.event_id = event_tables.event_id ```  ``` sessions.session_id = event_tables.session_id ```  ``` sessions.user_id = event_tables.user_id ``` |
| [pageviews](#pageviews) | ``` sessions.event_id = pageviews.event_id ```  ``` sessions.session_id = pageviews.session_id ```  ``` sessions.user_id = pageviews.user_id ``` |
| [user\_migrations](#user-migrations) | ``` sessions.user_id = user_migrations.to_user_id ``` |
| [users](#users) | ``` sessions.user_id = users.user_id ``` |

sessions table schema

|  |
| --- |
| **IP**  STRING |
| **app\_name**  STRING |
| **app\_version**  STRING |
| **browser**  STRING |
| **carrier**  STRING |
| **city**  STRING |
| **country**  STRING |
| **device**  STRING |
| **device\_type**  STRING |
| **event\_id**  STRING |
| **landing\_page**  STRING |
| **library**  STRING |
| **platform**  STRING |
| **referrer**  STRING |
| **region**  STRING |
| **search\_keyword**  STRING |
| **session\_id**  INTEGER |
| **time**  STRING |
| **user\_id**  INTEGER |
| **utm\_campaign**  STRING |
| **utm\_content**  STRING |
| **utm\_medium**  STRING |
| **utm\_source**  STRING |
| **utm\_term**  STRING |

### user\_migrations

The `user_migrations` table contains info about user migrations.

**Note**: Custom attributes are supported for this table. As Heap schemas are dynamic, `user_migrations` documentation will only list the non-custom attributes outlined in Heap’s documentation.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | from\_user\_id |
| **Useful links** | [Heap documentation](https://help.heap.io/heap-connect/heap-connect-guide/data-schema/#user-migrations-table) |

user\_migrations table foreign keys

| Join user\_migrations with | on |
| --- | --- |
| [event\_tables](#event-tables) | ``` user_migrations.to_user_id = event_tables.user_id ``` |
| [pageviews](#pageviews) | ``` user_migrations.to_user_id = pageviews.user_id ``` |
| [sessions](#sessions) | ``` user_migrations.to_user_id = sessions.user_id ``` |
| [users](#users) | ``` user_migrations.to_user_id = users.user_id ``` |

user\_migrations table schema

|  |
| --- |
| **from\_user\_id**  STRING |
| **time**  STRING |
| **to\_user\_id**  INTEGER |

### users

The `users` table contains info about users.

**Note**: Custom attributes are supported for this table. As Heap schemas are dynamic, `users` documentation will only list the non-custom attributes outlined in Heap’s documentation.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | user\_id |
| **Useful links** | [Heap documentation](https://help.heap.io/heap-connect/heap-connect-guide/data-schema/#users-table) |

users table foreign keys

| Join users with | on |
| --- | --- |
| [event\_tables](#event-tables) | ``` users.user_id = event_tables.user_id ``` |
| [pageviews](#pageviews) | ``` users.user_id = pageviews.user_id ``` |
| [sessions](#sessions) | ``` users.user_id = sessions.user_id ``` |
| [user\_migrations](#user-migrations) | ``` users.user_id = user_migrations.to_user_id ``` |

users table schema

|  |
| --- |
| **email**  STRING |
| **handle**  STRING |
| **identity**  STRING |
| **joindate**  STRING |
| **last\_modified**  STRING |
| **user\_id**  STRING |
