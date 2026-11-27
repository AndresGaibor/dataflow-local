---
title: "Pipedrive"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Pipedrive.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Pipedrive

Pipedrive is a sales pipeline CRM designed to help small businesses manage leads, track sales activities and close more deals.

For more information about the API, see the [Pipedrive REST API](https://developers.pipedrive.com/Content/api/v1/).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To obtain the API token:

1. Make sure you have the Admin permissions in Pipedrive.

   You need them to ensure Qlik can access and replicate all your data. It is recommend that you [create a separate Pipedrive Admin user for Qlik](http://support.pipedrive.com/hc/en-us/articles/207319685-How-to-add-edit-remove-a-user), but this is not mandatory to use the integration. Creating a dedicated user makes the activities easier to distinguish in logs and audits.

   If you do not want to create a dedicated user, make sure that the credentials you use to connect to Qlik have Admin permissions. If the API token associated with a non-Admin user is used to set up the integration, Qlik may be unable to access and replicate all of your data.

   Users are counted at the account-level in Pipedrive, not the company level. If you want to create a user for Qlik and are concerned about the cost of your Pipedrive subscription, you will not be charged twice.
2. If you created a Pipedrive user for Qlik, log into Pipedrive as the Qlik user. If you did not, log into Pipedrive as an Admin user.
3. Click the user menu (where your avatar is) in the top-right corner of the screen.
4. Click Settings > API.
5. Copy the API token:

   ![Personal API token in the Pipedrive app](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/pipedrive-api-token.png)

### Connecting multiple Pipedrive companies

If you want to connect more than one Pipedrive company, repeat the entire procedure above for every company you want to add. You must create a separate Pipedrive integration for each company.

Our Pipedrive integration uses an API Token to authenticate. Pipedrive API tokens are unique not only at the user level, but the company level as well. This means that a user’s API Token will vary from company to company, even if everything is housed in the same Pipedrive account.

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

### activities

The `activities` table contains info about recent activities - calls, tasks, lunches, etc. - recorded in your Pipedrive account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | update\_time |
| **Useful links** | [Pipedrive API method](https://developers.pipedrive.com/Content/api/v1/#!/Recents "Opens in new tab: Pipedrive API method") |

activities table foreign keys

| Join activities with | on |
| --- | --- |
| [deals](#deals) | ``` activities.id = deals.last_activity_id ```  ``` activities.id = deals.next_activity_id ```  ``` activities.deal_id = deals.id ```  ``` activities.org_id = deals.org_id ```  ``` activities.assigned_to_user_id = deals.creator_user_id ```  ``` activities.created_by_user_id = deals.creator_user_id ```  ``` activities.user_id = deals.creator_user_id ```  ``` activities.assigned_to_user_id = deals.user_id ```  ``` activities.created_by_user_id = deals.user_id ```  ``` activities.user_id = deals.user_id ``` |
| [files](#files) | ``` activities.id = files.activity_id ```  ``` activities.deal_id = files.deal_id ```  ``` activities.org_id = files.org_id ```  ``` activities.participants.person_id = files.person_id ```  ``` activities.person_id = files.person_id ```  ``` activities.assigned_to_user_id = files.user_id ```  ``` activities.created_by_user_id = files.user_id ```  ``` activities.user_id = files.user_id ``` |
| [organizations](#organizations) | ``` activities.id = organizations.last_activity_id ```  ``` activities.id = organizations.next_activity_id ```  ``` activities.org_id = organizations.id ``` |
| [persons](#persons) | ``` activities.id = persons.last_activity_id ```  ``` activities.id = persons.next_activity_id ```  ``` activities.participants.person_id = persons.id ```  ``` activities.person_id = persons.id ``` |
| [deal\_products](#deal-products) | ``` activities.deal_id = deal_products.deal_id ``` |
| [notes](#notes) | ``` activities.deal_id = notes.deal_id ```  ``` activities.org_id = notes.org_id ```  ``` activities.participants.person_id = notes.person_id ```  ``` activities.person_id = notes.person_id ```  ``` activities.assigned_to_user_id = notes.last_update_user_id ```  ``` activities.created_by_user_id = notes.last_update_user_id ```  ``` activities.user_id = notes.last_update_user_id ```  ``` activities.assigned_to_user_id = notes.user_id ```  ``` activities.created_by_user_id = notes.user_id ```  ``` activities.user_id = notes.user_id ``` |
| [dealflow](#dealflow) | ``` activities.assigned_to_user_id = dealflow.user_id ```  ``` activities.created_by_user_id = dealflow.user_id ```  ``` activities.user_id = dealflow.user_id ``` |
| [filters](#filters) | ``` activities.assigned_to_user_id = filters.user_id ```  ``` activities.created_by_user_id = filters.user_id ```  ``` activities.user_id = filters.user_id ``` |
| [users](#users) | ``` activities.assigned_to_user_id = users.id ```  ``` activities.created_by_user_id = users.id ```  ``` activities.user_id = users.id ``` |

activities table schema

|  |
| --- |
| **active\_flag**  BOOLEAN |
| **add\_time**  DATE-TIME |
| **assigned\_to\_user\_id**  INTEGER |
| **company\_id**  INTEGER |
| **created\_by\_user\_id**  INTEGER |
| **deal\_dropbox\_bcc**  STRING |
| **deal\_id**  INTEGER |
| **deal\_title**  STRING |
| **done**  BOOLEAN |
| **due\_date**  STRING |
| **due\_time**  STRING |
| **duration**  STRING |
| **gcal\_event\_id**  STRING |
| **google\_calendar\_etag**  STRING |
| **google\_calendar\_id**  STRING |
| **id**  INTEGER |
| **marked\_as\_done\_time**  DATE-TIME |
| **note**  STRING |
| **org\_id**  INTEGER |
| **org\_name**  STRING |
| **owner\_name**  STRING |
| **participants**  ARRAY This is a nested data structure:   - **person\_id**: INTEGER - **primary\_flag**: BOOLEAN |
| **person\_dropbox\_bcc**  STRING |
| **person\_id**  INTEGER |
| **person\_name**  STRING |
| **reference\_id**  INTEGER |
| **reference\_type**  STRING |
| **subject**  STRING |
| **type**  STRING |
| **update\_time**  DATE-TIME |
| **user\_id**  INTEGER |

### activity\_types

The `activity_types` table contains info about the different kinds of activities in your Pipedrive account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Pipedrive documentation](https://developers.pipedrive.com/Content/api/v1/#!/ActivityTypes)  [Pipedrive API method](https://developers.pipedrive.com/Content/api/v1/#!/ActivityTypes/get_activityTypes "Opens in new tab: Pipedrive API method") |

activity\_types table schema

|  |
| --- |
| **active\_flag**  BOOLEAN |
| **add\_time**  DATE-TIME |
| **color**  STRING |
| **icon\_key**  STRING |
| **id**  INTEGER |
| **is\_custom\_flag**  BOOLEAN |
| **key\_string**  STRING |
| **name**  STRING |
| **order\_nr**  INTEGER |
| **update\_time**  DATE-TIME |

### currency

The `currency` table contains info about the currencies listed in your Pipedrive account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Pipedrive API method](https://developers.pipedrive.com/Content/api/v1/#!/Currencies "Opens in new tab: Pipedrive API method") |

currency table schema

|  |
| --- |
| **active\_flag**  BOOLEAN |
| **code**  STRING |
| **decimal\_points**  INTEGER |
| **id**  INTEGER |
| **is\_custom\_flag**  BOOLEAN |
| **name**  STRING |
| **symbol**  STRING |

### deal\_fields

The `deal_fields` table contains info about all deal fields.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | update\_time |
| **Useful links** | [Pipedrive API method](https://developers.pipedrive.com/Content/api/v1/DealFields#getDealFields "Opens in new tab: Pipedrive API method") |

deal\_fields table schema

|  |
| --- |
| **active\_flag**  BOOLEAN |
| **add\_time**  DATE-TIME |
| **add\_visible\_flag**  BOOLEAN |
| **bulk\_edit\_allowed**  BOOLEAN |
| **details\_visible\_flag**  BOOLEAN |
| **edit\_flag**  BOOLEAN |
| **field\_type**  STRING |
| **filtering\_allowed**  BOOLEAN |
| **id**  INTEGER |
| **important\_flag**  BOOLEAN |
| **index\_visible\_flag**  BOOLEAN |
| **key**  STRING |
| **last\_updated\_by\_user\_id**  INTEGER |
| **mandatory\_flag**  BOOLEAN |
| **name**  STRING |
| **options**  ARRAY This is a nested data structure:   - **id**: STRING - **label**: STRING |
| **order\_nr**  INTEGER |
| **searchable\_flag**  BOOLEAN |
| **sortable\_flag**  BOOLEAN |
| **update\_time**  DATE-TIME |

### deal\_products

The `deal_products` table contains info about the products attached to deals.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Pipedrive documentation](https://developers.pipedrive.com/Content/api/v1/#!/Deals)  [Pipedrive API method](https://developers.pipedrive.com/Content/api/v1/#!/Deals/get_deals_id_products "Opens in new tab: Pipedrive API method") |

deal\_products table foreign keys

| Join deal\_products with | on |
| --- | --- |
| [activities](#activities) | ``` deal_products.deal_id = activities.deal_id ``` |
| [deals](#deals) | ``` deal_products.deal_id = deals.id ``` |
| [files](#files) | ``` deal_products.deal_id = files.deal_id ```  ``` deal_products.product_id = files.product_id ``` |
| [notes](#notes) | ``` deal_products.deal_id = notes.deal_id ``` |
| [products](#products) | ``` deal_products.product_id = products.id ``` |

deal\_products table schema

|  |
| --- |
| **active\_flag**  BOOLEAN |
| **add\_time**  DATE-TIME |
| **comments**  STRING |
| **currency**  STRING |
| **deal\_id**  INTEGER |
| **discount\_percentage**  NUMBER |
| **duration**  NUMBER |
| **enabled\_flag**  BOOLEAN |
| **id**  INTEGER |
| **item\_price**  NUMBER |
| **last\_edit**  DATE-TIME |
| **name**  STRING |
| **order\_nr**  INTEGER |
| **product\_id**  INTEGER |
| **product\_variation\_id**  INTEGER |
| **quantity**  INTEGER |
| **quantity\_formatted**  STRING |
| **sum**  NUMBER |
| **sum\_formatted**  STRING |
| **sum\_no\_discount**  NUMBER |

### dealflow

The `dealflow` table contains info about the updates made to a deal.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | log\_time |
| **Useful links** | [Pipedrive API method](https://developers.pipedrive.com/Content/api/v1/#!/Deals/get_deals_id_flow "Opens in new tab: Pipedrive API method") |

dealflow table foreign keys

| Join dealflow with | on |
| --- | --- |
| [activities](#activities) | ``` dealflow.user_id = activities.assigned_to_user_id ```  ``` dealflow.user_id = activities.created_by_user_id ```  ``` dealflow.user_id = activities.user_id ``` |
| [deals](#deals) | ``` dealflow.user_id = deals.creator_user_id ```  ``` dealflow.user_id = deals.user_id ``` |
| [files](#files) | ``` dealflow.user_id = files.user_id ``` |
| [filters](#filters) | ``` dealflow.user_id = filters.user_id ``` |
| [notes](#notes) | ``` dealflow.user_id = notes.last_update_user_id ```  ``` dealflow.user_id = notes.user_id ``` |
| [users](#users) | ``` dealflow.user_id = users.id ``` |

dealflow table schema

|  |
| --- |
| **additional\_data**  STRING |
| **change\_source**  STRING |
| **field\_key**  STRING |
| **id**  INTEGER |
| **is\_bulk\_update\_flag**  BOOLEAN |
| **item\_id**  INTEGER |
| **log\_time**  DATE-TIME |
| **new\_value**  STRING |
| **old\_value**  STRING |
| **user\_id**  INTEGER |

### deals

The `deals` table contains info about updates made recently to the deals in your Pipedrive account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | update\_time |
| **Useful links** | [Pipedrive API method](https://developers.pipedrive.com/Content/api/v1/#!/Recents "Opens in new tab: Pipedrive API method") |

deals table foreign keys

| Join deals with | on |
| --- | --- |
| [activities](#activities) | ``` deals.last_activity_id = activities.id ```  ``` deals.next_activity_id = activities.id ```  ``` deals.id = activities.deal_id ```  ``` deals.org_id = activities.org_id ```  ``` deals.creator_user_id = activities.assigned_to_user_id ```  ``` deals.user_id = activities.assigned_to_user_id ```  ``` deals.creator_user_id = activities.created_by_user_id ```  ``` deals.user_id = activities.created_by_user_id ```  ``` deals.creator_user_id = activities.user_id ```  ``` deals.user_id = activities.user_id ``` |
| [files](#files) | ``` deals.last_activity_id = files.activity_id ```  ``` deals.next_activity_id = files.activity_id ```  ``` deals.id = files.deal_id ```  ``` deals.org_id = files.org_id ```  ``` deals.creator_user_id = files.user_id ```  ``` deals.user_id = files.user_id ``` |
| [organizations](#organizations) | ``` deals.last_activity_id = organizations.last_activity_id ```  ``` deals.next_activity_id = organizations.last_activity_id ```  ``` deals.last_activity_id = organizations.next_activity_id ```  ``` deals.next_activity_id = organizations.next_activity_id ```  ``` deals.org_id = organizations.id ``` |
| [persons](#persons) | ``` deals.last_activity_id = persons.last_activity_id ```  ``` deals.next_activity_id = persons.last_activity_id ```  ``` deals.last_activity_id = persons.next_activity_id ```  ``` deals.next_activity_id = persons.next_activity_id ``` |
| [deal\_products](#deal-products) | ``` deals.id = deal_products.deal_id ``` |
| [notes](#notes) | ``` deals.id = notes.deal_id ```  ``` deals.org_id = notes.org_id ```  ``` deals.creator_user_id = notes.last_update_user_id ```  ``` deals.user_id = notes.last_update_user_id ```  ``` deals.creator_user_id = notes.user_id ```  ``` deals.user_id = notes.user_id ``` |
| [pipelines](#pipelines) | ``` deals.pipeline_id = pipelines.id ``` |
| [stages](#stages) | ``` deals.pipeline_id = stages.pipeline_id ```  ``` deals.stage_id = stages.id ``` |
| [dealflow](#dealflow) | ``` deals.creator_user_id = dealflow.user_id ```  ``` deals.user_id = dealflow.user_id ``` |
| [filters](#filters) | ``` deals.creator_user_id = filters.user_id ```  ``` deals.user_id = filters.user_id ``` |
| [users](#users) | ``` deals.creator_user_id = users.id ```  ``` deals.user_id = users.id ``` |

deals table schema

|  |
| --- |
| **active**  BOOLEAN |
| **activities\_count**  INTEGER |
| **add\_time**  DATE-TIME |
| **cc\_email**  STRING |
| **close\_time**  DATE-TIME |
| **creator\_user\_id**  INTEGER |
| **currency**  STRING |
| **deleted**  BOOLEAN |
| **done\_activities\_count**  INTEGER |
| **email\_messages\_count**  INTEGER |
| **expected\_close\_date**  STRING |
| **files\_count**  INTEGER |
| **first\_won\_time**    DATE-TIME  STRING |
| **followers\_count**  INTEGER |
| **formatted\_value**  STRING |
| **formatted\_weighted\_value**  STRING |
| **group\_id**  INTEGER |
| **group\_name**  STRING |
| **id**  INTEGER |
| **last\_activity\_date**  STRING |
| **last\_activity\_id**  INTEGER |
| **last\_incoming\_mail\_time**  DATE-TIME |
| **last\_outgoing\_mail\_time**  DATE-TIME |
| **lost\_reason**  STRING |
| **lost\_time**  DATE-TIME |
| **next\_activity\_date**  STRING |
| **next\_activity\_duration**  STRING |
| **next\_activity\_id**  INTEGER |
| **next\_activity\_note**  STRING |
| **next\_activity\_subject**  STRING |
| **next\_activity\_time**  STRING |
| **next\_activity\_type**  STRING |
| **notes\_count**  INTEGER |
| **org\_hidden**  BOOLEAN |
| **org\_id**  INTEGER |
| **org\_name**  STRING |
| **owner\_name**  STRING |
| **participants\_count**  INTEGER |
| **person\_hidden**  BOOLEAN |
| **person\_id**  INTEGER |
| **person\_name**  STRING |
| **pipeline\_id**  INTEGER |
| **probability**  NUMBER |
| **products\_count**  INTEGER |
| **reference\_activities\_count**  INTEGER |
| **renewal\_type**  STRING |
| **rotten\_time**  DATE-TIME |
| **stage\_change\_time**  DATE-TIME |
| **stage\_id**  INTEGER |
| **stage\_order\_nr**  INTEGER |
| **status**  STRING |
| **title**  STRING |
| **undone\_activities\_count**  INTEGER |
| **update\_time**  DATE-TIME |
| **user\_id**  INTEGER |
| **value**  NUMBER |
| **visible\_to**  STRING |
| **weighted\_value**  NUMBER |
| **won\_time**  DATE-TIME |

### files

The `files` table contains info about the recently updated files in your Pipedrive account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | update\_time |
| **Useful links** | [Pipedrive API method](https://developers.pipedrive.com/Content/api/v1/#!/Recents "Opens in new tab: Pipedrive API method") |

files table foreign keys

| Join files with | on |
| --- | --- |
| [activities](#activities) | ``` files.activity_id = activities.id ```  ``` files.deal_id = activities.deal_id ```  ``` files.org_id = activities.org_id ```  ``` files.person_id = activities.participants.person_id ```  ``` files.person_id = activities.person_id ```  ``` files.user_id = activities.assigned_to_user_id ```  ``` files.user_id = activities.created_by_user_id ```  ``` files.user_id = activities.user_id ``` |
| [deals](#deals) | ``` files.activity_id = deals.last_activity_id ```  ``` files.activity_id = deals.next_activity_id ```  ``` files.deal_id = deals.id ```  ``` files.org_id = deals.org_id ```  ``` files.user_id = deals.creator_user_id ```  ``` files.user_id = deals.user_id ``` |
| [organizations](#organizations) | ``` files.activity_id = organizations.last_activity_id ```  ``` files.activity_id = organizations.next_activity_id ```  ``` files.org_id = organizations.id ``` |
| [persons](#persons) | ``` files.activity_id = persons.last_activity_id ```  ``` files.activity_id = persons.next_activity_id ```  ``` files.person_id = persons.id ``` |
| [deal\_products](#deal-products) | ``` files.deal_id = deal_products.deal_id ```  ``` files.product_id = deal_products.product_id ``` |
| [notes](#notes) | ``` files.deal_id = notes.deal_id ```  ``` files.note_id = notes.id ```  ``` files.org_id = notes.org_id ```  ``` files.person_id = notes.person_id ```  ``` files.user_id = notes.last_update_user_id ```  ``` files.user_id = notes.user_id ``` |
| [products](#products) | ``` files.product_id = products.id ``` |
| [dealflow](#dealflow) | ``` files.user_id = dealflow.user_id ``` |
| [filters](#filters) | ``` files.user_id = filters.user_id ``` |
| [users](#users) | ``` files.user_id = users.id ``` |

files table schema

|  |
| --- |
| **active\_flag**  BOOLEAN |
| **activity\_id**  INTEGER |
| **add\_time**  DATE-TIME |
| **cid**  STRING |
| **deal\_id**  INTEGER |
| **deal\_name**  STRING |
| **description**  STRING |
| **email\_message\_id**  INTEGER |
| **file\_name**  STRING |
| **file\_size**  INTEGER |
| **file\_type**  STRING |
| **id**  INTEGER |
| **inline\_flag**  BOOLEAN |
| **log\_id**  INTEGER |
| **mail\_message\_id**  INTEGER |
| **name**  STRING |
| **note\_id**  INTEGER |
| **org\_id**  INTEGER |
| **org\_name**  STRING |
| **people\_name**  STRING |
| **person\_id**  INTEGER |
| **person\_name**  STRING |
| **product\_id**  INTEGER |
| **product\_name**  STRING |
| **remote\_id**  STRING |
| **remote\_location**  STRING |
| **s3\_bucket**  STRING |
| **update\_time**  DATE-TIME |
| **url**  STRING |
| **user\_id**  INTEGER |

### filters

The `filters` table contains info about the filters, or data validation conditions, used in your Pipedrive account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Pipedrive API method](https://developers.pipedrive.com/Content/api/v1/#!/Filters "Opens in new tab: Pipedrive API method") |

filters table foreign keys

| Join filters with | on |
| --- | --- |
| [activities](#activities) | ``` filters.user_id = activities.assigned_to_user_id ```  ``` filters.user_id = activities.created_by_user_id ```  ``` filters.user_id = activities.user_id ``` |
| [dealflow](#dealflow) | ``` filters.user_id = dealflow.user_id ``` |
| [deals](#deals) | ``` filters.user_id = deals.creator_user_id ```  ``` filters.user_id = deals.user_id ``` |
| [files](#files) | ``` filters.user_id = files.user_id ``` |
| [notes](#notes) | ``` filters.user_id = notes.last_update_user_id ```  ``` filters.user_id = notes.user_id ``` |
| [users](#users) | ``` filters.user_id = users.id ``` |

filters table schema

|  |
| --- |
| **active\_flag**  BOOLEAN |
| **add\_time**  DATE-TIME |
| **custom\_view\_id**  INTEGER |
| **id**  INTEGER |
| **name**  STRING |
| **temporary\_flag**  BOOLEAN |
| **type**  STRING |
| **update\_time**  DATE-TIME |
| **user\_id**  INTEGER |
| **visible\_to**  STRING |

### notes

The `notes` table contains info about recent notes in your Pipedrive account. Notes are pieces of textual (HTML-formatted) information that can be attached to [`deals`](#deals), [`persons`](#persons) and [`organizations`](#organizations).

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | update\_time |
| **Useful links** | [Pipedrive API method](https://developers.pipedrive.com/Content/api/v1/#!/Recents "Opens in new tab: Pipedrive API method") |

notes table foreign keys

| Join notes with | on |
| --- | --- |
| [activities](#activities) | ``` notes.deal_id = activities.deal_id ```  ``` notes.org_id = activities.org_id ```  ``` notes.person_id = activities.participants.person_id ```  ``` notes.person_id = activities.person_id ```  ``` notes.last_update_user_id = activities.assigned_to_user_id ```  ``` notes.user_id = activities.assigned_to_user_id ```  ``` notes.last_update_user_id = activities.created_by_user_id ```  ``` notes.user_id = activities.created_by_user_id ```  ``` notes.last_update_user_id = activities.user_id ```  ``` notes.user_id = activities.user_id ``` |
| [deals](#deals) | ``` notes.deal_id = deals.id ```  ``` notes.org_id = deals.org_id ```  ``` notes.last_update_user_id = deals.creator_user_id ```  ``` notes.user_id = deals.creator_user_id ```  ``` notes.last_update_user_id = deals.user_id ```  ``` notes.user_id = deals.user_id ``` |
| [deal\_products](#deal-products) | ``` notes.deal_id = deal_products.deal_id ``` |
| [files](#files) | ``` notes.deal_id = files.deal_id ```  ``` notes.id = files.note_id ```  ``` notes.org_id = files.org_id ```  ``` notes.person_id = files.person_id ```  ``` notes.last_update_user_id = files.user_id ```  ``` notes.user_id = files.user_id ``` |
| [organizations](#organizations) | ``` notes.org_id = organizations.id ``` |
| [persons](#persons) | ``` notes.person_id = persons.id ``` |
| [dealflow](#dealflow) | ``` notes.last_update_user_id = dealflow.user_id ```  ``` notes.user_id = dealflow.user_id ``` |
| [filters](#filters) | ``` notes.last_update_user_id = filters.user_id ```  ``` notes.user_id = filters.user_id ``` |
| [users](#users) | ``` notes.last_update_user_id = users.id ```  ``` notes.user_id = users.id ``` |

notes table schema

|  |
| --- |
| **active\_flag**  BOOLEAN |
| **add\_time**  DATE-TIME |
| **content**  STRING |
| **deal**  OBJECT This is a nested data structure: **title**, STRING. |
| **deal\_id**  INTEGER |
| **id**  INTEGER |
| **last\_update\_user\_id**  INTEGER |
| **org\_id**  INTEGER |
| **organization**  OBJECT This is a nested data structure: **name**, STRING. |
| **person**  OBJECT This is a nested data structure: **name**, STRING. |
| **person\_id**  INTEGER |
| **pinned\_to\_deal\_flag**  BOOLEAN |
| **pinned\_to\_organization\_flag**  BOOLEAN |
| **pinned\_to\_person\_flag**  BOOLEAN |
| **update\_time**  DATE-TIME |
| **user**  OBJECT This is a nested data structure:   - **email**: STRING - **icon\_url**: STRING - **is\_you**: BOOLEAN - **name**: STRING |
| **user\_id**  INTEGER |

### organizations

The `organizations` table contains info about the recent organizations in your Pipedrive account. Organizations are companies and other types of organizations you are making deals with.

|  |  |
| --- | --- |
| **Replication Method** |  |
| **Primary Key** | id |
| **Replication Key** | update\_time |
| **Useful links** | [Pipedrive API method](https://developers.pipedrive.com/Content/api/v1/#!/Recents "Opens in new tab: Pipedrive API method") |

organizations table foreign keys

| Join organizations with | on |
| --- | --- |
| [activities](#activities) | ``` organizations.last_activity_id = activities.id ```  ``` organizations.next_activity_id = activities.id ```  ``` organizations.id = activities.org_id ``` |
| [deals](#deals) | ``` organizations.last_activity_id = deals.last_activity_id ```  ``` organizations.next_activity_id = deals.last_activity_id ```  ``` organizations.last_activity_id = deals.next_activity_id ```  ``` organizations.next_activity_id = deals.next_activity_id ```  ``` organizations.id = deals.org_id ``` |
| [files](#files) | ``` organizations.last_activity_id = files.activity_id ```  ``` organizations.next_activity_id = files.activity_id ```  ``` organizations.id = files.org_id ``` |
| [persons](#persons) | ``` organizations.last_activity_id = persons.last_activity_id ```  ``` organizations.next_activity_id = persons.last_activity_id ```  ``` organizations.last_activity_id = persons.next_activity_id ```  ``` organizations.next_activity_id = persons.next_activity_id ``` |
| [notes](#notes) | ``` organizations.id = notes.org_id ``` |

organizations table schema

|  |
| --- |
| **active\_flag**  BOOLEAN |
| **activities\_count**  INTEGER |
| **add\_time**  DATE-TIME |
| **address**  STRING |
| **address\_admin\_area\_level\_1**  STRING |
| **address\_admin\_area\_level\_2**  STRING |
| **address\_country**  STRING |
| **address\_formatted\_address**  STRING |
| **address\_locality**  STRING |
| **address\_postal\_code**  STRING |
| **address\_route**  STRING |
| **address\_street\_number**  STRING |
| **address\_sublocality**  STRING |
| **address\_subpremise**  STRING |
| **category\_id**  INTEGER |
| **cc\_email**  STRING |
| **closed\_deals\_count**  INTEGER |
| **company\_id**  INTEGER |
| **country\_code**  STRING |
| **done\_activities\_count**  INTEGER |
| **email\_messages\_count**  INTEGER |
| **files\_count**  INTEGER |
| **first\_char**  STRING |
| **followers\_count**  INTEGER |
| **id**  INTEGER |
| **last\_activity\_date**  STRING |
| **last\_activity\_id**  INTEGER |
| **lost\_deals\_count**  INTEGER |
| **name**  STRING |
| **next\_activity\_date**  STRING |
| **next\_activity\_id**  INTEGER |
| **next\_activity\_time**  STRING |
| **notes\_count**  INTEGER |
| **open\_deals\_count**  INTEGER |
| **owner\_id**  INTEGER |
| **owner\_name**  STRING |
| **people\_count**  INTEGER |
| **picture\_id**  INTEGER |
| **reference\_activities\_count**  INTEGER |
| **related\_closed\_deals\_count**  INTEGER |
| **related\_lost\_deals\_count**  INTEGER |
| **related\_open\_deals\_count**  INTEGER |
| **related\_won\_deals\_count**  INTEGER |
| **timeline\_last\_activity\_time**  DATE-TIME |
| **timeline\_last\_activity\_time\_by\_owner**  DATE-TIME |
| **undone\_activities\_count**  INTEGER |
| **update\_time**  DATE-TIME |
| **visible\_to**  STRING |
| **won\_deals\_count**  INTEGER |

### persons

The `persons` table contains info about the recent persons in your Pipedrive account. In Pipedrive, a person represents a contact, or a customer you’re doing a deal with.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | update\_time |
| **Useful links** | [Pipedrive API method](https://developers.pipedrive.com/Content/api/v1/#!/Recents "Opens in new tab: Pipedrive API method") |

persons table foreign keys

| Join persons with | on |
| --- | --- |
| [activities](#activities) | ``` persons.last_activity_id = activities.id ```  ``` persons.next_activity_id = activities.id ```  ``` persons.id = activities.participants.person_id ```  ``` persons.id = activities.person_id ``` |
| [deals](#deals) | ``` persons.last_activity_id = deals.last_activity_id ```  ``` persons.next_activity_id = deals.last_activity_id ```  ``` persons.last_activity_id = deals.next_activity_id ```  ``` persons.next_activity_id = deals.next_activity_id ``` |
| [files](#files) | ``` persons.last_activity_id = files.activity_id ```  ``` persons.next_activity_id = files.activity_id ```  ``` persons.id = files.person_id ``` |
| [organizations](#organizations) | ``` persons.last_activity_id = organizations.last_activity_id ```  ``` persons.next_activity_id = organizations.last_activity_id ```  ``` persons.last_activity_id = organizations.next_activity_id ```  ``` persons.next_activity_id = organizations.next_activity_id ``` |
| [notes](#notes) | ``` persons.id = notes.person_id ``` |

persons table schema

|  |
| --- |
| **active\_flag**  BOOLEAN |
| **activities\_count**  INTEGER |
| **add\_time**  DATE-TIME |
| **cc\_email**  STRING |
| **closed\_deals\_count**  INTEGER |
| **company\_id**  INTEGER |
| **done\_activities\_count**  INTEGER |
| **email**  ARRAY This is a nested data structure:   - **label**: STRING - **primary**: BOOLEAN - **value**: STRING |
| **email\_messages\_count**  INTEGER |
| **files\_count**  INTEGER |
| **first\_char**  STRING |
| **first\_name**  STRING |
| **followers\_count**  INTEGER |
| **id**  INTEGER |
| **last\_activity\_date**  STRING |
| **last\_activity\_id**  INTEGER |
| **last\_incoming\_mail\_time**  DATE-TIME |
| **last\_name**  STRING |
| **last\_outgoing\_mail\_time**  DATE-TIME |
| **lost\_deals\_count**  INTEGER |
| **name**  STRING |
| **next\_activity\_date**  STRING |
| **next\_activity\_id**  INTEGER |
| **next\_activity\_time**  STRING |
| **notes\_count**  INTEGER |
| **open\_deals\_count**  INTEGER |
| **org\_id**  INTEGER |
| **org\_name**  STRING |
| **owner\_id**  INTEGER |
| **owner\_name**  STRING |
| **participant\_closed\_deals\_count**  INTEGER |
| **participant\_open\_deals\_count**  INTEGER |
| **phone**  ARRAY This is a nested data structure:   - **label**: STRING - **primary**: BOOLEAN - **value**: STRING |
| **picture\_id**  INTEGER |
| **reference\_activities\_count**  INTEGER |
| **related\_closed\_deals\_count**  INTEGER |
| **related\_lost\_deals\_count**  INTEGER |
| **related\_open\_deals\_count**  INTEGER |
| **related\_won\_deals\_count**  INTEGER |
| **timeline\_last\_activity\_time**  DATE-TIME |
| **timeline\_last\_activity\_time\_by\_owner**  DATE-TIME |
| **undone\_activities\_count**  INTEGER |
| **update\_time**  DATE-TIME |
| **visible\_to**  STRING |
| **won\_deals\_count**  INTEGER |

### pipelines

The `pipelines` table contains info about the pipelines in your Pipedrive account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Pipedrive API method](https://developers.pipedrive.com/Content/api/v1/#!/Pipelines "Opens in new tab: Pipedrive API method") |

pipelines table foreign keys

| Join pipelines with | on |
| --- | --- |
| [deals](#deals) | ``` pipelines.id = deals.pipeline_id ``` |
| [stages](#stages) | ``` pipelines.id = stages.pipeline_id ``` |

pipelines table schema

|  |
| --- |
| **active**  BOOLEAN |
| **add\_time**  DATE-TIME |
| **id**  INTEGER |
| **name**  STRING |
| **order\_nr**  INTEGER |
| **selected**  BOOLEAN |
| **update\_time**  DATE-TIME |
| **url\_title**  STRING |

### products

The `products` table contains info about the recent products in your Pipedrive account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | update\_time |
| **Useful links** | [Pipedrive API method](https://developers.pipedrive.com/Content/api/v1/#!/Recents "Opens in new tab: Pipedrive API method") |

products table foreign keys

| Join products with | on |
| --- | --- |
| [deal\_products](#deal-products) | ``` products.id = deal_products.product_id ``` |
| [files](#files) | ``` products.id = files.product_id ``` |

products table schema

|  |
| --- |
| **active\_flag**  BOOLEAN |
| **add\_time**  DATE-TIME |
| **code**  STRING |
| **files\_count**  INTEGER |
| **first\_char**  STRING |
| **followers\_count**  INTEGER |
| **id**  INTEGER |
| **name**  STRING |
| **owner\_id**  INTEGER |
| **owner\_name**  STRING |
| **prices**  OBJECT, ARRAY This is a nested data structure: **USD**, OBJECT, which is also a nested data structure.   - **cost**: NUMBER - **currency**: STRING - **id**: INTEGER - **overhead\_cost**: NUMBER - **price**: INTEGER - **product\_id**: INTEGER |
| **selectable**  BOOLEAN |
| **tax**  INTEGER |
| **unit**  STRING |
| **update\_time**  DATE-TIME |
| **visible\_to**  STRING |

### stages

The `stages` table contains info about the pipeline stages in your Pipedrive account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Pipedrive API method](https://developers.pipedrive.com/Content/api/v1/#!/Stages/get_stages "Opens in new tab: Pipedrive API method") |

stages table foreign keys

| Join stages with | on |
| --- | --- |
| [deals](#deals) | ``` stages.pipeline_id = deals.pipeline_id ```  ``` stages.id = deals.stage_id ``` |
| [pipelines](#pipelines) | ``` stages.pipeline_id = pipelines.id ``` |

stages table schema

|  |
| --- |
| **active\_flag**  BOOLEAN |
| **add\_time**  DATE-TIME |
| **deal\_probability**  INTEGER |
| **id**  INTEGER |
| **name**  STRING |
| **order\_nr**  INTEGER |
| **pipeline\_id**  INTEGER |
| **pipeline\_name**  STRING |
| **rotten\_days**  INTEGER |
| **rotten\_flag**  BOOLEAN |
| **update\_time**  DATE-TIME |

### users

The `users` table contains info about the users associated with your Pipedrive account. **Note**: This table contains info about the people with access to your Pipedrive account - they should not be confused with [`persons`](#persons).

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Pipedrive API method](https://developers.pipedrive.com/Content/api/v1/#!/Recents "Opens in new tab: Pipedrive API method") |

users table foreign keys

| Join users with | on |
| --- | --- |
| [activities](#activities) | ``` users.id = activities.assigned_to_user_id ```  ``` users.id = activities.created_by_user_id ```  ``` users.id = activities.user_id ``` |
| [dealflow](#dealflow) | ``` users.id = dealflow.user_id ``` |
| [deals](#deals) | ``` users.id = deals.creator_user_id ```  ``` users.id = deals.user_id ``` |
| [files](#files) | ``` users.id = files.user_id ``` |
| [filters](#filters) | ``` users.id = filters.user_id ``` |
| [notes](#notes) | ``` users.id = notes.last_update_user_id ```  ``` users.id = notes.user_id ``` |

users table schema

|  |
| --- |
| **activated**  BOOLEAN |
| **active\_flag**  BOOLEAN |
| **created**  DATE-TIME |
| **default\_currency**  STRING |
| **email**  STRING |
| **has\_created\_company**  BOOLEAN |
| **icon\_url**  STRING |
| **id**  INTEGER |
| **is\_admin**  INTEGER |
| **is\_you**  BOOLEAN |
| **lang**  INTEGER |
| **last\_login**    DATE-TIME  STRING |
| **locale**  STRING |
| **modified**  DATE-TIME |
| **name**  STRING |
| **phone**  STRING |
| **role\_id**  INTEGER |
| **signup\_flow\_variation**  STRING |
| **timezone\_name**  STRING |
| **timezone\_offset**  STRING |
