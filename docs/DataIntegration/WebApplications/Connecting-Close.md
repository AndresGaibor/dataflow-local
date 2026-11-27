---
title: "Close"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Close.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Close

Close is a specialized CRM platform designed for small to medium-sized businesses, focusing on converting leads into revenue.

For more information about the API, see the [Close REST API](https://developer.close.com/).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To generate an API key:

1. Log into your Close account.
2. Click the user menu (your icon) in the top-right corner.
3. Go to Settings > Developer > API Keys.
4. Click New API Key.
5. Enter a API key name.
6. Click Create API Key.
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
| API key | API key. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### activities

The `activities` table contains info about various activities in your Close account.

An activity belongs to a lead and can represent any type of activity that was performed on a lead or its contact. This includes calls, emails, notes, and so on.

#### Attribution window

When data is replicated for this table, it will use an attribution window of 24 hours to fetch updated activities.

This means that every time a replication job runs, the last 24 hours’ worth of data will be replicated for this table. This is because Close doesn’t provide a way to query for activites based on a modification time, only when activities are created. A list of available querying methods can be found in [Close’s documentation](https://developer.close.io/#activities-list-or-filter-all-activity-types).

Refer to the [Replication](#replication) section for more info and examples of how the attribution window is used to query for data.

|  |  |
| --- | --- |
| **Replication Method** | Append-Only Incremental |
| **Primary Key** | id |
| **Replication Key** | date\_created |
| **Useful links** | [Close documentation](https://developer.close.io/#activities)  [Close API method](https://developer.close.io/#activities-list-or-filter-all-activity-types "Opens in new tab: Close API method") |

activities table foreign keys

| Join activities with | on |
| --- | --- |
| [leads](#leads) | ``` activities.contact_id = leads.contacts.id ```  ``` activities.contact_id = leads.opportunities.contact_id ```  ``` activities.contact_id = leads.tasks.contact_id ```  ``` activities.lead_id = leads.id ```  ``` activities.lead_id = leads.contacts.lead_id ```  ``` activities.lead_id = leads.opportunities.lead_id ```  ``` activities.lead_id = leads.tasks.lead_id ```  ``` activities.organization_id = leads.contacts.organization_id ```  ``` activities.organization_id = leads.opportunities.organization_id ```  ``` activities.organization_id = leads.organization_id ```  ``` activities.organization_id = leads.tasks.organization_id ```  ``` activities.task_id = leads.tasks.id ```  ``` activities.created_by = leads.contacts.created_by ```  ``` activities.updated_by = leads.contacts.created_by ```  ``` activities.user_id = leads.contacts.created_by ```  ``` activities.task_assigned_to = leads.contacts.created_by ```  ``` activities.users = leads.contacts.created_by ```  ``` activities.created_by = leads.contacts.updated_by ```  ``` activities.updated_by = leads.contacts.updated_by ```  ``` activities.user_id = leads.contacts.updated_by ```  ``` activities.task_assigned_to = leads.contacts.updated_by ```  ``` activities.users = leads.contacts.updated_by ```  ``` activities.created_by = leads.created_by ```  ``` activities.updated_by = leads.created_by ```  ``` activities.user_id = leads.created_by ```  ``` activities.task_assigned_to = leads.created_by ```  ``` activities.users = leads.created_by ```  ``` activities.created_by = leads.opportunities.created_by ```  ``` activities.updated_by = leads.opportunities.created_by ```  ``` activities.user_id = leads.opportunities.created_by ```  ``` activities.task_assigned_to = leads.opportunities.created_by ```  ``` activities.users = leads.opportunities.created_by ```  ``` activities.created_by = leads.opportunities.updated_by ```  ``` activities.updated_by = leads.opportunities.updated_by ```  ``` activities.user_id = leads.opportunities.updated_by ```  ``` activities.task_assigned_to = leads.opportunities.updated_by ```  ``` activities.users = leads.opportunities.updated_by ```  ``` activities.created_by = leads.opportunities.user_id ```  ``` activities.updated_by = leads.opportunities.user_id ```  ``` activities.user_id = leads.opportunities.user_id ```  ``` activities.task_assigned_to = leads.opportunities.user_id ```  ``` activities.users = leads.opportunities.user_id ```  ``` activities.created_by = leads.tasks.assigned_to ```  ``` activities.updated_by = leads.tasks.assigned_to ```  ``` activities.user_id = leads.tasks.assigned_to ```  ``` activities.task_assigned_to = leads.tasks.assigned_to ```  ``` activities.users = leads.tasks.assigned_to ```  ``` activities.created_by = leads.tasks.created_by ```  ``` activities.updated_by = leads.tasks.created_by ```  ``` activities.user_id = leads.tasks.created_by ```  ``` activities.task_assigned_to = leads.tasks.created_by ```  ``` activities.users = leads.tasks.created_by ```  ``` activities.created_by = leads.tasks.updated_by ```  ``` activities.updated_by = leads.tasks.updated_by ```  ``` activities.user_id = leads.tasks.updated_by ```  ``` activities.task_assigned_to = leads.tasks.updated_by ```  ``` activities.users = leads.tasks.updated_by ```  ``` activities.created_by = leads.updated_by ```  ``` activities.updated_by = leads.updated_by ```  ``` activities.user_id = leads.updated_by ```  ``` activities.task_assigned_to = leads.updated_by ```  ``` activities.users = leads.updated_by ``` |
| [tasks](#tasks) | ``` activities.contact_id = tasks.contact_id ```  ``` activities.lead_id = tasks.lead_id ```  ``` activities.organization_id = tasks.organization_id ```  ``` activities.task_id = tasks.id ```  ``` activities.created_by = tasks.assigned_to ```  ``` activities.updated_by = tasks.assigned_to ```  ``` activities.user_id = tasks.assigned_to ```  ``` activities.task_assigned_to = tasks.assigned_to ```  ``` activities.users = tasks.assigned_to ```  ``` activities.created_by = tasks.created_by ```  ``` activities.updated_by = tasks.created_by ```  ``` activities.user_id = tasks.created_by ```  ``` activities.task_assigned_to = tasks.created_by ```  ``` activities.users = tasks.created_by ```  ``` activities.created_by = tasks.updated_by ```  ``` activities.updated_by = tasks.updated_by ```  ``` activities.user_id = tasks.updated_by ```  ``` activities.task_assigned_to = tasks.updated_by ```  ``` activities.users = tasks.updated_by ``` |
| [event\_log](#event-log) | ``` activities.lead_id = event_log.lead_id ```  ``` activities.organization_id = event_log.organization_id ```  ``` activities.created_by = event_log.user_id ```  ``` activities.updated_by = event_log.user_id ```  ``` activities.user_id = event_log.user_id ```  ``` activities.task_assigned_to = event_log.user_id ```  ``` activities.users = event_log.user_id ``` |
| [custom\_fields](#custom-fields) | ``` activities.organization_id = custom_fields.organization_id ```  ``` activities.created_by = custom_fields.created_by ```  ``` activities.updated_by = custom_fields.created_by ```  ``` activities.user_id = custom_fields.created_by ```  ``` activities.task_assigned_to = custom_fields.created_by ```  ``` activities.users = custom_fields.created_by ```  ``` activities.created_by = custom_fields.updated_by ```  ``` activities.updated_by = custom_fields.updated_by ```  ``` activities.user_id = custom_fields.updated_by ```  ``` activities.task_assigned_to = custom_fields.updated_by ```  ``` activities.users = custom_fields.updated_by ``` |
| [users](#users) | ``` activities.organization_id = users.organizations ```  ``` activities.created_by = users.id ```  ``` activities.updated_by = users.id ```  ``` activities.user_id = users.id ```  ``` activities.task_assigned_to = users.id ```  ``` activities.users = users.id ``` |

activities table schema

|  |
| --- |
| **\_type**  STRING |
| **attachments**  ARRAY |
| **bcc**  ARRAY |
| **body\_html**  STRING |
| **body\_html\_quoted**  ARRAY **body\_html\_quoted**  This is a nested data structure:   - **expand**: INTEGER, BOOLEAN - **html**: STRING |
| **body\_preview**  STRING |
| **body\_text**  STRING |
| **body\_text\_quoted**  ARRAY **body\_text\_quoted**  This is a nested data structure:   - **expand**: INTEGER, BOOLEAN - **text**: STRING |
| **cc**  ARRAY |
| **contact\_id**  STRING |
| **created\_by**  STRING |
| **created\_by\_name**  STRING |
| **date\_created**  DATE-TIME |
| **date\_scheduled**  DATE-TIME |
| **date\_sent**  DATE-TIME |
| **date\_updated**  DATE-TIME |
| **dialer\_id**  STRING |
| **direction**  STRING |
| **duration**  INTEGER |
| **email\_account\_id**  STRING |
| **envelope**  OBJECT This is a nested data structure:   - **bcc**: ARRAY, which is also a nested data structure.   - **email**: STRING   - **name**: STRING - **cc**: ARRAY, which is also a nested data structure.   - **email**: STRING   - **name**: STRING - **date**: DATE-TIME, STRING - **from**: ARRAY, which is also a nested data structure.   - **email**: STRING   - **name**: STRING - **in\_reply\_to**: STRING - **is\_autoreply**: INTEGER, BOOLEAN - **message\_id**: STRING - **reply\_to**: ARRAY, which is also a nested data structure.   - **email**: STRING   - **name**: STRING - **sender**: ARRAY, which is also a nested data structure.   - **email**: STRING   - **name**: STRING - **subject**: STRING - **to**: ARRAY, which is also a nested data structure.   - **email**: STRING   - **name**: STRING |
| **id**  STRING |
| **import\_id**  STRING |
| **in\_reply\_to\_id**  STRING |
| **lead\_id**  STRING |
| **local\_phone**  STRING |
| **message\_ids**  ARRAY |
| **need\_smtp\_credentials**  INTEGER, BOOLEAN |
| **new\_status\_id**  STRING |
| **new\_status\_label**  STRING |
| **new\_status\_type**  STRING |
| **note**  STRING |
| **old\_status\_id**  STRING |
| **old\_status\_label**  STRING |
| **old\_status\_type**  STRING |
| **opens**  ARRAY This is a nested data structure:   - **ip\_address**: STRING - **opened\_at**: STRING - **opened\_by**: STRING - **user\_agent**: STRING |
| **opens\_summary**  STRING |
| **opportunity\_confidence**  INTEGER |
| **opportunity\_date\_won**  STRING |
| **opportunity\_id**  STRING |
| **opportunity\_value**  INTEGER |
| **opportunity\_value\_currency**  STRING |
| **opportunity\_value\_formatted**  STRING |
| **opportunity\_value\_period**  STRING |
| **organization\_id**  STRING |
| **phone**  STRING |
| **recording\_url**  STRING |
| **references**  ARRAY |
| **remote\_phone**  STRING |
| **send\_attempts**  ARRAY This is a nested data structure:   - **date**: DATE-TIME - **error\_class**: STRING - **message**: STRING |
| **sender**  STRING |
| **source**  STRING |
| **status**  STRING |
| **subject**  STRING |
| **task\_assigned\_to**  STRING |
| **task\_assigned\_to\_name**  STRING |
| **task\_id**  STRING |
| **task\_text**  STRING |
| **template\_id**  STRING |
| **template\_name**  STRING |
| **thread\_id**  STRING |
| **to**  ARRAY |
| **transferred\_from**  STRING |
| **transferred\_to**  STRING |
| **updated\_by**  STRING |
| **updated\_by\_name**  STRING |
| **user\_id**  STRING |
| **user\_name**  STRING |
| **users**  ARRAY |
| **voicemail\_duration**  INTEGER |
| **voicemail\_url**  STRING |

### custom\_fields

The `custom_fields` table contains info about the custom fields in your Close account.

Custom fields allow you to store arbitrary data on leads in Close. [Refer to Close’s documentation](https://help.close.io/customer/portal/articles/1104820-custom-fields) for more info.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | date\_updated |
| **Useful links** | [Close API method](https://developer.close.io/#custom-fields-list-all-the-custom-fields-for-your-organization "Opens in new tab: Close API method") |

custom\_fields table foreign keys

| Join custom\_fields with | on |
| --- | --- |
| [activities](#activities) | ``` custom_fields.organization_id = activities.organization_id ```  ``` custom_fields.created_by = activities.created_by ```  ``` custom_fields.updated_by = activities.created_by ```  ``` custom_fields.created_by = activities.updated_by ```  ``` custom_fields.updated_by = activities.updated_by ```  ``` custom_fields.created_by = activities.user_id ```  ``` custom_fields.updated_by = activities.user_id ```  ``` custom_fields.created_by = activities.task_assigned_to ```  ``` custom_fields.updated_by = activities.task_assigned_to ```  ``` custom_fields.created_by = activities.users ```  ``` custom_fields.updated_by = activities.users ``` |
| [event\_log](#event-log) | ``` custom_fields.organization_id = event_log.organization_id ```  ``` custom_fields.created_by = event_log.user_id ```  ``` custom_fields.updated_by = event_log.user_id ``` |
| [leads](#leads) | ``` custom_fields.organization_id = leads.contacts.organization_id ```  ``` custom_fields.organization_id = leads.opportunities.organization_id ```  ``` custom_fields.organization_id = leads.organization_id ```  ``` custom_fields.organization_id = leads.tasks.organization_id ```  ``` custom_fields.created_by = leads.contacts.created_by ```  ``` custom_fields.updated_by = leads.contacts.created_by ```  ``` custom_fields.created_by = leads.contacts.updated_by ```  ``` custom_fields.updated_by = leads.contacts.updated_by ```  ``` custom_fields.created_by = leads.created_by ```  ``` custom_fields.updated_by = leads.created_by ```  ``` custom_fields.created_by = leads.opportunities.created_by ```  ``` custom_fields.updated_by = leads.opportunities.created_by ```  ``` custom_fields.created_by = leads.opportunities.updated_by ```  ``` custom_fields.updated_by = leads.opportunities.updated_by ```  ``` custom_fields.created_by = leads.opportunities.user_id ```  ``` custom_fields.updated_by = leads.opportunities.user_id ```  ``` custom_fields.created_by = leads.tasks.assigned_to ```  ``` custom_fields.updated_by = leads.tasks.assigned_to ```  ``` custom_fields.created_by = leads.tasks.created_by ```  ``` custom_fields.updated_by = leads.tasks.created_by ```  ``` custom_fields.created_by = leads.tasks.updated_by ```  ``` custom_fields.updated_by = leads.tasks.updated_by ```  ``` custom_fields.created_by = leads.updated_by ```  ``` custom_fields.updated_by = leads.updated_by ``` |
| [tasks](#tasks) | ``` custom_fields.organization_id = tasks.organization_id ```  ``` custom_fields.created_by = tasks.assigned_to ```  ``` custom_fields.updated_by = tasks.assigned_to ```  ``` custom_fields.created_by = tasks.created_by ```  ``` custom_fields.updated_by = tasks.created_by ```  ``` custom_fields.created_by = tasks.updated_by ```  ``` custom_fields.updated_by = tasks.updated_by ``` |
| [users](#users) | ``` custom_fields.organization_id = users.organizations ```  ``` custom_fields.created_by = users.id ```  ``` custom_fields.updated_by = users.id ``` |

custom\_fields table schema

|  |
| --- |
| **choices**  ARRAY |
| **created\_by**  STRING |
| **date\_created**  DATE-TIME |
| **date\_updated**  DATE-TIME |
| **editable\_with\_roles**  ARRAY |
| **id**  STRING |
| **name**  STRING |
| **organization\_id**  STRING |
| **type**  STRING |
| **updated\_by**  STRING |

### event\_log

The `event_log` table contains info about events generated in your Close account. This could include creating a lead, sending an email, or deleting a note.

#### Historical data limitations

Due to how Close’s API functions, [only 30 days of historical data is available for this table](https://developer.close.io/#event-log) from the initial connection date.

Refer to the [Replication section](#historical-event-log-data) for more info.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | date\_updated |
| **Useful links** | [Close API method](https://developer.close.io/#event-log-retrieve-a-list-of-events "Opens in new tab: Close API method") |

event\_log table foreign keys

| Join event\_log with | on |
| --- | --- |
| [activities](#activities) | ``` event_log.lead_id = activities.lead_id ```  ``` event_log.organization_id = activities.organization_id ```  ``` event_log.user_id = activities.created_by ```  ``` event_log.user_id = activities.updated_by ```  ``` event_log.user_id = activities.user_id ```  ``` event_log.user_id = activities.task_assigned_to ```  ``` event_log.user_id = activities.users ``` |
| [leads](#leads) | ``` event_log.lead_id = leads.id ```  ``` event_log.lead_id = leads.contacts.lead_id ```  ``` event_log.lead_id = leads.opportunities.lead_id ```  ``` event_log.lead_id = leads.tasks.lead_id ```  ``` event_log.organization_id = leads.contacts.organization_id ```  ``` event_log.organization_id = leads.opportunities.organization_id ```  ``` event_log.organization_id = leads.organization_id ```  ``` event_log.organization_id = leads.tasks.organization_id ```  ``` event_log.user_id = leads.contacts.created_by ```  ``` event_log.user_id = leads.contacts.updated_by ```  ``` event_log.user_id = leads.created_by ```  ``` event_log.user_id = leads.opportunities.created_by ```  ``` event_log.user_id = leads.opportunities.updated_by ```  ``` event_log.user_id = leads.opportunities.user_id ```  ``` event_log.user_id = leads.tasks.assigned_to ```  ``` event_log.user_id = leads.tasks.created_by ```  ``` event_log.user_id = leads.tasks.updated_by ```  ``` event_log.user_id = leads.updated_by ``` |
| [tasks](#tasks) | ``` event_log.lead_id = tasks.lead_id ```  ``` event_log.organization_id = tasks.organization_id ```  ``` event_log.user_id = tasks.assigned_to ```  ``` event_log.user_id = tasks.created_by ```  ``` event_log.user_id = tasks.updated_by ``` |
| [custom\_fields](#custom-fields) | ``` event_log.organization_id = custom_fields.organization_id ```  ``` event_log.user_id = custom_fields.created_by ```  ``` event_log.user_id = custom_fields.updated_by ``` |
| [users](#users) | ``` event_log.organization_id = users.organizations ```  ``` event_log.user_id = users.id ``` |

event\_log table schema

|  |
| --- |
| **action**  STRING |
| **changed\_fields**  ARRAY |
| **data**  STRING |
| **date\_created**  DATE-TIME |
| **date\_updated**  DATE-TIME |
| **id**  STRING |
| **lead\_id**  STRING |
| **meta**  OBJECT This is a nested data structure:   - **request\_method**: STRING - **request\_path**: STRING |
| **object\_id**  STRING |
| **object\_type**  STRING |
| **organization\_id**  STRING |
| **previous\_data**  STRING |
| **request\_id**  STRING |
| **user\_id**  STRING |

### leads

The `leads` table contains info about the leads in your Close account.

Leads represent a company or organization and may contain contacts, tasks, opportunities, and activities. In Close, a lead is synonymous with “account” in other CRMs.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | date\_updated |
| **Useful links** | [Close API method](https://developer.close.io/#leads-list-or-search-for-leads "Opens in new tab: Close API method") |

leads table foreign keys

| Join leads with | on |
| --- | --- |
| [activities](#activities) | ``` leads.contacts.id = activities.contact_id ```  ``` leads.opportunities.contact_id = activities.contact_id ```  ``` leads.tasks.contact_id = activities.contact_id ```  ``` leads.id = activities.lead_id ```  ``` leads.contacts.lead_id = activities.lead_id ```  ``` leads.opportunities.lead_id = activities.lead_id ```  ``` leads.tasks.lead_id = activities.lead_id ```  ``` leads.contacts.organization_id = activities.organization_id ```  ``` leads.opportunities.organization_id = activities.organization_id ```  ``` leads.organization_id = activities.organization_id ```  ``` leads.tasks.organization_id = activities.organization_id ```  ``` leads.tasks.id = activities.task_id ```  ``` leads.contacts.created_by = activities.created_by ```  ``` leads.contacts.updated_by = activities.created_by ```  ``` leads.created_by = activities.created_by ```  ``` leads.opportunities.created_by = activities.created_by ```  ``` leads.opportunities.updated_by = activities.created_by ```  ``` leads.opportunities.user_id = activities.created_by ```  ``` leads.tasks.assigned_to = activities.created_by ```  ``` leads.tasks.created_by = activities.created_by ```  ``` leads.tasks.updated_by = activities.created_by ```  ``` leads.updated_by = activities.created_by ```  ``` leads.contacts.created_by = activities.updated_by ```  ``` leads.contacts.updated_by = activities.updated_by ```  ``` leads.created_by = activities.updated_by ```  ``` leads.opportunities.created_by = activities.updated_by ```  ``` leads.opportunities.updated_by = activities.updated_by ```  ``` leads.opportunities.user_id = activities.updated_by ```  ``` leads.tasks.assigned_to = activities.updated_by ```  ``` leads.tasks.created_by = activities.updated_by ```  ``` leads.tasks.updated_by = activities.updated_by ```  ``` leads.updated_by = activities.updated_by ```  ``` leads.contacts.created_by = activities.user_id ```  ``` leads.contacts.updated_by = activities.user_id ```  ``` leads.created_by = activities.user_id ```  ``` leads.opportunities.created_by = activities.user_id ```  ``` leads.opportunities.updated_by = activities.user_id ```  ``` leads.opportunities.user_id = activities.user_id ```  ``` leads.tasks.assigned_to = activities.user_id ```  ``` leads.tasks.created_by = activities.user_id ```  ``` leads.tasks.updated_by = activities.user_id ```  ``` leads.updated_by = activities.user_id ```  ``` leads.contacts.created_by = activities.task_assigned_to ```  ``` leads.contacts.updated_by = activities.task_assigned_to ```  ``` leads.created_by = activities.task_assigned_to ```  ``` leads.opportunities.created_by = activities.task_assigned_to ```  ``` leads.opportunities.updated_by = activities.task_assigned_to ```  ``` leads.opportunities.user_id = activities.task_assigned_to ```  ``` leads.tasks.assigned_to = activities.task_assigned_to ```  ``` leads.tasks.created_by = activities.task_assigned_to ```  ``` leads.tasks.updated_by = activities.task_assigned_to ```  ``` leads.updated_by = activities.task_assigned_to ```  ``` leads.contacts.created_by = activities.users ```  ``` leads.contacts.updated_by = activities.users ```  ``` leads.created_by = activities.users ```  ``` leads.opportunities.created_by = activities.users ```  ``` leads.opportunities.updated_by = activities.users ```  ``` leads.opportunities.user_id = activities.users ```  ``` leads.tasks.assigned_to = activities.users ```  ``` leads.tasks.created_by = activities.users ```  ``` leads.tasks.updated_by = activities.users ```  ``` leads.updated_by = activities.users ``` |
| [tasks](#tasks) | ``` leads.contacts.id = tasks.contact_id ```  ``` leads.opportunities.contact_id = tasks.contact_id ```  ``` leads.tasks.contact_id = tasks.contact_id ```  ``` leads.id = tasks.lead_id ```  ``` leads.contacts.lead_id = tasks.lead_id ```  ``` leads.opportunities.lead_id = tasks.lead_id ```  ``` leads.tasks.lead_id = tasks.lead_id ```  ``` leads.contacts.organization_id = tasks.organization_id ```  ``` leads.opportunities.organization_id = tasks.organization_id ```  ``` leads.organization_id = tasks.organization_id ```  ``` leads.tasks.organization_id = tasks.organization_id ```  ``` leads.tasks.id = tasks.id ```  ``` leads.contacts.created_by = tasks.assigned_to ```  ``` leads.contacts.updated_by = tasks.assigned_to ```  ``` leads.created_by = tasks.assigned_to ```  ``` leads.opportunities.created_by = tasks.assigned_to ```  ``` leads.opportunities.updated_by = tasks.assigned_to ```  ``` leads.opportunities.user_id = tasks.assigned_to ```  ``` leads.tasks.assigned_to = tasks.assigned_to ```  ``` leads.tasks.created_by = tasks.assigned_to ```  ``` leads.tasks.updated_by = tasks.assigned_to ```  ``` leads.updated_by = tasks.assigned_to ```  ``` leads.contacts.created_by = tasks.created_by ```  ``` leads.contacts.updated_by = tasks.created_by ```  ``` leads.created_by = tasks.created_by ```  ``` leads.opportunities.created_by = tasks.created_by ```  ``` leads.opportunities.updated_by = tasks.created_by ```  ``` leads.opportunities.user_id = tasks.created_by ```  ``` leads.tasks.assigned_to = tasks.created_by ```  ``` leads.tasks.created_by = tasks.created_by ```  ``` leads.tasks.updated_by = tasks.created_by ```  ``` leads.updated_by = tasks.created_by ```  ``` leads.contacts.created_by = tasks.updated_by ```  ``` leads.contacts.updated_by = tasks.updated_by ```  ``` leads.created_by = tasks.updated_by ```  ``` leads.opportunities.created_by = tasks.updated_by ```  ``` leads.opportunities.updated_by = tasks.updated_by ```  ``` leads.opportunities.user_id = tasks.updated_by ```  ``` leads.tasks.assigned_to = tasks.updated_by ```  ``` leads.tasks.created_by = tasks.updated_by ```  ``` leads.tasks.updated_by = tasks.updated_by ```  ``` leads.updated_by = tasks.updated_by ``` |
| [event\_log](#event-log) | ``` leads.id = event_log.lead_id ```  ``` leads.contacts.lead_id = event_log.lead_id ```  ``` leads.opportunities.lead_id = event_log.lead_id ```  ``` leads.tasks.lead_id = event_log.lead_id ```  ``` leads.contacts.organization_id = event_log.organization_id ```  ``` leads.opportunities.organization_id = event_log.organization_id ```  ``` leads.organization_id = event_log.organization_id ```  ``` leads.tasks.organization_id = event_log.organization_id ```  ``` leads.contacts.created_by = event_log.user_id ```  ``` leads.contacts.updated_by = event_log.user_id ```  ``` leads.created_by = event_log.user_id ```  ``` leads.opportunities.created_by = event_log.user_id ```  ``` leads.opportunities.updated_by = event_log.user_id ```  ``` leads.opportunities.user_id = event_log.user_id ```  ``` leads.tasks.assigned_to = event_log.user_id ```  ``` leads.tasks.created_by = event_log.user_id ```  ``` leads.tasks.updated_by = event_log.user_id ```  ``` leads.updated_by = event_log.user_id ``` |
| [custom\_fields](#custom-fields) | ``` leads.contacts.organization_id = custom_fields.organization_id ```  ``` leads.opportunities.organization_id = custom_fields.organization_id ```  ``` leads.organization_id = custom_fields.organization_id ```  ``` leads.tasks.organization_id = custom_fields.organization_id ```  ``` leads.contacts.created_by = custom_fields.created_by ```  ``` leads.contacts.updated_by = custom_fields.created_by ```  ``` leads.created_by = custom_fields.created_by ```  ``` leads.opportunities.created_by = custom_fields.created_by ```  ``` leads.opportunities.updated_by = custom_fields.created_by ```  ``` leads.opportunities.user_id = custom_fields.created_by ```  ``` leads.tasks.assigned_to = custom_fields.created_by ```  ``` leads.tasks.created_by = custom_fields.created_by ```  ``` leads.tasks.updated_by = custom_fields.created_by ```  ``` leads.updated_by = custom_fields.created_by ```  ``` leads.contacts.created_by = custom_fields.updated_by ```  ``` leads.contacts.updated_by = custom_fields.updated_by ```  ``` leads.created_by = custom_fields.updated_by ```  ``` leads.opportunities.created_by = custom_fields.updated_by ```  ``` leads.opportunities.updated_by = custom_fields.updated_by ```  ``` leads.opportunities.user_id = custom_fields.updated_by ```  ``` leads.tasks.assigned_to = custom_fields.updated_by ```  ``` leads.tasks.created_by = custom_fields.updated_by ```  ``` leads.tasks.updated_by = custom_fields.updated_by ```  ``` leads.updated_by = custom_fields.updated_by ``` |
| [users](#users) | ``` leads.contacts.organization_id = users.organizations ```  ``` leads.opportunities.organization_id = users.organizations ```  ``` leads.organization_id = users.organizations ```  ``` leads.tasks.organization_id = users.organizations ```  ``` leads.contacts.created_by = users.id ```  ``` leads.contacts.updated_by = users.id ```  ``` leads.created_by = users.id ```  ``` leads.opportunities.created_by = users.id ```  ``` leads.opportunities.updated_by = users.id ```  ``` leads.opportunities.user_id = users.id ```  ``` leads.tasks.assigned_to = users.id ```  ``` leads.tasks.created_by = users.id ```  ``` leads.tasks.updated_by = users.id ```  ``` leads.updated_by = users.id ``` |

leads table schema

|  |
| --- |
| **addresses**  ARRAY This is a nested data structure:   - **address\_1**: STRING - **address\_2**: STRING - **city**: STRING - **country**: STRING - **label**: STRING - **state**: STRING - **zipcode**: STRING |
| **contacts**  ARRAY This is a nested data structure:   - **created\_by**: STRING - **date\_created**: DATE-TIME - **date\_updated**: DATE-TIME - **display\_name**: STRING - **emails**: ARRAY, which is also a nested data structure.   - **email**: STRING   - **type**: STRING - **id**: STRING - **integration\_links**: ARRAY, which is also a nested data structure.   - **name**: STRING   - **url**: STRING - **lead\_id**: STRING - **name**: STRING - **organization\_id**: STRING - **phones**: ARRAY, which is also a nested data structure.   - **phone**: STRING   - **phone\_formatted**: STRING   - **type**: STRING - **title**: STRING - **updated\_by**: STRING - **urls**: ARRAY, which is also a nested data structure.   - **type**: STRING   - **url**: STRING |
| **created\_by**  STRING |
| **created\_by\_name**  STRING |
| **custom\_fields**  ARRAY This is a nested data structure:   - **id**: STRING - **value**: STRING, NUMBER, BOOLEAN, OBJECT, ARRAY, which is also a nested data structure. |
| **date\_created**  DATE-TIME |
| **date\_updated**  DATE-TIME |
| **description**  STRING |
| **display\_name**  STRING |
| **html\_url**  STRING |
| **id**  STRING |
| **integration\_links**  ARRAY This is a nested data structure:   - **name**: INTEGER - **url**: STRING |
| **name**  STRING |
| **opportunities**  ARRAY This is a nested data structure:   - **name**: INTEGER - **opportunities**: ARRAY, which is also a nested data structure.   - **confidence**: INTEGER   - **contact\_id**: STRING   - **contact\_name**: STRING   - **created\_by**: STRING   - **date\_created**: DATE-TIME   - **date\_lost**: DATE-TIME   - **date\_updated**: DATE-TIME   - **date\_won**: DATE-TIME   - **id**: STRING   - **integration\_links**: ARRAY, which is also a nested data structure.     - **name**: STRING     - **url**: STRING   - **lead\_id**: STRING   - **lead\_name**: STRING   - **note**: STRING   - **organization\_id**: STRING   - **status\_id**: STRING   - **status\_label**: STRING   - **status\_type**: STRING   - **updated\_by**: STRING   - **updated\_by\_name**: STRING   - **user\_id**: STRING   - **user\_name**: STRING   - **value**: INTEGER   - **value\_currency**: STRING   - **value\_formatted**: STRING   - **value\_period**: STRING |
| **organization\_id**  STRING |
| **status\_id**  STRING |
| **status\_label**  STRING |
| **tasks**  ARRAY This is a nested data structure:   - **type**: STRING - **assigned\_to**: STRING - **assigned\_to\_name**: STRING - **contact\_id**: STRING - **contact\_name**: STRING - **created\_by**: STRING - **created\_by\_name**: STRING - **date**: DATE-TIME - **date\_crated**: DATE-TIME - **date\_updated**: DATE-TIME - **due\_date**: DATE-TIME - **id**: STRING - **is\_complete**: INTEGER, BOOLEAN - **is\_dateless**: INTEGER, BOOLEAN - **lead\_id**: STRING - **lead\_name**: STRING - **object\_id**: STRING - **object\_type**: STRING - **organization\_id**: STRING - **text**: STRING - **updated\_by**: STRING - **updated\_by\_name**: STRING - **view**: STRING |
| **updated\_by**  STRING |
| **updated\_by\_name**  STRING |
| **url**  STRING |

### tasks

The `tasks` table contains info about the tasks in your Close account. Tasks are action items with a given date that are assigned to a sales rep.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | date\_updated |
| **Useful links** | [Close API method](https://developer.close.io/#tasks-list-or-filter-tasks "Opens in new tab: Close API method") |

tasks table foreign keys

| Join tasks with | on |
| --- | --- |
| [activities](#activities) | ``` tasks.contact_id = activities.contact_id ```  ``` tasks.lead_id = activities.lead_id ```  ``` tasks.organization_id = activities.organization_id ```  ``` tasks.id = activities.task_id ```  ``` tasks.assigned_to = activities.created_by ```  ``` tasks.created_by = activities.created_by ```  ``` tasks.updated_by = activities.created_by ```  ``` tasks.assigned_to = activities.updated_by ```  ``` tasks.created_by = activities.updated_by ```  ``` tasks.updated_by = activities.updated_by ```  ``` tasks.assigned_to = activities.user_id ```  ``` tasks.created_by = activities.user_id ```  ``` tasks.updated_by = activities.user_id ```  ``` tasks.assigned_to = activities.task_assigned_to ```  ``` tasks.created_by = activities.task_assigned_to ```  ``` tasks.updated_by = activities.task_assigned_to ```  ``` tasks.assigned_to = activities.users ```  ``` tasks.created_by = activities.users ```  ``` tasks.updated_by = activities.users ``` |
| [leads](#leads) | ``` tasks.contact_id = leads.contacts.id ```  ``` tasks.contact_id = leads.opportunities.contact_id ```  ``` tasks.contact_id = leads.tasks.contact_id ```  ``` tasks.lead_id = leads.id ```  ``` tasks.lead_id = leads.contacts.lead_id ```  ``` tasks.lead_id = leads.opportunities.lead_id ```  ``` tasks.lead_id = leads.tasks.lead_id ```  ``` tasks.organization_id = leads.contacts.organization_id ```  ``` tasks.organization_id = leads.opportunities.organization_id ```  ``` tasks.organization_id = leads.organization_id ```  ``` tasks.organization_id = leads.tasks.organization_id ```  ``` tasks.id = leads.tasks.id ```  ``` tasks.assigned_to = leads.contacts.created_by ```  ``` tasks.created_by = leads.contacts.created_by ```  ``` tasks.updated_by = leads.contacts.created_by ```  ``` tasks.assigned_to = leads.contacts.updated_by ```  ``` tasks.created_by = leads.contacts.updated_by ```  ``` tasks.updated_by = leads.contacts.updated_by ```  ``` tasks.assigned_to = leads.created_by ```  ``` tasks.created_by = leads.created_by ```  ``` tasks.updated_by = leads.created_by ```  ``` tasks.assigned_to = leads.opportunities.created_by ```  ``` tasks.created_by = leads.opportunities.created_by ```  ``` tasks.updated_by = leads.opportunities.created_by ```  ``` tasks.assigned_to = leads.opportunities.updated_by ```  ``` tasks.created_by = leads.opportunities.updated_by ```  ``` tasks.updated_by = leads.opportunities.updated_by ```  ``` tasks.assigned_to = leads.opportunities.user_id ```  ``` tasks.created_by = leads.opportunities.user_id ```  ``` tasks.updated_by = leads.opportunities.user_id ```  ``` tasks.assigned_to = leads.tasks.assigned_to ```  ``` tasks.created_by = leads.tasks.assigned_to ```  ``` tasks.updated_by = leads.tasks.assigned_to ```  ``` tasks.assigned_to = leads.tasks.created_by ```  ``` tasks.created_by = leads.tasks.created_by ```  ``` tasks.updated_by = leads.tasks.created_by ```  ``` tasks.assigned_to = leads.tasks.updated_by ```  ``` tasks.created_by = leads.tasks.updated_by ```  ``` tasks.updated_by = leads.tasks.updated_by ```  ``` tasks.assigned_to = leads.updated_by ```  ``` tasks.created_by = leads.updated_by ```  ``` tasks.updated_by = leads.updated_by ``` |
| [event\_log](#event-log) | ``` tasks.lead_id = event_log.lead_id ```  ``` tasks.organization_id = event_log.organization_id ```  ``` tasks.assigned_to = event_log.user_id ```  ``` tasks.created_by = event_log.user_id ```  ``` tasks.updated_by = event_log.user_id ``` |
| [custom\_fields](#custom-fields) | ``` tasks.organization_id = custom_fields.organization_id ```  ``` tasks.assigned_to = custom_fields.created_by ```  ``` tasks.created_by = custom_fields.created_by ```  ``` tasks.updated_by = custom_fields.created_by ```  ``` tasks.assigned_to = custom_fields.updated_by ```  ``` tasks.created_by = custom_fields.updated_by ```  ``` tasks.updated_by = custom_fields.updated_by ``` |
| [users](#users) | ``` tasks.organization_id = users.organizations ```  ``` tasks.assigned_to = users.id ```  ``` tasks.created_by = users.id ```  ``` tasks.updated_by = users.id ``` |

tasks table schema

|  |
| --- |
| **\_type**  STRING |
| **assigned\_to**  STRING |
| **assigned\_to\_name**  STRING |
| **body\_preview**  STRING |
| **contact\_id**  STRING |
| **contact\_name**  STRING |
| **created\_by**  STRING |
| **created\_by\_name**  STRING |
| **date**  DATE-TIME |
| **date\_created**  DATE-TIME |
| **date\_updated**  DATE-TIME |
| **due\_date**  DATE-TIME |
| **email\_id**  STRING |
| **emails**  ARRAY |
| **id**  STRING |
| **is\_complete**  BOOLEAN |
| **is\_dateless**  BOOLEAN |
| **lead\_id**  STRING |
| **lead\_name**  STRING |
| **local\_phone**  STRING |
| **object\_id**  STRING |
| **object\_type**  STRING |
| **opportunity\_note**  STRING |
| **opportunity\_value**  INTEGER |
| **opportunity\_value\_currency**  STRING |
| **opportunity\_value\_formatted**  STRING |
| **opportunity\_value\_period**  STRING |
| **organization\_id**  STRING |
| **phone**  STRING |
| **phone\_formatted**  STRING |
| **phone\_number\_description**  STRING |
| **recording\_url**  STRING |
| **remote\_phone**  STRING |
| **remote\_phone\_description**  STRING |
| **remote\_phone\_formatted**  STRING |
| **subject**  STRING |
| **text**  STRING |
| **updated\_by**  STRING |
| **updated\_by\_name**  STRING |
| **view**  STRING |
| **voicemail\_duration**  INTEGER |
| **voicemail\_url**  STRING |

### users

The `users` table contains info about the users in your Close account.

In Close, users are typically your co-workers and sales reps, or those inside your company.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | date\_updated |
| **Useful links** | [Close API method](https://developer.close.io/#users-list-all-the-users-who-are-members-of-the-same-organizations-as-you-are "Opens in new tab: Close API method") |

users table foreign keys

| Join users with | on |
| --- | --- |
| [activities](#activities) | ``` users.organizations = activities.organization_id ```  ``` users.id = activities.created_by ```  ``` users.id = activities.updated_by ```  ``` users.id = activities.user_id ```  ``` users.id = activities.task_assigned_to ```  ``` users.id = activities.users ``` |
| [custom\_fields](#custom-fields) | ``` users.organizations = custom_fields.organization_id ```  ``` users.id = custom_fields.created_by ```  ``` users.id = custom_fields.updated_by ``` |
| [event\_log](#event-log) | ``` users.organizations = event_log.organization_id ```  ``` users.id = event_log.user_id ``` |
| [leads](#leads) | ``` users.organizations = leads.contacts.organization_id ```  ``` users.organizations = leads.opportunities.organization_id ```  ``` users.organizations = leads.organization_id ```  ``` users.organizations = leads.tasks.organization_id ```  ``` users.id = leads.contacts.created_by ```  ``` users.id = leads.contacts.updated_by ```  ``` users.id = leads.created_by ```  ``` users.id = leads.opportunities.created_by ```  ``` users.id = leads.opportunities.updated_by ```  ``` users.id = leads.opportunities.user_id ```  ``` users.id = leads.tasks.assigned_to ```  ``` users.id = leads.tasks.created_by ```  ``` users.id = leads.tasks.updated_by ```  ``` users.id = leads.updated_by ``` |
| [tasks](#tasks) | ``` users.organizations = tasks.organization_id ```  ``` users.id = tasks.assigned_to ```  ``` users.id = tasks.created_by ```  ``` users.id = tasks.updated_by ``` |

users table schema

|  |
| --- |
| **date\_created**  DATE-TIME |
| **date\_updated**  DATE-TIME |
| **email**  STRING |
| **first\_name**  STRING |
| **id**  STRING |
| **image**  STRING |
| **last\_name**  STRING |
| **last\_used\_timezone**  STRING |
| **organizations**  ARRAY |
