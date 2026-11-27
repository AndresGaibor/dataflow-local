---
title: "Pendo"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Pendo-v2.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Pendo

Pendo is a SaaS platform that helps businesses improve product adoption, usage, and satisfaction by providing in-app guidance, communications, and analytics. You can use Pendo as a data source when landing or replicating data.

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To generate an integration key:

1. Make sure you have the Admin privileges in Pendo. You need them to create an integration key.
2. Log into your Pendo account as a user with Admin privileges.
3. Go tp Settings > Integrations > Integration Keys.
4. Click + Add Integration Key.
5. In Description field of the window that displays, enter a description. For example: `Qlik`.
6. Click Create.The integration key will display in the Key column:![Highlighted Key column and integration key in the Integration Keys tab of the Pendo web app](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/pendo-integration-key.png)
7. Copy the key.

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
| Period | Select the period from the drop-down list:   - Days: Data will be aggregated by day.- Hours: Data will be aggregated by hour. |
| X Pendo Integration Key | Pendo integration key. |
| App IDs | App IDs separated by a comma. Example: `1122, 2345`. |
| Include Anonymous Visitors | Select the check box if needed. This lets you collect data from visitors that have no assigned Visitor ID and counts toward your total monthly active users. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### accounts

The `accounts` table contains info about your customer accounts in Pendo.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | account\_id |
| **Replication Key** | lastupdated |
| **Useful links** | [Pendo documentation](https://engageapi.pendo.io/#12dd758f-1578-4eba-894c-0d6ea64f600a)  [Pendo API method](https://engageapi.pendo.io/#7c8479b8-3843-403c-94a9-04cbdf542db9 "Opens in new tab: Pendo API method") |

accounts table foreign keys

| Join accounts with | on |
| --- | --- |
| [events](#events) | ``` accounts.account_id = events.account_id ``` |
| [feature\_events](#feature-events) | ``` accounts.account_id = feature_events.account_id ``` |
| [guide\_events](#guide-events) | ``` accounts.account_id = guide_events.account_id ```  ``` accounts.account_id = guide_events.account_ids ``` |
| [page\_events](#page-events) | ``` accounts.account_id = page_events.account_id ``` |
| [poll\_events](#poll-events) | ``` accounts.account_id = poll_events.account_id ```  ``` accounts.account_id = poll_events.account_ids ``` |
| [track\_events](#track-events) | ``` accounts.account_id = track_events.account_id ``` |
| [visitors](#visitors) | ``` accounts.account_id = visitors.metadata_auto.accountid ```  ``` accounts.account_id = visitors.metadata_auto.accountids ``` |

accounts table schema

|  |
| --- |
| **account\_id**  STRING |
| **lastupdated**  DATE-TIME |
| **metadata\_auto**  OBJECT This is a nested data structure:   - **firstvisit**: DATE-TIME - **id**: STRING - **idhash**: INTEGER - **lastupdated**: DATE-TIME - **lastvisit**: DATE-TIME |
| **metadata\_custom**  OBJECT |

### events

The `events` table contains info about events recorded in your Pendo account.

**Note**: The **Period** setting you define during setup determine how this table is replicated, including the field used as a Replication Key. Refer to the [Replication section](#event-replication) for more info.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | account\_id  server  remote\_ip |
| **Useful links** | [Pendo documentation](https://engageapi.pendo.io/#3d10cfdb-c4b3-4a9c-8d67-dc250cab82ab)  [Pendo API method](https://engageapi.pendo.io/#7c8479b8-3843-403c-94a9-04cbdf542db9 "Opens in new tab: Pendo API method") |

events table foreign keys

| Join events with | on |
| --- | --- |
| [accounts](#accounts) | ``` events.account_id = accounts.account_id ``` |
| [feature\_events](#feature-events) | ``` events.account_id = feature_events.account_id ```  ``` events.app_id = feature_events.app_id ```  ``` events.feature_id = feature_events.feature_id ```  ``` events.visitor_id = feature_events.visitor_id ``` |
| [guide\_events](#guide-events) | ``` events.account_id = guide_events.account_id ```  ``` events.account_id = guide_events.account_ids ```  ``` events.app_id = guide_events.app_id ```  ``` events.visitor_id = guide_events.visitor_id ``` |
| [page\_events](#page-events) | ``` events.account_id = page_events.account_id ```  ``` events.app_id = page_events.app_id ```  ``` events.page_id = page_events.page_id ```  ``` events.visitor_id = page_events.visitor_id ``` |
| [poll\_events](#poll-events) | ``` events.account_id = poll_events.account_id ```  ``` events.account_id = poll_events.account_ids ```  ``` events.visitor_id = poll_events.visitor_id ``` |
| [track\_events](#track-events) | ``` events.account_id = track_events.account_id ```  ``` events.app_id = track_events.app_id ```  ``` events.visitor_id = track_events.visitor_id ``` |
| [visitors](#visitors) | ``` events.account_id = visitors.metadata_auto.accountid ```  ``` events.account_id = visitors.metadata_auto.accountids ```  ``` events.visitor_id = visitors.visitor_id ``` |
| [features](#features) | ``` events.app_id = features.created_by_user.app_id ```  ``` events.feature_id = features.id ```  ``` events.page_id = features.page_id ``` |
| [visitor\_history](#visitor-history) | ``` events.app_id = visitor_history.app_id ```  ``` events.feature_id = visitor_history.feature_id ```  ``` events.page_id = visitor_history.page_id ```  ``` events.visitor_id = visitor_history.visitor_id ``` |
| [guides](#guides) | ``` events.page_id = guides.steps.page_id ```  ``` events.visitor_id = guides.audience.select.visitor_id ``` |
| [pages](#pages) | ``` events.page_id = pages.id ``` |

events table schema

|  |
| --- |
| **account\_id**  STRING |
| **app\_id**  NUMBER |
| **day**  DATE-TIME |
| **feature\_id**  STRING |
| **hour**  DATE-TIME |
| **num\_events**  INTEGER |
| **num\_minutes**  INTEGER |
| **page\_id**  STRING |
| **parameters**  STRING |
| **remote\_ip**  STRING |
| **server**  STRING |
| **user\_agent**  STRING |
| **visitor\_id**  STRING |

### feature\_events

The `feature_events` table contains info about feature events recorded in your Pendo account.

**Note**: The **Period** setting you define during setup determine how this table is replicated, including the field used as a Replication Key. Refer to the [Replication section](#event-replication) for more info.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | account\_id  server  remote\_ip  visitor\_id  day  feature\_id  user\_agent |
| **Useful links** | [Pendo documentation](https://engageapi.pendo.io/#3d10cfdb-c4b3-4a9c-8d67-dc250cab82ab)  [Pendo API method](https://engageapi.pendo.io/#7c8479b8-3843-403c-94a9-04cbdf542db9 "Opens in new tab: Pendo API method") |

feature\_events table foreign keys

| Join feature\_events with | on |
| --- | --- |
| [accounts](#accounts) | ``` feature_events.account_id = accounts.account_id ``` |
| [events](#events) | ``` feature_events.account_id = events.account_id ```  ``` feature_events.app_id = events.app_id ```  ``` feature_events.feature_id = events.feature_id ```  ``` feature_events.visitor_id = events.visitor_id ``` |
| [guide\_events](#guide-events) | ``` feature_events.account_id = guide_events.account_id ```  ``` feature_events.account_id = guide_events.account_ids ```  ``` feature_events.app_id = guide_events.app_id ```  ``` feature_events.visitor_id = guide_events.visitor_id ``` |
| [page\_events](#page-events) | ``` feature_events.account_id = page_events.account_id ```  ``` feature_events.app_id = page_events.app_id ```  ``` feature_events.visitor_id = page_events.visitor_id ``` |
| [poll\_events](#poll-events) | ``` feature_events.account_id = poll_events.account_id ```  ``` feature_events.account_id = poll_events.account_ids ```  ``` feature_events.visitor_id = poll_events.visitor_id ``` |
| [track\_events](#track-events) | ``` feature_events.account_id = track_events.account_id ```  ``` feature_events.app_id = track_events.app_id ```  ``` feature_events.visitor_id = track_events.visitor_id ``` |
| [visitors](#visitors) | ``` feature_events.account_id = visitors.metadata_auto.accountid ```  ``` feature_events.account_id = visitors.metadata_auto.accountids ```  ``` feature_events.visitor_id = visitors.visitor_id ``` |
| [features](#features) | ``` feature_events.app_id = features.created_by_user.app_id ```  ``` feature_events.feature_id = features.id ``` |
| [visitor\_history](#visitor-history) | ``` feature_events.app_id = visitor_history.app_id ```  ``` feature_events.feature_id = visitor_history.feature_id ```  ``` feature_events.visitor_id = visitor_history.visitor_id ``` |
| [guides](#guides) | ``` feature_events.visitor_id = guides.audience.select.visitor_id ``` |

feature\_events table schema

|  |
| --- |
| **account\_id**  STRING |
| **app\_id**  NUMBER |
| **day**  DATE-TIME |
| **feature\_id**  STRING |
| **hour**  DATE-TIME |
| **num\_events**  INTEGER |
| **num\_minutes**  INTEGER |
| **parameters**  STRING |
| **remote\_ip**  STRING |
| **server**  STRING |
| **user\_agent**  STRING |
| **visitor\_id**  STRING |

### features

The `features` table contains info about app features listed in your Pendo account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | last\_updated\_at |
| **Useful links** | [Pendo documentation](https://engageapi.pendo.io/#b7ba5380-68c7-4c6a-bf17-50159e56a8d8)  [Pendo API method](https://engageapi.pendo.io/#7c8479b8-3843-403c-94a9-04cbdf542db9 "Opens in new tab: Pendo API method") |

features table foreign keys

| Join features with | on |
| --- | --- |
| [events](#events) | ``` features.created_by_user.app_id = events.app_id ```  ``` features.id = events.feature_id ```  ``` features.page_id = events.page_id ``` |
| [feature\_events](#feature-events) | ``` features.created_by_user.app_id = feature_events.app_id ```  ``` features.id = feature_events.feature_id ``` |
| [guide\_events](#guide-events) | ``` features.created_by_user.app_id = guide_events.app_id ``` |
| [page\_events](#page-events) | ``` features.created_by_user.app_id = page_events.app_id ```  ``` features.page_id = page_events.page_id ``` |
| [track\_events](#track-events) | ``` features.created_by_user.app_id = track_events.app_id ``` |
| [visitor\_history](#visitor-history) | ``` features.created_by_user.app_id = visitor_history.app_id ```  ``` features.id = visitor_history.feature_id ```  ``` features.page_id = visitor_history.page_id ``` |
| [pages](#pages) | ``` features.group.id = pages.group.id ```  ``` features.page_id = pages.id ```  ``` features.created_by_user.id = pages.created_by_user.id ```  ``` features.group.created_by_user.id = pages.created_by_user.id ```  ``` features.group.last_updated_by_user.id = pages.created_by_user.id ```  ``` features.last_updated_by_user.id = pages.created_by_user.id ```  ``` features.created_by_user.id = pages.group.created_by_user.id ```  ``` features.group.created_by_user.id = pages.group.created_by_user.id ```  ``` features.group.last_updated_by_user.id = pages.group.created_by_user.id ```  ``` features.last_updated_by_user.id = pages.group.created_by_user.id ```  ``` features.created_by_user.id = pages.group.last_updated_by_user.id ```  ``` features.group.created_by_user.id = pages.group.last_updated_by_user.id ```  ``` features.group.last_updated_by_user.id = pages.group.last_updated_by_user.id ```  ``` features.last_updated_by_user.id = pages.group.last_updated_by_user.id ```  ``` features.created_by_user.id = pages.last_updated_by_user.id ```  ``` features.group.created_by_user.id = pages.last_updated_by_user.id ```  ``` features.group.last_updated_by_user.id = pages.last_updated_by_user.id ```  ``` features.last_updated_by_user.id = pages.last_updated_by_user.id ``` |
| [track\_types](#track-types) | ``` features.group.id = track_types.group.id ```  ``` features.created_by_user.id = track_types.created_by_user.id ```  ``` features.group.created_by_user.id = track_types.created_by_user.id ```  ``` features.group.last_updated_by_user.id = track_types.created_by_user.id ```  ``` features.last_updated_by_user.id = track_types.created_by_user.id ```  ``` features.created_by_user.id = track_types.last_updated_by_user.id ```  ``` features.group.created_by_user.id = track_types.last_updated_by_user.id ```  ``` features.group.last_updated_by_user.id = track_types.last_updated_by_user.id ```  ``` features.last_updated_by_user.id = track_types.last_updated_by_user.id ``` |
| [guides](#guides) | ``` features.page_id = guides.steps.page_id ```  ``` features.created_by_user.id = guides.created_by_user.id ```  ``` features.group.created_by_user.id = guides.created_by_user.id ```  ``` features.group.last_updated_by_user.id = guides.created_by_user.id ```  ``` features.last_updated_by_user.id = guides.created_by_user.id ```  ``` features.created_by_user.id = guides.last_updated_by_user.id ```  ``` features.group.created_by_user.id = guides.last_updated_by_user.id ```  ``` features.group.last_updated_by_user.id = guides.last_updated_by_user.id ```  ``` features.last_updated_by_user.id = guides.last_updated_by_user.id ``` |

features table schema

|  |
| --- |
| **app\_id**  NUMBER |
| **color**  STRING |
| **created\_at**  DATE-TIME |
| **created\_by\_user**  OBJECT This is a nested data structure:   - **app\_id**: NUMBER - **app\_wide**: BOOLEAN - **event\_property\_configurations**: ARRAY, which is also a nested data structure. - **first**: STRING - **id**: STRING - **is\_core\_event**: BOOLEAN - **last**: STRING - **role**: INTEGER - **user\_type**: STRING - **username**: STRING - **valid\_through**: NUMBER |
| **dirty**  BOOLEAN |
| **element\_path\_rules**  ARRAY |
| **group**  OBJECT This is a nested data structure:   - **color**: STRING - **created\_at**: DATE-TIME - **created\_by\_user**: OBJECT, which is also a nested data structure.   - **first**: STRING   - **id**: STRING   - **last**: STRING   - **role**: INTEGER   - **type**: STRING   - **username**: STRING - **description**: STRING - **id**: STRING - **last\_updated\_at**: DATE-TIME - **last\_updated\_by\_user**: OBJECT, which is also a nested data structure.   - **first**: STRING   - **id**: STRING   - **last**: STRING   - **role**: INTEGER   - **username**: STRING - **length**: INTEGER - **name**: STRING |
| **id**  STRING |
| **kind**  STRING |
| **last\_updated\_at**  DATE-TIME |
| **last\_updated\_by\_user**  OBJECT This is a nested data structure:   - **first**: STRING - **id**: STRING - **last**: STRING - **role**: INTEGER - **type**: STRING - **username**: STRING |
| **name**  STRING |
| **page\_id**  STRING |
| **root\_version\_id**  STRING |
| **stable\_version\_id**  STRING |

### guide\_events

The `guide_events` table contains info about guide events recorded in your Pendo account.

**Note**: The **Period** setting you define during setup determine how this table is replicated, including the field used as a Replication Key. Refer to the [Replication section](#event-replication) for more info.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | account\_id  browser\_time  guide\_id  guide\_step\_id  remote\_ip  type  url  visitor\_id |
| **Replication Key** | browser\_time |
| **Useful links** | [Pendo documentation](https://engageapi.pendo.io/#3d10cfdb-c4b3-4a9c-8d67-dc250cab82ab)  [Pendo API method](https://engageapi.pendo.io/#7c8479b8-3843-403c-94a9-04cbdf542db9 "Opens in new tab: Pendo API method") |

guide\_events table foreign keys

| Join guide\_events with | on |
| --- | --- |
| [accounts](#accounts) | ``` guide_events.account_id = accounts.account_id ```  ``` guide_events.account_ids = accounts.account_id ``` |
| [events](#events) | ``` guide_events.account_id = events.account_id ```  ``` guide_events.account_ids = events.account_id ```  ``` guide_events.app_id = events.app_id ```  ``` guide_events.visitor_id = events.visitor_id ``` |
| [feature\_events](#feature-events) | ``` guide_events.account_id = feature_events.account_id ```  ``` guide_events.account_ids = feature_events.account_id ```  ``` guide_events.app_id = feature_events.app_id ```  ``` guide_events.visitor_id = feature_events.visitor_id ``` |
| [page\_events](#page-events) | ``` guide_events.account_id = page_events.account_id ```  ``` guide_events.account_ids = page_events.account_id ```  ``` guide_events.app_id = page_events.app_id ```  ``` guide_events.visitor_id = page_events.visitor_id ``` |
| [poll\_events](#poll-events) | ``` guide_events.account_id = poll_events.account_id ```  ``` guide_events.account_ids = poll_events.account_id ```  ``` guide_events.account_id = poll_events.account_ids ```  ``` guide_events.account_ids = poll_events.account_ids ```  ``` guide_events.guide_id = poll_events.guide_id ```  ``` guide_events.poll_id = poll_events.poll_id ```  ``` guide_events.visitor_id = poll_events.visitor_id ``` |
| [track\_events](#track-events) | ``` guide_events.account_id = track_events.account_id ```  ``` guide_events.account_ids = track_events.account_id ```  ``` guide_events.app_id = track_events.app_id ```  ``` guide_events.visitor_id = track_events.visitor_id ``` |
| [visitors](#visitors) | ``` guide_events.account_id = visitors.metadata_auto.accountid ```  ``` guide_events.account_ids = visitors.metadata_auto.accountid ```  ``` guide_events.account_id = visitors.metadata_auto.accountids ```  ``` guide_events.account_ids = visitors.metadata_auto.accountids ```  ``` guide_events.visitor_id = visitors.visitor_id ``` |
| [features](#features) | ``` guide_events.app_id = features.created_by_user.app_id ``` |
| [visitor\_history](#visitor-history) | ``` guide_events.app_id = visitor_history.app_id ```  ``` guide_events.guide_id = visitor_history.guide_id ```  ``` guide_events.visitor_id = visitor_history.visitor_id ``` |
| [guides](#guides) | ``` guide_events.guide_id = guides.id ```  ``` guide_events.guide_id = guides.steps.guide_id ```  ``` guide_events.visitor_id = guides.audience.select.visitor_id ``` |

guide\_events table schema

|  |
| --- |
| **account\_id**  STRING |
| **account\_ids**    ARRAY |
| **app\_id**  NUMBER |
| **browser\_time**  DATE-TIME |
| **country**  STRING |
| **guide\_id**  STRING |
| **guide\_step\_id**  STRING |
| **latitude**  NUMBER |
| **load\_time**  INTEGER |
| **longitude**  NUMBER |
| **poll\_id**  STRING |
| **poll\_response**  STRING |
| **region**  STRING |
| **remote\_ip**  STRING |
| **server\_name**  STRING |
| **type**  STRING |
| **url**  STRING |
| **user\_agent**  STRING |
| **visitor\_id**  STRING |

### guides

The `guides` table contains info about the guides in your Pendo account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | last\_updated\_at |
| **Useful links** | [Pendo API method](https://engageapi.pendo.io/#7c8479b8-3843-403c-94a9-04cbdf542db9 "Opens in new tab: Pendo API method") |

guides table foreign keys

| Join guides with | on |
| --- | --- |
| [guide\_events](#guide-events) | ``` guides.id = guide_events.guide_id ```  ``` guides.steps.guide_id = guide_events.guide_id ```  ``` guides.audience.select.visitor_id = guide_events.visitor_id ``` |
| [poll\_events](#poll-events) | ``` guides.id = poll_events.guide_id ```  ``` guides.steps.guide_id = poll_events.guide_id ```  ``` guides.audience.select.visitor_id = poll_events.visitor_id ``` |
| [visitor\_history](#visitor-history) | ``` guides.id = visitor_history.guide_id ```  ``` guides.steps.guide_id = visitor_history.guide_id ```  ``` guides.steps.id = visitor_history.guide_id ```  ``` guides.steps.page_id = visitor_history.page_id ```  ``` guides.audience.select.visitor_id = visitor_history.visitor_id ``` |
| [events](#events) | ``` guides.steps.page_id = events.page_id ```  ``` guides.audience.select.visitor_id = events.visitor_id ``` |
| [features](#features) | ``` guides.steps.page_id = features.page_id ```  ``` guides.created_by_user.id = features.created_by_user.id ```  ``` guides.last_updated_by_user.id = features.created_by_user.id ```  ``` guides.created_by_user.id = features.group.created_by_user.id ```  ``` guides.last_updated_by_user.id = features.group.created_by_user.id ```  ``` guides.created_by_user.id = features.group.last_updated_by_user.id ```  ``` guides.last_updated_by_user.id = features.group.last_updated_by_user.id ```  ``` guides.created_by_user.id = features.last_updated_by_user.id ```  ``` guides.last_updated_by_user.id = features.last_updated_by_user.id ``` |
| [page\_events](#page-events) | ``` guides.steps.page_id = page_events.page_id ```  ``` guides.audience.select.visitor_id = page_events.visitor_id ``` |
| [pages](#pages) | ``` guides.steps.page_id = pages.id ```  ``` guides.created_by_user.id = pages.created_by_user.id ```  ``` guides.last_updated_by_user.id = pages.created_by_user.id ```  ``` guides.created_by_user.id = pages.group.created_by_user.id ```  ``` guides.last_updated_by_user.id = pages.group.created_by_user.id ```  ``` guides.created_by_user.id = pages.group.last_updated_by_user.id ```  ``` guides.last_updated_by_user.id = pages.group.last_updated_by_user.id ```  ``` guides.created_by_user.id = pages.last_updated_by_user.id ```  ``` guides.last_updated_by_user.id = pages.last_updated_by_user.id ``` |
| [track\_types](#track-types) | ``` guides.created_by_user.id = track_types.created_by_user.id ```  ``` guides.last_updated_by_user.id = track_types.created_by_user.id ```  ``` guides.created_by_user.id = track_types.last_updated_by_user.id ```  ``` guides.last_updated_by_user.id = track_types.last_updated_by_user.id ``` |
| [feature\_events](#feature-events) | ``` guides.audience.select.visitor_id = feature_events.visitor_id ``` |
| [track\_events](#track-events) | ``` guides.audience.select.visitor_id = track_events.visitor_id ``` |
| [visitors](#visitors) | ``` guides.audience.select.visitor_id = visitors.visitor_id ``` |

guides table schema

|  |
| --- |
| **app\_id**  NUMBER |
| **attributes**  OBJECT This is a nested data structure: **badge**, OBJECT, which is alaso a nested data structure.   - **can\_change\_badge\_color**: BOOLEAN - **color**: STRING - **height**: INTEGER - **image\_url**: STRING - **is\_only\_show\_once**: BOOLEAN - **name**: STRING - **offsets**: OBJECT, which is also a nested data structure.   - **left**: INTEGER   - **right**: INTEGER   - **top**: INTEGER - **position**: STRING - **show\_on\_event**: STRING - **use\_hover**: STRING - **width**: INTEGER - **device**: OBJECT, which is also a nested data structure.   - **type**: STRING - **priority**: INTEGER - **type**: STRING |
| **audience**  ARRAY This is a nested data structure:   - **identified**: STRING - **select**: OBJECT, which is also a nested data structure.   - **visitor\_id**: STRING - **source**: OBJECT, which is also a nested data structure.   - **visitors**: STRING |
| **created\_at**  DATE-TIME |
| **created\_by\_user**  OBJECT This is a nested data structure:   - **first**: STRING - **id**: STRING - **last**: STRING - **role**: INTEGER - **username**: STRING |
| **id**  STRING |
| **is\_multi\_step**  BOOLEAN |
| **kind**  STRING |
| **last\_updated\_at**  DATE-TIME |
| **last\_updated\_by\_user**  OBJECT This is a nested data structure:   - **first**: STRING - **id**: STRING - **last**: STRING - **role**: INTEGER - **username**: STRING |
| **launch\_method**  STRING |
| **name**  STRING |
| **published\_at**  DATE-TIME |
| **reset\_at**  DATE-TIME |
| **root\_version\_id**  STRING |
| **stable\_version\_id**  STRING |
| **state**  STRING |
| **steps**  ARRAY This is a nested data structure:   - **advance\_method**: STRING - **attributes**: OBJECT, which is also a nested data structure.   - **auto\_height**: BOOLEAN   - **css**: STRING   - **height**: INTEGER   - **width**: INTEGER - **content\_type**: STRING - **content\_url**: STRING - **content\_url\_css**: STRING - **content\_url\_js**: STRING - **element\_path\_rule**: STRING - **guide\_id**: STRING - **id**: STRING - **last\_updated\_at**: DATE-TIME - **page\_id**: STRING - **rank**: INTEGER - **regex\_url\_rule**: STRING - **reset\_at**: DATE-TIME - **type**: STRING |

### metadata\_accounts

The `metadata_accounts` table contains info about the metadata schema used for account objects in your Pendo account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Useful links** | [Pendo documentation](https://engageapi.pendo.io/#a0064303-3aa9-41ef-a7bc-2e43c0ccd88e)  [Pendo API method](https://engageapi.pendo.io/#a59ff30a-d29c-430c-b28a-fa64d199a9b9 "Opens in new tab: Pendo API method") |

metadata\_accounts table schema

|  |
| --- |
| **auto**  OBJECT This is a nested data structure:   - **firstvisit**: OBJECT, which is also a nested data structure.   - **dirty**: BOOLEAN   - **display\_name**: STRING   - **element\_format**: STRING   - **element\_type**: STRING   - **is\_calculated**: BOOLEAN   - **is\_deleted**: BOOLEAN   - **is\_hidden**: BOOLEAN   - **is\_per\_app**: BOOLEAN   - **never\_index**: BOOLEAN   - **type**: STRING - **id**: OBJECT, which is also a nested data structure.   - **dirty**: BOOLEAN   - **display\_name**: STRING   - **element\_format**: STRING   - **element\_type**: STRING   - **is\_calculated**: BOOLEAN   - **is\_deleted**: BOOLEAN   - **is\_hidden**: BOOLEAN   - **is\_per\_app**: BOOLEAN   - **never\_index**: BOOLEAN   - **type**: STRING - **lastvisit**: OBJECT, which is also a nested data structure.   - **dirty**: BOOLEAN   - **display\_name**: STRING   - **element\_format**: STRING   - **element\_type**: STRING   - **is\_calculated**: BOOLEAN   - **is\_deleted**: BOOLEAN   - **is\_hidden**: BOOLEAN   - **is\_per\_app**: BOOLEAN   - **never\_index**: BOOLEAN   - **type**: STRING |

### metadata\_visitors

The `metadata_visitors` table contains info about the metadata schema used for visitor objects in your Pendo account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Useful links** | [Pendo documentation](https://engageapi.pendo.io/#a0064303-3aa9-41ef-a7bc-2e43c0ccd88e)  [Pendo API method](https://engageapi.pendo.io/#a59ff30a-d29c-430c-b28a-fa64d199a9b9 "Opens in new tab: Pendo API method") |

metadata\_visitors table schema

|  |
| --- |
| **agent**  OBJECT This is a nested data structure:  - **language**, OBJECT, which is also a nested data structure:   - **dirty**: OBJECT   - **display\_name**: STRING   - **element\_format**: STRING   - **element\_type**: STRING   - **is\_calculated**: BOOLEAN   - **is\_deleted**: BOOLEAN   - **is\_hidden**: BOOLEAN   - **is\_per\_app**: BOOLEAN   - **never\_index**: BOOLEAN   - **type**: STRING - **auto**, OBJECT, which is also a nested data structure:   - **accountid**: OBJECT, which is also a nested data structure:     - **dirty**: OBJECT     - **display\_name**: STRING     - **element\_format**: STRING     - **element\_type**: STRING     - **is\_calculated**: BOOLEAN     - **is\_deleted**: BOOLEAN     - **is\_hidden**: BOOLEAN     - **is\_per\_app**: BOOLEAN     - **never\_index**: BOOLEAN     - **type**: STRING   - **accountids**, OBJECT, which is also a nested data structure:     - **display\_name**: STRING     - **element\_format**: STRING     - **element\_type**: STRING     - **is\_calculated**: BOOLEAN     - **is\_deleted**: BOOLEAN     - **is\_hidden**: BOOLEAN     - **is\_per\_app**: BOOLEAN     - **never\_index**: BOOLEAN     - **type**: STRING   - **firstvisit**, OBJECT, which is also a nested data structure:     - **display\_name**: STRING     - **element\_format**: STRING     - **element\_type**: STRING     - **is\_calculated**: BOOLEAN     - **is\_deleted**: BOOLEAN     - **is\_hidden**: BOOLEAN     - **is\_per\_app**: BOOLEAN     - **never\_index**: BOOLEAN     - **type**: STRING   - **id**, OBJECT, which is also a nested data structure:     - **display\_name**: STRING     - **element\_format**: STRING     - **element\_type**: STRING     - **is\_calculated**: BOOLEAN     - **is\_deleted**: BOOLEAN     - **is\_hidden**: BOOLEAN     - **is\_per\_app**: BOOLEAN     - **never\_index**: BOOLEAN     - **type**: STRING   - **lastbrowsername**, OBJECT, which is also a nested data structure:     - **display\_name**: STRING     - **element\_format**: STRING     - **element\_type**: STRING     - **is\_calculated**: BOOLEAN     - **is\_deleted**: BOOLEAN     - **is\_hidden**: BOOLEAN     - **is\_per\_app**: BOOLEAN     - **never\_index**: BOOLEAN     - **type**: STRING   - **lastbrowserversion**, OBJECT, which is also a nested data structure:     - **display\_name**: STRING     - **element\_format**: STRING     - **element\_type**: STRING     - **is\_calculated**: BOOLEAN     - **is\_deleted**: BOOLEAN     - **is\_hidden**: BOOLEAN     - **is\_per\_app**: BOOLEAN     - **never\_index**: BOOLEAN     - **type**: STRING   - **lastoperatingsystem**, OBJECT, which is also a nested data structure:     - **display\_name**: STRING     - **element\_format**: STRING     - **element\_type**: STRING     - **is\_calculated**: BOOLEAN     - **is\_deleted**: BOOLEAN     - **is\_hidden**: BOOLEAN     - **is\_per\_app**: BOOLEAN     - **never\_index**: BOOLEAN     - **type**: STRING   - **lastservername**, OBJECT, which is also a nested data structure:     - **display\_name**: STRING     - **element\_format**: STRING     - **element\_type**: STRING     - **is\_calculated**: BOOLEAN     - **is\_deleted**: BOOLEAN     - **is\_hidden**: BOOLEAN     - **is\_per\_app**: BOOLEAN     - **never\_index**: BOOLEAN     - **type**: STRING   - **lastvisit**, OBJECT, which is also a nested data structure:     - **display\_name**: STRING     - **element\_format**: STRING     - **element\_type**: STRING     - **is\_calculated**: BOOLEAN     - **is\_deleted**: BOOLEAN     - **is\_hidden**: BOOLEAN     - **is\_per\_app**: BOOLEAN     - **never\_index**: BOOLEAN     - **type**: STRING- **pendo**, OBJECT, which is also a nested data structure:     - **designerenabled**: OBJECT       - **display\_name**: STRING       - **element\_format**: STRING       - **element\_type**: STRING       - **is\_calculated**: BOOLEAN       - **is\_deleted**: BOOLEAN       - **is\_hidden**: BOOLEAN       - **is\_per\_app**: BOOLEAN       - **never\_index**: BOOLEAN       - **type**: STRING |

### page\_events

The `page_events` table contains info about page events recorded in your Pendo account.

**Note**: The **Period** setting you define during setup determine how this table is replicated, including the field used as a Replication Key. Refer to the [Replication section](#event-replication) for more info.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | account\_id  server  remote\_ip  visitor\_id  day  page\_id  user\_agent |
| **Useful links** | [Pendo documentation](https://engageapi.pendo.io/#3d10cfdb-c4b3-4a9c-8d67-dc250cab82ab)  [Pendo API method](https://engageapi.pendo.io/#7c8479b8-3843-403c-94a9-04cbdf542db9 "Opens in new tab: Pendo API method") |

page\_events table foreign keys

| Join page\_events with | on |
| --- | --- |
| [accounts](#accounts) | ``` page_events.account_id = accounts.account_id ``` |
| [events](#events) | ``` page_events.account_id = events.account_id ```  ``` page_events.app_id = events.app_id ```  ``` page_events.page_id = events.page_id ```  ``` page_events.visitor_id = events.visitor_id ``` |
| [feature\_events](#feature-events) | ``` page_events.account_id = feature_events.account_id ```  ``` page_events.app_id = feature_events.app_id ```  ``` page_events.visitor_id = feature_events.visitor_id ``` |
| [guide\_events](#guide-events) | ``` page_events.account_id = guide_events.account_id ```  ``` page_events.account_id = guide_events.account_ids ```  ``` page_events.app_id = guide_events.app_id ```  ``` page_events.visitor_id = guide_events.visitor_id ``` |
| [poll\_events](#poll-events) | ``` page_events.account_id = poll_events.account_id ```  ``` page_events.account_id = poll_events.account_ids ```  ``` page_events.visitor_id = poll_events.visitor_id ``` |
| [track\_events](#track-events) | ``` page_events.account_id = track_events.account_id ```  ``` page_events.app_id = track_events.app_id ```  ``` page_events.visitor_id = track_events.visitor_id ``` |
| [visitors](#visitors) | ``` page_events.account_id = visitors.metadata_auto.accountid ```  ``` page_events.account_id = visitors.metadata_auto.accountids ```  ``` page_events.visitor_id = visitors.visitor_id ``` |
| [features](#features) | ``` page_events.app_id = features.created_by_user.app_id ```  ``` page_events.page_id = features.page_id ``` |
| [visitor\_history](#visitor-history) | ``` page_events.app_id = visitor_history.app_id ```  ``` page_events.page_id = visitor_history.page_id ```  ``` page_events.visitor_id = visitor_history.visitor_id ``` |
| [guides](#guides) | ``` page_events.page_id = guides.steps.page_id ```  ``` page_events.visitor_id = guides.audience.select.visitor_id ``` |
| [pages](#pages) | ``` page_events.page_id = pages.id ``` |

page\_events table schema

|  |
| --- |
| **account\_id**  STRING |
| **app\_id**  NUMBER |
| **day**  DATE-TIME |
| **hour**  DATE-TIME |
| **num\_events**  INTEGER |
| **num\_minutes**  INTEGER |
| **page\_id**  STRING |
| **parameters**  STRING |
| **remote\_ip**  STRING |
| **server**  STRING |
| **user\_agent**  STRING |
| **visitor\_id**  STRING |

### pages

The `pages` table contains info about specific pages in your Pendo app.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | last\_updated\_at |
| **Useful links** | [Pendo documentation](https://engageapi.pendo.io/#e7ef2d55-8ae8-46a5-b36e-1197fb3d9c3a)  [Pendo API method](https://engageapi.pendo.io/#7c8479b8-3843-403c-94a9-04cbdf542db9 "Opens in new tab: Pendo API method") |

pages table foreign keys

| Join pages with | on |
| --- | --- |
| [features](#features) | ``` pages.group.id = features.group.id ```  ``` pages.id = features.page_id ```  ``` pages.created_by_user.id = features.created_by_user.id ```  ``` pages.group.created_by_user.id = features.created_by_user.id ```  ``` pages.group.last_updated_by_user.id = features.created_by_user.id ```  ``` pages.last_updated_by_user.id = features.created_by_user.id ```  ``` pages.created_by_user.id = features.group.created_by_user.id ```  ``` pages.group.created_by_user.id = features.group.created_by_user.id ```  ``` pages.group.last_updated_by_user.id = features.group.created_by_user.id ```  ``` pages.last_updated_by_user.id = features.group.created_by_user.id ```  ``` pages.created_by_user.id = features.group.last_updated_by_user.id ```  ``` pages.group.created_by_user.id = features.group.last_updated_by_user.id ```  ``` pages.group.last_updated_by_user.id = features.group.last_updated_by_user.id ```  ``` pages.last_updated_by_user.id = features.group.last_updated_by_user.id ```  ``` pages.created_by_user.id = features.last_updated_by_user.id ```  ``` pages.group.created_by_user.id = features.last_updated_by_user.id ```  ``` pages.group.last_updated_by_user.id = features.last_updated_by_user.id ```  ``` pages.last_updated_by_user.id = features.last_updated_by_user.id ``` |
| [track\_types](#track-types) | ``` pages.group.id = track_types.group.id ```  ``` pages.created_by_user.id = track_types.created_by_user.id ```  ``` pages.group.created_by_user.id = track_types.created_by_user.id ```  ``` pages.group.last_updated_by_user.id = track_types.created_by_user.id ```  ``` pages.last_updated_by_user.id = track_types.created_by_user.id ```  ``` pages.created_by_user.id = track_types.last_updated_by_user.id ```  ``` pages.group.created_by_user.id = track_types.last_updated_by_user.id ```  ``` pages.group.last_updated_by_user.id = track_types.last_updated_by_user.id ```  ``` pages.last_updated_by_user.id = track_types.last_updated_by_user.id ``` |
| [events](#events) | ``` pages.id = events.page_id ``` |
| [guides](#guides) | ``` pages.id = guides.steps.page_id ```  ``` pages.created_by_user.id = guides.created_by_user.id ```  ``` pages.group.created_by_user.id = guides.created_by_user.id ```  ``` pages.group.last_updated_by_user.id = guides.created_by_user.id ```  ``` pages.last_updated_by_user.id = guides.created_by_user.id ```  ``` pages.created_by_user.id = guides.last_updated_by_user.id ```  ``` pages.group.created_by_user.id = guides.last_updated_by_user.id ```  ``` pages.group.last_updated_by_user.id = guides.last_updated_by_user.id ```  ``` pages.last_updated_by_user.id = guides.last_updated_by_user.id ``` |
| [page\_events](#page-events) | ``` pages.id = page_events.page_id ``` |
| [visitor\_history](#visitor-history) | ``` pages.id = visitor_history.page_id ``` |

pages table schema

|  |
| --- |
| **app\_id**  NUMBER |
| **color**  STRING |
| **created\_at**  DATE-TIME |
| **created\_by\_user**  OBJECT This is a nested data structure:   - **first**: STRING - **id**: STRING - **last**: STRING - **role**: INTEGER - **username**: INTEGER |
| **dirty**  BOOLEAN |
| **group**  OBJECT This is a nested data structure:   - **color**: STRING - **created\_at**: DATE-TIME - **created\_by\_user**: OBJECT, which is also a nested data structure:   - **first**: STRING   - **id**: STRING   - **last**: STRING   - **role**: INTEGER   - **username**: STRING - **description**: STRING - **id**: STRING - **last\_updated\_at**: DATE-TIME - **last\_updated\_by\_user**: OBJECT, which is also a nested data structure:   - **first**: STRING   - **id**: STRING   - **last**: STRING   - **role**: INTEGER   - **username**: STRING - **length**: INTEGER - **name**: STRING |
| **id**  STRING |
| **kind**  STRING |
| **last\_updated\_at**  DATE-TIME |
| **last\_updated\_by\_user**  OBJECT This is a nested data structure:   - **first**: STRING - **id**: STRING - **last**: STRING - **role**: INTEGER - **username**: STRING |
| **name**  STRING |
| **root\_version\_id**  STRING |
| **rules**  ARRAY This is a nested data structure:   - **designer\_hint**: STRING - **parsed\_rule**: STRING - **rule**: STRING |
| **stable\_version\_id**  STRING |

### poll\_events

The `poll_events` table contains info about poll events recorded in your Pendo account.

**Note**: The **Period** setting you define during setup determine how this table is replicated, including the field used as a Replication Key. Refer to the [Replication section](#event-replication) for more info.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | account\_id  remote\_ip  visitor\_id  browser\_time  poll\_id |
| **Replication Key** | browser\_time |
| **Useful links** | [Pendo documentation](https://engageapi.pendo.io/#3d10cfdb-c4b3-4a9c-8d67-dc250cab82ab)  [Pendo API method](https://engageapi.pendo.io/#7c8479b8-3843-403c-94a9-04cbdf542db9 "Opens in new tab: Pendo API method") |

poll\_events table foreign keys

| Join poll\_events with | on |
| --- | --- |
| [accounts](#accounts) | ``` poll_events.account_id = accounts.account_id ```  ``` poll_events.account_ids = accounts.account_id ``` |
| [events](#events) | ``` poll_events.account_id = events.account_id ```  ``` poll_events.account_ids = events.account_id ```  ``` poll_events.visitor_id = events.visitor_id ``` |
| [feature\_events](#feature-events) | ``` poll_events.account_id = feature_events.account_id ```  ``` poll_events.account_ids = feature_events.account_id ```  ``` poll_events.visitor_id = feature_events.visitor_id ``` |
| [guide\_events](#guide-events) | ``` poll_events.account_id = guide_events.account_id ```  ``` poll_events.account_ids = guide_events.account_id ```  ``` poll_events.account_id = guide_events.account_ids ```  ``` poll_events.account_ids = guide_events.account_ids ```  ``` poll_events.guide_id = guide_events.guide_id ```  ``` poll_events.poll_id = guide_events.poll_id ```  ``` poll_events.visitor_id = guide_events.visitor_id ``` |
| [page\_events](#page-events) | ``` poll_events.account_id = page_events.account_id ```  ``` poll_events.account_ids = page_events.account_id ```  ``` poll_events.visitor_id = page_events.visitor_id ``` |
| [track\_events](#track-events) | ``` poll_events.account_id = track_events.account_id ```  ``` poll_events.account_ids = track_events.account_id ```  ``` poll_events.visitor_id = track_events.visitor_id ``` |
| [visitors](#visitors) | ``` poll_events.account_id = visitors.metadata_auto.accountid ```  ``` poll_events.account_ids = visitors.metadata_auto.accountid ```  ``` poll_events.account_id = visitors.metadata_auto.accountids ```  ``` poll_events.account_ids = visitors.metadata_auto.accountids ```  ``` poll_events.visitor_id = visitors.visitor_id ``` |
| [guides](#guides) | ``` poll_events.guide_id = guides.id ```  ``` poll_events.guide_id = guides.steps.guide_id ```  ``` poll_events.visitor_id = guides.audience.select.visitor_id ``` |
| [visitor\_history](#visitor-history) | ``` poll_events.guide_id = visitor_history.guide_id ```  ``` poll_events.visitor_id = visitor_history.visitor_id ``` |

poll\_events table schema

|  |
| --- |
| **account\_id**  STRING |
| **account\_ids**    ARRAY |
| **app\_id**  NUMBER |
| **browser\_time**  DATE-TIME |
| **country**  STRING |
| **guide\_id**  STRING |
| **latitude**  NUMBER |
| **load\_time**  INTEGER |
| **longitude**  NUMBER |
| **poll\_id**  STRING |
| **poll\_response**  STRING |
| **region**  STRING |
| **remote\_ip**  STRING |
| **server\_name**  STRING |
| **type**  STRING |
| **user\_agent**  STRING |
| **visitor\_id**  STRING |

### track\_events

The `track_events` table contains info about the track events recorded in your Pendo account.

**Note**: The **Period** setting you define during setup determine how this table is replicated, including the field used as a Replication Key. Refer to the [Replication section](#event-replication) for more info.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | account\_id  remote\_ip  server  visitor\_id  day  track\_type\_id  user\_agent |
| **Useful links** | [Pendo documentation](https://engageapi.pendo.io/#2757f228-ca94-4075-a840-b1fafd6d43b2)  [Pendo API method](https://engageapi.pendo.io/#7c8479b8-3843-403c-94a9-04cbdf542db9 "Opens in new tab: Pendo API method") |

track\_events table foreign keys

| Join track\_events with | on |
| --- | --- |
| [accounts](#accounts) | ``` track_events.account_id = accounts.account_id ``` |
| [events](#events) | ``` track_events.account_id = events.account_id ```  ``` track_events.app_id = events.app_id ```  ``` track_events.visitor_id = events.visitor_id ``` |
| [feature\_events](#feature-events) | ``` track_events.account_id = feature_events.account_id ```  ``` track_events.app_id = feature_events.app_id ```  ``` track_events.visitor_id = feature_events.visitor_id ``` |
| [guide\_events](#guide-events) | ``` track_events.account_id = guide_events.account_id ```  ``` track_events.account_id = guide_events.account_ids ```  ``` track_events.app_id = guide_events.app_id ```  ``` track_events.visitor_id = guide_events.visitor_id ``` |
| [page\_events](#page-events) | ``` track_events.account_id = page_events.account_id ```  ``` track_events.app_id = page_events.app_id ```  ``` track_events.visitor_id = page_events.visitor_id ``` |
| [poll\_events](#poll-events) | ``` track_events.account_id = poll_events.account_id ```  ``` track_events.account_id = poll_events.account_ids ```  ``` track_events.visitor_id = poll_events.visitor_id ``` |
| [visitors](#visitors) | ``` track_events.account_id = visitors.metadata_auto.accountid ```  ``` track_events.account_id = visitors.metadata_auto.accountids ```  ``` track_events.visitor_id = visitors.visitor_id ``` |
| [features](#features) | ``` track_events.app_id = features.created_by_user.app_id ``` |
| [visitor\_history](#visitor-history) | ``` track_events.app_id = visitor_history.app_id ```  ``` track_events.visitor_id = visitor_history.visitor_id ``` |
| [track\_types](#track-types) | ``` track_events.track_type_id = track_types.id ``` |
| [guides](#guides) | ``` track_events.visitor_id = guides.audience.select.visitor_id ``` |

track\_events table schema

|  |
| --- |
| **account\_id**  STRING |
| **app\_id**  NUMBER |
| **day**  DATE-TIME |
| **hour**  DATE-TIME |
| **num\_events**  INTEGER |
| **num\_minutes**  INTEGER |
| **properties**  OBJECT This is a nested data structure:   - **android**: BOOLEAN - **any**: BOOLEAN - **apple**: BOOLEAN - **phone**: BOOLEAN - **table**: BOOLEAN |
| **remote\_ip**  STRING |
| **server**  STRING |
| **track\_type\_id**  STRING |
| **user\_agent**  STRING |
| **visitor\_id**  STRING |

### track\_types

The `track_types` table contains info about

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Pendo API method](https://engageapi.pendo.io/#7c8479b8-3843-403c-94a9-04cbdf542db9 "Opens in new tab: Pendo API method") |

track\_types table foreign keys

| Join track\_types with | on |
| --- | --- |
| [features](#features) | ``` track_types.group.id = features.group.id ```  ``` track_types.created_by_user.id = features.created_by_user.id ```  ``` track_types.last_updated_by_user.id = features.created_by_user.id ```  ``` track_types.created_by_user.id = features.group.created_by_user.id ```  ``` track_types.last_updated_by_user.id = features.group.created_by_user.id ```  ``` track_types.created_by_user.id = features.group.last_updated_by_user.id ```  ``` track_types.last_updated_by_user.id = features.group.last_updated_by_user.id ```  ``` track_types.created_by_user.id = features.last_updated_by_user.id ```  ``` track_types.last_updated_by_user.id = features.last_updated_by_user.id ``` |
| [pages](#pages) | ``` track_types.group.id = pages.group.id ```  ``` track_types.created_by_user.id = pages.created_by_user.id ```  ``` track_types.last_updated_by_user.id = pages.created_by_user.id ```  ``` track_types.created_by_user.id = pages.group.created_by_user.id ```  ``` track_types.last_updated_by_user.id = pages.group.created_by_user.id ```  ``` track_types.created_by_user.id = pages.group.last_updated_by_user.id ```  ``` track_types.last_updated_by_user.id = pages.group.last_updated_by_user.id ```  ``` track_types.created_by_user.id = pages.last_updated_by_user.id ```  ``` track_types.last_updated_by_user.id = pages.last_updated_by_user.id ``` |
| [track\_events](#track-events) | ``` track_types.id = track_events.track_type_id ``` |
| [guides](#guides) | ``` track_types.created_by_user.id = guides.created_by_user.id ```  ``` track_types.last_updated_by_user.id = guides.created_by_user.id ```  ``` track_types.created_by_user.id = guides.last_updated_by_user.id ```  ``` track_types.last_updated_by_user.id = guides.last_updated_by_user.id ``` |

track\_types table schema

|  |
| --- |
| **app\_id**  NUMBER |
| **color**  STRING |
| **created\_at**  DATE-TIME |
| **created\_by\_user**  OBJECT This is a nested data structure:   - **first**: STRING - **id**: STRING - **last**: STRING - **role**: INTEGER - **username**: STRING |
| **dirty**  BOOLEAN |
| **group**  OBJECT This is a nested data structure:   - **color**: STRING - **description**: STRING - **id**: STRING - **length**: INTEGER - **name**: STRING |
| **id**  STRING |
| **kind**  STRING |
| **last\_updated\_at**  DATE-TIME |
| **last\_updated\_by\_user**  OBJECT This is a nested data structure:   - **color**: STRING - **description**: STRING - **id**: STRING - **length**: INTEGER - **name**: STRING |
| **name**  STRING |
| **root\_version\_id**  STRING |
| **stable\_version\_id**  STRING |
| **track\_type\_name**  BOOLEAN |
| **track\_type\_rules**    ARRAY |

### visitor\_history

The `visitor_history` table contains info about visitor activity.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | visitor\_id |
| **Replication Key** | modified\_ts |
| **Useful links** | [Pendo documentation](https://engageapi.pendo.io/#3acb7d0d-69dc-4508-a9ba-e085a7301c27)  [Pendo API method](https://engageapi.pendo.io/#7c8479b8-3843-403c-94a9-04cbdf542db9 "Opens in new tab: Pendo API method") |

visitor\_history table foreign keys

| Join visitor\_history with | on |
| --- | --- |
| [events](#events) | ``` visitor_history.app_id = events.app_id ```  ``` visitor_history.feature_id = events.feature_id ```  ``` visitor_history.page_id = events.page_id ```  ``` visitor_history.visitor_id = events.visitor_id ``` |
| [feature\_events](#feature-events) | ``` visitor_history.app_id = feature_events.app_id ```  ``` visitor_history.feature_id = feature_events.feature_id ```  ``` visitor_history.visitor_id = feature_events.visitor_id ``` |
| [features](#features) | ``` visitor_history.app_id = features.created_by_user.app_id ```  ``` visitor_history.feature_id = features.id ```  ``` visitor_history.page_id = features.page_id ``` |
| [guide\_events](#guide-events) | ``` visitor_history.app_id = guide_events.app_id ```  ``` visitor_history.guide_id = guide_events.guide_id ```  ``` visitor_history.visitor_id = guide_events.visitor_id ``` |
| [page\_events](#page-events) | ``` visitor_history.app_id = page_events.app_id ```  ``` visitor_history.page_id = page_events.page_id ```  ``` visitor_history.visitor_id = page_events.visitor_id ``` |
| [track\_events](#track-events) | ``` visitor_history.app_id = track_events.app_id ```  ``` visitor_history.visitor_id = track_events.visitor_id ``` |
| [guides](#guides) | ``` visitor_history.guide_id = guides.id ```  ``` visitor_history.guide_id = guides.steps.guide_id ```  ``` visitor_history.guide_id = guides.steps.id ```  ``` visitor_history.page_id = guides.steps.page_id ```  ``` visitor_history.visitor_id = guides.audience.select.visitor_id ``` |
| [poll\_events](#poll-events) | ``` visitor_history.guide_id = poll_events.guide_id ```  ``` visitor_history.visitor_id = poll_events.visitor_id ``` |
| [pages](#pages) | ``` visitor_history.page_id = pages.id ``` |
| [visitors](#visitors) | ``` visitor_history.visitor_id = visitors.visitor_id ``` |

visitor\_history table schema

|  |
| --- |
| **app\_id**  NUMBER |
| **duration**  INTEGER |
| **feature\_id**  STRING |
| **guide\_id**  STRING |
| **guide\_step\_id**  STRING |
| **last\_ts**  DATE-TIME |
| **modified\_ts**  DATE-TIME |
| **page\_id**  STRING |
| **parsed\_user\_agent**  OBJECT This is a nested data structure:   - **name**: STRING - **os**: STRING - **version**: STRING |
| **ts**  DATE-TIME |
| **type**  STRING |
| **untagged\_url**  STRING |
| **uri**  STRING |
| **visitor\_id**  STRING |

### visitors

The `visitors` table contains info about the visitors recorded in your Pendo account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | visitor\_id |
| **Replication Key** | lastupdated |
| **Useful links** | [Pendo documentation](https://engageapi.pendo.io/#3acb7d0d-69dc-4508-a9ba-e085a7301c27)  [Pendo API method](https://engageapi.pendo.io/#7c8479b8-3843-403c-94a9-04cbdf542db9 "Opens in new tab: Pendo API method") |

visitors table foreign keys

| Join visitors with | on |
| --- | --- |
| [accounts](#accounts) | ``` visitors.metadata_auto.accountid = accounts.account_id ```  ``` visitors.metadata_auto.accountids = accounts.account_id ``` |
| [events](#events) | ``` visitors.metadata_auto.accountid = events.account_id ```  ``` visitors.metadata_auto.accountids = events.account_id ```  ``` visitors.visitor_id = events.visitor_id ``` |
| [feature\_events](#feature-events) | ``` visitors.metadata_auto.accountid = feature_events.account_id ```  ``` visitors.metadata_auto.accountids = feature_events.account_id ```  ``` visitors.visitor_id = feature_events.visitor_id ``` |
| [guide\_events](#guide-events) | ``` visitors.metadata_auto.accountid = guide_events.account_id ```  ``` visitors.metadata_auto.accountids = guide_events.account_id ```  ``` visitors.metadata_auto.accountid = guide_events.account_ids ```  ``` visitors.metadata_auto.accountids = guide_events.account_ids ```  ``` visitors.visitor_id = guide_events.visitor_id ``` |
| [page\_events](#page-events) | ``` visitors.metadata_auto.accountid = page_events.account_id ```  ``` visitors.metadata_auto.accountids = page_events.account_id ```  ``` visitors.visitor_id = page_events.visitor_id ``` |
| [poll\_events](#poll-events) | ``` visitors.metadata_auto.accountid = poll_events.account_id ```  ``` visitors.metadata_auto.accountids = poll_events.account_id ```  ``` visitors.metadata_auto.accountid = poll_events.account_ids ```  ``` visitors.metadata_auto.accountids = poll_events.account_ids ```  ``` visitors.visitor_id = poll_events.visitor_id ``` |
| [track\_events](#track-events) | ``` visitors.metadata_auto.accountid = track_events.account_id ```  ``` visitors.metadata_auto.accountids = track_events.account_id ```  ``` visitors.visitor_id = track_events.visitor_id ``` |
| [guides](#guides) | ``` visitors.visitor_id = guides.audience.select.visitor_id ``` |
| [visitor\_history](#visitor-history) | ``` visitors.visitor_id = visitor_history.visitor_id ``` |

visitors table schema

|  |
| --- |
| **lastupdated**  DATE-TIME |
| **metadata\_agent**  OBJECT This is a nested data structure:   - **email**: STRING - **ipaddress**: STRING - **language**: STRING |
| **metadata\_auto**  OBJECT This is a nested data structure:   - **accountid**: STRING - **accountids**: ARRAY, which is also a nested data structure:   - **firstvisit**: DATE-TIME   - **id**: STRING   - **idhash**: INTEGER   - **lastbrowsername**: STRING   - **lastbrowserversion**: STRING   - **lastoperatingsystem**: STRING   - **lastservername**: STRING   - **lastupdated**: DATE-TIME   - **lastuseragent**: STRING   - **lastvisit**: DATE-TIME   - **nid**: INTEGER |
| **metadata\_custom**  OBJECT |
| **visitor\_id**  STRING |
