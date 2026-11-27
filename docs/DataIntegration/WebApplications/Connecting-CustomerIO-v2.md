---
title: "Customer.io"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-CustomerIO-v2.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Customer.io

Customer.io is a messaging platform.

Customer.io integration replicates data using the [Customer.io API](https://docs.customer.io/integrations/api/app/).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To retrieve your access token:

1. Log into your [Customer.io](https://fly.customer.io/login) account.
2. Navigate to Account Settings > API Credentials.
3. Under Manage API Credentials, search for your access token.
4. Copy and paste your access token into a secured file.

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
| Access Token | Access token. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### broadcasts

The `broadcasts` table contains info about the broadcasts in your Customer.io account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Keys** | updated |
| **Useful links** | [Customer.io documentation](https://docs.customer.io/integrations/api/app/#operation/listBroadcasts) |

### messages

The `messages` table contains info about the messages in your Customer.io account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Keys** | updated\_at |
| **Useful links** | [Customer.io documentation](https://docs.customer.io/integrations/api/app/#operation/listTransactional) |

### customers

The `customers` table contains info about the customers in your Customer.io account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Customer.io documentation](https://docs.customer.io/integrations/api/app/#operation/getPeopleEmail) |

### campaigns

The `campaigns` table contains info about the campaigns in your Customer.io account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Keys** | updated |
| **Useful links** | [Customer.io documentation](https://docs.customer.io/integrations/api/app/#tag/Campaigns) |

### newsletters

The `newsletters` table contains info about the newsletters in your Customer.io account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Keys** | updated |
| **Useful links** | [Customer.io documentation](https://docs.customer.io/integrations/api/app/#tag/Newsletters) |

### segments

The `segments` table contains info about the segments in your Customer.io account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Keys** | updated\_at |
| **Useful links** | [Customer.io documentation](https://docs.customer.io/integrations/api/app/#tag/Snippets) |

### messages

The `messages` table contains info about the messages in your Customer.io account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Customer.io documentation](https://docs.customer.io/integrations/api/app/#operation/listMessages) |

### exports

The `exports` table contains info about the exports in your Customer.io account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Keys** | updated\_at |
| **Useful links** | [Customer.io documentation](https://docs.customer.io/integrations/api/app/#tag/Exports) |

### activities

The `activities` table contains info about the activities in your Customer.io account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Customer.io documentation](https://docs.customer.io/integrations/api/app/#tag/Activities) |

### sender\_identities

The `sender_identities` table contains info about the sender identities in your Customer.io account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Customer.io documentation](https://docs.customer.io/integrations/api/app/#tag/Sender-Identities) |

### reporting\_webhooks

The `reporting_webhooks` table contains info about the reporting webhooks in your Customer.io account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Customer.io documentation](https://docs.customer.io/integrations/api/app/#tag/Reporting-Webhooks) |

### snippets

The `snippets` table contains info about the snippets in your Customer.io account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | name |
| **Replication Keys** | updated\_at |
| **Useful links** | [Customer.io documentation](https://docs.customer.io/integrations/api/app/#tag/Snippets) |

### ip\_addresses

The `ip_addresses` table contains info about the list of IP addresses in your Customer.io account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Customer.io documentation](https://docs.customer.io/integrations/api/app/#tag/Info) |

### collections

The `collections` table contains info about the collections in your Customer.io account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Keys** | updated\_at |
| **Useful links** | [Customer.io documentation](https://docs.customer.io/integrations/api/app/#operation/addCollection) |

### topics

The `topics` table contains info about the subscription topics in your Customer.io account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Customer.io documentation](https://docs.customer.io/integrations/api/app/#tag/Subscription-Center) |

### workspaces

The `workspaces` table contains info about the workspaces in your Customer.io account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Customer.io documentation](https://docs.customer.io/integrations/api/app/#tag/Workspaces) |

### types

The `types` table contains info about the object types in your Customer.io account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Customer.io documentation](https://docs.customer.io/integrations/api/app/#operation/getObjectTypes) |

### eps\_suppression

The `suppressions` table contains info about the ESP suppressions in your Customer.io account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Customer.io documentation](https://docs.customer.io/integrations/api/app/#tag/ESP-Suppression) |
