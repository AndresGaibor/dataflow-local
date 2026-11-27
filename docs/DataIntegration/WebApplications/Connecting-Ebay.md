---
title: "eBay"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Ebay.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# eBay

eBay is a global marketplace where businesses and individuals can buy and sell items.

eBay integration replicates data using the [eBay Fulfillment API](https://developer.ebay.com/api-docs/sell/fulfillment/static/overview.html).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To retrieve your client secret and ID:

1. Log into your [eBay](https://developer.ebay.com/signin?return_to=%2Fmy%2Fkeys) developer portal.
2. Go to the Application Keys page.
3. Enter your application name.
4. Under either Sandbox or Production, click Create a keyset.
5. Click OAuth Scopes to confirm the App ID has the required scopes.
6. In the User Tokens field, enter the redirect URL https://connector.qlik.com/auth/oauth/v3.htm.
7. Copy and paste your client secret and client ID into a secured file.

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
| Client Secret | Client secret. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### orders

The orders table contains details about all orders in your eBay seller account.

**Note**: The integration’s **Start Date** must be within 90 days of the current date, if initially creating or resetting the integration. Exceeding 90 days will result in an [eBay 30830 API error](https://developer.ebay.com/api-docs/sell/fulfillment/resources/order/methods/getOrders#h2-error-codes).

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | orderId |
| **Useful links** | [eBay API method](https://developer.ebay.com/api-docs/sell/fulfillment/resources/order/methods/getOrders "Opens in new tab: eBay API method") |

orders table schema

|  |
| --- |
| **buyer**  OBJECT This is a nested data structure:   - username: STRING |
| **buyerCheckoutNotes**  STRING |
| **cancelStatus**  OBJECT This is a nested data structure:   - cancelRequests: ARRAY, which is also a nested data structure.   - cancelCompletedDate: STRING   - cancelInitiator: STRING   - cancelReason: STRING   - cancelRequestId: STRING   - cancelRequestState: STRING   - cancelRequestedDate: STRING - cancelState: STRING - cancelledDate: STRING |
| **creationDate**  STRING |
| **ebayCollectAndRemitTax**  BOOLEAN |
| **fulfillmentHrefs**  ARRAY This is a nested data structure. |
| **fulfillmentStartInstructions**  ARRAY This is a nested data structure:   - ebaySupportedFulfillment: BOOLEAN - finalDestinationAddress: OBJECT, which is also a nested data structure.   - addressLine1: STRING   - addressLine2: STRING   - city: STRING   - countryCode: STRING   - county: STRING   - postalCode: STRING   - stateOrProvince: STRING - fulfillmentInstructionsType: STRING - maxEstimatedDeliveryDate: STRING - minEstimatedDeliveryDate: STRING - pickupStep: OBJECT, which is also a nested data structure.   - merchantLocationKey: STRING - shippingStep: OBJECT, which is also a nested data structure.   - shipTo: OBJECT, which is also a nested data structure.     - companyName: STRING     - contactAddress: OBJECT, which is also a nested data structure.       - addressLine1: STRING       - addressLine2: STRING       - city: STRING       - countryCode: STRING       - county: STRING       - postalCode: STRING       - stateOrProvince: STRING     - email: STRING     - fullName: STRING     - primaryPhone: OBJECT, which is also a nested data structure.       - phoneNumber: STRING   - shipToReferenceId: STRING   - shippingCarrierCode: STRING   - shippingServiceCode: STRING |
| **lastModifiedDate**  STRING |
| **legacyOrderId**  STRING |
| **lineItems**  ARRAY This is a nested data structure:   - appliedPromotions: ARRAY, which is also a nested data structure.   - description: STRING   - discountAmount: OBJECT, which is also a nested data structure.     - convertedFromCurrency: STRING     - convertedFromValue: STRING     - currency: STRING     - value: STRING   - promotionId: STRING - deliveryCost: OBJECT, which is also a nested data structure.   - importCharges: OBJECT, which is also a nested data structure.     - convertedFromCurrency: STRING     - convertedFromValue: STRING     - currency: STRING     - value: STRING   - shippingCost: OBJECT, which is also a nested data structure.     - convertedFromCurrency: STRING     - convertedFromValue: STRING     - currency: STRING     - value: STRING   - shippingIntermediationFee: OBJECT, which is also a nested data structure.     - convertedFromCurrency: STRING     - convertedFromValue: STRING     - currency: STRING     - value: STRING - discountedLineItemCost: OBJECT, which is also a nested data structure.   - convertedFromCurrency: STRING   - convertedFromValue: STRING   - currency: STRING   - value: STRING - ebayCollectAndRemitTaxes: ARRAY, which is also a nested data structure.   - amount: OBJECT, which is also a nested data structure.     - convertedFromCurrency: STRING     - convertedFromValue: STRING     - currency: STRING     - value: STRING   - taxType: STRING - giftDetails: OBJECT, which is also a nested data structure.   - message: STRING   - recipientEmail: STRING   - senderName: STRING - legacyItemId: STRING - legacyVariationId: STRING - lineItemCost: OBJECT, which is also a nested data structure.   - convertedFromCurrency: STRING   - convertedFromValue: STRING   - currency: STRING   - value: STRING - lineItemFulfillmentInstructions: OBJECT, which is also a nested data structure.   - guaranteedDelivery: BOOLEAN   - maxEstimatedDeliveryDate: STRING   - minEstimatedDeliveryDate: STRING   - shipByDate: STRING - lineItemFulfillmentStatus: STRING - lineItemId: STRING - listingMarketplaceId: STRING - properties: OBJECT, which is also a nested data structure.   - buyerProtection: BOOLEAN   - fromBestOffer: BOOLEAN   - soldViaAdCampaign: BOOLEAN - purchaseMarketplaceId: STRING - quantity: INTEGER - refunds: ARRAY, which is also a nested data structure.   - amount: OBJECT, which is also a nested data structure.     - convertedFromCurrency: STRING     - convertedFromValue: STRING     - currency: STRING     - value: STRING   - refundDate: STRING   - refundReferenceId: STRING - sku: STRING - soldFormat: STRING - taxes: ARRAY, which is also a nested data structure.   - amount: OBJECT, which is also a nested data structure.     - convertedFromCurrency: STRING     - convertedFromValue: STRING     - currency: STRING     - value: STRING - title: STRING - total: OBJECT, which is also a nested data structure.   - convertedFromCurrency: STRING   - convertedFromValue: STRING   - currency: STRING   - value: STRING |
| **orderFulfillmentStatus**  STRING |
| **orderId**  STRING |
| **orderPaymentStatus**  STRING |
| **paymentSummary**  OBJECT This is a nested data structure:   - payments: ARRAY, which is also a nested data structure.   - amount: OBJECT, which is also a nested data structure.     - convertedFromCurrency: STRING     - convertedFromValue: STRING     - currency: STRING     - value: STRING   - paymentDate: STRING   - paymentHolds: ARRAY, which is also a nested data structure.     - expectedReleaseDate: STRING     - holdAmount: OBJECT, which is also a nested data structure.       - convertedFromCurrency: STRING       - convertedFromValue: STRING       - currency: STRING       - value: STRING     - holdReason: STRING     - holdState: STRING     - releaseDate: STRING     - sellerActionsToRelease: ARRAY, which is also a nested data structure.       - sellerActionToRelease: STRING   - paymentMethod: STRING   - paymentReferenceId: STRING   - paymentStatus: STRING - refunds: ARRAY, which is also a nested data structure.   - amount: OBJECT, which is also a nested data structure.     - convertedFromCurrency: STRING     - convertedFromValue: STRING     - currency: STRING     - value: STRING   - refundDate: STRING   - refundReferenceId: STRING   - refundStatus: STRING - totalDueSeller: OBJECT, which is also a nested data structure.   - convertedFromCurrency: STRING   - convertedFromValue: STRING   - currency: STRING   - value: STRING |
| **pricingSummary**  OBJECT This is a nested data structure:   - adjustment: OBJECT, which is also a nested data structure.   - convertedFromCurrency: STRING   - convertedFromValue: STRING   - currency: STRING   - value: STRING - deliveryCost: OBJECT, which is also a nested data structure.   - convertedFromCurrency: STRING   - convertedFromValue: STRING   - currency: STRING   - value: STRING - deliveryDiscount: OBJECT, which is also a nested data structure.   - convertedFromCurrency: STRING   - convertedFromValue: STRING   - currency: STRING   - value: STRING - fee: OBJECT, which is also a nested data structure.   - convertedFromCurrency: STRING   - convertedFromValue: STRING   - currency: STRING   - value: STRING - priceDiscountSubtotal: OBJECT, which is also a nested data structure.   - convertedFromCurrency: STRING   - convertedFromValue: STRING   - currency: STRING   - value: STRING - priceSubtotal: OBJECT, which is also a nested data structure.   - convertedFromCurrency: STRING   - convertedFromValue: STRING   - currency: STRING   - value: STRING - tax: OBJECT, which is also a nested data structure.   - convertedFromCurrency: STRING   - convertedFromValue: STRING   - currency: STRING   - value: STRING - total: OBJECT, which is also a nested data structure.   - convertedFromCurrency: STRING   - convertedFromValue: STRING   - currency: STRING   - value: STRING |
| **salesRecordReference**  STRING |
| **sellerId**  STRING |
