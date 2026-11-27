---
title: "Mailjet"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Mailjet.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Mailjet

Mailjet is an email marketing and transactional email service provider.

Mailjet integration replicates data using the [Mailjet Email API](https://dev.mailjet.com/email/guides/#about-the-mailjet-api).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

You can connect only one account at a time. For example, you might have one primary Mailjet account and multiple subaccounts for different use cases. Qlik Talend Cloud replicates data using the API key and secret associated with the specific account you connect, either the primary account or a subaccount.

To create a subaccount:

1. Log into your [Mailjet](https://app.mailjet.com/signin) account.
2. Navigate to Account settings > API Key Management (Primary and Sub-account).
3. Click Create sub-account (API Key).
4. Enter a name for your new API Key name, and then click Create.
5. In Sub-account API Keys, copy and paste your API key and secret key into a secured file.

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
| API Secret | API secret. |

## Schema

Depending on your destination, table and column names may not appear as they are outlined below.

### messages

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | ID |
| **Replication Key** | Data |
| **Useful links** | [Mailjet documentation](https://dev.mailjet.com/email/reference/messages/#v3_get_message) |

### contacts

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | ID |
| **Replication Key** | Data |
| **Useful links** | [Mailjet documentation](https://dev.mailjet.com/email/reference/contacts/contact/#v3_get_contact) |

### contacts\_list

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | ID |
| **Replication Key** | Data |
| **Useful links** | [Mailjet documentation](https://dev.mailjet.com/email/reference/contacts/contact-list/#v3_get_contactslist) |

### list\_recipient

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | ID |
| **Replication Key** | Data |
| **Useful links** | [Mailjet documentation](https://dev.mailjet.com/email/reference/contacts/subscriptions/#v3_get_listrecipient) |

### campaigns

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | ID |
| **Replication Key** | Data |
| **Useful links** | [Mailjet documentation](https://dev.mailjet.com/email/reference/campaigns/sent-campaigns/#v3_get_campaign) |

### template

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | ID |
| **Replication Key** | Data |
| **Useful links** | [Mailjet documentation](https://dev.mailjet.com/email/reference/templates/#v3_get_template) |

### message\_information

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | ID |
| **Replication Key** | Data |
| **Useful links** | [Mailjet documentation](https://dev.mailjet.com/email/reference/messages/#v3_get_messageinformation) |

### geo\_statistics

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Replication Key** | Data |
| **Useful links** | [Mailjet documentation](https://dev.mailjet.com/email/reference/statistics/#v3_get_geostatistics) |

### click\_statistics

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | ID |
| **Replication Key** | Data |
| **Useful links** | [Mailjet documentation](https://dev.mailjet.com/email/reference/message-events/#v3_get_clickstatistics) |

### top\_link\_clicked

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | ID |
| **Replication Key** | Data |
| **Useful links** | [Mailjet documentation](https://dev.mailjet.com/email/reference/statistics/#v3_get_toplinkclicked) |

### campaign\_overview

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | ID |
| **Replication Key** | Data |
| **Useful links** | [Mailjet documentation](https://dev.mailjet.com/email/reference/messages/#v3_get_campaignoverview) |
