---
title: "LinkedIn Ads"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-LinkedIn-Ads.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# LinkedIn Ads

LinkedIn is a social networking site designed for the business community. You can use LinkedIn Ads to promote your brand, increase traffic, find new leads and more.

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To set up a LinkedIn Ads connection in Qlik Talend Cloud, you must have access to the following:

- LinkedIn Ads account
- LinkedIn Campaign Manager account

To retrieve your client ID and client secret:

1. Log into your [LinkedIn](https://www.linkedin.com/login/en) account.
2. Navigate to Work > Advertise.
3. Locate the IDs for the accounts from which you want to replicate data.
4. Log into your [LinkedIn Developers](https://www.linkedin.com/developers/login) account.
5. Navigate to My Apps > Create App.
6. Enter the app information, and then click Create App.
7. From the Auth tab, copy and paste your client ID and client secret into a secured file.
8. Make sure Authorized Redirect URLs is set to https://connector.qlik.com/auth/oauth/v3.htm.
9. Open the Team Members tab and make sure you are added as a team member who can use the app.

Information note

Ask your LinkedIn organization admin to verify the app. If the app is not verified, you might not be able to grant the required scopes during authentication.

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
| Accounts | A comma separated list of accounts to sync. |
| Client ID | Client ID. |
| Client Secret | Client secret. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### account\_users

The `account_users` table contains info about the users who have permissions to an ad account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | account\_id  user\_person\_id |
| **Replication Key** | last\_modified\_time |
| **Useful links** | [LinkedIn Ads API method](https://docs.microsoft.com/en-us/linkedin/marketing/integrations/ads/account-structure/create-and-manage-account-users?view=li-lms-2022-07&tabs=http#find-ad-account-users-by-accounts "Opens in new tab: LinkedIn Ads API method") |

account\_users table foreign keys

| Join account\_users with | on |
| --- | --- |
| [accounts](#accounts) | ``` account_users.account_id = accounts.id ``` |
| [campaigns](#campaigns) | ``` account_users.account_id = campaigns.account_id ``` |
| [campaign\_groups](#campaign-groups) | ``` account_users.account_id = campaign_groups.account_id ``` |
| [video\_ads](#video-ads) | ``` account_users.account_id = video_ads.account_id ``` |

account\_users table schema

|  |
| --- |
| **account**  STRING |
| **account\_id**  INTEGER |
| **campaign\_contact**  BOOLEAN |
| **change\_audit\_stamps**  OBJECT This is a nested data structure:   - created: OBJECT, which is also a nested data structure.   - time: DATE-TIME - last\_modified: OBJECT, which is also a nested data structure.   - time: DATE-TIME |
| **created\_time**  DATE-TIME |
| **last\_modified\_time**  DATE-TIME |
| **role**  STRING |
| **user**  STRING |
| **user\_person\_id**  STRING |

### accounts

The `accounts` table contains info about your LinkedIn Ads ad accounts.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | last\_modified\_time |
| **Useful links** | [LinkedIn Ads API method](https://docs.microsoft.com/en-us/linkedin/marketing/integrations/ads/account-structure/create-and-manage-accounts?view=li-lms-2022-07&tabs=http#search-for-accounts "Opens in new tab: LinkedIn Ads API method") |

accounts table foreign keys

| Join accounts with | on |
| --- | --- |
| [account\_users](#account-users) | ``` accounts.id = account_users.account_id ``` |
| [campaigns](#campaigns) | ``` accounts.id = campaigns.account_id ``` |
| [campaign\_groups](#campaign-groups) | ``` accounts.id = campaign_groups.account_id ``` |
| [video\_ads](#video-ads) | ``` accounts.id = video_ads.account_id ``` |

accounts table schema

|  |
| --- |
| **change\_audit\_stamps**  OBJECT This is a nested data structure:   - created: OBJECT, which is also a nested data structure.   - time: DATE-TIME - last\_modified: OBJECT, which is also a nested data structure.   - time: DATE-TIME |
| **created\_time**  DATE-TIME |
| **currency**  STRING |
| **id**  INTEGER |
| **last\_modified\_time**  DATE-TIME |
| **name**  STRING |
| **notified\_on\_campaign\_optimization**  BOOLEAN |
| **notified\_on\_creative\_approval**  BOOLEAN |
| **notified\_on\_creative\_rejection**  BOOLEAN |
| **notified\_on\_end\_of\_campaign**  BOOLEAN |
| **notified\_on\_new\_features\_enabled**  BOOLEAN |
| **reference**  STRING |
| **reference\_organization\_id**  INTEGER |
| **reference\_person\_id**  STRING |
| **serving\_statuses**  ARRAY This is a nested data structure. |
| **status**  STRING |
| **test**  BOOLEAN |
| **total\_budget**  OBJECT This is a nested data structure:   - amount: NUMBER - currency\_code: STRING |
| **total\_budget\_ends\_at**  DATE-TIME |
| **type**  STRING |
| **version**  OBJECT This is a nested data structure:   - version\_tag: STRING |

### ad\_analytics\_by\_campaign

The `ad_analytics_by_campaign` table contains analytics data for ads, segmented by campaign.

**Note**: This table is replicated using an attribution window of 7 days. Refer to the [Replication](#replication) section for more info.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | campaign\_id  start\_at |
| **Replication Key** | end\_at |
| **Useful links** | [LinkedIn Ads API method](https://docs.microsoft.com/en-us/linkedin/marketing/integrations/ads-reporting/ads-reporting?view=li-lms-2022-07&tabs=http#analytics-finder "Opens in new tab: LinkedIn Ads API method") |

ad\_analytics\_by\_campaign table foreign keys

| Join ad\_analytics\_by\_campaign with | on |
| --- | --- |
| [campaigns](#campaigns) | ``` ad_analytics_by_campaign.campaign_id = campaigns.id ``` |
| [creatives](#creatives) | ``` ad_analytics_by_campaign.campaign_id = creatives.campaign_id ``` |

ad\_analytics\_by\_campaign table schema

|  |
| --- |
| **action\_clicks**  INTEGER |
| **ad\_unit\_clicks**  INTEGER |
| **approximate\_unique\_impressions**  INTEGER |
| **average\_daily\_reach\_metrics**  OBJECT This is a nested data structure:   - approximate\_cost\_in\_currency\_per\_thousand\_members\_reached: NUMBER - approximate\_frequency: NUMBER - approximate\_reach: NUMBER |
| **average\_previous\_seven\_day\_reach\_metrics**  OBJECT This is a nested data structure:   - approximate\_cost\_in\_currency\_per\_thousand\_members\_reached: NUMBER - approximate\_frequency: NUMBER - approximate\_reach: NUMBER |
| **average\_previous\_thirty\_day\_reach\_metrics**  OBJECT This is a nested data structure:   - approximate\_cost\_in\_currency\_per\_thousand\_members\_reached: NUMBER - approximate\_frequency: NUMBER - approximate\_reach: NUMBER |
| **campaign**  STRING |
| **campaign\_id**  INTEGER |
| **card\_clicks**  INTEGER |
| **card\_impressions**  INTEGER |
| **clicks**  INTEGER |
| **comment\_likes**  INTEGER |
| **comments**  INTEGER |
| **company\_page\_clicks**  INTEGER |
| **conversion\_value\_in\_local\_currency**  NUMBER |
| **cost\_in\_local\_currency**  NUMBER |
| **cost\_in\_usd**  NUMBER |
| **date\_range**  OBJECT This is a nested data structure:   - end: OBJECT, which is also a nested data structure.   - day: INTEGER   - month: INTEGER   - year: INTEGER - start: OBJECT, which is also a nested data structure.   - day: INTEGER   - month: INTEGER   - year: INTEGER |
| **document\_completions**  INTEGER |
| **document\_first\_quartile\_completions**  INTEGER |
| **document\_midpoint\_completions**  INTEGER |
| **document\_third\_quartile\_completions**  INTEGER |
| **download\_clicks**  INTEGER |
| **end\_at**  DATE-TIME |
| **external\_website\_conversions**  INTEGER |
| **external\_website\_post\_click\_conversions**  INTEGER |
| **external\_website\_post\_view\_conversions**  INTEGER |
| **follows**  INTEGER |
| **full\_screen\_plays**  INTEGER |
| **impressions**  INTEGER |
| **job\_applications**  NUMBER |
| **job\_apply\_clicks**  NUMBER |
| **landing\_page\_clicks**  INTEGER |
| **lead\_generation\_mail\_contact\_info\_shares**  INTEGER |
| **lead\_generation\_mail\_interested\_clicks**  INTEGER |
| **likes**  INTEGER |
| **one\_click\_lead\_form\_opens**  INTEGER |
| **one\_click\_leads**  INTEGER |
| **opens**  INTEGER |
| **other\_engagements**  INTEGER |
| **pivot**  STRING |
| **pivot\_value**  STRING |
| **pivot\_values**  ARRAY This is a nested data structure. |
| **post\_click\_job\_applications**  NUMBER |
| **post\_click\_job\_apply\_clicks**  NUMBER |
| **post\_click\_registrations**  NUMBER |
| **post\_view\_job\_applications**  NUMBER |
| **post\_view\_job\_apply\_clicks**  NUMBER |
| **post\_view\_registrations**  NUMBER |
| **reactions**  INTEGER |
| **registrations**  NUMBER |
| **sends**  INTEGER |
| **shares**  INTEGER |
| **start\_at**  DATE-TIME |
| **talent\_leads**  INTEGER |
| **text\_url\_clicks**  INTEGER |
| **total\_engagements**  INTEGER |
| **video\_completions**  INTEGER |
| **video\_first\_quartile\_completions**  INTEGER |
| **video\_midpoint\_completions**  INTEGER |
| **video\_starts**  INTEGER |
| **video\_third\_quartile\_completions**  INTEGER |
| **video\_views**  INTEGER |
| **viral\_card\_clicks**  INTEGER |
| **viral\_card\_impressions**  INTEGER |
| **viral\_clicks**  INTEGER |
| **viral\_comment\_likes**  INTEGER |
| **viral\_comments**  INTEGER |
| **viral\_company\_page\_clicks**  INTEGER |
| **viral\_document\_completions**  INTEGER |
| **viral\_document\_first\_quartile\_completions**  INTEGER |
| **viral\_document\_midpoint\_completions**  INTEGER |
| **viral\_document\_third\_quartile\_completions**  INTEGER |
| **viral\_download\_clicks**  INTEGER |
| **viral\_external\_website\_conversions**  INTEGER |
| **viral\_external\_website\_post\_click\_conversions**  INTEGER |
| **viral\_external\_website\_post\_view\_conversions**  INTEGER |
| **viral\_follows**  INTEGER |
| **viral\_full\_screen\_plays**  INTEGER |
| **viral\_impressions**  INTEGER |
| **viral\_job\_applications**  NUMBER |
| **viral\_job\_apply\_clicks**  NUMBER |
| **viral\_landing\_page\_clicks**  INTEGER |
| **viral\_likes**  INTEGER |
| **viral\_one\_click\_lead\_form\_opens**  INTEGER |
| **viral\_one\_click\_leads**  INTEGER |
| **viral\_other\_engagements**  INTEGER |
| **viral\_post\_click\_job\_applications**  NUMBER |
| **viral\_post\_click\_job\_apply\_clicks**  NUMBER |
| **viral\_post\_click\_registrations**  NUMBER |
| **viral\_post\_view\_job\_applications**  NUMBER |
| **viral\_post\_view\_job\_apply\_clicks**  NUMBER |
| **viral\_post\_view\_registrations**  NUMBER |
| **viral\_reactions**  INTEGER |
| **viral\_registrations**  NUMBER |
| **viral\_shares**  INTEGER |
| **viral\_total\_engagements**  INTEGER |
| **viral\_video\_completions**  INTEGER |
| **viral\_video\_first\_quartile\_completions**  INTEGER |
| **viral\_video\_midpoint\_completions**  INTEGER |
| **viral\_video\_starts**  INTEGER |
| **viral\_video\_third\_quartile\_completions**  INTEGER |
| **viral\_video\_views**  INTEGER |

### ad\_analytics\_by\_creative

The `ad_analytics_by_creative` table contains info about ad analytics, segmented by creative.

**Note**: This table is replicated using an attribution window of 7 days. Refer to the [Replication](#replication) section for more info.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | creative\_id  start\_at |
| **Replication Key** | end\_at |
| **Useful links** | [LinkedIn Ads API method](https://docs.microsoft.com/en-us/linkedin/marketing/integrations/ads-reporting/ads-reporting?view=li-lms-2022-07&tabs=http#analytics-finder "Opens in new tab: LinkedIn Ads API method") |

ad\_analytics\_by\_creative table foreign keys

| Join ad\_analytics\_by\_creative with | on |
| --- | --- |
| [creatives](#creatives) | ``` ad_analytics_by_creative.creative_id = creatives.id ``` |

ad\_analytics\_by\_creative table schema

|  |
| --- |
| **action\_clicks**  INTEGER |
| **ad\_unit\_clicks**  INTEGER |
| **approximate\_unique\_impressions**  INTEGER |
| **average\_daily\_reach\_metrics**  OBJECT This is a nested data structure:   - approximate\_cost\_in\_currency\_per\_thousand\_members\_reached: NUMBER - approximate\_frequency: NUMBER - approximate\_reach: NUMBER |
| **average\_previous\_seven\_day\_reach\_metrics**  OBJECT This is a nested data structure:   - approximate\_cost\_in\_currency\_per\_thousand\_members\_reached: NUMBER - approximate\_frequency: NUMBER - approximate\_reach: NUMBER |
| **average\_previous\_thirty\_day\_reach\_metrics**  OBJECT This is a nested data structure:   - approximate\_cost\_in\_currency\_per\_thousand\_members\_reached: NUMBER - approximate\_frequency: NUMBER - approximate\_reach: NUMBER |
| **card\_clicks**  INTEGER |
| **card\_impressions**  INTEGER |
| **clicks**  INTEGER |
| **comment\_likes**  INTEGER |
| **comments**  INTEGER |
| **company\_page\_clicks**  INTEGER |
| **conversion\_value\_in\_local\_currency**  NUMBER |
| **cost\_in\_local\_currency**  NUMBER |
| **cost\_in\_usd**  NUMBER |
| **creative**  STRING |
| **creative\_id**  INTEGER |
| **date\_range**  OBJECT This is a nested data structure:   - end: OBJECT, which is also a nested data structure.   - day: INTEGER   - month: INTEGER   - year: INTEGER - start: OBJECT, which is also a nested data structure.   - day: INTEGER   - month: INTEGER   - year: INTEGER |
| **document\_completions**  INTEGER |
| **document\_first\_quartile\_completions**  INTEGER |
| **document\_midpoint\_completions**  INTEGER |
| **document\_third\_quartile\_completions**  INTEGER |
| **download\_clicks**  INTEGER |
| **end\_at**  DATE-TIME |
| **external\_website\_conversions**  INTEGER |
| **external\_website\_post\_click\_conversions**  INTEGER |
| **external\_website\_post\_view\_conversions**  INTEGER |
| **follows**  INTEGER |
| **full\_screen\_plays**  INTEGER |
| **impressions**  INTEGER |
| **job\_applications**  NUMBER |
| **job\_apply\_clicks**  NUMBER |
| **landing\_page\_clicks**  INTEGER |
| **lead\_generation\_mail\_contact\_info\_shares**  INTEGER |
| **lead\_generation\_mail\_interested\_clicks**  INTEGER |
| **likes**  INTEGER |
| **one\_click\_lead\_form\_opens**  INTEGER |
| **one\_click\_leads**  INTEGER |
| **opens**  INTEGER |
| **other\_engagements**  INTEGER |
| **pivot**  STRING |
| **pivot\_value**  STRING |
| **pivot\_values**  ARRAY This is a nested data structure. |
| **post\_click\_job\_applications**  NUMBER |
| **post\_click\_job\_apply\_clicks**  NUMBER |
| **post\_click\_registrations**  NUMBER |
| **post\_view\_job\_applications**  NUMBER |
| **post\_view\_job\_apply\_clicks**  NUMBER |
| **post\_view\_registrations**  NUMBER |
| **reactions**  INTEGER |
| **registrations**  NUMBER |
| **sends**  INTEGER |
| **shares**  INTEGER |
| **start\_at**  DATE-TIME |
| **talent\_leads**  INTEGER |
| **text\_url\_clicks**  INTEGER |
| **total\_engagements**  INTEGER |
| **video\_completions**  INTEGER |
| **video\_first\_quartile\_completions**  INTEGER |
| **video\_midpoint\_completions**  INTEGER |
| **video\_starts**  INTEGER |
| **video\_third\_quartile\_completions**  INTEGER |
| **video\_views**  INTEGER |
| **viral\_card\_clicks**  INTEGER |
| **viral\_card\_impressions**  INTEGER |
| **viral\_clicks**  INTEGER |
| **viral\_comment\_likes**  INTEGER |
| **viral\_comments**  INTEGER |
| **viral\_company\_page\_clicks**  INTEGER |
| **viral\_document\_completions**  INTEGER |
| **viral\_document\_first\_quartile\_completions**  INTEGER |
| **viral\_document\_midpoint\_completions**  INTEGER |
| **viral\_document\_third\_quartile\_completions**  INTEGER |
| **viral\_download\_clicks**  INTEGER |
| **viral\_external\_website\_conversions**  INTEGER |
| **viral\_external\_website\_post\_click\_conversions**  INTEGER |
| **viral\_external\_website\_post\_view\_conversions**  INTEGER |
| **viral\_follows**  INTEGER |
| **viral\_full\_screen\_plays**  INTEGER |
| **viral\_impressions**  INTEGER |
| **viral\_job\_applications**  NUMBER |
| **viral\_job\_apply\_clicks**  NUMBER |
| **viral\_landing\_page\_clicks**  INTEGER |
| **viral\_likes**  INTEGER |
| **viral\_one\_click\_lead\_form\_opens**  INTEGER |
| **viral\_one\_click\_leads**  INTEGER |
| **viral\_other\_engagements**  INTEGER |
| **viral\_post\_click\_job\_applications**  NUMBER |
| **viral\_post\_click\_job\_apply\_clicks**  NUMBER |
| **viral\_post\_click\_registrations**  NUMBER |
| **viral\_post\_view\_job\_applications**  NUMBER |
| **viral\_post\_view\_job\_apply\_clicks**  NUMBER |
| **viral\_post\_view\_registrations**  NUMBER |
| **viral\_reactions**  INTEGER |
| **viral\_registrations**  INTEGER |
| **viral\_shares**  INTEGER |
| **viral\_total\_engagements**  INTEGER |
| **viral\_video\_completions**  INTEGER |
| **viral\_video\_first\_quartile\_completions**  INTEGER |
| **viral\_video\_midpoint\_completions**  INTEGER |
| **viral\_video\_starts**  INTEGER |
| **viral\_video\_third\_quartile\_completions**  INTEGER |
| **viral\_video\_views**  INTEGER |

### campaign\_groups

The `campaign_groups` table contains info about the campaign groups in your LinkedIn Ads account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | last\_modified\_time |
| **Useful links** | [LinkedIn Ads API method](https://docs.microsoft.com/en-us/linkedin/marketing/integrations/ads/account-structure/create-and-manage-campaign-groups?view=li-lms-2022-07&tabs=http#search-for-campaign-groups "Opens in new tab: LinkedIn Ads API method") |

campaign\_groups table foreign keys

| Join campaign\_groups with | on |
| --- | --- |
| [account\_users](#account-users) | ``` campaign_groups.account_id = account_users.account_id ``` |
| [accounts](#accounts) | ``` campaign_groups.account_id = accounts.id ``` |
| [campaigns](#campaigns) | ``` campaign_groups.account_id = campaigns.account_id ```  ``` campaign_groups.id = campaigns.campaign_group_id ``` |
| [video\_ads](#video-ads) | ``` campaign_groups.account_id = video_ads.account_id ``` |

campaign\_groups table schema

|  |
| --- |
| **account**  STRING |
| **account\_id**  INTEGER |
| **allowed\_campaign\_types**  ARRAY This is a nested data structure. |
| **backfilled**  BOOLEAN |
| **change\_audit\_stamps**  OBJECT This is a nested data structure:   - created: OBJECT, which is also a nested data structure.   - time: DATE-TIME - last\_modified: OBJECT, which is also a nested data structure.   - time: DATE-TIME |
| **created\_time**  DATE-TIME |
| **id**  INTEGER |
| **last\_modified\_time**  DATE-TIME |
| **name**  STRING |
| **run\_schedule**  OBJECT This is a nested data structure:   - end: DATE-TIME - start: DATE-TIME |
| **serving\_statuses**  ARRAY This is a nested data structure. |
| **status**  STRING |
| **test**  BOOLEAN |
| **total\_budget**  OBJECT This is a nested data structure:   - amount: NUMBER - currency\_code: STRING |

### campaigns

The `campaigns` table contains info about the campaigns in your LinkedIn Ads account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | last\_modified\_time |
| **Useful links** | [LinkedIn Ads API method](https://docs.microsoft.com/en-us/linkedin/marketing/integrations/ads/account-structure/create-and-manage-campaigns?view=li-lms-2022-07&tabs=http#search-for-campaigns "Opens in new tab: LinkedIn Ads API method") |

campaigns table foreign keys

| Join campaigns with | on |
| --- | --- |
| [account\_users](#account-users) | ``` campaigns.account_id = account_users.account_id ``` |
| [accounts](#accounts) | ``` campaigns.account_id = accounts.id ``` |
| [campaign\_groups](#campaign-groups) | ``` campaigns.account_id = campaign_groups.account_id ```  ``` campaigns.campaign_group_id = campaign_groups.id ``` |
| [video\_ads](#video-ads) | ``` campaigns.account_id = video_ads.account_id ``` |
| [creatives](#creatives) | ``` campaigns.id = creatives.campaign_id ``` |
| [ad\_analytics\_by\_campaign](#ad-analytics-by-campaign) | ``` campaigns.id = ad_analytics_by_campaign.campaign_id ``` |

campaigns table schema

|  |
| --- |
| **account**  STRING |
| **account\_id**  INTEGER |
| **associated\_entity**  STRING |
| **associated\_entity\_organization\_id**  INTEGER |
| **associated\_entity\_person\_id**  STRING |
| **audience\_expansion\_enabled**  BOOLEAN |
| **campaign\_group**  STRING |
| **campaign\_group\_id**  INTEGER |
| **change\_audit\_stamps**  OBJECT This is a nested data structure:   - created: OBJECT, which is also a nested data structure.   - time: DATE-TIME - last\_modified: OBJECT, which is also a nested data structure.   - time: DATE-TIME |
| **cost\_type**  STRING |
| **created\_time**  DATE-TIME |
| **creative\_selection**  STRING |
| **daily\_budget**  OBJECT This is a nested data structure:   - amount: NUMBER - currency\_code: STRING |
| **format**  STRING |
| **id**  INTEGER |
| **last\_modified\_time**  DATE-TIME |
| **locale**  OBJECT This is a nested data structure:   - country: STRING - language: STRING |
| **name**  STRING |
| **objective\_type**  STRING |
| **offsite\_delivery\_enabled**  BOOLEAN |
| **offsite\_preferences**  OBJECT This is a nested data structure:   - iab\_categories: OBJECT, which is also a nested data structure.   - exclude: ARRAY, which is also a nested data structure.   - include: ARRAY, which is also a nested data structure. - publisher\_restriction\_files: OBJECT, which is also a nested data structure.   - exclude: ARRAY, which is also a nested data structure. |
| **optimization\_target\_type**  STRING |
| **pacing\_strategy**  STRING |
| **run\_schedule**  OBJECT This is a nested data structure:   - end: DATE-TIME - start: DATE-TIME |
| **serving\_statuses**  ARRAY This is a nested data structure. |
| **status**  STRING |
| **targeting**  OBJECT This is a nested data structure:   - excluded\_targeting\_facets: ARRAY, which is also a nested data structure.   - type: STRING   - values: ARRAY, which is also a nested data structure. - included\_targeting\_facets: ARRAY, which is also a nested data structure.   - type: STRING   - values: ARRAY, which is also a nested data structure. |
| **targeting\_criteria**  OBJECT This is a nested data structure:   - exclude: OBJECT, which is also a nested data structure.   - or: OBJECT, which is also a nested data structure.     - urn:li:ad\_targeting\_facet:followed\_companies: ARRAY, which is also a nested data structure.     - urn:li:ad\_targeting\_facet:seniorities: ARRAY, which is also a nested data structure.     - urn:li:ad\_targeting\_facet:staff\_count\_ranges: ARRAY, which is also a nested data structure.     - urn:li:ad\_targeting\_facet:titles: ARRAY, which is also a nested data structure. - include: OBJECT, which is also a nested data structure.   - and: OBJECT, which is also a nested data structure.     - type: STRING     - values: ARRAY, which is also a nested data structure. |
| **test**  BOOLEAN |
| **total\_budget**  OBJECT This is a nested data structure:   - amount: NUMBER - currency\_code: STRING |
| **type**  STRING |
| **unit\_cost**  OBJECT This is a nested data structure:   - amount: NUMBER - currency\_code: STRING |
| **version**  OBJECT This is a nested data structure:   - version\_tag: STRING |
| **version\_tag**  STRING |

### creatives

The Creatives API contains all the data and information for visually rendering an ad.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | last\_modified\_at |
| **Useful links** | [LinkedIn Ads documentation](https://learn.microsoft.com/en-us/linkedin/marketing/integrations/ads/account-structure/create-and-manage-creatives?view=li-lms-2023-01&tabs=http#search-for-creatives) |

creatives table foreign keys

| Join creatives with | on |
| --- | --- |
| [campaigns](#campaigns) | ``` creatives.campaign_id = campaigns.id ``` |
| [ad\_analytics\_by\_campaign](#ad-analytics-by-campaign) | ``` creatives.campaign_id = ad_analytics_by_campaign.campaign_id ``` |
| [ad\_analytics\_by\_creative](#ad-analytics-by-creative) | ``` creatives.id = ad_analytics_by_creative.creative_id ``` |

creatives table schema

|  |
| --- |
| **account**  STRING |
| **account\_id**  INTEGER |
| **campaign**  STRING |
| **campaign\_id**  INTEGER |
| **content**  OBJECT This is a nested data structure:   - reference: STRING - text\_ad: OBJECT, which is also a nested data structure.   - description: STRING   - headline: STRING   - landing\_page: STRING |
| **created\_at**  DATE-TIME |
| **created\_by**  STRING |
| **id**  STRING |
| **intended\_status**  STRING |
| **is\_serving**  BOOLEAN |
| **is\_test**  BOOLEAN |
| **last\_modified\_at**  DATE-TIME |
| **last\_modified\_by**  STRING |
| **serving\_hold\_reasons**  ARRAY This is a nested data structure. |

### video\_ads

The `video_ads` table contains info about the video ads in your LinkedIn Ads account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | content\_reference |
| **Replication Key** | last\_modified\_time |
| **Useful links** | [LinkedIn Ads API method](https://docs.microsoft.com/en-us/linkedin/marketing/integrations/ads/advertising-targeting/create-and-manage-video?view=li-lms-unversioned&tabs=http&viewFallbackFrom=li-lms-2022-07#finders "Opens in new tab: LinkedIn Ads API method") |

video\_ads table foreign keys

| Join video\_ads with | on |
| --- | --- |
| [account\_users](#account-users) | ``` video_ads.account_id = account_users.account_id ``` |
| [accounts](#accounts) | ``` video_ads.account_id = accounts.id ``` |
| [campaigns](#campaigns) | ``` video_ads.account_id = campaigns.account_id ``` |
| [campaign\_groups](#campaign-groups) | ``` video_ads.account_id = campaign_groups.account_id ``` |

video\_ads table schema

|  |
| --- |
| **account**  STRING |
| **account\_id**  INTEGER |
| **change\_audit\_stamps**  OBJECT This is a nested data structure:   - created: OBJECT, which is also a nested data structure.   - time: DATE-TIME - last\_modified: OBJECT, which is also a nested data structure.   - time: DATE-TIME |
| **content\_reference**  STRING |
| **content\_reference\_share\_id**  INTEGER |
| **content\_reference\_ucg\_post\_id**  INTEGER |
| **created\_time**  DATE-TIME |
| **last\_modified\_time**  DATE-TIME |
| **name**  STRING |
| **owner**  STRING |
| **owner\_organization\_id**  INTEGER |
| **type**  STRING |
