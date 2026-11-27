---
title: "Impact"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Impact-v2.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Impact

Impact is an affiliate software that helps brands track and optimize money from affiliate marketing with a partnership marketplace and detailed reporting.

Impact integration replicates data using the [Impact Radius API](https://developer.impact.com/default) and the Advertisers API catalog.

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To enable the API access for your Impact account:

1. Log into your Impact account.
2. Click the gear icon.
3. Click Technical Settings > API Access.
4. Click Enable API Access Now.

To retrieve your account SID and auth token:

1. Log into your Impact account.
2. Click the vertical ellipsis in the bottom-left corner.
3. Click Settings.
4. On the settings page, locate the Technical section and click API.
5. As the account SID and auth token are displayed only once, copy and paste them to a secured file.

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
| Account SID | Account SID. |
| Auth Token | Auth token. |
| API Catalog | API catalog. |
| Model ID | Model ID. This is used in the `conversion_paths` table to extract data about conversions from clicks to conversion purchases.  To access your model ID, contact [Impact Radius Support](mailto:support@impactradius.com) or [open an help desk request](https://app.impact.com/login.user) with Impact. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### action\_inquiries

The `action_inquiries` table contains info about a campaign’s action inquiries.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | creation\_date |
| **Useful links** | [Impact API method](https://developer.impact.com/default#operations-Action_Inquiries-GetActionInquiries "Opens in new tab: Impact API method") |

action\_inquiries table foreign keys

| Join action\_inquiries with | on |
| --- | --- |
| [action\_updates](#action-updates) | ``` action_inquiries.action_id = action_updates.action_id ```  ``` action_inquiries.campaign_id = action_updates.campaign_id ```  ``` action_inquiries.media_partner_id = action_updates.media_partner_id ``` |
| [actions](#actions) | ``` action_inquiries.action_id = actions.id ```  ``` action_inquiries.campaign_id = actions.campaign_id ```  ``` action_inquiries.media_partner_id = actions.media_partner_id ``` |
| [conversion\_paths](#conversion-paths) | ``` action_inquiries.action_id = conversion_paths.events.action_id ```  ``` action_inquiries.campaign_id = conversion_paths.campaign_id ``` |
| [ads](#ads) | ``` action_inquiries.campaign_id = ads.campaign_id ``` |
| [api\_submissions](#api-submissions) | ``` action_inquiries.campaign_id = api_submissions.campaign_id ```  ``` action_inquiries.media_partner_id = api_submissions.media_partner_id ``` |
| [campaigns](#campaigns) | ``` action_inquiries.campaign_id = campaigns.id ``` |
| [catalogs](#catalogs) | ``` action_inquiries.campaign_id = catalogs.campaign_id ``` |
| [clicks](#clicks) | ``` action_inquiries.campaign_id = clicks.campaign_id ``` |
| [contacts](#contacts) | ``` action_inquiries.campaign_id = contacts.campaign_id ``` |
| [deals](#deals) | ``` action_inquiries.campaign_id = deals.campaign_id ``` |
| [exception\_lists](#exception-lists) | ``` action_inquiries.campaign_id = exception_lists.campaign_id ``` |
| [invoices](#invoices) | ``` action_inquiries.campaign_id = invoices.line_items.campaign_id ``` |
| [media\_partner\_groups](#media-partner-groups) | ``` action_inquiries.campaign_id = media_partner_groups.campaign_id ```  ``` action_inquiries.media_partner_id = media_partner_groups.media_partners.partner_id ``` |
| [media\_partners](#media-partners) | ``` action_inquiries.campaign_id = media_partners.campaigns.campaign_id ```  ``` action_inquiries.media_partner_id = media_partners.id ``` |
| [notes](#notes) | ``` action_inquiries.campaign_id = notes.campaign_id ``` |
| [promo\_codes](#promo-codes) | ``` action_inquiries.campaign_id = promo_codes.campaign_id ``` |
| [tracking\_value\_requests](#tracking-value-requests) | ``` action_inquiries.campaign_id = tracking_value_requests.campaign_id ```  ``` action_inquiries.media_partner_id = tracking_value_requests.media_partner_id ``` |
| [unique\_urls](#unique-urls) | ``` action_inquiries.campaign_id = unique_urls.campaign_id ```  ``` action_inquiries.media_partner_id = unique_urls.media_partner_id ``` |

action\_inquiries table schema

|  |
| --- |
| **action\_id**  STRING |
| **action\_uri**  STRING |
| **auto\_approval\_date**  DATE-TIME |
| **campaign\_id**  INTEGER |
| **campaign\_name**  STRING |
| **comments**  ARRAY This is a nested data structure:   - comment: STRING - date: DATE-TIME - user: STRING |
| **creation\_date**  DATE-TIME |
| **expected\_payout**  NUMBER |
| **final\_payout**  NUMBER |
| **id**  INTEGER |
| **inquiry\_type**  STRING |
| **media\_partner\_id**  INTEGER |
| **media\_partner\_name**  STRING |
| **order\_id**  STRING |
| **reject\_reason**  STRING |
| **resolution\_date**  DATE-TIME |
| **resolution\_deadline\_date**  DATE-TIME |
| **resolution\_status**  STRING |
| **tracking\_link**  STRING |
| **transaction\_amount**  NUMBER |
| **transaction\_date**  DATE-TIME |
| **uri**  STRING |

### action\_updates

The `action_updates` table contains info about a campaign’s action updates.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | update\_date |
| **Useful links** | [Impact API method](https://developer.impact.com/default#operations-Action_Updates-ListActionUpdates "Opens in new tab: Impact API method") |

action\_updates table foreign keys

| Join action\_updates with | on |
| --- | --- |
| [actions](#actions) | ``` action_updates.action_tracker_id = actions.action_tracker_id ```  ``` action_updates.action_id = actions.id ```  ``` action_updates.ad_id = actions.ad_id ```  ``` action_updates.campaign_id = actions.campaign_id ```  ``` action_updates.customer_id = actions.customer_id ```  ``` action_updates.media_partner_id = actions.media_partner_id ``` |
| [api\_submissions](#api-submissions) | ``` action_updates.action_tracker_id = api_submissions.action_tracker_id ```  ``` action_updates.campaign_id = api_submissions.campaign_id ```  ``` action_updates.media_partner_id = api_submissions.media_partner_id ``` |
| [conversion\_paths](#conversion-paths) | ``` action_updates.action_tracker_id = conversion_paths.events.action_tracker_id ```  ``` action_updates.action_id = conversion_paths.events.action_id ```  ``` action_updates.ad_id = conversion_paths.events.ad_id ```  ``` action_updates.campaign_id = conversion_paths.campaign_id ```  ``` action_updates.customer_id = conversion_paths.customer_id ``` |
| [exception\_lists](#exception-lists) | ``` action_updates.action_tracker_id = exception_lists.action_trackers.id ```  ``` action_updates.campaign_id = exception_lists.campaign_id ``` |
| [action\_inquiries](#action-inquiries) | ``` action_updates.action_id = action_inquiries.action_id ```  ``` action_updates.campaign_id = action_inquiries.campaign_id ```  ``` action_updates.media_partner_id = action_inquiries.media_partner_id ``` |
| [ads](#ads) | ``` action_updates.ad_id = ads.id ```  ``` action_updates.campaign_id = ads.campaign_id ``` |
| [campaigns](#campaigns) | ``` action_updates.campaign_id = campaigns.id ``` |
| [catalogs](#catalogs) | ``` action_updates.campaign_id = catalogs.campaign_id ``` |
| [clicks](#clicks) | ``` action_updates.campaign_id = clicks.campaign_id ``` |
| [contacts](#contacts) | ``` action_updates.campaign_id = contacts.campaign_id ``` |
| [deals](#deals) | ``` action_updates.campaign_id = deals.campaign_id ``` |
| [invoices](#invoices) | ``` action_updates.campaign_id = invoices.line_items.campaign_id ``` |
| [media\_partner\_groups](#media-partner-groups) | ``` action_updates.campaign_id = media_partner_groups.campaign_id ```  ``` action_updates.media_partner_id = media_partner_groups.media_partners.partner_id ``` |
| [media\_partners](#media-partners) | ``` action_updates.campaign_id = media_partners.campaigns.campaign_id ```  ``` action_updates.media_partner_id = media_partners.id ``` |
| [notes](#notes) | ``` action_updates.campaign_id = notes.campaign_id ``` |
| [promo\_codes](#promo-codes) | ``` action_updates.campaign_id = promo_codes.campaign_id ``` |
| [tracking\_value\_requests](#tracking-value-requests) | ``` action_updates.campaign_id = tracking_value_requests.campaign_id ```  ``` action_updates.media_partner_id = tracking_value_requests.media_partner_id ``` |
| [unique\_urls](#unique-urls) | ``` action_updates.campaign_id = unique_urls.campaign_id ```  ``` action_updates.media_partner_id = unique_urls.media_partner_id ``` |

action\_updates table schema

|  |
| --- |
| **action\_date**  DATE-TIME |
| **action\_id**  STRING |
| **action\_tracker\_id**  INTEGER |
| **action\_uri**  STRING |
| **ad\_id**  INTEGER |
| **caller\_id**  STRING |
| **campaign\_id**  INTEGER |
| **category**  STRING |
| **clearing\_date**  DATE-TIME |
| **currency**  STRING |
| **customer\_id**  INTEGER |
| **customer\_status**  STRING |
| **delta\_amount**  NUMBER |
| **delta\_payout**  NUMBER |
| **disposition**  STRING |
| **id**  STRING |
| **locking\_date**  DATE-TIME |
| **media\_partner\_id**  INTEGER |
| **order\_id**  STRING |
| **quantity**  INTEGER |
| **shared\_id**  STRING |
| **sku**  STRING |
| **state**  STRING |
| **state\_detail**  STRING |
| **state\_detail\_description**  STRING |
| **update\_date**  DATE-TIME |
| **uri**  STRING |

### actions

The `actions` table contains info about a campaign’s actions.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | event\_date |
| **Useful links** | [Impact API method](https://developer.impact.com/default#operations-Actions-GetActions "Opens in new tab: Impact API method") |

actions table foreign keys

| Join actions with | on |
| --- | --- |
| [action\_updates](#action-updates) | ``` actions.action_tracker_id = action_updates.action_tracker_id ```  ``` actions.id = action_updates.action_id ```  ``` actions.ad_id = action_updates.ad_id ```  ``` actions.campaign_id = action_updates.campaign_id ```  ``` actions.customer_id = action_updates.customer_id ```  ``` actions.media_partner_id = action_updates.media_partner_id ``` |
| [api\_submissions](#api-submissions) | ``` actions.action_tracker_id = api_submissions.action_tracker_id ```  ``` actions.campaign_id = api_submissions.campaign_id ```  ``` actions.media_partner_id = api_submissions.media_partner_id ``` |
| [conversion\_paths](#conversion-paths) | ``` actions.action_tracker_id = conversion_paths.events.action_tracker_id ```  ``` actions.id = conversion_paths.events.action_id ```  ``` actions.ad_id = conversion_paths.events.ad_id ```  ``` actions.campaign_id = conversion_paths.campaign_id ```  ``` actions.customer_id = conversion_paths.customer_id ``` |
| [exception\_lists](#exception-lists) | ``` actions.action_tracker_id = exception_lists.action_trackers.id ```  ``` actions.campaign_id = exception_lists.campaign_id ``` |
| [action\_inquiries](#action-inquiries) | ``` actions.id = action_inquiries.action_id ```  ``` actions.campaign_id = action_inquiries.campaign_id ```  ``` actions.media_partner_id = action_inquiries.media_partner_id ``` |
| [ads](#ads) | ``` actions.ad_id = ads.id ```  ``` actions.campaign_id = ads.campaign_id ``` |
| [campaigns](#campaigns) | ``` actions.campaign_id = campaigns.id ``` |
| [catalogs](#catalogs) | ``` actions.campaign_id = catalogs.campaign_id ``` |
| [clicks](#clicks) | ``` actions.campaign_id = clicks.campaign_id ``` |
| [contacts](#contacts) | ``` actions.campaign_id = contacts.campaign_id ``` |
| [deals](#deals) | ``` actions.campaign_id = deals.campaign_id ``` |
| [invoices](#invoices) | ``` actions.campaign_id = invoices.line_items.campaign_id ``` |
| [media\_partner\_groups](#media-partner-groups) | ``` actions.campaign_id = media_partner_groups.campaign_id ```  ``` actions.media_partner_id = media_partner_groups.media_partners.partner_id ``` |
| [media\_partners](#media-partners) | ``` actions.campaign_id = media_partners.campaigns.campaign_id ```  ``` actions.media_partner_id = media_partners.id ``` |
| [notes](#notes) | ``` actions.campaign_id = notes.campaign_id ``` |
| [promo\_codes](#promo-codes) | ``` actions.campaign_id = promo_codes.campaign_id ``` |
| [tracking\_value\_requests](#tracking-value-requests) | ``` actions.campaign_id = tracking_value_requests.campaign_id ```  ``` actions.media_partner_id = tracking_value_requests.media_partner_id ``` |
| [unique\_urls](#unique-urls) | ``` actions.campaign_id = unique_urls.campaign_id ```  ``` actions.media_partner_id = unique_urls.media_partner_id ``` |

actions table schema

|  |
| --- |
| **action\_tracker\_id**  INTEGER |
| **action\_tracker\_name**  STRING |
| **ad\_id**  INTEGER |
| **amount**  NUMBER |
| **caller\_id**  STRING |
| **campaign\_id**  INTEGER |
| **campaign\_name**  STRING |
| **cleared\_date**  DATE-TIME |
| **client\_cost**  NUMBER |
| **creation\_date**  DATE-TIME |
| **currency**  STRING |
| **customer\_area**  STRING |
| **customer\_city**  STRING |
| **customer\_country**  STRING |
| **customer\_id**  STRING |
| **customer\_post\_code**  STRING |
| **customer\_region**  STRING |
| **customer\_status**  STRING |
| **delta\_amount**  NUMBER |
| **delta\_payout**  NUMBER |
| **event\_date**  DATE-TIME |
| **id**  STRING |
| **intended\_amount**  NUMBER |
| **intended\_payout**  NUMBER |
| **ip\_address**  STRING |
| **locking\_date**  DATE-TIME |
| **media\_partner\_id**  INTEGER |
| **media\_partner\_name**  STRING |
| **note**  STRING |
| **order\_id**  STRING |
| **payout**  NUMBER |
| **promo\_code**  STRING |
| **referring\_date**  DATE-TIME |
| **referring\_domain**  STRING |
| **referring\_type**  STRING |
| **shared\_id**  STRING |
| **state**  STRING |
| **uri**  STRING |

### ads

The `ads` table contains info about ads.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Impact API method](https://developer.impact.com/default#operations-Ads-ListAds "Opens in new tab: Impact API method") |

ads table foreign keys

| Join ads with | on |
| --- | --- |
| [action\_updates](#action-updates) | ``` ads.id = action_updates.ad_id ```  ``` ads.campaign_id = action_updates.campaign_id ``` |
| [actions](#actions) | ``` ads.id = actions.ad_id ```  ``` ads.campaign_id = actions.campaign_id ``` |
| [conversion\_paths](#conversion-paths) | ``` ads.id = conversion_paths.events.ad_id ```  ``` ads.campaign_id = conversion_paths.campaign_id ``` |
| [action\_inquiries](#action-inquiries) | ``` ads.campaign_id = action_inquiries.campaign_id ``` |
| [api\_submissions](#api-submissions) | ``` ads.campaign_id = api_submissions.campaign_id ``` |
| [campaigns](#campaigns) | ``` ads.campaign_id = campaigns.id ``` |
| [catalogs](#catalogs) | ``` ads.campaign_id = catalogs.campaign_id ``` |
| [clicks](#clicks) | ``` ads.campaign_id = clicks.campaign_id ``` |
| [contacts](#contacts) | ``` ads.campaign_id = contacts.campaign_id ``` |
| [deals](#deals) | ``` ads.campaign_id = deals.campaign_id ```  ``` ads.deal_id = deals.id ``` |
| [exception\_lists](#exception-lists) | ``` ads.campaign_id = exception_lists.campaign_id ``` |
| [invoices](#invoices) | ``` ads.campaign_id = invoices.line_items.campaign_id ``` |
| [media\_partner\_groups](#media-partner-groups) | ``` ads.campaign_id = media_partner_groups.campaign_id ``` |
| [media\_partners](#media-partners) | ``` ads.campaign_id = media_partners.campaigns.campaign_id ``` |
| [notes](#notes) | ``` ads.campaign_id = notes.campaign_id ``` |
| [promo\_codes](#promo-codes) | ``` ads.campaign_id = promo_codes.campaign_id ```  ``` ads.deal_id = promo_codes.deal_id ``` |
| [tracking\_value\_requests](#tracking-value-requests) | ``` ads.campaign_id = tracking_value_requests.campaign_id ```  ``` ads.deal_id = tracking_value_requests.deal_id ``` |
| [unique\_urls](#unique-urls) | ``` ads.campaign_id = unique_urls.campaign_id ``` |

ads table schema

|  |
| --- |
| **ad\_code\_template**  STRING |
| **ad\_type**  STRING |
| **allow\_deep\_linking**  BOOLEAN |
| **banner\_alternative\_tag**  STRING |
| **bogo\_buy\_image\_url**  STRING |
| **bogo\_buy\_name**  STRING |
| **bogo\_buy\_quantity**  STRING |
| **bogo\_buy\_scope**  STRING |
| **bogo\_get\_discount\_amount**  NUMBER |
| **bogo\_get\_discount\_currency**  STRING |
| **bogo\_get\_discount\_percent**  NUMBER |
| **bogo\_get\_discount\_type**  STRING |
| **bogo\_get\_image\_url**  STRING |
| **bogo\_get\_name**  STRING |
| **bogo\_get\_quantity**  STRING |
| **bogo\_get\_scope**  STRING |
| **campaign\_id**  INTEGER |
| **campaign\_name**  STRING |
| **coupon\_allow\_custom\_promo\_code**  BOOLEAN |
| **coupon\_link\_name**  STRING |
| **custom\_ad\_serving\_url**  STRING |
| **customisation\_charge**  NUMBER |
| **deal\_categories**  STRING |
| **deal\_default\_promo\_code**  STRING |
| **deal\_description**  STRING |
| **deal\_end\_date**  DATE-TIME |
| **deal\_id**  STRING |
| **deal\_name**  STRING |
| **deal\_products**  ARRAY This is a nested data structure:   - product\_after\_price\_amount: NUMBER - product\_after\_price\_currency: STRING - product\_before\_price\_amount: NUMBER - product\_before\_price\_currency: STRING - product\_image\_url: STRING - product\_name: STRING |
| **deal\_restricted\_media\_partner\_groups**  ARRAY This is a nested data structure. |
| **deal\_restricted\_media\_partners**  ARRAY This is a nested data structure. |
| **deal\_scope**  STRING |
| **deal\_start\_date**  DATE-TIME |
| **deal\_state**  STRING |
| **deal\_type**  STRING |
| **description**  STRING |
| **discount\_amount**  NUMBER |
| **discount\_currency**  STRING |
| **discount\_maximum\_percent**  NUMBER |
| **discount\_percent**  NUMBER |
| **discount\_percent\_range\_end**  NUMBER |
| **discount\_percent\_range\_start**  NUMBER |
| **discount\_type**  STRING |
| **get\_html\_code\_type**  STRING |
| **gift**  STRING |
| **iab\_ad\_unit**  STRING |
| **id**  INTEGER |
| **labels**  STRING |
| **landing\_page**  STRING |
| **language**  STRING |
| **limited\_time\_end\_date**  DATE-TIME |
| **limited\_time\_start\_date**  DATE-TIME |
| **link\_text**  STRING |
| **maximum\_savings\_amount**  NUMBER |
| **maximum\_savings\_currency**  STRING |
| **minimum\_purchase\_amount**  NUMBER |
| **minimum\_purchase\_amount\_currency**  STRING |
| **mobile\_ready**  BOOLEAN |
| **name**  STRING |
| **phone\_tracking**  BOOLEAN |
| **promo\_code\_tracking**  BOOLEAN |
| **purchase\_limit\_quantity**  STRING |
| **rebate\_amount**  NUMBER |
| **rebate\_currency**  STRING |
| **restricted\_media\_partner\_groups**  ARRAY This is a nested data structure. |
| **restricted\_media\_partners**  ARRAY This is a nested data structure. |
| **season**  STRING |
| **synch\_ads\_promo\_codes**  STRING |
| **third\_party\_servable\_ad\_creative\_height**  STRING |
| **third\_party\_servable\_ad\_creative\_width**  STRING |
| **top\_seller**  BOOLEAN |
| **uri**  STRING |

### api\_submissions

The `api_submissions` table contains info about API submissions.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | batch\_id |
| **Replication Key** | submission\_date |
| **Useful links** | [Impact API method](https://developer.impact.com/default/documentation/Rest-Adv-v8#operations-API_Submissions-GetAPISubmissions "Opens in new tab: Impact API method") |

api\_submissions table foreign keys

| Join api\_submissions with | on |
| --- | --- |
| [ftp\_file\_submissions](#ftp-file-submissions) | ``` api_submissions.account_id = ftp_file_submissions.account_id ``` |
| [action\_updates](#action-updates) | ``` api_submissions.action_tracker_id = action_updates.action_tracker_id ```  ``` api_submissions.campaign_id = action_updates.campaign_id ```  ``` api_submissions.media_partner_id = action_updates.media_partner_id ``` |
| [actions](#actions) | ``` api_submissions.action_tracker_id = actions.action_tracker_id ```  ``` api_submissions.campaign_id = actions.campaign_id ```  ``` api_submissions.media_partner_id = actions.media_partner_id ``` |
| [conversion\_paths](#conversion-paths) | ``` api_submissions.action_tracker_id = conversion_paths.events.action_tracker_id ```  ``` api_submissions.campaign_id = conversion_paths.campaign_id ``` |
| [exception\_lists](#exception-lists) | ``` api_submissions.action_tracker_id = exception_lists.action_trackers.id ```  ``` api_submissions.campaign_id = exception_lists.campaign_id ``` |
| [action\_inquiries](#action-inquiries) | ``` api_submissions.campaign_id = action_inquiries.campaign_id ```  ``` api_submissions.media_partner_id = action_inquiries.media_partner_id ``` |
| [ads](#ads) | ``` api_submissions.campaign_id = ads.campaign_id ``` |
| [campaigns](#campaigns) | ``` api_submissions.campaign_id = campaigns.id ``` |
| [catalogs](#catalogs) | ``` api_submissions.campaign_id = catalogs.campaign_id ``` |
| [clicks](#clicks) | ``` api_submissions.campaign_id = clicks.campaign_id ``` |
| [contacts](#contacts) | ``` api_submissions.campaign_id = contacts.campaign_id ``` |
| [deals](#deals) | ``` api_submissions.campaign_id = deals.campaign_id ``` |
| [invoices](#invoices) | ``` api_submissions.campaign_id = invoices.line_items.campaign_id ``` |
| [media\_partner\_groups](#media-partner-groups) | ``` api_submissions.campaign_id = media_partner_groups.campaign_id ```  ``` api_submissions.media_partner_id = media_partner_groups.media_partners.partner_id ``` |
| [media\_partners](#media-partners) | ``` api_submissions.campaign_id = media_partners.campaigns.campaign_id ```  ``` api_submissions.media_partner_id = media_partners.id ``` |
| [notes](#notes) | ``` api_submissions.campaign_id = notes.campaign_id ``` |
| [promo\_codes](#promo-codes) | ``` api_submissions.campaign_id = promo_codes.campaign_id ``` |
| [tracking\_value\_requests](#tracking-value-requests) | ``` api_submissions.campaign_id = tracking_value_requests.campaign_id ```  ``` api_submissions.media_partner_id = tracking_value_requests.media_partner_id ``` |
| [unique\_urls](#unique-urls) | ``` api_submissions.campaign_id = unique_urls.campaign_id ```  ``` api_submissions.media_partner_id = unique_urls.media_partner_id ``` |

api\_submissions table schema

|  |
| --- |
| **account\_id**  INTEGER |
| **action\_tracker\_id**  INTEGER |
| **batch\_id**  STRING |
| **campaign\_id**  INTEGER |
| **completion\_date**  DATE-TIME |
| **error\_reason**  STRING |
| **error\_type**  STRING |
| **event\_code**  STRING |
| **media\_partner\_id**  INTEGER |
| **order\_id**  STRING |
| **payload**  STRING |
| **status**  STRING |
| **submission\_date**  DATE-TIME |
| **type**  STRING |
| **uri**  STRING |

### campaigns

The `campaigns` table contains info about campaigns in your Impact account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Impact API method](https://developer.impact.com/default#operations-Campaigns-GetCampaigns "Opens in new tab: Impact API method") |

campaigns table foreign keys

| Join campaigns with | on |
| --- | --- |
| [action\_inquiries](#action-inquiries) | ``` campaigns.id = action_inquiries.campaign_id ``` |
| [action\_updates](#action-updates) | ``` campaigns.id = action_updates.campaign_id ``` |
| [actions](#actions) | ``` campaigns.id = actions.campaign_id ``` |
| [ads](#ads) | ``` campaigns.id = ads.campaign_id ``` |
| [api\_submissions](#api-submissions) | ``` campaigns.id = api_submissions.campaign_id ``` |
| [catalogs](#catalogs) | ``` campaigns.id = catalogs.campaign_id ``` |
| [clicks](#clicks) | ``` campaigns.id = clicks.campaign_id ``` |
| [contacts](#contacts) | ``` campaigns.id = contacts.campaign_id ``` |
| [conversion\_paths](#conversion-paths) | ``` campaigns.id = conversion_paths.campaign_id ``` |
| [deals](#deals) | ``` campaigns.id = deals.campaign_id ``` |
| [exception\_lists](#exception-lists) | ``` campaigns.id = exception_lists.campaign_id ``` |
| [invoices](#invoices) | ``` campaigns.id = invoices.line_items.campaign_id ``` |
| [media\_partner\_groups](#media-partner-groups) | ``` campaigns.id = media_partner_groups.campaign_id ``` |
| [media\_partners](#media-partners) | ``` campaigns.id = media_partners.campaigns.campaign_id ``` |
| [notes](#notes) | ``` campaigns.id = notes.campaign_id ``` |
| [promo\_codes](#promo-codes) | ``` campaigns.id = promo_codes.campaign_id ``` |
| [tracking\_value\_requests](#tracking-value-requests) | ``` campaigns.id = tracking_value_requests.campaign_id ``` |
| [unique\_urls](#unique-urls) | ``` campaigns.id = unique_urls.campaign_id ``` |

campaigns table schema

|  |
| --- |
| **categories**  OBJECT This is a nested data structure:   - additional\_category: STRING - additional\_sub\_categories: ARRAY, which is also a nested data structure. - primary\_category: STRING - primary\_sub\_categories: ARRAY, which is also a nested data structure. |
| **company\_contacts**  ARRAY This is a nested data structure:   - email\_address: STRING - first\_name: STRING - last\_name: STRING - phone\_number: STRING |
| **direct\_tracking\_settings**  OBJECT This is a nested data structure:   - session\_window\_length: INTEGER - unidentified\_source\_name: STRING |
| **display\_future\_ads**  BOOLEAN |
| **display\_servicing\_agency**  BOOLEAN |
| **gateway\_tracking\_settings**  OBJECT This is a nested data structure:   - campaign\_tracking\_template: STRING - deep\_link\_domains: STRING - deep\_linking: BOOLEAN - default\_landing\_page: STRING - media\_partner\_tracking\_template: STRING - ssl\_support: BOOLEAN - third\_party\_gateway\_query\_string\_parameters: STRING - third\_party\_gateway\_url: STRING - unique\_click\_window\_length: STRING - unique\_click\_window\_type: STRING |
| **gift\_card\_payouts**  BOOLEAN |
| **id**  INTEGER |
| **identity\_collapsing**  STRING |
| **impression\_tracking**  BOOLEAN |
| **list\_in\_marketplace**  BOOLEAN |
| **long\_description**  STRING |
| **mobile\_ready\_ads**  BOOLEAN |
| **name**  STRING |
| **promo\_code\_tracking**  BOOLEAN |
| **rating**  INTEGER |
| **resources**  OBJECT This is a nested data structure:   - additional\_related\_links: ARRAY, which is also a nested data structure.   - link\_display\_name: STRING   - link\_type: STRING   - link\_url: STRING - company\_homepage: STRING - example\_landing\_page: STRING - information\_page: STRING |
| **search\_keywords**  STRING |
| **shipping\_regions**  STRING |
| **short\_description**  STRING |
| **site\_definition**  STRING |
| **state**  STRING |
| **third\_party\_impression\_pixel**  STRING |
| **tracking\_domain**  STRING |
| **trademark\_bidding**  BOOLEAN |
| **view\_through\_crediting**  BOOLEAN |

### catalog\_items

The `catalog_items` table contains info about a catalog’s items.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | catalog\_item\_id |
| **Useful links** | [Impact API method](https://developer.impact.com/default#operations-Catalogs-ListCatalogs "Opens in new tab: Impact API method") |

catalog\_items table foreign keys

| Join catalog\_items with | on |
| --- | --- |
| [catalogs](#catalogs) | ``` catalog_items.catalog_id = catalogs.id ``` |

catalog\_items table schema

|  |
| --- |
| **additional\_image\_urls**  ARRAY This is a nested data structure. |
| **adult**  BOOLEAN |
| **age\_group**  STRING |
| **asin**  STRING |
| **bullets**  ARRAY This is a nested data structure. |
| **catalog\_id**  INTEGER |
| **catalog\_item\_id**  STRING |
| **category**  STRING |
| **colors**  ARRAY This is a nested data structure. |
| **condition**  STRING |
| **currency**  STRING |
| **current\_price**  NUMBER |
| **description**  STRING |
| **estimated\_ship\_date**  DATE-TIME |
| **expiration\_date**  DATE-TIME |
| **gender**  STRING |
| **gtin**  STRING |
| **gtin\_type**  STRING |
| **image\_url**  STRING |
| **inventory**  NUMBER |
| **is\_parent**  BOOLEAN |
| **labels**  ARRAY This is a nested data structure. |
| **launch\_date**  DATE-TIME |
| **manufacturer**  STRING |
| **manufacturing\_cost**  NUMBER |
| **material**  STRING |
| **mobile\_url**  STRING |
| **money1**  NUMBER |
| **money2**  NUMBER |
| **money3**  NUMBER |
| **mpn**  STRING |
| **multi\_pack**  INTEGER |
| **name**  STRING |
| **numeric1**  NUMBER |
| **numeric2**  NUMBER |
| **numeric3**  NUMBER |
| **original\_format\_category**  STRING |
| **original\_format\_category\_id**  INTEGER |
| **original\_price**  NUMBER |
| **parent\_name**  STRING |
| **parent\_sku**  STRING |
| **pattern**  STRING |
| **product\_bid**  NUMBER |
| **shipping\_height**  NUMBER |
| **shipping\_label**  STRING |
| **shipping\_length**  NUMBER |
| **shipping\_length\_unit**  STRING |
| **shipping\_rate**  NUMBER |
| **shipping\_weight**  NUMBER |
| **shipping\_weight\_unit**  STRING |
| **shipping\_width**  NUMBER |
| **size**  STRING |
| **size\_unit**  STRING |
| **stock\_availability**  STRING |
| **text1**  STRING |
| **text2**  STRING |
| **text3**  STRING |
| **uri**  STRING |
| **url**  STRING |
| **weight**  NUMBER |
| **weight\_unit**  STRING |

### catalogs

The `catalogs` table contains info about the catalogs in your Impact account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Impact API method](https://developer.impact.com/default#operations-Catalogs-ListCatalogs "Opens in new tab: Impact API method") |

catalogs table foreign keys

| Join catalogs with | on |
| --- | --- |
| [action\_inquiries](#action-inquiries) | ``` catalogs.campaign_id = action_inquiries.campaign_id ``` |
| [action\_updates](#action-updates) | ``` catalogs.campaign_id = action_updates.campaign_id ``` |
| [actions](#actions) | ``` catalogs.campaign_id = actions.campaign_id ``` |
| [ads](#ads) | ``` catalogs.campaign_id = ads.campaign_id ``` |
| [api\_submissions](#api-submissions) | ``` catalogs.campaign_id = api_submissions.campaign_id ``` |
| [campaigns](#campaigns) | ``` catalogs.campaign_id = campaigns.id ``` |
| [clicks](#clicks) | ``` catalogs.campaign_id = clicks.campaign_id ``` |
| [contacts](#contacts) | ``` catalogs.campaign_id = contacts.campaign_id ``` |
| [conversion\_paths](#conversion-paths) | ``` catalogs.campaign_id = conversion_paths.campaign_id ``` |
| [deals](#deals) | ``` catalogs.campaign_id = deals.campaign_id ``` |
| [exception\_lists](#exception-lists) | ``` catalogs.campaign_id = exception_lists.campaign_id ``` |
| [invoices](#invoices) | ``` catalogs.campaign_id = invoices.line_items.campaign_id ``` |
| [media\_partner\_groups](#media-partner-groups) | ``` catalogs.campaign_id = media_partner_groups.campaign_id ``` |
| [media\_partners](#media-partners) | ``` catalogs.campaign_id = media_partners.campaigns.campaign_id ``` |
| [notes](#notes) | ``` catalogs.campaign_id = notes.campaign_id ``` |
| [promo\_codes](#promo-codes) | ``` catalogs.campaign_id = promo_codes.campaign_id ``` |
| [tracking\_value\_requests](#tracking-value-requests) | ``` catalogs.campaign_id = tracking_value_requests.campaign_id ``` |
| [unique\_urls](#unique-urls) | ``` catalogs.campaign_id = unique_urls.campaign_id ``` |
| [catalog\_items](#catalog-items) | ``` catalogs.id = catalog_items.catalog_id ``` |

catalogs table schema

|  |
| --- |
| **advertiser\_id**  INTEGER |
| **campaign\_id**  INTEGER |
| **date\_last\_updated**  DATE-TIME |
| **filename**  STRING |
| **id**  INTEGER |
| **items\_uri**  STRING |
| **name**  STRING |
| **number\_of\_items**  INTEGER |
| **status**  STRING |
| **upload\_method**  STRING |
| **uri**  STRING |

### clicks

The `clicks` table contains info about a campaign’s clicks.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | event\_date |
| **Useful links** | [Impact API method](https://developer.impact.com/default#operations-Clicks-GetClicks "Opens in new tab: Impact API method") |

clicks table foreign keys

| Join clicks with | on |
| --- | --- |
| [action\_inquiries](#action-inquiries) | ``` clicks.campaign_id = action_inquiries.campaign_id ``` |
| [action\_updates](#action-updates) | ``` clicks.campaign_id = action_updates.campaign_id ``` |
| [actions](#actions) | ``` clicks.campaign_id = actions.campaign_id ``` |
| [ads](#ads) | ``` clicks.campaign_id = ads.campaign_id ``` |
| [api\_submissions](#api-submissions) | ``` clicks.campaign_id = api_submissions.campaign_id ``` |
| [campaigns](#campaigns) | ``` clicks.campaign_id = campaigns.id ``` |
| [catalogs](#catalogs) | ``` clicks.campaign_id = catalogs.campaign_id ``` |
| [contacts](#contacts) | ``` clicks.campaign_id = contacts.campaign_id ``` |
| [conversion\_paths](#conversion-paths) | ``` clicks.campaign_id = conversion_paths.campaign_id ```  ``` clicks.media_id = conversion_paths.events.media_id ``` |
| [deals](#deals) | ``` clicks.campaign_id = deals.campaign_id ``` |
| [exception\_lists](#exception-lists) | ``` clicks.campaign_id = exception_lists.campaign_id ``` |
| [invoices](#invoices) | ``` clicks.campaign_id = invoices.line_items.campaign_id ```  ``` clicks.media_id = invoices.media_id ``` |
| [media\_partner\_groups](#media-partner-groups) | ``` clicks.campaign_id = media_partner_groups.campaign_id ``` |
| [media\_partners](#media-partners) | ``` clicks.campaign_id = media_partners.campaigns.campaign_id ``` |
| [notes](#notes) | ``` clicks.campaign_id = notes.campaign_id ```  ``` clicks.media_id = notes.media_id ``` |
| [promo\_codes](#promo-codes) | ``` clicks.campaign_id = promo_codes.campaign_id ``` |
| [tracking\_value\_requests](#tracking-value-requests) | ``` clicks.campaign_id = tracking_value_requests.campaign_id ``` |
| [unique\_urls](#unique-urls) | ``` clicks.campaign_id = unique_urls.campaign_id ``` |

clicks table schema

|  |
| --- |
| **ad\_campaign**  STRING |
| **ad\_group**  STRING |
| **ad\_id**  INTEGER |
| **ad\_name**  STRING |
| **ad\_type**  STRING |
| **bid\_keyword**  STRING |
| **browser**  STRING |
| **campaign\_id**  INTEGER |
| **campaign\_name**  STRING |
| **channel**  STRING |
| **cpc\_bid**  NUMBER |
| **customer\_area**  STRING |
| **customer\_city**  STRING |
| **customer\_country"**  STRING |
| **customer\_region**  STRING |
| **deal\_name**  STRING |
| **deal\_scope**  STRING |
| **deal\_type**  STRING |
| **device\_family**  STRING |
| **device\_type**  STRING |
| **event\_date**  DATE-TIME |
| **id**  STRING |
| **ip\_address**  STRING |
| **keyword**  STRING |
| **landing\_page\_url**  STRING |
| **match\_type**  STRING |
| **media\_id**  INTEGER |
| **media\_name**  STRING |
| **os**  STRING |
| **payout**  NUMBER |
| **product\_sku**  STRING |
| **profile\_id**  STRING |
| **referring\_domain**  STRING |
| **referring\_url**  STRING |
| **search\_text**  STRING |
| **shared\_id**  STRING |
| **traffic\_category**  STRING |
| **traffic\_source**  STRING |
| **unique\_click**  BOOLEAN |

### company\_information

The `company_information` table contains details about companies.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | company\_name |
| **Useful links** | [Impact API method](https://developer.impact.com/default#operations-Company_Information-GetCompanyInfo "Opens in new tab: Impact API method") |

company\_information table schema

|  |
| --- |
| **billing\_address**  OBJECT This is a nested data structure:   - address\_line1: STRING - address\_line2: STRING - city: STRING - country: STRING - postal\_code: STRING - state: STRING |
| **commercial\_contact**  OBJECT This is a nested data structure:   - cell\_phone\_number: STRING - cell\_phone\_number\_country: STRING - email: STRING - name: STRING - user\_id: INTEGER - work\_phone\_number: STRING - work\_phone\_number\_country: STRING |
| **company\_name**  STRING |
| **corporate\_address**  OBJECT This is a nested data structure:   - address\_line1: STRING - address\_line2: STRING - city: STRING - country: STRING - postal\_code: STRING - state: STRING |
| **currency**  STRING |
| **ein\_ssn\_foreign\_tax\_id**  STRING |
| **financial\_contact**  OBJECT This is a nested data structure:   - cell\_phone\_number: STRING - cell\_phone\_number\_country: STRING - email: STRING - name: STRING - user\_id: INTEGER - work\_phone\_number: STRING - work\_phone\_number\_country: STRING |
| **indirect\_tax\_number**  STRING |
| **industry**  OBJECT This is a nested data structure:   - industry\_id: INTEGER - industry\_name: STRING |
| **minimum\_contact\_rating**  INTEGER |
| **organization\_type**  STRING |
| **primary\_phone\_number**  STRING |
| **primary\_phone\_number\_country**  STRING |
| **registered\_for\_indirect\_tax**  BOOLEAN |
| **secondary\_phone\_number**  STRING |
| **secondary\_phone\_number\_country**  STRING |
| **technical\_contact**  OBJECT This is a nested data structure:   - cell\_phone\_number: STRING - cell\_phone\_number\_country: STRING - email: STRING - name: STRING - user\_id: INTEGER - work\_phone\_number: STRING - work\_phone\_number\_country: STRING |
| **timezone**  STRING |
| **uri**  STRING |
| **website**  STRING |

### contacts

The `contacts` table contains info about a campaign’s contacts.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Impact API method](https://developer.impact.com/default#operations-Contacts-GetContacts "Opens in new tab: Impact API method") |

contacts table foreign keys

| Join contacts with | on |
| --- | --- |
| [action\_inquiries](#action-inquiries) | ``` contacts.campaign_id = action_inquiries.campaign_id ``` |
| [action\_updates](#action-updates) | ``` contacts.campaign_id = action_updates.campaign_id ``` |
| [actions](#actions) | ``` contacts.campaign_id = actions.campaign_id ``` |
| [ads](#ads) | ``` contacts.campaign_id = ads.campaign_id ``` |
| [api\_submissions](#api-submissions) | ``` contacts.campaign_id = api_submissions.campaign_id ``` |
| [campaigns](#campaigns) | ``` contacts.campaign_id = campaigns.id ``` |
| [catalogs](#catalogs) | ``` contacts.campaign_id = catalogs.campaign_id ``` |
| [clicks](#clicks) | ``` contacts.campaign_id = clicks.campaign_id ``` |
| [conversion\_paths](#conversion-paths) | ``` contacts.campaign_id = conversion_paths.campaign_id ``` |
| [deals](#deals) | ``` contacts.campaign_id = deals.campaign_id ``` |
| [exception\_lists](#exception-lists) | ``` contacts.campaign_id = exception_lists.campaign_id ``` |
| [invoices](#invoices) | ``` contacts.campaign_id = invoices.line_items.campaign_id ``` |
| [media\_partner\_groups](#media-partner-groups) | ``` contacts.campaign_id = media_partner_groups.campaign_id ``` |
| [media\_partners](#media-partners) | ``` contacts.campaign_id = media_partners.campaigns.campaign_id ``` |
| [notes](#notes) | ``` contacts.campaign_id = notes.campaign_id ``` |
| [promo\_codes](#promo-codes) | ``` contacts.campaign_id = promo_codes.campaign_id ``` |
| [tracking\_value\_requests](#tracking-value-requests) | ``` contacts.campaign_id = tracking_value_requests.campaign_id ``` |
| [unique\_urls](#unique-urls) | ``` contacts.campaign_id = unique_urls.campaign_id ``` |

contacts table schema

|  |
| --- |
| **accounts**  ARRAY This is a nested data structure:   - id: INTEGER - name: STRING  OBJECT This is a nested data structure.  Click to expand name |
| **campaign\_id**  INTEGER |
| **cellphone\_number**  STRING |
| **cellphone\_number\_country**  STRING |
| **email\_address**  STRING |
| **first\_name**  STRING |
| **id**  STRING |
| **labels**  ARRAY This is a nested data structure. |
| **last\_name**  STRING |
| **profile\_image**  STRING |
| **title**  STRING |
| **uri**  STRING |
| **work\_phone\_number**  INTEGER |
| **work\_phone\_number\_country**  STRING |

### conversion\_paths

The `conversion_paths` table contains info about a campaign’s conversions.

**Note**: Your **Model ID** must be provided [in the integration’s settings](#add-stitch-data-source) to replicate data for this table.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | campaign\_id  customer\_id  model\_id |
| **Useful links** | [Impact API method](https://developer.impact.com/default/documentation/Rest-Adv-v8#operations-Conversion_Paths-GetConversionPaths "Opens in new tab: Impact API method") |

conversion\_paths table foreign keys

| Join conversion\_paths with | on |
| --- | --- |
| [action\_updates](#action-updates) | ``` conversion_paths.events.action_tracker_id = action_updates.action_tracker_id ```  ``` conversion_paths.events.action_id = action_updates.action_id ```  ``` conversion_paths.events.ad_id = action_updates.ad_id ```  ``` conversion_paths.campaign_id = action_updates.campaign_id ```  ``` conversion_paths.customer_id = action_updates.customer_id ``` |
| [actions](#actions) | ``` conversion_paths.events.action_tracker_id = actions.action_tracker_id ```  ``` conversion_paths.events.action_id = actions.id ```  ``` conversion_paths.events.ad_id = actions.ad_id ```  ``` conversion_paths.campaign_id = actions.campaign_id ```  ``` conversion_paths.customer_id = actions.customer_id ``` |
| [api\_submissions](#api-submissions) | ``` conversion_paths.events.action_tracker_id = api_submissions.action_tracker_id ```  ``` conversion_paths.campaign_id = api_submissions.campaign_id ``` |
| [exception\_lists](#exception-lists) | ``` conversion_paths.events.action_tracker_id = exception_lists.action_trackers.id ```  ``` conversion_paths.campaign_id = exception_lists.campaign_id ``` |
| [action\_inquiries](#action-inquiries) | ``` conversion_paths.events.action_id = action_inquiries.action_id ```  ``` conversion_paths.campaign_id = action_inquiries.campaign_id ``` |
| [ads](#ads) | ``` conversion_paths.events.ad_id = ads.id ```  ``` conversion_paths.campaign_id = ads.campaign_id ``` |
| [campaigns](#campaigns) | ``` conversion_paths.campaign_id = campaigns.id ``` |
| [catalogs](#catalogs) | ``` conversion_paths.campaign_id = catalogs.campaign_id ``` |
| [clicks](#clicks) | ``` conversion_paths.campaign_id = clicks.campaign_id ```  ``` conversion_paths.events.media_id = clicks.media_id ``` |
| [contacts](#contacts) | ``` conversion_paths.campaign_id = contacts.campaign_id ``` |
| [deals](#deals) | ``` conversion_paths.campaign_id = deals.campaign_id ``` |
| [invoices](#invoices) | ``` conversion_paths.campaign_id = invoices.line_items.campaign_id ```  ``` conversion_paths.events.media_id = invoices.media_id ``` |
| [media\_partner\_groups](#media-partner-groups) | ``` conversion_paths.campaign_id = media_partner_groups.campaign_id ``` |
| [media\_partners](#media-partners) | ``` conversion_paths.campaign_id = media_partners.campaigns.campaign_id ``` |
| [notes](#notes) | ``` conversion_paths.campaign_id = notes.campaign_id ```  ``` conversion_paths.events.media_id = notes.media_id ``` |
| [promo\_codes](#promo-codes) | ``` conversion_paths.campaign_id = promo_codes.campaign_id ``` |
| [tracking\_value\_requests](#tracking-value-requests) | ``` conversion_paths.campaign_id = tracking_value_requests.campaign_id ``` |
| [unique\_urls](#unique-urls) | ``` conversion_paths.campaign_id = unique_urls.campaign_id ``` |

conversion\_paths table schema

|  |
| --- |
| **campaign\_id**  INTEGER |
| **campaign\_name**  STRING |
| **channel\_count**  INTEGER |
| **cost**  NUMBER |
| **customer\_id**  INTEGER |
| **events**  ARRAY This is a nested data structure:   - action\_date: DATE-TIME - action\_id: STRING - action\_tracker\_id: INTEGER - action\_tracker\_name: STRING - ad\_campaign: STRING - ad\_distribution\_type: STRING - ad\_group: STRING - ad\_id: INTEGER - ad\_name: STRING - ad\_site\_location: STRING - amount: NUMBER - app\_name: STRING - app\_package\_name: STRING - app\_version: STRING - attributed\_credit: NUMBER - attributed\_revenue: NUMBER - browser: STRING - channel: STRING - customer\_area: STRING - customer\_city: STRING - customer\_country: STRING - customer\_post\_code: STRING - customer\_region: STRING - customer\_status: STRING - date\_1: DATE - date\_2: DATE - date\_3: DATE - deal\_name: STRING - deal\_scope: STRING - deal\_type: STRING - device\_family: STRING - device\_type: STRING - event\_date: DATE-TIME - fingerprint: STRING - id: STRING - keyword: STRING - landing\_page: STRING - match\_type: STRING - media\_id: INTEGER - media\_name: STRING - money\_1: NUMBER - money\_2: NUMBER - money\_3: NUMBER - note: STRING - numeric\_1: NUMBER - numeric\_2: NUMBER - numeric\_3: NUMBER - order\_discount: NUMBER - order\_id: STRING - order\_margin: NUMBER - order\_shipping: NUMBER - order\_subtotal: NUMBER - order\_tax: NUMBER - order\_vat: NUMBER - os: STRING - payout: NUMBER - phone\_number: STRING - platform: STRING - position\_type: STRING - profile\_id: STRING - promocode: STRING - referring\_url: STRING - shared\_id: STRING - site\_category: STRING - site\_version: STRING - step: INTEGER - sub\_id\_1: INTEGER - sub\_id\_2: INTEGER - sub\_id\_3: INTEGER - sub\_type: STRING - text\_1: STRING - text\_2: STRING - text\_3: STRING - traffic\_type: STRING - type: STRING |
| **latency**  NUMBER |
| **media\_count**  INTEGER |
| **model\_id**  INTEGER |
| **model\_name**  STRING |
| **referral\_counts**  ARRAY This is a nested data structure:   - count: INTEGER - type: STRING |
| **revenue**  NUMBER |
| **steps**  INTEGER |
| **uri**  STRING |

### deals

The `deals` table contains info about the deals in your Impact account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Impact API method](https://developer.impact.com/default#operations-Deals-GetDeals "Opens in new tab: Impact API method") |

deals table foreign keys

| Join deals with | on |
| --- | --- |
| [action\_inquiries](#action-inquiries) | ``` deals.campaign_id = action_inquiries.campaign_id ``` |
| [action\_updates](#action-updates) | ``` deals.campaign_id = action_updates.campaign_id ``` |
| [actions](#actions) | ``` deals.campaign_id = actions.campaign_id ``` |
| [ads](#ads) | ``` deals.campaign_id = ads.campaign_id ```  ``` deals.id = ads.deal_id ``` |
| [api\_submissions](#api-submissions) | ``` deals.campaign_id = api_submissions.campaign_id ``` |
| [campaigns](#campaigns) | ``` deals.campaign_id = campaigns.id ``` |
| [catalogs](#catalogs) | ``` deals.campaign_id = catalogs.campaign_id ``` |
| [clicks](#clicks) | ``` deals.campaign_id = clicks.campaign_id ``` |
| [contacts](#contacts) | ``` deals.campaign_id = contacts.campaign_id ``` |
| [conversion\_paths](#conversion-paths) | ``` deals.campaign_id = conversion_paths.campaign_id ``` |
| [exception\_lists](#exception-lists) | ``` deals.campaign_id = exception_lists.campaign_id ``` |
| [invoices](#invoices) | ``` deals.campaign_id = invoices.line_items.campaign_id ``` |
| [media\_partner\_groups](#media-partner-groups) | ``` deals.campaign_id = media_partner_groups.campaign_id ``` |
| [media\_partners](#media-partners) | ``` deals.campaign_id = media_partners.campaigns.campaign_id ``` |
| [notes](#notes) | ``` deals.campaign_id = notes.campaign_id ``` |
| [promo\_codes](#promo-codes) | ``` deals.campaign_id = promo_codes.campaign_id ```  ``` deals.id = promo_codes.deal_id ``` |
| [tracking\_value\_requests](#tracking-value-requests) | ``` deals.campaign_id = tracking_value_requests.campaign_id ```  ``` deals.id = tracking_value_requests.deal_id ``` |
| [unique\_urls](#unique-urls) | ``` deals.campaign_id = unique_urls.campaign_id ``` |

deals table schema

|  |
| --- |
| **bogo\_buy\_image\_url**  STRING |
| **bogo\_buy\_name**  STRING |
| **bogo\_buy\_quantity**  STRING |
| **bogo\_buy\_scope**  STRING |
| **bogo\_get\_discount\_amount**  NUMBER |
| **bogo\_get\_discount\_currency**  STRING |
| **bogo\_get\_discount\_percent**  INTEGER |
| **bogo\_get\_discount\_type**  STRING |
| **bogo\_get\_image\_url**  STRING |
| **bogo\_get\_name**  STRING |
| **bogo\_get\_quantity**  STRING |
| **bogo\_get\_scope**  STRING |
| **campaign\_id**  INTEGER |
| **categories**  STRING |
| **default\_promo\_code**  STRING |
| **description**  STRING |
| **discount\_amount**  NUMBER |
| **discount\_currency**  STRING |
| **discount\_maximum\_percent**  INTEGER |
| **discount\_percent**  INTEGER |
| **discount\_percent\_range\_end**  INTEGER |
| **discount\_percent\_range\_start**  INTEGER |
| **discount\_type**  STRING |
| **end\_date**  DATE-TIME |
| **gift**  STRING |
| **id**  INTEGER |
| **maximum\_savings\_amount**  NUMBER |
| **maximum\_savings\_currency**  STRING |
| **minimum\_purchase\_amount**  NUMBER |
| **minimum\_purchase\_amount\_currency**  STRING |
| **name**  STRING |
| **products**  ARRAY This is a nested data structure:   - product\_after\_price\_amount: NUMBER - product\_after\_price\_currency: STRING - product\_before\_price\_amount: NUMBER - product\_before\_price\_currency: STRING - product\_image\_url: STRING - product\_name: STRING |
| **purchase\_limit\_quantity**  STRING |
| **rebate\_amount**  NUMBER |
| **rebate\_currency**  STRING |
| **restricted\_media\_partner\_groups**  ARRAY This is a nested data structure. |
| **restricted\_media\_partners**  ARRAY This is a nested data structure. |
| **scope**  STRING |
| **start\_date**  DATE-TIME |
| **state**  STRING |
| **synch\_ads\_promo\_codes**  STRING |
| **type**  STRING |
| **uri**  STRING |

### exception\_list\_items

The `exception_list_items` table contains info about an exception list’s items.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Impact API method](https://developer.impact.com/default#operations-Exception_Lists-GetExceptionListItems "Opens in new tab: Impact API method") |

exception\_list\_items table foreign keys

| Join exception\_list\_items with | on |
| --- | --- |
| [exception\_lists](#exception-lists) | ``` exception_list_items.list_id = exception_lists.id ``` |

exception\_list\_items table schema

|  |
| --- |
| **created\_date**  DATE-TIME |
| **id**  INTEGER |
| **list\_id**  INTEGER |
| **match\_mode**  STRING |
| **name**  STRING |
| **uri**  STRING |
| **value**  STRING |

### exception\_lists

The `exception_lists` table contains info about exception lists.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Impact API method](https://developer.impact.com/default#operations-Exception_Lists-GetExceptionLists "Opens in new tab: Impact API method") |

exception\_lists table foreign keys

| Join exception\_lists with | on |
| --- | --- |
| [action\_updates](#action-updates) | ``` exception_lists.action_trackers.id = action_updates.action_tracker_id ```  ``` exception_lists.campaign_id = action_updates.campaign_id ``` |
| [actions](#actions) | ``` exception_lists.action_trackers.id = actions.action_tracker_id ```  ``` exception_lists.campaign_id = actions.campaign_id ``` |
| [api\_submissions](#api-submissions) | ``` exception_lists.action_trackers.id = api_submissions.action_tracker_id ```  ``` exception_lists.campaign_id = api_submissions.campaign_id ``` |
| [conversion\_paths](#conversion-paths) | ``` exception_lists.action_trackers.id = conversion_paths.events.action_tracker_id ```  ``` exception_lists.campaign_id = conversion_paths.campaign_id ``` |
| [action\_inquiries](#action-inquiries) | ``` exception_lists.campaign_id = action_inquiries.campaign_id ``` |
| [ads](#ads) | ``` exception_lists.campaign_id = ads.campaign_id ``` |
| [campaigns](#campaigns) | ``` exception_lists.campaign_id = campaigns.id ``` |
| [catalogs](#catalogs) | ``` exception_lists.campaign_id = catalogs.campaign_id ``` |
| [clicks](#clicks) | ``` exception_lists.campaign_id = clicks.campaign_id ``` |
| [contacts](#contacts) | ``` exception_lists.campaign_id = contacts.campaign_id ``` |
| [deals](#deals) | ``` exception_lists.campaign_id = deals.campaign_id ``` |
| [invoices](#invoices) | ``` exception_lists.campaign_id = invoices.line_items.campaign_id ``` |
| [media\_partner\_groups](#media-partner-groups) | ``` exception_lists.campaign_id = media_partner_groups.campaign_id ``` |
| [media\_partners](#media-partners) | ``` exception_lists.campaign_id = media_partners.campaigns.campaign_id ``` |
| [notes](#notes) | ``` exception_lists.campaign_id = notes.campaign_id ``` |
| [promo\_codes](#promo-codes) | ``` exception_lists.campaign_id = promo_codes.campaign_id ``` |
| [tracking\_value\_requests](#tracking-value-requests) | ``` exception_lists.campaign_id = tracking_value_requests.campaign_id ``` |
| [unique\_urls](#unique-urls) | ``` exception_lists.campaign_id = unique_urls.campaign_id ``` |
| [exception\_list\_items](#exception-list-items) | ``` exception_lists.id = exception_list_items.list_id ``` |

exception\_lists table schema

|  |
| --- |
| **action\_trackers**  ARRAY This is a nested data structure:   - id: INTEGER - name: STRING |
| **campaign\_id**  INTEGER |
| **created\_date**  DATE-TIME |
| **deactivation\_date**  DATE-TIME |
| **id**  INTEGER |
| **items\_uri**  STRING |
| **name**  STRING |
| **number\_of\_items**  INTEGER |
| **state**  STRING |
| **type**  STRING |
| **uri**  STRING |

### ftp\_file\_submissions

The `ftp_file_submissions` table contains info about FTP file submissions.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | batch\_id |
| **Replication Key** | submission\_date |
| **Useful links** | [Impact API method](https://developer.impact.com/default#operations-FTP_File_Submissions-GetFTPFileSubmissions "Opens in new tab: Impact API method") |

ftp\_file\_submissions table foreign keys

| Join ftp\_file\_submissions with | on |
| --- | --- |
| [api\_submissions](#api-submissions) | ``` ftp_file_submissions.account_id = api_submissions.account_id ``` |

ftp\_file\_submissions table schema

|  |
| --- |
| **account\_id**  INTEGER |
| **batch\_id**  STRING |
| **completion\_date**  DATE-TIME |
| **errors\_uri**  STRING |
| **file\_name**  STRING |
| **status**  STRING |
| **submission\_date**  DATE-TIME |
| **total\_errors**  STRING |
| **total\_records**  INTEGER |
| **type**  STRING |
| **uri**  STRING |

### invoices

The `invoices` table contains info about the invoices in your Impact account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | created\_date |
| **Useful links** | [Impact API method](https://developer.impact.com/default#operations-Invoices-GetInvoices "Opens in new tab: Impact API method") |

invoices table foreign keys

| Join invoices with | on |
| --- | --- |
| [action\_inquiries](#action-inquiries) | ``` invoices.line_items.campaign_id = action_inquiries.campaign_id ``` |
| [action\_updates](#action-updates) | ``` invoices.line_items.campaign_id = action_updates.campaign_id ``` |
| [actions](#actions) | ``` invoices.line_items.campaign_id = actions.campaign_id ``` |
| [ads](#ads) | ``` invoices.line_items.campaign_id = ads.campaign_id ``` |
| [api\_submissions](#api-submissions) | ``` invoices.line_items.campaign_id = api_submissions.campaign_id ``` |
| [campaigns](#campaigns) | ``` invoices.line_items.campaign_id = campaigns.id ``` |
| [catalogs](#catalogs) | ``` invoices.line_items.campaign_id = catalogs.campaign_id ``` |
| [clicks](#clicks) | ``` invoices.line_items.campaign_id = clicks.campaign_id ```  ``` invoices.media_id = clicks.media_id ``` |
| [contacts](#contacts) | ``` invoices.line_items.campaign_id = contacts.campaign_id ``` |
| [conversion\_paths](#conversion-paths) | ``` invoices.line_items.campaign_id = conversion_paths.campaign_id ```  ``` invoices.media_id = conversion_paths.events.media_id ``` |
| [deals](#deals) | ``` invoices.line_items.campaign_id = deals.campaign_id ``` |
| [exception\_lists](#exception-lists) | ``` invoices.line_items.campaign_id = exception_lists.campaign_id ``` |
| [media\_partner\_groups](#media-partner-groups) | ``` invoices.line_items.campaign_id = media_partner_groups.campaign_id ``` |
| [media\_partners](#media-partners) | ``` invoices.line_items.campaign_id = media_partners.campaigns.campaign_id ``` |
| [notes](#notes) | ``` invoices.line_items.campaign_id = notes.campaign_id ```  ``` invoices.media_id = notes.media_id ``` |
| [promo\_codes](#promo-codes) | ``` invoices.line_items.campaign_id = promo_codes.campaign_id ``` |
| [tracking\_value\_requests](#tracking-value-requests) | ``` invoices.line_items.campaign_id = tracking_value_requests.campaign_id ``` |
| [unique\_urls](#unique-urls) | ``` invoices.line_items.campaign_id = unique_urls.campaign_id ``` |

invoices table schema

|  |
| --- |
| **created\_date**  DATE-TIME |
| **currency**  STRING |
| **id**  STRING |
| **line\_items**  ARRAY This is a nested data structure:   - actions: INTEGER - campaign\_id: INTEGER - campaign\_name: STRING - description: STRING - due\_date: DATE-TIME - event\_month\_year: STRING - net\_item\_amount: NUMBER - paid\_date: DATE-TIME - status: STRING - total\_item\_amount: NUMBER - vat\_item\_amount: NUMBER |
| **media\_id**  INTEGER |
| **media\_name**  STRING |
| **pdf**  STRING |
| **total\_amount**  NUMBER |
| **total\_vat\_amount**  NUMBER |

### media\_partner\_groups

The `media_partner_groups` table contains info about a campaign’s media partner groups.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Impact API method](https://developer.impact.com/default#operations-Partner_Groups-GetMediaPartnerGroups "Opens in new tab: Impact API method") |

media\_partner\_groups table foreign keys

| Join media\_partner\_groups with | on |
| --- | --- |
| [action\_inquiries](#action-inquiries) | ``` media_partner_groups.campaign_id = action_inquiries.campaign_id ```  ``` media_partner_groups.media_partners.partner_id = action_inquiries.media_partner_id ``` |
| [action\_updates](#action-updates) | ``` media_partner_groups.campaign_id = action_updates.campaign_id ```  ``` media_partner_groups.media_partners.partner_id = action_updates.media_partner_id ``` |
| [actions](#actions) | ``` media_partner_groups.campaign_id = actions.campaign_id ```  ``` media_partner_groups.media_partners.partner_id = actions.media_partner_id ``` |
| [ads](#ads) | ``` media_partner_groups.campaign_id = ads.campaign_id ``` |
| [api\_submissions](#api-submissions) | ``` media_partner_groups.campaign_id = api_submissions.campaign_id ```  ``` media_partner_groups.media_partners.partner_id = api_submissions.media_partner_id ``` |
| [campaigns](#campaigns) | ``` media_partner_groups.campaign_id = campaigns.id ``` |
| [catalogs](#catalogs) | ``` media_partner_groups.campaign_id = catalogs.campaign_id ``` |
| [clicks](#clicks) | ``` media_partner_groups.campaign_id = clicks.campaign_id ``` |
| [contacts](#contacts) | ``` media_partner_groups.campaign_id = contacts.campaign_id ``` |
| [conversion\_paths](#conversion-paths) | ``` media_partner_groups.campaign_id = conversion_paths.campaign_id ``` |
| [deals](#deals) | ``` media_partner_groups.campaign_id = deals.campaign_id ``` |
| [exception\_lists](#exception-lists) | ``` media_partner_groups.campaign_id = exception_lists.campaign_id ``` |
| [invoices](#invoices) | ``` media_partner_groups.campaign_id = invoices.line_items.campaign_id ``` |
| [media\_partners](#media-partners) | ``` media_partner_groups.campaign_id = media_partners.campaigns.campaign_id ```  ``` media_partner_groups.id = media_partners.groups.group_id ```  ``` media_partner_groups.media_partners.partner_id = media_partners.id ``` |
| [notes](#notes) | ``` media_partner_groups.campaign_id = notes.campaign_id ``` |
| [promo\_codes](#promo-codes) | ``` media_partner_groups.campaign_id = promo_codes.campaign_id ``` |
| [tracking\_value\_requests](#tracking-value-requests) | ``` media_partner_groups.campaign_id = tracking_value_requests.campaign_id ```  ``` media_partner_groups.media_partners.partner_id = tracking_value_requests.media_partner_id ``` |
| [unique\_urls](#unique-urls) | ``` media_partner_groups.campaign_id = unique_urls.campaign_id ```  ``` media_partner_groups.media_partners.partner_id = unique_urls.media_partner_id ``` |

media\_partner\_groups table schema

|  |
| --- |
| **campaign\_id**  INTEGER |
| **id**  INTEGER |
| **media\_partners**  ARRAY This is a nested data structure:   - partner\_id: INTEGER - partner\_name: STRING - partner\_uri: STRING |
| **name**  STRING |
| **uri**  STRING |

### media\_partners

The `media_partners` table contains info about the media partners in your Impact account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Impact API method](https://developer.impact.com/default#operations-Partners-GetMediaPartners "Opens in new tab: Impact API method") |

media\_partners table foreign keys

| Join media\_partners with | on |
| --- | --- |
| [action\_inquiries](#action-inquiries) | ``` media_partners.campaigns.campaign_id = action_inquiries.campaign_id ```  ``` media_partners.id = action_inquiries.media_partner_id ``` |
| [action\_updates](#action-updates) | ``` media_partners.campaigns.campaign_id = action_updates.campaign_id ```  ``` media_partners.id = action_updates.media_partner_id ``` |
| [actions](#actions) | ``` media_partners.campaigns.campaign_id = actions.campaign_id ```  ``` media_partners.id = actions.media_partner_id ``` |
| [ads](#ads) | ``` media_partners.campaigns.campaign_id = ads.campaign_id ``` |
| [api\_submissions](#api-submissions) | ``` media_partners.campaigns.campaign_id = api_submissions.campaign_id ```  ``` media_partners.id = api_submissions.media_partner_id ``` |
| [campaigns](#campaigns) | ``` media_partners.campaigns.campaign_id = campaigns.id ``` |
| [catalogs](#catalogs) | ``` media_partners.campaigns.campaign_id = catalogs.campaign_id ``` |
| [clicks](#clicks) | ``` media_partners.campaigns.campaign_id = clicks.campaign_id ``` |
| [contacts](#contacts) | ``` media_partners.campaigns.campaign_id = contacts.campaign_id ``` |
| [conversion\_paths](#conversion-paths) | ``` media_partners.campaigns.campaign_id = conversion_paths.campaign_id ``` |
| [deals](#deals) | ``` media_partners.campaigns.campaign_id = deals.campaign_id ``` |
| [exception\_lists](#exception-lists) | ``` media_partners.campaigns.campaign_id = exception_lists.campaign_id ``` |
| [invoices](#invoices) | ``` media_partners.campaigns.campaign_id = invoices.line_items.campaign_id ``` |
| [media\_partner\_groups](#media-partner-groups) | ``` media_partners.campaigns.campaign_id = media_partner_groups.campaign_id ```  ``` media_partners.groups.group_id = media_partner_groups.id ```  ``` media_partners.id = media_partner_groups.media_partners.partner_id ``` |
| [notes](#notes) | ``` media_partners.campaigns.campaign_id = notes.campaign_id ``` |
| [promo\_codes](#promo-codes) | ``` media_partners.campaigns.campaign_id = promo_codes.campaign_id ``` |
| [tracking\_value\_requests](#tracking-value-requests) | ``` media_partners.campaigns.campaign_id = tracking_value_requests.campaign_id ```  ``` media_partners.id = tracking_value_requests.media_partner_id ``` |
| [unique\_urls](#unique-urls) | ``` media_partners.campaigns.campaign_id = unique_urls.campaign_id ```  ``` media_partners.id = unique_urls.media_partner_id ``` |

media\_partners table schema

|  |
| --- |
| **address\_line1**  STRING |
| **address\_line2**  STRING |
| **campaigns**  ARRAY This is a nested data structure:   - campaign\_id: INTEGER - campaign\_name: STRING - insertion\_order\_id: INTEGER - insertion\_order\_name: STRING - join\_date: DATE-TIME |
| **city**  STRING |
| **contact**  OBJECT This is a nested data structure:   - email\_address: STRING - first\_name: STRING - last\_name: STRING - phone\_number: STRING |
| **country**  STRING |
| **country\_state**  STRING |
| **currency**  STRING |
| **date\_created**  DATE-TIME |
| **description**  STRING |
| **groups**  ARRAY This is a nested data structure:   - group\_id: INTEGER - group\_name: STRING |
| **id**  INTEGER |
| **mp\_value1**  STRING |
| **mp\_value2**  STRING |
| **mp\_value3**  STRING |
| **name**  STRING |
| **partner\_type**  STRING |
| **phone\_number**  STRING |
| **postal\_code**  STRING |
| **primary\_promotional\_method**  STRING |
| **promoting\_countries**  STRING |
| **promotional\_methods**  STRING |
| **rating**  INTEGER |
| **relationship\_state**  STRING |
| **state**  STRING |
| **timezone**  STRING |
| **uri**  STRING |
| **website**  STRING |

### notes

The `notes` table contains info about a campaign’s notes.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | modification\_date |
| **Useful links** | [Impact API method](https://developer.impact.com/default#operations-Notes-GetNotes "Opens in new tab: Impact API method") |

notes table foreign keys

| Join notes with | on |
| --- | --- |
| [action\_inquiries](#action-inquiries) | ``` notes.campaign_id = action_inquiries.campaign_id ``` |
| [action\_updates](#action-updates) | ``` notes.campaign_id = action_updates.campaign_id ``` |
| [actions](#actions) | ``` notes.campaign_id = actions.campaign_id ``` |
| [ads](#ads) | ``` notes.campaign_id = ads.campaign_id ``` |
| [api\_submissions](#api-submissions) | ``` notes.campaign_id = api_submissions.campaign_id ``` |
| [campaigns](#campaigns) | ``` notes.campaign_id = campaigns.id ``` |
| [catalogs](#catalogs) | ``` notes.campaign_id = catalogs.campaign_id ``` |
| [clicks](#clicks) | ``` notes.campaign_id = clicks.campaign_id ```  ``` notes.media_id = clicks.media_id ``` |
| [contacts](#contacts) | ``` notes.campaign_id = contacts.campaign_id ``` |
| [conversion\_paths](#conversion-paths) | ``` notes.campaign_id = conversion_paths.campaign_id ```  ``` notes.media_id = conversion_paths.events.media_id ``` |
| [deals](#deals) | ``` notes.campaign_id = deals.campaign_id ``` |
| [exception\_lists](#exception-lists) | ``` notes.campaign_id = exception_lists.campaign_id ``` |
| [invoices](#invoices) | ``` notes.campaign_id = invoices.line_items.campaign_id ```  ``` notes.media_id = invoices.media_id ``` |
| [media\_partner\_groups](#media-partner-groups) | ``` notes.campaign_id = media_partner_groups.campaign_id ``` |
| [media\_partners](#media-partners) | ``` notes.campaign_id = media_partners.campaigns.campaign_id ``` |
| [promo\_codes](#promo-codes) | ``` notes.campaign_id = promo_codes.campaign_id ``` |
| [tracking\_value\_requests](#tracking-value-requests) | ``` notes.campaign_id = tracking_value_requests.campaign_id ``` |
| [unique\_urls](#unique-urls) | ``` notes.campaign_id = unique_urls.campaign_id ``` |

notes table schema

|  |
| --- |
| **attachments**  ARRAY This is a nested data structure. |
| **campaign\_id**  INTEGER |
| **content**  STRING |
| **creation\_date**  STRING |
| **creator**  STRING |
| **id**  INTEGER |
| **media\_id**  INTEGER |
| **media\_name**  STRING |
| **modification\_date**  DATE-TIME |
| **type**  STRING |
| **uri**  STRING |

### phone\_numbers

The `phone_numbers` table contains info about phone numbers.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Impact API method](https://developer.impact.com/default#operations-Phone_Numbers-GetPhoneNumbers "Opens in new tab: Impact API method") |

phone\_numbers table foreign keys

| Join phone\_numbers with | on |
| --- | --- |
| [tracking\_value\_requests](#tracking-value-requests) | ``` phone_numbers.id = tracking_value_requests.phone_numbers.id ``` |

phone\_numbers table schema

|  |
| --- |
| **country**  STRING |
| **date\_created**  DATE-TIME |
| **id**  INTEGER |
| **international\_number**  STRING |
| **last\_date\_assigned**  DATE-TIME |
| **last\_date\_released**  DATE-TIME |
| **number**  STRING |
| **uri**  STRING |

### promo\_codes

The `promo_codes` table contains info about promo codes.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Impact API method](https://developer.impact.com/default#operations-Promo_Codes-GetPromoCodes "Opens in new tab: Impact API method") |

promo\_codes table foreign keys

| Join promo\_codes with | on |
| --- | --- |
| [action\_inquiries](#action-inquiries) | ``` promo_codes.campaign_id = action_inquiries.campaign_id ``` |
| [action\_updates](#action-updates) | ``` promo_codes.campaign_id = action_updates.campaign_id ``` |
| [actions](#actions) | ``` promo_codes.campaign_id = actions.campaign_id ``` |
| [ads](#ads) | ``` promo_codes.campaign_id = ads.campaign_id ```  ``` promo_codes.deal_id = ads.deal_id ``` |
| [api\_submissions](#api-submissions) | ``` promo_codes.campaign_id = api_submissions.campaign_id ``` |
| [campaigns](#campaigns) | ``` promo_codes.campaign_id = campaigns.id ``` |
| [catalogs](#catalogs) | ``` promo_codes.campaign_id = catalogs.campaign_id ``` |
| [clicks](#clicks) | ``` promo_codes.campaign_id = clicks.campaign_id ``` |
| [contacts](#contacts) | ``` promo_codes.campaign_id = contacts.campaign_id ``` |
| [conversion\_paths](#conversion-paths) | ``` promo_codes.campaign_id = conversion_paths.campaign_id ``` |
| [deals](#deals) | ``` promo_codes.campaign_id = deals.campaign_id ```  ``` promo_codes.deal_id = deals.id ``` |
| [exception\_lists](#exception-lists) | ``` promo_codes.campaign_id = exception_lists.campaign_id ``` |
| [invoices](#invoices) | ``` promo_codes.campaign_id = invoices.line_items.campaign_id ``` |
| [media\_partner\_groups](#media-partner-groups) | ``` promo_codes.campaign_id = media_partner_groups.campaign_id ``` |
| [media\_partners](#media-partners) | ``` promo_codes.campaign_id = media_partners.campaigns.campaign_id ``` |
| [notes](#notes) | ``` promo_codes.campaign_id = notes.campaign_id ``` |
| [tracking\_value\_requests](#tracking-value-requests) | ``` promo_codes.campaign_id = tracking_value_requests.campaign_id ```  ``` promo_codes.deal_id = tracking_value_requests.deal_id ```  ``` promo_codes.id = tracking_value_requests.promo_codes.id ``` |
| [unique\_urls](#unique-urls) | ``` promo_codes.campaign_id = unique_urls.campaign_id ``` |

promo\_codes table schema

|  |
| --- |
| **assigned\_partner\_id**  INTEGER |
| **assigned\_partner\_name**  STRING |
| **bogo\_buy\_image\_url**  STRING |
| **bogo\_buy\_name**  STRING |
| **bogo\_buy\_quantity**  STRING |
| **bogo\_buy\_scope**  STRING |
| **bogo\_get\_discount\_amount**  NUMBER |
| **bogo\_get\_discount\_currency**  STRING |
| **bogo\_get\_discount\_percent**  INTEGER |
| **bogo\_get\_discount\_type**  STRING |
| **bogo\_get\_image\_url**  STRING |
| **bogo\_get\_name**  STRING |
| **bogo\_get\_quantity**  STRING |
| **bogo\_get\_scope**  STRING |
| **campaign\_id**  INTEGER |
| **campaign\_name**  STRING |
| **code**  STRING |
| **created\_date**  DATE-TIME |
| **credit\_policy**  STRING |
| **deal\_categories**  STRING |
| **deal\_default\_promo\_code**  STRING |
| **deal\_description**  STRING |
| **deal\_end\_date**  DATE-TIME |
| **deal\_id**  STRING |
| **deal\_name**  STRING |
| **deal\_products**  ARRAY This is a nested data structure:   - product\_after\_price\_amount: NUMBER - product\_after\_price\_currency: STRING - product\_before\_price\_amount: NUMBER - product\_before\_price\_currency: STRING - product\_image\_url: STRING - product\_name: STRING |
| **deal\_restricted\_media\_partner\_groups**  ARRAY This is a nested data structure. |
| **deal\_restricted\_media\_partners**  ARRAY This is a nested data structure. |
| **deal\_scope**  STRING |
| **deal\_start\_date**  DATE-TIME |
| **deal\_state**  STRING |
| **deal\_type**  STRING |
| **discount\_amount**  NUMBER |
| **discount\_currency**  STRING |
| **discount\_maximum\_percent**  INTEGER |
| **discount\_percent**  INTEGER |
| **discount\_percent\_range\_end**  INTEGER |
| **discount\_percent\_range\_start**  INTEGER |
| **discount\_type**  STRING |
| **end\_date**  DATE-TIME |
| **gift**  STRING |
| **id**  INTEGER |
| **maximum\_savings\_amount**  NUMBER |
| **maximum\_savings\_currency**  STRING |
| **minimum\_purchase\_amount**  NUMBER |
| **minimum\_purchase\_amount\_currency**  STRING |
| **purchase\_limit\_quantity**  STRING |
| **rebate\_amount**  NUMBER |
| **rebate\_currency**  STRING |
| **start\_date**  DATE-TIME |
| **state**  STRING |
| **synch\_ads\_promo\_codes**  STRING |
| **type**  STRING |
| **uri**  STRING |

### report\_metadata

The `report_metadata` table contains info about metadata associated with reports.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Impact API method](https://developer.impact.com/default/documentation/Rest-Adv-v8#operations-Reports-GetReportMetadata "Opens in new tab: Impact API method") |

report\_metadata table foreign keys

| Join report\_metadata with | on |
| --- | --- |
| [reports](#reports) | ``` report_metadata.id = reports.id ``` |

report\_metadata table schema

|  |
| --- |
| **attributes**  ARRAY This is a nested data structure:   - data\_type: STRING - description: STRING - name: STRING |
| **description**  STRING |
| **filters**  ARRAY This is a nested data structure:   - data\_type: STRING - format: STRING - name: STRING |
| **id**  STRING |
| **name**  STRING |
| **run\_uri**  STRING |
| **uri**  STRING |

### reports

The `reports` table contains info about the reports in your Impact account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Impact API method](https://developer.impact.com/default#operations-Reports-ListReports "Opens in new tab: Impact API method") |

reports table foreign keys

| Join reports with | on |
| --- | --- |
| [report\_metadata](#report-metadata) | ``` reports.id = report_metadata.id ``` |

reports table schema

|  |
| --- |
| **description**  STRING |
| **id**  STRING |
| **meta\_data\_uri**  STRING |
| **name**  STRING |
| **run\_uri**  STRING |

### tracking\_value\_requests

The `tracking_value_requests` table contains info about tracking value requests.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Impact API method](https://developer.impact.com/default#operations-Tracking_Value_Requests-GetTrackingValueRequests "Opens in new tab: Impact API method") |

tracking\_value\_requests table foreign keys

| Join tracking\_value\_requests with | on |
| --- | --- |
| [action\_inquiries](#action-inquiries) | ``` tracking_value_requests.campaign_id = action_inquiries.campaign_id ```  ``` tracking_value_requests.media_partner_id = action_inquiries.media_partner_id ``` |
| [action\_updates](#action-updates) | ``` tracking_value_requests.campaign_id = action_updates.campaign_id ```  ``` tracking_value_requests.media_partner_id = action_updates.media_partner_id ``` |
| [actions](#actions) | ``` tracking_value_requests.campaign_id = actions.campaign_id ```  ``` tracking_value_requests.media_partner_id = actions.media_partner_id ``` |
| [ads](#ads) | ``` tracking_value_requests.campaign_id = ads.campaign_id ```  ``` tracking_value_requests.deal_id = ads.deal_id ``` |
| [api\_submissions](#api-submissions) | ``` tracking_value_requests.campaign_id = api_submissions.campaign_id ```  ``` tracking_value_requests.media_partner_id = api_submissions.media_partner_id ``` |
| [campaigns](#campaigns) | ``` tracking_value_requests.campaign_id = campaigns.id ``` |
| [catalogs](#catalogs) | ``` tracking_value_requests.campaign_id = catalogs.campaign_id ``` |
| [clicks](#clicks) | ``` tracking_value_requests.campaign_id = clicks.campaign_id ``` |
| [contacts](#contacts) | ``` tracking_value_requests.campaign_id = contacts.campaign_id ``` |
| [conversion\_paths](#conversion-paths) | ``` tracking_value_requests.campaign_id = conversion_paths.campaign_id ``` |
| [deals](#deals) | ``` tracking_value_requests.campaign_id = deals.campaign_id ```  ``` tracking_value_requests.deal_id = deals.id ``` |
| [exception\_lists](#exception-lists) | ``` tracking_value_requests.campaign_id = exception_lists.campaign_id ``` |
| [invoices](#invoices) | ``` tracking_value_requests.campaign_id = invoices.line_items.campaign_id ``` |
| [media\_partner\_groups](#media-partner-groups) | ``` tracking_value_requests.campaign_id = media_partner_groups.campaign_id ```  ``` tracking_value_requests.media_partner_id = media_partner_groups.media_partners.partner_id ``` |
| [media\_partners](#media-partners) | ``` tracking_value_requests.campaign_id = media_partners.campaigns.campaign_id ```  ``` tracking_value_requests.media_partner_id = media_partners.id ``` |
| [notes](#notes) | ``` tracking_value_requests.campaign_id = notes.campaign_id ``` |
| [promo\_codes](#promo-codes) | ``` tracking_value_requests.campaign_id = promo_codes.campaign_id ```  ``` tracking_value_requests.deal_id = promo_codes.deal_id ```  ``` tracking_value_requests.promo_codes.id = promo_codes.id ``` |
| [unique\_urls](#unique-urls) | ``` tracking_value_requests.campaign_id = unique_urls.campaign_id ```  ``` tracking_value_requests.media_partner_id = unique_urls.media_partner_id ```  ``` tracking_value_requests.unique_urls.id = unique_urls.id ``` |
| [phone\_numbers](#phone-numbers) | ``` tracking_value_requests.phone_numbers.id = phone_numbers.id ``` |

tracking\_value\_requests table schema

|  |
| --- |
| **additional\_instructions**  STRING |
| **bogo\_buy\_image\_url**  STRING |
| **bogo\_buy\_name**  STRING |
| **bogo\_buy\_quantity**  STRING |
| **bogo\_buy\_scope**  STRING |
| **bogo\_get\_discount\_amount**  NUMBER |
| **bogo\_get\_discount\_currency**  STRING |
| **bogo\_get\_discount\_percent**  INTEGER |
| **bogo\_get\_discount\_type**  STRING |
| **bogo\_get\_image\_url**  STRING |
| **bogo\_get\_name**  STRING |
| **bogo\_get\_quantity**  STRING |
| **bogo\_get\_scope**  STRING |
| **campaign\_id**  INTEGER |
| **campaign\_name**  STRING |
| **date\_completed**  DATE-TIME |
| **date\_needed**  DATE-TIME |
| **date\_placed**  DATE-TIME |
| **deal\_categories**  STRING |
| **deal\_default\_promo\_code**  STRING |
| **deal\_description**  STRING |
| **deal\_end\_date**  DATE-TIME |
| **deal\_id**  STRING |
| **deal\_name**  STRING |
| **deal\_products**  ARRAY This is a nested data structure:   - product\_after\_price\_amount: NUMBER - product\_after\_price\_currency: STRING - product\_before\_price\_amount: NUMBER - product\_before\_price\_currency: STRING - product\_image\_url: STRING - product\_name: STRING |
| **deal\_restricted\_media\_partner\_groups**  ARRAY This is a nested data structure. |
| **deal\_restricted\_media\_partners**  ARRAY This is a nested data structure. |
| **deal\_scope**  STRING |
| **deal\_start\_date**  DATE-TIME |
| **deal\_state**  STRING |
| **deal\_type**  STRING |
| **discount\_amount**  NUMBER |
| **discount\_currency**  STRING |
| **discount\_maximum\_percent**  INTEGER |
| **discount\_percent**  INTEGER |
| **discount\_percent\_range\_end**  INTEGER |
| **discount\_percent\_range\_start**  INTEGER |
| **discount\_type**  STRING |
| **gift**  STRING |
| **id**  INTEGER |
| **maximum\_savings\_amount**  NUMBER |
| **maximum\_savings\_currency**  STRING |
| **media\_partner\_id**  INTEGER |
| **media\_partner\_name**  STRING |
| **minimum\_purchase\_amount**  NUMBER |
| **minimum\_purchase\_amount\_currency**  STRING |
| **number\_requested**  INTEGER |
| **phone\_numbers**  ARRAY This is a nested data structure:   - assigned\_phone\_number: STRING - assigned\_phone\_number\_id: INTEGER - id: INTEGER |
| **processing\_comments**  STRING |
| **promo\_codes**  ARRAY This is a nested data structure:   - approved\_code: STRING - credit\_policy: STRING - id: INTEGER - match\_mode: STRING - requested\_code: STRING |
| **purchase\_limit\_quantity**  STRING |
| **rebate\_amount**  NUMBER |
| **rebate\_currency**  STRING |
| **request\_type**  STRING |
| **state**  STRING |
| **synch\_ads\_promo\_codes**  STRING |
| **unique\_urls**  ARRAY This is a nested data structure:   - id: INTEGER - url: STRING - url\_id: INTEGER |
| **uri**  STRING |

### unique\_urls

The `unique_urls` table contains info about unique URLs.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Impact API method](https://developer.impact.com/default#operations-Unique_Urls-GetUniqueUrls "Opens in new tab: Impact API method") |

unique\_urls table foreign keys

| Join unique\_urls with | on |
| --- | --- |
| [action\_inquiries](#action-inquiries) | ``` unique_urls.campaign_id = action_inquiries.campaign_id ```  ``` unique_urls.media_partner_id = action_inquiries.media_partner_id ``` |
| [action\_updates](#action-updates) | ``` unique_urls.campaign_id = action_updates.campaign_id ```  ``` unique_urls.media_partner_id = action_updates.media_partner_id ``` |
| [actions](#actions) | ``` unique_urls.campaign_id = actions.campaign_id ```  ``` unique_urls.media_partner_id = actions.media_partner_id ``` |
| [ads](#ads) | ``` unique_urls.campaign_id = ads.campaign_id ``` |
| [api\_submissions](#api-submissions) | ``` unique_urls.campaign_id = api_submissions.campaign_id ```  ``` unique_urls.media_partner_id = api_submissions.media_partner_id ``` |
| [campaigns](#campaigns) | ``` unique_urls.campaign_id = campaigns.id ``` |
| [catalogs](#catalogs) | ``` unique_urls.campaign_id = catalogs.campaign_id ``` |
| [clicks](#clicks) | ``` unique_urls.campaign_id = clicks.campaign_id ``` |
| [contacts](#contacts) | ``` unique_urls.campaign_id = contacts.campaign_id ``` |
| [conversion\_paths](#conversion-paths) | ``` unique_urls.campaign_id = conversion_paths.campaign_id ``` |
| [deals](#deals) | ``` unique_urls.campaign_id = deals.campaign_id ``` |
| [exception\_lists](#exception-lists) | ``` unique_urls.campaign_id = exception_lists.campaign_id ``` |
| [invoices](#invoices) | ``` unique_urls.campaign_id = invoices.line_items.campaign_id ``` |
| [media\_partner\_groups](#media-partner-groups) | ``` unique_urls.campaign_id = media_partner_groups.campaign_id ```  ``` unique_urls.media_partner_id = media_partner_groups.media_partners.partner_id ``` |
| [media\_partners](#media-partners) | ``` unique_urls.campaign_id = media_partners.campaigns.campaign_id ```  ``` unique_urls.media_partner_id = media_partners.id ``` |
| [notes](#notes) | ``` unique_urls.campaign_id = notes.campaign_id ``` |
| [promo\_codes](#promo-codes) | ``` unique_urls.campaign_id = promo_codes.campaign_id ``` |
| [tracking\_value\_requests](#tracking-value-requests) | ``` unique_urls.campaign_id = tracking_value_requests.campaign_id ```  ``` unique_urls.media_partner_id = tracking_value_requests.media_partner_id ```  ``` unique_urls.id = tracking_value_requests.unique_urls.id ``` |

unique\_urls table schema

|  |
| --- |
| **campaign\_id**  INTEGER |
| **campaign\_name**  STRING |
| **date\_created**  DATE-TIME |
| **date\_last\_assigned**  DATE-TIME |
| **date\_last\_released**  DATE-TIME |
| **id**  INTEGER |
| **landing\_page**  STRING |
| **media\_partner\_id**  INTEGER |
| **media\_partner\_name**  STRING |
| **state**  STRING |
| **uri**  STRING |
| **url**  STRING |
