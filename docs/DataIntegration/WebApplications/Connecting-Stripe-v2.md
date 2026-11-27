---
title: "Stripe"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Stripe-v2.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Stripe

Stripe is a suite of APIs+ powering online payment processing and commerce solutions. You can use Stripe as a data source when landing or replicating data.

It replicates data using the [Stripe REST API](https://stripe.com/Content/api).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To generate your client ID:

1. Log into [Stripe](https://dashboard.stripe.com).
2. In the top right, click the gear wheel and select Settings.
3. Click Connect.
4. Click Onboarding options.
5. Click the OAuth tab to generate your client ID.

To generate your secret key:

1. Click the Developers button in the bottom left corner of the screen.
2. Select the API Keys tab.
3. Click Reveal live key to reveal your secret key.

To redirect the URI:

1. Visit the OAuth page, where you got your Client ID.
2. Make sure Authorized Redirect URIs is set to https://connector.qlik.com/auth/oauth/v3.htm.

## Creating the connection

For more information, see [*Connecting to SaaS applications*](../Landing/connecting-web-applications.htm).

1. Click Authenticate when you have filled in the required connection settings.

   You may be asked to log in to the source application.

   A window is displayed with an authentication code.
2. Copy the code to the clipboard and return to the connection dialog.
3. Paste the code in Complete authentication with the code provided by the source and click Verify.

   Tip noteYou may need to scroll down to see this field.

   When status is Verified, the authentication is verified.
4. Provide a name for the connection in Connection name.
5. Select Open connection metadata to define metadata for the connection when it has been created.

Connection settings

| Setting | Description |
| --- | --- |
| Data gateway | Select a Data Movement gateway if required by your use case.  Information note This field is not available with the Qlik Talend Cloud Starter subscription, as it does not support Data Movement gateway. If you have another subscription tier and do not want to use Data Movement gateway, select None.  For information on the benefits of Data Movement gateway and use cases that require it, see [*Qlik Data Gateway - Data Movement*](../../Gateways/replication-gateway.htm). |
| Start Date | Enter the date, in the format `MM/DD/YYYY`, from which the data must be replicated from your source to your target. |
| Client ID | Client ID. |
| Secret Key | Secret Key. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### balance\_transactions

The `balance_transactions` table contains info about transactions have have contributed to your Stripe account balance, including charges, transfers, etc.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | created |
| **Useful links** | [Stripe documentation](https://stripe.com/Content/api/balance/balance_transaction)  [Stripe API method](https://stripe.com/Content/api/balance/balance_history "Opens in new tab: Stripe API method") |

balance\_transactions table foreign keys

| Join balance\_transactions with | on |
| --- | --- |
| [charges](#charges) | ``` balance_transactions.id = charges.balance_transaction ``` |
| [payouts](#payouts) | ``` balance_transactions.id = payouts.balance_transaction ```  ``` balance_transactions.id = payouts.failure_balance_transaction ``` |
| [transfers](#transfers) | ``` balance_transactions.id = transfers.balance_transaction ```  ``` balance_transactions.id = transfers.failure_balance_transaction ``` |
| [disputes](#disputes) | ``` balance_transactions.id = disputes.balance_transactions.id ``` |

balance\_transactions table schema

|  |
| --- |
| **amount**  INTEGER |
| **available\_on**  INTEGER |
| **created**  DATE-TIME |
| **currency**  STRING |
| **description**  STRING |
| **exchange\_rate**  NUMBER |
| **fee**  INTEGER |
| **fee\_details**  ARRAY This is a nested data structure:   - amount: INTEGER - application: STRING - currency: STRING - description: STRING - type: STRING |
| **id**  STRING |
| **net**  INTEGER |
| **object**  STRING |
| **source**  STRING |
| **sourced\_transfers**  ARRAY |
| **status**  STRING |
| **type**  STRING |
| **updated**  DATE-TIME |

### charges

The `charges` table contains info about charges to credit and debit cards.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | created |
| **Useful links** | [Stripe documentation](https://stripe.com/Content/api/charges/object)  [Stripe API method](https://stripe.com/Content/api/charges/list "Opens in new tab: Stripe API method") |

charges table foreign keys

| Join charges with | on |
| --- | --- |
| [balance\_transactions](#balance-transactions) | ``` charges.balance_transaction = balance_transactions.id ``` |
| [payouts](#payouts) | ``` charges.balance_transaction = payouts.balance_transaction ```  ``` charges.balance_transaction = payouts.failure_balance_transaction ``` |
| [transfers](#transfers) | ``` charges.balance_transaction = transfers.balance_transaction ```  ``` charges.balance_transaction = transfers.failure_balance_transaction ```  ``` charges.source_transfer = transfers.id ``` |
| [disputes](#disputes) | ``` charges.balance_transaction = disputes.balance_transactions.id ```  ``` charges.id = disputes.charge ``` |
| [customers](#customers) | ``` charges.card.id = customers.cards.id ```  ``` charges.source.id = customers.cards.id ```  ``` charges.customer = customers.id ```  ``` charges.card.customer = customers.id ```  ``` charges.customer = customers.cards.customer ```  ``` charges.card.customer = customers.cards.customer ```  ``` charges.customer = customers.discount.customer ```  ``` charges.card.customer = customers.discount.customer ``` |
| [invoices](#invoices) | ``` charges.id = invoices.charge ```  ``` charges.customer = invoices.customer ```  ``` charges.card.customer = invoices.customer ```  ``` charges.customer = invoices.discount.customer ```  ``` charges.card.customer = invoices.discount.customer ```  ``` charges.invoice = invoices.id ``` |
| [invoice\_items](#invoice-items) | ``` charges.customer = invoice_items.customer ```  ``` charges.card.customer = invoice_items.customer ```  ``` charges.invoice = invoice_items.invoice ``` |
| [subscription\_items](#subscription-items) | ``` charges.customer = subscription_items.customer ```  ``` charges.card.customer = subscription_items.customer ``` |
| [subscriptions](#subscriptions) | ``` charges.customer = subscriptions.customer ```  ``` charges.card.customer = subscriptions.customer ``` |
| [invoice\_line\_items](#invoice-line-items) | ``` charges.invoice = invoice_line_items.invoice ``` |

charges table schema

|  |
| --- |
| **amount**  INTEGER |
| **amount\_captured**  INTEGER |
| **amount\_refunded**  INTEGER |
| **application**  STRING |
| **application\_fee**  STRING |
| **application\_fee\_amount**  INTEGER |
| **balance\_transaction**  STRING |
| **billing\_details**  OBJECT This is a nested data structure:   - address: OBJECT, which is also a nested data structure.   - city: STRING   - country: STRING   - line1: STRING   - line2: STRING   - postal\_code: STRING   - state: STRING - email: STRING - name: STRING - phone: STRING |
| **calculated\_statement\_descriptor**  STRING |
| **captured**  BOOLEAN |
| **card**  OBJECT This is a nested data structure:   - address\_city: STRING - address\_country: STRING - address\_line1: STRING - address\_line1\_check: STRING - address\_line2: STRING - address\_state: STRING - address\_zip: STRING - address\_zip\_check: STRING - brand: STRING - country: STRING - customer: STRING - cvc\_check: STRING - dynamic\_last4: STRING - exp\_month: INTEGER - exp\_year: INTEGER - fingerprint - funding: STRING - id: STRING - last4: STRING - metadata: OBJECT - name: STRING - object: STRING - tokenization\_method: STRING - type: STRING |
| **created**  DATE-TIME |
| **currency**  STRING |
| **customer**  STRING |
| **description**  STRING |
| **destination**  STRING |
| **dispute**  STRING |
| **disputed**  BOOLEAN |
| **failure\_code**  STRING |
| **failure\_message**  STRING |
| **fraud\_details**  OBJECT This is a nested data structure:   - stripe\_report: STRING |
| **id**  STRING |
| **invoice**  STRING |
| **livemode**  BOOLEAN |
| **metadata**  OBJECT |
| **object**  STRING |
| **on\_behalf\_of**  STRING |
| **order**  STRING |
| **outcome**  OBJECT This is a nested data structure:   - network\_status: STRING - reason: STRING - risk\_level: STRING - risk\_score: INTEGER - seller\_message: STRING - type: STRING |
| **paid**  BOOLEAN |
| **payment\_intent**  STRING |
| **payment\_method**  STRING |
| **payment\_method\_details**  OBJECT This is a nested data structure:   - ach\_credit\_transfer: OBJECT, which is also a nested data structure.   - account\_number: STRING   - bank\_name: STRING   - routing\_number: STRING   - swift\_code: STRING - ach\_debit: OBJECT, which is also a nested data structure.   - account\_holder\_type: STRING   - bank\_name: STRING   - country: STRING   - fingerprint: STRING   - last4: STRING   - routing\_number: STRING - alipay: OBJECT - bancontact: OBJECT, which is also a nested data structure.   - bank\_code: STRING   - bank\_name: STRING   - bic: STRING   - iban\_last4: STRING   - preferred\_language: STRING   - verified\_name: STRING - card: OBJECT, which is also a nested data structure.   - address\_city: STRING   - address\_country: STRING   - address\_line1: STRING   - address\_line1\_check: STRING   - address\_line2: STRING   - address\_state: STRING   - address\_zip: STRING   - address\_zip\_check: STRING   - brand: STRING   - card\_present: OBJECT, which is also a nested data structure.     - brand: STRING     - country: STRING     - emv\_auth\_data: STRING     - exp\_month: INTEGER     - exp\_year: INTEGER     - fingerprint: STRING     - funding: STRING     - generated\_card: STRING     - last4: STRING     - network: STRING     - read\_method: STRING     - receipt: OBJECT, which is also a nested data structure.       - application\_cryptogram: STRING       - application\_preferred\_name: STRING       - authorization\_code: STRING       - authorization\_response\_code: STRING       - cardholder\_verification\_method: STRING       - dedicated\_file\_name: STRING       - terminal\_verification\_results: STRING       - transaction\_status\_information: STRING   - checks: OBJECT, which is also a nested data structure.     - address\_line1\_check: STRING     - address\_postal\_code\_check: STRING     - cvc\_check: STRING   - country: STRING   - customer: STRING   - cvc\_check: STRING   - dynamic\_last4: STRING   - eps: OBJECT, which is also a nested data structure.     - verified\_name: STRING   - exp\_month: INTEGER   - exp\_year: INTEGER   - fingerprint: STRING   - funding: STRING   - giropay: OBJECT, which is also a nested data structure.     - bank\_code: STRING     - bank\_name: STRING     - bic: STRING     - verified\_name: STRING   - id: STRING   - ideal: OBJECT, which is also a nested data structure.     - bank: STRING     - bic: STRING     - iban\_last4: STRING     - verified\_name: STRING   - installments: OBJECT, which is also a nested data structure.     - plan: OBJECT, which is also a nested data structure.       - count: INTEGER       - interval: STRING       - type: STRING   - klarna: OBJECT   - last4: STRING   - metadata: OBJECT   - multibanco: OBJECT, which is also a nested data structure.     - entity: STRING     - reference: STRING   - name: STRING   - network: STRING   - object: STRING   - p24: OBJECT, which is also a nested data structure.     - reference: STRING     - verified\_name: STRING   - sepa\_debit: OBJECT, which is also a nested data structure.     - bank\_code: STRING     - branch\_code: STRING     - country: STRING     - fingerprint: STRING     - last4: STRING     - mandate: STRING   - sofort: OBJECT, which is also a nested data structure.     - bank\_code: STRING     - bank\_name: STRING     - bic: STRING     - country: STRING     - iban\_last4: STRING     - verified\_name: STRING   - stripe\_account: OBJECT   - three\_d\_secure: OBJECT, which is also a nested data structure.     - authenticated: BOOLEAN     - succeeded: BOOLEAN     - version: STRING   - tokenization\_method: STRING   - type: STRING   - wallet: OBJECT, which is also a nested data structure.     - amex\_express\_checkout: OBJECT     - apple\_pay: OBJECT     - dynamic\_last4: STRING     - google\_pay: OBJECT     - masterpass: OBJECT, which is also a nested data structure.       - billing\_address: OBJECT, which is also a nested data structure.         - city: STRING         - country: STRING         - line1: STRING         - line2: STRING         - postal\_code: STRING         - state: STRING       - email: STRING       - name: STRING       - shipping\_address: OBJECT, which is also a nested data structure.         - city: STRING         - country: STRING         - line1: STRING         - line2: STRING         - postal\_code: STRING         - state: STRING     - samsung\_pay: OBJECT     - type: STRING     - visa\_checkout: OBJECT, which is also a nested data structure.       - billing\_address: OBJECT, which is also a nested data structure.         - city: STRING         - country: STRING         - line1: STRING         - line2: STRING         - postal\_code: STRING         - state: STRING       - email: STRING       - name: STRING       - shipping\_address: OBJECT, which is also a nested data structure.         - city: STRING         - country: STRING         - line1: STRING         - line2: STRING         - postal\_code: STRING         - state: STRING   - wechat: OBJECT - card\_present: OBJECT, which is also a nested data structure.   - amount\_authorized: INTEGER   - brand: STRING   - cardholder\_name: STRING   - country: STRING   - emv\_auth\_data: STRING   - exp\_month: INTEGER   - exp\_year: INTEGER   - fingerprint: STRING   - funding: STRING   - generated\_card: STRING   - last4: STRING   - network: STRING   - overcapture\_supported: BOOLEAN   - read\_method: STRING   - receipt: OBJECT, which is also a nested data structure.     - account\_type: STRING     - application\_cryptogram: STRING     - application\_preferred\_name: STRING     - authorization\_code: STRING     - authorization\_response\_code: STRING     - cardholder\_verification\_method: STRING     - dedicated\_file\_name: STRING     - terminal\_verification\_results: STRING     - transaction\_status\_information: STRING - type: STRING |
| **receipt\_email**  STRING |
| **receipt\_number**  STRING |
| **receipt\_url**  STRING |
| **refunded**  BOOLEAN |
| **refunds**  ARRAY This is a nested data structure:   - amount: INTEGER - balance\_transaction: STRING - charge: STRING - created: DATE-TIME - currency: STRING - description: STRING - failure\_reason: STRING - id: STRING - instructions\_email: STRING - metadata: OBJECT - next\_action: OBJECT, which is also a nested data structure.   - display\_details: OBJECT, which is also a nested data structure.     - email\_sent: OBJECT, which is also a nested data structure.       - email\_sent\_at: DATE-TIME       - email\_sent\_to: STRING     - expires\_at: DATE-TIME   - type: STRING - object: STRING - payment\_intent: STRING - reason: STRING - receipt\_number: STRING - source\_transfer\_reversal: STRING - status: STRING - transfer\_reversal: STRING |
| **review**  STRING |
| **shipping**  OBJECT |
| **source**  OBJECT This is a nested data structure:   - ach\_credit\_transfer: OBJECT, which is also a nested data structure.   - account\_number: STRING   - bank\_name: STRING   - fingerprint: STRING   - refund\_account\_holder\_name: STRING   - refund\_account\_holder\_type: STRING   - refund\_account\_number: STRING   - refund\_routing\_number: STRING   - routing\_number: STRING   - swift\_code: STRING - address\_city: STRING - address\_country: STRING - address\_line1: STRING - address\_line1\_check: STRING - address\_line2: STRING - address\_state: STRING - address\_zip: STRING - address\_zip\_check: STRING - alipay: OBJECT - amount: INTEGER - bancontact: OBJECT - brand: STRING - card: OBJECT, which is also a nested data structure.   - address\_line1\_check: STRING   - address\_zip\_check: STRING   - brand: STRING   - country: STRING   - cvc\_check: STRING   - dynamic\_last4: STRING   - exp\_month: INTEGER   - exp\_year: INTEGER   - fingerprint: STRING   - funding: STRING   - last4: STRING   - name: STRING   - three\_d\_secure: STRING   - tokenization\_method: STRING   - type: STRING - client\_secret: STRING - country: STRING - created: DATE-TIME - currency: STRING - customer: STRING - cvc\_check: STRING - dynamic\_last4: STRING - eps: OBJECT - exp\_month: INTEGER - exp\_year: INTEGER - fingerprint: STRING - flow: STRING - funding: STRING - id: STRING - ideal: OBJECT - last4: STRING - livemode: BOOLEAN - metadata: OBJECT - multibanco: OBJECT - name: STRING - object: STRING - owner: OBJECT, which is also a nested data structure.   - address: OBJECT, which is also a nested data structure.   - email: STRING   - name: STRING   - phone: STRING   - verified\_address: STRING   - verified\_email: STRING   - verified\_name: STRING   - verified\_phone: STRING - receiver: OBJECT, which is also a nested data structure.   - address: STRING   - amount\_charged: INTEGER   - amount\_received: INTEGER   - amount\_returned: INTEGER   - refund\_attributes\_method: STRING   - refund\_attributes\_status: STRING - redirect: OBJECT, which is also a nested data structure.   - failure\_reason: STRING   - return\_url: STRING   - status: STRING   - url: STRING - statement\_descriptor: STRING - status: STRING - tokenization\_method: STRING - type: STRING - usage: STRING |
| **source\_transfer**  STRING |
| **statement\_description**  STRING |
| **statement\_descriptor**  STRING |
| **statement\_descriptor\_suffix**  STRING |
| **status**  STRING |
| **transfer\_data**  OBJECT This is a nested data structure:   - amount: INTEGER - destination: STRING |
| **transfer\_group**  STRING |
| **updated**  DATE-TIME |
| **updated\_by\_event\_type**  STRING |

### coupons

The `coupons` table contains info about percent or amount-off discounts that may be applied to a customer. **Note:** Coupons only apply to invoices; they don’t apply to one-off charges.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | created |
| **Useful links** | [Stripe documentation](https://stripe.com/Content/api/coupons)  [Stripe API method](https://stripe.com/Content/api/coupons/list "Opens in new tab: Stripe API method") |

coupons table foreign keys

| Join coupons with | on |
| --- | --- |
| [customers](#customers) | ``` coupons.id = customers.discount.coupon.id ``` |
| [invoices](#invoices) | ``` coupons.id = invoices.discount.coupon.id ``` |
| [subscriptions](#subscriptions) | ``` coupons.id = subscriptions.discount.coupon.id ``` |

coupons table schema

|  |
| --- |
| **amount\_off**  INTEGER |
| **created**  DATE-TIME |
| **currency**  STRING |
| **duration**  STRING |
| **duration\_in\_months**  INTEGER |
| **id**  STRING |
| **livemode**  BOOLEAN |
| **max\_redemptions**  INTEGER |
| **metadata**  OBJECT |
| **name**  STRING |
| **object**  STRING |
| **percent\_off**  NUMBER |
| **percent\_off\_precise**  NUMBER |
| **redeem\_by**  DATE-TIME |
| **times\_redeemed**  INTEGER |
| **updated**  DATE-TIME |
| **updated\_by\_event\_type**  STRING |
| **valid**  BOOLEAN |

### customers

The `customers` table contains info about your customers.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | created |
| **Useful links** | [Stripe documentation](https://stripe.com/Content/api/customers/object)  [Stripe API method](https://stripe.com/Content/api/customers/list "Opens in new tab: Stripe API method") |

customers table foreign keys

| Join customers with | on |
| --- | --- |
| [charges](#charges) | ``` customers.cards.id = charges.card.id ```  ``` customers.cards.id = charges.source.id ```  ``` customers.id = charges.customer ```  ``` customers.cards.customer = charges.customer ```  ``` customers.discount.customer = charges.customer ```  ``` customers.id = charges.card.customer ```  ``` customers.cards.customer = charges.card.customer ```  ``` customers.discount.customer = charges.card.customer ``` |
| [coupons](#coupons) | ``` customers.discount.coupon.id = coupons.id ``` |
| [invoices](#invoices) | ``` customers.discount.coupon.id = invoices.discount.coupon.id ```  ``` customers.id = invoices.customer ```  ``` customers.cards.customer = invoices.customer ```  ``` customers.discount.customer = invoices.customer ```  ``` customers.id = invoices.discount.customer ```  ``` customers.cards.customer = invoices.discount.customer ```  ``` customers.discount.customer = invoices.discount.customer ```  ``` customers.subscriptions = invoices.subscription ```  ``` customers.discount.subscription = invoices.subscription ```  ``` customers.subscriptions = invoices.discount.subscription ```  ``` customers.discount.subscription = invoices.discount.subscription ``` |
| [subscriptions](#subscriptions) | ``` customers.discount.coupon.id = subscriptions.discount.coupon.id ```  ``` customers.id = subscriptions.customer ```  ``` customers.cards.customer = subscriptions.customer ```  ``` customers.discount.customer = subscriptions.customer ```  ``` customers.subscriptions = subscriptions.id ```  ``` customers.discount.subscription = subscriptions.id ``` |
| [invoice\_items](#invoice-items) | ``` customers.id = invoice_items.customer ```  ``` customers.cards.customer = invoice_items.customer ```  ``` customers.discount.customer = invoice_items.customer ```  ``` customers.subscriptions = invoice_items.subscription ```  ``` customers.discount.subscription = invoice_items.subscription ``` |
| [subscription\_items](#subscription-items) | ``` customers.id = subscription_items.customer ```  ``` customers.cards.customer = subscription_items.customer ```  ``` customers.discount.customer = subscription_items.customer ```  ``` customers.subscriptions = subscription_items.subscription ```  ``` customers.discount.subscription = subscription_items.subscription ``` |
| [invoice\_line\_items](#invoice-line-items) | ``` customers.subscriptions = invoice_line_items.subscription ```  ``` customers.discount.subscription = invoice_line_items.subscription ``` |

customers table schema

|  |
| --- |
| **account\_balance**  INTEGER |
| **address**  OBJECT This is a nested data structure:   - city: STRING - country: STRING - line1: STRING - line2: STRING - postal\_code: STRING - state: STRING |
| **balance**  INTEGER |
| **cards**  ARRAY This is a nested data structure:   - address\_city: STRING - address\_country: STRING - address\_line1: STRING - address\_line1\_check: STRING - address\_line2: STRING - address\_state: STRING - address\_zip: STRING - address\_zip\_check: STRING - brand: STRING - country: STRING - customer: STRING - cvc\_check: STRING - dynamic\_last4: STRING - exp\_month: INTEGER - exp\_year: INTEGER - fingerprint: STRING - funding: STRING - id: STRING - last4: STRING - metadata: STRING - name: STRING - object: STRING - tokenization\_method: STRING - type: STRING |
| **created**  DATE-TIME |
| **currency**  STRING |
| **default\_card**  STRING |
| **default\_source**  STRING |
| **delinquent**  BOOLEAN |
| **description**  STRING |
| **discount**  OBJECT This is a nested data structure:   - checkout\_session: STRING - coupon: OBJECT, which is also a nested data structure.   - amount\_off: INTEGER   - created: DATE-TIME   - currency: STRING   - duration: STRING   - duration\_in\_months: INTEGER   - id: STRING   - livemode: BOOLEAN   - max\_redemptions: INTEGER   - metadata: OBJECT   - name: STRING   - object: STRING   - percent\_off: NUMBER   - percent\_off\_precise: NUMBER   - redeem\_by: DATE-TIME   - times\_redeemed: INTEGER   - valid: BOOLEAN - customer: STRING - end: DATE-TIME - id: STRING - invoice: STRING - invoice\_item: STRING - object: STRING - promotion\_code: STRING - start: DATE-TIME - subscription: STRING |
| **email**  STRING |
| **id**  STRING |
| **invoice\_prefix**  STRING |
| **invoice\_settings**  OBJECT This is a nested data structure:   - custom\_fields: ARRAY - default\_payment\_method: STRING - footer: STRING |
| **livemode**  BOOLEAN |
| **metadata**  OBJECT |
| **name**  STRING |
| **next\_invoice\_sequence**  INTEGER |
| **object**  STRING |
| **phone**  STRING |
| **preferred\_locales**  ARRAY |
| **shipping**  OBJECT This is a nested data structure:   - address: OBJECT, which is also a nested data structure.   - city: STRING   - country: STRING   - line1: STRING   - line2: STRING   - postal\_code: STRING   - state: STRING - name: STRING - phone: STRING |
| **sources**  ARRAY This is a nested data structure:   - ach\_credit\_transfer: OBJECT, which is also a nested data structure.   - account\_number: STRING   - bank\_name: STRING   - fingerprint: STRING   - refund\_account\_holder\_name: STRING   - refund\_account\_holder\_type: STRING   - refund\_account\_number: STRING   - refund\_routing\_number: STRING   - routing\_number: STRING   - swift\_code: STRING - address\_city: STRING - address\_country: STRING - address\_line1: STRING - address\_line1\_check: STRING - address\_line2: STRING - address\_state: STRING - address\_zip: STRING - address\_zip\_check: STRING - alipay: OBJECT - amount: INTEGER - bancontact: OBJECT - brand: STRING - card: OBJECT, which is also a nested data structure.   - address\_line1\_check: STRING   - address\_zip\_check: STRING   - brand: STRING   - country: STRING   - cvc\_check: STRING   - dynamic\_last4: STRING   - exp\_month: INTEGER   - exp\_year: INTEGER   - fingerprint: STRING   - funding: STRING   - last4: STRING   - name: STRING   - three\_d\_secure: STRING   - tokenization\_method: STRING   - type: STRING - client\_secret: STRING - country: STRING - created: DATE-TIME - currency: STRING - customer: STRING - cvc\_check: STRING - dynamic\_last4: STRING - eps: OBJECT - exp\_month: INTEGER - exp\_year: INTEGER - fingerprint: STRING - flow: STRING - funding: STRING - id: STRING - ideal: OBJECT - last4: STRING - livemode: BOOLEAN - metadata: OBJECT - multibanco: OBJECT - name: STRING - object: STRING - owner: OBJECT, which is also a nested data structure.   - address: OBJECT, which is also a nested data structure.     - city: STRING     - country: STRING     - line1: STRING     - line2: STRING     - postal\_code: STRING     - state: STRING   - email: STRING   - name: STRING   - phone: STRING   - verified\_address: STRING   - verified\_email: STRING   - verified\_name: STRING   - verified\_phone: STRING - receiver: OBJECT, which is also a nested data structure.   - address: STRING   - amount\_charged: INTEGER   - amount\_received: INTEGER   - amount\_returned: INTEGER   - refund\_attributes\_method: STRING   - refund\_attributes\_status: STRING - redirect: OBJECT, which is also a nested data structure.   - failure\_reason: STRING   - return\_url: STRING   - status: STRING   - url: STRING - statement\_descriptor: STRING - status: STRING - tokenization\_method: STRING - type: STRING - usage: STRING  ["TYPE", ["NULL", "STRING"]] |
| **subscriptions**  ARRAY |
| **tax\_exempt**  STRING |
| **tax\_ids**  ARRAY This is a nested data structure:   - country: STRING - created: DATE-TIME - customer: STRING - id: STRING - livemode: BOOLEAN - object: STRING - type: STRING - value: STRING - verification: OBJECT, which is also a nested data structure.   - status: STRING   - verified\_address: STRING   - verified\_name: STRING  ["TYPE", ["NULL", "STRING"]] |
| **tax\_info**  STRING |
| **tax\_info\_verification**  STRING |
| **updated**  DATE-TIME |
| **updated\_by\_event\_type**  STRING |

### disputes

This table contains information about customer disputes related to charges on their credit card.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | created |
| **Useful links** | [Stripe documentation](https://stripe.com/Content/api/disputes/object)  [Stripe API method](https://stripe.com/Content/api/disputes/list "Opens in new tab: Stripe API method") |

disputes table foreign keys

| Join disputes with | on |
| --- | --- |
| [balance\_transactions](#balance-transactions) | ``` disputes.balance_transactions.id = balance_transactions.id ``` |
| [charges](#charges) | ``` disputes.balance_transactions.id = charges.balance_transaction ```  ``` disputes.charge = charges.id ``` |
| [payouts](#payouts) | ``` disputes.balance_transactions.id = payouts.balance_transaction ```  ``` disputes.balance_transactions.id = payouts.failure_balance_transaction ``` |
| [transfers](#transfers) | ``` disputes.balance_transactions.id = transfers.balance_transaction ```  ``` disputes.balance_transactions.id = transfers.failure_balance_transaction ``` |
| [invoices](#invoices) | ``` disputes.charge = invoices.charge ``` |

disputes table schema

|  |
| --- |
| **amount**  INTEGER |
| **balance\_transactions**  ARRAY This is a nested data structure:   - id: STRING |
| **charge**  STRING |
| **created**  DATE-TIME |
| **currency**  STRING |
| **evidence**  STRING, OBJECT This is a nested data structure:   - access\_activity\_log: STRING - billing\_address: STRING - cancellation\_policy: STRING - cancellation\_policy\_disclosure: STRING - cancellation\_rebuttal: STRING - customer\_communication: STRING - customer\_email\_address: STRING - customer\_name: STRING - customer\_purchase\_ip: STRING - customer\_signature: STRING - duplicate\_charge\_documentation: STRING - duplicate\_charge\_explanation: STRING - duplicate\_charge\_id: STRING - product\_description: STRING - receipt: STRING - refund\_policy: STRING - refund\_policy\_disclosure: STRING - refund\_refusal\_explanation: STRING - service\_date: STRING - service\_documentation: STRING - shipping\_address: STRING - shipping\_carrier: STRING - shipping\_date: STRING - shipping\_documentation: STRING - shipping\_tracking\_number: STRING - uncategorized\_file: STRING - uncategorized\_text: STRING |
| **evidence\_details**  OBJECT This is a nested data structure:   - due\_by: DATE-TIME - has\_evidence: BOOLEAN - past\_due: BOOLEAN - submission\_count: INTEGER |
| **id**  STRING |
| **is\_charge\_refundable**  BOOLEAN |
| **livemode**  BOOLEAN |
| **metadata**  OBJECT |
| **object**  STRING |
| **reason**  STRING |
| **status**  STRING |
| **updated**  DATE-TIME |
| **updated\_by\_event\_type**  STRING |

### events

The `events` table contains info about [events](https://stripe.com/Content/api/events). When an event occurs, a new event object is created. This table acts as the history of an object, allowing you to see how it has changed over time.

For example: When an invoice is created, an `invoice.created` event is created. When the draft invoice is finalized and updated to be open, an `invoice.finalized` event is created. When the invoice is sent to the customer, an `invoice.sent` event is created.

For more info about this table and how data is replicated, refer to the [Replication](#replication) section. Additionally, refer to [Stripe’s documentation](https://stripe.com/Content/api/events/types) for info about event types and the objects they describe.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | created |
| **Useful links** | [Stripe documentation](https://stripe.com/Content/api/events)  [Stripe API method](https://stripe.com/Content/api/events/list "Opens in new tab: Stripe API method") |

events table schema

|  |
| --- |
| **api\_version**  STRING |
| **created**  DATE-TIME |
| **data**  OBJECT |
| **id**  STRING |
| **livemode**  BOOLEAN |
| **object**  STRING |
| **pending\_webhooks**  INTEGER |
| **request**  STRING |
| **type**  STRING |
| **updated**  DATE-TIME |

### invoice\_items

The `invoice_items` table contains info about items contained in customer invoices.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | date |
| **Useful links** | Stripe documentation  [Stripe API method](https://stripe.com/Content/api/invoiceitems/list "Opens in new tab: Stripe API method") |

invoice\_items table foreign keys

| Join invoice\_items with | on |
| --- | --- |
| [charges](#charges) | ``` invoice_items.customer = charges.customer ```  ``` invoice_items.customer = charges.card.customer ```  ``` invoice_items.invoice = charges.invoice ``` |
| [customers](#customers) | ``` invoice_items.customer = customers.id ```  ``` invoice_items.customer = customers.cards.customer ```  ``` invoice_items.customer = customers.discount.customer ```  ``` invoice_items.subscription = customers.subscriptions ```  ``` invoice_items.subscription = customers.discount.subscription ``` |
| [invoices](#invoices) | ``` invoice_items.customer = invoices.customer ```  ``` invoice_items.customer = invoices.discount.customer ```  ``` invoice_items.invoice = invoices.id ```  ``` invoice_items.subscription = invoices.subscription ```  ``` invoice_items.subscription = invoices.discount.subscription ``` |
| [subscription\_items](#subscription-items) | ``` invoice_items.customer = subscription_items.customer ```  ``` invoice_items.plan.id = subscription_items.plan.id ```  ``` invoice_items.plan.product = subscription_items.plan.product ```  ``` invoice_items.subscription_item = subscription_items.id ```  ``` invoice_items.subscription = subscription_items.subscription ``` |
| [subscriptions](#subscriptions) | ``` invoice_items.customer = subscriptions.customer ```  ``` invoice_items.plan.id = subscriptions.plan.id ```  ``` invoice_items.plan.product = subscriptions.plan.product ```  ``` invoice_items.subscription_item = subscriptions.items ```  ``` invoice_items.subscription = subscriptions.id ``` |
| [invoice\_line\_items](#invoice-line-items) | ``` invoice_items.invoice = invoice_line_items.invoice ```  ``` invoice_items.id = invoice_line_items.invoice_item ```  ``` invoice_items.plan.product = invoice_line_items.plan.product ```  ``` invoice_items.subscription = invoice_line_items.subscription ``` |
| [plans](#plans) | ``` invoice_items.plan.id = plans.id ```  ``` invoice_items.plan.product = plans.product ``` |
| [products](#products) | ``` invoice_items.plan.product = products.id ``` |

invoice\_items table schema

|  |
| --- |
| **amount**  INTEGER |
| **currency**  STRING |
| **customer**  STRING |
| **date**  DATE-TIME |
| **description**  STRING |
| **discountable**  BOOLEAN |
| **discounts**  ARRAY |
| **id**  STRING |
| **invoice**  STRING |
| **livemode**  BOOLEAN |
| **metadata**  OBJECT |
| **object**  STRING |
| **period**  OBJECT This is a nested data structure:   - end: DATE-TIME - start: DATE-TIME |
| **plan**  OBJECT This is a nested data structure:   - active: BOOLEAN - aggregate\_usage: STRING - amount: INTEGER - amount\_decimal: NUMBER - billing\_scheme: STRING - created: DATE-TIME - currency: STRING - id: STRING - interval: STRING - interval\_count: INTEGER - livemode: BOOLEAN - metadata: OBJECT - name: STRING - nickname: STRING - object: STRING - product: STRING - statement\_description: STRING - statement\_descriptor: STRING - tiers: ARRAY, which is also a nested data structure.   - flat\_amount: INTEGER   - unit\_amount: INTEGER   - up\_to: INTEGER - tiers\_mode: STRING - transform\_usage: OBJECT - trial\_period\_days: INTEGER - updated: DATE-TIME - updated\_by\_event\_type: STRING - usage\_type: STRING |
| **proration**  BOOLEAN |
| **quantity**  INTEGER |
| **subscription**  STRING |
| **subscription\_item**  STRING |
| **tax\_rates**  ARRAY This is a nested data structure:   - active: BOOLEAN - country: STRING - created: DATE-TIME - description: STRING - display\_name: STRING - id: STRING - inclusive: BOOLEAN - jurisdiction: STRING - livemode: BOOLEAN - object: STRING - percentage: NUMBER - state: STRING |
| **unit\_amount**  INTEGER |
| **unit\_amount\_decimal**  NUMBER |
| **updated**  DATE-TIME |
| **updated\_by\_event\_type**  STRING |

### invoice\_line\_items

The `invoice_line_items` table contains info about the line items contained in invoices.

**Note**: In order to replicate invoice line item data, the [`invoices`](#invoices) table must also be set to replicate.

#### Invoice line item replication

To replicate invoice line items, Stitch will use the Replication Key of the corresponding invoice in the [`invoices`](#invoices) table to detect new and updated records. This means that any time an invoice is updated, its associated line items will also be replicated.

For example: An invoice with five line items is updated when its status changes from `draft` to `open`. The record in `invoices` will be replicated, as will the records for its five line items. In this example, a total of six records will be replicated.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | id  invoice |
| **Useful links** | [Stripe documentation](https://stripe.com/Content/api/invoices/line_item)  [Stripe API method](https://stripe.com/Content/api/invoices/invoice_lines "Opens in new tab: Stripe API method") |

invoice\_line\_items table foreign keys

| Join invoice\_line\_items with | on |
| --- | --- |
| [charges](#charges) | ``` invoice_line_items.invoice = charges.invoice ``` |
| [invoice\_items](#invoice-items) | ``` invoice_line_items.invoice = invoice_items.invoice ```  ``` invoice_line_items.invoice_item = invoice_items.id ```  ``` invoice_line_items.plan.product = invoice_items.plan.product ```  ``` invoice_line_items.subscription = invoice_items.subscription ``` |
| [invoices](#invoices) | ``` invoice_line_items.invoice = invoices.id ```  ``` invoice_line_items.id = invoices.lines ```  ``` invoice_line_items.subscription = invoices.subscription ```  ``` invoice_line_items.subscription = invoices.discount.subscription ``` |
| [plans](#plans) | ``` invoice_line_items.plan.product = plans.product ``` |
| [products](#products) | ``` invoice_line_items.plan.product = products.id ``` |
| [subscription\_items](#subscription-items) | ``` invoice_line_items.plan.product = subscription_items.plan.product ```  ``` invoice_line_items.subscription = subscription_items.subscription ``` |
| [subscriptions](#subscriptions) | ``` invoice_line_items.plan.product = subscriptions.plan.product ```  ``` invoice_line_items.subscription = subscriptions.id ``` |
| [customers](#customers) | ``` invoice_line_items.subscription = customers.subscriptions ```  ``` invoice_line_items.subscription = customers.discount.subscription ``` |

invoice\_line\_items table schema

|  |
| --- |
| **amount**  INTEGER |
| **currency**  STRING |
| **description**  STRING |
| **discount\_amounts**  ARRAY This is a nested data structure:   - amount: INTEGER - discount: STRING |
| **discountable**  BOOLEAN |
| **discounts**  ARRAY |
| **id**  STRING |
| **invoice**  STRING |
| **invoice\_item**  STRING |
| **livemode**  BOOLEAN |
| **metadata**  OBJECT |
| **object**  STRING |
| **period**  OBJECT This is a nested data structure:   - end: DATE-TIME - start: DATE-TIME |
| **plan**  OBJECT This is a nested data structure:   - active: BOOLEAN - aggregate\_usage: STRING - amount: INTEGER - amount\_decimal: NUMBER - billing\_scheme: STRING - created: DATE-TIME - currency: STRING - id: STRING - interval: STRING - interval\_count: INTEGER - livemode: BOOLEAN - metadata: OBJECT - name: STRING - nickname: STRING - object: STRING - product: STRING - statement\_description: STRING - statement\_descriptor: STRING - tiers: ARRAY, which is also a nested data structure.   - flat\_amount: INTEGER   - unit\_amount: INTEGER   - up\_to: INTEGER - tiers\_mode: STRING - transform\_usage: OBJECT - trial\_period\_days: INTEGER - updated: DATE-TIME - updated\_by\_event\_type: STRING - usage\_type: STRING |
| **price**  OBJECT This is a nested data structure:   - active: BOOLEAN - billing\_scheme: STRING - created: DATE-TIME - currency: STRING - id: STRING - livemode: BOOLEAN - lookup\_key: STRING - metadata: OBJECT - nickname: STRING - object: STRING - product: STRING - recurring: OBJECT, which is also a nested data structure.   - aggregate\_usage: STRING   - interval: STRING   - interval\_count: INTEGER   - usage\_type: STRING - tax\_behavior: STRING - tiers: ARRAY, which is also a nested data structure.   - flat\_amount: INTEGER   - flat\_amount\_decimal: NUMBER   - unit\_amount: INTEGER   - unit\_amount\_decimal: NUMBER   - up\_to: INTEGER - tiers\_mode: STRING - transform\_quantity: OBJECT, which is also a nested data structure.   - divide\_by: INTEGER   - round: STRING - type: STRING - unit\_amount: INTEGER - unit\_amount\_decimal: NUMBER |
| **proration**  BOOLEAN |
| **proration\_details**  OBJECT |
| **quantity**  INTEGER |
| **subscription**  STRING |
| **subscription\_item**  STRING |
| **tax\_amounts**  ARRAY This is a nested data structure:   - amount: INTEGER - inclusive: BOOLEAN - tax\_rate: STRING |
| **tax\_rates**  ARRAY This is a nested data structure:   - active: BOOLEAN - country: STRING - created: DATE-TIME - description: STRING - display\_name: STRING - id: STRING - inclusive: BOOLEAN - jurisdiction: STRING - livemode: BOOLEAN - metadata: OBJECT - object: STRING - percentage: NUMBER - state: STRING - tax\_type: BOOLEAN |
| **type**  STRING |

### invoices

The `invoices` table contains info about invoices. Invoices are statements of amounts owed by customers, which can be one-off charges or generated periodically from a subscription.

#### Invoice line items

Full records for the line items associated with an invoice can be found in the [`invoice_line_items`](#invoice_line_items) table. To replicate these records, you must set this table and the `invoice_line_items` table to replicate.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | created |
| **Useful links** | [Stripe documentation](https://stripe.com/Content/api/invoices)  [Stripe API method](https://stripe.com/Content/api/invoices/list "Opens in new tab: Stripe API method") |

invoices table foreign keys

| Join invoices with | on |
| --- | --- |
| [charges](#charges) | ``` invoices.charge = charges.id ```  ``` invoices.customer = charges.customer ```  ``` invoices.discount.customer = charges.customer ```  ``` invoices.customer = charges.card.customer ```  ``` invoices.discount.customer = charges.card.customer ```  ``` invoices.id = charges.invoice ``` |
| [disputes](#disputes) | ``` invoices.charge = disputes.charge ``` |
| [coupons](#coupons) | ``` invoices.discount.coupon.id = coupons.id ``` |
| [customers](#customers) | ``` invoices.discount.coupon.id = customers.discount.coupon.id ```  ``` invoices.customer = customers.id ```  ``` invoices.discount.customer = customers.id ```  ``` invoices.customer = customers.cards.customer ```  ``` invoices.discount.customer = customers.cards.customer ```  ``` invoices.customer = customers.discount.customer ```  ``` invoices.discount.customer = customers.discount.customer ```  ``` invoices.subscription = customers.subscriptions ```  ``` invoices.discount.subscription = customers.subscriptions ```  ``` invoices.subscription = customers.discount.subscription ```  ``` invoices.discount.subscription = customers.discount.subscription ``` |
| [subscriptions](#subscriptions) | ``` invoices.discount.coupon.id = subscriptions.discount.coupon.id ```  ``` invoices.customer = subscriptions.customer ```  ``` invoices.discount.customer = subscriptions.customer ```  ``` invoices.subscription = subscriptions.id ```  ``` invoices.discount.subscription = subscriptions.id ``` |
| [invoice\_items](#invoice-items) | ``` invoices.customer = invoice_items.customer ```  ``` invoices.discount.customer = invoice_items.customer ```  ``` invoices.id = invoice_items.invoice ```  ``` invoices.subscription = invoice_items.subscription ```  ``` invoices.discount.subscription = invoice_items.subscription ``` |
| [subscription\_items](#subscription-items) | ``` invoices.customer = subscription_items.customer ```  ``` invoices.discount.customer = subscription_items.customer ```  ``` invoices.subscription = subscription_items.subscription ```  ``` invoices.discount.subscription = subscription_items.subscription ``` |
| [invoice\_line\_items](#invoice-line-items) | ``` invoices.id = invoice_line_items.invoice ```  ``` invoices.lines = invoice_line_items.id ```  ``` invoices.subscription = invoice_line_items.subscription ```  ``` invoices.discount.subscription = invoice_line_items.subscription ``` |

invoices table schema

|  |
| --- |
| **account\_country**  STRING |
| **account\_name**  STRING |
| **account\_tax\_ids**  ARRAY |
| **amount\_due**  INTEGER |
| **amount\_paid**  INTEGER |
| **amount\_remaining**  INTEGER |
| **application\_fee**  INTEGER |
| **application\_fee\_amount**  INTEGER |
| **attempt\_count**  INTEGER |
| **attempted**  BOOLEAN |
| **auto\_advance**  BOOLEAN |
| **automatic\_tax**  OBJECT This is a nested data structure:   - enabled: BOOLEAN - status: STRING |
| **billing**  STRING |
| **billing\_reason**  STRING |
| **charge**  STRING |
| **closed**  BOOLEAN |
| **collection\_method**  STRING |
| **created**  DATE-TIME |
| **currency**  STRING |
| **custom\_fields**  ARRAY This is a nested data structure:   - name: STRING - value: STRING |
| **customer**  STRING |
| **customer\_address**  OBJECT This is a nested data structure:   - city: STRING - country: STRING - line1: STRING - line2: STRING - postal\_code: STRING - state: STRING |
| **customer\_email**  STRING |
| **customer\_name**  STRING |
| **customer\_phone**  STRING |
| **customer\_shipping**  OBJECT This is a nested data structure:   - address: OBJECT, which is also a nested data structure.   - city: STRING   - country: STRING   - line1: STRING   - line2: STRING   - postal\_code: STRING   - state: STRING - name: STRING - phone: STRING |
| **customer\_tax\_exempt**  STRING |
| **customer\_tax\_ids**  ARRAY This is a nested data structure:   - type: STRING - value: STRING |
| **date**  DATE-TIME |
| **default\_payment\_method**  STRING |
| **default\_source**  STRING |
| **default\_tax\_rates**  ARRAY This is a nested data structure:   - active: BOOLEAN - country: STRING - created: DATE-TIME - description: STRING - display\_name: STRING - id: STRING - inclusive: BOOLEAN - jurisdiction: STRING - livemode: BOOLEAN - metadata: OBJECT - object: STRING - percentage: NUMBER - state: STRING |
| **description**  STRING |
| **discount**  OBJECT This is a nested data structure:   - checkout\_session: STRING - coupon: OBJECT, which is also a nested data structure.   - amount\_off: INTEGER   - created: DATE-TIME   - currency: STRING   - duration: STRING   - duration\_in\_months: INTEGER   - id: STRING   - livemode: BOOLEAN   - max\_redemptions: INTEGER   - metadata: OBJECT   - name: STRING   - object: STRING   - percent\_off: NUMBER   - percent\_off\_precise: NUMBER   - redeem\_by: DATE-TIME   - times\_redeemed: INTEGER   - valid: BOOLEAN - customer: STRING - end: DATE-TIME - id: STRING - invoice: STRING - invoice\_item: STRING - object: STRING - promotion\_code: STRING - start: DATE-TIME - subscription: STRING |
| **discounts**  ARRAY |
| **due\_date**  DATE-TIME |
| **ending\_balance**  INTEGER |
| **finalized\_at**  DATE-TIME |
| **footer**  STRING |
| **forgiven**  BOOLEAN |
| **hosted\_invoice\_url**  STRING |
| **id**  STRING |
| **invoice\_pdf**  STRING |
| **last\_finalization\_error**  OBJECT This is a nested data structure:   - code: STRING - doc\_url: STRING - message: STRING - param: STRING - payment\_method\_type: STRING - type: STRING |
| **lines**  ARRAY, OBJECT |
| **livemode**  BOOLEAN |
| **metadata**  OBJECT |
| **next\_payment\_attempt**  DATE-TIME |
| **number**  STRING |
| **object**  STRING |
| **on\_behalf\_of**  STRING, OBJECT |
| **paid**  BOOLEAN |
| **paid\_out\_of\_band**  BOOLEAN |
| **payment**  STRING |
| **payment\_intent**  STRING |
| **payment\_settings**  OBJECT This is a nested data structure:   - payment\_method\_options: OBJECT, which is also a nested data structure.   - acss\_debit: OBJECT, which is also a nested data structure.     - mandate\_options: OBJECT, which is also a nested data structure.       - transaction\_type: STRING     - verification\_method: STRING   - bancontact: OBJECT, which is also a nested data structure.     - preferred\_language: STRING   - card: OBJECT, which is also a nested data structure.     - request\_three\_d\_secure: STRING - payment\_method\_types: ARRAY |
| **period\_end**  DATE-TIME |
| **period\_start**  DATE-TIME |
| **post\_payment\_credit\_notes\_amount**  INTEGER |
| **pre\_payment\_credit\_notes\_amount**  INTEGER |
| **quote**  OBJECT, STRING |
| **receipt\_number**  STRING |
| **starting\_balance**  INTEGER |
| **statement\_description**  STRING |
| **statement\_descriptor**  STRING |
| **status**  STRING |
| **status\_transitions**  OBJECT This is a nested data structure:   - finalized\_at: DATE-TIME - marked\_uncollectible\_at: DATE-TIME - paid\_at: DATE-TIME - voided\_at: DATE-TIME |
| **subscription**  STRING |
| **subscription\_details**  OBJECT This is a nested data structure:   - metadata: STRING |
| **subtotal**  INTEGER |
| **tax**  INTEGER |
| **tax\_percent**  NUMBER |
| **total**  INTEGER |
| **total\_discount\_amounts**  ARRAY This is a nested data structure:   - amount: INTEGER - discount: STRING |
| **total\_tax\_amounts**  ARRAY This is a nested data structure:   - amount: INTEGER - inclusive: BOOLEAN - tax\_rate: STRING |
| **transfer\_data**  OBJECT This is a nested data structure:   - amount: INTEGER - destination: STRING |
| **updated**  DATE-TIME |
| **updated\_by\_event\_type**  STRING |
| **webhooks\_delivered\_at**  DATE-TIME |

### payment\_intents

This table contains information about payments, from creation through checkout, in your Stripe account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | created |
| **Useful links** | [Stripe documentation](https://stripe.com/Content/payments/payment-intents)  [Stripe API method](https://stripe.com/Content/api/payment_intents/list "Opens in new tab: Stripe API method") |

payment\_intents table schema

|  |
| --- |
| **amount**  INTEGER |
| **amount\_capturable**  INTEGER |
| **amount\_received**  INTEGER |
| **application**  STRING |
| **application\_fee\_amount**  INTEGER |
| **automatic\_payment\_methods**  OBJECT This is a nested data structure:   - enabled: BOOLEAN |
| **canceled\_at**  DATE-TIME |
| **cancellation\_reason**  STRING |
| **capture\_method**  STRING |
| **client\_secret**  STRING |
| **confirmation\_method**  STRING |
| **created**  DATE-TIME |
| **currency**  STRING |
| **customer**  STRING |
| **description**  STRING |
| **id**  STRING |
| **invoice**  STRING |
| **last\_payment\_error**  OBJECT This is a nested data structure:   - charge: STRING - code: STRING - decline\_code: STRING - doc\_url: STRING - message: STRING - param: STRING - payment\_method\_type: STRING - type: STRING |
| **latest\_charge**  STRING |
| **livemode**  BOOLEAN |
| **metadata**  OBJECT |
| **next\_action**  OBJECT This is a nested data structure:   - alipay\_handle\_redirect: OBJECT, which is also a nested data structure.   - native\_data: STRING   - native\_url: STRING   - return\_url: STRING   - url: STRING - boleto\_display\_details: OBJECT, which is also a nested data structure.   - expires\_at: DATE-TIME   - hosted\_voucher\_url: STRING   - number: STRING   - pdf: STRING - oxxo\_display\_details: OBJECT, which is also a nested data structure.   - expires\_after: DATE-TIME   - hosted\_voucher\_url: STRING   - number: STRING - redirect\_to\_url: OBJECT, which is also a nested data structure.   - return\_url: STRING   - url: STRING - type: STRING - use\_stripe\_sdk: OBJECT - verify\_with\_microdeposits: OBJECT, which is also a nested data structure.   - arrival\_date: DATE-TIME   - hosted\_verification\_url: STRING - wechat\_pay\_display\_qr\_code: OBJECT, which is also a nested data structure.   - data: STRING   - image\_data\_url: STRING   - image\_url\_png: STRING   - image\_url\_svg: STRING - wechat\_pay\_redirect\_to\_android\_app: OBJECT, which is also a nested data structure.   - app\_id: STRING   - nonce\_str: STRING   - package: STRING   - partner\_id: STRING   - prepay\_id: STRING   - sign: STRING   - timestamp: STRING - wechat\_pay\_redirect\_to\_ios\_app: OBJECT, which is also a nested data structure.   - native\_url: STRING |
| **object**  STRING |
| **on\_behalf\_of**  STRING |
| **payment\_method**  STRING |
| **payment\_method\_options**  OBJECT This is a nested data structure:   - acss\_debit: OBJECT, which is also a nested data structure.   - mandate\_options: OBJECT, which is also a nested data structure.     - custom\_mandate\_url: STRING     - interval\_description: STRING     - payment\_schedule: STRING     - transaction\_type: STRING - afterpay\_clearpay: OBJECT, which is also a nested data structure.   - reference: STRING   - setup\_future\_usage: STRING - alipay: OBJECT, which is also a nested data structure.   - setup\_future\_usage: STRING - au\_becs\_debit: OBJECT, which is also a nested data structure.   - setup\_future\_usage: STRING - bacs\_debit: OBJECT, which is also a nested data structure.   - setup\_future\_usage: STRING - bancontact: OBJECT, which is also a nested data structure.   - preferred\_language: STRING   - setup\_future\_usage: STRING - boleto: OBJECT, which is also a nested data structure.   - expires\_after\_days: INTEGER   - setup\_future\_usage: STRING - card: OBJECT, which is also a nested data structure.   - installments: OBJECT, which is also a nested data structure.     - available\_plans: ARRAY, which is also a nested data structure.       - count: INTEGER       - interval: STRING       - type: STRING     - enabled: BOOLEAN     - plan: OBJECT, which is also a nested data structure.       - count: INTEGER       - interval: STRING       - type: STRING   - network: STRING   - request\_three\_d\_secure: STRING   - setup\_future\_usage: STRING - card\_present: OBJECT - eps: OBJECT, which is also a nested data structure.   - setup\_future\_usage: STRING - fps: OBJECT, which is also a nested data structure.   - setup\_future\_usage: STRING - giropay: OBJECT, which is also a nested data structure.   - setup\_future\_usage: STRING - grabpay: OBJECT, which is also a nested data structure.   - setup\_future\_usage: STRING - ideal: OBJECT, which is also a nested data structure.   - setup\_future\_usage: STRING - interac\_present: OBJECT - klarna: OBJECT, which is also a nested data structure.   - preferred\_locale: STRING   - setup\_future\_usage: STRING - oxxo: OBJECT, which is also a nested data structure.   - expires\_after\_days: STRING   - setup\_future\_usage: STRING - p24: OBJECT, which is also a nested data structure.   - setup\_future\_usage: STRING - sepa\_debit: OBJECT, which is also a nested data structure.   - mandate\_options: OBJECT   - setup\_future\_usage: STRING - sofort: OBJECT, which is also a nested data structure.   - preferred\_language: STRING   - setup\_future\_usage: STRING - wechat\_pay: OBJECT, which is also a nested data structure.   - app\_id: STRING   - client: STRING   - setup\_future\_usage: STRING |
| **payment\_method\_types**  ARRAY |
| **processing**  OBJECT |
| **receipt\_email**  STRING |
| **review**  STRING |
| **setup\_future\_usage**  STRING |
| **shipping**  OBJECT This is a nested data structure:   - address: OBJECT, which is also a nested data structure.   - city: STRING   - country: STRING   - line1: STRING   - line2: STRING   - postal\_code STRING   - state: STRING - carrier: STRING - name: STRING - phone: STRING - tracking\_number: STRING |
| **source**  STRING |
| **statement\_descriptor**  STRING |
| **statement\_descriptor\_suffix**  STRING |
| **status**  STRING |
| **transfer\_data**  OBJECT This is a nested data structure:   - amount: INTEGER - destination: STRING |
| **transfer\_group**  STRING |
| **updated**  DATE-TIME |
| **updated\_by\_event\_type**  STRING |

### payout\_transactions

This table contains info about payout transactions.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Stripe documentation](https://stripe.com/Content/api/payouts)  [Stripe API method](https://stripe.com/Content/api/payouts/list "Opens in new tab: Stripe API method") |

payout\_transactions table foreign keys

| Join payout\_transactions with | on |
| --- | --- |
| [payouts](#payouts) | ``` payout_transactions.payout_id = payouts.id ``` |

payout\_transactions table schema

|  |
| --- |
| **id**  STRING |
| **payout\_id**  STRING |

### payouts

The `payouts` table contains info about payouts, which occur when you receive funds from Stripe or initiate a payout to a bank account of the debit card of a connected Stripe account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | created |
| **Useful links** | [Stripe documentation](https://stripe.com/Content/api/payouts)  [Stripe API method](https://stripe.com/Content/api/payouts/list "Opens in new tab: Stripe API method") |

payouts table foreign keys

| Join payouts with | on |
| --- | --- |
| [balance\_transactions](#balance-transactions) | ``` payouts.balance_transaction = balance_transactions.id ```  ``` payouts.failure_balance_transaction = balance_transactions.id ``` |
| [charges](#charges) | ``` payouts.balance_transaction = charges.balance_transaction ```  ``` payouts.failure_balance_transaction = charges.balance_transaction ``` |
| [transfers](#transfers) | ``` payouts.balance_transaction = transfers.balance_transaction ```  ``` payouts.failure_balance_transaction = transfers.balance_transaction ```  ``` payouts.balance_transaction = transfers.failure_balance_transaction ```  ``` payouts.failure_balance_transaction = transfers.failure_balance_transaction ``` |
| [disputes](#disputes) | ``` payouts.balance_transaction = disputes.balance_transactions.id ```  ``` payouts.failure_balance_transaction = disputes.balance_transactions.id ``` |
| [payout\_transactions](#payout-transactions) | ``` payouts.id = payout_transactions.payout_id ``` |

payouts table schema

|  |
| --- |
| **amount**  INTEGER |
| **amount\_reversed**  INTEGER |
| **arrival\_date**  DATE-TIME |
| **automatic**  BOOLEAN |
| **balance\_transaction**  STRING |
| **bank\_account**  OBJECT This is a nested data structure:   - account\_holder\_name: STRING - account\_holder\_type: STRING - bank\_name: STRING - country: STRING - currency: STRING - fingerprint: STRING - id: STRING - last4: STRING - metadata: OBJECT - name: STRING - object: STRING - routing\_number: STRING - status: STRING |
| **created**  DATE-TIME |
| **currency**  STRING |
| **date**  DATE-TIME |
| **description**  STRING |
| **destination**  STRING |
| **failure\_balance\_transaction**  STRING |
| **failure\_code**  STRING |
| **failure\_message**  STRING |
| **id**  STRING |
| **livemode**  BOOLEAN |
| **metadata**  OBJECT |
| **method**  STRING |
| **object**  STRING |
| **original\_payout**  STRING |
| **recipient**  STRING |
| **reversed\_by**  STRING |
| **source\_transaction**  STRING |
| **source\_type**  STRING |
| **statement\_description**  STRING |
| **statement\_descriptor**  STRING |
| **status**  STRING |
| **transfer\_group**  STRING |
| **type**  STRING |
| **updated**  DATE-TIME |
| **updated\_by\_event\_type**  STRING |

### plans

The `plans` table contains info about the plans in your Stripe account. A plan defines the base price, currency, and billing cycle for subscriptions.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | created |
| **Useful links** | [Stripe documentation](https://stripe.com/Content/api/plans)  [Stripe API method](https://stripe.com/Content/api/plans/list "Opens in new tab: Stripe API method") |

plans table foreign keys

| Join plans with | on |
| --- | --- |
| [invoice\_items](#invoice-items) | ``` plans.id = invoice_items.plan.id ```  ``` plans.product = invoice_items.plan.product ``` |
| [subscription\_items](#subscription-items) | ``` plans.id = subscription_items.plan.id ```  ``` plans.product = subscription_items.plan.product ``` |
| [subscriptions](#subscriptions) | ``` plans.id = subscriptions.plan.id ```  ``` plans.product = subscriptions.plan.product ``` |
| [invoice\_line\_items](#invoice-line-items) | ``` plans.product = invoice_line_items.plan.product ``` |
| [products](#products) | ``` plans.product = products.id ``` |

plans table schema

|  |
| --- |
| **active**  BOOLEAN |
| **aggregate\_usage**  STRING |
| **amount**  INTEGER |
| **amount\_decimal**  NUMBER |
| **billing\_scheme**  STRING |
| **created**  DATE-TIME |
| **currency**  STRING |
| **id**  STRING |
| **interval**  STRING |
| **interval\_count**  INTEGER |
| **livemode**  BOOLEAN |
| **metadata**  OBJECT |
| **name**  STRING |
| **nickname**  STRING |
| **object**  STRING |
| **product**  STRING |
| **statement\_description**  STRING |
| **statement\_descriptor**  STRING |
| **tiers**  ARRAY This is a nested data structure:   - flat\_amount: INTEGER - unit\_amount: INTEGER - up\_to: INTEGER |
| **tiers\_mode**  STRING |
| **transform\_usage**  OBJECT |
| **trial\_period\_days**  INTEGER |
| **updated**  DATE-TIME |
| **updated\_by\_event\_type**  STRING |
| **usage\_type**  STRING |

### products

The `products` table contains info about the products in your Stripe account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | created |
| **Useful links** | [Stripe documentation](https://stripe.com/Content/api/products)  [Stripe API method](https://stripe.com/Content/api/products/list "Opens in new tab: Stripe API method") |

products table foreign keys

| Join products with | on |
| --- | --- |
| [invoice\_items](#invoice-items) | ``` products.id = invoice_items.plan.product ``` |
| [invoice\_line\_items](#invoice-line-items) | ``` products.id = invoice_line_items.plan.product ``` |
| [plans](#plans) | ``` products.id = plans.product ``` |
| [subscription\_items](#subscription-items) | ``` products.id = subscription_items.plan.product ``` |
| [subscriptions](#subscriptions) | ``` products.id = subscriptions.plan.product ``` |

products table schema

|  |
| --- |
| **active**  BOOLEAN |
| **attributes**  ARRAY |
| **caption**  STRING |
| **created**  DATE-TIME |
| **deactivate\_on**  ARRAY |
| **description**  STRING |
| **id**  STRING |
| **images**  ARRAY |
| **livemode**  BOOLEAN |
| **metadata**  OBJECT |
| **name**  STRING |
| **object**  STRING |
| **package\_dimensions**  OBJECT This is a nested data structure:   - height: NUMBER - length: NUMBER - weight: NUMBER - width: NUMBER |
| **shippable**  BOOLEAN |
| **statement\_descriptor**  STRING |
| **tax\_code**  STRING |
| **type**  STRING |
| **unit\_label**  STRING |
| **updated**  DATE-TIME |
| **updated\_by\_event\_type**  STRING |
| **url**  STRING |

### subscription\_items

The `subscription_items` table contains info about subscription items. In Stripe, subscription items are used to create customer subscriptions with more than one plan.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | created |
| **Useful links** | [Stripe documentation](https://stripe.com/Content/api/subscription_items)  [Stripe API method](https://stripe.com/Content/api/subscription_items/list "Opens in new tab: Stripe API method") |

subscription\_items table foreign keys

| Join subscription\_items with | on |
| --- | --- |
| [charges](#charges) | ``` subscription_items.customer = charges.customer ```  ``` subscription_items.customer = charges.card.customer ``` |
| [customers](#customers) | ``` subscription_items.customer = customers.id ```  ``` subscription_items.customer = customers.cards.customer ```  ``` subscription_items.customer = customers.discount.customer ```  ``` subscription_items.subscription = customers.subscriptions ```  ``` subscription_items.subscription = customers.discount.subscription ``` |
| [invoice\_items](#invoice-items) | ``` subscription_items.customer = invoice_items.customer ```  ``` subscription_items.plan.id = invoice_items.plan.id ```  ``` subscription_items.plan.product = invoice_items.plan.product ```  ``` subscription_items.id = invoice_items.subscription_item ```  ``` subscription_items.subscription = invoice_items.subscription ``` |
| [invoices](#invoices) | ``` subscription_items.customer = invoices.customer ```  ``` subscription_items.customer = invoices.discount.customer ```  ``` subscription_items.subscription = invoices.subscription ```  ``` subscription_items.subscription = invoices.discount.subscription ``` |
| [subscriptions](#subscriptions) | ``` subscription_items.customer = subscriptions.customer ```  ``` subscription_items.plan.id = subscriptions.plan.id ```  ``` subscription_items.plan.product = subscriptions.plan.product ```  ``` subscription_items.id = subscriptions.items ```  ``` subscription_items.subscription = subscriptions.id ``` |
| [plans](#plans) | ``` subscription_items.plan.id = plans.id ```  ``` subscription_items.plan.product = plans.product ``` |
| [invoice\_line\_items](#invoice-line-items) | ``` subscription_items.plan.product = invoice_line_items.plan.product ```  ``` subscription_items.subscription = invoice_line_items.subscription ``` |
| [products](#products) | ``` subscription_items.plan.product = products.id ``` |

subscription\_items table schema

|  |
| --- |
| **application\_fee\_percent**  NUMBER |
| **billing\_thresholds**  OBJECT This is a nested data structure:   - usage\_gte: INTEGER |
| **cancel\_at\_period\_end**  BOOLEAN |
| **canceled\_at**  DATE-TIME |
| **created**  DATE-TIME |
| **current\_period\_end**  DATE-TIME |
| **current\_period\_start**  DATE-TIME |
| **customer**  STRING |
| **discount**  OBJECT |
| **ended\_at**  DATE-TIME |
| **id**  STRING |
| **livemode**  BOOLEAN |
| **metadata**  OBJECT |
| **object**  STRING |
| **plan**  OBJECT This is a nested data structure:   - active: BOOLEAN - aggregate\_usage: STRING - amount: INTEGER - amount\_decimal: NUMBER - billing\_scheme: STRING - created: DATE-TIME - currency: STRING - id: STRING - interval: STRING - interval\_count: INTEGER - livemode: BOOLEAN - metadata: OBJECT - name: STRING - nickname: STRING - object: STRING - product: STRING - statement\_description: STRING - statement\_descriptor: STRING - tiers: ARRAY, which is also a nested data structure.   - flat\_amount: INTEGER   - unit\_amount: INTEGER   - up\_to: INTEGER - tiers\_mode: STRING - transform\_usage: OBJECT - trial\_period\_days: INTEGER - updated: DATE-TIME - updated\_by\_event\_type: STRING - usage\_type: STRING |
| **price**  OBJECT This is a nested data structure:   - active: BOOLEAN - billing\_scheme: STRING - created: DATE-TIME - currency: STRING - id: STRING - livemode: BOOLEAN - lookup\_key: STRING - metadata: OBJECT - nickname: STRING - object: STRING - product: STRING - recurring: OBJECT, which is also a nested data structure.   - aggregate\_usage: STRING   - interval: STRING   - interval\_count: INTEGER   - usage\_type: STRING - tax\_behavior: STRING - tiers: ARRAY, which is also a nested data structure.   - flat\_amount: INTEGER   - flat\_amount\_decimal: STRING   - unit\_amount: INTEGER   - unit\_amount\_decimal: STRING   - up\_to: INTEGER - tiers\_mode: STRING - transform\_quantity: OBJECT, which is also a nested data structure.   - divide\_by: INTEGER   - round: STRING - type: STRING - unit\_amount: INTEGER - unit\_amount\_decimal: STRING |
| **quantity**  INTEGER |
| **start**  DATE-TIME |
| **status**  STRING |
| **subscription**  STRING |
| **tax\_percent**  NUMBER |
| **tax\_rates**  ARRAY This is a nested data structure:   - active: BOOLEAN - country: STRING - created: DATE-TIME - description: STRING - display\_name: STRING - id: STRING - inclusive: BOOLEAN - jurisdiction: STRING - livemode: BOOLEAN - metadata: OBJECT - object: STRING - percentage: NUMBER - state: STRING - tax\_type: BOOLEAN |
| **trial\_end**  DATE-TIME |
| **trial\_start**  DATE-TIME |

### subscriptions

The `subscriptions` table contains info about subscriptions, which allow you to charge a customer on a recurring basis. A subscription ties a customer to a particular [plan](#plans).

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | created |
| **Useful links** | [Stripe documentation](https://stripe.com/Content/api/subscriptions)  [Stripe API method](https://stripe.com/Content/api/subscriptions/list "Opens in new tab: Stripe API method") |

subscriptions table foreign keys

| Join subscriptions with | on |
| --- | --- |
| [coupons](#coupons) | ``` subscriptions.discount.coupon.id = coupons.id ``` |
| [customers](#customers) | ``` subscriptions.discount.coupon.id = customers.discount.coupon.id ```  ``` subscriptions.customer = customers.id ```  ``` subscriptions.customer = customers.cards.customer ```  ``` subscriptions.customer = customers.discount.customer ```  ``` subscriptions.id = customers.subscriptions ```  ``` subscriptions.id = customers.discount.subscription ``` |
| [invoices](#invoices) | ``` subscriptions.discount.coupon.id = invoices.discount.coupon.id ```  ``` subscriptions.customer = invoices.customer ```  ``` subscriptions.customer = invoices.discount.customer ```  ``` subscriptions.id = invoices.subscription ```  ``` subscriptions.id = invoices.discount.subscription ``` |
| [charges](#charges) | ``` subscriptions.customer = charges.customer ```  ``` subscriptions.customer = charges.card.customer ``` |
| [invoice\_items](#invoice-items) | ``` subscriptions.customer = invoice_items.customer ```  ``` subscriptions.plan.id = invoice_items.plan.id ```  ``` subscriptions.plan.product = invoice_items.plan.product ```  ``` subscriptions.items = invoice_items.subscription_item ```  ``` subscriptions.id = invoice_items.subscription ``` |
| [subscription\_items](#subscription-items) | ``` subscriptions.customer = subscription_items.customer ```  ``` subscriptions.plan.id = subscription_items.plan.id ```  ``` subscriptions.plan.product = subscription_items.plan.product ```  ``` subscriptions.items = subscription_items.id ```  ``` subscriptions.id = subscription_items.subscription ``` |
| [plans](#plans) | ``` subscriptions.plan.id = plans.id ```  ``` subscriptions.plan.product = plans.product ``` |
| [invoice\_line\_items](#invoice-line-items) | ``` subscriptions.plan.product = invoice_line_items.plan.product ```  ``` subscriptions.id = invoice_line_items.subscription ``` |
| [products](#products) | ``` subscriptions.plan.product = products.id ``` |

subscriptions table schema

|  |
| --- |
| **application\_fee\_percent**  NUMBER |
| **billing**  STRING |
| **billing\_cycle\_anchor**  DATE-TIME |
| **billing\_thresholds**  OBJECT This is a nested data structure:   - amount\_gte: INTEGER - reset\_billing\_cycle\_anchor: BOOLEAN |
| **cancel\_at**  DATE-TIME |
| **cancel\_at\_period\_end**  BOOLEAN |
| **canceled\_at**  DATE-TIME |
| **collection\_method**  STRING |
| **created**  DATE-TIME |
| **current\_period\_end**  DATE-TIME |
| **current\_period\_start**  DATE-TIME |
| **customer**  STRING |
| **days\_until\_due**  INTEGER |
| **default\_payment\_method**  STRING |
| **default\_source**  STRING |
| **discount**  OBJECT This is a nested data structure:   - checkout\_session: STRING - coupon: OBJECT, which is also a nested data structure.   - amount\_off: INTEGER   - created: DATE-TIME   - currency: STRING   - duration: STRING   - duration\_in\_months: INTEGER   - id: STRING   - livemode: BOOLEAN   - max\_redemptions: INTEGER   - metadata: OBJECT   - name: STRING   - object: STRING   - percent\_off: NUMBER   - percent\_off\_precise: NUMBER   - redeem\_by: DATE-TIME   - times\_redeemed: INTEGER   - valid: BOOLEAN - customer: STRING - end: DATE-TIME - id: STRING - invoice: STRING - invoice\_item: STRING - object: STRING - promotion\_code: STRING - start: DATE-TIME - subscription: STRING |
| **ended\_at**  DATE-TIME |
| **id**  STRING |
| **invoice\_customer\_balance\_settings**  OBJECT This is a nested data structure:   - consume\_applied\_balance\_on\_void: BOOLEAN |
| **items**  ARRAY |
| **latest\_invoice**  STRING |
| **livemode**  BOOLEAN |
| **metadata**  OBJECT |
| **next\_pending\_invoice\_item\_invoice**  DATE-TIME |
| **object**  STRING |
| **pause\_collection**  OBJECT This is a nested data structure:   - behavior: STRING - resumes\_at: DATE-TIME |
| **pending\_invoice\_item\_interval**  OBJECT This is a nested data structure:   - interval: STRING - interval\_count: INTEGER |
| **pending\_setup\_intent**  STRING |
| **plan**  OBJECT This is a nested data structure:   - active: BOOLEAN - aggregate\_usage: STRING - amount: INTEGER - billing\_scheme: STRING - created: DATE-TIME - currency: STRING - id: STRING - interval: STRING - interval\_count: INTEGER - livemode: BOOLEAN - metadata: OBJECT - name: STRING - nickname: STRING - object: STRING - product: STRING - statement\_description: STRING - statement\_descriptor: STRING - tiers: ARRAY, which is also a nested data structure.   - flat\_amount: INTEGER   - unit\_amount: INTEGER   - up\_to: INTEGER - tiers\_mode: STRING - transform\_usage: OBJECT - trial\_period\_days: INTEGER - usage\_type: STRING |
| **quantity**  INTEGER |
| **schedule**  STRING |
| **start**  DATE-TIME |
| **start\_date**  DATE-TIME |
| **status**  STRING |
| **tax\_percent**  NUMBER |
| **transfer\_data**  OBJECT This is a nested data structure:   - amount\_percent: NUMBER - destination: STRING |
| **trial\_end**  DATE-TIME |
| **trial\_start**  DATE-TIME |
| **updated**  DATE-TIME |
| **updated\_by\_event\_type**  STRING |

### transfers

The `transfers` table contains info about transfers sent to connected accounts.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | created |
| **Useful links** | Stripe documentation  [Stripe API method](https://stripe.com/Content/api/transfers/list "Opens in new tab: Stripe API method") |

transfers table foreign keys

| Join transfers with | on |
| --- | --- |
| [balance\_transactions](#balance-transactions) | ``` transfers.balance_transaction = balance_transactions.id ```  ``` transfers.failure_balance_transaction = balance_transactions.id ``` |
| [charges](#charges) | ``` transfers.balance_transaction = charges.balance_transaction ```  ``` transfers.failure_balance_transaction = charges.balance_transaction ```  ``` transfers.id = charges.source_transfer ``` |
| [payouts](#payouts) | ``` transfers.balance_transaction = payouts.balance_transaction ```  ``` transfers.failure_balance_transaction = payouts.balance_transaction ```  ``` transfers.balance_transaction = payouts.failure_balance_transaction ```  ``` transfers.failure_balance_transaction = payouts.failure_balance_transaction ``` |
| [disputes](#disputes) | ``` transfers.balance_transaction = disputes.balance_transactions.id ```  ``` transfers.failure_balance_transaction = disputes.balance_transactions.id ``` |

transfers table schema

|  |
| --- |
| **amount**  INTEGER |
| **amount\_reversed**  INTEGER |
| **arrival\_date**  DATE-TIME |
| **automatic**  BOOLEAN |
| **balance\_transaction**  STRING |
| **created**  DATE-TIME |
| **currency**  STRING |
| **date**  DATE-TIME |
| **description**  STRING |
| **destination**  STRING |
| **failure\_balance\_transaction**  STRING |
| **id**  STRING |
| **livemode**  BOOLEAN |
| **metadata**  OBJECT |
| **object**  STRING |
| **recipient**  STRING |
| **reversals**  ARRAY |
| **reversed**  BOOLEAN |
| **source\_transaction**  STRING |
| **source\_type**  STRING |
| **statement\_description**  STRING |
| **statement\_descriptor**  STRING |
| **transfer\_group**  STRING |
| **updated**  DATE-TIME |
| **updated\_by\_event\_type**  STRING |
