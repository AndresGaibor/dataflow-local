---
title: "AdRoll"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-AdRoll.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# AdRoll

AdRoll is an ecommerce marketing platform that gives growing D2C brands the power to connect with customers wherever they are.

AdRoll integration replicates data using the [NextRoll API](https://apidocs.nextroll.com/guides/get-started.html#guide-get-started).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To generate your client ID and secret:

1. Log into your [AdRoll](https://developers.nextroll.com/accounts/login) account.
2. Click your user email in the upper-right corner, then click Apps.
3. Select New Apps to start registration.
4. Enter a meaningful App name.
5. Enable Starter API Access; it is recommended to select Basic API Key Access due to NextRoll's API rate limits.
6. Set Callback URL to https://connector.qlik.com/auth/oauth/v3.htm.
7. Click Save.
8. Copy and paste your client ID and secret into a secured file.

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
| Lookback Window | Lookback window is the period during which recent data changes are checked and captured at each sync. Default is 7 days. |
| Client ID | Client ID. |
| Client Secret | Client secret. |
| End Date | The end date defines the last day included in data extraction in yyyy-mm-dd format. Default is the current day. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### ad\_groups

The `ad_groups` table contains info about the adgroups contained within the campaigns of your AdRoll account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | eid |
| **Useful links** | [AdRoll documentation](https://developers.nextroll.com/Content/crud-api/reference.html#get--api-v1-adgroup-get)  [AdRoll API method](https://developers.nextroll.com/Content/crud-api/reference.html#get--api-v1-advertisable-get_adgroups "Opens in new tab: AdRoll API method") |

ad\_groups table foreign keys

| Join ad\_groups with | on |
| --- | --- |
| [ads](#ads) | ``` ad_groups.eid = ads.adgroups.id ```  ``` ad_groups.ads.id = ads.eid ```  ``` ad_groups.ads.id = ads.original_ad ``` |
| [campaigns](#campaigns) | ``` ad_groups.eid = campaigns.adgroups.items ``` |
| [ad\_reports](#ad-reports) | ``` ad_groups.ads.id = ad_reports.ad ``` |
| [segments](#segments) | ``` ad_groups.segments.id = segments.eid ``` |

ad\_groups table schema

|  |
| --- |
| **ad\_optimization**  STRING |
| **ads**  ARRAY This is a nested data structure:   - id: STRING - status: STRING |
| **campaign**  STRING |
| **coops**  ARRAY This is a nested data structure. |
| **created\_date**  DATE-TIME |
| **demographic\_targets**  ARRAY This is a nested data structure. |
| **eid**  STRING |
| **flight\_timezone**  STRING |
| **geo\_targets**  ARRAY This is a nested data structure. |
| **is\_cats4gold**  BOOLEAN |
| **name**  STRING |
| **placement\_targets**  ARRAY This is a nested data structure. |
| **platform\_targets**  ARRAY This is a nested data structure. |
| **segments**  ARRAY This is a nested data structure:   - id: STRING - is\_negative: BOOLEAN |
| **site\_exclusions**  ARRAY This is a nested data structure. |
| **space\_optimization**  STRING |
| **status**  STRING |
| **type**  STRING |
| **updated\_date**  DATE-TIME |

### ad\_reports

The `ad_reports` table contains ad-level reporting data from your AdRoll account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | eid  date |
| **Replication Key** | date |
| **Useful links** | [AdRoll API method](https://developers.nextroll.com/Content/crud-api/reference.html#get--api-v1-report-ad "Opens in new tab: AdRoll API method") |

ad\_reports table foreign keys

| Join ad\_reports with | on |
| --- | --- |
| [ad\_groups](#ad-groups) | ``` ad_reports.ad = ad_groups.ads.id ``` |
| [ads](#ads) | ``` ad_reports.ad = ads.eid ```  ``` ad_reports.ad = ads.original_ad ``` |

ad\_reports table schema

|  |
| --- |
| **ad**  STRING |
| **ad\_size**  STRING |
| **adjusted\_click\_through\_ratio**  NUMBER |
| **adjusted\_cpa**  NUMBER |
| **adjusted\_ctc**  INTEGER |
| **adjusted\_total\_conversion\_rate**  NUMBER |
| **adjusted\_total\_conversions**  INTEGER |
| **adjusted\_view\_through\_ratio**  NUMBER |
| **adjusted\_vtc**  INTEGER |
| **advertiser**  STRING |
| **attributed\_click\_through\_rev**  NUMBER |
| **attributed\_rev**  NUMBER |
| **attributed\_view\_through\_rev**  NUMBER |
| **billing\_cost**  NUMBER |
| **click\_cpa**  NUMBER |
| **click\_through\_conversions**  INTEGER |
| **click\_through\_ratio**  NUMBER |
| **clicks**  INTEGER |
| **cost**  NUMBER |
| **cpa**  NUMBER |
| **cpc**  NUMBER |
| **cpm**  NUMBER |
| **created\_date**  STRING |
| **ctr**  NUMBER |
| **date**  DATE-TIME |
| **eid**  STRING |
| **height**  INTEGER |
| **impressions**  INTEGER |
| **paid\_impressions**  INTEGER |
| **prospects**  INTEGER |
| **roi**  NUMBER |
| **status**  STRING |
| **total\_conversion\_rate**  NUMBER |
| **total\_conversions**  INTEGER |
| **type**  STRING |
| **view\_through\_conversions**  INTEGER |
| **view\_through\_ratio**  NUMBER |
| **width**  INTEGER |

### ads

The `ads` table contains information about the ads and creatives associated with the advertisables in your AdRoll account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | eid |
| **Useful links** | [AdRoll documentation](https://developers.nextroll.com/Content/crud-api/reference.html#get--api-v1-ad-get)  [AdRoll API method](https://developers.nextroll.com/Content/crud-api/reference.html#get--api-v1-advertisable-get_ads "Opens in new tab: AdRoll API method") |

ads table foreign keys

| Join ads with | on |
| --- | --- |
| [ad\_groups](#ad-groups) | ``` ads.adgroups.id = ad_groups.eid ```  ``` ads.eid = ad_groups.ads.id ```  ``` ads.original_ad = ad_groups.ads.id ``` |
| [campaigns](#campaigns) | ``` ads.adgroups.id = campaigns.adgroups.items ``` |
| [ad\_reports](#ad-reports) | ``` ads.eid = ad_reports.ad ```  ``` ads.original_ad = ad_reports.ad ``` |

ads table schema

|  |
| --- |
| **ad\_format**  STRING |
| **ad\_format\_id**  INTEGER |
| **ad\_format\_name**  STRING |
| **ad\_parameters**  ARRAY This is a nested data structure. |
| **adgroups**  ARRAY This is a nested data structure:   - id: STRING - status: STRING |
| **advertisable**  STRING |
| **app\_id**  STRING |
| **body**  STRING |
| **body\_dynamic**  STRING |
| **brand\_name**  STRING |
| **call\_to\_action**  STRING |
| **created\_date**  DATE-TIME |
| **destination\_url**  STRING |
| **display\_url\_override**  STRING |
| **eid**  STRING |
| **has\_edits**  BOOLEAN |
| **has\_future\_campaigns**  BOOLEAN |
| **has\_pending\_edits**  BOOLEAN |
| **headline**  STRING |
| **headline\_dynamic**  STRING |
| **height**  INTEGER |
| **inventory\_type**  STRING |
| **is\_active**  BOOLEAN |
| **is\_fb\_dynamic**  BOOLEAN |
| **is\_liquid**  STRING |
| **is\_outlined**  BOOLEAN |
| **lead\_gen\_form\_id**  STRING |
| **message**  STRING |
| **message\_dynamic**  STRING |
| **multi\_share\_optimized**  STRING |
| **multiple\_products**  STRING |
| **name**  STRING |
| **original\_ad**  STRING |
| **outline\_color**  STRING |
| **replacement\_ad**  STRING |
| **src**  STRING |
| **status**  STRING |
| **type**  STRING |
| **updated\_date**  DATE-TIME |
| **valid\_clicktag**  BOOLEAN |
| **width**  INTEGER |

### advertisables

The `advertisables` table contains information about the advertisables in your AdRoll account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | eid |
| **Useful links** | [AdRoll documentation](https://developers.nextroll.com/Content/crud-api/reference.html#get--api-v1-advertisable-get)  [AdRoll API method](https://developers.nextroll.com/Content/crud-api/reference.html#get--api-v1-organization-get_advertisables "Opens in new tab: AdRoll API method") |

advertisables table foreign keys

| Join advertisables with | on |
| --- | --- |
| [campaigns](#campaigns) | ``` advertisables.eid = campaigns.advertisable ``` |
| [segments](#segments) | ``` advertisables.eid = segments.advertisable_eid ``` |

advertisables table schema

|  |
| --- |
| **abm\_onboarding\_status**  STRING |
| **account**  STRING |
| **account\_country\_code**  STRING |
| **account\_is\_autobilled**  BOOLEAN |
| **account\_is\_prepaid**  BOOLEAN |
| **account\_is\_suspended**  BOOLEAN |
| **account\_suspension\_reason**  STRING |
| **admin\_page\_permission**  BOOLEAN |
| **am\_email**  STRING |
| **approval\_state**  STRING |
| **attached\_users**  ARRAY This is a nested data structure. |
| **blacklisted\_sites**  ARRAY This is a nested data structure. |
| **business\_unit**  STRING |
| **campaign\_monitor\_client\_api\_key**  STRING |
| **campaign\_monitor\_client\_id**  STRING |
| **click\_through\_conversion\_window**  INTEGER |
| **cm\_networks**  STRING |
| **company\_phone**  STRING |
| **constant\_contact\_code**  STRING |
| **constant\_contact\_oauth\_url**  STRING |
| **country\_code**  STRING |
| **created\_date**  DATE-TIME |
| **csm\_admin**  STRING |
| **currency**  STRING |
| **default\_homepage**  STRING |
| **default\_utm**  STRING |
| **eid**  STRING |
| **enable\_customer\_multi\_dur\_segs**  BOOLEAN |
| **fb\_offsite\_pixels\_tos\_accepted**  BOOLEAN |
| **fbx\_account\_id**  INTEGER |
| **fbx\_page\_id**  STRING |
| **fbx\_page\_url**  STRING |
| **has\_approved\_consent\_solution**  BOOLEAN |
| **has\_approved\_safari\_add\_on**  BOOLEAN |
| **has\_created\_campaign**  BOOLEAN |
| **has\_offsite\_pixels**  BOOLEAN |
| **has\_privacy\_policy**  BOOLEAN |
| **has\_sales\_and\_leads\_automation**  BOOLEAN |
| **hide\_optins\_page**  BOOLEAN |
| **homepage\_enabled**  BOOLEAN |
| **iab1\_category\_id**  INTEGER |
| **iab1\_category\_name**  STRING |
| **iab2\_category\_id**  INTEGER |
| **iab2\_category\_name**  STRING |
| **iab\_content\_id**  INTEGER |
| **instagram\_actor\_id**  STRING |
| **ip\_address\_exclusions**  ARRAY This is a nested data structure. |
| **is\_abm\_customer**  BOOLEAN |
| **is\_active**  BOOLEAN |
| **is\_b2b**  BOOLEAN |
| **is\_campaign\_monitor\_syncing**  BOOLEAN |
| **is\_constant\_contact\_syncing**  BOOLEAN |
| **is\_coop\_approved**  STRING |
| **is\_kpi\_eligible**  BOOLEAN |
| **is\_managed**  BOOLEAN |
| **is\_marketo\_syncing**  BOOLEAN |
| **is\_salesforce\_system\_owned**  BOOLEAN |
| **is\_suspended**  BOOLEAN |
| **is\_trusted**  BOOLEAN |
| **is\_twitter\_syncing**  BOOLEAN |
| **liquidads**  STRING |
| **logo\_url**  STRING |
| **magellan\_legacy**  BOOLEAN |
| **magellan\_query**  BOOLEAN |
| **marketo\_api\_endpoint**  STRING |
| **marketo\_client\_id**  STRING |
| **marketo\_secret\_key**  STRING |
| **name**  STRING |
| **nbam\_admin**  STRING |
| **ops**  STRING |
| **optimizer**  STRING |
| **optimizer\_email**  STRING |
| **organization**  STRING |
| **page\_access\_request\_status**  STRING |
| **path\_name**  STRING |
| **product\_name**  STRING |
| **recent\_theme\_color**  STRING |
| **reskin\_enabled**  BOOLEAN |
| **revshare\_click\_percent**  NUMBER |
| **revshare\_view\_percent**  NUMBER |
| **rollcrawl\_enabled**  BOOLEAN |
| **rollworks\_self\_serve\_ads**  BOOLEAN |
| **safari\_add\_on\_theme**  STRING |
| **saleser**  STRING |
| **self\_serve\_prospecting\_enabled**  BOOLEAN |
| **show\_dpa**  BOOLEAN |
| **show\_web\_dynamic\_ads**  BOOLEAN |
| **source**  STRING |
| **status**  STRING |
| **twitter\_handle**  STRING |
| **uhura\_enabled**  BOOLEAN |
| **updated\_date**  STRING |
| **url**  STRING |
| **use\_universal\_campaigns**  BOOLEAN |
| **view\_through\_conversion\_window**  INTEGER |
| **zvelo\_category\_id**  INTEGER |
| **zvelo\_category\_name**  STRING |

### campaigns

The `campaigns` table contains information about the advertising campaigns in your AdRoll account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | eid |
| **Useful links** | [AdRoll documentation](https://developers.nextroll.com/Content/crud-api/reference.html#get--api-v1-campaign-get)  [AdRoll API method](https://developers.nextroll.com/Content/crud-api/reference.html#get--api-v1-advertisable-get_campaigns "Opens in new tab: AdRoll API method") |

campaigns table foreign keys

| Join campaigns with | on |
| --- | --- |
| [ad\_groups](#ad-groups) | ``` campaigns.adgroups.items = ad_groups.eid ``` |
| [ads](#ads) | ``` campaigns.adgroups.items = ads.adgroups.id ``` |
| [advertisables](#advertisables) | ``` campaigns.advertisable = advertisables.eid ``` |
| [segments](#segments) | ``` campaigns.advertisable = segments.advertisable_eid ``` |

campaigns table schema

|  |
| --- |
| **abm\_type**  STRING |
| **adgroups**  ARRAY This is a nested data structure. |
| **advertisable**  STRING |
| **bid\_strategy**  STRING |
| **bid\_strategy\_target**  STRING |
| **bid\_type**  STRING |
| **budget**  NUMBER |
| **campaign\_type**  STRING |
| **cpc**  NUMBER |
| **cpm**  NUMBER |
| **created\_date**  DATE-TIME |
| **eid**  STRING |
| **end\_date**  DATE-TIME |
| **facebook\_campaign\_objective**  STRING |
| **frequency\_cap**  STRING |
| **is\_active**  BOOLEAN |
| **is\_apple**  BOOLEAN |
| **is\_cats4gold**  BOOLEAN |
| **is\_coop**  BOOLEAN |
| **is\_facebook**  BOOLEAN |
| **is\_fb\_lookalike**  BOOLEAN |
| **is\_fb\_wca**  BOOLEAN |
| **is\_fbx\_newsfeed**  BOOLEAN |
| **is\_pubgraph**  BOOLEAN |
| **is\_retargeting**  BOOLEAN |
| **is\_rtb**  BOOLEAN |
| **max\_cpm**  NUMBER |
| **name**  STRING |
| **pa\_sales\_stage\_eid**  STRING |
| **pricing\_strategies**  ARRAY This is a nested data structure. |
| **source**  STRING |
| **spend\_limit\_until**  STRING |
| **start\_date**  DATE-TIME |
| **status**  STRING |
| **ui\_budget\_daily**  BOOLEAN |
| **updated\_date**  DATE-TIME |
| **use\_case**  STRING |

### segments

The `segments` table contains information about segments, or the lists of users that visit your AdRoll site.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | eid |
| **Useful links** | [AdRoll documentation](https://developers.nextroll.com/Content/crud-api/reference.html#get--api-v1-segment-get)  [AdRoll API method](https://developers.nextroll.com/Content/crud-api/reference.html#get--api-v1-advertisable-get_segments "Opens in new tab: AdRoll API method") |

segments table foreign keys

| Join segments with | on |
| --- | --- |
| [advertisables](#advertisables) | ``` segments.advertisable_eid = advertisables.eid ``` |
| [campaigns](#campaigns) | ``` segments.advertisable_eid = campaigns.advertisable ``` |
| [ad\_groups](#ad-groups) | ``` segments.eid = ad_groups.segments.id ``` |

segments table schema

|  |
| --- |
| **advertisable\_eid**  STRING |
| **conversion\_value**  STRING |
| **created\_date**  DATE-TIME |
| **display\_name**  STRING |
| **duration**  INTEGER |
| **duration\_sec**  INTEGER |
| **eid**  STRING |
| **group**  INTEGER |
| **has\_default\_rule**  BOOLEAN |
| **is\_active**  BOOLEAN |
| **match\_method**  STRING |
| **name**  STRING |
| **parent\_id**  STRING |
| **pattern**  STRING |
| **product**  STRING |
| **recent\_first\_match**  BOOLEAN |
| **rule**  STRING |
| **rule\_id**  INTEGER |
| **source**  STRING |
| **threshold**  INTEGER |
| **type**  STRING |
