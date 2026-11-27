---
title: "Mailchimp"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Mailchimp.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Mailchimp

Mailchimp is an email and marketing automation platform for growing businesses.

MailChimp integration replicates data using the [MailChimp API 3.0](https://developer.mailchimp.com/documentation/mailchimp/reference/overview/).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To obtain your client ID and secret:

1. Log into your [Mailchimp](https://us1.admin.mailchimp.com/account/oauth2/) account.
2. Either:
   - Create a new app. The client ID and secret are displayed when the app is created.

     As the client secret is displayed only once, copy and paste it to a secured file.
   - Edit an existing app and click Rotate to generate a new client secret.
3. Make sure Authorized Redirect URIs is set to https://connector.qlik.com/auth/oauth/v3.htm.

   Each OAuth app can only have one redirect URI.

Use a unique set of client id and client secret to authenticate each of your connections. Otherwise, your tasks associated with your older connections will fail.

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
| Email Activity Date Window | Enter the number of days for which you need to retrieve the email activity reports. Example: 10. The reports of the last 10 days will be retrieved. |
| Client ID | Client ID. |
| Client Secret | Client secret. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### automations

The `automations` table contains summary info about your MailChimp account’s automations. In MailChimp, an automation is a feature that sends a series of emails to subscribers when triggered by a specific date, activity, or event.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Replication Key** | create\_time |
| **Useful links** | [MailChimp API method](https://developer.mailchimp.com/documentation/mailchimp/reference/automations/#read-get_automations "Opens in new tab: MailChimp API method") |

automations table foreign keys

| Join automations with | on |
| --- | --- |
| [campaigns](#campaigns) | ``` automations.recipients.list_id = campaigns.recipients.list_id ``` |
| [list\_members](#list-members) | ``` automations.recipients.list_id = list_members.list_id ``` |
| [list\_segment\_members](#list-segment-members) | ``` automations.recipients.list_id = list_segment_members.list_id ``` |
| [list\_segments](#list-segments) | ``` automations.recipients.list_id = list_segments.list_id ``` |
| [lists](#lists) | ``` automations.recipients.list_id = lists.id ``` |
| [reports\_email\_activity](#reports-email-activity) | ``` automations.recipients.list_id = reports_email_activity.list_id ``` |

automations table schema

|  |
| --- |
| **create\_time**  DATE-TIME |
| **emails\_sent**  INTEGER |
| **id**  STRING |
| **recipients**  OBJECT This is a nested data structure:   - create\_time: DATE-TIME - emails\_sent: INTEGER - id: STRING - recipients: OBJECT, which is also a nested data structure.   - list\_id: STRING   - list\_is\_active: BOOLEAN   - list\_name: STRING   - segments\_opts: OBJECT, which is also a nested structure.     - conditions: ARRAY, which is also a nested structure.       - condition\_type: STRING       - field: STRING       - op: STRING       - value: STRING     - match: STRING     - saved\_segment\_id: INTEGER   - store\_id: STRING - report\_summary: OBJECT, which is also a nested data structure.   - click\_rate: NUMBER   - clicks: INTEGER   - open\_rate: NUMBER   - opens: INTEGER   - subscriber\_clicks: INTEGER   - unique\_opens: INTEGER - settings: OBJECT, which is also a nested data structure.   - authenticate: BOOLEAN   - auto\_footer: BOOLEAN   - from\_name: STRING   - inline\_css: BOOLEAN   - reply\_to: STRING   - title: STRING   - to\_name: STRING   - use\_conversation: BOOLEAN - start\_time: DATE-TIME - status: STRING - tracking: OBJECT, which is also a nested data structure.   - capsule: OBJECT, which is also a nested data structure.     - notes: BOOLEAN   - clicktale: STRING   - ecomm360: BOOLEAN   - goal\_tracking: BOOLEAN   - google\_analytics: STRING   - html\_clicks: BOOLEAN   - opens: BOOLEAN   - salesforce: OBJECT, which is also a nested data structure.     - campaign: BOOLEAN     - notes: BOOLEAN   - text\_clicks: BOOLEAN - trigger\_settings: OBJECT, which is also a nested data structure.   - runtime: STRING   - workflow\_emails\_count: INTEGER   - workflow\_title: STRING   - workflow\_type: STRING |

### campaigns

The `campaigns` table contains info about the campaigns in your MailChimp account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [MailChimp API method](https://developer.mailchimp.com/documentation/mailchimp/reference/campaigns/#read-get_campaigns "Opens in new tab: MailChimp API method") |

campaigns table foreign keys

| Join campaigns with | on |
| --- | --- |
| [reports\_email\_activity](#reports-email-activity) | ``` campaigns.id = reports_email_activity.campaign_id ```  ``` campaigns.recipients.list_id = reports_email_activity.list_id ``` |
| [automations](#automations) | ``` campaigns.recipients.list_id = automations.recipients.list_id ``` |
| [list\_members](#list-members) | ``` campaigns.recipients.list_id = list_members.list_id ``` |
| [list\_segment\_members](#list-segment-members) | ``` campaigns.recipients.list_id = list_segment_members.list_id ``` |
| [list\_segments](#list-segments) | ``` campaigns.recipients.list_id = list_segments.list_id ``` |
| [lists](#lists) | ``` campaigns.recipients.list_id = lists.id ``` |

campaigns table schema

|  |
| --- |
| **archive\_url**  STRING |
| **content\_type**  STRING |
| **create\_time**  DATE-TIME |
| **delivery\_status**  OBJECT This is a nested data structure:   - enabled: BOOLEAN |
| **emails\_sent**  INTEGER |
| **has\_logo\_merge\_tag**  BOOLEAN |
| **id**  STRING |
| **long\_archive\_url**  STRING |
| **needs\_block\_refresh**  BOOLEAN |
| **recipients**  OBJECT This is a nested data structure:   - list\_id: STRING - list\_is\_active: BOOLEAN - list\_name: STRING - recipient\_count: INTEGER - segment\_opts: OBJECT, which is also a nested data structure.   - conditions: ARRAY, which is also a nested data structure.     - condition\_type: STRING     - field: STRING     - op: STRING     - value: STRING   - match: STRING   - prebuilt\_segment\_id: STRING   - saved\_segment\_id: INTEGER - segment\_text: STRING |
| **report\_summary**  OBJECT This is a nested data structure:   - click\_rate: NUMBER - clicks: INTEGER - ecommerce: OBJECT, which is also a nested data structure.   - total\_orders: INTEGER   - total\_revenue: INTEGER   - total\_spent: INTEGER - open\_rate: NUMBER - opens: INTEGER - subscriber\_clicks: INTEGER - unique\_opens: INTEGER |
| **resendable**  BOOLEAN |
| **send\_time**  DATE-TIME |
| **settings**  OBJECT This is a nested data structure:   - authenticate: BOOLEAN - auto\_footer: BOOLEAN - auto\_tweet: BOOLEAN - drag\_and\_drop: BOOLEAN - fb\_comments: BOOLEAN - folder\_id: STRING - from\_name: STRING - inline\_css: BOOLEAN - preview\_text: STRING - reply\_to: STRING - subject\_line: STRING - template\_id: STRING - timewarp: BOOLEAN - title: STRING - to\_name: STRING - use\_conversation: BOOLEAN |
| **social\_card**  OBJECT This is a nested data structure:   - description: STRING - image\_url: STRING - title: STRING |
| **status**  STRING |
| **tracking**  OBJECT This is a nested data structure:   - clicktale: STRING - ecomm360: BOOLEAN - goal\_tracking: BOOLEAN - google\_analytics: STRING - html\_clicks: BOOLEAN - opens: BOOLEAN - text\_clicks: BOOLEAN |
| **type**  STRING |
| **web\_id**  INTEGER |

### list\_members

The `list_members` table contains info about the members in a specific MailChimp list, including currently subscribed, unsubscribed, and bounced members.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | id  list\_id |
| **Replication Key** | last\_changed |
| **Useful links** | [MailChimp API method](https://developer.mailchimp.com/documentation/mailchimp/reference/lists/members/#read-get_lists_list_id_members "Opens in new tab: MailChimp API method") |

list\_members table foreign keys

| Join list\_members with | on |
| --- | --- |
| [automations](#automations) | ``` list_members.list_id = automations.recipients.list_id ``` |
| [campaigns](#campaigns) | ``` list_members.list_id = campaigns.recipients.list_id ``` |
| [list\_segment\_members](#list-segment-members) | ``` list_members.list_id = list_segment_members.list_id ``` |
| [list\_segments](#list-segments) | ``` list_members.list_id = list_segments.list_id ``` |
| [lists](#lists) | ``` list_members.list_id = lists.id ``` |
| [reports\_email\_activity](#reports-email-activity) | ``` list_members.list_id = reports_email_activity.list_id ``` |

list\_members table schema

|  |
| --- |
| **email\_address**  STRING |
| **email\_client**  STRING |
| **email\_type**  STRING |
| **id**  STRING |
| **ip\_opt**  STRING |
| **ip\_signup**  STRING |
| **language**  STRING |
| **last\_changed**  DATE-TIME |
| **list\_id**  STRING |
| **location**  OBJECT This is a nested data structure:   - country\_code: STRING - dstoff: INTEGER - gmtoff: INTEGER - latitude: NUMBER - longitude: NUMBER - timezone: STRING |
| **member\_rating**  NUMBER |
| **source**  STRING |
| **stats**  OBJECT This is a nested data structure:   - avg\_click\_rate: NUMBER - avg\_open\_rate: NUMBER |
| **status**  STRING |
| **tags**  ARRAY This is a nested data structure:   - id: INTEGER - name: STRING |
| **tags\_count**  INTEGER |
| **timestamp\_opt**  DATE-TIME |
| **timestamp\_signup**  DATE-TIME |
| **unique\_email\_id**  STRING |
| **unsubscribe\_reason**  STRING |
| **vip**  BOOLEAN |
| **web\_id**  INTEGER |

### list\_segment\_members

The `list_segment_members` table contains info about members in a [saved segment](https://mailchimp.com/help/save-and-manage-segments/)

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [MailChimp API method](https://developer.mailchimp.com/documentation/mailchimp/reference/lists/segments/members/#read-get_lists_list_id_segments_segment_id_members "Opens in new tab: MailChimp API method") |

list\_segment\_members table foreign keys

| Join list\_segment\_members with | on |
| --- | --- |
| [automations](#automations) | ``` list_segment_members.list_id = automations.recipients.list_id ``` |
| [campaigns](#campaigns) | ``` list_segment_members.list_id = campaigns.recipients.list_id ``` |
| [list\_members](#list-members) | ``` list_segment_members.list_id = list_members.list_id ``` |
| [list\_segments](#list-segments) | ``` list_segment_members.list_id = list_segments.list_id ``` |
| [lists](#lists) | ``` list_segment_members.list_id = lists.id ``` |
| [reports\_email\_activity](#reports-email-activity) | ``` list_segment_members.list_id = reports_email_activity.list_id ``` |

list\_segment\_members table schema

|  |
| --- |
| **email\_address**  STRING |
| **email\_client**  STRING |
| **email\_type**  STRING |
| **id**  STRING |
| **ip\_opt**  STRING |
| **ip\_signup**  STRING |
| **language**  STRING |
| **last\_changed**  DATE-TIME |
| **list\_id**  STRING |
| **location**  OBJECT This is a nested data structure:   - country\_code: STRING - dstoff: INTEGER - gmtoff: INTEGER - latitude: NUMBER - longitude: NUMBER - timezone: STRING |
| **member\_rating**  NUMBER |
| **stats**  OBJECT This is a nested data structure:   - avg\_click\_rate: NUMBER - avg\_open\_rate: NUMBER |
| **status**  STRING |
| **timestamp\_opt**  DATE-TIME |
| **timestamp\_signup**  STRING |
| **unique\_email\_id**  STRING |
| **vip**  BOOLEAN |

### list\_segments

The `list_segments` table contains info about the available segments for a specific list.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [MailChimp API method](https://developer.mailchimp.com/documentation/mailchimp/reference/lists/segments/#read-get_lists_list_id_segments "Opens in new tab: MailChimp API method") |

list\_segments table foreign keys

| Join list\_segments with | on |
| --- | --- |
| [automations](#automations) | ``` list_segments.list_id = automations.recipients.list_id ``` |
| [campaigns](#campaigns) | ``` list_segments.list_id = campaigns.recipients.list_id ``` |
| [list\_members](#list-members) | ``` list_segments.list_id = list_members.list_id ``` |
| [list\_segment\_members](#list-segment-members) | ``` list_segments.list_id = list_segment_members.list_id ``` |
| [lists](#lists) | ``` list_segments.list_id = lists.id ``` |
| [reports\_email\_activity](#reports-email-activity) | ``` list_segments.list_id = reports_email_activity.list_id ``` |

list\_segments table schema

|  |
| --- |
| **created\_at**  DATE-TIME |
| **id**  STRING |
| **list\_id**  STRING |
| **member\_count**  INTEGER |
| **name**  STRING |
| **options**  OBJECT This is a nested data structure:   - conditions: ARRAY, which is also a nested data structure.   - condition\_type: STRING   - field: STRING   - op: STRING   - value: STRING - match: STRING |
| **type**  STRING |
| **updated\_at**  DATE-TIME |

### lists

The `lists` table contains info about all the lists in your MailChimp account. A list is also known as an audience, and is where all contacts are stored and managed in MailChimp.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [MailChimp API method](https://developer.mailchimp.com/documentation/mailchimp/reference/lists/#read-get_lists "Opens in new tab: MailChimp API method") |

lists table foreign keys

| Join lists with | on |
| --- | --- |
| [automations](#automations) | ``` lists.id = automations.recipients.list_id ``` |
| [campaigns](#campaigns) | ``` lists.id = campaigns.recipients.list_id ``` |
| [list\_members](#list-members) | ``` lists.id = list_members.list_id ``` |
| [list\_segment\_members](#list-segment-members) | ``` lists.id = list_segment_members.list_id ``` |
| [list\_segments](#list-segments) | ``` lists.id = list_segments.list_id ``` |
| [reports\_email\_activity](#reports-email-activity) | ``` lists.id = reports_email_activity.list_id ``` |

lists table schema

|  |
| --- |
| **beamer\_address**  STRING |
| **campaign\_defaults**  OBJECT This is a nested data structure:   - from\_email: STRING - from\_name: STRING - language: STRING - subject: STRING |
| **contact**  OBJECT This is a nested data structure:   - address1: STRING - address2: STRING - city: STRING - company: STRING - country: STRING - phone: STRING - state: STRING - zip: STRING |
| **date\_created**  DATE-TIME |
| **double\_optin**  BOOLEAN |
| **email\_type\_option**  BOOLEAN |
| **has\_welcome**  BOOLEAN |
| **id**  STRING |
| **list\_rating**  INTEGER |
| **marketing\_permissions**  BOOLEAN |
| **modules**  ARRAY |
| **name**  STRING |
| **notify\_on\_subscribe**  STRING |
| **notify\_on\_unsubscribe**  STRING |
| **permission\_reminder**  STRING |
| **stats**  OBJECT This is a nested data structure:   - avg\_sub\_rate: NUMBER - avg\_unsub\_rate: NUMBER - campaign\_count: INTEGER - campaign\_last\_sent: DATE-TIME - cleaned\_count: INTEGER - cleaned\_count\_since\_send: INTEGER - click\_rate: NUMBER - last\_sub\_date: DATE-TIME - last\_unsub\_date: DATE-TIME - member\_count\_since\_send: INTEGER - merge\_field\_count: INTEGER - open\_rate: NUMBER - target\_sub\_rate: NUMBER - unsubscribe\_count: INTEGER - unsubscribe\_count\_since\_send: INTEGER |
| **subscribe\_url\_long**  STRING |
| **subscribe\_url\_short**  STRING |
| **use\_archive\_bar**  BOOLEAN |
| **visibility**  STRING |
| **web\_id**  STRING |

### reports\_email\_activity

The `reports_email_activity` table contains info about a member’s subscriber activity in a specific campaign.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | action  campaign\_id  email\_id  timestamp |
| **Useful links** | [MailChimp documentation](https://developer.mailchimp.com/documentation/mailchimp/reference/reports/email-activity/)  [MailChimp API method](https://developer.mailchimp.com/documentation/mailchimp/guides/how-to-use-batch-operations/ "Opens in new tab: MailChimp API method") |

reports\_email\_activity table foreign keys

| Join reports\_email\_activity with | on |
| --- | --- |
| [campaigns](#campaigns) | ``` reports_email_activity.campaign_id = campaigns.id ```  ``` reports_email_activity.list_id = campaigns.recipients.list_id ``` |
| [automations](#automations) | ``` reports_email_activity.list_id = automations.recipients.list_id ``` |
| [list\_members](#list-members) | ``` reports_email_activity.list_id = list_members.list_id ``` |
| [list\_segment\_members](#list-segment-members) | ``` reports_email_activity.list_id = list_segment_members.list_id ``` |
| [list\_segments](#list-segments) | ``` reports_email_activity.list_id = list_segments.list_id ``` |
| [lists](#lists) | ``` reports_email_activity.list_id = lists.id ``` |

reports\_email\_activity table schema

|  |
| --- |
| **action**  STRING |
| **campaign\_id**  STRING |
| **email\_address**  STRING |
| **email\_id**  STRING |
| **ip**  STRING |
| **list\_id**  STRING |
| **list\_is\_active**  BOOLEAN |
| **timestamp**  DATE-TIME |
| **type**  STRING |
| **url**  STRING |

### unsubscribes

The `unsubscribes` table contains info about members who have unsubscribed from a specific campaign.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | campaign\_id  email\_id |
| **Useful links** | [MailChimp API method](https://developer.mailchimp.com/documentation/mailchimp/reference/reports/unsubscribed/#read-get_reports_campaign_id_unsubscribed "Opens in new tab: MailChimp API method") |

unsubscribes table schema

|  |
| --- |
| **campaign\_id**  STRING |
| **email\_address**  STRING |
| **email\_id**  STRING |
| **list\_id**  STRING |
| **list\_is\_active**  BOOLEAN |
| **reason**  STRING |
| **timestamp**  DATE-TIME |
| **vip**  BOOLEAN |
