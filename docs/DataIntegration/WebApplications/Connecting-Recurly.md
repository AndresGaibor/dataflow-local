---
title: "Recurly"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Recurly.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Recurly

Recurly is a billing system designed to assist small and medium-sized enterprises in automating and managing their subscription and revenue workflows.

For more information about the API, see [Recurly Partner API (v2018-08-09)](https://partner-docs.recurly.com/v2018-08-09#section/Getting-Started).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To generate the API key:

1. Make sure you have a role with the Integration permission in Recurly. You need it to generate the API key.
2. Log into your Recurly account.
3. Click Admin > Users.
4. On the Users page, go to Integrations > API Credentials.
5. Click Add Private API Key.
6. Fill in the fields:
   - Key Name: Enter a name for the API key. For example: Qlik.
   - Notes: Enter any notes you want about the API key.
7. Click Save Changes.
8. Copy the API key.

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
| Subdomain | Enter your Recurly subdomain. If the full URL of the subdomain is `qlik.recurly.com`, enter qlik into this field. |
| Quota limit | Enter the percentage of the API rate limit you want to allocate to the integration. Example: 30. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### accounts

The `accounts` table contains info about the customer accounts in your Recurly account. Account objects store the history of the customer, billing info, etc.

### Custom fields

Recurly integration supports replicating custom fields for accounts objects.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Recurly documentation](https://dev.recurly.com/Content/account-object)  [Recurly API method](https://partner-docs.recurly.com/v2018-08-09#operation/list_accounts "Opens in new tab: Recurly API method") |

accounts table foreign keys

| Join accounts with | on |
| --- | --- |
| [adjustments](#adjustments) | ``` accounts.id = adjustments.account.id ```  ``` accounts.parent_account_id = adjustments.account.id ```  ``` accounts.shipping_addresses.account_id = adjustments.account.id ```  ``` accounts.id = adjustments.account.parent_account_id ```  ``` accounts.parent_account_id = adjustments.account.parent_account_id ```  ``` accounts.shipping_addresses.account_id = adjustments.account.parent_account_id ``` |
| [billing\_info](#billing-info) | ``` accounts.id = billing_info.account_id ```  ``` accounts.parent_account_id = billing_info.account_id ```  ``` accounts.shipping_addresses.account_id = billing_info.account_id ``` |
| [coupon\_redemptions](#coupon-redemptions) | ``` accounts.id = coupon_redemptions.account_id ```  ``` accounts.parent_account_id = coupon_redemptions.account_id ```  ``` accounts.shipping_addresses.account_id = coupon_redemptions.account_id ``` |
| [invoices](#invoices) | ``` accounts.id = invoices.account.id ```  ``` accounts.parent_account_id = invoices.account.id ```  ``` accounts.shipping_addresses.account_id = invoices.account.id ```  ``` accounts.id = invoices.account.parent_account_id ```  ``` accounts.parent_account_id = invoices.account.parent_account_id ```  ``` accounts.shipping_addresses.account_id = invoices.account.parent_account_id ```  ``` accounts.id = invoices.credit_payments.refund_transaction.account.id ```  ``` accounts.parent_account_id = invoices.credit_payments.refund_transaction.account.id ```  ``` accounts.shipping_addresses.account_id = invoices.credit_payments.refund_transaction.account.id ```  ``` accounts.id = invoices.line_items.data.shipping_addresses.account_id ```  ``` accounts.parent_account_id = invoices.line_items.data.shipping_addresses.account_id ```  ``` accounts.shipping_addresses.account_id = invoices.line_items.data.shipping_addresses.account_id ``` |
| [subscriptions](#subscriptions) | ``` accounts.id = subscriptions.shipping_address.account_id ```  ``` accounts.parent_account_id = subscriptions.shipping_address.account_id ```  ``` accounts.shipping_addresses.account_id = subscriptions.shipping_address.account_id ``` |
| [transactions](#transactions) | ``` accounts.id = transactions.account.id ```  ``` accounts.parent_account_id = transactions.account.id ```  ``` accounts.shipping_addresses.account_id = transactions.account.id ```  ``` accounts.id = transactions.account.parent_account_id ```  ``` accounts.parent_account_id = transactions.account.parent_account_id ```  ``` accounts.shipping_addresses.account_id = transactions.account.parent_account_id ``` |

accounts table schema

|  |
| --- |
| **address**  OBJECT This is a nested data structure:   - **city**: STRING - **country**: STRING - **first\_name**: STRING - **last\_name**: STRING - **phone**: STRING - **postal\_code**: STRING - **region**: STRING - **street1**: STRING - **street2**: STRING |
| **bill\_to**  STRING |
| **billing\_info**  OBJECT This is a nested data structure:   - **account\_id**: STRING - **address**: OBJECT, which is also a nested data structure:   - **city**: STRING   - **country**: STRING   - **first\_name**: STRING   - **last\_name**: STRING   - **phone**: STRING   - **postal\_code**: STRING   - **region**: STRING   - **street1**: STRING   - **street2**: STRING - **company**: STRING - **created\_at**: DATE-TIME - **first\_name**: STRING - **fraud**: OBJECT, which is also a nested data structure:   - **decision**: STRING   - **risk\_rules\_triggered**: OBJECT, which is also a nested data structure:     - **score**: INTEGER - **id**: STRING - **last\_name**: STRING - **object**: STRING - **payment\_info**: OBJECT, which is also a nested data structure:   - **card\_type**: STRING   - **exp\_month**: INTEGER   - **exp\_year**: INTEGER   - **first\_six**: STRING   - **last\_four**: STRING   - **object**: STRING - **updated\_at**: DATE-TIME - **updated\_by**: OBJECT, which is also a nested data structure:   - **country**: STRING   - **ip**: STRING - **valid**: BOOLEAN - **vat\_number**: STRING |
| **cc\_emails**  STRING |
| **code**  STRING |
| **company**  STRING |
| **created\_at**  DATE-TIME |
| **custom\_fields**  ARRAY This is a nested data structure:   - **name**: STRING - **value**: STRING |
| **deleted\_at**  DATE-TIME |
| **email**  STRING |
| **exemption\_certificate**  STRING |
| **first\_name**  STRING |
| **hosted\_login\_token**  STRING |
| **id**  STRING |
| **last\_name**  STRING |
| **object**  STRING |
| **parent\_account\_id**  STRING |
| **preferred\_locale**  STRING |
| **shipping\_addresses**  ARRAY This is a nested data structure:   - **account\_id**: STRING - **city**: STRING - **company**: STRING - **country**: STRING - **created\_at**: DATE-TIME - **email**: STRING - **first\_name**: STRING - **id**: STRING - **last\_name**: STRING - **nickname**: STRING - **postal\_code**: STRING - **region**: STRING - **street1**: STRING - **street2**: STRING - **updated\_at**: DATE-TIME - **vat\_number**: STRING |
| **state**  STRING |
| **tax\_exempt**  BOOLEAN |
| **updated\_at**  DATE-TIME |
| **username**  STRING |
| **vat\_number**  STRING |

### adjustments

The `adjustments` table contains info about adjustments, which are credits and charges associated with your customers.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Recurly documentation](https://dev.recurly.com/Content/adjustment-object)  [Recurly API method](https://partner-docs.recurly.com/v2018-08-09#operation/list_account_line_items "Opens in new tab: Recurly API method") |

adjustments table foreign keys

| Join adjustments with | on |
| --- | --- |
| [accounts](#accounts) | ``` adjustments.account.id = accounts.id ```  ``` adjustments.account.parent_account_id = accounts.id ```  ``` adjustments.account.id = accounts.parent_account_id ```  ``` adjustments.account.parent_account_id = accounts.parent_account_id ```  ``` adjustments.account.id = accounts.shipping_addresses.account_id ```  ``` adjustments.account.parent_account_id = accounts.shipping_addresses.account_id ``` |
| [billing\_info](#billing-info) | ``` adjustments.account.id = billing_info.account_id ```  ``` adjustments.account.parent_account_id = billing_info.account_id ``` |
| [coupon\_redemptions](#coupon-redemptions) | ``` adjustments.account.id = coupon_redemptions.account_id ```  ``` adjustments.account.parent_account_id = coupon_redemptions.account_id ``` |
| [invoices](#invoices) | ``` adjustments.account.id = invoices.account.id ```  ``` adjustments.account.parent_account_id = invoices.account.id ```  ``` adjustments.account.id = invoices.account.parent_account_id ```  ``` adjustments.account.parent_account_id = invoices.account.parent_account_id ```  ``` adjustments.account.id = invoices.credit_payments.refund_transaction.account.id ```  ``` adjustments.account.parent_account_id = invoices.credit_payments.refund_transaction.account.id ```  ``` adjustments.account.id = invoices.line_items.data.shipping_addresses.account_id ```  ``` adjustments.account.parent_account_id = invoices.line_items.data.shipping_addresses.account_id ```  ``` adjustments.invoice_id = invoices.id ```  ``` adjustments.invoice_id = invoices.credit_payments.applied_to_invoice.id ```  ``` adjustments.invoice_id = invoices.credit_payments.original_invoice.id ```  ``` adjustments.invoice_id = invoices.credit_payments.refund_transaction.invoice.id ```  ``` adjustments.invoice_id = invoices.credit_payments.refund_transaction.voided_by_invoice.id ```  ``` adjustments.invoice_id = invoices.line_items.data.invoice_id ```  ``` adjustments.invoice_id = invoices.subscription_ids ```  ``` adjustments.plan_id = invoices.line_items.data.plan_id ```  ``` adjustments.add_on_id = invoices.line_items.data.add_on_id ``` |
| [subscriptions](#subscriptions) | ``` adjustments.account.id = subscriptions.shipping_address.account_id ```  ``` adjustments.account.parent_account_id = subscriptions.shipping_address.account_id ```  ``` adjustments.plan_id = subscriptions.pending_change.plan.id ```  ``` adjustments.add_on_id = subscriptions.add_ons.add_on.id ``` |
| [transactions](#transactions) | ``` adjustments.account.id = transactions.account.id ```  ``` adjustments.account.parent_account_id = transactions.account.id ```  ``` adjustments.account.id = transactions.account.parent_account_id ```  ``` adjustments.account.parent_account_id = transactions.account.parent_account_id ```  ``` adjustments.invoice_id = transactions.invoice.id ```  ``` adjustments.invoice_id = transactions.voided_by_invoice.id ``` |
| [plans](#plans) | ``` adjustments.plan_id = plans.id ``` |
| [plans\_add\_ons](#plans-add-ons) | ``` adjustments.plan_id = plans_add_ons.plan_id ```  ``` adjustments.add_on_id = plans_add_ons.id ``` |

adjustments table schema

|  |
| --- |
| **account**  OBJECT This is a nested data structure:   - **bill\_to**: STRING - **code**: STRING - **company**: STRING - **email**: STRING - **first\_name**: STRING - **id**: STRING - **last\_name**: STRING - **parent\_account\_id**: STRING |
| **accounting\_code**  STRING |
| **add\_on\_code**  STRING |
| **add\_on\_id**  STRING |
| **amount**  NUMBER |
| **created\_at**  DATE-TIME |
| **credit\_applied**  NUMBER |
| **credit\_reason\_code**  STRING |
| **currency**  STRING |
| **description**  STRING |
| **discount**  NUMBER |
| **end\_date**  DATE-TIME |
| **id**  STRING |
| **invoice\_id**  STRING |
| **invoice\_number**  STRING |
| **legacy\_category**  STRING |
| **object**  STRING |
| **origin**  STRING |
| **original\_line\_item\_invoice\_id**  STRING |
| **plan\_code**  STRING |
| **plan\_id**  STRING |
| **previous\_line\_item\_id**  STRING |
| **product\_code**  STRING |
| **proration\_rate**  NUMBER |
| **quantity**  INTEGER |
| **refund**  BOOLEAN |
| **refunded\_quantity**  INTEGER |
| **shipping\_address**  OBJECT This is a nested data structure:   - **account\_id**: STRING - **city**: STRING - **company**: STRING - **country**: STRING - **created\_at**: DATE-TIME - **email**: STRING - **first\_name**: STRING - **id**: STRING - **last\_name**: STRING - **nickname**: STRING - **phone**: STRING - **postal\_code**: STRING - **region**: STRING - **street1**: STRING - **street2**: STRING - **updated\_at**: DATE-TIME - **vat\_number**: STRING |
| **start\_date**  DATE-TIME |
| **state**  STRING |
| **subscription\_id**  STRING |
| **subtotal**  NUMBER |
| **tax**  NUMBER |
| **tax\_code**  STRING |
| **tax\_exempt**  BOOLEAN |
| **tax\_info**  STRING |
| **taxable**  BOOLEAN |
| **type**  STRING |
| **unit\_amount**  NUMBER |
| **updated\_at**  DATE-TIME |
| **uuid**  STRING |

### billing\_info

The `billing_info` table contains info about the billing information for [`accounts`](#accounts).

**Note**: To replicate this table, you must also have the [`accounts`](#accounts) table set to replicate.

### Custom fields

Recurly integration supports replicating custom fields for billing info objects.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | account\_id |
| **Replication Key** | updated\_at |
| **Useful links** | [Recurly API method](https://partner-docs.recurly.com/v2018-08-09#operation/get_billing_info "Opens in new tab: Recurly API method") |

billing\_info table foreign keys

| Join billing\_info with | on |
| --- | --- |
| [accounts](#accounts) | ``` billing_info.account_id = accounts.id ```  ``` billing_info.account_id = accounts.parent_account_id ```  ``` billing_info.account_id = accounts.shipping_addresses.account_id ``` |
| [adjustments](#adjustments) | ``` billing_info.account_id = adjustments.account.id ```  ``` billing_info.account_id = adjustments.account.parent_account_id ``` |
| [coupon\_redemptions](#coupon-redemptions) | ``` billing_info.account_id = coupon_redemptions.account_id ``` |
| [invoices](#invoices) | ``` billing_info.account_id = invoices.account.id ```  ``` billing_info.account_id = invoices.account.parent_account_id ```  ``` billing_info.account_id = invoices.credit_payments.refund_transaction.account.id ```  ``` billing_info.account_id = invoices.line_items.data.shipping_addresses.account_id ``` |
| [subscriptions](#subscriptions) | ``` billing_info.account_id = subscriptions.shipping_address.account_id ``` |
| [transactions](#transactions) | ``` billing_info.account_id = transactions.account.id ```  ``` billing_info.account_id = transactions.account.parent_account_id ``` |

billing\_info table schema

|  |
| --- |
| **account\_id**  STRING |
| **address**  OBJECT This is a nested data structure:   - **city**: STRING - **country**: STRING - **first\_name**: STRING - **last\_name**: STRING - **phone**: STRING - **postal\_code**: STRING - **region**: STRING - **street1**: STRING - **street2**: STRING |
| **company**  STRING |
| **created\_at**  DATE-TIME |
| **custom\_fields**  ARRAY This is a nested data structure:   - **name**: STRING - **value**: STRING |
| **exemption\_certificate**  STRING |
| **first\_name**  STRING |
| **fraud**  OBJECT This is a nested data structure:   - **decision**: STRING - **risk\_rules\_triggered**: OBJECT, which is also a nested data structure:   - **score**: INTEGER |
| **id**  STRING |
| **last\_name**  STRING |
| **object**  STRING |
| **payment\_method**  OBJECT This is a nested data structure:   - **account\_type**: STRING - **card\_type**: STRING - **exp\_month**: INTEGER - **exp\_year**: INTEGER - **last\_four**: STRING - **object**: STRING - **routing\_number**: INTEGER - **routing\_number\_banl**: STRING |
| **updated\_at**  DATE-TIME |
| **updated\_by**  OBJECT This is a nested data structure:   - **country**: STRING - **ip**: STRING |
| **valid**  BOOLEAN |
| **vat\_number**  STRING |

### coupon\_redemptions

The `coupon_redemptions` table contains info about the coupons redeemed in your Recurly account.

**Note**: In order to replicate this table, you must also set the following tables to replicate:

- [accounts](#accounts)
- [subscription](#subscription)
- [invoices](#invoices)

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | created\_at |
|  | accounts  subscription  invoices |
| **Useful links** | [Recurly API method](https://recurly.com/developers/api/v2018-08-09/index.html#operation/list_account_coupon_redemptions "Opens in new tab: Recurly API method") |

coupon\_redemptions table foreign keys

| Join coupon\_redemptions with | on |
| --- | --- |
| [accounts](#accounts) | ``` coupon_redemptions.account_id = accounts.id ```  ``` coupon_redemptions.account_id = accounts.parent_account_id ```  ``` coupon_redemptions.account_id = accounts.shipping_addresses.account_id ``` |
| [adjustments](#adjustments) | ``` coupon_redemptions.account_id = adjustments.account.id ```  ``` coupon_redemptions.account_id = adjustments.account.parent_account_id ``` |
| [billing\_info](#billing-info) | ``` coupon_redemptions.account_id = billing_info.account_id ``` |
| [invoices](#invoices) | ``` coupon_redemptions.account_id = invoices.account.id ```  ``` coupon_redemptions.account_id = invoices.account.parent_account_id ```  ``` coupon_redemptions.account_id = invoices.credit_payments.refund_transaction.account.id ```  ``` coupon_redemptions.account_id = invoices.line_items.data.shipping_addresses.account_id ``` |
| [subscriptions](#subscriptions) | ``` coupon_redemptions.account_id = subscriptions.shipping_address.account_id ```  ``` coupon_redemptions.coupon.id = subscriptions.coupon_redemptions.coupon.id ```  ``` coupon_redemptions.id = subscriptions.coupon_redemptions.id ``` |
| [transactions](#transactions) | ``` coupon_redemptions.account_id = transactions.account.id ```  ``` coupon_redemptions.account_id = transactions.account.parent_account_id ``` |
| [coupons](#coupons) | ``` coupon_redemptions.coupon.id = coupons.id ``` |

coupon\_redemptions table schema

|  |
| --- |
| **account**  OBJECT This is a nested data structure:   - **bill\_to**: STRING - **code**: STRING - **company**: STRING - **email**: STRING - **first\_name**: STRING - **id**: STRING - **last\_name**: STRING - **object**: STRING - **parent\_account\_id**: STRING |
| **account\_id**  STRING |
| **coupon**  OBJECT This is a nested data structure:   - **applies\_to\_all\_plans**: BOOLEAN - **applies\_to\_non\_plan\_charges**: BOOLEAN - **code**: STRING - **coupon\_type**: STRING - **created\_at**: DATE-TIME - **discount**: OBJECT, which is also a nested data structure:   - **currencies**: ARRAY, which is also a nested data structure:     - **amount**: NUMBER     - **currency**: STRING   - **percent**: INTEGER   - **trial**: OBJECT, which is also a nested data structure:     - **length**: INTEGER     - **unit**: STRING- **type**: STRING - **duration**: STRING - **expired\_at**: DATE-TIME - **free\_trial\_amount**: INTEGER - **free\_trial\_unit**: STRING - **hosted\_page\_description**: STRING - **id**: STRING - **invoice\_description**: STRING - **max\_redemptions**: INTEGER - **max\_redemptions\_per\_account**: INTEGER - **name**: STRING - **object**: STRING - **plans**: STRING - **plans\_names**: ARRAY - **redeem\_by**: DATE-TIME - **redemption\_resource**: STRING - **state**: STRING - **temporal\_amount**: INTEGER - **temporal\_unit**: STRING - **unique\_coupon\_codes\_count**: INTEGER - **updated\_at**: DATE-TIME |
| **created\_at**  DATE-TIME |
| **currency**  STRING |
| **discounted**  STRING |
| **id**  STRING |
| **object**  STRING |
| **removed\_at**  DATE-TIME |
| **state**  STRING |
| **unique\_code\_template**  STRING |
| **updated\_at**  DATE-TIME |

### coupons

The `coupons` table contains info about the coupons available in your Recurly account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Recurly API method](https://partner-docs.recurly.com/v2018-08-09#operation/list_coupons "Opens in new tab: Recurly API method") |

coupons table foreign keys

| Join coupons with | on |
| --- | --- |
| [coupon\_redemptions](#coupon-redemptions) | ``` coupons.id = coupon_redemptions.coupon.id ``` |
| [subscriptions](#subscriptions) | ``` coupons.id = subscriptions.coupon_redemptions.coupon.id ``` |

coupons table schema

|  |
| --- |
| **applies\_to\_all\_plans**  BOOLEAN |
| **applies\_to\_non\_plan\_charges**  BOOLEAN |
| **code**  STRING |
| **coupon\_type**  STRING |
| **created\_at**  DATE-TIME |
| **discount**  OBJECT This is a nested data structure:   - **currencies**: ARRAY, which is also a nested data structure:   - **amount**: NUMBER   - **currency**: STRING - **percent**: INTEGER - **trial**: OBJECT, which is also a nested data structure:   - **length**: INTEGER   - **unit**: STRING - **type**: STRING |
| **duration**  STRING |
| **expired\_at**  DATE-TIME |
| **free\_trial\_amount**  INTEGER |
| **free\_trial\_unit**  STRING |
| **hosted\_page\_description**  STRING |
| **id**  STRING |
| **invoice\_description**  STRING |
| **max\_redemptions**  INTEGER |
| **max\_redemptions\_per\_account**  INTEGER |
| **name**  STRING |
| **object**  STRING |
| **plans**  ARRAY, STRING This is a nested data structure:   - **code**: STRING - **id**: STRING - **name**: STRING - **object**: STRING |
| **plans\_names**  ARRAY |
| **redeem\_by**  DATE-TIME |
| **redemption\_resource**  STRING |
| **state**  STRING |
| **temporal\_amount**  INTEGER |
| **temporal\_unit**  STRING |
| **unique\_coupon\_codes\_count**  INTEGER |
| **updated\_at**  DATE-TIME |

### invoices

The `invoices` table contains info about the invoices in your Recurly account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Recurly API method](https://recurly.com/developers/api/v2018-08-09/index.html#operation/list_account_invoices "Opens in new tab: Recurly API method") |

invoices table foreign keys

| Join invoices with | on |
| --- | --- |
| [accounts](#accounts) | ``` invoices.account.id = accounts.id ```  ``` invoices.account.parent_account_id = accounts.id ```  ``` invoices.credit_payments.refund_transaction.account.id = accounts.id ```  ``` invoices.line_items.data.shipping_addresses.account_id = accounts.id ```  ``` invoices.account.id = accounts.parent_account_id ```  ``` invoices.account.parent_account_id = accounts.parent_account_id ```  ``` invoices.credit_payments.refund_transaction.account.id = accounts.parent_account_id ```  ``` invoices.line_items.data.shipping_addresses.account_id = accounts.parent_account_id ```  ``` invoices.account.id = accounts.shipping_addresses.account_id ```  ``` invoices.account.parent_account_id = accounts.shipping_addresses.account_id ```  ``` invoices.credit_payments.refund_transaction.account.id = accounts.shipping_addresses.account_id ```  ``` invoices.line_items.data.shipping_addresses.account_id = accounts.shipping_addresses.account_id ``` |
| [adjustments](#adjustments) | ``` invoices.account.id = adjustments.account.id ```  ``` invoices.account.parent_account_id = adjustments.account.id ```  ``` invoices.credit_payments.refund_transaction.account.id = adjustments.account.id ```  ``` invoices.line_items.data.shipping_addresses.account_id = adjustments.account.id ```  ``` invoices.account.id = adjustments.account.parent_account_id ```  ``` invoices.account.parent_account_id = adjustments.account.parent_account_id ```  ``` invoices.credit_payments.refund_transaction.account.id = adjustments.account.parent_account_id ```  ``` invoices.line_items.data.shipping_addresses.account_id = adjustments.account.parent_account_id ```  ``` invoices.id = adjustments.invoice_id ```  ``` invoices.credit_payments.applied_to_invoice.id = adjustments.invoice_id ```  ``` invoices.credit_payments.original_invoice.id = adjustments.invoice_id ```  ``` invoices.credit_payments.refund_transaction.invoice.id = adjustments.invoice_id ```  ``` invoices.credit_payments.refund_transaction.voided_by_invoice.id = adjustments.invoice_id ```  ``` invoices.line_items.data.invoice_id = adjustments.invoice_id ```  ``` invoices.subscription_ids = adjustments.invoice_id ```  ``` invoices.line_items.data.plan_id = adjustments.plan_id ```  ``` invoices.line_items.data.add_on_id = adjustments.add_on_id ``` |
| [billing\_info](#billing-info) | ``` invoices.account.id = billing_info.account_id ```  ``` invoices.account.parent_account_id = billing_info.account_id ```  ``` invoices.credit_payments.refund_transaction.account.id = billing_info.account_id ```  ``` invoices.line_items.data.shipping_addresses.account_id = billing_info.account_id ``` |
| [coupon\_redemptions](#coupon-redemptions) | ``` invoices.account.id = coupon_redemptions.account_id ```  ``` invoices.account.parent_account_id = coupon_redemptions.account_id ```  ``` invoices.credit_payments.refund_transaction.account.id = coupon_redemptions.account_id ```  ``` invoices.line_items.data.shipping_addresses.account_id = coupon_redemptions.account_id ``` |
| [subscriptions](#subscriptions) | ``` invoices.account.id = subscriptions.shipping_address.account_id ```  ``` invoices.account.parent_account_id = subscriptions.shipping_address.account_id ```  ``` invoices.credit_payments.refund_transaction.account.id = subscriptions.shipping_address.account_id ```  ``` invoices.line_items.data.shipping_addresses.account_id = subscriptions.shipping_address.account_id ```  ``` invoices.line_items.data.plan_id = subscriptions.pending_change.plan.id ```  ``` invoices.line_items.data.add_on_id = subscriptions.add_ons.add_on.id ```  ``` invoices.credit_payments.refund_transaction.subscription_ids = subscriptions.id ```  ``` invoices.line_items.data.subscription_id = subscriptions.id ```  ``` invoices.credit_payments.refund_transaction.subscription_ids = subscriptions.add_ons.subscription_id ```  ``` invoices.line_items.data.subscription_id = subscriptions.add_ons.subscription_id ```  ``` invoices.credit_payments.refund_transaction.subscription_ids = subscriptions.pending_change.add_ons.subscription_id ```  ``` invoices.line_items.data.subscription_id = subscriptions.pending_change.add_ons.subscription_id ```  ``` invoices.credit_payments.refund_transaction.subscription_ids = subscriptions.pending_change.subscription_id ```  ``` invoices.line_items.data.subscription_id = subscriptions.pending_change.subscription_id ``` |
| [transactions](#transactions) | ``` invoices.account.id = transactions.account.id ```  ``` invoices.account.parent_account_id = transactions.account.id ```  ``` invoices.credit_payments.refund_transaction.account.id = transactions.account.id ```  ``` invoices.line_items.data.shipping_addresses.account_id = transactions.account.id ```  ``` invoices.account.id = transactions.account.parent_account_id ```  ``` invoices.account.parent_account_id = transactions.account.parent_account_id ```  ``` invoices.credit_payments.refund_transaction.account.id = transactions.account.parent_account_id ```  ``` invoices.line_items.data.shipping_addresses.account_id = transactions.account.parent_account_id ```  ``` invoices.id = transactions.invoice.id ```  ``` invoices.credit_payments.applied_to_invoice.id = transactions.invoice.id ```  ``` invoices.credit_payments.original_invoice.id = transactions.invoice.id ```  ``` invoices.credit_payments.refund_transaction.invoice.id = transactions.invoice.id ```  ``` invoices.credit_payments.refund_transaction.voided_by_invoice.id = transactions.invoice.id ```  ``` invoices.line_items.data.invoice_id = transactions.invoice.id ```  ``` invoices.subscription_ids = transactions.invoice.id ```  ``` invoices.id = transactions.voided_by_invoice.id ```  ``` invoices.credit_payments.applied_to_invoice.id = transactions.voided_by_invoice.id ```  ``` invoices.credit_payments.original_invoice.id = transactions.voided_by_invoice.id ```  ``` invoices.credit_payments.refund_transaction.invoice.id = transactions.voided_by_invoice.id ```  ``` invoices.credit_payments.refund_transaction.voided_by_invoice.id = transactions.voided_by_invoice.id ```  ``` invoices.line_items.data.invoice_id = transactions.voided_by_invoice.id ```  ``` invoices.subscription_ids = transactions.voided_by_invoice.id ```  ``` invoices.credit_payments.refund_transaction.subscription_ids = transactions.subscription_ids ```  ``` invoices.line_items.data.subscription_id = transactions.subscription_ids ```  ``` invoices.credit_payments.refund_transaction.id = transactions.id ```  ``` invoices.credit_payments.refund_transaction.original_transaction_id = transactions.id ```  ``` invoices.transactions.id = transactions.id ```  ``` invoices.credit_payments.refund_transaction.id = transactions.original_transaction_id ```  ``` invoices.credit_payments.refund_transaction.original_transaction_id = transactions.original_transaction_id ```  ``` invoices.transactions.id = transactions.original_transaction_id ``` |
| [plans](#plans) | ``` invoices.line_items.data.plan_id = plans.id ``` |
| [plans\_add\_ons](#plans-add-ons) | ``` invoices.line_items.data.plan_id = plans_add_ons.plan_id ```  ``` invoices.line_items.data.add_on_id = plans_add_ons.id ``` |

invoices table schema

|  |
| --- |
| **account**  OBJECT This is a nested data structure:   - **bill\_to**: STRING - **code**: STRING - **company**: STRING - **email**: STRING - **first\_name**: STRING - **id**: STRING - **last\_name**: STRING - **object**: STRING - **parent\_account\_id**: STRING |
| **address**  OBJECT This is a nested data structure:   - **city**: STRING - **company**: STRING - **country**: STRING - **first\_name**: STRING - **last\_name**: STRING - **name\_on\_account**: STRING - **phone**: STRING - **postal\_code**: STRING - **region**: STRING - **street1**: STRING - **street2**: STRING |
| **balance**  NUMBER |
| **closed\_at**  DATE-TIME |
| **collection\_method**  STRING |
| **created\_at**  DATE-TIME |
| **credit\_payments**  ARRAY This is a nested data structure:   - **account**: OBJECT, which is also a nested data structure:   - **code**: STRING   - **company**: STRING   - **email**: STRING   - **first\_name**: STRING   - **id**: STRING   - **last\_name**: STRING   - **object**: STRING - **action**: STRING - **amount**: NUMBER - **applied\_to\_invoice**: OBJECT   - **id**: STRING   - **number**: STRING   - **object**: STRING   - **state**: STRING   - **type**: STRING - **created\_at**: DATE-TIME - **currency**: STRING - **id**: STRING - **object**: STRING - **original\_credit\_payment\_id**: STRING - **original\_invoice**: OBJECT, which is also a nested data structure:   - **id**: STRING   - **number**: STRING   - **object**: STRING   - **state**: STRING   - **type**: STRING - **refund\_transaction**: OBJECT, which is also a nested data structure:   - **account**: OBJECT, which is also a nested data structure:     - **code**: STRING     - **company**: STRING     - **email**: STRING     - **first\_name**: STRING     - **id**: STRING     - **last\_name**: STRING     - **object**: STRING   - **amount**: NUMBER   - **avs\_check**: STRING   - **billing\_address**: OBJECT, which is also a nested data structure:     - **city**: STRING     - **country**: STRING     - **first\_name**: STRING     - **last\_name**: STRING     - **phone**: STRING     - **postal\_code**: STRING     - **region**: STRING     - **street1**: STRING     - **street2**: STRING   - **collected\_at**: DATE-TIME   - **collection\_method**: STRING   - **created\_at**: DATE-TIME   - **currency**: STRING   - **customer\_message**: STRING   - **customer\_message\_locale**: STRING   - **cvv\_check**: STRING   - **gateway\_approval\_code**: STRING   - **gateway\_message**: STRING   - **gateway\_reference**: STRING   - **gateway\_response\_code**: STRING   - **gateway\_response\_time**: STRING   - **gateway\_response\_values**: OBJECT, which is also a nested data structure.   - **id**: STRING   - **invoice**: OBJECT, which is also a nested data structure:     - **id**: STRING     - **number**: STRING     - **object**: STRING     - **state**: STRING     - **type**: STRING   - **ip\_address\_country**: STRING   - **ip\_address\_v4**: STRING   - **object**: STRING   - **origin**: STRING   - **original\_transaction\_id**: STRING   - **payment\_gateway**: OBJECT, which is also a nested data structure:     - **id**: STRING     - **name**: STRING     - **object**: STRING     - **type**: STRING   - **payment\_method**: OBJECT, which is also a nested data structure:     - **card\_type**: STRING     - **exp\_month**: INTEGER     - **exp\_year**: INTEGER     - **first\_six**: STRING     - **last\_four**: STRING     - **object**: STRING   - **refunded**: BOOLEAN   - **status**: STRING   - **status\_code**: STRING   - **status\_message**: STRING   - **subscription\_ids**: ARRAY, which is also a nested data structure.   - **success**: BOOLEAN   - **type**: STRING   - **uuid**: STRING   - **voided\_at**: DATE-TIME   - **voided\_by\_invoice**: OBJECT     - **id**: STRING     - **number**: STRING     - **object**: STRING     - **state**: STRING     - **type**: STRING - **updated\_at**: DATE-TIME - **uuid**: STRING - **voided\_at**: DATE-TIME |
| **currency**  STRING |
| **customer\_notes**  STRING |
| **discount**  NUMBER |
| **due\_at**  DATE-TIME |
| **id**  STRING |
| **line\_items**  OBJECT This is a nested data structure:   - **data**: ARRAY, which is also a nested data structure:   - **account**: OBJECT, which is also a nested data structure:     - **bill\_to**: STRING     - **code**: STRING     - **company**: STRING     - **email**: STRING     - **first\_name**: STRING     - **id**: STRING     - **last\_name**: STRING     - **object**: STRING     - **parent\_account\_id**: STRING   - **accounting\_code**: STRING   - **add\_on\_code**: STRING   - **add\_on\_id**: STRING   - **amount**: NUMBER   - **created\_at**: DATE-TIME   - **credit\_applied**: NUMBER   - **credit\_reason\_code**: STRING   - **currency**: STRING   - **description**: STRING   - **discount**: NUMBER   - **end\_date**: DATE-TIME   - **id**: STRING   - **invoice\_id**: STRING   - **invoice\_number**: STRING   - **legacy\_category**: STRING   - **object**: STRING   - **origin**: STRING   - **original\_line\_item\_invoice\_id**: STRING   - **plan\_code**: STRING   - **plan\_id**: STRING   - **previous\_line\_item\_id**: STRING   - **product\_code**: STRING   - **proration\_rate**: NUMBER   - **quantity**: INTEGER   - **refund**: BOOLEAN   - **refunded\_quantity**: INTEGER   - **shipping\_addresses**: ARRAY, which is also a nested data structure:     - **account\_id**: STRING     - **city**: STRING     - **company**: STRING     - **country**: STRING     - **created\_at**: DATE-TIME     - **email**: STRING     - **first\_name**: STRING     - **id**: STRING     - **last\_name**: STRING     - **nickname**: STRING     - **phone**: STRING     - **postal\_code**: STRING     - **region**: STRING     - **street1**: STRING     - **street2**: STRING     - **updated\_at**: DATE-TIME     - **vat\_number**: STRING   - **start\_date**: DATE-TIME   - **state**: STRING   - **subscription\_id**: STRING   - **subtotal**: NUMBER   - **tax**: NUMBER   - **tax\_code**: STRING   - **tax\_exempt**: STRING   - **tax\_info**: OBJECT, which is also a nested data structure:     - **rate**: NUMBER     - **region**: STRING     - **type**: STRING   - **taxable**: BOOLEAN   - **type**: STRING   - **unit\_amount**: NUMBER   - **updated\_at**: DATE-TIME   - **uuid**: STRING - **has\_more**: BOOLEAN - **next**: STRING - **object**: STRING |
| **net\_terms**  NUMBER |
| **number**  STRING |
| **object**  STRING |
| **origin**  STRING |
| **paid**  NUMBER |
| **po\_number**  STRING |
| **previous\_invoice\_id**  STRING |
| **refundable\_amount**  NUMBER |
| **state**  STRING |
| **subscription\_ids**  ARRAY |
| **subtotal**  NUMBER |
| **tax**  NUMBER |
| **tax\_info**  OBJECT This is a nested data structure:   - **rate**: NUMBER - **region**: STRING - **type**: STRING |
| **terms\_and\_conditions**  STRING |
| **total**  NUMBER |
| **transactions**  ARRAY This is a nested data structure:   - **account**: OBJECT, which is also a nested data structure:   - **bill\_to**: STRING   - **code**: STRING   - **company**: STRING   - **email**: STRING   - **first\_name**: STRING   - **id**: STRING   - **last\_name**: STRING   - **object**: STRING   - **parent\_account\_id**: STRING - **amount**: NUMBER - **avs\_check**: STRING - **billing\_address**: OBJECT   - **city**: STRING   - **country**: STRING   - **first\_name**: STRING   - **last\_name**: STRING   - **phone**: STRING   - **postal\_code**: STRING   - **region**: STRING   - **street1**: STRING   - **street2**: STRING - **collected\_at**: DATE-TIME - **collection\_method**: STRING - **created\_at**: DATE-TIME - **currency**: STRING - **customer\_message**: STRING - **customer\_message\_locale**: STRING - **cvv\_check**: STRING - **gateway\_approval\_code**: STRING - **gateway\_message**: STRING - **gateway\_reference**: STRING - **gateway\_response\_code**: STRING - **gateway\_response\_time**: NUMBER - **gateway\_response\_values**: OBJECT, which is also a nested data structure. - **id**: STRING - **invoice**: OBJECT, which is also a nested data structure:   - **id**: STRING   - **number**: STRING   - **object**: STRING   - **state**: STRING   - **type**: STRING - **ip\_address\_country**: STRING - **ip\_address\_v4**: STRING - **object**: STRING - **origin**: STRING - **original\_transaction\_id**: STRING - **payment\_gateway**: OBJECT, which is also a nested data structure:   - **id**: STRING   - **name**: STRING   - **object**: STRING   - **type**: STRING - **payment\_method**: OBJECT, which is also a nested data structure:   - **card\_type**: STRING   - **exp\_month**: INTEGER   - **exp\_year**: INTEGER   - **first\_six**: STRING   - **last\_four**: STRING   - **object**: STRING - **refunded**: BOOLEAN - **status**: STRING - **status\_code**: STRING - **status\_message**: STRING - **subscription\_ids**: ARRAY - **success**: BOOLEAN - **type**: STRING - **uuid**: STRING - **voided\_at**: DATE-TIME - **voided\_by\_invoice**: OBJECT, which is also a nested data structure:   - **id**: STRING   - **number**: STRING   - **object**: STRING   - **state**: STRING   - **type**: STRING |
| **type**  STRING |
| **updated\_at**  DATE-TIME |
| **vat\_number**  STRING |
| **vat\_reverse\_charge\_notes**  STRING |

### plans

The `plans` table contains info about the plans in your Recurly account. A plan tells Recurly how much to charge customers.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Recurly API method](https://partner-docs.recurly.com/v2018-08-09#operation/list_plans "Opens in new tab: Recurly API method") |

plans table foreign keys

| Join plans with | on |
| --- | --- |
| [adjustments](#adjustments) | ``` plans.id = adjustments.plan_id ``` |
| [invoices](#invoices) | ``` plans.id = invoices.line_items.data.plan_id ``` |
| [plans\_add\_ons](#plans-add-ons) | ``` plans.id = plans_add_ons.plan_id ``` |
| [subscriptions](#subscriptions) | ``` plans.id = subscriptions.pending_change.plan.id ``` |

plans table schema

|  |
| --- |
| **accounting\_code**  STRING |
| **auto\_renew**  BOOLEAN |
| **code**  STRING |
| **created\_at**  DATE-TIME |
| **currencies**  ARRAY This is a nested data structure:   - **currency**: STRING - **setup\_free**: NUMBER - **unit\_amount**: NUMBER |
| **deleted\_at**  DATE-TIME |
| **description**  STRING |
| **hosted\_pages**  OBJECT This is a nested data structure:   - **bypass\_confirmation**: BOOLEAN - **cancel\_url**: STRING - **display\_quantity**: BOOLEAN - **success\_url**: STRING |
| **id**  STRING |
| **interval\_length**  INTEGER |
| **interval\_unit**  STRING |
| **name**  STRING |
| **object**  STRING |
| **setup\_fee\_accounting\_code**  STRING |
| **state**  STRING |
| **tax\_code**  STRING |
| **tax\_exempt**  BOOLEAN |
| **total\_billing\_cycles**  INTEGER |
| **trial\_length**  INTEGER |
| **trial\_unit**  STRING |
| **updated\_at**  DATE-TIME |

### plans\_add\_ons

The `plans_add_ons` table contains info about the add-ons in your Recurly account. An add-on is a charge billed each billing period in addition to a subscription’s base charge.

**Note**: To replicate this table, you must also have the [`plans`](#plans) table set to replicate.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Recurly API method](https://partner-docs.recurly.com/v2018-08-09#operation/list_plan_add_ons "Opens in new tab: Recurly API method") |

plans\_add\_ons table foreign keys

| Join plans\_add\_ons with | on |
| --- | --- |
| [adjustments](#adjustments) | ``` plans_add_ons.plan_id = adjustments.plan_id ```  ``` plans_add_ons.id = adjustments.add_on_id ``` |
| [invoices](#invoices) | ``` plans_add_ons.plan_id = invoices.line_items.data.plan_id ```  ``` plans_add_ons.id = invoices.line_items.data.add_on_id ``` |
| [plans](#plans) | ``` plans_add_ons.plan_id = plans.id ``` |
| [subscriptions](#subscriptions) | ``` plans_add_ons.plan_id = subscriptions.pending_change.plan.id ```  ``` plans_add_ons.id = subscriptions.add_ons.add_on.id ``` |

plans\_add\_ons table schema

|  |
| --- |
| **accounting\_code**  STRING |
| **code**  STRING |
| **created\_at**  DATE-TIME |
| **currencies**  ARRAY This is a nested data structure:   - **currency**: STRING - **unit\_amount**: NUMBER |
| **default\_quantity**  INTEGER |
| **deleted\_at**  DATE-TIME |
| **display\_quantity**  BOOLEAN |
| **id**  STRING |
| **name**  STRING |
| **object**  STRING |
| **plan\_id**  STRING |
| **state**  STRING |
| **tax\_code**  STRING |
| **updated\_at**  DATE-TIME |

### subscriptions

The `subscriptions` table contains info about the subscriptions in your Recurly account. Subscriptions are created when your customers subscribe to one of your plans. The customer’s subscription tells Recurly when and how much to bill the customer.

### Custom fields

Recurly integration supports replicating custom fields for subscription objects.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Recurly API method](https://partner-docs.recurly.com/v2018-08-09#operation/list_subscriptions "Opens in new tab: Recurly API method") |

subscriptions table foreign keys

| Join subscriptions with | on |
| --- | --- |
| [accounts](#accounts) | ``` subscriptions.shipping_address.account_id = accounts.id ```  ``` subscriptions.shipping_address.account_id = accounts.parent_account_id ```  ``` subscriptions.shipping_address.account_id = accounts.shipping_addresses.account_id ``` |
| [adjustments](#adjustments) | ``` subscriptions.shipping_address.account_id = adjustments.account.id ```  ``` subscriptions.shipping_address.account_id = adjustments.account.parent_account_id ```  ``` subscriptions.pending_change.plan.id = adjustments.plan_id ```  ``` subscriptions.add_ons.add_on.id = adjustments.add_on_id ``` |
| [billing\_info](#billing-info) | ``` subscriptions.shipping_address.account_id = billing_info.account_id ``` |
| [coupon\_redemptions](#coupon-redemptions) | ``` subscriptions.shipping_address.account_id = coupon_redemptions.account_id ```  ``` subscriptions.coupon_redemptions.coupon.id = coupon_redemptions.coupon.id ```  ``` subscriptions.coupon_redemptions.id = coupon_redemptions.id ``` |
| [invoices](#invoices) | ``` subscriptions.shipping_address.account_id = invoices.account.id ```  ``` subscriptions.shipping_address.account_id = invoices.account.parent_account_id ```  ``` subscriptions.shipping_address.account_id = invoices.credit_payments.refund_transaction.account.id ```  ``` subscriptions.shipping_address.account_id = invoices.line_items.data.shipping_addresses.account_id ```  ``` subscriptions.pending_change.plan.id = invoices.line_items.data.plan_id ```  ``` subscriptions.add_ons.add_on.id = invoices.line_items.data.add_on_id ```  ``` subscriptions.id = invoices.credit_payments.refund_transaction.subscription_ids ```  ``` subscriptions.add_ons.subscription_id = invoices.credit_payments.refund_transaction.subscription_ids ```  ``` subscriptions.pending_change.add_ons.subscription_id = invoices.credit_payments.refund_transaction.subscription_ids ```  ``` subscriptions.pending_change.subscription_id = invoices.credit_payments.refund_transaction.subscription_ids ```  ``` subscriptions.id = invoices.line_items.data.subscription_id ```  ``` subscriptions.add_ons.subscription_id = invoices.line_items.data.subscription_id ```  ``` subscriptions.pending_change.add_ons.subscription_id = invoices.line_items.data.subscription_id ```  ``` subscriptions.pending_change.subscription_id = invoices.line_items.data.subscription_id ``` |
| [transactions](#transactions) | ``` subscriptions.shipping_address.account_id = transactions.account.id ```  ``` subscriptions.shipping_address.account_id = transactions.account.parent_account_id ```  ``` subscriptions.id = transactions.subscription_ids ```  ``` subscriptions.add_ons.subscription_id = transactions.subscription_ids ```  ``` subscriptions.pending_change.add_ons.subscription_id = transactions.subscription_ids ```  ``` subscriptions.pending_change.subscription_id = transactions.subscription_ids ``` |
| [coupons](#coupons) | ``` subscriptions.coupon_redemptions.coupon.id = coupons.id ``` |
| [plans](#plans) | ``` subscriptions.pending_change.plan.id = plans.id ``` |
| [plans\_add\_ons](#plans-add-ons) | ``` subscriptions.pending_change.plan.id = plans_add_ons.plan_id ```  ``` subscriptions.add_ons.add_on.id = plans_add_ons.id ``` |

subscriptions table schema

|  |
| --- |
| **account**  OBJECT This is a nested data structure:   - **bill\_to**: STRING - **code**: STRING - **company**: STRING - **email**: STRING - **first\_name**: STRING - **id**: STRING - **last\_name**: STRING - **object**: STRING - **parent\_account\_id**: STRING |
| **activated\_at**  DATE-TIME |
| **add\_ons**  ARRAY This is a nested data structure:   - **add\_on**: OBJECT   - **accounting\_code**: STRING   - **code**: STRING   - **id**: STRING   - **name**: STRING   - **object**: STRING - **created\_at**: DATE-TIME - **expired\_at**: DATE-TIME - **id**: STRING - **object**: STRING - **quantity**: NUMBER - **subscription\_id**: STRING - **unit\_amount**: NUMBER - **updated\_at**: DATE-TIME |
| **add\_ons\_total**  NUMBER |
| **auto\_renew**  BOOLEAN |
| **bank\_account\_authorized\_at**  DATE-TIME |
| **canceled\_at**  DATE-TIME |
| **collection\_method**  STRING |
| **coupon\_redemptions**  ARRAY This is a nested data structure:   - **coupon**: OBJECT, which is also a nested data structure:   - **code**: STRING   - **coupon\_type**: STRING   - **discount**: OBJECT, which is also a nested data structure:     - **currencies**: ARRAY, which is also a nested data structure:       - **amount**: NUMBER       - **currency**: STRING     - **percent**: INTEGER     - **discount**: OBJECT, which is also a nested data structure:       - **trial**: OBJECT, , which is also a nested data structure:         - **length**: NUMBER         - **unit**: STRING       - **type**: STRING   - **expired\_at**: DATE-TIME   - **id**: STRING   - **name**: STRING   - **object**: STRING   - **state**: STRING - **created\_at**: DATE-TIME - **discounted**: STRING - **id**: STRING - **object**: STRING - **state**: STRING |
| **created\_at**  DATE-TIME |
| **currency**  STRING |
| **current\_period\_ends\_at**  DATE-TIME |
| **current\_period\_started\_at**  DATE-TIME |
| **current\_term\_ends\_at**  DATE-TIME |
| **current\_term\_started\_at**  DATE-TIME |
| **custom\_fields**  ARRAY This is a nested data structure:   - **name**: STRING - **value**: STRING |
| **customer\_notes**  STRING |
| **expiration\_reason**  STRING |
| **expires\_at**  DATE-TIME |
| **id**  STRING |
| **net\_terms**  INTEGER |
| **object**  STRING |
| **paused\_at**  DATE-TIME |
| **pending\_change**  OBJECT This is a nested data structure:   - **activate\_at**: DATE-TIME - **activated**: BOOLEAN - **add\_ons**: ARRAY, which is also a nested data structure:   - **add\_on**: OBJECT, which is also a nested data structure:     - **accounting\_code**: STRING     - **code**: STRING     - **id**: STRING     - **name**: STRING     - **object**: STRING   - **created\_at**: DATE-TIME   - **expired\_at**: DATE-TIME   - **id**: STRING   - **object**: STRING   - **quantity**: NUMBER   - **subscription\_id**: STRING   - **unit\_amount**: NUMBER   - **updated\_at**: DATE-TIME - **created\_at**: DATE-TIME - **deleted\_at**: BOOLEAN - **id**: STRING - **object**: STRING - **plan**: OBJECT, which is also a nested data structure:   - **code**: STRING   - **id**: STRING   - **name**: STRING   - **object**: STRING - **quantity**: NUMBER - **subscription\_id**: STRING - **unit\_amount**: NUMBER - **updated\_at**: DATE-TIME |
| **plan**  OBJECT This is a nested data structure:   - **code**: STRING - **id**: STRING - **name**: STRING - **object**: STRING |
| **po\_number**  STRING |
| **quantity**  INTEGER |
| **remaining\_billing\_cycles**  INTEGER |
| **remaining\_pause\_cycles**  INTEGER |
| **renewal\_billing\_cycles**  INTEGER |
| **shipping\_address**  OBJECT This is a nested data structure:   - **account\_id**: STRING - **city**: STRING - **company**: STRING - **country**: STRING - **created\_at**: DATE-TIME - **email**: STRING - **first\_name**: STRING - **id**: STRING - **last\_name**: STRING - **nickname**: STRING - **postal\_code**: STRING - **region**: STRING - **street1**: STRING - **street2**: STRING - **updated\_at**: DATE-TIME - **vat\_number**: STRING |
| **state**  STRING |
| **subtotal**  NUMBER |
| **terms\_and\_conditions**  STRING |
| **total\_billing\_cycles**  INTEGER |
| **trial\_ends\_at**  DATE-TIME |
| **trial\_started\_at**  DATE-TIME |
| **unit\_amount**  NUMBER |
| **updated\_at**  DATE-TIME |
| **uuid**  STRING |

### transactions

The `transactions` table contains info about the transactions in your Recurly account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | collected\_at |
| **Useful links** | [Recurly API method](https://partner-docs.recurly.com/v2018-08-09#operation/list_transactions "Opens in new tab: Recurly API method") |

transactions table foreign keys

| Join transactions with | on |
| --- | --- |
| [accounts](#accounts) | ``` transactions.account.id = accounts.id ```  ``` transactions.account.parent_account_id = accounts.id ```  ``` transactions.account.id = accounts.parent_account_id ```  ``` transactions.account.parent_account_id = accounts.parent_account_id ```  ``` transactions.account.id = accounts.shipping_addresses.account_id ```  ``` transactions.account.parent_account_id = accounts.shipping_addresses.account_id ``` |
| [adjustments](#adjustments) | ``` transactions.account.id = adjustments.account.id ```  ``` transactions.account.parent_account_id = adjustments.account.id ```  ``` transactions.account.id = adjustments.account.parent_account_id ```  ``` transactions.account.parent_account_id = adjustments.account.parent_account_id ```  ``` transactions.invoice.id = adjustments.invoice_id ```  ``` transactions.voided_by_invoice.id = adjustments.invoice_id ``` |
| [billing\_info](#billing-info) | ``` transactions.account.id = billing_info.account_id ```  ``` transactions.account.parent_account_id = billing_info.account_id ``` |
| [coupon\_redemptions](#coupon-redemptions) | ``` transactions.account.id = coupon_redemptions.account_id ```  ``` transactions.account.parent_account_id = coupon_redemptions.account_id ``` |
| [invoices](#invoices) | ``` transactions.account.id = invoices.account.id ```  ``` transactions.account.parent_account_id = invoices.account.id ```  ``` transactions.account.id = invoices.account.parent_account_id ```  ``` transactions.account.parent_account_id = invoices.account.parent_account_id ```  ``` transactions.account.id = invoices.credit_payments.refund_transaction.account.id ```  ``` transactions.account.parent_account_id = invoices.credit_payments.refund_transaction.account.id ```  ``` transactions.account.id = invoices.line_items.data.shipping_addresses.account_id ```  ``` transactions.account.parent_account_id = invoices.line_items.data.shipping_addresses.account_id ```  ``` transactions.invoice.id = invoices.id ```  ``` transactions.voided_by_invoice.id = invoices.id ```  ``` transactions.invoice.id = invoices.credit_payments.applied_to_invoice.id ```  ``` transactions.voided_by_invoice.id = invoices.credit_payments.applied_to_invoice.id ```  ``` transactions.invoice.id = invoices.credit_payments.original_invoice.id ```  ``` transactions.voided_by_invoice.id = invoices.credit_payments.original_invoice.id ```  ``` transactions.invoice.id = invoices.credit_payments.refund_transaction.invoice.id ```  ``` transactions.voided_by_invoice.id = invoices.credit_payments.refund_transaction.invoice.id ```  ``` transactions.invoice.id = invoices.credit_payments.refund_transaction.voided_by_invoice.id ```  ``` transactions.voided_by_invoice.id = invoices.credit_payments.refund_transaction.voided_by_invoice.id ```  ``` transactions.invoice.id = invoices.line_items.data.invoice_id ```  ``` transactions.voided_by_invoice.id = invoices.line_items.data.invoice_id ```  ``` transactions.invoice.id = invoices.subscription_ids ```  ``` transactions.voided_by_invoice.id = invoices.subscription_ids ```  ``` transactions.subscription_ids = invoices.credit_payments.refund_transaction.subscription_ids ```  ``` transactions.subscription_ids = invoices.line_items.data.subscription_id ```  ``` transactions.id = invoices.credit_payments.refund_transaction.id ```  ``` transactions.original_transaction_id = invoices.credit_payments.refund_transaction.id ```  ``` transactions.id = invoices.credit_payments.refund_transaction.original_transaction_id ```  ``` transactions.original_transaction_id = invoices.credit_payments.refund_transaction.original_transaction_id ```  ``` transactions.id = invoices.transactions.id ```  ``` transactions.original_transaction_id = invoices.transactions.id ``` |
| [subscriptions](#subscriptions) | ``` transactions.account.id = subscriptions.shipping_address.account_id ```  ``` transactions.account.parent_account_id = subscriptions.shipping_address.account_id ```  ``` transactions.subscription_ids = subscriptions.id ```  ``` transactions.subscription_ids = subscriptions.add_ons.subscription_id ```  ``` transactions.subscription_ids = subscriptions.pending_change.add_ons.subscription_id ```  ``` transactions.subscription_ids = subscriptions.pending_change.subscription_id ``` |

transactions table schema

|  |
| --- |
| **account**  OBJECT This is a nested data structure:   - **bill\_to**: STRING - **code**: STRING - **company**: STRING - **email**: STRING - **first\_name**: STRING - **id**: STRING - **last\_name**: STRING - **object**: STRING - **parent\_account\_id**: STRING |
| **amount**  NUMBER |
| **avs\_check**  STRING |
| **billing\_address**  OBJECT This is a nested data structure:   - **city**: STRING - **country**: STRING - **first\_name**: STRING - **last\_name**: STRING - **phone**: STRING - **postal\_code**: STRING - **region**: STRING - **street1**: STRING - **street2**: STRING |
| **collected\_at**  DATE-TIME |
| **collection\_method**  STRING |
| **created\_at**  DATE-TIME |
| **currency**  STRING |
| **customer\_message**  STRING |
| **customer\_message\_locale**  STRING |
| **cvv\_check**  STRING |
| **gateway\_approval\_code**  STRING |
| **gateway\_message**  STRING |
| **gateway\_reference**  STRING |
| **gateway\_response\_code**  STRING |
| **gateway\_response\_time**  NUMBER |
| **gateway\_response\_values**  OBJECT This is a nested data structure:   - **amount**: NUMBER - **amount\_refunded**: NUMBER - **card\_fingerprint**: STRING - **card\_type**: STRING - **currency**: STRING - **description**: STRING - **livemode**: STRING |
| **id**  STRING |
| **invoice**  OBJECT This is a nested data structure:   - **id**: STRING - **number**: STRING - **object**: STRING - **state**: STRING - **type**: STRING |
| **ip\_address\_country**  STRING |
| **ip\_address\_v4**  STRING |
| **object**  STRING |
| **origin**  STRING |
| **original\_transaction\_id**  STRING |
| **payment\_gateway**  OBJECT This is a nested data structure:   - **id**: STRING - **name**: STRING - **object**: STRING - **type**: STRING |
| **payment\_method**  OBJECT This is a nested data structure:   - **card\_type**: STRING - **exp\_month**: INTEGER - **exp\_year**: INTEGER - **first\_six**: STRING - **last\_four**: STRING - **object**: STRING |
| **refunded**  BOOLEAN |
| **status**  STRING |
| **status\_code**  STRING |
| **status\_message**  STRING |
| **subscription\_ids**  ARRAY |
| **success**  BOOLEAN |
| **type**  STRING |
| **uuid**  STRING |
| **voided\_at**  DATE-TIME |
| **voided\_by\_invoice**  OBJECT This is a nested data structure:   - **id**: STRING - **number**: STRING - **object**: STRING - **state**: STRING - **type**: STRING |
