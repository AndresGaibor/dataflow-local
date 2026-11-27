---
title: "FrontApp"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-FrontApp.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# FrontApp

FrontApp is a customer communication platform that combines emails, apps, and teammates into a single view.

Front integration replicates data using the [Front API](https://dev.frontapp.com/).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

Before you begin authentication, make sure you meet the following requirements:

- You have a FrontApp developer account.
- You are a company admin in FrontApp, which is required to create an API token in the FrontApp portal.

To generate your API token:

1. Log into your [Front](https://app.frontapp.com/signin) account.
2. Go to Settings > Company > Developers.
3. Go to the API Tokens tab.
4. Click Create API token.
5. Specify an API token name.
6. Specify a token Scope.
7. Click Create.
8. Copy and paste your API token into a secured file.

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
| Token | Token. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

The schema and info displayed below is for version 2.

Depending on your destination, table and column names may not appear as they are outlined below.

### accounts\_table

The `accounts_table` table contains data about accounts in your Front account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | report\_id |
| **Replication Keys** | analytics\_date  analytics\_range |
| **Useful links** | [Front documentation](https://dev.frontapp.com/reference/analytics) |

accounts\_table table schema

|  |
| --- |
| **analytics\_date**  STRING |
| **analytics\_range**  STRING |
| **avg\_first\_response\_time**  NUMBER |
| **avg\_handle\_time**  NUMBER |
| **avg\_response\_time**  NUMBER |
| **avg\_sla\_breach\_time**  NUMBER |
| **avg\_total\_reply\_time**  NUMBER |
| **metric\_description**  STRING |
| **metric\_id**  STRING |
| **new\_segments\_count**  NUMBER |
| **num\_active\_segments\_full**  NUMBER |
| **num\_archived\_segments**  NUMBER |
| **num\_archived\_segments\_with\_reply**  NUMBER |
| **num\_closed\_segments**  NUMBER |
| **num\_csat\_survey\_response**  NUMBER |
| **num\_messages\_received**  NUMBER |
| **num\_messages\_sent**  NUMBER |
| **num\_open\_segments\_end**  NUMBER |
| **num\_open\_segments\_start**  NUMBER |
| **num\_sla\_breach**  NUMBER |
| **num\_workload\_segments**  NUMBER |
| **pct\_csat\_survey\_satisfaction**  NUMBER |
| **pct\_tagged\_conversations**  NUMBER |
| **report\_id**  STRING |

### channels\_table

The `channels_table` table contains data about channels in your Front account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | report\_id |
| **Replication Keys** | analytics\_date  analytics\_range |
| **Useful links** | [Front documentation](https://dev.frontapp.com/reference/analytics) |

channels\_table table schema

|  |
| --- |
| **analytics\_date**  STRING |
| **analytics\_range**  STRING |
| **avg\_first\_response\_time**  NUMBER |
| **avg\_handle\_time**  NUMBER |
| **avg\_response\_time**  NUMBER |
| **avg\_sla\_breach\_time**  NUMBER |
| **avg\_total\_reply\_time**  NUMBER |
| **metric\_description**  STRING |
| **metric\_id**  STRING |
| **new\_segments\_count**  NUMBER |
| **num\_active\_segments\_full**  NUMBER |
| **num\_archived\_segments**  NUMBER |
| **num\_archived\_segments\_with\_reply**  NUMBER |
| **num\_closed\_segments**  NUMBER |
| **num\_csat\_survey\_response**  NUMBER |
| **num\_messages\_received**  NUMBER |
| **num\_messages\_sent**  NUMBER |
| **num\_open\_segments\_end**  NUMBER |
| **num\_open\_segments\_start**  NUMBER |
| **num\_sla\_breach**  NUMBER |
| **num\_workload\_segments**  NUMBER |
| **pct\_csat\_survey\_satisfaction**  NUMBER |
| **pct\_tagged\_conversations**  NUMBER |
| **report\_id**  STRING |

### inboxes\_table

The `inboxes_table` table contains data about inboxes in your Front account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | report\_id |
| **Replication Keys** | analytics\_date  analytics\_range |
| **Useful links** | [Front documentation](https://dev.frontapp.com/reference/analytics) |

inboxes\_table table schema

|  |
| --- |
| **analytics\_date**  STRING |
| **analytics\_range**  STRING |
| **avg\_first\_response\_time**  NUMBER |
| **avg\_handle\_time**  NUMBER |
| **avg\_response\_time**  NUMBER |
| **avg\_sla\_breach\_time**  NUMBER |
| **avg\_total\_reply\_time**  NUMBER |
| **metric\_description**  STRING |
| **metric\_id**  STRING |
| **new\_segments\_count**  NUMBER |
| **num\_active\_segments\_full**  NUMBER |
| **num\_archived\_segments**  NUMBER |
| **num\_archived\_segments\_with\_reply**  NUMBER |
| **num\_closed\_segments**  NUMBER |
| **num\_csat\_survey\_response**  NUMBER |
| **num\_messages\_received**  NUMBER |
| **num\_messages\_sent**  NUMBER |
| **num\_open\_segments\_end**  NUMBER |
| **num\_open\_segments\_start**  NUMBER |
| **num\_sla\_breach**  NUMBER |
| **num\_workload\_segments**  NUMBER |
| **pct\_csat\_survey\_satisfaction**  NUMBER |
| **pct\_tagged\_conversations**  NUMBER |
| **report\_id**  STRING |

### tags\_table

The `tags_table` table contains a list of tag statistics since the last completed replication job through the most recent iteration of the defined [**Incremental Range**](#add-stitch-data-source) (day or hour).
This table will include tags in your Front account.
**Note**: During the historical replication job, all increments (defined using the **Incremental Range** setting) since the **Start Date** will be replicated. This will result in the first record for this table being an aggregated record across all tags.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | report\_id |
| **Replication Keys** | analytics\_date  analytics\_range |
| **Useful links** | [Front documentation](https://dev.frontapp.com/reference/analytics) |

tags\_table table schema

|  |
| --- |
| **analytics\_date**  STRING |
| **analytics\_range**  STRING |
| **avg\_first\_response\_time**  NUMBER |
| **avg\_handle\_time**  NUMBER |
| **avg\_response\_time**  NUMBER |
| **avg\_sla\_breach\_time**  NUMBER |
| **avg\_total\_reply\_time**  NUMBER |
| **metric\_description**  STRING |
| **metric\_id**  STRING |
| **new\_segments\_count**  NUMBER |
| **num\_active\_segments\_full**  NUMBER |
| **num\_archived\_segments**  NUMBER |
| **num\_archived\_segments\_with\_reply**  NUMBER |
| **num\_closed\_segments**  NUMBER |
| **num\_csat\_survey\_response**  NUMBER |
| **num\_messages\_received**  NUMBER |
| **num\_messages\_sent**  NUMBER |
| **num\_open\_segments\_end**  NUMBER |
| **num\_open\_segments\_start**  NUMBER |
| **num\_sla\_breach**  NUMBER |
| **num\_workload\_segments**  NUMBER |
| **pct\_csat\_survey\_satisfaction**  NUMBER |
| **pct\_tagged\_conversations**  NUMBER |
| **report\_id**  STRING |

### teammates\_table

The `teammates_table` table contains data about teammates in your Front account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | report\_id |
| **Replication Keys** | analytics\_date  analytics\_range |
| **Useful links** | [Front documentation](https://dev.frontapp.com/reference/analytics) |

teammates\_table table schema

|  |
| --- |
| **analytics\_date**  STRING |
| **analytics\_range**  STRING |
| **avg\_first\_response\_time**  NUMBER |
| **avg\_handle\_time**  NUMBER |
| **avg\_response\_time**  NUMBER |
| **avg\_sla\_breach\_time**  NUMBER |
| **avg\_total\_reply\_time**  NUMBER |
| **metric\_description**  STRING |
| **metric\_id**  STRING |
| **new\_segments\_count**  NUMBER |
| **num\_active\_segments\_full**  NUMBER |
| **num\_archived\_segments**  NUMBER |
| **num\_archived\_segments\_with\_reply**  NUMBER |
| **num\_closed\_segments**  NUMBER |
| **num\_csat\_survey\_response**  NUMBER |
| **num\_messages\_received**  NUMBER |
| **num\_messages\_sent**  NUMBER |
| **num\_open\_segments\_end**  NUMBER |
| **num\_open\_segments\_start**  NUMBER |
| **num\_sla\_breach**  NUMBER |
| **num\_workload\_segments**  NUMBER |
| **pct\_csat\_survey\_satisfaction**  NUMBER |
| **pct\_tagged\_conversations**  NUMBER |
| **report\_id**  STRING |

### teams\_table

The `teams_table` table contains data about teams in your Front account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | report\_id |
| **Replication Keys** | analytics\_date  analytics\_range |
| **Useful links** | [Front documentation](https://dev.frontapp.com/reference/analytics) |

teams\_table table schema

|  |
| --- |
| **analytics\_date**  STRING |
| **analytics\_range**  STRING |
| **avg\_first\_response\_time**  NUMBER |
| **avg\_handle\_time**  NUMBER |
| **avg\_response\_time**  NUMBER |
| **avg\_sla\_breach\_time**  NUMBER |
| **avg\_total\_reply\_time**  NUMBER |
| **metric\_description**  STRING |
| **metric\_id**  STRING |
| **new\_segments\_count**  NUMBER |
| **num\_active\_segments\_full**  NUMBER |
| **num\_archived\_segments**  NUMBER |
| **num\_archived\_segments\_with\_reply**  NUMBER |
| **num\_closed\_segments**  NUMBER |
| **num\_csat\_survey\_response**  NUMBER |
| **num\_messages\_received**  NUMBER |
| **num\_messages\_sent**  NUMBER |
| **num\_open\_segments\_end**  NUMBER |
| **num\_open\_segments\_start**  NUMBER |
| **num\_sla\_breach**  NUMBER |
| **num\_workload\_segments**  NUMBER |
| **pct\_csat\_survey\_satisfaction**  NUMBER |
| **pct\_tagged\_conversations**  NUMBER |
| **report\_id**  STRING |
