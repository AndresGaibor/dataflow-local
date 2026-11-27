---
title: "Aftership"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Aftership.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Aftership

Aftership is a shipment tracking application and API for eCommerce retailers and buyers.

Aftership integration replicates data using the [Aftership Tracking, Returns and Shipping API](https://www.aftership.com/docs/shipping/quickstart/api-quick-start?undefined).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To create your API key:

1. Log into your [Aftership](https://accounts.aftership.com/auth/realms/business/protocol/openid-connect/auth?client_id=organization&state=40c75cab-a548-438c-b894-e5bd893194a8&response_mode=fragment&response_type=code&scope=openid&nonce=06e640db-b470-4853-b72b-ff1384ed1369&code_challenge_method=S256&code_challenge=CiedkiYTb9RDhYeCcQysKkNcdu5X8baYt_eILtd2OI0&redirect_uri=https%3A%2F%2Fadmin.aftership.com%2Forganization%2Fapi-keys%3Fas_signup%3Dwww.aftership.com%252Fdocs&page_referrer=admin.aftership.com%2Forganization%2Fapi-keys&page_referrer_referrer=www.aftership.com%2F&as_signup=www.aftership.com%2Fdocs) account.
2. Navigate to Developers > API keys > Create API key.
3. Enter the following information:
   - Name: Enter a name for your API key.
   - Signature Header: Select API key.
   - API permissions: Select Read permission for all scopes, except for Tracking - Estimated delivery dates, where only Write permission is available.
4. Click Save.
5. Copy and paste your API key into a secured file.

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

## Schema

Depending on your destination, table and column names may not appear as they are outlined below.

Replication of all tables and objects requires an Aftership Pro—or higher—subscription.

### trackings

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [AfterShip documentation](https://www.aftership.com/docs/tracking/jh865r66gc6hi-get-trackings) |

### couriers

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [AfterShip documentation](https://www.aftership.com/docs/tracking/ukw8ouy82dp1k-get-couriers) |

### courier\_connections

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [AfterShip documentation](https://www.aftership.com/docs/tracking/2ar6bpph8n7ye-get-courier-connections) |

### item\_returns

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [AfterShip documentation](https://www.aftership.com/docs/returns/wpx1lk91k5ima-get-returns) |

### item\_tags

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [AfterShip documentation](https://www.aftership.com/docs/returns/sxu3emct2h6is-get-item-tags) |

### query\_claims

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [AfterShip documentation](https://www.aftership.com/docs/protection/e99b7b198fd97-query-claims) |

### query\_coverages

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [AfterShip documentation](https://www.aftership.com/docs/protection/0202765fded3f-query-coverages) |

### stores

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [AfterShip documentation](https://www.aftership.com/docs/commerce/yc24p1srfyqiv-get-stores) |

### orders

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [AfterShip documentation](https://www.aftership.com/docs/commerce/kr3dy6e5ma49n-get-orders) |

### products

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [AfterShip documentation](https://www.aftership.com/docs/commerce/rloip27l58tm1-get-products) |

### fulfillments

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [AfterShip documentation](https://www.aftership.com/docs/commerce/6dafeb354dd2b-get-fulfillments) |

### memberships

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [AfterShip documentation](https://www.aftership.com/docs/members/50fa1b4e7b871-get-memberships) |

### roles

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | code |
| **Useful links** | [AfterShip documentation](https://www.aftership.com/docs/members/bb5124963ea73-get-roles) |

### shipping\_rates

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [AfterShip documentation](https://www.aftership.com/docs/shipping/99f88b084657b-get-rates) |

### shipping\_labels

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [AfterShip documentation](https://www.aftership.com/docs/shipping/c056230c3b6c4-get-labels) |

### shipping\_manifests

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [AfterShip documentation](https://www.aftership.com/docs/shipping/8ba86e501d12e-get-manifests) |

### shipping\_couriers

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | slug |
| **Useful links** | [AfterShip documentation](https://www.aftership.com/docs/shipping/89c99df22fcd7-get-all-couriers) |

### cancel\_labels

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [AfterShip documentation](https://www.aftership.com/docs/shipping/24ec02f862c50-get-the-cancelled-labels) |

### pickups

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [AfterShip documentation](https://www.aftership.com/docs/shipping/x8mxu5wa7m6y3-get-pickups) |

### cancel\_pickups

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [AfterShip documentation](https://www.aftership.com/docs/shipping/35p8o3dsqpaqc-get-the-cancelled-pickups) |

### shipper\_accounts

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [AfterShip documentation](https://www.aftership.com/docs/shipping/5742112a2c755-get-shipper-accounts) |

### locations

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | location\_id |
| **Useful links** | [AfterShip documentation](https://www.aftership.com/docs/shipping/bdb851fc7dfdc-get-locations) |
