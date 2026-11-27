---
title: "Taboola"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Taboola-v2.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Taboola

Taboola is a public advertising solution.

Taboola integration replicates data using the [Taboola Backstage API](https://github.com/taboola/Backstage-API).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

The client ID and client secret must be obtained from your Taboola account manager.

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
| Username | Username. |
| Password | Password. |
| Account ID | Account ID. |
| Client ID | Client ID. |
| Client Secret | Client secret. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### campaign

The `campaign` table contains info about the campaigns in your Taboola account.

#### Replication

During every replication job, all campaigns in your Taboola account will be extracted, or “fully replicated.” If you look in the Extraction Logs in the Stitch app, you’ll see lines like this:

```
2017-10-25 13:46:52,254Z tap - INFO Synced 100 campaigns.
2017-10-25 13:46:52,255Z tap - INFO Done syncing campaigns.
```

Roughly the same amount of campaigns should be extracted during every job, unless brand new campaigns are added between jobs.

When Stitch loads the extracted records into your destination, however, only new and updated campaigns will be loaded. **This means that only new and updated campaign records will count towards your row count**.

#### Deleted campaigns

If a campaign is deleted at the source, the record for that campaign will remain in the destination.

#### NULL dates

On occasion, Taboola’s API will push `NULL` for `start_date` and `999-12-31` for `end_date`. It will convert `NULL` dates to `999-12-31` for consistency.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Taboola API method](https://github.com/taboola/Backstage-API/blob/master/Backstage%20API%20-%20Campaigns.pdf "Opens in new tab: Taboola API method") |

campaign table foreign keys

| Join campaign with | on |
| --- | --- |
| [campaign\_performance](#campaign-performance) | ``` campaign.id = campaign_performance.campaign_id ``` |

campaign table schema

|  |
| --- |
| **advertiser\_id**  STRING |
| **approval\_state**  STRING |
| **country\_targeting**  OBJECT This is a nested data structure:   - type: STRING - value: ARRAY, which is also a nested data structure.   - type: STRING |
| **cpc**  NUMBER |
| **daily\_cap**  NUMBER |
| **end\_date**  DATE |
| **id**  INTEGER |
| **is\_active**  BOOLEAN |
| **name**  STRING |
| **platform\_targeting**  OBJECT This is a nested data structure:   - type: STRING - value: ARRAY, which is also a nested data structure.   - type: STRING |
| **publisher\_targeting**  OBJECT This is a nested data structure:   - type: STRING - value: ARRAY, which is also a nested data structure.   - type: STRING |
| **spending\_limit**  NUMBER |
| **spending\_limit\_model**  STRING |
| **spent**  NUMBER |
| **start\_date**  DATE |
| **status**  STRING |
| **tracking\_code**  STRING |

### campaign\_performance

The `campaign_performance` table contains performance data for the campaigns in your Taboola account, broken down by day.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | campaign\_id  date |
| **Replication Key** | date |
| **Useful links** | [Taboola documentation](https://github.com/taboola/Backstage-API/blob/master/Backstage%20API%20-%20Reports.pdf) |

campaign\_performance table foreign keys

| Join campaign\_performance with | on |
| --- | --- |
| [campaign](#campaign) | ``` campaign_performance.campaign_id = campaign.id ``` |

campaign\_performance table schema

|  |
| --- |
| **campaign\_id**  INTEGER |
| **clicks**  INTEGER |
| **cpa**  NUMBER |
| **cpa\_actions\_num**  INTEGER |
| **cpa\_conversion\_rate**  NUMBER |
| **cpc**  NUMBER |
| **cpm**  NUMBER |
| **ctr**  NUMBER |
| **currency**  STRING |
| **date**  DATE |
| **impressions**  INTEGER |
| **spent**  NUMBER |
