---
title: "SaaSOptics"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-SaaSOptics.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# SaaSOptics

SaaSOptics is a subscription management platform that automates financial operations for growing B2B SaaS businesses.

SaaSOptics integration replicates data using the [SaaSOptics REST API](https://developers.maxio.com/http/getting-started/about-the-api/tips-and-best-practices).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

SaaSOptics is now part of Maxio.

You need administrator permissions in your SaaSOptics account.

Only SaaSOptics account admins can generate the first API token for you. After an admin generates the initial token, you can regenerate your token as needed.

To generate an API token:

1. Log into your [SaaSOptics](https://www.maxio.com/login) account.
2. Navigate to Admin > Settings > API Tokens.
3. Enter a name for you API token and click Create API Token.
4. Copy and paste your API token into a secured file.

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
| Account Name | You can find your account name in the URL you use to access your SaaSOptics account. If the URL is https://your-subdomain.saasoptics.com/your-account-name/so, the account name is your-account-name. |
| Server Subdomain | You can find your server subdomain in the URL you use to access your SaaSOptics account. If the URL is https://your-subdomain.saasoptics.com/your-account-name/so, the subdomain is your-subdomain. |
| Token | API token. |
| Date Window Size | The size of the date window for retrieving data. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### accounts

The `accounts` table contains info about accounts, or records in your Chart of Accounts, in SaaSOptics.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [SaaSOptics API method](https://saasoptics.zendesk.com/hc/en-us/articles/115013751507-Accounts-R- "Opens in new tab: SaaSOptics API method") |

accounts table schema

|  |
| --- |
| **account\_type**  STRING |
| **id**  INTEGER |
| **intacct\_id**  STRING |
| **intacct\_modified**  DATE-TIME |
| **intacct\_recordno**  INTEGER |
| **name**  STRING |
| **netsuite\_id**  STRING |
| **source\_system**  STRING |

### auto\_renewal\_profiles

The `auto_renewal_profiles` table contains info about auto-renwal profiles, or transaction renewal rules in your SaaSOptics account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [SaaSOptics API method](https://saasoptics.zendesk.com/hc/en-us/articles/115013918268-Auto-Renewal-Profiles-R- "Opens in new tab: SaaSOptics API method") |

auto\_renewal\_profiles table schema

|  |
| --- |
| **days**  INTEGER |
| **generate\_revenue**  BOOLEAN |
| **id**  INTEGER |
| **months**  INTEGER |
| **name**  STRING |
| **recognize**  BOOLEAN |

### billing\_descriptions

The `billing_descriptions` table contains info about billing line item descriptions.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [SaaSOptics API method](https://saasoptics.zendesk.com/hc/en-us/articles/115013751807-Billing-Line-Item-Descriptions-R- "Opens in new tab: SaaSOptics API method") |

billing\_descriptions table schema

|  |
| --- |
| **contents**  STRING |
| **id**  INTEGER |
| **name**  STRING |
| **notes**  STRING |

### billing\_methods

The `billing_methods` table contains info about billing methods, which are used to specify billing/invoice frequencies for transactions in your SaaSOptics account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [SaaSOptics API method](https://saasoptics.zendesk.com/hc/en-us/articles/115003604433-Billing-Methods-R- "Opens in new tab: SaaSOptics API method") |

billing\_methods table schema

|  |
| --- |
| **id**  INTEGER |
| **name**  STRING |

### contracts

The `contracts` table contains info about the contracts in your SaaSOptics account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | modified |
| **Useful links** | [SaaSOptics API method](https://saasoptics.zendesk.com/hc/en-us/articles/115013751607-Contracts-CRUD- "Opens in new tab: SaaSOptics API method") |

contracts table schema

|  |
| --- |
| **billing\_profile**  OBJECT This is a nested data structure:   - account\_number: STRING - addr1: STRING - addr2: STRING - addr3: STRING - alt\_contact: STRING - alt\_phone: STRING - city: STRING - company\_name: STRING - contact: STRING - country: STRING - currency: INTEGER - customer\_type\_ref\_fullname: STRING - default\_credit\_memo\_template: INTEGER - default\_invoice\_template: INTEGER - edit\_sequence: STRING - email: STRING - entity\_use\_code: INTEGER - fax: STRING - first\_name: STRING - full\_name: STRING - invoice\_email\_preference: BOOLEAN - invoice\_print\_preference: BOOLEAN - is\_active: BOOLEAN - job\_description: STRING - job\_end\_date: DATE-TIME - job\_projected\_end\_date: DATE-TIME - job\_start\_date: DATE-TIME - job\_status: STRING - job\_type: INTEGER - last\_name: STRING - name: STRING - parent\_id: STRING - payment\_terms: INTEGER - phone: STRING - resale\_number: STRING - sales\_rep: INTEGER - salutation: STRING - shipping\_addr1: STRING - shipping\_addr2: STRING - shipping\_addr3: STRING - shipping\_city: STRING - shipping\_country: STRING - shipping\_state: STRING - shipping\_zip\_code: STRING - state: STRING - zip\_code: STRING |
| **channel**  STRING |
| **customer**  INTEGER |
| **email**  STRING |
| **entry\_date**  DATE-TIME |
| **id**  INTEGER |
| **is\_job**  BOOLEAN |
| **lead\_date**  DATE-TIME |
| **lead\_source**  STRING |
| **modified**  DATE-TIME |
| **notes**  STRING |
| **number**  STRING |
| **number\_field1**  NUMBER |
| **number\_field2**  NUMBER |
| **qb\_job\_id**  STRING |
| **register**  INTEGER |
| **sf\_id**  STRING |
| **text\_field1**  STRING |
| **text\_field2**  STRING |
| **unbalanced\_revenue\_exception**  BOOLEAN |

### country\_codes

The `country_codes` table contains info about country codes.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [SaaSOptics API method](https://saasoptics.zendesk.com/hc/en-us/articles/115003604453-Country-Codes-R- "Opens in new tab: SaaSOptics API method") |

country\_codes table schema

|  |
| --- |
| **code**  STRING |
| **id**  INTEGER |
| **name**  STRING |

### currency\_codes

The `currency_codes` table contains info about currency codes.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | code |
| **Useful links** | [SaaSOptics API method](https://saasoptics.zendesk.com/hc/en-us/articles/115003604453-Country-Codes-R- "Opens in new tab: SaaSOptics API method") |

currency\_codes table schema

|  |
| --- |
| **code**  STRING |
| **name**  STRING |

### customers

The `customers` table contains info about customers.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | modified |
| **Useful links** | [SaaSOptics API method](https://saasoptics.zendesk.com/hc/en-us/articles/115013751587-Customers-CRUD- "Opens in new tab: SaaSOptics API method") |

customers table schema

|  |
| --- |
| **autopay\_enrollment**  STRING |
| **billing\_profile**  OBJECT This is a nested data structure:   - account\_number: STRING - addr1: STRING - addr2: STRING - addr3: STRING - alt\_contact: STRING - alt\_phone: STRING - avatax\_address\_validation\_timestamp: DATE-TIME - city: STRING - company\_name: STRING - contact: STRING - country: STRING - currency: INTEGER - customer\_type: INTEGER - default\_class: INTEGER - default\_credit\_memo\_template: INTEGER - default\_invoice\_template: INTEGER - edit\_sequence: STRING - email: STRING - entity\_use\_code: INTEGER - fax: STRING - first\_name: STRING - full\_name: STRING - invoice\_email\_preference: BOOLEAN - invoice\_print\_preference: BOOLEAN - is\_active: BOOLEAN - last\_name: STRING - last\_updated\_by\_qb: BOOLEAN - name: STRING - payment\_method: INTEGER - payment\_terms: INTEGER - phone: STRING - resale\_number: STRING - sales\_rep: INTEGER - sales\_rep\_fullname: STRING - sales\_tax\_code: INTEGER - salutation: STRING - shipping\_addr1: STRING - shipping\_addr2: STRING - shipping\_addr3: STRING - shipping\_city: STRING - shipping\_country: STRING - shipping\_state: STRING - shipping\_zip\_code: STRING - state: STRING - zip\_code: STRING |
| **cc\_email**  STRING |
| **code**  STRING |
| **crm\_id**  STRING |
| **default\_autorenewal\_profile**  STRING |
| **default\_email\_from\_so**  BOOLEAN |
| **default\_enable\_ach\_payment**  BOOLEAN |
| **default\_enable\_cc\_payment**  BOOLEAN |
| **default\_theme**  INTEGER |
| **do\_not\_sync**  BOOLEAN |
| **einvoicing\_id**  STRING |
| **email**  STRING |
| **enable\_autopay**  BOOLEAN |
| **escalation\_email**  STRING |
| **id**  INTEGER |
| **industry**  STRING |
| **is\_active**  BOOLEAN |
| **market**  STRING |
| **modified**  DATE-TIME |
| **name**  STRING |
| **notes**  STRING |
| **number**  STRING |
| **number\_field1**  NUMBER |
| **number\_field2**  NUMBER |
| **number\_field3**  NUMBER |
| **parent**  INTEGER |
| **qb\_id**  STRING |
| **recurly\_id**  STRING |
| **segment**  STRING |
| **sf\_default\_renewal\_opportunity\_rule**  INTEGER |
| **sf\_id**  STRING |
| **sf\_opportunity\_price\_book\_id**  STRING |
| **sf\_owner\_id**  STRING |
| **stripe\_id**  STRING |
| **subsegment**  STRING |
| **text\_field1**  STRING |
| **text\_field2**  STRING |
| **text\_field3**  STRING |
| **unbalanced\_revenue\_exception**  BOOLEAN |

### deleted\_contracts

The `deleted_contracts` table contains a list of deleted SaaSOptics contracts.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | deleted |
| **Useful links** |  |

deleted\_contracts table schema

|  |
| --- |
| **deleted**  DATE-TIME |
| **deleted\_by**  STRING |
| **id**  INTEGER |

### deleted\_invoices

The `deleted_invoices` table contains a list of deleted SaaSOptics invoices.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | deleted |
| **Useful links** |  |

deleted\_invoices table schema

|  |
| --- |
| **deleted**  DATE-TIME |
| **deleted\_by**  STRING |
| **id**  INTEGER |

### deleted\_revenue\_entries

The `deleted_revenue_entries` table contains a list of deleted SaaSOptics revenue entries.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | deleted |
| **Useful links** |  |

deleted\_revenue\_entries table schema

|  |
| --- |
| **deleted**  DATE-TIME |
| **deleted\_by**  STRING |
| **id**  INTEGER |

### deleted\_transactions

The `deleted_transactions` table contains a list of deleted SaaSOptics transactions.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | deleted |
| **Useful links** |  |

deleted\_transactions table schema

|  |
| --- |
| **deleted**  DATE-TIME |
| **deleted\_by**  STRING |
| **id**  INTEGER |

### invoices

The `invoices` table contains info about invoices in your SaaSOptics account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | auditentry\_modified |
| **Useful links** | [SaaSOptics API method](https://saasoptics.zendesk.com/hc/en-us/articles/115013918148-Invoices-CRUD- "Opens in new tab: SaaSOptics API method") |

invoices table schema

|  |
| --- |
| **applied\_amount**  NUMBER |
| **auditentry\_created**  DATE-TIME |
| **auditentry\_created\_by\_name**  STRING |
| **auditentry\_modified**  DATE-TIME |
| **auditentry\_modified\_by\_name**  STRING |
| **auditentry\_qb\_created**  DATE-TIME |
| **auditentry\_qb\_modified**  DATE-TIME |
| **avatax\_commit\_timestamp**  DATE-TIME |
| **avatax\_id**  STRING |
| **avatax\_modify\_timestamp**  DATE-TIME |
| **avatax\_reconciliation\_status**  STRING |
| **avatax\_status**  STRING |
| **balance**  NUMBER |
| **billing\_addr1**  STRING |
| **billing\_addr2**  STRING |
| **billing\_addr3**  STRING |
| **billing\_city**  STRING |
| **billing\_country**  STRING |
| **billing\_state**  STRING |
| **billing\_zip\_code**  STRING |
| **contract**  INTEGER |
| **date**  DATE-TIME |
| **deleted\_in\_qb**  BOOLEAN |
| **do\_not\_sync**  BOOLEAN |
| **due\_date**  DATE-TIME |
| **ei\_theme**  INTEGER |
| **email\_from\_so**  BOOLEAN |
| **enable\_ach\_payment**  BOOLEAN |
| **enable\_cc\_payment**  BOOLEAN |
| **exported\_date**  DATE-TIME |
| **external\_id**  STRING |
| **foreign\_exchange\_rate**  NUMBER |
| **id**  INTEGER |
| **ignore\_date\_when\_syncing**  BOOLEAN |
| **is\_paid**  BOOLEAN |
| **line\_items**  ARRAY This is a nested data structure:   - deleted\_in\_qb: BOOLEAN - exported\_date: DATE-TIME - external\_id: STRING - home\_amount: NUMBER - id: INTEGER - invoice: INTEGER - item: INTEGER - local\_amount: NUMBER - modified: DATE-TIME - no\_transaction\_permitted: BOOLEAN - notes: STRING - number: STRING - qb\_class: INTEGER - qb\_time\_modified: DATE-TIME - qb\_txn\_line\_id: STRING - quantity: NUMBER - recurly\_id: STRING - refund\_of: INTEGER - refund\_of\_stripe\_id: STRING - sf\_id: STRING - stripe\_id: STRING - sync\_date: DATE-TIME - transaction: INTEGER |
| **memo**  STRING |
| **number**  STRING |
| **other**  STRING |
| **po\_number**  STRING |
| **qb\_ar\_account**  INTEGER |
| **qb\_class**  INTEGER |
| **qb\_currency**  INTEGER |
| **qb\_customer\_message**  INTEGER |
| **qb\_number**  STRING |
| **qb\_payment\_terms**  INTEGER |
| **qb\_sales\_rep**  INTEGER |
| **qb\_template**  INTEGER |
| **qb\_txn\_id**  STRING |
| **recurly\_id**  STRING |
| **refund\_of**  INTEGER |
| **sales\_tax**  NUMBER |
| **sales\_tax\_percentage**  NUMBER |
| **sf\_id**  STRING |
| **ship\_date**  DATE-TIME |
| **shipping\_addr1**  STRING |
| **shipping\_addr2**  STRING |
| **shipping\_addr3**  STRING |
| **shipping\_city**  STRING |
| **shipping\_country**  STRING |
| **shipping\_state**  STRING |
| **shipping\_zip\_code**  STRING |
| **stripe\_id**  STRING |
| **stripe\_refund\_id**  STRING |
| **subtotal**  NUMBER |
| **sync\_date**  DATE-TIME |
| **to\_be\_emailed**  BOOLEAN |
| **to\_be\_printed**  BOOLEAN |
| **type**  STRING |

### items

The `items` table contains info about items, which are products and services you sell.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | modified |
| **Useful links** | [SaaSOptics API method](https://saasoptics.zendesk.com/hc/en-us/articles/115013751567-Items-R- "Opens in new tab: SaaSOptics API method") |

items table schema

|  |
| --- |
| **asset\_account**  INTEGER |
| **avatax\_id**  STRING |
| **avatax\_sales\_tax\_code**  STRING |
| **billing\_description**  STRING |
| **billing\_method**  INTEGER |
| **code**  STRING |
| **create\_revenue**  BOOLEAN |
| **default\_duration**  STRING |
| **description**  STRING |
| **enable\_create\_transactions**  BOOLEAN |
| **enforce\_start\_date\_after\_end\_date**  BOOLEAN |
| **gl\_created**  DATE-TIME |
| **gl\_description**  STRING |
| **gl\_is\_active**  BOOLEAN |
| **gl\_modified**  DATE-TIME |
| **gl\_name**  STRING |
| **id**  INTEGER |
| **income\_account**  INTEGER |
| **intacct\_id**  STRING |
| **intacct\_modified**  DATE-TIME |
| **intacct\_recordno**  STRING |
| **is\_active**  BOOLEAN |
| **is\_discount**  BOOLEAN |
| **is\_sales\_tax**  BOOLEAN |
| **is\_taxable**  BOOLEAN |
| **liability\_account**  INTEGER |
| **modified**  DATE-TIME |
| **name**  STRING |
| **needs\_so\_profile**  BOOLEAN |
| **netsuite\_id**  STRING |
| **netsuite\_modified**  DATE-TIME |
| **normalized\_term**  STRING |
| **product\_family**  STRING |
| **qb\_account**  INTEGER |
| **qb\_id**  STRING |
| **qb\_only**  BOOLEAN |
| **qb\_sales\_tax\_code**  STRING |
| **recurly\_id**  STRING |
| **recurring**  BOOLEAN |
| **renew\_all\_open\_transactions**  BOOLEAN |
| **renew\_using\_same\_item**  BOOLEAN |
| **revenue\_recognition\_method**  INTEGER |
| **sf\_do\_not\_sync**  BOOLEAN |
| **source\_system**  STRING |
| **stripe\_id**  STRING |
| **sync\_invoices**  BOOLEAN |
| **transaction\_end\_date**  DATE-TIME |
| **transaction\_start\_date**  DATE-TIME |
| **wizard\_enabled**  BOOLEAN |

### payment\_terms

The `payment_terms` table contains info about invoice payment terms.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [SaaSOptics API method](https://saasoptics.zendesk.com/hc/en-us/articles/115003642673-Payment-Terms-R- "Opens in new tab: SaaSOptics API method") |

payment\_terms table schema

|  |
| --- |
| **id**  INTEGER |
| **intacct\_id**  STRING |
| **intacct\_modified**  DATE-TIME |
| **intacct\_recordno**  INTEGER |
| **is\_active**  BOOLEAN |
| **name**  STRING |
| **netsuite\_id**  STRING |
| **num\_days**  NUMBER |

### registers

The `registers` table contains info about registers, which can contain one or more [contracts](#contracts).

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | modified |
| **Useful links** | [SaaSOptics API method](https://saasoptics.zendesk.com/hc/en-us/articles/115013751707-Registers-R- "Opens in new tab: SaaSOptics API method") |

registers table schema

|  |
| --- |
| **currency\_code**  STRING |
| **default\_qb\_ar\_account**  STRING |
| **generated\_invoice\_number\_prefix**  STRING |
| **id**  INTEGER |
| **modified**  DATE-TIME |
| **name**  STRING |

### revenue\_entries

The `revenue_entries` table contains info about revenue entries.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | modified |
| **Useful links** | [SaaSOptics API method](https://saasoptics.zendesk.com/hc/en-us/articles/115003674273-Revenue-Entries-R- "Opens in new tab: SaaSOptics API method") |

revenue\_entries table schema

|  |
| --- |
| **end\_date**  DATE-TIME |
| **home\_amount**  NUMBER |
| **id**  INTEGER |
| **local\_amount**  NUMBER |
| **modified**  DATE-TIME |
| **start\_date**  DATE-TIME |
| **transaction**  INTEGER |

### revenue\_recognition\_methods

The `revenue_recognition_methods` table contains info about revenue recognition methods, which are the methods for calculating and generating revenue records for a transaction.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [SaaSOptics API method](https://saasoptics.zendesk.com/hc/en-us/articles/115003617774-Revenue-Recognition-Methods-R- "Opens in new tab: SaaSOptics API method") |

revenue\_recognition\_methods table schema

|  |
| --- |
| **id**  INTEGER |
| **name**  STRING |

### sales\_orders

The `sales_orders` table contains info about sales orders, which have historically been synced in through the Salesforce integration and processed into financial records within SaaSOptics.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | created |
| **Useful links** | [SaaSOptics API method](https://saasoptics.zendesk.com/hc/en-us/articles/360000738813-Sales-Orders-CR- "Opens in new tab: SaaSOptics API method") |

sales\_orders table schema

|  |
| --- |
| **close\_date**  DATE-TIME |
| **contract\_channel**  STRING |
| **contract\_email**  STRING |
| **contract\_entry\_date**  DATE-TIME |
| **contract\_is\_job**  BOOLEAN |
| **contract\_lead\_date**  DATE-TIME |
| **contract\_lead\_source**  STRING |
| **contract\_notes**  STRING |
| **contract\_number**  STRING |
| **contract\_number\_field1**  NUMBER |
| **contract\_number\_field2**  NUMBER |
| **contract\_register\_name**  STRING |
| **contract\_sf\_id**  STRING |
| **contract\_text\_field1**  STRING |
| **contract\_text\_field2**  STRING |
| **contract\_unbalanced\_revenue\_exception**  BOOLEAN |
| **created**  DATE-TIME |
| **created\_by\_username**  STRING |
| **customer\_account\_number**  STRING |
| **customer\_alt\_contact**  STRING |
| **customer\_alt\_phone**  STRING |
| **customer\_autopay\_enrollment**  STRING |
| **customer\_billing\_addr3**  STRING |
| **customer\_billing\_city**  STRING |
| **customer\_billing\_country**  STRING |
| **customer\_billing\_state**  STRING |
| **customer\_billing\_street**  STRING |
| **customer\_billing\_zip\_code**  STRING |
| **customer\_code**  STRING |
| **customer\_contact**  STRING |
| **customer\_crm\_id**  STRING |
| **customer\_currency**  STRING |
| **customer\_default\_autorenewal\_profile**  STRING |
| **customer\_default\_cadence\_template**  STRING |
| **customer\_default\_email\_from\_so**  STRING |
| **customer\_default\_enable\_ach\_payment**  BOOLEAN |
| **customer\_default\_enable\_cc\_payment**  BOOLEAN |
| **customer\_default\_invoice\_template**  STRING |
| **customer\_default\_theme**  STRING |
| **customer\_do\_not\_sync**  BOOLEAN |
| **customer\_email**  STRING |
| **customer\_enable\_autopay**  BOOLEAN |
| **customer\_entity\_use\_code**  STRING |
| **customer\_fax**  STRING |
| **customer\_first\_name**  STRING |
| **customer\_industry**  STRING |
| **customer\_invoice\_email\_preference**  BOOLEAN |
| **customer\_invoice\_print\_preference**  BOOLEAN |
| **customer\_item\_sales\_tax**  STRING |
| **customer\_last\_name**  STRING |
| **customer\_market**  STRING |
| **customer\_name**  STRING |
| **customer\_notes**  STRING |
| **customer\_number**  STRING |
| **customer\_number\_field1**  NUMBER |
| **customer\_number\_field2**  NUMBER |
| **customer\_number\_field3**  NUMBER |
| **customer\_parent**  STRING |
| **customer\_payment\_terms**  STRING |
| **customer\_phone**  STRING |
| **customer\_resale\_number**  STRING |
| **customer\_sales\_rep**  STRING |
| **customer\_sales\_tax\_code**  STRING |
| **customer\_salutation**  STRING |
| **customer\_segment**  STRING |
| **customer\_sf\_default\_renewal\_opportunity\_rule**  STRING |
| **customer\_sf\_opportunity\_price\_book\_id**  STRING |
| **customer\_sf\_owner\_id**  STRING |
| **customer\_sfdc\_object\_id**  STRING |
| **customer\_shipping\_addr3**  STRING |
| **customer\_shipping\_city**  STRING |
| **customer\_shipping\_country**  STRING |
| **customer\_shipping\_state**  STRING |
| **customer\_shipping\_street**  STRING |
| **customer\_shipping\_zip\_code**  STRING |
| **customer\_subsegment**  STRING |
| **customer\_text\_field1**  STRING |
| **customer\_text\_field2**  STRING |
| **customer\_text\_field3**  STRING |
| **customer\_type**  STRING |
| **customer\_unbalanced\_revenue\_exception**  BOOLEAN |
| **id**  INTEGER |
| **line\_items**  ARRAY This is a nested data structure:   - affected\_transaction: STRING - created: DATE-TIME - created\_by\_username: STRING - id: INTEGER - invoice\_billing\_addr1: STRING - invoice\_billing\_addr2: STRING - invoice\_billing\_addr3: STRING - invoice\_billing\_city: STRING - invoice\_billing\_country: STRING - invoice\_billing\_state: STRING - invoice\_billing\_zip\_code: STRING - invoice\_cadence\_template: STRING - invoice\_date: STRING - invoice\_do\_not\_sync: BOOLEAN - invoice\_ei\_combine\_all\_description: STRING - invoice\_ei\_combine\_lines: STRING - invoice\_ei\_theme: STRING - invoice\_email\_from\_so: BOOLEAN - invoice\_enable\_ach\_payment: BOOLEAN - invoice\_enable\_cc\_payment: BOOLEAN - invoice\_ignore\_date\_when\_syncing: BOOLEAN - invoice\_memo: STRING - invoice\_other: STRING - invoice\_payment\_terms: STRING - invoice\_po\_number: STRING - invoice\_qb\_class: STRING - invoice\_qb\_customer\_message: STRING - invoice\_qb\_payment\_terms: STRING - invoice\_qb\_sales\_rep: STRING - invoice\_qb\_template: STRING - invoice\_ship\_date: DATE-TIME - invoice\_shipping\_addr1: STRING - invoice\_shipping\_addr2: STRING - invoice\_shipping\_addr3: STRING - invoice\_shipping\_city: STRING - invoice\_shipping\_country: STRING - invoice\_shipping\_state: STRING - invoice\_shipping\_zip\_code: STRING - invoice\_suppress\_zero\_value\_line\_items: BOOLEAN - invoice\_to\_be\_emailed: BOOLEAN - invoice\_to\_be\_printed: BOOLEAN - line\_item\_id: STRING - processed: BOOLEAN - project\_template: STRING - renewed\_transaction: STRING - sfdc\_object\_type: STRING - transaction\_action: STRING - transaction\_amount: NUMBER - transaction\_amount\_after\_discount: NUMBER - transaction\_arr\_amount: NUMBER - transaction\_billing\_method: STRING - transaction\_conversion: STRING - transaction\_crm\_opportunity\_id: STRING - transaction\_crm\_opportunity\_line\_item\_id: STRING - transaction\_discount\_amount: NUMBER - transaction\_duration: STRING - transaction\_effective\_change\_date: DATE-TIME - transaction\_effective\_end\_date: DATE-TIME - transaction\_end\_date: DATE-TIME - transaction\_flagged: STRING - transaction\_foreign\_exchange\_rate: NUMBER - transaction\_generate\_invoices: BOOLEAN - transaction\_generate\_revenue: BOOLEAN - transaction\_ili\_description: STRING - transaction\_ili\_qb\_class: STRING - transaction\_invoice\_end\_date: DATE-TIME - transaction\_invoice\_quantity: NUMBER - transaction\_invoice\_start\_date: DATE-TIME - transaction\_item\_class\_name: STRING - transaction\_item\_code: STRING - transaction\_item\_name: STRING - transaction\_monthly\_rate: NUMBER - transaction\_normalized\_amount: NUMBER - transaction\_normalized\_term: STRING - transaction\_notes: STRING - transaction\_number\_field1: NUMBER - transaction\_number\_field2: NUMBER - transaction\_order\_date: DATE-TIME - transaction\_order\_number: STRING - transaction\_quantity: NUMBER - transaction\_recognize: BOOLEAN - transaction\_renew\_using\_item: STRING - transaction\_renewal\_amount: NUMBER - transaction\_renewal\_amount\_percentage: NUMBER - transaction\_renewal\_duration: STRING - transaction\_renewal\_factor: STRING - transaction\_renewal\_probability: NUMBER - transaction\_renewal\_quantity: NUMBER - transaction\_revenue\_amount: NUMBER - transaction\_revenue\_end\_date: DATE-TIME - transaction\_revenue\_recognition\_method: STRING - transaction\_revenue\_start\_date: DATE-TIME - transaction\_sales\_manager: STRING - transaction\_sales\_rep: STRING - transaction\_sf\_group\_id: STRING - transaction\_sf\_id: STRING - transaction\_sf\_renewal\_opportunitiy\_rule: STRING - transaction\_start\_date: DATE-TIME - transaction\_term\_number: INTEGER - transaction\_text\_field1: STRING - transaction\_text\_field2: STRING - transaction\_unbalanced\_revenue\_exception: BOOLEAN |
| **name**  STRING |
| **order\_notes**  STRING |
| **order\_total**  STRING |
| **project\_name**  STRING |
| **project\_template**  STRING |
| **quickbooks\_job\_account\_number**  STRING |
| **quickbooks\_job\_addr1**  STRING |
| **quickbooks\_job\_addr2**  STRING |
| **quickbooks\_job\_addr3**  STRING |
| **quickbooks\_job\_alt\_contact**  STRING |
| **quickbooks\_job\_alt\_phone**  STRING |
| **quickbooks\_job\_city**  STRING |
| **quickbooks\_job\_company\_name**  STRING |
| **quickbooks\_job\_contact**  STRING |
| **quickbooks\_job\_country**  STRING |
| **quickbooks\_job\_default\_credit\_memo\_template**  STRING |
| **quickbooks\_job\_default\_invoice\_template**  STRING |
| **quickbooks\_job\_description**  STRING |
| **quickbooks\_job\_email**  STRING |
| **quickbooks\_job\_end\_date**  DATE-TIME |
| **quickbooks\_job\_fax**  STRING |
| **quickbooks\_job\_first\_name**  STRING |
| **quickbooks\_job\_invoice\_email\_preference**  BOOLEAN |
| **quickbooks\_job\_invoice\_print\_preference**  BOOLEAN |
| **quickbooks\_job\_is\_active**  BOOLEAN |
| **quickbooks\_job\_last\_name**  STRING |
| **quickbooks\_job\_name**  STRING |
| **quickbooks\_job\_payment\_terms**  STRING |
| **quickbooks\_job\_phone**  STRING |
| **quickbooks\_job\_projected\_end\_date**  DATE-TIME |
| **quickbooks\_job\_resale\_number**  STRING |
| **quickbooks\_job\_sales\_rep**  STRING |
| **quickbooks\_job\_salutation**  STRING |
| **quickbooks\_job\_shipping\_addr1**  STRING |
| **quickbooks\_job\_shipping\_addr2**  STRING |
| **quickbooks\_job\_shipping\_addr3**  STRING |
| **quickbooks\_job\_shipping\_city**  STRING |
| **quickbooks\_job\_shipping\_country**  STRING |
| **quickbooks\_job\_shipping\_state**  STRING |
| **quickbooks\_job\_shipping\_zip\_code**  STRING |
| **quickbooks\_job\_start\_date**  DATE-TIME |
| **quickbooks\_job\_state**  STRING |
| **quickbooks\_job\_status**  STRING |
| **quickbooks\_job\_type**  STRING |
| **quickbooks\_job\_zip\_code**  STRING |
| **sales\_order\_id**  STRING |
| **stage\_name**  STRING |
| **type**  STRING |

### transactions

The `transactions` table contains info about transactions.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | modified |
| **Useful links** | [SaaSOptics API method](https://saasoptics.zendesk.com/hc/en-us/articles/360000066333-Transactions-CRUD- "Opens in new tab: SaaSOptics API method") |

transactions table schema

|  |
| --- |
| **always\_use\_amount\_as\_normalized\_amount**  BOOLEAN |
| **auditentry\_created**  DATE-TIME |
| **auditentry\_created\_by\_name**  STRING |
| **auditentry\_modified**  DATE-TIME |
| **auditentry\_modified\_by\_name**  STRING |
| **automatically\_update\_revenue**  BOOLEAN |
| **autorenewal\_profile**  INTEGER |
| **billing\_method**  INTEGER |
| **cancelled**  BOOLEAN |
| **contract**  INTEGER |
| **conversion**  STRING |
| **crm\_opportunity\_id**  STRING |
| **crm\_opportunity\_line\_item\_id**  STRING |
| **different\_invoice\_item\_permitted**  BOOLEAN |
| **do\_not\_sync\_invoices**  BOOLEAN |
| **duration**  STRING |
| **end\_date**  DATE-TIME |
| **flagged**  STRING |
| **foreign\_exchange\_rate**  NUMBER |
| **home\_amount**  NUMBER |
| **home\_arr\_amount**  NUMBER |
| **home\_normalized\_amount**  NUMBER |
| **home\_normalized\_rate**  NUMBER |
| **home\_rate**  NUMBER |
| **id**  INTEGER |
| **ili\_qb\_class**  STRING |
| **invoice\_description**  STRING |
| **is\_autorenewal**  BOOLEAN |
| **item**  INTEGER |
| **item\_class**  INTEGER |
| **local\_amount**  NUMBER |
| **local\_arr\_amount**  NUMBER |
| **local\_normalized\_amount**  NUMBER |
| **local\_normalized\_rate**  NUMBER |
| **local\_rate**  NUMBER |
| **modified**  DATE-TIME |
| **monthyear**  STRING |
| **notes**  STRING |
| **number**  STRING |
| **number\_field1**  NUMBER |
| **number\_field2**  NUMBER |
| **order\_date**  DATE-TIME |
| **order\_number**  STRING |
| **project**  INTEGER |
| **quantity**  NUMBER |
| **recognize**  BOOLEAN |
| **reconcile\_required**  BOOLEAN |
| **renew\_using\_item**  INTEGER |
| **renewal\_amount**  NUMBER |
| **renewal\_amount\_percentage**  NUMBER |
| **renewal\_amount\_value**  NUMBER |
| **renewal\_duration**  STRING |
| **renewal\_factor**  INTEGER |
| **renewal\_of\_set**  ARRAY |
| **renewal\_probability**  NUMBER |
| **renewal\_quantity**  NUMBER |
| **revenue\_amount**  NUMBER |
| **revenue\_notes**  STRING |
| **sales\_manager**  STRING |
| **sales\_rep**  STRING |
| **sf\_group\_id**  STRING |
| **sf\_id**  STRING |
| **sf\_opportunity\_id**  STRING |
| **sf\_opportunity\_line\_item\_id**  STRING |
| **sf\_renewal\_opportunity\_id**  STRING |
| **sf\_renewal\_opportunity\_line\_item\_id**  STRING |
| **sf\_renewal\_opportunity\_rule**  STRING |
| **start\_date**  DATE-TIME |
| **term\_number**  INTEGER |
| **text\_field1**  STRING |
| **text\_field2**  STRING |
| **unbalanced\_revenue\_exception**  BOOLEAN |
