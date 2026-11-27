---
title: "Pardot"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Pardot.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Pardot

Pardot is a marketing automation solution that enables marketers to identify prospective customers that are most likely to convert.

Pardot integration replicates data using the [Pardot API](http://developer.pardot.com/#official-pardot-api-documentation).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To retrieve your business unit ID:

1. Log into your [Salesforce](https://login.salesforce.com/) account.
2. Navigate to Setup.
3. Search for Pardot in the Quick Find box.
4. Copy and paste your business unit ID into a secured file.

To retrieve your consumer key and secret:

1. Log into your [Salesforce](https://login.salesforce.com/) account.
2. Navigate to Setup.
3. Search for App Manager in the Quick Find box.
4. Go to your connected app and select View.
5. Copy and paste your consumer key into a secured file.
6. Click Click to reveal to show your consumer secret and copy it.

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
| Pardot Business Unit ID | Business unit ID. |
| Consumer Key | A unique identifier for the connected app. |
| Consumer Secret | A password for the connected app. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### campaigns

The `campaigns` table contains info about the campaigns in your Pardot account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | id |
| **Useful links** | [Pardot documentation](http://developer.pardot.com/kb/object-field-references/#campaign)  [Pardot API method](http://developer.pardot.com/kb/api-version-3/campaigns/ "Opens in new tab: Pardot API method") |

campaigns table foreign keys

| Join campaigns with | on |
| --- | --- |
| [opportunities](#opportunities) | ``` campaigns.id = opportunities.campaign_id ``` |
| [prospects](#prospects) | ``` campaigns.id = prospects.campaign_id ``` |

campaigns table schema

|  |
| --- |
| **cost**  INTEGER |
| **id**  INTEGER |
| **name**  STRING |

### email\_clicks

The `email_clicks` table contains info about email click events.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | created\_at |
| **Useful links** | [Pardot documentation](http://developer.pardot.com/kb/object-field-references/#email-clicks)  [Pardot API method](http://developer.pardot.com/kb/api-version-3/batch-email-clicks/ "Opens in new tab: Pardot API method") |

email\_clicks table foreign keys

| Join email\_clicks with | on |
| --- | --- |
| [visitor\_activities](#visitor-activities) | ``` email_clicks.email_template_id = visitor_activities.email_template_id ```  ``` email_clicks.list_email_id = visitor_activities.list_email_id ```  ``` email_clicks.prospect_id = visitor_activities.prospect_id ``` |
| [list\_memberships](#list-memberships) | ``` email_clicks.prospect_id = list_memberships.prospect_id ``` |
| [prospects](#prospects) | ``` email_clicks.prospect_id = prospects.id ``` |
| [visits](#visits) | ``` email_clicks.prospect_id = visits.prospect_id ``` |

email\_clicks table schema

|  |
| --- |
| **created\_at**  DATE-TIME |
| **drip\_program\_action\_id**  INTEGER |
| **email\_template\_id**  INTEGER |
| **id**  INTEGER |
| **list\_email\_id**  INTEGER |
| **prospect\_id**  INTEGER |
| **tracker\_redirect\_id**  INTEGER |
| **url**  STRING |

### list\_memberships

The `list_memberships` table contains info about list memberships.

**Note**: To replicate this table, the [`lists`](#lists) table must also be set to replicate.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Keys** | id  list\_id  updated\_at |
| **Useful links** | [Pardot documentation](http://developer.pardot.com/kb/object-field-references/#list-membership)  [Pardot API method](http://developer.pardot.com/kb/api-version-3/list-memberships/ "Opens in new tab: Pardot API method") |

list\_memberships table foreign keys

| Join list\_memberships with | on |
| --- | --- |
| [lists](#lists) | ``` list_memberships.list_id = lists.id ``` |
| [email\_clicks](#email-clicks) | ``` list_memberships.prospect_id = email_clicks.prospect_id ``` |
| [prospects](#prospects) | ``` list_memberships.prospect_id = prospects.id ``` |
| [visitor\_activities](#visitor-activities) | ``` list_memberships.prospect_id = visitor_activities.prospect_id ``` |
| [visits](#visits) | ``` list_memberships.prospect_id = visits.prospect_id ``` |

list\_memberships table schema

|  |
| --- |
| **created\_at**  DATE-TIME |
| **id**  INTEGER |
| **list\_id**  INTEGER |
| **opted\_out**  INTEGER |
| **prospect\_id**  INTEGER |
| **updated\_at**  DATE-TIME |

### lists

The `lists` table contains info about the lists in your Pardot account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Pardot documentation](http://developer.pardot.com/kb/object-field-references/#list)  [Pardot API method](http://developer.pardot.com/kb/api-version-3/lists/ "Opens in new tab: Pardot API method") |

lists table foreign keys

| Join lists with | on |
| --- | --- |
| [list\_memberships](#list-memberships) | ``` lists.id = list_memberships.list_id ``` |

lists table schema

|  |
| --- |
| **created\_at**  DATE-TIME |
| **description**  STRING |
| **id**  INTEGER |
| **is\_crm\_visible**  BOOLEAN |
| **is\_dynamic**  BOOLEAN |
| **is\_public**  BOOLEAN |
| **name**  STRING |
| **title**  STRING |
| **updated\_at**  DATE-TIME |

### opportunities

The `opportunities` table contains info about the opportunities in your Pardot account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Keys** | id  updated\_at |
| **Useful links** | [Pardot documentation](http://developer.pardot.com/kb/object-field-references/#opportunity)  [Pardot API method](http://developer.pardot.com/kb/api-version-3/opportunities/ "Opens in new tab: Pardot API method") |

opportunities table foreign keys

| Join opportunities with | on |
| --- | --- |
| [campaigns](#campaigns) | ``` opportunities.campaign_id = campaigns.id ``` |
| [prospects](#prospects) | ``` opportunities.campaign_id = prospects.campaign_id ``` |

opportunities table schema

|  |
| --- |
| **campaign\_id**  INTEGER |
| **closed\_at**  DATE-TIME |
| **created\_at**  DATE-TIME |
| **id**  INTEGER |
| **name**  STRING |
| **probability**  INTEGER |
| **stage**  STRING |
| **status**  STRING |
| **type**  STRING |
| **updated\_at**  DATE-TIME |
| **value**  NUMBER |

### prospect\_accounts

The `prospect_accounts` table contains info about prospect accounts.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Pardot documentation](http://developer.pardot.com/kb/object-field-references/#prospect-account)  [Pardot API method](http://developer.pardot.com/kb/api-version-3/prospect-accounts/ "Opens in new tab: Pardot API method") |

prospect\_accounts table foreign keys

| Join prospect\_accounts with | on |
| --- | --- |
| [users](#users) | ``` prospect_accounts.assigned_to.user.id = users.id ``` |

prospect\_accounts table schema

|  |
| --- |
| **assigned\_to**  OBJECT This is a nested data structure:   - user: OBJECT, which is also a nested data structure.   - account: INTEGER   - created\_at: DATE-TIME   - email: STRING   - first\_name: STRING   - id: INTEGER   - job\_tile: STRING   - last\_name: STRING   - role: STRING   - updated\_at: DATE-TIME |
| **created\_at**  DATE-TIME |
| **id**  INTEGER |
| **name**  STRING |
| **updated\_at**  DATE-TIME |

### prospects

The `prospects` table contains info about the prospects in your Pardot account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Pardot documentation](http://developer.pardot.com/kb/object-field-references/#prospect)  [Pardot API method](http://developer.pardot.com/kb/api-version-3/prospects/#supported-operations_1 "Opens in new tab: Pardot API method") |

prospects table foreign keys

| Join prospects with | on |
| --- | --- |
| [campaigns](#campaigns) | ``` prospects.campaign_id = campaigns.id ``` |
| [opportunities](#opportunities) | ``` prospects.campaign_id = opportunities.campaign_id ``` |
| [email\_clicks](#email-clicks) | ``` prospects.id = email_clicks.prospect_id ``` |
| [list\_memberships](#list-memberships) | ``` prospects.id = list_memberships.prospect_id ``` |
| [visitor\_activities](#visitor-activities) | ``` prospects.id = visitor_activities.prospect_id ``` |
| [visits](#visits) | ``` prospects.id = visits.prospect_id ``` |

prospects table schema

|  |
| --- |
| **address\_one**  STRING |
| **address\_two**  STRING |
| **annual\_revenue**  STRING |
| **campaign\_id**  INTEGER |
| **city**  STRING |
| **comments**  STRING |
| **company**  STRING |
| **country**  STRING |
| **created\_at**  DATE-TIME |
| **crm\_account\_fid**  STRING |
| **crm\_contact\_fid**  STRING |
| **crm\_last\_sync**  DATE-TIME |
| **crm\_lead\_fid**  STRING |
| **crm\_owner\_fid**  STRING |
| **crm\_url**  STRING |
| **department**  STRING |
| **email**  STRING |
| **employees**  STRING |
| **fax**  STRING |
| **first\_name**  STRING |
| **grade**  STRING |
| **id**  INTEGER |
| **industry**  STRING |
| **is\_do\_not\_call**  BOOLEAN |
| **is\_do\_not\_email**  BOOLEAN |
| **is\_reviewed**  BOOLEAN |
| **is\_starred**  BOOLEAN |
| **job\_title**  STRING |
| **last\_activity\_at**  DATE-TIME |
| **last\_name**  STRING |
| **notes**  STRING |
| **opted\_out**  BOOLEAN |
| **password**  STRING |
| **phone**  STRING |
| **prospect\_account\_id**  INTEGER |
| **recent\_interaction**  STRING |
| **salutation**  STRING |
| **score**  INTEGER |
| **source**  STRING |
| **state**  STRING |
| **territory**  STRING |
| **updated\_at**  DATE-TIME |
| **website**  STRING |
| **years\_in\_business**  STRING |
| **zip**  STRING |

### users

The `users` table contains info about the users in your Pardot account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Keys** | id  updated\_at |
| **Useful links** | [Pardot documentation](http://developer.pardot.com/kb/object-field-references/#user)  [Pardot API method](http://developer.pardot.com/kb/api-version-3/users/ "Opens in new tab: Pardot API method") |

users table foreign keys

| Join users with | on |
| --- | --- |
| [prospect\_accounts](#prospect-accounts) | ``` users.id = prospect_accounts.assigned_to.user.id ``` |

users table schema

|  |
| --- |
| **created\_at**  DATE-TIME |
| **email**  STRING |
| **first\_name**  STRING |
| **id**  INTEGER |
| **job\_title**  STRING |
| **last\_name**  STRING |
| **role**  STRING |
| **updated\_at**  DATE-TIME |

### visitor\_activities

The `visitor_activities` table contains info about visitor activities.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | id |
| **Useful links** | [Pardot documentation](http://developer.pardot.com/kb/object-field-references/#visitor-activity)  [Pardot API method](http://developer.pardot.com/kb/api-version-3/visitor-activities/ "Opens in new tab: Pardot API method") |

visitor\_activities table foreign keys

| Join visitor\_activities with | on |
| --- | --- |
| [email\_clicks](#email-clicks) | ``` visitor_activities.email_template_id = email_clicks.email_template_id ```  ``` visitor_activities.list_email_id = email_clicks.list_email_id ```  ``` visitor_activities.prospect_id = email_clicks.prospect_id ``` |
| [list\_memberships](#list-memberships) | ``` visitor_activities.prospect_id = list_memberships.prospect_id ``` |
| [prospects](#prospects) | ``` visitor_activities.prospect_id = prospects.id ``` |
| [visits](#visits) | ``` visitor_activities.prospect_id = visits.prospect_id ```  ``` visitor_activities.visitor_id = visits.visitor_id ``` |
| [visitors](#visitors) | ``` visitor_activities.visitor_id = visitors.id ``` |

visitor\_activities table schema

|  |
| --- |
| **campaign**  OBJECT This is a nested data structure. |
| **campaign\_id**  INTEGER |
| **created\_at**  DATE-TIME |
| **details**  STRING |
| **email\_id**  INTEGER |
| **email\_template\_id**  INTEGER |
| **file\_id**  INTEGER |
| **form\_handler\_id**  INTEGER |
| **form\_id**  INTEGER |
| **id**  INTEGER |
| **landing\_page\_id**  INTEGER |
| **list\_email\_id**  INTEGER |
| **multivariate\_test\_variation\_id**  INTEGER |
| **paid\_search\_id\_id**  INTEGER |
| **prospect\_id**  INTEGER |
| **site\_search\_query\_id**  INTEGER |
| **type**  INTEGER |
| **type\_name**  STRING |
| **updated\_at**  DATE-TIME |
| **visitor\_id**  INTEGER |
| **visitor\_page\_view\_id**  INTEGER |

### visitors

The `visitors` table contains info about visitors.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Pardot documentation](http://developer.pardot.com/kb/object-field-references/#visitor)  [Pardot API method](http://developer.pardot.com/kb/api-version-3/visitors/ "Opens in new tab: Pardot API method") |

visitors table foreign keys

| Join visitors with | on |
| --- | --- |
| [visitor\_activities](#visitor-activities) | ``` visitors.id = visitor_activities.visitor_id ``` |
| [visits](#visits) | ``` visitors.id = visits.visitor_id ``` |

visitors table schema

|  |
| --- |
| **campaign\_parameter**  STRING |
| **content\_parameter**  STRING |
| **created\_at**  DATE-TIME |
| **hostname**  STRING |
| **id**  INTEGER |
| **ip\_address**  STRING |
| **medium\_parameter**  STRING |
| **page\_view\_count**  INTEGER |
| **source\_parameter**  STRING |
| **term\_parameter**  STRING |
| **updated\_at**  DATE-TIME |

### visits

The `visits` table contains info about visits.

**Note**: To replicate this table, you must also set the [`visitors`](#visitors) table to replicate.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Keys** | id  updated\_at |
| **Useful links** | [Pardot documentation](http://developer.pardot.com/kb/object-field-references/#visit)  [Pardot API method](http://developer.pardot.com/kb/api-version-3/visits/ "Opens in new tab: Pardot API method") |

visits table foreign keys

| Join visits with | on |
| --- | --- |
| [email\_clicks](#email-clicks) | ``` visits.prospect_id = email_clicks.prospect_id ``` |
| [list\_memberships](#list-memberships) | ``` visits.prospect_id = list_memberships.prospect_id ``` |
| [prospects](#prospects) | ``` visits.prospect_id = prospects.id ``` |
| [visitor\_activities](#visitor-activities) | ``` visits.prospect_id = visitor_activities.prospect_id ```  ``` visits.visitor_id = visitor_activities.visitor_id ``` |
| [visitors](#visitors) | ``` visits.visitor_id = visitors.id ``` |

visits table schema

|  |
| --- |
| **campaign\_parameter**  STRING |
| **content\_parameter**  STRING |
| **created\_at**  DATE-TIME |
| **duration\_in\_seconds**  INTEGER |
| **first\_visitor\_page\_view\_at**  DATE-TIME |
| **id**  INTEGER |
| **last\_visitor\_page\_view\_at**  DATE-TIME |
| **medium\_parameter**  STRING |
| **prospect\_id**  INTEGER |
| **source\_parameter**  STRING |
| **term\_parameter**  STRING |
| **updated\_at**  DATE-TIME |
| **visitor\_id**  INTEGER |
| **visitor\_page\_view\_count**  INTEGER |
| **visitor\_page\_views**  OBJECT This is a nested data structure:   - visitor\_page\_view: ARRAY, which is also a nested data structure.   - created\_at: DATE-TIME   - id: INTEGER   - title: STRING   - url: STRING |
