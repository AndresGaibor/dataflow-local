---
title: "Drip"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Drip.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Drip

Drip is an email marketing automation platform designed for e-commerce businesses.

Drip integration replicates data using the [Drip REST API](https://developer.drip.com/#introduction).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To retrieve your API token:

1. Log into your [Drip](https://auth.getdrip.com/u/login/identifier?state=hKFo2SBIVmsxNmFhak5sN0dRekJreUYxWmIzek5MTktlZlIwcKFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIHJlZG84QXhGeFNqdWpzN25yYy1qY1FFUklzQThjUksxo2NpZNkgSm5Edllxc0tlOUd2d2J6VzJDSjZtME1XVTZBaUtCeEk) account.
2. Navigate to Settings > User Settings > User Info.
3. Copy and paste your API token into a secured file.

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

## Schema

Depending on your destination, table and column names may not appear as they are outlined below.

### accounts

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Drip documentation](https://developer.drip.com/?shell#list-all-accounts) |

### conversions

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id  account\_id |
| **Useful links** | [Drip documentation](https://developer.drip.com/?shell#list-all-conversions) |

### custom\_field\_identifiers

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | custom\_field\_id  account\_id |
| **Useful links** | [Drip documentation](https://developer.drip.com/?shell#list-all-custom-field-identifiers-used-in-an-account) |

### email\_series\_campaigns

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id  account\_id |
| **Useful links** | [Drip documentation](https://developer.drip.com/?shell#list-all-email-series-campaigns) |

### email\_series\_subscriber\_active

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id  account\_id  campaign\_id |
| **Useful links** | [Drip documentation](https://developer.drip.com/?shell#list-all-subscribers-subscribed-to-an-email-series-campaign) |

### email\_series\_subscriber\_removed

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id  account\_id  campaign\_id |
| **Useful links** | [Drip documentation](https://developer.drip.com/?shell#list-all-subscribers-subscribed-to-an-email-series-campaign) |

### email\_series\_subscriber\_unsubscribed

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id  account\_id  campaign\_id |
| **Useful links** | [Drip documentation](https://developer.drip.com/?shell#list-all-subscribers-subscribed-to-an-email-series-campaign) |

### event\_actions

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | event\_action  account\_id |
| **Useful links** | [Drip documentation](https://developer.drip.com/?shell#list-all-custom-events-actions-used-in-an-account) |

### forms

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id  account\_id |
| **Useful links** | [Drip documentation](https://developer.drip.com/?shell#list-all-forms) |

### people

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id  account\_id |
| **Useful links** | [Drip documentation](https://developer.drip.com/?shell#list-all-subscribers) |

### single\_email\_campaigns

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id  account\_id |
| **Useful links** | [Drip documentation](https://developer.drip.com/?shell#list-all-single-email-campaigns) |

### tags

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | tag\_id  account\_id |
| **Useful links** | [Drip documentation](https://developer.drip.com/?shell#list-all-tags-used-in-an-account) |

### users

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | email |
| **Useful links** | [Drip documentation](https://developer.drip.com/?shell#users) |

### workflows

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id  account\_id |
| **Useful links** | [Drip documentation](https://developer.drip.com/?shell#list-all-workflows) |

### workflow\_triggers

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id  account\_id  workflow\_id |
| **Useful links** | [Drip documentation](https://developer.drip.com/?shell#list-all-workflow-triggers) |
