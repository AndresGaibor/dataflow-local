---
title: "Branch"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Branch.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Branch

Branch is a mobile attribution and analytics platform that helps organizations measure, optimize, and manage app growth across channels.

Branch integration replicates data using the [Branch Custom Export API](https://help.branch.io/apidocs/custom-exports-api).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To set up your Branch account, you need:

- A Branch account with access to the app you want to replicate.
- An access token with sufficient permissions. To ensure all tables replicate successfully, the token's user must have Export Access and Sensitive data view access enabled. Verify or update these settings in Configurations > Security & Access > Team.
- A custom export dashboard created in the Branch portal. The Custom Export API requires a dashboard to be set up before use. For instructions, see [Prerequisites — API access](https://help.branch.io/apidocs/custom-exports-api#prerequisites-api-access) in the Branch documentation.

To find your Branch App ID and access token:

- **Branch App ID**: In the Branch portal, navigate to Configurations > App Settings > General.
- **Access Token**: In the Branch portal, navigate to Configurations > Security & Access > Credentials.

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
| Branch App ID | App ID. |
| Access Token | Access token. |

## Schema

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### cost

The `cost` table contains ad cost data for your Branch app. This is a non-event table.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Branch API reference](https://help.branch.io/apidocs/custom-exports-api "Opens in new tab: Branch API reference") |

### eo\_branch\_cta\_view

The `eo_branch_cta_view` table contains Branch call-to-action view events for your app. This is a core event table.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Branch API reference](https://help.branch.io/apidocs/custom-exports-api "Opens in new tab: Branch API reference") |

### eo\_branch\_cta\_view\_blocked

The `eo_branch_cta_view_blocked` table contains blocked Branch call-to-action view events for your app. This is a blocked and fraud event table.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Branch API reference](https://help.branch.io/apidocs/custom-exports-api "Opens in new tab: Branch API reference") |

### eo\_click

The `eo_click` table contains ad click events for your Branch app. This is a core event table.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Branch API reference](https://help.branch.io/apidocs/custom-exports-api "Opens in new tab: Branch API reference") |

### eo\_click\_blocked

The `eo_click_blocked` table contains blocked ad click events for your Branch app. This is a blocked and fraud event table.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Branch API reference](https://help.branch.io/apidocs/custom-exports-api "Opens in new tab: Branch API reference") |

### eo\_commerce\_event

The `eo_commerce_event` table contains commerce (purchase) events for your Branch app. This is a core event table.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Branch API reference](https://help.branch.io/apidocs/custom-exports-api "Opens in new tab: Branch API reference") |

### eo\_commerce\_event\_blocked

The `eo_commerce_event_blocked` table contains blocked commerce events for your Branch app. This is a blocked and fraud event table.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Branch API reference](https://help.branch.io/apidocs/custom-exports-api "Opens in new tab: Branch API reference") |

### eo\_content\_event

The `eo_content_event` table contains content interaction events for your Branch app. This is a core event table.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Branch API reference](https://help.branch.io/apidocs/custom-exports-api "Opens in new tab: Branch API reference") |

### eo\_content\_event\_blocked

The `eo_content_event_blocked` table contains blocked content interaction events for your Branch app. This is a blocked and fraud event table.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Branch API reference](https://help.branch.io/apidocs/custom-exports-api "Opens in new tab: Branch API reference") |

### eo\_custom\_event

The `eo_custom_event` table contains custom events defined in your Branch app. This is a core event table.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Branch API reference](https://help.branch.io/apidocs/custom-exports-api "Opens in new tab: Branch API reference") |

### eo\_custom\_event\_blocked

The `eo_custom_event_blocked` table contains blocked custom events for your Branch app. This is a blocked and fraud event table.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Branch API reference](https://help.branch.io/apidocs/custom-exports-api "Opens in new tab: Branch API reference") |

### eo\_dismissal

The `eo_dismissal` table contains banner and interstitial dismissal events for your Branch app. This is a core event table.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Branch API reference](https://help.branch.io/apidocs/custom-exports-api "Opens in new tab: Branch API reference") |

### eo\_impression

The `eo_impression` table contains ad impression events for your Branch app. This is a core event table.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Branch API reference](https://help.branch.io/apidocs/custom-exports-api "Opens in new tab: Branch API reference") |

### eo\_impression\_blocked

The `eo_impression_blocked` table contains blocked ad impression events for your Branch app. This is a blocked and fraud event table.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Branch API reference](https://help.branch.io/apidocs/custom-exports-api "Opens in new tab: Branch API reference") |

### eo\_install

The `eo_install` table contains app install events for your Branch app. This is a core event table.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Branch API reference](https://help.branch.io/apidocs/custom-exports-api "Opens in new tab: Branch API reference") |

### eo\_install\_blocked

The `eo_install_blocked` table contains blocked app install events for your Branch app. This is a blocked and fraud event table.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Branch API reference](https://help.branch.io/apidocs/custom-exports-api "Opens in new tab: Branch API reference") |

### eo\_open

The `eo_open` table contains app open events for your Branch app. This is a core event table.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Branch API reference](https://help.branch.io/apidocs/custom-exports-api "Opens in new tab: Branch API reference") |

### eo\_open\_blocked

The `eo_open_blocked` table contains blocked app open events for your Branch app. This is a blocked and fraud event table.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Branch API reference](https://help.branch.io/apidocs/custom-exports-api "Opens in new tab: Branch API reference") |

### eo\_pageview

The `eo_pageview` table contains web page view events for your Branch app. This is a core event table.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Branch API reference](https://help.branch.io/apidocs/custom-exports-api "Opens in new tab: Branch API reference") |

### eo\_pageview\_blocked

The `eo_pageview_blocked` table contains blocked web page view events for your Branch app. This is a blocked and fraud event table.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Branch API reference](https://help.branch.io/apidocs/custom-exports-api "Opens in new tab: Branch API reference") |

### eo\_reinstall

The `eo_reinstall` table contains app reinstall events for your Branch app. This is a core event table.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Branch API reference](https://help.branch.io/apidocs/custom-exports-api "Opens in new tab: Branch API reference") |

### eo\_reinstall\_blocked

The `eo_reinstall_blocked` table contains blocked app reinstall events for your Branch app. This is a blocked and fraud event table.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Branch API reference](https://help.branch.io/apidocs/custom-exports-api "Opens in new tab: Branch API reference") |

### eo\_san\_touch

The `eo_san_touch` table contains self-attributing network touch events for your Branch app. This is a core event table.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Branch API reference](https://help.branch.io/apidocs/custom-exports-api "Opens in new tab: Branch API reference") |

### eo\_user\_lifecycle\_event

The `eo_user_lifecycle_event` table contains user lifecycle events (for example, registrations and logins) for your Branch app. This is a core event table.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Branch API reference](https://help.branch.io/apidocs/custom-exports-api "Opens in new tab: Branch API reference") |

### eo\_user\_lifecycle\_event\_blocked

The `eo_user_lifecycle_event_blocked` table contains blocked user lifecycle events for your Branch app. This is a blocked and fraud event table.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Branch API reference](https://help.branch.io/apidocs/custom-exports-api "Opens in new tab: Branch API reference") |

### eo\_web\_session\_start

The `eo_web_session_start` table contains web session start events for your Branch app. This is a core event table.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Branch API reference](https://help.branch.io/apidocs/custom-exports-api "Opens in new tab: Branch API reference") |

### eo\_web\_session\_start\_blocked

The `eo_web_session_start_blocked` table contains blocked web session start events for your Branch app. This is a blocked and fraud event table.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Branch API reference](https://help.branch.io/apidocs/custom-exports-api "Opens in new tab: Branch API reference") |

### eo\_web\_to\_app\_auto\_redirect

The `eo_web_to_app_auto_redirect` table contains web-to-app auto-redirect events for your Branch app. This is a core event table.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Branch API reference](https://help.branch.io/apidocs/custom-exports-api "Opens in new tab: Branch API reference") |

### eo\_web\_to\_app\_auto\_redirect\_blocked

The `eo_web_to_app_auto_redirect_blocked` table contains blocked web-to-app auto-redirect events for your Branch app. This is a blocked and fraud event table.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Branch API reference](https://help.branch.io/apidocs/custom-exports-api "Opens in new tab: Branch API reference") |

### skadnetwork\_valid\_messages

The `skadnetwork_valid_messages` table contains valid SKAdNetwork postback messages (iOS) for your Branch app. This is a non-event table.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Branch API reference](https://help.branch.io/apidocs/custom-exports-api "Opens in new tab: Branch API reference") |
