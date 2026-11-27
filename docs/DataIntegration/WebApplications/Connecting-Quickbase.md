---
title: "Quickbase"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Quickbase.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Quickbase

Quickbase is a no-code application development platform for dynamic work management.

Quickbase integration replicates data using the [QuickBase REST API](https://developer.quickbase.com/).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

You need administrator permissions in your Quickbase account.

To create a user token:

1. Log into your [Quickbase](https://login.quickbase.com/db/main?a=SignIn) account.
2. In the upper-right corner, select your user name, and then select Manage User Tokens.
3. Click New user token.
4. Enter the token details: a Name and a Description.
5. In the Assign token to apps section, use the drop-down lists to select the apps to which the token will be assigned.
6. Click Save.

   The new token appears in the list of user tokens.

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
| Quick Base Application ID | You can find the application ID of your Quickbase site in the URL of your account homepage. If the URL is https://yourcompany.quickbase.com/db/bq7z6x7xx, the application ID is bq7z6x7xx. |
| Quick Base API URL | API URL. |
| Quick Base User Token | User token. |
| Page Size | Optional. The default value is set to 100. |

## Schema

Depending on your destination, table and column names may not appear as they are outlined below.

### apps

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Quickbase documentation](https://developer.quickbase.com/operation/getApp) |

### events

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Quickbase documentation](https://developer.quickbase.com/operation/getAppEvents) |

### roles

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Quickbase documentation](https://developer.quickbase.com/operation/getRoles) |

### app\_tables

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Quickbase documentation](https://developer.quickbase.com/operation/getAppTables) |

### tables

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Quickbase documentation](https://developer.quickbase.com/operation/getTable) |

### table\_relationships

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id  tableId |
| **Useful links** | [Quickbase documentation](https://developer.quickbase.com/operation/getRelationships) |

### table\_reports

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Quickbase documentation](https://developer.quickbase.com/operation/getTableReports) |

### reports

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Quickbase documentation](https://developer.quickbase.com/operation/getReport) |

### fields

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id  tableId |
| **Useful links** | [Quickbase documentation](https://developer.quickbase.com/operation/getFields) |

### fields\_usage

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id  tableId |
| **Useful links** | [Quickbase documentation](https://developer.quickbase.com/operation/getFieldsUsage) |
