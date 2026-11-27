---
title: "Chargebee"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Chargebee.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Chargebee

Chargebee is a recurring billing and subscription management tool.

Chargebee integration replicates data using the [Chargebee v2 API](https://apidocs.chargebee.com/docs/api).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To generate your API key:

1. Log into your [Chargebee account](https://app.chargebee.com/login).
2. Click Settings > Configure Chargebee > API Keys and Webhooks.
3. On the API Keys page, click + Add API Key. The Create an API Key modal is displayed.
4. Select Read-Only Key as the API key type.
5. Select All to define the API key’s access. This grants read-only access to your Chargebee site.
6. In the Name the API key field, enter QTC.
7. Click Create Key. Chargebee creates the API key and redirects you back to the API Keys page.
8. Copy and paste your API key into a secured file.

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
| Include Deleted | Select the check box to include deleted data. |
| Subdomain | The subdomain for your Chargebee account.  Example: my-chargebee-site.chargebee.com, enter my-chargebee-site. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### addons

The `addons` table contains info about the addons in your Chargebee account. Addons are additional charges applied to subscriptions apart from base charges.

**Note**: This table is available Refer to the [Table and field availability and Chargebee Product Catalogs section](#product-catalog-versions) for more info.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Chargebee API method](https://apidocs.chargebee.com/Content/api/addons?prod_cat_ver=1#list_addons "Opens in new tab: Chargebee API method") |

addons table foreign keys

| Join addons with | on |
| --- | --- |
| [coupons](#coupons) | ``` addons.id = coupons.addon_ids ``` |
| [events](#events) | ``` addons.id = events.content.subscription.addons.id ```  ``` addons.id = events.content.subscription.charged_event_based_addons.id ```  ``` addons.id = events.content.subscription.event_based_addons.id ``` |
| [invoices](#invoices) | ``` addons.id = invoices.notes.entity_id ``` |
| [plans](#plans) | ``` addons.id = plans.applicable_addons.id ``` |
| [subscriptions](#subscriptions) | ``` addons.id = subscriptions.addons.id ```  ``` addons.id = subscriptions.charged_event_based_addons.id ```  ``` addons.id = subscriptions.event_based_addons.id ``` |

addons table schema

|  |
| --- |
| **accounting\_category1**  STRING |
| **accounting\_category2**  STRING |
| **accounting\_category3**  STRING |
| **accounting\_category4**  STRING |
| **accounting\_code**  STRING |
| **archived\_at**  DATE-TIME |
| **avalara\_sale\_type**  STRING |
| **avalara\_service\_type**  INTEGER |
| **avalara\_transaction\_type**  INTEGER |
| **channel**  STRING |
| **charge\_type**  STRING |
| **currency\_code**  STRING |
| **custom\_fields**  STRING |
| **description**  STRING |
| **enabled\_in\_portal**  BOOLEAN |
| **id**  STRING |
| **included\_in\_mrr**  BOOLEAN |
| **invoice\_name**  STRING |
| **invoice\_notes**  STRING |
| **is\_shippable**  BOOLEAN |
| **meta\_data**  STRING |
| **name**  STRING |
| **object**  STRING |
| **period**  INTEGER |
| **period\_unit**  STRING |
| **price**  INTEGER |
| **price\_in\_decimal**  STRING |
| **pricing\_model**  STRING |
| **resource\_version**  INTEGER |
| **shipping\_frequency\_period**  INTEGER |
| **shipping\_frequency\_period\_unit**  STRING |
| **show\_description\_in\_invoices**  BOOLEAN |
| **show\_description\_in\_quotes**  BOOLEAN |
| **sku**  STRING |
| **status**  STRING |
| **tax\_code**  STRING |
| **tax\_profile\_id**  STRING |
| **taxable**  BOOLEAN |
| **taxjar\_product\_code**  STRING |
| **tiers**  ARRAY This is a nested data structure:   - ending\_unit: INTEGER - ending\_unit\_in\_decimal: STRING - object: STRING - price: INTEGER - price\_in\_decimal: STRING - starting\_unit: INTEGER - starting\_unit\_in\_decimal: STRING |
| **type**  STRING |
| **unit**  STRING |
| **updated\_at**  DATE-TIME |

### comments

The `comments` table contains info about comments in your Chargebee account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | created\_at |
| **Useful links** | [Chargebee documentation](https://apidocs.chargebee.com/Content/api/comments)  [Chargebee API method](https://apidocs.chargebee.com/Content/api/comments#list_comments "Opens in new tab: Chargebee API method") |

comments table schema

|  |
| --- |
| **added\_by**  STRING |
| **created\_at**  DATE-TIME |
| **entity\_id**  STRING |
| **entity\_type**  STRING |
| **id**  STRING |
| **notes**  STRING |
| **object**  STRING |
| **type**  STRING |

### coupons

The `coupons` table contains info about the coupons in your Chargebee account.

**Note**: This table is available Refer to the [Table and field availability and Chargebee Product Catalogs section](#product-catalog-versions) for more info.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Chargebee API method](https://apidocs.chargebee.com/Content/api/coupons#list_coupons "Opens in new tab: Chargebee API method") |

coupons table foreign keys

| Join coupons with | on |
| --- | --- |
| [addons](#addons) | ``` coupons.addon_ids = addons.id ``` |
| [events](#events) | ``` coupons.addon_ids = events.content.subscription.addons.id ```  ``` coupons.addon_ids = events.content.subscription.charged_event_based_addons.id ```  ``` coupons.addon_ids = events.content.subscription.event_based_addons.id ```  ``` coupons.id = events.content.coupon.id ```  ``` coupons.id = events.content.invoice.discounts.entity_id ```  ``` coupons.id = events.content.invoice.line_item_discounts.coupon_id ```  ``` coupons.id = events.content.subscription.coupons.coupon_id ```  ``` coupons.plan_ids = events.content.coupon.plan_ids ```  ``` coupons.plan_ids = events.content.subscription.plan_id ``` |
| [invoices](#invoices) | ``` coupons.addon_ids = invoices.notes.entity_id ```  ``` coupons.id = invoices.discounts.entity_id ```  ``` coupons.id = invoices.line_item_discounts.coupon_id ```  ``` coupons.id = invoices.notes.entity_id ```  ``` coupons.plan_ids = invoices.notes.entity_id ``` |
| [plans](#plans) | ``` coupons.addon_ids = plans.applicable_addons.id ```  ``` coupons.plan_ids = plans.id ``` |
| [subscriptions](#subscriptions) | ``` coupons.addon_ids = subscriptions.addons.id ```  ``` coupons.addon_ids = subscriptions.charged_event_based_addons.id ```  ``` coupons.addon_ids = subscriptions.event_based_addons.id ```  ``` coupons.id = subscriptions.coupons.coupon_id ```  ``` coupons.plan_ids = subscriptions.plan_id ``` |
| [credit\_notes](#credit-notes) | ``` coupons.id = credit_notes.discounts.entity_id ```  ``` coupons.id = credit_notes.line_item_discounts.coupon_id ``` |
| [orders](#orders) | ``` coupons.id = orders.line_item_discounts.coupon_id ``` |

coupons table schema

|  |
| --- |
| **apply\_discount\_on**  STRING |
| **apply\_on**  STRING |
| **archived\_at**  DATE-TIME |
| **created\_at**  DATE-TIME |
| **currency\_code**  STRING |
| **discount\_amount**  NUMBER |
| **discount\_percentage**  NUMBER |
| **discount\_type**  STRING |
| **duration\_month**  INTEGER |
| **duration\_type**  STRING |
| **id**  STRING |
| **invoice\_name**  STRING |
| **invoice\_notes**  STRING |
| **item\_constraint\_criteria**  ARRAY This is a nested data structure:   - currencies: ARRAY, which is also a nested data structure. - item\_family\_ids: ARRAY, which is also a nested data structure. - item\_price\_periods: ARRAY, which is also a nested data structure. - item\_type: STRING |
| **item\_constraints**  ARRAY This is a nested data structure:   - constraint: STRING - item\_price\_ids: ARRAY, which is also a nested data structure. - item\_type: STRING |
| **max\_redemptions**  INTEGER |
| **meta\_data**  STRING |
| **name**  STRING |
| **object**  STRING |
| **period**  INTEGER |
| **period\_unit**  STRING |
| **redemptions**  INTEGER |
| **resource\_version**  INTEGER |
| **status**  STRING |
| **updated\_at**  DATE-TIME |
| **valid\_till**  DATE-TIME |

### credit\_notes

The `credit_notes` table contains info about the credit notes in your Chargebee account. A credit note is a document that specifies the money owed by a business to a customer.

**Note**: This table is available Refer to the [Table and field availability and Chargebee Product Catalogs section](#product-catalog-versions) for more info.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Chargebee documentation](https://apidocs.chargebee.com/Content/api/credit_notes)  [Chargebee API method](https://apidocs.chargebee.com/Content/api/credit_notes#list_credit_notes "Opens in new tab: Chargebee API method") |

credit\_notes table foreign keys

| Join credit\_notes with | on |
| --- | --- |
| [coupons](#coupons) | ``` credit_notes.discounts.entity_id = coupons.id ```  ``` credit_notes.line_item_discounts.coupon_id = coupons.id ``` |
| [events](#events) | ``` credit_notes.discounts.entity_id = events.content.coupon.id ```  ``` credit_notes.line_item_discounts.coupon_id = events.content.coupon.id ```  ``` credit_notes.discounts.entity_id = events.content.invoice.discounts.entity_id ```  ``` credit_notes.line_item_discounts.coupon_id = events.content.invoice.discounts.entity_id ```  ``` credit_notes.discounts.entity_id = events.content.invoice.line_item_discounts.coupon_id ```  ``` credit_notes.line_item_discounts.coupon_id = events.content.invoice.line_item_discounts.coupon_id ```  ``` credit_notes.discounts.entity_id = events.content.subscription.coupons.coupon_id ```  ``` credit_notes.line_item_discounts.coupon_id = events.content.subscription.coupons.coupon_id ```  ``` credit_notes.id = events.content.invoice.adjustment_credit_notes.cn_id ```  ``` credit_notes.id = events.content.invoice.applied_credits.cn_id ```  ``` credit_notes.id = events.content.invoice.issued_credit_notes.cn_id ```  ``` credit_notes.customer_id = events.content.customer.id ```  ``` credit_notes.customer_id = events.content.invoice.customer_id ```  ``` credit_notes.customer_id = events.content.subscription.customer_id ```  ``` credit_notes.customer_id = events.content.transaction.customer_id ```  ``` credit_notes.allocations.invoice_id = events.content.invoice.id ```  ``` credit_notes.reference_invoice_id = events.content.invoice.id ```  ``` credit_notes.allocations.invoice_id = events.content.transaction.linked_credit_notes.cn_reference_invoice_id ```  ``` credit_notes.reference_invoice_id = events.content.transaction.linked_credit_notes.cn_reference_invoice_id ```  ``` credit_notes.line_item_discounts.line_item_id = events.content.invoice.line_item_discounts.line_item_id ```  ``` credit_notes.line_item_taxes.line_item_id = events.content.invoice.line_item_discounts.line_item_id ```  ``` credit_notes.line_item_tiers.line_item_id = events.content.invoice.line_item_discounts.line_item_id ```  ``` credit_notes.line_items.id = events.content.invoice.line_item_discounts.line_item_id ```  ``` credit_notes.line_item_discounts.line_item_id = events.content.invoice.line_item_taxes.line_item_id ```  ``` credit_notes.line_item_taxes.line_item_id = events.content.invoice.line_item_taxes.line_item_id ```  ``` credit_notes.line_item_tiers.line_item_id = events.content.invoice.line_item_taxes.line_item_id ```  ``` credit_notes.line_items.id = events.content.invoice.line_item_taxes.line_item_id ```  ``` credit_notes.line_item_discounts.line_item_id = events.content.invoice.line_items.id ```  ``` credit_notes.line_item_taxes.line_item_id = events.content.invoice.line_items.id ```  ``` credit_notes.line_item_tiers.line_item_id = events.content.invoice.line_items.id ```  ``` credit_notes.line_items.id = events.content.invoice.line_items.id ```  ``` credit_notes.subscription_id = events.content.subscription.id ```  ``` credit_notes.line_items.subscription_id = events.content.subscription.id ```  ``` credit_notes.subscription_id = events.content.invoice.subscription_id ```  ``` credit_notes.line_items.subscription_id = events.content.invoice.subscription_id ```  ``` credit_notes.subscription_id = events.content.transaction.subscription_id ```  ``` credit_notes.line_items.subscription_id = events.content.transaction.subscription_id ```  ``` credit_notes.linked_refunds.txn_id = events.content.invoice.linked_payments.txn_id ```  ``` credit_notes.linked_refunds.txn_id = events.content.transaction.id ```  ``` credit_notes.linked_refunds.txn_id = events.content.transaction.linked_refunds.txn_id ```  ``` credit_notes.linked_refunds.txn_id = events.content.transaction.reference_transaction_id ```  ``` credit_notes.linked_refunds.txn_id = events.content.transaction.refunded_txn_id ``` |
| [invoices](#invoices) | ``` credit_notes.discounts.entity_id = invoices.discounts.entity_id ```  ``` credit_notes.line_item_discounts.coupon_id = invoices.discounts.entity_id ```  ``` credit_notes.discounts.entity_id = invoices.line_item_discounts.coupon_id ```  ``` credit_notes.line_item_discounts.coupon_id = invoices.line_item_discounts.coupon_id ```  ``` credit_notes.discounts.entity_id = invoices.notes.entity_id ```  ``` credit_notes.line_item_discounts.coupon_id = invoices.notes.entity_id ```  ``` credit_notes.id = invoices.adjustment_credit_notes.cn_id ```  ``` credit_notes.id = invoices.applied_credits.cn_id ```  ``` credit_notes.id = invoices.issued_credit_notes.cn_id ```  ``` credit_notes.customer_id = invoices.customer_id ```  ``` credit_notes.customer_id = invoices.notes.entity_id ```  ``` credit_notes.allocations.invoice_id = invoices.id ```  ``` credit_notes.reference_invoice_id = invoices.id ```  ``` credit_notes.line_item_discounts.line_item_id = invoices.line_item_discounts.line_item_id ```  ``` credit_notes.line_item_taxes.line_item_id = invoices.line_item_discounts.line_item_id ```  ``` credit_notes.line_item_tiers.line_item_id = invoices.line_item_discounts.line_item_id ```  ``` credit_notes.line_items.id = invoices.line_item_discounts.line_item_id ```  ``` credit_notes.line_item_discounts.line_item_id = invoices.line_item_taxes.line_item_id ```  ``` credit_notes.line_item_taxes.line_item_id = invoices.line_item_taxes.line_item_id ```  ``` credit_notes.line_item_tiers.line_item_id = invoices.line_item_taxes.line_item_id ```  ``` credit_notes.line_items.id = invoices.line_item_taxes.line_item_id ```  ``` credit_notes.line_item_discounts.line_item_id = invoices.line_item_tiers.line_item_id ```  ``` credit_notes.line_item_taxes.line_item_id = invoices.line_item_tiers.line_item_id ```  ``` credit_notes.line_item_tiers.line_item_id = invoices.line_item_tiers.line_item_id ```  ``` credit_notes.line_items.id = invoices.line_item_tiers.line_item_id ```  ``` credit_notes.line_item_discounts.line_item_id = invoices.line_items.id ```  ``` credit_notes.line_item_taxes.line_item_id = invoices.line_items.id ```  ``` credit_notes.line_item_tiers.line_item_id = invoices.line_items.id ```  ``` credit_notes.line_items.id = invoices.line_items.id ```  ``` credit_notes.subscription_id = invoices.line_items.subscription_id ```  ``` credit_notes.line_items.subscription_id = invoices.line_items.subscription_id ```  ``` credit_notes.subscription_id = invoices.notes.entity_id ```  ``` credit_notes.line_items.subscription_id = invoices.notes.entity_id ```  ``` credit_notes.subscription_id = invoices.subscription_id ```  ``` credit_notes.line_items.subscription_id = invoices.subscription_id ```  ``` credit_notes.linked_refunds.txn_id = invoices.linked_payments.txn_id ``` |
| [subscriptions](#subscriptions) | ``` credit_notes.discounts.entity_id = subscriptions.coupons.coupon_id ```  ``` credit_notes.line_item_discounts.coupon_id = subscriptions.coupons.coupon_id ```  ``` credit_notes.customer_id = subscriptions.customer_id ```  ``` credit_notes.subscription_id = subscriptions.id ```  ``` credit_notes.line_items.subscription_id = subscriptions.id ``` |
| [orders](#orders) | ``` credit_notes.discounts.entity_id = orders.line_item_discounts.coupon_id ```  ``` credit_notes.line_item_discounts.coupon_id = orders.line_item_discounts.coupon_id ```  ``` credit_notes.id = orders.linked_credit_notes.id ```  ``` credit_notes.customer_id = orders.customer_id ```  ``` credit_notes.allocations.invoice_id = orders.invoice_id ```  ``` credit_notes.reference_invoice_id = orders.invoice_id ```  ``` credit_notes.line_item_discounts.line_item_id = orders.line_item_discounts.line_item_id ```  ``` credit_notes.line_item_taxes.line_item_id = orders.line_item_discounts.line_item_id ```  ``` credit_notes.line_item_tiers.line_item_id = orders.line_item_discounts.line_item_id ```  ``` credit_notes.line_items.id = orders.line_item_discounts.line_item_id ```  ``` credit_notes.line_item_discounts.line_item_id = orders.line_item_taxes.line_item_id ```  ``` credit_notes.line_item_taxes.line_item_id = orders.line_item_taxes.line_item_id ```  ``` credit_notes.line_item_tiers.line_item_id = orders.line_item_taxes.line_item_id ```  ``` credit_notes.line_items.id = orders.line_item_taxes.line_item_id ```  ``` credit_notes.subscription_id = orders.subscription_id ```  ``` credit_notes.line_items.subscription_id = orders.subscription_id ``` |
| [customers](#customers) | ``` credit_notes.customer_id = customers.id ``` |
| [payment\_sources](#payment-sources) | ``` credit_notes.customer_id = payment_sources.customer_id ``` |
| [promotional\_credits](#promotional-credits) | ``` credit_notes.customer_id = promotional_credits.customer_id ``` |
| [transactions](#transactions) | ``` credit_notes.customer_id = transactions.customer_id ```  ``` credit_notes.allocations.invoice_id = transactions.linked_credit_notes.cn_reference_invoice_id ```  ``` credit_notes.reference_invoice_id = transactions.linked_credit_notes.cn_reference_invoice_id ```  ``` credit_notes.subscription_id = transactions.subscription_id ```  ``` credit_notes.line_items.subscription_id = transactions.subscription_id ```  ``` credit_notes.linked_refunds.txn_id = transactions.id ```  ``` credit_notes.linked_refunds.txn_id = transactions.linked_refunds.txn_id ```  ``` credit_notes.linked_refunds.txn_id = transactions.reference_transaction_id ```  ``` credit_notes.linked_refunds.txn_id = transactions.refunded_txn_id ``` |
| [virtual\_bank\_accounts](#virtual-bank-accounts) | ``` credit_notes.customer_id = virtual_bank_accounts.customer_id ``` |
| [gifts](#gifts) | ``` credit_notes.customer_id = gifts.gift_receiver.customer_id ```  ``` credit_notes.customer_id = gifts.gifter.customer_id ```  ``` credit_notes.allocations.invoice_id = gifts.gifter.invoice_id ```  ``` credit_notes.reference_invoice_id = gifts.gifter.invoice_id ```  ``` credit_notes.subscription_id = gifts.gift_receiver.subscription_id ```  ``` credit_notes.line_items.subscription_id = gifts.gift_receiver.subscription_id ``` |

credit\_notes table schema

|  |
| --- |
| **allocations**  ARRAY This is a nested data structure:   - allocated\_amount: INTEGER - allocated\_at: DATE-TIME - invoice\_date: DATE-TIME - invoice\_id: STRING - invoice\_status: STRING |
| **amount\_allocated**  INTEGER |
| **amount\_available**  INTEGER |
| **amount\_refunded**  INTEGER |
| **base\_currency\_code**  STRING |
| **channel**  STRING |
| **create\_reason\_code**  STRING |
| **currency\_code**  STRING |
| **customer\_id**  STRING |
| **date**  DATE-TIME |
| **deleted**  BOOLEAN |
| **discounts**  ARRAY This is a nested data structure:   - amount: INTEGER - description: STRING - entity\_id: STRING - entity\_type: STRING - object: STRING |
| **einvoice**  OBJECT This is a nested data structure:   - id: STRING - message: STRING - status: STRING |
| **exchange\_rate**  NUMBER |
| **fractional\_correction**  INTEGER |
| **generated\_at**  DATE-TIME |
| **id**  STRING |
| **line\_item\_discounts**  ARRAY This is a nested data structure:   - coupon\_id: STRING - discount\_amount: INTEGER - discount\_type: STRING - entity\_id: STRING - line\_item\_id: STRING - object: STRING |
| **line\_item\_taxes**  ARRAY This is a nested data structure:   - is\_non\_compliance\_tax: BOOLEAN - is\_partial\_tax\_applied: BOOLEAN - line\_item\_id: STRING - local\_currency\_code: STRING - tax\_amount: INTEGER - tax\_amount\_in\_local\_currency: INTEGER - tax\_juris\_code: STRING - tax\_juris\_name: STRING - tax\_juris\_type: STRING - tax\_name: STRING - tax\_rate: NUMBER - taxable\_amount: INTEGER |
| **line\_item\_tiers**  ARRAY This is a nested data structure:   - ending\_unit: INTEGER - ending\_unit\_in\_decimal: STRING - line\_item\_id: STRING - quantity\_used: INTEGER - quantity\_used\_in\_decimal: STRING - starting\_unit: INTEGER - starting\_unit\_in\_decimal: STRING - unit\_amount: INTEGER - unit\_amount\_in\_decimal: STRING |
| **line\_items**  ARRAY This is a nested data structure:   - amount: INTEGER - amount\_in\_decimal: STRING - customer\_id: STRING - date\_from: DATE-TIME - date\_to: DATE-TIME - description: STRING - discount\_amount: INTEGER - entity\_description: STRING - entity\_id: STRING - entity\_type: STRING - id: STRING - is\_taxed: BOOLEAN - item\_level\_discount\_amount: INTEGER - object: STRING - pricing\_model: STRING - quantity: INTEGER - quantity\_in\_decimal: STRING - subscription\_id: STRING - tax\_amount: INTEGER - tax\_exempt\_reason: STRING - tax\_rate: NUMBER - unit\_amount: INTEGER - unit\_amount\_in\_decimal: STRING |
| **linked\_refunds**  ARRAY This is a nested data structure:   - applied\_amount: INTEGER - applied\_at: DATE-TIME - refund\_reason\_code: STRING - txn\_amount: INTEGER - txn\_date: DATE-TIME - txn\_id: STRING - txn\_status: STRING |
| **local\_currency\_code**  STRING |
| **object**  STRING |
| **price\_type**  STRING |
| **reason\_code**  STRING |
| **reference\_invoice\_id**  STRING |
| **refunded\_at**  DATE-TIME |
| **resource\_version**  INTEGER |
| **round\_off\_amount**  INTEGER |
| **status**  STRING |
| **sub\_total**  INTEGER |
| **sub\_total\_in\_local\_currency**  INTEGER |
| **subscription\_id**  STRING |
| **taxes**  ARRAY This is a nested data structure:   - amount: INTEGER - description: STRING - name: STRING |
| **total**  INTEGER |
| **total\_in\_local\_currency**  INTEGER |
| **type**  STRING |
| **updated\_at**  DATE-TIME |
| **vat\_number**  STRING |
| **vat\_number\_prefix**  STRING |
| **voided\_at**  DATE-TIME |

### customers

The `customers` table contains info about the customers in your Chargebee account.

**Note**: This table is available Refer to the [Table and field availability and Chargebee Product Catalogs section](#product-catalog-versions) for more info.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Chargebee documentation](https://apidocs.chargebee.com/Content/api/customers)  [Chargebee API method](https://apidocs.chargebee.com/Content/api/customers#list_customers "Opens in new tab: Chargebee API method") |

customers table foreign keys

| Join customers with | on |
| --- | --- |
| [credit\_notes](#credit-notes) | ``` customers.id = credit_notes.customer_id ``` |
| [events](#events) | ``` customers.id = events.content.customer.id ```  ``` customers.id = events.content.invoice.customer_id ```  ``` customers.id = events.content.subscription.customer_id ```  ``` customers.id = events.content.transaction.customer_id ```  ``` customers.primary_payment_source_id = events.content.subscription.payment_source_id ```  ``` customers.primary_payment_source_id = events.content.transaction.payment_source_id ``` |
| [invoices](#invoices) | ``` customers.id = invoices.customer_id ```  ``` customers.id = invoices.notes.entity_id ``` |
| [payment\_sources](#payment-sources) | ``` customers.id = payment_sources.customer_id ```  ``` customers.primary_payment_source_id = payment_sources.id ``` |
| [promotional\_credits](#promotional-credits) | ``` customers.id = promotional_credits.customer_id ``` |
| [subscriptions](#subscriptions) | ``` customers.id = subscriptions.customer_id ```  ``` customers.primary_payment_source_id = subscriptions.payment_source_id ``` |
| [transactions](#transactions) | ``` customers.id = transactions.customer_id ```  ``` customers.primary_payment_source_id = transactions.payment_source_id ``` |
| [virtual\_bank\_accounts](#virtual-bank-accounts) | ``` customers.id = virtual_bank_accounts.customer_id ``` |
| [gifts](#gifts) | ``` customers.id = gifts.gift_receiver.customer_id ```  ``` customers.id = gifts.gifter.customer_id ``` |
| [orders](#orders) | ``` customers.id = orders.customer_id ``` |

customers table schema

|  |
| --- |
| **allow\_direct\_debit**  BOOLEAN |
| **auto\_close\_invoices**  BOOLEAN |
| **auto\_collection**  STRING |
| **backup\_payment\_source\_id**  STRING |
| **balances**  ARRAY This is a nested data structure:   - balance\_currency\_code: STRING - currency\_code: STRING - excess\_payments: INTEGER - object: STRING - promotional\_credits: INTEGER - refundable\_credits: INTEGER - unbilled\_charges: INTEGER |
| **billing\_address**  OBJECT This is a nested data structure:   - city: STRING - company: STRING - country: STRING - email: STRING - first\_name: STRING - last\_name: STRING - line1: STRING - line2: STRING - line3: STRING - object: STRING - phone: STRING - state: STRING - state\_code: STRING - validation\_status: STRING - zip: STRING |
| **billing\_date**  BOOLEAN |
| **billing\_date\_mode**  STRING |
| **billing\_day\_of\_week**  BOOLEAN |
| **billing\_day\_of\_week\_mode**  STRING |
| **business\_customer\_without\_vat\_number**  BOOLEAN |
| **card\_status**  STRING |
| **cf\_company\_id**  INTEGER, STRING |
| **channel**  STRING |
| **child\_account\_access**  OBJECT This is a nested data structure:   - portal\_download\_invoices: STRING - portal\_edit\_subscriptions: STRING - send\_invoice\_emails: BOOLEAN - send\_payment\_emails: BOOLEAN - send\_subscription\_emails: BOOLEAN |
| **client\_profile\_id**  STRING |
| **company**  STRING |
| **consolidated\_invoicing**  BOOLEAN |
| **contacts**  ARRAY This is a nested data structure:   - email: STRING - enabled: BOOLEAN - first\_name: STRING - id: STRING - label: STRING - last\_name: STRING - object: STRING - phone: STRING - send\_account\_email: STRING - send\_billing\_email: STRING |
| **created\_at**  DATE-TIME |
| **created\_from\_ip**  STRING |
| **custom\_fields**  STRING |
| **customer\_type**  STRING |
| **deleted**  BOOLEAN |
| **email**  STRING |
| **entity\_code**  STRING |
| **entity\_identifier\_scheme**  STRING |
| **entity\_identifier\_standard**  STRING |
| **entity\_identifiers**  ARRAY This is a nested data structure:   - id: STRING - scheme: STRING - standard: STRING - value: STRING |
| **excess\_payments**  INTEGER |
| **exempt\_number**  STRING |
| **exemption\_details**  STRING |
| **first\_name**  STRING |
| **fraud\_flag**  STRING |
| **id**  STRING |
| **invoice\_notes**  STRING |
| **is\_einvoice\_enabled**  BOOLEAN |
| **is\_location\_valid**  BOOLEAN |
| **last\_name**  STRING |
| **locale**  STRING |
| **meta\_data**  STRING |
| **mrr**  INTEGER |
| **net\_term\_days**  INTEGER |
| **object**  STRING |
| **offline\_payment\_method**  STRING |
| **parent\_account\_access**  OBJECT This is a nested data structure:   - portal\_download\_child\_invoices: STRING - portal\_edit\_child\_subscriptions: STRING - send\_invoice\_emails: BOOLEAN - send\_payment\_emails: BOOLEAN - send\_subscription\_emails: BOOLEAN |
| **payment\_method**  OBJECT This is a nested data structure:   - gateway: STRING - gateway\_account\_id: STRING - object: STRING - reference\_id: STRING - status: STRING - type: STRING |
| **phone**  STRING |
| **pii\_cleared**  STRING |
| **preferred\_currency\_code**  STRING |
| **primary\_payment\_source\_id**  STRING |
| **promotional\_credits**  INTEGER |
| **referral\_urls**  ARRAY This is a nested data structure:   - created\_at: DATE-TIME - external\_customer\_id: STRING - referral\_account\_id: STRING - referral\_campaign\_id: STRING - referral\_external\_account\_id: STRING - referral\_sharing\_url: STRING - referral\_system: STRING - updated\_at: DATE-TIME |
| **refundable\_credits**  INTEGER |
| **registered\_for\_gst**  BOOLEAN |
| **relationship**  OBJECT This is a nested data structure:   - invoice\_owner\_id: STRING - parent\_id: STRING - payment\_owner\_id: STRING - root\_id: STRING |
| **resource\_version**  INTEGER |
| **taxability**  STRING |
| **unbilled\_charges**  INTEGER |
| **updated\_at**  DATE-TIME |
| **use\_default\_hierarchy\_settings**  BOOLEAN |
| **vat\_number**  STRING |
| **vat\_number\_prefix**  STRING |
| **vat\_number\_status**  STRING |
| **vat\_number\_validated\_time**  DATE-TIME |

### events

The `events` table contains info about the events that have occurred on your Chargebee site. Event records contain data about affected resources and additional details, such as when the change occurred. This can be used to create a log of events for a record and analyze how it has changed over time.

**Note**: This table is available Refer to the [Table and field availability and Chargebee Product Catalogs section](#product-catalog-versions) for more info.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | occurred\_at |
| **Useful links** | [Chargebee documentation](https://apidocs.chargebee.com/Content/api/events)  [Chargebee API method](https://apidocs.chargebee.com/Content/api/events#list_events "Opens in new tab: Chargebee API method") |

events table foreign keys

| Join events with | on |
| --- | --- |
| [addons](#addons) | ``` events.content.subscription.addons.id = addons.id ```  ``` events.content.subscription.charged_event_based_addons.id = addons.id ```  ``` events.content.subscription.event_based_addons.id = addons.id ``` |
| [coupons](#coupons) | ``` events.content.subscription.addons.id = coupons.addon_ids ```  ``` events.content.subscription.charged_event_based_addons.id = coupons.addon_ids ```  ``` events.content.subscription.event_based_addons.id = coupons.addon_ids ```  ``` events.content.coupon.id = coupons.id ```  ``` events.content.invoice.discounts.entity_id = coupons.id ```  ``` events.content.invoice.line_item_discounts.coupon_id = coupons.id ```  ``` events.content.subscription.coupons.coupon_id = coupons.id ```  ``` events.content.coupon.plan_ids = coupons.plan_ids ```  ``` events.content.subscription.plan_id = coupons.plan_ids ``` |
| [invoices](#invoices) | ``` events.content.subscription.addons.id = invoices.notes.entity_id ```  ``` events.content.subscription.charged_event_based_addons.id = invoices.notes.entity_id ```  ``` events.content.subscription.event_based_addons.id = invoices.notes.entity_id ```  ``` events.content.coupon.id = invoices.discounts.entity_id ```  ``` events.content.invoice.discounts.entity_id = invoices.discounts.entity_id ```  ``` events.content.invoice.line_item_discounts.coupon_id = invoices.discounts.entity_id ```  ``` events.content.subscription.coupons.coupon_id = invoices.discounts.entity_id ```  ``` events.content.coupon.id = invoices.line_item_discounts.coupon_id ```  ``` events.content.invoice.discounts.entity_id = invoices.line_item_discounts.coupon_id ```  ``` events.content.invoice.line_item_discounts.coupon_id = invoices.line_item_discounts.coupon_id ```  ``` events.content.subscription.coupons.coupon_id = invoices.line_item_discounts.coupon_id ```  ``` events.content.coupon.id = invoices.notes.entity_id ```  ``` events.content.invoice.discounts.entity_id = invoices.notes.entity_id ```  ``` events.content.invoice.line_item_discounts.coupon_id = invoices.notes.entity_id ```  ``` events.content.subscription.coupons.coupon_id = invoices.notes.entity_id ```  ``` events.content.invoice.adjustment_credit_notes.cn_id = invoices.adjustment_credit_notes.cn_id ```  ``` events.content.invoice.applied_credits.cn_id = invoices.adjustment_credit_notes.cn_id ```  ``` events.content.invoice.issued_credit_notes.cn_id = invoices.adjustment_credit_notes.cn_id ```  ``` events.content.invoice.adjustment_credit_notes.cn_id = invoices.applied_credits.cn_id ```  ``` events.content.invoice.applied_credits.cn_id = invoices.applied_credits.cn_id ```  ``` events.content.invoice.issued_credit_notes.cn_id = invoices.applied_credits.cn_id ```  ``` events.content.invoice.adjustment_credit_notes.cn_id = invoices.issued_credit_notes.cn_id ```  ``` events.content.invoice.applied_credits.cn_id = invoices.issued_credit_notes.cn_id ```  ``` events.content.invoice.issued_credit_notes.cn_id = invoices.issued_credit_notes.cn_id ```  ``` events.content.customer.id = invoices.customer_id ```  ``` events.content.invoice.customer_id = invoices.customer_id ```  ``` events.content.subscription.customer_id = invoices.customer_id ```  ``` events.content.transaction.customer_id = invoices.customer_id ```  ``` events.content.customer.id = invoices.notes.entity_id ```  ``` events.content.invoice.customer_id = invoices.notes.entity_id ```  ``` events.content.subscription.customer_id = invoices.notes.entity_id ```  ``` events.content.transaction.customer_id = invoices.notes.entity_id ```  ``` events.content.invoice.id = invoices.id ```  ``` events.content.transaction.linked_credit_notes.cn_reference_invoice_id = invoices.id ```  ``` events.content.invoice.line_item_discounts.line_item_id = invoices.line_item_discounts.line_item_id ```  ``` events.content.invoice.line_item_taxes.line_item_id = invoices.line_item_discounts.line_item_id ```  ``` events.content.invoice.line_items.id = invoices.line_item_discounts.line_item_id ```  ``` events.content.invoice.line_item_discounts.line_item_id = invoices.line_item_taxes.line_item_id ```  ``` events.content.invoice.line_item_taxes.line_item_id = invoices.line_item_taxes.line_item_id ```  ``` events.content.invoice.line_items.id = invoices.line_item_taxes.line_item_id ```  ``` events.content.invoice.line_item_discounts.line_item_id = invoices.line_item_tiers.line_item_id ```  ``` events.content.invoice.line_item_taxes.line_item_id = invoices.line_item_tiers.line_item_id ```  ``` events.content.invoice.line_items.id = invoices.line_item_tiers.line_item_id ```  ``` events.content.invoice.line_item_discounts.line_item_id = invoices.line_items.id ```  ``` events.content.invoice.line_item_taxes.line_item_id = invoices.line_items.id ```  ``` events.content.invoice.line_items.id = invoices.line_items.id ```  ``` events.content.coupon.plan_ids = invoices.notes.entity_id ```  ``` events.content.subscription.plan_id = invoices.notes.entity_id ```  ``` events.content.subscription.id = invoices.line_items.subscription_id ```  ``` events.content.invoice.subscription_id = invoices.line_items.subscription_id ```  ``` events.content.transaction.subscription_id = invoices.line_items.subscription_id ```  ``` events.content.subscription.id = invoices.notes.entity_id ```  ``` events.content.invoice.subscription_id = invoices.notes.entity_id ```  ``` events.content.transaction.subscription_id = invoices.notes.entity_id ```  ``` events.content.subscription.id = invoices.subscription_id ```  ``` events.content.invoice.subscription_id = invoices.subscription_id ```  ``` events.content.transaction.subscription_id = invoices.subscription_id ```  ``` events.content.invoice.linked_payments.txn_id = invoices.linked_payments.txn_id ```  ``` events.content.transaction.id = invoices.linked_payments.txn_id ```  ``` events.content.transaction.linked_refunds.txn_id = invoices.linked_payments.txn_id ```  ``` events.content.transaction.reference_transaction_id = invoices.linked_payments.txn_id ```  ``` events.content.transaction.refunded_txn_id = invoices.linked_payments.txn_id ``` |
| [plans](#plans) | ``` events.content.subscription.addons.id = plans.applicable_addons.id ```  ``` events.content.subscription.charged_event_based_addons.id = plans.applicable_addons.id ```  ``` events.content.subscription.event_based_addons.id = plans.applicable_addons.id ```  ``` events.content.coupon.plan_ids = plans.id ```  ``` events.content.subscription.plan_id = plans.id ``` |
| [subscriptions](#subscriptions) | ``` events.content.subscription.addons.id = subscriptions.addons.id ```  ``` events.content.subscription.charged_event_based_addons.id = subscriptions.addons.id ```  ``` events.content.subscription.event_based_addons.id = subscriptions.addons.id ```  ``` events.content.subscription.addons.id = subscriptions.charged_event_based_addons.id ```  ``` events.content.subscription.charged_event_based_addons.id = subscriptions.charged_event_based_addons.id ```  ``` events.content.subscription.event_based_addons.id = subscriptions.charged_event_based_addons.id ```  ``` events.content.subscription.addons.id = subscriptions.event_based_addons.id ```  ``` events.content.subscription.charged_event_based_addons.id = subscriptions.event_based_addons.id ```  ``` events.content.subscription.event_based_addons.id = subscriptions.event_based_addons.id ```  ``` events.content.coupon.id = subscriptions.coupons.coupon_id ```  ``` events.content.invoice.discounts.entity_id = subscriptions.coupons.coupon_id ```  ``` events.content.invoice.line_item_discounts.coupon_id = subscriptions.coupons.coupon_id ```  ``` events.content.subscription.coupons.coupon_id = subscriptions.coupons.coupon_id ```  ``` events.content.customer.id = subscriptions.customer_id ```  ``` events.content.invoice.customer_id = subscriptions.customer_id ```  ``` events.content.subscription.customer_id = subscriptions.customer_id ```  ``` events.content.transaction.customer_id = subscriptions.customer_id ```  ``` events.content.coupon.plan_ids = subscriptions.plan_id ```  ``` events.content.subscription.plan_id = subscriptions.plan_id ```  ``` events.content.subscription.payment_source_id = subscriptions.payment_source_id ```  ``` events.content.transaction.payment_source_id = subscriptions.payment_source_id ```  ``` events.content.subscription.id = subscriptions.id ```  ``` events.content.invoice.subscription_id = subscriptions.id ```  ``` events.content.transaction.subscription_id = subscriptions.id ``` |
| [credit\_notes](#credit-notes) | ``` events.content.coupon.id = credit_notes.discounts.entity_id ```  ``` events.content.invoice.discounts.entity_id = credit_notes.discounts.entity_id ```  ``` events.content.invoice.line_item_discounts.coupon_id = credit_notes.discounts.entity_id ```  ``` events.content.subscription.coupons.coupon_id = credit_notes.discounts.entity_id ```  ``` events.content.coupon.id = credit_notes.line_item_discounts.coupon_id ```  ``` events.content.invoice.discounts.entity_id = credit_notes.line_item_discounts.coupon_id ```  ``` events.content.invoice.line_item_discounts.coupon_id = credit_notes.line_item_discounts.coupon_id ```  ``` events.content.subscription.coupons.coupon_id = credit_notes.line_item_discounts.coupon_id ```  ``` events.content.invoice.adjustment_credit_notes.cn_id = credit_notes.id ```  ``` events.content.invoice.applied_credits.cn_id = credit_notes.id ```  ``` events.content.invoice.issued_credit_notes.cn_id = credit_notes.id ```  ``` events.content.customer.id = credit_notes.customer_id ```  ``` events.content.invoice.customer_id = credit_notes.customer_id ```  ``` events.content.subscription.customer_id = credit_notes.customer_id ```  ``` events.content.transaction.customer_id = credit_notes.customer_id ```  ``` events.content.invoice.id = credit_notes.allocations.invoice_id ```  ``` events.content.transaction.linked_credit_notes.cn_reference_invoice_id = credit_notes.allocations.invoice_id ```  ``` events.content.invoice.id = credit_notes.reference_invoice_id ```  ``` events.content.transaction.linked_credit_notes.cn_reference_invoice_id = credit_notes.reference_invoice_id ```  ``` events.content.invoice.line_item_discounts.line_item_id = credit_notes.line_item_discounts.line_item_id ```  ``` events.content.invoice.line_item_taxes.line_item_id = credit_notes.line_item_discounts.line_item_id ```  ``` events.content.invoice.line_items.id = credit_notes.line_item_discounts.line_item_id ```  ``` events.content.invoice.line_item_discounts.line_item_id = credit_notes.line_item_taxes.line_item_id ```  ``` events.content.invoice.line_item_taxes.line_item_id = credit_notes.line_item_taxes.line_item_id ```  ``` events.content.invoice.line_items.id = credit_notes.line_item_taxes.line_item_id ```  ``` events.content.invoice.line_item_discounts.line_item_id = credit_notes.line_item_tiers.line_item_id ```  ``` events.content.invoice.line_item_taxes.line_item_id = credit_notes.line_item_tiers.line_item_id ```  ``` events.content.invoice.line_items.id = credit_notes.line_item_tiers.line_item_id ```  ``` events.content.invoice.line_item_discounts.line_item_id = credit_notes.line_items.id ```  ``` events.content.invoice.line_item_taxes.line_item_id = credit_notes.line_items.id ```  ``` events.content.invoice.line_items.id = credit_notes.line_items.id ```  ``` events.content.subscription.id = credit_notes.subscription_id ```  ``` events.content.invoice.subscription_id = credit_notes.subscription_id ```  ``` events.content.transaction.subscription_id = credit_notes.subscription_id ```  ``` events.content.subscription.id = credit_notes.line_items.subscription_id ```  ``` events.content.invoice.subscription_id = credit_notes.line_items.subscription_id ```  ``` events.content.transaction.subscription_id = credit_notes.line_items.subscription_id ```  ``` events.content.invoice.linked_payments.txn_id = credit_notes.linked_refunds.txn_id ```  ``` events.content.transaction.id = credit_notes.linked_refunds.txn_id ```  ``` events.content.transaction.linked_refunds.txn_id = credit_notes.linked_refunds.txn_id ```  ``` events.content.transaction.reference_transaction_id = credit_notes.linked_refunds.txn_id ```  ``` events.content.transaction.refunded_txn_id = credit_notes.linked_refunds.txn_id ``` |
| [orders](#orders) | ``` events.content.coupon.id = orders.line_item_discounts.coupon_id ```  ``` events.content.invoice.discounts.entity_id = orders.line_item_discounts.coupon_id ```  ``` events.content.invoice.line_item_discounts.coupon_id = orders.line_item_discounts.coupon_id ```  ``` events.content.subscription.coupons.coupon_id = orders.line_item_discounts.coupon_id ```  ``` events.content.invoice.adjustment_credit_notes.cn_id = orders.linked_credit_notes.id ```  ``` events.content.invoice.applied_credits.cn_id = orders.linked_credit_notes.id ```  ``` events.content.invoice.issued_credit_notes.cn_id = orders.linked_credit_notes.id ```  ``` events.content.customer.id = orders.customer_id ```  ``` events.content.invoice.customer_id = orders.customer_id ```  ``` events.content.subscription.customer_id = orders.customer_id ```  ``` events.content.transaction.customer_id = orders.customer_id ```  ``` events.content.invoice.id = orders.invoice_id ```  ``` events.content.transaction.linked_credit_notes.cn_reference_invoice_id = orders.invoice_id ```  ``` events.content.invoice.line_item_discounts.line_item_id = orders.line_item_discounts.line_item_id ```  ``` events.content.invoice.line_item_taxes.line_item_id = orders.line_item_discounts.line_item_id ```  ``` events.content.invoice.line_items.id = orders.line_item_discounts.line_item_id ```  ``` events.content.invoice.line_item_discounts.line_item_id = orders.line_item_taxes.line_item_id ```  ``` events.content.invoice.line_item_taxes.line_item_id = orders.line_item_taxes.line_item_id ```  ``` events.content.invoice.line_items.id = orders.line_item_taxes.line_item_id ```  ``` events.content.subscription.id = orders.subscription_id ```  ``` events.content.invoice.subscription_id = orders.subscription_id ```  ``` events.content.transaction.subscription_id = orders.subscription_id ``` |
| [customers](#customers) | ``` events.content.customer.id = customers.id ```  ``` events.content.invoice.customer_id = customers.id ```  ``` events.content.subscription.customer_id = customers.id ```  ``` events.content.transaction.customer_id = customers.id ```  ``` events.content.subscription.payment_source_id = customers.primary_payment_source_id ```  ``` events.content.transaction.payment_source_id = customers.primary_payment_source_id ``` |
| [payment\_sources](#payment-sources) | ``` events.content.customer.id = payment_sources.customer_id ```  ``` events.content.invoice.customer_id = payment_sources.customer_id ```  ``` events.content.subscription.customer_id = payment_sources.customer_id ```  ``` events.content.transaction.customer_id = payment_sources.customer_id ```  ``` events.content.subscription.payment_source_id = payment_sources.id ```  ``` events.content.transaction.payment_source_id = payment_sources.id ``` |
| [promotional\_credits](#promotional-credits) | ``` events.content.customer.id = promotional_credits.customer_id ```  ``` events.content.invoice.customer_id = promotional_credits.customer_id ```  ``` events.content.subscription.customer_id = promotional_credits.customer_id ```  ``` events.content.transaction.customer_id = promotional_credits.customer_id ``` |
| [transactions](#transactions) | ``` events.content.customer.id = transactions.customer_id ```  ``` events.content.invoice.customer_id = transactions.customer_id ```  ``` events.content.subscription.customer_id = transactions.customer_id ```  ``` events.content.transaction.customer_id = transactions.customer_id ```  ``` events.content.invoice.id = transactions.linked_credit_notes.cn_reference_invoice_id ```  ``` events.content.transaction.linked_credit_notes.cn_reference_invoice_id = transactions.linked_credit_notes.cn_reference_invoice_id ```  ``` events.content.subscription.payment_source_id = transactions.payment_source_id ```  ``` events.content.transaction.payment_source_id = transactions.payment_source_id ```  ``` events.content.subscription.id = transactions.subscription_id ```  ``` events.content.invoice.subscription_id = transactions.subscription_id ```  ``` events.content.transaction.subscription_id = transactions.subscription_id ```  ``` events.content.invoice.linked_payments.txn_id = transactions.id ```  ``` events.content.transaction.id = transactions.id ```  ``` events.content.transaction.linked_refunds.txn_id = transactions.id ```  ``` events.content.transaction.reference_transaction_id = transactions.id ```  ``` events.content.transaction.refunded_txn_id = transactions.id ```  ``` events.content.invoice.linked_payments.txn_id = transactions.linked_refunds.txn_id ```  ``` events.content.transaction.id = transactions.linked_refunds.txn_id ```  ``` events.content.transaction.linked_refunds.txn_id = transactions.linked_refunds.txn_id ```  ``` events.content.transaction.reference_transaction_id = transactions.linked_refunds.txn_id ```  ``` events.content.transaction.refunded_txn_id = transactions.linked_refunds.txn_id ```  ``` events.content.invoice.linked_payments.txn_id = transactions.reference_transaction_id ```  ``` events.content.transaction.id = transactions.reference_transaction_id ```  ``` events.content.transaction.linked_refunds.txn_id = transactions.reference_transaction_id ```  ``` events.content.transaction.reference_transaction_id = transactions.reference_transaction_id ```  ``` events.content.transaction.refunded_txn_id = transactions.reference_transaction_id ```  ``` events.content.invoice.linked_payments.txn_id = transactions.refunded_txn_id ```  ``` events.content.transaction.id = transactions.refunded_txn_id ```  ``` events.content.transaction.linked_refunds.txn_id = transactions.refunded_txn_id ```  ``` events.content.transaction.reference_transaction_id = transactions.refunded_txn_id ```  ``` events.content.transaction.refunded_txn_id = transactions.refunded_txn_id ``` |
| [virtual\_bank\_accounts](#virtual-bank-accounts) | ``` events.content.customer.id = virtual_bank_accounts.customer_id ```  ``` events.content.invoice.customer_id = virtual_bank_accounts.customer_id ```  ``` events.content.subscription.customer_id = virtual_bank_accounts.customer_id ```  ``` events.content.transaction.customer_id = virtual_bank_accounts.customer_id ``` |
| [gifts](#gifts) | ``` events.content.customer.id = gifts.gift_receiver.customer_id ```  ``` events.content.invoice.customer_id = gifts.gift_receiver.customer_id ```  ``` events.content.subscription.customer_id = gifts.gift_receiver.customer_id ```  ``` events.content.transaction.customer_id = gifts.gift_receiver.customer_id ```  ``` events.content.customer.id = gifts.gifter.customer_id ```  ``` events.content.invoice.customer_id = gifts.gifter.customer_id ```  ``` events.content.subscription.customer_id = gifts.gifter.customer_id ```  ``` events.content.transaction.customer_id = gifts.gifter.customer_id ```  ``` events.content.invoice.id = gifts.gifter.invoice_id ```  ``` events.content.transaction.linked_credit_notes.cn_reference_invoice_id = gifts.gifter.invoice_id ```  ``` events.content.subscription.id = gifts.gift_receiver.subscription_id ```  ``` events.content.invoice.subscription_id = gifts.gift_receiver.subscription_id ```  ``` events.content.transaction.subscription_id = gifts.gift_receiver.subscription_id ``` |

events table schema

|  |
| --- |
| **api\_version**  STRING |
| **content**  OBJECT This is a nested data structure:   - coupon: OBJECT, which is also a nested data structure.   - apply\_discount\_on: STRING   - apply\_on: STRING   - archived\_at: DATE-TIME   - created\_at: DATE-TIME   - currency\_code: STRING   - discount\_amount: NUMBER   - discount\_percentage: NUMBER   - discount\_type: STRING   - duration\_month: INTEGER   - duration\_type: STRING   - id: STRING   - invoice\_name: STRING   - invoice\_notes: STRING   - item\_constraint\_criteria: ARRAY, which is also a nested data structure.     - currencies: ARRAY, which is also a nested data structure.     - item\_family\_ids: ARRAY, which is also a nested data structure.     - item\_price\_periods: ARRAY, which is also a nested data structure.     - item\_type: STRING   - item\_constraints: ARRAY, which is also a nested data structure.     - constraint: STRING     - item\_price\_ids: ARRAY, which is also a nested data structure.     - item\_type: STRING   - max\_redemptions: INTEGER   - meta\_data: STRING   - name: STRING   - object: STRING   - period: INTEGER   - period\_unit: STRING   - redemptions: INTEGER   - resource\_version: INTEGER   - status: STRING   - updated\_at: DATE-TIME   - valid\_till: DATE-TIME - coupon\_code: OBJECT, which is also a nested data structure.   - code: STRING   - coupon\_id: STRING   - coupon\_set\_id: STRING   - coupon\_set\_name: STRING   - coupon\_site\_id: STRING   - status: STRING - coupon\_set: OBJECT, which is also a nested data structure.   - archived\_count: INTEGER   - coupon\_id: STRING   - id: STRING   - meta\_data: STRING   - name: STRING   - redeemed\_count: INTEGER   - total\_count: INTEGER - credit\_note: OBJECT, which is also a nested data structure.   - allocations: ARRAY, which is also a nested data structure.     - allocated\_amount: INTEGER     - allocated\_at: DATE-TIME     - invoice\_date: DATE-TIME     - invoice\_id: STRING     - invoice\_status: STRING   - amount\_allocated: INTEGER   - amount\_available: INTEGER   - amount\_refunded: INTEGER   - base\_currency\_code: STRING   - channel: STRING   - create\_reason\_code: STRING   - currency\_code: STRING   - customer\_id: STRING   - date: DATE-TIME   - deleted: BOOLEAN   - discounts: ARRAY, which is also a nested data structure.     - amount: INTEGER     - description: STRING     - entity\_id: STRING     - entity\_type: STRING     - object: STRING   - einvoice: OBJECT, which is also a nested data structure.     - id: STRING     - message: STRING     - status: STRING   - exchange\_rate: NUMBER   - fractional\_correction: INTEGER   - generated\_at: DATE-TIME   - id: STRING   - line\_item\_discounts: ARRAY, which is also a nested data structure.     - coupon\_id: STRING     - discount\_amount: INTEGER     - discount\_type: STRING     - entity\_id: STRING     - line\_item\_id: STRING     - object: STRING   - line\_item\_taxes: ARRAY, which is also a nested data structure.     - is\_non\_compliance\_tax: BOOLEAN     - is\_partial\_tax\_applied: BOOLEAN     - line\_item\_id: STRING     - local\_currency\_code: STRING     - tax\_amount: INTEGER     - tax\_amount\_in\_local\_currency: INTEGER     - tax\_juris\_code: STRING     - tax\_juris\_name: STRING     - tax\_juris\_type: STRING     - tax\_name: STRING     - tax\_rate: NUMBER     - taxable\_amount: INTEGER   - line\_item\_tiers: ARRAY, which is also a nested data structure.     - ending\_unit: INTEGER     - ending\_unit\_in\_decimal: STRING     - line\_item\_id: STRING     - quantity\_used: INTEGER     - quantity\_used\_in\_decimal: STRING     - starting\_unit: INTEGER     - starting\_unit\_in\_decimal: STRING     - unit\_amount: INTEGER     - unit\_amount\_in\_decimal: STRING   - line\_items: ARRAY, which is also a nested data structure.     - amount: INTEGER     - amount\_in\_decimal: STRING     - customer\_id: STRING     - date\_from: DATE-TIME     - date\_to: DATE-TIME     - description: STRING     - discount\_amount: INTEGER     - entity\_description: STRING     - entity\_id: STRING     - entity\_type: STRING     - id: STRING     - is\_taxed: BOOLEAN     - item\_level\_discount\_amount: INTEGER     - object: STRING     - pricing\_model: STRING     - quantity: INTEGER     - quantity\_in\_decimal: STRING     - subscription\_id: STRING     - tax\_amount: INTEGER     - tax\_exempt\_reason: STRING     - tax\_rate: NUMBER     - unit\_amount: INTEGER     - unit\_amount\_in\_decimal: STRING   - linked\_refunds: ARRAY, which is also a nested data structure.     - applied\_amount: INTEGER     - applied\_at: DATE-TIME     - refund\_reason\_code: STRING     - txn\_amount: INTEGER     - txn\_date: DATE-TIME     - txn\_id: STRING     - txn\_status: STRING   - local\_currency\_code: STRING   - object: STRING   - price\_type: STRING   - reason\_code: STRING   - reference\_invoice\_id: STRING   - refunded\_at: DATE-TIME   - resource\_version: INTEGER   - round\_off\_amount: INTEGER   - status: STRING   - sub\_total: INTEGER   - sub\_total\_in\_local\_currency: INTEGER   - subscription\_id: STRING   - taxes: ARRAY, which is also a nested data structure.     - amount: INTEGER     - description: STRING     - name: STRING   - total: INTEGER   - total\_in\_local\_currency: INTEGER   - type: STRING   - updated\_at: DATE-TIME   - vat\_number: STRING   - vat\_number\_prefix: STRING   - voided\_at: DATE-TIME - customer: OBJECT, which is also a nested data structure.   - allow\_direct\_debit: BOOLEAN   - auto\_close\_invoices: BOOLEAN   - auto\_collection: STRING   - backup\_payment\_source\_id: STRING   - balances: ARRAY, which is also a nested data structure.     - balance\_currency\_code: STRING     - currency\_code: STRING     - excess\_payments: INTEGER     - object: STRING     - promotional\_credits: INTEGER     - refundable\_credits: INTEGER     - unbilled\_charges: INTEGER   - billing\_address: OBJECT, which is also a nested data structure.     - city: STRING     - company: STRING     - country: STRING     - email: STRING     - first\_name: STRING     - last\_name: STRING     - line1: STRING     - line2: STRING     - line3: STRING     - object: STRING     - phone: STRING     - state: STRING     - state\_code: STRING     - validation\_status: STRING     - zip: STRING   - billing\_date: BOOLEAN   - billing\_date\_mode: STRING   - billing\_day\_of\_week: BOOLEAN   - billing\_day\_of\_week\_mode: STRING   - business\_customer\_without\_vat\_number: BOOLEAN   - business\_entity\_id: STRING   - card\_status: STRING   - cf\_company\_id: INTEGER, STRING   - cf\_people\_id: STRING   - channel: STRING   - child\_account\_access: OBJECT, which is also a nested data structure.     - portal\_download\_invoices: STRING     - portal\_edit\_subscriptions: STRING     - send\_invoice\_emails: BOOLEAN     - send\_payment\_emails: BOOLEAN     - send\_subscription\_emails: BOOLEAN   - client\_profile\_id: STRING   - company: STRING   - consolidated\_invoicing: BOOLEAN   - contacts: ARRAY, which is also a nested data structure.     - email: STRING     - enabled: BOOLEAN     - first\_name: STRING     - id: STRING     - label: STRING     - last\_name: STRING     - object: STRING     - phone: STRING     - send\_account\_email: STRING     - send\_billing\_email: STRING   - created\_at: DATE-TIME   - created\_from\_ip: STRING   - custom\_fields: STRING   - customer\_type: STRING   - deleted: BOOLEAN   - email: STRING   - entity\_code: STRING   - entity\_identifier\_scheme: STRING   - entity\_identifier\_standard: STRING   - entity\_identifiers: ARRAY, which is also a nested data structure.     - id: STRING     - scheme: STRING     - standard: STRING     - value: STRING   - excess\_payments: INTEGER   - exempt\_number: STRING   - exemption\_details: STRING   - first\_name: STRING   - fraud\_flag: STRING   - id: STRING   - invoice\_notes: STRING   - is\_einvoice\_enabled: BOOLEAN   - is\_location\_valid: BOOLEAN   - last\_name: STRING   - locale: STRING   - meta\_data: STRING   - mrr: INTEGER   - net\_term\_days: INTEGER   - object: STRING   - offline\_payment\_method: STRING   - parent\_account\_access: OBJECT, which is also a nested data structure.     - portal\_download\_child\_invoices: STRING     - portal\_edit\_child\_subscriptions: STRING     - send\_invoice\_emails: BOOLEAN     - send\_payment\_emails: BOOLEAN     - send\_subscription\_emails: BOOLEAN   - payment\_method: OBJECT, which is also a nested data structure.     - gateway: STRING     - gateway\_account\_id: STRING     - object: STRING     - reference\_id: STRING     - status: STRING     - type: STRING   - phone: STRING   - pii\_cleared: STRING   - preferred\_currency\_code: STRING   - primary\_payment\_source\_id: STRING   - promotional\_credits: INTEGER   - referral\_urls: ARRAY, which is also a nested data structure.     - created\_at: DATE-TIME     - external\_customer\_id: STRING     - referral\_account\_id: STRING     - referral\_campaign\_id: STRING     - referral\_external\_account\_id: STRING     - referral\_sharing\_url: STRING     - referral\_system: STRING     - updated\_at: DATE-TIME   - refundable\_credits: INTEGER   - registered\_for\_gst: BOOLEAN   - relationship: OBJECT, which is also a nested data structure.     - invoice\_owner\_id: STRING     - parent\_id: STRING     - payment\_owner\_id: STRING     - root\_id: STRING   - resource\_version: INTEGER   - tax\_providers\_fields: STRING   - taxability: STRING   - unbilled\_charges: INTEGER   - updated\_at: DATE-TIME   - use\_default\_hierarchy\_settings: BOOLEAN   - vat\_number: STRING   - vat\_number\_prefix: STRING   - vat\_number\_status: STRING   - vat\_number\_validated\_time: DATE-TIME - gift: OBJECT, which is also a nested data structure.   - auto\_claim: BOOLEAN   - claim\_expiry\_date: DATE-TIME   - gift\_receiver: OBJECT, which is also a nested data structure.     - customer\_id: STRING     - email: STRING     - first\_name: STRING     - last\_name: STRING     - subscription\_id: STRING   - gift\_timelines: ARRAY, which is also a nested data structure.     - occurred\_at: DATE-TIME     - status: STRING   - gifter: OBJECT, which is also a nested data structure.     - customer\_id: STRING     - invoice\_id: STRING     - note: STRING     - signature: STRING   - id: STRING   - no\_expiry: BOOLEAN   - resource\_version: INTEGER   - scheduled\_at: DATE-TIME   - status: STRING   - updated\_at: DATE-TIME - invoice: OBJECT, which is also a nested data structure.   - adjustment\_credit\_notes: ARRAY, which is also a nested data structure.     - cn\_create\_reason\_code: STRING     - cn\_date: DATE-TIME     - cn\_id: STRING     - cn\_reason\_code: STRING     - cn\_status: STRING     - cn\_total: INTEGER   - amount\_adjusted: INTEGER   - amount\_due: INTEGER   - amount\_paid: INTEGER   - amount\_to\_collect: INTEGER   - applied\_credits: ARRAY, which is also a nested data structure.     - applied\_amount: INTEGER     - applied\_at: DATE-TIME     - cn\_create\_reason\_code: STRING     - cn\_date: DATE-TIME     - cn\_id: STRING     - cn\_reason\_code: STRING     - cn\_status: STRING   - base\_currency\_code: STRING   - billing\_address: OBJECT, which is also a nested data structure.     - city: STRING     - company: STRING     - country: STRING     - email: STRING     - first\_name: STRING     - last\_name: STRING     - line1: STRING     - line2: STRING     - line3: STRING     - object: STRING     - phone: STRING     - state: STRING     - state\_code: STRING     - validation\_status: STRING     - zip: STRING   - channel: STRING   - credits\_applied: INTEGER   - currency\_code: STRING   - customer\_id: STRING   - date: DATE-TIME   - deleted: BOOLEAN   - discounts: ARRAY, which is also a nested data structure.     - amount: INTEGER     - description: STRING     - entity\_id: STRING     - entity\_type: STRING     - object: STRING   - due\_date: DATE-TIME   - dunning\_attempts: ARRAY, which is also a nested data structure.     - attempt: INTEGER     - created\_at: DATE-TIME     - dunning\_type: STRING     - transaction\_id: STRING     - txn\_amount: INTEGER     - txn\_status: STRING   - dunning\_status: STRING   - einvoice: OBJECT, which is also a nested data structure.     - id: STRING     - message: STRING     - status: STRING   - exchange\_rate: NUMBER   - expected\_payment\_date: DATE-TIME   - first\_invoice: BOOLEAN   - generated\_at: DATE-TIME   - has\_advance\_charges: BOOLEAN   - id: STRING   - is\_gifted: BOOLEAN   - issued\_credit\_notes: ARRAY, which is also a nested data structure.     - cn\_create\_reason\_code: STRING     - cn\_date: DATE-TIME     - cn\_id: STRING     - cn\_reason\_code: STRING     - cn\_status: STRING     - cn\_total: INTEGER   - line\_item\_discounts: ARRAY, which is also a nested data structure.     - coupon\_id: STRING     - discount\_amount: INTEGER     - discount\_type: STRING     - entity\_id: STRING     - line\_item\_id: STRING     - object: STRING   - line\_item\_taxes: ARRAY, which is also a nested data structure.     - is\_non\_compliance\_tax: BOOLEAN     - is\_partial\_tax\_applied: BOOLEAN     - line\_item\_id: STRING     - local\_currency\_code: STRING     - tax\_amount: INTEGER     - tax\_amount\_in\_local\_currency: INTEGER     - tax\_juris\_code: STRING     - tax\_juris\_name: STRING     - tax\_juris\_type: STRING     - tax\_name: STRING     - tax\_rate: INTEGER, NUMBER     - taxable\_amount: INTEGER   - line\_item\_tiers: ARRAY, which is also a nested data structure.     - ending\_unit: INTEGER     - ending\_unit\_in\_decimal: STRING     - line\_item\_id: STRING     - quantity\_used: INTEGER     - quantity\_used\_in\_decimal: STRING     - starting\_unit: INTEGER     - starting\_unit\_in\_decimal: STRING     - unit\_amount: INTEGER     - unit\_amount\_in\_decimal: STRING   - line\_items: ARRAY, which is also a nested data structure.     - amount: INTEGER     - amount\_in\_decimal: STRING     - customer\_id: STRING     - date\_from: DATE-TIME     - date\_to: DATE-TIME     - description: STRING     - discount\_amount: INTEGER     - entity\_description: STRING     - entity\_id: STRING     - entity\_type: STRING     - id: STRING     - is\_taxed: BOOLEAN     - item\_level\_discount\_amount: INTEGER     - object: STRING     - pricing\_model: STRING     - quantity: INTEGER     - quantity\_in\_decimal: STRING     - subscription\_id: STRING     - tax\_amount: INTEGER     - tax\_exempt\_reason: STRING     - tax\_rate: NUMBER     - unit\_amount: INTEGER     - unit\_amount\_in\_decimal: STRING   - linked\_orders: ARRAY, which is also a nested data structure.     - batch\_id: STRING     - created\_at: DATE-TIME     - document\_number: STRING     - fulfillment\_status: STRING     - id: STRING     - order\_type: STRING     - reference\_id: STRING     - status: STRING   - linked\_payments: ARRAY, which is also a nested data structure.     - applied\_amount: INTEGER     - applied\_at: DATE-TIME     - txn\_amount: INTEGER     - txn\_date: DATE-TIME     - txn\_id: STRING     - txn\_status: STRING   - local\_currency\_code: STRING   - net\_term\_days: INTEGER   - new\_sales\_amount: INTEGER   - next\_retry\_at: DATE-TIME   - notes: ARRAY, which is also a nested data structure.     - entity\_id: STRING     - entity\_type: STRING     - note: STRING   - object: STRING   - paid\_at: DATE-TIME   - payment\_owner: STRING   - po\_number: STRING   - price\_type: STRING   - recurring: BOOLEAN   - resource\_version: INTEGER   - round\_off\_amount: INTEGER   - shipping\_address: OBJECT, which is also a nested data structure.     - city: STRING     - company: STRING     - country: STRING     - email: STRING     - first\_name: STRING     - last\_name: STRING     - line1: STRING     - line2: STRING     - line3: STRING     - object: STRING     - phone: STRING     - state: STRING     - state\_code: STRING     - validation\_status: STRING     - zip: STRING   - status: STRING   - sub\_total: INTEGER   - sub\_total\_in\_local\_currency: INTEGER   - subscription\_id: STRING   - tax: INTEGER   - taxes: ARRAY, which is also a nested data structure.     - amount: INTEGER     - description: STRING     - name: STRING   - term\_finalized: BOOLEAN   - total: INTEGER   - total\_in\_local\_currency: INTEGER   - updated\_at: DATE-TIME   - vat\_number: STRING   - vat\_number\_prefix: STRING   - void\_reason\_code: STRING   - voided\_at: DATE-TIME   - write\_off\_amount: INTEGER - item: OBJECT, which is also a nested data structure.   - applicable\_items: ARRAY, which is also a nested data structure.     - id: STRING   - archivable: BOOLEAN, STRING   - archived\_at: DATE-TIME   - channel: STRING   - custom\_fields: STRING   - description: STRING   - enabled\_for\_checkout: BOOLEAN   - enabled\_in\_portal: BOOLEAN   - external\_name: STRING   - gift\_claim\_redirect\_url: STRING   - id: STRING   - included\_in\_mrr: BOOLEAN   - is\_giftable: BOOLEAN   - is\_shippable: BOOLEAN   - item\_applicability: STRING   - item\_family\_id: STRING   - metadata: STRING   - metered: BOOLEAN   - name: STRING   - object: STRING   - redirect\_url: STRING   - resource\_version: INTEGER   - status: STRING   - type: STRING   - unit: STRING   - updated\_at: DATE-TIME   - usage\_calculation: STRING - item\_family: OBJECT, which is also a nested data structure.   - channel: STRING   - custom\_fields: STRING   - description: STRING   - id: STRING   - name: STRING   - object: STRING   - resource\_version: INTEGER   - status: STRING   - updated\_at: DATE-TIME - item\_price: OBJECT, which is also a nested data structure.   - accounting\_detail: OBJECT, which is also a nested data structure.     - accounting\_category1: STRING     - accounting\_category2: STRING     - accounting\_category3: STRING     - accounting\_category4: STRING     - accounting\_code: STRING     - sku: STRING   - archivable: BOOLEAN, STRING   - archived\_at: DATE-TIME   - billing\_cycles: INTEGER   - channel: STRING   - created\_at: DATE-TIME   - currency\_code: STRING   - custom\_fields: STRING   - description: STRING   - external\_name: STRING   - free\_quantity: INTEGER   - free\_quantity\_in\_decimal: STRING   - id: STRING   - invoice\_notes: STRING   - is\_taxable: BOOLEAN   - item\_family\_id: STRING   - item\_id: STRING   - item\_type: STRING   - metadata: STRING   - name: STRING   - object: STRING   - period: INTEGER   - period\_unit: STRING   - price: INTEGER   - price\_in\_decimal: STRING   - pricing\_model: STRING   - resource\_version: INTEGER   - shipping\_period: INTEGER   - shipping\_period\_unit: STRING   - show\_description\_in\_invoices: BOOLEAN   - show\_description\_in\_quotes: BOOLEAN   - status: STRING   - tax\_detail: OBJECT, which is also a nested data structure.     - avalara\_sale\_type: STRING     - avalara\_service\_type: INTEGER     - avalara\_tax\_code: STRING     - avalara\_transaction\_type: INTEGER     - tax\_profile\_id: STRING     - taxjar\_product\_code: STRING   - tiers: ARRAY, which is also a nested data structure.     - ending\_unit: INTEGER     - price: INTEGER     - starting\_unit: INTEGER   - trial\_end\_action: STRING   - trial\_period: INTEGER   - trial\_period\_unit: STRING   - updated\_at: DATE-TIME - order: OBJECT, which is also a nested data structure.   - amount\_adjusted: INTEGER   - amount\_paid: INTEGER   - batch\_id: STRING   - billing\_address: OBJECT, which is also a nested data structure.     - city: STRING     - company: STRING     - country: STRING     - email: STRING     - first\_name: STRING     - last\_name: STRING     - line1: STRING     - line2: STRING     - line3: STRING     - object: STRING     - phone: STRING     - state: STRING     - state\_code: STRING     - validation\_status: STRING     - zip: STRING   - cancellation\_reason: STRING   - cancelled\_at: DATE-TIME   - created\_at: DATE-TIME   - created\_by: STRING   - currency\_code: STRING   - customer\_id: STRING   - deleted: BOOLEAN   - delivered\_at: DATE-TIME   - discount: INTEGER   - document\_number: STRING   - fulfillment\_status: STRING   - gift\_id: STRING   - gift\_note: STRING   - id: STRING   - invoice\_id: STRING   - invoice\_round\_off\_amount: INTEGER   - is\_gifted: BOOLEAN   - is\_resent: BOOLEAN   - line\_item\_discounts: ARRAY, which is also a nested data structure.     - coupon\_id: STRING     - discount\_amount: INTEGER     - discount\_type: STRING     - line\_item\_id: STRING   - line\_item\_taxes: ARRAY, which is also a nested data structure.     - is\_non\_compliance\_tax: BOOLEAN     - is\_partial\_tax\_applied: BOOLEAN     - line\_item\_id: STRING     - local\_currency\_code: STRING     - tax\_amount: INTEGER     - tax\_amount\_in\_local\_currency: INTEGER     - tax\_juris\_code: STRING     - tax\_juris\_name: STRING     - tax\_juris\_type: STRING     - tax\_name: STRING     - tax\_rate: INTEGER, NUMBER     - taxable\_amount: INTEGER   - linked\_credit\_notes: ARRAY, which is also a nested data structure.     - amount: INTEGER     - amount\_adjusted: INTEGER     - amount\_refunded: INTEGER     - id: STRING     - id: STRING     - type: STRING   - note: STRING   - order\_date: DATE-TIME   - order\_line\_items: ARRAY, which is also a nested data structure.     - amount: INTEGER     - amount\_adjusted: INTEGER     - amount\_paid: INTEGER     - description: STRING     - discount\_amount: INTEGER     - entity\_id: STRING     - entity\_type: STRING     - fulfillment\_amount: INTEGER     - fulfillment\_quantity: INTEGER     - id: STRING     - invoice\_id: STRING     - invoice\_line\_item\_id: STRING     - is\_shippable: BOOLEAN     - item\_level\_discount\_amount: INTEGER     - refundable\_credits: INTEGER     - refundable\_credits\_issued: INTEGER     - sku: STRING     - status: STRING     - tax\_amount: INTEGER     - unit\_price: INTEGER   - order\_type: STRING   - original\_order\_id: STRING   - paid\_on: DATE-TIME   - payment\_status: STRING   - price\_type: STRING   - reference\_id: STRING   - refundable\_credits: INTEGER   - refundable\_credits\_issued: INTEGER   - resend\_reason: STRING   - resent\_orders: ARRAY, which is also a nested data structure.     - amount: INTEGER     - order\_id: STRING     - reason: STRING   - resent\_status: STRING   - resource\_version: INTEGER   - rounding\_adjustement: INTEGER   - shipment\_carrier: STRING   - shipped\_at: DATE-TIME   - shipping\_address: OBJECT, which is also a nested data structure.     - city: STRING     - company: STRING     - country: STRING     - email: STRING     - first\_name: STRING     - last\_name: STRING     - line1: STRING     - line2: STRING     - line3: STRING     - object: STRING     - phone: STRING     - state: STRING     - state\_code: STRING     - validation\_status: STRING     - zip: STRING   - shipping\_cut\_off\_date: DATE-TIME   - shipping\_date: DATE-TIME   - status: STRING   - status\_update\_at: DATE-TIME   - sub\_total: INTEGER   - subscription\_id: STRING   - tax: INTEGER   - total: INTEGER   - tracking\_id: STRING   - tracking\_url: STRING   - updated\_at: DATE-TIME - payment\_source: OBJECT, which is also a nested data structure.   - amazon\_payment: OBJECT, which is also a nested data structure.     - agreement\_id: STRING     - email: STRING   - bank\_account: OBJECT, which is also a nested data structure.     - account\_holder\_type: STRING     - account\_type: STRING     - bank\_name: STRING     - echeck\_type: STRING     - last4: STRING     - mandate\_id: STRING     - name\_on\_account: STRING   - card: OBJECT, which is also a nested data structure.     - billing\_addr1: STRING     - billing\_addr2: STRING     - billing\_city: STRING     - billing\_country: STRING     - billing\_state: STRING     - billing\_state\_code: STRING     - billing\_zip: STRING     - brand: STRING     - expiry\_month: INTEGER     - expiry\_year: INTEGER     - first\_name: STRING     - funding\_type: STRING     - iin: STRING     - last4: STRING     - last\_name: STRING     - masked\_number: STRING     - object: STRING   - created\_at: DATE-TIME   - customer\_id: STRING   - deleted: BOOLEAN   - gateway: STRING   - gateway\_account\_id: STRING   - id: STRING   - ip\_address: STRING   - issuing\_country: STRING   - mandates: ARRAY, which is also a nested data structure.     - created\_at: DATE-TIME     - id: STRING     - subscription\_id: STRING   - object: STRING   - paypal: OBJECT, which is also a nested data structure.     - agreement\_id: STRING     - email: STRING   - reference\_id: STRING   - resource\_version: INTEGER   - status: STRING   - type: STRING   - updated\_at: DATE-TIME   - upi: OBJECT, which is also a nested data structure.     - vpa: STRING - promotional\_credit: OBJECT, which is also a nested data structure.   - amount: STRING   - amount\_in\_decimal: STRING   - closing\_balance: INTEGER   - created\_at: DATE-TIME   - credit\_type: STRING   - currency\_code: STRING   - customer\_id: STRING   - description: STRING   - done\_by: STRING   - id: STRING   - object: STRING   - reference: STRING   - type: STRING - quote: OBJECT, which is also a nested data structure.   - amount\_due: INTEGER   - amount\_paid: INTEGER   - billing\_address: OBJECT, which is also a nested data structure.     - city: STRING     - company: STRING     - country: STRING     - email: STRING     - first\_name: STRING     - last\_name: STRING     - line1: STRING     - line2: STRING     - line3: STRING     - object: STRING     - phone: STRING     - state: STRING     - state\_code: STRING     - validation\_status: STRING     - zip: STRING   - charge\_on\_acceptance: INTEGER   - contract\_term\_end: DATE-TIME   - contract\_term\_start: DATE-TIME   - contract\_term\_termination\_fee: INTEGER   - credits\_applied: INTEGER   - currency\_code: STRING   - customer\_id: STRING   - date: DATE-TIME   - discounts: ARRAY, which is also a nested data structure.     - amount: INTEGER     - description: STRING     - entity\_id: STRING     - entity\_type: STRING   - id: STRING   - line\_item\_discounts: ARRAY, which is also a nested data structure.     - coupon\_id: STRING     - discount\_amount: INTEGER     - discount\_type: STRING     - entity\_id: STRING     - line\_item\_id: STRING   - line\_item\_taxes: ARRAY, which is also a nested data structure.     - is\_non\_compliance\_tax: BOOLEAN     - is\_partial\_tax\_applied: BOOLEAN     - line\_item\_id: STRING     - local\_currency\_code: STRING     - tax\_amount: INTEGER     - tax\_amount\_in\_local\_currency: INTEGER     - tax\_juris\_code: STRING     - tax\_juris\_name: STRING     - tax\_juris\_type: STRING     - tax\_name: STRING     - tax\_rate: INTEGER, NUMBER     - taxable\_amount: INTEGER   - line\_item\_tiers: ARRAY, which is also a nested data structure.     - ending\_unit: INTEGER     - ending\_unit\_in\_decimal: STRING     - line\_item\_id: STRING     - quantity\_used: INTEGER     - quantity\_used\_in\_decimal: STRING     - starting\_unit: INTEGER     - starting\_unit\_in\_decimal: STRING     - unit\_amount: INTEGER     - unit\_amount\_in\_decimal: STRING   - line\_items: ARRAY, ARRAY, which is also a nested data structure.     - amount: INTEGER     - amount\_in\_decimal: STRING     - customer\_id: STRING     - date\_from: DATE-TIME     - date\_to: DATE-TIME     - description: STRING     - discount\_amount: INTEGER     - entity\_description: STRING     - entity\_id: STRING     - entity\_type: STRING     - id: STRING     - is\_taxed: BOOLEAN     - item\_level\_discount\_amount: INTEGER     - object: STRING     - pricing\_model: STRING     - quantity: INTEGER     - quantity\_in\_decimal: STRING     - subscription\_id: STRING     - tax\_amount: INTEGER     - tax\_exempt\_reason: STRING     - tax\_rate: NUMBER     - unit\_amount: INTEGER     - unit\_amount\_in\_decimal: STRING   - name: STRING   - notes: ARRAY, which is also a nested data structure.   - object: STRING   - operation\_type: STRING   - po\_number: STRING   - price\_type: STRING   - resource\_version: INTEGER   - shipping\_address: OBJECT, which is also a nested data structure.     - city: STRING     - company: STRING     - country: STRING     - email: STRING     - first\_name: STRING     - last\_name: STRING     - line1: STRING     - line2: STRING     - line3: STRING     - object: STRING     - phone: STRING     - state: STRING     - state\_code: STRING     - validation\_status: STRING     - zip: STRING   - status: STRING   - sub\_total: INTEGER   - subscription\_id: STRING   - taxes: ARRAY, which is also a nested data structure.     - amount: INTEGER     - description: STRING     - name: STRING   - total: INTEGER   - total\_payable: INTEGER   - updated\_at: DATE-TIME   - valid\_till: DATE-TIME   - vat\_number: STRING   - vat\_number\_prefix: STRING   - version: INTEGER - subscription: OBJECT, which is also a nested data structure.   - activated\_at: DATE-TIME   - auto\_close\_invoices: BOOLEAN   - auto\_collection: STRING   - base\_currency\_code: STRING   - billing\_period: INTEGER   - billing\_period\_unit: STRING   - cancel\_reason: STRING   - cancel\_reason\_code: STRING   - cancel\_schedule\_created\_at: DATE-TIME   - cancelled\_at: DATE-TIME   - changes\_scheduled\_at: DATE-TIME   - channel: STRING   - charged\_items: ARRAY, which is also a nested data structure.     - item\_price\_id: STRING     - last\_charged\_at: DATE-TIME     - object: STRING   - contract\_term: OBJECT, which is also a nested data structure.     - action\_at\_term\_end: STRING     - billing\_cycle: INTEGER     - cancellation\_cutoff\_period: INTEGER     - contract\_end: DATE-TIME     - contract\_start: DATE-TIME     - created\_at: DATE-TIME     - id: STRING     - remaining\_billing\_cycles: INTEGER     - status: STRING     - subscription\_id: STRING     - total\_contract\_value: INTEGER   - contract\_term\_billing\_cycle\_on\_renewal: INTEGER   - coupon: STRING   - coupons: ARRAY, which is also a nested data structure.     - applied\_count: INTEGER     - apply\_till: DATE-TIME     - coupon\_code: STRING     - coupon\_id: STRING     - object: STRING   - create\_pending\_invoices: BOOLEAN   - created\_at: DATE-TIME   - created\_from\_ip: STRING   - currency\_code: STRING   - current\_term\_end: DATE-TIME   - current\_term\_start: DATE-TIME   - custom\_fields: STRING   - customer\_id: STRING   - deleted: BOOLEAN   - discounts: ARRAY, which is also a nested data structure.     - amount: NUMBER     - applied\_count: INTEGER     - apply\_on: STRING     - apply\_till: INTEGER     - coupon\_id: STRING     - created\_at: INTEGER     - currency\_code: STRING     - duration\_type: STRING     - id: STRING     - included\_in\_mrr: BOOLEAN     - index: INTEGER     - invoice\_name: STRING     - item\_price\_id: STRING     - name: STRING     - object: STRING     - percentage: NUMBER     - period: INTEGER     - period\_unit: STRING     - resource\_version: INTEGER     - type: STRING     - updated\_at: INTEGER   - due\_invoices\_count: INTEGER   - due\_since: DATE-TIME   - exchange\_rate: NUMBER   - free\_period: INTEGER   - free\_period\_unit: STRING   - has\_scheduled\_advance\_invoices: BOOLEAN   - has\_scheduled\_changes: BOOLEAN   - id: STRING   - invoice\_notes: STRING   - item\_tiers: ARRAY, which is also a nested data structure.     - ending\_unit: INTEGER     - ending\_unit\_in\_decimal: STRING     - item\_price\_id: STRING     - price: INTEGER     - price\_in\_decimal: STRING     - starting\_unit: INTEGER     - starting\_unit\_in\_decimal: STRING   - meta\_data: STRING   - mrr: INTEGER   - next\_billing\_at: DATE-TIME   - object: STRING   - override\_relationship: BOOLEAN   - pause\_date: DATE-TIME   - payment\_source\_id: STRING   - plan\_amount\_in\_decimal: STRING   - plan\_free\_quantity\_in\_decimal: STRING   - plan\_quantity\_in\_decimal: STRING   - plan\_unit\_price\_in\_decimal: STRING   - po\_number: STRING   - referral\_info: OBJECT, which is also a nested data structure.     - account\_id: STRING     - campaign\_id: STRING     - coupon\_code: STRING     - destination\_url: STRING     - external\_campaign\_id: STRING     - external\_reference\_id: STRING     - friend\_offer\_type: STRING     - notify\_referral\_system: STRING     - post\_purchase\_widget\_enabled: BOOLEAN     - referral\_code: STRING     - referral\_system: STRING     - referrer\_id: STRING     - referrer\_reward\_type: STRING     - reward\_status: STRING   - remaining\_billing\_cycles: INTEGER   - resource\_version: INTEGER   - resume\_date: DATE-TIME   - shipping\_address: OBJECT, which is also a nested data structure.     - city: STRING     - company: STRING     - country: STRING     - email: STRING     - first\_name: STRING     - last\_name: STRING     - line1: STRING     - line2: STRING     - line3: STRING     - object: STRING     - phone: STRING     - state: STRING     - state\_code: STRING     - validation\_status: STRING     - zip: STRING   - start\_date: DATE-TIME   - started\_at: DATE-TIME   - status: STRING   - subscription\_items: ARRAY, which is also a nested data structure.     - amount: INTEGER     - amount\_in\_decimal: STRING     - billing\_cycles: INTEGER     - charge\_on\_event: STRING     - charge\_on\_option: STRING     - charge\_once: BOOLEAN     - free\_quantity: INTEGER     - free\_quantity\_in\_decimal: STRING     - item\_price\_id: STRING     - item\_type: STRING     - object: STRING     - quantity: INTEGER     - quantity\_in\_decimal: STRING     - service\_period\_days: INTEGER     - trial\_end: DATE-TIME     - unit\_price: INTEGER     - unit\_price\_in\_decimal: STRING   - total\_dues: INTEGER   - trial\_end: DATE-TIME   - trial\_end\_action: STRING   - trial\_start: DATE-TIME   - updated\_at: DATE-TIME - transaction: OBJECT, which is also a nested data structure.   - amount: INTEGER   - amount\_capturable: STRING   - amount\_unused: INTEGER   - authorization\_reason: STRING   - base\_currency\_code: STRING   - currency\_code: STRING   - customer\_id: STRING   - date: DATE-TIME   - deleted: BOOLEAN   - error\_code: STRING   - error\_text: STRING   - exchange\_rate: NUMBER   - fraud\_flag: STRING   - fraud\_reason: STRING   - gateway: STRING   - gateway\_account\_id: STRING   - id: STRING   - id\_at\_gateway: STRING   - iin: STRING   - initiator\_type: STRING   - last4: STRING   - linked\_credit\_notes: ARRAY, which is also a nested data structure.     - applied\_amount: INTEGER     - applied\_at: DATE-TIME     - cn\_create\_reason\_code: STRING     - cn\_date: DATE-TIME     - cn\_id: STRING     - cn\_reason\_code: STRING     - cn\_reference\_invoice\_id: STRING     - cn\_status: STRING     - cn\_total: STRING   - linked\_invoices: ARRAY, which is also a nested data structure.     - applied\_amount: INTEGER     - applied\_at: DATE-TIME     - invoice\_date: DATE-TIME     - invoice\_id: STRING     - invoice\_status: STRING     - invoice\_total: INTEGER   - linked\_payments: ARRAY, which is also a nested data structure.     - amount: INTEGER     - date: DATE-TIME     - id: STRING     - status: STRING   - linked\_refunds: ARRAY, which is also a nested data structure.     - txn\_amount: INTEGER     - txn\_date: DATE-TIME     - txn\_id: STRING     - txn\_status: STRING   - masked\_card\_number: STRING   - merchant\_reference\_id: STRING   - object: STRING   - payment\_method: STRING   - payment\_source\_id: STRING   - reference\_authorization\_id: STRING   - reference\_number: STRING   - reference\_transaction\_id: STRING   - refunded\_txn\_id: STRING   - resource\_version: INTEGER   - reversal\_transaction\_id: STRING   - reversal\_txn\_id: STRING   - settled\_at: DATE-TIME   - status: STRING   - subscription\_id: STRING   - three\_d\_secure: BOOLEAN   - type: STRING   - updated\_at: DATE-TIME   - validated\_at: DATE-TIME   - voided\_at: DATE-TIME - unbilled\_charges: OBJECT, which is also a nested data structure.   - amount: INTEGER   - amount\_in\_decimal: STRING   - currency\_code: STRING   - customer\_id: STRING   - date\_from: DATE-TIME   - date\_to: DATE-TIME   - deleted: BOOLEAN   - description: STRING   - discount\_amount: INTEGER   - entity\_id: STRING   - entity\_type: STRING   - id: STRING   - is\_voided: BOOLEAN   - pricing\_model: STRING   - quantity: INTEGER   - quantity\_in\_decimal: STRING   - subscription\_id: STRING   - tiers: ARRAY, which is also a nested data structure.     - ending\_unit: INTEGER     - ending\_unit\_in\_decimal: STRING     - quantity\_used: INTEGER     - quantity\_used\_in\_decimal: STRING     - starting\_unit: INTEGER     - starting\_unit\_in\_decimal: STRING     - unit\_amount: INTEGER     - unit\_amount\_in\_decimal: STRING   - unit\_amount: INTEGER   - unit\_amount\_in\_decimal: STRING   - voided\_at: DATE-TIME - virtual\_bank\_account: OBJECT, which is also a nested data structure.   - account\_number: STRING   - bank\_name: STRING   - created\_at: DATE-TIME   - customer\_id: STRING   - deleted: BOOLEAN   - email: STRING   - gateway: STRING   - gateway\_account\_id: STRING   - id: STRING   - object: STRING   - reference\_id: STRING   - resource\_version: INTEGER   - routing\_number: STRING   - scheme: STRING   - swift\_code: STRING   - updated\_at: DATE-TIME |
| **event\_type**  STRING |
| **id**  STRING |
| **object**  STRING |
| **occurred\_at**  DATE-TIME |
| **source**  STRING |
| **user**  STRING |
| **webhook\_status**  STRING |

### gifts

The `gifts` table contains info about the gifts in your Chargebee account.

**Note**: This table is available Refer to the [Table and field availability and Chargebee Product Catalogs section](#product-catalog-versions) for more info.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Chargebee documentation](https://apidocs.chargebee.com/Content/api/gifts)  [Chargebee API method](https://apidocs.chargebee.com/Content/api/gifts#list_gifts "Opens in new tab: Chargebee API method") |

gifts table foreign keys

| Join gifts with | on |
| --- | --- |
| [credit\_notes](#credit-notes) | ``` gifts.gift_receiver.customer_id = credit_notes.customer_id ```  ``` gifts.gifter.customer_id = credit_notes.customer_id ```  ``` gifts.gifter.invoice_id = credit_notes.allocations.invoice_id ```  ``` gifts.gifter.invoice_id = credit_notes.reference_invoice_id ```  ``` gifts.gift_receiver.subscription_id = credit_notes.subscription_id ```  ``` gifts.gift_receiver.subscription_id = credit_notes.line_items.subscription_id ``` |
| [customers](#customers) | ``` gifts.gift_receiver.customer_id = customers.id ```  ``` gifts.gifter.customer_id = customers.id ``` |
| [events](#events) | ``` gifts.gift_receiver.customer_id = events.content.customer.id ```  ``` gifts.gifter.customer_id = events.content.customer.id ```  ``` gifts.gift_receiver.customer_id = events.content.invoice.customer_id ```  ``` gifts.gifter.customer_id = events.content.invoice.customer_id ```  ``` gifts.gift_receiver.customer_id = events.content.subscription.customer_id ```  ``` gifts.gifter.customer_id = events.content.subscription.customer_id ```  ``` gifts.gift_receiver.customer_id = events.content.transaction.customer_id ```  ``` gifts.gifter.customer_id = events.content.transaction.customer_id ```  ``` gifts.gifter.invoice_id = events.content.invoice.id ```  ``` gifts.gifter.invoice_id = events.content.transaction.linked_credit_notes.cn_reference_invoice_id ```  ``` gifts.gift_receiver.subscription_id = events.content.subscription.id ```  ``` gifts.gift_receiver.subscription_id = events.content.invoice.subscription_id ```  ``` gifts.gift_receiver.subscription_id = events.content.transaction.subscription_id ``` |
| [invoices](#invoices) | ``` gifts.gift_receiver.customer_id = invoices.customer_id ```  ``` gifts.gifter.customer_id = invoices.customer_id ```  ``` gifts.gift_receiver.customer_id = invoices.notes.entity_id ```  ``` gifts.gifter.customer_id = invoices.notes.entity_id ```  ``` gifts.gifter.invoice_id = invoices.id ```  ``` gifts.gift_receiver.subscription_id = invoices.line_items.subscription_id ```  ``` gifts.gift_receiver.subscription_id = invoices.notes.entity_id ```  ``` gifts.gift_receiver.subscription_id = invoices.subscription_id ``` |
| [payment\_sources](#payment-sources) | ``` gifts.gift_receiver.customer_id = payment_sources.customer_id ```  ``` gifts.gifter.customer_id = payment_sources.customer_id ``` |
| [promotional\_credits](#promotional-credits) | ``` gifts.gift_receiver.customer_id = promotional_credits.customer_id ```  ``` gifts.gifter.customer_id = promotional_credits.customer_id ``` |
| [subscriptions](#subscriptions) | ``` gifts.gift_receiver.customer_id = subscriptions.customer_id ```  ``` gifts.gifter.customer_id = subscriptions.customer_id ```  ``` gifts.id = subscriptions.gift_id ```  ``` gifts.gift_receiver.subscription_id = subscriptions.id ``` |
| [transactions](#transactions) | ``` gifts.gift_receiver.customer_id = transactions.customer_id ```  ``` gifts.gifter.customer_id = transactions.customer_id ```  ``` gifts.gifter.invoice_id = transactions.linked_credit_notes.cn_reference_invoice_id ```  ``` gifts.gift_receiver.subscription_id = transactions.subscription_id ``` |
| [virtual\_bank\_accounts](#virtual-bank-accounts) | ``` gifts.gift_receiver.customer_id = virtual_bank_accounts.customer_id ```  ``` gifts.gifter.customer_id = virtual_bank_accounts.customer_id ``` |
| [orders](#orders) | ``` gifts.gift_receiver.customer_id = orders.customer_id ```  ``` gifts.gifter.customer_id = orders.customer_id ```  ``` gifts.id = orders.gift_id ```  ``` gifts.gifter.invoice_id = orders.invoice_id ```  ``` gifts.gift_receiver.subscription_id = orders.subscription_id ``` |

gifts table schema

|  |
| --- |
| **auto\_claim**  BOOLEAN |
| **claim\_expiry\_date**  DATE-TIME |
| **gift\_receiver**  OBJECT This is a nested data structure:   - customer\_id: STRING - email: STRING - first\_name: STRING - last\_name: STRING - subscription\_id: STRING |
| **gift\_timelines**  ARRAY This is a nested data structure:   - occurred\_at: DATE-TIME - status: STRING |
| **gifter**  OBJECT This is a nested data structure:   - customer\_id: STRING - invoice\_id: STRING - note: STRING - signature: STRING |
| **id**  STRING |
| **no\_expiry**  BOOLEAN |
| **resource\_version**  INTEGER |
| **scheduled\_at**  DATE-TIME |
| **status**  STRING |
| **updated\_at**  DATE-TIME |

### invoices

The `invoices` table contains info about the invoices in your Chargebee account. Invoices are statements containing charges, adjustments, and any discounts for a subscription specific to a term.

**Note**: This table is available Refer to the [Table and field availability and Chargebee Product Catalogs section](#product-catalog-versions) for more info.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Chargebee documentation](https://apidocs.chargebee.com/Content/api/invoices)  [Chargebee API method](https://apidocs.chargebee.com/Content/api/invoices#list_invoices "Opens in new tab: Chargebee API method") |

invoices table foreign keys

| Join invoices with | on |
| --- | --- |
| [addons](#addons) | ``` invoices.notes.entity_id = addons.id ``` |
| [coupons](#coupons) | ``` invoices.notes.entity_id = coupons.addon_ids ```  ``` invoices.discounts.entity_id = coupons.id ```  ``` invoices.line_item_discounts.coupon_id = coupons.id ```  ``` invoices.notes.entity_id = coupons.id ```  ``` invoices.notes.entity_id = coupons.plan_ids ``` |
| [events](#events) | ``` invoices.notes.entity_id = events.content.subscription.addons.id ```  ``` invoices.notes.entity_id = events.content.subscription.charged_event_based_addons.id ```  ``` invoices.notes.entity_id = events.content.subscription.event_based_addons.id ```  ``` invoices.discounts.entity_id = events.content.coupon.id ```  ``` invoices.line_item_discounts.coupon_id = events.content.coupon.id ```  ``` invoices.notes.entity_id = events.content.coupon.id ```  ``` invoices.discounts.entity_id = events.content.invoice.discounts.entity_id ```  ``` invoices.line_item_discounts.coupon_id = events.content.invoice.discounts.entity_id ```  ``` invoices.notes.entity_id = events.content.invoice.discounts.entity_id ```  ``` invoices.discounts.entity_id = events.content.invoice.line_item_discounts.coupon_id ```  ``` invoices.line_item_discounts.coupon_id = events.content.invoice.line_item_discounts.coupon_id ```  ``` invoices.notes.entity_id = events.content.invoice.line_item_discounts.coupon_id ```  ``` invoices.discounts.entity_id = events.content.subscription.coupons.coupon_id ```  ``` invoices.line_item_discounts.coupon_id = events.content.subscription.coupons.coupon_id ```  ``` invoices.notes.entity_id = events.content.subscription.coupons.coupon_id ```  ``` invoices.adjustment_credit_notes.cn_id = events.content.invoice.adjustment_credit_notes.cn_id ```  ``` invoices.applied_credits.cn_id = events.content.invoice.adjustment_credit_notes.cn_id ```  ``` invoices.issued_credit_notes.cn_id = events.content.invoice.adjustment_credit_notes.cn_id ```  ``` invoices.adjustment_credit_notes.cn_id = events.content.invoice.applied_credits.cn_id ```  ``` invoices.applied_credits.cn_id = events.content.invoice.applied_credits.cn_id ```  ``` invoices.issued_credit_notes.cn_id = events.content.invoice.applied_credits.cn_id ```  ``` invoices.adjustment_credit_notes.cn_id = events.content.invoice.issued_credit_notes.cn_id ```  ``` invoices.applied_credits.cn_id = events.content.invoice.issued_credit_notes.cn_id ```  ``` invoices.issued_credit_notes.cn_id = events.content.invoice.issued_credit_notes.cn_id ```  ``` invoices.customer_id = events.content.customer.id ```  ``` invoices.notes.entity_id = events.content.customer.id ```  ``` invoices.customer_id = events.content.invoice.customer_id ```  ``` invoices.notes.entity_id = events.content.invoice.customer_id ```  ``` invoices.customer_id = events.content.subscription.customer_id ```  ``` invoices.notes.entity_id = events.content.subscription.customer_id ```  ``` invoices.customer_id = events.content.transaction.customer_id ```  ``` invoices.notes.entity_id = events.content.transaction.customer_id ```  ``` invoices.id = events.content.invoice.id ```  ``` invoices.id = events.content.transaction.linked_credit_notes.cn_reference_invoice_id ```  ``` invoices.line_item_discounts.line_item_id = events.content.invoice.line_item_discounts.line_item_id ```  ``` invoices.line_item_taxes.line_item_id = events.content.invoice.line_item_discounts.line_item_id ```  ``` invoices.line_item_tiers.line_item_id = events.content.invoice.line_item_discounts.line_item_id ```  ``` invoices.line_items.id = events.content.invoice.line_item_discounts.line_item_id ```  ``` invoices.line_item_discounts.line_item_id = events.content.invoice.line_item_taxes.line_item_id ```  ``` invoices.line_item_taxes.line_item_id = events.content.invoice.line_item_taxes.line_item_id ```  ``` invoices.line_item_tiers.line_item_id = events.content.invoice.line_item_taxes.line_item_id ```  ``` invoices.line_items.id = events.content.invoice.line_item_taxes.line_item_id ```  ``` invoices.line_item_discounts.line_item_id = events.content.invoice.line_items.id ```  ``` invoices.line_item_taxes.line_item_id = events.content.invoice.line_items.id ```  ``` invoices.line_item_tiers.line_item_id = events.content.invoice.line_items.id ```  ``` invoices.line_items.id = events.content.invoice.line_items.id ```  ``` invoices.notes.entity_id = events.content.coupon.plan_ids ```  ``` invoices.notes.entity_id = events.content.subscription.plan_id ```  ``` invoices.line_items.subscription_id = events.content.subscription.id ```  ``` invoices.notes.entity_id = events.content.subscription.id ```  ``` invoices.subscription_id = events.content.subscription.id ```  ``` invoices.line_items.subscription_id = events.content.invoice.subscription_id ```  ``` invoices.notes.entity_id = events.content.invoice.subscription_id ```  ``` invoices.subscription_id = events.content.invoice.subscription_id ```  ``` invoices.line_items.subscription_id = events.content.transaction.subscription_id ```  ``` invoices.notes.entity_id = events.content.transaction.subscription_id ```  ``` invoices.subscription_id = events.content.transaction.subscription_id ```  ``` invoices.linked_payments.txn_id = events.content.invoice.linked_payments.txn_id ```  ``` invoices.linked_payments.txn_id = events.content.transaction.id ```  ``` invoices.linked_payments.txn_id = events.content.transaction.linked_refunds.txn_id ```  ``` invoices.linked_payments.txn_id = events.content.transaction.reference_transaction_id ```  ``` invoices.linked_payments.txn_id = events.content.transaction.refunded_txn_id ``` |
| [plans](#plans) | ``` invoices.notes.entity_id = plans.applicable_addons.id ```  ``` invoices.notes.entity_id = plans.id ``` |
| [subscriptions](#subscriptions) | ``` invoices.notes.entity_id = subscriptions.addons.id ```  ``` invoices.notes.entity_id = subscriptions.charged_event_based_addons.id ```  ``` invoices.notes.entity_id = subscriptions.event_based_addons.id ```  ``` invoices.discounts.entity_id = subscriptions.coupons.coupon_id ```  ``` invoices.line_item_discounts.coupon_id = subscriptions.coupons.coupon_id ```  ``` invoices.notes.entity_id = subscriptions.coupons.coupon_id ```  ``` invoices.customer_id = subscriptions.customer_id ```  ``` invoices.notes.entity_id = subscriptions.customer_id ```  ``` invoices.notes.entity_id = subscriptions.plan_id ```  ``` invoices.line_items.subscription_id = subscriptions.id ```  ``` invoices.notes.entity_id = subscriptions.id ```  ``` invoices.subscription_id = subscriptions.id ``` |
| [credit\_notes](#credit-notes) | ``` invoices.discounts.entity_id = credit_notes.discounts.entity_id ```  ``` invoices.line_item_discounts.coupon_id = credit_notes.discounts.entity_id ```  ``` invoices.notes.entity_id = credit_notes.discounts.entity_id ```  ``` invoices.discounts.entity_id = credit_notes.line_item_discounts.coupon_id ```  ``` invoices.line_item_discounts.coupon_id = credit_notes.line_item_discounts.coupon_id ```  ``` invoices.notes.entity_id = credit_notes.line_item_discounts.coupon_id ```  ``` invoices.adjustment_credit_notes.cn_id = credit_notes.id ```  ``` invoices.applied_credits.cn_id = credit_notes.id ```  ``` invoices.issued_credit_notes.cn_id = credit_notes.id ```  ``` invoices.customer_id = credit_notes.customer_id ```  ``` invoices.notes.entity_id = credit_notes.customer_id ```  ``` invoices.id = credit_notes.allocations.invoice_id ```  ``` invoices.id = credit_notes.reference_invoice_id ```  ``` invoices.line_item_discounts.line_item_id = credit_notes.line_item_discounts.line_item_id ```  ``` invoices.line_item_taxes.line_item_id = credit_notes.line_item_discounts.line_item_id ```  ``` invoices.line_item_tiers.line_item_id = credit_notes.line_item_discounts.line_item_id ```  ``` invoices.line_items.id = credit_notes.line_item_discounts.line_item_id ```  ``` invoices.line_item_discounts.line_item_id = credit_notes.line_item_taxes.line_item_id ```  ``` invoices.line_item_taxes.line_item_id = credit_notes.line_item_taxes.line_item_id ```  ``` invoices.line_item_tiers.line_item_id = credit_notes.line_item_taxes.line_item_id ```  ``` invoices.line_items.id = credit_notes.line_item_taxes.line_item_id ```  ``` invoices.line_item_discounts.line_item_id = credit_notes.line_item_tiers.line_item_id ```  ``` invoices.line_item_taxes.line_item_id = credit_notes.line_item_tiers.line_item_id ```  ``` invoices.line_item_tiers.line_item_id = credit_notes.line_item_tiers.line_item_id ```  ``` invoices.line_items.id = credit_notes.line_item_tiers.line_item_id ```  ``` invoices.line_item_discounts.line_item_id = credit_notes.line_items.id ```  ``` invoices.line_item_taxes.line_item_id = credit_notes.line_items.id ```  ``` invoices.line_item_tiers.line_item_id = credit_notes.line_items.id ```  ``` invoices.line_items.id = credit_notes.line_items.id ```  ``` invoices.line_items.subscription_id = credit_notes.subscription_id ```  ``` invoices.notes.entity_id = credit_notes.subscription_id ```  ``` invoices.subscription_id = credit_notes.subscription_id ```  ``` invoices.line_items.subscription_id = credit_notes.line_items.subscription_id ```  ``` invoices.notes.entity_id = credit_notes.line_items.subscription_id ```  ``` invoices.subscription_id = credit_notes.line_items.subscription_id ```  ``` invoices.linked_payments.txn_id = credit_notes.linked_refunds.txn_id ``` |
| [orders](#orders) | ``` invoices.discounts.entity_id = orders.line_item_discounts.coupon_id ```  ``` invoices.line_item_discounts.coupon_id = orders.line_item_discounts.coupon_id ```  ``` invoices.notes.entity_id = orders.line_item_discounts.coupon_id ```  ``` invoices.adjustment_credit_notes.cn_id = orders.linked_credit_notes.id ```  ``` invoices.applied_credits.cn_id = orders.linked_credit_notes.id ```  ``` invoices.issued_credit_notes.cn_id = orders.linked_credit_notes.id ```  ``` invoices.customer_id = orders.customer_id ```  ``` invoices.notes.entity_id = orders.customer_id ```  ``` invoices.id = orders.invoice_id ```  ``` invoices.line_item_discounts.line_item_id = orders.line_item_discounts.line_item_id ```  ``` invoices.line_item_taxes.line_item_id = orders.line_item_discounts.line_item_id ```  ``` invoices.line_item_tiers.line_item_id = orders.line_item_discounts.line_item_id ```  ``` invoices.line_items.id = orders.line_item_discounts.line_item_id ```  ``` invoices.line_item_discounts.line_item_id = orders.line_item_taxes.line_item_id ```  ``` invoices.line_item_taxes.line_item_id = orders.line_item_taxes.line_item_id ```  ``` invoices.line_item_tiers.line_item_id = orders.line_item_taxes.line_item_id ```  ``` invoices.line_items.id = orders.line_item_taxes.line_item_id ```  ``` invoices.line_items.subscription_id = orders.subscription_id ```  ``` invoices.notes.entity_id = orders.subscription_id ```  ``` invoices.subscription_id = orders.subscription_id ```  ``` invoices.linked_orders.id = orders.id ``` |
| [customers](#customers) | ``` invoices.customer_id = customers.id ```  ``` invoices.notes.entity_id = customers.id ``` |
| [payment\_sources](#payment-sources) | ``` invoices.customer_id = payment_sources.customer_id ```  ``` invoices.notes.entity_id = payment_sources.customer_id ``` |
| [promotional\_credits](#promotional-credits) | ``` invoices.customer_id = promotional_credits.customer_id ```  ``` invoices.notes.entity_id = promotional_credits.customer_id ``` |
| [transactions](#transactions) | ``` invoices.customer_id = transactions.customer_id ```  ``` invoices.notes.entity_id = transactions.customer_id ```  ``` invoices.id = transactions.linked_credit_notes.cn_reference_invoice_id ```  ``` invoices.line_items.subscription_id = transactions.subscription_id ```  ``` invoices.notes.entity_id = transactions.subscription_id ```  ``` invoices.subscription_id = transactions.subscription_id ```  ``` invoices.linked_payments.txn_id = transactions.id ```  ``` invoices.linked_payments.txn_id = transactions.linked_refunds.txn_id ```  ``` invoices.linked_payments.txn_id = transactions.reference_transaction_id ```  ``` invoices.linked_payments.txn_id = transactions.refunded_txn_id ``` |
| [virtual\_bank\_accounts](#virtual-bank-accounts) | ``` invoices.customer_id = virtual_bank_accounts.customer_id ```  ``` invoices.notes.entity_id = virtual_bank_accounts.customer_id ``` |
| [gifts](#gifts) | ``` invoices.customer_id = gifts.gift_receiver.customer_id ```  ``` invoices.notes.entity_id = gifts.gift_receiver.customer_id ```  ``` invoices.customer_id = gifts.gifter.customer_id ```  ``` invoices.notes.entity_id = gifts.gifter.customer_id ```  ``` invoices.id = gifts.gifter.invoice_id ```  ``` invoices.line_items.subscription_id = gifts.gift_receiver.subscription_id ```  ``` invoices.notes.entity_id = gifts.gift_receiver.subscription_id ```  ``` invoices.subscription_id = gifts.gift_receiver.subscription_id ``` |

invoices table schema

|  |
| --- |
| **adjustment\_credit\_notes**  ARRAY This is a nested data structure:   - cn\_create\_reason\_code: STRING - cn\_date: DATE-TIME - cn\_id: STRING - cn\_reason\_code: STRING - cn\_status: STRING - cn\_total: INTEGER |
| **amount\_adjusted**  INTEGER |
| **amount\_due**  INTEGER |
| **amount\_paid**  INTEGER |
| **amount\_to\_collect**  INTEGER |
| **applied\_credits**  ARRAY This is a nested data structure:   - applied\_amount: INTEGER - applied\_at: DATE-TIME - cn\_create\_reason\_code: STRING - cn\_date: DATE-TIME - cn\_id: STRING - cn\_reason\_code: STRING - cn\_status: STRING |
| **base\_currency\_code**  STRING |
| **billing\_address**  OBJECT This is a nested data structure:   - city: STRING - company: STRING - country: STRING - email: STRING - first\_name: STRING - last\_name: STRING - line1: STRING - line2: STRING - line3: STRING - object: STRING - phone: STRING - state: STRING - state\_code: STRING - validation\_status: STRING - zip: STRING |
| **channel**  STRING |
| **credits\_applied**  INTEGER |
| **currency\_code**  STRING |
| **customer\_id**  STRING |
| **date**  DATE-TIME |
| **deleted**  BOOLEAN |
| **discounts**  ARRAY This is a nested data structure:   - amount: INTEGER - description: STRING - entity\_id: STRING - entity\_type: STRING - object: STRING |
| **due\_date**  DATE-TIME |
| **dunning\_attempts**  ARRAY This is a nested data structure:   - attempt: INTEGER - created\_at: DATE-TIME - dunning\_type: STRING - transaction\_id: STRING - txn\_amount: INTEGER - txn\_status: STRING |
| **dunning\_status**  STRING |
| **einvoice**  OBJECT This is a nested data structure:   - id: STRING - message: STRING - status: STRING |
| **exchange\_rate**  NUMBER |
| **expected\_payment\_date**  DATE-TIME |
| **first\_invoice**  BOOLEAN |
| **generated\_at**  DATE-TIME |
| **has\_advance\_charges**  BOOLEAN |
| **id**  STRING |
| **is\_gifted**  BOOLEAN |
| **issued\_credit\_notes**  ARRAY This is a nested data structure:   - cn\_create\_reason\_code: STRING - cn\_date: DATE-TIME - cn\_id: STRING - cn\_reason\_code: STRING - cn\_status: STRING - cn\_total: INTEGER |
| **line\_item\_discounts**  ARRAY This is a nested data structure:   - coupon\_id: STRING - discount\_amount: INTEGER - discount\_type: STRING - entity\_id: STRING - line\_item\_id: STRING - object: STRING |
| **line\_item\_taxes**  ARRAY This is a nested data structure:   - is\_non\_compliance\_tax: BOOLEAN - is\_partial\_tax\_applied: BOOLEAN - line\_item\_id: STRING - local\_currency\_code: STRING - tax\_amount: INTEGER - tax\_amount\_in\_local\_currency: INTEGER - tax\_juris\_code: STRING - tax\_juris\_name: STRING - tax\_juris\_type: STRING - tax\_name: STRING - tax\_rate: INTEGER, NUMBER - taxable\_amount: INTEGER |
| **line\_item\_tiers**  ARRAY This is a nested data structure:   - ending\_unit: INTEGER - ending\_unit\_in\_decimal: STRING - line\_item\_id: STRING - quantity\_used: INTEGER - quantity\_used\_in\_decimal: STRING - starting\_unit: INTEGER - starting\_unit\_in\_decimal: STRING - unit\_amount: INTEGER - unit\_amount\_in\_decimal: STRING |
| **line\_items**  ARRAY This is a nested data structure:   - amount: INTEGER - amount\_in\_decimal: STRING - customer\_id: STRING - date\_from: DATE-TIME - date\_to: DATE-TIME - description: STRING - discount\_amount: INTEGER - entity\_description: STRING - entity\_id: STRING - entity\_type: STRING - id: STRING - is\_taxed: BOOLEAN - item\_level\_discount\_amount: INTEGER - object: STRING - pricing\_model: STRING - quantity: INTEGER - quantity\_in\_decimal: STRING - subscription\_id: STRING - tax\_amount: INTEGER - tax\_exempt\_reason: STRING - tax\_rate: NUMBER - unit\_amount: INTEGER - unit\_amount\_in\_decimal: STRING |
| **linked\_orders**  ARRAY This is a nested data structure:   - batch\_id: STRING - created\_at: DATE-TIME - document\_number: STRING - fulfillment\_status: STRING - id: STRING - order\_type: STRING - reference\_id: STRING - status: STRING |
| **linked\_payments**  ARRAY This is a nested data structure:   - applied\_amount: INTEGER - applied\_at: DATE-TIME - txn\_amount: INTEGER - txn\_date: DATE-TIME - txn\_id: STRING - txn\_status: STRING |
| **local\_currency\_code**  STRING |
| **net\_term\_days**  INTEGER |
| **new\_sales\_amount**  INTEGER |
| **next\_retry\_at**  DATE-TIME |
| **notes**  ARRAY This is a nested data structure:   - entity\_id: STRING - entity\_type: STRING - note: STRING |
| **object**  STRING |
| **paid\_at**  DATE-TIME |
| **payment\_owner**  STRING |
| **po\_number**  STRING |
| **price\_type**  STRING |
| **recurring**  BOOLEAN |
| **resource\_version**  INTEGER |
| **round\_off\_amount**  INTEGER |
| **shipping\_address**  OBJECT This is a nested data structure:   - city: STRING - company: STRING - country: STRING - email: STRING - first\_name: STRING - last\_name: STRING - line1: STRING - line2: STRING - line3: STRING - object: STRING - phone: STRING - state: STRING - state\_code: STRING - validation\_status: STRING - zip: STRING |
| **status**  STRING |
| **sub\_total**  INTEGER |
| **sub\_total\_in\_local\_currency**  INTEGER |
| **subscription\_id**  STRING |
| **tax**  INTEGER |
| **taxes**  ARRAY This is a nested data structure:   - amount: INTEGER - description: STRING - name: STRING |
| **term\_finalized**  BOOLEAN |
| **total**  INTEGER |
| **total\_in\_local\_currency**  INTEGER |
| **updated\_at**  DATE-TIME |
| **vat\_number**  STRING |
| **vat\_number\_prefix**  STRING |
| **void\_reason\_code**  STRING |
| **voided\_at**  DATE-TIME |
| **write\_off\_amount**  INTEGER |

### item\_families

The `item_families` table contains info about item families.

**Note**: This table is available Refer to the [Table and field availability and Chargebee Product Catalogs section](#product-catalog-versions) for more info.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Chargebee API method](https://apidocs.chargebee.com/Content/api/item_families?prod_cat_ver=2#list_item_families "Opens in new tab: Chargebee API method") |

item\_families table foreign keys

| Join item\_families with | on |
| --- | --- |
| [item\_prices](#item-prices) | ``` item_families.id = item_prices.item_family_id ``` |
| [items](#items) | ``` item_families.id = items.item_family_id ``` |

item\_families table schema

|  |
| --- |
| **channel**  STRING |
| **custom\_fields**  STRING |
| **description**  STRING |
| **id**  STRING |
| **name**  STRING |
| **object**  STRING |
| **resource\_version**  INTEGER |
| **status**  STRING |
| **updated\_at**  DATE-TIME |

### item\_prices

The `item_prices` table contains info about item prices.

**Note**: This table is available Refer to the [Table and field availability and Chargebee Product Catalogs section](#product-catalog-versions) for more info.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Chargebee API method](https://apidocs.chargebee.com/Content/api/item_prices?prod_cat_ver=2#list_item_prices "Opens in new tab: Chargebee API method") |

item\_prices table foreign keys

| Join item\_prices with | on |
| --- | --- |
| [item\_families](#item-families) | ``` item_prices.item_family_id = item_families.id ``` |
| [items](#items) | ``` item_prices.item_family_id = items.item_family_id ```  ``` item_prices.item_id = items.id ``` |

item\_prices table schema

|  |
| --- |
| **accounting\_detail**  OBJECT This is a nested data structure:   - accounting\_category1: STRING - accounting\_category2: STRING - accounting\_category3: STRING - accounting\_category4: STRING - accounting\_code: STRING - sku: STRING |
| **archivable**  BOOLEAN, STRING |
| **archived\_at**  DATE-TIME |
| **billing\_cycles**  INTEGER |
| **channel**  STRING |
| **created\_at**  DATE-TIME |
| **currency\_code**  STRING |
| **custom\_fields**  STRING |
| **description**  STRING |
| **external\_name**  STRING |
| **free\_quantity**  INTEGER |
| **free\_quantity\_in\_decimal**  STRING |
| **id**  STRING |
| **invoice\_notes**  STRING |
| **is\_taxable**  BOOLEAN |
| **item\_family\_id**  STRING |
| **item\_id**  STRING |
| **item\_type**  STRING |
| **metadata**  STRING |
| **name**  STRING |
| **object**  STRING |
| **period**  INTEGER |
| **period\_unit**  STRING |
| **price**  INTEGER |
| **price\_in\_decimal**  STRING |
| **pricing\_model**  STRING |
| **resource\_version**  INTEGER |
| **shipping\_period**  INTEGER |
| **shipping\_period\_unit**  STRING |
| **show\_description\_in\_invoices**  BOOLEAN |
| **show\_description\_in\_quotes**  BOOLEAN |
| **status**  STRING |
| **tax\_detail**  OBJECT This is a nested data structure:   - avalara\_sale\_type: STRING - avalara\_service\_type: INTEGER - avalara\_tax\_code: STRING - avalara\_transaction\_type: INTEGER - tax\_profile\_id: STRING - taxjar\_product\_code: STRING |
| **tiers**  ARRAY This is a nested data structure:   - ending\_unit: INTEGER - price: INTEGER - starting\_unit: INTEGER |
| **trial\_end\_action**  STRING |
| **trial\_period**  INTEGER |
| **trial\_period\_unit**  STRING |
| **updated\_at**  DATE-TIME |

### items

The `items` table contains info about the items in your Chargebee account.

**Note**: This table is available Refer to the [Table and field availability and Chargebee Product Catalogs section](#product-catalog-versions) for more info.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Chargebee API method](https://apidocs.chargebee.com/Content/api/items?prod_cat_ver=2#list_items "Opens in new tab: Chargebee API method") |

items table foreign keys

| Join items with | on |
| --- | --- |
| [item\_families](#item-families) | ``` items.item_family_id = item_families.id ``` |
| [item\_prices](#item-prices) | ``` items.item_family_id = item_prices.item_family_id ```  ``` items.id = item_prices.item_id ``` |

items table schema

|  |
| --- |
| **applicable\_items**  ARRAY This is a nested data structure:   - id: STRING |
| **archivable**  BOOLEAN, STRING |
| **archived\_at**  DATE-TIME |
| **channel**  STRING |
| **custom\_fields**  STRING |
| **description**  STRING |
| **enabled\_for\_checkout**  BOOLEAN |
| **enabled\_in\_portal**  BOOLEAN |
| **external\_name**  STRING |
| **gift\_claim\_redirect\_url**  STRING |
| **id**  STRING |
| **included\_in\_mrr**  BOOLEAN |
| **is\_giftable**  BOOLEAN |
| **is\_shippable**  BOOLEAN |
| **item\_applicability**  STRING |
| **item\_family\_id**  STRING |
| **metadata**  STRING |
| **metered**  BOOLEAN |
| **name**  STRING |
| **object**  STRING |
| **redirect\_url**  STRING |
| **resource\_version**  INTEGER |
| **status**  STRING |
| **type**  STRING |
| **unit**  STRING |
| **updated\_at**  DATE-TIME |
| **usage\_calculation**  STRING |

### orders

The `orders` table contains info about the orders in your Chargebee account. The **Order Management** feature must be enabled to replicate this table. For more information, refer to the [Chargebee docs](https://www.chargebee.com/Content/orders.html).

**Note**: This table is available Refer to the [Table and field availability and Chargebee Product Catalogs section](#product-catalog-versions) for more info.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Chargebee documentation](https://apidocs.chargebee.com/Content/api/orders)  [Chargebee API method](https://apidocs.chargebee.com/Content/api/orders#list_orders "Opens in new tab: Chargebee API method") |

orders table foreign keys

| Join orders with | on |
| --- | --- |
| [coupons](#coupons) | ``` orders.line_item_discounts.coupon_id = coupons.id ``` |
| [credit\_notes](#credit-notes) | ``` orders.line_item_discounts.coupon_id = credit_notes.discounts.entity_id ```  ``` orders.line_item_discounts.coupon_id = credit_notes.line_item_discounts.coupon_id ```  ``` orders.linked_credit_notes.id = credit_notes.id ```  ``` orders.customer_id = credit_notes.customer_id ```  ``` orders.invoice_id = credit_notes.allocations.invoice_id ```  ``` orders.invoice_id = credit_notes.reference_invoice_id ```  ``` orders.line_item_discounts.line_item_id = credit_notes.line_item_discounts.line_item_id ```  ``` orders.line_item_taxes.line_item_id = credit_notes.line_item_discounts.line_item_id ```  ``` orders.line_item_discounts.line_item_id = credit_notes.line_item_taxes.line_item_id ```  ``` orders.line_item_taxes.line_item_id = credit_notes.line_item_taxes.line_item_id ```  ``` orders.line_item_discounts.line_item_id = credit_notes.line_item_tiers.line_item_id ```  ``` orders.line_item_taxes.line_item_id = credit_notes.line_item_tiers.line_item_id ```  ``` orders.line_item_discounts.line_item_id = credit_notes.line_items.id ```  ``` orders.line_item_taxes.line_item_id = credit_notes.line_items.id ```  ``` orders.subscription_id = credit_notes.subscription_id ```  ``` orders.subscription_id = credit_notes.line_items.subscription_id ``` |
| [events](#events) | ``` orders.line_item_discounts.coupon_id = events.content.coupon.id ```  ``` orders.line_item_discounts.coupon_id = events.content.invoice.discounts.entity_id ```  ``` orders.line_item_discounts.coupon_id = events.content.invoice.line_item_discounts.coupon_id ```  ``` orders.line_item_discounts.coupon_id = events.content.subscription.coupons.coupon_id ```  ``` orders.linked_credit_notes.id = events.content.invoice.adjustment_credit_notes.cn_id ```  ``` orders.linked_credit_notes.id = events.content.invoice.applied_credits.cn_id ```  ``` orders.linked_credit_notes.id = events.content.invoice.issued_credit_notes.cn_id ```  ``` orders.customer_id = events.content.customer.id ```  ``` orders.customer_id = events.content.invoice.customer_id ```  ``` orders.customer_id = events.content.subscription.customer_id ```  ``` orders.customer_id = events.content.transaction.customer_id ```  ``` orders.invoice_id = events.content.invoice.id ```  ``` orders.invoice_id = events.content.transaction.linked_credit_notes.cn_reference_invoice_id ```  ``` orders.line_item_discounts.line_item_id = events.content.invoice.line_item_discounts.line_item_id ```  ``` orders.line_item_taxes.line_item_id = events.content.invoice.line_item_discounts.line_item_id ```  ``` orders.line_item_discounts.line_item_id = events.content.invoice.line_item_taxes.line_item_id ```  ``` orders.line_item_taxes.line_item_id = events.content.invoice.line_item_taxes.line_item_id ```  ``` orders.line_item_discounts.line_item_id = events.content.invoice.line_items.id ```  ``` orders.line_item_taxes.line_item_id = events.content.invoice.line_items.id ```  ``` orders.subscription_id = events.content.subscription.id ```  ``` orders.subscription_id = events.content.invoice.subscription_id ```  ``` orders.subscription_id = events.content.transaction.subscription_id ``` |
| [invoices](#invoices) | ``` orders.line_item_discounts.coupon_id = invoices.discounts.entity_id ```  ``` orders.line_item_discounts.coupon_id = invoices.line_item_discounts.coupon_id ```  ``` orders.line_item_discounts.coupon_id = invoices.notes.entity_id ```  ``` orders.linked_credit_notes.id = invoices.adjustment_credit_notes.cn_id ```  ``` orders.linked_credit_notes.id = invoices.applied_credits.cn_id ```  ``` orders.linked_credit_notes.id = invoices.issued_credit_notes.cn_id ```  ``` orders.customer_id = invoices.customer_id ```  ``` orders.customer_id = invoices.notes.entity_id ```  ``` orders.invoice_id = invoices.id ```  ``` orders.line_item_discounts.line_item_id = invoices.line_item_discounts.line_item_id ```  ``` orders.line_item_taxes.line_item_id = invoices.line_item_discounts.line_item_id ```  ``` orders.line_item_discounts.line_item_id = invoices.line_item_taxes.line_item_id ```  ``` orders.line_item_taxes.line_item_id = invoices.line_item_taxes.line_item_id ```  ``` orders.line_item_discounts.line_item_id = invoices.line_item_tiers.line_item_id ```  ``` orders.line_item_taxes.line_item_id = invoices.line_item_tiers.line_item_id ```  ``` orders.line_item_discounts.line_item_id = invoices.line_items.id ```  ``` orders.line_item_taxes.line_item_id = invoices.line_items.id ```  ``` orders.subscription_id = invoices.line_items.subscription_id ```  ``` orders.subscription_id = invoices.notes.entity_id ```  ``` orders.subscription_id = invoices.subscription_id ```  ``` orders.id = invoices.linked_orders.id ``` |
| [subscriptions](#subscriptions) | ``` orders.line_item_discounts.coupon_id = subscriptions.coupons.coupon_id ```  ``` orders.customer_id = subscriptions.customer_id ```  ``` orders.gift_id = subscriptions.gift_id ```  ``` orders.subscription_id = subscriptions.id ``` |
| [customers](#customers) | ``` orders.customer_id = customers.id ``` |
| [payment\_sources](#payment-sources) | ``` orders.customer_id = payment_sources.customer_id ``` |
| [promotional\_credits](#promotional-credits) | ``` orders.customer_id = promotional_credits.customer_id ``` |
| [transactions](#transactions) | ``` orders.customer_id = transactions.customer_id ```  ``` orders.invoice_id = transactions.linked_credit_notes.cn_reference_invoice_id ```  ``` orders.subscription_id = transactions.subscription_id ``` |
| [virtual\_bank\_accounts](#virtual-bank-accounts) | ``` orders.customer_id = virtual_bank_accounts.customer_id ``` |
| [gifts](#gifts) | ``` orders.customer_id = gifts.gift_receiver.customer_id ```  ``` orders.customer_id = gifts.gifter.customer_id ```  ``` orders.gift_id = gifts.id ```  ``` orders.invoice_id = gifts.gifter.invoice_id ```  ``` orders.subscription_id = gifts.gift_receiver.subscription_id ``` |

orders table schema

|  |
| --- |
| **amount\_adjusted**  INTEGER |
| **amount\_paid**  INTEGER |
| **batch\_id**  STRING |
| **billing\_address**  OBJECT This is a nested data structure:   - city: STRING - company: STRING - country: STRING - email: STRING - first\_name: STRING - last\_name: STRING - line1: STRING - line2: STRING - line3: STRING - object: STRING - phone: STRING - state: STRING - state\_code: STRING - validation\_status: STRING - zip: STRING |
| **cancellation\_reason**  STRING |
| **cancelled\_at**  DATE-TIME |
| **created\_at**  DATE-TIME |
| **created\_by**  STRING |
| **currency\_code**  STRING |
| **customer\_id**  STRING |
| **deleted**  BOOLEAN |
| **delivered\_at**  DATE-TIME |
| **discount**  INTEGER |
| **document\_number**  STRING |
| **fulfillment\_status**  STRING |
| **gift\_id**  STRING |
| **gift\_note**  STRING |
| **id**  STRING |
| **invoice\_id**  STRING |
| **invoice\_round\_off\_amount**  INTEGER |
| **is\_gifted**  BOOLEAN |
| **is\_resent**  BOOLEAN |
| **line\_item\_discounts**  ARRAY This is a nested data structure:   - coupon\_id: STRING - discount\_amount: INTEGER - discount\_type: STRING - line\_item\_id: STRING |
| **line\_item\_taxes**  ARRAY This is a nested data structure:   - is\_non\_compliance\_tax: BOOLEAN - is\_partial\_tax\_applied: BOOLEAN - line\_item\_id: STRING - local\_currency\_code: STRING - tax\_amount: INTEGER - tax\_amount\_in\_local\_currency: INTEGER - tax\_juris\_code: STRING - tax\_juris\_name: STRING - tax\_juris\_type: STRING - tax\_name: STRING - tax\_rate: INTEGER, NUMBER - taxable\_amount: INTEGER |
| **linked\_credit\_notes**  ARRAY This is a nested data structure:   - amount: INTEGER - amount\_adjusted: INTEGER - amount\_refunded: INTEGER - id: STRING - status: STRING - type: STRING |
| **note**  STRING |
| **order\_date**  DATE-TIME |
| **order\_line\_items**  ARRAY This is a nested data structure:   - amount: INTEGER - amount\_adjusted: INTEGER - amount\_paid: INTEGER - description: STRING - discount\_amount: INTEGER - entity\_id: STRING - entity\_type: STRING - fulfillment\_amount: INTEGER - fulfillment\_quantity: INTEGER - id: STRING - invoice\_id: STRING - invoice\_line\_item\_id: STRING - is\_shippable: BOOLEAN - item\_level\_discount\_amount: INTEGER - refundable\_credits: INTEGER - refundable\_credits\_issued: INTEGER - sku: STRING - status: STRING - tax\_amount: INTEGER - unit\_price: INTEGER |
| **order\_type**  STRING |
| **original\_order\_id**  STRING |
| **paid\_on**  DATE-TIME |
| **payment\_status**  STRING |
| **price\_type**  STRING |
| **reference\_id**  STRING |
| **refundable\_credits**  INTEGER |
| **refundable\_credits\_issued**  INTEGER |
| **resend\_reason**  STRING |
| **resent\_orders**  ARRAY This is a nested data structure:   - amount: INTEGER - order\_id: STRING - reason: STRING |
| **resent\_status**  STRING |
| **resource\_version**  INTEGER |
| **rounding\_adjustement**  INTEGER |
| **shipment\_carrier**  STRING |
| **shipped\_at**  DATE-TIME |
| **shipping\_address**  OBJECT This is a nested data structure:   - city: STRING - company: STRING - country: STRING - email: STRING - first\_name: STRING - last\_name: STRING - line1: STRING - line2: STRING - line3: STRING - object: STRING - phone: STRING - state: STRING - state\_code: STRING - validation\_status: STRING - zip: STRING |
| **shipping\_cut\_off\_date**  DATE-TIME |
| **shipping\_date**  DATE-TIME |
| **status**  STRING |
| **status\_update\_at**  DATE-TIME |
| **sub\_total**  INTEGER |
| **subscription\_id**  STRING |
| **tax**  INTEGER |
| **total**  INTEGER |
| **tracking\_id**  STRING |
| **tracking\_url**  STRING |
| **updated\_at**  DATE-TIME |

### payment\_sources

The `payment_sources` table contains info about customer payment sources.

**Note**: This table is available Refer to the [Table and field availability and Chargebee Product Catalogs section](#product-catalog-versions) for more info.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Chargebee documentation](https://apidocs.chargebee.com/Content/api/payment_sources)  [Chargebee API method](https://apidocs.chargebee.com/Content/api/payment_sources#list_payment_sources "Opens in new tab: Chargebee API method") |

payment\_sources table foreign keys

| Join payment\_sources with | on |
| --- | --- |
| [credit\_notes](#credit-notes) | ``` payment_sources.customer_id = credit_notes.customer_id ``` |
| [customers](#customers) | ``` payment_sources.customer_id = customers.id ```  ``` payment_sources.id = customers.primary_payment_source_id ``` |
| [events](#events) | ``` payment_sources.customer_id = events.content.customer.id ```  ``` payment_sources.customer_id = events.content.invoice.customer_id ```  ``` payment_sources.customer_id = events.content.subscription.customer_id ```  ``` payment_sources.customer_id = events.content.transaction.customer_id ```  ``` payment_sources.id = events.content.subscription.payment_source_id ```  ``` payment_sources.id = events.content.transaction.payment_source_id ``` |
| [invoices](#invoices) | ``` payment_sources.customer_id = invoices.customer_id ```  ``` payment_sources.customer_id = invoices.notes.entity_id ``` |
| [promotional\_credits](#promotional-credits) | ``` payment_sources.customer_id = promotional_credits.customer_id ``` |
| [subscriptions](#subscriptions) | ``` payment_sources.customer_id = subscriptions.customer_id ```  ``` payment_sources.id = subscriptions.payment_source_id ``` |
| [transactions](#transactions) | ``` payment_sources.customer_id = transactions.customer_id ```  ``` payment_sources.id = transactions.payment_source_id ``` |
| [virtual\_bank\_accounts](#virtual-bank-accounts) | ``` payment_sources.customer_id = virtual_bank_accounts.customer_id ``` |
| [gifts](#gifts) | ``` payment_sources.customer_id = gifts.gift_receiver.customer_id ```  ``` payment_sources.customer_id = gifts.gifter.customer_id ``` |
| [orders](#orders) | ``` payment_sources.customer_id = orders.customer_id ``` |

payment\_sources table schema

|  |
| --- |
| **amazon\_payment**  OBJECT This is a nested data structure:   - agreement\_id: STRING - email: STRING |
| **bank\_account**  OBJECT This is a nested data structure:   - account\_holder\_type: STRING - account\_type: STRING - bank\_name: STRING - echeck\_type: STRING - last4: STRING - mandate\_id: STRING - name\_on\_account: STRING |
| **card**  OBJECT This is a nested data structure:   - billing\_addr1: STRING - billing\_addr2: STRING - billing\_city: STRING - billing\_country: STRING - billing\_state: STRING - billing\_state\_code: STRING - billing\_zip: STRING - brand: STRING - expiry\_month: INTEGER - expiry\_year: INTEGER - first\_name: STRING - funding\_type: STRING - iin: STRING - last4: STRING - last\_name: STRING - masked\_number: STRING - object: STRING |
| **created\_at**  DATE-TIME |
| **customer\_id**  STRING |
| **deleted**  BOOLEAN |
| **gateway**  STRING |
| **gateway\_account\_id**  STRING |
| **id**  STRING |
| **ip\_address**  STRING |
| **issuing\_country**  STRING |
| **mandates**  ARRAY This is a nested data structure:   - created\_at: DATE-TIME - id: STRING - subscription\_id: STRING |
| **object**  STRING |
| **paypal**  OBJECT This is a nested data structure:   - agremeent\_id: STRING - email: STRING |
| **reference\_id**  STRING |
| **resource\_version**  INTEGER |
| **status**  STRING |
| **type**  STRING |
| **updated\_at**  DATE-TIME |
| **upi**  OBJECT This is a nested data structure:   - vpa: STRING |

### plans

The `plans` table contains info about the plans in your Chargebee account. Plans are used to specify prices and billing frequencies for [`subscriptions`](#subscriptions).

**Note**: This table is available Refer to the [Table and field availability and Chargebee Product Catalogs section](#product-catalog-versions) for more info.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Chargebee API method](https://apidocs.chargebee.com/Content/api/plans?prod_cat_ver=1#list_plans "Opens in new tab: Chargebee API method") |

plans table foreign keys

| Join plans with | on |
| --- | --- |
| [addons](#addons) | ``` plans.applicable_addons.id = addons.id ``` |
| [coupons](#coupons) | ``` plans.applicable_addons.id = coupons.addon_ids ```  ``` plans.id = coupons.plan_ids ``` |
| [events](#events) | ``` plans.applicable_addons.id = events.content.subscription.addons.id ```  ``` plans.applicable_addons.id = events.content.subscription.charged_event_based_addons.id ```  ``` plans.applicable_addons.id = events.content.subscription.event_based_addons.id ```  ``` plans.id = events.content.coupon.plan_ids ```  ``` plans.id = events.content.subscription.plan_id ``` |
| [invoices](#invoices) | ``` plans.applicable_addons.id = invoices.notes.entity_id ```  ``` plans.id = invoices.notes.entity_id ``` |
| [subscriptions](#subscriptions) | ``` plans.applicable_addons.id = subscriptions.addons.id ```  ``` plans.applicable_addons.id = subscriptions.charged_event_based_addons.id ```  ``` plans.applicable_addons.id = subscriptions.event_based_addons.id ```  ``` plans.id = subscriptions.plan_id ``` |

plans table schema

|  |
| --- |
| **account\_code**  STRING |
| **accounting\_category1**  STRING |
| **accounting\_category2**  STRING |
| **accounting\_category3**  STRING |
| **accounting\_category4**  STRING |
| **accounting\_code**  STRING |
| **addon\_applicability**  STRING |
| **applicable\_addons**  ARRAY This is a nested data structure:   - id: STRING - quantity\_in\_decimal: STRING |
| **archived\_at**  DATE-TIME |
| **attached\_addons**  ARRAY This is a nested data structure:   - billing\_cycles: INTEGER - id: STRING - quantity: STRING - quantity\_in\_decimal: STRING - type: STRING |
| **avalara\_sale\_type**  STRING |
| **avalara\_service\_type**  INTEGER |
| **avalara\_transaction\_type**  INTEGER |
| **billing\_cycles**  INTEGER |
| **channel**  STRING |
| **charge\_model**  STRING |
| **claim\_url**  STRING |
| **currency\_code**  STRING |
| **custom\_fields**  STRING |
| **description**  STRING |
| **enabled\_in\_hosted\_pages**  BOOLEAN |
| **enabled\_in\_portal**  BOOLEAN |
| **event\_based\_addons**  ARRAY This is a nested data structure:   - charge\_once: BOOLEAN - id: STRING - on\_event: STRING - quantity: INTEGER - quantity\_in\_decimal: STRING |
| **free\_quantity**  INTEGER |
| **free\_quantity\_in\_decimal**  STRING |
| **giftable**  BOOLEAN |
| **id**  STRING |
| **invoice\_name**  STRING |
| **invoice\_notes**  STRING |
| **is\_shippable**  BOOLEAN |
| **meta\_data**  STRING |
| **name**  STRING |
| **object**  STRING |
| **period**  INTEGER |
| **period\_unit**  STRING |
| **price**  INTEGER |
| **price\_in\_decimal**  STRING |
| **pricing\_model**  STRING |
| **redirect\_url**  STRING |
| **resource\_version**  INTEGER |
| **setup\_cost**  INTEGER |
| **shipping\_frequency\_period**  INTEGER |
| **shipping\_frequency\_period\_unit**  STRING |
| **show\_description\_in\_invoices**  BOOLEAN |
| **show\_description\_in\_quotes**  BOOLEAN |
| **sku**  STRING |
| **status**  STRING |
| **tax\_code**  STRING |
| **tax\_profile\_id**  STRING |
| **taxable**  BOOLEAN |
| **taxjar\_product\_code**  STRING |
| **tiers**  ARRAY This is a nested data structure:   - ending\_unit: INTEGER - ending\_unit\_in\_decimal: STRING - price: INTEGER - price\_in\_decimal: STRING - starting\_unit: INTEGER - starting\_unit\_in\_decimal: STRING |
| **trial\_end\_action**  STRING |
| **trial\_period**  INTEGER |
| **trial\_period\_unit**  STRING |
| **updated\_at**  DATE-TIME |

### promotional\_credits

The `promotional_credits` table contains info about the promotional\_credits in your Chargebee account.

**Note**: This table is available Refer to the [Table and field availability and Chargebee Product Catalogs section](#product-catalog-versions) for more info.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | created\_at |
| **Useful links** | [Chargebee documentation](https://apidocs.chargebee.com/Content/api/promotional_credits)  [Chargebee API method](https://apidocs.chargebee.com/Content/api/promotional_credits#list_promotional_credits "Opens in new tab: Chargebee API method") |

promotional\_credits table foreign keys

| Join promotional\_credits with | on |
| --- | --- |
| [credit\_notes](#credit-notes) | ``` promotional_credits.customer_id = credit_notes.customer_id ``` |
| [customers](#customers) | ``` promotional_credits.customer_id = customers.id ``` |
| [events](#events) | ``` promotional_credits.customer_id = events.content.customer.id ```  ``` promotional_credits.customer_id = events.content.invoice.customer_id ```  ``` promotional_credits.customer_id = events.content.subscription.customer_id ```  ``` promotional_credits.customer_id = events.content.transaction.customer_id ``` |
| [invoices](#invoices) | ``` promotional_credits.customer_id = invoices.customer_id ```  ``` promotional_credits.customer_id = invoices.notes.entity_id ``` |
| [payment\_sources](#payment-sources) | ``` promotional_credits.customer_id = payment_sources.customer_id ``` |
| [subscriptions](#subscriptions) | ``` promotional_credits.customer_id = subscriptions.customer_id ``` |
| [transactions](#transactions) | ``` promotional_credits.customer_id = transactions.customer_id ``` |
| [virtual\_bank\_accounts](#virtual-bank-accounts) | ``` promotional_credits.customer_id = virtual_bank_accounts.customer_id ``` |
| [gifts](#gifts) | ``` promotional_credits.customer_id = gifts.gift_receiver.customer_id ```  ``` promotional_credits.customer_id = gifts.gifter.customer_id ``` |
| [orders](#orders) | ``` promotional_credits.customer_id = orders.customer_id ``` |

promotional\_credits table schema

|  |
| --- |
| **amount**  STRING |
| **amount\_in\_decimal**  STRING |
| **closing\_balance**  INTEGER |
| **created\_at**  DATE-TIME |
| **credit\_type**  STRING |
| **currency\_code**  STRING |
| **customer\_id**  STRING |
| **description**  STRING |
| **done\_by**  STRING |
| **id**  STRING |
| **object**  STRING |
| **reference**  STRING |
| **type**  STRING |

### quotes

The `quotes` table contains info about quotes in your Chargebee account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Chargebee documentation](https://apidocs.chargebee.com/Content/api/quotes)  [Chargebee API method](https://apidocs.chargebee.com/Content/api/quotes#list_quotes "Opens in new tab: Chargebee API method") |

quotes table schema

|  |
| --- |
| **amount\_due**  INTEGER |
| **amount\_paid**  INTEGER |
| **billing\_address**  OBJECT This is a nested data structure:   - city: STRING - company: STRING - country: STRING - email: STRING - first\_name: STRING - last\_name: STRING - line1: STRING - line2: STRING - line3: STRING - object: STRING - phone: STRING - state: STRING - state\_code: STRING - validation\_status: STRING - zip: STRING |
| **charge\_on\_acceptance**  INTEGER |
| **contract\_term\_end**  DATE-TIME |
| **contract\_term\_start**  DATE-TIME |
| **contract\_term\_termination\_fee**  INTEGER |
| **credits\_applied**  INTEGER |
| **currency\_code**  STRING |
| **customer\_id**  STRING |
| **date**  DATE-TIME |
| **discounts**  ARRAY This is a nested data structure:   - amount: INTEGER - description: STRING - entity\_id: STRING - entity\_type: STRING - object: STRING |
| **id**  STRING |
| **invoice\_id**  STRING |
| **line\_item\_discounts**  ARRAY This is a nested data structure:   - coupon\_id: STRING - discount\_amount: INTEGER - discount\_type: STRING - entity\_id: STRING - line\_item\_id: STRING |
| **line\_item\_taxes**  ARRAY This is a nested data structure:   - is\_non\_compliance\_tax: BOOLEAN - is\_partial\_tax\_applied: BOOLEAN - line\_item\_id: STRING - local\_currency\_code: STRING - tax\_amount: INTEGER - tax\_amount\_in\_local\_currency: INTEGER - tax\_juris\_code: STRING - tax\_juris\_name: STRING - tax\_juris\_type: STRING - tax\_name: STRING - tax\_rate: INTEGER, NUMBER - taxable\_amount: INTEGER |
| **line\_item\_tiers**  ARRAY This is a nested data structure:   - ending\_unit: INTEGER - line\_item\_id: STRING - quantity\_used: INTEGER - starting\_unit: INTEGER - unit\_amount: INTEGER |
| **line\_items**  ARRAY This is a nested data structure:   - amount: INTEGER - date\_from: DATE-TIME - description: STRING - discount\_amount: INTEGER - entity\_id: STRING - entity\_type: STRING - id: STRING - is\_taxed: BOOLEAN - item\_level\_discount\_amount: INTEGER - object: STRING - pricing\_model: STRING - quantity: INTEGER - subscription\_id: STRING - tax\_amount: INTEGER - tax\_exempt\_reason: STRING - tax\_rate: NUMBER - unit\_amount: INTEGER |
| **name**  STRING |
| **notes**  STRING |
| **operation\_type**  STRING |
| **po\_number**  STRING |
| **price\_type**  STRING |
| **resource\_version**  INTEGER |
| **shipping\_address**  OBJECT This is a nested data structure:   - city: STRING - company: STRING - country: STRING - email: STRING - first\_name: STRING - last\_name: STRING - line1: STRING - line2: STRING - line3: STRING - object: STRING - phone: STRING - state: STRING - state\_code: STRING - validation\_status: STRING - zip: STRING |
| **status**  STRING |
| **sub\_total**  INTEGER |
| **subscription\_id**  STRING |
| **taxes**  ARRAY This is a nested data structure:   - amount: INTEGER - description: STRING - name: STRING |
| **total**  INTEGER |
| **total\_payable**  INTEGER |
| **updated\_at**  DATE-TIME |
| **valid\_till**  DATE-TIME |
| **vat\_number**  STRING |
| **vat\_number\_prefix**  STRING |
| **version**  INTEGER |

### subscriptions

The `subscriptions` table contains info about the subscriptions your customers have subscribed to. A subscription is a recurring item that customers are billed for, such as a plan or addon. It may also contain discount items.

**Note**: Chargebee [does not update the `updated_at`](https://apidocs.chargebee.com/Content/api/subscriptions#subscription_updated_at) value when the following attributes on a subscription are modified:

- `due_invoices_count`
- `due_since`
- `total_dues`

**Note**: This table is available Refer to the [Table and field availability and Chargebee Product Catalogs section](#product-catalog-versions) for more info.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Chargebee documentation](https://apidocs.chargebee.com/Content/api/subscriptions)  [Chargebee API method](https://apidocs.chargebee.com/Content/api/subscriptions#list_subscriptions "Opens in new tab: Chargebee API method") |

subscriptions table foreign keys

| Join subscriptions with | on |
| --- | --- |
| [addons](#addons) | ``` subscriptions.addons.id = addons.id ```  ``` subscriptions.charged_event_based_addons.id = addons.id ```  ``` subscriptions.event_based_addons.id = addons.id ``` |
| [coupons](#coupons) | ``` subscriptions.addons.id = coupons.addon_ids ```  ``` subscriptions.charged_event_based_addons.id = coupons.addon_ids ```  ``` subscriptions.event_based_addons.id = coupons.addon_ids ```  ``` subscriptions.coupons.coupon_id = coupons.id ```  ``` subscriptions.plan_id = coupons.plan_ids ``` |
| [events](#events) | ``` subscriptions.addons.id = events.content.subscription.addons.id ```  ``` subscriptions.charged_event_based_addons.id = events.content.subscription.addons.id ```  ``` subscriptions.event_based_addons.id = events.content.subscription.addons.id ```  ``` subscriptions.addons.id = events.content.subscription.charged_event_based_addons.id ```  ``` subscriptions.charged_event_based_addons.id = events.content.subscription.charged_event_based_addons.id ```  ``` subscriptions.event_based_addons.id = events.content.subscription.charged_event_based_addons.id ```  ``` subscriptions.addons.id = events.content.subscription.event_based_addons.id ```  ``` subscriptions.charged_event_based_addons.id = events.content.subscription.event_based_addons.id ```  ``` subscriptions.event_based_addons.id = events.content.subscription.event_based_addons.id ```  ``` subscriptions.coupons.coupon_id = events.content.coupon.id ```  ``` subscriptions.coupons.coupon_id = events.content.invoice.discounts.entity_id ```  ``` subscriptions.coupons.coupon_id = events.content.invoice.line_item_discounts.coupon_id ```  ``` subscriptions.coupons.coupon_id = events.content.subscription.coupons.coupon_id ```  ``` subscriptions.customer_id = events.content.customer.id ```  ``` subscriptions.customer_id = events.content.invoice.customer_id ```  ``` subscriptions.customer_id = events.content.subscription.customer_id ```  ``` subscriptions.customer_id = events.content.transaction.customer_id ```  ``` subscriptions.plan_id = events.content.coupon.plan_ids ```  ``` subscriptions.plan_id = events.content.subscription.plan_id ```  ``` subscriptions.payment_source_id = events.content.subscription.payment_source_id ```  ``` subscriptions.payment_source_id = events.content.transaction.payment_source_id ```  ``` subscriptions.id = events.content.subscription.id ```  ``` subscriptions.id = events.content.invoice.subscription_id ```  ``` subscriptions.id = events.content.transaction.subscription_id ``` |
| [invoices](#invoices) | ``` subscriptions.addons.id = invoices.notes.entity_id ```  ``` subscriptions.charged_event_based_addons.id = invoices.notes.entity_id ```  ``` subscriptions.event_based_addons.id = invoices.notes.entity_id ```  ``` subscriptions.coupons.coupon_id = invoices.discounts.entity_id ```  ``` subscriptions.coupons.coupon_id = invoices.line_item_discounts.coupon_id ```  ``` subscriptions.coupons.coupon_id = invoices.notes.entity_id ```  ``` subscriptions.customer_id = invoices.customer_id ```  ``` subscriptions.customer_id = invoices.notes.entity_id ```  ``` subscriptions.plan_id = invoices.notes.entity_id ```  ``` subscriptions.id = invoices.line_items.subscription_id ```  ``` subscriptions.id = invoices.notes.entity_id ```  ``` subscriptions.id = invoices.subscription_id ``` |
| [plans](#plans) | ``` subscriptions.addons.id = plans.applicable_addons.id ```  ``` subscriptions.charged_event_based_addons.id = plans.applicable_addons.id ```  ``` subscriptions.event_based_addons.id = plans.applicable_addons.id ```  ``` subscriptions.plan_id = plans.id ``` |
| [credit\_notes](#credit-notes) | ``` subscriptions.coupons.coupon_id = credit_notes.discounts.entity_id ```  ``` subscriptions.coupons.coupon_id = credit_notes.line_item_discounts.coupon_id ```  ``` subscriptions.customer_id = credit_notes.customer_id ```  ``` subscriptions.id = credit_notes.subscription_id ```  ``` subscriptions.id = credit_notes.line_items.subscription_id ``` |
| [orders](#orders) | ``` subscriptions.coupons.coupon_id = orders.line_item_discounts.coupon_id ```  ``` subscriptions.customer_id = orders.customer_id ```  ``` subscriptions.gift_id = orders.gift_id ```  ``` subscriptions.id = orders.subscription_id ``` |
| [customers](#customers) | ``` subscriptions.customer_id = customers.id ```  ``` subscriptions.payment_source_id = customers.primary_payment_source_id ``` |
| [payment\_sources](#payment-sources) | ``` subscriptions.customer_id = payment_sources.customer_id ```  ``` subscriptions.payment_source_id = payment_sources.id ``` |
| [promotional\_credits](#promotional-credits) | ``` subscriptions.customer_id = promotional_credits.customer_id ``` |
| [transactions](#transactions) | ``` subscriptions.customer_id = transactions.customer_id ```  ``` subscriptions.payment_source_id = transactions.payment_source_id ```  ``` subscriptions.id = transactions.subscription_id ``` |
| [virtual\_bank\_accounts](#virtual-bank-accounts) | ``` subscriptions.customer_id = virtual_bank_accounts.customer_id ``` |
| [gifts](#gifts) | ``` subscriptions.customer_id = gifts.gift_receiver.customer_id ```  ``` subscriptions.customer_id = gifts.gifter.customer_id ```  ``` subscriptions.gift_id = gifts.id ```  ``` subscriptions.id = gifts.gift_receiver.subscription_id ``` |

subscriptions table schema

|  |
| --- |
| **activated\_at**  DATE-TIME |
| **auto\_close\_invoices**  BOOLEAN |
| **auto\_collection**  STRING |
| **base\_currency\_code**  STRING |
| **billing\_period**  INTEGER |
| **billing\_period\_unit**  STRING |
| **cancel\_reason**  STRING |
| **cancel\_reason\_code**  STRING |
| **cancel\_schedule\_created\_at**  DATE-TIME |
| **cancelled\_at**  DATE-TIME |
| **changes\_scheduled\_at**  DATE-TIME |
| **channel**  STRING |
| **charged\_items**  ARRAY This is a nested data structure:   - item\_price\_id: STRING - last\_charged\_at: DATE-TIME - object: STRING |
| **contract\_term**  OBJECT This is a nested data structure:   - action\_at\_term\_end: STRING - billing\_cycle: INTEGER - cancellation\_cutoff\_period: INTEGER - contract\_end: DATE-TIME - contract\_start: DATE-TIME - created\_at: DATE-TIME - id STRING - remaining\_billing\_cycles: INTEGER - status: STRING - subscription\_id STRING - total\_contract\_value: INTEGER |
| **contract\_term\_billing\_cycle\_on\_renewal**  INTEGER |
| **coupon**  STRING |
| **coupons**  ARRAY This is a nested data structure:   - applied\_count: INTEGER - apply\_till: DATE-TIME - coupon\_code: STRING - coupon\_id: STRING - object: STRING |
| **create\_pending\_invoices**  BOOLEAN |
| **created\_at**  DATE-TIME |
| **created\_from\_ip**  STRING |
| **currency\_code**  STRING |
| **current\_term\_end**  DATE-TIME |
| **current\_term\_start**  DATE-TIME |
| **custom\_fields**  STRING |
| **customer\_id**  STRING |
| **discounts**  ARRAY This is a nested data structure:   - amount: NUMBER - applied\_count: INTEGER - apply\_on: STRING - apply\_till: INTEGER - coupon\_id: STRING - created\_at: INTEGER - currency\_code: STRING - duration\_type: STRING - id: STRING - included\_in\_mrr: BOOLEAN - index: INTEGER - invoice\_name: STRING - item\_price\_id: STRING - name: STRING - object: STRING - percentage: NUMBER - period: INTEGER - period\_unit: STRING - resource\_version: INTEGER - type: STRING - updated\_at: INTEGER |
| **exchange\_rate**  NUMBER |
| **free\_period**  INTEGER |
| **free\_period\_unit**  STRING |
| **gift\_id**  STRING |
| **has\_scheduled\_advance\_invoices**  BOOLEAN |
| **has\_scheduled\_changes**  BOOLEAN |
| **id**  STRING |
| **invoice\_notes**  STRING |
| **meta\_data**  STRING |
| **mrr**  INTEGER |
| **next\_billing\_at**  DATE-TIME |
| **object**  STRING |
| **offline\_payment\_method**  STRING |
| **override\_relationship**  BOOLEAN |
| **pause\_date**  DATE-TIME |
| **payment\_source\_id**  STRING |
| **plan\_amount**  INTEGER |
| **plan\_amount\_in\_decimal**  STRING |
| **plan\_free\_quantity**  INTEGER |
| **plan\_free\_quantity\_in\_decimal**  STRING |
| **plan\_id**  STRING |
| **plan\_quantity**  INTEGER |
| **plan\_quantity\_in\_decimal**  STRING |
| **plan\_unit\_price**  INTEGER |
| **plan\_unit\_price\_in\_decimal**  STRING |
| **po\_number**  STRING |
| **referral\_info**  OBJECT This is a nested data structure:   - account\_id: STRING - campaign\_id: STRING - coupon\_code: STRING - destination\_url: STRING - external\_campaign\_id: STRING - external\_reference\_id: STRING - friend\_offer\_type: STRING - notify\_referral\_system: STRING - post\_purchase\_widget\_enabled: BOOLEAN - referral\_code: STRING - referral\_system: STRING - referrer\_id: STRING - referrer\_reward\_type: STRING - reward\_status: STRING |
| **remaining\_billing\_cycles**  INTEGER |
| **resource\_version**  INTEGER |
| **resume\_date**  DATE-TIME |
| **setup\_fee**  INTEGER |
| **shipping\_address**  OBJECT This is a nested data structure:   - city: STRING - company: STRING - country: STRING - email: STRING - first\_name: STRING - last\_name: STRING - line1: STRING - line2: STRING - line3: STRING - object: STRING - phone: STRING - state: STRING - state\_code: STRING - validation\_status: STRING - zip: STRING |
| **start\_date**  DATE-TIME |
| **started\_at**  DATE-TIME |
| **status**  STRING |
| **subscription\_items**  ARRAY This is a nested data structure:   - amount: INTEGER - amount\_in\_decimal: STRING - billing\_cycles: INTEGER - charge\_on\_event: STRING - charge\_on\_option: STRING - charge\_once: BOOLEAN - free\_quantity: INTEGER - free\_quantity\_in\_decimal: STRING - item\_price\_id: STRING - item\_type: STRING - object: STRING - quantity: INTEGER - quantity\_in\_decimal: STRING - service\_period\_days: INTEGER - trial\_end: DATE-TIME - unit\_price: INTEGER - unit\_price\_in\_decimal: STRING |
| **total\_dues**  INTEGER |
| **trial\_end**  DATE-TIME |
| **trial\_end\_action**  STRING |
| **trial\_start**  DATE-TIME |
| **updated\_at**  DATE-TIME |

### transactions

The `transactions` table contains info about the transactions that have occurred in your Chargebee account.

**Note**: This table is available Refer to the [Table and field availability and Chargebee Product Catalogs section](#product-catalog-versions) for more info.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Chargebee documentation](https://apidocs.chargebee.com/Content/api/transactions)  [Chargebee API method](https://apidocs.chargebee.com/Content/api/transactions#list_transactions "Opens in new tab: Chargebee API method") |

transactions table foreign keys

| Join transactions with | on |
| --- | --- |
| [credit\_notes](#credit-notes) | ``` transactions.customer_id = credit_notes.customer_id ```  ``` transactions.linked_credit_notes.cn_reference_invoice_id = credit_notes.allocations.invoice_id ```  ``` transactions.linked_credit_notes.cn_reference_invoice_id = credit_notes.reference_invoice_id ```  ``` transactions.subscription_id = credit_notes.subscription_id ```  ``` transactions.subscription_id = credit_notes.line_items.subscription_id ```  ``` transactions.id = credit_notes.linked_refunds.txn_id ```  ``` transactions.linked_refunds.txn_id = credit_notes.linked_refunds.txn_id ```  ``` transactions.reference_transaction_id = credit_notes.linked_refunds.txn_id ```  ``` transactions.refunded_txn_id = credit_notes.linked_refunds.txn_id ``` |
| [customers](#customers) | ``` transactions.customer_id = customers.id ```  ``` transactions.payment_source_id = customers.primary_payment_source_id ``` |
| [events](#events) | ``` transactions.customer_id = events.content.customer.id ```  ``` transactions.customer_id = events.content.invoice.customer_id ```  ``` transactions.customer_id = events.content.subscription.customer_id ```  ``` transactions.customer_id = events.content.transaction.customer_id ```  ``` transactions.linked_credit_notes.cn_reference_invoice_id = events.content.invoice.id ```  ``` transactions.linked_credit_notes.cn_reference_invoice_id = events.content.transaction.linked_credit_notes.cn_reference_invoice_id ```  ``` transactions.payment_source_id = events.content.subscription.payment_source_id ```  ``` transactions.payment_source_id = events.content.transaction.payment_source_id ```  ``` transactions.subscription_id = events.content.subscription.id ```  ``` transactions.subscription_id = events.content.invoice.subscription_id ```  ``` transactions.subscription_id = events.content.transaction.subscription_id ```  ``` transactions.id = events.content.invoice.linked_payments.txn_id ```  ``` transactions.linked_refunds.txn_id = events.content.invoice.linked_payments.txn_id ```  ``` transactions.reference_transaction_id = events.content.invoice.linked_payments.txn_id ```  ``` transactions.refunded_txn_id = events.content.invoice.linked_payments.txn_id ```  ``` transactions.id = events.content.transaction.id ```  ``` transactions.linked_refunds.txn_id = events.content.transaction.id ```  ``` transactions.reference_transaction_id = events.content.transaction.id ```  ``` transactions.refunded_txn_id = events.content.transaction.id ```  ``` transactions.id = events.content.transaction.linked_refunds.txn_id ```  ``` transactions.linked_refunds.txn_id = events.content.transaction.linked_refunds.txn_id ```  ``` transactions.reference_transaction_id = events.content.transaction.linked_refunds.txn_id ```  ``` transactions.refunded_txn_id = events.content.transaction.linked_refunds.txn_id ```  ``` transactions.id = events.content.transaction.reference_transaction_id ```  ``` transactions.linked_refunds.txn_id = events.content.transaction.reference_transaction_id ```  ``` transactions.reference_transaction_id = events.content.transaction.reference_transaction_id ```  ``` transactions.refunded_txn_id = events.content.transaction.reference_transaction_id ```  ``` transactions.id = events.content.transaction.refunded_txn_id ```  ``` transactions.linked_refunds.txn_id = events.content.transaction.refunded_txn_id ```  ``` transactions.reference_transaction_id = events.content.transaction.refunded_txn_id ```  ``` transactions.refunded_txn_id = events.content.transaction.refunded_txn_id ``` |
| [invoices](#invoices) | ``` transactions.customer_id = invoices.customer_id ```  ``` transactions.customer_id = invoices.notes.entity_id ```  ``` transactions.linked_credit_notes.cn_reference_invoice_id = invoices.id ```  ``` transactions.subscription_id = invoices.line_items.subscription_id ```  ``` transactions.subscription_id = invoices.notes.entity_id ```  ``` transactions.subscription_id = invoices.subscription_id ```  ``` transactions.id = invoices.linked_payments.txn_id ```  ``` transactions.linked_refunds.txn_id = invoices.linked_payments.txn_id ```  ``` transactions.reference_transaction_id = invoices.linked_payments.txn_id ```  ``` transactions.refunded_txn_id = invoices.linked_payments.txn_id ``` |
| [payment\_sources](#payment-sources) | ``` transactions.customer_id = payment_sources.customer_id ```  ``` transactions.payment_source_id = payment_sources.id ``` |
| [promotional\_credits](#promotional-credits) | ``` transactions.customer_id = promotional_credits.customer_id ``` |
| [subscriptions](#subscriptions) | ``` transactions.customer_id = subscriptions.customer_id ```  ``` transactions.payment_source_id = subscriptions.payment_source_id ```  ``` transactions.subscription_id = subscriptions.id ``` |
| [virtual\_bank\_accounts](#virtual-bank-accounts) | ``` transactions.customer_id = virtual_bank_accounts.customer_id ``` |
| [gifts](#gifts) | ``` transactions.customer_id = gifts.gift_receiver.customer_id ```  ``` transactions.customer_id = gifts.gifter.customer_id ```  ``` transactions.linked_credit_notes.cn_reference_invoice_id = gifts.gifter.invoice_id ```  ``` transactions.subscription_id = gifts.gift_receiver.subscription_id ``` |
| [orders](#orders) | ``` transactions.customer_id = orders.customer_id ```  ``` transactions.linked_credit_notes.cn_reference_invoice_id = orders.invoice_id ```  ``` transactions.subscription_id = orders.subscription_id ``` |

transactions table schema

|  |
| --- |
| **amount**  INTEGER |
| **amount\_capturable**  STRING |
| **amount\_unused**  INTEGER |
| **authorization\_reason**  STRING |
| **base\_currency\_code**  STRING |
| **currency\_code**  STRING |
| **customer\_id**  STRING |
| **date**  DATE-TIME |
| **deleted**  BOOLEAN |
| **error\_code**  STRING |
| **error\_text**  STRING |
| **exchange\_rate**  NUMBER |
| **fraud\_flag**  STRING |
| **fraud\_reason**  STRING |
| **gateway**  STRING |
| **gateway\_account\_id**  STRING |
| **id**  STRING |
| **id\_at\_gateway**  STRING |
| **iin**  STRING |
| **initiator\_type**  STRING |
| **last4**  STRING |
| **linked\_credit\_notes**  ARRAY This is a nested data structure:   - applied\_amount: INTEGER - applied\_at: DATE-TIME - cn\_create\_reason\_code: STRING - cn\_date: DATE-TIME - cn\_id: STRING - cn\_reason\_code: STRING - cn\_reference\_invoice\_id: STRING - cn\_status: STRING - cn\_total: INTEGER |
| **linked\_invoices**  ARRAY This is a nested data structure:   - applied\_amount: INTEGER - applied\_at: DATE-TIME - invoice\_date: DATE-TIME - invoice\_id: STRING - invoice\_status: STRING - invoice\_total: INTEGER |
| **linked\_payments**  ARRAY This is a nested data structure:   - amount: INTEGER - date: DATE-TIME - id: STRING - status: STRING |
| **linked\_refunds**  ARRAY This is a nested data structure:   - txn\_amount: INTEGER - txn\_date: DATE-TIME - txn\_id: STRING - txn\_status: STRING |
| **masked\_card\_number**  STRING |
| **merchant\_reference\_id**  STRING |
| **object**  STRING |
| **payment\_method**  STRING |
| **payment\_source\_id**  STRING |
| **reference\_authorization\_id**  STRING |
| **reference\_number**  STRING |
| **reference\_transaction\_id**  STRING |
| **refunded\_txn\_id**  STRING |
| **resource\_version**  INTEGER |
| **reversal\_transaction\_id**  STRING |
| **reversal\_txn\_id**  STRING |
| **settled\_at**  DATE-TIME |
| **status**  STRING |
| **subscription\_id**  STRING |
| **three\_d\_secure**  BOOLEAN |
| **type**  STRING |
| **updated\_at**  DATE-TIME |
| **validated\_at**  DATE-TIME |
| **voided\_at**  DATE-TIME |

### virtual\_bank\_accounts

The `virtual_bank_accounts` table contains info about the virtual bank accounts in your Chargebee account. A virtual bank account is a unique account number that can be shared with your users while still protecting your sensitive bank account details.

**Note**: This table is available Refer to the [Table and field availability and Chargebee Product Catalogs section](#product-catalog-versions) for more info.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Chargebee documentation](https://apidocs.chargebee.com/Content/api/virtual_bank_accounts)  [Chargebee API method](https://apidocs.chargebee.com/Content/api/virtual_bank_accounts#list_virtual_bank_accounts "Opens in new tab: Chargebee API method") |

virtual\_bank\_accounts table foreign keys

| Join virtual\_bank\_accounts with | on |
| --- | --- |
| [credit\_notes](#credit-notes) | ``` virtual_bank_accounts.customer_id = credit_notes.customer_id ``` |
| [customers](#customers) | ``` virtual_bank_accounts.customer_id = customers.id ``` |
| [events](#events) | ``` virtual_bank_accounts.customer_id = events.content.customer.id ```  ``` virtual_bank_accounts.customer_id = events.content.invoice.customer_id ```  ``` virtual_bank_accounts.customer_id = events.content.subscription.customer_id ```  ``` virtual_bank_accounts.customer_id = events.content.transaction.customer_id ``` |
| [invoices](#invoices) | ``` virtual_bank_accounts.customer_id = invoices.customer_id ```  ``` virtual_bank_accounts.customer_id = invoices.notes.entity_id ``` |
| [payment\_sources](#payment-sources) | ``` virtual_bank_accounts.customer_id = payment_sources.customer_id ``` |
| [promotional\_credits](#promotional-credits) | ``` virtual_bank_accounts.customer_id = promotional_credits.customer_id ``` |
| [subscriptions](#subscriptions) | ``` virtual_bank_accounts.customer_id = subscriptions.customer_id ``` |
| [transactions](#transactions) | ``` virtual_bank_accounts.customer_id = transactions.customer_id ``` |
| [gifts](#gifts) | ``` virtual_bank_accounts.customer_id = gifts.gift_receiver.customer_id ```  ``` virtual_bank_accounts.customer_id = gifts.gifter.customer_id ``` |
| [orders](#orders) | ``` virtual_bank_accounts.customer_id = orders.customer_id ``` |

virtual\_bank\_accounts table schema

|  |
| --- |
| **account\_number**  STRING |
| **bank\_name**  STRING |
| **created\_at**  DATE-TIME |
| **customer\_id**  STRING |
| **deleted**  BOOLEAN |
| **email**  STRING |
| **gateway**  STRING |
| **gateway\_account\_id**  STRING |
| **id**  STRING |
| **object**  STRING |
| **reference\_id**  STRING |
| **resource\_version**  INTEGER |
| **routing\_number**  STRING |
| **scheme**  STRING |
| **swift\_code**  STRING |
| **updated\_at**  DATE-TIME |
