---
title: "Kustomer"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Kustomer.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Kustomer

Kustomer is a cloud-based solution, which helps small to large businesses streamline communication and provide client support via multiple channels.

Kustomer integration replicates data using the [Kustomer REST API v1](https://apidocs.kustomer.com/?version=latest).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To create the API token:

1. Log into your [Kustomer](https://dash.readme.com/to/kustomer-enterprise-group) account.
2. Go to Settings > API Keys.
3. Click New API Key.
4. Select the roles that can have access to the API key.
5. Leave the API expiration option blank.

   If you set an expiration date, the API key will expire and the connection will break. If this happens, you need to re-generate the API key in Kustomer and enter the new key.
6. Click Create.
7. Copy and paste your API token into a secured file.

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

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### conversations

The `conversations` table contains information about conversations in the Kustomer app.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Kustomer documentation](https://dev.kustomer.com/v1/conversations/)  [Kustomer API method](https://dev.kustomer.com/v1/conversations/get-conversations "Opens in new tab: Kustomer API method") |

conversations table schema

|  |
| --- |
| **assigned\_teams**    ARRAY This is a nested data structure. |
| **assigned\_users**    ARRAY This is a nested data structure. |
| **channels**    ARRAY This is a nested data structure. |
| **created\_at**  STRING |
| **created\_by**  OBJECT This is a nested data structure:   - id: STRING - type: STRING |
| **custom**  OBJECT This is a nested data structure:   - auto\_response\_at: STRING - brand\_str: STRING - business\_area\_str: STRING - case\_id\_str: STRING - close\_out\_tree: STRING - contact\_reason\_tree: STRING - desk\_ticket\_url: STRING - issue\_report\_tree: STRING - new\_primary\_menu\_str: STRING - order\_number\_id: STRING - refund\_status\_str: STRING - return\_requested\_str: STRING - return\_str: STRING - rma\_id\_str: STRING - serial\_number\_str: STRING - shopify\_order\_str: STRING - yale\_call\_reason\_tree: STRING - yale\_connectivity\_str: STRING - yale\_finish\_str: STRING - yale\_model\_str: STRING - yale\_notes\_txt: STRING - yale\_resolution\_str: STRING - yale\_serial\_number\_str: STRING |
| **customer**  OBJECT This is a nested data structure:   - id: STRING - type: STRING |
| **direction**  STRING |
| **done\_count**  INTEGER |
| **ended**  BOOLEAN |
| **ended\_at**  STRING |
| **ended\_by**  OBJECT This is a nested data structure:   - id: STRING - type: STRING |
| **ended\_by\_type**  STRING |
| **ended\_reason**  STRING |
| **external\_id**  STRING |
| **first\_done**  OBJECT This is a nested data structure:   - assigned\_teams: ARRAY, which is also a nested data structure. - assigned\_users: ARRAY, which is also a nested data structure. - business\_time: INTEGER - created\_at: STRING - created\_by: STRING - created\_by\_teams: ARRAY, which is also a nested data structure. - last\_message\_direction: STRING - last\_message\_direction\_type: STRING - message\_count: INTEGER - message\_count\_by\_channel: OBJECT, which is also a nested data structure.   - email: INTEGER   - sms: INTEGER   - voice: INTEGER - note\_count: INTEGER - outbound\_message\_count: INTEGER - outbound\_message\_count\_by\_channel: OBJECT, which is is also a nested data structure.   - email: INTEGER   - sms: INTEGER   - voice: INTEGER - time: INTEGER |
| **first\_message\_in**  OBJECT This is a nested data structure:   - channel: STRING - created\_at: STRING - direction\_type: STRING - id: STRING - sent\_at: STRING |
| **first\_message\_out**  OBJECT This is a nested data structure:   - channel: STRING - created\_at: STRING - created\_by: STRING - created\_by\_teams: ARRAY, which is also a nested data structure. - direction\_type: STRING - id: STRING - sent\_at: STRING |
| **first\_response**  OBJECT This is a nested data structure:   - assigned\_teams: ARRAY, which is also a nested data structure. - assigned\_users: ARRAY, which is also a nested data structure. - business\_time: INTEGER - created\_at: STRING - created\_by: STRING - created\_by\_teams: ARRAY, which is also a nested data structure. - id: STRING - response\_time: INTEGER - sent\_at: STRING - time: INTEGER |
| **first\_response\_since\_last\_done**  OBJECT This is a nested data structure:   - assigned\_teams: ARRAY, which is also a nested data structure. - assigned\_users: ARRAY, which is also a nested data structure. - business\_time: INTEGER - created\_at: STRING - created\_by: STRING - created\_by\_teams: ARRAY, which is also a nested data structure. - id: STRING - response\_time: INTEGER - sent\_at: STRING - time: INTEGER |
| **id**  STRING |
| **imported\_at**  STRING |
| **last\_activity\_at**  STRING |
| **last\_done**  OBJECT This is a nested data structure:   - assigned\_teams: ARRAY, which is also a nested data structure. - assigned\_users: ARRAY, which is also a nested data structure. - business\_time: INTEGER - created\_at: STRING - created\_by: STRING - created\_by\_teams: ARRAY, which is also a nested data structure. - last\_message\_direction: STRING - last\_message\_direction\_type: INTEGER - message\_count: STRING - message\_count\_by\_channel: OBJECT, which is also a nested data structure.   - email: INTEGER   - sms: INTEGER   - voice: INTEGER - note\_count: INTEGER - outbound\_message\_count: INTEGER - outbound\_message\_count\_by\_channel: OBJECT, which is also a nested data structure.   - email: INTEGER   - sms: INTEGER   - voice: INTEGER - time: INTEGER |
| **last\_message\_at**  STRING |
| **last\_message\_direction**  STRING |
| **last\_message\_in**  OBJECT This is a nested data structure:   - created\_at: STRING - id: STRING - sent\_at: STRING |
| **last\_message\_out**  OBJECT This is a nested data structure:   - created\_at: STRING - id: STRING - sent\_at: STRING |
| **last\_message\_unresponded\_to**  OBJECT This is a nested data structure:   - created\_at: STRING - id: STRING - sent\_at: STRING |
| **last\_message\_unresponded\_to\_since\_last\_done**  OBJECT This is a nested data structure:   - created\_at: STRING - id: STRING - sent\_at: STRING |
| **last\_received\_at**  STRING |
| **last\_response**  OBJECT This is a nested data structure:   - assigned\_teams: ARRAY, which is also a nested data structure. - assigned\_users: ARRAY, which is also a nested data structure. - business\_time: INTEGER - created\_at: STRING - created\_by: STRING - created\_by\_teams: ARRAY, which is also a nested data structure. - id: STRING - time: INTEGER |
| **links**  OBJECT This is a nested data structure:   - self: STRING |
| **merged\_target**  BOOLEAN |
| **message\_count**  INTEGER |
| **modified\_at**  STRING |
| **modified\_by**  OBJECT This is a nested data structure:   - id: STRING - type: STRING |
| **name**  STRING |
| **note\_count**  INTEGER |
| **org**  OBJECT This is a nested data structure:   - id: STRING - type: STRING |
| **outbound\_message\_count**  INTEGER |
| **preview**  STRING |
| **priority**  INTEGER |
| **queue**  OBJECT This is a nested data structure:   - id: STRING - type: STRING |
| **reopen\_count**  INTEGER |
| **rev**  INTEGER |
| **role\_group\_versions**  STRING |
| **satisfaction**  STRING |
| **satisfaction\_level**  OBJECT This is a nested data structure:   - sent\_by\_teams: ARRAY, which is also a nested data structure. |
| **sla**  OBJECT This is a nested data structure:   - breach: OBJECT, which is also a nested data structure.   - at: STRING   - metric: STRING - breached: BOOLEAN - matched\_at: STRING - metrics: OBJECT, which is also a nested data structure.   - first\_response: OBJECT, which is also a nested data structure.     - breach\_at: STRING     - satisfied\_at: STRING   - longest\_unresponded\_message: OBJECT, which is also a nested data structure.     - breach\_at: STRING     - satisfied\_at: STRING - status: STRING - summary: OBJECT, which is also a nested data structure.   - first\_breach\_at: STRING   - satisfied\_at: STRING - version: INTEGER |
| **sla\_data**  OBJECT This is a nested data structure:   - id: STRING - type: STRING |
| **sla\_version**  OBJECT This is a nested data structure:   - id: STRING - type: STRING |
| **snooze**  OBJECT This is a nested data structure:   - status: STRING - status\_at: STRING - time: STRING |
| **snooze\_count**  INTEGER |
| **status**  STRING |
| **suggested\_shortcuts**  STRING |
| **suggested\_tags**  STRING |
| **tags**    ARRAY This is a nested data structure. |
| **total\_done**  OBJECT This is a nested data structure:   - business\_time: INTEGER - time: INTEGER |
| **total\_open**  OBJECT This is a nested data structure:   - business\_time: INTEGER - business\_time\_since\_last\_done: INTEGER - time: INTEGER - time\_since\_last\_done: INTEGER |
| **total\_snooze**  OBJECT This is a nested data structure:   - business\_time: INTEGER - time: INTEGER |
| **type**  STRING |
| **updated\_at**  STRING |

### customers

The `customers` table contains information about customers in the Kustomer app.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Kustomer documentation](https://dev.kustomer.com/v1/customers/)  [Kustomer API method](https://dev.kustomer.com/v1/customers/get-customers "Opens in new tab: Kustomer API method") |

customers table schema

|  |
| --- |
| **active\_users**  STRING |
| **avatar\_url**  STRING |
| **birthday\_at**  STRING |
| **conversation\_counts**  OBJECT This is a nested data structure:   - all: INTEGER - done: INTEGER - open: INTEGER - snoozed: INTEGER |
| **created\_at**  STRING |
| **created\_by**  OBJECT This is a nested data structure:   - id: STRING - type: STRING |
| **custom**  OBJECT This is a nested data structure:   - accepts\_marketing\_bool: BOOLEAN - activation\_date\_str: STRING - app\_version\_str: STRING - august\_id\_str: STRING - august\_serial\_number\_str: STRING - bridge\_date\_installed\_at: STRING - bridge\_serial\_number\_str: STRING - connect\_firmware\_version\_str: STRING - connect\_serial\_number\_str: STRING - doorbell\_date\_installed\_at: STRING - doorbell\_firmware\_version\_str: STRING - doorbell\_serial\_str: STRING - firmware\_version\_str: STRING - keypad\_firmware\_version\_str: STRING - keypad\_installed\_at: STRING - keypad\_serial\_str: STRING - last\_autoresponse\_at: STRING - last\_order\_id\_num: INTEGER - last\_order\_name\_str: STRING - latest\_csat\_num: INTEGER - latest\_nps\_num: INTEGER - lock\_date\_installed\_at: STRING - lock\_firmware\_version\_str: STRING - lock\_serial\_number\_str: STRING - orders\_count\_num: INTEGER - os00\_str: STRING - owner\_guest\_str: STRING - products\_owned\_str: STRING - proof\_of\_purchase\_str: STRING - purchase\_date\_str: STRING - sales\_force\_id\_str: STRING - total\_spent\_num: INTEGER |
| **deleted**  STRING |
| **display\_color**  STRING |
| **display\_icon**  STRING |
| **display\_name**  STRING |
| **emails**    ARRAY This is a nested data structure:   - email: STRING - type: STRING - verified: BOOLEAN |
| **external\_id**  STRING |
| **external\_ids**    ARRAY This is a nested data structure:   - external\_id: STRING - verified: BOOLEAN |
| **facebook\_ids**  STRING |
| **first\_name**  STRING |
| **gender**  STRING |
| **id**  STRING |
| **imported\_at**  DATE-TIME |
| **instagram\_ids**  STRING |
| **last\_activity\_at**  DATE-TIME |
| **last\_conversation**  OBJECT This is a nested data structure:   - channels: ARRAY, which is also a nested data structure. - id: STRING - sentiment: OBJECT, which is also a nested data structure.   - confidence: NUMBER   - polarity: INTEGER - tags: ARRAY, which is also a nested data structure. |
| **last\_customer\_activity\_at**  STRING |
| **last\_message\_at**  STRING |
| **last\_message\_in**  OBJECT This is a nested data structure:   - channel: STRING - sent\_at: STRING - sentiment: STRING |
| **last\_message\_out**  OBJECT This is a nested data structure:   - sent\_at: STRING |
| **last\_message\_unresponded\_to**  OBJECT This is a nested data structure:   - channel: STRING - sent\_at: STRING |
| **last\_name**  STRING |
| **last\_seen\_at**  STRING |
| **links**  OBJECT This is a nested data structure:   - self: STRING |
| **locale**  STRING |
| **locations**  STRING |
| **modified\_at**  STRING |
| **modified\_by**  OBJECT This is a nested data structure:   - id: STRING - type: STRING |
| **name**  STRING |
| **org**  OBJECT This is a nested data structure:   - id: STRING - type: STRING |
| **phones**    ARRAY This is a nested data structure:   - phone: STRING - type: STRING - verified: BOOLEAN |
| **preview**  OBJECT This is a nested data structure:   - channel: STRING - preview\_at: STRING - subject: STRING - text: STRING - type: STRING |
| **progressive\_status**  STRING |
| **recent\_items**    ARRAY This is a nested data structure:   - id: STRING - meta: OBJECT, which is also a nested data structure.   - klass\_name: STRING - type: STRING - updated\_at: STRING |
| **recent\_location**  OBJECT This is a nested data structure:   - updated\_at: STRING |
| **rev**  INTEGER |
| **role\_group\_versions**  STRING |
| **satisfaction\_level**  OBJECT This is a nested data structure:   - first\_satisfaction: OBJECT, which is also a nested data structure.   - sent\_by\_teams: ARRAY, which is also a nested data structure. - last\_satisfaction: OBJECT, which is also a nested data structure.   - sent\_by\_teams: ARRAY, which is also a nested data structure. |
| **sentiment**  OBJECT This is a nested data structure:   - confidence: NUMBER - polarity: INTEGER |
| **shared\_emails**  STRING |
| **shared\_external\_ids**  STRING |
| **shared\_phones**  STRING |
| **shared\_socials**  STRING |
| **signed\_up\_at**  STRING |
| **smooch\_ids**  STRING |
| **socials**  STRING |
| **tags**  STRING |
| **time\_zone**  STRING |
| **updated\_at**  STRING |
| **urls**  STRING |
| **username**  STRING |
| **verified**  BOOLEAN |
| **watchers**  STRING |
| **whatsapps**  STRING |

### kobjects

The `kobjects` table contains information about Kustomer objects in the Kustomer app.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Kustomer documentation](https://dev.kustomer.com/v1/klasses/)  [Kustomer API method](https://dev.kustomer.com/v1/klasses/get-kobject "Opens in new tab: Kustomer API method") |

kobjects table schema

|  |
| --- |
| **created\_at**  STRING |
| **custom**  OBJECT This is a nested data structure:   - billing\_status\_str: STRING - comment\_txt: STRING - delighted\_link\_str: STRING - order\_created\_at: STRING - order\_number\_str: STRING - order\_updated\_at: STRING - purchase\_amount\_num: INTEGER - score\_num: INTEGER - shipping\_address\_str: STRING - shipping\_country\_str: STRING - shipping\_state\_str: STRING - shipping\_zip\_str: STRING - skus\_txt: STRING - special\_instructions\_str: STRING - tags\_str: STRING - total\_price\_num: NUMBER - total\_price\_str: STRING - updated\_at: STRING |
| **customer**  OBJECT This is a nested data structure:   - id: STRING - type: STRING |
| **description**  STRING |
| **external\_id**  STRING |
| **icon**  STRING |
| **id**  STRING |
| **klass**  OBJECT This is a nested data structure:   - id: STRING - type: STRING |
| **links**  OBJECT This is a nested data structure:   - self: STRING |
| **org**  OBJECT This is a nested data structure:   - type: STRING |
| **title**  STRING |
| **type**  STRING |
| **updated\_at**  STRING |

### messages

The `messages` table contains information about messages in the Kustomer app.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Kustomer documentation](https://dev.kustomer.com/v1/messages/)  [Kustomer API method](https://dev.kustomer.com/v1/messages/get-message "Opens in new tab: Kustomer API method") |

messages table schema

|  |
| --- |
| **created\_at**  STRING |
| **custom**  OBJECT This is a nested data structure:   - billing\_status\_str: STRING - comment\_txt: STRING - delighted\_link\_str: STRING - order\_created\_at: STRING - order\_number\_str: STRING - order\_updated\_at: STRING - purchase\_amount\_num: INTEGER - score\_num: INTEGER - shipping\_address\_str: STRING - shipping\_country\_str: STRING - shipping\_state\_str: STRING - shipping\_zip\_str: STRING - skus\_txt: STRING - special\_instructions\_str: STRING - tags\_str: STRING - total\_price\_num: NUMBER - total\_price\_str: STRING - updated\_at: STRING |
| **customer**  OBJECT This is a nested data structure:   - id: STRING - type: STRING |
| **description**  STRING |
| **external\_id**  STRING |
| **icon**  STRING |
| **id**  STRING |
| **images**  ARRAY This is a nested data structure. |
| **klass**  OBJECT This is a nested data structure:   - id: STRING - type: STRING |
| **links**  OBJECT This is a nested data structure:   - self: STRING |
| **org**  OBJECT This is a nested data structure:   - id: STRING - type: STRING |
| **tags**  ARRAY This is a nested data structure. |
| **title**  STRING |
| **type**  STRING |
| **updated\_at**  STRING |

### notes

The `notes` table contains information about notes in the Kustomer app.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Kustomer documentation](https://dev.kustomer.com/v1/notes/)  [Kustomer API method](https://dev.kustomer.com/v1/notes/get-notes "Opens in new tab: Kustomer API method") |

notes table schema

|  |
| --- |
| **body**  STRING |
| **conversation**  OBJECT This is a nested data structure:   - id: STRING - type: STRING |
| **created\_at**  DATE-TIME |
| **created\_by**  OBJECT This is a nested data structure:   - id: STRING - type: STRING |
| **customer**  OBJECT This is a nested data structure:   - id: STRING - type: STRING |
| **deleted**  BOOLEAN |
| **deleted\_at**  DATE-TIME |
| **deleted\_by**  OBJECT This is a nested data structure:   - id: STRING - type: STRING |
| **external\_id**  STRING |
| **id**  STRING |
| **imported\_at**  DATE-TIME |
| **links**  OBJECT This is a nested data structure:   - self: STRING |
| **modified\_at**  DATE-TIME |
| **modified\_by**  OBJECT This is a nested data structure:   - id: STRING - type: STRING |
| **org**  OBJECT This is a nested data structure:   - id: STRING - type: STRING |
| **type**  STRING |
| **updated\_at**  DATE-TIME |
| **user\_mentions**    ARRAY This is a nested data structure:   - id: STRING - type: STRING |

### shortcuts

The `shortcuts` table contains information about shortcuts in the Kustomer app.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Kustomer documentation](https://dev.kustomer.com/v1/shortcuts)  [Kustomer API method](https://dev.kustomer.com/v1/shortcuts/KaRhy9CmfHsmaG4gZ "Opens in new tab: Kustomer API method") |

shortcuts table schema

|  |
| --- |
| **conversation**  OBJECT This is a nested data structure:   - name: OBJECT, which is also a nested data structure.   - operator: STRING   - value: STRING - tags: OBJECT, which is also a nested data structure.   - operator: STRING   - value: STRING, which is also a nested data structure. |
| **created\_at**  DATE-TIME |
| **created\_by**  OBJECT This is a nested data structure:   - id: STRING - type: STRING |
| **deleted**  BOOLEAN |
| **draft**  OBJECT This is a nested data structure:   - text: STRING |
| **id**  STRING |
| **is\_private**  BOOLEAN |
| **links**  OBJECT This is a nested data structure:   - self: STRING |
| **modified\_at**  STRING |
| **modified\_by**  OBJECT This is a nested data structure:   - id: STRING - type: STRING |
| **name**  STRING |
| **org**  OBJECT This is a nested data structure:   - id: STRING - type: STRING |
| **payload**  OBJECT This is a nested data structure:   - text: STRING, which is also a nested data structure.   - blocks: ARRAY, which is also a nested data structure.     - data: OBJECT, which is also a nested data structure.     - depth: INTEGER     - entity\_ranges: ARRAY, which is also a nested data structure.       - key: INTEGER       - length: INTEGER       - offset: INTEGER     - inline\_style\_ranges: ARRAY, which is also a nested data structure.       - key: INTEGER       - length: INTEGER       - style: STRING     - key: STRING     - text: STRING     - type: STRING     >   - entity\_map: OBJECT, which is also a nested data structure.     - 0: OBJECT, which is also a nested data structure.       - data: OBJECT, which is also a nested data structure.         - fallback\_text: STRING         - key: STRING         - url: STRING       - mutability: STRING       - type: STRING     - 1: OBJECT, which is also a nested data structure.       - data: OBJECT, which is also a nested data structure.         - fallback\_text: STRING         - key: STRING         - url: STRING       - mutability: STRING       - type: STRING     - 2: OBJECT, which is also a nested data structure.       - data: OBJECT, which is also a nested data structure.         - url: STRING       - mutability: STRING       - type: STRING     - 3: OBJECT, which is also a nested data structure.       - data: OBJECT, which is also a nested data structure.         - url: STRING       - mutability: STRING       - type: STRING |
| **type**  STRING |
| **updated\_at**  DATE-TIME |

### tags

The `tags` table contains information about tags in the Kustomer app.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Kustomer documentation](https://dev.kustomer.com/v1/tags/)  [Kustomer API method](https://dev.kustomer.com/v1/tags/NWydnz3xaPBWCePQp "Opens in new tab: Kustomer API method") |

tags table schema

|  |
| --- |
| **color**  STRING |
| **created\_at**  DATE-TIME |
| **created\_by**  OBJECT This is a nested data structure:   - id: STRING - type: STRING |
| **deleted**  BOOLEAN |
| **id**  STRING |
| **links**  OBJECT This is a nested data structure:   - self: STRING |
| **modified\_at**  STRING |
| **modified\_by**  OBJECT This is a nested data structure:   - id: STRING - type: STRING |
| **name**  STRING |
| **org**  OBJECT This is a nested data structure:   - id: STRING - type: STRING |
| **type**  STRING |
| **updated\_at**  DATE-TIME |

### teams

The `teams` table contains information about teams in the Kustomer app.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Kustomer documentation](https://dev.kustomer.com/v1/teams/)  [Kustomer API method](https://dev.kustomer.com/v1/teams/get-team "Opens in new tab: Kustomer API method") |

teams table schema

|  |
| --- |
| **created\_at**  DATE-TIME |
| **created\_by**  OBJECT This is a nested data structure:   - id: STRING - type: STRING |
| **deleted**  BOOLEAN |
| **deleted\_at**  STRING |
| **deleted\_by**  OBJECT This is a nested data structure:   - id: STRING - type: STRING |
| **display\_name**  STRING |
| **icon**  STRING |
| **id**  STRING |
| **links**  OBJECT This is a nested data structure:   - self: STRING |
| **members**    ARRAY This is a nested data structure. |
| **modified\_at**  STRING |
| **modified\_by**  OBJECT This is a nested data structure:   - id: STRING - type: STRING |
| **name**  STRING |
| **org**  OBJECT This is a nested data structure:   - id: STRING - type: STRING |
| **role\_groups**    ARRAY This is a nested data structure. |
| **type**  STRING |
| **updated\_at**  DATE-TIME |

### users

The `users` table contains information about users in the Kustomer app.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Kustomer documentation](https://dev.kustomer.com/v1/users/)  [Kustomer API method](https://dev.kustomer.com/v1/users/get-user "Opens in new tab: Kustomer API method") |

users table schema

|  |
| --- |
| **avatar\_url**  STRING |
| **created\_at**  DATE-TIME |
| **created\_by**  OBJECT This is a nested data structure:   - id: STRING - type: STRING |
| **deleted\_at**  STRING |
| **display\_name**  STRING |
| **email**  STRING |
| **email\_signature**  STRING |
| **email\_verified\_at**  STRING |
| **first\_email\_verified\_at**  STRING |
| **id**  STRING |
| **links**  OBJECT This is a nested data structure:   - self: STRING |
| **mobile**  STRING |
| **modified\_at**  STRING |
| **modified\_by**  OBJECT This is a nested data structure:   - id: STRING - type: STRING |
| **name**  STRING |
| **org**  OBJECT This is a nested data structure:   - id: STRING - type: STRING |
| **password**  OBJECT This is a nested data structure:   - allow\_new: BOOLEAN - force\_new: BOOLEAN - updated\_at: DATE-TIME |
| **role\_groups**    ARRAY This is a nested data structure. |
| **roles**    ARRAY This is a nested data structure. |
| **type**  STRING |
| **updated\_at**  DATE-TIME |
| **user\_type**  STRING |
