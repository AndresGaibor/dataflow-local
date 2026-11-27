---
title: "Shopify"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Shopify-v2.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Shopify

Shopify is an e-commerce platform. You can use Shopify as a data source when landing or replicating data with the new Shopify connector in Qlik Talend Cloud.

Shopify integration replicates data using the [Shopify GraphQL Admin API](https://shopify.dev/docs/api/admin-graphql).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To set up your Shopify account, you need:

- Your Shopify store short name (the part before `.myshopify.com`).
- A Shopify app in the Shopify Dev Dashboard with a client ID and client secret.
- The app and target store in the same Shopify organization. The client credentials grant is only available for apps in your organization's Dev Dashboard installed in stores that you own. Apps distributed through the Shopify App Store or created from the store admin cannot be used with this connector.
- The app installed on the target store (installation is per store).

To create the app and retrieve your credentials:

1. Log into your [Shopify Dev Dashboard](https://accounts.shopify.com/lookup?rid=642f670f-b1dd-4f14-aaba-b48058790157&verify=1786106416-xVbUfcTXVzZO%2BU9yQ3Ww%2BwmvIwYsBqJDm3a7VxtTOhQ%3D).
2. Create a custom app for your organization.
3. Configure the app's access scopes to grant read access to the resources you intend to replicate.
4. Install the app on the store that you want to replicate.
5. Navigate to Settings, and copy-paste your client ID and client secret into a secured file.

### Access scopes to grant

Grant read access for each resource you intend to replicate. Metafields are covered by the scope of the resource they are attached to.

All tables are offered for selection regardless of which scopes have been granted, so the list you see when setting up a task does not tell you what the app can actually read. Scopes are enforced when the task runs. Grant the scopes for the tables you intend to select before running a task.

| Grant this scope | To replicate these tables |
| --- | --- |
| `read_orders` | `orders`, `order_refunds`, `order_shipping_lines`, `transactions`, `abandoned_checkouts`, `metafields_orders` |
| `read_products` | `products`, `product_variants`, `collections`, `metafields_products`, `metafields_collections` |
| `read_customers` | `customers`, `metafields_customers` |
| `read_inventory` | `inventory_items`, `inventory_levels` |
| `read_locations` | `locations`, `inventory_levels` |
| `read_assigned_fulfillment_orders`, `read_merchant_managed_fulfillment_orders`, `read_third_party_fulfillment_orders` | `fulfillment_orders` |

The `events` table returns activity log entries for store resources rather than one resource type of its own. Grant the scopes for the resources whose events you want to see.

Two scopes deserve particular attention:

- `read_all_orders`: by default, `read_orders` only exposes orders created in the last 60 days. To replicate older order history, request `read_all_orders` from Shopify. This is a restricted scope that Shopify grants on request, not one you can simply select. Without it, a start date earlier than 60 days ago returns no data before the 60-day boundary.
- `read_users`: the `author` field on the `events` table requires this scope, which Shopify makes available on Shopify Plus plans only. Where it is not granted, `events` replicates without that one field and the rest of the table is unaffected.

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
| Shopify Shop | Shopify store short name (the part before `.myshopify.com`). |
| Client ID | Client ID. |
| Client Secret | Client secret. |

## Limitations and considerations

- **Deletes are not captured.** The connector replicates inserts and updates only. A record deleted in Shopify remains in the destination. Use a periodic full reload if you need deletes reflected.
- **Order history older than 60 days needs an extra scope.** See `read_all_orders` in the access scopes section above.
- **Only one replication task per store and app can run at a time.** The `orders` table uses Shopify's bulk operations API, which allows only one bulk query per store per app at a time. If a second task starts against the same store while the first is still running, the connector waits and backs off for up to roughly ten minutes before failing. Schedule tasks so they do not overlap, or use a separate Shopify app per task.
- **Large order backfills can take a long time.** A bulk operation is submitted per date window and Shopify processes it asynchronously. Reducing Date Window Size produces more, smaller operations, which usually finishes sooner on a large store.
- **Start Date applies to the initial sync only.** Once a table has a stored bookmark, later syncs resume from it. Changing Start Date does not retroactively re-replicate data.
- **Incremental runs can re-deliver boundary records.** Each incremental run filters from the previous run's high-water mark inclusive, so records whose timestamp exactly equals it are replicated again. Records are keyed on `id`, so this resolves to an upsert in the destination rather than a duplicate.
- **Rate limits are handled automatically.** Shopify applies per-store API limits and returns `HTTP 429 Too Many Requests` when they are exceeded. The connector waits and retries. Server errors and timeouts are retried separately, up to 5 attempts, with exponential backoff.
- **Access tokens are refreshed automatically.** Shopify access tokens expire after 24 hours. The connector requests a new one as needed. The client ID and client secret do not expire, but if the secret is rotated in the Dev Dashboard the new value must be saved to the connection.
- **Selecting a table the app cannot read fails the task.** Because every table is offered regardless of scope, it is possible to select one the app has not been granted access to. The task then fails when it reaches that table. The `fulfillment_orders` table is handled differently: the connector skips it, replicates the remaining selected tables, and reports that the connection needs to be re-authorized with the fulfillment order scopes.
- **Adding a scope later requires reinstalling the app.** If you grant a new scope after installation, apply it to the app in the Dev Dashboard and reinstall the app on the store before rerunning the task.

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

Every table carries three additional columns identifying the store the record came from: `_sdc_shop_id`, `_sdc_shop_name`, and `_sdc_shop_myshopify_domain`.

Two tables use `createdAt` as the replication key rather than `updatedAt`: `locations` (because the Shopify locations query does not support filtering on `updatedAt`, so a modified location is not picked up by an incremental run) and `transactions` (because transactions are read through their parent order, not as a top-level resource).

### abandoned\_checkouts

The `abandoned_checkouts` table contains info about abandoned checkouts. Shopify considers a checkout to be abandoned when a customer has entered billing and shipping details, but hasn’t completed the purchase.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [abandoned\_checkouts schema on GitHub](https://github.com/singer-io/tap-shopify/blob/master/tap_shopify/schemas/abandoned_checkouts.json "Opens in new tab: Shopify API method")  [Shopify API method](https://shopify.dev/docs/api/admin-graphql/latest/queries/abandonedCheckouts "Opens in new tab: Shopify API method") |

abandoned\_checkouts table foreign keys

| Join abandoned\_checkouts with | on |
| --- | --- |
| [customers](#customers) | ``` abandoned_checkouts.customer.id = customers.id ```  ``` abandoned_checkouts.customers.lastOrder.id = customers.lastOrder.id ``` |
| [order\_refunds](#order-refunds) | ``` abandoned_checkouts.customers.lastOrder.id = order_refunds.order.id ```  ``` abandoned_checkouts.lineItems.product.id = order_refunds.refundLineItems.lineItem.product.id ``` |
| [orders](#orders) | ``` abandoned_checkouts.customers.lastOrder.id = orders.id ```  ``` abandoned_checkouts.lineItems.product.id = orders.lineItems.product.id ``` |
| [transactions](#transactions) | ``` abandoned_checkouts.customers.lastOrder.id = transactions.order.id ``` |
| [products](#products) | ``` abandoned_checkouts.lineItems.product.id = products.id ``` |

abandoned\_checkouts table schema

|  |
| --- |
| **note**  STRING |
| **completedAt**  STRING |
| **billing\_address**  OBJECT This is a nested data structure:   - phone: STRING - country: STRING - firstName: STRING - name: STRING - latitude: STRING - zip: STRING - lastName: STRING - province: STRING - address2: STRING - address1: STRING - countryCodeV2: STRING - city: STRING - company: STRING - provinceCode: STRING - longitude: STRING - coordinatesValidated: BOOLEAN - formattedArea: STRING - id: STRING - timeZone: STRING - validationResultSummary: STRING |
| **discountCodes**  ARRAY This is a nested data structure. |
| **createdAt**  STRING |
| **updatedAt**  STRING |
| **taxLines**  ARRAY This is a nested data structure:   - priceSet: OBJECT, which is also a nested data structure.   - presentmentMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING   - shopMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING - title: STRING - rate: NUMBER - source: STRING - channelLiable: BOOLEAN - ratePercentage: NUMBER |
| **totalLineItemsPriceSet**  OBJECT This is a nested data structure:   - presentmentMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING - shopMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING |
| **id**  STRING |
| **name**  STRING |
| **totalTaxSet**  OBJECT This is a nested data structure:   - presentmentMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING - shopMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING |
| **shippingAddress**  OBJECT This is a nested data structure:   - phone: STRING - country: STRING - firstName: STRING - name: STRING - latitude: STRING - zip: STRING - lastName: STRING - province: STRING - address2: STRING - address1: STRING - countryCodeV2: STRING - city: STRING - company: STRING - provinceCode: STRING - longitude: STRING - coordinatesValidated: BOOLEAN - formattedArea: STRING - id: STRING - timeZone: STRING - validationResultSummary: STRING |
| **abandonedCheckoutUrl**  STRING |
| **totalDiscountSet**  OBJECT This is a nested data structure:   - presentmentMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING - shopMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING |
| **taxesIncluded**  BOOLEAN |
| **totalDutiesSet**  OBJECT This is a nested data structure:   - presentmentMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING - shopMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING |
| **totalPriceSet**  OBJECT This is a nested data structure:   - presentmentMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING - shopMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING |
| **lineItems**  ARRAY This is a nested data structure:   - id: STRING - quantity: INTEGER - sku: STRING - title: STRING - variantTitle: STRING - variant: OBJECT, which is also a nested data structure.   - title: STRING   - id: STRING - discountedTotalPriceSet: OBJECT, which is also a nested data structure.   - presentmentMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING   - shopMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING - components: ARRAY, which is also a nested data structure.   - id: STRING   - quantity: INTEGER   - title: STRING   - variantTitle: STRING - customAttributes: ARRAY, which is also a nested data structure.   - key: STRING   - value: STRING - product: OBJECT, which is also a nested data structure.   - id: STRING - discountedUnitPriceSet: OBJECT, which is also a nested data structure.   - presentmentMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING   - shopMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING - discountedUnitPriceWithCodeDiscount: OBJECT, which is also a nested data structure.   - presentmentMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING   - shopMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING - originalTotalPriceSet: OBJECT, which is also a nested data structure.   - presentmentMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING   - shopMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING - originalUnitPriceSet: OBJECT, which is also a nested data structure.   - presentmentMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING   - shopMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING |
| **subtotalPriceSet**  OBJECT This is a nested data structure:   - presentmentMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING - shopMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING |
| **customer**  OBJECT This is a nested data structure:   - id: STRING - lastOrder: OBJECT, which is also a nested data structure.   - id: STRING |

### collections

The `collections` table contains info about collections.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [collections schema on GitHub](https://github.com/singer-io/tap-shopify/blob/master/tap_shopify/schemas/collections.json "Opens in new tab: Shopify API method")  [Shopify API method](https://shopify.dev/docs/api/admin-graphql/latest/queries/collections "Opens in new tab: Shopify API method") |

collections table schema

|  |
| --- |
| **id**  STRING |
| **title**  STRING |
| **handle**  STRING |
| **collectionType**  STRING |
| **updatedAt**  STRING |
| **productsCount**  OBJECT This is a nested data structure:   - count: INTEGER - precision: STRING |
| **sortOrder**  STRING |
| **ruleSet**  OBJECT This is a nested data structure:   - appliedDisjunctively: BOOLEAN - rules: ARRAY, which is also a nested data structure.   - column: STRING   - condition: STRING   - relation: STRING |
| **seo**  OBJECT This is a nested data structure:   - description: STRING - title: STRING |
| **feedback**  OBJECT This is a nested data structure:   - summary: STRING |
| **products**  ARRAY This is a nested data structure. |

### customers

The `customers` table contains info about the shop’s customers. This includes their contact details, order history, and email marketing preferences.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [Shopify documentation](https://shopify.dev/docs/api/admin-graphql/latest/queries/customers "Opens in new tab: Shopify API method")  [customers schema on GitHub](https://github.com/singer-io/tap-shopify/blob/master/tap_shopify/schemas/customers.json "Opens in new tab: Shopify API method") |

customers table foreign keys

| Join custom\_collections with | on |
| --- | --- |
| [abandoned\_checkouts](#abandoned-checkouts) | ``` customers.id = abandoned_checkouts.customers.id ```  ``` customers.lastOrder.id = abandoned_checkouts.customers.lastOrder.id ``` |
| [order\_refunds](#order-refunds) | ``` customers.lastOrder.id = order_refunds.order.id ``` |
| [orders](#orders) | ``` customers.lastOrder.id = orders.id ``` |
| [transactions](#transactions) | ``` customers.lastOrder.id = transactions.order.id ``` |

customers table schema

|  |
| --- |
| **email**  STRING |
| **multipassIdentifier**  STRING |
| **defaultAddress**  OBJECT This is a nested data structure:   - city: STRING - address1: STRING - zip: STRING - id: STRING - province: STRING - phone: STRING - country: STRING - firstName: STRING - lastName: STRING - countryCodeV2: STRING - name: STRING - provinceCode: STRING - address2: STRING - company: STRING - timeZone: STRING - validationResultSummary: STRING - latitude: STRING - longitude: STRING - coordinatesValidated: BOOLEAN - formattedArea: STRING |
| **numberOfOrders**  STRING |
| **state**  STRING |
| **verifiedEmail**  BOOLEAN |
| **firstName**  STRING |
| **updatedAt**  STRING |
| **note**  STRING |
| **phone**  STRING |
| **addresses**  ARRAY This is a nested data structure:   - city: STRING - address1: STRING - zip: STRING - id: STRING - province: STRING - phone: STRING - country: STRING - firstName: STRING - lastName: STRING - countryCodeV2: STRING - name: STRING - provinceCode: STRING - address2: STRING - company: STRING - timeZone: STRING - validationResultSummary: STRING - latitude: STRING - longitude: STRING - coordinatesValidated: BOOLEAN - formattedArea: STRING |
| **lastName**  STRING |
| **tags**  ARRAY This is a nested data structure. |
| **taxExempt**  BOOLEAN |
| **id**  STRING |
| **createdAt**  STRING |
| **taxExemptions**  ARRAY This is a nested data structure. |
| **emailMarketingConsent**  OBJECT This is a nested data structure:   - consentUpdatedAt: STRING - marketingOptInLevel: STRING - marketingState: STRING |
| **smsMarketingConsent**  OBJECT This is a nested data structure:   - consentCollectedFrom: STRING - consentUpdatedAt: STRING - marketingOptInLevel: STRING - marketingState: STRING |
| **validEmailAddress**  BOOLEAN |
| **productSubscriberStatus**  STRING |
| **amountSpent**  OBJECT This is a nested data structure:   - amount: STRING - currencyCode: STRING |
| **dataSaleOptOut**  BOOLEAN |
| **displayName**  STRING |
| **locale**  STRING |
| **lifetimeDuration**  STRING |
| **lastOrder**  OBJECT This is a nested data structure:   - id: STRING |

### events

The `events` table contains info about events in the shop.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | createdAt |
| **Useful links** | [Shopify documentation](https://shopify.dev/docs/api/admin-graphql/latest/queries/event)  [events schema on GitHub](https://github.com/singer-io/tap-shopify/blob/master/tap_shopify/schemas/events.json "Opens in new tab: Shopify API method") |

events table schema

|  |
| --- |
| **id**  STRING |
| **createdAt**  STRING |
| **action**  STRING |
| **appTitle**  STRING |
| **attributeToApp**  BOOLEAN |
| **attributeToUser**  BOOLEAN |
| **criticalAlert**  BOOLEAN |
| **message**  STRING |
| **subjectId**  STRING |
| **subjectType**  STRING |
| **additionalContent**  STRING |
| **additionalData**  STRING |
| **arguments**  ARRAY This is a nested data structure. |
| **hasAdditionalContent**  BOOLEAN |
| **secondaryMessage**  STRING |
| **attachments**  ARRAY This is a nested data structure. |
| **author**  OBJECT This is a nested data structure:   - id: STRING |
| **canDelete**  BOOLEAN |
| **canEdit**  BOOLEAN |
| **edited**  BOOLEAN |
| **rawMessage**  STRING |

### fulfillment\_orders

The `fulfillment_orders` table contains datails about fulfillment orders.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Shopify documentation](https://shopify.dev/docs/api/admin-graphql/latest/queries/fulfillmentorders)  [fulfillment\_orders schema on GitHub](https://github.com/singer-io/tap-shopify/blob/master/tap_shopify/schemas/fulfillment_orders.json "Opens in new tab: Shopify API method") |

fulfillment\_orders table schema

|  |
| --- |
| **id**  STRING |
| **orderId**  STRING |
| **updatedAt**  STRING |
| **supportedActions**  ARRAY This is a nested data structure:   - action: STRING - externalUrl: STRING |
| **status**  STRING |
| **requestStatus**  STRING |
| **orderProcessedAt**  STRING |
| **orderName**  STRING |
| **channelId**  STRING |
| **fulfillAt**  STRING |
| **fulfillBy**  STRING |
| **createdAt**  STRING |
| **destination**  OBJECT This is a nested data structure:   - address1: STRING - address2: STRING - city: STRING - province: STRING - zip: STRING - countryCode: STRING - company: STRING - email: STRING - firstName: STRING - lastName: STRING - phone: STRING - id: STRING - location: OBJECT, which is also a nested data structure.   - id: STRING |
| **fulfillmentHolds**  ARRAY This is a nested data structure:   - displayReason: STRING - handle: STRING - reason: STRING - reasonNotes: STRING - id: STRING - heldByRequestingApp: BOOLEAN |
| **internationalDuties**  ARRAY This is a nested data structure:   - id: STRING - methodType: STRING - presentedName: STRING - serviceCode: STRING - sourceReference: STRING - minDeliveryDateTime: STRING - maxDeliveryDateTime: STRING - brandedPromise: OBJECT, which is also a nested data structure.   - handle: STRING   - name: STRING - additionalInformation: OBJECT, which is also a nested data structure.   - instructions: STRING   - phone: STRING |
| **deliveryMethod**  OBJECT This is a nested data structure:   - id: STRING - methodType: STRING - presentedName: STRING - serviceCode: STRING - sourceReference: STRING - minDeliveryDateTime: STRING - maxDeliveryDateTime: STRING - brandedPromise: OBJECT, which is also a nested data structure.   - handle: STRING   - name: STRING - additionalInformation: OBJECT, which is also a nested data structure.   - instructions: STRING   - phone: STRING |
| **assignedLocation**  OBJECT This is a nested data structure:   - address1: STRING - address2: STRING - city: STRING - province: STRING - zip: STRING - countryCode: STRING - name: STRING - phone: STRING - location: OBJECT, which is also a nested data structure.   - id: STRING |
| **merchantRequests**  ARRAY This is a nested data structure:   - id: STRING - kind: STRING - message: STRING - requestOptions: OBJECT, which is also a nested data structure. - responseData: OBJECT, which is also a nested data structure. - sentAt: STRING - fulfillmentOrder: OBJECT, which is also a nested data structure.   - id: STRING |
| **locationsForMove**  ARRAY This is a nested data structure:   - message: STRING - movable: BOOLEAN - unavailableLineItemsCount: OBJECT, which is also a nested data structure.   - count: INTEGER   - precision: STRING - availableLineItemsCount: OBJECT, which is also a nested data structure.   - count: INTEGER   - precision: STRING - location: OBJECT, which is also a nested data structure.   - id: STRING - availableLineItems: ARRAY, which is also a nested data structure. - unavailableLineItems: ARRAY, which is also a nested data structure.   - id: STRING |
| **fulfillmentOrdersForMerge**  ARRAY This is a nested data structure:   - id: STRING |
| **fulfillments**  ARRAY This is a nested data structure:   - id: STRING - name: STRING - status: STRING - displayStatus: STRING - requiresShipping: BOOLEAN - totalQuantity: INTEGER - createdAt: STRING - updatedAt: STRING - inTransitAt: STRING - deliveredAt: STRING - estimatedDeliveryAt: STRING - originAddress: OBJECT, which is also a nested data structure.   - address1: STRING   - address2: STRING   - city: STRING   - provinceCode: STRING   - zip: STRING   - countryCode: STRING - trackingInfo: ARRAY, which is also a nested data structure.   - company: STRING   - number: STRING   - url: STRING - service: OBJECT, which is also a nested data structure.   - id: STRING - location: OBJECT, which is also a nested data structure.   - id: STRING - fulfillmentOrders: ARRAY, which is also a nested data structure.   - id: STRING - fulfillmentLineItems: ARRAY, which is also a nested data structure.   - id: STRING   - quantity: NUMBER   - originalTotalSet: OBJECT, which is also a nested data structure.     - presentmentMoney: OBJECT, which is also a nested data structure.       - currencyCode: STRING       - amount: NUMBER     - shopMoney: OBJECT, which is also a nested data structure.       - currencyCode: STRING       - amount: NUMBER   - discountedTotalSet: OBJECT, which is also a nested data structure.     - presentmentMoney: OBJECT, which is also a nested data structure.       - currencyCode: STRING       - amount: NUMBER     - shopMoney: OBJECT, which is also a nested data structure.       - currencyCode: STRING       - amount: NUMBER   - lineItem: OBJECT, which is also a nested data structure.     - id: STRING - legacyResourceId: STRING - order: OBJECT, which is also a nested data structure.   - id: STRING - events: ARRAY, which is also a nested data structure.   - id: STRING |
| **legacyResourceId**  STRING |
| **order**  OBJECT This is a nested data structure:   - id: STRING |
| **events**  ARRAY This is a nested data structure:   - id: STRING |

### inventory\_items

The `inventory_items` table contains info about items in a shop.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [Shopify documentation](https://shopify.dev/docs/api/admin-graphql/latest/queries/inventoryitems)  [inventory\_items schema on GitHub](https://github.com/singer-io/tap-shopify/blob/master/tap_shopify/schemas/inventory_items.json "Opens in new tab: Shopify API method") |

inventory\_items table schema

|  |
| --- |
| **id**  STRING |
| **sku**  STRING |
| **createdAt**  STRING |
| **updatedAt**  STRING |
| **requiresShipping**  BOOLEAN |
| **unitCost**  OBJECT This is a nested data structure:   - amount: STRING |
| **countryCodeOfOrigin**  STRING |
| **provinceCodeOfOrigin**  STRING |
| **harmonizedSystemCode**  STRING |
| **tracked**  BOOLEAN |
| **countryHarmonizedSystemCodes**  ARRAY This is a nested data structure:   - countryCode: STRING - harmonizedSystemCode: STRING |

### inventory\_levels

The `inventory_levels` table contains info about quantities of an inventory item for a location.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [Shopify documentation](https://shopify.dev/docs/api/admin-graphql/latest/queries/inventorylevel)  [inventory\_levels schema on GitHub](https://github.com/singer-io/tap-shopify/blob/master/tap_shopify/schemas/inventory_levels.json "Opens in new tab: Shopify API method") |

inventory\_levels table schema

|  |
| --- |
| **id**  STRING |
| **canDeactivate**  BOOLEAN |
| **createdAt**  STRING |
| **updatedAt**  STRING |
| **deactivationAlert**  STRING |
| **item**  ARRAY This is a nested data structure:   - id: STRING - variant: OBJECT, which is also a nested data structure.   - id: STRING |
| **location**  OBJECT This is a nested data structure:   - id: STRING |
| **quantities**  ARRAY This is a nested data structure:   - id: STRING - name: STRING - quantity: INTEGER - updatedAt: STRING |

### locations

The `locations` table contains info about locations.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | createdAt |
| **Useful links** | [Shopify documentation](https://shopify.dev/docs/api/admin-graphql/latest/queries/locations)  [locations schema on GitHub](https://github.com/singer-io/tap-shopify/blob/master/tap_shopify/schemas/locations.json "Opens in new tab: Shopify API method") |

locations table schema

|  |
| --- |
| **id**  STRING |
| **name**  STRING |
| **updatedAt**  STRING |
| **createdAt**  STRING |
| **isActive**  BOOLEAN |
| **addressVerified**  BOOLEAN |
| **deactivatable**  BOOLEAN |
| **deactivatedAt**  STRING |
| **deletable**  BOOLEAN |
| **fulfillsOnlineOrders**  BOOLEAN |
| **hasActiveInventory**  BOOLEAN |
| **hasUnfulfilledOrders**  BOOLEAN |
| **isFulfillmentService**  BOOLEAN |
| **legacyResourceId**  STRING |
| **shipsInventory**  BOOLEAN |
| **address**  OBJECT This is a nested data structure:   - countryCode: STRING - address1: STRING - city: STRING - address2: STRING - provinceCode: STRING - zip: STRING - province: STRING - phone: STRING - country: STRING - formatted: ARRAY, which is also a nested data structure. - latitude: STRING - longitude: STRING |
| **localPickupSettingsV2**  OBJECT This is a nested data structure:   - instructions: STRING - pickupTime: STRING |

### metafields\_collections

The `metafields_collections` table contains info about metafields for collections.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [Shopify API method](https://shopify.dev/docs/api/admin-graphql/latest/objects/metafield "Opens in new tab: Shopify API method")  [metafields\_collections schema on GitHub](https://github.com/singer-io/tap-shopify/blob/master/tap_shopify/schemas/metafields_collections.json "Opens in new tab: Shopify API method") |

metafields\_collections table schema

|  |
| --- |
| **owner**  OBJECT This is a nested data structure:   - id: STRING |
| **ownerType**  STRING |
| **value\_type**  STRING |
| **key**  STRING |
| **createdAt**  STRING |
| **id**  STRING |
| **namespace**  STRING |
| **description**  STRING |
| **value**  INTEGER, OBJECT, STRING This is a nested data structure. |
| **updatedAt**  STRING |
| **type**  STRING |

### metafields\_customers

The `metafields_customers` table contains info about metafields for customers.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [Shopify API method](https://shopify.dev/docs/api/admin-graphql/latest/objects/metafield "Opens in new tab: Shopify API method")  [metafields\_customers schema on GitHub](https://github.com/singer-io/tap-shopify/blob/master/tap_shopify/schemas/metafields_customers.json "Opens in new tab: Shopify API method") |

metafields\_customers table schema

|  |
| --- |
| **owner**  OBJECT This is a nested data structure:   - id: STRING |
| **ownerType**  STRING |
| **value\_type**  STRING |
| **key**  STRING |
| **createdAt**  STRING |
| **id**  STRING |
| **namespace**  STRING |
| **description**  STRING |
| **value**  INTEGER, OBJECT, STRING This is a nested data structure. |
| **updatedAt**  STRING |
| **type**  STRING |

### metafields\_orders

The `metafields_orders` table contains info about metafields for orders.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [Shopify API method](https://shopify.dev/docs/api/admin-graphql/latest/objects/metafield "Opens in new tab: Shopify API method")  [metafields\_orders schema on GitHub](https://github.com/singer-io/tap-shopify/blob/master/tap_shopify/schemas/metafields_orders.json "Opens in new tab: Shopify API method") |

metafields\_orders table schema

|  |
| --- |
| **owner**  OBJECT This is a nested data structure:   - id: STRING |
| **ownerType**  STRING |
| **value\_type**  STRING |
| **key**  STRING |
| **createdAt**  STRING |
| **id**  STRING |
| **namespace**  STRING |
| **description**  STRING |
| **value**  INTEGER, OBJECT, STRING This is a nested data structure. |
| **updatedAt**  STRING |
| **type**  STRING |

### metafields\_products

The `metafields_products` table contains info about metafields for products.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [Shopify API method](https://shopify.dev/docs/api/admin-graphql/latest/objects/metafield "Opens in new tab: Shopify API method")  [metafields\_products schema on GitHub](https://github.com/singer-io/tap-shopify/blob/master/tap_shopify/schemas/metafields_products.json "Opens in new tab: Shopify API method") |

metafields\_products table schema

|  |
| --- |
| **owner**  OBJECT This is a nested data structure:   - id: STRING |
| **ownerType**  STRING |
| **value\_type**  STRING |
| **key**  STRING |
| **createdAt**  STRING |
| **id**  STRING |
| **namespace**  STRING |
| **description**  STRING |
| **updatedAt**  STRING |
| **value**  INTEGER, OBJECT, STRING This is a nested data structure. |
| **type**  STRING |

### order\_refunds

The `order_refunds` table contains info about refunds associated with orders.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | createdAt |
| **Useful links** | [Shopify API method](https://shopify.dev/Content/admin-api/rest/reference/orders/refund?api[version]=2019-07 "Opens in new tab: Shopify API method")  [order\_refunds schema on GitHub](https://github.com/singer-io/tap-shopify/blob/master/tap_shopify/schemas/order_refunds.json "Opens in new tab: Shopify API method") |

order\_refunds table foreign keys

| Join order\_refunds with | on |
| --- | --- |
| [abandoned\_checkouts](#abandoned-checkouts) | ``` order_refunds.order.id = abandoned_checkouts.customers.lastOrder.id ```  ``` order_refunds.refundLineItems.lineItem.product.id = abandoned_checkouts.lineItems.product.id ``` |
| [customers](#customers) | ``` order_refunds.order.id = customers.lastOrder.id ``` |
| [orders](#orders) | ``` order_refunds.order.id = orders.id ```  ``` order_refunds.refundLineItems.lineItem.product.id = orders.lineItems.product.id ``` |
| [transactions](#transactions) | ``` order_refunds.order.id = transactions.order.id ``` |
| [products](#products) | ``` order_refunds.refundLineItems.lineItem.product.id = products.id ``` |

order\_refunds table schema

|  |
| --- |
| **id**  STRING |
| **createdAt**  STRING |
| **legacyResourceId**  STRING |
| **note**  STRING |
| **order**  OBJECT This is a nested data structure:   - id: STRING |
| **refundLineItems**  ARRAY This is a nested data structure:   - id: STRING - quantity: INTEGER - priceSet: OBJECT, which is also a nested data structure.   - presentmentMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING   - shopMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING - restockType: STRING - restocked: BOOLEAN - location: OBJECT, which is also a nested data structure.   - id: STRING - subtotalSet: OBJECT, which is also a nested data structure.   - presentmentMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING   - shopMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING - totalTaxSet: OBJECT, which is also a nested data structure.   - presentmentMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING   - shopMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING - lineItem: OBJECT, which is also a nested data structure.   - id: STRING   - vendor: STRING   - quantity: INTEGER   - title: STRING   - requiresShipping: BOOLEAN   - originalTotalSet: OBJECT, which is also a nested data structure.     - presentmentMoney: OBJECT, which is also a nested data structure.       - amount: STRING       - currencyCode: STRING     - shopMoney: OBJECT, which is also a nested data structure.       - amount: STRING       - currencyCode: STRING   - taxLines: ARRAY, which is also a nested data structure.     - priceSet: OBJECT, which is also a nested data structure.       - presentmentMoney: OBJECT, which is also a nested data structure.         - amount: STRING         - currencyCode: STRING       - shopMoney: OBJECT, which is also a nested data structure.         - amount: STRING         - currencyCode: STRING     - rate: NUMBER     - title: STRING     - source: STRING     - channelLiable: BOOLEAN   - taxable: BOOLEAN   - isGiftCard: BOOLEAN   - name: STRING   - discountedTotalSet: OBJECT, which is also a nested data structure.     - presentmentMoney: OBJECT, which is also a nested data structure.       - amount: STRING       - currencyCode: STRING     - shopMoney: OBJECT, which is also a nested data structure.       - amount: STRING       - currencyCode: STRING   - sku: STRING   - product: OBJECT, which is also a nested data structure.     - id: STRING   - discountAllocations: ARRAY, which is also a nested data structure.     - allocatedAmountSet: OBJECT, which is also a nested data structure.       - presentmentMoney: OBJECT, which is also a nested data structure.         - amount: STRING         - currencyCode: STRING       - shopMoney: OBJECT, which is also a nested data structure.         - amount: STRING         - currencyCode: STRING     - discountApplication: OBJECT, which is also a nested data structure.       - index: INTEGER       - targetType: STRING       - targetSelection: STRING       - allocationMethod: STRING       - value: OBJECT, which is also a nested data structure.         - \_\_typename: STRING         - amount: NUMBER         - currencyCode: STRING         - percentage: NUMBER   - customAttributes: ARRAY, which is also a nested data structure.     - key: STRING     - value: STRING   - totalDiscountSet: OBJECT, which is also a nested data structure.     - presentmentMoney: OBJECT, which is also a nested data structure.       - amount: STRING       - currencyCode: STRING     - shopMoney: OBJECT, which is also a nested data structure.       - amount: STRING       - currencyCode: STRING   - duties: ARRAY, which is also a nested data structure.     - harmonizedSystemCode: STRING     - id: STRING     - taxLines: ARRAY, which is also a nested data structure.       - rate: NUMBER       - source: STRING       - title: STRING       - channelLiable: BOOLEAN       - priceSet: OBJECT, which is also a nested data structure.         - presentmentMoney: OBJECT, which is also a nested data structure.           - amount: STRING           - currencyCode: STRING         - shopMoney: OBJECT, which is also a nested data structure.           - amount: STRING           - currencyCode: STRING     - countryCodeOfOrigin: STRING   - discountedUnitPriceSet: OBJECT, which is also a nested data structure.     - presentmentMoney: OBJECT, which is also a nested data structure.       - amount: STRING       - currencyCode: STRING     - shopMoney: OBJECT, which is also a nested data structure.       - amount: STRING       - currencyCode: STRING |
| **orderAdjustments**  ARRAY This is a nested data structure:   - amountSet: OBJECT, which is also a nested data structure.   - presentmentMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING   - shopMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING - id: STRING - reason: STRING - taxAmountSet: OBJECT, which is also a nested data structure.   - presentmentMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING   - shopMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING |
| **updatedAt**  STRING |

### order\_shipping\_lines

The `order_shipping_lines` table contains the shipping details that the customer chose for their order.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Shopify API method](https://shopify.dev/docs/api/admin-graphql/latest/objects/ShippingLine "Opens in new tab: Shopify API method")  [order\_shipping\_lines schema on GitHub](https://github.com/singer-io/tap-shopify/blob/master/tap_shopify/schemas/order_shipping_lines.json "Opens in new tab: Shopify API method") |

order\_shipping\_lines table schema

|  |
| --- |
| **carrierIdentifier**  STRING |
| **code**  STRING |
| **orderId**  STRING |
| **currentDiscountedPriceSet**  OBJECT This is a nested data structure:   - presentmentMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING - shopMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING |
| **custom**  BOOLEAN |
| **deliveryCategory**  STRING |
| **discountAllocations**  ARRAY This is a nested data structure:   - allocatedAmountSet: OBJECT, which is also a nested data structure.   - presentmentMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING   - shopMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING - discountApplication: OBJECT, which is also a nested data structure.   - \_\_typename: STRING   - allocationMethod: STRING   - index: INTEGER   - targetSelection: STRING   - targetType: STRING   - title: STRING   - code: STRING   - description: STRING   - value: OBJECT, which is also a nested data structure.     - \_\_typename: STRING     - amount: STRING     - currencyCode: STRING     - percentage: NUMBER |
| **discountedPriceSet**  OBJECT This is a nested data structure:   - presentmentMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING - shopMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING |
| **id**  STRING |
| **isRemoved**  BOOLEAN |
| **originalPriceSet**  OBJECT This is a nested data structure:   - presentmentMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING - shopMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING |
| **phone**  STRING |
| **shippingRateHandle**  STRING |
| **source**  STRING |
| **taxLines**  ARRAY This is a nested data structure:   - channelLiable: BOOLEAN - priceSet: OBJECT, which is also a nested data structure.   - presentmentMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING   - shopMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING - rate: NUMBER - ratePercentage: STRING - source: STRING - title: STRING |
| **title**  STRING |
| **updatedAt**  STRING |

### orders

The `orders` table contains info about a shop’s completed orders.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [Shopify documentation](https://shopify.dev/docs/api/admin-graphql/latest/queries/orders)  [orders schema on GitHub](https://github.com/singer-io/tap-shopify/blob/master/tap_shopify/schemas/orders.json "Opens in new tab: Shopify API method") |

orders table foreign keys

| Join orders with | on |
| --- | --- |
| [abandoned\_checkouts](#abandoned-checkouts) | ``` orders.id = abandoned_checkouts.customers.lastOrder.id ```  ``` orders.lineItems.product.id = abandoned_checkouts.lineItems.product.id ``` |
| [customers](#customers) | ``` orders.id = customers.lastOrder.id ``` |
| [order\_refunds](#order-refunds) | ``` orders.id = order_refunds.order.id ```  ``` orders.lineItems.product.id = order_refunds.refundLineItems.lineItem.product.id ``` |
| [transactions](#transactions) | ``` orders.id = transactions.order.id ``` |
| [products](#products) | ``` orders.lineItems.product.id = products.id ``` |

orders table schema

|  |
| --- |
| **additionalFees**  ARRAY This is a nested data structure:   - id: STRING - name: STRING - price: OBJECT, which is also a nested data structure.   - presentmentMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING   - shopMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING - taxLines: ARRAY, which is also a nested data structure.   - channelLiable: BOOLEAN   - priceSet: OBJECT, which is also a nested data structure.     - presentmentMoney: OBJECT, which is also a nested data structure.       - amount: STRING       - currencyCode: STRING     - shopMoney: OBJECT, which is also a nested data structure.       - amount: STRING       - currencyCode: STRING   - rate: NUMBER   - ratePercentage: NUMBER   - source: STRING   - title: STRING |
| **app**  OBJECT This is a nested data structure:   - id: STRING - name: STRING - icon: OBJECT, which is also a nested data structure.   - id: STRING |
| **billingAddress**  OBJECT This is a nested data structure:   - address1: STRING - address2: STRING - city: STRING - company: STRING - coordinatesValidated: BOOLEAN - country: STRING - countryCodeV2: STRING - firstName: STRING - formattedArea: STRING - id: STRING - lastName: STRING - latitude: NUMBER - longitude: NUMBER - name: STRING - phone: STRING - province: STRING - provinceCode: STRING - timeZone: STRING - validationResultSummary: STRING - zip: STRING |
| **billingAddressMatchesShippingAddress**  BOOLEAN |
| **canMarkAsPaid**  BOOLEAN |
| **canNotifyCustomer**  BOOLEAN |
| **cancelReason**  STRING |
| **cancellation**  OBJECT This is a nested data structure:   - staffNote: STRING |
| **cancelledAt**  STRING |
| **capturable**  BOOLEAN |
| **cartDiscountAmountSet**  OBJECT This is a nested data structure:   - presentmentMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING - shopMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING |
| **channelInformation**  OBJECT This is a nested data structure:   - id: STRING - channelId: STRING |
| **clientIp**  STRING |
| **closed**  BOOLEAN |
| **closedAt**  STRING |
| **confirmationNumber**  STRING |
| **confirmed**  BOOLEAN |
| **createdAt**  STRING |
| **currencyCode**  STRING |
| **currentCartDiscountAmountSet**  OBJECT This is a nested data structure:   - presentmentMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING - shopMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING |
| **currentShippingPriceSet**  OBJECT This is a nested data structure:   - presentmentMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING - shopMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING |
| **currentSubtotalLineItemsQuantity**  INTEGER |
| **currentSubtotalPriceSet**  OBJECT This is a nested data structure:   - presentmentMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING - shopMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING |
| **currentTotalAdditionalFeesSet**  OBJECT This is a nested data structure:   - presentmentMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING - shopMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING |
| **currentTotalDiscountsSet**  OBJECT This is a nested data structure:   - presentmentMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING - shopMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING |
| **currentTotalDutiesSet**  OBJECT This is a nested data structure:   - presentmentMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING - shopMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING |
| **currentTotalPriceSet**  OBJECT This is a nested data structure:   - presentmentMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING - shopMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING |
| **currentTotalTaxSet**  OBJECT This is a nested data structure:   - presentmentMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING - shopMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING |
| **currentTotalWeight**  NUMBER |
| **customer**  OBJECT This is a nested data structure:   - id: STRING - email: STRING - firstName: STRING - lastName: STRING - state: STRING - verifiedEmail: BOOLEAN - lastOrder: OBJECT, which is also a nested data structure.   - id: STRING - updatedAt: STRING - createdAt: STRING - note: STRING - multipassIdentifier: STRING - tags: STRING - taxExempt: STRING - taxExemptions: STRING - defaultAddress: OBJECT, which is also a nested data structure.   - address1: STRING   - address2: STRING   - city: STRING   - countryCodeV2: STRING   - province: STRING   - zip: STRING   - id: STRING   - country: STRING   - lastName: STRING   - phone: STRING   - firstName: STRING   - name: STRING   - provinceCode: STRING   - company: STRING - addresses: ARRAY, which is also a nested data structure.   - address1: STRING   - address2: STRING   - city: STRING   - countryCodeV2: STRING   - province: STRING   - zip: STRING   - id: STRING   - country: STRING   - lastName: STRING   - phone: STRING   - firstName: STRING   - name: STRING   - provinceCode: STRING   - company: STRING |
| **customerJourneySummary**  OBJECT This is a nested data structure. |
| **merchantOfRecordApp**  OBJECT This is a nested data structure:   - id: STRING |
| **customerAcceptsMarketing**  BOOLEAN |
| **customerLocale**  STRING |
| **discountCodes**  ARRAY This is a nested data structure. |
| **discountCode**  STRING |
| **displayFinancialStatus**  STRING |
| **displayFulfillmentStatus**  STRING |
| **disputes**  ARRAY This is a nested data structure:   - id: STRING - initiatedAs: STRING - status: STRING |
| **dutiesIncluded**  BOOLEAN |
| **email**  STRING |
| **estimatedTaxes**  BOOLEAN |
| **fulfillable**  BOOLEAN |
| **fullyPaid**  BOOLEAN |
| **hasTimelineComment**  BOOLEAN |
| **fulfillmentsCount**  OBJECT This is a nested data structure:   - count: INTEGER - precisions: STRING |
| **id**  STRING |
| **legacyResourceId**  STRING |
| **merchantBusinessEntity**  OBJECT This is a nested data structure:   - address: OBJECT, which is also a nested data structure.   - address1: STRING   - address2: STRING   - city: STRING   - countryCode: STRING   - province: STRING   - zip: STRING - companyName: STRING - displayName: STRING - id: STRING - primary: BOOLEAN |
| **name**  STRING |
| **note**  STRING |
| **netPaymentSet**  OBJECT This is a nested data structure:   - presentmentMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING - shopMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING |
| **originalTotalAdditionalFeesSet**  OBJECT This is a nested data structure:   - presentmentMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING - shopMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING |
| **originalTotalDutiesSet**  OBJECT This is a nested data structure:   - presentmentMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING - shopMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING |
| **originalTotalPriceSet**  OBJECT This is a nested data structure:   - presentmentMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING - shopMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING |
| **paymentGatewayNames**  ARRAY This is a nested data structure. |
| **phone**  STRING |
| **poNumber**  STRING |
| **presentmentCurrencyCode**  STRING |
| **processedAt**  STRING |
| **refundable**  BOOLEAN |
| **refundDiscrepancySet**  OBJECT This is a nested data structure:   - presentmentMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING - shopMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING |
| **registeredSourceUrl**  STRING |
| **requiresShipping**  STRING |
| **restockable**  STRING |
| **returnStatus**  STRING |
| **shippingAddress**  OBJECT This is a nested data structure:   - address1: STRING - address2: STRING - city: STRING - company: STRING - coordinatesValidated: BOOLEAN - country: STRING - countryCodeV2: STRING - firstName: STRING - formattedArea: STRING - id: STRING - lastName: STRING - latitude: NUMBER - longitude: NUMBER - name: STRING - phone: STRING - province: STRING - provinceCode: STRING - timeZone: STRING - validationResultSummary: STRING - zip: STRING |
| **shopifyProtect**  OBJECT This is a nested data structure:   - eligibility: OBJECT, which is also a nested data structure.   - status: STRING - status: STRING |
| **sourceIdentifier**  STRING |
| **sourceName**  STRING |
| **statusPageUrl**  STRING |
| **subtotalLineItemsQuantity**  INTEGER |
| **subtotalPriceSet**  OBJECT This is a nested data structure:   - presentmentMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING - shopMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING |
| **tags**  ARRAY This is a nested data structure. |
| **taxExempt**  BOOLEAN |
| **taxLines**  ARRAY This is a nested data structure:   - channelLiable: BOOLEAN - priceSet: OBJECT, which is also a nested data structure.   - presentmentMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING   - shopMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING - rate: NUMBER - ratePercentage: NUMBER - source: STRING - title: STRING |
| **taxesIncluded**  BOOLEAN |
| **test**  BOOLEAN |
| **totalCapturableSet**  OBJECT This is a nested data structure:   - presentmentMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING - shopMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING |
| **totalCashRoundingAdjustment**  OBJECT This is a nested data structure:     - paymentSet: OBJECT, which is also a nested data structure.   - presentmentMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING   - shopMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING - refundSet: OBJECT, which is also a nested data structure.   - presentmentMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING   - shopMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING |
| **totalDiscountsSet**  OBJECT This is a nested data structure:   - presentmentMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING - shopMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING |
| **totalOutstandingSet**  OBJECT This is a nested data structure:   - presentmentMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING - shopMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING |
| **totalPriceSet**  OBJECT This is a nested data structure:   - presentmentMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING - shopMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING |
| **totalReceivedSet**  OBJECT This is a nested data structure:   - presentmentMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING - shopMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING |
| **totalRefundedSet**  OBJECT This is a nested data structure:   - presentmentMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING - shopMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING |
| **totalRefundedShippingSet**  OBJECT This is a nested data structure:   - presentmentMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING - shopMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING |
| **totalShippingPriceSet**  OBJECT This is a nested data structure:   - presentmentMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING - shopMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING |
| **totalTaxSet**  OBJECT This is a nested data structure:   - presentmentMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING - shopMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING |
| **totalTipReceivedSet**  OBJECT This is a nested data structure:   - presentmentMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING - shopMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING |
| **totalWeight**  NUMBER |
| **transactionsCount**  OBJECT This is a nested data structure:   - count: INTEGER - precision: STRING |
| **unpaid**  BOOLEAN |
| **updatedAt**  STRING |
| **fulfillments**  ARRAY This is a nested data structure:   - id: STRING - name: STRING - status: STRING - totalQuantity: NUMBER - updatedAt: STRING - deliveredAt: STRING - estimatedDeliveryAt: STRING - requiresShipping: BOOLEAN - inTransitAt: STRING - trackingInfo: ARRAY, which is also a nested data structure.   - number: STRING   - company: STRING   - url: STRING - service: OBJECT, which is also a nested data structure.   - serviceName: STRING   - id: STRING   - handle: STRING   - trackingSupport: BOOLEAN   - type: STRING   - permitsSkuSharing: BOOLEAN   - inventoryManagement: BOOLEAN |
| **lineItems**  ARRAY This is a nested data structure:   - id: STRING - vendor: STRING - quantity: NUMBER - title: STRING - requiresShipping: BOOLEAN - originalTotalSet: OBJECT, which is also a nested data structure.   - presentmentMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING   - shopMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING - taxLines: ARRAY, which is also a nested data structure.   - priceSet: OBJECT, which is also a nested data structure.     - presentmentMoney: OBJECT, which is also a nested data structure.       - amount: STRING       - currencyCode: STRING     - shopMoney: OBJECT, which is also a nested data structure.       - amount: STRING       - currencyCode: STRING   - rate: NUMBER   - title: STRING   - source: STRING   - channelLiable: BOOLEAN - taxable: BOOLEAN - isGiftCard: BOOLEAN - name: STRING - discountedTotalSet: OBJECT, which is also a nested data structure.   - presentmentMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING   - shopMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING - sku: STRING - product: OBJECT, which is also a nested data structure.   - id: STRING - discountAllocations: ARRAY, which is also a nested data structure.   - allocatedAmountSet: OBJECT, which is also a nested data structure.     - presentmentMoney: OBJECT, which is also a nested data structure.       - amount: STRING       - currencyCode: STRING     - shopMoney: OBJECT, which is also a nested data structure.       - amount: STRING       - currencyCode: STRING   - discountApplication: OBJECT, which is also a nested data structure.     - index: INTEGER     - title: STRING     - targetType: STRING     - targetSelection: STRING     - allocationMethod: STRING     - value: OBJECT, which is also a nested data structure.       - \_\_typename: STRING       - amount: NUMBER       - currencyCode: STRING       - percentage: NUMBER - customAttributes: ARRAY, which is also a nested data structure.   - key: STRING   - value: STRING - totalDiscountSet: OBJECT, which is also a nested data structure.   - presentmentMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING   - shopMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING - duties: ARRAY, which is also a nested data structure.   - harmonizedSystemCode: STRING   - id: STRING   - taxLines: ARRAY, which is also a nested data structure.     - rate: NUMBER     - source: STRING     - title: STRING     - channelLiable: BOOLEAN     - priceSet: OBJECT, which is also a nested data structure.       - presentmentMoney: OBJECT, which is also a nested data structure.         - amount: STRING         - currencyCode: STRING       - shopMoney: OBJECT, which is also a nested data structure.         - amount: STRING         - currencyCode: STRING   - countryCodeOfOrigin: STRING - discountedUnitPriceSet: OBJECT, which is also a nested data structure.   - presentmentMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING   - shopMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING - originalUnitPriceSet: OBJECT, which is also a nested data structure.   - presentmentMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING   - shopMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING - unfulfilledDiscountedTotalSet: OBJECT, which is also a nested data structure.   - presentmentMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING   - shopMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING - unfulfilledOriginalTotalSet: OBJECT, which is also a nested data structure.   - presentmentMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING   - shopMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING - variant: OBJECT, which is also a nested data structure.   - id: STRING |
| **shippingLine**  OBJECT This is a nested data structure:   - carrierIdentifier: STRING - code: STRING - currentDiscountedPriceSet: OBJECT, which is also a nested data structure.   - presentmentMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING   - shopMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING - custom: BOOLEAN - deliveryCategory: STRING - discountAllocations: ARRAY, which is also a nested data structure.   - allocatedAmountSet: OBJECT, which is also a nested data structure.     - presentmentMoney: OBJECT, which is also a nested data structure.       - amount: STRING       - currencyCode: STRING     - shopMoney: OBJECT, which is also a nested data structure.       - amount: STRING       - currencyCode: STRING   - discountApplication: OBJECT, which is also a nested data structure.     - \_\_typename: STRING     - allocationMethod: STRING     - index: INTEGER     - targetSelection: STRING     - targetType: STRING     - title: STRING     - code: STRING     - description: STRING     - value: OBJECT, which is also a nested data structure.       - \_\_typename: STRING       - amount: STRING       - currencyCode: STRING       - percentage: NUMBER - discountedPriceSet: OBJECT, which is also a nested data structure.   - presentmentMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING   - shopMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING - id: STRING - isRemoved: BOOLEAN - originalPriceSet: OBJECT, which is also a nested data structure.   - presentmentMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING   - shopMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING - phone: STRING - shippingRateHandle: STRING - source: STRING - taxLines: ARRAY, which is also a nested data structure.   - channelLiable: BOOLEAN   - priceSet: OBJECT, which is also a nested data structure.     - presentmentMoney: OBJECT, which is also a nested data structure.       - amount: STRING       - currencyCode: STRING     - shopMoney: OBJECT, which is also a nested data structure.       - amount: STRING       - currencyCode: STRING   - rate: NUMBER   - ratePercentage: STRING   - source: STRING   - title: STRING - title: STRING - finiiiii |

### product\_variants

The `product_variants` table contains info about variants that can be added to a product to represent one version of a product with several options.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [Shopify documentation](https://shopify.dev/docs/api/admin-graphql/latest/queries/productvariants)  [product\_variants schema on GitHub](https://github.com/singer-io/tap-shopify/blob/master/tap_shopify/schemas/product_variants.json "Opens in new tab: Shopify API method") |

product\_variants table schema

|  |
| --- |
| **id**  STRING |
| **createdAt**  STRING |
| **barcode**  STRING |
| **availableForSale**  BOOLEAN |
| **compareAtPrice**  STRING |
| **displayName**  STRING |
| **image**  OBJECT This is a nested data structure:   - altText: STRING - height: INTEGER - id: STRING - url: STRING - width: INTEGER |
| **inventoryPolicy**  STRING |
| **inventoryQuantity**  INTEGER |
| **position**  INTEGER |
| **price**  STRING |
| **requiresComponents**  BOOLEAN |
| **sellableOnlineQuantity**  INTEGER |
| **sku**  STRING |
| **taxCode**  STRING |
| **taxable**  BOOLEAN |
| **title**  STRING |
| **updatedAt**  STRING |
| **product**  OBJECT This is a nested data structure:   - id: STRING |
| **inventoryItem**  OBJECT This is a nested data structure:   - id: STRING - measurement: OBJECT, which is also a nested data structure.   - weight: OBJECT, which is also a nested data structure.     - unit: STRING     - value: STRING |

### products

The `products` table contains info about a shop’s products.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [Shopify documentation](https://shopify.dev/docs/api/admin-graphql/latest/queries/products)  [products schema on GitHub](https://github.com/singer-io/tap-shopify/blob/master/tap_shopify/schemas/products.json "Opens in new tab: Shopify API method") |

products table foreign keys

| Join products with | on |
| --- | --- |
| [abandoned\_checkouts](#abandoned-checkouts) | ``` products.id = abandoned_checkouts.lineItems.product.id ``` |
| [order\_refunds](#order-refunds) | ``` products.id = order_refunds.refundLineItems.lineItem.product.id ``` |
| [orders](#orders) | ``` products.id = orders.lineItems.product.id ``` |

products table schema

|  |
| --- |
| **status**  STRING |
| **publishedAt**  STRING |
| **createdAt**  STRING |
| **vendor**  STRING |
| **updatedAt**  STRING |
| **productType**  STRING |
| **tags**  STRING |
| **options**  ARRAY This is a nested data structure:   - name: STRING - values: ARRAY, which is also a nested data structure. - id: STRING - position: INTEGER |
| **handle**  STRING |
| **templateSuffix**  STRING |
| **title**  STRING |
| **id**  STRING |
| **giftCardTemplateSuffix**  STRING |
| **hasOnlyDefaultVariant**  STRING |
| **hasOutOfStockVariants**  BOOLEAN |
| **hasVariantsThatRequiresComponents**  BOOLEAN |
| **isGiftCard**  BOOLEAN |
| **description**  STRING |
| **descriptionHtml**  STRING |
| **category**  OBJECT This is a nested data structure:   - id: STRING |
| **featuredMedia**  OBJECT This is a nested data structure:   - id: STRING - mediaContentType: STRING - status: STRING |
| **requiresSellingPlan**  BOOLEAN |
| **totalInventory**  INTEGER |
| **tracksInventory**  BOOLEAN |
| **media**  ARRAY This is a nested data structure:   - id: STRING - alt: STRING - status: STRING - mediaContentType: STRING - embedUrl: STRING - mimeType: STRING - filename: STRING - image: OBJECT, which is also a nested data structure.   - id: STRING   - url: STRING   - width: STRING   - height: STRING - sources: ARRAY, which is also a nested data structure.   - url: STRING   - format: STRING   - mimeType: STRING   - fileSize: STRING - mediaWarnings: ARRAY, which is also a nested data structure.   - code: STRING   - message: STRING - mediaErrors: ARRAY, which is also a nested data structure.   - code: STRING   - details: STRING   - message: STRING |

### transactions

The `transactions` table contains info about transactions.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | createdAt |
| **Useful links** | [Shopify API method](https://shopify.dev/Content/admin-api/rest/reference/orders/transaction?api[version]=2019-07 "Opens in new tab: Shopify API method")  [transactions schema on GitHub](https://github.com/singer-io/tap-shopify/blob/master/tap_shopify/schemas/transactions.json "Opens in new tab: Shopify API method") |

transactions table foreign keys

| Join transactions with | on |
| --- | --- |
| [abandoned\_checkouts](#abandoned-checkouts) | ``` transactions.order.id = abandoned_checkouts.customers.lastOrder.id ``` |
| [customers](#customers) | ``` transactions.order.id = customers.lastOrder.id ``` |
| [order\_refunds](#order-refunds) | ``` transactions.order.id = order_refunds.order.id ``` |
| [orders](#orders) | ``` transactions.order.id = orders.id ``` |

transactions table schema

|  |
| --- |
| **accountNumber**  STRING |
| **amountRoundingSet**  OBJECT This is a nested data structure:   - presentmentMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING - shopMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING |
| **amountSet**  OBJECT This is a nested data structure:   - presentmentMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING - shopMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING |
| **authorizationCode**  STRING |
| **authorizationExpiresAt**  STRING |
| **createdAt**  STRING |
| **errorCode**  STRING |
| **formattedGateway**  STRING |
| **gateway**  STRING |
| **id**  STRING |
| **kind**  STRING |
| **manualPaymentGateway**  BOOLEAN |
| **maximumRefundableV2**  OBJECT This is a nested data structure. |
| **multiCapturable**  BOOLEAN |
| **order**  OBJECT This is a nested data structure:   - id: STRING |
| **parentTransaction**  OBJECT This is a nested data structure:   - accountNumber: STRING - createdAt: STRING - id: STRING - status: STRING - paymentId: STRING - processedAt: STRING - amountSet: OBJECT, which is also a nested data structure.   - presentmentMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING   - shopMoney: OBJECT, which is also a nested data structure.     - amount: STRING     - currencyCode: STRING |
| **paymentId**  STRING |
| **processedAt**  STRING |
| **receiptJson**  STRING |
| **settlementCurrency**  STRING |
| **settlementCurrencyRate**  STRING |
| **shopifyPaymentsSet**  OBJECT This is a nested data structure:   - extendedAuthorizationSet: OBJECT, which is also a nested data structure.   - extendedAuthorizationExpiresAt: STRING   - standardAuthorizationExpiresAt: STRING - refundSet: OBJECT, which is also a nested data structure.   - acquirerReferenceNumber: STRING |
| **status**  STRING |
| **test**  BOOLEAN |
| **totalUnsettledSet**  OBJECT This is a nested data structure:   - presentmentMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING - shopMoney: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING |
| **fees**  ARRAY This is a nested data structure:   - id: STRING - rate: NUMBER - rateName: STRING - taxAmount: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING - type: STRING - flatFeeName: STRING - amount: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING - flatFee: OBJECT, which is also a nested data structure.   - amount: STRING   - currencyCode: STRING |
| **manuallyCapturable**  BOOLEAN |
| **paymentDetails**  OBJECT This is a nested data structure:   - avsResultCode: STRING - bin: STRING - company: STRING - cvvResultCode: STRING - expirationMonth: INTEGER - expirationYear: INTEGER - name: STRING - number: STRING - paymentMethodName: STRING - wallet: STRING - paymentDescriptor: STRING |
