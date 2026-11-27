---
title: "Listrak"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Listrak.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Listrak

Listrak is a comprehensive digital marketing automation platform.

Listrak integration replicates data using the [Listrak SOAP API](https://webservices.listrak.com/SoapWSDL.aspx).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

You must have administrative privileges to create a user in your Listrak account.

To create a user:

1. Log into your [Listrak](https://admin.listrak.com/Account/Login.aspx) account.
2. From the home page, click Manage.
3. Click Accounts > User Manager.
4. Scroll to the bottom of the page and click Create New User.
5. Fill in the User Information fields.
6. In the Lists section, select the lists you want the Qlik Talend Cloud user to have access to.

   Qlik Talend Cloud can only replicate data for lists it can access.
7. In the Granted Access field, select Role Based Access, then, in the section below, check the boxes for the following permissions:
   - Analytics Access: Allows you to view analytics for messages, contacts, and lists within accessible lists.
   - API Access: Allows you to replicate data from Listrak using the Listrak API.
8. Click Add User.

Listrak restricts SOAP API access by IP address. To let Qlik Talend Cloud connect, add its IP address to Listrak’s IP authorization list:

1. Log into your [Listrak](https://admin.listrak.com/Account/Login.aspx) account.
2. Navigate to Manage > Accounts > SOAP API IP Authorization.
3. Add the Qlik Talend Cloud IP address that you retrieved.

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
| Username | Username. |
| Password | Password. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### lists

The `lists` table contains info about your contact lists.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | ListID |
| **Useful links** | Listrak documentation  [Listrak API method](https://webservices.listrak.com/v31/IntegrationService.asmx?op=GetContactListCollection "Opens in new tab: Listrak API method") |

lists table foreign keys

| Join lists with | on |
| --- | --- |
| [messages](#messages) | ``` lists.ListID = messages.ListID ``` |
| [subscribed\_contacts](#subscribed-contacts) | ``` lists.ListID = subscribed_contacts.ListID ``` |

lists table schema

|  |
| --- |
| **BounceUnsubscribeCount**  INTEGER |
| **CreateDate**  DATE-TIME |
| **DomainAliasEmail**  STRING |
| **DomainAliasLink**  STRING |
| **EnableBrowserLink**  BOOLEAN |
| **EnableDoubleOptin**  BOOLEAN |
| **EnableDynamicContent**  BOOLEAN |
| **EnableGoogleAnalytics**  BOOLEAN |
| **EnableInternationalization**  BOOLEAN |
| **EnableListHygiene**  BOOLEAN |
| **EnableListRemoveHeader**  BOOLEAN |
| **EnableRSS**  BOOLEAN |
| **EnableRemovalLink**  BOOLEAN |
| **FromEmail**  STRING |
| **FromName**  STRING |
| **GoogleTrackingDomains**  ARRAY This is a nested data structure. |
| **ListID**  INTEGER |
| **ListName**  STRING |
| **ShowAdvancedPersonalization**  BOOLEAN |
| **ShowEmailList**  BOOLEAN |
| **Vmta**  OBJECT This is a nested data structure:   - Description: STRING - VmtaID: INTEGER |
| **bounceHandling**  INTEGER |

### message\_bounces

The `message_bounces` table contains info about contact bounces for a message.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | MsgID  EmailAddress |
| **Useful links** | Listrak documentation  [Listrak API method](https://webservices.listrak.com/v31/IntegrationService.asmx?op=ReportRangeMessageContactBounces "Opens in new tab: Listrak API method") |

message\_bounces table foreign keys

| Join message\_bounces with | on |
| --- | --- |
| [message\_clicks](#message-clicks) | ``` message_bounces.ContactID = message_clicks.ContactID ```  ``` message_bounces.MsgID = message_clicks.MsgID ``` |
| [message\_opens](#message-opens) | ``` message_bounces.ContactID = message_opens.ContactID ```  ``` message_bounces.MsgID = message_opens.MsgID ``` |
| [message\_reads](#message-reads) | ``` message_bounces.ContactID = message_reads.ContactID ```  ``` message_bounces.MsgID = message_reads.MsgID ``` |
| [message\_unsubs](#message-unsubs) | ``` message_bounces.ContactID = message_unsubs.ContactID ```  ``` message_bounces.MsgID = message_unsubs.MsgID ``` |
| [subscribed\_contacts](#subscribed-contacts) | ``` message_bounces.ContactID = subscribed_contacts.ContactID ``` |
| [message\_sends](#message-sends) | ``` message_bounces.MsgID = message_sends.MsgID ``` |
| [messages](#messages) | ``` message_bounces.MsgID = messages.MsgID ``` |

message\_bounces table schema

|  |
| --- |
| **BounceCount**  INTEGER |
| **BounceDate**  STRING |
| **BounceDetail**  STRING |
| **BounceReason**  STRING |
| **ContactID**  STRING |
| **EmailAddress**  STRING |
| **MsgID**  INTEGER |

### message\_clicks

The `message_clicks` table contains info about contact clicks for a message.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | MsgID  EmailAddress |
| **Useful links** | Listrak documentation  [Listrak API method](https://webservices.listrak.com/v31/IntegrationService.asmx?op=ReportRangeMessageContactClick "Opens in new tab: Listrak API method") |

message\_clicks table foreign keys

| Join message\_clicks with | on |
| --- | --- |
| [message\_bounces](#message-bounces) | ``` message_clicks.ContactID = message_bounces.ContactID ```  ``` message_clicks.MsgID = message_bounces.MsgID ``` |
| [message\_opens](#message-opens) | ``` message_clicks.ContactID = message_opens.ContactID ```  ``` message_clicks.MsgID = message_opens.MsgID ``` |
| [message\_reads](#message-reads) | ``` message_clicks.ContactID = message_reads.ContactID ```  ``` message_clicks.MsgID = message_reads.MsgID ``` |
| [message\_unsubs](#message-unsubs) | ``` message_clicks.ContactID = message_unsubs.ContactID ```  ``` message_clicks.MsgID = message_unsubs.MsgID ``` |
| [subscribed\_contacts](#subscribed-contacts) | ``` message_clicks.ContactID = subscribed_contacts.ContactID ``` |
| [message\_sends](#message-sends) | ``` message_clicks.MsgID = message_sends.MsgID ``` |
| [messages](#messages) | ``` message_clicks.MsgID = messages.MsgID ``` |

message\_clicks table schema

|  |
| --- |
| **ClickDate**  STRING |
| **ContactID**  STRING |
| **EmailAddress**  STRING |
| **LinkDescription**  STRING |
| **LinkUrl**  STRING |
| **MsgID**  INTEGER |

### message\_opens

The `message_opens` table contains info about contact opens for a message.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | MsgID  EmailAddress |
| **Useful links** | Listrak documentation  [Listrak API method](https://webservices.listrak.com/v31/IntegrationService.asmx?op=ReportRangeMessageContactOpen "Opens in new tab: Listrak API method") |

message\_opens table foreign keys

| Join message\_opens with | on |
| --- | --- |
| [message\_bounces](#message-bounces) | ``` message_opens.ContactID = message_bounces.ContactID ```  ``` message_opens.MsgID = message_bounces.MsgID ``` |
| [message\_clicks](#message-clicks) | ``` message_opens.ContactID = message_clicks.ContactID ```  ``` message_opens.MsgID = message_clicks.MsgID ``` |
| [message\_reads](#message-reads) | ``` message_opens.ContactID = message_reads.ContactID ```  ``` message_opens.MsgID = message_reads.MsgID ``` |
| [message\_unsubs](#message-unsubs) | ``` message_opens.ContactID = message_unsubs.ContactID ```  ``` message_opens.MsgID = message_unsubs.MsgID ``` |
| [subscribed\_contacts](#subscribed-contacts) | ``` message_opens.ContactID = subscribed_contacts.ContactID ``` |
| [message\_sends](#message-sends) | ``` message_opens.MsgID = message_sends.MsgID ``` |
| [messages](#messages) | ``` message_opens.MsgID = messages.MsgID ``` |

message\_opens table schema

|  |
| --- |
| **ContactID**  STRING |
| **EmailAddress**  STRING |
| **MsgID**  INTEGER |
| **OpenDate**  STRING |

### message\_reads

The `message_reads` table contains info about contact reads for a message.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | MsgID  EmailAddress |
| **Useful links** | Listrak documentation  [Listrak API method](https://webservices.listrak.com/v31/IntegrationService.asmx?op=ReportRangeMessageContactRead "Opens in new tab: Listrak API method") |

message\_reads table foreign keys

| Join message\_reads with | on |
| --- | --- |
| [message\_bounces](#message-bounces) | ``` message_reads.ContactID = message_bounces.ContactID ```  ``` message_reads.MsgID = message_bounces.MsgID ``` |
| [message\_clicks](#message-clicks) | ``` message_reads.ContactID = message_clicks.ContactID ```  ``` message_reads.MsgID = message_clicks.MsgID ``` |
| [message\_opens](#message-opens) | ``` message_reads.ContactID = message_opens.ContactID ```  ``` message_reads.MsgID = message_opens.MsgID ``` |
| [message\_unsubs](#message-unsubs) | ``` message_reads.ContactID = message_unsubs.ContactID ```  ``` message_reads.MsgID = message_unsubs.MsgID ``` |
| [subscribed\_contacts](#subscribed-contacts) | ``` message_reads.ContactID = subscribed_contacts.ContactID ``` |
| [message\_sends](#message-sends) | ``` message_reads.MsgID = message_sends.MsgID ``` |
| [messages](#messages) | ``` message_reads.MsgID = messages.MsgID ``` |

message\_reads table schema

|  |
| --- |
| **ContactID**  STRING |
| **EmailAddress**  STRING |
| **MsgID**  INTEGER |
| **ReadDate**  STRING |

### message\_sends

The `message_sends` table contains `MsgID` and `EmailAddress` pairs, allowing you to identify the messages that your contacts have been sent.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | MsgID  EmailAddress |
| **Useful links** | Listrak documentation  [Listrak API method](https://webservices.listrak.com/v31/IntegrationService.asmx?op=ReportMessageContactSent "Opens in new tab: Listrak API method") |

message\_sends table foreign keys

| Join message\_sends with | on |
| --- | --- |
| [message\_bounces](#message-bounces) | ``` message_sends.MsgID = message_bounces.MsgID ``` |
| [message\_clicks](#message-clicks) | ``` message_sends.MsgID = message_clicks.MsgID ``` |
| [message\_opens](#message-opens) | ``` message_sends.MsgID = message_opens.MsgID ``` |
| [message\_reads](#message-reads) | ``` message_sends.MsgID = message_reads.MsgID ``` |
| [message\_unsubs](#message-unsubs) | ``` message_sends.MsgID = message_unsubs.MsgID ``` |
| [messages](#messages) | ``` message_sends.MsgID = messages.MsgID ``` |

message\_sends table schema

|  |
| --- |
| **EmailAddress**  STRING |
| **MsgID**  INTEGER |

### message\_unsubs

The `message_unsubs` table contains info about contacts who requested to be removed from a list from the supplied message.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | MsgID  EmailAddress |
| **Useful links** | Listrak documentation  [Listrak API method](https://webservices.listrak.com/v31/IntegrationService.asmx?op=ReportRangeMessageContactRemoval "Opens in new tab: Listrak API method") |

message\_unsubs table foreign keys

| Join message\_unsubs with | on |
| --- | --- |
| [message\_bounces](#message-bounces) | ``` message_unsubs.ContactID = message_bounces.ContactID ```  ``` message_unsubs.MsgID = message_bounces.MsgID ``` |
| [message\_clicks](#message-clicks) | ``` message_unsubs.ContactID = message_clicks.ContactID ```  ``` message_unsubs.MsgID = message_clicks.MsgID ``` |
| [message\_opens](#message-opens) | ``` message_unsubs.ContactID = message_opens.ContactID ```  ``` message_unsubs.MsgID = message_opens.MsgID ``` |
| [message\_reads](#message-reads) | ``` message_unsubs.ContactID = message_reads.ContactID ```  ``` message_unsubs.MsgID = message_reads.MsgID ``` |
| [subscribed\_contacts](#subscribed-contacts) | ``` message_unsubs.ContactID = subscribed_contacts.ContactID ``` |
| [message\_sends](#message-sends) | ``` message_unsubs.MsgID = message_sends.MsgID ``` |
| [messages](#messages) | ``` message_unsubs.MsgID = messages.MsgID ``` |

message\_unsubs table schema

|  |
| --- |
| **AdditionDate**  STRING |
| **ContactID**  STRING |
| **EmailAddress**  STRING |
| **MsgID**  INTEGER |
| **RemovalDate**  STRING |
| **RemovalMethod**  STRING |

### messages

The `messages` table contains info about message statistics.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | MsgID |
| **Useful links** | Listrak documentation  [Listrak API method](https://webservices.listrak.com/v31/IntegrationService.asmx?op=ReportListMessageActivity "Opens in new tab: Listrak API method") |

messages table foreign keys

| Join messages with | on |
| --- | --- |
| [message\_bounces](#message-bounces) | ``` messages.MsgID = message_bounces.MsgID ``` |
| [message\_clicks](#message-clicks) | ``` messages.MsgID = message_clicks.MsgID ``` |
| [message\_opens](#message-opens) | ``` messages.MsgID = message_opens.MsgID ``` |
| [message\_reads](#message-reads) | ``` messages.MsgID = message_reads.MsgID ``` |
| [message\_sends](#message-sends) | ``` messages.MsgID = message_sends.MsgID ``` |
| [message\_unsubs](#message-unsubs) | ``` messages.MsgID = message_unsubs.MsgID ``` |
| [lists](#lists) | ``` messages.ListID = lists.ListID ``` |
| [subscribed\_contacts](#subscribed-contacts) | ``` messages.ListID = subscribed_contacts.ListID ``` |

messages table schema

|  |
| --- |
| **AverageOrderValue**  NUMBER |
| **ClickCount**  INTEGER |
| **ClickerCount**  INTEGER |
| **ClickerPercent**  NUMBER |
| **ConversionCount**  INTEGER |
| **DeliverCount**  INTEGER |
| **ListID**  INTEGER |
| **MsgID**  INTEGER |
| **NewClickerCount**  INTEGER |
| **OpenCount**  INTEGER |
| **OpenPercent**  NUMBER |
| **OrderTotal**  NUMBER |
| **ReadCount**  INTEGER |
| **ReadPercent**  NUMBER |
| **RemoveCount**  INTEGER |
| **RemovePercent**  NUMBER |
| **RepeatClickerCount**  INTEGER |
| **SendDate**  DATE-TIME |
| **Subject**  STRING |

### subscribed\_contacts

The `subscribed_contacts` table contains info about contacts who are currently subscribed to the specified list.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | ContactID  ListID |
| **Useful links** | Listrak documentation  [Listrak API method](https://webservices.listrak.com/v31/IntegrationService.asmx?op=ReportRangeSubscribedContacts "Opens in new tab: Listrak API method") |

subscribed\_contacts table foreign keys

| Join subscribed\_contacts with | on |
| --- | --- |
| [message\_bounces](#message-bounces) | ``` subscribed_contacts.ContactID = message_bounces.ContactID ``` |
| [message\_clicks](#message-clicks) | ``` subscribed_contacts.ContactID = message_clicks.ContactID ``` |
| [message\_opens](#message-opens) | ``` subscribed_contacts.ContactID = message_opens.ContactID ``` |
| [message\_reads](#message-reads) | ``` subscribed_contacts.ContactID = message_reads.ContactID ``` |
| [message\_unsubs](#message-unsubs) | ``` subscribed_contacts.ContactID = message_unsubs.ContactID ``` |
| [lists](#lists) | ``` subscribed_contacts.ListID = lists.ListID ``` |
| [messages](#messages) | ``` subscribed_contacts.ListID = messages.ListID ``` |

subscribed\_contacts table schema

|  |
| --- |
| **AdditionDate**  DATE-TIME |
| **AdditionMethod**  STRING |
| **ContactID**  STRING |
| **EmailAddress**  STRING |
| **ListID**  INTEGER |
