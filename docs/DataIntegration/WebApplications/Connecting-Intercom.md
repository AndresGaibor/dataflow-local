---
title: "Intercom"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Intercom.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Intercom

Intercom is a customer communication platform.

It replicates data using the [Intercom API](https://developers.intercom.com/docs/references/introduction).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To generate your client ID and secret:

1. Log into your [Intercom Developers](https://developers.intercom.com/) account.
2. Select Developer Hub at the top of the page.
3. Create a new OAuth application.
4. Navigate to Authentication from the left navigation bar and click Edit.
5. Make sure OAuth is activated.
6. Make sure Authorized Redirect URIs is set to https://connector.qlik.com/auth/oauth/v3.htm.
7. Copy the client ID and client secret that are generated, to use in the connection settings.

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
| Client ID | Client ID of your Intercom account. |
| Client Secret | Client secret of your Intercom account. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### admins

The `admins` table lists info about the admins in your Intercom account. An admin is a user, or teammate, in your Intercom account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Intercom documentation](https://developers.intercom.com/intercom-api-reference/v2.5/reference/admin-model)  [Intercom API method](https://developers.intercom.com/intercom-api-reference/v2.5/reference/list-admins "Opens in new tab: Intercom API method") |

admins table schema

|  |
| --- |
| **admin\_ids**  ARRAY |
| **avatar**  OBJECT This is a nested data structure:   - image\_url: STRING |
| **away\_mode\_enabled**  BOOLEAN |
| **away\_mode\_reassign**  BOOLEAN |
| **email**  STRING |
| **has\_inbox\_seat**  BOOLEAN |
| **id**  STRING |
| **job\_title**  STRING |
| **name**  STRING |
| **team\_ids**  ARRAY |
| **type**  STRING |

### companies

The `companies` table contains info about companies that use your Intercom product.

#### Custom attributes

If applicable, Stitch will replicate custom fields related to `companies` in Intercom.

#### Limitations

Intercom’s API limits the number of simultaneous requests a single Intercom app, or connection, can make to the endpoint. Stitch uses this endpoint to replicate company data. Currently, only one request can occur at a time.

If multiple connections exist and they attempt to use this endpoint at the same time, only the connection who made the request first will succeed.

This means that if Stitch attempts to extract data when another connection is using the endpoint, Extraction will fail and an error will surface in the Extraction Logs.

To prevent or minimize this issue, we recommend limiting the number of connections a single workspace has or scheduling extraction jobs in Stitch around your other connections’ usage.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Intercom documentation](https://developers.intercom.com/intercom-api-reference/v2.5/reference/company-model)  [Intercom API method](https://developers.intercom.com/intercom-api-reference/v2.5/reference/iterating-over-all-companies "Opens in new tab: Intercom API method") |

companies table schema

|  |
| --- |
| **company\_id**  STRING |
| **created\_at**  DATE-TIME |
| **custom\_attributes**  OBJECT |
| **id**  STRING |
| **industry**  STRING |
| **last\_request\_at**  DATE-TIME |
| **monthly\_spend**  NUMBER |
| **name**  STRING |
| **plan**  OBJECT This is a nested data structure:   - id: STRING - name: STRING - type: STRING |
| **remote\_created\_at**  DATE-TIME |
| **segments**  ARRAY This is a nested data structure:   - id: STRING |
| **session\_count**  INTEGER |
| **size**  INTEGER |
| **tags**  ARRAY This is a nested data structure:   - id: STRING |
| **type**  STRING |
| **updated\_at**  DATE-TIME |
| **user\_count**  INTEGER |
| **website**  STRING |

### company\_attributes

The `company_attributes` lists data attributes for a specified company in your Intercom account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | \_sdc\_record\_hash |
| **Useful links** | [Intercom documentation](https://developers.intercom.com/intercom-api-reference/v2.5/reference/data-attribute-model)  [Intercom API method](https://developers.intercom.com/intercom-api-reference/v2.5/reference/list-data-attributes "Opens in new tab: Intercom API method") |

company\_attributes table schema

|  |
| --- |
| **\_sdc\_record\_hash**  STRING |
| **admin\_id**  STRING |
| **api\_writable**  BOOLEAN |
| **archived**  BOOLEAN |
| **created\_at**  DATE-TIME |
| **custom**  BOOLEAN |
| **data\_type**  STRING |
| **description**  STRING |
| **full\_name**  STRING |
| **id**  INTEGER |
| **label**  STRING |
| **model**  STRING |
| **name**  STRING |
| **options**  ARRAY |
| **type**  STRING |
| **ui\_writable**  BOOLEAN |
| **updated\_at**  DATE-TIME |

### company\_segments

The `company_segments` table contains information about company segments in your Intercom account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Intercom documentation](https://developers.intercom.com/intercom-api-reference/v2.5/reference/segment-model)  [Intercom API method](https://developers.intercom.com/intercom-api-reference/v2.5/reference/list-segments "Opens in new tab: Intercom API method") |

company\_segments table schema

|  |
| --- |
| **count**  INTEGER |
| **created\_at**  DATE-TIME |
| **id**  STRING |
| **name**  STRING |
| **person\_type**  STRING |
| **type**  STRING |
| **updated\_at**  DATE-TIME |

### contact\_attributes

The `contact_attributes` table contains information about contact attributes in your Intercom account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | \_sdc\_record\_hash |
| **Useful links** | [Intercom documentation](https://developers.intercom.com/intercom-api-reference/v2.5/reference/data-attribute-model)  [Intercom API method](https://developers.intercom.com/intercom-api-reference/v2.5/reference/list-data-attributes "Opens in new tab: Intercom API method") |

contact\_attributes table schema

|  |
| --- |
| **\_sdc\_record\_hash**  STRING |
| **admin\_id**  STRING |
| **api\_writable**  BOOLEAN |
| **archived**  BOOLEAN |
| **created\_at**  DATE-TIME |
| **custom**  BOOLEAN |
| **data\_type**  STRING |
| **description**  STRING |
| **full\_name**  STRING |
| **id**  INTEGER |
| **label**  STRING |
| **model**  STRING |
| **name**  STRING |
| **options**  ARRAY |
| **type**  STRING |
| **ui\_writable**  BOOLEAN |
| **updated\_at**  DATE-TIME |

### contacts

The `contacts` table contains info about users and leads in your Intercom account.

#### Custom attributes

If applicable, Stitch will replicate custom fields related to `contacts` in Intercom.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Intercom documentation](https://developers.intercom.com/intercom-api-reference/v2.5/reference/contacts-model)  [Intercom API method](https://developers.intercom.com/intercom-api-reference/v2.5/reference/list-contacts "Opens in new tab: Intercom API method") |

contacts table schema

|  |
| --- |
| **android\_app\_name**  STRING |
| **android\_app\_version**  STRING |
| **android\_device**  STRING |
| **android\_last\_seen\_at**  DATE-TIME |
| **android\_os\_version**  STRING |
| **android\_sdk\_version**  STRING |
| **avatar**  STRING |
| **browser**  STRING |
| **browser\_language**  STRING |
| **browser\_version**  STRING |
| **companies**  ARRAY This is a nested data structure:   - id: STRING - type: STRING - url: STRING |
| **created\_at**  DATE-TIME |
| **custom\_attributes**  OBJECT |
| **email**  STRING |
| **external\_id**  STRING |
| **has\_hard\_bounced**  BOOLEAN |
| **id**  STRING |
| **ios\_app\_name**  STRING |
| **ios\_app\_version**  STRING |
| **ios\_device**  STRING |
| **ios\_last\_seen\_at**  DATE-TIME |
| **ios\_os\_version**  STRING |
| **ios\_sdk\_version**  STRING |
| **language\_override**  STRING |
| **last\_contacted\_at**  DATE-TIME |
| **last\_email\_clicked\_at**  DATE-TIME |
| **last\_email\_opened\_at**  DATE-TIME |
| **last\_replied\_at**  DATE-TIME |
| **last\_seen\_at**  DATE-TIME |
| **location**  OBJECT This is a nested data structure:   - city: STRING - continent\_code: STRING - country: STRING - country\_code: STRING - region: STRING - type: STRING |
| **marked\_email\_as\_spam**  BOOLEAN |
| **name**  STRING |
| **notes**  OBJECT This is a nested data structure:   - data: ARRAY, which is also a nested data structure.   - id: STRING   - type: STRING   - url: STRING - has\_more: BOOLEAN - total\_count: INTEGER - type: STRING - url: STRING |
| **os**  STRING |
| **owner\_id**  INTEGER |
| **phone**  STRING |
| **role**  STRING |
| **signed\_up\_at**  DATE-TIME |
| **social\_profiles**  OBJECT This is a nested data structure:   - data: ARRAY, which is also a nested data structure.   - name: STRING   - type: STRING   - url: STRING - type: STRING |
| **tags**  ARRAY This is a nested data structure:   - id: STRING |
| **type**  STRING |
| **unsubscribed\_from\_emails**  BOOLEAN |
| **updated\_at**  DATE-TIME |
| **workspace\_id**  STRING |

### conversation\_parts

The `conversation_parts` table lists the individual parts of conversations in your Intercom account.

**Note**: When this table is replicated, all conversation parts associated with an updated conversation will be replicated.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Intercom documentation](https://developers.intercom.com/intercom-api-reference/v2.5/reference/conversation-model)  [Intercom API method](https://developers.intercom.com/intercom-api-reference/v2.5/reference/retrieve-a-conversation "Opens in new tab: Intercom API method") |

conversation\_parts table schema

|  |
| --- |
| **assigned\_to**  STRING |
| **attachments**  ARRAY This is a nested data structure:   - content\_type: STRING - filesize: INTEGER - height: INTEGER - name: STRING - type: STRING - url: STRING - width: INTEGER |
| **author**  OBJECT This is a nested data structure:   - email: STRING - id: STRING - name: STRING - type: STRING |
| **body**  STRING |
| **conversation\_created\_at**  DATE-TIME |
| **conversation\_id**  STRING |
| **conversation\_total\_parts**  INTEGER |
| **conversation\_updated\_at**  DATE-TIME |
| **created\_at**  DATE-TIME |
| **external\_id**  STRING |
| **id**  STRING |
| **notified\_at**  DATE-TIME |
| **part\_type**  STRING |
| **redacted**  BOOLEAN |
| **type**  STRING |
| **updated\_at**  DATE-TIME |

### conversations

The `conversations` table contains info about user conversations in your Intercom account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Intercom documentation](https://developers.intercom.com/intercom-api-reference/v2.5/reference/conversation-model)  [Intercom API method](https://developers.intercom.com/intercom-api-reference/v2.5/reference/list-conversations "Opens in new tab: Intercom API method") |

conversations table schema

|  |
| --- |
| **admin\_assignee\_id**  INTEGER |
| **contacts**  ARRAY This is a nested data structure:   - id: STRING - type: STRING |
| **conversation\_message**  OBJECT This is a nested data structure:   - attachments: ARRAY, which is also a nested data structure.   - content\_type: STRING   - filesize: INTEGER   - height: INTEGER   - name: STRING   - type: STRING   - url: STRING   - width: INTEGER - author: OBJECT, which is also a nested data structure.   - email: STRING   - id: STRING   - name: STRING   - type: STRING - body: STRING - delivered\_as: STRING - id: STRING - subject: STRING - type: STRING - url: STRING |
| **conversation\_rating**  OBJECT This is a nested data structure:   - contact: OBJECT, which is also a nested data structure.   - id: STRING   - type: STRING - created\_at: DATE-TIME - customer: OBJECT, which is also a nested data structure.   - id: STRING   - type: STRING - rating: INTEGER - remark: STRING - teammate: OBJECT, which is also a nested data structure.   - id: STRING   - type: STRING |
| **created\_at**  DATE-TIME |
| **custom\_attributes**  OBJECT |
| **customer\_first\_reply**  OBJECT  Click to expand customer\_first\_reply |  | | --- | | **created\_at**  DATE-TIME | | **type**  STRING | | **url**  STRING | |
| **customers**  ARRAY  Click to expand customers |  | | --- | | **id**  STRING | | **type**  STRING | |
| **first\_contact\_reply**  OBJECT This is a nested data structure:   - created\_at: DATE-TIME - type: STRING - url: STRING |
| **id**  STRING |
| **open**  BOOLEAN |
| **priority**  STRING |
| **read**  BOOLEAN |
| **sent\_at**  DATE-TIME |
| **sla\_applied**  OBJECT This is a nested data structure:   - sla\_name: STRING - sla\_status: STRING |
| **snoozed\_until**  DATE-TIME |
| **source**  OBJECT This is a nested data structure:   - attachments: ARRAY - author: OBJECT, which is also a nested data structure.   - email: STRING   - id: STRING   - name: STRING   - type: STRING - body: STRING - delivered\_as: STRING - id: STRING - redacted: BOOLEAN - subject: STRING - type: STRING - url: STRING |
| **state**  STRING |
| **statistics**  OBJECT This is a nested data structure:   - count\_assignments: INTEGER - count\_conversation\_parts: INTEGER - count\_reopens: INTEGER - first\_admin\_reply\_at: DATE-TIME - first\_assignment\_at: DATE-TIME - first\_close\_at: DATE-TIME - first\_contact\_reply\_at: DATE-TIME - last\_admin\_reply\_at: DATE-TIME - last\_assignment\_admin\_reply\_at: DATE-TIME - last\_assignment\_at: DATE-TIME - last\_close\_at: DATE-TIME - last\_closed\_by: DATE-TIME, which is also a nested data structure.   - email: STRING   - id: STRING   - name: STRING   - type: STRING - last\_closed\_by\_id: INTEGER - last\_contact\_reply\_at: DATE-TIME - median\_time\_to\_reply: INTEGER - time\_to\_admin\_reply: INTEGER - time\_to\_assignment: INTEGER - time\_to\_first\_close: INTEGER - time\_to\_last\_close: INTEGER - type: STRING |
| **tags**  ARRAY This is a nested data structure:   - applied\_at: DATE-TIME - applied\_by: OBJECT, which is also a nested data structure.   - id: STRING   - type: STRING - id: STRING - name: STRING - type: STRING |
| **team\_assignee\_id**  INTEGER |
| **teammates**  OBJECT This is a nested data structure:   - admins: ARRAY, which is also a nested data structure.   - id: STRING   - type: STRING - type: STRING |
| **title**  STRING |
| **type**  STRING |
| **updated\_at**  DATE-TIME |
| **user**  OBJECT This is a nested data structure:   - id: STRING - type: STRING |
| **waiting\_since**  DATE-TIME |

### segments

The `segments` table contains information about segments within your Intercom account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Intercom documentation](https://developers.intercom.com/intercom-api-reference/v2.5/reference/segment-model)  [Intercom API method](https://developers.intercom.com/intercom-api-reference/v2.5/reference/list-segments "Opens in new tab: Intercom API method") |

segments table schema

|  |
| --- |
| **count**  INTEGER |
| **created\_at**  DATE-TIME |
| **id**  STRING |
| **name**  STRING |
| **person\_type**  STRING |
| **type**  STRING |
| **updated\_at**  DATE-TIME |

### tags

The `tags` table contains information about tags within your Intercom account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Intercom documentation](https://developers.intercom.com/intercom-api-reference/v2.5/reference/tag-model)  [Intercom API method](https://developers.intercom.com/intercom-api-reference/v2.5/reference/list-tags-for-an-app "Opens in new tab: Intercom API method") |

tags table schema

|  |
| --- |
| **id**  STRING |
| **name**  STRING |
| **type**  STRING |

### teams

The `teams` table contains information about teams in your Intercom account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Intercom documentation](https://developers.intercom.com/intercom-api-reference/v2.5/reference/teams-model)  [Intercom API method](https://developers.intercom.com/intercom-api-reference/v2.5/reference/list-teams "Opens in new tab: Intercom API method") |

teams table schema

|  |
| --- |
| **admin\_ids**    ARRAY |
| **id**  STRING |
| **name**  STRING |
| **type**  STRING |
