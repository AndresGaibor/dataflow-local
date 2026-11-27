---
title: "AppsFlyer"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Appsflyer.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# AppsFlyer

AppsFlyer is a SaaS mobile marketing analytics and attribution platform.

AppsFlyer integration replicates data using the [AppsFlyer Raw Data Reports V5 API](https://support.appsflyer.com/hc/en-us/articles/360007530258-Using-Pull-API-raw-data).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To retrieve your app ID:

1. Log into your AppsFlyer account.
2. In the Pending Apps section, locate and copy your app ID depending on the app's type:
   - iOS: This is the iTunes ID of your app. Example: id987654321.
   - Android: This is the package name registered on AppsFlyer. For example: If the package is registered as com.yourcompany.test, the ID is com.yourcompany.test.
   - Windows: This is the Windows app ID. For example: f1e2d3c4b5a6.

To retrieve your API key:

You must be the Account Owner in AppsFlyer to complete this step.

1. In the list of apps, click the app you want to replicate data from. This opens the app’s dashboard page.
2. Under the Integration section, click API Access.
3. Copy the key from the Your API Key field.

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
| App ID | App ID. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### in\_app\_events

The `in_app_events` table contains information about in-app events for iOS and Android apps.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | appsflyer\_id  event\_name  event\_time |
| **Replication Key** | event\_time |
| **Useful links** | [AppsFlyer documentation](https://support.appsflyer.com/hc/en-us/articles/208387843-Raw-Data-Reports-V5-)  [AppsFlyer API method](https://dev.appsflyer.com/hc/reference/get_app-id-in-app-events-report-v5 "Opens in new tab: AppsFlyer API method") |

in\_app\_events table schema

|  |
| --- |
| **advertising\_id**  STRING |
| **af\_ad**  STRING |
| **af\_ad\_id**  STRING |
| **af\_ad\_type**  STRING |
| **af\_adset**  STRING |
| **af\_adset\_id**  STRING |
| **af\_attribution\_lookback**  STRING |
| **af\_c\_id**  STRING |
| **af\_channel**  STRING |
| **af\_cost\_currency**  STRING |
| **af\_cost\_model**  STRING |
| **af\_cost\_value**  STRING |
| **af\_keywords**  STRING |
| **af\_prt**  STRING |
| **af\_reengagement\_window**  STRING |
| **af\_siteid**  STRING |
| **af\_sub1**  STRING |
| **af\_sub2**  STRING |
| **af\_sub3**  STRING |
| **af\_sub4**  STRING |
| **af\_sub5**  STRING |
| **af\_sub\_siteid**  STRING |
| **android\_id**  STRING |
| **app\_id**  STRING |
| **app\_name**  STRING |
| **app\_version**  STRING |
| **appsflyer\_id**  STRING |
| **attributed\_touch\_time**  DATE-TIME |
| **attributed\_touch\_type**  STRING |
| **bundle\_id**  STRING |
| **campaign**  STRING |
| **carrier**  STRING |
| **city**  STRING |
| **contributor1\_af\_prt**  STRING |
| **contributor1\_campaign**  STRING |
| **contributor1\_media\_source**  STRING |
| **contributor1\_touch\_time**  STRING |
| **contributor1\_touch\_type**  STRING |
| **contributor2\_af\_prt**  STRING |
| **contributor2\_campaign**  STRING |
| **contributor2\_media\_source**  STRING |
| **contributor2\_touch\_time**  STRING |
| **contributor2\_touch\_type**  STRING |
| **contributor3\_af\_prt**  STRING |
| **contributor3\_campaign**  STRING |
| **contributor3\_media\_source**  STRING |
| **contributor3\_touch\_time**  STRING |
| **contributor3\_touch\_type**  STRING |
| **country\_code**  STRING |
| **customer\_user\_id**  INTEGER, STRING |
| **device\_type**  STRING |
| **dma**  STRING |
| **event\_name**  STRING |
| **event\_revenue**  STRING |
| **event\_revenue\_currency**  STRING |
| **event\_revenue\_usd**  STRING |
| **event\_source**  STRING |
| **event\_time**  DATE-TIME |
| **event\_value**  STRING |
| **http\_referrer**  STRING |
| **idfa**  STRING |
| **idfv**  STRING |
| **imei**  STRING |
| **install\_time**  DATE-TIME |
| **ip**  STRING |
| **is\_primary\_attribution**  BOOLEAN |
| **is\_receipt\_validated**  BOOLEAN |
| **is\_retargeting**  BOOLEAN |
| **language**  STRING |
| **media\_source**  STRING |
| **operator**  STRING |
| **original\_url**  STRING |
| **os\_version**  STRING |
| **platform**  STRING |
| **postal\_code**  STRING |
| **region**  STRING |
| **retargeting\_conversion\_type**  STRING |
| **sdk\_version**  STRING |
| **state**  STRING |
| **user\_agent**  STRING |
| **wifi**  BOOLEAN |

### installations

The `installations` table contains information about iOS and Android app installations.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | appsflyer\_id  event\_name  event\_time |
| **Replication Key** | event\_time |
| **Useful links** | [AppsFlyer documentation](https://support.appsflyer.com/hc/en-us/articles/208387843-Raw-Data-Reports-V5-)  [AppsFlyer API method](https://dev.appsflyer.com/hc/reference/get_app-id-installs-report-v5 "Opens in new tab: AppsFlyer API method") |

installations table schema

|  |
| --- |
| **advertising\_id**  STRING |
| **af\_ad**  STRING |
| **af\_ad\_id**  STRING |
| **af\_ad\_type**  STRING |
| **af\_adset**  STRING |
| **af\_adset\_id**  STRING |
| **af\_attribution\_lookback**  STRING |
| **af\_c\_id**  STRING |
| **af\_channel**  STRING |
| **af\_cost\_currency**  STRING |
| **af\_cost\_model**  STRING |
| **af\_cost\_value**  STRING |
| **af\_keywords**  STRING |
| **af\_prt**  STRING |
| **af\_reengagement\_window**  STRING |
| **af\_siteid**  STRING |
| **af\_sub1**  STRING |
| **af\_sub2**  STRING |
| **af\_sub3**  STRING |
| **af\_sub4**  STRING |
| **af\_sub5**  STRING |
| **af\_sub\_siteid**  STRING |
| **android\_id**  STRING |
| **app\_id**  STRING |
| **app\_name**  STRING |
| **app\_version**  STRING |
| **appsflyer\_id**  STRING |
| **attributed\_touch\_time**  DATE-TIME |
| **attributed\_touch\_type**  STRING |
| **bundle\_id**  STRING |
| **campaign**  STRING |
| **carrier**  STRING |
| **city**  STRING |
| **contributor1\_af\_prt**  STRING |
| **contributor1\_campaign**  STRING |
| **contributor1\_media\_source**  STRING |
| **contributor1\_touch\_time**  STRING |
| **contributor1\_touch\_type**  STRING |
| **contributor2\_af\_prt**  STRING |
| **contributor2\_campaign**  STRING |
| **contributor2\_media\_source**  STRING |
| **contributor2\_touch\_time**  STRING |
| **contributor2\_touch\_type**  STRING |
| **contributor3\_af\_prt**  STRING |
| **contributor3\_campaign**  STRING |
| **contributor3\_media\_source**  STRING |
| **contributor3\_touch\_time**  STRING |
| **contributor3\_touch\_type**  STRING |
| **country\_code**  STRING |
| **customer\_user\_id**  INTEGER, STRING |
| **device\_type**  STRING |
| **dma**  STRING |
| **event\_name**  STRING |
| **event\_revenue**  STRING |
| **event\_revenue\_currency**  STRING |
| **event\_revenue\_usd**  STRING |
| **event\_source**  STRING |
| **event\_time**  DATE-TIME |
| **event\_value**  STRING |
| **http\_referrer**  STRING |
| **idfa**  STRING |
| **idfv**  STRING |
| **imei**  STRING |
| **install\_time**  DATE-TIME |
| **ip**  STRING |
| **is\_primary\_attribution**  BOOLEAN |
| **is\_receipt\_validated**  BOOLEAN |
| **is\_retargeting**  BOOLEAN |
| **language**  STRING |
| **media\_source**  STRING |
| **operator**  STRING |
| **original\_url**  STRING |
| **os\_version**  STRING |
| **platform**  STRING |
| **postal\_code**  STRING |
| **region**  STRING |
| **retargeting\_conversion\_type**  STRING |
| **sdk\_version**  STRING |
| **state**  STRING |
| **user\_agent**  STRING |
| **wifi**  BOOLEAN |

### organic\_installs

The `organic_installs` table contains information about organic installs.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | appsflyer\_id  event\_name  event\_time |
| **Replication Key** | event\_time |
| **Useful links** | [AppsFlyer documentation](https://support.appsflyer.com/hc/en-us/articles/208387843-Raw-Data-Reports-V5-)  [AppsFlyer API method](https://dev.appsflyer.com/hc/reference/get_app-id-organic-installs-report-v5 "Opens in new tab: AppsFlyer API method") |

organic\_installs table schema

|  |
| --- |
| **advertising\_id**  STRING |
| **af\_ad**  STRING |
| **af\_ad\_id**  STRING |
| **af\_ad\_type**  STRING |
| **af\_adset**  STRING |
| **af\_adset\_id**  STRING |
| **af\_attribution\_lookback**  STRING |
| **af\_c\_id**  STRING |
| **af\_channel**  STRING |
| **af\_cost\_currency**  STRING |
| **af\_cost\_model**  STRING |
| **af\_cost\_value**  STRING |
| **af\_keywords**  STRING |
| **af\_prt**  STRING |
| **af\_reengagement\_window**  STRING |
| **af\_siteid**  STRING |
| **af\_sub1**  STRING |
| **af\_sub2**  STRING |
| **af\_sub3**  STRING |
| **af\_sub4**  STRING |
| **af\_sub5**  STRING |
| **af\_sub\_siteid**  STRING |
| **android\_id**  STRING |
| **app\_id**  STRING |
| **app\_name**  STRING |
| **app\_version**  STRING |
| **appsflyer\_id**  STRING |
| **attributed\_touch\_time**  DATE-TIME |
| **attributed\_touch\_type**  STRING |
| **bundle\_id**  STRING |
| **campaign**  STRING |
| **carrier**  STRING |
| **city**  STRING |
| **contributor1\_af\_prt**  STRING |
| **contributor1\_campaign**  STRING |
| **contributor1\_media\_source**  STRING |
| **contributor1\_touch\_time**  STRING |
| **contributor1\_touch\_type**  STRING |
| **contributor2\_af\_prt**  STRING |
| **contributor2\_campaign**  STRING |
| **contributor2\_media\_source**  STRING |
| **contributor2\_touch\_time**  STRING |
| **contributor2\_touch\_type**  STRING |
| **contributor3\_af\_prt**  STRING |
| **contributor3\_campaign**  STRING |
| **contributor3\_media\_source**  STRING |
| **contributor3\_touch\_time**  STRING |
| **contributor3\_touch\_type**  STRING |
| **country\_code**  STRING |
| **customer\_user\_id**  INTEGER, STRING |
| **device\_type**  STRING |
| **dma**  STRING |
| **event\_name**  STRING |
| **event\_revenue**  STRING |
| **event\_revenue\_currency**  STRING |
| **event\_revenue\_usd**  STRING |
| **event\_source**  STRING |
| **event\_time**  DATE-TIME |
| **event\_value**  STRING |
| **http\_referrer**  STRING |
| **idfa**  STRING |
| **idfv**  STRING |
| **imei**  STRING |
| **install\_time**  DATE-TIME |
| **ip**  STRING |
| **is\_primary\_attribution**  BOOLEAN |
| **is\_receipt\_validated**  BOOLEAN |
| **is\_retargeting**  BOOLEAN |
| **language**  STRING |
| **media\_source**  STRING |
| **operator**  STRING |
| **original\_url**  STRING |
| **os\_version**  STRING |
| **platform**  STRING |
| **postal\_code**  STRING |
| **region**  STRING |
| **retargeting\_conversion\_type**  STRING |
| **sdk\_version**  STRING |
| **state**  STRING |
| **user\_agent**  STRING |
| **wifi**  BOOLEAN |
