---
title: "Eloqua"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Eloqua.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Eloqua

Eloqua enables marketers to plan and execute campaigns while delivering a personalized customer experience for their prospects.

Eloqua integration replicates data using the [Oracle Eloqua Marketing Cloud Service REST API](https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAC/index.html) and [Eloqua bulk export API](https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAB/Developers/BulkAPI/Tutorials/Export.htm).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To obtain you client ID and secret:

1. Log into your Eloqua account as an account administrator.
2. Navigate to AppCloud Developer Console > Settings.
3. Under Platform Extensions, choose AppCloud Developer.
4. Under App Type, select Interactive or Web App.
5. Make sure Authorized Redirect URIs is set to https://connector.qlik.com/auth/oauth/v3.htm.
6. After the client ID and secret have been generated, copy and paste them to a secured file as they are displayed only once.

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
| Client ID | Client ID. |
| Client Secret | Client secret. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### accounts

The `accounts` table contains info about the accounts, or companies, in your Eloqua account.

**Note**: This table is replicated using the Eloqua Bulk API.

#### Custom accounts fields

If applicable, Stitch will replicate custom fields related to `accounts` in Eloqua.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Id |
| **Replication Key** | UpdatedAt |
| **Useful links** | [Eloqua API method](https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAC/op-api-bulk-2.0-accounts-exports-post.html "Opens in new tab: Eloqua API method") |

accounts table schema

|  |
| --- |
| **CompanyIDExt**  STRING |
| **CreatedAt**  DATE-TIME |
| **Custom Fields**  VARIES |
| **Id**  STRING |
| **UpdatedAt**  DATE-TIME |

### activity\_bounceback

The `activity_bounceback` table contains info about `Bounceback` contact activities.

**Note**: This table is replicated using the Eloqua Bulk API.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [Eloqua API method](https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAC/op-api-bulk-2.0-activities-exports-post.html "Opens in new tab: Eloqua API method") |

activity\_bounceback table foreign keys

