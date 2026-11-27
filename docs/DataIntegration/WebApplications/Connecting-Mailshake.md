---
title: "Mailshake"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Mailshake.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Mailshake

Mailshake is a sales engagement platform designed to streamline and automate cold outreach efforts.

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To generate the API key:

1. Log into your Mailshake account.
2. Go to Extensions > API.
3. Click Create API Key to create an API key. Your API key is displayed on the page.

   If your account already has an API key, it is displayed in the Your Access section of the page.
4. Fill in your API key in the Connection settings page.

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
| API Key | API key. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### campaigns

The `campaigns` table contains info about your team’s campaigns.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | created |
| **Useful links** | [Mailshake API method](https://api-docs.mailshake.com/?shell#List "Opens in new tab: Mailshake API method") |

campaigns table foreign keys

| Join campaigns with | on |
| --- | --- |
| [clicks](#clicks) | ``` campaigns.id = clicks.campaign.id ```  ``` campaigns.messages.id = clicks.campaign.id ```  ``` campaigns.messages.id = clicks.parent.message.id ``` |
| [leads](#leads) | ``` campaigns.id = leads.campaign.id ```  ``` campaigns.messages.id = leads.campaign.id ``` |
| [opens](#opens) | ``` campaigns.id = opens.campaign.id ```  ``` campaigns.messages.id = opens.campaign.id ```  ``` campaigns.messages.id = opens.parent.message.id ``` |
| [recipients](#recipients) | ``` campaigns.id = recipients.campaignId ```  ``` campaigns.messages.id = recipients.campaignId ``` |
| [replies](#replies) | ``` campaigns.id = replies.campaign.id ```  ``` campaigns.messages.id = replies.campaign.id ```  ``` campaigns.messages.id = replies.parent.message.id ``` |
| [sent\_messages](#sent-messages) | ``` campaigns.id = sent_messages.campaign.id ```  ``` campaigns.messages.id = sent_messages.campaign.id ```  ``` campaigns.messages.id = sent_messages.message.id ``` |
| [senders](#senders) | ``` campaigns.sender.id = senders.id ``` |

campaigns table schema

|  |
| --- |
| **actionDate**  DATE-TIME |
| **archived**  BOOLEAN |
| **created**  DATE-TIME |
| **endedAt**  DATE-TIME |
| **id**  INTEGER |
| **isPaused**  BOOLEAN |
| **messages**  ARRAY This is a nested data structure:   - campaignId: INTEGER - id: INTEGER - isPaused: BOOLEAN - object: STRING - replyToID: INTEGER - subject: STRING - type: STRING |
| **object**  STRING |
| **sender**  OBJECT This is a nested data structure:   - created: DATE-TIME - emailAddress: STRING - fromName: STRING - id: STRING - object: STRING |
| **title**  STRING |
| **url**  STRING |

### clicks

The `clicks` table contains info about recent click activity.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | actionDate |
| **Useful links** | [Mailshake API method](https://api-docs.mailshake.com/?shell#Clicks "Opens in new tab: Mailshake API method") |

clicks table foreign keys

| Join clicks with | on |
| --- | --- |
| [campaigns](#campaigns) | ``` clicks.campaign.id = campaigns.id ```  ``` clicks.campaign.id = campaigns.messages.id ```  ``` clicks.parent.message.id = campaigns.messages.id ``` |
| [leads](#leads) | ``` clicks.campaign.id = leads.campaign.id ```  ``` clicks.recipient.id = leads.recipient.id ``` |
| [opens](#opens) | ``` clicks.campaign.id = opens.campaign.id ```  ``` clicks.parent.message.id = opens.parent.message.id ```  ``` clicks.recipient.id = opens.recipient.id ``` |
| [recipients](#recipients) | ``` clicks.campaign.id = recipients.campaignId ```  ``` clicks.recipient.id = recipients.id ``` |
| [replies](#replies) | ``` clicks.campaign.id = replies.campaign.id ```  ``` clicks.parent.message.id = replies.parent.message.id ```  ``` clicks.recipient.id = replies.parent.message.id ``` |
| [sent\_messages](#sent-messages) | ``` clicks.campaign.id = sent_messages.campaign.id ```  ``` clicks.parent.message.id = sent_messages.message.id ```  ``` clicks.recipient.id = sent_messages.recipient.id ``` |

clicks table schema

|  |
| --- |
| **actionDate**  DATE-TIME |
| **campaign**  OBJECT This is a nested data structure:   - created: DATE-TIME - id: INTEGER - object: STRING - title: STRING |
| **id**  INTEGER |
| **isDuplicate**  BOOLEAN |
| **link**  STRING |
| **object**  STRING |
| **parent**  OBJECT This is a nested data structure:   - id: INTEGER - message: OBJECT, which is also a nested data structure.   - id: INTEGER   - object: STRING   - subject: STRING   - type: STRING - object: STRING - type: STRING |
| **recipient**  OBJECT This is a nested data structure:   - action: STRING - created: DATE-TIME - emailAddress: STRING - fields: OBJECT, which is also a nested data structure. - first: STRING - fullName: STRING - id: INTEGER - isPaused: BOOLEAN - last: STRING - object: STRING |

### leads

The `leads` table contains info about the leads in your Mailshake account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | created |
| **Useful links** | [Mailshake API method](https://api-docs.mailshake.com/?shell#List59 "Opens in new tab: Mailshake API method") |

leads table foreign keys

| Join leads with | on |
| --- | --- |
| [campaigns](#campaigns) | ``` leads.campaign.id = campaigns.id ```  ``` leads.campaign.id = campaigns.messages.id ``` |
| [clicks](#clicks) | ``` leads.campaign.id = clicks.campaign.id ```  ``` leads.recipient.id = clicks.recipient.id ``` |
| [opens](#opens) | ``` leads.campaign.id = opens.campaign.id ```  ``` leads.recipient.id = opens.recipient.id ``` |
| [recipients](#recipients) | ``` leads.campaign.id = recipients.campaignId ```  ``` leads.recipient.id = recipients.id ``` |
| [replies](#replies) | ``` leads.campaign.id = replies.campaign.id ```  ``` leads.recipient.id = replies.parent.message.id ``` |
| [sent\_messages](#sent-messages) | ``` leads.campaign.id = sent_messages.campaign.id ```  ``` leads.recipient.id = sent_messages.recipient.id ``` |
| [team\_members](#team-members) | ``` leads.assignedTo.id = team_members.id ``` |

leads table schema

|  |
| --- |
| **assignedTo**  OBJECT This is a nested data structure:   - emailAddress: STRING - first: STRING - fullName: STRING - id: INTEGER - last: STRING - object: STRING |
| **campaign**  OBJECT This is a nested data structure:   - created: DATE-TIME - id: INTEGER - object: STRING - title: STRING |
| **created**  DATE-TIME |
| **id**  INTEGER |
| **lastStatusChangeDate**  DATE-TIME |
| **object**  STRING |
| **openedDate**  DATE-TIME |
| **recipient**  OBJECT This is a nested data structure:   - created: DATE-TIME - emailAddress: STRING - fields: OBJECT, which is also a nested data structure. - first: STRING - fullName: STRING - id: INTEGER - last: STRING - object: STRING |
| **status**  STRING |

### opens

The `opens` table contains info about recently opened emails.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | actionDate |
| **Useful links** | [Mailshake API method](https://api-docs.mailshake.com/?shell#Opens "Opens in new tab: Mailshake API method") |

opens table foreign keys

| Join opens with | on |
| --- | --- |
| [campaigns](#campaigns) | ``` opens.campaign.id = campaigns.id ```  ``` opens.campaign.id = campaigns.messages.id ```  ``` opens.parent.message.id = campaigns.messages.id ``` |
| [clicks](#clicks) | ``` opens.campaign.id = clicks.campaign.id ```  ``` opens.parent.message.id = clicks.parent.message.id ```  ``` opens.recipient.id = clicks.recipient.id ``` |
| [leads](#leads) | ``` opens.campaign.id = leads.campaign.id ```  ``` opens.recipient.id = leads.recipient.id ``` |
| [recipients](#recipients) | ``` opens.campaign.id = recipients.campaignId ```  ``` opens.recipient.id = recipients.id ``` |
| [replies](#replies) | ``` opens.campaign.id = replies.campaign.id ```  ``` opens.parent.message.id = replies.parent.message.id ```  ``` opens.recipient.id = replies.parent.message.id ``` |
| [sent\_messages](#sent-messages) | ``` opens.campaign.id = sent_messages.campaign.id ```  ``` opens.parent.message.id = sent_messages.message.id ```  ``` opens.recipient.id = sent_messages.recipient.id ``` |

opens table schema

|  |
| --- |
| **actionDate**  DATE-TIME |
| **campaign**  OBJECT This is a nested data structure:   - created: DATE-TIME - id: INTEGER - object: STRING - title: STRING |
| **id**  INTEGER |
| **isDuplicate**  BOOLEAN |
| **object**  STRING |
| **parent**  OBJECT This is a nested data structure:   - id: INTEGER - message: OBJECT, which is also a nested data structure.   - id: INTEGER   - object: STRING   - subject: STRING   - type: STRING - object: STRING - type: STRING |
| **recipient**  OBJECT This is a nested data structure:   - action: STRING - created: DATE-TIME - emailAddress: STRING - fields: OBJECT, which is also a nested data structure. - first: STRING - fullName: STRING - id: INTEGER - isPaused: BOOLEAN - last: STRING - object: STRING |

### recipients

The `recipients` table contains info about the recipients in a campaign.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | created |
| **Useful links** | [Mailshake API method](https://api-docs.mailshake.com/?shell#List33 "Opens in new tab: Mailshake API method") |

recipients table foreign keys

| Join recipients with | on |
| --- | --- |
| [campaigns](#campaigns) | ``` recipients.campaignId = campaigns.id ```  ``` recipients.campaignId = campaigns.messages.id ``` |
| [clicks](#clicks) | ``` recipients.campaignId = clicks.campaign.id ```  ``` recipients.id = clicks.recipient.id ``` |
| [leads](#leads) | ``` recipients.campaignId = leads.campaign.id ```  ``` recipients.id = leads.recipient.id ``` |
| [opens](#opens) | ``` recipients.campaignId = opens.campaign.id ```  ``` recipients.id = opens.recipient.id ``` |
| [replies](#replies) | ``` recipients.campaignId = replies.campaign.id ```  ``` recipients.id = replies.parent.message.id ``` |
| [sent\_messages](#sent-messages) | ``` recipients.campaignId = sent_messages.campaign.id ```  ``` recipients.id = sent_messages.recipient.id ``` |

recipients table schema

|  |
| --- |
| **action**  STRING |
| **campaignId**  INTEGER |
| **created**  DATE-TIME |
| **emailAddress**  STRING |
| **fields**  OBJECT This is a nested data structure. |
| **first**  STRING |
| **fullName**  STRING |
| **id**  INTEGER |
| **last**  STRING |
| **object**  STRING |

### replies

The `replies` table contains info about recent replies to your emails.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | actionDate |
| **Useful links** | [Mailshake API method](https://api-docs.mailshake.com/?shell#Replies "Opens in new tab: Mailshake API method") |

replies table foreign keys

| Join replies with | on |
| --- | --- |
| [campaigns](#campaigns) | ``` replies.campaign.id = campaigns.id ```  ``` replies.campaign.id = campaigns.messages.id ```  ``` replies.parent.message.id = campaigns.messages.id ``` |
| [clicks](#clicks) | ``` replies.campaign.id = clicks.campaign.id ```  ``` replies.parent.message.id = clicks.parent.message.id ```  ``` replies.parent.message.id = clicks.recipient.id ``` |
| [leads](#leads) | ``` replies.campaign.id = leads.campaign.id ```  ``` replies.parent.message.id = leads.recipient.id ``` |
| [opens](#opens) | ``` replies.campaign.id = opens.campaign.id ```  ``` replies.parent.message.id = opens.parent.message.id ```  ``` replies.parent.message.id = opens.recipient.id ``` |
| [recipients](#recipients) | ``` replies.campaign.id = recipients.campaignId ```  ``` replies.parent.message.id = recipients.id ``` |
| [sent\_messages](#sent-messages) | ``` replies.campaign.id = sent_messages.campaign.id ```  ``` replies.parent.message.id = sent_messages.message.id ```  ``` replies.parent.message.id = sent_messages.recipient.id ``` |

replies table schema

|  |
| --- |
| **actionDate**  DATE-TIME |
| **body**  STRING |
| **campaign**  OBJECT This is a nested data structure:   - created: DATE-TIME - id: INTEGER - object: STRING - title: STRING |
| **externalConversationID**  STRING |
| **externalID**  STRING |
| **externalRawMessageID**  STRING |
| **id**  INTEGER |
| **object**  STRING |
| **parent**  OBJECT This is a nested data structure:   - id: INTEGER - message: OBJECT, which is also a nested data structure.   - id: INTEGER   - object: STRING   - subject: STRING   - type: STRING - object: STRING - type: STRING |
| **plainTextBody**  STRING |
| **rawBody**  STRING |
| **recipient**  OBJECT This is a nested data structure:   - action: STRING - created: DATE-TIME - emailAddress: STRING - fields: OBJECT, which is also a nested data structure. - first: STRING - fullName: STRING - id: INTEGER - isPaused: BOOLEAN - last: STRING - object: STRING |
| **subject**  STRING |
| **type**  STRING |

### senders

The `senders` table contains info about your team’s senders.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | created |
| **Useful links** | [Mailshake API method](https://api-docs.mailshake.com/?shell#List75 "Opens in new tab: Mailshake API method") |

senders table foreign keys

| Join senders with | on |
| --- | --- |
| [campaigns](#campaigns) | ``` senders.id = campaigns.sender.id ``` |

senders table schema

|  |
| --- |
| **created**  DATE-TIME |
| **emailAddress**  STRING |
| **fromName**  STRING |
| **id**  STRING |
| **object**  STRING |
| **offerType**  STRING |

### sent\_messages

The `sent_messages` table contains info about recently sent emails.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | actionDate |
| **Useful links** | [Mailshake API method](https://api-docs.mailshake.com/?shell#Sent "Opens in new tab: Mailshake API method") |

sent\_messages table foreign keys

| Join sent\_messages with | on |
| --- | --- |
| [campaigns](#campaigns) | ``` sent_messages.campaign.id = campaigns.id ```  ``` sent_messages.campaign.id = campaigns.messages.id ```  ``` sent_messages.message.id = campaigns.messages.id ``` |
| [clicks](#clicks) | ``` sent_messages.campaign.id = clicks.campaign.id ```  ``` sent_messages.message.id = clicks.parent.message.id ```  ``` sent_messages.recipient.id = clicks.recipient.id ``` |
| [leads](#leads) | ``` sent_messages.campaign.id = leads.campaign.id ```  ``` sent_messages.recipient.id = leads.recipient.id ``` |
| [opens](#opens) | ``` sent_messages.campaign.id = opens.campaign.id ```  ``` sent_messages.message.id = opens.parent.message.id ```  ``` sent_messages.recipient.id = opens.recipient.id ``` |
| [recipients](#recipients) | ``` sent_messages.campaign.id = recipients.campaignId ```  ``` sent_messages.recipient.id = recipients.id ``` |
| [replies](#replies) | ``` sent_messages.campaign.id = replies.campaign.id ```  ``` sent_messages.message.id = replies.parent.message.id ```  ``` sent_messages.recipient.id = replies.parent.message.id ``` |

sent\_messages table schema

|  |
| --- |
| **actionDate**  DATE-TIME |
| **body**  STRING |
| **campaign**  OBJECT This is a nested data structure:   - created: DATE-TIME - id: INTEGER - object: STRING - title: STRING |
| **externalConversationID**  STRING |
| **externalID**  STRING |
| **externalRawMessageID**  STRING |
| **from**  OBJECT This is a nested data structure:   - address: STRING - first: STRING - fullName: STRING - last: STRING - object: STRING |
| **id**  INTEGER |
| **message**  OBJECT This is a nested data structure:   - id: INTEGER - object: STRING - subject: STRING - type: STRING |
| **object**  STRING |
| **plainTextBody**  STRING |
| **rawBody**  STRING |
| **recipient**  OBJECT This is a nested data structure:   - action: STRING - created: DATE-TIME - emailAddress: STRING - fields: OBJECT, which is also a nested data structure. - first: STRING - fullName: STRING - id: INTEGER - isPaused: BOOLEAN - last: STRING - object: STRING |
| **subject**  STRING |
| **to**  ARRAY This is a nested data structure:   - address: STRING - first: STRING - fullName: STRING - last: STRING - object: STRING |
| **type**  STRING |

### team\_members

The `team_members` table contains info about the individual members of your team.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | teamID |
| **Useful links** | [Mailshake API method](https://api-docs.mailshake.com/?shell#List-Members "Opens in new tab: Mailshake API method") |

team\_members table foreign keys

| Join team\_members with | on |
| --- | --- |
| [leads](#leads) | ``` team_members.id = leads.assignedTo.id ``` |

team\_members table schema

|  |
| --- |
| **emailAddress**  STRING |
| **first**  STRING |
| **fullName**  STRING |
| **id**  INTEGER |
| **isDisabled**  BOOLEAN |
| **isTeamAdmin**  BOOLEAN |
| **last**  STRING |
| **object**  STRING |
| **teamBlockedDate**  DATE-TIME |
| **teamID**  INTEGER |
| **teamName**  BOOLEAN |
