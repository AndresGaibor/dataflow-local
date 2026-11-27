---
title: "BigCommerce"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-BigCommerce.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# BigCommerce

BigCommerce is an eCommerce platform to help retailers and brands create and manage their online businesses.

BigCommerce integration replicates data using the [BigCommerce REST API](https://developer.bigcommerce.com/).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To retrieve your API credentials:

1. Log into your [BigCommerce account](https://login.bigcommerce.com/login) as the store owner.
2. Click Advanced Settings > API Accounts. The Store API Accounts page is displayed.
3. Click Create API Account.
4. In the Name field, enter a name for your app.
5. In the OAuth Scopes section, set the following permission fields to read-only:
   - Customers.
   - Marketing.
   - Orders.
   - Products.
6. Click Save. The account is created.
7. From the pop-up window, download the .txt file containing your API credentials.

   If you are not prompted to download the .txt file or encounter other issues, contact [BigCommerce support](https://support.bigcommerce.com/s/?language=en_US).
8. Open the file and copy the credentials.

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
| Client ID | Client ID. |
| Access Token | Access token. |
| Store Hash | Store hash. The value between `stores/` and `/v3/` in the API path is your store hash. For example: If the API path were https://api.bigcommerce.com/stores/123456/v3/, the store hash would be 123456. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### coupons

The `coupons` table contains info about the coupons in your BigCommerce store.

Information note **Tip:**
This table uses Full Table Replication, which means all records will be replicated during every replication job.
To avoid re-replicating unnecessary data, create a second BigCommerce integration in your Stitch account (you can even use the same BigCommerce API credentials) and set the integration to replicate every 12 or 24 hours.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [BigCommerce API method](https://developer.bigcommerce.com/api-reference/marketing/marketing-api/coupons/getallcoupons "Opens in new tab: BigCommerce API method") |

coupons table foreign keys

| Join coupons with | on |
| --- | --- |
| [orders](#orders) | ``` coupons.id = orders.coupons.coupon_id ```  ``` coupons.id = orders.products.applied_discounts.id ``` |

coupons table schema

|  |
| --- |
| **amount**  NUMBER |
| **applies\_to**  OBJECT This is a nested data structure:   - entity: STRING - ids: ARRAY, which is also a nested data structure. |
| **code**  STRING |
| **date\_created**  DATE-TIME |
| **enabled**  BOOLEAN |
| **expires**  DATE-TIME |
| **id**  INTEGER |
| **max\_uses**  INTEGER |
| **max\_uses\_per\_customer**  INTEGER |
| **min\_purchase**  NUMBER |
| **name**  STRING |
| **num\_uses**  INTEGER |
| **restricted\_to**  ARRAY This is a nested data structure:   - countries: ARRAY, which is also a nested data structure. |
| **shipping\_methods**  ARRAY This is a nested data structure. |
| **type**  STRING |

### customers

The `customers` table contains info about the customers in your BigCommerce store.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | date\_modified |
| **Useful links** | [BigCommerce API method](https://developer.bigcommerce.com/api-reference/customer-subscribers/customers-api/customers/getallcustomers "Opens in new tab: BigCommerce API method") |

customers table foreign keys

| Join customers with | on |
| --- | --- |
| [orders](#orders) | ``` customers.id = orders.customer_id ``` |

customers table schema

|  |
| --- |
| **accepts\_marketing**  BOOLEAN |
| **company**  STRING |
| **customer\_group\_id**  INTEGER |
| **date\_created**  DATE-TIME |
| **date\_modified**  DATE-TIME |
| **email**  STRING |
| **first\_name**  STRING |
| **form\_fields**  ARRAY This is a nested data structure:   - name: STRING - value: STRING |
| **id**  INTEGER |
| **last\_name**  STRING |
| **notes**  STRING |
| **phone**  STRING |
| **registration\_ip\_address**  STRING |
| **reset\_pass\_on\_login**  BOOLEAN |
| **store\_credit**  NUMBER |
| **tax\_exempt\_category**  STRING |

### orders

The `orders` table contains info about the orders in your BigCommerce store.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | date\_modified |
| **Useful links** | [BigCommerce API method](https://developer.bigcommerce.com/Content/rest-management/orders#get-all-orders "Opens in new tab: BigCommerce API method") |

orders table foreign keys

| Join orders with | on |
| --- | --- |
| [coupons](#coupons) | ``` orders.coupons.coupon_id = coupons.id ```  ``` orders.products.applied_discounts.id = coupons.id ``` |
| [customers](#customers) | ``` orders.customer_id = customers.id ``` |
| [products](#products) | ``` orders.products.product_id = products.id ```  ``` orders.products.parent_order_product_id = products.id ```  ``` orders.products.product_id = products.images.product_id ```  ``` orders.products.parent_order_product_id = products.images.product_id ```  ``` orders.products.product_id = products.related_products.items ```  ``` orders.products.parent_order_product_id = products.related_products.items ```  ``` orders.products.product_id = products.variants.product_id ```  ``` orders.products.parent_order_product_id = products.variants.product_id ``` |

orders table schema

|  |
| --- |
| **base\_handling\_cost**  NUMBER |
| **base\_shipping\_cost**  NUMBER |
| **base\_wrapping\_cost**  NUMBER |
| **billing\_address**  OBJECT This is a nested data structure:   - city: STRING - company: STRING - country: STRING - country\_iso2: STRING - email: STRING - first\_name: STRING - form\_fields: ARRAY, which is also a nested data structure.   - name: STRING   - value: STRING - last\_name: STRING - phone: STRING - state: STRING - street\_1: STRING - street\_2: STRING - zip: STRING |
| **cart\_id**  STRING |
| **channel\_id**  INTEGER |
| **coupon\_discount**  NUMBER |
| **coupons**  ARRAY This is a nested data structure:   - amount: NUMBER - code: STRING - coupon\_id: INTEGER - discount: NUMBER - id: INTEGER - order\_id: INTEGER - type: STRING |
| **currency\_code**  STRING |
| **currency\_exchange\_rate**  NUMBER |
| **currency\_id**  INTEGER |
| **custom\_status**  STRING |
| **customer\_id**  INTEGER |
| **customer\_message**  STRING |
| **date\_created**  DATE-TIME |
| **date\_modified**  DATE-TIME |
| **date\_shipped**  DATE-TIME |
| **default\_currency\_code**  STRING |
| **default\_currency\_id**  INTEGER |
| **discount\_amount**  STRING |
| **ebay\_order\_id**  STRING |
| **external\_id**  STRING |
| **external\_merchant\_id**  STRING |
| **external\_source**  STRING |
| **form\_fields**  ARRAY This is a nested data structure:   - name: STRING - value: STRING |
| **geoip\_country**  STRING |
| **geoip\_country\_iso2**  STRING |
| **gift\_certificate\_amount**  NUMBER |
| **handling\_cost\_ex\_tax**  NUMBER |
| **handling\_cost\_inc\_tax**  NUMBER |
| **handling\_cost\_tax**  NUMBER |
| **handling\_cost\_tax\_class\_id**  INTEGER |
| **id**  INTEGER |
| **ip\_address**  STRING |
| **is\_deleted**  BOOLEAN |
| **is\_email\_opt\_in**  BOOLEAN |
| **items\_shipped**  INTEGER |
| **items\_total**  INTEGER |
| **order\_is\_digital**  BOOLEAN |
| **order\_source**  STRING |
| **payment\_method**  STRING |
| **payment\_provider\_id**  STRING |
| **payment\_status**  STRING |
| **products**  ARRAY This is a nested data structure:   - applied\_discounts: ARRAY, which is also a nested data structure.   - amount: NUMBER   - code: STRING   - id: STRING   - name: STRING   - type: STRING - base\_cost\_price: NUMBER - base\_price: NUMBER - base\_total: NUMBER - base\_wrapping\_cost: NUMBER - bin\_picking\_number: STRING - cost\_price\_ex\_tax: NUMBER - cost\_price\_inc\_tax: NUMBER - cost\_price\_tax: NUMBER - depth: STRING - ebay\_item\_id: STRING - ebay\_transaction\_id: STRING - event\_date: DATE-TIME - event\_name: STRING - external\_id: INTEGER, STRING - fixed\_shipping\_cost: NUMBER - height: STRING - id: INTEGER - is\_bundled\_product: BOOLEAN - is\_refunded: BOOLEAN - name: STRING - option\_set\_id: INTEGER - order\_address\_id: INTEGER - order\_id: INTEGER - parent\_order\_product\_id: INTEGER - price\_ex\_tax: NUMBER - price\_inc\_tax: NUMBER - price\_tax: NUMBER - product\_id: INTEGER - product\_options: ARRAY, which is also a nested data structure.   - display\_name: STRING   - display\_style: STRING   - display\_value: STRING   - id: INTEGER   - name: STRING   - option\_id: INTEGER   - order\_product\_id: INTEGER   - product\_option\_id: INTEGER   - type: STRING   - value: NUMBER - quantity: INTEGER - quantity\_refunded: INTEGER - quantity\_shipped: INTEGER - refund\_amount: NUMBER - return\_id: INTEGER - sku: STRING - total\_ex\_tax: NUMBER - total\_inc\_tax: NUMBER - total\_tax: NUMBER - type: STRING - weight: NUMBER - width: STRING - wrapping\_cost\_ex\_tax: NUMBER - wrapping\_cost\_inc\_tax: NUMBER - wrapping\_cost\_tax: NUMBER - wrapping\_message: STRING - wrapping\_name: STRING |
| **refunded\_amount**  NUMBER |
| **shipping\_address\_count**  INTEGER |
| **shipping\_addresses**  ARRAY  - base\_cost: NUMBER - base\_handling\_cost: NUMBER - city: STRING - company: STRING - cost\_ex\_tax: NUMBER - cost\_inc\_tax: NUMBER - cost\_tax: NUMBER - cost\_tax\_class\_id: INTEGER - country: STRING - country\_iso2: STRING - email: STRING - first\_name: STRING - form\_fields: ARRAY, which is also a nested data structure.   - name: STRING   - value: STRING - handling\_cost\_ex\_tax: NUMBER - handling\_cost\_inc\_tax: NUMBER - handling\_cost\_tax: NUMBER - handling\_cost\_tax\_class\_id: INTEGER - id: INTEGER - items\_shipped: INTEGER - items\_total: INTEGER - last\_name: STRING - order\_id: INTEGER - phone: STRING - shipping\_method: STRING - shipping\_zone\_id: INTEGER - shipping\_zone\_name: STRING - state: STRING - street\_1: STRING - street\_2: STRING - zip: STRING |
| **shipping\_cost\_ex\_tax**  NUMBER |
| **shipping\_cost\_inc\_tax**  NUMBER |
| **shipping\_cost\_tax**  NUMBER |
| **shipping\_cost\_tax\_class\_id**  INTEGER |
| **staff\_notes**  STRING |
| **status**  STRING |
| **status\_id**  INTEGER |
| **store\_credit\_amount**  NUMBER |
| **subtotal\_ex\_tax**  NUMBER |
| **subtotal\_inc\_tax**  NUMBER |
| **subtotal\_tax**  NUMBER |
| **tax\_provider\_id**  STRING |
| **total\_ex\_tax**  NUMBER |
| **total\_inc\_tax**  NUMBER |
| **total\_tax**  NUMBER |
| **wrapping\_cost\_ex\_tax**  NUMBER |
| **wrapping\_cost\_inc\_tax**  NUMBER |
| **wrapping\_cost\_tax**  NUMBER |
| **wrapping\_cost\_tax\_class\_id**  INTEGER |

### products

The `products` table contains info about the products in your BigCommerce store.

**Note**: During the initial replication job for a BigCommerce integration, all products will be replicated. On subsequent replication jobs, only new and updated product records will be replicated.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | date\_modified |
| **Useful links** | [BigCommerce API method](https://developer.bigcommerce.com/api-reference/catalog/catalog-api/products/getproducts "Opens in new tab: BigCommerce API method") |

products table foreign keys

| Join products with | on |
| --- | --- |
| [orders](#orders) | ``` products.id = orders.products.product_id ```  ``` products.images.product_id = orders.products.product_id ```  ``` products.related_products.items = orders.products.product_id ```  ``` products.variants.product_id = orders.products.product_id ```  ``` products.id = orders.products.parent_order_product_id ```  ``` products.images.product_id = orders.products.parent_order_product_id ```  ``` products.related_products.items = orders.products.parent_order_product_id ```  ``` products.variants.product_id = orders.products.parent_order_product_id ``` |

products table schema

|  |
| --- |
| **availability**  STRING |
| **availability\_description**  STRING |
| **base\_variant\_id**  INTEGER |
| **bin\_picking\_number**  STRING |
| **brand\_id**  INTEGER |
| **brand\_name**  STRING |
| **bulk\_pricing\_rules**  ARRAY This is a nested data structure:   - amount: NUMBER - id: INTEGER - quantity\_max: INTEGER - quantity\_min: INTEGER - type: STRING |
| **calculated\_price**  NUMBER |
| **categories**  ARRAY This is a nested data structure. |
| **condition**  STRING |
| **cost\_price**  NUMBER |
| **custom\_fields**  OBJECT This is a nested data structure:   - id: INTEGER - name: STRING - value: STRING |
| **custom\_url**  OBJECT This is a nested data structure:   - is\_customized: BOOLEAN - url: STRING |
| **date\_created**  DATE-TIME |
| **date\_modified**  DATE-TIME |
| **depth**  NUMBER |
| **description**  STRING |
| **fixed\_cost\_shipping\_price**  NUMBER |
| **gift\_wrapping\_options\_list**  ARRAY This is a nested data structure. |
| **gift\_wrapping\_options\_type**  STRING |
| **gtin**  STRING |
| **height**  NUMBER |
| **id**  INTEGER |
| **images**  ARRAY This is a nested data structure:   - date\_modified: DATE-TIME - description: STRING - id: INTEGER - image\_file: STRING - is\_thumbnail: BOOLEAN - product\_id: INTEGER - sort\_order: INTEGER - url\_standard: STRING - url\_thumbnail: STRING - url\_tiny: STRING - url\_zoom: STRING |
| **inventory\_level**  INTEGER |
| **inventory\_tracking**  STRING |
| **inventory\_warning\_level**  INTEGER |
| **is\_condition\_shown**  BOOLEAN |
| **is\_featured**  BOOLEAN |
| **is\_free\_shipping**  BOOLEAN |
| **is\_preorder\_only**  BOOLEAN |
| **is\_price\_hidden**  BOOLEAN |
| **is\_visible**  BOOLEAN |
| **layout\_file**  STRING |
| **map\_price**  NUMBER |
| **meta\_description**  STRING |
| **meta\_keywords**  STRING |
| **mpn**  STRING |
| **name**  STRING |
| **open\_graph\_description**  STRING |
| **open\_graph\_title**  STRING |
| **open\_graph\_type**  STRING |
| **open\_graph\_use\_image**  BOOLEAN |
| **open\_graph\_use\_meta\_description**  BOOLEAN |
| **open\_graph\_use\_product\_name**  BOOLEAN |
| **option\_set\_display**  STRING |
| **option\_set\_id**  INTEGER |
| **order\_quantity\_maximum**  INTEGER |
| **order\_quantity\_minimum**  INTEGER |
| **page\_title**  STRING |
| **preorder\_message**  STRING |
| **preorder\_release\_date**  STRING |
| **price**  NUMBER |
| **price\_hidden\_label**  STRING |
| **product\_tax\_code**  STRING |
| **related\_products**  ARRAY This is a nested data structure. |
| **retail\_price**  NUMBER |
| **reviews\_count**  INTEGER |
| **reviews\_rating\_sum**  INTEGER |
| **sale\_price**  NUMBER |
| **search\_keywords**  STRING |
| **sku**  STRING |
| **sort\_order**  INTEGER |
| **tax\_class\_id**  INTEGER |
| **total\_sold**  INTEGER |
| **type**  STRING |
| **upc**  STRING |
| **variants**  ARRAY This is a nested data structure:   - bin\_picking\_number: STRING - calculated\_price: NUMBER - cost\_price: NUMBER - depth: NUMBER - fixed\_cost\_shipping\_price: NUMBER - height: NUMBER - id: INTEGER - image\_url: STRING - inventory\_level: INTEGER - inventory\_warning\_level: INTEGER - is\_free\_shipping: BOOLEAN - map\_price: NUMBER - option\_values: ARRAY, which is also a nested data structure.   - id: INTEGER   - label: STRING   - option\_display\_name: STRING   - option\_id: INTEGER - price: NUMBER - product\_id: INTEGER - purchasing\_disabled: BOOLEAN - purchasing\_disabled\_message: STRING - sale\_price: NUMBER - sku: STRING - sku\_id: INTEGER - upc: STRING - weight: NUMBER - width: NUMBER |
| **videos**  ARRAY  - description: STRING - id: INTEGER - length: STRING - product\_id: INTEGER - sort\_order: INTEGER - title: STRING - type: STRING - video\_id: STRING |
| **view\_count**  INTEGER |
| **warranty**  STRING |
| **weight**  NUMBER |
| **width**  NUMBER |
