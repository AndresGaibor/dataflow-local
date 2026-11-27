---
title: "Segment"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Segment-v2.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Segment

Segment is Twilio's Customer Data Platform (CDP). It collects customer event data from websites, mobile apps, and server-side systems and routes it to analytics tools, marketing platforms, and data warehouse destinations.

Segment integration replicates data using the [Segment Public API](https://www.twilio.com/docs/segment/api/public-api).

This connector replicates workspace configuration and operational metrics from Segment. It does not replicate raw analytics events (track, identify, page, screen, or group calls).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with a Segment Public API token.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To set up your Segment account, you need:

- An active Segment workspace on a Team or Business tier plan. Free and Starter plans have limited Segment Public API support, and some streams may return 403 errors.
- A Segment user with Workspace Owner or Workspace Member role (required to create API tokens).

To create an API token:

1. Log into your [Segment](https://app.segment.com/) account.
2. Navigate to Settings > Workspace settings.
3. Select the Access Management tab.
4. Click the Tokens tab.
5. Click + Create Token.
6. Enter a description for the token, for example QlikDataIntegration.
7. Select Workspace Member access, which is sufficient for read-only access to workspace data.
8. Click Create.
9. Copy and paste your API token into a secured file.

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
| API Token | API token. |

## Limitations and considerations

- The Segment Public API requires a Team or Business tier plan for full access. Some endpoints may return 403 errors on Free or Starter plans.
- The `audit_events` stream requires the Audit Trail feature, which is available on Business tier plans only. Team tier accounts and below should de-select `audit_events` before syncing to avoid 403 errors.
- Usage metric streams (`usage_api_calls_per_source_daily`, `usage_api_calls_workspace_daily`, `usage_mtu_per_source_daily`, and `usage_mtu_workspace_daily`) paginate through data month by month from the configured start date. The day-of-month component of the start date is ignored for these streams — data is fetched from the first day of the calendar month containing the start date. Initial syncs may take longer when the start date is set far in the past.
- As of February 1, 2024, Segment no longer supports creating Config API tokens. Only Public API tokens are supported.

## Schema

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### audit\_events

The `audit_events` table contains the workspace audit trail, including user actions and configuration changes. Requires the Audit Trail feature (Business tier).

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | timestamp |
| **Useful links** | [Segment Public API reference](https://reference.segmentapis.com/ "Opens in new tab: Segment Public API reference") |

### catalog\_destinations

The `catalog_destinations` table contains all available destination types from the Segment Destinations Catalog, across all workspaces.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Segment Public API reference](https://reference.segmentapis.com/ "Opens in new tab: Segment Public API reference") |

### catalog\_sources

The `catalog_sources` table contains all available source types from the Segment Sources Catalog, across all workspaces.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Segment Public API reference](https://reference.segmentapis.com/ "Opens in new tab: Segment Public API reference") |

### catalog\_warehouses

The `catalog_warehouses` table contains all available warehouse types from the Segment Warehouses Catalog, across all workspaces.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Segment Public API reference](https://reference.segmentapis.com/ "Opens in new tab: Segment Public API reference") |

### destination\_delivery\_metrics\_summary

The `destination_delivery_metrics_summary` table contains delivery metrics for each source-to-destination pair in the workspace.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | sourceId, destinationId |
| **Useful links** | [Segment Public API reference](https://reference.segmentapis.com/ "Opens in new tab: Segment Public API reference") |

### destination\_subscriptions

The `destination_subscriptions` table contains event subscriptions configured per destination in the workspace.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Segment Public API reference](https://reference.segmentapis.com/ "Opens in new tab: Segment Public API reference") |

### destinations

The `destinations` table contains data destinations configured in the workspace.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id, sourceId |
| **Useful links** | [Segment Public API reference](https://reference.segmentapis.com/ "Opens in new tab: Segment Public API reference") |

### groups

The `groups` table contains user groups configured in the workspace.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Segment Public API reference](https://reference.segmentapis.com/ "Opens in new tab: Segment Public API reference") |

### source\_connected\_destinations

The `source_connected_destinations` table contains source-to-destination connections in the workspace.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id, sourceId |
| **Useful links** | [Segment Public API reference](https://reference.segmentapis.com/ "Opens in new tab: Segment Public API reference") |

### source\_connected\_warehouses

The `source_connected_warehouses` table contains source-to-warehouse connections in the workspace.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | sourceId |
| **Useful links** | [Segment Public API reference](https://reference.segmentapis.com/ "Opens in new tab: Segment Public API reference") |

### sources

The `sources` table contains data sources configured in the workspace.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Segment Public API reference](https://reference.segmentapis.com/ "Opens in new tab: Segment Public API reference") |

### transformations

The `transformations` table contains data transformations configured in the workspace.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Segment Public API reference](https://reference.segmentapis.com/ "Opens in new tab: Segment Public API reference") |

### usage\_api\_calls\_per\_source\_daily

The `usage_api_calls_per_source_daily` table contains daily API call usage broken down by source.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | sourceId |
| **Replication Key** | timestamp |
| **Useful links** | [Segment Public API reference](https://reference.segmentapis.com/ "Opens in new tab: Segment Public API reference") |

### usage\_api\_calls\_workspace\_daily

The `usage_api_calls_workspace_daily` table contains daily total API call usage for the workspace.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | timestamp |
| **Replication Key** | timestamp |
| **Useful links** | [Segment Public API reference](https://reference.segmentapis.com/ "Opens in new tab: Segment Public API reference") |

### usage\_mtu\_per\_source\_daily

The `usage_mtu_per_source_daily` table contains daily Monthly Tracked Users (MTU) usage broken down by source.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | sourceId |
| **Replication Key** | timestamp |
| **Useful links** | [Segment Public API reference](https://reference.segmentapis.com/ "Opens in new tab: Segment Public API reference") |

### usage\_mtu\_workspace\_daily

The `usage_mtu_workspace_daily` table contains daily total Monthly Tracked Users (MTU) usage for the workspace.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | timestamp |
| **Replication Key** | timestamp |
| **Useful links** | [Segment Public API reference](https://reference.segmentapis.com/ "Opens in new tab: Segment Public API reference") |

### users

The `users` table contains users with access to the workspace.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Segment Public API reference](https://reference.segmentapis.com/ "Opens in new tab: Segment Public API reference") |

### warehouses

The `warehouses` table contains warehouse connections configured in the workspace.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Segment Public API reference](https://reference.segmentapis.com/ "Opens in new tab: Segment Public API reference") |
