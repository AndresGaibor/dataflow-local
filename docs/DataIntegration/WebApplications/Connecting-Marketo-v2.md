---
title: "Marketo"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Marketo-v2.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Marketo

Marketo is a marketing automation platform. You can use Marketo as a data source when landing or replicating data.

Marketo integration replicates data using the [Marketo REST API](https://experienceleague.adobe.com/en/docs/marketo-developer/marketo/home) and [Marketo Bulk API](https://experienceleague.adobe.com/en/docs/marketo-developer/marketo/home).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

You need administrator permissions in your Marketo account.

To create an API-only user role:

1. Log into your [Marketo](https://login.marketo.com/) account.
2. Navigate to Admin > Users & Roles.
3. Click the Roles tab and then New Role.
4. In the Create New Role window, complete the following fields:
   - Role name: Enter a name for the role. If the role is specific to Qlik Talend Cloud, make that clear in the name, for example QTC API role.
   - Description: Enter a description of the role.
   - Permissions: Select the Access API checkbox.
5. Click Create.

To create an API-only user:

1. Log into your [Marketo](https://login.marketo.com/) account.
2. Navigate to Admin > Users & Roles.
3. Click the Users tab and then Invite New User.
4. In the Invite New User window, complete the following fields:
   - Email
   - First Name
   - Last Name
5. Click Next.
6. In the Permissions section, select the checkboxes for the API user role you created and API Only.
7. Click Next.
8. In the Message section, click Send to create the user.

To create an API Custom Service:

1. Log into your [Marketo](https://login.marketo.com/) account.
2. Navigate to Admin > LaunchPoint.
3. Click the New tab and then New Service.
4. In the New Service window, complete the following fields:
   - Display Name: Enter QTC .
   - Service: Select Custom from the drop-down list.
   - Description: Enter a description.
   - API Only User: Select the user you previously created.
5. Click Create.
6. In the Installed Services section, click View Details.
7. Copy and paste your client ID and client secret into a secured file.

IP restrictions may be enabled in Marketo. To verify, go to Admin > Web Services > IP Restrictions. If IP restrictions are not enabled, skip this step.

The IP addresses you must allowlist depend on your Qlik Talend Cloud region and country. For the current list, see [Qlik Cloud domains and IP addresses](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/qlik-cloud-dns-ip.htm).

To add the Qlik Talend Cloud IP addresses to Marketo’s web services allowlist:

1. Log into your [Marketo](https://login.marketo.com/) account.
2. In the Integration menu, click Web Services.
3. In the IP Restrictions section, click Edit.
4. In Allowed Addresses, paste one IP address for your region.
5. Repeat the previous step until you have added all required IP addresses for your data pipeline region.
6. Click Save.

To retrieve the base URLs:

1. Log into your [Marketo](https://login.marketo.com/) account.
2. Navigate to Web Services > REST API.
3. Locate the Endpoint and Identity fields.
4. Copy the URLs.

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
| Endpoint Base URL | Endpoint base URL, for example: https://457-RFG-234.mktorest.com/rest. |
| Client ID | Client ID. |
| Client Secret | Client secret. |
| Max Daily API Calls | Most Marketo subscriptions are allocated 50000 API calls per day. |

Information note

Marketo Bulk Extract has a 500 MB per day quota per Marketo instance, shared across bulk extract objects. The quota resets at midnight CT.

If your first historical replication includes more than one year of data, the initial load can fail when the daily quota is reached.

For large first loads, schedule the task to run once every 24 hours until the initial full load is complete.

If required, contact Marketo (Adobe) to request a higher Bulk Extract quota.

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### activities

You can choose to replicate lead activity data for specific activity types. For every activity type defined in your Marketo account, you’ll see an `activities` table in the **Tables to Replicate** tab. For example: `activities_click_email` contains lead activity data for the `click_email` activity type.

These tables will contain the fields listed below, along with any fields specific to that activity type.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | marketoGuid |
| **Replication Key** | activityDate |
| **Useful links** | [Marketo API method](http://developers.marketo.com/rest-api/endpoint-reference/lead-database-endpoint-reference/#!/Activities/getLeadActivitiesUsingGET "Opens in new tab: Marketo API method") |

activities table foreign keys

| Join activities with | on |
| --- | --- |
| [activity\_types](#activity-types) | ``` activities.activityTypeId = activity_types.id ``` |
| [leads](#leads) | ``` activities.leadId = leads.id ``` |

activities table schema

|  |
| --- |
| **activityDate**  DATE-TIME |
| **activityTypeId**  INTEGER |
| **campaignId**  INTEGER |
| **leadId**  INTEGER |
| **marketoGuid**  STRING |
| **primary\_attribute\_name**  STRING |
| **primary\_attribute\_value**  STRING |
| **primary\_attribute\_value\_id**  INTEGER |

### activity\_types

The `activity_types` table contains metadata about the activity types - form fill, web page visit, lead creation, and so on - available in Marketo.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Replication Key** | activityDate |
| **Useful links** | [Marketo API method](http://developers.marketo.com/rest-api/endpoint-reference/lead-database-endpoint-reference/#!/Activities/getAllActivityTypesUsingGET "Opens in new tab: Marketo API method") |

activity\_types table foreign keys

| Join activity\_types with | on |
| --- | --- |
| [activities](#activities) | ``` activity_types.id = activities.activityTypeId ``` |

activity\_types table schema

|  |
| --- |
| **attributes**  ARRAY This is a nested data structure:   - dataType: STRING - name: STRING |
| **description**  STRING |
| **id**  INTEGER |
| **name**  STRING |
| **primaryAttribute**  OBJECT This is a nested data structure:   - dataType: STRING - name: STRING |

### campaigns

The `campaigns` table contains info about your Marketo campaigns

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [Marketo documentation](http://developers.marketo.com/rest-api/endpoint-reference/lead-database-endpoint-reference/#!/Campaigns/getCampaignsUsingGET) |

campaigns table foreign keys

| Join campaigns with | on |
| --- | --- |
| [programs](#programs) | ``` campaigns.programId = programs.id ``` |

campaigns table schema

|  |
| --- |
| **active**  BOOLEAN |
| **createdAt**  DATE-TIME |
| **description**  STRING |
| **id**  INTEGER |
| **name**  STRING |
| **programId**  INTEGER |
| **programName**  STRING |
| **type**  STRING |
| **updatedAt**  DATE-TIME |
| **workspaceName**  STRING |

### leads

The `leads` table contains info about your Marketo leads.

The Replication Key for this table varies depending on your Marketo account setup:

- **If updatedAt filtering is enabled**, this table will use `updatedAt` as the Replication Key
- **If updatedAt filtering isn’t enabled,** this table will use `createdAt` as the Replication Key. Additionally, data will be loaded using Append-Only loading.

[Read more about replicating this table](#leads-replication).

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Marketo API method](http://developers.marketo.com/rest-api/endpoint-reference/lead-database-endpoint-reference/#!/Leads/getLeadsByFilterUsingGET "Opens in new tab: Marketo API method") |

leads table foreign keys

| Join leads with | on |
| --- | --- |
| [activities](#activities) | ``` leads.id = activities.leadId ``` |

leads table schema

|  |
| --- |
| **acquiredBy**  BOOLEAN |
| **id**  INTEGER |
| **isExhausted**  BOOLEAN |
| **membershipDate**  DATE |
| **nurtureCadence**  STRING |
| **progressionStatus**  STRING |
| **reachedSuccess**  BOOLEAN |
| **reachedSuccessDate**  STRING |
| **stream**  STRING |

### lists

The `lists` table contains info about the static lists in your Marketo account.

**Note**: Due to some of the limitations in Marketo API, only static lists will be replicated.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [Marketo API method](http://developers.marketo.com/rest-api/endpoint-reference/lead-database-endpoint-reference/#!/Static_Lists/getListsUsingGET "Opens in new tab: Marketo API method") |

lists table schema

|  |
| --- |
| **createdAt**  DATE-TIME |
| **description**  STRING |
| **id**  INTEGER |
| **name**  STRING |
| **programName**  STRING |
| **updatedAt**  DATE-TIME |
| **workspaceName**  STRING |

### programs

The `programs` table contains info about your Marketo programs. Programs can be parents to most types of assets in Marketo and allow you to track membership and success of leads.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [Marketo API method](https://developers.marketo.com/rest-api/endpoint-reference/asset-endpoint-reference/#!/Programs/browseProgramsUsingGET "Opens in new tab: Marketo API method") |

programs table foreign keys

| Join programs with | on |
| --- | --- |
| [campaigns](#campaigns) | ``` programs.id = campaigns.programId ``` |

programs table schema

|  |
| --- |
| **channel**  STRING |
| **createdAt**  DATE-TIME |
| **description**  STRING |
| **folder**  OBJECT This is a nested data structure:   - folderName: STRING - type: STRING - value: INTEGER |
| **id**  INTEGER |
| **name**  STRING |
| **status**  STRING |
| **type**  STRING |
| **updatedAt**  DATE-TIME |
| **url**  STRING |
| **workspace**  STRING |
