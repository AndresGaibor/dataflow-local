---
title: "TikTok Ads"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-TikTok-Ads.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# TikTok Ads

TikTok Ads is used by brands and individual creators by paying to share sponsored content on TikTok’s platform to reach a bigger and/or more specific audience.

TikTok Ads integration replicates data using the [TikTok Ads API (v1.3)](https://ads.tiktok.com/marketing_api/docs).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To generate your App ID and Secret:

1. Log into your [TikTok for Developers](https://developers.tiktok.com/) account.
2. Click your profile icon in the navigation bar.
3. Click Manage apps and select the relevant application.
4. Copy the App ID and Secret that are generated, to use in the connection settings.

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
| Include data from deleted campaigns, ads, and adgroups | Select the checkbox if needed. |
| Accounts | Enter the account names separated by a comma. |
| App ID | ID of the app. |
| Secret | Secret of the app. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### ad\_insights

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | ad\_id  adgroup\_id  advertiser\_id  campaign\_id  stat\_time\_day |
| **Replication Key** | stat\_time\_day |
| **Useful links** | [TikTok Ads documentation](https://ads.tiktok.com/marketing_api/docs?id=1707957200780290) |

ad\_insights table schema

|  |
| --- |
| **ad\_id**  STRING |
| **ad\_name**  STRING |
| **ad\_text**  STRING |
| **adgroup\_id**  STRING |
| **adgroup\_name**  STRING |
| **advertiser\_id**  STRING |
| **app\_promotion\_type**  STRING |
| **average\_video\_play**  NUMBER |
| **average\_video\_play\_per\_user**  NUMBER |
| **bid**  STRING |
| **bid\_strategy**  STRING |
| **billing\_event**  STRING |
| **budget**  STRING |
| **call\_to\_action**  STRING |
| **campaign\_budget**  STRING |
| **campaign\_dedicate\_type**  STRING |
| **campaign\_id**  STRING |
| **campaign\_name**  STRING |
| **clicks**  INTEGER |
| **clicks\_on\_music\_disc**  INTEGER |
| **comments**  INTEGER |
| **conversion**  INTEGER |
| **conversion\_rate**  NUMBER |
| **conversion\_rate\_v2**  NUMBER |
| **cost\_per\_1000\_reached**  STRING |
| **cost\_per\_100\_reached**  NUMBER |
| **cost\_per\_conversion**  NUMBER |
| **cost\_per\_result**  NUMBER |
| **cost\_per\_secondary\_goal\_result**  NUMBER |
| **cpc**  NUMBER |
| **cpm**  NUMBER |
| **ctr**  NUMBER |
| **dpa\_target\_audience\_type**  STRING |
| **follows**  INTEGER |
| **frequency**  NUMBER |
| **gross\_impressions**  STRING |
| **image\_mode**  STRING |
| **impressions**  INTEGER |
| **is\_smart\_creative**  BOOLEAN |
| **likes**  INTEGER |
| **mobile\_app\_id**  STRING |
| **objective\_type**  STRING |
| **opt\_status**  STRING |
| **placement\_type**  STRING |
| **profile\_visits**  INTEGER |
| **profile\_visits\_rate**  NUMBER |
| **promotion\_type**  STRING |
| **reach**  INTEGER |
| **real\_time\_conversion**  INTEGER |
| **real\_time\_conversion\_rate**  NUMBER |
| **real\_time\_conversion\_rate\_v2**  NUMBER |
| **real\_time\_cost\_per\_conversion**  NUMBER |
| **real\_time\_cost\_per\_result**  NUMBER |
| **real\_time\_result**  INTEGER |
| **real\_time\_result\_rate**  NUMBER |
| **result**  INTEGER |
| **result\_rate**  NUMBER |
| **secondary\_goal\_result**  INTEGER |
| **secondary\_goal\_result\_rate**  NUMBER |
| **shares**  INTEGER |
| **smart\_target**  STRING |
| **spend**  NUMBER |
| **split\_test**  STRING |
| **stat\_time\_day**  DATE-TIME |
| **tt\_app\_id**  STRING |
| **tt\_app\_name**  STRING |
| **video\_play\_actions**  INTEGER |
| **video\_views\_p100**  INTEGER |
| **video\_views\_p25**  INTEGER |
| **video\_views\_p50**  INTEGER |
| **video\_views\_p75**  INTEGER |
| **video\_watched\_2s**  INTEGER |
| **video\_watched\_6s**  INTEGER |

### ad\_insights\_by\_age\_and\_gender

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | ad\_id  adgroup\_id  advertiser\_id  age  campaign\_id  gender  stat\_time\_day |
| **Replication Key** | stat\_time\_day |
| **Useful links** | [TikTok Ads documentation](https://ads.tiktok.com/marketing_api/docs?id=1707957217727489) |

ad\_insights\_by\_age\_and\_gender table schema

|  |
| --- |
| **ad\_id**  STRING |
| **ad\_name**  STRING |
| **ad\_text**  STRING |
| **adgroup\_id**  STRING |
| **adgroup\_name**  STRING |
| **advertiser\_id**  STRING |
| **age**  STRING |
| **bid**  STRING |
| **bid\_strategy**  STRING |
| **billing\_event**  STRING |
| **budget**  STRING |
| **call\_to\_action**  STRING |
| **campaign\_budget**  STRING |
| **campaign\_dedicate\_type**  STRING |
| **campaign\_id**  STRING |
| **campaign\_name**  STRING |
| **clicks**  INTEGER |
| **conversion**  INTEGER |
| **conversion\_rate**  NUMBER |
| **conversion\_rate\_v2**  NUMBER |
| **cost\_per\_conversion**  NUMBER |
| **cost\_per\_result**  NUMBER |
| **cpc**  NUMBER |
| **cpm**  NUMBER |
| **ctr**  NUMBER |
| **dpa\_target\_audience\_type**  STRING |
| **gender**  STRING |
| **gross\_impressions**  STRING |
| **impressions**  INTEGER |
| **is\_smart\_creative**  BOOLEAN |
| **mobile\_app\_id**  STRING |
| **objective\_type**  STRING |
| **opt\_status**  STRING |
| **promotion\_type**  STRING |
| **real\_time\_conversion**  INTEGER |
| **real\_time\_conversion\_rate**  NUMBER |
| **real\_time\_conversion\_rate\_v2**  NUMBER |
| **real\_time\_cost\_per\_conversion**  NUMBER |
| **real\_time\_cost\_per\_result**  NUMBER |
| **real\_time\_result**  INTEGER |
| **real\_time\_result\_rate**  NUMBER |
| **result**  INTEGER |
| **result\_rate**  NUMBER |
| **rf\_campaign\_type**  STRING |
| **smart\_target**  STRING |
| **spend**  NUMBER |
| **split\_test**  STRING |
| **stat\_time\_day**  DATE-TIME |
| **tt\_app\_id**  STRING |
| **tt\_app\_name**  STRING |
| **user\_action**  STRING |

### ad\_insights\_by\_country

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | ad\_id  adgroup\_id  advertiser\_id  campaign\_id  country\_code  stat\_time\_day |
| **Replication Key** | stat\_time\_day |
| **Useful links** | [TikTok Ads documentation](https://ads.tiktok.com/marketing_api/docs?id=1707957217727489) |

ad\_insights\_by\_country table schema

|  |
| --- |
| **ad\_id**  STRING |
| **ad\_name**  STRING |
| **ad\_text**  STRING |
| **adgroup\_id**  STRING |
| **adgroup\_name**  STRING |
| **advertiser\_id**  STRING |
| **bid**  STRING |
| **bid\_strategy**  STRING |
| **billing\_event**  STRING |
| **budget**  STRING |
| **call\_to\_action**  STRING |
| **campaign\_budget**  STRING |
| **campaign\_dedicate\_type**  STRING |
| **campaign\_id**  STRING |
| **campaign\_name**  STRING |
| **clicks**  INTEGER |
| **conversion**  INTEGER |
| **conversion\_rate**  NUMBER |
| **conversion\_rate\_v2**  NUMBER |
| **cost\_per\_conversion**  NUMBER |
| **cost\_per\_result**  NUMBER |
| **country\_code**  STRING |
| **cpc**  NUMBER |
| **cpm**  NUMBER |
| **ctr**  NUMBER |
| **dpa\_target\_audience\_type**  STRING |
| **gross\_impressions**  STRING |
| **impressions**  INTEGER |
| **is\_smart\_creative**  BOOLEAN |
| **mobile\_app\_id**  STRING |
| **objective\_type**  STRING |
| **opt\_status**  STRING |
| **promotion\_type**  STRING |
| **real\_time\_conversion**  INTEGER |
| **real\_time\_conversion\_rate**  NUMBER |
| **real\_time\_conversion\_rate\_v2**  NUMBER |
| **real\_time\_cost\_per\_conversion**  NUMBER |
| **real\_time\_cost\_per\_result**  NUMBER |
| **real\_time\_result**  INTEGER |
| **real\_time\_result\_rate**  NUMBER |
| **result**  INTEGER |
| **result\_rate**  NUMBER |
| **rf\_campaign\_type**  STRING |
| **smart\_target**  STRING |
| **spend**  NUMBER |
| **split\_test**  STRING |
| **stat\_time\_day**  DATE-TIME |
| **tt\_app\_id**  STRING |
| **tt\_app\_name**  STRING |
| **user\_action**  STRING |

### ad\_insights\_by\_platform

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | ad\_id  adgroup\_id  campaign\_id  platform  stat\_time\_day |
| **Replication Key** | stat\_time\_day |
| **Useful links** | [TikTok Ads documentation](https://ads.tiktok.com/marketing_api/docs?id=1707957217727489) |

ad\_insights\_by\_platform table schema

|  |
| --- |
| **ad\_id**  STRING |
| **ad\_name**  STRING |
| **ad\_text**  STRING |
| **adgroup\_id**  STRING |
| **adgroup\_name**  STRING |
| **advertiser\_id**  STRING |
| **bid**  STRING |
| **bid\_strategy**  STRING |
| **billing\_event**  STRING |
| **budget**  STRING |
| **call\_to\_action**  STRING |
| **campaign\_budget**  STRING |
| **campaign\_dedicate\_type**  STRING |
| **campaign\_id**  STRING |
| **campaign\_name**  STRING |
| **clicks**  INTEGER |
| **conversion**  INTEGER |
| **conversion\_rate**  NUMBER |
| **conversion\_rate\_v2**  NUMBER |
| **cost\_per\_conversion**  NUMBER |
| **cost\_per\_result**  NUMBER |
| **cpc**  NUMBER |
| **cpm**  NUMBER |
| **ctr**  NUMBER |
| **dpa\_target\_audience\_type**  STRING |
| **gross\_impressions**  STRING |
| **impressions**  INTEGER |
| **is\_smart\_creative**  BOOLEAN |
| **mobile\_app\_id**  STRING |
| **objective\_type**  STRING |
| **opt\_status**  STRING |
| **platform**  STRING |
| **promotion\_type**  STRING |
| **real\_time\_conversion**  INTEGER |
| **real\_time\_conversion\_rate**  NUMBER |
| **real\_time\_conversion\_rate\_v2**  NUMBER |
| **real\_time\_cost\_per\_conversion**  NUMBER |
| **real\_time\_cost\_per\_result**  NUMBER |
| **real\_time\_result**  INTEGER |
| **real\_time\_result\_rate**  NUMBER |
| **result**  INTEGER |
| **result\_rate**  NUMBER |
| **rf\_campaign\_type**  STRING |
| **smart\_target**  STRING |
| **spend**  NUMBER |
| **split\_test**  STRING |
| **stat\_time\_day**  DATE-TIME |
| **tt\_app\_id**  STRING |
| **tt\_app\_name**  STRING |
| **user\_action**  STRING |

### adgroups

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | adgroup\_id  advertiser\_id  campaign\_id  modify\_time |
| **Replication Key** | modify\_time |
| **Useful links** | [TikTok Ads documentation](https://ads.tiktok.com/marketing_api/docs?id=1708503489590273) |

adgroups table schema

|  |
| --- |
| **actions**  ARRAY This is a nested data structure:   - action\_category\_ids: ARRAY - action\_period: NUMBER - action\_scene: STRING - video\_user\_actions: ARRAY |
| **adgroup\_app\_profile\_page\_state**  STRING |
| **adgroup\_id**  STRING |
| **adgroup\_name**  STRING |
| **advertiser\_id**  STRING |
| **age\_groups**  ARRAY |
| **app\_download\_url**  STRING |
| **app\_id**  STRING |
| **audience**  ARRAY |
| **audience\_type**  STRING |
| **bid\_price**  NUMBER |
| **bid\_type**  STRING |
| **billing\_event**  STRING |
| **brand\_safety\_partner**  STRING |
| **brand\_safety\_type**  STRING |
| **budget**  NUMBER |
| **budget\_mode**  STRING |
| **campaign\_id**  STRING |
| **carriers\_v2**  ARRAY |
| **catalog\_authorized\_bc**  INTEGER |
| **catalog\_id**  STRING |
| **conversion\_bid\_price**  NUMBER |
| **conversion\_window**  STRING |
| **cpv\_video\_duration**  STRING |
| **create\_time**  DATE-TIME |
| **creative\_material\_mode**  STRING |
| **current\_status**  STRING |
| **dayparting**  STRING |
| **deep\_bid\_type**  STRING |
| **deep\_cpa\_bid**  NUMBER |
| **delivery\_mode**  STRING |
| **device\_models**  ARRAY |
| **device\_price\_ranges**  ARRAY |
| **excluded\_audience**  ARRAY |
| **excluded\_custom\_actions**  ARRAY This is a nested data structure:   - code: STRING - days: INTEGER |
| **frequency**  INTEGER |
| **frequency\_schedule**  INTEGER |
| **gender**  STRING |
| **included\_custom\_actions**  ARRAY This is a nested data structure:   - code: STRING - days: INTEGER |
| **interest\_category\_v2**  ARRAY |
| **interest\_keywords**  ARRAY |
| **inventory\_filter\_enabled**  BOOLEAN |
| **ios14\_targeting**  STRING |
| **ios\_quota\_type**  STRING |
| **is\_comment\_disable**  BOOLEAN |
| **is\_hfss**  BOOLEAN |
| **is\_new\_structure**  BOOLEAN |
| **languages**  ARRAY |
| **location**  ARRAY |
| **min\_android\_version**  STRING |
| **min\_ios\_version**  STRING |
| **modify\_time**  DATE-TIME |
| **network\_types**  ARRAY |
| **next\_day\_retention**  NUMBER |
| **operating\_systems**  ARRAY |
| **operation\_status**  STRING |
| **optimization\_event**  STRING |
| **optimization\_goal**  STRING |
| **pacing**  STRING |
| **package**  STRING |
| **pangle\_audience\_package\_exclude**  ARRAY |
| **pangle\_audience\_package\_include**  ARRAY |
| **pangle\_block\_app\_list\_id**  ARRAY |
| **pixel\_id**  STRING |
| **placement\_type**  STRING |
| **placements**  ARRAY |
| **product\_set\_id**  STRING |
| **promotion\_type**  STRING |
| **promotion\_website\_type**  STRING |
| **purchased\_impression**  NUMBER |
| **purchased\_reach**  NUMBER |
| **rf\_estimated\_cpr**  NUMBER |
| **rf\_estimated\_frequency**  NUMBER |
| **rf\_purchased\_type**  STRING |
| **roas\_bid**  NUMBER |
| **schedule\_end\_time**  DATE-TIME |
| **schedule\_start\_time**  DATE-TIME |
| **schedule\_type**  STRING |
| **secondary\_optimization\_event**  STRING |
| **secondary\_status**  STRING |
| **share\_disabled**  BOOLEAN |
| **shopping\_ads\_retargeting\_type**  STRING |
| **skip\_learning\_phase**  BOOLEAN |
| **statistic\_type**  STRING |
| **targeting\_expansion**  OBJECT This is a nested data structure:   - expansion\_enabled: BOOLEAN - expansion\_types: ARRAY |
| **video\_download**  STRING |

### ads

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | ad\_id  adgroup\_id  advertiser\_id  campaign\_id  modify\_time |
| **Replication Key** | modify\_time |
| **Useful links** | [TikTok Ads documentation](https://ads.tiktok.com/marketing_api/docs?id=1708572923161602) |

ads table schema

|  |
| --- |
| **ad\_format**  STRING |
| **ad\_id**  STRING |
| **ad\_name**  STRING |
| **ad\_text**  STRING |
| **adgroup\_id**  STRING |
| **adgroup\_name**  STRING |
| **advertiser\_id**  STRING |
| **app\_name**  STRING |
| **brand\_safety\_vast\_url**  STRING |
| **call\_to\_action**  STRING |
| **campaign\_id**  STRING |
| **campaign\_name**  STRING |
| **card\_id**  STRING |
| **carousel\_image\_index**  INTEGER |
| **catalog\_id**  STRING |
| **click\_tracking\_url**  STRING |
| **create\_time**  DATE-TIME |
| **creative\_authorized**  BOOLEAN |
| **current\_status**  STRING |
| **deeplink**  STRING |
| **deeplink\_type**  STRING |
| **display\_name**  STRING |
| **dynamic\_destination**  STRING |
| **dynamic\_format**  STRING |
| **fallback\_type**  STRING |
| **image\_ids**  ARRAY |
| **image\_mode**  STRING |
| **impression\_tracking\_url**  STRING |
| **is\_aco**  BOOLEAN |
| **is\_new\_structure**  BOOLEAN |
| **item\_duet\_status**  STRING |
| **item\_group\_ids**  ARRAY |
| **item\_stitch\_status**  STRING |
| **landing\_page\_url**  STRING |
| **landing\_page\_urls**  STRING |
| **modify\_time**  DATE-TIME |
| **music\_id**  STRING |
| **operation\_status**  STRING |
| **page\_id**  NUMBER |
| **playable\_url**  STRING |
| **product\_set\_id**  STRING |
| **product\_specific\_type**  STRING |
| **profile\_image\_url**  STRING |
| **promotional\_music\_disabled**  BOOLEAN |
| **secondary\_status**  STRING |
| **shopping\_ads\_fallback\_type**  STRING |
| **shopping\_ads\_video\_package\_id**  STRING |
| **shopping\_deeplink\_type**  STRING |
| **showcase\_products**  ARRAY This is a nested data structure:   - catalog\_id: STRING - item\_group\_id: STRING - store\_id: STRING |
| **sku\_ids**  STRING |
| **tiktok\_item\_id**  STRING |
| **tracking\_app\_id**  STRING |
| **tracking\_offline\_event\_set\_ids**  ARRAY |
| **utm\_params**  ARRAY This is a nested data structure:   - key: STRING - value: STRING |
| **vast\_moat\_enabled**  BOOLEAN |
| **vertical\_video\_strategy**  STRING |
| **video\_id**  STRING |
| **viewability\_postbid\_partner**  STRING |
| **viewability\_vast\_url**  STRING |

### advertisers

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | advertiser\_id  create\_time |
| **Replication Key** | create\_time |
| **Useful links** | [TikTok Ads documentation](https://ads.tiktok.com/marketing_api/docs?id=1708503235186689) |

advertisers table schema

|  |
| --- |
| **address**  STRING |
| **advertiser\_account\_type**  STRING |
| **advertiser\_id**  STRING |
| **balance**  NUMBER |
| **cellphone\_number**  STRING |
| **company**  STRING |
| **contacter**  STRING |
| **country**  STRING |
| **create\_time**  STRING |
| **currency**  STRING |
| **description**  STRING |
| **email**  STRING |
| **industry**  STRING |
| **language**  STRING |
| **license\_no**  STRING |
| **license\_url**  STRING |
| **name**  STRING |
| **promotion\_area**  STRING |
| **promotion\_center\_city**  STRING |
| **promotion\_center\_province**  STRING |
| **rejection\_reason**  STRING |
| **role**  STRING |
| **status**  STRING |
| **telephone\_number**  STRING |
| **timezone**  STRING |

### campaign\_insights\_by\_province

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | advertiser\_id  campaign\_id  province\_id  stat\_time\_day |
| **Replication Key** | stat\_time\_day |
| **Useful links** | TikTok Ads documentation |

campaign\_insights\_by\_province table schema

|  |
| --- |
| **advertiser\_id**  STRING |
| **campaign\_budget**  STRING |
| **campaign\_dedicate\_type**  STRING |
| **campaign\_id**  STRING |
| **campaign\_name**  STRING |
| **clicks**  INTEGER |
| **conversion**  INTEGER |
| **conversion\_rate**  NUMBER |
| **conversion\_rate\_v2**  NUMBER |
| **cost\_per\_conversion**  NUMBER |
| **cost\_per\_result**  NUMBER |
| **cpc**  NUMBER |
| **cpm**  NUMBER |
| **ctr**  NUMBER |
| **gross\_impressions**  STRING |
| **impressions**  INTEGER |
| **objective\_type**  STRING |
| **province\_id**  STRING |
| **real\_time\_conversion**  INTEGER |
| **real\_time\_conversion\_rate**  NUMBER |
| **real\_time\_conversion\_rate\_v2**  NUMBER |
| **real\_time\_cost\_per\_conversion**  NUMBER |
| **real\_time\_cost\_per\_result**  NUMBER |
| **real\_time\_result**  INTEGER |
| **real\_time\_result\_rate**  NUMBER |
| **result**  INTEGER |
| **result\_rate**  NUMBER |
| **rf\_campaign\_type**  STRING |
| **spend**  NUMBER |
| **split\_test**  STRING |
| **stat\_time\_day**  DATE-TIME |

### campaigns

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | advertiser\_id  campaign\_id  modify\_time |
| **Replication Key** | modify\_time |
| **Useful links** | [TikTok Ads documentation](https://ads.tiktok.com/marketing_api/docs?id=1708582970809346) |

campaigns table schema

|  |
| --- |
| **advertiser\_id**  STRING |
| **app\_id**  STRING |
| **app\_promotion\_type**  STRING |
| **bid\_type**  STRING |
| **budget**  NUMBER |
| **budget\_mode**  STRING |
| **budget\_optimize\_on**  BOOLEAN |
| **campaign\_app\_profile\_page\_state**  STRING |
| **campaign\_id**  STRING |
| **campaign\_name**  STRING |
| **campaign\_product\_source**  STRING |
| **campaign\_type**  STRING |
| **create\_time**  DATE-TIME |
| **current\_status**  STRING |
| **deep\_bid\_type**  STRING |
| **is\_new\_structure**  BOOLEAN |
| **is\_smart\_performance\_campaign**  BOOLEAN |
| **modify\_time**  DATE-TIME |
| **objective**  STRING |
| **objective\_type**  STRING |
| **operation\_status**  STRING |
| **optimization\_goal**  STRING |
| **rf\_campaign\_type**  STRING |
| **roas\_bid**  NUMBER |
| **secondary\_status**  STRING |
| **special\_industries**  ARRAY |
