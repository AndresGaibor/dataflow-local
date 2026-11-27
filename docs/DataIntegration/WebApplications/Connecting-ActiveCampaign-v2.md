---
title: "ActiveCampaign"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-ActiveCampaign-v2.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# ActiveCampaign

ActiveCampaign is a SaaS platform for small-to-mid-sized businesses. It offers marketing and sales automation.

For more information about the API, see [ActiveCampaign v3 API](https://developers.activecampaign.com/reference#overview).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To retrieve your API URL and token:

1. Log into your ActiveCampaign account.
2. Go to the My Settings page.
3. Click the Developer tab.
4. Copy the API URL and API token.

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
| API URL | API URL. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### account\_contacts

The `account_contacts` table contains information about contacts in your ActiveCampaign account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_timestamp |
| **Useful links** | [ActiveCampaign documentation](https://developers.activecampaign.com/reference#account-contacts)  [ActiveCampaign API method](https://developers.activecampaign.com/reference#list-all-associations-1 "Opens in new tab: ActiveCampaign API method") |

account\_contacts table foreign keys

| Join account\_contacts with | on |
| --- | --- |
| [accounts](#accounts) | ``` account_contacts.account = accounts.id ``` |
| [deals](#deals) | ``` account_contacts.account = deals.account ```  ``` account_contacts.contact = deals.contact ``` |
| [contact\_emails](#contact-emails) | ``` account_contacts.account = contact_emails.account ```  ``` account_contacts.contact = contact_emails.contact ``` |
| [email\_activities](#email-activities) | ``` account_contacts.account = email_activities.account ```  ``` account_contacts.contact = email_activities.contact ``` |
| [account\_custom\_field\_values](#account-custom-field-values) | ``` account_contacts.account = account_custom_field_values.account_id ``` |
| [contacts](#contacts) | ``` account_contacts.contact = contacts.id ``` |
| [forms](#forms) | ``` account_contacts.contact = forms.contacts ``` |
| [bounce\_logs](#bounce-logs) | ``` account_contacts.contact = bounce_logs.contact ``` |
| [contact\_data](#contact-data) | ``` account_contacts.contact = contact_data.contact ``` |
| [contact\_lists](#contact-lists) | ``` account_contacts.contact = contact_lists.contact ``` |
| [contact\_tags](#contact-tags) | ``` account_contacts.contact = contact_tags.contact ``` |
| [contact\_conversions](#contact-conversions) | ``` account_contacts.contact = contact_conversions.contact ``` |
| [contact\_automations](#contact-automations) | ``` account_contacts.contact = contact_automations.contact ``` |
| [contact\_custom\_field\_values](#contact-custom-field-values) | ``` account_contacts.contact = contact_custom_field_values.contact ``` |
| [contact\_deals](#contact-deals) | ``` account_contacts.contact = contact_deals.contact ``` |

account\_contacts table schema

|  |
| --- |
| **account**  INTEGER |
| **contact**  INTEGER |
| **created\_timestamp**  DATE-TIME |
| **id**  INTEGER |
| **job\_title**  STRING |
| **updated\_timestamp**  DATE-TIME |

### account\_custom\_field\_values

The `account_custom_field_values` table contains information about your account custom fields’ values in your ActiveCampaign account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_timestamp |
| **Useful links** | [ActiveCampaign documentation](https://developers.activecampaign.com/reference#custom-account-field-values)  [ActiveCampaign API method](https://developers.activecampaign.com/reference#list-all-custom-field-values-2 "Opens in new tab: ActiveCampaign API method") |

account\_custom\_field\_values table foreign keys

| Join account\_custom\_field\_values with | on |
| --- | --- |
| [account\_custom\_fields](#account-custom-fields) | ``` account_custom_field_values.custom_field_id = account_custom_fields.id ``` |
| [accounts](#accounts) | ``` account_custom_field_values.account_id = accounts.id ``` |
| [deals](#deals) | ``` account_custom_field_values.account_id = deals.account ``` |
| [contact\_emails](#contact-emails) | ``` account_custom_field_values.account_id = contact_emails.account ``` |
| [email\_activities](#email-activities) | ``` account_custom_field_values.account_id = email_activities.account ``` |
| [account\_contacts](#account-contacts) | ``` account_custom_field_values.account_id = account_contacts.account ``` |

account\_custom\_field\_values table schema

|  |
| --- |
| **account\_custom\_field\_metum\_id**  INTEGER |
| **account\_id**  INTEGER |
| **created\_timestamp**  DATE-TIME |
| **custom\_field\_id**  INTEGER |
| **field\_value**  STRING |
| **id**  INTEGER |
| **updated\_timestamp**  DATE-TIME |

### account\_custom\_fields

The `account_custom_fields` table contains information about account custom fields in your ActiveCampaign account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_timestamp |
| **Useful links** | [ActiveCampaign documentation](https://developers.activecampaign.com/reference#custom-account-fields-1)  [ActiveCampaign API method](https://developers.activecampaign.com/reference#list-all-custom-fields "Opens in new tab: ActiveCampaign API method") |

account\_custom\_fields table foreign keys

| Join account\_custom\_fields with | on |
| --- | --- |
| [account\_custom\_field\_values](#account-custom-field-values) | ``` account_custom_fields.id = account_custom_field_values.custom_field_id ``` |

account\_custom\_fields table schema

|  |
| --- |
| **created\_timestamp**  DATE-TIME |
| **display\_order**  INTEGER |
| **field\_default**  STRING |
| **field\_default\_currency**  STRING |
| **field\_label**  STRING |
| **field\_options**  ARRAY |
| **field\_type**  STRING |
| **hide\_field\_flag**  BOOLEAN |
| **id**  INTEGER |
| **is\_form\_visible**  BOOLEAN |
| **is\_required**  BOOLEAN |
| **known\_field\_id**  INTEGER |
| **personalization**  STRING |
| **updated\_timestamp**  DATE-TIME |

### accounts

The `accounts` table contains information about accounts in your ActiveCampaign account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_timestamp |
| **Useful links** | [ActiveCampaign documentation](https://developers.activecampaign.com/reference#accounts)  [ActiveCampaign API method](https://developers.activecampaign.com/reference#list-all-accounts "Opens in new tab: ActiveCampaign API method") |

accounts table foreign keys

| Join accounts with | on |
| --- | --- |
| [deals](#deals) | ``` accounts.id = deals.account ``` |
| [contact\_emails](#contact-emails) | ``` accounts.id = contact_emails.account ``` |
| [email\_activities](#email-activities) | ``` accounts.id = email_activities.account ``` |
| [account\_contacts](#account-contacts) | ``` accounts.id = account_contacts.account ``` |
| [account\_custom\_field\_values](#account-custom-field-values) | ``` accounts.id = account_custom_field_values.account_id ``` |

accounts table schema

|  |
| --- |
| **account\_url**  STRING |
| **contact\_count**  INTEGER |
| **created\_timestamp**  DATE-TIME |
| **deal\_count**  INTEGER |
| **id**  INTEGER |
| **name**  STRING |
| **updated\_timestamp**  DATE-TIME |

### activities

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | tstamp |

activities table foreign keys

| Join activities with | on |
| --- | --- |
| [users](#users) | ``` activities.userid = users.id ``` |
| [forms](#forms) | ``` activities.userid = forms.userid ``` |
| [lists](#lists) | ``` activities.userid = lists.userid ``` |
| [messages](#messages) | ``` activities.userid = messages.userid ``` |
| [saved\_responses](#saved-responses) | ``` activities.userid = saved_responses.last_sent_user_id ``` |
| [tasks](#tasks) | ``` activities.userid = tasks.user ``` |
| [templates](#templates) | ``` activities.userid = templates.userid ``` |
| [campaign\_lists](#campaign-lists) | ``` activities.userid = campaign_lists.userid ``` |
| [configs](#configs) | ``` activities.userid = configs.userid ``` |
| [contact\_emails](#contact-emails) | ``` activities.userid = contact_emails.userid ``` |
| [deal\_activities](#deal-activities) | ``` activities.userid = deal_activities.userid ``` |
| [deal\_group\_users](#deal-group-users) | ``` activities.userid = deal_group_users.user ``` |
| [email\_activities](#email-activities) | ``` activities.userid = email_activities.userid ``` |
| [sms](#sms) | ``` activities.userid = sms.userid ``` |
| [automations](#automations) | ``` activities.userid = automations.userid ``` |
| [calendars](#calendars) | ``` activities.userid = calendars.userid ``` |
| [campaigns](#campaigns) | ``` activities.userid = campaigns.userid ``` |

activities table schema

|  |
| --- |
| **id**  INTEGER |
| **json\_data**  STRING |
| **permission**  STRING |
| **reference**  OBJECT This is a nested data structure:   - **id**: INTEGER - **type**: STRING |
| **reference\_action**  STRING |
| **reference\_id**  INTEGER |
| **reference\_model\_name**  STRING |
| **reference\_type**  STRING |
| **subscriberid**  INTEGER |
| **tstamp**  DATE-TIME |
| **user**  INTEGER |
| **userid**  INTEGER |

### addresses

The `addresses` table contains information about addresses in your ActiveCampaign account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [ActiveCampaign documentation](https://developers.activecampaign.com/reference#address)  [ActiveCampaign API method](https://developers.activecampaign.com/reference#list-all-addresses "Opens in new tab: ActiveCampaign API method") |

addresses table foreign keys

| Join addresses with | on |
| --- | --- |
| [campaigns](#campaigns) | ``` addresses.id = campaigns.addressid ``` |
| [forms](#forms) | ``` addresses.id = forms.addressid ``` |

addresses table schema

|  |
| --- |
| **address1**  STRING |
| **address2**  STRING |
| **allgroup**  INTEGER |
| **city**  STRING |
| **company\_name**  STRING |
| **country**  STRING |
| **district**  STRING |
| **id**  INTEGER |
| **is\_default**  BOOLEAN |
| **state**  STRING |
| **zip**  STRING |

### automation\_blocks

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |

automation\_blocks table foreign keys

| Join automation\_blocks with | on |
| --- | --- |
| [automations](#automations) | ``` automation_blocks.automation = automations.id ``` |
| [deal\_activities](#deal-activities) | ``` automation_blocks.automation = deal_activities.automation ``` |
| [goals](#goals) | ``` automation_blocks.automation = goals.automation ``` |
| [site\_messages](#site-messages) | ``` automation_blocks.automation = site_messages.automation ``` |
| [sms](#sms) | ``` automation_blocks.automation = sms.automation ``` |
| [campaigns](#campaigns) | ``` automation_blocks.automation = campaigns.automation ``` |
| [contact\_automations](#contact-automations) | ``` automation_blocks.automation = contact_automations.automation ``` |

automation\_blocks table schema

|  |
| --- |
| **automation**  INTEGER |
| **cdate**  DATE-TIME |
| **deleted**  INTEGER |
| **id**  INTEGER |
| **mdate**  DATE-TIME |
| **ordernum**  INTEGER |
| **params**  OBJECT  ARRAY |
| **parent**  INTEGER |

### automations

The `automations` table contains information about automations in your ActiveCampaign account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | mdate |
| **Useful links** | [ActiveCampaign documentation](https://developers.activecampaign.com/reference#automation)  [ActiveCampaign API method](https://developers.activecampaign.com/reference#list-all-automations "Opens in new tab: ActiveCampaign API method") |

automations table foreign keys

| Join automations with | on |
| --- | --- |
| [users](#users) | ``` automations.userid = users.id ``` |
| [forms](#forms) | ``` automations.userid = forms.userid ``` |
| [lists](#lists) | ``` automations.userid = lists.userid ``` |
| [messages](#messages) | ``` automations.userid = messages.userid ``` |
| [saved\_responses](#saved-responses) | ``` automations.userid = saved_responses.last_sent_user_id ``` |
| [tasks](#tasks) | ``` automations.userid = tasks.user ``` |
| [templates](#templates) | ``` automations.userid = templates.userid ``` |
| [activities](#activities) | ``` automations.userid = activities.userid ``` |
| [campaign\_lists](#campaign-lists) | ``` automations.userid = campaign_lists.userid ``` |
| [configs](#configs) | ``` automations.userid = configs.userid ``` |
| [contact\_emails](#contact-emails) | ``` automations.userid = contact_emails.userid ``` |
| [deal\_activities](#deal-activities) | ``` automations.userid = deal_activities.userid ```  ``` automations.id = deal_activities.automation ``` |
| [deal\_group\_users](#deal-group-users) | ``` automations.userid = deal_group_users.user ``` |
| [email\_activities](#email-activities) | ``` automations.userid = email_activities.userid ``` |
| [sms](#sms) | ``` automations.userid = sms.userid ```  ``` automations.id = sms.automation ``` |
| [calendars](#calendars) | ``` automations.userid = calendars.userid ``` |
| [campaigns](#campaigns) | ``` automations.userid = campaigns.userid ```  ``` automations.id = campaigns.automation ``` |
| [goals](#goals) | ``` automations.id = goals.automation ``` |
| [site\_messages](#site-messages) | ``` automations.id = site_messages.automation ``` |
| [automation\_blocks](#automation-blocks) | ``` automations.id = automation_blocks.automation ``` |
| [contact\_automations](#contact-automations) | ``` automations.id = contact_automations.automation ``` |

automations table schema

|  |
| --- |
| **cdate**  DATE-TIME |
| **defaultscreenshot**  STRING |
| **entered**  INTEGER |
| **exited**  INTEGER |
| **hidden**  INTEGER |
| **id**  INTEGER |
| **mdate**  DATE-TIME |
| **name**  STRING |
| **screenshot**  STRING |
| **status**  INTEGER |
| **userid**  INTEGER |

### bounce\_logs

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Replication Key** | updated\_timestamp |

bounce\_logs table foreign keys

| Join bounce\_logs with | on |
| --- | --- |
| [campaigns](#campaigns) | ``` bounce_logs.campaignid = campaigns.id ``` |
| [campaign\_links](#campaign-links) | ``` bounce_logs.campaignid = campaign_links.campaignid ```  ``` bounce_logs.messageid = campaign_links.messageid ``` |
| [campaign\_lists](#campaign-lists) | ``` bounce_logs.campaignid = campaign_lists.campaignid ``` |
| [campaign\_messages](#campaign-messages) | ``` bounce_logs.campaignid = campaign_messages.campaignid ```  ``` bounce_logs.messageid = campaign_messages.messageid ``` |
| [contact\_lists](#contact-lists) | ``` bounce_logs.campaignid = contact_lists.campaign ```  ``` bounce_logs.contact = contact_lists.contact ```  ``` bounce_logs.messageid = contact_lists.message ``` |
| [contacts](#contacts) | ``` bounce_logs.contact = contacts.id ``` |
| [deals](#deals) | ``` bounce_logs.contact = deals.contact ``` |
| [forms](#forms) | ``` bounce_logs.contact = forms.contacts ``` |
| [contact\_data](#contact-data) | ``` bounce_logs.contact = contact_data.contact ``` |
| [contact\_emails](#contact-emails) | ``` bounce_logs.contact = contact_emails.contact ```  ``` bounce_logs.messageid = contact_emails.messageid ``` |
| [contact\_tags](#contact-tags) | ``` bounce_logs.contact = contact_tags.contact ``` |
| [contact\_conversions](#contact-conversions) | ``` bounce_logs.contact = contact_conversions.contact ``` |
| [email\_activities](#email-activities) | ``` bounce_logs.contact = email_activities.contact ``` |
| [account\_contacts](#account-contacts) | ``` bounce_logs.contact = account_contacts.contact ``` |
| [contact\_automations](#contact-automations) | ``` bounce_logs.contact = contact_automations.contact ``` |
| [contact\_custom\_field\_values](#contact-custom-field-values) | ``` bounce_logs.contact = contact_custom_field_values.contact ``` |
| [contact\_deals](#contact-deals) | ``` bounce_logs.contact = contact_deals.contact ``` |
| [messages](#messages) | ``` bounce_logs.messageid = messages.id ``` |

bounce\_logs table schema

|  |
| --- |
| **bounce**  INTEGER |
| **bounceid**  INTEGER |
| **campaign**  INTEGER |
| **campaignid**  INTEGER |
| **code**  INTEGER |
| **codeid**  INTEGER |
| **contact**  INTEGER |
| **created\_by**  INTEGER |
| **created\_timestamp**  DATE-TIME |
| **email**  STRING |
| **error**  STRING |
| **id**  INTEGER |
| **message**  INTEGER |
| **messageid**  INTEGER |
| **source**  STRING |
| **subscriberid**  INTEGER |
| **tstamp**  DATE-TIME |
| **updated\_by**  INTEGER |
| **updated\_timestamp**  DATE-TIME |

### brandings

The `brandings` table contains information about existing branding resources in your ActiveCampaign account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [ActiveCampaign documentation](https://developers.activecampaign.com/reference#branding)  [ActiveCampaign API method](https://developers.activecampaign.com/reference#brandings "Opens in new tab: ActiveCampaign API method") |

brandings table schema

|  |
| --- |
| **admin\_template\_css**  STRING |
| **admin\_template\_htm**  STRING |
| **copyright**  INTEGER |
| **favicon**  STRING |
| **footer\_html\_value**  STRING |
| **footer\_text\_value**  STRING |
| **groupid**  STRING |
| **header\_html\_value**  STRING |
| **header\_text\_value**  STRING |
| **help**  INTEGER |
| **id**  INTEGER |
| **license**  INTEGER |
| **public\_template\_css**  STRING |
| **public\_template\_htm**  STRING |
| **site\_logo**  STRING |
| **site\_logo\_small**  STRING |
| **site\_name**  STRING |
| **version**  INTEGER |

### calendars

The `calendars` table contains information about calendar feeds in your ActiveCampaign account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | mdate |
| **Useful links** | [ActiveCampaign documentation](https://developers.activecampaign.com/reference#calendar-feeds)  [ActiveCampaign API method](https://developers.activecampaign.com/reference#list-all-calendar-feeds "Opens in new tab: ActiveCampaign API method") |

calendars table foreign keys

| Join calendars with | on |
| --- | --- |
| [users](#users) | ``` calendars.userid = users.id ``` |
| [forms](#forms) | ``` calendars.userid = forms.userid ``` |
| [lists](#lists) | ``` calendars.userid = lists.userid ``` |
| [messages](#messages) | ``` calendars.userid = messages.userid ``` |
| [saved\_responses](#saved-responses) | ``` calendars.userid = saved_responses.last_sent_user_id ``` |
| [tasks](#tasks) | ``` calendars.userid = tasks.user ``` |
| [templates](#templates) | ``` calendars.userid = templates.userid ``` |
| [activities](#activities) | ``` calendars.userid = activities.userid ``` |
| [campaign\_lists](#campaign-lists) | ``` calendars.userid = campaign_lists.userid ``` |
| [configs](#configs) | ``` calendars.userid = configs.userid ``` |
| [contact\_emails](#contact-emails) | ``` calendars.userid = contact_emails.userid ``` |
| [deal\_activities](#deal-activities) | ``` calendars.userid = deal_activities.userid ``` |
| [deal\_group\_users](#deal-group-users) | ``` calendars.userid = deal_group_users.user ``` |
| [email\_activities](#email-activities) | ``` calendars.userid = email_activities.userid ``` |
| [sms](#sms) | ``` calendars.userid = sms.userid ``` |
| [automations](#automations) | ``` calendars.userid = automations.userid ``` |
| [campaigns](#campaigns) | ``` calendars.userid = campaigns.userid ``` |

calendars table schema

|  |
| --- |
| **cdate**  DATE-TIME |
| **id**  INTEGER |
| **mdate**  DATE-TIME |
| **notification**  INTEGER |
| **title**  STRING |
| **token**  STRING |
| **type**  STRING |
| **userid**  INTEGER |

### campaign\_links

The `campaign_links` table contains information about the links attached to your campaigns in your ActiveCampaign account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_timestamp |
| **Useful links** | [ActiveCampaign documentation](https://developers.activecampaign.com/reference#test-1)  [ActiveCampaign API method](https://developers.activecampaign.com/reference#retrieve-links-associated-campaign "Opens in new tab: ActiveCampaign API method") |

campaign\_links table foreign keys

| Join campaign\_links with | on |
| --- | --- |
| [campaigns](#campaigns) | ``` campaign_links.campaignid = campaigns.id ``` |
| [bounce\_logs](#bounce-logs) | ``` campaign_links.campaignid = bounce_logs.campaignid ```  ``` campaign_links.messageid = bounce_logs.messageid ``` |
| [campaign\_lists](#campaign-lists) | ``` campaign_links.campaignid = campaign_lists.campaignid ``` |
| [campaign\_messages](#campaign-messages) | ``` campaign_links.campaignid = campaign_messages.campaignid ```  ``` campaign_links.messageid = campaign_messages.messageid ``` |
| [contact\_lists](#contact-lists) | ``` campaign_links.campaignid = contact_lists.campaign ```  ``` campaign_links.messageid = contact_lists.message ``` |
| [messages](#messages) | ``` campaign_links.messageid = messages.id ``` |
| [contact\_emails](#contact-emails) | ``` campaign_links.messageid = contact_emails.messageid ``` |

campaign\_links table schema

|  |
| --- |
| **campaign**  INTEGER |
| **campaignid**  INTEGER |
| **created\_by**  INTEGER |
| **created\_timestamp**  DATE-TIME |
| **id**  INTEGER |
| **link**  STRING |
| **linkclicks**  INTEGER |
| **message**  STRING |
| **messageid**  INTEGER |
| **name**  STRING |
| **ref**  STRING |
| **tracked**  INTEGER |
| **uniquelinkclicks**  INTEGER |
| **updated\_by**  INTEGER |
| **updated\_timestamp**  DATE-TIME |

### campaign\_lists

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |

campaign\_lists table foreign keys

| Join campaign\_lists with | on |
| --- | --- |
| [campaigns](#campaigns) | ``` campaign_lists.campaignid = campaigns.id ```  ``` campaign_lists.userid = campaigns.userid ``` |
| [campaign\_links](#campaign-links) | ``` campaign_lists.campaignid = campaign_links.campaignid ``` |
| [bounce\_logs](#bounce-logs) | ``` campaign_lists.campaignid = bounce_logs.campaignid ``` |
| [campaign\_messages](#campaign-messages) | ``` campaign_lists.campaignid = campaign_messages.campaignid ``` |
| [contact\_lists](#contact-lists) | ``` campaign_lists.campaignid = contact_lists.campaign ```  ``` campaign_lists.listid = contact_lists.list ``` |
| [users](#users) | ``` campaign_lists.userid = users.id ``` |
| [forms](#forms) | ``` campaign_lists.userid = forms.userid ``` |
| [lists](#lists) | ``` campaign_lists.userid = lists.userid ```  ``` campaign_lists.listid = lists.id ``` |
| [messages](#messages) | ``` campaign_lists.userid = messages.userid ``` |
| [saved\_responses](#saved-responses) | ``` campaign_lists.userid = saved_responses.last_sent_user_id ``` |
| [tasks](#tasks) | ``` campaign_lists.userid = tasks.user ``` |
| [templates](#templates) | ``` campaign_lists.userid = templates.userid ``` |
| [activities](#activities) | ``` campaign_lists.userid = activities.userid ``` |
| [configs](#configs) | ``` campaign_lists.userid = configs.userid ``` |
| [contact\_emails](#contact-emails) | ``` campaign_lists.userid = contact_emails.userid ``` |
| [deal\_activities](#deal-activities) | ``` campaign_lists.userid = deal_activities.userid ``` |
| [deal\_group\_users](#deal-group-users) | ``` campaign_lists.userid = deal_group_users.user ``` |
| [email\_activities](#email-activities) | ``` campaign_lists.userid = email_activities.userid ``` |
| [sms](#sms) | ``` campaign_lists.userid = sms.userid ``` |
| [automations](#automations) | ``` campaign_lists.userid = automations.userid ``` |
| [calendars](#calendars) | ``` campaign_lists.userid = calendars.userid ``` |
| [webhooks](#webhooks) | ``` campaign_lists.listid = webhooks.listid ``` |

campaign\_lists table schema

|  |
| --- |
| **campaign**  INTEGER |
| **campaignid**  INTEGER |
| **cdate**  DATE-TIME |
| **id**  INTEGER |
| **list**  INTEGER |
| **list\_amt**  INTEGER |
| **listid**  INTEGER |
| **name**  STRING |
| **udate**  DATE-TIME |
| **user**  INTEGER |
| **userid**  INTEGER |

### campaign\_messages

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |

campaign\_messages table foreign keys

| Join campaign\_messages with | on |
| --- | --- |
| [campaigns](#campaigns) | ``` campaign_messages.campaignid = campaigns.id ``` |
| [campaign\_links](#campaign-links) | ``` campaign_messages.campaignid = campaign_links.campaignid ```  ``` campaign_messages.messageid = campaign_links.messageid ``` |
| [bounce\_logs](#bounce-logs) | ``` campaign_messages.campaignid = bounce_logs.campaignid ```  ``` campaign_messages.messageid = bounce_logs.messageid ``` |
| [campaign\_lists](#campaign-lists) | ``` campaign_messages.campaignid = campaign_lists.campaignid ``` |
| [contact\_lists](#contact-lists) | ``` campaign_messages.campaignid = contact_lists.campaign ```  ``` campaign_messages.messageid = contact_lists.message ``` |
| [messages](#messages) | ``` campaign_messages.messageid = messages.id ``` |
| [contact\_emails](#contact-emails) | ``` campaign_messages.messageid = contact_emails.messageid ``` |

campaign\_messages table schema

|  |
| --- |
| **campaign**  INTEGER |
| **campaignid**  INTEGER |
| **forwards**  INTEGER |
| **hardbounces**  INTEGER |
| **id**  INTEGER |
| **initial\_split\_percentage**  NUMBER |
| **linkclicks**  INTEGER |
| **message**  INTEGER |
| **messageid**  INTEGER |
| **opens**  INTEGER |
| **percentage**  NUMBER |
| **replies**  INTEGER |
| **screenshot**  STRING |
| **send\_amt**  INTEGER |
| **socialshares**  INTEGER |
| **softbounces**  INTEGER |
| **sourcesize**  INTEGER |
| **spamcheck\_max**  INTEGER |
| **spamcheck\_score**  INTEGER |
| **subject**  STRING |
| **subscriberclicks**  INTEGER |
| **total\_amt**  INTEGER |
| **uniqueforwards**  INTEGER |
| **uniquelinkclicks**  INTEGER |
| **uniqueopens**  INTEGER |
| **uniquereplies**  INTEGER |
| **unsubreasons**  INTEGER |
| **unsubscribes**  INTEGER |
| **updates**  INTEGER |

### campaigns

The `campaigns` table contains information about your campaigns in your ActiveCampaign account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_timestamp |
| **Useful links** | [ActiveCampaign documentation](https://developers.activecampaign.com/reference#test-1)  [ActiveCampaign API method](https://developers.activecampaign.com/reference#list-all-campaigns "Opens in new tab: ActiveCampaign API method") |

campaigns table foreign keys

| Join campaigns with | on |
| --- | --- |
| [addresses](#addresses) | ``` campaigns.addressid = addresses.id ``` |
| [forms](#forms) | ``` campaigns.addressid = forms.addressid ```  ``` campaigns.userid = forms.userid ``` |
| [campaign\_links](#campaign-links) | ``` campaigns.id = campaign_links.campaignid ``` |
| [bounce\_logs](#bounce-logs) | ``` campaigns.id = bounce_logs.campaignid ``` |
| [campaign\_lists](#campaign-lists) | ``` campaigns.id = campaign_lists.campaignid ```  ``` campaigns.userid = campaign_lists.userid ``` |
| [campaign\_messages](#campaign-messages) | ``` campaigns.id = campaign_messages.campaignid ``` |
| [contact\_lists](#contact-lists) | ``` campaigns.id = contact_lists.campaign ``` |
| [users](#users) | ``` campaigns.userid = users.id ``` |
| [lists](#lists) | ``` campaigns.userid = lists.userid ``` |
| [messages](#messages) | ``` campaigns.userid = messages.userid ``` |
| [saved\_responses](#saved-responses) | ``` campaigns.userid = saved_responses.last_sent_user_id ``` |
| [tasks](#tasks) | ``` campaigns.userid = tasks.user ``` |
| [templates](#templates) | ``` campaigns.userid = templates.userid ``` |
| [activities](#activities) | ``` campaigns.userid = activities.userid ``` |
| [configs](#configs) | ``` campaigns.userid = configs.userid ``` |
| [contact\_emails](#contact-emails) | ``` campaigns.userid = contact_emails.userid ``` |
| [deal\_activities](#deal-activities) | ``` campaigns.userid = deal_activities.userid ```  ``` campaigns.automation = deal_activities.automation ``` |
| [deal\_group\_users](#deal-group-users) | ``` campaigns.userid = deal_group_users.user ``` |
| [email\_activities](#email-activities) | ``` campaigns.userid = email_activities.userid ``` |
| [sms](#sms) | ``` campaigns.userid = sms.userid ```  ``` campaigns.automation = sms.automation ``` |
| [automations](#automations) | ``` campaigns.userid = automations.userid ```  ``` campaigns.automation = automations.id ``` |
| [calendars](#calendars) | ``` campaigns.userid = calendars.userid ``` |
| [goals](#goals) | ``` campaigns.automation = goals.automation ``` |
| [site\_messages](#site-messages) | ``` campaigns.automation = site_messages.automation ``` |
| [automation\_blocks](#automation-blocks) | ``` campaigns.automation = automation_blocks.automation ``` |
| [contact\_automations](#contact-automations) | ``` campaigns.automation = contact_automations.automation ``` |
| [segments](#segments) | ``` campaigns.segmentid = segments.id ``` |

campaigns table schema

|  |
| --- |
| **activerss\_interval**  STRING |
| **activerss\_items**  INTEGER |
| **activerss\_url**  STRING |
| **addressid**  INTEGER |
| **analytics\_campaign\_name**  STRING |
| **automation**  INTEGER |
| **basemessageid**  INTEGER |
| **basetemplateid**  STRING |
| **bounceid**  INTEGER |
| **cdate**  DATE-TIME |
| **created\_timestamp**  DATE-TIME |
| **deletestamp**  DATE-TIME |
| **embed\_images**  INTEGER |
| **facebook**  INTEGER |
| **formid**  INTEGER |
| **forwards**  INTEGER |
| **hardbounces**  INTEGER |
| **htmlunsub**  INTEGER |
| **htmlunsubdata**  STRING |
| **id**  INTEGER |
| **ip4**  STRING |
| **laststep**  STRING |
| **ldate**  DATE-TIME |
| **linkclicks**  INTEGER |
| **mail\_cleanup**  INTEGER |
| **mail\_send**  INTEGER |
| **mail\_transfer**  INTEGER |
| **mailer\_log\_file**  INTEGER |
| **managetext**  INTEGER |
| **mdate**  DATE-TIME |
| **name**  STRING |
| **opens**  INTEGER |
| **public**  INTEGER |
| **realcid**  INTEGER |
| **recurring**  STRING |
| **reminder\_field**  STRING |
| **reminder\_format**  STRING |
| **reminder\_last\_cron\_run**  STRING |
| **reminder\_offset**  INTEGER |
| **reminder\_offset\_sign**  STRING |
| **reminder\_offset\_type**  STRING |
| **reminder\_type**  STRING |
| **replies**  INTEGER |
| **replysys**  INTEGER |
| **responder\_existing**  INTEGER |
| **responder\_offset**  INTEGER |
| **responder\_type**  STRING |
| **schedule**  INTEGER |
| **scheduleddate**  STRING |
| **sdate**  DATE-TIME |
| **segmentid**  INTEGER |
| **send\_amt**  INTEGER |
| **sendid**  INTEGER |
| **seriesid**  INTEGER |
| **socialshares**  INTEGER |
| **softbounces**  INTEGER |
| **source**  STRING |
| **split\_content**  INTEGER |
| **split\_offset**  INTEGER |
| **split\_offset\_type**  STRING |
| **split\_type**  STRING |
| **split\_winner\_awaiting**  INTEGER |
| **split\_winner\_messageid**  INTEGER |
| **status**  INTEGER |
| **subscriberclicks**  INTEGER |
| **survey**  STRING |
| **textunsub**  INTEGER |
| **textunsubdata**  STRING |
| **threadid**  INTEGER |
| **total\_amt**  INTEGER |
| **tracklinks**  STRING |
| **tracklinksanalytics**  INTEGER |
| **trackreads**  INTEGER |
| **trackreadsanalytics**  INTEGER |
| **tweet**  INTEGER |
| **type**  STRING |
| **uniqueforwards**  INTEGER |
| **uniquelinkclicks**  INTEGER |
| **uniqueopens**  INTEGER |
| **uniquereplies**  INTEGER |
| **unsubreasons**  INTEGER |
| **unsubscribes**  INTEGER |
| **updated\_timestamp**  DATE-TIME |
| **updates**  INTEGER |
| **user**  INTEGER |
| **userid**  INTEGER |
| **waitpreview**  INTEGER |
| **willrecur**  INTEGER |

### configs

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_timestamp |

configs table foreign keys

| Join configs with | on |
| --- | --- |
| [users](#users) | ``` configs.userid = users.id ``` |
| [forms](#forms) | ``` configs.userid = forms.userid ``` |
| [lists](#lists) | ``` configs.userid = lists.userid ``` |
| [messages](#messages) | ``` configs.userid = messages.userid ``` |
| [saved\_responses](#saved-responses) | ``` configs.userid = saved_responses.last_sent_user_id ``` |
| [tasks](#tasks) | ``` configs.userid = tasks.user ``` |
| [templates](#templates) | ``` configs.userid = templates.userid ``` |
| [activities](#activities) | ``` configs.userid = activities.userid ``` |
| [campaign\_lists](#campaign-lists) | ``` configs.userid = campaign_lists.userid ``` |
| [contact\_emails](#contact-emails) | ``` configs.userid = contact_emails.userid ``` |
| [deal\_activities](#deal-activities) | ``` configs.userid = deal_activities.userid ``` |
| [deal\_group\_users](#deal-group-users) | ``` configs.userid = deal_group_users.user ``` |
| [email\_activities](#email-activities) | ``` configs.userid = email_activities.userid ``` |
| [sms](#sms) | ``` configs.userid = sms.userid ``` |
| [automations](#automations) | ``` configs.userid = automations.userid ``` |
| [calendars](#calendars) | ``` configs.userid = calendars.userid ``` |
| [campaigns](#campaigns) | ``` configs.userid = campaigns.userid ``` |

configs table schema

|  |
| --- |
| **cdate**  DATE-TIME |
| **created\_by**  INTEGER |
| **created\_timestamp**  DATE-TIME |
| **id**  INTEGER |
| **item**  STRING |
| **keyname**  STRING |
| **owner**  INTEGER |
| **section**  STRING |
| **udate**  DATE-TIME |
| **updated\_by**  INTEGER |
| **updated\_timestamp**  DATE-TIME |
| **userid**  INTEGER |
| **val**  STRING |

### contact\_automations

The `contact_automations` table contains information about automations in your ActiveCampaign account that you can add contacts to.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Useful links** | [ActiveCampaign documentation](https://developers.activecampaign.com/reference#automations)  [ActiveCampaign API method](https://developers.activecampaign.com/reference#list-all-contact-automations "Opens in new tab: ActiveCampaign API method") |

contact\_automations table foreign keys

| Join contact\_automations with | on |
| --- | --- |
| [contacts](#contacts) | ``` contact_automations.contact = contacts.id ``` |
| [deals](#deals) | ``` contact_automations.contact = deals.contact ``` |
| [forms](#forms) | ``` contact_automations.contact = forms.contacts ``` |
| [bounce\_logs](#bounce-logs) | ``` contact_automations.contact = bounce_logs.contact ``` |
| [contact\_data](#contact-data) | ``` contact_automations.contact = contact_data.contact ``` |
| [contact\_emails](#contact-emails) | ``` contact_automations.contact = contact_emails.contact ``` |
| [contact\_lists](#contact-lists) | ``` contact_automations.contact = contact_lists.contact ``` |
| [contact\_tags](#contact-tags) | ``` contact_automations.contact = contact_tags.contact ``` |
| [contact\_conversions](#contact-conversions) | ``` contact_automations.contact = contact_conversions.contact ``` |
| [email\_activities](#email-activities) | ``` contact_automations.contact = email_activities.contact ``` |
| [account\_contacts](#account-contacts) | ``` contact_automations.contact = account_contacts.contact ``` |
| [contact\_custom\_field\_values](#contact-custom-field-values) | ``` contact_automations.contact = contact_custom_field_values.contact ``` |
| [contact\_deals](#contact-deals) | ``` contact_automations.contact = contact_deals.contact ``` |
| [automations](#automations) | ``` contact_automations.automation = automations.id ``` |
| [deal\_activities](#deal-activities) | ``` contact_automations.automation = deal_activities.automation ``` |
| [goals](#goals) | ``` contact_automations.automation = goals.automation ``` |
| [site\_messages](#site-messages) | ``` contact_automations.automation = site_messages.automation ``` |
| [sms](#sms) | ``` contact_automations.automation = sms.automation ``` |
| [automation\_blocks](#automation-blocks) | ``` contact_automations.automation = automation_blocks.automation ``` |
| [campaigns](#campaigns) | ``` contact_automations.automation = campaigns.automation ``` |

contact\_automations table schema

|  |
| --- |
| **adddate**  DATE-TIME |
| **automation**  INTEGER |
| **batchid**  STRING |
| **complete\_value**  INTEGER |
| **completed**  INTEGER |
| **completed\_elements**  INTEGER |
| **contact**  INTEGER |
| **id**  INTEGER |
| **lastblock**  INTEGER |
| **lastdate**  DATE-TIME |
| **lastlogid**  INTEGER |
| **remdate**  DATE-TIME |
| **seriesid**  INTEGER |
| **startid**  INTEGER |
| **status**  INTEGER |
| **timespan**  INTEGER |
| **total\_elements**  INTEGER |

### contact\_conversions

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | cdate |

contact\_conversions table foreign keys

| Join contact\_conversions with | on |
| --- | --- |
| [contacts](#contacts) | ``` contact_conversions.contact = contacts.id ``` |
| [deals](#deals) | ``` contact_conversions.contact = deals.contact ``` |
| [forms](#forms) | ``` contact_conversions.contact = forms.contacts ``` |
| [bounce\_logs](#bounce-logs) | ``` contact_conversions.contact = bounce_logs.contact ``` |
| [contact\_data](#contact-data) | ``` contact_conversions.contact = contact_data.contact ``` |
| [contact\_emails](#contact-emails) | ``` contact_conversions.contact = contact_emails.contact ``` |
| [contact\_lists](#contact-lists) | ``` contact_conversions.contact = contact_lists.contact ``` |
| [contact\_tags](#contact-tags) | ``` contact_conversions.contact = contact_tags.contact ``` |
| [email\_activities](#email-activities) | ``` contact_conversions.contact = email_activities.contact ``` |
| [account\_contacts](#account-contacts) | ``` contact_conversions.contact = account_contacts.contact ``` |
| [contact\_automations](#contact-automations) | ``` contact_conversions.contact = contact_automations.contact ``` |
| [contact\_custom\_field\_values](#contact-custom-field-values) | ``` contact_conversions.contact = contact_custom_field_values.contact ``` |
| [contact\_deals](#contact-deals) | ``` contact_conversions.contact = contact_deals.contact ``` |
| [conversions](#conversions) | ``` contact_conversions.conversion = conversions.id ``` |
| [conversion\_triggers](#conversion-triggers) | ``` contact_conversions.conversion = conversion_triggers.conversion ```  ``` contact_conversions.conversiontrigger = conversion_triggers.id ``` |

contact\_conversions table schema

|  |
| --- |
| **cdate**  DATE-TIME |
| **contact**  INTEGER |
| **conversion**  INTEGER |
| **conversion\_trigger**  INTEGER |
| **conversiontrigger**  INTEGER |
| **converted\_by**  INTEGER |
| **converted\_by\_id**  INTEGER |
| **converted\_by\_type**  STRING |
| **currency**  STRING |
| **dynamic**  INTEGER |
| **id**  INTEGER |
| **modifier**  STRING |
| **trigger\_type**  STRING |
| **value**  INTEGER |

### contact\_custom\_field\_options

The `contact_custom_field_options` table contains information about custom field options for your contacts in your ActiveCampaign account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [ActiveCampaign documentation](https://developers.activecampaign.com/reference#fields)  [ActiveCampaign API method](https://developers.activecampaign.com/reference#retrieve-fields-1 "Opens in new tab: ActiveCampaign API method") |

contact\_custom\_field\_options table foreign keys

| Join contact\_custom\_field\_options with | on |
| --- | --- |
| [ecommerce\_orders](#ecommerce-orders) | ``` contact_custom_field_options.orderid = ecommerce_orders.id ``` |
| [ecommerce\_order\_products](#ecommerce-order-products) | ``` contact_custom_field_options.orderid = ecommerce_order_products.orderid ``` |
| [ecommerce\_order\_activities](#ecommerce-order-activities) | ``` contact_custom_field_options.orderid = ecommerce_order_activities.orderid ``` |
| [deal\_stages](#deal-stages) | ``` contact_custom_field_options.orderid = deal_stages.order ``` |

contact\_custom\_field\_options table schema

|  |
| --- |
| **cdate**  DATE-TIME |
| **field**  INTEGER |
| **id**  INTEGER |
| **isdefault**  INTEGER |
| **label**  STRING |
| **orderid**  INTEGER |
| **udate**  DATE-TIME |
| **value**  STRING |

### contact\_custom\_field\_rels

The `contact_custom_field_rels` table contains information about custom field relationships for your contacts in your ActiveCampaign account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [ActiveCampaign documentation](https://developers.activecampaign.com/reference#fields)  [ActiveCampaign API method](https://developers.activecampaign.com/reference#retrieve-fields-1 "Opens in new tab: ActiveCampaign API method") |

contact\_custom\_field\_rels table schema

|  |
| --- |
| **cdate**  DATE-TIME |
| **dorder**  INTEGER |
| **field**  INTEGER |
| **id**  INTEGER |
| **relid**  INTEGER |

### contact\_custom\_field\_values

The `contact_custom_field_values` table contains information about custom field values for your contacts in your ActiveCampaign account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | udate |
| **Useful links** | [ActiveCampaign documentation](https://developers.activecampaign.com/reference#fieldvalues)  [ActiveCampaign API method](https://developers.activecampaign.com/reference#list-all-custom-field-values-1 "Opens in new tab: ActiveCampaign API method") |

contact\_custom\_field\_values table foreign keys

| Join contact\_custom\_field\_values with | on |
| --- | --- |
| [contacts](#contacts) | ``` contact_custom_field_values.contact = contacts.id ``` |
| [deals](#deals) | ``` contact_custom_field_values.contact = deals.contact ``` |
| [forms](#forms) | ``` contact_custom_field_values.contact = forms.contacts ``` |
| [bounce\_logs](#bounce-logs) | ``` contact_custom_field_values.contact = bounce_logs.contact ``` |
| [contact\_data](#contact-data) | ``` contact_custom_field_values.contact = contact_data.contact ``` |
| [contact\_emails](#contact-emails) | ``` contact_custom_field_values.contact = contact_emails.contact ``` |
| [contact\_lists](#contact-lists) | ``` contact_custom_field_values.contact = contact_lists.contact ``` |
| [contact\_tags](#contact-tags) | ``` contact_custom_field_values.contact = contact_tags.contact ``` |
| [contact\_conversions](#contact-conversions) | ``` contact_custom_field_values.contact = contact_conversions.contact ``` |
| [email\_activities](#email-activities) | ``` contact_custom_field_values.contact = email_activities.contact ``` |
| [account\_contacts](#account-contacts) | ``` contact_custom_field_values.contact = account_contacts.contact ``` |
| [contact\_automations](#contact-automations) | ``` contact_custom_field_values.contact = contact_automations.contact ``` |
| [contact\_deals](#contact-deals) | ``` contact_custom_field_values.contact = contact_deals.contact ``` |

contact\_custom\_field\_values table schema

|  |
| --- |
| **cdate**  DATE-TIME |
| **contact**  INTEGER |
| **created\_by**  INTEGER |
| **field**  INTEGER |
| **id**  INTEGER |
| **owner**  INTEGER |
| **udate**  DATE-TIME |
| **updated\_by**  INTEGER |
| **value**  STRING |

### contact\_custom\_fields

The `contact_custom_fields` table contains information about custom fields for your contacts in your ActiveCampaign account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [ActiveCampaign documentation](https://developers.activecampaign.com/reference#fields)  [ActiveCampaign API method](https://developers.activecampaign.com/reference#retrieve-fields-1 "Opens in new tab: ActiveCampaign API method") |

contact\_custom\_fields table schema

|  |
| --- |
| **cdate**  DATE-TIME |
| **cols**  INTEGER |
| **defval**  STRING |
| **descript**  STRING |
| **id**  INTEGER |
| **isrequired**  INTEGER |
| **ordernum**  INTEGER |
| **perstag**  STRING |
| **rows**  INTEGER |
| **service**  STRING |
| **show\_in\_list**  INTEGER |
| **title**  STRING |
| **type**  STRING |
| **udate**  DATE-TIME |
| **visible**  INTEGER |

### contact\_data

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | tstamp |

contact\_data table foreign keys

| Join contact\_data with | on |
| --- | --- |
| [contacts](#contacts) | ``` contact_data.contact = contacts.id ``` |
| [deals](#deals) | ``` contact_data.contact = deals.contact ``` |
| [forms](#forms) | ``` contact_data.contact = forms.contacts ``` |
| [bounce\_logs](#bounce-logs) | ``` contact_data.contact = bounce_logs.contact ``` |
| [contact\_emails](#contact-emails) | ``` contact_data.contact = contact_emails.contact ``` |
| [contact\_lists](#contact-lists) | ``` contact_data.contact = contact_lists.contact ``` |
| [contact\_tags](#contact-tags) | ``` contact_data.contact = contact_tags.contact ``` |
| [contact\_conversions](#contact-conversions) | ``` contact_data.contact = contact_conversions.contact ``` |
| [email\_activities](#email-activities) | ``` contact_data.contact = email_activities.contact ``` |
| [account\_contacts](#account-contacts) | ``` contact_data.contact = account_contacts.contact ``` |
| [contact\_automations](#contact-automations) | ``` contact_data.contact = contact_automations.contact ``` |
| [contact\_custom\_field\_values](#contact-custom-field-values) | ``` contact_data.contact = contact_custom_field_values.contact ``` |
| [contact\_deals](#contact-deals) | ``` contact_data.contact = contact_deals.contact ``` |

contact\_data table schema

|  |
| --- |
| **contact**  INTEGER |
| **created\_by**  INTEGER |
| **created\_timestamp**  DATE-TIME |
| **fb\_id**  INTEGER |
| **fb\_name**  STRING |
| **ga\_campaign\_content**  STRING |
| **ga\_campaign\_customsegment**  STRING |
| **ga\_campaign\_medium**  STRING |
| **ga\_campaign\_name**  STRING |
| **ga\_campaign\_source**  STRING |
| **ga\_campaign\_term**  STRING |
| **ga\_first\_visit**  STRING |
| **ga\_times\_visited**  INTEGER |
| **geo\_area**  STRING |
| **geo\_city**  STRING |
| **geo\_country**  STRING |
| **geo\_country2**  STRING |
| **geo\_ip4**  STRING |
| **geo\_lat**  STRING |
| **geo\_lon**  STRING |
| **geo\_state**  STRING |
| **geo\_tstamp**  DATE-TIME |
| **geo\_tz**  STRING |
| **geo\_tz\_offset**  STRING |
| **geo\_zip**  STRING |
| **id**  INTEGER |
| **tstamp**  DATE-TIME |
| **tw\_id**  INTEGER |
| **updated\_by**  INTEGER |
| **updated\_timestamp**  DATE-TIME |

### contact\_deals

The `contact_deals` contains information about secondary contacts associated with a deal in your ActiveCampaign account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_timestamp |
| **Useful links** | [ActiveCampaign documentation](https://developers.activecampaign.com/reference#secondary-contacts)  [ActiveCampaign API method](https://developers.activecampaign.com/reference#list-all-secondary-contacts "Opens in new tab: ActiveCampaign API method") |

contact\_deals table foreign keys

| Join contact\_deals with | on |
| --- | --- |
| [deals](#deals) | ``` contact_deals.deal = deals.id ```  ``` contact_deals.contact = deals.contact ``` |
| [deal\_custom\_field\_values](#deal-custom-field-values) | ``` contact_deals.deal = deal_custom_field_values.deal_id ``` |
| [forms](#forms) | ``` contact_deals.deal = forms.deals ```  ``` contact_deals.contact = forms.contacts ``` |
| [deal\_activities](#deal-activities) | ``` contact_deals.deal = deal_activities.deal ``` |
| [email\_activities](#email-activities) | ``` contact_deals.deal = email_activities.deal ```  ``` contact_deals.contact = email_activities.contact ``` |
| [contact\_emails](#contact-emails) | ``` contact_deals.deal = contact_emails.deal ```  ``` contact_deals.contact = contact_emails.contact ``` |
| [contacts](#contacts) | ``` contact_deals.contact = contacts.id ``` |
| [bounce\_logs](#bounce-logs) | ``` contact_deals.contact = bounce_logs.contact ``` |
| [contact\_data](#contact-data) | ``` contact_deals.contact = contact_data.contact ``` |
| [contact\_lists](#contact-lists) | ``` contact_deals.contact = contact_lists.contact ``` |
| [contact\_tags](#contact-tags) | ``` contact_deals.contact = contact_tags.contact ``` |
| [contact\_conversions](#contact-conversions) | ``` contact_deals.contact = contact_conversions.contact ``` |
| [account\_contacts](#account-contacts) | ``` contact_deals.contact = account_contacts.contact ``` |
| [contact\_automations](#contact-automations) | ``` contact_deals.contact = contact_automations.contact ``` |
| [contact\_custom\_field\_values](#contact-custom-field-values) | ``` contact_deals.contact = contact_custom_field_values.contact ``` |

contact\_deals table schema

|  |
| --- |
| **cdate**  DATE-TIME |
| **contact**  INTEGER |
| **created\_by**  INTEGER |
| **created\_timestamp**  DATE-TIME |
| **deal**  INTEGER |
| **id**  INTEGER |
| **role**  STRING |
| **updated\_by**  INTEGER |
| **updated\_timestamp**  DATE-TIME |

### contact\_emails

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | sdate |

contact\_emails table foreign keys

| Join contact\_emails with | on |
| --- | --- |
| [deals](#deals) | ``` contact_emails.deal = deals.id ```  ``` contact_emails.account = deals.account ```  ``` contact_emails.contact = deals.contact ``` |
| [deal\_custom\_field\_values](#deal-custom-field-values) | ``` contact_emails.deal = deal_custom_field_values.deal_id ``` |
| [contact\_deals](#contact-deals) | ``` contact_emails.deal = contact_deals.deal ```  ``` contact_emails.contact = contact_deals.contact ``` |
| [forms](#forms) | ``` contact_emails.deal = forms.deals ```  ``` contact_emails.contact = forms.contacts ```  ``` contact_emails.userid = forms.userid ``` |
| [deal\_activities](#deal-activities) | ``` contact_emails.deal = deal_activities.deal ```  ``` contact_emails.userid = deal_activities.userid ``` |
| [email\_activities](#email-activities) | ``` contact_emails.deal = email_activities.deal ```  ``` contact_emails.account = email_activities.account ```  ``` contact_emails.contact = email_activities.contact ```  ``` contact_emails.userid = email_activities.userid ``` |
| [accounts](#accounts) | ``` contact_emails.account = accounts.id ``` |
| [account\_contacts](#account-contacts) | ``` contact_emails.account = account_contacts.account ```  ``` contact_emails.contact = account_contacts.contact ``` |
| [account\_custom\_field\_values](#account-custom-field-values) | ``` contact_emails.account = account_custom_field_values.account_id ``` |
| [contacts](#contacts) | ``` contact_emails.contact = contacts.id ``` |
| [bounce\_logs](#bounce-logs) | ``` contact_emails.contact = bounce_logs.contact ```  ``` contact_emails.messageid = bounce_logs.messageid ``` |
| [contact\_data](#contact-data) | ``` contact_emails.contact = contact_data.contact ``` |
| [contact\_lists](#contact-lists) | ``` contact_emails.contact = contact_lists.contact ```  ``` contact_emails.messageid = contact_lists.message ``` |
| [contact\_tags](#contact-tags) | ``` contact_emails.contact = contact_tags.contact ``` |
| [contact\_conversions](#contact-conversions) | ``` contact_emails.contact = contact_conversions.contact ``` |
| [contact\_automations](#contact-automations) | ``` contact_emails.contact = contact_automations.contact ``` |
| [contact\_custom\_field\_values](#contact-custom-field-values) | ``` contact_emails.contact = contact_custom_field_values.contact ``` |
| [users](#users) | ``` contact_emails.userid = users.id ``` |
| [lists](#lists) | ``` contact_emails.userid = lists.userid ``` |
| [messages](#messages) | ``` contact_emails.userid = messages.userid ```  ``` contact_emails.messageid = messages.id ``` |
| [saved\_responses](#saved-responses) | ``` contact_emails.userid = saved_responses.last_sent_user_id ``` |
| [tasks](#tasks) | ``` contact_emails.userid = tasks.user ``` |
| [templates](#templates) | ``` contact_emails.userid = templates.userid ``` |
| [activities](#activities) | ``` contact_emails.userid = activities.userid ``` |
| [campaign\_lists](#campaign-lists) | ``` contact_emails.userid = campaign_lists.userid ``` |
| [configs](#configs) | ``` contact_emails.userid = configs.userid ``` |
| [deal\_group\_users](#deal-group-users) | ``` contact_emails.userid = deal_group_users.user ``` |
| [sms](#sms) | ``` contact_emails.userid = sms.userid ``` |
| [automations](#automations) | ``` contact_emails.userid = automations.userid ``` |
| [calendars](#calendars) | ``` contact_emails.userid = calendars.userid ``` |
| [campaigns](#campaigns) | ``` contact_emails.userid = campaigns.userid ``` |
| [campaign\_messages](#campaign-messages) | ``` contact_emails.messageid = campaign_messages.messageid ``` |
| [campaign\_links](#campaign-links) | ``` contact_emails.messageid = campaign_links.messageid ``` |

contact\_emails table schema

|  |
| --- |
| **account**  INTEGER |
| **contact**  INTEGER |
| **d\_id**  INTEGER |
| **deal**  INTEGER |
| **id**  INTEGER |
| **ip**  STRING |
| **message**  INTEGER |
| **messageheader**  STRING |
| **messageid**  INTEGER |
| **sdate**  DATE-TIME |
| **seriesid**  INTEGER |
| **source**  STRING |
| **subscriberid**  INTEGER |
| **user**  INTEGER |
| **userid**  INTEGER |

### contact\_lists

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_timestamp |

contact\_lists table foreign keys

| Join contact\_lists with | on |
| --- | --- |
| [campaigns](#campaigns) | ``` contact_lists.campaign = campaigns.id ``` |
| [campaign\_links](#campaign-links) | ``` contact_lists.campaign = campaign_links.campaignid ```  ``` contact_lists.message = campaign_links.messageid ``` |
| [bounce\_logs](#bounce-logs) | ``` contact_lists.campaign = bounce_logs.campaignid ```  ``` contact_lists.contact = bounce_logs.contact ```  ``` contact_lists.message = bounce_logs.messageid ``` |
| [campaign\_lists](#campaign-lists) | ``` contact_lists.campaign = campaign_lists.campaignid ```  ``` contact_lists.list = campaign_lists.listid ``` |
| [campaign\_messages](#campaign-messages) | ``` contact_lists.campaign = campaign_messages.campaignid ```  ``` contact_lists.message = campaign_messages.messageid ``` |
| [contacts](#contacts) | ``` contact_lists.contact = contacts.id ``` |
| [deals](#deals) | ``` contact_lists.contact = deals.contact ``` |
| [forms](#forms) | ``` contact_lists.contact = forms.contacts ```  ``` contact_lists.form = forms.id ``` |
| [contact\_data](#contact-data) | ``` contact_lists.contact = contact_data.contact ``` |
| [contact\_emails](#contact-emails) | ``` contact_lists.contact = contact_emails.contact ```  ``` contact_lists.message = contact_emails.messageid ``` |
| [contact\_tags](#contact-tags) | ``` contact_lists.contact = contact_tags.contact ``` |
| [contact\_conversions](#contact-conversions) | ``` contact_lists.contact = contact_conversions.contact ``` |
| [email\_activities](#email-activities) | ``` contact_lists.contact = email_activities.contact ``` |
| [account\_contacts](#account-contacts) | ``` contact_lists.contact = account_contacts.contact ``` |
| [contact\_automations](#contact-automations) | ``` contact_lists.contact = contact_automations.contact ``` |
| [contact\_custom\_field\_values](#contact-custom-field-values) | ``` contact_lists.contact = contact_custom_field_values.contact ``` |
| [contact\_deals](#contact-deals) | ``` contact_lists.contact = contact_deals.contact ``` |
| [lists](#lists) | ``` contact_lists.list = lists.id ``` |
| [webhooks](#webhooks) | ``` contact_lists.list = webhooks.listid ``` |
| [messages](#messages) | ``` contact_lists.message = messages.id ``` |

contact\_lists table schema

|  |
| --- |
| **automation**  INTEGER |
| **autosync\_log**  INTEGER |
| **campaign**  INTEGER |
| **contact**  INTEGER |
| **created\_by**  INTEGER |
| **created\_timestamp**  DATE-TIME |
| **first\_name**  STRING |
| **form**  INTEGER |
| **id**  INTEGER |
| **ip4\_last**  INTEGER |
| **ip\_4sub**  INTEGER |
| **ip\_4unsub**  INTEGER |
| **last\_name**  STRING |
| **list**  INTEGER |
| **message**  INTEGER |
| **responder**  INTEGER |
| **sdate**  DATE-TIME |
| **seriesid**  INTEGER |
| **sourceid**  INTEGER |
| **status**  INTEGER |
| **sync**  INTEGER |
| **udate**  DATE-TIME |
| **unsubreason**  STRING |
| **unsubscribe\_automation**  INTEGER |
| **updated\_by**  INTEGER |
| **updated\_timestamp**  DATE-TIME |

### contact\_tags

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_timestamp |

contact\_tags table foreign keys

| Join contact\_tags with | on |
| --- | --- |
| [contacts](#contacts) | ``` contact_tags.contact = contacts.id ``` |
| [deals](#deals) | ``` contact_tags.contact = deals.contact ``` |
| [forms](#forms) | ``` contact_tags.contact = forms.contacts ``` |
| [bounce\_logs](#bounce-logs) | ``` contact_tags.contact = bounce_logs.contact ``` |
| [contact\_data](#contact-data) | ``` contact_tags.contact = contact_data.contact ``` |
| [contact\_emails](#contact-emails) | ``` contact_tags.contact = contact_emails.contact ``` |
| [contact\_lists](#contact-lists) | ``` contact_tags.contact = contact_lists.contact ``` |
| [contact\_conversions](#contact-conversions) | ``` contact_tags.contact = contact_conversions.contact ``` |
| [email\_activities](#email-activities) | ``` contact_tags.contact = email_activities.contact ``` |
| [account\_contacts](#account-contacts) | ``` contact_tags.contact = account_contacts.contact ``` |
| [contact\_automations](#contact-automations) | ``` contact_tags.contact = contact_automations.contact ``` |
| [contact\_custom\_field\_values](#contact-custom-field-values) | ``` contact_tags.contact = contact_custom_field_values.contact ``` |
| [contact\_deals](#contact-deals) | ``` contact_tags.contact = contact_deals.contact ``` |
| [tags](#tags) | ``` contact_tags.tag = tags.id ``` |

contact\_tags table schema

|  |
| --- |
| **cdate**  DATE-TIME |
| **contact**  INTEGER |
| **created\_by**  INTEGER |
| **created\_timestamp**  DATE-TIME |
| **id**  INTEGER |
| **tag**  INTEGER |
| **updated\_by**  INTEGER |
| **updated\_timestamp**  DATE-TIME |

### contacts

The `contacts` table contains information about the people that you market or sell to in your ActiveCampaign account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_timestamp |
| **Useful links** | [ActiveCampaign documentation](https://developers.activecampaign.com/reference#contact)  [ActiveCampaign API method](https://developers.activecampaign.com/reference#list-all-contacts "Opens in new tab: ActiveCampaign API method") |

contacts table foreign keys

| Join contacts with | on |
| --- | --- |
| [deals](#deals) | ``` contacts.id = deals.contact ``` |
| [forms](#forms) | ``` contacts.id = forms.contacts ``` |
| [bounce\_logs](#bounce-logs) | ``` contacts.id = bounce_logs.contact ``` |
| [contact\_data](#contact-data) | ``` contacts.id = contact_data.contact ``` |
| [contact\_emails](#contact-emails) | ``` contacts.id = contact_emails.contact ``` |
| [contact\_lists](#contact-lists) | ``` contacts.id = contact_lists.contact ``` |
| [contact\_tags](#contact-tags) | ``` contacts.id = contact_tags.contact ``` |
| [contact\_conversions](#contact-conversions) | ``` contacts.id = contact_conversions.contact ``` |
| [email\_activities](#email-activities) | ``` contacts.id = email_activities.contact ``` |
| [account\_contacts](#account-contacts) | ``` contacts.id = account_contacts.contact ``` |
| [contact\_automations](#contact-automations) | ``` contacts.id = contact_automations.contact ``` |
| [contact\_custom\_field\_values](#contact-custom-field-values) | ``` contacts.id = contact_custom_field_values.contact ``` |
| [contact\_deals](#contact-deals) | ``` contacts.id = contact_deals.contact ``` |

contacts table schema

|  |
| --- |
| **account\_contacts**  ARRAY |
| **adate**  DATE-TIME |
| **anonymized**  INTEGER |
| **bounced\_date**  STRING |
| **bounced\_hard**  INTEGER |
| **bounced\_soft**  INTEGER |
| **cdate**  DATE-TIME |
| **created\_by**  INTEGER |
| **created\_timestamp**  DATE-TIME |
| **created\_utc\_timestamp**  DATE-TIME |
| **deleted**  INTEGER |
| **deleted\_at**  DATE-TIME |
| **edate**  DATE-TIME |
| **email**  STRING |
| **email\_domain**  STRING |
| **email\_empty**  BOOLEAN |
| **email\_local**  STRING |
| **first\_name**  STRING |
| **gravatar**  INTEGER |
| **hash**  STRING |
| **id**  INTEGER |
| **ip**  STRING |
| **last\_name**  STRING |
| **organization**  INTEGER |
| **orgid**  INTEGER |
| **phone**  STRING |
| **rating\_tstamp**  STRING |
| **score\_values**  ARRAY |
| **segmentio\_id**  STRING |
| **sentcnt**  INTEGER |
| **socialdata\_lastcheck**  DATE-TIME |
| **ua**  STRING |
| **udate**  DATE-TIME |
| **updated\_by**  INTEGER |
| **updated\_timestamp**  DATE-TIME |
| **updated\_utc\_timestamp**  DATE-TIME |

### conversion\_triggers

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | udate |

conversion\_triggers table foreign keys

| Join conversion\_triggers with | on |
| --- | --- |
| [conversions](#conversions) | ``` conversion_triggers.conversion = conversions.id ``` |
| [contact\_conversions](#contact-conversions) | ``` conversion_triggers.conversion = contact_conversions.conversion ```  ``` conversion_triggers.id = contact_conversions.conversiontrigger ``` |

conversion\_triggers table schema

|  |
| --- |
| **automation\_block**  INTEGER |
| **cdate**  DATE-TIME |
| **conversion**  INTEGER |
| **dynamic**  INTEGER |
| **id**  INTEGER |
| **modifier**  STRING |
| **retroactive**  INTEGER |
| **trigger\_type**  STRING |
| **udate**  DATE-TIME |
| **value**  STRING |

### conversions

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | udate |

conversions table foreign keys

| Join conversions with | on |
| --- | --- |
| [contact\_conversions](#contact-conversions) | ``` conversions.id = contact_conversions.conversion ``` |
| [conversion\_triggers](#conversion-triggers) | ``` conversions.id = conversion_triggers.conversion ``` |

conversions table schema

|  |
| --- |
| **cdate**  DATE-TIME |
| **currency**  STRING |
| **enforcelimit**  INTEGER |
| **id**  INTEGER |
| **limit**  INTEGER |
| **name**  STRING |
| **udate**  DATE-TIME |
| **value**  INTEGER |

### deal\_activities

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | cdate |

deal\_activities table foreign keys

| Join deal\_activities with | on |
| --- | --- |
| [deals](#deals) | ``` deal_activities.deal = deals.id ```  ``` deal_activities.stage = deals.stage ``` |
| [deal\_custom\_field\_values](#deal-custom-field-values) | ``` deal_activities.deal = deal_custom_field_values.deal_id ``` |
| [contact\_deals](#contact-deals) | ``` deal_activities.deal = contact_deals.deal ``` |
| [forms](#forms) | ``` deal_activities.deal = forms.deals ```  ``` deal_activities.userid = forms.userid ``` |
| [email\_activities](#email-activities) | ``` deal_activities.deal = email_activities.deal ```  ``` deal_activities.userid = email_activities.userid ``` |
| [contact\_emails](#contact-emails) | ``` deal_activities.deal = contact_emails.deal ```  ``` deal_activities.userid = contact_emails.userid ``` |
| [deal\_stages](#deal-stages) | ``` deal_activities.stage = deal_stages.id ``` |
| [deal\_groups](#deal-groups) | ``` deal_activities.stage = deal_groups.stages ``` |
| [users](#users) | ``` deal_activities.userid = users.id ``` |
| [lists](#lists) | ``` deal_activities.userid = lists.userid ``` |
| [messages](#messages) | ``` deal_activities.userid = messages.userid ``` |
| [saved\_responses](#saved-responses) | ``` deal_activities.userid = saved_responses.last_sent_user_id ``` |
| [tasks](#tasks) | ``` deal_activities.userid = tasks.user ``` |
| [templates](#templates) | ``` deal_activities.userid = templates.userid ``` |
| [activities](#activities) | ``` deal_activities.userid = activities.userid ``` |
| [campaign\_lists](#campaign-lists) | ``` deal_activities.userid = campaign_lists.userid ``` |
| [configs](#configs) | ``` deal_activities.userid = configs.userid ``` |
| [deal\_group\_users](#deal-group-users) | ``` deal_activities.userid = deal_group_users.user ``` |
| [sms](#sms) | ``` deal_activities.userid = sms.userid ```  ``` deal_activities.automation = sms.automation ``` |
| [automations](#automations) | ``` deal_activities.userid = automations.userid ```  ``` deal_activities.automation = automations.id ``` |
| [calendars](#calendars) | ``` deal_activities.userid = calendars.userid ``` |
| [campaigns](#campaigns) | ``` deal_activities.userid = campaigns.userid ```  ``` deal_activities.automation = campaigns.automation ``` |
| [goals](#goals) | ``` deal_activities.automation = goals.automation ``` |
| [site\_messages](#site-messages) | ``` deal_activities.automation = site_messages.automation ``` |
| [automation\_blocks](#automation-blocks) | ``` deal_activities.automation = automation_blocks.automation ``` |
| [contact\_automations](#contact-automations) | ``` deal_activities.automation = contact_automations.automation ``` |

deal\_activities table schema

|  |
| --- |
| **automation**  INTEGER |
| **cdate**  DATE-TIME |
| **d\_id**  INTEGER |
| **d\_stageid**  INTEGER |
| **data\_action**  STRING |
| **data\_id**  INTEGER |
| **data\_oldval**  STRING |
| **data\_type**  STRING |
| **deal**  INTEGER |
| **deleted**  INTEGER |
| **id**  INTEGER |
| **is\_addtask**  INTEGER |
| **seriesid**  INTEGER |
| **sortdate**  DATE-TIME |
| **stage**  INTEGER |
| **user**  INTEGER |
| **userid**  INTEGER |

### deal\_custom\_field\_values

The `deal_custom_field_values` table contains information about custom field values for deals in your ActiveCampaign account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_timestamp |
| **Useful links** | [ActiveCampaign documentation](https://developers.activecampaign.com/reference#dealcustomfielddata)  [ActiveCampaign API method](https://developers.activecampaign.com/reference#list-all-custom-field-values "Opens in new tab: ActiveCampaign API method") |

deal\_custom\_field\_values table foreign keys

| Join deal\_custom\_field\_values with | on |
| --- | --- |
| [deal\_custom\_fields](#deal-custom-fields) | ``` deal_custom_field_values.custom_field_id = deal_custom_fields.id ``` |
| [deals](#deals) | ``` deal_custom_field_values.deal_id = deals.id ``` |
| [contact\_deals](#contact-deals) | ``` deal_custom_field_values.deal_id = contact_deals.deal ``` |
| [forms](#forms) | ``` deal_custom_field_values.deal_id = forms.deals ``` |
| [deal\_activities](#deal-activities) | ``` deal_custom_field_values.deal_id = deal_activities.deal ``` |
| [email\_activities](#email-activities) | ``` deal_custom_field_values.deal_id = email_activities.deal ``` |
| [contact\_emails](#contact-emails) | ``` deal_custom_field_values.deal_id = contact_emails.deal ``` |

deal\_custom\_field\_values table schema

|  |
| --- |
| **created\_timestamp**  DATE-TIME |
| **custom\_field\_id**  INTEGER |
| **deal\_custom\_field\_metum\_id**  INTEGER |
| **deal\_id**  INTEGER |
| **field\_value**  STRING |
| **id**  INTEGER |
| **updated\_timestamp**  DATE-TIME |

### deal\_custom\_fields

The `deal_custom_fields` table contains information about custom fields for deals in your ActiveCampaign account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_timestamp |
| **Useful links** | [ActiveCampaign documentation](https://developers.activecampaign.com/reference#dealcustomfieldmeta)  [ActiveCampaign API method](https://developers.activecampaign.com/reference#retrieve-all-dealcustomfielddata-resources "Opens in new tab: ActiveCampaign API method") |

deal\_custom\_fields table foreign keys

| Join deal\_custom\_fields with | on |
| --- | --- |
| [deal\_custom\_field\_values](#deal-custom-field-values) | ``` deal_custom_fields.id = deal_custom_field_values.custom_field_id ``` |

deal\_custom\_fields table schema

|  |
| --- |
| **created\_timestamp**  DATE-TIME |
| **display\_order**  INTEGER |
| **field\_default**  STRING |
| **field\_default\_currency**  STRING |
| **field\_label**  STRING |
| **field\_options**  ARRAY |
| **field\_type**  STRING |
| **hide\_field\_flag**  BOOLEAN |
| **id**  INTEGER |
| **is\_form\_visible**  BOOLEAN |
| **is\_required**  BOOLEAN |
| **known\_field\_id**  INTEGER |
| **personalization**  STRING |
| **updated\_timestamp**  DATE-TIME |

### deal\_group\_users

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |

deal\_group\_users table foreign keys

| Join deal\_group\_users with | on |
| --- | --- |
| [deal\_groups](#deal-groups) | ``` deal_group_users.deal_group = deal_groups.id ``` |
| [deals](#deals) | ``` deal_group_users.deal_group = deals.group ``` |
| [deal\_stages](#deal-stages) | ``` deal_group_users.deal_group = deal_stages.group ``` |
| [users](#users) | ``` deal_group_users.user = users.id ``` |
| [forms](#forms) | ``` deal_group_users.user = forms.userid ``` |
| [lists](#lists) | ``` deal_group_users.user = lists.userid ``` |
| [messages](#messages) | ``` deal_group_users.user = messages.userid ``` |
| [saved\_responses](#saved-responses) | ``` deal_group_users.user = saved_responses.last_sent_user_id ``` |
| [tasks](#tasks) | ``` deal_group_users.user = tasks.user ``` |
| [templates](#templates) | ``` deal_group_users.user = templates.userid ``` |
| [activities](#activities) | ``` deal_group_users.user = activities.userid ``` |
| [campaign\_lists](#campaign-lists) | ``` deal_group_users.user = campaign_lists.userid ``` |
| [configs](#configs) | ``` deal_group_users.user = configs.userid ``` |
| [contact\_emails](#contact-emails) | ``` deal_group_users.user = contact_emails.userid ``` |
| [deal\_activities](#deal-activities) | ``` deal_group_users.user = deal_activities.userid ``` |
| [email\_activities](#email-activities) | ``` deal_group_users.user = email_activities.userid ``` |
| [sms](#sms) | ``` deal_group_users.user = sms.userid ``` |
| [automations](#automations) | ``` deal_group_users.user = automations.userid ``` |
| [calendars](#calendars) | ``` deal_group_users.user = calendars.userid ``` |
| [campaigns](#campaigns) | ``` deal_group_users.user = campaigns.userid ``` |

deal\_group\_users table schema

|  |
| --- |
| **cdate**  DATE-TIME |
| **deal\_group**  INTEGER |
| **id**  INTEGER |
| **user**  INTEGER |

### deal\_groups

The `deal_groups` table contains information about deal pipelines in your ActiveCampaign account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | udate |
| **Useful links** | [ActiveCampaign documentation](https://developers.activecampaign.com/reference#pipelines)  [ActiveCampaign API method](https://developers.activecampaign.com/reference#list-all-pipelines "Opens in new tab: ActiveCampaign API method") |

deal\_groups table foreign keys

| Join deal\_groups with | on |
| --- | --- |
| [deal\_stages](#deal-stages) | ``` deal_groups.stages = deal_stages.id ```  ``` deal_groups.id = deal_stages.group ``` |
| [deals](#deals) | ``` deal_groups.stages = deals.stage ```  ``` deal_groups.id = deals.group ``` |
| [deal\_activities](#deal-activities) | ``` deal_groups.stages = deal_activities.stage ``` |
| [deal\_group\_users](#deal-group-users) | ``` deal_groups.id = deal_group_users.deal_group ``` |

deal\_groups table schema

|  |
| --- |
| **allgroups**  STRING |
| **allusers**  STRING |
| **autoassign**  STRING |
| **cdate**  DATE-TIME |
| **currency**  STRING |
| **id**  INTEGER |
| **stages**  ARRAY |
| **title**  STRING |
| **udate**  DATE-TIME |

### deal\_stages

The `deal_stages` table contains information about grouped deals within a pipeline in your ActiveCampaign account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | udate |
| **Useful links** | [ActiveCampaign documentation](https://developers.activecampaign.com/reference#deal-stages)  [ActiveCampaign API method](https://developers.activecampaign.com/reference#list-all-deal-stages "Opens in new tab: ActiveCampaign API method") |

deal\_stages table foreign keys

| Join deal\_stages with | on |
| --- | --- |
| [deals](#deals) | ``` deal_stages.id = deals.stage ```  ``` deal_stages.group = deals.group ``` |
| [deal\_groups](#deal-groups) | ``` deal_stages.id = deal_groups.stages ```  ``` deal_stages.group = deal_groups.id ``` |
| [deal\_activities](#deal-activities) | ``` deal_stages.id = deal_activities.stage ``` |
| [deal\_group\_users](#deal-group-users) | ``` deal_stages.group = deal_group_users.deal_group ``` |
| [ecommerce\_orders](#ecommerce-orders) | ``` deal_stages.order = ecommerce_orders.id ``` |
| [ecommerce\_order\_products](#ecommerce-order-products) | ``` deal_stages.order = ecommerce_order_products.orderid ``` |
| [ecommerce\_order\_activities](#ecommerce-order-activities) | ``` deal_stages.order = ecommerce_order_activities.orderid ``` |
| [contact\_custom\_field\_options](#contact-custom-field-options) | ``` deal_stages.order = contact_custom_field_options.orderid ``` |

deal\_stages table schema

|  |
| --- |
| **card\_region1**  STRING |
| **card\_region2**  STRING |
| **card\_region3**  STRING |
| **card\_region4**  STRING |
| **card\_region5**  STRING |
| **cdate**  DATE-TIME |
| **color**  STRING |
| **deal\_order**  STRING |
| **group**  INTEGER |
| **id**  INTEGER |
| **order**  INTEGER |
| **title**  STRING |
| **udate**  DATE-TIME |
| **width**  INTEGER |

### deals

The `deals` table contains information about deals in your ActiveCampaign account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | mdate |
| **Useful links** | [ActiveCampaign documentation](https://developers.activecampaign.com/reference#deal)  [ActiveCampaign API method](https://developers.activecampaign.com/reference#list-all-deals "Opens in new tab: ActiveCampaign API method") |

deals table foreign keys

| Join deals with | on |
| --- | --- |
| [deal\_custom\_field\_values](#deal-custom-field-values) | ``` deals.id = deal_custom_field_values.deal_id ``` |
| [contact\_deals](#contact-deals) | ``` deals.id = contact_deals.deal ```  ``` deals.contact = contact_deals.contact ``` |
| [forms](#forms) | ``` deals.id = forms.deals ```  ``` deals.contact = forms.contacts ``` |
| [deal\_activities](#deal-activities) | ``` deals.id = deal_activities.deal ```  ``` deals.stage = deal_activities.stage ``` |
| [email\_activities](#email-activities) | ``` deals.id = email_activities.deal ```  ``` deals.account = email_activities.account ```  ``` deals.contact = email_activities.contact ``` |
| [contact\_emails](#contact-emails) | ``` deals.id = contact_emails.deal ```  ``` deals.account = contact_emails.account ```  ``` deals.contact = contact_emails.contact ``` |
| [deal\_stages](#deal-stages) | ``` deals.stage = deal_stages.id ```  ``` deals.group = deal_stages.group ``` |
| [deal\_groups](#deal-groups) | ``` deals.stage = deal_groups.stages ```  ``` deals.group = deal_groups.id ``` |
| [deal\_group\_users](#deal-group-users) | ``` deals.group = deal_group_users.deal_group ``` |
| [accounts](#accounts) | ``` deals.account = accounts.id ``` |
| [account\_contacts](#account-contacts) | ``` deals.account = account_contacts.account ```  ``` deals.contact = account_contacts.contact ``` |
| [account\_custom\_field\_values](#account-custom-field-values) | ``` deals.account = account_custom_field_values.account_id ``` |
| [contacts](#contacts) | ``` deals.contact = contacts.id ``` |
| [bounce\_logs](#bounce-logs) | ``` deals.contact = bounce_logs.contact ``` |
| [contact\_data](#contact-data) | ``` deals.contact = contact_data.contact ``` |
| [contact\_lists](#contact-lists) | ``` deals.contact = contact_lists.contact ``` |
| [contact\_tags](#contact-tags) | ``` deals.contact = contact_tags.contact ``` |
| [contact\_conversions](#contact-conversions) | ``` deals.contact = contact_conversions.contact ``` |
| [contact\_automations](#contact-automations) | ``` deals.contact = contact_automations.contact ``` |
| [contact\_custom\_field\_values](#contact-custom-field-values) | ``` deals.contact = contact_custom_field_values.contact ``` |

deals table schema

|  |
| --- |
| **account**  INTEGER |
| **activitycount**  INTEGER |
| **cdate**  DATE-TIME |
| **contact**  INTEGER |
| **currency**  STRING |
| **customer\_account**  INTEGER |
| **description**  STRING |
| **edate**  DATE-TIME |
| **group**  INTEGER |
| **hash**  STRING |
| **id**  INTEGER |
| **is\_disabled**  BOOLEAN |
| **mdate**  DATE-TIME |
| **next\_task**  INTEGER |
| **nextdate**  STRING |
| **nextdealid**  INTEGER |
| **nexttaskid**  INTEGER |
| **organization**  INTEGER |
| **owner**  INTEGER |
| **percent**  NUMBER |
| **stage**  INTEGER |
| **status**  INTEGER |
| **title**  STRING |
| **value**  NUMBER |
| **win\_probability**  NUMBER |
| **win\_probability\_mdate**  DATE-TIME |

### ecommerce\_connections

The `ecommerce_connections` table contains information about accounts within your ActiveCampaign account that are linked to an external e-commerce service.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | udate |
| **Useful links** | [ActiveCampaign documentation](https://developers.activecampaign.com/reference#connections)  [ActiveCampaign API method](https://developers.activecampaign.com/reference#list-all-connections "Opens in new tab: ActiveCampaign API method") |

ecommerce\_connections table foreign keys

| Join ecommerce\_connections with | on |
| --- | --- |
| [ecommerce\_customers](#ecommerce-customers) | ``` ecommerce_connections.id = ecommerce_customers.connectionid ``` |
| [ecommerce\_orders](#ecommerce-orders) | ``` ecommerce_connections.id = ecommerce_orders.connectionid ``` |
| [ecommerce\_order\_products](#ecommerce-order-products) | ``` ecommerce_connections.id = ecommerce_order_products.connectionid ``` |
| [ecommerce\_order\_activities](#ecommerce-order-activities) | ``` ecommerce_connections.id = ecommerce_order_activities.connectionid ``` |

ecommerce\_connections table schema

|  |
| --- |
| **cdate**  DATE-TIME |
| **externalid**  STRING |
| **id**  INTEGER |
| **is\_internal**  INTEGER |
| **last\_sync**  DATE-TIME |
| **link\_url**  STRING |
| **logo\_url**  STRING |
| **name**  STRING |
| **service**  STRING |
| **status**  INTEGER |
| **sync\_status**  INTEGER |
| **udate**  DATE-TIME |

### ecommerce\_customers

The `ecommerce_customers` table contains the aggregated e-commerce data from customers in your ActiveCampaign account who are using an external e-commerce service.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | tstamp |
| **Useful links** | [ActiveCampaign documentation](https://developers.activecampaign.com/reference#customers)  [ActiveCampaign API method](https://developers.activecampaign.com/reference#list-all-customers "Opens in new tab: ActiveCampaign API method") |

ecommerce\_customers table foreign keys

| Join ecommerce\_customers with | on |
| --- | --- |
| [ecommerce\_connections](#ecommerce-connections) | ``` ecommerce_customers.connectionid = ecommerce_connections.id ``` |
| [ecommerce\_orders](#ecommerce-orders) | ``` ecommerce_customers.connectionid = ecommerce_orders.connectionid ```  ``` ecommerce_customers.id = ecommerce_orders.customer ``` |
| [ecommerce\_order\_products](#ecommerce-order-products) | ``` ecommerce_customers.connectionid = ecommerce_order_products.connectionid ``` |
| [ecommerce\_order\_activities](#ecommerce-order-activities) | ``` ecommerce_customers.connectionid = ecommerce_order_activities.connectionid ```  ``` ecommerce_customers.id = ecommerce_order_activities.customerid ``` |

ecommerce\_customers table schema

|  |
| --- |
| **avg\_product\_category**  STRING |
| **avg\_revenue\_per\_order**  NUMBER |
| **connection**  INTEGER |
| **connectionid**  INTEGER |
| **email**  STRING |
| **externalid**  STRING |
| **id**  INTEGER |
| **total\_orders**  INTEGER |
| **total\_products**  INTEGER |
| **total\_revenue**  NUMBER |
| **tstamp**  DATE-TIME |

### ecommerce\_order\_activities

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_date |

ecommerce\_order\_activities table foreign keys

| Join ecommerce\_order\_activities with | on |
| --- | --- |
| [ecommerce\_connections](#ecommerce-connections) | ``` ecommerce_order_activities.connectionid = ecommerce_connections.id ``` |
| [ecommerce\_customers](#ecommerce-customers) | ``` ecommerce_order_activities.connectionid = ecommerce_customers.connectionid ```  ``` ecommerce_order_activities.customerid = ecommerce_customers.id ``` |
| [ecommerce\_orders](#ecommerce-orders) | ``` ecommerce_order_activities.connectionid = ecommerce_orders.connectionid ```  ``` ecommerce_order_activities.customerid = ecommerce_orders.customer ```  ``` ecommerce_order_activities.orderid = ecommerce_orders.id ``` |
| [ecommerce\_order\_products](#ecommerce-order-products) | ``` ecommerce_order_activities.connectionid = ecommerce_order_products.connectionid ```  ``` ecommerce_order_activities.orderid = ecommerce_order_products.orderid ``` |
| [contact\_custom\_field\_options](#contact-custom-field-options) | ``` ecommerce_order_activities.orderid = contact_custom_field_options.orderid ``` |
| [deal\_stages](#deal-stages) | ``` ecommerce_order_activities.orderid = deal_stages.order ``` |

ecommerce\_order\_activities table schema

|  |
| --- |
| **abandoned\_date**  DATE-TIME |
| **connection**  INTEGER |
| **connectionid**  INTEGER |
| **created\_date**  DATE-TIME |
| **currency**  STRING |
| **customerid**  INTEGER |
| **discount\_amount**  NUMBER |
| **email**  STRING |
| **external\_created\_date**  DATE-TIME |
| **external\_updated\_date**  DATE-TIME |
| **externalcheckoutid**  STRING |
| **externalid**  STRING |
| **id**  INTEGER |
| **logo\_url**  STRING |
| **order**  INTEGER |
| **order\_number**  STRING |
| **order\_url**  STRING |
| **orderid**  INTEGER |
| **shipping\_amount**  NUMBER |
| **shipping\_method**  STRING |
| **source**  INTEGER |
| **state**  INTEGER |
| **store\_name**  STRING |
| **tax\_amount**  NUMBER |
| **total\_price**  NUMBER |
| **total\_products**  INTEGER |
| **updated\_date**  DATE-TIME |

### ecommerce\_order\_products

The `ecommerce_order_products` table contains lists of products for e-commerce orders in your ActiveCampaign account that come from external services. This is a child table of `ecommerce_order_products`.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [ActiveCampaign documentation](https://developers.activecampaign.com/reference#e-commerce-order-products)  [ActiveCampaign API method](https://developers.activecampaign.com/reference#list-products-for-order "Opens in new tab: ActiveCampaign API method") |

ecommerce\_order\_products table foreign keys

| Join ecommerce\_order\_products with | on |
| --- | --- |
| [ecommerce\_connections](#ecommerce-connections) | ``` ecommerce_order_products.connectionid = ecommerce_connections.id ``` |
| [ecommerce\_customers](#ecommerce-customers) | ``` ecommerce_order_products.connectionid = ecommerce_customers.connectionid ``` |
| [ecommerce\_orders](#ecommerce-orders) | ``` ecommerce_order_products.connectionid = ecommerce_orders.connectionid ```  ``` ecommerce_order_products.orderid = ecommerce_orders.id ``` |
| [ecommerce\_order\_activities](#ecommerce-order-activities) | ``` ecommerce_order_products.connectionid = ecommerce_order_activities.connectionid ```  ``` ecommerce_order_products.orderid = ecommerce_order_activities.orderid ``` |
| [contact\_custom\_field\_options](#contact-custom-field-options) | ``` ecommerce_order_products.orderid = contact_custom_field_options.orderid ``` |
| [deal\_stages](#deal-stages) | ``` ecommerce_order_products.orderid = deal_stages.order ``` |

ecommerce\_order\_products table schema

|  |
| --- |
| **category**  STRING |
| **connectionid**  INTEGER |
| **created\_date**  DATE-TIME |
| **description**  STRING |
| **ecom\_order**  INTEGER |
| **externalid**  STRING |
| **id**  INTEGER |
| **image\_url**  STRING |
| **name**  STRING |
| **orderid**  INTEGER |
| **price**  NUMBER |
| **product\_url**  STRING |
| **quantity**  INTEGER |
| **sku**  STRING |
| **tstamp**  DATE-TIME |
| **updated\_date**  DATE-TIME |

### ecommerce\_orders

The `ecommerce_orders` table contains information about your ActiveCampaign account’s customer orders using an external e-commerce service.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_date |
| **Useful links** | [ActiveCampaign documentation](https://developers.activecampaign.com/reference#orders)  [ActiveCampaign API method](https://developers.activecampaign.com/reference#list-all-orders "Opens in new tab: ActiveCampaign API method") |

ecommerce\_orders table foreign keys

| Join ecommerce\_orders with | on |
| --- | --- |
| [ecommerce\_connections](#ecommerce-connections) | ``` ecommerce_orders.connectionid = ecommerce_connections.id ``` |
| [ecommerce\_customers](#ecommerce-customers) | ``` ecommerce_orders.connectionid = ecommerce_customers.connectionid ```  ``` ecommerce_orders.customer = ecommerce_customers.id ``` |
| [ecommerce\_order\_products](#ecommerce-order-products) | ``` ecommerce_orders.connectionid = ecommerce_order_products.connectionid ```  ``` ecommerce_orders.id = ecommerce_order_products.orderid ``` |
| [ecommerce\_order\_activities](#ecommerce-order-activities) | ``` ecommerce_orders.connectionid = ecommerce_order_activities.connectionid ```  ``` ecommerce_orders.customer = ecommerce_order_activities.customerid ```  ``` ecommerce_orders.id = ecommerce_order_activities.orderid ``` |
| [contact\_custom\_field\_options](#contact-custom-field-options) | ``` ecommerce_orders.id = contact_custom_field_options.orderid ``` |
| [deal\_stages](#deal-stages) | ``` ecommerce_orders.id = deal_stages.order ``` |

ecommerce\_orders table schema

|  |
| --- |
| **connection**  INTEGER |
| **connectionid**  INTEGER |
| **created\_date**  DATE-TIME |
| **currency**  STRING |
| **customer**  INTEGER |
| **discount\_amount**  NUMBER |
| **email**  STRING |
| **external\_created\_date**  DATE-TIME |
| **external\_updated\_date**  DATE-TIME |
| **externalid**  STRING |
| **id**  INTEGER |
| **order\_date**  DATE-TIME |
| **order\_products**  ARRAY |
| **order\_url**  STRING |
| **shipping\_amount**  NUMBER |
| **shipping\_method**  STRING |
| **source**  INTEGER |
| **state**  INTEGER |
| **tax\_amount**  NUMBER |
| **total\_price**  NUMBER |
| **total\_products**  INTEGER |
| **tstamp**  DATE-TIME |
| **updated\_date**  DATE-TIME |

### email\_activities

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | tstamp |

email\_activities table foreign keys

| Join email\_activities with | on |
| --- | --- |
| [deals](#deals) | ``` email_activities.deal = deals.id ```  ``` email_activities.account = deals.account ```  ``` email_activities.contact = deals.contact ``` |
| [deal\_custom\_field\_values](#deal-custom-field-values) | ``` email_activities.deal = deal_custom_field_values.deal_id ``` |
| [contact\_deals](#contact-deals) | ``` email_activities.deal = contact_deals.deal ```  ``` email_activities.contact = contact_deals.contact ``` |
| [forms](#forms) | ``` email_activities.deal = forms.deals ```  ``` email_activities.contact = forms.contacts ```  ``` email_activities.userid = forms.userid ``` |
| [deal\_activities](#deal-activities) | ``` email_activities.deal = deal_activities.deal ```  ``` email_activities.userid = deal_activities.userid ``` |
| [contact\_emails](#contact-emails) | ``` email_activities.deal = contact_emails.deal ```  ``` email_activities.account = contact_emails.account ```  ``` email_activities.contact = contact_emails.contact ```  ``` email_activities.userid = contact_emails.userid ``` |
| [accounts](#accounts) | ``` email_activities.account = accounts.id ``` |
| [account\_contacts](#account-contacts) | ``` email_activities.account = account_contacts.account ```  ``` email_activities.contact = account_contacts.contact ``` |
| [account\_custom\_field\_values](#account-custom-field-values) | ``` email_activities.account = account_custom_field_values.account_id ``` |
| [contacts](#contacts) | ``` email_activities.contact = contacts.id ``` |
| [bounce\_logs](#bounce-logs) | ``` email_activities.contact = bounce_logs.contact ``` |
| [contact\_data](#contact-data) | ``` email_activities.contact = contact_data.contact ``` |
| [contact\_lists](#contact-lists) | ``` email_activities.contact = contact_lists.contact ``` |
| [contact\_tags](#contact-tags) | ``` email_activities.contact = contact_tags.contact ``` |
| [contact\_conversions](#contact-conversions) | ``` email_activities.contact = contact_conversions.contact ``` |
| [contact\_automations](#contact-automations) | ``` email_activities.contact = contact_automations.contact ``` |
| [contact\_custom\_field\_values](#contact-custom-field-values) | ``` email_activities.contact = contact_custom_field_values.contact ``` |
| [users](#users) | ``` email_activities.userid = users.id ``` |
| [lists](#lists) | ``` email_activities.userid = lists.userid ``` |
| [messages](#messages) | ``` email_activities.userid = messages.userid ``` |
| [saved\_responses](#saved-responses) | ``` email_activities.userid = saved_responses.last_sent_user_id ``` |
| [tasks](#tasks) | ``` email_activities.userid = tasks.user ``` |
| [templates](#templates) | ``` email_activities.userid = templates.userid ``` |
| [activities](#activities) | ``` email_activities.userid = activities.userid ``` |
| [campaign\_lists](#campaign-lists) | ``` email_activities.userid = campaign_lists.userid ``` |
| [configs](#configs) | ``` email_activities.userid = configs.userid ``` |
| [deal\_group\_users](#deal-group-users) | ``` email_activities.userid = deal_group_users.user ``` |
| [sms](#sms) | ``` email_activities.userid = sms.userid ``` |
| [automations](#automations) | ``` email_activities.userid = automations.userid ``` |
| [calendars](#calendars) | ``` email_activities.userid = calendars.userid ``` |
| [campaigns](#campaigns) | ``` email_activities.userid = campaigns.userid ``` |

email\_activities table schema

|  |
| --- |
| **account**  INTEGER |
| **cc\_address**  STRING |
| **contact**  INTEGER |
| **d\_id**  INTEGER |
| **deal**  INTEGER |
| **from\_address**  STRING |
| **from\_name**  STRING |
| **id**  INTEGER |
| **message**  STRING |
| **message\_html**  STRING |
| **reference**  OBJECT This is a nested data structure:   - **id**: INTEGER - **type**: STRING |
| **relid**  INTEGER |
| **reltype**  STRING |
| **subject**  STRING |
| **subscriberid**  INTEGER |
| **to\_address**  STRING |
| **tstamp**  DATE-TIME |
| **user**  INTEGER |
| **userid**  INTEGER |

### forms

The `forms` table contains information about forms in your ActiveCampaign account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | udate |
| **Useful links** | [ActiveCampaign documentation](https://developers.activecampaign.com/reference#forms)  [ActiveCampaign API method](https://developers.activecampaign.com/reference#forms-1 "Opens in new tab: ActiveCampaign API method") |

forms table foreign keys

| Join forms with | on |
| --- | --- |
| [addresses](#addresses) | ``` forms.addressid = addresses.id ``` |
| [campaigns](#campaigns) | ``` forms.addressid = campaigns.addressid ```  ``` forms.userid = campaigns.userid ``` |
| [deals](#deals) | ``` forms.deals = deals.id ```  ``` forms.contacts = deals.contact ``` |
| [deal\_custom\_field\_values](#deal-custom-field-values) | ``` forms.deals = deal_custom_field_values.deal_id ``` |
| [contact\_deals](#contact-deals) | ``` forms.deals = contact_deals.deal ```  ``` forms.contacts = contact_deals.contact ``` |
| [deal\_activities](#deal-activities) | ``` forms.deals = deal_activities.deal ```  ``` forms.userid = deal_activities.userid ``` |
| [email\_activities](#email-activities) | ``` forms.deals = email_activities.deal ```  ``` forms.contacts = email_activities.contact ```  ``` forms.userid = email_activities.userid ``` |
| [contact\_emails](#contact-emails) | ``` forms.deals = contact_emails.deal ```  ``` forms.contacts = contact_emails.contact ```  ``` forms.userid = contact_emails.userid ``` |
| [contacts](#contacts) | ``` forms.contacts = contacts.id ``` |
| [bounce\_logs](#bounce-logs) | ``` forms.contacts = bounce_logs.contact ``` |
| [contact\_data](#contact-data) | ``` forms.contacts = contact_data.contact ``` |
| [contact\_lists](#contact-lists) | ``` forms.contacts = contact_lists.contact ```  ``` forms.id = contact_lists.form ``` |
| [contact\_tags](#contact-tags) | ``` forms.contacts = contact_tags.contact ``` |
| [contact\_conversions](#contact-conversions) | ``` forms.contacts = contact_conversions.contact ``` |
| [account\_contacts](#account-contacts) | ``` forms.contacts = account_contacts.contact ``` |
| [contact\_automations](#contact-automations) | ``` forms.contacts = contact_automations.contact ``` |
| [contact\_custom\_field\_values](#contact-custom-field-values) | ``` forms.contacts = contact_custom_field_values.contact ``` |
| [users](#users) | ``` forms.userid = users.id ``` |
| [lists](#lists) | ``` forms.userid = lists.userid ``` |
| [messages](#messages) | ``` forms.userid = messages.userid ``` |
| [saved\_responses](#saved-responses) | ``` forms.userid = saved_responses.last_sent_user_id ``` |
| [tasks](#tasks) | ``` forms.userid = tasks.user ``` |
| [templates](#templates) | ``` forms.userid = templates.userid ``` |
| [activities](#activities) | ``` forms.userid = activities.userid ``` |
| [campaign\_lists](#campaign-lists) | ``` forms.userid = campaign_lists.userid ``` |
| [configs](#configs) | ``` forms.userid = configs.userid ``` |
| [deal\_group\_users](#deal-group-users) | ``` forms.userid = deal_group_users.user ``` |
| [sms](#sms) | ``` forms.userid = sms.userid ``` |
| [automations](#automations) | ``` forms.userid = automations.userid ``` |
| [calendars](#calendars) | ``` forms.userid = calendars.userid ``` |

forms table schema

|  |
| --- |
| **action**  STRING |
| **actiondata**  OBJECT This is a nested data structure: ARRAY, which is also a nested data structure.  **actions**   - **email**: STRING - **list**: INTEGER - **type**: STRING |
| **address**  INTEGER |
| **addressid**  INTEGER |
| **aid**  INTEGER |
| **body**  STRING |
| **button**  STRING |
| **cdate**  DATE-TIME |
| **cfields**  OBJECT This is a nested data structure: ARRAY, which is also a nested data structure.  **cfields**   - **class**: STRING - **default\_text**: STRING - **header**: STRING - **html**: STRING - **required**: BOOLEAN - **type**: STRING |
| **contacts**  INTEGER |
| **deals**  INTEGER |
| **defaultscreenshot**  STRING |
| **entries**  INTEGER |
| **id**  INTEGER |
| **layout**  STRING |
| **name**  STRING |
| **options**  OBJECT This is a nested data structure:   - **blank\_overwrite**: BOOLEAN - **confaction**: STRING - **confform**: STRING - **optin\_created**: BOOLEAN - **optin\_id**: INTEGER - **sendoptin**: BOOLEAN |
| **parentformid**  INTEGER |
| **recent**  ARRAY |
| **style**  OBJECT This is a nested data structure: OBJECT, which is also a nested data structure.  **style**   - **ac\_branding**: BOOLEAN - **background**: STRING - **border**: OBJECT, which is also a nested data structure:   - **color**: STRING   - **radius**: INTEGER   - **style**: STRING   - **width**: INTEGER - **button**: OBJECT, which is also a nested data structure:   - **background**: STRING   - **border**: OBJECT, which is also a nested data structure:     - **color**: STRING     - **radius**: INTEGER     - **style**: STRING     - **width**: INTEGER - **fontcolor**: STRING - **padding**: STRING - **dark**: BOOLEAN - **fontcolor**: STRING - **layout**: STRING - **width**: STRING |
| **submit**  STRING |
| **submitdata**  OBJECT This is a nested data structure:  **type**: STRING |
| **thanks**  STRING |
| **title**  STRING |
| **udate**  DATE-TIME |
| **url**  STRING |
| **userid**  INTEGER |

### goals

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |

goals table foreign keys

| Join goals with | on |
| --- | --- |
| [automations](#automations) | ``` goals.automation = automations.id ``` |
| [deal\_activities](#deal-activities) | ``` goals.automation = deal_activities.automation ``` |
| [site\_messages](#site-messages) | ``` goals.automation = site_messages.automation ``` |
| [sms](#sms) | ``` goals.automation = sms.automation ``` |
| [automation\_blocks](#automation-blocks) | ``` goals.automation = automation_blocks.automation ``` |
| [campaigns](#campaigns) | ``` goals.automation = campaigns.automation ``` |
| [contact\_automations](#contact-automations) | ``` goals.automation = contact_automations.automation ``` |

goals table schema

|  |
| --- |
| **automation**  INTEGER |
| **automation\_block**  INTEGER |
| **blockid**  INTEGER |
| **cdate**  DATE-TIME |
| **dirty\_stats**  INTEGER |
| **id**  INTEGER |
| **name**  STRING |
| **seriesid**  INTEGER |

### groups

The `groups` table contains information about user groups in your ActiveCampaign account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [ActiveCampaign documentation](https://developers.activecampaign.com/reference#groups)  [ActiveCampaign API method](https://developers.activecampaign.com/reference#list-all-groups "Opens in new tab: ActiveCampaign API method") |

groups table schema

|  |
| --- |
| **descript**  STRING |
| **id**  INTEGER |
| **optinconfirm**  INTEGER |
| **p\_admin**  INTEGER |
| **pg\_automation\_manage**  INTEGER |
| **pg\_contact\_actions**  INTEGER |
| **pg\_contact\_add**  INTEGER |
| **pg\_contact\_approve**  INTEGER |
| **pg\_contact\_delete**  INTEGER |
| **pg\_contact\_edit**  INTEGER |
| **pg\_contact\_export**  INTEGER |
| **pg\_contact\_fields**  INTEGER |
| **pg\_contact\_filters**  INTEGER |
| **pg\_contact\_import**  INTEGER |
| **pg\_contact\_merge**  INTEGER |
| **pg\_contact\_sync**  INTEGER |
| **pg\_deal**  INTEGER |
| **pg\_deal\_delete**  INTEGER |
| **pg\_deal\_group\_add**  INTEGER |
| **pg\_deal\_group\_delete**  INTEGER |
| **pg\_deal\_group\_edit**  INTEGER |
| **pg\_deal\_reassign**  INTEGER |
| **pg\_form\_edit**  INTEGER |
| **pg\_group\_add**  INTEGER |
| **pg\_group\_delete**  INTEGER |
| **pg\_group\_edit**  INTEGER |
| **pg\_list\_add**  INTEGER |
| **pg\_list\_bounce**  INTEGER |
| **pg\_list\_delete**  INTEGER |
| **pg\_list\_edit**  INTEGER |
| **pg\_list\_emailaccount**  INTEGER |
| **pg\_list\_headers**  INTEGER |
| **pg\_message\_add**  INTEGER |
| **pg\_message\_delete**  INTEGER |
| **pg\_message\_edit**  INTEGER |
| **pg\_message\_send**  INTEGER |
| **pg\_personalization\_add**  INTEGER |
| **pg\_personalization\_delete**  INTEGER |
| **pg\_personalization\_edit**  INTEGER |
| **pg\_reports\_campaign**  INTEGER |
| **pg\_reports\_list**  INTEGER |
| **pg\_reports\_trend**  INTEGER |
| **pg\_reports\_user**  INTEGER |
| **pg\_saved\_responses\_manage**  INTEGER |
| **pg\_startup\_gettingstarted**  INTEGER |
| **pg\_startup\_reports**  INTEGER |
| **pg\_template\_add**  INTEGER |
| **pg\_template\_delete**  INTEGER |
| **pg\_template\_edit**  INTEGER |
| **pg\_user\_add**  INTEGER |
| **pg\_user\_delete**  INTEGER |
| **pg\_user\_edit**  INTEGER |
| **req\_approval**  INTEGER |
| **req\_approval1st**  INTEGER |
| **req\_approval\_notify**  INTEGER |
| **sdate**  DATE-TIME |
| **socialdata**  INTEGER |
| **title**  STRING |
| **unsubscribelink**  INTEGER |

### lists

The `lists` table contains information about groups of contacts that campaigns can be sent to in your ActiveCampaign account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_timestamp |
| **Useful links** | [ActiveCampaign documentation](https://developers.activecampaign.com/reference#lists)  [ActiveCampaign API method](https://developers.activecampaign.com/reference#retrieve-all-lists "Opens in new tab: ActiveCampaign API method") |

lists table foreign keys

| Join lists with | on |
| --- | --- |
| [users](#users) | ``` lists.userid = users.id ``` |
| [forms](#forms) | ``` lists.userid = forms.userid ``` |
| [messages](#messages) | ``` lists.userid = messages.userid ``` |
| [saved\_responses](#saved-responses) | ``` lists.userid = saved_responses.last_sent_user_id ``` |
| [tasks](#tasks) | ``` lists.userid = tasks.user ``` |
| [templates](#templates) | ``` lists.userid = templates.userid ``` |
| [activities](#activities) | ``` lists.userid = activities.userid ``` |
| [campaign\_lists](#campaign-lists) | ``` lists.userid = campaign_lists.userid ```  ``` lists.id = campaign_lists.listid ``` |
| [configs](#configs) | ``` lists.userid = configs.userid ``` |
| [contact\_emails](#contact-emails) | ``` lists.userid = contact_emails.userid ``` |
| [deal\_activities](#deal-activities) | ``` lists.userid = deal_activities.userid ``` |
| [deal\_group\_users](#deal-group-users) | ``` lists.userid = deal_group_users.user ``` |
| [email\_activities](#email-activities) | ``` lists.userid = email_activities.userid ``` |
| [sms](#sms) | ``` lists.userid = sms.userid ``` |
| [automations](#automations) | ``` lists.userid = automations.userid ``` |
| [calendars](#calendars) | ``` lists.userid = calendars.userid ``` |
| [campaigns](#campaigns) | ``` lists.userid = campaigns.userid ``` |
| [webhooks](#webhooks) | ``` lists.id = webhooks.listid ``` |
| [contact\_lists](#contact-lists) | ``` lists.id = contact_lists.list ``` |

lists table schema

|  |
| --- |
| **analytics\_domains**  STRING |
| **analytics\_source**  STRING |
| **analytics\_ua**  STRING |
| **carboncopy**  STRING |
| **cdate**  DATE-TIME |
| **created\_by**  INTEGER |
| **created\_timestamp**  DATE-TIME |
| **deletestamp**  STRING |
| **facebook\_session**  STRING |
| **fulladdress**  STRING |
| **get\_unsubscribe\_reason**  INTEGER |
| **id**  INTEGER |
| **name**  STRING |
| **optinmessageid**  INTEGER |
| **optinoptout**  INTEGER |
| **optoutconf**  INTEGER |
| **p\_embed\_image**  INTEGER |
| **p\_use\_analytics\_link**  INTEGER |
| **p\_use\_analytics\_read**  INTEGER |
| **p\_use\_captcha**  INTEGER |
| **p\_use\_facebook**  INTEGER |
| **p\_use\_tracking**  INTEGER |
| **p\_use\_twitter**  INTEGER |
| **private**  INTEGER |
| **require\_name**  INTEGER |
| **send\_last\_broadcast**  INTEGER |
| **sender\_addr1**  STRING |
| **sender\_addr2**  STRING |
| **sender\_city**  STRING |
| **sender\_country**  STRING |
| **sender\_name**  STRING |
| **sender\_phone**  STRING |
| **sender\_reminder**  STRING |
| **sender\_state**  STRING |
| **sender\_url**  STRING |
| **sender\_zip**  STRING |
| **stringid**  STRING |
| **subscription\_notify**  STRING |
| **to\_name**  STRING |
| **twitter\_token**  STRING |
| **twitter\_token\_secret**  STRING |
| **udate**  DATE-TIME |
| **unsubscription\_notify**  STRING |
| **updated\_by**  INTEGER |
| **updated\_timestamp**  DATE-TIME |
| **user**  INTEGER |
| **userid**  INTEGER |

### messages

The `messages` table contains information about messages for campaigns in your ActiveCampaign account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | mdate |
| **Useful links** | [ActiveCampaign documentation](https://developers.activecampaign.com/reference#messages)  [ActiveCampaign API method](https://developers.activecampaign.com/reference#list-all-messages "Opens in new tab: ActiveCampaign API method") |

messages table foreign keys

| Join messages with | on |
| --- | --- |
| [users](#users) | ``` messages.userid = users.id ``` |
| [forms](#forms) | ``` messages.userid = forms.userid ``` |
| [lists](#lists) | ``` messages.userid = lists.userid ``` |
| [saved\_responses](#saved-responses) | ``` messages.userid = saved_responses.last_sent_user_id ``` |
| [tasks](#tasks) | ``` messages.userid = tasks.user ``` |
| [templates](#templates) | ``` messages.userid = templates.userid ``` |
| [activities](#activities) | ``` messages.userid = activities.userid ``` |
| [campaign\_lists](#campaign-lists) | ``` messages.userid = campaign_lists.userid ``` |
| [configs](#configs) | ``` messages.userid = configs.userid ``` |
| [contact\_emails](#contact-emails) | ``` messages.userid = contact_emails.userid ```  ``` messages.id = contact_emails.messageid ``` |
| [deal\_activities](#deal-activities) | ``` messages.userid = deal_activities.userid ``` |
| [deal\_group\_users](#deal-group-users) | ``` messages.userid = deal_group_users.user ``` |
| [email\_activities](#email-activities) | ``` messages.userid = email_activities.userid ``` |
| [sms](#sms) | ``` messages.userid = sms.userid ``` |
| [automations](#automations) | ``` messages.userid = automations.userid ``` |
| [calendars](#calendars) | ``` messages.userid = calendars.userid ``` |
| [campaigns](#campaigns) | ``` messages.userid = campaigns.userid ``` |
| [bounce\_logs](#bounce-logs) | ``` messages.id = bounce_logs.messageid ``` |
| [campaign\_messages](#campaign-messages) | ``` messages.id = campaign_messages.messageid ``` |
| [contact\_lists](#contact-lists) | ``` messages.id = contact_lists.message ``` |
| [campaign\_links](#campaign-links) | ``` messages.id = campaign_links.messageid ``` |

messages table schema

|  |
| --- |
| **cdate**  DATE-TIME |
| **charset**  STRING |
| **ed\_instanceid**  INTEGER |
| **ed\_version**  INTEGER |
| **encoding**  STRING |
| **format**  STRING |
| **fromemail**  STRING |
| **fromname**  STRING |
| **hidden**  INTEGER |
| **html**  STRING |
| **htmlfetch**  STRING |
| **id**  INTEGER |
| **mdate**  DATE-TIME |
| **name**  STRING |
| **preheader\_text**  STRING |
| **preview\_data**  STRING |
| **preview\_mime**  STRING |
| **priority**  INTEGER |
| **reply2**  STRING |
| **subject**  STRING |
| **text**  STRING |
| **textfetch**  STRING |
| **user**  INTEGER |
| **userid**  INTEGER |

### saved\_responses

The `saved_responses` table contains information about email response templates in your ActiveCampaign account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | mdate |
| **Useful links** | [ActiveCampaign documentation](https://developers.activecampaign.com/reference#saved-responses-1)  [ActiveCampaign API method](https://developers.activecampaign.com/reference#list-all-saved-responses "Opens in new tab: ActiveCampaign API method") |

saved\_responses table foreign keys

| Join saved\_responses with | on |
| --- | --- |
| [users](#users) | ``` saved_responses.last_sent_user_id = users.id ``` |
| [forms](#forms) | ``` saved_responses.last_sent_user_id = forms.userid ``` |
| [lists](#lists) | ``` saved_responses.last_sent_user_id = lists.userid ``` |
| [messages](#messages) | ``` saved_responses.last_sent_user_id = messages.userid ``` |
| [tasks](#tasks) | ``` saved_responses.last_sent_user_id = tasks.user ``` |
| [templates](#templates) | ``` saved_responses.last_sent_user_id = templates.userid ``` |
| [activities](#activities) | ``` saved_responses.last_sent_user_id = activities.userid ``` |
| [campaign\_lists](#campaign-lists) | ``` saved_responses.last_sent_user_id = campaign_lists.userid ``` |
| [configs](#configs) | ``` saved_responses.last_sent_user_id = configs.userid ``` |
| [contact\_emails](#contact-emails) | ``` saved_responses.last_sent_user_id = contact_emails.userid ``` |
| [deal\_activities](#deal-activities) | ``` saved_responses.last_sent_user_id = deal_activities.userid ``` |
| [deal\_group\_users](#deal-group-users) | ``` saved_responses.last_sent_user_id = deal_group_users.user ``` |
| [email\_activities](#email-activities) | ``` saved_responses.last_sent_user_id = email_activities.userid ``` |
| [sms](#sms) | ``` saved_responses.last_sent_user_id = sms.userid ``` |
| [automations](#automations) | ``` saved_responses.last_sent_user_id = automations.userid ``` |
| [calendars](#calendars) | ``` saved_responses.last_sent_user_id = calendars.userid ``` |
| [campaigns](#campaigns) | ``` saved_responses.last_sent_user_id = campaigns.userid ``` |

saved\_responses table schema

|  |
| --- |
| **body**  STRING |
| **cdate**  DATE-TIME |
| **id**  INTEGER |
| **last\_sent\_user\_id**  INTEGER |
| **ldate**  DATE-TIME |
| **mdate**  DATE-TIME |
| **subject**  STRING |
| **title**  STRING |

### scores

The `scores` table contains information about prioritization scores on leads in your ActiveCampaign account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | mdate |
| **Useful links** | [ActiveCampaign API method](https://developers.activecampaign.com/reference#list-all-scores "Opens in new tab: ActiveCampaign API method") |

scores table schema

|  |
| --- |
| **cdate**  DATE-TIME |
| **descript**  STRING |
| **id**  INTEGER |
| **mdate**  DATE-TIME |
| **name**  STRING |
| **reltype**  STRING |
| **status**  INTEGER |

### segments

The `segments` table contains information about targeted groups of contacts that meet specified criteria in your ActiveCampaign account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [ActiveCampaign documentation](https://developers.activecampaign.com/reference#segments)  [ActiveCampaign API method](https://developers.activecampaign.com/reference#list-all-segments "Opens in new tab: ActiveCampaign API method") |

segments table foreign keys

| Join segments with | on |
| --- | --- |
| [campaigns](#campaigns) | ``` segments.id = campaigns.segmentid ``` |

segments table schema

|  |
| --- |
| **created\_by**  INTEGER |
| **created\_timestamp**  DATE-TIME |
| **hidden**  INTEGER |
| **id**  INTEGER |
| **logic**  STRING |
| **name**  STRING |
| **seriesid**  INTEGER |
| **updated\_by**  INTEGER |
| **updated\_timestamp**  DATE-TIME |

### site\_messages

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | ldate |

site\_messages table foreign keys

| Join site\_messages with | on |
| --- | --- |
| [automations](#automations) | ``` site_messages.automation = automations.id ``` |
| [deal\_activities](#deal-activities) | ``` site_messages.automation = deal_activities.automation ``` |
| [goals](#goals) | ``` site_messages.automation = goals.automation ``` |
| [sms](#sms) | ``` site_messages.automation = sms.automation ``` |
| [automation\_blocks](#automation-blocks) | ``` site_messages.automation = automation_blocks.automation ``` |
| [campaigns](#campaigns) | ``` site_messages.automation = campaigns.automation ``` |
| [contact\_automations](#contact-automations) | ``` site_messages.automation = contact_automations.automation ``` |

site\_messages table schema

|  |
| --- |
| **automation**  INTEGER |
| **id**  INTEGER |
| **ldate**  DATE-TIME |
| **name**  STRING |
| **template**  OBJECT This is a nested data structure:   - **detailed**: OBJECT, which is also a nested data structure. - **initial**: OBJECT, which is also a nested data structure. |

### sms

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | ldate |

sms table foreign keys

| Join sms with | on |
| --- | --- |
| [users](#users) | ``` sms.userid = users.id ``` |
| [forms](#forms) | ``` sms.userid = forms.userid ``` |
| [lists](#lists) | ``` sms.userid = lists.userid ``` |
| [messages](#messages) | ``` sms.userid = messages.userid ``` |
| [saved\_responses](#saved-responses) | ``` sms.userid = saved_responses.last_sent_user_id ``` |
| [tasks](#tasks) | ``` sms.userid = tasks.user ``` |
| [templates](#templates) | ``` sms.userid = templates.userid ``` |
| [activities](#activities) | ``` sms.userid = activities.userid ``` |
| [campaign\_lists](#campaign-lists) | ``` sms.userid = campaign_lists.userid ``` |
| [configs](#configs) | ``` sms.userid = configs.userid ``` |
| [contact\_emails](#contact-emails) | ``` sms.userid = contact_emails.userid ``` |
| [deal\_activities](#deal-activities) | ``` sms.userid = deal_activities.userid ```  ``` sms.automation = deal_activities.automation ``` |
| [deal\_group\_users](#deal-group-users) | ``` sms.userid = deal_group_users.user ``` |
| [email\_activities](#email-activities) | ``` sms.userid = email_activities.userid ``` |
| [automations](#automations) | ``` sms.userid = automations.userid ```  ``` sms.automation = automations.id ``` |
| [calendars](#calendars) | ``` sms.userid = calendars.userid ``` |
| [campaigns](#campaigns) | ``` sms.userid = campaigns.userid ```  ``` sms.automation = campaigns.automation ``` |
| [goals](#goals) | ``` sms.automation = goals.automation ``` |
| [site\_messages](#site-messages) | ``` sms.automation = site_messages.automation ``` |
| [automation\_blocks](#automation-blocks) | ``` sms.automation = automation_blocks.automation ``` |
| [contact\_automations](#contact-automations) | ``` sms.automation = contact_automations.automation ``` |

sms table schema

|  |
| --- |
| **automation**  INTEGER |
| **failed**  INTEGER |
| **id**  INTEGER |
| **ldate**  DATE-TIME |
| **msg**  STRING |
| **replies**  INTEGER |
| **sdate**  DATE-TIME |
| **sent**  INTEGER |
| **seriesid**  INTEGER |
| **tf\_day**  STRING |
| **tf\_hr\_from**  INTEGER |
| **tf\_hr\_to**  INTEGER |
| **tstamp**  DATE-TIME |
| **uniquereplies**  INTEGER |
| **unsubscribes**  INTEGER |
| **user**  INTEGER |
| **userid**  INTEGER |

### tags

The `tags` table contains information about labels that you can apply to contacts in your ActiveCampaign account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [ActiveCampaign API method](https://developers.activecampaign.com/reference#retrieve-all-tags "Opens in new tab: ActiveCampaign API method") |

tags table foreign keys

| Join tags with | on |
| --- | --- |
| [contact\_tags](#contact-tags) | ``` tags.id = contact_tags.tag ``` |

tags table schema

|  |
| --- |
| **cdate**  DATE-TIME |
| **created\_by**  INTEGER |
| **created\_timestamp**  DATE-TIME |
| **description**  STRING |
| **id**  INTEGER |
| **tag**  STRING |
| **tag\_type**  STRING |
| **updated\_by**  INTEGER |
| **updated\_timestamp**  DATE-TIME |

### task\_types

The `task_types` table contains information about task types in your ActiveCampaign account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [ActiveCampaign documentation](https://developers.activecampaign.com/reference#deal-task-types)  [ActiveCampaign API method](https://developers.activecampaign.com/reference#list-all-deal-task-types "Opens in new tab: ActiveCampaign API method") |

task\_types table foreign keys

| Join task\_types with | on |
| --- | --- |
| [tasks](#tasks) | ``` task_types.id = tasks.deal_tasktype ``` |

task\_types table schema

|  |
| --- |
| **cdate**  DATE-TIME |
| **defduration**  INTEGER |
| **id**  INTEGER |
| **status**  INTEGER |
| **title**  STRING |
| **udate**  DATE-TIME |

### tasks

The `tasks` table contains information about tasks to do in your ActiveCampaign account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | udate |
| **Useful links** | [ActiveCampaign documentation](https://developers.activecampaign.com/reference#tasks)  [ActiveCampaign API method](https://developers.activecampaign.com/reference#list-all-tasks "Opens in new tab: ActiveCampaign API method") |

tasks table foreign keys

| Join tasks with | on |
| --- | --- |
| [users](#users) | ``` tasks.user = users.id ``` |
| [forms](#forms) | ``` tasks.user = forms.userid ``` |
| [lists](#lists) | ``` tasks.user = lists.userid ``` |
| [messages](#messages) | ``` tasks.user = messages.userid ``` |
| [saved\_responses](#saved-responses) | ``` tasks.user = saved_responses.last_sent_user_id ``` |
| [templates](#templates) | ``` tasks.user = templates.userid ``` |
| [activities](#activities) | ``` tasks.user = activities.userid ``` |
| [campaign\_lists](#campaign-lists) | ``` tasks.user = campaign_lists.userid ``` |
| [configs](#configs) | ``` tasks.user = configs.userid ``` |
| [contact\_emails](#contact-emails) | ``` tasks.user = contact_emails.userid ``` |
| [deal\_activities](#deal-activities) | ``` tasks.user = deal_activities.userid ``` |
| [deal\_group\_users](#deal-group-users) | ``` tasks.user = deal_group_users.user ``` |
| [email\_activities](#email-activities) | ``` tasks.user = email_activities.userid ``` |
| [sms](#sms) | ``` tasks.user = sms.userid ``` |
| [automations](#automations) | ``` tasks.user = automations.userid ``` |
| [calendars](#calendars) | ``` tasks.user = calendars.userid ``` |
| [campaigns](#campaigns) | ``` tasks.user = campaigns.userid ``` |
| [task\_types](#task-types) | ``` tasks.deal_tasktype = task_types.id ``` |

tasks table schema

|  |
| --- |
| **assignee**  INTEGER |
| **automation**  INTEGER |
| **cdate**  DATE-TIME |
| **deal\_tasktype**  INTEGER |
| **done\_automation**  INTEGER |
| **duedate**  DATE-TIME |
| **edate**  DATE-TIME |
| **id**  INTEGER |
| **note**  STRING |
| **owner**  OBJECT This is a nested data structure:   - **id**: INTEGER - **type**: STRING |
| **relid**  INTEGER |
| **reltype**  STRING |
| **status**  INTEGER |
| **title**  STRING |
| **udate**  DATE-TIME |
| **user**  INTEGER |

### templates

The `templates` table contains information about templates used for campaign emails in your ActiveCampaign account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | mdate |
| **Useful links** | [ActiveCampaign API method](https://developers.activecampaign.com/reference#templates "Opens in new tab: ActiveCampaign API method") |

templates table foreign keys

| Join templates with | on |
| --- | --- |
| [users](#users) | ``` templates.userid = users.id ``` |
| [forms](#forms) | ``` templates.userid = forms.userid ``` |
| [lists](#lists) | ``` templates.userid = lists.userid ``` |
| [messages](#messages) | ``` templates.userid = messages.userid ``` |
| [saved\_responses](#saved-responses) | ``` templates.userid = saved_responses.last_sent_user_id ``` |
| [tasks](#tasks) | ``` templates.userid = tasks.user ``` |
| [activities](#activities) | ``` templates.userid = activities.userid ``` |
| [campaign\_lists](#campaign-lists) | ``` templates.userid = campaign_lists.userid ``` |
| [configs](#configs) | ``` templates.userid = configs.userid ``` |
| [contact\_emails](#contact-emails) | ``` templates.userid = contact_emails.userid ``` |
| [deal\_activities](#deal-activities) | ``` templates.userid = deal_activities.userid ``` |
| [deal\_group\_users](#deal-group-users) | ``` templates.userid = deal_group_users.user ``` |
| [email\_activities](#email-activities) | ``` templates.userid = email_activities.userid ``` |
| [sms](#sms) | ``` templates.userid = sms.userid ``` |
| [automations](#automations) | ``` templates.userid = automations.userid ``` |
| [calendars](#calendars) | ``` templates.userid = calendars.userid ``` |
| [campaigns](#campaigns) | ``` templates.userid = campaigns.userid ``` |

templates table schema

|  |
| --- |
| **categoryid**  INTEGER |
| **content**  STRING |
| **ed\_instanceid**  INTEGER |
| **ed\_version**  INTEGER |
| **hidden**  INTEGER |
| **id**  INTEGER |
| **importnum**  INTEGER |
| **mdate**  DATE-TIME |
| **modified**  INTEGER |
| **name**  STRING |
| **preview\_content**  STRING |
| **screenshot**  STRING |
| **subject**  STRING |
| **used**  INTEGER |
| **userid**  INTEGER |
| **waitpreview**  INTEGER |

### users

The `users` table contains information about users who can login to your ActiveCampaign account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [ActiveCampaign documentation](https://developers.activecampaign.com/reference#users)  [ActiveCampaign API method](https://developers.activecampaign.com/reference#list-all-users "Opens in new tab: ActiveCampaign API method") |

users table foreign keys

| Join users with | on |
| --- | --- |
| [forms](#forms) | ``` users.id = forms.userid ``` |
| [lists](#lists) | ``` users.id = lists.userid ``` |
| [messages](#messages) | ``` users.id = messages.userid ``` |
| [saved\_responses](#saved-responses) | ``` users.id = saved_responses.last_sent_user_id ``` |
| [tasks](#tasks) | ``` users.id = tasks.user ``` |
| [templates](#templates) | ``` users.id = templates.userid ``` |
| [activities](#activities) | ``` users.id = activities.userid ``` |
| [campaign\_lists](#campaign-lists) | ``` users.id = campaign_lists.userid ``` |
| [configs](#configs) | ``` users.id = configs.userid ``` |
| [contact\_emails](#contact-emails) | ``` users.id = contact_emails.userid ``` |
| [deal\_activities](#deal-activities) | ``` users.id = deal_activities.userid ``` |
| [deal\_group\_users](#deal-group-users) | ``` users.id = deal_group_users.user ``` |
| [email\_activities](#email-activities) | ``` users.id = email_activities.userid ``` |
| [sms](#sms) | ``` users.id = sms.userid ``` |
| [automations](#automations) | ``` users.id = automations.userid ``` |
| [calendars](#calendars) | ``` users.id = calendars.userid ``` |
| [campaigns](#campaigns) | ``` users.id = campaigns.userid ``` |

users table schema

|  |
| --- |
| **cdate**  DATE-TIME |
| **email**  STRING |
| **first\_name**  STRING |
| **id**  INTEGER |
| **last\_name**  STRING |
| **local\_zoneid**  STRING |
| **mfa\_enabled**  INTEGER |
| **password\_updated\_utc\_timestamp**  DATE-TIME |
| **phone**  STRING |
| **signature**  STRING |
| **udate**  DATE-TIME |
| **username**  STRING |

### webhooks

The `webhooks` table contains information about real-time updates about your contact and campaign activity in your ActiveCampaign account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [ActiveCampaign API method](https://developers.activecampaign.com/reference#get-a-list-of-webhook-events "Opens in new tab: ActiveCampaign API method") |

webhooks table foreign keys

| Join webhooks with | on |
| --- | --- |
| [lists](#lists) | ``` webhooks.listid = lists.id ``` |
| [campaign\_lists](#campaign-lists) | ``` webhooks.listid = campaign_lists.listid ``` |
| [contact\_lists](#contact-lists) | ``` webhooks.listid = contact_lists.list ``` |

webhooks table schema

|  |
| --- |
| **cdate**  DATE-TIME |
| **events**  ARRAY |
| **id**  INTEGER |
| **listid**  INTEGER |
| **name**  STRING |
| **sources**  ARRAY |
| **url**  STRING |
