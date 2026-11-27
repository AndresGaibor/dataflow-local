---
title: "Chargify"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Chargify.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Chargify

Chargify is a recurring billing and revenue management platform built specifically for B2B SaaS companies.

Chargify integration replicates data using the [Chargify API](https://reference.chargify.com/v1/basics/introduction).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

Chargify is part of Maxio, providing subscription billing solutions within Maxio’s unified financial operations platform.

API keys can only be managed by admin users.

To retrieve your API key:

1. Log into your [Chargify](https://www.maxio.com/login) account.
2. Go to Config > Integrations > API Keys > New API Key.
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
| Subdomain | You can find your subdomain in the URL of your account homepage. If the URL is my-chargify-site.chargify.com, the subdomain is my-chargify-site. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### components

The `components` table contains info about components associated with a product family in Chargify.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Chargify API method](https://reference.chargify.com/v1/components/list-components-for-a-product-family "Opens in new tab: Chargify API method") |

components table foreign keys

| Join components with | on |
| --- | --- |
| [invoices](#invoices) | ``` components.id = invoices.charges.component_id ```  ``` components.prices.id = invoices.charges.component_id ```  ``` components.id = invoices.payments_and_credits.component_id ```  ``` components.prices.id = invoices.payments_and_credits.component_id ``` |
| [price\_points](#price-points) | ``` components.id = price_points.component_id ```  ``` components.prices.id = price_points.component_id ```  ``` components.id = price_points.prices.component_id ```  ``` components.prices.id = price_points.prices.component_id ```  ``` components.default_price_point_id = price_points.id ```  ``` components.prices.price_point_id = price_points.id ``` |
| [statements](#statements) | ``` components.id = statements.transactions.component_id ```  ``` components.prices.id = statements.transactions.component_id ``` |
| [transactions](#transactions) | ``` components.id = transactions.component_id ```  ``` components.prices.id = transactions.component_id ``` |
| [coupons](#coupons) | ``` components.product_family_id = coupons.product_family_id ``` |
| [product\_families](#product-families) | ``` components.product_family_id = product_families.id ``` |
| [products](#products) | ``` components.product_family_id = products.product_family.id ``` |
| [subscriptions](#subscriptions) | ``` components.product_family_id = subscriptions.product.product_family.id ``` |

components table schema

|  |
| --- |
| **archived**  BOOLEAN |
| **created\_at**  DATE-TIME |
| **default\_price\_point\_id**  NUMBER |
| **default\_price\_point\_name**  STRING |
| **description**  STRING |
| **downgrade\_credit**  STRING |
| **handle**  STRING |
| **id**  INTEGER |
| **kind**  STRING |
| **name**  STRING |
| **price\_per\_unit\_in\_cents**  INTEGER |
| **price\_point\_count**  NUMBER |
| **price\_points\_url**  STRING |
| **prices**  ARRAY This is a nested data structure:   - component\_id: INTEGER - ending\_quantity: INTEGER - formatted\_unit\_price: STRING - id: INTEGER - price\_point\_id: INTEGER - starting\_quantity: INTEGER - unit\_price: STRING |
| **pricing\_scheme**  STRING |
| **product\_family\_id**  INTEGER |
| **product\_family\_name**  STRING |
| **recurring**  BOOLEAN |
| **tax\_code**  STRING |
| **taxable**  BOOLEAN |
| **unit\_name**  STRING |
| **unit\_price**  STRING |
| **upgrade\_charge**  STRING |

### coupons

The `coupons` table contains info about coupons associated with a product family in Chargify.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Chargify API method](https://reference.chargify.com/v1/coupons-editing/list-product-family-coupons "Opens in new tab: Chargify API method") |

coupons table foreign keys

| Join coupons with | on |
| --- | --- |
| [components](#components) | ``` coupons.product_family_id = components.product_family_id ``` |
| [product\_families](#product-families) | ``` coupons.product_family_id = product_families.id ``` |
| [products](#products) | ``` coupons.product_family_id = products.product_family.id ``` |
| [subscriptions](#subscriptions) | ``` coupons.product_family_id = subscriptions.product.product_family.id ``` |

coupons table schema

|  |
| --- |
| **allow\_negative\_balance**  BOOLEAN |
| **amount\_in\_cents**  INTEGER |
| **archived\_at**  DATE-TIME |
| **code**  STRING |
| **compounding\_strategy**  STRING |
| **conversion\_limit**  INTEGER |
| **coupon\_restrictions**  ARRAY This is a nested data structure:   - handle: STRING - id: INTEGER - item\_id: INTEGER - item\_type: STRING - name: STRING |
| **created\_at**  DATE-TIME |
| **description**  STRING |
| **duration\_interval**  INTEGER |
| **duration\_interval\_unit**  STRING |
| **duration\_period\_count**  NUMBER |
| **end\_date**  DATE-TIME |
| **id**  INTEGER |
| **name**  STRING |
| **percentage**  NUMBER |
| **product\_family\_id**  INTEGER |
| **recurring**  BOOLEAN |
| **stackable**  BOOLEAN |
| **start\_date**  DATE-TIME |
| **updated\_at**  DATE-TIME |

### customers

The `customers` table contains info about customers associated with your Chargify site.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Chargify API method](https://reference.chargify.com/v1/customers/list-customers-for-a-site "Opens in new tab: Chargify API method") |

customers table foreign keys

| Join customers with | on |
| --- | --- |
| [invoices](#invoices) | ``` customers.id = invoices.charges.customer_id ```  ``` customers.parent_id = invoices.charges.customer_id ```  ``` customers.id = invoices.payments_and_credits.customer_id ```  ``` customers.parent_id = invoices.payments_and_credits.customer_id ``` |
| [statements](#statements) | ``` customers.id = statements.transactions.customer_id ```  ``` customers.parent_id = statements.transactions.customer_id ``` |
| [subscriptions](#subscriptions) | ``` customers.id = subscriptions.credit_card.customer_id ```  ``` customers.parent_id = subscriptions.credit_card.customer_id ```  ``` customers.id = subscriptions.customer.id ```  ``` customers.parent_id = subscriptions.customer.id ``` |
| [transactions](#transactions) | ``` customers.id = transactions.customer_id ```  ``` customers.parent_id = transactions.customer_id ``` |

customers table schema

|  |
| --- |
| **address**  STRING |
| **address\_2**  STRING |
| **cc\_emails**  STRING |
| **city**  STRING |
| **country**  STRING |
| **created\_at**  DATE-TIME |
| **first\_name**  STRING |
| **id**  INTEGER |
| **last\_name**  STRING |
| **organization**  STRING |
| **parent\_id**  INTEGER |
| **phone**  STRING |
| **portal\_customer\_created\_at**  DATE-TIME |
| **portal\_invite\_last\_accepted\_at**  DATE-TIME |
| **portal\_invite\_last\_sent\_at**  DATE-TIME |
| **reference**  STRING |
| **state**  STRING |
| **tax\_exempt**  BOOLEAN |
| **updated\_at**  DATE-TIME |
| **vat\_number**  STRING |
| **verified**  BOOLEAN |
| **zip**  STRING |

### events

The `events` table contains info about activity on your Chargify site.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Chargify API method](https://reference.chargify.com/v1/events/list-events-for-a-site "Opens in new tab: Chargify API method") |

events table foreign keys

| Join events with | on |
| --- | --- |
| [statements](#statements) | ``` events.id = statements.events.event.id ```  ``` events.event_specific_data.product_id = statements.events.event.event_specific_data.product_id ```  ``` events.event_specific_data.product_id = statements.transactions.product_id ```  ``` events.subscription_id = statements.events.event.subscription_id ```  ``` events.subscription_id = statements.subscription_id ```  ``` events.subscription_id = statements.transactions.subscription_id ```  ``` events.event_specific_data.account_transaction_id = statements.transactions.id ``` |
| [invoices](#invoices) | ``` events.event_specific_data.product_id = invoices.charges.product_id ```  ``` events.event_specific_data.product_id = invoices.payments_and_credits.product_id ```  ``` events.subscription_id = invoices.charges.subscription_id ```  ``` events.subscription_id = invoices.payments_and_credits.subscription_id ```  ``` events.subscription_id = invoices.subscription_id ```  ``` events.event_specific_data.account_transaction_id = invoices.charges.payment_id ```  ``` events.event_specific_data.account_transaction_id = invoices.payments_and_credits.payment_id ``` |
| [products](#products) | ``` events.event_specific_data.product_id = products.id ``` |
| [subscriptions](#subscriptions) | ``` events.event_specific_data.product_id = subscriptions.next_product_id ```  ``` events.event_specific_data.product_id = subscriptions.product.id ```  ``` events.subscription_id = subscriptions.id ```  ``` events.event_specific_data.account_transaction_id = subscriptions.signup_payment_id ```  ``` events.event_specific_data.account_transaction_id = subscriptions.stored_credential_transaction_id ``` |
| [transactions](#transactions) | ``` events.event_specific_data.product_id = transactions.product_id ```  ``` events.subscription_id = transactions.subscription_id ```  ``` events.event_specific_data.account_transaction_id = transactions.id ```  ``` events.event_specific_data.account_transaction_id = transactions.parent_id ```  ``` events.event_specific_data.account_transaction_id = transactions.payment_id ``` |

events table schema

|  |
| --- |
| **created\_at**  DATE-TIME |
| **event\_specific\_data**  OBJECT This is a nested data structure:   - account\_transaction\_id: INTEGER - current\_step: OBJECT, which is also a nested data structure.   - action: STRING   - day\_threshold: INTEGER   - email\_body: STRING   - email\_subject: STRING   - send\_bcc\_email: BOOLEAN   - send\_email: BOOLEAN   - send\_sms: BOOLEAN   - sms\_body: STRING - dunner: OBJECT, which is also a nested data structure.   - attempts: INTEGER   - created\_at: STRING   - last\_attempted\_at: STRING   - revenue\_at\_risk\_in\_cents: INTEGER   - state: STRING   - subscription\_id: INTEGER - new\_product\_id: INTEGER - new\_subscription\_state: STRING - next\_step: OBJECT, which is also a nested data structure.   - action: STRING   - day\_threshold: INTEGER   - email\_body: STRING   - email\_subject: STRING   - send\_bcc\_email: BOOLEAN   - send\_email: BOOLEAN   - send\_sms: BOOLEAN   - sms\_body: STRING - previous\_product\_id: INTEGER - previous\_subscription\_state: STRING - product\_id: INTEGER |
| **id**  INTEGER |
| **key**  STRING |
| **message**  STRING |
| **subscription\_id**  INTEGER |

### invoices

The `invoices` table contains info about invoices in your Chargify instance.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Chargify API method](https://reference.chargify.com/v1/invoices-legacy/list-all-invoices-by-subscription "Opens in new tab: Chargify API method") |

invoices table foreign keys

| Join invoices with | on |
| --- | --- |
| [components](#components) | ``` invoices.charges.component_id = components.id ```  ``` invoices.payments_and_credits.component_id = components.id ```  ``` invoices.charges.component_id = components.prices.id ```  ``` invoices.payments_and_credits.component_id = components.prices.id ``` |
| [price\_points](#price-points) | ``` invoices.charges.component_id = price_points.component_id ```  ``` invoices.payments_and_credits.component_id = price_points.component_id ```  ``` invoices.charges.component_id = price_points.prices.component_id ```  ``` invoices.payments_and_credits.component_id = price_points.prices.component_id ``` |
| [statements](#statements) | ``` invoices.charges.component_id = statements.transactions.component_id ```  ``` invoices.payments_and_credits.component_id = statements.transactions.component_id ```  ``` invoices.charges.customer_id = statements.transactions.customer_id ```  ``` invoices.payments_and_credits.customer_id = statements.transactions.customer_id ```  ``` invoices.charges.product_id = statements.events.event.event_specific_data.product_id ```  ``` invoices.payments_and_credits.product_id = statements.events.event.event_specific_data.product_id ```  ``` invoices.charges.product_id = statements.transactions.product_id ```  ``` invoices.payments_and_credits.product_id = statements.transactions.product_id ```  ``` invoices.statement_id = statements.id ```  ``` invoices.statement_id = statements.transactions.statement_id ```  ``` invoices.charges.subscription_id = statements.events.event.subscription_id ```  ``` invoices.payments_and_credits.subscription_id = statements.events.event.subscription_id ```  ``` invoices.subscription_id = statements.events.event.subscription_id ```  ``` invoices.charges.subscription_id = statements.subscription_id ```  ``` invoices.payments_and_credits.subscription_id = statements.subscription_id ```  ``` invoices.subscription_id = statements.subscription_id ```  ``` invoices.charges.subscription_id = statements.transactions.subscription_id ```  ``` invoices.payments_and_credits.subscription_id = statements.transactions.subscription_id ```  ``` invoices.subscription_id = statements.transactions.subscription_id ```  ``` invoices.charges.payment_id = statements.transactions.id ```  ``` invoices.payments_and_credits.payment_id = statements.transactions.id ``` |
| [transactions](#transactions) | ``` invoices.charges.component_id = transactions.component_id ```  ``` invoices.payments_and_credits.component_id = transactions.component_id ```  ``` invoices.charges.customer_id = transactions.customer_id ```  ``` invoices.payments_and_credits.customer_id = transactions.customer_id ```  ``` invoices.charges.product_id = transactions.product_id ```  ``` invoices.payments_and_credits.product_id = transactions.product_id ```  ``` invoices.statement_id = transactions.statement_id ```  ``` invoices.charges.subscription_id = transactions.subscription_id ```  ``` invoices.payments_and_credits.subscription_id = transactions.subscription_id ```  ``` invoices.subscription_id = transactions.subscription_id ```  ``` invoices.charges.payment_id = transactions.id ```  ``` invoices.payments_and_credits.payment_id = transactions.id ```  ``` invoices.charges.payment_id = transactions.parent_id ```  ``` invoices.payments_and_credits.payment_id = transactions.parent_id ```  ``` invoices.charges.payment_id = transactions.payment_id ```  ``` invoices.payments_and_credits.payment_id = transactions.payment_id ``` |
| [customers](#customers) | ``` invoices.charges.customer_id = customers.id ```  ``` invoices.payments_and_credits.customer_id = customers.id ```  ``` invoices.charges.customer_id = customers.parent_id ```  ``` invoices.payments_and_credits.customer_id = customers.parent_id ``` |
| [subscriptions](#subscriptions) | ``` invoices.charges.customer_id = subscriptions.credit_card.customer_id ```  ``` invoices.payments_and_credits.customer_id = subscriptions.credit_card.customer_id ```  ``` invoices.charges.customer_id = subscriptions.customer.id ```  ``` invoices.payments_and_credits.customer_id = subscriptions.customer.id ```  ``` invoices.charges.product_id = subscriptions.next_product_id ```  ``` invoices.payments_and_credits.product_id = subscriptions.next_product_id ```  ``` invoices.charges.product_id = subscriptions.product.id ```  ``` invoices.payments_and_credits.product_id = subscriptions.product.id ```  ``` invoices.charges.subscription_id = subscriptions.id ```  ``` invoices.payments_and_credits.subscription_id = subscriptions.id ```  ``` invoices.subscription_id = subscriptions.id ```  ``` invoices.charges.payment_id = subscriptions.signup_payment_id ```  ``` invoices.payments_and_credits.payment_id = subscriptions.signup_payment_id ```  ``` invoices.charges.payment_id = subscriptions.stored_credential_transaction_id ```  ``` invoices.payments_and_credits.payment_id = subscriptions.stored_credential_transaction_id ``` |
| [events](#events) | ``` invoices.charges.product_id = events.event_specific_data.product_id ```  ``` invoices.payments_and_credits.product_id = events.event_specific_data.product_id ```  ``` invoices.charges.subscription_id = events.subscription_id ```  ``` invoices.payments_and_credits.subscription_id = events.subscription_id ```  ``` invoices.subscription_id = events.subscription_id ```  ``` invoices.charges.payment_id = events.event_specific_data.account_transaction_id ```  ``` invoices.payments_and_credits.payment_id = events.event_specific_data.account_transaction_id ``` |
| [products](#products) | ``` invoices.charges.product_id = products.id ```  ``` invoices.payments_and_credits.product_id = products.id ``` |

invoices table schema

|  |
| --- |
| **amount\_due\_in\_cents**  INTEGER |
| **charges**  ARRAY This is a nested data structure:   - amount\_in\_cents: INTEGER - component\_id: INTEGER - created\_at: DATE-TIME - customer\_id: INTEGER - ending\_balance\_in\_cents: INTEGER - gateway\_order\_id: STRING - gateway\_transaction\_id: STRING - id: INTEGER - kind: STRING - memo: STRING - payment\_id: INTEGER - product\_id: INTEGER - starting\_balance\_in\_cents: INTEGER - subscription\_id: INTEGER - success: BOOLEAN - tax\_id: INTEGER - transaction\_type: STRING - type: STRING |
| **created\_at**  DATE-TIME |
| **id**  INTEGER |
| **number**  STRING |
| **paid\_at**  DATE-TIME |
| **payments\_and\_credits**  ARRAY This is a nested data structure:   - amount\_in\_cents: INTEGER - card\_expiration: STRING - card\_number: STRING - card\_type: STRING - component\_id: INTEGER - created\_at: DATE-TIME - customer\_id: INTEGER - ending\_balance\_in\_cents: INTEGER - gateway\_order\_id: STRING - gateway\_transaction\_id: STRING - id: INTEGER - kind: STRING - memo: STRING - payment\_id: INTEGER - product\_id: INTEGER - starting\_balance\_in\_cents: INTEGER - subscription\_id: INTEGER - success: BOOLEAN - tax\_id: INTEGER - transaction\_type: STRING - type: STRING |
| **site\_id**  INTEGER |
| **state**  STRING |
| **statement\_id**  INTEGER |
| **subscription\_id**  INTEGER |
| **total\_amount\_in\_cents**  INTEGER |
| **updated\_at**  DATE-TIME |

### price\_points

The `price_points` table contains info about product price points in your Chargify instance.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Chargify API method](https://reference.chargify.com/v1/products-price-points/read-product-price-points "Opens in new tab: Chargify API method") |

price\_points table foreign keys

| Join price\_points with | on |
| --- | --- |
| [components](#components) | ``` price_points.component_id = components.id ```  ``` price_points.prices.component_id = components.id ```  ``` price_points.component_id = components.prices.id ```  ``` price_points.prices.component_id = components.prices.id ```  ``` price_points.id = components.default_price_point_id ```  ``` price_points.id = components.prices.price_point_id ``` |
| [invoices](#invoices) | ``` price_points.component_id = invoices.charges.component_id ```  ``` price_points.prices.component_id = invoices.charges.component_id ```  ``` price_points.component_id = invoices.payments_and_credits.component_id ```  ``` price_points.prices.component_id = invoices.payments_and_credits.component_id ``` |
| [statements](#statements) | ``` price_points.component_id = statements.transactions.component_id ```  ``` price_points.prices.component_id = statements.transactions.component_id ``` |
| [transactions](#transactions) | ``` price_points.component_id = transactions.component_id ```  ``` price_points.prices.component_id = transactions.component_id ``` |

price\_points table schema

|  |
| --- |
| **archived\_at**  DATE-TIME |
| **component\_id**  INTEGER |
| **created\_at**  DATE-TIME |
| **default**  BOOLEAN |
| **handle**  STRING |
| **id**  INTEGER |
| **name**  STRING |
| **prices**  ARRAY This is a nested data structure:   - component\_id: INTEGER - ending\_quantity: INTEGER - id: INTEGER - starting\_quantity: INTEGER - unit\_price: STRING |
| **pricing\_scheme**  STRING |
| **updated\_at**  DATE-TIME |

### product\_families

The `product_families` table contains info about product families in your Chargify instance. Product families house your products, components, and coupons and are used to categorize products, product levels, or service offerings to your subscribers.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Chargify API method](https://reference.chargify.com/v1/product-families/list-product-family-via-site "Opens in new tab: Chargify API method") |

product\_families table foreign keys

| Join product\_families with | on |
| --- | --- |
| [components](#components) | ``` product_families.id = components.product_family_id ``` |
| [coupons](#coupons) | ``` product_families.id = coupons.product_family_id ``` |
| [products](#products) | ``` product_families.id = products.product_family.id ``` |
| [subscriptions](#subscriptions) | ``` product_families.id = subscriptions.product.product_family.id ``` |

product\_families table schema

|  |
| --- |
| **accounting\_code**  STRING |
| **description**  STRING |
| **handle**  STRING |
| **id**  INTEGER |
| **name**  STRING |

### products

The `products` table contains info about the prodcts in your Chargify instance.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Chargify API method](https://reference.chargify.com/v1/products/list-products "Opens in new tab: Chargify API method") |

products table foreign keys

| Join products with | on |
| --- | --- |
| [components](#components) | ``` products.product_family.id = components.product_family_id ``` |
| [coupons](#coupons) | ``` products.product_family.id = coupons.product_family_id ``` |
| [product\_families](#product-families) | ``` products.product_family.id = product_families.id ``` |
| [subscriptions](#subscriptions) | ``` products.product_family.id = subscriptions.product.product_family.id ```  ``` products.id = subscriptions.next_product_id ```  ``` products.id = subscriptions.product.id ``` |
| [events](#events) | ``` products.id = events.event_specific_data.product_id ``` |
| [invoices](#invoices) | ``` products.id = invoices.charges.product_id ```  ``` products.id = invoices.payments_and_credits.product_id ``` |
| [statements](#statements) | ``` products.id = statements.events.event.event_specific_data.product_id ```  ``` products.id = statements.transactions.product_id ``` |
| [transactions](#transactions) | ``` products.id = transactions.product_id ``` |

products table schema

|  |
| --- |
| **accounting\_code**  STRING |
| **archived\_at**  DATE-TIME |
| **created\_at**  DATE-TIME |
| **description**  STRING |
| **expiration\_interval**  STRING |
| **expiration\_interval\_unit**  STRING |
| **handle**  STRING |
| **id**  INTEGER |
| **initial\_charge\_after\_trial**  BOOLEAN |
| **initial\_charge\_in\_cents**  INTEGER |
| **interval**  INTEGER |
| **interval\_unit**  STRING |
| **name**  STRING |
| **price\_in\_cents**  INTEGER |
| **product\_family**  OBJECT This is a nested data structure:   - accounting\_code: STRING - description: STRING - handle: - id: INTEGER - name: STRING |
| **public\_signup\_pages**  ARRAY This is a nested data structure:   - id: INTEGER - return\_params: STRING - return\_url: STRING - url: STRING |
| **request\_credit\_card**  BOOLEAN |
| **require\_credit\_card**  BOOLEAN |
| **return\_params**  STRING |
| **tax\_code**  STRING |
| **taxable**  BOOLEAN |
| **trial\_interval**  INTEGER |
| **trial\_interval\_unit**  STRING |
| **trial\_price\_in\_cents**  INTEGER |
| **update\_return\_params**  STRING |
| **update\_return\_url**  STRING |
| **updated\_at**  DATE-TIME |
| **version\_number**  INTEGER |

### statements

The `statements` table contains info about the statements in your Chargify instance. Statements show all account activity for a specific usage period and are similar to invoices, as they can be marked as currently paid or unpaid.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Chargify API method](https://reference.chargify.com/v1/statements/list-statements-for-a-site "Opens in new tab: Chargify API method") |

statements table foreign keys

| Join statements with | on |
| --- | --- |
| [components](#components) | ``` statements.transactions.component_id = components.id ```  ``` statements.transactions.component_id = components.prices.id ``` |
| [invoices](#invoices) | ``` statements.transactions.component_id = invoices.charges.component_id ```  ``` statements.transactions.component_id = invoices.payments_and_credits.component_id ```  ``` statements.transactions.customer_id = invoices.charges.customer_id ```  ``` statements.transactions.customer_id = invoices.payments_and_credits.customer_id ```  ``` statements.events.event.event_specific_data.product_id = invoices.charges.product_id ```  ``` statements.transactions.product_id = invoices.charges.product_id ```  ``` statements.events.event.event_specific_data.product_id = invoices.payments_and_credits.product_id ```  ``` statements.transactions.product_id = invoices.payments_and_credits.product_id ```  ``` statements.id = invoices.statement_id ```  ``` statements.transactions.statement_id = invoices.statement_id ```  ``` statements.events.event.subscription_id = invoices.charges.subscription_id ```  ``` statements.subscription_id = invoices.charges.subscription_id ```  ``` statements.transactions.subscription_id = invoices.charges.subscription_id ```  ``` statements.events.event.subscription_id = invoices.payments_and_credits.subscription_id ```  ``` statements.subscription_id = invoices.payments_and_credits.subscription_id ```  ``` statements.transactions.subscription_id = invoices.payments_and_credits.subscription_id ```  ``` statements.events.event.subscription_id = invoices.subscription_id ```  ``` statements.subscription_id = invoices.subscription_id ```  ``` statements.transactions.subscription_id = invoices.subscription_id ```  ``` statements.transactions.id = invoices.charges.payment_id ```  ``` statements.transactions.id = invoices.payments_and_credits.payment_id ``` |
| [price\_points](#price-points) | ``` statements.transactions.component_id = price_points.component_id ```  ``` statements.transactions.component_id = price_points.prices.component_id ``` |
| [transactions](#transactions) | ``` statements.transactions.component_id = transactions.component_id ```  ``` statements.transactions.customer_id = transactions.customer_id ```  ``` statements.events.event.event_specific_data.product_id = transactions.product_id ```  ``` statements.transactions.product_id = transactions.product_id ```  ``` statements.id = transactions.statement_id ```  ``` statements.transactions.statement_id = transactions.statement_id ```  ``` statements.events.event.subscription_id = transactions.subscription_id ```  ``` statements.subscription_id = transactions.subscription_id ```  ``` statements.transactions.subscription_id = transactions.subscription_id ```  ``` statements.transactions.id = transactions.id ```  ``` statements.transactions.id = transactions.parent_id ```  ``` statements.transactions.id = transactions.payment_id ``` |
| [customers](#customers) | ``` statements.transactions.customer_id = customers.id ```  ``` statements.transactions.customer_id = customers.parent_id ``` |
| [subscriptions](#subscriptions) | ``` statements.transactions.customer_id = subscriptions.credit_card.customer_id ```  ``` statements.transactions.customer_id = subscriptions.customer.id ```  ``` statements.events.event.event_specific_data.product_id = subscriptions.next_product_id ```  ``` statements.transactions.product_id = subscriptions.next_product_id ```  ``` statements.events.event.event_specific_data.product_id = subscriptions.product.id ```  ``` statements.transactions.product_id = subscriptions.product.id ```  ``` statements.events.event.subscription_id = subscriptions.id ```  ``` statements.subscription_id = subscriptions.id ```  ``` statements.transactions.subscription_id = subscriptions.id ```  ``` statements.transactions.id = subscriptions.signup_payment_id ```  ``` statements.transactions.id = subscriptions.stored_credential_transaction_id ``` |
| [events](#events) | ``` statements.events.event.id = events.id ```  ``` statements.events.event.event_specific_data.product_id = events.event_specific_data.product_id ```  ``` statements.transactions.product_id = events.event_specific_data.product_id ```  ``` statements.events.event.subscription_id = events.subscription_id ```  ``` statements.subscription_id = events.subscription_id ```  ``` statements.transactions.subscription_id = events.subscription_id ```  ``` statements.transactions.id = events.event_specific_data.account_transaction_id ``` |
| [products](#products) | ``` statements.events.event.event_specific_data.product_id = products.id ```  ``` statements.transactions.product_id = products.id ``` |

statements table schema

|  |
| --- |
| **basic\_html\_view**  STRING |
| **closed\_at**  DATE-TIME |
| **created\_at**  DATE-TIME |
| **customer\_billing\_address**  STRING |
| **customer\_billing\_address\_2**  STRING |
| **customer\_billing\_city**  STRING |
| **customer\_billing\_country**  STRING |
| **customer\_billing\_state**  STRING |
| **customer\_billing\_zip**  STRING |
| **customer\_first\_name**  STRING |
| **customer\_last\_name**  STRING |
| **customer\_organization**  STRING |
| **customer\_shipping\_address**  STRING |
| **customer\_shipping\_address\_2**  STRING |
| **customer\_shipping\_city**  STRING |
| **customer\_shipping\_country**  STRING |
| **customer\_shipping\_state**  STRING |
| **customer\_shipping\_zip**  STRING |
| **ending\_balance\_in\_cents**  INTEGER |
| **events**  ARRAY This is a nested data structure:   - event: OBJECT, which is also a nested data structure.   - created\_at: DATE-TIME   - event\_specific\_data: OBJECT, which is also a nested data structure.     - account\_transaction\_id: INTEGER     - current\_step: OBJECT, which is also a nested data structure.       - action: STRING       - day\_threshold: INTEGER       - email\_body: STRING       - email\_subject: STRING       - send\_bcc\_email: BOOLEAN       - send\_email: BOOLEAN       - send\_sms: BOOLEAN       - sms\_body: STRING     - dunner: OBJECT, which is also a nested data structure.       - attempts: INTEGER       - created\_at: STRING       - last\_attempted\_at: STRING       - revenue\_at\_risk\_in\_cents: INTEGER       - state: STRING       - subscription\_id: INTEGER     - new\_product\_id: INTEGER     - new\_subscription\_state: STRING     - next\_step: OBJECT, which is also a nested data structure.       - action: STRING       - day\_threshold: INTEGER       - email\_body: STRING       - email\_subject: STRING       - send\_bcc\_email: BOOLEAN       - send\_email: BOOLEAN       - send\_sms: BOOLEAN       - sms\_body: STRING     - previous\_product\_id: INTEGER     - previous\_subscription\_state: STRING     - product\_id: INTEGER   - id: INTEGER   - key: STRING   - message: STRING   - subscription\_id: INTEGER |
| **future\_payments**  ARRAY This is a nested data structure:   - id: INTEGER |
| **html\_view**  STRING |
| **id**  INTEGER |
| **memo**  STRING |
| **opened\_at**  DATE-TIME |
| **settled\_at**  DATE-TIME |
| **starting\_balance\_in\_cents**  INTEGER |
| **subscription\_id**  INTEGER |
| **text\_view**  STRING |
| **total\_in\_cents**  INTEGER |
| **transactions**  ARRAY This is a nested data structure:   - amount\_in\_cents: INTEGER - component\_id: INTEGER - created\_at: DATE-TIME - customer\_id: INTEGER - discount\_amount\_in\_cents: INTEGER - ending\_balance\_in\_cents: INTEGER - gateway\_order\_id: STRING - gateway\_transaction\_id: STRING - gateway\_used: STRING - id: INTEGER - item\_name: STRING - kind: STRING - memo: STRING - original\_amount\_in\_cents: INTEGER - payment\_id: INTEGER - product\_id: INTEGER - starting\_balance\_in\_cents: INTEGER - statement\_id: INTEGER - subscription\_id: INTEGER - success: BOOLEAN - tax\_id: INTEGER - taxable\_amount\_in\_cents: INTEGER - taxations: ARRAY, which is also a nested data structure.   - id: INTEGER - transaction\_type: STRING - type: STRING |
| **updated\_at**  DATE-TIME |

### subscriptions

The `subscriptions` table contains info about the subscriptions in your Chargify instance.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Chargify API method](https://reference.chargify.com/v1/subscriptions/list-subscriptions "Opens in new tab: Chargify API method") |

subscriptions table foreign keys

| Join subscriptions with | on |
| --- | --- |
| [customers](#customers) | ``` subscriptions.credit_card.customer_id = customers.id ```  ``` subscriptions.customer.id = customers.id ```  ``` subscriptions.credit_card.customer_id = customers.parent_id ```  ``` subscriptions.customer.id = customers.parent_id ``` |
| [invoices](#invoices) | ``` subscriptions.credit_card.customer_id = invoices.charges.customer_id ```  ``` subscriptions.customer.id = invoices.charges.customer_id ```  ``` subscriptions.credit_card.customer_id = invoices.payments_and_credits.customer_id ```  ``` subscriptions.customer.id = invoices.payments_and_credits.customer_id ```  ``` subscriptions.next_product_id = invoices.charges.product_id ```  ``` subscriptions.product.id = invoices.charges.product_id ```  ``` subscriptions.next_product_id = invoices.payments_and_credits.product_id ```  ``` subscriptions.product.id = invoices.payments_and_credits.product_id ```  ``` subscriptions.id = invoices.charges.subscription_id ```  ``` subscriptions.id = invoices.payments_and_credits.subscription_id ```  ``` subscriptions.id = invoices.subscription_id ```  ``` subscriptions.signup_payment_id = invoices.charges.payment_id ```  ``` subscriptions.stored_credential_transaction_id = invoices.charges.payment_id ```  ``` subscriptions.signup_payment_id = invoices.payments_and_credits.payment_id ```  ``` subscriptions.stored_credential_transaction_id = invoices.payments_and_credits.payment_id ``` |
| [statements](#statements) | ``` subscriptions.credit_card.customer_id = statements.transactions.customer_id ```  ``` subscriptions.customer.id = statements.transactions.customer_id ```  ``` subscriptions.next_product_id = statements.events.event.event_specific_data.product_id ```  ``` subscriptions.product.id = statements.events.event.event_specific_data.product_id ```  ``` subscriptions.next_product_id = statements.transactions.product_id ```  ``` subscriptions.product.id = statements.transactions.product_id ```  ``` subscriptions.id = statements.events.event.subscription_id ```  ``` subscriptions.id = statements.subscription_id ```  ``` subscriptions.id = statements.transactions.subscription_id ```  ``` subscriptions.signup_payment_id = statements.transactions.id ```  ``` subscriptions.stored_credential_transaction_id = statements.transactions.id ``` |
| [transactions](#transactions) | ``` subscriptions.credit_card.customer_id = transactions.customer_id ```  ``` subscriptions.customer.id = transactions.customer_id ```  ``` subscriptions.next_product_id = transactions.product_id ```  ``` subscriptions.product.id = transactions.product_id ```  ``` subscriptions.id = transactions.subscription_id ```  ``` subscriptions.signup_payment_id = transactions.id ```  ``` subscriptions.stored_credential_transaction_id = transactions.id ```  ``` subscriptions.signup_payment_id = transactions.parent_id ```  ``` subscriptions.stored_credential_transaction_id = transactions.parent_id ```  ``` subscriptions.signup_payment_id = transactions.payment_id ```  ``` subscriptions.stored_credential_transaction_id = transactions.payment_id ``` |
| [components](#components) | ``` subscriptions.product.product_family.id = components.product_family_id ``` |
| [coupons](#coupons) | ``` subscriptions.product.product_family.id = coupons.product_family_id ``` |
| [product\_families](#product-families) | ``` subscriptions.product.product_family.id = product_families.id ``` |
| [products](#products) | ``` subscriptions.product.product_family.id = products.product_family.id ```  ``` subscriptions.next_product_id = products.id ```  ``` subscriptions.product.id = products.id ``` |
| [events](#events) | ``` subscriptions.next_product_id = events.event_specific_data.product_id ```  ``` subscriptions.product.id = events.event_specific_data.product_id ```  ``` subscriptions.id = events.subscription_id ```  ``` subscriptions.signup_payment_id = events.event_specific_data.account_transaction_id ```  ``` subscriptions.stored_credential_transaction_id = events.event_specific_data.account_transaction_id ``` |

subscriptions table schema

|  |
| --- |
| **activated\_at**  DATE-TIME |
| **balance\_in\_cents**  INTEGER |
| **cancel\_at\_end\_of\_period**  BOOLEAN |
| **canceled\_at**  DATE-TIME |
| **cancellation\_message**  STRING |
| **cancellation\_method**  STRING |
| **coupon\_codes**  STRING |
| **created\_at**  DATE-TIME |
| **credit\_card**  OBJECT This is a nested data structure:   - billing\_address: STRING - billing\_address\_2: STRING - billing\_city: STRING - billing\_country: STRING - billing\_state: STRING - billing\_zip: STRING - card\_type: STRING - current\_vault: STRING - customer\_id: INTEGER - customer\_vault\_token: STRING - expiration\_month: NUMBER - expiration\_year: NUMBER - first\_name: STRING - id: INTEGER - last\_name: STRING - masked\_card\_number: STRING - payment\_type: STRING - vault\_token: STRING |
| **current\_period\_ends\_at**  DATE-TIME |
| **current\_period\_started\_at**  DATE-TIME |
| **customer**  OBJECT This is a nested data structure:   - address: STRING - address\_2: STRING - cc\_emails: STRING - city: STRING - country: STRING - created\_at: DATE-TIME - email: STRING - first\_name: STRING - id: INTEGER - last\_name: STRING - organization: STRING - phone: STRING - portal\_customer\_created\_at: DATE-TIME - portal\_invite\_last\_accepted\_at: DATE-TIME - portal\_invite\_last\_sent\_at: DATE-TIME - reference: STRING - state: STRING - tax\_exempt: BOOLEAN - updated\_at: DATE-TIME - vat\_number: STRING - verified: BOOLEAN - zip: STRING |
| **delayed\_cancel\_at**  DATE-TIME |
| **expires\_at**  DATE-TIME |
| **id**  INTEGER |
| **net\_terms**  INTEGER |
| **next\_assessment\_at**  DATE-TIME |
| **next\_product\_id**  INTEGER |
| **payment\_collection\_method**  STRING |
| **payment\_type**  STRING |
| **previous\_state**  STRING |
| **product**  OBJECT This is a nested data structure:   - accounting\_code: STRING - archived\_at: DATE-TIME - created\_at: DATE-TIME - description: STRING - expiration\_interval: INTEGER - expiration\_interval\_unit: STRING - handle: STRING - id: INTEGER - initial\_charge\_after\_trial: BOOLEAN - initial\_charge\_in\_cents: INTEGER - interval: INTEGER - interval\_unit: STRING - name: STRING - price\_in\_cents: INTEGER - product\_family: OBJECT, which is also a nested data structure.   - accounting\_code: STRING   - description: STRING   - handle: STRING   - id: INTEGER   - name: STRING - public\_signup\_pages: ARRAY, which is also a nested data structure.   - id: INTEGER   - url: STRING - request\_credit\_card: BOOLEAN - require\_credit\_card: BOOLEAN - return\_params: STRING - taxable: BOOLEAN - trial\_interval: INTEGER - trial\_interval\_unit: STRING - trial\_price\_in\_cents: INTEGER - update\_return\_params: STRING - update\_return\_url: STRING - updated\_at: DATE-TIME - version\_number: NUMBER |
| **product\_price\_in\_cents**  INTEGER |
| **product\_version\_number**  INTEGER |
| **reason\_code**  STRING |
| **receives\_invoice\_emails**  BOOLEAN |
| **referral\_code**  STRING |
| **signup\_payment\_id**  NUMBER |
| **signup\_revenue**  STRING |
| **snap\_day**  STRING |
| **state**  STRING |
| **stored\_credential\_transaction\_id**  INTEGER |
| **total\_revenue\_in\_cents**  INTEGER |
| **trial\_ended\_at**  DATE-TIME |
| **trial\_started\_at**  DATE-TIME |
| **updated\_at**  DATE-TIME |

### transactions

The `transactions` table contains info about the transactions for your Chargify site.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Loading Behavior** | Append-Only |
| **Primary Key** | id |
| **Replication Key** | created\_at |
| **Useful links** | [Chargify API method](https://reference.chargify.com/v1/transactions/list-transactions-for-the-site "Opens in new tab: Chargify API method") |

transactions table foreign keys

| Join transactions with | on |
| --- | --- |
| [components](#components) | ``` transactions.component_id = components.id ```  ``` transactions.component_id = components.prices.id ``` |
| [invoices](#invoices) | ``` transactions.component_id = invoices.charges.component_id ```  ``` transactions.component_id = invoices.payments_and_credits.component_id ```  ``` transactions.customer_id = invoices.charges.customer_id ```  ``` transactions.customer_id = invoices.payments_and_credits.customer_id ```  ``` transactions.product_id = invoices.charges.product_id ```  ``` transactions.product_id = invoices.payments_and_credits.product_id ```  ``` transactions.statement_id = invoices.statement_id ```  ``` transactions.subscription_id = invoices.charges.subscription_id ```  ``` transactions.subscription_id = invoices.payments_and_credits.subscription_id ```  ``` transactions.subscription_id = invoices.subscription_id ```  ``` transactions.id = invoices.charges.payment_id ```  ``` transactions.parent_id = invoices.charges.payment_id ```  ``` transactions.payment_id = invoices.charges.payment_id ```  ``` transactions.id = invoices.payments_and_credits.payment_id ```  ``` transactions.parent_id = invoices.payments_and_credits.payment_id ```  ``` transactions.payment_id = invoices.payments_and_credits.payment_id ``` |
| [price\_points](#price-points) | ``` transactions.component_id = price_points.component_id ```  ``` transactions.component_id = price_points.prices.component_id ``` |
| [statements](#statements) | ``` transactions.component_id = statements.transactions.component_id ```  ``` transactions.customer_id = statements.transactions.customer_id ```  ``` transactions.product_id = statements.events.event.event_specific_data.product_id ```  ``` transactions.product_id = statements.transactions.product_id ```  ``` transactions.statement_id = statements.id ```  ``` transactions.statement_id = statements.transactions.statement_id ```  ``` transactions.subscription_id = statements.events.event.subscription_id ```  ``` transactions.subscription_id = statements.subscription_id ```  ``` transactions.subscription_id = statements.transactions.subscription_id ```  ``` transactions.id = statements.transactions.id ```  ``` transactions.parent_id = statements.transactions.id ```  ``` transactions.payment_id = statements.transactions.id ``` |
| [customers](#customers) | ``` transactions.customer_id = customers.id ```  ``` transactions.customer_id = customers.parent_id ``` |
| [subscriptions](#subscriptions) | ``` transactions.customer_id = subscriptions.credit_card.customer_id ```  ``` transactions.customer_id = subscriptions.customer.id ```  ``` transactions.product_id = subscriptions.next_product_id ```  ``` transactions.product_id = subscriptions.product.id ```  ``` transactions.subscription_id = subscriptions.id ```  ``` transactions.id = subscriptions.signup_payment_id ```  ``` transactions.parent_id = subscriptions.signup_payment_id ```  ``` transactions.payment_id = subscriptions.signup_payment_id ```  ``` transactions.id = subscriptions.stored_credential_transaction_id ```  ``` transactions.parent_id = subscriptions.stored_credential_transaction_id ```  ``` transactions.payment_id = subscriptions.stored_credential_transaction_id ``` |
| [events](#events) | ``` transactions.product_id = events.event_specific_data.product_id ```  ``` transactions.subscription_id = events.subscription_id ```  ``` transactions.id = events.event_specific_data.account_transaction_id ```  ``` transactions.parent_id = events.event_specific_data.account_transaction_id ```  ``` transactions.payment_id = events.event_specific_data.account_transaction_id ``` |
| [products](#products) | ``` transactions.product_id = products.id ``` |

transactions table schema

|  |
| --- |
| **amount\_in\_cents**  INTEGER |
| **card\_expiration**  STRING |
| **card\_number**  STRING |
| **card\_type**  STRING |
| **component\_handle**  STRING |
| **component\_id**  INTEGER |
| **component\_price\_point\_handle**  STRING |
| **component\_price\_point\_id**  INTEGER |
| **created\_at**  DATE-TIME |
| **customer\_id**  INTEGER |
| **ending\_balance\_in\_cents**  INTEGER |
| **gateway\_order\_id**  NUMBER |
| **gateway\_transaction\_id**  STRING |
| **gateway\_used**  STRING |
| **id**  INTEGER |
| **item\_name**  STRING |
| **kind**  STRING |
| **memo**  STRING |
| **parent\_id**  INTEGER |
| **payment\_id**  INTEGER |
| **period\_range\_end**  STRING |
| **period\_range\_start**  STRING |
| **price\_point\_handle**  STRING |
| **price\_point\_id**  INTEGER |
| **product\_id**  INTEGER |
| **refunded\_amount\_in\_cents**  INTEGER |
| **role**  STRING |
| **starting\_balance\_in\_cents**  INTEGER |
| **statement\_id**  INTEGER |
| **subscription\_id**  INTEGER |
| **success**  BOOLEAN |
| **tax\_id**  INTEGER |
| **transaction\_type**  STRING |
| **type**  STRING |
