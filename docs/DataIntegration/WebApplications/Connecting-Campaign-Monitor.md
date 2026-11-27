---
title: "Campaign Monitor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Campaign-Monitor.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Campaign Monitor

Campaign Monitor is an email marketing service.

Campaign Monitor integration replicates data using the [Campaign Monitor API](https://www.campaignmonitor.com/api/).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

You need administrator permissions in your Campaign Monitor account.

To retrieve your API client ID:

1. Log into your [Campaign Monitor](https://login.createsend.com/l) account.
2. Click your profile image in the upper-right corner.
3. Navigate to Account settings > API keys.
4. Copy and paste your API client ID into a secured file.

To retrieve your client ID and client secret:

1. Log into your [Campaign Monitor](https://login.createsend.com/l) account.
2. Navigate to Integrations > OAuth Registration.
3. Enter the application information.
4. Register your application.
5. Copy and paste your client ID and client secret into a secured file.

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
| Application Client ID | Application client ID. |
| Application Client Secret | Application client secret. |
| API Client ID | API client ID. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### campaign\_bounces

The `campaign_bounces` table contains info about the subscribers who bounced for a given campaign.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | CampaignID  EmailAddress  Date  ListID |
| **Replication Key** | Date |
| **Useful links** | [Campaign Monitor API method](https://www.campaignmonitor.com/api/campaigns/#campaign-bounces "Opens in new tab: Campaign Monitor API method") |

campaign\_bounces table schema

|  |
| --- |
| **BounceType**  STRING |
| **CampaignID**  STRING |
| **Date**  DATE-TIME |
| **EmailAddress**  STRING |
| **ListID**  STRING |
| **Reason**  STRING |

### campaign\_clicks

The `campaign_clicks` table contains info about subscribers who clicked a link in a given campaign.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | CampaignID  EmailAddress  ListID  Date |
| **Replication Key** | Date |
| **Useful links** | [Campaign Monitor API method](https://www.campaignmonitor.com/api/campaigns/#campaign-clicks "Opens in new tab: Campaign Monitor API method") |

campaign\_clicks table schema

|  |
| --- |
| **CampaignID**  STRING |
| **City**  STRING |
| **CountryCode**  STRING |
| **CountryName**  STRING |
| **Date**  DATE-TIME |
| **EmailAddress**  STRING |
| **IPAddress**  STRING |
| **Latitude**  NUMBER |
| **ListID**  STRING |
| **Longitude**  NUMBER |
| **Region**  STRING |
| **URL**  STRING |

### campaign\_email\_client\_usage

The `campaign_email_client_usage` table contains info about the email clients subscribers use to open campaigns.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | CampaignID  Client  Version |
| **Useful links** | [Campaign Monitor API method](https://www.campaignmonitor.com/api/campaigns/#campaign-email-client-usage "Opens in new tab: Campaign Monitor API method") |

campaign\_email\_client\_usage table schema

|  |
| --- |
| **CampaignID**  STRING |
| **Client**  STRING |
| **Percentage**  NUMBER |
| **Subscribers**  INTEGER |
| **Version**  STRING |

### campaign\_opens

The `campaign_opens` table contains info about subscribers who opened a campaign.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | CampaignID  EmailAddress  ListID  Date |
| **Replication Key** | Date |
| **Useful links** | [Campaign Monitor API method](https://www.campaignmonitor.com/api/campaigns/#campaign-opens "Opens in new tab: Campaign Monitor API method") |

campaign\_opens table schema

|  |
| --- |
| **CampaignID**  STRING |
| **City**  STRING |
| **CountryCode**  STRING |
| **CountryName**  STRING |
| **Date**  DATE-TIME |
| **EmailAddress**  STRING |
| **IPAddress**  STRING |
| **Latitude**  NUMBER |
| **ListID**  STRING |
| **Longitude**  NUMBER |
| **Region**  STRING |

### campaign\_recipients

The `campaign_recipients` table contains info about the subscribers that a campaign was sent to.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | CampaignID  EmailAddress  ListID |
| **Useful links** | [Campaign Monitor API method](https://www.campaignmonitor.com/api/campaigns/#campaign-recipients "Opens in new tab: Campaign Monitor API method") |

campaign\_recipients table schema

|  |
| --- |
| **CampaignID**  STRING |
| **EmailAddress**  STRING |
| **ListID**  STRING |

### campaign\_spam\_complaints

The `campaign_spam_complaints` table contains info about subscribers who marked a campaign as spam.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | CampaignID  EmailAddress  ListID  Date |
| **Replication Key** | Date |
| **Useful links** | [Campaign Monitor API method](https://www.campaignmonitor.com/api/campaigns/#campaign-spam-complaints "Opens in new tab: Campaign Monitor API method") |

campaign\_spam\_complaints table schema

|  |
| --- |
| **CampaignID**  STRING |
| **Date**  DATE-TIME |
| **EmailAddress**  STRING |
| **ListID**  STRING |

### campaign\_summary

The `campaign_summary` table contains summary info about sent campaigns.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | CampaignID |
| **Useful links** | [Campaign Monitor API method](https://www.campaignmonitor.com/api/campaigns/#campaign-summary "Opens in new tab: Campaign Monitor API method") |

campaign\_summary table schema

|  |
| --- |
| **Bounced**  INTEGER |
| **CampaignID**  STRING |
| **Clicks**  INTEGER |
| **Forwards**  INTEGER |
| **Likes**  INTEGER |
| **Mentions**  INTEGER |
| **Recipients**  INTEGER |
| **SpamComplaints**  INTEGER |
| **TotalOpened**  INTEGER |
| **UniqueOpened**  INTEGER |
| **Unsubscribed**  INTEGER |
| **WebVersionTextURL**  STRING |
| **WebVersionURL**  STRING |
| **WorldviewURL**  STRING |

### campaign\_unsubscribes

The `campaign_unsubscribes` table contains info about the subscribers who unsubscribed from the email for a campaign.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | CampaignID  EmailAddress  ListID  Date |
| **Replication Key** | Date |
| **Useful links** | [Campaign Monitor API method](https://www.campaignmonitor.com/api/campaigns/#campaign-unsubscribes "Opens in new tab: Campaign Monitor API method") |

campaign\_unsubscribes table schema

|  |
| --- |
| **CampaignID**  STRING |
| **Date**  DATE-TIME |
| **EmailAddress**  STRING |
| **IPAddress**  STRING |
| **ListID**  STRING |

### campaigns

The `campaigns` table contains info about the the campaigns in your Campaign Monitor account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | CampaignID |
| **Useful links** | [Campaign Monitor documentation](https://www.campaignmonitor.com/api/campaigns/) |

campaigns table schema

|  |
| --- |
| **CampaignID**  STRING |
| **FromEmail**  STRING |
| **FromName**  STRING |
| **Name**  STRING |
| **ReplyTo**  STRING |
| **SentDate**  DATE-TIME |
| **Subject**  STRING |
| **TotalRecipients**  NUMBER |
| **WebVersionTextURL**  STRING |
| **WebVersionURL**  STRING |

### list\_active\_subscribers

The `list_active_subscribers` table contains info about the active subscribers for lists.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | ListID  EmailAddress  Date |
| **Replication Key** | Date |
| **Useful links** | [Campaign Monitor API method](https://www.campaignmonitor.com/api/lists/#active-subscribers "Opens in new tab: Campaign Monitor API method") |

list\_active\_subscribers table schema

|  |
| --- |
| **ConsentToTrack**  STRING |
| **CustomFields**  ARRAY This is a nested data structure:   - Key: STRING - Value: STRING |
| **Date**  DATE-TIME |
| **EmailAddress**  STRING |
| **ListID**  STRING |
| **Name**  STRING |
| **ReadsEmailWith**  STRING |
| **State**  STRING |

### list\_bounced\_subscribers

The `list_bounced_subscribers` table contains info about the bounced subscribers for lists.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | ListID  EmailAddress  Date |
| **Replication Key** | Date |
| **Useful links** | [Campaign Monitor API method](https://www.campaignmonitor.com/api/lists/#bounced-subscribers "Opens in new tab: Campaign Monitor API method") |

list\_bounced\_subscribers table schema

|  |
| --- |
| **ConsentToTrack**  STRING |
| **CustomFields**  ARRAY This is a nested data structure:   - Key: STRING - Value: STRING |
| **Date**  DATE-TIME |
| **EmailAddress**  STRING |
| **ListID**  STRING |
| **Name**  STRING |
| **ReadsEmailWith**  STRING |
| **State**  STRING |

### list\_deleted\_subscribers

The `list_deleted_subscribers` table contains info about the deleted subscribers for lists.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | ListID  EmailAddress  Date |
| **Replication Key** | Date |
| **Useful links** | [Campaign Monitor API method](https://www.campaignmonitor.com/api/lists/#deleted-subscribers "Opens in new tab: Campaign Monitor API method") |

list\_deleted\_subscribers table schema

|  |
| --- |
| **ConsentToTrack**  STRING |
| **CustomFields**  ARRAY This is a nested data structure:   - Key: STRING - Value: STRING |
| **Date**  DATE-TIME |
| **EmailAddress**  STRING |
| **ListID**  STRING |
| **Name**  STRING |
| **ReadsEmailWith**  STRING |
| **State**  STRING |

### list\_details

The `list_details` table contains summary info about lists in your Campaign Monitor account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | ListID |
| **Useful links** | [Campaign Monitor API method](https://www.campaignmonitor.com/api/lists/#list-details "Opens in new tab: Campaign Monitor API method") |

list\_details table schema

|  |
| --- |
| **ConfirmationSuccessPage**  STRING |
| **ConfirmedOptIn**  BOOLEAN |
| **ListID**  STRING |
| **Title**  STRING |
| **UnsubscribePage**  STRING |
| **UnsubscribeSetting**  STRING |

### list\_unconfirmed\_subscribers

The `list_unconfirmed_subscribers` table contains info about the unconfirmed subscribers for lists.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | ListID  EmailAddress  Date |
| **Replication Key** | Date |
| **Useful links** | [Campaign Monitor API method](https://www.campaignmonitor.com/api/lists/#unconfirmed-subscribers "Opens in new tab: Campaign Monitor API method") |

list\_unconfirmed\_subscribers table schema

|  |
| --- |
| **ConsentToTrack**  STRING |
| **CustomFields**  ARRAY This is a nested data structure:   - Key: STRING - Value: STRING |
| **Date**  DATE-TIME |
| **EmailAddress**  STRING |
| **ListID**  STRING |
| **Name**  STRING |
| **ReadsEmailWith**  STRING |
| **State**  STRING |

### list\_unsubscribed\_subscribers

The `list_unsubscribed_subscribers` table contains info about the unsubscribed subscribers for lists.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | ListID  EmailAddress  Date |
| **Replication Key** | Date |
| **Useful links** | [Campaign Monitor API method](https://www.campaignmonitor.com/api/lists/#unsubscribed-subscribers "Opens in new tab: Campaign Monitor API method") |

list\_unsubscribed\_subscribers table schema

|  |
| --- |
| **ConsentToTrack**  STRING |
| **CustomFields**  ARRAY This is a nested data structure:   - Key: STRING - Value: STRING |
| **Date**  DATE-TIME |
| **EmailAddress**  STRING |
| **ListID**  STRING |
| **Name**  STRING |
| **ReadsEmailWith**  STRING |
| **State**  STRING |

### lists

The `lists` table contains info about the lists in your Campaign Monitor account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | ListID |
| **Useful links** | [Campaign Monitor documentation](https://www.campaignmonitor.com/api/lists/) |

lists table schema

|  |
| --- |
| **ListID**  STRING |
| **Name**  STRING |
