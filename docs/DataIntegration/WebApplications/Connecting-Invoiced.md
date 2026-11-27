---
title: "Invoiced"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Invoiced.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Invoiced

Invoiced offers tools to simplify invoicing, payment tracking, and account reconciliation.

Invoiced integration replicates data using the [Invoiced REST API](https://developer.invoiced.com/api).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To create an API key:

1. Log into your [Invoiced](https://app.invoiced.com/login) account.
2. Navigate to Settings > Integrations > Developer > New API Key.
3. Copy and paste your API key into a secured file.

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
| Connect to a sandbox environment | Select this option if you are connecting to a sandbox environment. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### credit\_notes

The `credit_notes` table contains info about the credit notes in your Invoiced account. A credit note represents a balance you owe to a customer.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Invoiced API method](https://developer.invoiced.com/api/#list-all-credit-notes "Opens in new tab: Invoiced API method") |

credit\_notes table foreign keys

| Join credit\_notes with | on |
| --- | --- |
| [customers](#customers) | ``` credit_notes.customer = customers.id ``` |
| [estimates](#estimates) | ``` credit_notes.customer = estimates.customer ```  ``` credit_notes.id = estimates.id ``` |
| [invoices](#invoices) | ``` credit_notes.customer = invoices.customer ```  ``` credit_notes.id = invoices.id ``` |
| [subscriptions](#subscriptions) | ``` credit_notes.customer = subscriptions.customer ``` |
| [transactions](#transactions) | ``` credit_notes.customer = transactions.customer ```  ``` credit_notes.id = transactions.id ``` |

credit\_notes table schema

|  |
| --- |
| **balance**  NUMBER |
| **closed**  BOOLEAN |
| **created\_at**  DATE-TIME |
| **currency**  STRING |
| **customer**  INTEGER |
| **date**  DATE-TIME |
| **discounts**  ARRAY |
| **draft**  BOOLEAN |
| **id**  INTEGER |
| **invoice**  INTEGER |
| **items**  ARRAY |
| **metadata**  OBJECT |
| **name**  STRING |
| **notes**  STRING |
| **number**  STRING |
| **paid**  BOOLEAN |
| **status**  STRING |
| **subtotal**  NUMBER |
| **taxes**  ARRAY |
| **total**  NUMBER |
| **updated\_at**  DATE-TIME |

### customers

The `customers` table contains info about the customers in your Invoiced account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Invoiced API method](https://developer.invoiced.com/api/#list-all-customers "Opens in new tab: Invoiced API method") |

customers table foreign keys

| Join customers with | on |
| --- | --- |
| [credit\_notes](#credit-notes) | ``` customers.id = credit_notes.customer ``` |
| [estimates](#estimates) | ``` customers.id = estimates.customer ``` |
| [invoices](#invoices) | ``` customers.id = invoices.customer ``` |
| [subscriptions](#subscriptions) | ``` customers.id = subscriptions.customer ``` |
| [transactions](#transactions) | ``` customers.id = transactions.customer ``` |

customers table schema

|  |
| --- |
| **address1**  STRING |
| **address2**  STRING |
| **attention\_to**  STRING |
| **autopay**  BOOLEAN |
| **chase**  BOOLEAN |
| **chasing\_cadence**  INTEGER |
| **city**  STRING |
| **country**  STRING |
| **created\_at**  DATE-TIME |
| **credit\_hold**  BOOLEAN |
| **credit\_limit**  NUMBER |
| **email**  STRING |
| **id**  INTEGER |
| **language**  STRING |
| **metadata**  OBJECT |
| **name**  STRING |
| **next\_chase\_step**  INTEGER |
| **notes**  STRING |
| **number**  STRING |
| **parent\_customer**  INTEGER |
| **payment\_source**  OBJECT |
| **payment\_terms**  STRING |
| **phone**  STRING |
| **postal\_code**  STRING |
| **sign\_up\_page**  INTEGER |
| **state**  STRING |
| **tax\_id**  STRING |
| **taxable**  BOOLEAN |
| **taxes**  ARRAY |
| **type**  STRING |
| **updated\_at**  DATE-TIME |

### estimates

The `estimates` table contains info about the estimates in your Invoiced account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Invoiced API method](https://developer.invoiced.com/api/#list-all-estimates "Opens in new tab: Invoiced API method") |

estimates table foreign keys

| Join estimates with | on |
| --- | --- |
| [credit\_notes](#credit-notes) | ``` estimates.customer = credit_notes.customer ```  ``` estimates.id = credit_notes.id ``` |
| [customers](#customers) | ``` estimates.customer = customers.id ``` |
| [invoices](#invoices) | ``` estimates.customer = invoices.customer ```  ``` estimates.id = invoices.id ``` |
| [subscriptions](#subscriptions) | ``` estimates.customer = subscriptions.customer ``` |
| [transactions](#transactions) | ``` estimates.customer = transactions.customer ```  ``` estimates.id = transactions.id ``` |

estimates table schema

|  |
| --- |
| **approval**  OBJECT |
| **approved**  BOOLEAN |
| **balance**  NUMBER |
| **closed**  BOOLEAN |
| **created\_at**  DATE-TIME |
| **currency**  STRING |
| **customer**  INTEGER |
| **date**  DATE-TIME |
| **deposit**  NUMBER |
| **deposit\_paid**  BOOLEAN |
| **discounts**  ARRAY |
| **draft**  BOOLEAN |
| **expiration\_date**  DATE-TIME |
| **id**  INTEGER |
| **invoice**  INTEGER |
| **items**  ARRAY |
| **metadata**  OBJECT |
| **name**  STRING |
| **notes**  STRING |
| **number**  STRING |
| **paid**  BOOLEAN |
| **payment\_terms**  STRING |
| **status**  STRING |
| **subtotal**  NUMBER |
| **taxes**  ARRAY |
| **total**  NUMBER |
| **updated\_at**  DATE-TIME |

### invoices

The `invoices` table contains info about the invoices in your Invoiced account. An invoice represents a balance owed to you by a customer.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Invoiced API method](https://developer.invoiced.com/api/#list-all-invoices "Opens in new tab: Invoiced API method") |

invoices table foreign keys

| Join invoices with | on |
| --- | --- |
| [credit\_notes](#credit-notes) | ``` invoices.customer = credit_notes.customer ```  ``` invoices.id = credit_notes.id ``` |
| [customers](#customers) | ``` invoices.customer = customers.id ``` |
| [estimates](#estimates) | ``` invoices.customer = estimates.customer ```  ``` invoices.id = estimates.id ``` |
| [subscriptions](#subscriptions) | ``` invoices.customer = subscriptions.customer ```  ``` invoices.subscription = subscriptions.id ``` |
| [transactions](#transactions) | ``` invoices.customer = transactions.customer ```  ``` invoices.id = transactions.id ``` |

invoices table schema

|  |
| --- |
| **attempt\_count**  INTEGER |
| **autopay**  BOOLEAN |
| **balance**  NUMBER |
| **closed**  BOOLEAN |
| **created\_at**  DATE-TIME |
| **currency**  STRING |
| **customer**  INTEGER |
| **date**  DATE-TIME |
| **discounts**  ARRAY |
| **draft**  BOOLEAN |
| **due\_date**  DATE-TIME |
| **id**  INTEGER |
| **items**  ARRAY |
| **metadata**  OBJECT |
| **name**  STRING |
| **needs\_attention**  BOOLEAN |
| **next\_payment\_attempt**  DATE-TIME |
| **notes**  STRING |
| **number**  STRING |
| **paid**  BOOLEAN |
| **payment\_terms**  STRING |
| **status**  STRING |
| **subscription**  INTEGER |
| **subtotal**  NUMBER |
| **taxes**  ARRAY |
| **total**  NUMBER |
| **updated\_at**  DATE-TIME |

### plans

The `plans` table contains info about the plans in your Invoiced account. A plan describes a fixed amount that is billed to customers over a recurring interval.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Invoiced API method](https://developer.invoiced.com/api/#list-all-plans "Opens in new tab: Invoiced API method") |

plans table schema

|  |
| --- |
| **amount**  NUMBER |
| **catalog\_item**  STRING |
| **created\_at**  INTEGER |
| **currency**  STRING |
| **description**  STRING |
| **id**  STRING |
| **interval**  STRING |
| **interval\_count**  INTEGER |
| **metadata**  OBJECT |
| **name**  STRING |
| **notes**  STRING |
| **object**  STRING |
| **pricing\_mode**  STRING |
| **quantity\_type**  STRING |
| **tiers**  OBJECT |
| **updated\_at**  INTEGER |

### subscriptions

The `subscriptions` table contains info about the subscriptions in your Invoiced account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Invoiced API method](https://developer.invoiced.com/api/#list-all-subscriptions "Opens in new tab: Invoiced API method") |

subscriptions table foreign keys

| Join subscriptions with | on |
| --- | --- |
| [credit\_notes](#credit-notes) | ``` subscriptions.customer = credit_notes.customer ``` |
| [customers](#customers) | ``` subscriptions.customer = customers.id ``` |
| [estimates](#estimates) | ``` subscriptions.customer = estimates.customer ``` |
| [invoices](#invoices) | ``` subscriptions.customer = invoices.customer ```  ``` subscriptions.id = invoices.subscription ``` |
| [transactions](#transactions) | ``` subscriptions.customer = transactions.customer ``` |

subscriptions table schema

|  |
| --- |
| **addons**  ARRAY |
| **approval**  OBJECT |
| **cancel\_at\_period\_end**  BOOLEAN |
| **canceled\_at**  DATE-TIME |
| **contract\_period\_end**  DATE-TIME |
| **contract\_period\_start**  DATE-TIME |
| **contract\_renewal\_cycles**  INTEGER |
| **contract\_renewal\_mode**  STRING |
| **created\_at**  DATE-TIME |
| **customer**  INTEGER |
| **cycles**  INTEGER |
| **discounts**  ARRAY |
| **id**  INTEGER |
| **metadata**  OBJECT |
| **mrr**  NUMBER |
| **period\_end**  DATE-TIME |
| **period\_start**  DATE-TIME |
| **plan**  STRING |
| **quantity**  NUMBER |
| **recurring\_total**  NUMBER |
| **renewed\_last**  DATE-TIME |
| **renews\_next**  DATE-TIME |
| **start\_date**  DATE-TIME |
| **status**  STRING |
| **taxes**  ARRAY |
| **updated\_at**  DATE-TIME |

### transactions

The `transactions` table contains info about the transactions in your Invoiced account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Invoiced API method](https://developer.invoiced.com/api/#list-all-transactions "Opens in new tab: Invoiced API method") |

transactions table foreign keys

| Join transactions with | on |
| --- | --- |
| [credit\_notes](#credit-notes) | ``` transactions.customer = credit_notes.customer ```  ``` transactions.id = credit_notes.id ``` |
| [customers](#customers) | ``` transactions.customer = customers.id ``` |
| [estimates](#estimates) | ``` transactions.customer = estimates.customer ```  ``` transactions.id = estimates.id ``` |
| [invoices](#invoices) | ``` transactions.customer = invoices.customer ```  ``` transactions.id = invoices.id ``` |
| [subscriptions](#subscriptions) | ``` transactions.customer = subscriptions.customer ``` |

transactions table schema

|  |
| --- |
| **amount**  NUMBER |
| **created\_at**  DATE-TIME |
| **credit\_note**  INTEGER |
| **currency**  STRING |
| **customer**  INTEGER |
| **date**  DATE-TIME |
| **failure\_reason**  STRING |
| **gateway**  STRING |
| **gateway\_id**  STRING |
| **id**  INTEGER |
| **invoice**  INTEGER |
| **metadata**  OBJECT |
| **method**  STRING |
| **notes**  STRING |
| **parent\_transaction**  INTEGER |
| **payment\_source**  OBJECT |
| **status**  STRING |
| **type**  STRING |
| **updated\_at**  DATE-TIME |
