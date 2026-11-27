---
title: "Recharge"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Recharge.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Recharge

Recharge helps ecommerce businesses by offering subscriptions and recurring billing for their customers.

For more information about the API, see [Recharge Payments API](https://developer.rechargepayments.com/).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To generate the access token:

1. Make sure you have a Shopify account. You need it to access your Recharge information.
2. Log into your Shopify account, select Apps, and then click your Recharge application.
3. Go to the Tools & apps page.
4. Click API tokens.
5. Click Create an API token.
6. On the Create an API token page:
   - In the Details section, enter a Token nickname and Contact email into their respective fields.
   - In the Permission section, select the Read Access scope for each permission.
7. Click Save.
8. Copy the token.

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

### addresses

The `addresses` table contains info about the addresses (shipping locations) a customer has. A subscription is tied to a given address, but a customer can have multiple addresses.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Recharge API method](https://developer.rechargepayments.com/2021-11/addresses/list_addresses "Opens in new tab: Recharge API method") |

addresses table foreign keys

| Join addresses with | on |
| --- | --- |
| [charges](#charges) | ``` addresses.id = charges.address_id ```  ``` addresses.customer_id = charges.customer_id ``` |
| [onetimes](#onetimes) | ``` addresses.id = onetimes.address_id ```  ``` addresses.customer_id = onetimes.customer_id ``` |
| [orders](#orders) | ``` addresses.id = orders.address_id ```  ``` addresses.customer_id = orders.customer_id ``` |
| [subscriptions](#subscriptions) | ``` addresses.id = subscriptions.address_id ```  ``` addresses.customer_id = subscriptions.customer_id ``` |
| [customers](#customers) | ``` addresses.customer_id = customers.id ``` |
| [discounts](#discounts) | ``` addresses.discount_id = discounts.id ``` |

addresses table schema

|  |
| --- |
| **address1**  STRING |
| **address2**  STRING |
| **cart\_attributes**    ARRAY This is a nested data structure:   - **name**: STRING - **value**: STRING |
| **cart\_note**  STRING |
| **city**  STRING |
| **company**  STRING |
| **country**  STRING |
| **country\_code**  STRING |
| **created\_at**  DATE-TIME |
| **customer\_id**  INTEGER |
| **discount\_id**  INTEGER |
| **discounts**    ARRAY This is a nested data structure:   - **id**: INTEGER |
| **first\_name**  STRING |
| **id**  INTEGER |
| **last\_name**  STRING |
| **note\_attributes**    ARRAY This is a nested data structure:   - **name**: STRING - **value**: STRING |
| **order\_attributes**    ARRAY This is a nested data structure:   - **name**: STRING - **value**: STRING |
| **order\_note**  STRING |
| **original\_shipping\_lines**    ARRAY This is a nested data structure:   - **code**: STRING - **price**: STRING - **title**: STRING |
| **payment\_method\_id**  INTEGER |
| **phone**  STRING |
| **presentment\_currency**  STRING |
| **province**  STRING |
| **shipping\_lines\_override**    ARRAY This is a nested data structure:   - **code**: STRING - **price**: STRING - **title**: STRING |
| **updated\_at**  DATE-TIME |
| **zip**  STRING |

### charges

The `charges` table contains info about charges. A charge is a placeholder for an upcoming charge once the charge is processed successfully.

|  |  |
| --- | --- |
| **Replication Method>** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Recharge API method](https://developer.rechargepayments.com/2021-11/charges/charge_list "Opens in new tab: Recharge API method") |

charges table foreign keys

| Join charges with | on |
| --- | --- |
| [addresses](#addresses) | ``` charges.address_id = addresses.id ```  ``` charges.customer_id = addresses.customer_id ``` |
| [onetimes](#onetimes) | ``` charges.address_id = onetimes.address_id ```  ``` charges.customer_id = onetimes.customer_id ```  ``` charges.line_items.shopify_product_id = onetimes.shopify_product_id ``` |
| [orders](#orders) | ``` charges.address_id = orders.address_id ```  ``` charges.id = orders.charge_id ```  ``` charges.customer_id = orders.customer_id ```  ``` charges.line_items.shopify_product_id = orders.line_items.shopify_product_id ```  ``` charges.line_items.subscription_id = orders.line_items.subscription_id ``` |
| [subscriptions](#subscriptions) | ``` charges.address_id = subscriptions.address_id ```  ``` charges.customer_id = subscriptions.customer_id ```  ``` charges.line_items.shopify_product_id = subscriptions.shopify_product_id ```  ``` charges.line_items.subscription_id = subscriptions.id ``` |
| [customers](#customers) | ``` charges.customer_id = customers.id ``` |
| [products](#products) | ``` charges.line_items.shopify_product_id = products.id ``` |

charges table schema

|  |
| --- |
| **address\_id**  INTEGER |
| **analytics\_data**  OBJECT This is a nested data structure: **utm\_params**, ARRAY, which is also a nested data structure   - **utm\_campaign**: STRING - **utm\_content**: STRING - **utm\_data\_source**: STRING - **utm\_medium**: STRING - **utm\_source**: STRING - **utm\_term**: STRING - **utm\_timestamp**: STRING |
| **billing\_address**  OBJECT This is a nested data structure:   - **address1**: STRING - **address2**: STRING - **city**: STRING - **company**: STRING - **country**: STRING - **country\_code**: STRING - **first\_name**: STRING - **last\_name**: STRING - **phone**: STRING - **province**: STRING - **zip**: STRING |
| **browser\_ip**  STRING |
| **client\_details**  OBJECT This is a nested data structure:   - **browser\_ip**: STRING - **user\_agent**: STRING |
| **created\_at**  DATE-TIME |
| **currency**  STRING |
| **customer**  OBJECT This is a nested data structure:   - **email**: STRING - **external\_customer\_id**: OBJECT, which is also a nested data structure:   - **ecommerce**: STRING - **hash**: STRING - **id**: INTEGER |
| **customer\_hash**  STRING |
| **customer\_id**  INTEGER |
| **discount\_codes**    ARRAY This is a nested data structure:   - **amount**: STRING - **code**: STRING - **id**: INTEGER - **value**: NUMBER - **value\_type**: STRING |
| **email**  STRING |
| **external\_order\_id**  OBJECT This is a nested data structure: **ecommerce**, STRING. |
| **external\_transaction\_id**  OBJECT This is a nested data structure: **payment\_processor**, STRING. |
| **first\_name**  STRING |
| **has\_uncommited\_changes**  BOOLEAN |
| **id**  INTEGER |
| **last\_name**  STRING |
| **line\_items**    ARRAY This is a nested data structure:   - **external\_product\_id**, OBJECT, which is also a nested data structure:   - **ecommerce**: STRING - **external\_product\_id**, OBJECT, which is also a nested data structure:   - **ecommerce**: STRING - **grams**: INTEGER - **handle**: STRING - **images**: OBJECT   - **large**: STRING   - **medium**: STRING   - **original**: STRING   - **small**: STRING   - **sort\_order**: INTEGER - **price**: STRING - **properties**: ARRAY, which is also a nested data structure:   - **name**: STRING   - **value**: STRING- **purchase\_item\_id**: INTEGER   - **purchase\_item\_type**: STRING   - **quantity**: STRING   - **shopify\_product\_id**: STRING   - **shopify\_variant\_id**: STRING   - **sku**: STRING   - **subscription\_id**: INTEGER   - **tax\_due**: STRING   - **tax\_lines**: ARRAY, which is also a nested data structure:     - **price**: STRING     - **rate**: STRING     - **title**: STRING   - **taxable**: BOOLEAN   - **taxable\_amount**: STRING   - **title**: STRING   - **total\_price**: STRING   - **unit\_price**: STRING   - **unit\_price\_includes\_tax**: BOOLEAN   - **variant\_title**: BOOLEAN |
| **note**  STRING |
| **note\_attributes**    ARRAY This is a nested data structure:   - **name**: STRING - **value**: STRING |
| **order\_attributes**    ARRAY This is a nested data structure:   - **name**: STRING - **value**: STRING |
| **orders\_count**  INTEGER |
| **payment\_processor**  STRING |
| **processed\_at**  DATE-TIME |
| **processor\_name**  STRING |
| **retry\_date**  DATE-TIME |
| **scheduled\_at**  DATE-TIME |
| **shipments\_count**  INTEGER |
| **shipping\_address**  OBJECT This is a nested data structure:   - **address1**: STRING - **address2**: STRING - **city**: STRING - **company**: STRING - **country**: STRING - **country\_code**: STRING - **first\_name**: STRING - **last\_name**: STRING - **phone**: STRING - **province**: STRING - **zip**: STRING |
| **shipping\_lines**    ARRAY This is a nested data structure:   - **code**: STRING - **price**: STRING - **source**: STRING - **tax\_lines**: ARRAY, which is also a nested data structure:   - **price**: STRING   - **rate**: STRING   - **title**: STRING - **taxable**: STRING - **title**: STRING |
| **shopify\_order\_id**  STRING |
| **status**  STRING |
| **sub\_total**  STRING |
| **subtotal\_price**  STRING |
| **tags**  STRING |
| **tax\_lines**    ARRAY This is a nested data structure:   - **price**: STRING - **rate**: STRING - **title**: STRING |
| **taxable**  BOOLEAN |
| **total\_discounts**  STRING |
| **total\_line\_items\_price**  STRING |
| **total\_price**  STRING |
| **total\_refunds**  STRING |
| **total\_tax**  STRING |
| **total\_weight**  INTEGER |
| **total\_weight\_grams**  INTEGER |
| **transaction\_id**  STRING |
| **type**  STRING |
| **updated\_at**  DATE-TIME |

### collections

The `collections` table contains info about your collections.

|  |  |
| --- | --- |
| **Replication Method>** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Recharge API method](https://developer.rechargepayments.com/2021-11/collection_products "Opens in new tab: Recharge API method") |

collections table foreign keys

| Join collections with | on |
| --- | --- |
| [products](#products) | ``` collections.id = products.collection_id ``` |

collections table schema

|  |
| --- |
| **created\_at**  DATE-TIME |
| **description**  STRING |
| **id**  INTEGER |
| **name**  STRING |
| **sort\_order**  STRING |
| **title**  STRING |
| **type**  STRING |
| **updated\_at**  DATE-TIME |

### customers

The `customers` table contains info about customer accounts with a store.

|  |  |
| --- | --- |
| **Replication Method>** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Recharge API method](https://developer.rechargepayments.com/2021-11/customers/customers_list "Opens in new tab: Recharge API method") |

customers table foreign keys

| Join customers with | on |
| --- | --- |
| [addresses](#addresses) | ``` customers.id = addresses.customer_id ``` |
| [charges](#charges) | ``` customers.id = charges.customer_id ``` |
| [onetimes](#onetimes) | ``` customers.id = onetimes.customer_id ``` |
| [orders](#orders) | ``` customers.id = orders.customer_id ``` |
| [subscriptions](#subscriptions) | ``` customers.id = subscriptions.customer_id ``` |

customers table schema

|  |
| --- |
| **analytics\_data**  OBJECT This is a nested data structure: **utm\_params**, ARRAY, which is also a nested data structure:  - **utm\_campaign**: STRING - **utm\_content**: STRING - **utm\_data\_source**: STRING - **utm\_medium**: STRING - **utm\_source**: STRING - **utm\_term**: STRING - **utm\_timestamp**: STRING |
| **billing\_address1**  STRING |
| **billing\_address2**  STRING |
| **billing\_city**  STRING |
| **billing\_company**  STRING |
| **billing\_country**  STRING |
| **billing\_phone**  STRING |
| **billing\_province**  STRING |
| **billing\_zip**  STRING |
| **braintree\_customer\_token**  STRING |
| **created\_at**  DATE-TIME |
| **email**  STRING |
| **external\_customer\_id**  OBJECT This is a nested data structure: **ecommerce**: STRING |
| **first\_charge\_processed\_at**  DATE-TIME |
| **first\_name**  STRING |
| **has\_card\_error\_in\_dunning**  BOOLEAN |
| **has\_payment\_method\_in\_dunning**  BOOLEAN |
| **has\_valid\_payment\_method**  BOOLEAN |
| **hash**  STRING |
| **id**  INTEGER |
| **last\_name**  STRING |
| **number\_active\_subscriptions**  INTEGER |
| **number\_subscriptions**  INTEGER |
| **paypal\_customer\_token**  STRING |
| **processor\_type**  STRING |
| **reason\_payment\_method\_not\_valid**  STRING |
| **status**  STRING |
| **subscriptions\_active\_count**  INTEGER |
| **subscriptions\_total\_count**  INTEGER |
| **updated\_at**  DATE-TIME |

### discounts

The `discounts` table contains info about discounts.

|  |  |
| --- | --- |
| **Replication Method>** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Recharge API method](https://developer.rechargepayments.com/2021-11/discounts/discounts_list "Opens in new tab: Recharge API method") |

discounts table foreign keys

| Join discounts with | on |
| --- | --- |
| [addresses](#addresses) | ``` discounts.id = addresses.discount_id ``` |

discounts table schema

|  |
| --- |
| **applies\_to**  OBJECT This is a nested data structure:**ids**: ARRAY, which is also a nested data structure:   - **purchase\_item\_type**: STRING - **resource**: STRING |
| **applies\_to\_id**  INTEGER |
| **applies\_to\_product\_type**  STRING |
| **applies\_to\_resource**  STRING |
| **channel\_settings**  OBJECT This is a nested data structure:   - **api**, OBJECT, which is also a nested data structure:   - **can\_apply**: BOOLEAN - **checkout\_page**: OBJECT, which is also a nested data structure:   - **can\_apply**: BOOLEAN - **customer\_portal**: OBJECT, which is also a nested data structure:   - **can\_apply**: BOOLEAN - **merchant\_portal**: OBJECT, which is also a nested data structure:   - **can\_apply**: BOOLEAN |
| **code**  STRING |
| **created\_at**  DATE-TIME |
| **duration**  STRING |
| **duration\_usage\_limit**  INTEGER |
| **ends\_at**  DATE-TIME |
| **external\_discount\_id**  OBJECT This is a nested data structure: **ecommerce**: STRING. |
| **first\_time\_customer\_restriction**  BOOLEAN |
| **id**  INTEGER |
| **once\_per\_customer**  BOOLEAN |
| **prerequisite\_subtotal\_min**  STRING |
| **starts\_at**  DATE-TIME |
| **status**  STRING |
| **times\_used**  INTEGER |
| **updated\_at**  DATE-TIME |
| **usage\_limit**  INTEGER |
| **usage\_limits**  OBJECT This is a nested data structure:   - **first\_time\_customer\_restriction**: BOOLEAN - **max\_subsequent\_redemptions**: INTEGER - **one\_application\_per\_customer**: STRING |
| **value**  STRING |
| **value\_type**  STRING |

### metafields\_customer

The `metafields_customer` table contains info about metafields related to customers.

|  |  |
| --- | --- |
| **Replication Method>** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Recharge API method](https://developer.rechargepayments.com/2021-11/metafields/metafields_list "Opens in new tab: Recharge API method") |

metafields\_customer table schema

|  |
| --- |
| **created\_at**  DATE-TIME |
| **description**  STRING |
| **id**  INTEGER |
| **key**  STRING |
| **namespace**  STRING |
| **owner\_id**  STRING |
| **owner\_resource**  STRING |
| **updated\_at**  DATE-TIME |
| **value**  STRING |
| **value\_type**  STRING |

### metafields\_store

The `metafields_store` table contains info about metafields related to stores.

|  |  |
| --- | --- |
| **Replication Method>** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Recharge API method](https://developer.rechargepayments.com/2021-11/metafields/metafields_list "Opens in new tab: Recharge API method") |

metafields\_store table schema

|  |
| --- |
| **created\_at**  DATE-TIME |
| **description**  STRING |
| **id**  INTEGER |
| **key**  STRING |
| **namespace**  STRING |
| **owner\_id**  STRING |
| **owner\_resource**  STRING |
| **updated\_at**  DATE-TIME |
| **value**  STRING |
| **value\_type**  STRING |

### metafields\_subscription

The `metafields_subscription` table contains info about metafields related to subscriptions.

|  |  |
| --- | --- |
| **Replication Method>** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Recharge API method](https://developer.rechargepayments.com/2021-11/metafields/metafields_list "Opens in new tab: Recharge API method") |

metafields\_subscription table schema

|  |
| --- |
| **created\_at**  DATE-TIME |
| **description**  STRING |
| **id**  INTEGER |
| **key**  STRING |
| **namespace**  STRING |
| **owner\_id**  STRING |
| **owner\_resource**  STRING |
| **updated\_at**  DATE-TIME |
| **value**  STRING |
| **value\_type**  STRING |

### onetimes

The `onetimes` table contains info about one time products.

|  |  |
| --- | --- |
| **Replication Method>** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Recharge API method](https://developer.rechargepayments.com/2021-11/onetimes/onetimes_list "Opens in new tab: Recharge API method") |

onetimes table foreign keys

| Join onetimes with | on |
| --- | --- |
| [addresses](#addresses) | ``` onetimes.address_id = addresses.id ```  ``` onetimes.customer_id = addresses.customer_id ``` |
| [charges](#charges) | ``` onetimes.address_id = charges.address_id ```  ``` onetimes.customer_id = charges.customer_id ```  ``` onetimes.shopify_product_id = charges.line_items.shopify_product_id ``` |
| [orders](#orders) | ``` onetimes.address_id = orders.address_id ```  ``` onetimes.customer_id = orders.customer_id ```  ``` onetimes.shopify_product_id = orders.line_items.shopify_product_id ``` |
| [subscriptions](#subscriptions) | ``` onetimes.address_id = subscriptions.address_id ```  ``` onetimes.customer_id = subscriptions.customer_id ```  ``` onetimes.shopify_product_id = subscriptions.shopify_product_id ``` |
| [customers](#customers) | ``` onetimes.customer_id = customers.id ``` |
| [products](#products) | ``` onetimes.shopify_product_id = products.id ``` |

onetimes table schema

|  |
| --- |
| **address\_id**  INTEGER |
| **created\_at**  DATE-TIME |
| **customer\_id**  INTEGER |
| **external\_product\_id**  OBJECT This is a nested data structure: **ecommerce**, STRING. |
| **external\_variant\_id**  OBJECT This is a nested data structure: **ecommerce**, STRING. |
| **id**  INTEGER |
| **next\_charge\_scheduled\_at**  DATE-TIME |
| **price**  STRING |
| **product\_title**  STRING |
| **properties**    ARRAY This is a nested data structure:   - **name**: STRING - **value**: STRING |
| **quantity**  INTEGER |
| **recharge\_product\_id**  INTEGER |
| **shopify\_product\_id**  INTEGER |
| **shopify\_variant\_id**  INTEGER |
| **sku**  STRING |
| **sku\_override**  BOOLEAN |
| **status**  STRING |
| **updated\_at**  DATE-TIME |
| **variant\_title**  STRING |

### orders

The `orders` table contains info about orders. Orders are created after a charge is successfully processed.

|  |  |
| --- | --- |
| **Replication Method>** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Recharge API method](https://developer.rechargepayments.com/2021-11/orders/orders_list "Opens in new tab: Recharge API method") |

orders table foreign keys

| Join orders with | on |
| --- | --- |
| [addresses](#addresses) | ``` orders.address_id = addresses.id ```  ``` orders.customer_id = addresses.customer_id ``` |
| [charges](#charges) | ``` orders.address_id = charges.address_id ```  ``` orders.charge_id = charges.id ```  ``` orders.customer_id = charges.customer_id ```  ``` orders.line_items.shopify_product_id = charges.line_items.shopify_product_id ```  ``` orders.line_items.subscription_id = charges.line_items.subscription_id ``` |
| [onetimes](#onetimes) | ``` orders.address_id = onetimes.address_id ```  ``` orders.customer_id = onetimes.customer_id ```  ``` orders.line_items.shopify_product_id = onetimes.shopify_product_id ``` |
| [subscriptions](#subscriptions) | ``` orders.address_id = subscriptions.address_id ```  ``` orders.customer_id = subscriptions.customer_id ```  ``` orders.line_items.shopify_product_id = subscriptions.shopify_product_id ```  ``` orders.line_items.subscription_id = subscriptions.id ``` |
| [customers](#customers) | ``` orders.customer_id = customers.id ``` |
| [products](#products) | ``` orders.line_items.shopify_product_id = products.id ``` |

orders table schema

|  |
| --- |
| **address\_id**  INTEGER |
| **address\_is\_active**  INTEGER |
| **billing\_address**  OBJECT This is a nested data structure:   - **address1**: STRING - **address2**: STRING - **city**: STRING - **company**: STRING - **country**: STRING - **country\_code**: STRING - **first\_name**: STRING - **last\_name**: STRING - **phone**: STRING - **province**: STRING - **zip**: STRING |
| **charge**  OBJECT This is a nested data structure:   - **external\_transaction\_id** OBJECT, which is also a nested data structure:   - **payment\_processor**: STRING - **id**: INTEGER |
| **charge\_id**  INTEGER |
| **charge\_status**  STRING |
| **client\_details**  OBJECT This is a nested data structure:   - **browser\_ip**: STRING - **user\_agent**: STRING |
| **created\_at**  DATE-TIME |
| **currency**  STRING |
| **customer**  OBJECT This is a nested data structure:   - **email**: STRING - **external\_customer\_id**: OBJECT, which is also a nested data structure:   - **ecommerce**: STRING - **hash**: STRING - **id**: INTEGER |
| **customer\_id**  INTEGER |
| **discount\_codes**    ARRAY This is a nested data structure:   - **amount**: STRING - **code**: STRING - **type**: STRING |
| **discounts**    ARRAY This is a nested data structure:   - **code**: STRING - **id**: INTEGER - **value**: NUMBER - **value\_type**: STRING |
| **email**  STRING |
| **external\_cart\_token**  STRING |
| **external\_order\_id**  OBJECT This is a nested data structure: **ecommerce**, STRING. |
| **external\_order\_number**  OBJECT This is a nested data structure: **ecommerce**, STRING. |
| **first\_name**  STRING |
| **hash**  STRING |
| **id**  INTEGER |
| **is\_prepaid**  BOOLEAN |
| **last\_name**  STRING |
| **line\_items**    ARRAY This is a nested data structure:   - **external\_product\_id**: OBJECT, which is also a nested data structure:   - **ecommerce**: STRING - **external\_variant\_id**: OBJECT, which is also a nested data structure:   - **ecommerce**: STRING - **grams**: INTEGER - **handle**: STRING - **images**: OBJECT, which is also a nested data structure:   - **large**: STRING   - **medium**: STRING   - **original**: STRING   - **small**: STRING   - **sort\_order**: INTEGER - **price**: NUMBER - **properties**: ARRAY, which is also a nested data structure:   - **name**: STRING   - **value**: STRING - **purchase\_item\_id**: INTEGER - **purchase\_item\_type**: STRING - **quantity**: INTEGER - **shopify\_product\_id**: STRING - **shopify\_variant\_id**: STRING - **sku**: STRING - **sort\_order**: INTEGER - **subscription\_id**: INTEGER - **tax\_due**: STRING - **tax\_lines**: ARRAY, which is also a nested data structure:   - **price**: STRING   - **rate**: STRING   - **title**: INTEGER - **taxable**: BOOLEAN - **taxable\_amount**: STRING - **title**: STRING - **total\_price**: STRING - **unit\_price**: STRING - **unit\_price\_includes\_tax**: BOOLEAN - **variant\_title**: STRING |
| **note**  STRING |
| **note\_attributes**    ARRAY This is a nested data structure:   - **name**: STRING - **value**: STRING |
| **order\_attributes**    ARRAY This is a nested data structure:   - **name**: STRING - **value**: STRING |
| **payment\_processor**  STRING |
| **processed\_at**  DATE-TIME |
| **scheduled\_at**  DATE-TIME |
| **shipped\_date**  DATE-TIME |
| **shipping\_address**  OBJECT This is a nested data structure:   - **address1**: STRING - **address1**: STRING - **city**: STRING - **company**: STRING - **country**: STRING - **country\_code**: STRING - **first\_name**: STRING - **last\_name**: STRING - **phone**: STRING - **province**: STRING - **zip**: STRING |
| **shipping\_date**  DATE-TIME |
| **shipping\_lines**    ARRAY This is a nested data structure:   - **code**: STRING - **price**: STRING - **source**: STRING - **tax\_lines**: ARRAY, which is also a nested data structre:   - **price**: STRING   - **rate**: STRING   - **title**: STRING - **taxable**: STRING - **title**: STRING |
| **shopify\_cart\_token**  STRING |
| **shopify\_customer\_id**  STRING |
| **shopify\_id**  STRING |
| **shopify\_order\_id**  STRING |
| **shopify\_order\_number**  INTEGER |
| **status**  STRING |
| **subtotal\_price**  STRING |
| **tags**  STRING |
| **tax\_lines**    ARRAY This is a nested data structure:   - **code**: STRING - **price**: STRING - **rate**: STRING - **title**: STRING |
| **taxable**  BOOLEAN |
| **total\_discounts**  STRING |
| **total\_line\_items\_price**  NUMBER |
| **total\_price**  STRING |
| **total\_refunds**  STRING |
| **total\_tax**  STRING |
| **total\_weight**  INTEGER |
| **total\_weight\_grams**  INTEGER |
| **transaction\_id**  STRING |
| **type**  STRING |
| **updated\_at**  DATE-TIME |

### products

The `products` table contains info about your products. This table uses the 2021-01 API version.

|  |  |
| --- | --- |
| **Replication Method>** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Recharge documentation](https://developer.rechargepayments.com/2021-11/products/products_list)  [Recharge API method](https://developer.rechargepayments.com/2021-01/products/products_list "Opens in new tab: Recharge API method") |

products table foreign keys

| Join products with | on |
| --- | --- |
| [collections](#collections) | ``` products.collection_id = collections.id ``` |
| [charges](#charges) | ``` products.id = charges.line_items.shopify_product_id ``` |
| [onetimes](#onetimes) | ``` products.id = onetimes.shopify_product_id ``` |
| [orders](#orders) | ``` products.id = orders.line_items.shopify_product_id ``` |
| [subscriptions](#subscriptions) | ``` products.id = subscriptions.shopify_product_id ``` |

products table schema

|  |
| --- |
| **collection\_id**  INTEGER |
| **created\_at**  DATE-TIME |
| **discount\_amount**  NUMBER |
| **discount\_type**  STRING |
| **handle**  STRING |
| **id**  INTEGER |
| **images**  OBJECT This is a nested data structure:   - **large**: STRING - **medium**: STRING - **original**: STRING - **small**: STRING |
| **product\_id**  INTEGER |
| **shopify\_product\_id**  INTEGER |
| **subscription\_defaults**  OBJECT This is a nested data structure:   - **charge\_interval\_frequency**: INTEGER - **cutoff\_day\_of\_month**: STRING - **cutoff\_day\_of\_week**: STRING - **expire\_after\_specific\_number\_of\_charges**: INTEGER - **handle**: STRING - **modifiable\_properties**: ARRAY, which is also a nested data structure:   - **number\_charges\_until\_expiration**: INTEGER   - **order\_day\_of\_month**: STRING   - **order\_day\_of\_week**: STRING   - **order\_interval\_frequency**: INTEGER   - **order\_interval\_frequency\_options**: ARRAY     - **order\_interval\_unit**: STRING     - **storefront\_purchase\_options**: STRING |
| **title**  STRING |
| **updated\_at**  DATE-TIME |

### store

The `store` table contains info about your store.

|  |  |
| --- | --- |
| **Replication Method>** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Recharge API method](https://developer.rechargepayments.com/2021-11/store/store_retrieve "Opens in new tab: Recharge API method") |

store table schema

|  |
| --- |
| **checkout\_logo\_url**  STRING |
| **checkout\_platform**  STRING |
| **created\_at**  DATE-TIME |
| **currency**  STRING |
| **customer\_portal\_base\_url**  STRING |
| **default\_api\_version**  STRING |
| **domain**  STRING |
| **email**  STRING |
| **external\_platform**  STRING |
| **iana\_timezone**  STRING |
| **id**  INTEGER |
| **identifier**  STRING |
| **merchant\_portal\_base\_url**  STRING |
| **my\_shopify\_domain**  STRING |
| **name**  STRING |
| **phone**  STRING |
| **shop\_email**  STRING |
| **shop\_phone**  STRING |
| **timezone**  OBJECT This is a nested data structure:   - **iana\_name**: STRING - **iana\_timezone**: STRING - **name**: STRING |
| **updated\_at**  DATE-TIME |
| **weight\_unit**  STRING |

### subscriptions

The `subscriptions` table contains info about subscriptions. Subscriptions are individual items that customers receive on a recurring basis.

|  |  |
| --- | --- |
| **Replication Method>** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Recharge API method](https://developer.rechargepayments.com/2021-11/subscriptions/subscriptions_list "Opens in new tab: Recharge API method") |

subscriptions table foreign keys

| Join subscriptions with | on |
| --- | --- |
| [addresses](#addresses) | ``` subscriptions.address_id = addresses.id ```  ``` subscriptions.customer_id = addresses.customer_id ``` |
| [charges](#charges) | ``` subscriptions.address_id = charges.address_id ```  ``` subscriptions.customer_id = charges.customer_id ```  ``` subscriptions.shopify_product_id = charges.line_items.shopify_product_id ```  ``` subscriptions.id = charges.line_items.subscription_id ``` |
| [onetimes](#onetimes) | ``` subscriptions.address_id = onetimes.address_id ```  ``` subscriptions.customer_id = onetimes.customer_id ```  ``` subscriptions.shopify_product_id = onetimes.shopify_product_id ``` |
| [orders](#orders) | ``` subscriptions.address_id = orders.address_id ```  ``` subscriptions.customer_id = orders.customer_id ```  ``` subscriptions.shopify_product_id = orders.line_items.shopify_product_id ```  ``` subscriptions.id = orders.line_items.subscription_id ``` |
| [customers](#customers) | ``` subscriptions.customer_id = customers.id ``` |
| [products](#products) | ``` subscriptions.shopify_product_id = products.id ``` |

subscriptions table schema

|  |
| --- |
| **address\_id**  INTEGER |
| **analytics\_data**  OBJECT This is a nested data structure: **utm\_params**, ARRAY, which is also a nested data structure:   - **utm\_campaign**: STRING - **utm\_content**: STRING - **utm\_data\_source**: STRING - **utm\_medium**: STRING - **utm\_source**: STRING - **utm\_term**: STRING - **utm\_timestamp**: STRING |
| **cancellation\_reason**  STRING |
| **cancellation\_reason\_comments**  STRING |
| **cancelled\_at**  DATE-TIME |
| **charge\_interval\_frequency**  STRING |
| **created\_at**  DATE-TIME |
| **customer\_id**  INTEGER |
| **expire\_after\_specific\_number\_of\_charges**  INTEGER |
| **external\_product\_id**  OBJECT This is a nested data structure: **ecommerce**, STRING. |
| **external\_variant\_id**  OBJECT This is a nested data structure: **ecommerce**, STRING. |
| **has\_queued\_charges**  BOOLEAN |
| **id**  INTEGER |
| **is\_prepaid**  BOOLEAN |
| **is\_skippable**  BOOLEAN |
| **is\_swappable**  BOOLEAN |
| **max\_retries\_reached**  BOOLEAN |
| **next\_charge\_scheduled\_at**  DATE-TIME |
| **order\_day\_of\_month**  STRING |
| **order\_day\_of\_week**  STRING |
| **order\_interval\_frequency**  STRING |
| **order\_interval\_unit**  STRING |
| **presentment\_currency**  STRING |
| **price**  STRING |
| **product\_title**  STRING |
| **properties**    ARRAY This is a nested data structure:   - **name**: STRING - **value**: STRING |
| **quantity**  INTEGER |
| **recharge\_product\_id**  INTEGER |
| **shopify\_product\_id**  INTEGER |
| **shopify\_variant\_id**  INTEGER |
| **sku**  STRING |
| **sku\_override**  BOOLEAN |
| **status**  STRING |
| **updated\_at**  DATE-TIME |
| **variant\_title**  STRING |
