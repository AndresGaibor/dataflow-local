---
title: "Mixpanel"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Mixpanel.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Mixpanel

Mixpanel is a real-time analytics platform that helps companies measure and optimize user engagement.

For more information about the API, see the [Mixpanel Query API](https://developer.mixpanel.com/reference/query-api) and [Event Export API](https://developer.mixpanel.com/reference/raw-data-export-api).

See the [Schema](#Schema) section for a list of objects available for replication.

## Mixpanel integration summary

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To obtain the project timezone and API secret:

1. Make sure you have the Admin privileges in Mixpanel. You need them to access the API secret.
2. Log into your Mixpanel account.
3. In the dropdown menu in the upper left corner of the page, select the project you want to replicate data from.
4. Hover over the Settings icon in the upper right corner. In the Project Settings section, click the name of your project.
5. Copy the Project Timezone and API Secret.

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
| API Secret | API secret. |
| Attribution Window (days) | Enter the number of days you want your tables’ attribution window to be. |
| Project Timezone | Project timezone. |
| Export Events (optional) | Enter the events separated by a comma. Example: `Page Viewed, Signed Up`. |
| Select Properties By Default | To capture new properties automatically in the `events` and `engage` tables, select the check box. Otherwise, new properties will be ignored. |
| EU Residency | To process and store your customers’ personal data in Europe, select the check box. |

## Schema

Information note

**Mixpanel free plan**

The `engage` and `export` tables are not available if you are using the free Mixpanel plan.

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### annotations

The `annotations` table contains info about annotations.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | date |
| **Useful links** | [Mixpanel documentation](https://developer.mixpanel.com/reference/overview-1) |

annotations table foreign keys

| Join annotations with | on |
| --- | --- |
| [cohorts](#cohorts) | ``` annotations.project_id = cohorts.project_id ``` |

annotations table schema

|  |
| --- |
| **date**  DATE-TIME |
| **description**  STRING |
| **id**  INTEGER |
| **project\_id**  INTEGER |

### cohort\_members

The `cohort_members` table contains info about the cohorts user profiles belong to.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | cohort\_id  distinct\_id |
| **Useful links** | [Mixpanel documentation](https://developer.mixpanel.com/reference/engage-query)  [Mixpanel API method](https://developer.mixpanel.com/reference/cohorts-list "Opens in new tab: Mixpanel API method") |

cohort\_members table foreign keys

| Join cohort\_members with | on |
| --- | --- |
| [cohorts](#cohorts) | ``` cohort_members.cohort_id = cohorts.id ``` |

cohort\_members table schema

|  |
| --- |
| **cohort\_id**  INTEGER |
| **distinct\_id**  STRING |

### cohorts

The `cohorts` table contains info about the cohorts in a Mixpanel project.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Mixpanel API method](https://developer.mixpanel.com/reference/cohorts-list "Opens in new tab: Mixpanel API method") |

cohorts table foreign keys

| Join cohorts with | on |
| --- | --- |
| [cohort\_members](#cohort-members) | ``` cohorts.id = cohort_members.cohort_id ``` |
| [annotations](#annotations) | ``` cohorts.project_id = annotations.project_id ``` |

cohorts table schema

|  |
| --- |
| **count**  INTEGER |
| **created**  DATE-TIME |
| **description**  STRING |
| **id**  INTEGER |
| **is\_visible**  INTEGER |
| **name**  STRING |
| **project\_id**  INTEGER |

### engage

The `engage` table contains info about user profiles.

The schema for this table is dynamic, meaning that the detected columns are dependent upon the properties provided upon upload in Mixpanel. For every property available in Mixpanel for `engage` records, a column will be displayed in the integration’s **Tables to Replicate** tab.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | distinct\_id |
| **Useful links** | [Mixpanel API method](https://developer.mixpanel.com/Content/data-export-api#section-engage "Opens in new tab: Mixpanel API method") |

engage table schema

|  |
| --- |
| **distinct\_id**  STRING |

### export

The `export` table contains “raw data dumps” of tracked events. The API endpoint for EU region servers will return a `200 terminated early` error code.

#### Table schema

The schema for this table is dynamic, meaning that the detected columns are dependent upon the properties provided upon upload in Mixpanel. For every property available in Mixpanel for `export` records, a column will be displayed in the integration’s **Tables to Replicate** tab.

#### Replication with attribution window

This table is replicated using the **Attribution Window** value defined in the integration’s settings page. Refer to the [Replication section](#attribution-windows-extraction) for more info.

#### Distinct events and loading behavior

As a Primary Key is not used for this table, data will be loaded using Append-Only loading. This means you may see duplicate records in your destination, which requires a querying strategy that selects the latest version of each record.

This approach allows to track events without a `distinct_id`. In Mixpanel, `distinct_id` [is used to identify a unique user](https://help.mixpanel.com/hc/en-us/articles/115004509406-Distinct-IDs-):

> Mixpanel’s client-side tracking libraries automatically assign a distinct\_id to a user when they first visit a website or an application that has Mixpanel installed. Distinct\_id should not contain any special characters such as forward slashes, as it will break the URL.
> Distinct\_ids can and often should be sent in server-side implementations as well.

In order to replicate records’ `distinct_id` attributes, your server-side Mixpanel implementation must send them with tracked events. If the server-side implementation doesn’t do this, this attribute will be `null`.

Previous versions of Mixpanel integration used `distinct_id` as part of a composite Primary Key for this table. However, due to the possibility of this attribute being `null`, a Primary Key is not used for this table, as `null` values in Primary Key columns will prevent successful Extraction.

When working with `exports` data in your destination, you’ll need to use a querying strategy that accounts for the Append-Only loading used by this table. We recommend using the following columns to de-duplicate records, along with the approach outlined in the Querying Append-Only tables guide:

- `distinct_id`
- `event`
- `time`

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Loading Behavior** | Append-Only |
| **Replication Key** | time |
| **Useful links** | [Mixpanel API method](https://developer.mixpanel.com/reference/raw-event-export "Opens in new tab: Mixpanel API method") |

export table schema

|  |
| --- |
| **dataset**  STRING |
| **distinct\_id**  STRING |
| **event**  STRING |
| **labels**    ARRAY |
| **sampling\_factor**  INTEGER |
| **time**  DATE-TIME |

### funnels

The `funnels` table contains data about your Mixpanel funnels, segmented by funnel and day.

**Note**: This table is replicated using the **Attribution Window** value defined in the integration’s settings page. Refer to the [Replication section](#attribution-windows-extraction) for more info.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | funnel\_id  date |
| **Replication Key** | date |
| **Useful links** | [Mixpanel API method](https://developer.mixpanel.com/Content/data-export-api#section-funnels "Opens in new tab: Mixpanel API method") |

funnels table schema

|  |
| --- |
| **analysis**  OBJECT This is a nested data structure:   - **completion**: INTEGER - **starting\_amount**: INTEGER - **steps**: INTEGER - **worst**: INTEGER |
| **date**  DATE |
| **datetime**  DATE-TIME |
| **funnel\_id**  INTEGER |
| **name**  STRING |
| **steps**    ARRAY This is a nested data structure:   - **avg\_time**: NUMBER - **count**: INTEGER - **event**: STRING - **goal**: STRING - **overall\_conv\_ratio**: NUMBER - **step\_conv\_ratio**: NUMBER - **step\_label**: NUMBER - **time\_buckets\_from\_prev**: OBJECT, which is also a nested data structure. **buckets**, ARRAY    - **higher**: INTEGER   - **lower**: INTEGER - **time\_buckets\_from\_start**: OBJECT, which is also a nested data structure. **buckets**, ARRAY    - **higher**: INTEGER   - **lower**: INTEGER |

### revenue

The `revenue` table contains info about revenue, segmented by day. The API endpoint for EU region servers will return a `400 bad requests (Timeout Error)` code.

**Note**: This table is replicated using the **Attribution Window** value defined in the integration’s settings page. Refer to the [Replication section](#attribution-windows-extraction) for more info.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | date |
| **Replication Key** | date |

revenue table schema

|  |
| --- |
| **amount**  NUMBER |
| **count**  INTEGER |
| **date**  DATE |
| **datetime**  DATE-TIME |
| **paid\_count**  INTEGER |
