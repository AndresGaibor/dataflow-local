---
title: "Klaviyo"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Klaviyo.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Klaviyo

Klaviyo is a marketing automation platform that automates eCommerce SMS and email marketing. It helps businesses acquire, retain and grow their customers by sending marketing emails.

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To generate the API key:

1. Log into your Klaviyo account.
2. Click your account name.
3. Go to Settings > API Keys.
4. Click Create API Key to create an API key.
5. In the Label column, click the pencil icon next to the API key you just created.
6. Enter a name for the API key. For example: `Qlik.integration`.
7. Click Create.
8. Copy the key.

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
| API Key | API key. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### bounce

The `bounce` table contains metrics related to `Bounced Email` events.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | timestamp |
| **Useful links** | [Klaviyo API method](https://developers.klaviyo.com/en/reference/metrics_api_overview) |

bounce table schema

|  |
| --- |
| **datetime**  STRING |
| **event\_name**  STRING |
| **event\_properties**  OBJECT |
| **id**  STRING |
| **object**  STRING |
| **person**  OBJECT |
| **statistic\_id**  STRING |
| **timestamp**  INTEGER |
| **uuid**  STRING |

### campaigns

The campaigns table contains info about the campaigns in your Klaviyo account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Klaviyo API method](https://apidocs.klaviyo.com/reference/campaigns#get-campaigns) |

campaigns table schema

|  |
| --- |
| **campaign\_type**  STRING |
| **created**  DATE-TIME |
| **from\_email**  STRING |
| **from\_name**  STRING |
| **id**  STRING |
| **is\_segmented**  BOOLEAN |
| **list\_id**  STRING |
| **message\_type**  STRING |
| **name**  STRING |
| **num\_recipients**  INTEGER |
| **object**  STRING |
| **send\_time**  DATE-TIME |
| **sent\_at**  DATE-TIME |
| **status**  STRING |
| **status\_id**  INTEGER |
| **status\_label**  STRING |
| **subject**  STRING |
| **template**  OBJECT This is a nested data structure:   - **html**: STRING - **id**: STRING - **object**: STRING |
| **template\_id**  STRING |
| **updated**  DATE-TIME |

### click

The `click` table contains metrics related to `Clicked Email` events.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | timestamp |
| **Useful links** | [Klaviyo API method](https://developers.klaviyo.com/en/reference/metrics_api_overview) |

click table schema

|  |
| --- |
| **datetime**  STRING |
| **event\_name**  STRING |
| **event\_properties**  OBJECT |
| **id**  STRING |
| **object**  STRING |
| **person**  OBJECT |
| **statistic\_id**  STRING |
| **timestamp**  INTEGER |
| **uuid**  STRING |

### clicked\_sms

The `clicked_sms` table contains metrics related to `Clicked SMS` events.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | timestamp |
| **Useful links** | [Klaviyo API method](https://developers.klaviyo.com/en/reference/metrics_api_overview) |

clicked\_sms table schema

|  |
| --- |
| **datetime**  STRING |
| **event\_name**  STRING |
| **event\_properties**  OBJECT |
| **id**  STRING |
| **object**  STRING |
| **person**  OBJECT |
| **statistic\_id**  STRING |
| **timestamp**  INTEGER |
| **uuid**  STRING |

### consented\_to\_receive

The `consented_to_receive` table contains metrics related to `Consented to Receive SMS` events.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | timestamp |
| **Useful links** | [Klaviyo API method](https://developers.klaviyo.com/en/reference/metrics_api_overview) |

consented\_to\_receive table schema

|  |
| --- |
| **datetime**  STRING |
| **event\_name**  STRING |
| **event\_properties**  OBJECT |
| **id**  STRING |
| **object**  STRING |
| **person**  OBJECT |
| **statistic\_id**  STRING |
| **timestamp**  INTEGER |
| **uuid**  STRING |

### dropped\_email

The `dropped_email` table contains metrics related to `Clicked Email` events.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | timestamp |
| **Useful links** | [Klaviyo API method](https://developers.klaviyo.com/en/reference/metrics_api_overview) |

dropped\_email table schema

|  |
| --- |
| **datetime**  STRING |
| **event\_name**  STRING |
| **event\_properties**  OBJECT |
| **id**  STRING |
| **object**  STRING |
| **person**  OBJECT |
| **statistic\_id**  STRING |
| **timestamp**  INTEGER |
| **uuid**  STRING |

### failed\_to\_deliver

The `failed_to_deliver` table contains metrics related to `Failed to Deliver SMS` events.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | timestamp |
| **Useful links** | [Klaviyo API method](https://developers.klaviyo.com/en/reference/metrics_api_overview) |

failed\_to\_deliver table schema

|  |
| --- |
| **datetime**  STRING |
| **event\_name**  STRING |
| **event\_properties**  OBJECT |
| **id**  STRING |
| **object**  STRING |
| **person**  OBJECT |
| **statistic\_id**  STRING |
| **timestamp**  INTEGER |
| **uuid**  STRING |

### failed\_to\_deliver\_automated\_response

The `failed_to_deliver_automated_response` table contains metrics related to `Failed to Deliver Automated Response SMS` events.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | timestamp |
| **Useful links** | [Klaviyo API method](https://developers.klaviyo.com/en/reference/metrics_api_overview) |

failed\_to\_deliver\_automated\_response table schema

|  |
| --- |
| **datetime**  STRING |
| **event\_name**  STRING |
| **event\_properties**  OBJECT |
| **id**  STRING |
| **object**  STRING |
| **person**  OBJECT |
| **statistic\_id**  STRING |
| **timestamp**  INTEGER |
| **uuid**  STRING |

### global\_exclusions

The global\_exclusions table contains info about the global exclusions in your Klaviyo account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | email |
| **Useful links** | [Klaviyo API method](https://apidocs.klaviyo.com/reference/lists-segments#get-global-exclusions) |

global\_exclusions table schema

|  |
| --- |
| **email**  STRING |
| **object**  STRING |
| **reason**  STRING |
| **timestamp**  STRING |

### lists

The lists table contains info about the lists in your Klaviyo account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Klaviyo API method](https://apidocs.klaviyo.com/reference/lists-segments#get-lists) |

lists table schema

|  |
| --- |
| **created**  STRING |
| **folder**  STRING |
| **id**  STRING |
| **list\_type**  STRING |
| **name**  STRING |
| **object**  STRING |
| **person\_count**  INTEGER |
| **updated**  STRING |

### mark\_as\_spam

The `mark_as_spam` table contains metrics related to `Marked Email as Spam` events.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | timestamp |
| **Useful links** | [Klaviyo API method](https://developers.klaviyo.com/en/reference/metrics_api_overview) |

mark\_as\_spam table schema

|  |
| --- |
| **datetime**  STRING |
| **event\_name**  STRING |
| **event\_properties**  OBJECT |
| **id**  STRING |
| **object**  STRING |
| **person**  OBJECT |
| **statistic\_id**  STRING |
| **timestamp**  INTEGER |
| **uuid**  STRING |

### open

The `open` table contains metrics related to `Opened Email` events.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | timestamp |
| **Useful links** | [Klaviyo API method](https://developers.klaviyo.com/en/reference/metrics_api_overview) |

open table schema

|  |
| --- |
| **datetime**  STRING |
| **event\_name**  STRING |
| **event\_properties**  OBJECT |
| **id**  STRING |
| **object**  STRING |
| **person**  OBJECT |
| **statistic\_id**  STRING |
| **timestamp**  INTEGER |
| **uuid**  STRING |

### receive

The `receive` table contains metrics related to `Received Email` events.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | timestamp |
| **Useful links** | [Klaviyo API method](https://developers.klaviyo.com/en/reference/metrics_api_overview) |

receive table schema

|  |
| --- |
| **datetime**  STRING |
| **event\_name**  STRING |
| **event\_properties**  OBJECT |
| **id**  STRING |
| **object**  STRING |
| **person**  OBJECT |
| **statistic\_id**  STRING |
| **timestamp**  INTEGER |
| **uuid**  STRING |

### received\_automated\_response

The `received_automated_response` table contains metrics related to `Received Automated Response SMS` events.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | timestamp |
| **Useful links** | [Klaviyo API method](https://developers.klaviyo.com/en/reference/metrics_api_overview) |

received\_automated\_response table schema

|  |
| --- |
| **datetime**  STRING |
| **event\_name**  STRING |
| **event\_properties**  OBJECT |
| **id**  STRING |
| **object**  STRING |
| **person**  OBJECT |
| **statistic\_id**  STRING |
| **timestamp**  INTEGER |
| **uuid**  STRING |

### received\_sms

The `received_sms` table contains metrics related to `Received SMS` events.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | timestamp |
| **Useful links** | [Klaviyo API method](https://developers.klaviyo.com/en/reference/metrics_api_overview) |

received\_sms table schema

|  |
| --- |
| **datetime**  STRING |
| **event\_name**  STRING |
| **event\_properties**  OBJECT |
| **id**  STRING |
| **object**  STRING |
| **person**  OBJECT |
| **statistic\_id**  STRING |
| **timestamp**  INTEGER |
| **uuid**  STRING |

### sent\_sms

The `sent_sms` table contains metrics related to `Sent SMS` events.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | timestamp |
| **Useful links** | [Klaviyo API method](https://developers.klaviyo.com/en/reference/metrics_api_overview) |

sent\_sms table schema

|  |
| --- |
| **datetime**  STRING |
| **event\_name**  STRING |
| **event\_properties**  OBJECT |
| **id**  STRING |
| **object**  STRING |
| **person**  OBJECT |
| **statistic\_id**  STRING |
| **timestamp**  INTEGER |
| **uuid**  STRING |

### subscribe\_list

The `subscribe_list` table contains metrics related to `Subscribed to List` events.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Replication Key** | timestamp |
| **Useful links** | [Klaviyo API method](https://developers.klaviyo.com/en/reference/metrics_api_overview) |

subscribe\_list table schema

|  |
| --- |
| **datetime**  STRING |
| **event\_name**  STRING |
| **event\_properties**  OBJECT |
| **id**  STRING |
| **object**  STRING |
| **person**  OBJECT |
| **statistic\_id**  STRING |
| **timestamp**  INTEGER |
| **uuid**  STRING |

### unsub\_list

The `unsub_list` table contains metrics related to `Unsubscribed from List` events.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Replication Key** | timestamp |
| **Useful links** | [Klaviyo API method](https://developers.klaviyo.com/en/reference/metrics_api_overview) |

unsub\_list table schema

|  |
| --- |
| **datetime**  STRING |
| **event\_name**  STRING |
| **event\_properties**  OBJECT |
| **id**  STRING |
| **object**  STRING |
| **person**  OBJECT |
| **statistic\_id**  STRING |
| **timestamp**  INTEGER |
| **uuid**  STRING |

### unsubscribe

The `unsubscribe` table contains metrics related to `Unsubscribed` events.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Replication Key** | timestamp |
| **Useful links** | [Klaviyo API method](https://developers.klaviyo.com/en/reference/metrics_api_overview) |

unsubscribe table schema

|  |
| --- |
| **datetime**  STRING |
| **event\_name**  STRING |
| **event\_properties**  OBJECT |
| **id**  STRING |
| **object**  STRING |
| **person**  OBJECT |
| **statistic\_id**  STRING |
| **timestamp**  INTEGER |
| **uuid**  STRING |

### unsubscribed\_from\_sms

The `unsubscribed_from_sms` table contains metrics related to `Unsubscribed from SMS` events.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | timestamp |
| **Useful links** | [Klaviyo API method](https://developers.klaviyo.com/en/reference/metrics_api_overview) |

unsubscribed\_from\_sms table schema

|  |
| --- |
| **datetime**  STRING |
| **event\_name**  STRING |
| **event\_properties**  OBJECT |
| **id**  STRING |
| **object**  STRING |
| **person**  OBJECT |
| **statistic\_id**  STRING |
| **timestamp**  INTEGER |
| **uuid**  STRING |

### update\_email\_preferences

The `update_email_preferences` table contains metrics related to `Updated Email Preferences` events.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Replication Key** | timestamp |
| **Useful links** | [Klaviyo API method](https://developers.klaviyo.com/en/reference/metrics_api_overview) |

update\_email\_preferences table schema

|  |
| --- |
| **datetime**  STRING |
| **event\_name**  STRING |
| **event\_properties**  OBJECT |
| **id**  STRING |
| **object**  STRING |
| **person**  OBJECT |
| **statistic\_id**  STRING |
| **timestamp**  INTEGER |
| **uuid**  STRING |