| Join activity\_bounceback with | on |
| --- | --- |
| [assets](#assets) | ``` activity_bounceback.AssetId = assets.id ``` |
| [activity\_email\_clickthrough](#activity-email-clickthrough) | ``` activity_bounceback.AssetId = activity_email_clickthrough.AssetId ```  ``` activity_bounceback.CampaignId = activity_email_clickthrough.CampaignId ```  ``` activity_bounceback.ContactId = activity_email_clickthrough.ContactId ``` |
| [activity\_email\_open](#activity-email-open) | ``` activity_bounceback.AssetId = activity_email_open.AssetId ```  ``` activity_bounceback.CampaignId = activity_email_open.CampaignId ```  ``` activity_bounceback.ContactId = activity_email_open.ContactId ``` |
| [activity\_email\_send](#activity-email-send) | ``` activity_bounceback.AssetId = activity_email_send.AssetId ```  ``` activity_bounceback.CampaignId = activity_email_send.CampaignId ```  ``` activity_bounceback.ContactId = activity_email_send.ContactId ``` |
| [activity\_form\_submit](#activity-form-submit) | ``` activity_bounceback.AssetId = activity_form_submit.AssetId ```  ``` activity_bounceback.CampaignId = activity_form_submit.CampaignId ```  ``` activity_bounceback.ContactId = activity_form_submit.ContactId ``` |
| [activity\_page\_view](#activity-page-view) | ``` activity_bounceback.AssetId = activity_page_view.AssetId ```  ``` activity_bounceback.CampaignId = activity_page_view.CampaignId ```  ``` activity_bounceback.ContactId = activity_page_view.ContactId ``` |
| [activity\_subscribe](#activity-subscribe) | ``` activity_bounceback.AssetId = activity_subscribe.AssetId ```  ``` activity_bounceback.CampaignId = activity_subscribe.CampaignId ```  ``` activity_bounceback.ContactId = activity_subscribe.ContactId ``` |
| [activity\_unsubscribe](#activity-unsubscribe) | ``` activity_bounceback.AssetId = activity_unsubscribe.AssetId ```  ``` activity_bounceback.CampaignId = activity_unsubscribe.CampaignId ```  ``` activity_bounceback.ContactId = activity_unsubscribe.ContactId ``` |
| [activity\_web\_visit](#activity-web-visit) | ``` activity_bounceback.AssetId = activity_web_visit.AssetId ``` |
| [campaigns](#campaigns) | ``` activity_bounceback.CampaignId = campaigns.id ``` |
| [forms](#forms) | ``` activity_bounceback.CampaignId = forms.processingSteps.campaignId ``` |
| [contacts](#contacts) | ``` activity_bounceback.ContactId = contacts.Id ``` |
| [visitors](#visitors) | ``` activity_bounceback.ContactId = visitors.contactId ``` |

activity\_bounceback table schema

|  |
| --- |
| **ActivityDate**  DATE-TIME |
| **ActivityId**  STRING |
| **ActivityType**  STRING |
| **AssetId**  STRING |
| **AssetName**  STRING |
| **AssetType**  STRING |
| **CampaignId**  INTEGER |
| **ContactId**  STRING |
| **DeploymentId**  STRING |
| **EmailAddress**  STRING |
| **EmailRecipientId**  STRING |
| **ExternalId**  STRING |
| **SmtpErrorCode**  STRING |
| **SmtpStatusCode**  STRING |
| **Type**  STRING |
| **id**  STRING |
| **updatedAt**  DATE-TIME |

### activity\_email\_clickthrough

The `activity_email_clickthrough` table contains info about `EmailClickthrough` contact activities.

**Note**: This table is replicated using the Eloqua Bulk API.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [Eloqua API method](https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAC/op-api-bulk-2.0-activities-exports-post.html "Opens in new tab: Eloqua API method") |

activity\_email\_clickthrough table foreign keys

| Join activity\_email\_clickthrough with | on |
| --- | --- |
| [assets](#assets) | ``` activity_email_clickthrough.AssetId = assets.id ``` |
| [activity\_bounceback](#activity-bounceback) | ``` activity_email_clickthrough.AssetId = activity_bounceback.AssetId ```  ``` activity_email_clickthrough.CampaignId = activity_bounceback.CampaignId ```  ``` activity_email_clickthrough.ContactId = activity_bounceback.ContactId ``` |
| [activity\_email\_open](#activity-email-open) | ``` activity_email_clickthrough.AssetId = activity_email_open.AssetId ```  ``` activity_email_clickthrough.CampaignId = activity_email_open.CampaignId ```  ``` activity_email_clickthrough.ContactId = activity_email_open.ContactId ```  ``` activity_email_clickthrough.VisitorId = activity_email_open.VisitorId ``` |
| [activity\_email\_send](#activity-email-send) | ``` activity_email_clickthrough.AssetId = activity_email_send.AssetId ```  ``` activity_email_clickthrough.CampaignId = activity_email_send.CampaignId ```  ``` activity_email_clickthrough.ContactId = activity_email_send.ContactId ``` |
| [activity\_form\_submit](#activity-form-submit) | ``` activity_email_clickthrough.AssetId = activity_form_submit.AssetId ```  ``` activity_email_clickthrough.CampaignId = activity_form_submit.CampaignId ```  ``` activity_email_clickthrough.ContactId = activity_form_submit.ContactId ```  ``` activity_email_clickthrough.VisitorId = activity_form_submit.VisitorId ``` |
| [activity\_page\_view](#activity-page-view) | ``` activity_email_clickthrough.AssetId = activity_page_view.AssetId ```  ``` activity_email_clickthrough.CampaignId = activity_page_view.CampaignId ```  ``` activity_email_clickthrough.ContactId = activity_page_view.ContactId ```  ``` activity_email_clickthrough.VisitorId = activity_page_view.VisitorId ``` |
| [activity\_subscribe](#activity-subscribe) | ``` activity_email_clickthrough.AssetId = activity_subscribe.AssetId ```  ``` activity_email_clickthrough.CampaignId = activity_subscribe.CampaignId ```  ``` activity_email_clickthrough.ContactId = activity_subscribe.ContactId ``` |
| [activity\_unsubscribe](#activity-unsubscribe) | ``` activity_email_clickthrough.AssetId = activity_unsubscribe.AssetId ```  ``` activity_email_clickthrough.CampaignId = activity_unsubscribe.CampaignId ```  ``` activity_email_clickthrough.ContactId = activity_unsubscribe.ContactId ``` |
| [activity\_web\_visit](#activity-web-visit) | ``` activity_email_clickthrough.AssetId = activity_web_visit.AssetId ``` |
| [campaigns](#campaigns) | ``` activity_email_clickthrough.CampaignId = campaigns.id ``` |
| [forms](#forms) | ``` activity_email_clickthrough.CampaignId = forms.processingSteps.campaignId ``` |
| [contacts](#contacts) | ``` activity_email_clickthrough.ContactId = contacts.Id ``` |
| [visitors](#visitors) | ``` activity_email_clickthrough.ContactId = visitors.contactId ```  ``` activity_email_clickthrough.VisitorId = visitors.id ``` |

activity\_email\_clickthrough table schema

|  |
| --- |
| **ActivityDate**  DATE-TIME |
| **ActivityId**  STRING |
| **ActivityType**  STRING |
| **AssetId**  STRING |
| **AssetName**  STRING |
| **AssetType**  STRING |
| **CampaignId**  INTEGER |
| **ContactId**  STRING |
| **DeploymentId**  STRING |
| **EmailAddress**  STRING |
| **EmailClickedThruLink**  STRING |
| **EmailRecipientId**  STRING |
| **EmailSendType**  STRING |
| **EmailWebLink**  STRING |
| **ExternalId**  STRING |
| **IpAddress**  STRING |
| **SubjectLine**  STRING |
| **Type**  STRING |
| **VisitorExternalId**  STRING |
| **VisitorId**  STRING |
| **id**  STRING |
| **updatedAt**  DATE-TIME |

### activity\_email\_open

The `activity_email_open` table contains info about `EmailOpen` contact activities.

**Note**: This table is replicated using the Eloqua Bulk API.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [Eloqua API method](https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAC/op-api-bulk-2.0-activities-exports-post.html "Opens in new tab: Eloqua API method") |

activity\_email\_open table foreign keys

| Join activity\_email\_open with | on |
| --- | --- |
| [assets](#assets) | ``` activity_email_open.AssetId = assets.id ``` |
| [activity\_bounceback](#activity-bounceback) | ``` activity_email_open.AssetId = activity_bounceback.AssetId ```  ``` activity_email_open.CampaignId = activity_bounceback.CampaignId ```  ``` activity_email_open.ContactId = activity_bounceback.ContactId ``` |
| [activity\_email\_clickthrough](#activity-email-clickthrough) | ``` activity_email_open.AssetId = activity_email_clickthrough.AssetId ```  ``` activity_email_open.CampaignId = activity_email_clickthrough.CampaignId ```  ``` activity_email_open.ContactId = activity_email_clickthrough.ContactId ```  ``` activity_email_open.VisitorId = activity_email_clickthrough.VisitorId ``` |
| [activity\_email\_send](#activity-email-send) | ``` activity_email_open.AssetId = activity_email_send.AssetId ```  ``` activity_email_open.CampaignId = activity_email_send.CampaignId ```  ``` activity_email_open.ContactId = activity_email_send.ContactId ``` |
| [activity\_form\_submit](#activity-form-submit) | ``` activity_email_open.AssetId = activity_form_submit.AssetId ```  ``` activity_email_open.CampaignId = activity_form_submit.CampaignId ```  ``` activity_email_open.ContactId = activity_form_submit.ContactId ```  ``` activity_email_open.VisitorId = activity_form_submit.VisitorId ``` |
| [activity\_page\_view](#activity-page-view) | ``` activity_email_open.AssetId = activity_page_view.AssetId ```  ``` activity_email_open.CampaignId = activity_page_view.CampaignId ```  ``` activity_email_open.ContactId = activity_page_view.ContactId ```  ``` activity_email_open.VisitorId = activity_page_view.VisitorId ``` |
| [activity\_subscribe](#activity-subscribe) | ``` activity_email_open.AssetId = activity_subscribe.AssetId ```  ``` activity_email_open.CampaignId = activity_subscribe.CampaignId ```  ``` activity_email_open.ContactId = activity_subscribe.ContactId ``` |
| [activity\_unsubscribe](#activity-unsubscribe) | ``` activity_email_open.AssetId = activity_unsubscribe.AssetId ```  ``` activity_email_open.CampaignId = activity_unsubscribe.CampaignId ```  ``` activity_email_open.ContactId = activity_unsubscribe.ContactId ``` |
| [activity\_web\_visit](#activity-web-visit) | ``` activity_email_open.AssetId = activity_web_visit.AssetId ``` |
| [campaigns](#campaigns) | ``` activity_email_open.CampaignId = campaigns.id ``` |
| [forms](#forms) | ``` activity_email_open.CampaignId = forms.processingSteps.campaignId ``` |
| [contacts](#contacts) | ``` activity_email_open.ContactId = contacts.Id ``` |
| [visitors](#visitors) | ``` activity_email_open.ContactId = visitors.contactId ```  ``` activity_email_open.VisitorId = visitors.id ``` |

activity\_email\_open table schema

|  |
| --- |
| **ActivityDate**  DATE-TIME |
| **ActivityType**  STRING |
| **AssetId**  STRING |
| **AssetName**  STRING |
| **AssetType**  STRING |
| **CampaignId**  INTEGER |
| **ContactId**  STRING |
| **DeploymentId**  STRING |
| **EmailAddress**  STRING |
| **EmailRecipientId**  STRING |
| **EmailWebLink**  STRING |
| **ExternalId**  STRING |
| **IpAddress**  STRING |
| **Type**  STRING |
| **VisitorExternalId**  STRING |
| **VisitorId**  STRING |
| **id**  STRING |
| **updatedAt**  DATE-TIME |

### activity\_email\_send

The `activity_email_send` table contains info about `EmailSend` contact activities.

**Note**: This table is replicated using the Eloqua Bulk API.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [Eloqua API method](https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAC/op-api-bulk-2.0-activities-exports-post.html "Opens in new tab: Eloqua API method") |

activity\_email\_send table foreign keys

| Join activity\_email\_send with | on |
| --- | --- |
| [assets](#assets) | ``` activity_email_send.AssetId = assets.id ``` |
| [activity\_bounceback](#activity-bounceback) | ``` activity_email_send.AssetId = activity_bounceback.AssetId ```  ``` activity_email_send.CampaignId = activity_bounceback.CampaignId ```  ``` activity_email_send.ContactId = activity_bounceback.ContactId ``` |
| [activity\_email\_clickthrough](#activity-email-clickthrough) | ``` activity_email_send.AssetId = activity_email_clickthrough.AssetId ```  ``` activity_email_send.CampaignId = activity_email_clickthrough.CampaignId ```  ``` activity_email_send.ContactId = activity_email_clickthrough.ContactId ``` |
| [activity\_email\_open](#activity-email-open) | ``` activity_email_send.AssetId = activity_email_open.AssetId ```  ``` activity_email_send.CampaignId = activity_email_open.CampaignId ```  ``` activity_email_send.ContactId = activity_email_open.ContactId ``` |
| [activity\_form\_submit](#activity-form-submit) | ``` activity_email_send.AssetId = activity_form_submit.AssetId ```  ``` activity_email_send.CampaignId = activity_form_submit.CampaignId ```  ``` activity_email_send.ContactId = activity_form_submit.ContactId ``` |
| [activity\_page\_view](#activity-page-view) | ``` activity_email_send.AssetId = activity_page_view.AssetId ```  ``` activity_email_send.CampaignId = activity_page_view.CampaignId ```  ``` activity_email_send.ContactId = activity_page_view.ContactId ``` |
| [activity\_subscribe](#activity-subscribe) | ``` activity_email_send.AssetId = activity_subscribe.AssetId ```  ``` activity_email_send.CampaignId = activity_subscribe.CampaignId ```  ``` activity_email_send.ContactId = activity_subscribe.ContactId ``` |
| [activity\_unsubscribe](#activity-unsubscribe) | ``` activity_email_send.AssetId = activity_unsubscribe.AssetId ```  ``` activity_email_send.CampaignId = activity_unsubscribe.CampaignId ```  ``` activity_email_send.ContactId = activity_unsubscribe.ContactId ``` |
| [activity\_web\_visit](#activity-web-visit) | ``` activity_email_send.AssetId = activity_web_visit.AssetId ``` |
| [campaigns](#campaigns) | ``` activity_email_send.CampaignId = campaigns.id ``` |
| [forms](#forms) | ``` activity_email_send.CampaignId = forms.processingSteps.campaignId ``` |
| [contacts](#contacts) | ``` activity_email_send.ContactId = contacts.Id ``` |
| [visitors](#visitors) | ``` activity_email_send.ContactId = visitors.contactId ``` |

activity\_email\_send table schema

|  |
| --- |
| **ActivityDate**  DATE-TIME |
| **ActivityId**  STRING |
| **ActivityType**  STRING |
| **AssetId**  STRING |
| **AssetName**  STRING |
| **AssetType**  STRING |
| **CampaignId**  INTEGER |
| **ContactId**  STRING |
| **DeploymentId**  STRING |
| **EmailAddress**  STRING |
| **EmailRecipientId**  STRING |
| **EmailSendType**  STRING |
| **EmailWebLink**  STRING |
| **ExternalId**  STRING |
| **SubjectLine**  STRING |
| **Type**  STRING |
| **id**  STRING |
| **updatedAt**  DATE-TIME |

### activity\_form\_submit

The `activity_form_submit` table contains info about `FormSubmit` contact activities.

**Note**: This table is replicated using the Eloqua Bulk API.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [Eloqua API method](https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAC/op-api-bulk-2.0-activities-exports-post.html "Opens in new tab: Eloqua API method") |

activity\_form\_submit table foreign keys

| Join activity\_form\_submit with | on |
| --- | --- |
| [assets](#assets) | ``` activity_form_submit.AssetId = assets.id ``` |
| [activity\_bounceback](#activity-bounceback) | ``` activity_form_submit.AssetId = activity_bounceback.AssetId ```  ``` activity_form_submit.CampaignId = activity_bounceback.CampaignId ```  ``` activity_form_submit.ContactId = activity_bounceback.ContactId ``` |
| [activity\_email\_clickthrough](#activity-email-clickthrough) | ``` activity_form_submit.AssetId = activity_email_clickthrough.AssetId ```  ``` activity_form_submit.CampaignId = activity_email_clickthrough.CampaignId ```  ``` activity_form_submit.ContactId = activity_email_clickthrough.ContactId ```  ``` activity_form_submit.VisitorId = activity_email_clickthrough.VisitorId ``` |
| [activity\_email\_open](#activity-email-open) | ``` activity_form_submit.AssetId = activity_email_open.AssetId ```  ``` activity_form_submit.CampaignId = activity_email_open.CampaignId ```  ``` activity_form_submit.ContactId = activity_email_open.ContactId ```  ``` activity_form_submit.VisitorId = activity_email_open.VisitorId ``` |
| [activity\_email\_send](#activity-email-send) | ``` activity_form_submit.AssetId = activity_email_send.AssetId ```  ``` activity_form_submit.CampaignId = activity_email_send.CampaignId ```  ``` activity_form_submit.ContactId = activity_email_send.ContactId ``` |
| [activity\_page\_view](#activity-page-view) | ``` activity_form_submit.AssetId = activity_page_view.AssetId ```  ``` activity_form_submit.CampaignId = activity_page_view.CampaignId ```  ``` activity_form_submit.ContactId = activity_page_view.ContactId ```  ``` activity_form_submit.VisitorId = activity_page_view.VisitorId ``` |
| [activity\_subscribe](#activity-subscribe) | ``` activity_form_submit.AssetId = activity_subscribe.AssetId ```  ``` activity_form_submit.CampaignId = activity_subscribe.CampaignId ```  ``` activity_form_submit.ContactId = activity_subscribe.ContactId ``` |
| [activity\_unsubscribe](#activity-unsubscribe) | ``` activity_form_submit.AssetId = activity_unsubscribe.AssetId ```  ``` activity_form_submit.CampaignId = activity_unsubscribe.CampaignId ```  ``` activity_form_submit.ContactId = activity_unsubscribe.ContactId ``` |
| [activity\_web\_visit](#activity-web-visit) | ``` activity_form_submit.AssetId = activity_web_visit.AssetId ``` |
| [campaigns](#campaigns) | ``` activity_form_submit.CampaignId = campaigns.id ``` |
| [forms](#forms) | ``` activity_form_submit.CampaignId = forms.processingSteps.campaignId ``` |
| [contacts](#contacts) | ``` activity_form_submit.ContactId = contacts.Id ``` |
| [visitors](#visitors) | ``` activity_form_submit.ContactId = visitors.contactId ```  ``` activity_form_submit.VisitorId = visitors.id ``` |

activity\_form\_submit table schema

|  |
| --- |
| **ActivityDate**  DATE-TIME |
| **ActivityType**  STRING |
| **AssetId**  STRING |
| **AssetName**  STRING |
| **AssetType**  STRING |
| **CampaignId**  INTEGER |
| **ContactId**  STRING |
| **ExternalId**  STRING |
| **RawData**  STRING |
| **Type**  STRING |
| **VisitorExternalId**  STRING |
| **VisitorId**  STRING |
| **id**  STRING |
| **updatedAt**  DATE-TIME |

### activity\_page\_view

The `activity_page_view` table contains info about `PageView` contact activities.

**Note**: This table is replicated using the Eloqua Bulk API.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [Eloqua API method](https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAC/op-api-bulk-2.0-activities-exports-post.html "Opens in new tab: Eloqua API method") |

activity\_page\_view table foreign keys

| Join activity\_page\_view with | on |
| --- | --- |
| [assets](#assets) | ``` activity_page_view.AssetId = assets.id ``` |
| [activity\_bounceback](#activity-bounceback) | ``` activity_page_view.AssetId = activity_bounceback.AssetId ```  ``` activity_page_view.CampaignId = activity_bounceback.CampaignId ```  ``` activity_page_view.ContactId = activity_bounceback.ContactId ``` |
| [activity\_email\_clickthrough](#activity-email-clickthrough) | ``` activity_page_view.AssetId = activity_email_clickthrough.AssetId ```  ``` activity_page_view.CampaignId = activity_email_clickthrough.CampaignId ```  ``` activity_page_view.ContactId = activity_email_clickthrough.ContactId ```  ``` activity_page_view.VisitorId = activity_email_clickthrough.VisitorId ``` |
| [activity\_email\_open](#activity-email-open) | ``` activity_page_view.AssetId = activity_email_open.AssetId ```  ``` activity_page_view.CampaignId = activity_email_open.CampaignId ```  ``` activity_page_view.ContactId = activity_email_open.ContactId ```  ``` activity_page_view.VisitorId = activity_email_open.VisitorId ``` |
| [activity\_email\_send](#activity-email-send) | ``` activity_page_view.AssetId = activity_email_send.AssetId ```  ``` activity_page_view.CampaignId = activity_email_send.CampaignId ```  ``` activity_page_view.ContactId = activity_email_send.ContactId ``` |
| [activity\_form\_submit](#activity-form-submit) | ``` activity_page_view.AssetId = activity_form_submit.AssetId ```  ``` activity_page_view.CampaignId = activity_form_submit.CampaignId ```  ``` activity_page_view.ContactId = activity_form_submit.ContactId ```  ``` activity_page_view.VisitorId = activity_form_submit.VisitorId ``` |
| [activity\_subscribe](#activity-subscribe) | ``` activity_page_view.AssetId = activity_subscribe.AssetId ```  ``` activity_page_view.CampaignId = activity_subscribe.CampaignId ```  ``` activity_page_view.ContactId = activity_subscribe.ContactId ``` |
| [activity\_unsubscribe](#activity-unsubscribe) | ``` activity_page_view.AssetId = activity_unsubscribe.AssetId ```  ``` activity_page_view.CampaignId = activity_unsubscribe.CampaignId ```  ``` activity_page_view.ContactId = activity_unsubscribe.ContactId ``` |
| [activity\_web\_visit](#activity-web-visit) | ``` activity_page_view.AssetId = activity_web_visit.AssetId ``` |
| [campaigns](#campaigns) | ``` activity_page_view.CampaignId = campaigns.id ``` |
| [forms](#forms) | ``` activity_page_view.CampaignId = forms.processingSteps.campaignId ``` |
| [contacts](#contacts) | ``` activity_page_view.ContactId = contacts.Id ``` |
| [visitors](#visitors) | ``` activity_page_view.ContactId = visitors.contactId ```  ``` activity_page_view.VisitorId = visitors.id ``` |

activity\_page\_view table schema

|  |
| --- |
| **ActivityDate**  DATE-TIME |
| **ActivityId**  STRING |
| **ActivityType**  STRING |
| **AssetId**  STRING |
| **AssetName**  STRING |
| **AssetType**  STRING |
| **CampaignId**  INTEGER |
| **ContactId**  STRING |
| **ExternalId**  STRING |
| **IpAddress**  STRING |
| **Type**  STRING |
| **Url**  STRING |
| **VisitorExternalId**  STRING |
| **VisitorId**  STRING |
| **WebVisitId**  STRING |
| **id**  STRING |
| **updatedAt**  DATE-TIME |

### activity\_subscribe

The `activity_subscribe` table contains info about `Subscribe` contact activities.

**Note**: This table is replicated using the Eloqua Bulk API.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [Eloqua API method](https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAC/op-api-bulk-2.0-activities-exports-post.html "Opens in new tab: Eloqua API method") |

activity\_subscribe table foreign keys

| Join activity\_subscribe with | on |
| --- | --- |
| [assets](#assets) | ``` activity_subscribe.AssetId = assets.id ``` |
| [activity\_bounceback](#activity-bounceback) | ``` activity_subscribe.AssetId = activity_bounceback.AssetId ```  ``` activity_subscribe.CampaignId = activity_bounceback.CampaignId ```  ``` activity_subscribe.ContactId = activity_bounceback.ContactId ``` |
| [activity\_email\_clickthrough](#activity-email-clickthrough) | ``` activity_subscribe.AssetId = activity_email_clickthrough.AssetId ```  ``` activity_subscribe.CampaignId = activity_email_clickthrough.CampaignId ```  ``` activity_subscribe.ContactId = activity_email_clickthrough.ContactId ``` |
| [activity\_email\_open](#activity-email-open) | ``` activity_subscribe.AssetId = activity_email_open.AssetId ```  ``` activity_subscribe.CampaignId = activity_email_open.CampaignId ```  ``` activity_subscribe.ContactId = activity_email_open.ContactId ``` |
| [activity\_email\_send](#activity-email-send) | ``` activity_subscribe.AssetId = activity_email_send.AssetId ```  ``` activity_subscribe.CampaignId = activity_email_send.CampaignId ```  ``` activity_subscribe.ContactId = activity_email_send.ContactId ``` |
| [activity\_form\_submit](#activity-form-submit) | ``` activity_subscribe.AssetId = activity_form_submit.AssetId ```  ``` activity_subscribe.CampaignId = activity_form_submit.CampaignId ```  ``` activity_subscribe.ContactId = activity_form_submit.ContactId ``` |
| [activity\_page\_view](#activity-page-view) | ``` activity_subscribe.AssetId = activity_page_view.AssetId ```  ``` activity_subscribe.CampaignId = activity_page_view.CampaignId ```  ``` activity_subscribe.ContactId = activity_page_view.ContactId ``` |
| [activity\_unsubscribe](#activity-unsubscribe) | ``` activity_subscribe.AssetId = activity_unsubscribe.AssetId ```  ``` activity_subscribe.CampaignId = activity_unsubscribe.CampaignId ```  ``` activity_subscribe.ContactId = activity_unsubscribe.ContactId ``` |
| [activity\_web\_visit](#activity-web-visit) | ``` activity_subscribe.AssetId = activity_web_visit.AssetId ``` |
| [campaigns](#campaigns) | ``` activity_subscribe.CampaignId = campaigns.id ``` |
| [forms](#forms) | ``` activity_subscribe.CampaignId = forms.processingSteps.campaignId ``` |
| [contacts](#contacts) | ``` activity_subscribe.ContactId = contacts.Id ``` |
| [visitors](#visitors) | ``` activity_subscribe.ContactId = visitors.contactId ``` |

activity\_subscribe table schema

|  |
| --- |
| **ActivityDate**  DATE-TIME |
| **ActivityId**  STRING |
| **ActivityType**  STRING |
| **AssetId**  STRING |
| **AssetName**  STRING |
| **AssetType**  STRING |
| **CampaignId**  INTEGER |
| **ContactId**  STRING |
| **EmailAddress**  STRING |
| **EmailRecipientId**  STRING |
| **ExternalId**  STRING |
| **Type**  STRING |
| **id**  STRING |
| **updatedAt**  DATE-TIME |

### activity\_unsubscribe

The `activity_unsubscribe` table contains info about `Unsubscribe` contact activities.

**Note**: This table is replicated using the Eloqua Bulk API.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [Eloqua API method](https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAC/op-api-bulk-2.0-activities-exports-post.html "Opens in new tab: Eloqua API method") |

activity\_unsubscribe table foreign keys

| Join activity\_unsubscribe with | on |
| --- | --- |
| [assets](#assets) | ``` activity_unsubscribe.AssetId = assets.id ``` |
| [activity\_bounceback](#activity-bounceback) | ``` activity_unsubscribe.AssetId = activity_bounceback.AssetId ```  ``` activity_unsubscribe.CampaignId = activity_bounceback.CampaignId ```  ``` activity_unsubscribe.ContactId = activity_bounceback.ContactId ``` |
| [activity\_email\_clickthrough](#activity-email-clickthrough) | ``` activity_unsubscribe.AssetId = activity_email_clickthrough.AssetId ```  ``` activity_unsubscribe.CampaignId = activity_email_clickthrough.CampaignId ```  ``` activity_unsubscribe.ContactId = activity_email_clickthrough.ContactId ``` |
| [activity\_email\_open](#activity-email-open) | ``` activity_unsubscribe.AssetId = activity_email_open.AssetId ```  ``` activity_unsubscribe.CampaignId = activity_email_open.CampaignId ```  ``` activity_unsubscribe.ContactId = activity_email_open.ContactId ``` |
| [activity\_email\_send](#activity-email-send) | ``` activity_unsubscribe.AssetId = activity_email_send.AssetId ```  ``` activity_unsubscribe.CampaignId = activity_email_send.CampaignId ```  ``` activity_unsubscribe.ContactId = activity_email_send.ContactId ``` |
| [activity\_form\_submit](#activity-form-submit) | ``` activity_unsubscribe.AssetId = activity_form_submit.AssetId ```  ``` activity_unsubscribe.CampaignId = activity_form_submit.CampaignId ```  ``` activity_unsubscribe.ContactId = activity_form_submit.ContactId ``` |
| [activity\_page\_view](#activity-page-view) | ``` activity_unsubscribe.AssetId = activity_page_view.AssetId ```  ``` activity_unsubscribe.CampaignId = activity_page_view.CampaignId ```  ``` activity_unsubscribe.ContactId = activity_page_view.ContactId ``` |
| [activity\_subscribe](#activity-subscribe) | ``` activity_unsubscribe.AssetId = activity_subscribe.AssetId ```  ``` activity_unsubscribe.CampaignId = activity_subscribe.CampaignId ```  ``` activity_unsubscribe.ContactId = activity_subscribe.ContactId ``` |
| [activity\_web\_visit](#activity-web-visit) | ``` activity_unsubscribe.AssetId = activity_web_visit.AssetId ``` |
| [campaigns](#campaigns) | ``` activity_unsubscribe.CampaignId = campaigns.id ``` |
| [forms](#forms) | ``` activity_unsubscribe.CampaignId = forms.processingSteps.campaignId ``` |
| [contacts](#contacts) | ``` activity_unsubscribe.ContactId = contacts.Id ``` |
| [visitors](#visitors) | ``` activity_unsubscribe.ContactId = visitors.contactId ``` |

activity\_unsubscribe table schema

|  |
| --- |
| **ActivityDate**  DATE-TIME |
| **ActivityId**  STRING |
| **ActivityType**  STRING |
| **AssetId**  STRING |
| **AssetName**  STRING |
| **AssetType**  STRING |
| **CampaignId**  INTEGER |
| **ContactId**  STRING |
| **EmailAddress**  STRING |
| **EmailRecipientId**  STRING |
| **ExternalId**  STRING |
| **Type**  STRING |
| **id**  STRING |
| **updatedAt**  DATE-TIME |

### activity\_web\_visit

The `activity_web_visit` table contains info about `WebVisit` contact activities.

**Note**: This table is replicated using the Eloqua Bulk API.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [Eloqua API method](https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAC/op-api-bulk-2.0-activities-exports-post.html "Opens in new tab: Eloqua API method") |

activity\_web\_visit table foreign keys

| Join activity\_web\_visit with | on |
| --- | --- |
| [assets](#assets) | ``` activity_web_visit.AssetId = assets.id ``` |
| [activity\_bounceback](#activity-bounceback) | ``` activity_web_visit.AssetId = activity_bounceback.AssetId ``` |
| [activity\_email\_clickthrough](#activity-email-clickthrough) | ``` activity_web_visit.AssetId = activity_email_clickthrough.AssetId ``` |
| [activity\_email\_open](#activity-email-open) | ``` activity_web_visit.AssetId = activity_email_open.AssetId ``` |
| [activity\_email\_send](#activity-email-send) | ``` activity_web_visit.AssetId = activity_email_send.AssetId ``` |
| [activity\_form\_submit](#activity-form-submit) | ``` activity_web_visit.AssetId = activity_form_submit.AssetId ``` |
| [activity\_page\_view](#activity-page-view) | ``` activity_web_visit.AssetId = activity_page_view.AssetId ``` |
| [activity\_subscribe](#activity-subscribe) | ``` activity_web_visit.AssetId = activity_subscribe.AssetId ``` |
| [activity\_unsubscribe](#activity-unsubscribe) | ``` activity_web_visit.AssetId = activity_unsubscribe.AssetId ``` |

activity\_web\_visit table schema

|  |
| --- |
| **ActivityDate**  DATE-TIME |
| **ActivityType**  STRING |
| **AssetId**  STRING |
| **AssetType**  STRING |
| **ContactId**  STRING |
| **Type**  STRING |
| **id**  STRING |
| **updatedAt**  DATE-TIME |

### assets

The `assets` table contains info about the external assets associated with your Eloqua account. External assets are non-Eloqua, or offline, activities performed by your contacts or prospects.

**Note**: This table is replicated using the Eloqua Application REST API.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [Eloqua API method](https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAC/op-api-rest-2.0-assets-externals-get.html "Opens in new tab: Eloqua API method") |

assets table foreign keys

| Join assets with | on |
| --- | --- |
| [activity\_bounceback](#activity-bounceback) | ``` assets.id = activity_bounceback.AssetId ``` |
| [activity\_email\_clickthrough](#activity-email-clickthrough) | ``` assets.id = activity_email_clickthrough.AssetId ``` |
| [activity\_email\_open](#activity-email-open) | ``` assets.id = activity_email_open.AssetId ``` |
| [activity\_email\_send](#activity-email-send) | ``` assets.id = activity_email_send.AssetId ``` |
| [activity\_form\_submit](#activity-form-submit) | ``` assets.id = activity_form_submit.AssetId ``` |
| [activity\_page\_view](#activity-page-view) | ``` assets.id = activity_page_view.AssetId ``` |
| [activity\_subscribe](#activity-subscribe) | ``` assets.id = activity_subscribe.AssetId ``` |
| [activity\_unsubscribe](#activity-unsubscribe) | ``` assets.id = activity_unsubscribe.AssetId ``` |
| [activity\_web\_visit](#activity-web-visit) | ``` assets.id = activity_web_visit.AssetId ``` |
| [campaigns](#campaigns) | ``` assets.folderId = campaigns.folderId ```  ``` assets.createdBy = campaigns.createdBy ```  ``` assets.updatedBy = campaigns.createdBy ```  ``` assets.createdBy = campaigns.updatedBy ```  ``` assets.updatedBy = campaigns.updatedBy ```  ``` assets.createdBy = campaigns.runAsUserId ```  ``` assets.updatedBy = campaigns.runAsUserId ``` |
| [emails](#emails) | ``` assets.folderId = emails.dynamicContents.folderId ```  ``` assets.folderId = emails.hyperlinks.folderId ```  ``` assets.folderId = emails.images.folderId ```  ``` assets.createdBy = emails.createdBy ```  ``` assets.updatedBy = emails.createdBy ```  ``` assets.createdBy = emails.dynamicContents.createdBy ```  ``` assets.updatedBy = emails.dynamicContents.createdBy ```  ``` assets.createdBy = emails.dynamicContents.updatedBy ```  ``` assets.updatedBy = emails.dynamicContents.updatedBy ```  ``` assets.createdBy = emails.fieldMerges.createdBy ```  ``` assets.updatedBy = emails.fieldMerges.createdBy ```  ``` assets.createdBy = emails.fieldMerges.updatedBy ```  ``` assets.updatedBy = emails.fieldMerges.updatedBy ```  ``` assets.createdBy = emails.hyperlinks.createdBy ```  ``` assets.updatedBy = emails.hyperlinks.createdBy ```  ``` assets.createdBy = emails.hyperlinks.updatedBy ```  ``` assets.updatedBy = emails.hyperlinks.updatedBy ```  ``` assets.createdBy = emails.images.createdBy ```  ``` assets.updatedBy = emails.images.createdBy ```  ``` assets.createdBy = emails.images.updatedBy ```  ``` assets.updatedBy = emails.images.updatedBy ```  ``` assets.createdBy = emails.updatedBy ```  ``` assets.updatedBy = emails.updatedBy ``` |
| [forms](#forms) | ``` assets.folderId = forms.folderId ``` |

assets table schema

|  |
| --- |
| **accessedAt**  DATE-TIME |
| **createdAt**  DATE-TIME |
| **createdBy**  STRING |
| **currentStatus**  STRING |
| **depth**  STRING |
| **description**  STRING |
| **externalAssetTypeId**  STRING |
| **folderId**  STRING |
| **id**  STRING |
| **name**  STRING |
| **permissions**  ARRAY This is a nested data structure. |
| **scheduledFor**  STRING |
| **sourceTemplateId**  STRING |
| **type**  STRING |
| **updatedAt**  DATE-TIME |
| **updatedBy**  STRING |

### campaigns

The `campaigns` table contains info about the campaigns in your Eloqua account. Campaigns are comprised of different elements (such as segments, emails, landing pages, etc.) that are used to perform a variety of functions.

**Note**: This table is replicated using the Eloqua Application REST API.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [Eloqua API method](https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAC/op-api-rest-2.0-assets-campaigns-get.html "Opens in new tab: Eloqua API method") |

campaigns table foreign keys

| Join campaigns with | on |
| --- | --- |
| [activity\_bounceback](#activity-bounceback) | ``` campaigns.id = activity_bounceback.CampaignId ``` |
| [activity\_email\_clickthrough](#activity-email-clickthrough) | ``` campaigns.id = activity_email_clickthrough.CampaignId ``` |
| [activity\_email\_open](#activity-email-open) | ``` campaigns.id = activity_email_open.CampaignId ``` |
| [activity\_email\_send](#activity-email-send) | ``` campaigns.id = activity_email_send.CampaignId ``` |
| [activity\_form\_submit](#activity-form-submit) | ``` campaigns.id = activity_form_submit.CampaignId ``` |
| [activity\_page\_view](#activity-page-view) | ``` campaigns.id = activity_page_view.CampaignId ``` |
| [activity\_subscribe](#activity-subscribe) | ``` campaigns.id = activity_subscribe.CampaignId ``` |
| [activity\_unsubscribe](#activity-unsubscribe) | ``` campaigns.id = activity_unsubscribe.CampaignId ``` |
| [forms](#forms) | ``` campaigns.id = forms.processingSteps.campaignId ```  ``` campaigns.folderId = forms.folderId ``` |
| [assets](#assets) | ``` campaigns.folderId = assets.folderId ```  ``` campaigns.createdBy = assets.createdBy ```  ``` campaigns.updatedBy = assets.createdBy ```  ``` campaigns.runAsUserId = assets.createdBy ```  ``` campaigns.createdBy = assets.updatedBy ```  ``` campaigns.updatedBy = assets.updatedBy ```  ``` campaigns.runAsUserId = assets.updatedBy ``` |
| [emails](#emails) | ``` campaigns.folderId = emails.dynamicContents.folderId ```  ``` campaigns.folderId = emails.hyperlinks.folderId ```  ``` campaigns.folderId = emails.images.folderId ```  ``` campaigns.createdBy = emails.createdBy ```  ``` campaigns.updatedBy = emails.createdBy ```  ``` campaigns.runAsUserId = emails.createdBy ```  ``` campaigns.createdBy = emails.dynamicContents.createdBy ```  ``` campaigns.updatedBy = emails.dynamicContents.createdBy ```  ``` campaigns.runAsUserId = emails.dynamicContents.createdBy ```  ``` campaigns.createdBy = emails.dynamicContents.updatedBy ```  ``` campaigns.updatedBy = emails.dynamicContents.updatedBy ```  ``` campaigns.runAsUserId = emails.dynamicContents.updatedBy ```  ``` campaigns.createdBy = emails.fieldMerges.createdBy ```  ``` campaigns.updatedBy = emails.fieldMerges.createdBy ```  ``` campaigns.runAsUserId = emails.fieldMerges.createdBy ```  ``` campaigns.createdBy = emails.fieldMerges.updatedBy ```  ``` campaigns.updatedBy = emails.fieldMerges.updatedBy ```  ``` campaigns.runAsUserId = emails.fieldMerges.updatedBy ```  ``` campaigns.createdBy = emails.hyperlinks.createdBy ```  ``` campaigns.updatedBy = emails.hyperlinks.createdBy ```  ``` campaigns.runAsUserId = emails.hyperlinks.createdBy ```  ``` campaigns.createdBy = emails.hyperlinks.updatedBy ```  ``` campaigns.updatedBy = emails.hyperlinks.updatedBy ```  ``` campaigns.runAsUserId = emails.hyperlinks.updatedBy ```  ``` campaigns.createdBy = emails.images.createdBy ```  ``` campaigns.updatedBy = emails.images.createdBy ```  ``` campaigns.runAsUserId = emails.images.createdBy ```  ``` campaigns.createdBy = emails.images.updatedBy ```  ``` campaigns.updatedBy = emails.images.updatedBy ```  ``` campaigns.runAsUserId = emails.images.updatedBy ```  ``` campaigns.createdBy = emails.updatedBy ```  ``` campaigns.updatedBy = emails.updatedBy ```  ``` campaigns.runAsUserId = emails.updatedBy ``` |

campaigns table schema

|  |
| --- |
| **accessedAt**  DATE-TIME |
| **actualCost**  STRING |
| **badgeId**  STRING |
| **budgetedCost**  STRING |
| **campaignCategory**  STRING |
| **campaignType**  STRING |
| **clrEndDate**  DATE-TIME |
| **createdAt**  DATE-TIME |
| **createdBy**  STRING |
| **crmId**  STRING |
| **currentStatus**  STRING |
| **depth**  STRING |
| **description**  STRING |
| **elements**  ARRAY This is a nested data structure. |
| **endAt**  DATE-TIME |
| **fieldValues**  ARRAY This is a nested data structure. |
| **firstActivation**  DATE-TIME |
| **folderId**  STRING |
| **id**  STRING |
| **isEmailMarketingCampaign**  STRING |
| **isIncludedInROI**  STRING |
| **isMemberAllowedReEntry**  STRING |
| **isReadOnly**  STRING |
| **isSyncedWithCRM**  STRING |
| **memberCount**  STRING |
| **name**  STRING |
| **permissions**  ARRAY This is a nested data structure. |
| **product**  STRING |
| **region**  STRING |
| **runAsUserId**  STRING |
| **scheduledFor**  DATE-TIME |
| **sourceTemplateId**  STRING |
| **startAt**  DATE-TIME |
| **type**  STRING |
| **updatedAt**  DATE-TIME |
| **updatedBy**  STRING |

### contacts

The `contacts` table contains info the contacts in your Eloqua account.

**Note**: This table is replicated using the Eloqua Bulk API.

#### Custom contacts fields

If applicable, Stitch will replicate custom fields related to `contacts` in Eloqua.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | Id |
| **Replication Key** | UpdatedAt |
| **Useful links** | [Eloqua API method](https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAC/op-api-bulk-2.0-contacts-exports-post.html "Opens in new tab: Eloqua API method") |

contacts table foreign keys

| Join contacts with | on |
| --- | --- |
| [activity\_bounceback](#activity-bounceback) | ``` contacts.Id = activity_bounceback.ContactId ``` |
| [activity\_email\_clickthrough](#activity-email-clickthrough) | ``` contacts.Id = activity_email_clickthrough.ContactId ``` |
| [activity\_email\_open](#activity-email-open) | ``` contacts.Id = activity_email_open.ContactId ``` |
| [activity\_email\_send](#activity-email-send) | ``` contacts.Id = activity_email_send.ContactId ``` |
| [activity\_form\_submit](#activity-form-submit) | ``` contacts.Id = activity_form_submit.ContactId ``` |
| [activity\_page\_view](#activity-page-view) | ``` contacts.Id = activity_page_view.ContactId ``` |
| [activity\_subscribe](#activity-subscribe) | ``` contacts.Id = activity_subscribe.ContactId ``` |
| [activity\_unsubscribe](#activity-unsubscribe) | ``` contacts.Id = activity_unsubscribe.ContactId ``` |
| [visitors](#visitors) | ``` contacts.Id = visitors.contactId ``` |

contacts table schema

|  |
| --- |
| **AccountName**  STRING |
| **ContactIDExt**  STRING |
| **CreatedAt**  DATE-TIME |
| **Custom Fields**  VARIES |
| **EmailFormat**  STRING |
| **Id**  STRING |
| **IsBounceBack**  STRING |
| **IsSubscribed**  STRING |
| **UpdatedAt**  DATE-TIME |

### custom\_objects

For each custom object in your Eloqua account, Stitch will display a table as available for selection. The name of the table will be the normalized name of the object, using snake case (spaces replaced with underscores) and removing special characters. For example: If your account contains an `Enrichement Attributes` custom object, there will be a corresponding `enrichment_attributes` available for selection in Stitch.

**Note**: This table is replicated using the Eloqua Bulk API.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | UpdatedAt |
| **Useful links** | [Eloqua API method](https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAC/op-api-bulk-2.0-customobjects-parentid-exports-post.html "Opens in new tab: Eloqua API method") |

custom\_objects table schema

|  |
| --- |
| **CreatedAt**  DATE-TIME |
| **Custom Fields**  VARIES |
| **DataCardIDExt**  STRING |
| **UpdatedAt**  DATE-TIME |
| **id**  STRING |

### emailGroups

The `emailGroups` table contains details about the email groups in your Eloqua account.

**Note**: This table is replicated using the Eloqua Application REST API.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [Eloqua API method](https://docs.oracle.com/en/cloud/saas/marketing/eloqua-rest-api/op-api-rest-1.0-assets-email-groups-get.html "Opens in new tab: Eloqua API method") |

emailGroups table foreign keys

| Join emailGroups with | on |
| --- | --- |
| [emails](#emails) | ``` emailGroups.emailFooterId = emails.emailFooterId ```  ``` emailGroups.emailHeaderId = emails.emailHeaderId ``` |

emailGroups table schema

|  |
| --- |
| **createdAt**  DATE-TIME |
| **createdBy**  STRING |
| **depth**  STRING |
| **displayName**  STRING |
| **emailFooterId**  STRING |
| **emailHeaderId**  STRING |
| **id**  STRING |
| **isSecureNotificationsGroup**  STRING |
| **isVisibleInOutlookPlugin**  STRING |
| **isVisibleInPublicSubscriptionList**  STRING |
| **isWelcomeCommunicationsGroup**  STRING |
| **name**  STRING |
| **notificationEmailId**  STRING |
| **requireOptIn**  STRING |
| **subscriptionLandingPageId**  STRING |
| **subscriptionListDataLookupId**  STRING |
| **subscriptionListId**  STRING |
| **type**  STRING |
| **unSubscriptionListDataLookupId**  STRING |
| **unSubscriptionListId**  STRING |
| **unsubscriptionLandingPageId**  STRING |
| **updatedAt**  DATE-TIME |
| **updatedBy**  STRING |
| **useSecureChannel**  STRING |

### emails

The `emails` table contains details about the emails sent from your Eloqua account.

**Note**: This table is replicated using the Eloqua Application REST API.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [Eloqua API method](https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAC/op-api-rest-1.0-assets-emails-get.html "Opens in new tab: Eloqua API method") |

emails table foreign keys

| Join emails with | on |
| --- | --- |
| [forms](#forms) | ``` emails.id = forms.processingSteps.emailId ```  ``` emails.dynamicContents.folderId = forms.folderId ```  ``` emails.hyperlinks.folderId = forms.folderId ```  ``` emails.images.folderId = forms.folderId ``` |
| [emailGroups](#emailgroups) | ``` emails.emailFooterId = emailGroups.emailFooterId ```  ``` emails.emailHeaderId = emailGroups.emailHeaderId ``` |
| [assets](#assets) | ``` emails.dynamicContents.folderId = assets.folderId ```  ``` emails.hyperlinks.folderId = assets.folderId ```  ``` emails.images.folderId = assets.folderId ```  ``` emails.createdBy = assets.createdBy ```  ``` emails.dynamicContents.createdBy = assets.createdBy ```  ``` emails.dynamicContents.updatedBy = assets.createdBy ```  ``` emails.fieldMerges.createdBy = assets.createdBy ```  ``` emails.fieldMerges.updatedBy = assets.createdBy ```  ``` emails.hyperlinks.createdBy = assets.createdBy ```  ``` emails.hyperlinks.updatedBy = assets.createdBy ```  ``` emails.images.createdBy = assets.createdBy ```  ``` emails.images.updatedBy = assets.createdBy ```  ``` emails.updatedBy = assets.createdBy ```  ``` emails.createdBy = assets.updatedBy ```  ``` emails.dynamicContents.createdBy = assets.updatedBy ```  ``` emails.dynamicContents.updatedBy = assets.updatedBy ```  ``` emails.fieldMerges.createdBy = assets.updatedBy ```  ``` emails.fieldMerges.updatedBy = assets.updatedBy ```  ``` emails.hyperlinks.createdBy = assets.updatedBy ```  ``` emails.hyperlinks.updatedBy = assets.updatedBy ```  ``` emails.images.createdBy = assets.updatedBy ```  ``` emails.images.updatedBy = assets.updatedBy ```  ``` emails.updatedBy = assets.updatedBy ``` |
| [campaigns](#campaigns) | ``` emails.dynamicContents.folderId = campaigns.folderId ```  ``` emails.hyperlinks.folderId = campaigns.folderId ```  ``` emails.images.folderId = campaigns.folderId ```  ``` emails.createdBy = campaigns.createdBy ```  ``` emails.dynamicContents.createdBy = campaigns.createdBy ```  ``` emails.dynamicContents.updatedBy = campaigns.createdBy ```  ``` emails.fieldMerges.createdBy = campaigns.createdBy ```  ``` emails.fieldMerges.updatedBy = campaigns.createdBy ```  ``` emails.hyperlinks.createdBy = campaigns.createdBy ```  ``` emails.hyperlinks.updatedBy = campaigns.createdBy ```  ``` emails.images.createdBy = campaigns.createdBy ```  ``` emails.images.updatedBy = campaigns.createdBy ```  ``` emails.updatedBy = campaigns.createdBy ```  ``` emails.createdBy = campaigns.updatedBy ```  ``` emails.dynamicContents.createdBy = campaigns.updatedBy ```  ``` emails.dynamicContents.updatedBy = campaigns.updatedBy ```  ``` emails.fieldMerges.createdBy = campaigns.updatedBy ```  ``` emails.fieldMerges.updatedBy = campaigns.updatedBy ```  ``` emails.hyperlinks.createdBy = campaigns.updatedBy ```  ``` emails.hyperlinks.updatedBy = campaigns.updatedBy ```  ``` emails.images.createdBy = campaigns.updatedBy ```  ``` emails.images.updatedBy = campaigns.updatedBy ```  ``` emails.updatedBy = campaigns.updatedBy ```  ``` emails.createdBy = campaigns.runAsUserId ```  ``` emails.dynamicContents.createdBy = campaigns.runAsUserId ```  ``` emails.dynamicContents.updatedBy = campaigns.runAsUserId ```  ``` emails.fieldMerges.createdBy = campaigns.runAsUserId ```  ``` emails.fieldMerges.updatedBy = campaigns.runAsUserId ```  ``` emails.hyperlinks.createdBy = campaigns.runAsUserId ```  ``` emails.hyperlinks.updatedBy = campaigns.runAsUserId ```  ``` emails.images.createdBy = campaigns.runAsUserId ```  ``` emails.images.updatedBy = campaigns.runAsUserId ```  ``` emails.updatedBy = campaigns.runAsUserId ``` |

emails table schema

|  |
| --- |
| **accessedAt**  DATE-TIME |
| **archive**  BOOLEAN |
| **bounceBackEmail**  STRING |
| **contentSections**  ARRAY This is a nested data structure. |
| **createdAt**  DATE-TIME |
| **createdBy**  STRING |
| **currentStatus**  STRING |
| **depth**  STRING |
| **description**  STRING |
| **dynamicContents**  ARRAY This is a nested data structure:   - createdAt: DATE-TIME - createdBy: STRING - defaultContentSection: STRING - depth: STRING - description: STRING - folderId: STRING - id: STRING - name: STRING - permissions: STRING - rules: STRING - type: STRING - updatedAt: DATE-TIME - updatedBy: STRING |
| **emailFooterId**  STRING |
| **emailGroupId**  STRING |
| **emailHeaderId**  STRING |
| **encodingId**  STRING |
| **fieldMerges**  ARRAY This is a nested data structure:   - allowUrlsInValue: STRING - contactFieldId: STRING - createdAt: DATE-TIME - createdBy: STRING - defaultValue: STRING - depth: STRING - eventId: STRING - eventSessionFieldId: STRING - fieldConditions: STRING - folderId: STRING - id: STRING - mergeType: STRING - name: STRING - syntax: STRING - type: STRING - updatedAt: DATE-TIME - updatedBy: STRING |
| **files**  ARRAY This is a nested data structure. |
| **folderId**  STRING |
| **forms**  ARRAY This is a nested data structure. |
| **htmlContent**  OBJECT This is a nested data structure:   - contentSource: STRING - cssHeader: STRING - docType: STRING - documentDescription: STRING - html: STRING - htmlBody: STRING - metaTags: ARRAY, which is also a nested data structure. - root: STRING - systemHeader: STRING - type: STRING |
| **hyperlinks**  ARRAY This is a nested data structure:   - createdAt: DATE-TIME - createdBy: STRING - depth: STRING - folderId: STRING - href: STRING - hyperlinkType: STRING - id: STRING - name: STRING - referencedEntityId: STRING - type: STRING - updatedAt: DATE-TIME - updatedBy: STRING |
| **id**  STRING |
| **images**  ARRAY This is a nested data structure. |
| **isContentProtected**  BOOLEAN |
| **isPlainTextEditable**  STRING |
| **isPrivate**  BOOLEAN |
| **isTracked**  STRING |
| **landingPages**  ARRAY This is a nested data structure. |
| **layout**  STRING |
| **name**  STRING |
| **permissions**  STRING |
| **plainText**  STRING |
| **renderMode**  STRING |
| **replyToEmail**  STRING |
| **replyToName**  STRING |
| **sendPlainTextOnly**  STRING |
| **senderEmail**  STRING |
| **senderName**  STRING |
| **sourceTemplateId**  STRING |
| **style**  STRING |
| **subject**  STRING |
| **type**  STRING |
| **updatedAt**  DATE-TIME |
| **updatedBy**  STRING |
| **virtualMTAId**  STRING |

### forms

The `forms` table contains info about the forms in your Eloqua account.

**Note**: This table is replicated using the Eloqua Application REST API.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [Eloqua API method](https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAC/op-api-rest-1.0-assets-forms-get.html "Opens in new tab: Eloqua API method") |

forms table foreign keys

| Join forms with | on |
| --- | --- |
| [campaigns](#campaigns) | ``` forms.processingSteps.campaignId = campaigns.id ```  ``` forms.folderId = campaigns.folderId ``` |
| [activity\_bounceback](#activity-bounceback) | ``` forms.processingSteps.campaignId = activity_bounceback.CampaignId ``` |
| [activity\_email\_clickthrough](#activity-email-clickthrough) | ``` forms.processingSteps.campaignId = activity_email_clickthrough.CampaignId ``` |
| [activity\_email\_open](#activity-email-open) | ``` forms.processingSteps.campaignId = activity_email_open.CampaignId ``` |
| [activity\_email\_send](#activity-email-send) | ``` forms.processingSteps.campaignId = activity_email_send.CampaignId ``` |
| [activity\_form\_submit](#activity-form-submit) | ``` forms.processingSteps.campaignId = activity_form_submit.CampaignId ``` |
| [activity\_page\_view](#activity-page-view) | ``` forms.processingSteps.campaignId = activity_page_view.CampaignId ``` |
| [activity\_subscribe](#activity-subscribe) | ``` forms.processingSteps.campaignId = activity_subscribe.CampaignId ``` |
| [activity\_unsubscribe](#activity-unsubscribe) | ``` forms.processingSteps.campaignId = activity_unsubscribe.CampaignId ``` |
| [emails](#emails) | ``` forms.processingSteps.emailId = emails.id ```  ``` forms.folderId = emails.dynamicContents.folderId ```  ``` forms.folderId = emails.hyperlinks.folderId ```  ``` forms.folderId = emails.images.folderId ``` |
| [assets](#assets) | ``` forms.folderId = assets.folderId ``` |

forms table schema

|  |
| --- |
| **accessedAt**  DATE-TIME |
| **createdAt**  DATE-TIME |
| **createdBy**  STRING |
| **currentStatus**  STRING |
| **customCSS**  STRING |
| **defaultKeyFieldMapping**  STRING |
| **depth**  STRING |
| **description**  STRING |
| **elements**  ARRAY This is a nested data structure:   - altText: STRING - createdFromContactFieldId: STRING - dataType: STRING - depth: STRING - displayType: STRING - fieldMergeId: STRING - fields: STRING - htmlName: STRING - id: STRING - instructions: STRING - name: STRING - numberOfFieldsToDisplay: STRING - onlyShowIncompleteFields: STRING - optionListId: STRING - randomizeFields: STRING - style: STRING - type: STRING - useGlobalSubscriptionStatus: STRING - validations: STRING |
| **emailAddressFormFieldId**  STRING |
| **folderId**  STRING |
| **html**  STRING |
| **htmlName**  STRING |
| **id**  STRING |
| **name**  STRING |
| **permissions**  STRING |
| **processingSteps**  ARRAY This is a nested data structure:   - allowResend: BOOLEAN - campaignElementId: STRING - campaignId: STRING - description: STRING - emailAddressFormFieldId: STRING - emailId: STRING - eventId: STRING - execute: STRING - id: STRING - keyFieldId: STRING - keyFieldMapping: STRING - landingPageId: STRING - mappings: STRING - name: STRING - resendLimit: INTEGER - type: STRING |
| **processingType**  STRING |
| **size**  STRING |
| **style**  STRING |
| **submitFailedLandingPageId**  STRING |
| **type**  STRING |
| **updatedAt**  DATE-TIME |
| **updatedBy**  STRING |

### visitors

The `visitors` table contains info about your Eloqua visitors. According to Eloqua, *“A visitor is a data entity that represents a unique cookie. The tracked activity data from that cookie is associated with the Visitor. There can be multiple visitors linked to a single contact.”*

**Note**: This table is replicated using the Eloqua Application REST API.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | V\_LastVisitDateAndTime |
| **Useful links** | [Eloqua API method](https://docs.oracle.com/cloud/latest/marketingcs_gs/OMCAC/op-api-rest-2.0-data-visitors-get.html "Opens in new tab: Eloqua API method") |

visitors table foreign keys

| Join visitors with | on |
| --- | --- |
| [contacts](#contacts) | ``` visitors.contactId = contacts.Id ``` |
| [activity\_bounceback](#activity-bounceback) | ``` visitors.contactId = activity_bounceback.ContactId ``` |
| [activity\_email\_clickthrough](#activity-email-clickthrough) | ``` visitors.contactId = activity_email_clickthrough.ContactId ```  ``` visitors.id = activity_email_clickthrough.VisitorId ``` |
| [activity\_email\_open](#activity-email-open) | ``` visitors.contactId = activity_email_open.ContactId ```  ``` visitors.id = activity_email_open.VisitorId ``` |
| [activity\_email\_send](#activity-email-send) | ``` visitors.contactId = activity_email_send.ContactId ``` |
| [activity\_form\_submit](#activity-form-submit) | ``` visitors.contactId = activity_form_submit.ContactId ```  ``` visitors.id = activity_form_submit.VisitorId ``` |
| [activity\_page\_view](#activity-page-view) | ``` visitors.contactId = activity_page_view.ContactId ```  ``` visitors.id = activity_page_view.VisitorId ``` |
| [activity\_subscribe](#activity-subscribe) | ``` visitors.contactId = activity_subscribe.ContactId ``` |
| [activity\_unsubscribe](#activity-unsubscribe) | ``` visitors.contactId = activity_unsubscribe.ContactId ``` |

visitors table schema

|  |
| --- |
| **V\_Browser\_Type**  STRING |
| **V\_CityFromIP**  STRING |
| **V\_CompanyDNSName**  STRING |
| **V\_CompanyNameFromIP1**  STRING |
| **V\_CountryFromIP**  STRING |
| **V\_CountryName**  STRING |
| **V\_Current\_Total\_Pages**  INTEGER |
| **V\_Current\_Visit\_Length**  INTEGER |
| **V\_FirstPageInVisit**  STRING |
| **V\_FirstVisitDateAndTime**  DATE-TIME |
| **V\_HostName**  STRING |
| **V\_IPAddress**  STRING |
| **V\_ISPFromIP**  STRING |
| **V\_LastPageInVisit**  STRING |
| **V\_LastVisitDateAndTime**  DATE-TIME |
| **V\_LatitudeFromIP**  NUMBER |
| **V\_LongitudeFromIP**  NUMBER |
| **V\_Name**  STRING |
| **V\_ProvinceFromIP**  STRING |
| **V\_TimeZone**  STRING |
| **V\_TimeZoneOffsetMin**  INTEGER |
| **V\_Total\_Pages**  INTEGER |
| **V\_Total\_Time**  INTEGER |
| **V\_Total\_Visits**  INTEGER |
| **V\_ZipCodeFromIP**  STRING |
| **contactId**  STRING |
| **createdAt**  STRING |
| **currentStatus**  STRING |
| **externalId**  STRING |
| **id**  STRING |
| **type**  STRING |
| **visitorId**  STRING |
