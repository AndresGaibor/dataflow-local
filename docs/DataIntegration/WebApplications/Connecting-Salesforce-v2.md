---
title: "Salesforce"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Salesforce-v2.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Salesforce

Salesforce is a cloud-based CRM platform. You can use Salesforce data as a data source for replication. OAuth 2.0 Client Credentials is the only supported flow for new Salesforce connections, using the `client_credentials` grant.

Salesforce integration replicates data from your Salesforce account. When setting up a Salesforce integration, you can select one of the following Salesforce APIs to replicate your data:

- [Salesforce REST API v61.0](https://developer.salesforce.com/docs/atlas.en-us.250.0.api_rest.meta/api_rest/intro_rest.htm)
- [Salesforce Bulk API](https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/asynch_api_intro.htm)

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

Before creating the Salesforce connection in Qlik Talend Cloud, confirm that:

- Your Salesforce org supports API access and you have API access enabled. See
  [REST API compatible editions](https://developer.salesforce.com/docs/atlas.en-us.250.0.api_rest.meta/api_rest/intro_rest_compatible_editions.htm).
  API access is enabled by default in Enterprise, Performance, Unlimited, and Developer editions.
- If you need help confirming API access for your org, see
  [Salesforce Help](https://help.salesforce.com/s/articleView?id=xcloud.users_add_products_subscription_management.htm&type=5)
  or contact your Salesforce account executive.

**Note:** You can’t create Connected Apps.
Salesforce recommends using an External Client App instead. For more information, see [Salesforce Help](https://help.salesforce.com/s/articleView?id=005228017&type=1) and [External Client Apps](https://help.salesforce.com/s/articleView?id=xcloud.external_client_apps.htm&type=5).

To create, edit, or delete external client apps, you need admin permissions.

To create an integration user for the external client apps:

1. Log into your [Salesforce](https://login.salesforce.com/) account.
2. From Setup, search for and open Users.
3. Click New User, then enter the integration user details.

   Use an email address that you can access.
4. Set User License to Salesforce Integration.
5. Set Profile to Minimum Access - API only Integrations.

   This profile does not have access to certain Salesforce objects. Administrators might need to extend the object permissions set. For more information, see [Salesforce API Integration license release notes](https://help.salesforce.com/s/articleView?id=release-notes.rn_api_integration_license.htm&release=242&type=5).
6. Click Save.

To set up an external client app and retrieve your client ID and client secret:

1. Log into your [Salesforce](https://login.salesforce.com/) account.
2. From Setup, search for and open App Manager.
3. Select New External Client App and enter a name.
4. Set Distribution State to Local.
5. Enable OAuth Settings.
6. Select these OAuth scopes:
   - Manage user data via APIs (`api`)
   - Full access (`full`)
7. Set Callback URL to https://connector.qlik.com/auth/oauth/v3.htm.
8. Under Flow Enablement, enable Client Credentials Flow.
9. Click Create.
10. Under OAuth Flows and External Client App Enhancements, confirm Enable Client Credentials Flow is selected, then enter the integration username.
11. Under App Authorization, review Refresh Token Policy. The default is Expire refresh token if not used for specific time. Qlik uses the client credentials flow for new connections and does not require refresh tokens.
12. Set IP Relaxation to Relax IP restrictions, then click Save.
13. Open Settings > Plugin Policies.
14. Open OAuth Settings and select Consumer Key and Secret. Copy your client ID and client secret.

To find the Salesforce instance URL:

1. Log into Salesforce as an administrator.
2. From Setup, search for and open My Domain.
3. Copy your current My Domain URL. Use this value as `instance_url` when you create the connection.

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
| Production or Sandbox Environment | Select the type of Salesforce environment for this connection:  - Production Environment: Connects to your production Salesforce org. - Sandbox Environment: Connects to your Salesforce sandbox org. |
| API Type | Select the API type from the drop-down list:  - BULK (recommended): Best for large datasets and less frequent replication. Limited to 10,000 batches per rolling 24 hours. See [Salesforce Bulk API limits](https://developer.salesforce.com/docs/atlas.en-us.260.0.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_bulkapi.htm). - REST: Best for smaller datasets and frequent updates. |
| Max percentage of API quota to use | Percentage of your standard API quota Qlik Talend Cloud can use. If the limit is reached, replication pauses and resumes when quota is available. If set to 80 and your quota is 10,000 calls/24 hours, Qlik Talend Cloud can use up to 8,000 calls across all connected apps.  API quota limits depend on your Salesforce subscription and edition. See [Salesforce API limits](https://developer.salesforce.com/docs/atlas.en-us.210.0.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_api.htm).  Note: Enter 80, not 80%. |
| Max percentage allowed per run | Percentage of your total API quota that Qlik Talend Cloud can use per replication job. If set to 10 and your quota is 10,000 calls, Qlik Talend Cloud can use up to 1,000 calls per job (10,000 × 0.1).  Note: Enter 10, not 10%. |
| Client ID | Client ID. |
| Client Secret | Client secret. |
| Instance URL | Salesforce My Domain URL. |

## Unsupported objects in REST API

The following objects won’t be available for replications in Qlik Talend Cloud:

- Announcement
- CollaborationGroupRecord
- ContentDocumentLink
- ContentFolderMember
- DataStatistics
- EntityParticle
- FieldDefinition
- FlexQueueItem
- IdeaComment
- OwnerChangeOptionInfo
- PicklistValueInfo
- PlatformAction
- RelationshipDomain
- RelationshipInfo
- SearchLayout
- SiteDetail
- UserEntityAccess
- UserFieldAccess
- Vote
- Any `*ChangeEvent` object
- ActivityHistory
- AggregateResult
- AttachedContentDocument
- CombinedAttachment
- ContentBody
- EmailStatus
- FeedLike
- FeedTrackedChange
- FeedSignal
- FolderedContentDocument
- ListViewChartInstance
- LookedUpFromActivity
- Name
- NoteAndAttachment
- OpenActivity
- OutgoingEmail
- OutgoingEmailRelation
- OwnedContentDocument
- ProcessInstanceHistory
- UserRecordAccess

The unsupported objects list is not exhaustive. Salesforce might change the unsupported objects for the API as Salesforce continues to maintain and update their APIs.

## Unsupported objects in Bulk API

The following objects won’t be available for selection in Qlik Talend Cloud:

- AcceptedEventRelation
- AssetTokenEvent
- AttachedContentNote
- CaseStatus
- ContentFolderItem
- ContractStatus
- DeclinedEventRelation
- EventWhoRelation
- PartnerRole
- QuoteTemplateRichTextData
- RecentlyViewed
- SolutionStatus
- TaskPriority
- TaskWhoRelation
- TaskStatus
- UndecidedEventRelation

The unsupported objects list is not exhaustive. Salesforce might change the unsupported objects for the API as Salesforce continues to maintain and update their APIs.

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

The schema and info displayed below is for version 2.

To ensure we can provide you with up-to-date documentation, this section covers a few of the most popular tables that Salesforce integration offers.

See the [Salesforce Object Reference](https://developer.salesforce.com/Content/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_list.htm) guide for info on objects not listed here, including the fields available in each object.

### Custom Salesforce object and field replication

Salesforce integration supports the replication of custom objects and fields.

Custom object and field names are appended with `__c` to make identification easier. For example: `AE_Assignment__c` or `Assignment_Group_Name__c`

Some custom fields are formula (calculated) fields. Their values are derived from other fields and can change without updating the record replication key (for example, `systemModStamp`).

With incremental replication, derived values can become stale in your destination if only source fields referenced by the formula change.

If you need formula-field freshness in Qlik Talend Cloud, use one of the following approaches:

- Recreate the formula logic in transformations (for example, joins, lookups, SQL, or expressions) so values are recalculated during processing.
- Run periodic full loads to refresh derived values when incremental updates are not enough. Consider API usage and destination processing impact before scheduling full refreshes.

The following patterns can help when recreating formula logic in your pipeline:

- Cross-object formula fields: if an `Opportunity` formula depends on `Account.Name`, replicate both objects and join on `Opportunity.AccountId = Account.Id` so the derived value is recalculated from the related account field.
- Same-object formula logic: for a weighted value based on `Amount` and `Probability`, recalculate with SQL or an expression (for example, `Amount * (Probability / 100)`) during transformation.

Use periodic full loads when you need a full refresh of derived values across previously replicated records. This can improve freshness, but it may increase Salesforce API usage.

Depending on your destination, table and column names may not appear as they are outlined below.

### account

The `account` table contains info about the individual accounts (organizations and persons) involved with your business. This could be a customer, a competitor, a partner, and so on.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | systemModStamp |
| **Useful links** | [Salesforce documentation](https://developer.salesforce.com/Content/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_account.htm#!) |

account table foreign keys

| Join account with | on |
| --- | --- |
| [contact](#contact) | ``` account.id = contact.accountId ```  ``` account.ownerId = contact.ownerId ``` |
| [lead](#lead) | ``` account.id = lead.convertedAccountId ```  ``` account.ownerId = lead.ownerId ``` |
| [opportunity](#opportunity) | ``` account.id = opportunity.accountId ```  ``` account.ownerId = opportunity.ownerId ``` |
| [user](#user) | ``` account.id = user.accountId ```  ``` account.ownerId = user.id ```  ``` account.ownerId = user.delegatedApproverId ```  ``` account.ownerId = user.managerId ``` |

account table schema

|  |
| --- |
| **accountNumber**  STRING |
| **accountSource**  STRING |
| **annualRevenue**  NUMBER |
| **billingAddress**  STRING |
| **billingCity**  STRING |
| **billingCountry**  STRING |
| **billingCountryCode**  STRING |
| **billingGeocodeAccuracy**  STRING |
| **billingLatitude**  INTEGER |
| **billingLongitude**  INTEGER |
| **billingPostalCode**  STRING |
| **billingState**  STRING |
| **billingStateCode**  STRING |
| **billingStreet**  STRING |
| **cleanStatus**  STRING |
| **connectionReceivedId**  STRING |
| **description**  STRING |
| **dunsNumber**  STRING |
| **fax**  STRING |
| **id**  STRING |
| **industry**  STRING |
| **isCustomerPortal**  BOOLEAN |
| **isDeleted**  BOOLEAN |
| **isPartner**  BOOLEAN |
| **isPersonAccount**  BOOLEAN |
| **jigsaw**  STRING |
| **lastActivityDate**  DATE-TIME |
| **lastReferenceDate**  DATE-TIME |
| **lastViewedDate**  DATE-TIME |
| **masterRecordId**  STRING |
| **naicsCode**  STRING |
| **naicsDescription**  STRING |
| **name**  STRING |
| **numberOfEmployees**  NUMBER |
| **operatingHoursId**  STRING |
| **ownerId**  STRING |
| **ownership**  STRING |
| **parentId**  STRING |
| **phone**  STRING |
| **photoUrl**  STRING |
| **rating**  STRING |
| **recordTypeId**  STRING |
| **salutation**  STRING |
| **shippingAddress**  STRING |
| **shippingCity**  STRING |
| **shippingCountry**  STRING |
| **shippingCountryCode**  STRING |
| **shippingGeocodeAccuracy**  STRING |
| **shippingLatitude**  INTEGER |
| **shippingLongitude**  INTEGER |
| **shippingPostalCode**  STRING |
| **shippingState**  STRING |
| **shippingStateCode**  STRING |
| **shippingStreet**  STRING |
| **sic**  STRING |
| **sicDesc**  STRING |
| **site**  STRING |
| **systemModStamp**  DATE-TIME |
| **tickerSymbol**  STRING |
| **tradeStyle**  STRING |
| **type**  STRING |
| **website**  STRING |
| **yearStarted**  STRING |

### contact

The `contact` table contains info about your contacts, who are individuals associated with accounts in your Salesforce instance.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | systemModStamp |
| **Useful links** | [Salesforce documentation](https://developer.salesforce.com/Content/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_contact.htm) |

contact table foreign keys

| Join contact with | on |
| --- | --- |
| [account](#account) | ``` contact.accountId = account.id ```  ``` contact.ownerId = account.ownerId ``` |
| [lead](#lead) | ``` contact.accountId = lead.convertedAccountId ```  ``` contact.id = lead.convertedContactId ```  ``` contact.ownerId = lead.ownerId ``` |
| [opportunity](#opportunity) | ``` contact.accountId = opportunity.accountId ```  ``` contact.ownerId = opportunity.ownerId ``` |
| [user](#user) | ``` contact.accountId = user.accountId ```  ``` contact.id = user.contactId ```  ``` contact.ownerId = user.id ```  ``` contact.ownerId = user.delegatedApproverId ```  ``` contact.ownerId = user.managerId ``` |

contact table schema

|  |
| --- |
| **accountId**  STRING |
| **assistantName**  STRING |
| **assistantPhone**  STRING |
| **birthdate**  DATE |
| **canAllowPortalSelfReg**  BOOLEAN |
| **cleanStatus**  STRING |
| **connectionReceivedId**  STRING |
| **connectionSentId**  STRING |
| **department**  STRING |
| **description**  STRING |
| **doNotCall**  BOOLEAN |
| **email**  STRING |
| **emailBouncedDate**  DATE-TIME |
| **emailBouncedReason**  STRING |
| **fax**  STRING |
| **firstName**  STRING |
| **hasOptedOutOfEmail**  BOOLEAN |
| **hasOptedOutOfFax**  BOOLEAN |
| **homePhone**  STRING |
| **id**  STRING |
| **isDeleted**  BOOLEAN |
| **isEmailBounced**  BOOLEAN |
| **isPersonAccount**  BOOLEAN |
| **jigsaw**  STRING |
| **lastActivityDate**  DATE-TIME |
| **lastName**  STRING |
| **lastReferenceDate**  DATE-TIME |
| **lastViewedDate**  DATE-TIME |
| **leadSource**  STRING |
| **mailingAddress**  STRING |
| **mailingCity**  STRING |
| **mailingCountry**  STRING |
| **mailingCountryCode**  STRING |
| **mailingGeocodeAccuracy**  STRING |
| **mailingLatitude**  INTEGER |
| **mailingLongitude**  INTEGER |
| **mailingPostalCode**  STRING |
| **mailingState**  STRING |
| **mailingStateCode**  STRING |
| **mailingStreet**  STRING |
| **masterRecordId**  STRING |
| **middleName**  STRING |
| **mobilePhone**  STRING |
| **name**  STRING |
| **otherAddress**  STRING |
| **otherCity**  STRING |
| **otherCountry**  STRING |
| **otherCountryCode**  STRING |
| **otherGeocodeAccuracy**  STRING |
| **otherLatitude**  INTEGER |
| **otherLongitude**  INTEGER |
| **otherPhone**  STRING |
| **otherPostalCode**  STRING |
| **otherState**  STRING |
| **otherStateCode**  STRING |
| **otherStreet**  STRING |
| **ownerId**  STRING |
| **phone**  STRING |
| **photoUrl**  STRING |
| **recordTypeId**  STRING |
| **reportsToId**  STRING |
| **salutation**  STRING |
| **suffix**  STRING |
| **systemModStamp**  DATE-TIME |
| **title**  STRING |

### lead

The `lead` table contains info about your leads, who are prospects or potential Opportunities.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | systemModStamp |
| **Useful links** | [Salesforce documentation](https://developer.salesforce.com/Content/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_lead.htm) |

lead table foreign keys

| Join lead with | on |
| --- | --- |
| [account](#account) | ``` lead.convertedAccountId = account.id ```  ``` lead.ownerId = account.ownerId ``` |
| [contact](#contact) | ``` lead.convertedAccountId = contact.accountId ```  ``` lead.convertedContactId = contact.id ```  ``` lead.ownerId = contact.ownerId ``` |
| [opportunity](#opportunity) | ``` lead.convertedAccountId = opportunity.accountId ```  ``` lead.convertedOpportunityId = opportunity.id ```  ``` lead.ownerId = opportunity.ownerId ``` |
| [user](#user) | ``` lead.convertedAccountId = user.accountId ```  ``` lead.convertedContactId = user.contactId ```  ``` lead.ownerId = user.id ```  ``` lead.ownerId = user.delegatedApproverId ```  ``` lead.ownerId = user.managerId ``` |

lead table schema

|  |
| --- |
| **PostalCode**  STRING |
| **address**  STRING |
| **annualRevenue**  NUMBER |
| **city**  STRING |
| **cleanStatus**  STRING |
| **company**  STRING |
| **companyDunsNumber**  STRING |
| **connectionReceivedId**  STRING |
| **convertedAccountId**  STRING |
| **convertedContactId**  STRING |
| **convertedDate**  DATE-TIME |
| **convertedOpportunityId**  STRING |
| **country**  STRING |
| **countryCode**  STRING |
| **currencyIsoCode**  STRING |
| **description**  STRING |
| **division**  STRING |
| **email**  STRING |
| **emailBouncedDate**  DATE-TIME |
| **emailBouncedReason**  STRING |
| **fax**  STRING |
| **firstName**  STRING |
| **geocodeAccuracy**  STRING |
| **hasOptedOutOfEmail**  BOOLEAN |
| **id**  STRING |
| **industry**  STRING |
| **isConverted**  BOOLEAN |
| **isDeleted**  BOOLEAN |
| **isUnreadByOwner**  BOOLEAN |
| **jigsaw**  STRING |
| **lastActivityDate**  DATE-TIME |
| **lastName**  STRING |
| **lastReferenceDate**  DATE-TIME |
| **lastViewedDate**  DATE-TIME |
| **latitude**  INTEGER |
| **leadSource**  STRING |
| **longitude**  INTEGER |
| **masterRecordId**  STRING |
| **middleName**  STRING |
| **mobilePhone**  STRING |
| **name**  STRING |
| **numberOfEmployees**  INTEGER |
| **ownerId**  STRING |
| **partnerAccountId**  STRING |
| **phone**  STRING |
| **photoUrl**  STRING |
| **rating**  STRING |
| **recordTypeId**  STRING |
| **salutation**  STRING |
| **scoreIntelligenceId**  STRING |
| **state**  STRING |
| **stateCode**  STRING |
| **status**  STRING |
| **street**  STRING |
| **suffix**  STRING |
| **systemModStamp**  DATE-TIME |
| **title**  STRING |
| **website**  STRING |

### opportunity

The `opportunity` table contains info about your opportunities, which are sales or pending deals.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | systemModStamp |
| **Useful links** | [Salesforce documentation](https://developer.salesforce.com/Content/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_opportunity.htm) |

opportunity table foreign keys

| Join opportunity with | on |
| --- | --- |
| [account](#account) | ``` opportunity.accountId = account.id ```  ``` opportunity.ownerId = account.ownerId ``` |
| [contact](#contact) | ``` opportunity.accountId = contact.accountId ```  ``` opportunity.ownerId = contact.ownerId ``` |
| [lead](#lead) | ``` opportunity.accountId = lead.convertedAccountId ```  ``` opportunity.id = lead.convertedOpportunityId ```  ``` opportunity.ownerId = lead.ownerId ``` |
| [user](#user) | ``` opportunity.accountId = user.accountId ```  ``` opportunity.ownerId = user.id ```  ``` opportunity.ownerId = user.delegatedApproverId ```  ``` opportunity.ownerId = user.managerId ``` |

opportunity table schema

|  |
| --- |
| **accountId**  STRING |
| **amount**  NUMBER |
| **campaignId**  STRING |
| **closeDate**  DATE-TIME |
| **connectionReceivedId**  STRING |
| **connectionSentId**  STRING |
| **currencyIsoCode**  STRING |
| **description**  STRING |
| **expectedRevenue**  NUMBER |
| **fiscal**  STRING |
| **fiscalQuarter**  INTEGER |
| **fiscalYear**  INTEGER |
| **forecastCategory**  STRING |
| **forecastCategoryName**  STRING |
| **hasOpenActivity**  BOOLEAN |
| **hasOpportunityLineItem**  BOOLEAN |
| **hasOverdueTask**  BOOLEAN |
| **id**  STRING |
| **isClosed**  BOOLEAN |
| **isDeleted**  BOOLEAN |
| **isExcludedFromTerritory2Filter**  BOOLEAN |
| **isSplit**  BOOLEAN |
| **isWon**  BOOLEAN |
| **lastActivityDate**  DATE-TIME |
| **lastReferenceDate**  DATE-TIME |
| **lastViewedDate**  DATE-TIME |
| **leadSource**  STRING |
| **name**  STRING |
| **nextStep**  STRING |
| **ownerId**  STRING |
| **pricebook2Id**  STRING |
| **pricebookId**  STRING |
| **probability**  INTEGER |
| **recordTypeId**  STRING |
| **stageName**  STRING |
| **syncedQuoteId**  STRING |
| **systemModStamp**  DATE-TIME |
| **territory2Id**  STRING |
| **totalOpportunityQuantity**  NUMBER |
| **type**  STRING |

### user

The `user` table contains info about the users in your organization.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | systemModStamp |
| **Useful links** | [Salesforce documentation](https://developer.salesforce.com/Content/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_user.htm) |

user table foreign keys

| Join user with | on |
| --- | --- |
| [account](#account) | ``` user.accountId = account.id ```  ``` user.id = account.ownerId ```  ``` user.delegatedApproverId = account.ownerId ```  ``` user.managerId = account.ownerId ``` |
| [contact](#contact) | ``` user.accountId = contact.accountId ```  ``` user.contactId = contact.id ```  ``` user.id = contact.ownerId ```  ``` user.delegatedApproverId = contact.ownerId ```  ``` user.managerId = contact.ownerId ``` |
| [lead](#lead) | ``` user.accountId = lead.convertedAccountId ```  ``` user.contactId = lead.convertedContactId ```  ``` user.id = lead.ownerId ```  ``` user.delegatedApproverId = lead.ownerId ```  ``` user.managerId = lead.ownerId ``` |
| [opportunity](#opportunity) | ``` user.accountId = opportunity.accountId ```  ``` user.id = opportunity.ownerId ```  ``` user.delegatedApproverId = opportunity.ownerId ```  ``` user.managerId = opportunity.ownerId ``` |

user table schema

|  |
| --- |
| **aboutMe**  STRING |
| **accountId**  STRING |
| **address**  STRING |
| **alias**  STRING |
| **badgeText**  STRING |
| **bannerPhotoUrl**  STRING |
| **callCenterId**  STRING |
| **city**  STRING |
| **communityNickname**  STRING |
| **companyName**  STRING |
| **contactId**  STRING |
| **country**  STRING |
| **countryCode**  STRING |
| **defaultCurrencyIsoCode**  STRING |
| **defaultDivision**  STRING |
| **defaultGroupNotificationFrequency**  STRING |
| **delegatedApproverId**  STRING |
| **department**  STRING |
| **digestFrequency**  STRING |
| **division**  STRING |
| **email**  STRING |
| **emailEncodingKey**  STRING |
| **emailPreferencesAutoBcc**  BOOLEAN |
| **employeeNumber**  STRING |
| **extension**  STRING |
| **fax**  STRING |
| **federationIdentifier**  STRING |
| **firstName**  STRING |
| **forecastEnabled**  BOOLEAN |
| **fullPhotoUrl**  STRING |
| **id**  STRING |
| **isActive**  BOOLEAN |
| **isPortalEnabled**  BOOLEAN |
| **isPortalSelfRegistered**  BOOLEAN |
| **isPrmSuperUser**  BOOLEAN |
| **isProfilePhotoActive**  BOOLEAN |
| **jigsawImportLimitOverride**  INTEGER |
| **languageLocaleKey**  STRING |
| **lastLoginDate**  DATE-TIME |
| **lastName**  STRING |
| **lastReferenceDate**  DATE-TIME |
| **lastViewedDate**  DATE-TIME |
| **latitude**  INTEGER |
| **localeSidKey**  STRING |
| **longitude**  INTEGER |
| **manager**  STRING |
| **managerId**  STRING |
| **mediumBannerPhotoUrl**  STRING |
| **middleName**  STRING |
| **mobilePhone**  STRING |
| **name**  STRING |
| **offlineTrialExpirationDate**  DATE-TIME |
| **phone**  STRING |
| **portalRole**  STRING |
| **postalCode**  STRING |
| **profileId**  STRING |
| **receivesAdminInfoEmails**  BOOLEAN |
| **receivesInfoEmails**  BOOLEAN |
| **senderEmail**  STRING |
| **senderName**  STRING |
| **signature**  STRING |
| **smallBannerPhotoUrl**  STRING |
| **smallPhotoUrl**  STRING |
| **state**  STRING |
| **stateCode**  STRING |
| **street**  STRING |
| **suffix**  STRING |
| **systemModStamp**  DATE-TIME |
| **timeZoneSidKey**  STRING |
| **title**  STRING |
| **userPermissionsCallCenterAutoLogin**  BOOLEAN |
| **userPermissionsChatterAnswersUser**  BOOLEAN |
| **userPermissionsInteractionUser**  BOOLEAN |
| **userPermissionsJigsawProspectingUser**  BOOLEAN |
| **userPermissionsKnowledgeUser**  BOOLEAN |
| **userPermissionsLiveAgentUser**  BOOLEAN |
| **userPermissionsMarketingUser**  BOOLEAN |
| **userPermissionsMobileUser**  BOOLEAN |
| **userPermissionsOfflineUser**  BOOLEAN |
| **userPermissionsSFContentUser**  BOOLEAN |
| **userPermissionsSiteforceContributorUser**  BOOLEAN |
| **userPermissionsSiteforcePublisherUser**  BOOLEAN |
| **userPermissionsSupportUser**  BOOLEAN |
| **userPermissionsWorkDotComeUserFeature**  BOOLEAN |
| **userPreferencesAcitivityRemindersPopup**  BOOLEAN |
| **userPreferencesApexPagesDeveloperMode**  BOOLEAN |
| **userPreferencesContentEmailAsAndWhen**  BOOLEAN |
| **userPreferencesContentNoEmail**  BOOLEAN |
| **userPreferencesDisCommentAfterLikeEmail**  BOOLEAN |
| **userPreferencesDisMentionsCommentEmail**  BOOLEAN |
| **userPreferencesDisProfPostCommentEmail**  BOOLEAN |
| **userPreferencesDisableAllFeedsEmail**  BOOLEAN |
| **userPreferencesDisableBookmarkEmail**  BOOLEAN |
| **userPreferencesDisableChangeCommentEmail**  BOOLEAN |
| **userPreferencesDisableEndorsementEmail**  BOOLEAN |
| **userPreferencesDisableFeedbackEmail**  BOOLEAN |
| **userPreferencesDisableFileShareNotificationsForApi**  BOOLEAN |
| **userPreferencesDisableFollowersEmail**  BOOLEAN |
| **userPreferencesDisableLaterCommentEmail**  BOOLEAN |
| **userPreferencesDisableLikeEmail**  BOOLEAN |
| **userPreferencesDisableMentionsPostEmail**  BOOLEAN |
| **userPreferencesDisableMessageEmail**  BOOLEAN |
| **userPreferencesDisableProfilePostEmail**  BOOLEAN |
| **userPreferencesDisableRewardEmail**  BOOLEAN |
| **userPreferencesDisableSharePostEmail**  BOOLEAN |
| **userPreferencesDisableWorkEmail**  BOOLEAN |
| **userPreferencesEnableAutoSubForFeeds**  BOOLEAN |
| **userPreferencesEventRemindersCheckboxDefault**  BOOLEAN |
| **userPreferencesHideBiggerPhotoCallout**  BOOLEAN |
| **userPreferencesHideCSNDesktopTask**  BOOLEAN |
| **userPreferencesHideCSNGetChatterMobileTask**  BOOLEAN |
| **userPreferencesHideChatterOnboardingSplash**  BOOLEAN |
| **userPreferencesHideHideSecondChatterOnboardingSplash**  BOOLEAN |
| **userPreferencesHideS1BrowserUI**  BOOLEAN |
| **userPreferencesHideSfxWelcomeMat**  BOOLEAN |
| **userPreferencesJigsawListUser**  BOOLEAN |
| **userPreferencesLightningExperiencePreferred**  BOOLEAN |
| **userPreferencesPathAssistantCollapsed**  BOOLEAN |
| **userPreferencesReminderSoundOff**  BOOLEAN |
| **userPreferencesShowCityToExternalUsers**  BOOLEAN |
| **userPreferencesShowCityToGuestUsers**  BOOLEAN |
| **userPreferencesShowCountryToExternalUsers**  BOOLEAN |
| **userPreferencesShowCountryToGuestUsers**  BOOLEAN |
| **userPreferencesShowEmailToExternalUsers**  BOOLEAN |
| **userPreferencesShowEmailToGuestUsers**  BOOLEAN |
| **userPreferencesShowFaxToExternalUsers**  BOOLEAN |
| **userPreferencesShowFaxToGuestUsers**  BOOLEAN |
| **userPreferencesShowManagerToExternalUsers**  BOOLEAN |
| **userPreferencesShowManagerToGuestUsers**  BOOLEAN |
| **userPreferencesShowMobilePhoneToExternalUsers**  BOOLEAN |
| **userPreferencesShowMobilePhoneToGuestUsers**  BOOLEAN |
| **userPreferencesShowPostalCodeToExternalUsers**  BOOLEAN |
| **userPreferencesShowPostalCodeToGuestUsers**  BOOLEAN |
| **userPreferencesShowProfilePicToExternalUsers**  BOOLEAN |
| **userPreferencesShowProfilePicToGuestUsers**  BOOLEAN |
| **userPreferencesShowStateToExternalUsers**  BOOLEAN |
| **userPreferencesShowStateToGuestUsers**  BOOLEAN |
| **userPreferencesShowStreetAddressToExternalUsers**  BOOLEAN |
| **userPreferencesShowStreetAddressToGuestUsers**  BOOLEAN |
| **userPreferencesShowTitleToExternalUsers**  BOOLEAN |
| **userPreferencesShowTitleToGuestUsers**  BOOLEAN |
| **userPreferencesShowWorkPhoneToExternalUsers**  BOOLEAN |
| **userPreferencesShowWorkPhoneToGuestUsers**  BOOLEAN |
| **userPreferencesSortFeedByComment**  BOOLEAN |
| **userPreferencesTaskRemindersCheckboxDefault**  BOOLEAN |
| **userRoleId**  STRING |
| **userType**  STRING |
| **username**  STRING |
