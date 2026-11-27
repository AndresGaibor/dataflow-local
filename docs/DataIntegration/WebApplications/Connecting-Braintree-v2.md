---
title: "Braintree"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Braintree-v2.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Braintree

Braintree is an online and in-app payment platform.

Braintree integration replicates data using the [Braintree API](https://developers.braintreepayments.com/start/overview).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To set up your Braintree account, you need:

- Super Admin and API Access permissions in Braintree. This is required to create the API access token. For more information, see [Braintree user roles and permissions](https://developer.paypal.com/braintree/articles/control-panel/users-roles/managing-users-roles).
- Additionally, Braintree replicates transactions for the default merchant account in your Braintree instance.

To retrieve your private key:

1. Log into your Braintree account.
2. Click Account > My User.
3. Scroll down to the API Keys, Tokenization Keys, Encryption Keys section.
4. Click View Authorizations.
5. In the API Keys section, click Generate New API Key.
6. After the key has been generated, click the View link in the Private Key column.

   The Client Library Key page is displayed with your Braintree API credentials.

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
| Merchant ID | Merchant ID. |
| Private Key | Private key. |
| Public Key | Public key. |
| Environment | Enter a value: Development, QA, Sandbox, Production, or All. If left empty, Production is set as default. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### transactions

The `transactions` table contains info about the transactions in your Braintree account, including the transaction’s status.

**Note**: Our Braintree integration will only replicate transactions for the **default merchant account** in your Braintree instance. You can verify the merchant account set as the default by going to **Settings > Processing > Merchant Accounts** when signed into Braintree.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | created\_at |
| **Useful links** | [Braintree documentation](https://developers.braintreepayments.com/reference/request/transaction/search/java) |

transactions table schema

|  |
| --- |
| **amount**  NUMBER |
| **created\_at**  DATE-TIME |
| **credit\_card\_details**  OBJECT This is a nested data structure:   - card\_type: STRING - customer\_location: STRING |
| **currency\_iso\_code**  STRING |
| **customer\_details**  OBJECT This is a nested data structure:   - email: STRING - id: STRING |
| **disbursement\_details**  OBJECT  Click to expand disbursement\_details |
| **gateway\_rejection\_reason**  STRING |
| **id**  STRING |
| **merchant\_account\_id**  STRING |
| **order\_id**  STRING |
| **payment\_instrument\_type**  STRING |
| **paypal\_details**  OBJECT  Click to expand paypal\_details |
| **plan\_id**  STRING |
| **processor\_authorization\_code**  STRING |
| **processor\_response\_code**  STRING |
| **processor\_response\_text**  STRING |
| **recurring**  BOOLEAN |
| **refunded\_transaction\_id**  STRING |
| **service\_fee\_amount**  NUMBER |
| **settlement\_batch\_id**  STRING |
| **status**  STRING |
| **subscription\_details**  OBJECT This is a nested data structure:   - billing\_period\_end\_date: DATE-TIME - billing\_period\_start\_date: DATE-TIME |
| **subscription\_id**  STRING |
| **type**  STRING |
| **updated\_at**  DATE-TIME |
