---
title: "Zoho CRM"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Zoho-CRM-v2.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Zoho CRM

Zoho CRM is online CRM software, part of the Zoho online software suite. You can use Zoho CRM as a data source when landing or replicating data.

Zoho CRM integration replicates data using the [Zoho CRM API](https://www.zoho.com/crm/developer/docs/api/v8/get-records.html).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To retrieve your client secret and ID:

1. Log into your [Zoho CRM](https://api-console.zoho.com/) account.
2. Click Add Client.
3. Select Qlik Server Based App.
4. Enter your client name.
5. In the Homepage URL field, enter www.qlik.com.
6. Make sure Authorized Redirect URIs is set to https://connector.qlik.com/auth/oauth/v3.htm.
7. Click Create.
8. Navigate to Client Secret tab.
9. Copy and paste your client secret and client ID into a secured file.

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
| Select Fields by Default | Select this check box to include new Zoho CRM fields in replication datasets automatically. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### currencies

The `currencies` table contains info about the currencies in your Zoho CRM account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Zoho CRM documentation](https://www.zoho.com/crm/developer/docs/api/v8/get-currencies-data.html) |

### organization

The `organization` table contains info about the organization in your Zoho CRM account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Zoho CRM documentation](https://www.zoho.com/crm/developer/docs/api/v8/get-org-data.html) |

### profiles

The `profiles` table contains info about the profiles in your Zoho CRM account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Zoho CRM documentation](https://www.zoho.com/crm/developer/docs/api/v8/get-profiles.html) |

### roles

The `roles` table contains info about the roles in your Zoho CRM account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Zoho CRM documentation](https://www.zoho.com/crm/developer/docs/api/v8/get-roles.html) |

### territories

The `territories` table contains info about the territories in your Zoho CRM account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Zoho CRM documentation](https://www.zoho.com/crm/developer/docs/api/v8/territories.html) |

### users

The `users` table contains info about the users in your Zoho CRM account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Zoho CRM documentation](https://www.zoho.com/crm/developer/docs/api/v8/get-users.html) |
