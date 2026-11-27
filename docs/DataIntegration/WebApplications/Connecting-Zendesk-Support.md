---
title: "Zendesk Support"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Zendesk-Support.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Zendesk Support

Zendesk Support provides SaaS products related to customer support, sales, and other customer communications. You can use Zendesk Support as a data source when landing or replicating data.

Zendesk Support integration replicates data using [Zendesk Ticketing API](https://developer.zendesk.com/api-reference/ticketing/introduction/) and [Zendesk Voice API](https://developer.zendesk.com/api-reference/voice/talk-api/introduction/).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To set up the integration, you must have administrator permissions in Zendesk. Replicating SLA policies requires an Enterprise or Professional plan.

To retrieve your client ID and client secret:

1. Log into your [Zendesk](https://support.zendesk.com/auth/v3/signin?brand_id=360002256920&locale=en-us&return_to=https%3A%2F%2Fsupport.zendesk.com%2Fhc%2Fen-us%2Farticles%2F4408845965210-Using-OAuth-authentication-with-your-application&role=end_user) account.
2. In Admin Center, navigate to Apps and integrations > APIs > OAuth clients >  Add OAuth client.
3. Enter the following fields to create a client:
   - Name: Enter a name for your app.
   - Client kind: Select Confidential.
   - Redirect URLs: Enter https://connector.qlik.com/auth/oauth/v3.htm.
4. Click Save.

   A Secret field is generated.
5. Copy and paste your client ID and client secret into a secured file.

## Creating the connection

For more information, see [*Connecting to SaaS applications*](../Landing/connecting-web-applications.htm).

1. Click Authenticate when you have filled in the required connection settings.

   You may be asked to log in to the source application.

   A window is displayed with an authentication code.
2. Copy the code to the clipboard and return to the connection dialog.
3. Paste the code in Complete authentication with the code provided by the source and click Verify.

   Tip noteYou may need to scroll down to see this field.

   When status is Verified, the authentication is verified.
4. Provide a name for the connection in Connection name.
5. Select Open connection metadata to define metadata for the connection when it has been created.

Connection settings

| Setting | Description |
| --- | --- |
| Data gateway | Select a Data Movement gateway if required by your use case.  Information note This field is not available with the Qlik Talend Cloud Starter subscription, as it does not support Data Movement gateway. If you have another subscription tier and do not want to use Data Movement gateway, select None.  For information on the benefits of Data Movement gateway and use cases that require it, see [*Qlik Data Gateway - Data Movement*](../../Gateways/replication-gateway.htm). |
| Start Date | Enter the date, in the format `MM/DD/YYYY`, from which the data must be replicated from your source to your target. |
| Zendesk Subdomain | You can find the subdomain of your Zendesk site in the URL of your account homepage. If the URL is https://qlik.zendesk.com/, the subdomain is qlik. |
| Client ID | Client ID. |
| Client Secret | Client secret. |
| Marketplace Name | Name of the integration. |
| Marketplace Organization ID | Organization ID. |
| Marketplace App ID | App ID. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### group\_memberships

The `group_memberships` table contains info about the groups your Zendesk Support agents are members of.

**Note**: Retrieving group membership data requires Zendesk Support Agent or Admin permissions.

#### Deleted group memberships

As Zendesk Support’s API doesn’t currently provide a method for identifying deleted group memberships, we recommend periodically dropping this table and allowing Stitch to re-create it. Currently, dropping and re-populating the table is the only way to detect deletions.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Zendesk Support documentation](https://developer.zendesk.com/documentation/)  [Zendesk Support API method](https://developer.zendesk.com/api-reference/ticketing/groups/group_memberships/ "Opens in new tab: Zendesk Support API method") |

group\_memberships table foreign keys

| Join group\_memberships with | on |
| --- | --- |
| [groups](#groups) | ``` group_memberships.group_id = groups.id ``` |
| [organizations](#organizations) | ``` group_memberships.group_id = organizations.group_id ``` |
| [satisfaction\_ratings](#satisfaction-ratings) | ``` group_memberships.group_id = satisfaction_ratings.group_id ``` |
| [tickets](#tickets) | ``` group_memberships.group_id = tickets.group_id ``` |
| [users](#users) | ``` group_memberships.group_id = users.default_group_id ``` |

group\_memberships table schema

|  |
| --- |
| **created\_at**  DATE-TIME |
| **default**  BOOLEAN |
| **group\_id**  INTEGER |
| **id**  INTEGER |
| **updated\_at**  DATE-TIME |
| **url**  STRING |
| **user\_id**  INTEGER |

### groups

The `groups` table contains info about the groups in your Zendesk Support account.

**Note**: Retrieving group data requires Zendesk Support Admin or Agent permissions.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Zendesk Support documentation](https://developer.zendesk.com/documentation/)  [Zendesk Support API method](https://developer.zendesk.com/api-reference/ticketing/groups/groups/ "Opens in new tab: Zendesk Support API method") |

groups table foreign keys

| Join groups with | on |
| --- | --- |
| [group\_memberships](#group-memberships) | ``` groups.id = group_memberships.group_id ``` |
| [organizations](#organizations) | ``` groups.id = organizations.group_id ``` |
| [satisfaction\_ratings](#satisfaction-ratings) | ``` groups.id = satisfaction_ratings.group_id ``` |
| [tickets](#tickets) | ``` groups.id = tickets.group_id ``` |
| [users](#users) | ``` groups.id = users.default_group_id ```  ``` groups.id = users.id ``` |
| [macros](#macros) | ``` groups.id = macros.restriction.id ``` |

groups table schema

|  |
| --- |
| **created\_at**  DATE-TIME |
| **default**  BOOLEAN |
| **deleted**  BOOLEAN |
| **description**  STRING |
| **id**  INTEGER |
| **is\_public**  BOOLEAN |
| **name**  STRING |
| **updated\_at**  DATE-TIME |
| **url**  STRING |

### macros

The `macros` table contains info about the macros in your Zendesk Support account. Macros are actions defined by you that modify the values of a ticket’s fields.

**Note**: Retrieving macro data requires Zendesk Support Agent or Admin permissions.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Zendesk Support documentation](https://developer.zendesk.com/documentation/)  [Zendesk Support API method](https://developer.zendesk.com/api-reference/ticketing/business-rules/macros/ "Opens in new tab: Zendesk Support API method") |

macros table foreign keys

| Join macros with | on |
| --- | --- |
| [ticket\_audits](#ticket-audits) | ``` macros.id = ticket_audits.events.macro_id ``` |
| [groups](#groups) | ``` macros.restriction.id = groups.id ``` |
| [users](#users) | ``` macros.restriction.id = users.id ``` |

macros table schema

|  |
| --- |
| **actions**  ARRAY This is a nested data structure:   - field: STRING - value: STRING |
| **active**  BOOLEAN |
| **created\_at**  DATE-TIME |
| **description**  STRING |
| **id**  INTEGER |
| **position**  INTEGER |
| **restriction**  OBJECT This is a nested data structure:   - id: INTEGER - ids: ARRAY, which is also a nested data structure. - type: STRING |
| **title**  STRING |
| **updated\_at**  DATE-TIME |
| **url**  STRING |

### organizations

The `organizations` table contains information about the organizations your end-users belong to.

#### Custom organization fields

Zendesk Support integration will replicate any custom fields associated with organization records.

**Note**: Replicating organization custom fields requires that you be on a Team, Professional, or Enterprise Zendesk Support plan and have Admin permissions in Zendesk Support.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Zendesk Support documentation](https://developer.zendesk.com/documentation/)  [Zendesk Support API method](https://developer.zendesk.com/api-reference/ticketing/organizations/organizations/ "Opens in new tab: Zendesk Support API method") |

organizations table foreign keys

| Join organizations with | on |
| --- | --- |
| [groups](#groups) | ``` organizations.group_id = groups.id ``` |
| [group\_memberships](#group-memberships) | ``` organizations.group_id = group_memberships.group_id ``` |
| [satisfaction\_ratings](#satisfaction-ratings) | ``` organizations.group_id = satisfaction_ratings.group_id ``` |
| [tickets](#tickets) | ``` organizations.group_id = tickets.group_id ```  ``` organizations.id = tickets.organization_id ```  ``` organizations.tags = tickets.tags ``` |
| [users](#users) | ``` organizations.group_id = users.default_group_id ```  ``` organizations.id = users.organization_id ```  ``` organizations.tags = users.tags ``` |
| [tags](#tags) | ``` organizations.tags = tags.name ``` |

organizations table schema

|  |
| --- |
| **created\_at**  DATE-TIME |
| **deleted\_at**  DATE-TIME |
| **details**  STRING |
| **domain\_names**  ARRAY This is a nested data structure. |
| **external\_id**  STRING |
| **group\_id**  INTEGER |
| **id**  INTEGER |
| **name**  STRING |
| **notes**  STRING |
| **organization\_fields**  OBJECT This is a nested data structure. |
| **shared\_comments**  BOOLEAN |
| **shared\_tickets**  BOOLEAN |
| **tags**  ARRAY This is a nested data structure. |
| **updated\_at**  DATE-TIME |
| **url**  STRING |

### satisfaction\_ratings

The `satisfaction_ratings` table contains info about ratings users have offered on support tickets.

**Note**: This table is only available if satisfaction ratings are enabled in your Zendesk Support account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Zendesk Support documentation](https://developer.zendesk.com/documentation/)  [Zendesk Support API method](https://developer.zendesk.com/api-reference/ticketing/ticket-management/satisfaction_ratings/ "Opens in new tab: Zendesk Support API method") |

satisfaction\_ratings table foreign keys

| Join satisfaction\_ratings with | on |
| --- | --- |
| [groups](#groups) | ``` satisfaction_ratings.group_id = groups.id ``` |
| [group\_memberships](#group-memberships) | ``` satisfaction_ratings.group_id = group_memberships.group_id ``` |
| [organizations](#organizations) | ``` satisfaction_ratings.group_id = organizations.group_id ``` |
| [tickets](#tickets) | ``` satisfaction_ratings.group_id = tickets.group_id ```  ``` satisfaction_ratings.ticket_id = tickets.id ```  ``` satisfaction_ratings.assignee_id = tickets.requester_id ```  ``` satisfaction_ratings.requester_id = tickets.requester_id ```  ``` satisfaction_ratings.assignee_id = tickets.follower_ids ```  ``` satisfaction_ratings.requester_id = tickets.follower_ids ```  ``` satisfaction_ratings.assignee_id = tickets.submitter_id ```  ``` satisfaction_ratings.requester_id = tickets.submitter_id ```  ``` satisfaction_ratings.assignee_id = tickets.collaborator_ids ```  ``` satisfaction_ratings.requester_id = tickets.collaborator_ids ```  ``` satisfaction_ratings.assignee_id = tickets.assignee_id ```  ``` satisfaction_ratings.requester_id = tickets.assignee_id ``` |
| [users](#users) | ``` satisfaction_ratings.group_id = users.default_group_id ```  ``` satisfaction_ratings.assignee_id = users.id ```  ``` satisfaction_ratings.requester_id = users.id ``` |
| [ticket\_audits](#ticket-audits) | ``` satisfaction_ratings.ticket_id = ticket_audits.ticket_id ```  ``` satisfaction_ratings.assignee_id = ticket_audits.author_id ```  ``` satisfaction_ratings.requester_id = ticket_audits.author_id ``` |
| [ticket\_comments](#ticket-comments) | ``` satisfaction_ratings.ticket_id = ticket_comments.ticket_id ```  ``` satisfaction_ratings.assignee_id = ticket_comments.author_id ```  ``` satisfaction_ratings.requester_id = ticket_comments.author_id ``` |
| [ticket\_metrics](#ticket-metrics) | ``` satisfaction_ratings.ticket_id = ticket_metrics.ticket_id ``` |

satisfaction\_ratings table schema

|  |
| --- |
| **assignee\_id**  INTEGER |
| **comment**  STRING |
| **created\_at**  DATE-TIME |
| **group\_id**  INTEGER |
| **id**  INTEGER |
| **reason**  STRING |
| **reason\_id**  INTEGER |
| **requester\_id**  INTEGER |
| **score**  STRING |
| **ticket\_id**  INTEGER |
| **updated\_at**  DATE-TIME |
| **url**  STRING |

### sla\_policies

The `sla_policies` table contains info about the Service Level Agreements (SLAs) in your Zendesk Support account. An SLA is a documented agreement between a support provider and their customers that defines performance measures for support.

**Note**: Replicating SLA policies requires that you be on an Enterprise or Professional Zendesk Support plan, and have Admin permissions in Zendesk Support.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Zendesk Support documentation](https://developer.zendesk.com/documentation/)  [Zendesk Support API method](https://developer.zendesk.com/api-reference/ticketing/business-rules/sla_policies/ "Opens in new tab: Zendesk Support API method") |

sla\_policies table schema

|  |
| --- |
| **created\_at**  DATE-TIME |
| **description**  STRING |
| **filter**  OBJECT This is a nested data structure:   - all: ARRAY, which is also a nested data structure.   - field: STRING   - operator: STRING   - value: STRING - any: ARRAY, which is also a nested data structure.   - field: STRING   - operator: STRING   - value: STRING |
| **id**  INTEGER |
| **policy\_metrics**  ARRAY This is a nested data structure:   - business\_hours: BOOLEAN - priority: STRING - target: INTEGER |
| **position**  INTEGER |
| **title**  STRING |
| **updated\_at**  DATE-TIME |
| **url**  STRING |

### tags

The `tags` table the names and total number of applications of the tags in your Zendesk Support account.

**Note**: Retrieving tag data requires Zendesk Support Admin permissions.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | name |
| **Useful links** | [Zendesk Support documentation](https://developer.zendesk.com/documentation/)  [Zendesk Support API method](https://developer.zendesk.com/api-reference/ticketing/ticket-management/tags/ "Opens in new tab: Zendesk Support API method") |

tags table foreign keys

| Join tags with | on |
| --- | --- |
| [organizations](#organizations) | ``` tags.name = organizations.tags ``` |
| [tickets](#tickets) | ``` tags.name = tickets.tags ``` |
| [users](#users) | ``` tags.name = users.tags ``` |

tags table schema

|  |
| --- |
| **count**  INTEGER |
| **name**  STRING |

### talk\_phone\_numbers

This table contains data about phone numbers in Zendesk Talk.

**Note**: Zendesk Voice is an add-on feature and is not enabled by default. You can create a Zendesk Support connection without Zendesk Voice. However, the `talk_phone_numbers` table is replicated through the Zendesk Voice API. To replicate this table, your Zendesk account must have at least a Suite Team subscription and the Zendesk Voice add-on enabled. See [Zendesk pricing](https://www.zendesk.com/pricing/).

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Zendesk Support documentation](https://developer.zendesk.com/documentation/voice/)  [Zendesk Support API method](https://developer.zendesk.com/api-reference/voice/talk-api/phone_numbers/ "Opens in new tab: Zendesk Support API method") |

talk\_phone\_numbers table schema

|  |
| --- |
| **capabilities**  OBJECT This is a nested data structure:   - mms: BOOLEAN - sms: BOOLEAN - voice: BOOLEAN |
| **categorised\_greetings**  OBJECT This is a nested data structure. |
| **categorised\_greetings\_with\_sub\_settings**  OBJECT This is a nested data structure. |
| **country\_code**  STRING |
| **created\_at**  DATE-TIME |
| **default\_greeting\_ids**  ARRAY This is a nested data structure. |
| **default\_group\_id**  INTEGER |
| **display\_number**  STRING |
| **external**  BOOLEAN |
| **greeting\_ids**  ARRAY This is a nested data structure. |
| **group\_ids**  ARRAY This is a nested data structure. |
| **id**  INTEGER |
| **ivr\_id**  INTEGER |
| **line\_type**  STRING |
| **location**  STRING |
| **name**  STRING |
| **nickname**  STRING |
| **number**  STRING |
| **outbound\_enabled**  BOOLEAN |
| **priority**  INTEGER |
| **recorded**  BOOLEAN |
| **schedule\_id**  INTEGER |
| **sms\_enabled**  BOOLEAN |
| **sms\_group\_id**  INTEGER |
| **token**  STRING |
| **toll\_free**  BOOLEAN |
| **transcription**  BOOLEAN |
| **voice\_enabled**  BOOLEAN |

### ticket\_audits

The `ticket_audits` table contains info about the activity associated with a ticket. An audit is a history of all updates to a given ticket. When a ticket is updated in Zendesk Support, an audit record is created. Each audit represents a single update to a ticket.

A single audit record may include multiple event types. For example: A ticket comment, satisfaction rating, and a change event. For a full list of Zendesk Support audit event types, [refer to Zendesk Support’s documentation](https://developer.zendesk.com/rest_api/Content/support/ticket_audits#audit-events).

#### Replication

This table uses Append-Only Incremental Replication. This means that new audit records, or updates made to existing audits, are appended as new rows to the end of the table.

|  |  |
| --- | --- |
| **Replication Method** | Append-Only Incremental |
| **Primary Key** | id |
| **Replication Key** | created\_at |
| **Useful links** | [Zendesk Support documentation](https://developer.zendesk.com/documentation/ticketing/)  [Zendesk Support API method](https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_audits/#list-audits-for-a-ticket "Opens in new tab: Zendesk Support API method") |

ticket\_audits table foreign keys

| Join ticket\_audits with | on |
| --- | --- |
| [macros](#macros) | ``` ticket_audits.events.macro_id = macros.id ``` |
| [ticket\_comments](#ticket-comments) | ``` ticket_audits.id = ticket_comments.audit_id ```  ``` ticket_audits.events.audit_id = ticket_comments.audit_id ```  ``` ticket_audits.ticket_id = ticket_comments.ticket_id ```  ``` ticket_audits.author_id = ticket_comments.author_id ``` |
| [satisfaction\_ratings](#satisfaction-ratings) | ``` ticket_audits.ticket_id = satisfaction_ratings.ticket_id ```  ``` ticket_audits.author_id = satisfaction_ratings.assignee_id ```  ``` ticket_audits.author_id = satisfaction_ratings.requester_id ``` |
| [tickets](#tickets) | ``` ticket_audits.ticket_id = tickets.id ```  ``` ticket_audits.author_id = tickets.requester_id ```  ``` ticket_audits.author_id = tickets.follower_ids ```  ``` ticket_audits.author_id = tickets.submitter_id ```  ``` ticket_audits.author_id = tickets.collaborator_ids ```  ``` ticket_audits.author_id = tickets.assignee_id ``` |
| [ticket\_metrics](#ticket-metrics) | ``` ticket_audits.ticket_id = ticket_metrics.ticket_id ``` |
| [users](#users) | ``` ticket_audits.author_id = users.id ``` |

ticket\_audits table schema

|  |
| --- |
| **author\_id**  INTEGER |
| **created\_at**  DATE-TIME |
| **events**  ARRAY This is a nested data structure:   - attachments: ARRAY, which is also a nested data structure. - audit\_id: INTEGER - author\_id: INTEGER - body: STRING - created\_at: DATE-TIME - data: OBJECT, which is also a nested data structure.   - answered\_by\_id: INTEGER   - answered\_by\_name: STRING   - call\_duration: STRING   - from: STRING   - recording\_url: STRING   - started\_at: DATE-TIME   - to: STRING   - transcription\_status: STRING   - transcription\_text: STRING - field\_name: STRING - formatted\_from: STRING - formatted\_to: STRING - html\_body: STRING - id: INTEGER - macro\_deleted: BOOLEAN - macro\_id: STRING - macro\_title: STRING - plain\_body: STRING - previous\_value: ARRAY, STRING, which is also a nested data structure. - public: BOOLEAN - recipients: ARRAY, which is also a nested data structure. - resource: STRING - subject: STRING - trusted: BOOLEAN - type: STRING - value: ARRAY, STRING, which is also a nested data structure. - via: OBJECT, which is also a nested data structure.   - channel: STRING   - source: OBJECT, which is also a nested data structure.     - from: OBJECT, which is also a nested data structure.       - address: STRING       - deleted: BOOLEAN       - id: INTEGER       - name: STRING       - original\_recipients: ARRAY, which is also a nested data structure.       - revision\_id: INTEGER       - subject: STRING       - ticket\_id: INTEGER       - title: STRING     - rel: STRING     - to: OBJECT, which is also a nested data structure.       - address: STRING       - name: STRING |
| **id**  INTEGER |
| **metadata**  OBJECT This is a nested data structure:   - flags: ARRAY, which is also a nested data structure. - flags\_options: OBJECT, which is also a nested data structure.   - 11: OBJECT, which is also a nested data structure.     - message: OBJECT, which is also a nested data structure.       - user: STRING     - trusted: BOOLEAN   - 2: OBJECT, which is also a nested data structure.     - trusted: BOOLEAN - notifications\_suppressed\_for: ARRAY, which is also a nested data structure. - system: OBJECT, which is also a nested data structure.   - client: STRING   - ip\_address: STRING   - json\_email\_identifier: STRING   - latitude: NUMBER   - location: STRING   - longitude: NUMBER   - message\_id: STRING   - raw\_email\_identifier: STRING - trusted: BOOLEAN |
| **ticket\_id**  INTEGER |
| **via**  OBJECT This is a nested data structure:   - channel: STRING - source: OBJECT, which is also a nested data structure.   - from: OBJECT, which is also a nested data structure.     - address: STRING     - deleted: BOOLEAN     - id: INTEGER     - name: STRING     - original\_recipients: ARRAY, which is also a nested data structure.     - subject: STRING     - ticket\_id: INTEGER     - ticket\_ids: ARRAY, which is also a nested data structure.     - title: STRING   - rel: STRING   - to: OBJECT, which is also a nested data structure.     - address: STRING     - name: STRING |

### ticket\_comments

The `ticket_comments` table contains info about the comments on tickets, which is the conversation between requesters, collaborators, and agents. Comments can be public or private.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | created\_at |
| **Useful links** | [Zendesk Support documentation](https://developer.zendesk.com/documentation/ticketing/)  [Zendesk Support API method](https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_comments/ "Opens in new tab: Zendesk Support API method") |

ticket\_comments table foreign keys

| Join ticket\_comments with | on |
| --- | --- |
| [ticket\_audits](#ticket-audits) | ``` ticket_comments.audit_id = ticket_audits.id ```  ``` ticket_comments.audit_id = ticket_audits.events.audit_id ```  ``` ticket_comments.ticket_id = ticket_audits.ticket_id ```  ``` ticket_comments.author_id = ticket_audits.author_id ``` |
| [satisfaction\_ratings](#satisfaction-ratings) | ``` ticket_comments.ticket_id = satisfaction_ratings.ticket_id ```  ``` ticket_comments.author_id = satisfaction_ratings.assignee_id ```  ``` ticket_comments.author_id = satisfaction_ratings.requester_id ``` |
| [tickets](#tickets) | ``` ticket_comments.ticket_id = tickets.id ```  ``` ticket_comments.author_id = tickets.requester_id ```  ``` ticket_comments.author_id = tickets.follower_ids ```  ``` ticket_comments.author_id = tickets.submitter_id ```  ``` ticket_comments.author_id = tickets.collaborator_ids ```  ``` ticket_comments.author_id = tickets.assignee_id ``` |
| [ticket\_metrics](#ticket-metrics) | ``` ticket_comments.ticket_id = ticket_metrics.ticket_id ``` |
| [users](#users) | ``` ticket_comments.author_id = users.id ``` |

ticket\_comments table schema

|  |
| --- |
| **attachments**  ARRAY This is a nested data structure. |
| **audit\_id**  INTEGER |
| **author\_id**  INTEGER |
| **body**  STRING |
| **created\_at**  DATE-TIME |
| **html\_body**  STRING |
| **id**  INTEGER |
| **metadata**  OBJECT This is a nested data structure:   - flags: ARRAY, which is also a nested data structure. - flags\_options: OBJECT, which is also a nested data structure.   - 11: OBJECT, which is also a nested data structure.     - message: OBJECT, which is also a nested data structure.       - user: STRING     - trusted: BOOLEAN   - 2: OBJECT, which is also a nested data structure.     - trusted: BOOLEAN - notifications\_suppressed\_for: ARRAY, which is also a nested data structure. - system: OBJECT, which is also a nested data structure.   - client: STRING   - ip\_address: STRING   - json\_email\_identifier: STRING   - latitude: NUMBER   - location: STRING   - longitude: NUMBER   - message\_id: STRING   - raw\_email\_identifier: STRING - trusted: BOOLEAN |
| **plain\_body**  STRING |
| **public**  BOOLEAN |
| **ticket\_id**  INTEGER |
| **type**  STRING |
| **via**  OBJECT This is a nested data structure:   - channel: STRING - source: OBJECT, which is also a nested data structure.   - from: OBJECT, which is also a nested data structure.     - address: STRING     - deleted: BOOLEAN     - id: INTEGER     - name: STRING     - original\_recipients: ARRAY, which is also a nested data structure.     - subject: STRING     - ticket\_id: INTEGER     - ticket\_ids: ARRAY, which is also a nested data structure.     - title: STRING   - rel: STRING   - to: OBJECT, which is also a nested data structure.     - address: STRING     - name: STRING |

### ticket\_fields

The `ticket_fields` table contains info about the basic text and custom ticket fields in your Zendesk Support account.

**Note**: Retrieving ticket metric data requires Zendesk Support Agent or Admin permissions.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Zendesk Support documentation](https://developer.zendesk.com/documentation/ticketing/)  [Zendesk Support API method](https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_fields/ "Opens in new tab: Zendesk Support API method") |

ticket\_fields table foreign keys

| Join ticket\_fields with | on |
| --- | --- |
| [ticket\_forms](#ticket-forms) | ``` ticket_fields.id = ticket_forms.ticket_field_ids ``` |
| [tickets](#tickets) | ``` ticket_fields.id = tickets.custom_fields.id ``` |

ticket\_fields table schema

|  |
| --- |
| **active**  BOOLEAN |
| **agent\_can\_edit**  BOOLEAN |
| **agent\_description**  STRING |
| **collapsed\_for\_agents**  BOOLEAN |
| **created\_at**  DATE-TIME |
| **custom\_field\_options**  ARRAY This is a nested data structure:   - default: BOOLEAN - id: INTEGER - name: STRING - raw\_name: STRING - value: STRING |
| **description**  STRING |
| **editable\_in\_portal**  BOOLEAN |
| **id**  INTEGER |
| **key**  STRING |
| **position**  INTEGER |
| **raw\_agent\_description**  STRING |
| **raw\_description**  STRING |
| **raw\_title**  STRING |
| **raw\_title\_in\_portal**  STRING |
| **regexp\_for\_validation**  STRING |
| **removable**  BOOLEAN |
| **required**  BOOLEAN |
| **required\_in\_portal**  BOOLEAN |
| **sub\_type\_id**  INTEGER |
| **system\_field\_options**  ARRAY This is a nested data structure. |
| **tag**  STRING |
| **title**  STRING |
| **title\_in\_portal**  STRING |
| **type**  STRING |
| **updated\_at**  DATE-TIME |
| **url**  STRING |
| **visible\_in\_portal**  BOOLEAN |

### ticket\_forms

The `ticket_forms` table contains info about the ticket forms in your Zendesk Support account.

**Note**: Replicating ticket forms requires that you be on an Enterprise Zendesk Support plan or a Professional plan with the corresponding add-on, and have Admin permissions in Zendesk Support.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Zendesk Support documentation](https://developer.zendesk.com/documentation/ticketing/)  [Zendesk Support API method](https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_forms/ "Opens in new tab: Zendesk Support API method") |

ticket\_forms table foreign keys

| Join ticket\_forms with | on |
| --- | --- |
| [ticket\_fields](#ticket-fields) | ``` ticket_forms.ticket_field_ids = ticket_fields.id ``` |
| [tickets](#tickets) | ``` ticket_forms.ticket_field_ids = tickets.custom_fields.id ```  ``` ticket_forms.id = tickets.ticket_form_id ``` |

ticket\_forms table schema

|  |
| --- |
| **active**  BOOLEAN |
| **agent\_conditions**  ARRAY |
| **created\_at**  DATE-TIME |
| **default**  BOOLEAN |
| **deleted\_at**  DATE-TIME |
| **display\_name**  STRING |
| **end\_user\_conditions**  ARRAY |
| **end\_user\_visible**  BOOLEAN |
| **form\_type**  STRING |
| **id**  INTEGER |
| **in\_all\_brands**  BOOLEAN |
| **name**  STRING |
| **position**  INTEGER |
| **raw\_display\_name**  STRING |
| **raw\_name**  STRING |
| **restricted\_brand\_ids**  ARRAY This is a nested data structure. |
| **ticket\_field\_ids**  ARRAY This is a nested data structure. |
| **updated\_at**  DATE-TIME |
| **url**  STRING |

### ticket\_metric\_events

This table contains data about reply times, agent work times, and requester wait times.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | time |
| **Useful links** | [Zendesk Support documentation](https://developer.zendesk.com/documentation/ticketing/)  [Zendesk Support API method](https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_metric_events/ "Opens in new tab: Zendesk Support API method") |

ticket\_metric\_events table schema

|  |
| --- |
| **deleted**  BOOLEAN |
| **id**  INTEGER |
| **instance\_id**  INTEGER |
| **metric**  STRING |
| **sla**  OBJECT This is a nested data structure:   - business\_hours: BOOLEAN - policy: OBJECT, which is also a nested data structure.   - description: STRING   - id: INTEGER   - title: STRING - target: INTEGER |
| **status**  OBJECT This is a nested data structure:   - business: INTEGER - calendar: INTEGER |
| **ticket\_id**  INTEGER |
| **time**  DATE-TIME |
| **type**  STRING |

### ticket\_metrics

The `ticket_metrics` table contains info about the metrics associated with Zendesk Support tickets. **This table will not include records for deleted tickets.**

**Note**: Retrieving ticket metric data requires Zendesk Support Admin permissions.

#### Deleted ticket metrics

As Zendesk Support’s API doesn’t currently support returning metrics for deleted tickets, this table will not contain any metrics for deleted tickets.

If you believe you’re missing records, check in your Zendesk Support account to see if the missing records are for deleted tickets.

For more info on how Zendesk Support handles deleting tickets, [refer to their documentation](https://support.zendesk.com/hc/en-us/articles/203690936).

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Zendesk Support documentation](https://developer.zendesk.com/documentation/ticketing/)  [Zendesk Support API method](https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_metrics/ "Opens in new tab: Zendesk Support API method") |

ticket\_metrics table foreign keys

| Join ticket\_metrics with | on |
| --- | --- |
| [satisfaction\_ratings](#satisfaction-ratings) | ``` ticket_metrics.ticket_id = satisfaction_ratings.ticket_id ``` |
| [tickets](#tickets) | ``` ticket_metrics.ticket_id = tickets.id ``` |
| [ticket\_audits](#ticket-audits) | ``` ticket_metrics.ticket_id = ticket_audits.ticket_id ``` |
| [ticket\_comments](#ticket-comments) | ``` ticket_metrics.ticket_id = ticket_comments.ticket_id ``` |

ticket\_metrics table schema

|  |
| --- |
| **agent\_wait\_time\_in\_minutes**  OBJECT This is a nested data structure:   - business: INTEGER - calendar: INTEGER |
| **assigned\_at**  DATE-TIME |
| **assignee\_stations**  INTEGER |
| **assignee\_updated\_at**  DATE-TIME |
| **created\_at**  DATE-TIME |
| **custom\_status\_updated\_at**  DATE-TIME |
| **first\_resolution\_time\_in\_minutes**  OBJECT This is a nested data structure:   - business: INTEGER - calendar: INTEGER |
| **full\_resolution\_time\_in\_minutes**  OBJECT This is a nested data structure:   - business: INTEGER - calendar: INTEGER |
| **group\_stations**  INTEGER |
| **id**  INTEGER |
| **initially\_assigned\_at**  DATE-TIME |
| **instance\_id**  INTEGER |
| **latest\_comment\_added\_at**  DATE-TIME |
| **metric**  STRING |
| **on\_hold\_time\_in\_minutes**  OBJECT This is a nested data structure:   - business: INTEGER - calendar: INTEGER |
| **reopens**  INTEGER |
| **replies**  INTEGER |
| **reply\_time\_in\_minutes**  OBJECT This is a nested data structure:   - business: INTEGER - calendar: INTEGER |
| **requester\_updated\_at**  DATE-TIME |
| **requester\_wait\_time\_in\_minutes**  OBJECT This is a nested data structure:   - business: INTEGER - calendar: INTEGER |
| **solved\_at**  DATE-TIME |
| **status**  OBJECT This is a nested data structure:   - business: INTEGER - calendar: INTEGER |
| **status\_updated\_at**  DATE-TIME |
| **ticket\_id**  INTEGER |
| **time**  STRING |
| **type**  STRING |
| **updated\_at**  DATE-TIME |
| **url**  STRING |

### tickets

The `tickets` table contains info about the tickets in your Zendesk Support account. Tickets are the means through which your end users (customers) communicate with your Zendesk Support agents.

**Note**: Retrieving ticket data requires Zendesk Support Admin permissions.

#### Custom ticket fields

Zendesk Support integration will replicate all custom ticket fields.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | generated\_timestamp |
| **Useful links** | [Zendesk Support documentation](https://developer.zendesk.com/documentation/ticketing/)  [Zendesk Support API method](https://developer.zendesk.com/api-reference/ticketing/ticket-management/incremental_exports/#incremental-ticket-export-cursor-based "Opens in new tab: Zendesk Support API method") |

tickets table foreign keys

| Join tickets with | on |
| --- | --- |
| [groups](#groups) | ``` tickets.group_id = groups.id ``` |
| [group\_memberships](#group-memberships) | ``` tickets.group_id = group_memberships.group_id ``` |
| [organizations](#organizations) | ``` tickets.group_id = organizations.group_id ```  ``` tickets.organization_id = organizations.id ```  ``` tickets.tags = organizations.tags ``` |
| [satisfaction\_ratings](#satisfaction-ratings) | ``` tickets.group_id = satisfaction_ratings.group_id ```  ``` tickets.id = satisfaction_ratings.ticket_id ```  ``` tickets.requester_id = satisfaction_ratings.assignee_id ```  ``` tickets.follower_ids = satisfaction_ratings.assignee_id ```  ``` tickets.submitter_id = satisfaction_ratings.assignee_id ```  ``` tickets.collaborator_ids = satisfaction_ratings.assignee_id ```  ``` tickets.assignee_id = satisfaction_ratings.assignee_id ```  ``` tickets.requester_id = satisfaction_ratings.requester_id ```  ``` tickets.follower_ids = satisfaction_ratings.requester_id ```  ``` tickets.submitter_id = satisfaction_ratings.requester_id ```  ``` tickets.collaborator_ids = satisfaction_ratings.requester_id ```  ``` tickets.assignee_id = satisfaction_ratings.requester_id ``` |
| [users](#users) | ``` tickets.group_id = users.default_group_id ```  ``` tickets.organization_id = users.organization_id ```  ``` tickets.tags = users.tags ```  ``` tickets.requester_id = users.id ```  ``` tickets.follower_ids = users.id ```  ``` tickets.submitter_id = users.id ```  ``` tickets.collaborator_ids = users.id ```  ``` tickets.assignee_id = users.id ``` |
| [tags](#tags) | ``` tickets.tags = tags.name ``` |
| [ticket\_fields](#ticket-fields) | ``` tickets.custom_fields.id = ticket_fields.id ``` |
| [ticket\_forms](#ticket-forms) | ``` tickets.custom_fields.id = ticket_forms.ticket_field_ids ```  ``` tickets.ticket_form_id = ticket_forms.id ``` |
| [ticket\_audits](#ticket-audits) | ``` tickets.id = ticket_audits.ticket_id ```  ``` tickets.requester_id = ticket_audits.author_id ```  ``` tickets.follower_ids = ticket_audits.author_id ```  ``` tickets.submitter_id = ticket_audits.author_id ```  ``` tickets.collaborator_ids = ticket_audits.author_id ```  ``` tickets.assignee_id = ticket_audits.author_id ``` |
| [ticket\_comments](#ticket-comments) | ``` tickets.id = ticket_comments.ticket_id ```  ``` tickets.requester_id = ticket_comments.author_id ```  ``` tickets.follower_ids = ticket_comments.author_id ```  ``` tickets.submitter_id = ticket_comments.author_id ```  ``` tickets.collaborator_ids = ticket_comments.author_id ```  ``` tickets.assignee_id = ticket_comments.author_id ``` |
| [ticket\_metrics](#ticket-metrics) | ``` tickets.id = ticket_metrics.ticket_id ``` |

tickets table schema

|  |
| --- |
| **allow\_attachments**  BOOLEAN |
| **allow\_channelback**  BOOLEAN |
| **assignee\_id**  INTEGER |
| **brand\_id**  INTEGER |
| **collaborator\_ids**  ARRAY This is a nested data structure. |
| **created\_at**  DATE-TIME |
| **custom\_fields**  ARRAY This is a nested data structure:   - id: INTEGER |
| **custom\_status\_id**  INTEGER |
| **description**  STRING |
| **due\_at**  DATE-TIME |
| **email\_cc\_ids**  ARRAY This is a nested data structure. |
| **encoded\_id**  STRING |
| **external\_id**  STRING |
| **fields**  ARRAY |
| **follower\_ids**  ARRAY This is a nested data structure. |
| **followup\_ids**  ARRAY This is a nested data structure. |
| **from\_messaging\_channel**  BOOLEAN |
| **forum\_topic\_id**  INTEGER |
| **generated\_timestamp**  INTEGER |
| **group\_id**  INTEGER |
| **has\_incidents**  BOOLEAN |
| **id**  INTEGER |
| **is\_public**  BOOLEAN |
| **organization\_id**  INTEGER |
| **priority**  STRING |
| **problem\_id**  INTEGER |
| **raw\_subject**  STRING |
| **recipient**  STRING |
| **requester\_id**  INTEGER |
| **satisfaction\_rating**  OBJECT, STRING This is a nested data structure:   - assignee\_id: INTEGER - comment: STRING - created\_at: DATE-TIME - group\_id: INTEGER - id: INTEGER - reason: STRING - reason\_id: INTEGER - requester\_id: INTEGER - score: STRING - ticket\_id: INTEGER - updated\_at: DATE-TIME - url: STRING |
| **sharing\_agreement\_ids**  ARRAY This is a nested data structure. |
| **status**  STRING |
| **subject**  STRING |
| **submitter\_id**  INTEGER |
| **support\_type**  STRING |
| **tags**  ARRAY This is a nested data structure. |
| **ticket\_form\_id**  INTEGER |
| **type**  STRING |
| **updated\_at**  DATE-TIME |
| **url**  STRING |
| **via**  OBJECT This is a nested data structure:   - channel: STRING - source: OBJECT, which is also a nested data structure.   - from: OBJECT, which is also a nested data structure.     - address: STRING     - name: STRING     - subject: STRING     - ticket\_id: INTEGER   - rel: STRING   - to: OBJECT, which is also a nested data structure.     - address: STRING     - name: STRING |

### users

The `users` table contains info about the users associated with your Zendesk Support account. This includes agents, admins, and end-users (customers).

**Note**: Retrieving user data requires Zendesk Support Admin permissions.

#### Custom user fields

Zendesk Support integration will replicate any custom fields associated with user records.

**Note**: Replicating user custom fields requires that you be on a Team, Professional, or Enterprise Zendesk Support plan.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [Zendesk Support documentation](https://developer.zendesk.com/documentation/ticketing/)  [Zendesk Support API method](https://developer.zendesk.com/api-reference/ticketing/users/users/ "Opens in new tab: Zendesk Support API method") |

users table foreign keys

| Join users with | on |
| --- | --- |
| [groups](#groups) | ``` users.default_group_id = groups.id ```  ``` users.id = groups.id ``` |
| [group\_memberships](#group-memberships) | ``` users.default_group_id = group_memberships.group_id ``` |
| [organizations](#organizations) | ``` users.default_group_id = organizations.group_id ```  ``` users.organization_id = organizations.id ```  ``` users.tags = organizations.tags ``` |
| [satisfaction\_ratings](#satisfaction-ratings) | ``` users.default_group_id = satisfaction_ratings.group_id ```  ``` users.id = satisfaction_ratings.assignee_id ```  ``` users.id = satisfaction_ratings.requester_id ``` |
| [tickets](#tickets) | ``` users.default_group_id = tickets.group_id ```  ``` users.organization_id = tickets.organization_id ```  ``` users.tags = tickets.tags ```  ``` users.id = tickets.requester_id ```  ``` users.id = tickets.follower_ids ```  ``` users.id = tickets.submitter_id ```  ``` users.id = tickets.collaborator_ids ```  ``` users.id = tickets.assignee_id ``` |
| [macros](#macros) | ``` users.id = macros.restriction.id ``` |
| [tags](#tags) | ``` users.tags = tags.name ``` |
| [ticket\_audits](#ticket-audits) | ``` users.id = ticket_audits.author_id ``` |
| [ticket\_comments](#ticket-comments) | ``` users.id = ticket_comments.author_id ``` |

users table schema

|  |
| --- |
| **active**  BOOLEAN |
| **alias**  STRING |
| **chat\_only**  BOOLEAN |
| **created\_at**  DATE-TIME |
| **custom\_role\_id**  INTEGER |
| **default\_group\_id**  INTEGER |
| **details**  STRING |
| **email**  STRING |
| **external\_id**  STRING |
| **id**  INTEGER |
| **iana\_time\_zone**  STRING |
| **is\_billing\_admin**  BOOLEAN |
| **last\_login\_at**  DATE-TIME |
| **locale**  STRING |
| **locale\_id**  INTEGER |
| **moderator**  BOOLEAN |
| **name**  STRING |
| **notes**  STRING |
| **only\_private\_comments**  BOOLEAN |
| **organization\_id**  INTEGER |
| **permanently\_deleted**  BOOLEAN |
| **phone**  STRING |
| **photo**  OBJECT This is a nested data structure. |
| **report\_csv**  BOOLEAN |
| **restricted\_agent**  BOOLEAN |
| **role**  STRING |
| **role\_type**  INTEGER |
| **shared**  BOOLEAN |
| **shared\_agent**  BOOLEAN |
| **shared\_phone\_number**  BOOLEAN |
| **signature**  STRING |
| **suspended**  BOOLEAN |
| **suspension\_details**  OBJECT |
| **tags**  ARRAY This is a nested data structure. |
| **ticket\_restriction**  STRING |
| **time\_zone**  STRING |
| **two\_factor\_auth\_enabled**  BOOLEAN |
| **updated\_at**  DATE-TIME |
| **url**  STRING |
| **user\_fields**  OBJECT This is a nested data structure. |
| **verified**  BOOLEAN |
