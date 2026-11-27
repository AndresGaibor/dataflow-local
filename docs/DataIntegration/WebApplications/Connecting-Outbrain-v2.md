---
title: "Outbrain"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Outbrain-v2.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Outbrain

Outbrain is an advertising platform.

Outbrain integration replicates data using the [Outbrain Amplify API](http://developer.outbrain.com/home-page/amplify-api/).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

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
| Account ID | You can find your account ID in the URL of your Outbrain account, at the Overview dashboard, located between marketers and campaigns. If the URL is https://my.outbrain.com/amplify/site/marketers/your-account-id/campaigns/overview, the subdomain is your-account-id. |
| Username | Username. |
| Password | Password. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### campaign\_performance

The `campaign_performance` table contains performance metrics for your Outbrain campaigns.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | campaignId  fromDate |
| **Replication Key** | fromDate |
| **Useful links** | [Outbrain documentation](http://docs.amplifyv01.apiary.io/#reference/performance-reporting/campaigns)  [Outbrain API method](http://docs.amplifyv01.apiary.io/#reference/performance-reporting/campaigns/retrieve-campaigns-with-performance-statistics-for-a-marketer "Opens in new tab: Outbrain API method") |

campaign\_performance table schema

|  |
| --- |
| **campaignId**  STRING |
| **clicks**  NUMBER |
| **conversionRate**  NUMBER |
| **conversions**  NUMBER |
| **cpa**  NUMBER |
| **ctr**  NUMBER |
| **ecpc**  NUMBER |
| **fromDate**  DATE |
| **impressions**  NUMBER |
| **spend**  NUMBER |

### campaigns

The `campaigns` table contains info about your Outbrain campaigns.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Outbrain documentation](http://docs.amplifyv01.apiary.io/#reference/campaigns)  [Outbrain API method](http://docs.amplifyv01.apiary.io/#reference/campaigns/campaigns-collection-via-marketer/list-all-campaigns-associated-with-a-marketer "Opens in new tab: Outbrain API method") |

campaigns table schema

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **budget**  OBJECT This is a nested data structure:   - amount: NUMBER - amountRemaining: NUMBER - amountSpent: NUMBER - creationTime: DATE-TIME - currency: STRING - dailyTarget: NUMBER - endDate: DATE - id: STRING - lastModified: DATE-TIME - maximumAmount: NUMBER - name: STRING - pacing: STRING - runForever: BOOLEAN - shared: BOOLEAN - startDate: DATE - type: STRING  Click to expand budget |  | | --- | | **amount**  NUMBER | | **amountRemaining**  NUMBER | | **amountSpent**  NUMBER | | **creationTime**  DATE-TIME | | **currency**  STRING | | **dailyTarget**  NUMBER | | **endDate**  DATE | | **id**  STRING | | **lastModified**  DATE-TIME | | **maximumAmount**  NUMBER | | **name**  STRING | | **pacing**  STRING | | **runForever**  BOOLEAN | | **shared**  BOOLEAN | | **startDate**  DATE | | **type**  STRING | |
| **campaignOnAir**  BOOLEAN |
| **cpc**  NUMBER |
| **enabled**  BOOLEAN |
| **id**  STRING |
| **name**  STRING |
| **onAirReason**  STRING |
