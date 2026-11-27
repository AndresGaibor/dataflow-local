---
title: "Twilio"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Twilio.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Twilio

Twilio is a customer engagement platform.

For more information about the API, see [Twilio REST API](https://www.twilio.com/docs/usage/api) .

See the [Schema](#Schema) section for a list of objects available for replication.See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To obtain the Account SID and Auth token:

1. Log into your Twilio account.
2. Click Console.
3. Copy your Account SID and Auth Token.

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
| Auth Token | Authentication token. |
| Date Window Days | Enter a value. Example: 30.  This parameter should be set to an optimum value to improve historical sync performance. Setting this value too low will take longer to complete historical sync and setting it larger may result in request timeouts or memory overflow issues. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### account\_balance

The **account\_balance** returns your Twilio account balance.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | account\_sid |

account\_balance table schema

|  |
| --- |
| **account\_sid**  STRING |
| **balance**  NUMBER |
| **currency**  STRING |

### accounts

The **accounts** table returns a list of accounts in your Twilio account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | sid |
| **Useful links** | [Twilio documentation](https://www.twilio.com/docs/iam/api/account#read-multiple-account-resources)  [Twilio API method](https://www.twilio.com/docs/iam/api/account#code-list-all-accounts) |

accounts table schema

|  |
| --- |
| **auth\_token**  STRING |
| **date\_created**  DATE-TIME |
| **date\_updated**  DATE-TIME |
| **friendly\_name**  STRING |
| **owner\_account\_sid**  STRING |
| **sid**  STRING |
| **status**  STRING |
| **subresource\_uris**    ARRAY This is a nested data structure:   - **subresource**: STRING - **uri**: STRING |
| **type**  STRING |
| **uri**  STRING |

### addresses

The **addresses** table returns a list of address resource representations, each representing an address within your Twilio account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | sid |
| **Replication Key** | date\_updated |
| **Useful links** | [Twilio documentation](https://www.twilio.com/docs/usage/api/address#read-multiple-address-resources)  [Twilio API method](https://www.twilio.com/docs/usage/api/address#code-show-all-addresses) |

addresses table schema

|  |
| --- |
| **account\_sid**  STRING |
| **city**  STRING |
| **customer\_name**  STRING |
| **date\_created**  DATE-TIME |
| **date\_updated**  DATE-TIME |
| **emergency\_enabled**  BOOLEAN |
| **friendly\_name**  STRING |
| **iso\_country**  STRING |
| **postal\_code**  STRING |
| **region**  STRING |
| **sid**  STRING |
| **street**  STRING |
| **uri**  STRING |
| **validated**  BOOLEAN |
| **verified**  BOOLEAN |

### alerts

The **alerts** returns a list of alerts generated for an account within your Twilio account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | sid |
| **Replication Key** | date\_updated |
| **Useful links** | [Twilio documentation](https://www.twilio.com/docs/usage/monitor-alert#read-multiple-alert-resources)  [Twilio API method](https://www.twilio.com/docs/usage/monitor-alert#code-list-all-alerts) |

alerts table schema

|  |
| --- |
| **account\_sid**  STRING |
| **alert\_text**  STRING |
| **api\_version**  STRING |
| **date\_created**  DATE-TIME |
| **date\_generated**  DATE-TIME |
| **date\_updated**  DATE-TIME |
| **error\_code**  STRING |
| **log\_level**  STRING |
| **more\_info**  STRING |
| **request\_method**  STRING |
| **request\_url**  STRING |
| **resource\_sid**  STRING |
| **service\_sid**  STRING |
| **sid**  STRING |
| **url**  STRING |

### applications

The **applications** table returns a list of application resource representations, each representing an application within your Twilio account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | sid |
| **Replication Key** | date\_created |
| **Useful links** | [Twilio documentation](https://www.twilio.com/docs/usage/api/applications#read-multiple-application-resources)  [Twilio API method](https://www.twilio.com/docs/usage/api/applications#code-list-all-application-resource-representations) |

applications table schema

|  |
| --- |
| **account\_sid**  STRING |
| **api\_version**  STRING |
| **date\_created**  DATE-TIME |
| **date\_updated**  DATE-TIME |
| **friendly\_name**  STRING |
| **message\_status\_callback**  STRING |
| **sid**  STRING |
| **sms\_fallback\_method**  STRING |
| **sms\_fallback\_url**  STRING |
| **sms\_method**  STRING |
| **sms\_status\_callback**  STRING |
| **sms\_url**  STRING |
| **status\_callback**  STRING |
| **status\_callback\_method**  STRING |
| **uri**  STRING |
| **voice\_callback\_id\_lookup**  BOOLEAN |
| **voice\_fallback\_method**  STRING |
| **voice\_fallback\_url**  STRING |
| **voice\_method**  STRING |
| **voice\_url**  STRING |

### available\_phone\_number\_countries

The **available\_phone\_number\_countries** table returns a list of countries that have phone numbers to purchase for your Twilio account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | country\_code |
| **Useful links** | [Twilio documentation](https://www.twilio.com/docs/phone-numbers/api/availablephonenumber-resource#read-a-list-of-countries)  [Twilio API method](https://www.twilio.com/docs/phone-numbers/api/availablephonenumber-resource#code-read-a-list-of-countries) |

available\_phone\_number\_countries table schema

|  |
| --- |
| **beta**  BOOLEAN |
| **country**  STRING |
| **country\_code**  STRING |
| **subresource\_uris**    ARRAY This is a nested data structure:   - **subresource**: STRING - **uri**: STRING |
| **uri**  STRING |

### available\_phone\_numbers\_local

The **available\_phone\_numbers\_local** table returns a list of available phone numbers for local resources for your Twilio account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | iso\_country  phone\_number |
| **Useful links** | [Twilio API method](https://www.twilio.com/docs/phone-numbers/api/availablephonenumberlocal-resource) |

available\_phone\_numbers\_local table schema

|  |
| --- |
| **address\_requirements**  STRING |
| **beta**  BOOLEAN |
| **capabilities**  OBJECT This is a nested data structure:   - **MMS**: BOOLEAN - **SMS**: BOOLEAN - **fax**: BOOLEAN - **voice**: BOOLEAN |
| **friendly\_name**  STRING |
| **iso\_country**  STRING |
| **lata**  STRING |
| **latitude**    NUMBER  STRING |
| **locality**  STRING |
| **longitude**    NUMBER  STRING |
| **phone\_number**  STRING |
| **postal\_code**  STRING |
| **rate\_center**  STRING |
| **region**  STRING |

### available\_phone\_numbers\_mobile

The **available\_phone\_numbers\_mobile** table returns a list of available phone numbers for mobile resources for your Twilio account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | iso\_country  phone\_number |
| **Useful links** | [Twilio documentation](https://www.twilio.com/docs/phone-numbers/api/availablephonenumber-mobile-resource)  [Twilio API method](https://www.twilio.com/docs/phone-numbers/api/availablephonenumber-mobile-resource#code-find-mobile-numbers-by-region) |

available\_phone\_numbers\_mobile table schema

|  |
| --- |
| **address\_requirements**  STRING |
| **beta**  BOOLEAN |
| **capabilities**  OBJECT This is a nested data structure:   - **MMS**: BOOLEAN - **SMS**: BOOLEAN - **fax**: BOOLEAN - **voice**: BOOLEAN |
| **friendly\_name**  STRING |
| **iso\_country**  STRING |
| **lata**  STRING |
| **latitude**    NUMBER  STRING |
| **locality**  STRING |
| **longitude**    NUMBER  STRING |
| **phone\_number**  STRING |
| **postal\_code**  STRING |
| **rate\_center**  STRING |
| **region**  STRING |

### available\_phone\_numbers\_toll\_free

The **available\_phone\_numbers\_toll\_free** table returns a list of available toll free phone numbers for your Twilio account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | iso\_country  phone\_number |
| **Useful links** | [Twilio documentation](https://www.twilio.com/docs/phone-numbers/api/availablephonenumber-tollfree-resource)  [Twilio API method](https://www.twilio.com/docs/phone-numbers/api/availablephonenumber-tollfree-resource#code-find-any-toll-free-number) |

available\_phone\_numbers\_toll\_free table schema

|  |
| --- |
| **address\_requirements**  STRING |
| **beta**  BOOLEAN |
| **capabilities**  OBJECT This is a nested data structure:   - **MMS**: BOOLEAN - **SMS**: BOOLEAN - **fax**: BOOLEAN - **voice**: BOOLEAN |
| **friendly\_name**  STRING |
| **iso\_country**  STRING |
| **lata**  STRING |
| **latitude**    NUMBER  STRING |
| **locality**  STRING |
| **longitude**    NUMBER  STRING |
| **phone\_number**  STRING |
| **postal\_code**  STRING |
| **rate\_center**  STRING |
| **region**  STRING |

### calls

The **calls** table returns a list of phone calls made to and from an account in your Twilio account, identified by its `AccountSid`.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | sid |
| **Replication Key** | date\_updated |
| **Useful links** | [Twilio documentation](https://www.twilio.com/docs/voice/api/call-resource#read-multiple-call-resources)  [Twilio API method](https://www.twilio.com/docs/voice/api/call-resource#code-read-multiple-call-resources) |

calls table schema

|  |
| --- |
| **account\_sid**  STRING |
| **annotation**  STRING |
| **answered\_by**  STRING |
| **api\_version**  STRING |
| **caller\_name**  STRING |
| **date\_created**  DATE-TIME |
| **date\_updated**  DATE-TIME |
| **direction**  STRING |
| **duration**  INTEGER |
| **end\_time**  DATE-TIME |
| **forwarded\_from**  STRING |
| **from**  STRING |
| **from\_formatted**  STRING |
| **group\_sid**  STRING |
| **parent\_call\_sid**  STRING |
| **phone\_number\_sid**  STRING |
| **price**  NUMBER |
| **price\_unit**  STRING |
| **queue\_time**  INTEGER |
| **sid**  STRING |
| **start\_time**  DATE-TIME |
| **status**  STRING |
| **subresource\_uris**    ARRAY This is a nested data structure:   - **subresource**: STRING - **uri**: STRING |
| **to**  STRING |
| **to\_formatted**  STRING |
| **trunk\_sid**  STRING |
| **uri**  STRING |

### conference\_participants

The **conference\_participants** table returns the list of active participants in the Twilio conference identified by `ConferenceSid`.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | uri |
| **Useful links** | [Twilio documentation](https://www.twilio.com/docs/voice/api/conference-participant-resource#twilio-docs-content-area)  [Twilio API method](https://www.twilio.com/docs/voice/api/conference-participant-resource#code-create-a-conference-participant) |

conference\_participants table schema

|  |
| --- |
| **account\_sid**  STRING |
| **call\_sid**  STRING |
| **call\_sid\_to\_coach**  STRING |
| **coaching**  BOOLEAN |
| **conference\_sid**  STRING |
| **date\_created**  DATE-TIME |
| **date\_updated**  DATE-TIME |
| **end\_conference\_on\_exit**  BOOLEAN |
| **hold**  BOOLEAN |
| **label**  STRING |
| **muted**  BOOLEAN |
| **start\_conference\_on\_enter**  BOOLEAN |
| **status**  STRING |
| **uri**  STRING |

### conferences

The **conferences** table returns all the conferences within your Twilio account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | sid |
| **Replication Key** | date\_updated |
| **Useful links** | [Twilio documentation](https://www.twilio.com/docs/voice/api/conference-resource#read-multiple-conference-resources)  [Twilio API method](https://www.twilio.com/docs/voice/api/conference-resource#code-read-multiple-conference-resources) |

conferences table schema

|  |
| --- |
| **account\_sid**  STRING |
| **api\_version**  STRING |
| **call\_sid\_ending\_conference**  STRING |
| **date\_created**  DATE-TIME |
| **date\_updated**  DATE-TIME |
| **friendly\_name**  STRING |
| **reason\_conference\_ended**  STRING |
| **region**  STRING |
| **sid**  STRING |
| **status**  STRING |
| **subresource\_uris**    ARRAY This is a nested data structure:   - **subresource**: STRING - **uri**: STRING |
| **uri**  STRING |

### dependent\_phone\_numbers

The **dependent\_phone\_numbers** table returns a list of `IncomingPhoneNumbers` in your Twilio account that require the specified address.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | sid |
| **Useful links** | [Twilio API method](https://www.twilio.com/docs/usage/api/address#code-list-dependent-pns-subresources) |

dependent\_phone\_numbers table schema

|  |
| --- |
| **account\_sid**  STRING |
| **address\_requirements**  STRING |
| **api\_version**  STRING |
| **capabilities**  OBJECT This is a nested data structure:   - **fax**: BOOLEAN - **mms**: BOOLEAN - **sms**: BOOLEAN - **voice**: BOOLEAN |
| **date\_created**  DATE-TIME |
| **date\_updated**  DATE-TIME |
| **emergency\_address\_sid**  STRING |
| **emergency\_status**  STRING |
| **friendly\_name**  STRING |
| **phone\_number**  STRING |
| **sid**  STRING |
| **sms\_application\_sid**  STRING |
| **sms\_fallback\_method**  STRING |
| **sms\_fallback\_url**  STRING |
| **sms\_method**  STRING |
| **sms\_url**  STRING |
| **status\_callback**  STRING |
| **status\_callback\_method**  STRING |
| **trunk\_sid**  STRING |
| **uri**  STRING |
| **voice\_application\_sid**  STRING |
| **voice\_caller\_id\_lookup**  BOOLEAN |
| **voice\_fallback\_method**  STRING |
| **voice\_fallback\_url**  STRING |
| **voice\_method**  STRING |
| **voice\_url**  STRING |

### incoming\_phone\_numbers

The **incoming\_phone\_numbers** table returns a list of `IncomingPhoneNumbers` in your Twilio account that require the specified address.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | sid |
| **Replication Key** | date\_updated |
| **Useful links** | [Twilio documentation](https://www.twilio.com/docs/phone-numbers/api/incomingphonenumber-resource#twilio-docs-content-area)  [Twilio API method](https://www.twilio.com/docs/phone-numbers/api/incomingphonenumber-resource#code-provision-a-phone-number) |

incoming\_phone\_numbers table schema

|  |
| --- |
| **account\_sid**  STRING |
| **address\_requirements**  STRING |
| **address\_sid**  STRING |
| **api\_version**  STRING |
| **beta**  BOOLEAN |
| **bundle\_sid**  STRING |
| **capabilities**  OBJECT This is a nested data structure:   - **fax**: BOOLEAN - **mms**: BOOLEAN - **sms**: BOOLEAN - **voice**: BOOLEAN |
| **date\_created**  DATE-TIME |
| **date\_updated**  DATE-TIME |
| **emergency\_address\_sid**  STRING |
| **emergency\_address\_status**  STRING |
| **emergency\_status**  STRING |
| **friendly\_name**  STRING |
| **identity\_sid**  STRING |
| **origin**  STRING |
| **phone\_number**  STRING |
| **sid**  STRING |
| **sms\_application\_sid**  STRING |
| **sms\_fallback\_method**  STRING |
| **sms\_fallback\_url**  STRING |
| **sms\_method**  STRING |
| **sms\_url**  STRING |
| **status**  STRING |
| **status\_callback**  STRING |
| **status\_callback\_method**  STRING |
| **trunk\_sid**  STRING |
| **uri**  STRING |
| **voice\_application\_sid**  STRING |
| **voice\_caller\_id\_lookup**  BOOLEAN |
| **voice\_fallback\_method**  STRING |
| **voice\_fallback\_url**  STRING |
| **voice\_method**  STRING |
| **voice\_receive\_mode**  STRING |
| **voice\_url**  STRING |

### keys

The **keys** table returns a list of API Keys in your Twilio account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | sid |
| **Replication Key** | date\_updated |
| **Useful links** | [Twilio API method](https://www.twilio.com/docs/iam/api-keys/key-resource-v2010#read-a-key-resource) |

keys table schema

|  |
| --- |
| **account\_sid**  STRING |
| **date\_created**  DATE-TIME |
| **date\_updated**  DATE-TIME |
| **friendly\_name**  STRING |
| **sid**  STRING |

### message\_media

The **message\_media** table returns the list of media associated with your Twilio message.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | sid |
| **Useful links** | [Twilio documentation](https://www.twilio.com/docs/messaging/api/media-resource#read-multiple-media-resources)  [Twilio API method](https://www.twilio.com/docs/messaging/api/media-resource#code-read-media) |

message\_media table schema

|  |
| --- |
| **account\_sid**  STRING |
| **content\_type**  STRING |
| **date\_created**  DATE-TIME |
| **date\_updated**  DATE-TIME |
| **parent\_sid**  STRING |
| **sid**  STRING |
| **uri**  STRING |

### messages

The **messages** table returns a list of messages associated with your Twilio account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | sid |
| **Replication Key** | date\_updated |
| **Useful links** | [Twilio documentation](https://www.twilio.com/docs/messaging/api/message-resource#read-multiple-message-resources)  [Twilio API method](https://www.twilio.com/docs/messaging/api/message-resource#code-list-all-message-resources) |

messages table schema

|  |
| --- |
| **account\_sid**  STRING |
| **api\_version**  STRING |
| **body**  STRING |
| **date\_created**  DATE-TIME |
| **date\_sent**  DATE-TIME |
| **date\_updated**  DATE-TIME |
| **direction**  STRING |
| **error\_code**  STRING |
| **error\_message**  STRING |
| **from**  STRING |
| **messaging\_service\_sid**  STRING |
| **num\_media**  INTEGER |
| **num\_segments**  INTEGER |
| **price**  NUMBER |
| **price\_unit**  STRING |
| **sid**  STRING |
| **status**  STRING |
| **subresource\_uris**    ARRAY This is a nested data structure:   - **subresource**: STRING - **uri**: STRING |
| **to**  STRING |
| **uri**  STRING |

### outgoing\_caller\_ids

The **outgoing\_caller\_ids** table returns a list of `OutgoingCallerId` resource representations, each representing a Caller ID number valid for a Twilio account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | sid |
| **Replication Key** | date\_updated |
| **Useful links** | [Twilio API method](https://www.twilio.com/docs/voice/api/outgoing-caller-ids#twilio-docs-content-area) |

outgoing\_caller\_ids table schema

|  |
| --- |
| **account\_sid**  STRING |
| **date\_created**  DATE-TIME |
| **date\_updated**  DATE-TIME |
| **friendly\_name**  STRING |
| **phone\_number**  STRING |
| **sid**  STRING |
| **uri**  STRING |

### queues

The **queues** table returns the list of call queues within your Twilio account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | sid |
| **Replication Key** | date\_updated |
| **Useful links** | [Twilio documentation](https://www.twilio.com/docs/voice/api/queue-resource#read-multiple-queue-resources)  [Twilio API method](https://www.twilio.com/docs/voice/api/queue-resource#code-read-multiple-queue-resources) |

queues table schema

|  |
| --- |
| **account\_sid**  STRING |
| **average\_wait\_time**  INTEGER |
| **current\_size**  INTEGER |
| **date\_created**  DATE-TIME |
| **date\_updated**  DATE-TIME |
| **friendly\_name**  STRING |
| **max\_size**  INTEGER |
| **sid**  STRING |
| **subresource\_uris**    ARRAY This is a nested data structure:   - **subresource**: STRING - **uri**: STRING |
| **uri**  STRING |

### recordings

The **recordings** table returns a list of recordings, each representing a recording generated during a call or conference in your Twilio account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | sid |
| **Replication Key** | date\_created |
| **Useful links** | [Twilio documentation](https://www.twilio.com/docs/voice/api/recording#read-multiple-recording-resources)  [Twilio API method](https://www.twilio.com/docs/voice/api/recording#code-get-all-recordings-for-an-account) |

recordings table schema

|  |
| --- |
| **account\_sid**  STRING |
| **api\_version**  STRING |
| **call\_sid**  STRING |
| **channels**  INTEGER |
| **conference\_sid**  STRING |
| **date\_created**  DATE-TIME |
| **date\_updated**  DATE-TIME |
| **duration**  INTEGER |
| **encryption\_details**  OBJECT This is a nested data structure:   - **encryption\_cek**: STRING - **encryption\_public\_key\_sid**: STRING - **iv**: STRING - **type**: STRING |
| **error\_code**  STRING |
| **price**  NUMBER |
| **price\_unit**  STRING |
| **sid**  STRING |
| **source**  STRING |
| **start\_time**  DATE-TIME |
| **status**  STRING |
| **subresource\_uris**    ARRAY This is a nested data structure:   - **subresource**: STRING - **uri**: STRING |
| **uri**  STRING |

### transcriptions

The **transcriptions** table returns the full set of transcriptions generated from all recordings in your Twilio account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | sid |
| **Replication Key** | date\_updated |
| **Useful links** | [Twilio documentation](https://www.twilio.com/docs/voice/api/recording-transcription#read-multiple-transcription-resources)  [Twilio API method](https://www.twilio.com/docs/voice/api/recording-transcription#code-read-list-all-transcriptions) |

transcriptions table schema

|  |
| --- |
| **account\_sid**  STRING |
| **api\_version**  STRING |
| **date\_created**  DATE-TIME |
| **date\_updated**  DATE-TIME |
| **duration**  INTEGER |
| **price**  NUMBER |
| **price\_unit**  STRING |
| **recording\_sid**  STRING |
| **sid**  STRING |
| **status**  STRING |
| **transcription\_text**  STRING |
| **type**  STRING |
| **uri**  STRING |

### usage\_records

The **usage\_records** table returns a list of usage records in your Twilio account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | account\_sid  category  start\_date |
| **Replication Key** | start\_date |
| **Useful links** | [Twilio documentation](https://www.twilio.com/docs/usage/api/usage-record#read-multiple-usagerecord-resources)  [Twilio API method](https://www.twilio.com/docs/usage/api/usage-record#usage-all-categories) |

usage\_records table schema

|  |
| --- |
| **account\_sid**  STRING |
| **api\_version**  STRING |
| **as\_of**  DATE-TIME |
| **category**  STRING |
| **count**    INTEGER  STRING |
| **count\_unit**  STRING |
| **description**  STRING |
| **end\_date**  DATE-TIME |
| **price**    NUMBER |
| **price\_unit**  STRING |
| **start\_date**  DATE-TIME |
| **subresource\_uris**    ARRAY This is a nested data structure:   - **subresource**: STRING - **uri**: STRING |
| **uri**  STRING |
| **usage**    NUMBER  STRING |
| **usage\_unit**  STRING |

### usage\_triggers

The **usage\_triggers** table returns list of usage triggers in your Twilio account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | sid |
| **Replication Key** | date\_updated |
| **Useful links** | [Twilio documentation](https://www.twilio.com/docs/usage/api/usage-trigger#read-multiple-usagetrigger-resources)  [Twilio API method](https://www.twilio.com/docs/usage/api/usage-trigger#code-read-multiple-usagetrigger-resources) |

usage\_triggers table schema

|  |
| --- |
| **account\_sid**  STRING |
| **api\_version**  STRING |
| **callback\_method**  STRING |
| **callback\_url**  STRING |
| **current\_value**  NUMBER |
| **date\_created**  DATE-TIME |
| **date\_fired**  DATE-TIME |
| **date\_updated**  DATE-TIME |
| **friendly\_name**  STRING |
| **recurring**  STRING |
| **sid**  STRING |
| **trigger\_by**  STRING |
| **trigger\_value**  NUMBER |
| **uri**  STRING |
| **usage\_category**  STRING |
| **usage\_record\_uri**  STRING |
