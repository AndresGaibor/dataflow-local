---
title: "Yotpo"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Yotpo.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Yotpo

Yotpo is a cloud-based content marketing platform for e-commerce businesses. It lets users collect user-generated content and use the content to build a brand and manage the customer experience.

For more information about the API, see [Yotpo Core API](https://apidocs.yotpo.com/reference).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To obtain the API key and secret:

1. Make sure you are an Yotpo account administrator. The API secret is only visible to this role.
2. Log into your [Yotpo account](https://yap.yotpo.com/#/login).
3. Click the Profile icon in the top-right corner.
4. Go to Account Settings > General Settings.
5. Locate the API Credentials section:

   ![The API Credentials section in Yotpo, highlighted](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/yotpo-api-credentials.png)

   The App Key field contains your API Key, and the Secret Key is your API Secret.
6. Copy and paste these values into the corresponding fields.

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

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### collections

The `collections` table contains data about your store’s product groupings - collections - in your Yotpo account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | yotpo\_id |
| **Replication Key** | updated\_at |
| **Useful links** | [Yotpo documentation](https://core-api.yotpo.com/reference/collections)  [Yotpo API method](https://core-api.yotpo.com/reference/retrieve-collections "Opens in new tab: Yotpo API method") |

collections table schema

|  |
| --- |
| **created\_at**  DATE-TIME |
| **external\_id**  STRING |
| **name**  STRING |
| **updated\_at**  DATE-TIME |
| **yotpo\_id**  INTEGER |

### emails

The `emails` table contains data about every email sent from Yotpo.

#### Attribution window

When data is replicated for this table, it will use an attribution window of 30 days to fetch updated email statistics such as opens, clicks, etc. This means that every time a replication job runs, the last 30 days’ worth of data will be replicated for this table.

Refer to the [Replication](#replication) section for more info and examples of how the attribution window is used to query for data.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | email\_address  email\_sent\_timestamp |
| **Replication Key** | email\_sent\_timestamp |
| **Useful links** | [Yotpo documentation](https://apidocs.yotpo.com/v1.0/reference#email-analytics-intro)  [Yotpo API method](https://apidocs.yotpo.com/v1.0/reference#raw-data "Opens in new tab: Yotpo API method") |

emails table foreign keys

| Join emails with | on |
| --- | --- |
| [unsubscribers](#unsubscribers) | ``` emails.email_address = unsubscribers.user_email ``` |

emails table schema

|  |
| --- |
| **arrived\_early\_timestamp**  DATE-TIME |
| **clicked\_through\_timestamp**  DATE-TIME |
| **content\_creation\_timestamp**  DATE-TIME |
| **coupon\_code**  STRING |
| **email\_address**  STRING |
| **email\_sent\_timestamp**  DATE-TIME |
| **email\_type**  STRING |
| **failed\_timestamp**  DATE-TIME |
| **invalid\_address\_timestamp**  DATE-TIME |
| **marked\_spam\_timestamp**  DATE-TIME |
| **opened\_timestamp**  DATE-TIME |
| **order\_id**  STRING |
| **order\_timestamp**  DATE-TIME |
| **platform**  STRING |
| **product\_id**  STRING |
| **reminder\_num**  NUMBER |
| **review\_form**  STRING |
| **review\_type**  STRING |
| **sku**  STRING |
| **trr\_bundle\_id**  STRING |
| **trr\_bundle\_subject**  STRING |
| **unsubscribed\_timestamp**  DATE-TIME |

### order\_fulfillments

The `order_fulfillments` table contains data about fulfilled store orders in your Yotpo account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Yotpo documentation](https://core-api.yotpo.com/reference/order-fulfillments)  [Yotpo API method](https://core-api.yotpo.com/reference/retrieve-order-fulfillments "Opens in new tab: Yotpo API method") |

order\_fulfillments table schema

|  |
| --- |
| **created\_at**  DATE-TIME |
| **external\_id**  STRING |
| **fulfilled\_items**  ARRAY This is a nested data structure:   - **external\_product\_id**: STRING - **quantity**: INTEGER - **yotpo\_product\_id**: INTEGER |
| **fulfillment\_date**  DATE-TIME |
| **id**  INTEGER |
| **order\_id**  STRING |
| **shipment\_info**  OBJECT This is a nested data structure:   - **shipment\_status**: STRING - **tracking\_company**: STRING - **tracking\_number**: STRING - **tracking\_url**: STRING |
| **status**  STRING |
| **updated\_at**  DATE-TIME |

### orders

The `orders` table contains data about orders in your Yotpo account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | yotpo\_id |
| **Replication Key** | order\_date |
| **Useful links** | [Yotpo documentation](https://core-api.yotpo.com/reference/orders)  [Yotpo API method](https://core-api.yotpo.com/reference/retrieve-orders "Opens in new tab: Yotpo API method") |

orders table schema

|  |
| --- |
| **billing\_address**  OBJECT This is a nested data structure:   - **address1**: STRING - **address2**: STRING - **city**: STRING - **company**: STRING - **country\_code**: STRING - **phone\_number**: STRING - **province\_code**: STRING - **state**: STRING - **zip**: STRING |
| **cancellation**  OBJECT This is a nested data structure: **cancellation\_date**, DATE-TIME |
| **checkout\_token**  STRING |
| **created\_at**  DATE-TIME |
| **currency**  STRING |
| **custom\_properties**  OBJECT |
| **customer**  OBJECT This is a nested data structure:   - **accepts\_email\_marketing**: STRING - **accepts\_sms\_marketing**: STRING - **custom\_properties**: OBJECT - **email**: STRING - **external\_id**: STRING - **first\_name**: STRING - **last\_name**: STRING - **phone\_number**: STRING |
| **external\_id**  STRING |
| **fulfillments**  ARRAY This is a nested data structure:   - **external\_id**: STRING - **fulfilled\_items**: ARRAY, which is also a nested data structure.   - **external\_product\_id**: STRING   - **quantity**: INTEGER - **fulfillment\_date**: DATE-TIME - **shipment\_info**: OBJECT, which is also a nested data structure.   - **shipment\_status**: STRING   - **tracking\_company**: STRING   - **tracking\_number**: STRING   - **tracking\_url**: STRING |
| **landing\_site\_url**  STRING |
| **line\_items**  ARRAY This is a nested data structure:   - **coupon\_code**: STRING - **created\_at**: DATE-TIME - **custom\_properties**: OBJECT, which is also a nested data structure.   - **external\_product\_id**: STRING   - **product\_id**: STRING   - **quantity**: INTEGER   - **subtotal\_price**: NUMBER   - **total\_price**: NUMBER   - **updated\_at**: DATE-TIME   - **yotpo\_id**: INTEGER |
| **order\_date**  DATE-TIME |
| **order\_name**  STRING |
| **payment\_method**  STRING |
| **payment\_status**  STRING |
| **shipping\_address**  OBJECT This is a nested data structure:   - **address1**: STRING - **address2**: STRING - **city**: STRING - **company**: STRING - **country\_code**: STRING - **phone\_number**: STRING - **province\_code**: STRING - **state**: STRING - **zip**: STRING |
| **source**  STRING |
| **subtotal\_price**  NUMBER |
| **total\_price**  NUMBER |
| **updated\_at**  DATE-TIME |
| **yotpo\_id**  INTEGER |

### product\_reviews

The `product_reviews` table contains data about reviews for a certain product.

**Note**: This table is similar to the `reviews` table, but also contains custom fields. If you don’t have or need custom product fields, you may only want to replicate the `reviews` table to prevent redundant data.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | created\_at |
| **Useful links** | [Yotpo documentation](https://apidocs.yotpo.com/reference/about-storefront-reviews)  [Yotpo API method](https://apidocs.yotpo.com/reference/retrieve-reviews-for-a-product "Opens in new tab: Yotpo API method") |

product\_reviews table foreign keys

| Join product\_reviews with | on |
| --- | --- |
| [products](#products) | ``` product_reviews.product_id = products.yotpo_id ``` |
| [reviews](#reviews) | ``` product_reviews.source_review_id = reviews.id ``` |

product\_reviews table schema

|  |
| --- |
| **comment**  OBJECT This is a nested data structure:   - **comments\_avatar**: STRING - **content**: STRING - **created\_at**: DATE-TIME - **display\_name**: STRING - **id**: INTEGER |
| **content**  STRING |
| **created\_at**  DATE-TIME |
| **custom\_fields**  OBJECT |
| **deleted**  BOOLEAN |
| **domain\_key**  STRING |
| **id**  INTEGER |
| **images\_data**  ARRAY This is a nested data structure:   - **id**: INTEGER - **original\_url**: STRING - **thumb\_url**: STRING |
| **name**  STRING |
| **product\_id**  INTEGER |
| **product\_yotpo\_id**  STRING |
| **score**  NUMBER |
| **sentiment**  NUMBER |
| **source\_review\_id**  NUMBER |
| **title**  STRING |
| **user**  OBJECT This is a nested data structure:   - **display\_name**: STRING - **is\_social\_connected**: NUMBER - **social\_image**: STRING - **user\_id**: INTEGER - **user\_type**: STRING |
| **verified\_buyer**  BOOLEAN |
| **votes\_down**  INTEGER |
| **votes\_up**  INTEGER |

### product\_variants

The `product_variants` table contains data about product variations in your Yotpo account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | yotpo\_id |
| **Replication Key** | updated\_at |
| **Useful links** | [Yotpo documentation](https://core-api.yotpo.com/reference/product-variants)  [Yotpo API method](https://core-api.yotpo.com/reference/retrieve-product-variants "Opens in new tab: Yotpo API method") |

product\_variants table schema

|  |
| --- |
| **compare\_at\_price**  NUMBER |
| **created\_at**  DATE-TIME |
| **currency**  STRING |
| **description**  STRING |
| **external\_id**  STRING |
| **gtins**  ARRAY This is a nested data structure:   - **declared\_type**: STRING - **value**: STRING |
| **image\_url**  STRING |
| **inventory\_quantity**  INTEGER |
| **is\_discontinued**  BOOLEAN |
| **is\_valid\_url\_format**  BOOLEAN |
| **name**  STRING |
| **options**  ARRAY This is a nested data structure:   - **name**: STRING - **value**: STRING |
| **price**  NUMBER |
| **sku**  STRING |
| **updated\_at**  DATE-TIME |
| **url**  STRING |
| **yotpo\_id**  INTEGER |
| **yotpo\_product\_id**  INTEGER |

### products

The `products` table contains data about products in your Yotpo account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | yotpo\_id |
| **Useful links** | [Yotpo documentation](https://apidocs.yotpo.com/reference#introduction-to-products)  [Yotpo API method](https://apidocs.yotpo.com/reference#retrieve-all-products "Opens in new tab: Yotpo API method") |

products table foreign keys

| Join products with | on |
| --- | --- |
| [product\_reviews](#product-reviews) | ``` products.yotpo_id = product_reviews.product_id ``` |

products table schema

|  |
| --- |
| **brand**  STRING |
| **compare\_at\_price**  NUMBER |
| **created\_at**  DATE-TIME |
| **currency**  STRING |
| **custom\_properties**  OBJECT |
| **description**  STRING |
| **external\_created\_at**  DATE-TIME |
| **external\_id**  STRING |
| **external\_updated\_at**  DATE-TIME |
| **group\_name**  STRING |
| **gtins**  ARRAY This is a nested data structure:   - **declared\_type**: STRING - **detected\_type**: STRING - **value**: STRING |
| **handle**  STRING |
| **image\_url**  STRING |
| **inventory\_quantity**  INTEGER |
| **is\_discontinued**  BOOLEAN |
| **is\_valid\_url\_format**  BOOLEAN |
| **mpn**  STRING |
| **name**  STRING |
| **price**  NUMBER |
| **sku**  STRING |
| **status**  STRING |
| **updated\_at**  DATE-TIME |
| **url**  STRING |
| **yotpo\_id**  INTEGER |

### reviews

The `reviews` table contains data about reviews.

**Note**: This table is similar to the `product_reviews` table, but doesn’t contain custom fields. If you have or need custom fields, you may want to only replicate the `product_reviews` table to prevent redundant data.

#### Attribution window

When data is replicated for this table, it will use an attribution window of 30 days to fetch updated (or deleted) reviews. This means that every time a replication job runs, the last 30 days’ worth of data will be replicated for this table.

Refer to the [Replication](#replication) section for more info and examples of how the attribution window is used to query for data.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Yotpo documentation](https://apidocs.yotpo.com/reference#section-what-are-reviews)  [Yotpo API method](https://apidocs.yotpo.com/reference#retrieve-all-reviews "Opens in new tab: Yotpo API method") |

reviews table foreign keys

| Join reviews with | on |
| --- | --- |
| [product\_reviews](#product-reviews) | ``` reviews.id = product_reviews.source_review_id ``` |

reviews table schema

|  |
| --- |
| **archived**  BOOLEAN |
| **content**  STRING |
| **created\_at**  DATE-TIME |
| **deleted**  BOOLEAN |
| **email**  STRING |
| **escalated**  BOOLEAN |
| **id**  INTEGER |
| **name**  STRING |
| **reviewer\_type**  STRING |
| **score**  NUMBER |
| **sentiment**  NUMBER |
| **sku**  STRING |
| **title**  STRING |
| **updated\_at**  DATE-TIME |
| **user\_reference**  STRING |
| **votes\_down**  NUMBER |
| **votes\_up**  NUMBER |

### unsubscribers

The `unsubscribers` table contains data about customers who unsubscribed from one of Yotpo’s emails.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Yotpo documentation](https://apidocs.yotpo.com/reference#introduction-to-unsubscribers)  [Yotpo API method](https://apidocs.yotpo.com/reference#retrieve-a-list-of-unsubscribers "Opens in new tab: Yotpo API method") |

unsubscribers table foreign keys

| Join unsubscribers with | on |
| --- | --- |
| [emails](#emails) | ``` unsubscribers.user_email = emails.email_address ``` |

unsubscribers table schema

|  |
| --- |
| **email\_type\_id**  NUMBER |
| **id**  INTEGER |
| **unsubscirbed\_by\_name**  STRING |
| **user\_email**  STRING |
