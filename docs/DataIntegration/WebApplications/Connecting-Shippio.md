---
title: "Shippio"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Shippio.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Shippio

Shippio is a freight forwarding and logistics management platform.

Shippio integration replicates data using the [Shippio REST API](https://shippio.stoplight.io/docs/shippio-api/753cf96a69c40-shippio-api).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with a Shippio Client ID and Client Secret.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To generate your client ID and client secret:

1. Log into your [Shippio](https://app.shippio.jp/) account.
2. Navigate to Settings > API Credentials > Shippio API Applications.
3. Click + New Application.
4. Copy and paste your client ID and client secret into a secured file.

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
| Client Secret | Client secret. |

## Limitations and considerations

- The Shippio API does not provide a date field that can be used as a query parameter. All tables use Full Table replication.
- The Shippio API has a rate limit of 500 requests per minute. It is recommended to use a single task per Shippio connection. Creating multiple tasks replicating from the same Shippio account may cause the API to throttle requests and lead to task failures.
- Tables with large volumes of data (for example, `in_transit_products`) may take a significant amount of time to extract due to full table replication. This can potentially cause tasks to time out.

## Schema

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### addresses

The `addresses` table contains address records in your Shippio account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Shippio API reference](https://shippio.stoplight.io/docs/shippio-api/426cb0ee47dff-get-a-list-of-address "Opens in new tab: Shippio API reference") |

### carriers

The `carriers` table contains carrier records in your Shippio account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Shippio API reference](https://shippio.stoplight.io/docs/shippio-api/17478f3b4e8fa-get-a-list-of-carriers "Opens in new tab: Shippio API reference") |

### companies

The `companies` table contains company records in your Shippio account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Shippio API reference](https://shippio.stoplight.io/docs/shippio-api/6597574e19009-get-a-list-of-companies "Opens in new tab: Shippio API reference") |

### consignees

The `consignees` table contains consignee records in your Shippio account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Shippio API reference](https://shippio.stoplight.io/docs/shippio-api/221ed1e46d192-get-a-list-of-consignees "Opens in new tab: Shippio API reference") |

### containers

The `containers` table contains container records in your Shippio account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Shippio API reference](https://shippio.stoplight.io/docs/shippio-api/33a8b98333cf0-get-a-list-of-containers "Opens in new tab: Shippio API reference") |

### customer\_teams

The `customer_teams` table contains customer team records in your Shippio account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Shippio API reference](https://shippio.stoplight.io/docs/shippio-api/ff5cd3084e2bf-get-a-list-of-customer-teams "Opens in new tab: Shippio API reference") |

### customer\_users

The `customer_users` table contains customer user records in your Shippio account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Shippio API reference](https://shippio.stoplight.io/docs/shippio-api/b01ce4b032304-get-a-list-of-customer-user "Opens in new tab: Shippio API reference") |

### events

The `events` table contains event records in your Shippio account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Shippio API reference](https://shippio.stoplight.io/docs/shippio-api/f60c45a296a41-get-a-list-of-events "Opens in new tab: Shippio API reference") |

### in\_transit\_products

The `in_transit_products` table contains records of products currently in transit in your Shippio account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Shippio API reference](https://shippio.stoplight.io/docs/shippio-api/e31aaf61668e0-get-a-list-of-in-transit-products "Opens in new tab: Shippio API reference") |

### partners

The `partners` table contains partner records in your Shippio account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Shippio API reference](https://shippio.stoplight.io/docs/shippio-api/bb1c7444ed368-get-a-list-of-partner "Opens in new tab: Shippio API reference") |

### ports

The `ports` table contains port records in your Shippio account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Shippio API reference](https://shippio.stoplight.io/docs/shippio-api/72a8a9492f358-get-a-list-of-ports "Opens in new tab: Shippio API reference") |

### products

The `products` table contains product records in your Shippio account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Shippio API reference](https://shippio.stoplight.io/docs/shippio-api/8d4754b558997-get-a-list-of-products "Opens in new tab: Shippio API reference") |

### shipments

The `shipments` table contains shipment records in your Shippio account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Shippio API reference](https://shippio.stoplight.io/docs/shippio-api/4af9bcd3b1c78-get-a-list-of-shipments "Opens in new tab: Shippio API reference") |

### shippers

The `shippers` table contains shipper records in your Shippio account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Shippio API reference](https://shippio.stoplight.io/docs/shippio-api/031ef0a3c825a-get-a-list-of-shippers "Opens in new tab: Shippio API reference") |

### user\_groups

The `user_groups` table contains user group records in your Shippio account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Shippio API reference](https://shippio.stoplight.io/docs/shippio-api/ffd1f144fd5be-get-a-list-of-user-group "Opens in new tab: Shippio API reference") |

### vessels

The `vessels` table contains vessel records in your Shippio account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Shippio API reference](https://shippio.stoplight.io/docs/shippio-api/e5943012cec3c-get-a-list-of-vessels "Opens in new tab: Shippio API reference") |

### warehouses

The `warehouses` table contains warehouse records in your Shippio account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Shippio API reference](https://shippio.stoplight.io/docs/shippio-api/35f0f5e7f93d0-get-a-list-of-warehouses "Opens in new tab: Shippio API reference") |
