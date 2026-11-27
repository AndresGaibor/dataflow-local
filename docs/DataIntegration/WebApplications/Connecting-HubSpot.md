---
title: "HubSpot"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-HubSpot.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# HubSpot

HubSpot is an AI-powered customer platform with all the software, integrations, and resources you need to connect your marketing, sales, and customer service.

It replicates data using the [HubSpot REST API](https://developers.hubspot.com/docs/api-reference/overview).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To retrieve your access token:

1. Log into [HubSpot](https://app.hubspot.com/myaccounts).
2. Create a private app by following [HubSpot's documentation](https://developers.hubspot.com/docs/apps/legacy-apps/private-apps/overview#create-a-private-app).

   You must have a HubSpot super admin role to create a private app.
3. Once your private app is created, navigate to Development.
4. In the left sidebar menu, navigate to Legacy apps.
5. Click the name of your app.
6. Click the Auth tab > Show token to reveal your access token.
7. Copy and paste your access token into a secured file.

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
| Personal Access Token | Personal access token. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

### Custom HubSpot field replication

Custom object properties, or fields, are supported by HubSpot integration. It will query the `properties` list for each object and, if custom fields are available through HubSpot’s API, replicate them to your destination.

The data types of these fields will be the same as the data type in HubSpot. For example: A custom field containing `date` data will be a `date` field in your destination.

This is applicable to any object that supports custom fields in HubSpot.

### HubSpot date/date-time values & UNIX timestamps

HubSpot uses UNIX-formatted timestamps in milliseconds to store `date` and `datetime` data. For more information, see [Charts overview](https://developers.hubspot.com/docs/apps/developer-platform/add-features/ui-extensibility/ui-components/standard-components/charts/overview). It doesn’t perform any transformation during the replication process, meaning these values won’t be converted to timestamps before they’re loaded into your destination.

To account for this, consider creating a user-defined function to perform the conversion or building views on top of the raw data.

Depending on your destination, table and column names may not appear as they are outlined below.

### campaigns

The `campaigns` table contains info about the campaigns in your HubSpot account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [HubSpot API method](https://developers.hubspot.com/docs/api-reference/legacy/marketing/marketing-emails/guide "Opens in new tab: HubSpot API method") |

campaigns table foreign keys

| Join campaigns with | on |
| --- | --- |
| [email\_events](#email-events) | ``` campaigns.id = email_events.emailCampaignId ``` |
| [forms](#forms) | ``` campaigns.id = forms.leadNurturingCampaignId ``` |

campaigns table schema

|  |
| --- |
| **appId**  INTEGER |
| **appName**  STRING |
| **contentId**  INTEGER |
| **counters**  OBJECT This is a nested data structure:   - bounce: INTEGER - click: INTEGER - deferred: INTEGER - delievered: INTEGER - delivered: INTEGER - dropped: INTEGER - forward: INTEGER - mta\_dropped: INTEGER - open: INTEGER - print: INTEGER - processed: INTEGER - reply: INTEGER - sent: INTEGER - spamreport: INTEGER - statuschange: INTEGER - suppressed: INTEGER - unsubscribed: INTEGER |
| **id**  INTEGER |
| **name**  STRING |
| **numIncluded**  INTEGER |
| **numQueued**  INTEGER |
| **subType**  STRING |
| **subject**  STRING |
| **type**  STRING |

### companies

The `companies` table contains info about the companies your HubSpot contacts belong to.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | companyId |
| **Useful links** | [HubSpot API method](https://developers.hubspot.com/docs/api-reference/legacy/crm/objects/companies/guide "Opens in new tab: HubSpot API method") |

companies table foreign keys

| Join companies with | on |
| --- | --- |
| [contacts\_by\_company](#contacts-by-company) | ``` companies.companyId = contacts_by_company.company-id ``` |
| [deals](#deals) | ``` companies.companyId = deals.associations.associatedCompanyIds ```  ``` companies.portalId = deals.portalId ``` |
| [engagements](#engagements) | ``` companies.companyId = engagements.associations.companyIds ```  ``` companies.portalId = engagements.engagement.portalId ``` |
| [contact\_lists](#contact-lists) | ``` companies.portalId = contact_lists.portalId ``` |
| [contacts](#contacts) | ``` companies.portalId = contacts.portal-id ```  ``` companies.portalId = contacts.form-submissions.portal-id ``` |
| [email\_events](#email-events) | ``` companies.portalId = email_events.portalId ``` |
| [forms](#forms) | ``` companies.portalId = forms.portalId ``` |
| [owners](#owners) | ``` companies.portalId = owners.portalId ```  ``` companies.portalId = owners.remoteList.portalId ``` |
| [subscription\_changes](#subscription-changes) | ``` companies.portalId = subscription_changes.portalId ```  ``` companies.portalId = subscription_changes.changes.portalId ``` |

companies table schema

|  |
| --- |
| **companyId**  INTEGER |
| **portalId**  INTEGER |

### contact\_lists

The `contact_lists` table contains info about the contacts lists in your HubSpot account. Contact lists are used to segment contacts into groups, and there are two types: dynamic (smart lists) and static.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | listId |
| **Replication Key** | updatedAt |
| **Useful links** | [HubSpot API method](https://developers.hubspot.com/docs/api-reference/legacy/crm/lists/guide "Opens in new tab: HubSpot API method") |

contact\_lists table foreign keys

| Join contact\_lists with | on |
| --- | --- |
| [contacts](#contacts) | ``` contact_lists.listId = contacts.list-memberships.internal-list-id ```  ``` contact_lists.portalId = contacts.portal-id ```  ``` contact_lists.portalId = contacts.form-submissions.portal-id ``` |
| [engagements](#engagements) | ``` contact_lists.listId = engagements.associations.contactIds ```  ``` contact_lists.portalId = engagements.engagement.portalId ``` |
| [companies](#companies) | ``` contact_lists.portalId = companies.portalId ``` |
| [deals](#deals) | ``` contact_lists.portalId = deals.portalId ``` |
| [email\_events](#email-events) | ``` contact_lists.portalId = email_events.portalId ``` |
| [forms](#forms) | ``` contact_lists.portalId = forms.portalId ``` |
| [owners](#owners) | ``` contact_lists.portalId = owners.portalId ```  ``` contact_lists.portalId = owners.remoteList.portalId ``` |
| [subscription\_changes](#subscription-changes) | ``` contact_lists.portalId = subscription_changes.portalId ```  ``` contact_lists.portalId = subscription_changes.changes.portalId ``` |

contact\_lists table schema

|  |
| --- |
| **processingType**  STRING |
| **objectTypeId**  STRING |
| **listId**  STRING |
| **processingStatus**  STRING |
| **listVersion**  STRING |
| **additionalProperties**  OBJECT This is a nested data structure:   - hs\_folder\_name: STRING - hs\_last\_record\_added\_at: STRING - hs\_last\_record\_removed\_at: STRING - hs\_list\_reference\_count: STRING - hs\_list\_size: STRING |
| **updatedById**  STRING |
| **createdById**  STRING |
| **name**  STRING |
| **createdAt**  STRING |
| **updatedAt**  STRING |
| **filtersUpdatedAt**  STRING |
| **deletedAt**  STRING |

### contacts

The `contacts` table contains info about individual contacts in HubSpot.

### Contact properties

If properties have been set for the contact, additional fields beginning with `properties__` will be included in the table. **Note**: Contacts will only have an entry for a property if that property has been set for the contact’s record.

HubSpot always types the value of `properties` fields as `STRING` despite the property type. [Refer to HubSpot’s documentation for more info](https://developers.hubspot.com/docs/api-reference/legacy/crm/properties/get-property#required-scopes).

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | vid |
| **Replication Key** | versionTimestamp |
| **Useful links** | [HubSpot API method](https://developers.hubspot.com/Content/methods/contacts/get_contacts "Opens in new tab: HubSpot API method") |

contacts table foreign keys

| Join contacts with | on |
| --- | --- |
| [contacts\_by\_company](#contacts-by-company) | ``` contacts.canonical-vid = contacts_by_company.contact-id ``` |
| [contact\_lists](#contact-lists) | ``` contacts.list-memberships.internal-list-id = contact_lists.listId ```  ``` contacts.portal-id = contact_lists.portalId ```  ``` contacts.form-submissions.portal-id = contact_lists.portalId ``` |
| [engagements](#engagements) | ``` contacts.list-memberships.internal-list-id = engagements.associations.contactIds ```  ``` contacts.portal-id = engagements.engagement.portalId ```  ``` contacts.form-submissions.portal-id = engagements.engagement.portalId ``` |
| [forms](#forms) | ``` contacts.form-submissions.form-id = forms.guid ```  ``` contacts.portal-id = forms.portalId ```  ``` contacts.form-submissions.portal-id = forms.portalId ``` |
| [companies](#companies) | ``` contacts.portal-id = companies.portalId ```  ``` contacts.form-submissions.portal-id = companies.portalId ``` |
| [deals](#deals) | ``` contacts.portal-id = deals.portalId ```  ``` contacts.form-submissions.portal-id = deals.portalId ``` |
| [email\_events](#email-events) | ``` contacts.portal-id = email_events.portalId ```  ``` contacts.form-submissions.portal-id = email_events.portalId ``` |
| [owners](#owners) | ``` contacts.portal-id = owners.portalId ```  ``` contacts.form-submissions.portal-id = owners.portalId ```  ``` contacts.portal-id = owners.remoteList.portalId ```  ``` contacts.form-submissions.portal-id = owners.remoteList.portalId ``` |
| [subscription\_changes](#subscription-changes) | ``` contacts.portal-id = subscription_changes.portalId ```  ``` contacts.form-submissions.portal-id = subscription_changes.portalId ```  ``` contacts.portal-id = subscription_changes.changes.portalId ```  ``` contacts.form-submissions.portal-id = subscription_changes.changes.portalId ``` |

contacts table schema

|  |
| --- |
| **id**  STRING |
| **createdAt**  STRING |
| **updatedAt**  STRING |
| **archived**  BOOLEAN |
| **associations**  OBJECT This is a nested data structure:   - contacts: OBJECT, which is also a nested data structure.   - results: ARRAY, which is also a nested data structure.     - id: STRING     - type: STRING - deals: OBJECT, which is also a nested data structure.   - results: ARRAY, which is also a nested data structure.     - id: STRING     - type: STRING - tickets: OBJECT, which is also a nested data structure.   - results: ARRAY, which is also a nested data structure.     - id: STRING     - type: STRING |
| **objectWriteTraceId**  STRING |

### contacts\_by\_company

The `contacts_by_company` table contains contact and company ID pairs, allowing you to join contacts to relevant company data.

To replicate data from this table, you must also select the parent `companies` table.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | contact-id  company-id |
| **Useful links** |  |

contacts\_by\_company table foreign keys

| Join contacts\_by\_company with | on |
| --- | --- |
| [contacts](#contacts) | ``` contacts_by_company.contact-id = contacts.canonical-vid ``` |
| [companies](#companies) | ``` contacts_by_company.company-id = companies.companyId ``` |
| [deals](#deals) | ``` contacts_by_company.company-id = deals.associations.associatedCompanyIds ``` |
| [engagements](#engagements) | ``` contacts_by_company.company-id = engagements.associations.companyIds ``` |

contacts\_by\_company table schema

|  |
| --- |
| **company-id**  INTEGER |
| **contact-id**  INTEGER |

### custom\_objects

Tables for custom CRM objects in your HubSpot account will have the same name as the object. For example, if you have a custom object named `cars`, the table will be named `cars`.

The fields listed below are standard fields; they are included in every custom object table. A field will be added for each property you select when configuring the table. The property names will be prefixed with `property_`. For example, if you have a property named `model`, it will appear as `property_model`.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** |  |

custom\_objects table schema

|  |
| --- |
| **archived**  BOOLEAN |
| **associations**  OBJECT This is a nested data structure:   - calls: OBJECT, which is also a nested data structure.   - results: ARRAY, which is also a nested data structure.     - id: STRING     - type: STRING - companies: OBJECT, which is also a nested data structure.   - results: ARRAY, which is also a nested data structure.     - id: STRING     - type: STRING - contacts: OBJECT, which is also a nested data structure.   - results: ARRAY, which is also a nested data structure.     - id: STRING     - type: STRING - conversation\_session: OBJECT, which is also a nested data structure.   - results: ARRAY, which is also a nested data structure.     - id: STRING     - type: STRING - deals: OBJECT, which is also a nested data structure.   - results: ARRAY, which is also a nested data structure.     - id: STRING     - type: STRING - emails: OBJECT, which is also a nested data structure.   - results: ARRAY, which is also a nested data structure.     - id: STRING     - type: STRING - meetings: OBJECT, which is also a nested data structure.   - results: ARRAY, which is also a nested data structure.     - id: STRING     - type: STRING - notes: OBJECT, which is also a nested data structure.   - results: ARRAY, which is also a nested data structure.     - id: STRING     - type: STRING - products: OBJECT, which is also a nested data structure.   - results: ARRAY, which is also a nested data structure.     - id: STRING     - type: STRING - tasks: OBJECT, which is also a nested data structure.   - results: ARRAY, which is also a nested data structure.     - id: STRING     - type: STRING - tickets: OBJECT, which is also a nested data structure.   - results: ARRAY, which is also a nested data structure.     - id: STRING     - type: STRING |
| **createdAt**  DATE-TIME |
| **id**  STRING |
| **updatedAt**  DATE-TIME |

### deal\_pipelines

The `deal_pipelines` table contains info about the `deal stage` and `pipeline` properties.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | pipelineId |
| **Useful links** | [HubSpot API method](https://developers.hubspot.com/docs/methods/deal-pipelines/get-all-deal-pipelines "Opens in new tab: HubSpot API method") |

deal\_pipelines table schema

|  |
| --- |
| **active**  BOOLEAN |
| **displayOrder**  INTEGER |
| **label**  STRING |
| **pipelineId**  STRING |
| **stages**  ARRAY This is a nested data structure:   - active: BOOLEAN - closedWon: BOOLEAN - displayOrder: INTEGER - label: STRING - probability: NUMBER - stageId: STRING |
| **staticDefault**  BOOLEAN |

### deals

The `deals` table contains info about the deals in a HubSpot portal.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | dealId |
| **Useful links** | [HubSpot API method](https://developers.hubspot.com/docs/api-reference/legacy/crm/objects/deals/guide "Opens in new tab: HubSpot API method") |

deals table foreign keys

| Join deals with | on |
| --- | --- |
| [companies](#companies) | ``` deals.associations.associatedCompanyIds = companies.companyId ```  ``` deals.portalId = companies.portalId ``` |
| [contacts\_by\_company](#contacts-by-company) | ``` deals.associations.associatedCompanyIds = contacts_by_company.company-id ``` |
| [engagements](#engagements) | ``` deals.associations.associatedCompanyIds = engagements.associations.companyIds ```  ``` deals.dealId = engagements.associations.dealIds ```  ``` deals.associations.associatedDealIds = engagements.associations.dealIds ```  ``` deals.portalId = engagements.engagement.portalId ``` |
| [contact\_lists](#contact-lists) | ``` deals.portalId = contact_lists.portalId ``` |
| [contacts](#contacts) | ``` deals.portalId = contacts.portal-id ```  ``` deals.portalId = contacts.form-submissions.portal-id ``` |
| [email\_events](#email-events) | ``` deals.portalId = email_events.portalId ``` |
| [forms](#forms) | ``` deals.portalId = forms.portalId ``` |
| [owners](#owners) | ``` deals.portalId = owners.portalId ```  ``` deals.portalId = owners.remoteList.portalId ``` |
| [subscription\_changes](#subscription-changes) | ``` deals.portalId = subscription_changes.portalId ```  ``` deals.portalId = subscription_changes.changes.portalId ``` |

deals table schema

|  |
| --- |
| **associations**  OBJECT This is a nested data structure:   - associatedCompanyIds: ARRAY - associatedDealIds! ARRAY - associatedVids: ARRAY |
| **dealId**  INTEGER |
| **isDeleted**  BOOLEAN |
| **portalId**  INTEGER |

### email\_events

The `email_events` table contains info about email events and how recipients interact with content.

#### Email events and HubSpot permissions

Replicating this table requires **Super Admin** permissions in HubSpot. The Super Admin role is different than the Admin role, which you can read more about in [HubSpot’s documentation](https://knowledge.hubspot.com/articles/kcs_article/settings/hubspot-user-roles-guide#admin).

If this table is selected and you don’t have Super Admin permissions in HubSpot, an error similar to the following will surface in the integration’s Extraction Logs:

```
tap - ERROR b'{"status":"error","message":"This oauth-token (**********) does not have proper permissions! (requires any of [email-access])", [...]
```

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [HubSpot API method](http://developers.hubspot.com/docs/methods/email/get_events "Opens in new tab: HubSpot API method") |

email\_events table foreign keys

| Join email\_events with | on |
| --- | --- |
| [campaigns](#campaigns) | ``` email_events.emailCampaignId = campaigns.id ``` |
| [forms](#forms) | ``` email_events.emailCampaignId = forms.leadNurturingCampaignId ```  ``` email_events.portalId = forms.portalId ``` |
| [companies](#companies) | ``` email_events.portalId = companies.portalId ``` |
| [contact\_lists](#contact-lists) | ``` email_events.portalId = contact_lists.portalId ``` |
| [contacts](#contacts) | ``` email_events.portalId = contacts.portal-id ```  ``` email_events.portalId = contacts.form-submissions.portal-id ``` |
| [deals](#deals) | ``` email_events.portalId = deals.portalId ``` |
| [engagements](#engagements) | ``` email_events.portalId = engagements.engagement.portalId ``` |
| [owners](#owners) | ``` email_events.portalId = owners.portalId ```  ``` email_events.portalId = owners.remoteList.portalId ``` |
| [subscription\_changes](#subscription-changes) | ``` email_events.portalId = subscription_changes.portalId ```  ``` email_events.portalId = subscription_changes.changes.portalId ``` |

email\_events table schema

|  |
| --- |
| **appId**  INTEGER |
| **appName**  STRING |
| **browser**  OBJECT This is a nested data structure:   - family: STRING - name: STRING - producer: STRING - producerUrl: STRING - type: STRING - url: STRING |
| **created**  DATE-TIME |
| **deviceType**  STRING |
| **duration**  INTEGER |
| **emailCampaignGroupId**  INTEGER |
| **emailCampaignId**  INTEGER |
| **filteredEvent**  BOOLEAN |
| **from**  STRING |
| **hmid**  STRING |
| **id**  STRING |
| **ipAddress**  STRING |
| **linkId**  INTEGER |
| **location**  OBJECT This is a nested data structure:   - city: STRING - country: STRING - state: STRING |
| **portalId**  INTEGER |
| **recipient**  STRING |
| **response**  STRING |
| **sentBy**  OBJECT This is a nested data structure:   - created: DATE-TIME - id: STRING |
| **smtpId**  STRING |
| **subject**  STRING |
| **type**  STRING |
| **url**  STRING |
| **userAgent**  STRING |

### engagements

The `engagements` table contains info about all the engagements in a HubSpot portal.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | engagement\_id |
| **Replication Key** | lastUpdated |
| **Useful links** | [HubSpot API method](https://developers.hubspot.com/docs/api-reference/legacy/crm/using-object-apis "Opens in new tab: HubSpot API method") |

engagements table foreign keys

| Join engagements with | on |
| --- | --- |
| [companies](#companies) | ``` engagements.associations.companyIds = companies.companyId ```  ``` engagements.engagement.portalId = companies.portalId ``` |
| [contacts\_by\_company](#contacts-by-company) | ``` engagements.associations.companyIds = contacts_by_company.company-id ``` |
| [deals](#deals) | ``` engagements.associations.companyIds = deals.associations.associatedCompanyIds ```  ``` engagements.associations.dealIds = deals.dealId ```  ``` engagements.associations.dealIds = deals.associations.associatedDealIds ```  ``` engagements.engagement.portalId = deals.portalId ``` |
| [contact\_lists](#contact-lists) | ``` engagements.associations.contactIds = contact_lists.listId ```  ``` engagements.engagement.portalId = contact_lists.portalId ``` |
| [contacts](#contacts) | ``` engagements.associations.contactIds = contacts.list-memberships.internal-list-id ```  ``` engagements.engagement.portalId = contacts.portal-id ```  ``` engagements.engagement.portalId = contacts.form-submissions.portal-id ``` |
| [owners](#owners) | ``` engagements.engagement.ownerId = owners.ownerId ```  ``` engagements.engagement.ownerId = owners.remoteList.ownerId ```  ``` engagements.engagement.portalId = owners.portalId ```  ``` engagements.engagement.portalId = owners.remoteList.portalId ``` |
| [email\_events](#email-events) | ``` engagements.engagement.portalId = email_events.portalId ``` |
| [forms](#forms) | ``` engagements.engagement.portalId = forms.portalId ``` |
| [subscription\_changes](#subscription-changes) | ``` engagements.engagement.portalId = subscription_changes.portalId ```  ``` engagements.engagement.portalId = subscription_changes.changes.portalId ``` |

engagements table schema

|  |
| --- |
| **associations**  OBJECT This is a nested data structure:   - companyIds: ARRAY, which is also a nested data structure. - contactIds: ARRAY, which is also a nested data structure. - dealIds: ARRAY, which is also a nested data structure. |
| **attachments**  ARRAY This is a nested data structure:   - id: INTEGER |
| **engagement**  OBJECT This is a nested data structure:   - active: BOOLEAN - createdAt: DATE-TIME - id: INTEGER - lastUpdated: DATE-TIME - ownerId: INTEGER - portalId: INTEGER - timestamp: DATE-TIME - type: STRING |
| **engagement\_id**  INTEGER |
| **lastUpdated**  DATE-TIME |
| **metadata**  OBJECT This is a nested data structure:   - bcc: ARRAY, which is also a nested data structure.   - email: STRING - body: STRING - cc: ARRAY, which is also a nested data structure.   - email: STRING - disposition: STRING - durationMilliseconds: INTEGER - endTime: INTEGER - externalAccountId: STRING - externalId: STRING - forObjectType: STRING - from: OBJECT, which is also a nested data structure.   - email: STRING   - firstName: STRING   - lastName: STRING - fromNumber: STRING - html: STRING - recordingUrl: STRING - startTime: INTEGER - status: STRING - subject: STRING - text: STRING - title: STRING - to: ARRAY, which is also a nested data structure.   - email: STRING - toNumber: STRING |

### forms

The `forms` table contains info about your HubSpot website forms.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | guid |
| **Replication Key** | updatedAt |
| **Useful links** | [HubSpot API method](https://developers.hubspot.com/docs/api-reference/legacy/marketing/forms/guide "Opens in new tab: HubSpot API method") |

forms table foreign keys

| Join forms with | on |
| --- | --- |
| [campaigns](#campaigns) | ``` forms.leadNurturingCampaignId = campaigns.id ``` |
| [email\_events](#email-events) | ``` forms.leadNurturingCampaignId = email_events.emailCampaignId ```  ``` forms.portalId = email_events.portalId ``` |
| [contacts](#contacts) | ``` forms.guid = contacts.form-submissions.form-id ```  ``` forms.portalId = contacts.portal-id ```  ``` forms.portalId = contacts.form-submissions.portal-id ``` |
| [companies](#companies) | ``` forms.portalId = companies.portalId ``` |
| [contact\_lists](#contact-lists) | ``` forms.portalId = contact_lists.portalId ``` |
| [deals](#deals) | ``` forms.portalId = deals.portalId ``` |
| [engagements](#engagements) | ``` forms.portalId = engagements.engagement.portalId ``` |
| [owners](#owners) | ``` forms.portalId = owners.portalId ```  ``` forms.portalId = owners.remoteList.portalId ``` |
| [subscription\_changes](#subscription-changes) | ``` forms.portalId = subscription_changes.portalId ```  ``` forms.portalId = subscription_changes.changes.portalId ``` |

forms table schema

|  |
| --- |
| **action**  STRING |
| **campaignGuid**  STRING |
| **captchaEnabled**  BOOLEAN |
| **cloneable**  BOOLEAN |
| **createdAt**  DATE-TIME |
| **cssClass**  STRING |
| **deletable**  BOOLEAN |
| **deletedAt**  INTEGER |
| **editable**  BOOLEAN |
| **followUpId**  STRING |
| **formFieldGroups**  ARRAY This is a nested data structure:   - default: BOOLEAN - fields: ARRAY, which is also a nested data structure.   - defaultValue: STRING   - description: STRING   - displayOrder: INTEGER   - enabled: BOOLEAN   - fieldType: STRING   - groupName: STRING   - hidden: BOOLEAN   - isSmartField: BOOLEAN   - label: STRING   - labelHidden: BOOLEAN   - name: STRING   - options: ARRAY, which is also a nested data structure.     - description: STRING     - displayOrder: INTEGER     - doubleData: NUMBER     - hidden: BOOLEAN     - label: STRING     - readOnly: BOOLEAN     - value: STRING   - placeholder: STRING   - required: BOOLEAN   - selectedOptions: ARRAY   - type: STRING   - unselectedLabel: STRING   - validation: OBJECT, which is also a nested data structure.     - blockedEmailAddresses: ARRAY     - data: STRING     - message: STRING     - name: STRING     - useDefaultBlockList: BOOLEAN - isSmartGroup: BOOLEAN - richText: OBJECT, which is also a nested data structure.   - content: STRING |
| **formType**  STRING |
| **guid**  STRING |
| **ignoreCurrentValues**  BOOLEAN |
| **inlineMessage**  STRING |
| **leadNurturingCampaignId**  STRING |
| **metaData**  ARRAY This is a nested data structure:   - name: STRING - value: STRING |
| **method**  STRING |
| **migratedFrom**  STRING |
| **name**  STRING |
| **notifyRecipients**  STRING |
| **performableHtml**  STRING |
| **portalId**  INTEGER |
| **redirect**  STRING |
| **submitText**  STRING |
| **tmsId**  STRING |
| **updatedAt**  DATE-TIME |

### owners

The `owners` table contains info about the owners that exist in your HubSpot portal. Owners are created and updated in HubSpot when new users are added or when owners are synced from Salesforce to HubSpot.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | ownerId |
| **Replication Key** | updatedAt |
| **Useful links** | [HubSpot API method](https://developers.hubspot.com/docs/api-reference/legacy/crm/owners/guide "Opens in new tab: HubSpot API method") |

owners table foreign keys

| Join owners with | on |
| --- | --- |
| [engagements](#engagements) | ``` owners.ownerId = engagements.engagement.ownerId ```  ``` owners.remoteList.ownerId = engagements.engagement.ownerId ```  ``` owners.portalId = engagements.engagement.portalId ```  ``` owners.remoteList.portalId = engagements.engagement.portalId ``` |
| [companies](#companies) | ``` owners.portalId = companies.portalId ```  ``` owners.remoteList.portalId = companies.portalId ``` |
| [contact\_lists](#contact-lists) | ``` owners.portalId = contact_lists.portalId ```  ``` owners.remoteList.portalId = contact_lists.portalId ``` |
| [contacts](#contacts) | ``` owners.portalId = contacts.portal-id ```  ``` owners.remoteList.portalId = contacts.portal-id ```  ``` owners.portalId = contacts.form-submissions.portal-id ```  ``` owners.remoteList.portalId = contacts.form-submissions.portal-id ``` |
| [deals](#deals) | ``` owners.portalId = deals.portalId ```  ``` owners.remoteList.portalId = deals.portalId ``` |
| [email\_events](#email-events) | ``` owners.portalId = email_events.portalId ```  ``` owners.remoteList.portalId = email_events.portalId ``` |
| [forms](#forms) | ``` owners.portalId = forms.portalId ```  ``` owners.remoteList.portalId = forms.portalId ``` |
| [subscription\_changes](#subscription-changes) | ``` owners.portalId = subscription_changes.portalId ```  ``` owners.remoteList.portalId = subscription_changes.portalId ```  ``` owners.portalId = subscription_changes.changes.portalId ```  ``` owners.remoteList.portalId = subscription_changes.changes.portalId ``` |

owners table schema

|  |
| --- |
| **archived**  BOOLEAN |
| **createdAt**  DATE-TIME |
| **email**  STRING |
| **firstName**  STRING |
| **id**  STRING |
| **lastName**  STRING |
| **teams**  ARRAY This is a nested data structure:   - id: STRING - name: STRING - primary: BOOLEAN |
| **updatedAt**  DATE-TIME |
| **userId**  INTEGER |

### subscription\_changes

The `subscription_changes` table contains info about changes made subscriptions.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | recipient  portalId  timestamp |
| **Useful links** | [HubSpot API method](https://developers.hubspot.com/docs/api-reference/legacy/communication-preferences/v1/get-subscriptions-timeline "Opens in new tab: HubSpot API method") |

subscription\_changes table foreign keys

| Join subscription\_changes with | on |
| --- | --- |
| [companies](#companies) | ``` subscription_changes.portalId = companies.portalId ```  ``` subscription_changes.changes.portalId = companies.portalId ``` |
| [contact\_lists](#contact-lists) | ``` subscription_changes.portalId = contact_lists.portalId ```  ``` subscription_changes.changes.portalId = contact_lists.portalId ``` |
| [contacts](#contacts) | ``` subscription_changes.portalId = contacts.portal-id ```  ``` subscription_changes.changes.portalId = contacts.portal-id ```  ``` subscription_changes.portalId = contacts.form-submissions.portal-id ```  ``` subscription_changes.changes.portalId = contacts.form-submissions.portal-id ``` |
| [deals](#deals) | ``` subscription_changes.portalId = deals.portalId ```  ``` subscription_changes.changes.portalId = deals.portalId ``` |
| [email\_events](#email-events) | ``` subscription_changes.portalId = email_events.portalId ```  ``` subscription_changes.changes.portalId = email_events.portalId ``` |
| [engagements](#engagements) | ``` subscription_changes.portalId = engagements.engagement.portalId ```  ``` subscription_changes.changes.portalId = engagements.engagement.portalId ``` |
| [forms](#forms) | ``` subscription_changes.portalId = forms.portalId ```  ``` subscription_changes.changes.portalId = forms.portalId ``` |
| [owners](#owners) | ``` subscription_changes.portalId = owners.portalId ```  ``` subscription_changes.changes.portalId = owners.portalId ```  ``` subscription_changes.portalId = owners.remoteList.portalId ```  ``` subscription_changes.changes.portalId = owners.remoteList.portalId ``` |

subscription\_changes table schema

|  |
| --- |
| **changes**  ARRAY This is a nested data structure:   - causedByEvent: OBJECT, which is also a nested data structure.   - created: DATE-TIME   - id: STRING - change: STRING - changeType: STRING - portalId: INTEGER - source: STRING - subscriptionId: INTEGER - timestamp: DATE-TIME |
| **portalId**  INTEGER |
| **recipient**  STRING |
| **timestamp**  DATE-TIME |

### tickets

In HubSpot, tickets represents customer requests for help

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [HubSpot API method](https://developers.hubspot.com/docs/api-reference/legacy/crm/objects/tickets/guide "Opens in new tab: HubSpot API method") |

tickets table schema

|  |
| --- |
| **archived**  BOOLEAN |
| **associations**  OBJECT This is a nested data structure:   - companies: OBJECT, which is also a nested data structure.   - results: ARRAY, which is also a nested data structure.     - id: STRING     - type: STRING - contacts: OBJECT, which is also a nested data structure.   - results: ARRAY, which is also a nested data structure.     - id: STRING     - type: STRING - deals: OBJECT, which is also a nested data structure.   - results: ARRAY, which is also a nested data structure.     - id: STRING     - type: STRING |
| **createdAt**  DATE-TIME |
| **id**  STRING |
| **updatedAt**  DATE-TIME |

### workflows

The `workflows` table contains info about the workflows in your HubSpot portal.

**Note**: The `workflows` stream only supports contact-based workflows.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [HubSpot API method](https://developers.hubspot.com/docs/methods/workflows/v3/get_workflows "Opens in new tab: HubSpot API method") |

workflows table schema

|  |
| --- |
| **contactListIds**  OBJECT This is a nested data structure:   - active: INTEGER - enrolled: INTEGER - steps: ARRAY, which is also a nested data structure. |
| **enabled**  BOOLEAN |
| **id**  INTEGER |
| **insertedAt**  DATE-TIME |
| **name**  STRING |
| **personaTagIds**  ARRAY This is a nested data structure. |
| **type**  STRING |
| **updatedAt**  DATE-TIME |
