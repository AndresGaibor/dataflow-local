---
title: "Salesforce Marketing Cloud"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Salesforce-Marketing-Cloud.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Salesforce Marketing Cloud

Salesforce Marketing Cloud is a digital marketing platform that automates email marketing, social media, apps, websites, and more.

Salesforce Marketing Cloud integration replicates data using the [Salesforce Marketing Cloud both REST API and SOAP API](https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/apis-overview.html).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

Before you create connections in Qlik Talend Cloud, make sure you have the following:

- A Salesforce Professional, Corporate, or Enterprise license (required to use the Salesforce Marketing Cloud API).
- A Salesforce Marketing Cloud Administrator user, or a System Administrator user in Salesforce.
- An External Client App created in Salesforce. To integrate with Salesforce, external applications must use an External Client App (not a package).

The following instructions are available only in the Salesforce Lightning Experience menu. If you are using Salesforce Classic, switch to Salesforce Lightning Experience.

To retrieve your client ID and client secret:

1. Switch to Salesforce Lightning Experience if you are using Salesforce Classic.
2. Log into your [Salesforce Marketing Cloud](https://mc.login.exacttarget.com/hub-cas/login?&service=https%3a%2f%2fauth.exacttargetapis.com%2fv2%2fauthorize%3fclient_id%3dhbw6vmsadg5epio6bd1eg4uc%26redirect_uri%3dhttps%253A%252F%252Fmc.exacttarget.com%252Fcloud%252Fauth_redirect%26response_type%3dcode%26state%3deyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdXRob3JpemVTdGFydFRpbWUiOjE3NzMyNDUxMjMwMjYsImtleSI6IkZva2RQWFE3ZzFXYVBia3pEZEs4bCIsInJlZGlyZWN0SGFuZGxlciI6Imh0dHBzOi8vbWMuZXhhY3R0YXJnZXQuY29tL2Nsb3VkL2F1dGhfcmVkaXJlY3QiLCJyZWRpcmVjdFVyaSI6Imh0dHBzOi8vbWMuZXhhY3R0YXJnZXQuY29tL2Nsb3VkLz9oYXNoPWxvZ2dlZC1pbkl3PT0ifQ.M8_PaOcLuB62gYJq3AqmpgshPzPdtMwZqeDBn99Pk9o) account.
3. In Setup, navigate to Apps > App Manager, and then click New External Client App.
4. Configure the app:
   - Enter a name.
   - Set Distribution State to Local.
   - Under API (Enable OAuth Settings), select Enable OAuth and set OAuth Scopes to Full access.
   - Under Flow Enablement, select Enable Client Credentials Flow.
5. Click Create.
6. Once the external app is created, navigate to Settings > OAuth Settings > Consumer Key and Secret.
7. When prompted, verify your identity using one of your registered methods.
8. Copy and paste your client ID and client secret into a secured file.
9. Navigate to Policies > Edit > OAuth Policies, and then enable Enable Client Credentials Flow.
10. In Run As (Username), enter your email, and then click Save.

To enable REST API access:

1. Log into your [Salesforce Marketing Cloud](https://mc.login.exacttarget.com/hub-cas/login?&service=https%3a%2f%2fauth.exacttargetapis.com%2fv2%2fauthorize%3fclient_id%3dhbw6vmsadg5epio6bd1eg4uc%26redirect_uri%3dhttps%253A%252F%252Fmc.exacttarget.com%252Fcloud%252Fauth_redirect%26response_type%3dcode%26state%3deyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdXRob3JpemVTdGFydFRpbWUiOjE3NzMyNDUxMjMwMjYsImtleSI6IkZva2RQWFE3ZzFXYVBia3pEZEs4bCIsInJlZGlyZWN0SGFuZGxlciI6Imh0dHBzOi8vbWMuZXhhY3R0YXJnZXQuY29tL2Nsb3VkL2F1dGhfcmVkaXJlY3QiLCJyZWRpcmVjdFVyaSI6Imh0dHBzOi8vbWMuZXhhY3R0YXJnZXQuY29tL2Nsb3VkLz9oYXNoPWxvZ2dlZC1pbkl3PT0ifQ.M8_PaOcLuB62gYJq3AqmpgshPzPdtMwZqeDBn99Pk9o) account.
2. In Setup, navigate to Apps > External Client Apps > Settings.
3. Enable Allow access to External Client App consumer secrets via REST API.

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
| Client ID | Client ID. |
| Client Secret | Client secret. |
| Tenant Subdomain | The tenant subdomain for your Salesforce Marketing Cloud account. Example: https://subdomain.auth.marketingcloudapis.com, enter subdomain. |

## Schema

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### campaigns

The `campaigns` table contains information about the campaigns in your Salesforce Marketing Cloud account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Replication Key** | modifiedDate |
| **Useful links** | [Salesforce Marketing Cloud API method](https://developer.salesforce.com/Content/atlas.en-us.noversion.mc-apis.meta/mc-apis/campaign.htm "Opens in new tab: Salesforce Marketing Cloud API method") |

campaigns table schema

|  |
| --- |
| **campaignCode**  STRING |
| **color**  STRING |
| **createdDate**  STRING |
| **description**  STRING |
| **id**  STRING |
| **modifiedDate**  STRING |
| **name**  STRING |

### content\_areas

The `content_areas` table contains information about the reusable content sections in your Salesforce Marketing Cloud account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | ID |
| **Replication Key** | ModifiedDate |
| **Useful links** | [Salesforce Marketing Cloud API method](https://developer.salesforce.com/Content/atlas.en-us.noversion.mc-apis.meta/mc-apis/contentarea.htm "Opens in new tab: Salesforce Marketing Cloud API method") |

content\_areas table foreign keys

| Join content\_areas with | on |
| --- | --- |
| [emails](#emails) | ``` content_areas.ID = emails.ContentAreaIDs ```  ``` content_areas.CategoryID = emails.CategoryID ``` |
| [folders](#folders) | ``` content_areas.CategoryID = folders.ID ```  ``` content_areas.CategoryID = folders.ParentFolder ``` |
| [lists](#lists) | ``` content_areas.CategoryID = lists.Category ``` |

content\_areas table schema

|  |
| --- |
| **BackgroundColor**  STRING |
| **BorderColor**  STRING |
| **BorderWidth**  INTEGER |
| **CategoryID**  INTEGER |
| **Cellpadding**  INTEGER |
| **Cellspacing**  INTEGER |
| **Content**  STRING |
| **CreatedDate**  STRING |
| **CustomerKey**  STRING |
| **FontFamily**  STRING |
| **HasFontSize**  BOOLEAN |
| **ID**  INTEGER |
| **IsBlank**  BOOLEAN |
| **IsDynamicContent**  BOOLEAN |
| **IsLocked**  BOOLEAN |
| **IsSurvey**  BOOLEAN |
| **Key**  STRING |
| **ModifiedDate**  STRING |
| **Name**  STRING |
| **ObjectID**  STRING |
| **PartnerProperties**  ARRAY This is a nested data structure:   - Name: STRING - Value: STRING |
| **Width**  INTEGER |

### data\_extension

The `data_extension` table contains information about the data extensions in your Salesforce Marketing Cloud account. A table will be created for each [data extension](https://help.salesforce.com/articleView?id=mc_cab_data_extensions.htm&type=5) in your Salesforce Marketing Cloud account.

For example: If there are two data extensions named `MobileAddress` and `MobileSubscription`, two tables would be created: `data_extension._MobileAddress` and `data_extension._MobileSubscription`

**Note**: Retrieving data extension data requires [**Read, Write** permissions for Data Extensions](#add-api-component-to-package).

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | \_CustomObjectKey |
| **Useful links** | [Salesforce Marketing Cloud API method](https://developer.salesforce.com/Content/atlas.en-us.noversion.mc-apis.meta/mc-apis/dataextensionobject.htm "Opens in new tab: Salesforce Marketing Cloud API method") |

data\_extension table schema

|  |
| --- |
| **CategoryID**  INTEGER |
| **\_CustomObjectKey**  STRING |

### emails

The `emails` table contains information about the emails in your Salesforce Marketing Cloud account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | ID |
| **Replication Key** | ModifiedDate |
| **Useful links** | [Salesforce Marketing Cloud API method](https://developer.salesforce.com/Content/atlas.en-us.noversion.mc-apis.meta/mc-apis/email.htm "Opens in new tab: Salesforce Marketing Cloud API method") |

emails table foreign keys

| Join emails with | on |
| --- | --- |
| [content\_areas](#content-areas) | ``` emails.ContentAreaIDs = content_areas.ID ```  ``` emails.CategoryID = content_areas.CategoryID ``` |
| [sends](#sends) | ``` emails.ID = sends.EmailID ```  ``` emails.ClonedFromID = sends.EmailID ``` |
| [folders](#folders) | ``` emails.CategoryID = folders.ID ```  ``` emails.CategoryID = folders.ParentFolder ``` |
| [lists](#lists) | ``` emails.CategoryID = lists.Category ``` |

emails table schema

|  |
| --- |
| **CategoryID**  INTEGER |
| **CharacterSet**  STRING |
| **ClonedFromID**  INTEGER |
| **ContentAreaIDs**  ARRAY This is a nested data structure. |
| **ContentCheckStatus**  STRING |
| **CreatedDate**  STRING |
| **CustomerKey**  STRING |
| **EmailType**  STRING |
| **HTMLBody**  STRING |
| **HasDynamicSubjectLine**  BOOLEAN |
| **ID**  INTEGER |
| **IsActive**  BOOLEAN |
| **IsHTMLPaste**  BOOLEAN |
| **ModifiedDate**  STRING |
| **Name**  STRING |
| **ObjectID**  STRING |
| **PartnerProperties**  ARRAY This is a nested data structure:   - Name: STRING - Value: STRING |
| **PreHeader**  STRING |
| **Status**  STRING |
| **Subject**  STRING |
| **SyncTextWithHTML**  BOOLEAN |
| **TextBody**  STRING |
| **\_\_AdditionalEmailAttribute1**  STRING |
| **\_\_AdditionalEmailAttribute2**  STRING |
| **\_\_AdditionalEmailAttribute3**  STRING |
| **\_\_AdditionalEmailAttribute4**  STRING |
| **\_\_AdditionalEmailAttribute5**  STRING |

### events

The `events` table contains information about the events in your Salesforce Marketing Cloud account.

When events are replicated to the destination, they are split into the following tables: `BounceEvent`, `ClickEvent`, `OpenEvent`, `SentEvent`, and `UnsubEvent`.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | EventType  EventDate  SendID  SubscriberKey |
| **Replication Key** | EventDate |
| **Useful links** |  |

events table foreign keys

| Join events with | on |
| --- | --- |
| [list\_sends](#list-sends) | ``` events.SendID = list_sends.SendID ``` |
| [sends](#sends) | ``` events.SendID = sends.ID ``` |
| [list\_subscribers](#list-subscribers) | ``` events.SubscriberKey = list_subscribers.SubscriberKey ``` |
| [subscribers](#subscribers) | ``` events.SubscriberKey = subscribers.ID ``` |

events table schema

|  |
| --- |
| **BatchID**  INTEGER |
| **CorrelationID**  STRING |
| **EventDate**  DATE-TIME |
| **EventType**  STRING |
| **SendID**  INTEGER |
| **SubscriberKey**  STRING |
| **URL**  STRING |

### folders

The `folders` table contains information about the folders in your Salesforce Marketing Cloud account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | ID |
| **Replication Key** | ModifiedDate |
| **Useful links** | [Salesforce Marketing Cloud API method](https://developer.salesforce.com/Content/atlas.en-us.noversion.mc-apis.meta/mc-apis/datafolder.htm "Opens in new tab: Salesforce Marketing Cloud API method") |

folders table foreign keys

| Join folders with | on |
| --- | --- |
| [content\_areas](#content-areas) | ``` folders.ID = content_areas.CategoryID ```  ``` folders.ParentFolder = content_areas.CategoryID ``` |
| [emails](#emails) | ``` folders.ID = emails.CategoryID ```  ``` folders.ParentFolder = emails.CategoryID ``` |
| [lists](#lists) | ``` folders.ID = lists.Category ```  ``` folders.ParentFolder = lists.Category ``` |

folders table schema

|  |
| --- |
| **AllowChildren**  BOOLEAN |
| **ContentType**  STRING |
| **CreatedDate**  STRING |
| **CustomerKey**  STRING |
| **Description**  STRING |
| **ID**  INTEGER |
| **ModifiedDate**  STRING |
| **Name**  STRING |
| **ObjectID**  STRING |
| **ParentFolder**  INTEGER |
| **PartnerProperties**  ARRAY This is a nested data structure:   - Name: STRING - Value: STRING |
| **Type**  STRING |

### list\_sends

The `list_sends` table contains information about the completed sends for lists in your Salesforce Marketing Cloud account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | ListID  SendID |
| **Replication Key** | ModifiedDate |
| **Useful links** | [Salesforce Marketing Cloud API method](https://developer.salesforce.com/Content/atlas.en-us.noversion.mc-apis.meta/mc-apis/listsend.htm "Opens in new tab: Salesforce Marketing Cloud API method") |

list\_sends table foreign keys

| Join list\_sends with | on |
| --- | --- |
| [lists](#lists) | ``` list_sends.ListID = lists.ID ``` |
| [list\_subscribers](#list-subscribers) | ``` list_sends.ListID = list_subscribers.ListID ``` |
| [subscribers](#subscribers) | ``` list_sends.ListID = subscribers.ListIDs ``` |
| [events](#events) | ``` list_sends.SendID = events.SendID ``` |
| [sends](#sends) | ``` list_sends.SendID = sends.ID ``` |

list\_sends table schema

|  |
| --- |
| **CreatedDate**  STRING |
| **CustomerKey**  STRING |
| **ExistingUndeliverables**  INTEGER |
| **ExistingUnsubscribes**  INTEGER |
| **ForwardedEmails**  INTEGER |
| **HardBounces**  INTEGER |
| **ID**  INTEGER |
| **InvalidAddresses**  INTEGER |
| **ListID**  INTEGER |
| **MissingAddresses**  INTEGER |
| **ModifiedDate**  STRING |
| **NumberDelivered**  INTEGER |
| **NumberSent**  INTEGER |
| **ObjectID**  STRING |
| **OtherBounces**  INTEGER |
| **PartnerProperties**  ARRAY This is a nested data structure:   - Name: STRING - Value: STRING |
| **SendID**  INTEGER |
| **SoftBounces**  INTEGER |
| **UniqueClicks**  INTEGER |
| **UniqueOpens**  INTEGER |
| **Unsubscribes**  INTEGER |

### list\_subscribers

The `list_subscribers` table contains information about the lists associated with a specific subscriber in your Salesforce Marketing Cloud account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | ListID  SubscriberKey |
| **Replication Key** | ModifiedDate |
| **Useful links** | [Salesforce Marketing Cloud API method](https://developer.salesforce.com/Content/atlas.en-us.noversion.mc-apis.meta/mc-apis/listsubscriber.htm "Opens in new tab: Salesforce Marketing Cloud API method") |

list\_subscribers table foreign keys

| Join list\_subscribers with | on |
| --- | --- |
| [lists](#lists) | ``` list_subscribers.ListID = lists.ID ``` |
| [list\_sends](#list-sends) | ``` list_subscribers.ListID = list_sends.ListID ``` |
| [subscribers](#subscribers) | ``` list_subscribers.ListID = subscribers.ListIDs ```  ``` list_subscribers.SubscriberKey = subscribers.ID ``` |
| [events](#events) | ``` list_subscribers.SubscriberKey = events.SubscriberKey ``` |

list\_subscribers table schema

|  |
| --- |
| **CreatedDate**  STRING |
| **ID**  INTEGER |
| **ListID**  INTEGER |
| **ModifiedDate**  STRING |
| **ObjectID**  STRING |
| **PartnerProperties**  ARRAY This is a nested data structure:   - Name: STRING - Value: STRING |
| **Status**  STRING |
| **SubscriberKey**  STRING |

### lists

The `lists` table contains information about the lists in your Salesforce Marketing Cloud account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | ID |
| **Replication Key** | ModifiedDate |
| **Useful links** | [Salesforce Marketing Cloud documentation](https://developer.salesforce.com/Content/atlas.en-us.noversion.mc-apis.meta/mc-apis/list.htm)  [Salesforce Marketing Cloud API method](https://developer.salesforce.com/Content/atlas.en-us.noversion.mc-apis.meta/mc-apis/retrieve.htm "Opens in new tab: Salesforce Marketing Cloud API method") |

lists table foreign keys

| Join lists with | on |
| --- | --- |
| [content\_areas](#content-areas) | ``` lists.Category = content_areas.CategoryID ``` |
| [emails](#emails) | ``` lists.Category = emails.CategoryID ``` |
| [folders](#folders) | ``` lists.Category = folders.ID ```  ``` lists.Category = folders.ParentFolder ``` |
| [list\_sends](#list-sends) | ``` lists.ID = list_sends.ListID ``` |
| [list\_subscribers](#list-subscribers) | ``` lists.ID = list_subscribers.ListID ``` |
| [subscribers](#subscribers) | ``` lists.ID = subscribers.ListIDs ``` |

lists table schema

|  |
| --- |
| **Category**  INTEGER |
| **CreatedDate**  STRING |
| **Description**  STRING |
| **ID**  INTEGER |
| **ListClassification**  STRING |
| **ListName**  STRING |
| **ModifiedDate**  STRING |
| **ObjectID**  STRING |
| **PartnerProperties**  ARRAY This is a nested data structure:   - Name: STRING - Value: STRING |
| **SendClassification**  STRING |
| **Type**  STRING |

### sends

The `sends` table contains information about the email sends in your Salesforce Marketing Cloud account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | ID |
| **Replication Key** | ModifiedDate |
| **Useful links** | [Salesforce Marketing Cloud API method](https://developer.salesforce.com/Content/atlas.en-us.noversion.mc-apis.meta/mc-apis/send.htm "Opens in new tab: Salesforce Marketing Cloud API method") |

sends table foreign keys

| Join sends with | on |
| --- | --- |
| [emails](#emails) | ``` sends.EmailID = emails.ID ```  ``` sends.EmailID = emails.ClonedFromID ``` |
| [events](#events) | ``` sends.ID = events.SendID ``` |
| [list\_sends](#list-sends) | ``` sends.ID = list_sends.SendID ``` |

sends table schema

|  |
| --- |
| **CreatedDate**  STRING |
| **EmailID**  INTEGER |
| **EmailName**  STRING |
| **FromAddress**  STRING |
| **FromName**  STRING |
| **ID**  INTEGER |
| **IsAlwaysOn**  BOOLEAN |
| **IsMultipart**  BOOLEAN |
| **ModifiedDate**  STRING |
| **PartnerProperties**  ARRAY This is a nested data structure:   - Name: STRING - Value: STRING |
| **SendDate**  DATE-TIME |
| **SentDate**  DATE-TIME |
| **Status**  STRING |
| **Subject**  STRING |

### subscribers

The `subscribers` table contains information about the subscribers (people subscribed to receive email and/or SMS communication) in your Salesforce Marketing Cloud account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | ID |
| **Replication Key** | ModifiedDate |
| **Useful links** | [Salesforce Marketing Cloud API method](https://developer.salesforce.com/Content/atlas.en-us.noversion.mc-apis.meta/mc-apis/subscriber.htm "Opens in new tab: Salesforce Marketing Cloud API method") |

subscribers table foreign keys

| Join subscribers with | on |
| --- | --- |
| [lists](#lists) | ``` subscribers.ListIDs = lists.ID ``` |
| [list\_sends](#list-sends) | ``` subscribers.ListIDs = list_sends.ListID ``` |
| [list\_subscribers](#list-subscribers) | ``` subscribers.ListIDs = list_subscribers.ListID ```  ``` subscribers.ID = list_subscribers.SubscriberKey ``` |
| [events](#events) | ``` subscribers.ID = events.SubscriberKey ``` |

subscribers table schema

|  |
| --- |
| **Addresses**  ARRAY This is a nested data structure:   - Address: STRING - AddressStatus: STRING - AddressType: STRING |
| **Attributes**  ARRAY This is a nested data structure:   - Name: STRING - Value: STRING |
| **CreatedDate**  STRING |
| **CustomerKey**  STRING |
| **EmailAddress**  STRING |
| **EmailTypePreference**  STRING |
| **ID**  INTEGER |
| **ListIDs**  ARRAY This is a nested data structure. |
| **Locale**  STRING |
| **ModifiedDate**  STRING |
| **ObjectID**  STRING |
| **PartnerKey**  STRING |
| **PartnerProperties**  ARRAY This is a nested data structure:   - Name: STRING - Value: STRING |
| **PartnerType**  STRING |
| **PrimaryEmailAddress**  STRING |
| **PrimarySMSAddress**  STRING |
| **PrimarySMSPublicationStatus**  STRING |
| **Status**  STRING |
| **SubscriberKey**  STRING |
| **SubscriberTypeDefinition**  STRING |
| **UnsubscribedDate**  STRING |
