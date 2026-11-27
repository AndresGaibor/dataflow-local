---
title: "Outreach"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Outreach.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Outreach

Outreach is a sales engagement platform that accelerates revenue growth by optimizing every interaction throughout the customer lifecycle.

Outreach integration replicates data using the [Outreach REST API](https://api.outreach.io/api/v2/docs).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To generate your OAuth Application ID and Application Secret:

1. Log into your [Outreach Developers](https://developers.outreach.io/apps) account.
2. Select the OAuth application you want to use, or create a new one.
3. In the left navigation bar, click Feature Selection to make sure the Outreach OAuth API feature is added.
4. In the left navigation bar, click API access (OAuth) to generate your OAuth Application ID.
5. Copy and save the Application Secret in a secured file. You will need it to connect to the application.
6. Enter https://connector.qlik.com/auth/oauth/v3.htm as your Callback URL.
7. Make sure the following scopes are selected in the configuration:
   - callDispositions.read
   - callPurposes.read
   - duties.read
   - events.read
   - mailboxes.read
   - stages.read
   - users.read
   - accounts.read
   - calls.read
   - personas.read
   - prospects.read
   - mailings.read
   - opportunities.read
   - tasks.read
   - teams.read
   - contentCategories.read
   - sequences.read
   - sequenceTemplates.read
   - sequenceStates.read
   - sequenceSteps.read

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
| Quota Limit | The percentage of the rate limit dedicated to the tap. |
| OAuth Application ID | OAuth Application ID. |
| Application Secret | Application secret. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### accounts

The `accounts` table contains information about prospective clients in Outreach.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [Outreach API method](https://api.outreach.io/api/v2/docs#account "Opens in new tab: Outreach API method") |

accounts table foreign keys

| Join accounts with | on |
| --- | --- |
| [opportunities](#opportunities) | ``` accounts.id = opportunities.id ```  ``` accounts.creatorId = opportunities.creatorId ```  ``` accounts.ownerId = opportunities.creatorId ```  ``` accounts.updaterId = opportunities.creatorId ```  ``` accounts.creatorId = opportunities.ownerId ```  ``` accounts.ownerId = opportunities.ownerId ```  ``` accounts.updaterId = opportunities.ownerId ``` |
| [prospects](#prospects) | ``` accounts.id = prospects.id ```  ``` accounts.creatorId = prospects.creatorId ```  ``` accounts.ownerId = prospects.creatorId ```  ``` accounts.updaterId = prospects.creatorId ```  ``` accounts.creatorId = prospects.updaterId ```  ``` accounts.ownerId = prospects.updaterId ```  ``` accounts.updaterId = prospects.updaterId ``` |
| [sequence\_states](#sequence-states) | ``` accounts.id = sequence_states.id ```  ``` accounts.creatorId = sequence_states.creatorId ```  ``` accounts.ownerId = sequence_states.creatorId ```  ``` accounts.updaterId = sequence_states.creatorId ``` |
| [tasks](#tasks) | ``` accounts.id = tasks.id ```  ``` accounts.creatorId = tasks.creatorId ```  ``` accounts.ownerId = tasks.creatorId ```  ``` accounts.updaterId = tasks.creatorId ```  ``` accounts.creatorId = tasks.completerId ```  ``` accounts.ownerId = tasks.completerId ```  ``` accounts.updaterId = tasks.completerId ``` |
| [call\_dispositions](#call-dispositions) | ``` accounts.creatorId = call_dispositions.creatorId ```  ``` accounts.ownerId = call_dispositions.creatorId ```  ``` accounts.updaterId = call_dispositions.creatorId ``` |
| [call\_purposes](#call-purposes) | ``` accounts.creatorId = call_purposes.creatorId ```  ``` accounts.ownerId = call_purposes.creatorId ```  ``` accounts.updaterId = call_purposes.creatorId ``` |
| [calls](#calls) | ``` accounts.creatorId = calls.userId ```  ``` accounts.ownerId = calls.userId ```  ``` accounts.updaterId = calls.userId ``` |
| [content\_categories](#content-categories) | ``` accounts.creatorId = content_categories.creatorId ```  ``` accounts.ownerId = content_categories.creatorId ```  ``` accounts.updaterId = content_categories.creatorId ``` |
| [mailboxes](#mailboxes) | ``` accounts.creatorId = mailboxes.creatorId ```  ``` accounts.ownerId = mailboxes.creatorId ```  ``` accounts.updaterId = mailboxes.creatorId ```  ``` accounts.creatorId = mailboxes.updaterId ```  ``` accounts.ownerId = mailboxes.updaterId ```  ``` accounts.updaterId = mailboxes.updaterId ```  ``` accounts.creatorId = mailboxes.userId ```  ``` accounts.ownerId = mailboxes.userId ```  ``` accounts.updaterId = mailboxes.userId ``` |
| [sequence\_steps](#sequence-steps) | ``` accounts.creatorId = sequence_steps.creatorId ```  ``` accounts.ownerId = sequence_steps.creatorId ```  ``` accounts.updaterId = sequence_steps.creatorId ```  ``` accounts.creatorId = sequence_steps.updaterId ```  ``` accounts.ownerId = sequence_steps.updaterId ```  ``` accounts.updaterId = sequence_steps.updaterId ``` |
| [sequence\_templates](#sequence-templates) | ``` accounts.creatorId = sequence_templates.creatorId ```  ``` accounts.ownerId = sequence_templates.creatorId ```  ``` accounts.updaterId = sequence_templates.creatorId ```  ``` accounts.creatorId = sequence_templates.updaterId ```  ``` accounts.ownerId = sequence_templates.updaterId ```  ``` accounts.updaterId = sequence_templates.updaterId ``` |
| [sequences](#sequences) | ``` accounts.creatorId = sequences.creatorId ```  ``` accounts.ownerId = sequences.creatorId ```  ``` accounts.updaterId = sequences.creatorId ```  ``` accounts.creatorId = sequences.ownerId ```  ``` accounts.ownerId = sequences.ownerId ```  ``` accounts.updaterId = sequences.ownerId ```  ``` accounts.creatorId = sequences.updaterId ```  ``` accounts.ownerId = sequences.updaterId ```  ``` accounts.updaterId = sequences.updaterId ``` |
| [stages](#stages) | ``` accounts.creatorId = stages.creatorId ```  ``` accounts.ownerId = stages.creatorId ```  ``` accounts.updaterId = stages.creatorId ```  ``` accounts.creatorId = stages.updaterId ```  ``` accounts.ownerId = stages.updaterId ```  ``` accounts.updaterId = stages.updaterId ``` |
| [users](#users) | ``` accounts.creatorId = users.creatorId ```  ``` accounts.ownerId = users.creatorId ```  ``` accounts.updaterId = users.creatorId ```  ``` accounts.creatorId = users.id ```  ``` accounts.ownerId = users.id ```  ``` accounts.updaterId = users.id ```  ``` accounts.creatorId = users.updaterId ```  ``` accounts.ownerId = users.updaterId ```  ``` accounts.updaterId = users.updaterId ``` |

accounts table schema

|  |
| --- |
| **buyerIntentScore**  NUMBER |
| **companyType**  STRING |
| **createdAt**  DATE-TIME |
| **creatorId**  INTEGER |
| **custom1**  STRING |
| **custom10**  STRING |
| **custom100**  STRING |
| **custom101**  STRING |
| **custom102**  STRING |
| **custom103**  STRING |
| **custom104**  STRING |
| **custom105**  STRING |
| **custom106**  STRING |
| **custom107**  STRING |
| **custom108**  STRING |
| **custom109**  STRING |
| **custom11**  STRING |
| **custom110**  STRING |
| **custom111**  STRING |
| **custom112**  STRING |
| **custom113**  STRING |
| **custom114**  STRING |
| **custom115**  STRING |
| **custom116**  STRING |
| **custom117**  STRING |
| **custom118**  STRING |
| **custom119**  STRING |
| **custom12**  STRING |
| **custom120**  STRING |
| **custom121**  STRING |
| **custom122**  STRING |
| **custom123**  STRING |
| **custom124**  STRING |
| **custom125**  STRING |
| **custom126**  STRING |
| **custom127**  STRING |
| **custom128**  STRING |
| **custom129**  STRING |
| **custom13**  STRING |
| **custom130**  STRING |
| **custom131**  STRING |
| **custom132**  STRING |
| **custom133**  STRING |
| **custom134**  STRING |
| **custom135**  STRING |
| **custom136**  STRING |
| **custom137**  STRING |
| **custom138**  STRING |
| **custom139**  STRING |
| **custom14**  STRING |
| **custom140**  STRING |
| **custom141**  STRING |
| **custom142**  STRING |
| **custom143**  STRING |
| **custom144**  STRING |
| **custom145**  STRING |
| **custom146**  STRING |
| **custom147**  STRING |
| **custom148**  STRING |
| **custom149**  STRING |
| **custom15**  STRING |
| **custom150**  STRING |
| **custom16**  STRING |
| **custom17**  STRING |
| **custom18**  STRING |
| **custom19**  STRING |
| **custom2**  STRING |
| **custom20**  STRING |
| **custom21**  STRING |
| **custom22**  STRING |
| **custom23**  STRING |
| **custom24**  STRING |
| **custom25**  STRING |
| **custom26**  STRING |
| **custom27**  STRING |
| **custom28**  STRING |
| **custom29**  STRING |
| **custom3**  STRING |
| **custom30**  STRING |
| **custom31**  STRING |
| **custom32**  STRING |
| **custom33**  STRING |
| **custom34**  STRING |
| **custom35**  STRING |
| **custom36**  STRING |
| **custom37**  STRING |
| **custom38**  STRING |
| **custom39**  STRING |
| **custom4**  STRING |
| **custom40**  STRING |
| **custom41**  STRING |
| **custom42**  STRING |
| **custom43**  STRING |
| **custom44**  STRING |
| **custom45**  STRING |
| **custom46**  STRING |
| **custom47**  STRING |
| **custom48**  STRING |
| **custom49**  STRING |
| **custom5**  STRING |
| **custom50**  STRING |
| **custom51**  STRING |
| **custom52**  STRING |
| **custom53**  STRING |
| **custom54**  STRING |
| **custom55**  STRING |
| **custom56**  STRING |
| **custom57**  STRING |
| **custom58**  STRING |
| **custom59**  STRING |
| **custom6**  STRING |
| **custom60**  STRING |
| **custom61**  STRING |
| **custom62**  STRING |
| **custom63**  STRING |
| **custom64**  STRING |
| **custom65**  STRING |
| **custom66**  STRING |
| **custom67**  STRING |
| **custom68**  STRING |
| **custom69**  STRING |
| **custom7**  STRING |
| **custom70**  STRING |
| **custom71**  STRING |
| **custom72**  STRING |
| **custom73**  STRING |
| **custom74**  STRING |
| **custom75**  STRING |
| **custom76**  STRING |
| **custom77**  STRING |
| **custom78**  STRING |
| **custom79**  STRING |
| **custom8**  STRING |
| **custom80**  STRING |
| **custom81**  STRING |
| **custom82**  STRING |
| **custom83**  STRING |
| **custom84**  STRING |
| **custom85**  STRING |
| **custom86**  STRING |
| **custom87**  STRING |
| **custom88**  STRING |
| **custom89**  STRING |
| **custom9**  STRING |
| **custom90**  STRING |
| **custom91**  STRING |
| **custom92**  STRING |
| **custom93**  STRING |
| **custom94**  STRING |
| **custom95**  STRING |
| **custom96**  STRING |
| **custom97**  STRING |
| **custom98**  STRING |
| **custom99**  STRING |
| **customId**  STRING |
| **description**  STRING |
| **domain**  STRING |
| **externalSource**  STRING |
| **followers**  INTEGER |
| **foundedAt**  DATE-TIME |
| **id**  INTEGER |
| **industry**  STRING |
| **linkedInEmployees**  INTEGER |
| **linkedInUrl**  STRING |
| **locality**  STRING |
| **name**  STRING |
| **named**  BOOLEAN |
| **naturalName**  STRING |
| **numberOfEmployees**  INTEGER |
| **ownerId**  INTEGER |
| **sharingTeamId**  STRING |
| **tags**  ARRAY This is a nested data structure. |
| **touchedAt**  DATE-TIME |
| **updatedAt**  DATE-TIME |
| **updaterId**  INTEGER |
| **websiteUrl**  STRING |

### call\_dispositions

The `call_dispositions` table contains information about call dispositions from your call log in Outreach.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [Outreach API method](https://api.outreach.io/api/v2/docs#callDisposition "Opens in new tab: Outreach API method") |

call\_dispositions table foreign keys

| Join call\_dispositions with | on |
| --- | --- |
| [calls](#calls) | ``` call_dispositions.id = calls.callDispositionId ```  ``` call_dispositions.creatorId = calls.userId ``` |
| [accounts](#accounts) | ``` call_dispositions.creatorId = accounts.creatorId ```  ``` call_dispositions.creatorId = accounts.ownerId ```  ``` call_dispositions.creatorId = accounts.updaterId ``` |
| [call\_purposes](#call-purposes) | ``` call_dispositions.creatorId = call_purposes.creatorId ``` |
| [content\_categories](#content-categories) | ``` call_dispositions.creatorId = content_categories.creatorId ``` |
| [mailboxes](#mailboxes) | ``` call_dispositions.creatorId = mailboxes.creatorId ```  ``` call_dispositions.creatorId = mailboxes.updaterId ```  ``` call_dispositions.creatorId = mailboxes.userId ``` |
| [opportunities](#opportunities) | ``` call_dispositions.creatorId = opportunities.creatorId ```  ``` call_dispositions.creatorId = opportunities.ownerId ``` |
| [prospects](#prospects) | ``` call_dispositions.creatorId = prospects.creatorId ```  ``` call_dispositions.creatorId = prospects.updaterId ``` |
| [sequence\_states](#sequence-states) | ``` call_dispositions.creatorId = sequence_states.creatorId ``` |
| [sequence\_steps](#sequence-steps) | ``` call_dispositions.creatorId = sequence_steps.creatorId ```  ``` call_dispositions.creatorId = sequence_steps.updaterId ``` |
| [sequence\_templates](#sequence-templates) | ``` call_dispositions.creatorId = sequence_templates.creatorId ```  ``` call_dispositions.creatorId = sequence_templates.updaterId ``` |
| [sequences](#sequences) | ``` call_dispositions.creatorId = sequences.creatorId ```  ``` call_dispositions.creatorId = sequences.ownerId ```  ``` call_dispositions.creatorId = sequences.updaterId ``` |
| [stages](#stages) | ``` call_dispositions.creatorId = stages.creatorId ```  ``` call_dispositions.creatorId = stages.updaterId ``` |
| [tasks](#tasks) | ``` call_dispositions.creatorId = tasks.creatorId ```  ``` call_dispositions.creatorId = tasks.completerId ``` |
| [users](#users) | ``` call_dispositions.creatorId = users.creatorId ```  ``` call_dispositions.creatorId = users.id ```  ``` call_dispositions.creatorId = users.updaterId ``` |

call\_dispositions table schema

|  |
| --- |
| **createdAt**  DATE-TIME |
| **creatorId**  INTEGER |
| **id**  INTEGER |
| **name**  STRING |
| **order**  INTEGER |
| **outcome**  STRING |
| **updatedAt**  DATE-TIME |

### call\_purposes

The `call_purposes` table contains information about the purpose of calls in your Outreach call logs.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [Outreach API method](https://api.outreach.io/api/v2/docs#callPurpose "Opens in new tab: Outreach API method") |

call\_purposes table foreign keys

| Join call\_purposes with | on |
| --- | --- |
| [calls](#calls) | ``` call_purposes.id = calls.callPurposeId ```  ``` call_purposes.creatorId = calls.userId ``` |
| [accounts](#accounts) | ``` call_purposes.creatorId = accounts.creatorId ```  ``` call_purposes.creatorId = accounts.ownerId ```  ``` call_purposes.creatorId = accounts.updaterId ``` |
| [call\_dispositions](#call-dispositions) | ``` call_purposes.creatorId = call_dispositions.creatorId ``` |
| [content\_categories](#content-categories) | ``` call_purposes.creatorId = content_categories.creatorId ``` |
| [mailboxes](#mailboxes) | ``` call_purposes.creatorId = mailboxes.creatorId ```  ``` call_purposes.creatorId = mailboxes.updaterId ```  ``` call_purposes.creatorId = mailboxes.userId ``` |
| [opportunities](#opportunities) | ``` call_purposes.creatorId = opportunities.creatorId ```  ``` call_purposes.creatorId = opportunities.ownerId ``` |
| [prospects](#prospects) | ``` call_purposes.creatorId = prospects.creatorId ```  ``` call_purposes.creatorId = prospects.updaterId ``` |
| [sequence\_states](#sequence-states) | ``` call_purposes.creatorId = sequence_states.creatorId ``` |
| [sequence\_steps](#sequence-steps) | ``` call_purposes.creatorId = sequence_steps.creatorId ```  ``` call_purposes.creatorId = sequence_steps.updaterId ``` |
| [sequence\_templates](#sequence-templates) | ``` call_purposes.creatorId = sequence_templates.creatorId ```  ``` call_purposes.creatorId = sequence_templates.updaterId ``` |
| [sequences](#sequences) | ``` call_purposes.creatorId = sequences.creatorId ```  ``` call_purposes.creatorId = sequences.ownerId ```  ``` call_purposes.creatorId = sequences.updaterId ``` |
| [stages](#stages) | ``` call_purposes.creatorId = stages.creatorId ```  ``` call_purposes.creatorId = stages.updaterId ``` |
| [tasks](#tasks) | ``` call_purposes.creatorId = tasks.creatorId ```  ``` call_purposes.creatorId = tasks.completerId ``` |
| [users](#users) | ``` call_purposes.creatorId = users.creatorId ```  ``` call_purposes.creatorId = users.id ```  ``` call_purposes.creatorId = users.updaterId ``` |

call\_purposes table schema

|  |
| --- |
| **createdAt**  DATE-TIME |
| **creatorId**  INTEGER |
| **id**  INTEGER |
| **name**  STRING |
| **order**  INTEGER |
| **updatedAt**  DATE-TIME |

### calls

The `calls` table contains information about inbound and outbound calls in your Outreach call logs.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [Outreach API method](https://api.outreach.io/api/v2/docs#call "Opens in new tab: Outreach API method") |

calls table foreign keys

| Join calls with | on |
| --- | --- |
| [call\_dispositions](#call-dispositions) | ``` calls.callDispositionId = call_dispositions.id ```  ``` calls.userId = call_dispositions.creatorId ``` |
| [call\_purposes](#call-purposes) | ``` calls.callPurposeId = call_purposes.id ```  ``` calls.userId = call_purposes.creatorId ``` |
| [tasks](#tasks) | ``` calls.id = tasks.callId ```  ``` calls.opportunityId = tasks.opportunityId ```  ``` calls.prospectId = tasks.prospectId ```  ``` calls.sequenceId = tasks.sequenceId ```  ``` calls.sequenceStateId = tasks.sequenceStateId ```  ``` calls.sequenceStepId = tasks.sequenceStepId ```  ``` calls.id = tasks.id ```  ``` calls.userId = tasks.creatorId ```  ``` calls.userId = tasks.completerId ``` |
| [mailings](#mailings) | ``` calls.opportunityId = mailings.opportunityId ```  ``` calls.prospectId = mailings.prospectId ```  ``` calls.sequenceId = mailings.sequenceId ```  ``` calls.sequenceStateId = mailings.sequenceStateId ```  ``` calls.sequenceStepId = mailings.sequenceStepId ```  ``` calls.id = mailings.id ``` |
| [opportunities](#opportunities) | ``` calls.opportunityId = opportunities.id ```  ``` calls.userId = opportunities.creatorId ```  ``` calls.userId = opportunities.ownerId ``` |
| [events](#events) | ``` calls.prospectId = events.prospectId ``` |
| [prospects](#prospects) | ``` calls.prospectId = prospects.id ```  ``` calls.userId = prospects.creatorId ```  ``` calls.userId = prospects.updaterId ``` |
| [sequence\_states](#sequence-states) | ``` calls.prospectId = sequence_states.prospectId ```  ``` calls.sequenceId = sequence_states.sequenceId ```  ``` calls.sequenceStateId = sequence_states.id ```  ``` calls.userId = sequence_states.creatorId ``` |
| [sequence\_steps](#sequence-steps) | ``` calls.sequenceId = sequence_steps.sequenceId ```  ``` calls.sequenceStepId = sequence_steps.id ```  ``` calls.userId = sequence_steps.creatorId ```  ``` calls.userId = sequence_steps.updaterId ``` |
| [accounts](#accounts) | ``` calls.userId = accounts.creatorId ```  ``` calls.userId = accounts.ownerId ```  ``` calls.userId = accounts.updaterId ``` |
| [content\_categories](#content-categories) | ``` calls.userId = content_categories.creatorId ``` |
| [mailboxes](#mailboxes) | ``` calls.userId = mailboxes.creatorId ```  ``` calls.userId = mailboxes.updaterId ```  ``` calls.userId = mailboxes.userId ``` |
| [sequence\_templates](#sequence-templates) | ``` calls.userId = sequence_templates.creatorId ```  ``` calls.userId = sequence_templates.updaterId ``` |
| [sequences](#sequences) | ``` calls.userId = sequences.creatorId ```  ``` calls.userId = sequences.ownerId ```  ``` calls.userId = sequences.updaterId ``` |
| [stages](#stages) | ``` calls.userId = stages.creatorId ```  ``` calls.userId = stages.updaterId ``` |
| [users](#users) | ``` calls.userId = users.creatorId ```  ``` calls.userId = users.id ```  ``` calls.userId = users.updaterId ``` |

calls table schema

|  |
| --- |
| **answeredAt**  DATE-TIME |
| **callDispositionId**  INTEGER |
| **callPurposeId**  INTEGER |
| **completedAt**  DATE-TIME |
| **createdAt**  DATE-TIME |
| **dialedAt**  DATE-TIME |
| **direction**  STRING |
| **externalVendor**  STRING |
| **from**  STRING |
| **id**  INTEGER |
| **note**  STRING |
| **opportunityId**  INTEGER |
| **outcome**  STRING |
| **phoneNumberId**  INTEGER |
| **prospectId**  INTEGER |
| **recordingUrl**  STRING |
| **returnedAt**  DATE-TIME |
| **sequenceAction**  STRING |
| **sequenceId**  INTEGER |
| **sequenceStateId**  INTEGER |
| **sequenceStepId**  INTEGER |
| **shouldRecordCall**  BOOLEAN |
| **state**  STRING |
| **stateChangedAt**  DATE-TIME |
| **tags**  ARRAY This is a nested data structure. |
| **taskId**  INTEGER |
| **to**  STRING |
| **uid**  STRING |
| **updatedAt**  DATE-TIME |
| **userCallType**  STRING |
| **userId**  INTEGER |
| **vendorCallId**  STRING |
| **voicemailRecordingUrl**  STRING |

### content\_categories

The `content_categories` table contains information about your content categories in Outreach.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [Outreach API method](https://api.outreach.io/api/v2/docs#contentCategory "Opens in new tab: Outreach API method") |

content\_categories table foreign keys

| Join content\_categories with | on |
| --- | --- |
| [accounts](#accounts) | ``` content_categories.creatorId = accounts.creatorId ```  ``` content_categories.creatorId = accounts.ownerId ```  ``` content_categories.creatorId = accounts.updaterId ``` |
| [call\_dispositions](#call-dispositions) | ``` content_categories.creatorId = call_dispositions.creatorId ``` |
| [call\_purposes](#call-purposes) | ``` content_categories.creatorId = call_purposes.creatorId ``` |
| [calls](#calls) | ``` content_categories.creatorId = calls.userId ``` |
| [mailboxes](#mailboxes) | ``` content_categories.creatorId = mailboxes.creatorId ```  ``` content_categories.creatorId = mailboxes.updaterId ```  ``` content_categories.creatorId = mailboxes.userId ``` |
| [opportunities](#opportunities) | ``` content_categories.creatorId = opportunities.creatorId ```  ``` content_categories.creatorId = opportunities.ownerId ``` |
| [prospects](#prospects) | ``` content_categories.creatorId = prospects.creatorId ```  ``` content_categories.creatorId = prospects.updaterId ``` |
| [sequence\_states](#sequence-states) | ``` content_categories.creatorId = sequence_states.creatorId ``` |
| [sequence\_steps](#sequence-steps) | ``` content_categories.creatorId = sequence_steps.creatorId ```  ``` content_categories.creatorId = sequence_steps.updaterId ``` |
| [sequence\_templates](#sequence-templates) | ``` content_categories.creatorId = sequence_templates.creatorId ```  ``` content_categories.creatorId = sequence_templates.updaterId ``` |
| [sequences](#sequences) | ``` content_categories.creatorId = sequences.creatorId ```  ``` content_categories.creatorId = sequences.ownerId ```  ``` content_categories.creatorId = sequences.updaterId ``` |
| [stages](#stages) | ``` content_categories.creatorId = stages.creatorId ```  ``` content_categories.creatorId = stages.updaterId ``` |
| [tasks](#tasks) | ``` content_categories.creatorId = tasks.creatorId ```  ``` content_categories.creatorId = tasks.completerId ``` |
| [users](#users) | ``` content_categories.creatorId = users.creatorId ```  ``` content_categories.creatorId = users.id ```  ``` content_categories.creatorId = users.updaterId ``` |

content\_categories table schema

|  |
| --- |
| **allowSequences**  BOOLEAN |
| **allowSnippets**  BOOLEAN |
| **allowTemplates**  BOOLEAN |
| **color**  STRING |
| **createdAt**  DATE-TIME |
| **creatorId**  INTEGER |
| **id**  INTEGER |
| **name**  STRING |
| **updatedAt**  DATE-TIME |

### duties

The `duties` table contains Outreach-suggested job roles for users.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Outreach API method](https://api.outreach.io/api/v2/docs#duty "Opens in new tab: Outreach API method") |

duties table foreign keys

| Join duties with | on |
| --- | --- |
| [users](#users) | ``` duties.id = users.duties.id ``` |

duties table schema

|  |
| --- |
| **dutyType**  STRING |
| **id**  INTEGER |
| **symbolicName**  STRING |

### events

The `events` table contains information about application events in your Outreach account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | eventAt |
| **Useful links** | [Outreach API method](https://api.outreach.io/api/v2/docs#event "Opens in new tab: Outreach API method") |

events table foreign keys

| Join events with | on |
| --- | --- |
| [mailings](#mailings) | ``` events.mailingId = mailings.id ```  ``` events.prospectId = mailings.prospectId ``` |
| [tasks](#tasks) | ``` events.mailingId = tasks.mailingId ```  ``` events.prospectId = tasks.prospectId ``` |
| [calls](#calls) | ``` events.prospectId = calls.prospectId ``` |
| [prospects](#prospects) | ``` events.prospectId = prospects.id ``` |
| [sequence\_states](#sequence-states) | ``` events.prospectId = sequence_states.prospectId ``` |

events table schema

|  |
| --- |
| **accountId**  INTEGER |
| **body**  STRING |
| **callId**  INTEGER |
| **createdAt**  DATE-TIME |
| **eventAt**  DATE-TIME |
| **externalUrl**  STRING |
| **id**  INTEGER |
| **mailingId**  INTEGER |
| **name**  STRING |
| **opportunityId**  INTEGER |
| **payload**  OBJECT This is a nested data structure. |
| **prospectId**  INTEGER |
| **requestCity**  STRING |
| **requestDevice**  STRING |
| **requestHost**  STRING |
| **requestProxied**  BOOLEAN |
| **requestRegion**  BOOLEAN |
| **taskId**  INTEGER |
| **userId**  INTEGER |

### mailboxes

The `mailboxes` table contains information about your Outreach email mailbox.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [Outreach API method](https://api.outreach.io/api/v2/docs#mailbox "Opens in new tab: Outreach API method") |

mailboxes table foreign keys

| Join mailboxes with | on |
| --- | --- |
| [mailings](#mailings) | ``` mailboxes.id = mailings.mailboxId ``` |
| [users](#users) | ``` mailboxes.id = users.mailboxId ```  ``` mailboxes.creatorId = users.creatorId ```  ``` mailboxes.updaterId = users.creatorId ```  ``` mailboxes.userId = users.creatorId ```  ``` mailboxes.creatorId = users.id ```  ``` mailboxes.updaterId = users.id ```  ``` mailboxes.userId = users.id ```  ``` mailboxes.creatorId = users.updaterId ```  ``` mailboxes.updaterId = users.updaterId ```  ``` mailboxes.userId = users.updaterId ``` |
| [accounts](#accounts) | ``` mailboxes.creatorId = accounts.creatorId ```  ``` mailboxes.updaterId = accounts.creatorId ```  ``` mailboxes.userId = accounts.creatorId ```  ``` mailboxes.creatorId = accounts.ownerId ```  ``` mailboxes.updaterId = accounts.ownerId ```  ``` mailboxes.userId = accounts.ownerId ```  ``` mailboxes.creatorId = accounts.updaterId ```  ``` mailboxes.updaterId = accounts.updaterId ```  ``` mailboxes.userId = accounts.updaterId ``` |
| [call\_dispositions](#call-dispositions) | ``` mailboxes.creatorId = call_dispositions.creatorId ```  ``` mailboxes.updaterId = call_dispositions.creatorId ```  ``` mailboxes.userId = call_dispositions.creatorId ``` |
| [call\_purposes](#call-purposes) | ``` mailboxes.creatorId = call_purposes.creatorId ```  ``` mailboxes.updaterId = call_purposes.creatorId ```  ``` mailboxes.userId = call_purposes.creatorId ``` |
| [calls](#calls) | ``` mailboxes.creatorId = calls.userId ```  ``` mailboxes.updaterId = calls.userId ```  ``` mailboxes.userId = calls.userId ``` |
| [content\_categories](#content-categories) | ``` mailboxes.creatorId = content_categories.creatorId ```  ``` mailboxes.updaterId = content_categories.creatorId ```  ``` mailboxes.userId = content_categories.creatorId ``` |
| [opportunities](#opportunities) | ``` mailboxes.creatorId = opportunities.creatorId ```  ``` mailboxes.updaterId = opportunities.creatorId ```  ``` mailboxes.userId = opportunities.creatorId ```  ``` mailboxes.creatorId = opportunities.ownerId ```  ``` mailboxes.updaterId = opportunities.ownerId ```  ``` mailboxes.userId = opportunities.ownerId ``` |
| [prospects](#prospects) | ``` mailboxes.creatorId = prospects.creatorId ```  ``` mailboxes.updaterId = prospects.creatorId ```  ``` mailboxes.userId = prospects.creatorId ```  ``` mailboxes.creatorId = prospects.updaterId ```  ``` mailboxes.updaterId = prospects.updaterId ```  ``` mailboxes.userId = prospects.updaterId ``` |
| [sequence\_states](#sequence-states) | ``` mailboxes.creatorId = sequence_states.creatorId ```  ``` mailboxes.updaterId = sequence_states.creatorId ```  ``` mailboxes.userId = sequence_states.creatorId ``` |
| [sequence\_steps](#sequence-steps) | ``` mailboxes.creatorId = sequence_steps.creatorId ```  ``` mailboxes.updaterId = sequence_steps.creatorId ```  ``` mailboxes.userId = sequence_steps.creatorId ```  ``` mailboxes.creatorId = sequence_steps.updaterId ```  ``` mailboxes.updaterId = sequence_steps.updaterId ```  ``` mailboxes.userId = sequence_steps.updaterId ``` |
| [sequence\_templates](#sequence-templates) | ``` mailboxes.creatorId = sequence_templates.creatorId ```  ``` mailboxes.updaterId = sequence_templates.creatorId ```  ``` mailboxes.userId = sequence_templates.creatorId ```  ``` mailboxes.creatorId = sequence_templates.updaterId ```  ``` mailboxes.updaterId = sequence_templates.updaterId ```  ``` mailboxes.userId = sequence_templates.updaterId ``` |
| [sequences](#sequences) | ``` mailboxes.creatorId = sequences.creatorId ```  ``` mailboxes.updaterId = sequences.creatorId ```  ``` mailboxes.userId = sequences.creatorId ```  ``` mailboxes.creatorId = sequences.ownerId ```  ``` mailboxes.updaterId = sequences.ownerId ```  ``` mailboxes.userId = sequences.ownerId ```  ``` mailboxes.creatorId = sequences.updaterId ```  ``` mailboxes.updaterId = sequences.updaterId ```  ``` mailboxes.userId = sequences.updaterId ``` |
| [stages](#stages) | ``` mailboxes.creatorId = stages.creatorId ```  ``` mailboxes.updaterId = stages.creatorId ```  ``` mailboxes.userId = stages.creatorId ```  ``` mailboxes.creatorId = stages.updaterId ```  ``` mailboxes.updaterId = stages.updaterId ```  ``` mailboxes.userId = stages.updaterId ``` |
| [tasks](#tasks) | ``` mailboxes.creatorId = tasks.creatorId ```  ``` mailboxes.updaterId = tasks.creatorId ```  ``` mailboxes.userId = tasks.creatorId ```  ``` mailboxes.creatorId = tasks.completerId ```  ``` mailboxes.updaterId = tasks.completerId ```  ``` mailboxes.userId = tasks.completerId ``` |

mailboxes table schema

|  |
| --- |
| **authId**  INTEGER |
| **createdAt**  DATE-TIME |
| **creatorId**  INTEGER |
| **editable**  BOOLEAN |
| **email**  STRING |
| **emailHash**  STRING |
| **emailProvider**  STRING |
| **emailSignature**  STRING |
| **ewsEndpoint**  STRING |
| **ewsSslVerifyMode**  INTEGER |
| **exchangeVersion**  STRING |
| **id**  INTEGER |
| **imapHost**  STRING |
| **imapPort**  INTEGER |
| **imapSsl**  BOOLEAN |
| **maxEmailsPerDay**  INTEGER |
| **maxMailingsPerDay**  INTEGER |
| **maxMailingsPerWeek**  INTEGER |
| **optOutMessage**  STRING |
| **optOutSignature**  STRING |
| **prospectEmailExclusions**  STRING |
| **providerId**  INTEGER |
| **providerType**  STRING |
| **sendDisabled**  BOOLEAN |
| **sendErroredAt**  DATE-TIME |
| **sendMaxRetries**  INTEGER |
| **sendMethod**  STRING |
| **sendPeriod**  INTEGER |
| **sendRequiresSync**  BOOLEAN |
| **sendSuccessAt**  DATE-TIME |
| **sendThreshold**  INTEGER |
| **sendgridWebhookUrl**  STRING |
| **smtpHost**  STRING |
| **smtpPort**  INTEGER |
| **smtpSsl**  BOOLEAN |
| **smtpUsername**  STRING |
| **syncActiveFrequency**  INTEGER |
| **syncDisabled**  BOOLEAN |
| **syncErroredAt**  DATE-TIME |
| **syncFinishedAt**  DATE-TIME |
| **syncMethod**  STRING |
| **syncOutreachFolder**  BOOLEAN |
| **syncPassiveFrequency**  INTEGER |
| **syncSuccessAt**  DATE-TIME |
| **updatedAt**  DATE-TIME |
| **updaterId**  INTEGER |
| **userId**  INTEGER |
| **username**  STRING |

### mailings

The `mailings` table is a representation of a platform-related email.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [Outreach API method](https://api.outreach.io/api/v2/docs#mailing "Opens in new tab: Outreach API method") |

mailings table foreign keys

| Join mailings with | on |
| --- | --- |
| [mailboxes](#mailboxes) | ``` mailings.mailboxId = mailboxes.id ``` |
| [users](#users) | ``` mailings.mailboxId = users.mailboxId ``` |
| [events](#events) | ``` mailings.id = events.mailingId ```  ``` mailings.prospectId = events.prospectId ``` |
| [tasks](#tasks) | ``` mailings.id = tasks.mailingId ```  ``` mailings.opportunityId = tasks.opportunityId ```  ``` mailings.prospectId = tasks.prospectId ```  ``` mailings.sequenceId = tasks.sequenceId ```  ``` mailings.sequenceStateId = tasks.sequenceStateId ```  ``` mailings.sequenceStepId = tasks.sequenceStepId ```  ``` mailings.id = tasks.id ``` |
| [calls](#calls) | ``` mailings.opportunityId = calls.opportunityId ```  ``` mailings.prospectId = calls.prospectId ```  ``` mailings.sequenceId = calls.sequenceId ```  ``` mailings.sequenceStateId = calls.sequenceStateId ```  ``` mailings.sequenceStepId = calls.sequenceStepId ```  ``` mailings.id = calls.id ``` |
| [opportunities](#opportunities) | ``` mailings.opportunityId = opportunities.id ``` |
| [prospects](#prospects) | ``` mailings.prospectId = prospects.id ``` |
| [sequence\_states](#sequence-states) | ``` mailings.prospectId = sequence_states.prospectId ```  ``` mailings.sequenceId = sequence_states.sequenceId ```  ``` mailings.sequenceStateId = sequence_states.id ``` |
| [sequence\_steps](#sequence-steps) | ``` mailings.sequenceId = sequence_steps.sequenceId ```  ``` mailings.sequenceStepId = sequence_steps.id ``` |

mailings table schema

|  |
| --- |
| **bodyHtml**  STRING |
| **bodyText**  STRING |
| **bouncedAt**  DATE-TIME |
| **clickCount**  INTEGER |
| **clickedAt**  DATE-TIME |
| **createdAt**  DATE-TIME |
| **deliveredAt**  DATE-TIME |
| **errorBacktrace**  STRING |
| **errorReason**  STRING |
| **followUpSequenceId**  INTEGER |
| **followUpTaskScheduledAt**  DATE-TIME |
| **followUpTaskType**  STRING |
| **id**  INTEGER |
| **mailboxAddress**  STRING |
| **mailboxId**  INTEGER |
| **mailingType**  STRING |
| **markedAsSpamAt**  DATE-TIME |
| **messageId**  STRING |
| **notifyThreadCondition**  STRING |
| **notifyThreadScheduledAt**  DATE-TIME |
| **notifyThreadStatus**  STRING |
| **openCount**  INTEGER |
| **openedAt**  DATE-TIME |
| **opportunityId**  INTEGER |
| **overrideSafetySettings**  BOOLEAN |
| **prospectId**  INTEGER |
| **references**  ARRAY This is a nested data structure. |
| **repliedAt**  DATE-TIME |
| **retryAt**  DATE-TIME |
| **retryCount**  INTEGER |
| **retryInterval**  INTEGER |
| **scheduledAt**  DATE-TIME |
| **sequenceId**  INTEGER |
| **sequenceStateId**  INTEGER |
| **sequenceStepId**  INTEGER |
| **state**  STRING |
| **stateChangedAt**  DATE-TIME |
| **subject**  STRING |
| **taskId**  INTEGER |
| **templateId**  INTEGER |
| **trackLinks**  BOOLEAN |
| **trackOpens**  BOOLEAN |
| **unsubscribedAt**  DATE-TIME |
| **updatedAt**  DATE-TIME |
| **userId**  INTEGER |

### opportunities

The `opportunities` table contains information about your pending deals and sales in Outreach.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [Outreach API method](https://api.outreach.io/api/v2/docs#opportunity "Opens in new tab: Outreach API method") |

opportunities table foreign keys

| Join opportunities with | on |
| --- | --- |
| [accounts](#accounts) | ``` opportunities.id = accounts.id ```  ``` opportunities.creatorId = accounts.creatorId ```  ``` opportunities.ownerId = accounts.creatorId ```  ``` opportunities.creatorId = accounts.ownerId ```  ``` opportunities.ownerId = accounts.ownerId ```  ``` opportunities.creatorId = accounts.updaterId ```  ``` opportunities.ownerId = accounts.updaterId ``` |
| [prospects](#prospects) | ``` opportunities.id = prospects.id ```  ``` opportunities.opportunityStageId = prospects.stageId ```  ``` opportunities.creatorId = prospects.creatorId ```  ``` opportunities.ownerId = prospects.creatorId ```  ``` opportunities.creatorId = prospects.updaterId ```  ``` opportunities.ownerId = prospects.updaterId ``` |
| [sequence\_states](#sequence-states) | ``` opportunities.id = sequence_states.id ```  ``` opportunities.creatorId = sequence_states.creatorId ```  ``` opportunities.ownerId = sequence_states.creatorId ``` |
| [tasks](#tasks) | ``` opportunities.id = tasks.id ```  ``` opportunities.id = tasks.opportunityId ```  ``` opportunities.creatorId = tasks.creatorId ```  ``` opportunities.ownerId = tasks.creatorId ```  ``` opportunities.creatorId = tasks.completerId ```  ``` opportunities.ownerId = tasks.completerId ``` |
| [calls](#calls) | ``` opportunities.id = calls.opportunityId ```  ``` opportunities.creatorId = calls.userId ```  ``` opportunities.ownerId = calls.userId ``` |
| [mailings](#mailings) | ``` opportunities.id = mailings.opportunityId ``` |
| [stages](#stages) | ``` opportunities.opportunityStageId = stages.id ```  ``` opportunities.creatorId = stages.creatorId ```  ``` opportunities.ownerId = stages.creatorId ```  ``` opportunities.creatorId = stages.updaterId ```  ``` opportunities.ownerId = stages.updaterId ``` |
| [call\_dispositions](#call-dispositions) | ``` opportunities.creatorId = call_dispositions.creatorId ```  ``` opportunities.ownerId = call_dispositions.creatorId ``` |
| [call\_purposes](#call-purposes) | ``` opportunities.creatorId = call_purposes.creatorId ```  ``` opportunities.ownerId = call_purposes.creatorId ``` |
| [content\_categories](#content-categories) | ``` opportunities.creatorId = content_categories.creatorId ```  ``` opportunities.ownerId = content_categories.creatorId ``` |
| [mailboxes](#mailboxes) | ``` opportunities.creatorId = mailboxes.creatorId ```  ``` opportunities.ownerId = mailboxes.creatorId ```  ``` opportunities.creatorId = mailboxes.updaterId ```  ``` opportunities.ownerId = mailboxes.updaterId ```  ``` opportunities.creatorId = mailboxes.userId ```  ``` opportunities.ownerId = mailboxes.userId ``` |
| [sequence\_steps](#sequence-steps) | ``` opportunities.creatorId = sequence_steps.creatorId ```  ``` opportunities.ownerId = sequence_steps.creatorId ```  ``` opportunities.creatorId = sequence_steps.updaterId ```  ``` opportunities.ownerId = sequence_steps.updaterId ``` |
| [sequence\_templates](#sequence-templates) | ``` opportunities.creatorId = sequence_templates.creatorId ```  ``` opportunities.ownerId = sequence_templates.creatorId ```  ``` opportunities.creatorId = sequence_templates.updaterId ```  ``` opportunities.ownerId = sequence_templates.updaterId ``` |
| [sequences](#sequences) | ``` opportunities.creatorId = sequences.creatorId ```  ``` opportunities.ownerId = sequences.creatorId ```  ``` opportunities.creatorId = sequences.ownerId ```  ``` opportunities.ownerId = sequences.ownerId ```  ``` opportunities.creatorId = sequences.updaterId ```  ``` opportunities.ownerId = sequences.updaterId ``` |
| [users](#users) | ``` opportunities.creatorId = users.creatorId ```  ``` opportunities.ownerId = users.creatorId ```  ``` opportunities.creatorId = users.id ```  ``` opportunities.ownerId = users.id ```  ``` opportunities.creatorId = users.updaterId ```  ``` opportunities.ownerId = users.updaterId ``` |

opportunities table schema

|  |
| --- |
| **accountId**  INTEGER |
| **amount**  INTEGER |
| **closeDate**  DATE-TIME |
| **createdAt**  DATE-TIME |
| **creatorId**  INTEGER |
| **currencyType**  STRING |
| **custom1**  STRING |
| **custom10**  STRING |
| **custom100**  STRING |
| **custom101**  STRING |
| **custom102**  STRING |
| **custom103**  STRING |
| **custom104**  STRING |
| **custom105**  STRING |
| **custom106**  STRING |
| **custom107**  STRING |
| **custom108**  STRING |
| **custom109**  STRING |
| **custom11**  STRING |
| **custom110**  STRING |
| **custom111**  STRING |
| **custom112**  STRING |
| **custom113**  STRING |
| **custom114**  STRING |
| **custom115**  STRING |
| **custom116**  STRING |
| **custom117**  STRING |
| **custom118**  STRING |
| **custom119**  STRING |
| **custom12**  STRING |
| **custom120**  STRING |
| **custom121**  STRING |
| **custom122**  STRING |
| **custom123**  STRING |
| **custom124**  STRING |
| **custom125**  STRING |
| **custom126**  STRING |
| **custom127**  STRING |
| **custom128**  STRING |
| **custom129**  STRING |
| **custom13**  STRING |
| **custom130**  STRING |
| **custom131**  STRING |
| **custom132**  STRING |
| **custom133**  STRING |
| **custom134**  STRING |
| **custom135**  STRING |
| **custom136**  STRING |
| **custom137**  STRING |
| **custom138**  STRING |
| **custom139**  STRING |
| **custom14**  STRING |
| **custom140**  STRING |
| **custom141**  STRING |
| **custom142**  STRING |
| **custom143**  STRING |
| **custom144**  STRING |
| **custom145**  STRING |
| **custom146**  STRING |
| **custom147**  STRING |
| **custom148**  STRING |
| **custom149**  STRING |
| **custom15**  STRING |
| **custom150**  STRING |
| **custom16**  STRING |
| **custom17**  STRING |
| **custom18**  STRING |
| **custom19**  STRING |
| **custom2**  STRING |
| **custom20**  STRING |
| **custom21**  STRING |
| **custom22**  STRING |
| **custom23**  STRING |
| **custom24**  STRING |
| **custom25**  STRING |
| **custom26**  STRING |
| **custom27**  STRING |
| **custom28**  STRING |
| **custom29**  STRING |
| **custom3**  STRING |
| **custom30**  STRING |
| **custom31**  STRING |
| **custom32**  STRING |
| **custom33**  STRING |
| **custom34**  STRING |
| **custom35**  STRING |
| **custom36**  STRING |
| **custom37**  STRING |
| **custom38**  STRING |
| **custom39**  STRING |
| **custom4**  STRING |
| **custom40**  STRING |
| **custom41**  STRING |
| **custom42**  STRING |
| **custom43**  STRING |
| **custom44**  STRING |
| **custom45**  STRING |
| **custom46**  STRING |
| **custom47**  STRING |
| **custom48**  STRING |
| **custom49**  STRING |
| **custom5**  STRING |
| **custom50**  STRING |
| **custom51**  STRING |
| **custom52**  STRING |
| **custom53**  STRING |
| **custom54**  STRING |
| **custom55**  STRING |
| **custom56**  STRING |
| **custom57**  STRING |
| **custom58**  STRING |
| **custom59**  STRING |
| **custom6**  STRING |
| **custom60**  STRING |
| **custom61**  STRING |
| **custom62**  STRING |
| **custom63**  STRING |
| **custom64**  STRING |
| **custom65**  STRING |
| **custom66**  STRING |
| **custom67**  STRING |
| **custom68**  STRING |
| **custom69**  STRING |
| **custom7**  STRING |
| **custom70**  STRING |
| **custom71**  STRING |
| **custom72**  STRING |
| **custom73**  STRING |
| **custom74**  STRING |
| **custom75**  STRING |
| **custom76**  STRING |
| **custom77**  STRING |
| **custom78**  STRING |
| **custom79**  STRING |
| **custom8**  STRING |
| **custom80**  STRING |
| **custom81**  STRING |
| **custom82**  STRING |
| **custom83**  STRING |
| **custom84**  STRING |
| **custom85**  STRING |
| **custom86**  STRING |
| **custom87**  STRING |
| **custom88**  STRING |
| **custom89**  STRING |
| **custom9**  STRING |
| **custom90**  STRING |
| **custom91**  STRING |
| **custom92**  STRING |
| **custom93**  STRING |
| **custom94**  STRING |
| **custom95**  STRING |
| **custom96**  STRING |
| **custom97**  STRING |
| **custom98**  STRING |
| **custom99**  STRING |
| **description**  STRING |
| **externalCreatedAt**  DATE-TIME |
| **id**  INTEGER |
| **mapLink**  STRING |
| **mapNextSteps**  STRING |
| **mapStatus**  STRING |
| **name**  STRING |
| **nextStep**  STRING |
| **opportunityStageId**  INTEGER |
| **opportunityType**  STRING |
| **ownerId**  INTEGER |
| **probability**  INTEGER |
| **prospectingRepId**  STRING |
| **sharingTeamId**  STRING |
| **stageId**  INTEGER |
| **tags**  ARRAY This is a nested data structure. |
| **touchedAt**  DATE-TIME |
| **updatedAt**  DATE-TIME |
| **updaterId**  INTEGER |

### personas

The `personas` table contains information about descriptions and types of people in Outreach.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [Outreach API method](https://api.outreach.io/api/v2/docs#persona "Opens in new tab: Outreach API method") |

personas table foreign keys

| Join personas with | on |
| --- | --- |
| [prospects](#prospects) | ``` personas.id = prospects.personaId ``` |

personas table schema

|  |
| --- |
| **createdAt**  DATE-TIME |
| **description**  STRING |
| **id**  INTEGER |
| **name**  STRING |
| **updatedAt**  DATE-TIME |

### prospects

The `prospects` table contains information about your prospects.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [Outreach API method](https://api.outreach.io/api/v2/docs#prospect "Opens in new tab: Outreach API method") |

prospects table foreign keys

| Join prospects with | on |
| --- | --- |
| [accounts](#accounts) | ``` prospects.id = accounts.id ```  ``` prospects.creatorId = accounts.creatorId ```  ``` prospects.updaterId = accounts.creatorId ```  ``` prospects.creatorId = accounts.ownerId ```  ``` prospects.updaterId = accounts.ownerId ```  ``` prospects.creatorId = accounts.updaterId ```  ``` prospects.updaterId = accounts.updaterId ``` |
| [opportunities](#opportunities) | ``` prospects.id = opportunities.id ```  ``` prospects.stageId = opportunities.opportunityStageId ```  ``` prospects.creatorId = opportunities.creatorId ```  ``` prospects.updaterId = opportunities.creatorId ```  ``` prospects.creatorId = opportunities.ownerId ```  ``` prospects.updaterId = opportunities.ownerId ``` |
| [sequence\_states](#sequence-states) | ``` prospects.id = sequence_states.id ```  ``` prospects.id = sequence_states.prospectId ```  ``` prospects.creatorId = sequence_states.creatorId ```  ``` prospects.updaterId = sequence_states.creatorId ``` |
| [tasks](#tasks) | ``` prospects.id = tasks.id ```  ``` prospects.id = tasks.prospectId ```  ``` prospects.creatorId = tasks.creatorId ```  ``` prospects.updaterId = tasks.creatorId ```  ``` prospects.creatorId = tasks.completerId ```  ``` prospects.updaterId = tasks.completerId ``` |
| [personas](#personas) | ``` prospects.personaId = personas.id ``` |
| [calls](#calls) | ``` prospects.id = calls.prospectId ```  ``` prospects.creatorId = calls.userId ```  ``` prospects.updaterId = calls.userId ``` |
| [events](#events) | ``` prospects.id = events.prospectId ``` |
| [mailings](#mailings) | ``` prospects.id = mailings.prospectId ``` |
| [stages](#stages) | ``` prospects.stageId = stages.id ```  ``` prospects.creatorId = stages.creatorId ```  ``` prospects.updaterId = stages.creatorId ```  ``` prospects.creatorId = stages.updaterId ```  ``` prospects.updaterId = stages.updaterId ``` |
| [call\_dispositions](#call-dispositions) | ``` prospects.creatorId = call_dispositions.creatorId ```  ``` prospects.updaterId = call_dispositions.creatorId ``` |
| [call\_purposes](#call-purposes) | ``` prospects.creatorId = call_purposes.creatorId ```  ``` prospects.updaterId = call_purposes.creatorId ``` |
| [content\_categories](#content-categories) | ``` prospects.creatorId = content_categories.creatorId ```  ``` prospects.updaterId = content_categories.creatorId ``` |
| [mailboxes](#mailboxes) | ``` prospects.creatorId = mailboxes.creatorId ```  ``` prospects.updaterId = mailboxes.creatorId ```  ``` prospects.creatorId = mailboxes.updaterId ```  ``` prospects.updaterId = mailboxes.updaterId ```  ``` prospects.creatorId = mailboxes.userId ```  ``` prospects.updaterId = mailboxes.userId ``` |
| [sequence\_steps](#sequence-steps) | ``` prospects.creatorId = sequence_steps.creatorId ```  ``` prospects.updaterId = sequence_steps.creatorId ```  ``` prospects.creatorId = sequence_steps.updaterId ```  ``` prospects.updaterId = sequence_steps.updaterId ``` |
| [sequence\_templates](#sequence-templates) | ``` prospects.creatorId = sequence_templates.creatorId ```  ``` prospects.updaterId = sequence_templates.creatorId ```  ``` prospects.creatorId = sequence_templates.updaterId ```  ``` prospects.updaterId = sequence_templates.updaterId ``` |
| [sequences](#sequences) | ``` prospects.creatorId = sequences.creatorId ```  ``` prospects.updaterId = sequences.creatorId ```  ``` prospects.creatorId = sequences.ownerId ```  ``` prospects.updaterId = sequences.ownerId ```  ``` prospects.creatorId = sequences.updaterId ```  ``` prospects.updaterId = sequences.updaterId ``` |
| [users](#users) | ``` prospects.creatorId = users.creatorId ```  ``` prospects.updaterId = users.creatorId ```  ``` prospects.creatorId = users.id ```  ``` prospects.updaterId = users.id ```  ``` prospects.creatorId = users.updaterId ```  ``` prospects.updaterId = users.updaterId ``` |

prospects table schema

|  |
| --- |
| **accountId**  INTEGER |
| **addedAt**  DATE-TIME |
| **addressCity**  STRING |
| **addressCountry**  STRING |
| **addressState**  STRING |
| **addressStreet**  STRING |
| **addressStreet2**  STRING |
| **addressZip**  STRING |
| **angelListUrl**  STRING |
| **availableAt**  DATE-TIME |
| **callOptedOut**  BOOLEAN |
| **callsOptStatus**  STRING |
| **callsOptedAt**  DATE-TIME |
| **campaignName**  STRING |
| **clickCount**  INTEGER |
| **company**  STRING |
| **contactHistogram**  ARRAY This is a nested data structure. |
| **createdAt**  DATE-TIME |
| **creatorId**  INTEGER |
| **custom1**  STRING |
| **custom10**  STRING |
| **custom100**  STRING |
| **custom101**  STRING |
| **custom102**  STRING |
| **custom103**  STRING |
| **custom104**  STRING |
| **custom105**  STRING |
| **custom106**  STRING |
| **custom107**  STRING |
| **custom108**  STRING |
| **custom109**  STRING |
| **custom11**  STRING |
| **custom110**  STRING |
| **custom111**  STRING |
| **custom112**  STRING |
| **custom113**  STRING |
| **custom114**  STRING |
| **custom115**  STRING |
| **custom116**  STRING |
| **custom117**  STRING |
| **custom118**  STRING |
| **custom119**  STRING |
| **custom12**  STRING |
| **custom120**  STRING |
| **custom121**  STRING |
| **custom122**  STRING |
| **custom123**  STRING |
| **custom124**  STRING |
| **custom125**  STRING |
| **custom126**  STRING |
| **custom127**  STRING |
| **custom128**  STRING |
| **custom129**  STRING |
| **custom13**  STRING |
| **custom130**  STRING |
| **custom131**  STRING |
| **custom132**  STRING |
| **custom133**  STRING |
| **custom134**  STRING |
| **custom135**  STRING |
| **custom136**  STRING |
| **custom137**  STRING |
| **custom138**  STRING |
| **custom139**  STRING |
| **custom14**  STRING |
| **custom140**  STRING |
| **custom141**  STRING |
| **custom142**  STRING |
| **custom143**  STRING |
| **custom144**  STRING |
| **custom145**  STRING |
| **custom146**  STRING |
| **custom147**  STRING |
| **custom148**  STRING |
| **custom149**  STRING |
| **custom15**  STRING |
| **custom150**  STRING |
| **custom16**  STRING |
| **custom17**  STRING |
| **custom18**  STRING |
| **custom19**  STRING |
| **custom2**  STRING |
| **custom20**  STRING |
| **custom21**  STRING |
| **custom22**  STRING |
| **custom23**  STRING |
| **custom24**  STRING |
| **custom25**  STRING |
| **custom26**  STRING |
| **custom27**  STRING |
| **custom28**  STRING |
| **custom29**  STRING |
| **custom3**  STRING |
| **custom30**  STRING |
| **custom31**  STRING |
| **custom32**  STRING |
| **custom33**  STRING |
| **custom34**  STRING |
| **custom35**  STRING |
| **custom36**  STRING |
| **custom37**  STRING |
| **custom38**  STRING |
| **custom39**  STRING |
| **custom4**  STRING |
| **custom40**  STRING |
| **custom41**  STRING |
| **custom42**  STRING |
| **custom43**  STRING |
| **custom44**  STRING |
| **custom45**  STRING |
| **custom46**  STRING |
| **custom47**  STRING |
| **custom48**  STRING |
| **custom49**  STRING |
| **custom5**  STRING |
| **custom50**  STRING |
| **custom51**  STRING |
| **custom52**  STRING |
| **custom53**  STRING |
| **custom54**  STRING |
| **custom55**  STRING |
| **custom56**  STRING |
| **custom57**  STRING |
| **custom58**  STRING |
| **custom59**  STRING |
| **custom6**  STRING |
| **custom60**  STRING |
| **custom61**  STRING |
| **custom62**  STRING |
| **custom63**  STRING |
| **custom64**  STRING |
| **custom65**  STRING |
| **custom66**  STRING |
| **custom67**  STRING |
| **custom68**  STRING |
| **custom69**  STRING |
| **custom7**  STRING |
| **custom70**  STRING |
| **custom71**  STRING |
| **custom72**  STRING |
| **custom73**  STRING |
| **custom74**  STRING |
| **custom75**  STRING |
| **custom76**  STRING |
| **custom77**  STRING |
| **custom78**  STRING |
| **custom79**  STRING |
| **custom8**  STRING |
| **custom80**  STRING |
| **custom81**  STRING |
| **custom82**  STRING |
| **custom83**  STRING |
| **custom84**  STRING |
| **custom85**  STRING |
| **custom86**  STRING |
| **custom87**  STRING |
| **custom88**  STRING |
| **custom89**  STRING |
| **custom9**  STRING |
| **custom90**  STRING |
| **custom91**  STRING |
| **custom92**  STRING |
| **custom93**  STRING |
| **custom94**  STRING |
| **custom95**  STRING |
| **custom96**  STRING |
| **custom97**  STRING |
| **custom98**  STRING |
| **custom99**  STRING |
| **dateOfBirth**  DATE-TIME |
| **degree**  STRING |
| **emailOptedOut**  BOOLEAN |
| **emails**  ARRAY This is a nested data structure. |
| **emailsOptStatus**  STRING |
| **emailsOptedAt**  DATE-TIME |
| **engagedAt**  DATE-TIME |
| **engagedScore**  NUMBER |
| **eventName**  STRING |
| **externalId**  STRING |
| **externalOwner**  STRING |
| **externalSource**  STRING |
| **facebookUrl**  STRING |
| **firstName**  STRING |
| **gender**  STRING |
| **githubUrl**  STRING |
| **githubUsername**  STRING |
| **googlePlusUrl**  STRING |
| **graduationDate**  DATE-TIME |
| **homePhones**  ARRAY This is a nested data structure. |
| **id**  INTEGER |
| **jobStartDate**  DATE-TIME |
| **lastName**  STRING |
| **linkedInConnections**  INTEGER |
| **linkedInId**  STRING |
| **linkedInSlug**  STRING |
| **linkedInUrl**  STRING |
| **middleName**  STRING |
| **mobilePhones**  ARRAY This is a nested data structure. |
| **name**  STRING |
| **nickname**  STRING |
| **occupation**  STRING |
| **openCount**  INTEGER |
| **optedOut**  BOOLEAN |
| **optedOutAt**  DATE-TIME |
| **otherPhones**  ARRAY This is a nested data structure. |
| **ownerId**  INTEGER |
| **personaId**  INTEGER |
| **personalNote1**  STRING |
| **personalNote2**  STRING |
| **preferredContact**  STRING |
| **quoraUrl**  STRING |
| **region**  STRING |
| **replyCount**  INTEGER |
| **school**  STRING |
| **score**  NUMBER |
| **sharingTeamId**  STRING |
| **source**  STRING |
| **specialties**  STRING |
| **stackOverflowId**  STRING |
| **stackOverflowUrl**  STRING |
| **stageId**  INTEGER |
| **tags**  ARRAY This is a nested data structure. |
| **timeZone**  STRING |
| **timeZoneIana**  STRING |
| **timeZoneInferred**  STRING |
| **title**  STRING |
| **touchedAt**  DATE-TIME |
| **trashedAt**  DATE-TIME |
| **twitterUrl**  STRING |
| **twitterUsername**  STRING |
| **updatedAt**  DATE-TIME |
| **updaterId**  INTEGER |
| **voipPhones**  ARRAY This is a nested data structure. |
| **websiteUrl1**  STRING |
| **websiteUrl2**  STRING |
| **websiteUrl3**  STRING |
| **workPhones**  ARRAY This is a nested data structure. |

### sequence\_states

The `sequence_states` table contains info about currently sequenced prospects.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [Outreach API method](https://api.outreach.io/api/v2/docs#sequenceState "Opens in new tab: Outreach API method") |

sequence\_states table foreign keys

| Join sequence\_states with | on |
| --- | --- |
| [accounts](#accounts) | ``` sequence_states.id = accounts.id ```  ``` sequence_states.creatorId = accounts.creatorId ```  ``` sequence_states.creatorId = accounts.ownerId ```  ``` sequence_states.creatorId = accounts.updaterId ``` |
| [opportunities](#opportunities) | ``` sequence_states.id = opportunities.id ```  ``` sequence_states.creatorId = opportunities.creatorId ```  ``` sequence_states.creatorId = opportunities.ownerId ``` |
| [prospects](#prospects) | ``` sequence_states.id = prospects.id ```  ``` sequence_states.prospectId = prospects.id ```  ``` sequence_states.creatorId = prospects.creatorId ```  ``` sequence_states.creatorId = prospects.updaterId ``` |
| [tasks](#tasks) | ``` sequence_states.id = tasks.id ```  ``` sequence_states.prospectId = tasks.prospectId ```  ``` sequence_states.sequenceId = tasks.sequenceId ```  ``` sequence_states.id = tasks.sequenceStateId ```  ``` sequence_states.creatorId = tasks.creatorId ```  ``` sequence_states.creatorId = tasks.completerId ``` |
| [calls](#calls) | ``` sequence_states.prospectId = calls.prospectId ```  ``` sequence_states.sequenceId = calls.sequenceId ```  ``` sequence_states.id = calls.sequenceStateId ```  ``` sequence_states.creatorId = calls.userId ``` |
| [events](#events) | ``` sequence_states.prospectId = events.prospectId ``` |
| [mailings](#mailings) | ``` sequence_states.prospectId = mailings.prospectId ```  ``` sequence_states.sequenceId = mailings.sequenceId ```  ``` sequence_states.id = mailings.sequenceStateId ``` |
| [sequence\_steps](#sequence-steps) | ``` sequence_states.sequenceId = sequence_steps.sequenceId ```  ``` sequence_states.creatorId = sequence_steps.creatorId ```  ``` sequence_states.creatorId = sequence_steps.updaterId ``` |
| [call\_dispositions](#call-dispositions) | ``` sequence_states.creatorId = call_dispositions.creatorId ``` |
| [call\_purposes](#call-purposes) | ``` sequence_states.creatorId = call_purposes.creatorId ``` |
| [content\_categories](#content-categories) | ``` sequence_states.creatorId = content_categories.creatorId ``` |
| [mailboxes](#mailboxes) | ``` sequence_states.creatorId = mailboxes.creatorId ```  ``` sequence_states.creatorId = mailboxes.updaterId ```  ``` sequence_states.creatorId = mailboxes.userId ``` |
| [sequence\_templates](#sequence-templates) | ``` sequence_states.creatorId = sequence_templates.creatorId ```  ``` sequence_states.creatorId = sequence_templates.updaterId ``` |
| [sequences](#sequences) | ``` sequence_states.creatorId = sequences.creatorId ```  ``` sequence_states.creatorId = sequences.ownerId ```  ``` sequence_states.creatorId = sequences.updaterId ``` |
| [stages](#stages) | ``` sequence_states.creatorId = stages.creatorId ```  ``` sequence_states.creatorId = stages.updaterId ``` |
| [users](#users) | ``` sequence_states.creatorId = users.creatorId ```  ``` sequence_states.creatorId = users.id ```  ``` sequence_states.creatorId = users.updaterId ``` |

sequence\_states table schema

|  |
| --- |
| **accountId**  INTEGER |
| **activeAt**  DATE-TIME |
| **bounceCount**  INTEGER |
| **callCompletedAt**  DATE-TIME |
| **clickCount**  INTEGER |
| **createdAt**  DATE-TIME |
| **creatorId**  INTEGER |
| **deliverCount**  INTEGER |
| **errorReason**  STRING |
| **failureCount**  INTEGER |
| **id**  INTEGER |
| **mailboxId**  INTEGER |
| **negativeReplyCount**  INTEGER |
| **neutralReplyCount**  INTEGER |
| **openCount**  INTEGER |
| **opportunityId**  INTEGER |
| **optOutCount**  INTEGER |
| **pauseReason**  STRING |
| **positiveReplyCount**  INTEGER |
| **prospectId**  INTEGER |
| **repliedAt**  DATE-TIME |
| **replyCount**  INTEGER |
| **scheduleCount**  INTEGER |
| **sequenceId**  INTEGER |
| **sequenceStepId**  INTEGER |
| **state**  STRING |
| **stateChangedAt**  DATE-TIME |
| **updatedAt**  DATE-TIME |

### sequence\_steps

The `sequence_steps` table contains info about individual steps within automated sequences.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [Outreach API method](https://api.outreach.io/api/v2/docs#sequenceStep "Opens in new tab: Outreach API method") |

sequence\_steps table foreign keys

| Join sequence\_steps with | on |
| --- | --- |
| [calls](#calls) | ``` sequence_steps.sequenceId = calls.sequenceId ```  ``` sequence_steps.id = calls.sequenceStepId ```  ``` sequence_steps.creatorId = calls.userId ```  ``` sequence_steps.updaterId = calls.userId ``` |
| [mailings](#mailings) | ``` sequence_steps.sequenceId = mailings.sequenceId ```  ``` sequence_steps.id = mailings.sequenceStepId ``` |
| [sequence\_states](#sequence-states) | ``` sequence_steps.sequenceId = sequence_states.sequenceId ```  ``` sequence_steps.creatorId = sequence_states.creatorId ```  ``` sequence_steps.updaterId = sequence_states.creatorId ``` |
| [tasks](#tasks) | ``` sequence_steps.sequenceId = tasks.sequenceId ```  ``` sequence_steps.id = tasks.sequenceStepId ```  ``` sequence_steps.creatorId = tasks.creatorId ```  ``` sequence_steps.updaterId = tasks.creatorId ```  ``` sequence_steps.creatorId = tasks.completerId ```  ``` sequence_steps.updaterId = tasks.completerId ``` |
| [accounts](#accounts) | ``` sequence_steps.creatorId = accounts.creatorId ```  ``` sequence_steps.updaterId = accounts.creatorId ```  ``` sequence_steps.creatorId = accounts.ownerId ```  ``` sequence_steps.updaterId = accounts.ownerId ```  ``` sequence_steps.creatorId = accounts.updaterId ```  ``` sequence_steps.updaterId = accounts.updaterId ``` |
| [call\_dispositions](#call-dispositions) | ``` sequence_steps.creatorId = call_dispositions.creatorId ```  ``` sequence_steps.updaterId = call_dispositions.creatorId ``` |
| [call\_purposes](#call-purposes) | ``` sequence_steps.creatorId = call_purposes.creatorId ```  ``` sequence_steps.updaterId = call_purposes.creatorId ``` |
| [content\_categories](#content-categories) | ``` sequence_steps.creatorId = content_categories.creatorId ```  ``` sequence_steps.updaterId = content_categories.creatorId ``` |
| [mailboxes](#mailboxes) | ``` sequence_steps.creatorId = mailboxes.creatorId ```  ``` sequence_steps.updaterId = mailboxes.creatorId ```  ``` sequence_steps.creatorId = mailboxes.updaterId ```  ``` sequence_steps.updaterId = mailboxes.updaterId ```  ``` sequence_steps.creatorId = mailboxes.userId ```  ``` sequence_steps.updaterId = mailboxes.userId ``` |
| [opportunities](#opportunities) | ``` sequence_steps.creatorId = opportunities.creatorId ```  ``` sequence_steps.updaterId = opportunities.creatorId ```  ``` sequence_steps.creatorId = opportunities.ownerId ```  ``` sequence_steps.updaterId = opportunities.ownerId ``` |
| [prospects](#prospects) | ``` sequence_steps.creatorId = prospects.creatorId ```  ``` sequence_steps.updaterId = prospects.creatorId ```  ``` sequence_steps.creatorId = prospects.updaterId ```  ``` sequence_steps.updaterId = prospects.updaterId ``` |
| [sequence\_templates](#sequence-templates) | ``` sequence_steps.creatorId = sequence_templates.creatorId ```  ``` sequence_steps.updaterId = sequence_templates.creatorId ```  ``` sequence_steps.creatorId = sequence_templates.updaterId ```  ``` sequence_steps.updaterId = sequence_templates.updaterId ``` |
| [sequences](#sequences) | ``` sequence_steps.creatorId = sequences.creatorId ```  ``` sequence_steps.updaterId = sequences.creatorId ```  ``` sequence_steps.creatorId = sequences.ownerId ```  ``` sequence_steps.updaterId = sequences.ownerId ```  ``` sequence_steps.creatorId = sequences.updaterId ```  ``` sequence_steps.updaterId = sequences.updaterId ``` |
| [stages](#stages) | ``` sequence_steps.creatorId = stages.creatorId ```  ``` sequence_steps.updaterId = stages.creatorId ```  ``` sequence_steps.creatorId = stages.updaterId ```  ``` sequence_steps.updaterId = stages.updaterId ``` |
| [users](#users) | ``` sequence_steps.creatorId = users.creatorId ```  ``` sequence_steps.updaterId = users.creatorId ```  ``` sequence_steps.creatorId = users.id ```  ``` sequence_steps.updaterId = users.id ```  ``` sequence_steps.creatorId = users.updaterId ```  ``` sequence_steps.updaterId = users.updaterId ``` |

sequence\_steps table schema

|  |
| --- |
| **bounceCount**  INTEGER |
| **callPurposeId**  INTEGER |
| **clickCount**  INTEGER |
| **createdAt**  DATE-TIME |
| **creatorId**  INTEGER |
| **date**  DATE-TIME |
| **deliverCount**  INTEGER |
| **displayName**  STRING |
| **failureCount**  INTEGER |
| **id**  INTEGER |
| **interval**  INTEGER |
| **negativeReplyCount**  INTEGER |
| **neutralReplyCount**  INTEGER |
| **openCount**  INTEGER |
| **optOutCount**  INTEGER |
| **order**  INTEGER |
| **positiveReplyCount**  INTEGER |
| **replyCount**  INTEGER |
| **scheduleCount**  INTEGER |
| **sequenceId**  INTEGER |
| **stepType**  STRING |
| **taskAutoskipDelay**  INTEGER |
| **taskNote**  STRING |
| **taskPriorityId**  INTEGER |
| **updatedAt**  DATE-TIME |
| **updaterId**  INTEGER |

### sequence\_templates

The `sequence_templates` table contains info about templates used by sequence steps.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Outreach API method](https://api.outreach.io/api/v2/docs#sequenceTemplate "Opens in new tab: Outreach API method") |

sequence\_templates table foreign keys

| Join sequence\_templates with | on |
| --- | --- |
| [accounts](#accounts) | ``` sequence_templates.creatorId = accounts.creatorId ```  ``` sequence_templates.updaterId = accounts.creatorId ```  ``` sequence_templates.creatorId = accounts.ownerId ```  ``` sequence_templates.updaterId = accounts.ownerId ```  ``` sequence_templates.creatorId = accounts.updaterId ```  ``` sequence_templates.updaterId = accounts.updaterId ``` |
| [call\_dispositions](#call-dispositions) | ``` sequence_templates.creatorId = call_dispositions.creatorId ```  ``` sequence_templates.updaterId = call_dispositions.creatorId ``` |
| [call\_purposes](#call-purposes) | ``` sequence_templates.creatorId = call_purposes.creatorId ```  ``` sequence_templates.updaterId = call_purposes.creatorId ``` |
| [calls](#calls) | ``` sequence_templates.creatorId = calls.userId ```  ``` sequence_templates.updaterId = calls.userId ``` |
| [content\_categories](#content-categories) | ``` sequence_templates.creatorId = content_categories.creatorId ```  ``` sequence_templates.updaterId = content_categories.creatorId ``` |
| [mailboxes](#mailboxes) | ``` sequence_templates.creatorId = mailboxes.creatorId ```  ``` sequence_templates.updaterId = mailboxes.creatorId ```  ``` sequence_templates.creatorId = mailboxes.updaterId ```  ``` sequence_templates.updaterId = mailboxes.updaterId ```  ``` sequence_templates.creatorId = mailboxes.userId ```  ``` sequence_templates.updaterId = mailboxes.userId ``` |
| [opportunities](#opportunities) | ``` sequence_templates.creatorId = opportunities.creatorId ```  ``` sequence_templates.updaterId = opportunities.creatorId ```  ``` sequence_templates.creatorId = opportunities.ownerId ```  ``` sequence_templates.updaterId = opportunities.ownerId ``` |
| [prospects](#prospects) | ``` sequence_templates.creatorId = prospects.creatorId ```  ``` sequence_templates.updaterId = prospects.creatorId ```  ``` sequence_templates.creatorId = prospects.updaterId ```  ``` sequence_templates.updaterId = prospects.updaterId ``` |
| [sequence\_states](#sequence-states) | ``` sequence_templates.creatorId = sequence_states.creatorId ```  ``` sequence_templates.updaterId = sequence_states.creatorId ``` |
| [sequence\_steps](#sequence-steps) | ``` sequence_templates.creatorId = sequence_steps.creatorId ```  ``` sequence_templates.updaterId = sequence_steps.creatorId ```  ``` sequence_templates.creatorId = sequence_steps.updaterId ```  ``` sequence_templates.updaterId = sequence_steps.updaterId ``` |
| [sequences](#sequences) | ``` sequence_templates.creatorId = sequences.creatorId ```  ``` sequence_templates.updaterId = sequences.creatorId ```  ``` sequence_templates.creatorId = sequences.ownerId ```  ``` sequence_templates.updaterId = sequences.ownerId ```  ``` sequence_templates.creatorId = sequences.updaterId ```  ``` sequence_templates.updaterId = sequences.updaterId ``` |
| [stages](#stages) | ``` sequence_templates.creatorId = stages.creatorId ```  ``` sequence_templates.updaterId = stages.creatorId ```  ``` sequence_templates.creatorId = stages.updaterId ```  ``` sequence_templates.updaterId = stages.updaterId ``` |
| [tasks](#tasks) | ``` sequence_templates.creatorId = tasks.creatorId ```  ``` sequence_templates.updaterId = tasks.creatorId ```  ``` sequence_templates.creatorId = tasks.completerId ```  ``` sequence_templates.updaterId = tasks.completerId ``` |
| [users](#users) | ``` sequence_templates.creatorId = users.creatorId ```  ``` sequence_templates.updaterId = users.creatorId ```  ``` sequence_templates.creatorId = users.id ```  ``` sequence_templates.updaterId = users.id ```  ``` sequence_templates.creatorId = users.updaterId ```  ``` sequence_templates.updaterId = users.updaterId ``` |

sequence\_templates table schema

|  |
| --- |
| **bounceCount**  INTEGER |
| **clickCount**  INTEGER |
| **createdAt**  DATE-TIME |
| **creatorId**  INTEGER |
| **deliverCount**  INTEGER |
| **enabled**  BOOLEAN |
| **enabledAt**  DATE-TIME |
| **failureCount**  INTEGER |
| **id**  INTEGER |
| **isReply**  BOOLEAN |
| **negaitveReplyCount**  INTEGER |
| **neutralReplyCount**  INTEGER |
| **openCount**  INTEGER |
| **optOutCount**  INTEGER |
| **positiveReplyCount**  INTEGER |
| **replyCount**  INTEGER |
| **scheduleCount**  INTEGER |
| **sequenceStepId**  INTEGER |
| **templateId**  INTEGER |
| **updatedAt**  DATE-TIME |
| **updaterId**  INTEGER |

### sequences

The `sequences` table contains info about sequences.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [Outreach API method](https://api.outreach.io/api/v2/docs#sequence "Opens in new tab: Outreach API method") |

sequences table foreign keys

| Join sequences with | on |
| --- | --- |
| [accounts](#accounts) | ``` sequences.creatorId = accounts.creatorId ```  ``` sequences.ownerId = accounts.creatorId ```  ``` sequences.updaterId = accounts.creatorId ```  ``` sequences.creatorId = accounts.ownerId ```  ``` sequences.ownerId = accounts.ownerId ```  ``` sequences.updaterId = accounts.ownerId ```  ``` sequences.creatorId = accounts.updaterId ```  ``` sequences.ownerId = accounts.updaterId ```  ``` sequences.updaterId = accounts.updaterId ``` |
| [call\_dispositions](#call-dispositions) | ``` sequences.creatorId = call_dispositions.creatorId ```  ``` sequences.ownerId = call_dispositions.creatorId ```  ``` sequences.updaterId = call_dispositions.creatorId ``` |
| [call\_purposes](#call-purposes) | ``` sequences.creatorId = call_purposes.creatorId ```  ``` sequences.ownerId = call_purposes.creatorId ```  ``` sequences.updaterId = call_purposes.creatorId ``` |
| [calls](#calls) | ``` sequences.creatorId = calls.userId ```  ``` sequences.ownerId = calls.userId ```  ``` sequences.updaterId = calls.userId ``` |
| [content\_categories](#content-categories) | ``` sequences.creatorId = content_categories.creatorId ```  ``` sequences.ownerId = content_categories.creatorId ```  ``` sequences.updaterId = content_categories.creatorId ``` |
| [mailboxes](#mailboxes) | ``` sequences.creatorId = mailboxes.creatorId ```  ``` sequences.ownerId = mailboxes.creatorId ```  ``` sequences.updaterId = mailboxes.creatorId ```  ``` sequences.creatorId = mailboxes.updaterId ```  ``` sequences.ownerId = mailboxes.updaterId ```  ``` sequences.updaterId = mailboxes.updaterId ```  ``` sequences.creatorId = mailboxes.userId ```  ``` sequences.ownerId = mailboxes.userId ```  ``` sequences.updaterId = mailboxes.userId ``` |
| [opportunities](#opportunities) | ``` sequences.creatorId = opportunities.creatorId ```  ``` sequences.ownerId = opportunities.creatorId ```  ``` sequences.updaterId = opportunities.creatorId ```  ``` sequences.creatorId = opportunities.ownerId ```  ``` sequences.ownerId = opportunities.ownerId ```  ``` sequences.updaterId = opportunities.ownerId ``` |
| [prospects](#prospects) | ``` sequences.creatorId = prospects.creatorId ```  ``` sequences.ownerId = prospects.creatorId ```  ``` sequences.updaterId = prospects.creatorId ```  ``` sequences.creatorId = prospects.updaterId ```  ``` sequences.ownerId = prospects.updaterId ```  ``` sequences.updaterId = prospects.updaterId ``` |
| [sequence\_states](#sequence-states) | ``` sequences.creatorId = sequence_states.creatorId ```  ``` sequences.ownerId = sequence_states.creatorId ```  ``` sequences.updaterId = sequence_states.creatorId ``` |
| [sequence\_steps](#sequence-steps) | ``` sequences.creatorId = sequence_steps.creatorId ```  ``` sequences.ownerId = sequence_steps.creatorId ```  ``` sequences.updaterId = sequence_steps.creatorId ```  ``` sequences.creatorId = sequence_steps.updaterId ```  ``` sequences.ownerId = sequence_steps.updaterId ```  ``` sequences.updaterId = sequence_steps.updaterId ``` |
| [sequence\_templates](#sequence-templates) | ``` sequences.creatorId = sequence_templates.creatorId ```  ``` sequences.ownerId = sequence_templates.creatorId ```  ``` sequences.updaterId = sequence_templates.creatorId ```  ``` sequences.creatorId = sequence_templates.updaterId ```  ``` sequences.ownerId = sequence_templates.updaterId ```  ``` sequences.updaterId = sequence_templates.updaterId ``` |
| [stages](#stages) | ``` sequences.creatorId = stages.creatorId ```  ``` sequences.ownerId = stages.creatorId ```  ``` sequences.updaterId = stages.creatorId ```  ``` sequences.creatorId = stages.updaterId ```  ``` sequences.ownerId = stages.updaterId ```  ``` sequences.updaterId = stages.updaterId ``` |
| [tasks](#tasks) | ``` sequences.creatorId = tasks.creatorId ```  ``` sequences.ownerId = tasks.creatorId ```  ``` sequences.updaterId = tasks.creatorId ```  ``` sequences.creatorId = tasks.completerId ```  ``` sequences.ownerId = tasks.completerId ```  ``` sequences.updaterId = tasks.completerId ``` |
| [users](#users) | ``` sequences.creatorId = users.creatorId ```  ``` sequences.ownerId = users.creatorId ```  ``` sequences.updaterId = users.creatorId ```  ``` sequences.creatorId = users.id ```  ``` sequences.ownerId = users.id ```  ``` sequences.updaterId = users.id ```  ``` sequences.creatorId = users.updaterId ```  ``` sequences.ownerId = users.updaterId ```  ``` sequences.updaterId = users.updaterId ``` |

sequences table schema

|  |
| --- |
| **automationPercentage**  NUMBER |
| **bounceCount**  INTEGER |
| **clickCount**  INTEGER |
| **createdAt**  DATE-TIME |
| **creatorId**  INTEGER |
| **deliverCount**  INTEGER |
| **description**  STRING |
| **durationInDays**  INTEGER |
| **enabled**  BOOLEAN |
| **enabledAt**  DATE-TIME |
| **failureCount**  INTEGER |
| **finishOnReply**  BOOLEAN |
| **id**  INTEGER |
| **lastUsedAt**  DATE-TIME |
| **locked**  BOOLEAN |
| **lockedAt**  DATE-TIME |
| **maxActivations**  INTEGER |
| **name**  STRING |
| **negativeReplyCount**  INTEGER |
| **neutralReplyCount**  INTEGER |
| **numContactedProspects**  INTEGER |
| **numRepliedProspects**  INTEGER |
| **openCount**  INTEGER |
| **optOutCount**  INTEGER |
| **ownerId**  INTEGER |
| **positiveReplyCount**  INTEGER |
| **primaryReplyAction**  STRING |
| **primaryReplyPauseDuration**  INTEGER |
| **replyCount**  INTEGER |
| **rulesetId**  INTEGER |
| **scheduleCount**  INTEGER |
| **scheduleIntervalType**  STRING |
| **secondaryReplyAction**  STRING |
| **secondaryReplyPauseDuration**  INTEGER |
| **sequenceStepCount**  INTEGER |
| **sequenceType**  STRING |
| **shareType**  STRING |
| **tags**  ARRAY This is a nested data structure. |
| **throttleCapacity**  INTEGER |
| **throttleMaxAddsPerDay**  INTEGER |
| **throttlePaused**  BOOLEAN |
| **throttlePausedAt**  DATE-TIME |
| **transactional**  BOOLEAN |
| **updatedAt**  DATE-TIME |
| **updaterId**  INTEGER |

### stages

The `stages` table contains information about different stages in a deal process.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [Outreach API method](https://api.outreach.io/api/v2/docs#stage "Opens in new tab: Outreach API method") |

stages table foreign keys

| Join stages with | on |
| --- | --- |
| [opportunities](#opportunities) | ``` stages.id = opportunities.opportunityStageId ```  ``` stages.creatorId = opportunities.creatorId ```  ``` stages.updaterId = opportunities.creatorId ```  ``` stages.creatorId = opportunities.ownerId ```  ``` stages.updaterId = opportunities.ownerId ``` |
| [prospects](#prospects) | ``` stages.id = prospects.stageId ```  ``` stages.creatorId = prospects.creatorId ```  ``` stages.updaterId = prospects.creatorId ```  ``` stages.creatorId = prospects.updaterId ```  ``` stages.updaterId = prospects.updaterId ``` |
| [accounts](#accounts) | ``` stages.creatorId = accounts.creatorId ```  ``` stages.updaterId = accounts.creatorId ```  ``` stages.creatorId = accounts.ownerId ```  ``` stages.updaterId = accounts.ownerId ```  ``` stages.creatorId = accounts.updaterId ```  ``` stages.updaterId = accounts.updaterId ``` |
| [call\_dispositions](#call-dispositions) | ``` stages.creatorId = call_dispositions.creatorId ```  ``` stages.updaterId = call_dispositions.creatorId ``` |
| [call\_purposes](#call-purposes) | ``` stages.creatorId = call_purposes.creatorId ```  ``` stages.updaterId = call_purposes.creatorId ``` |
| [calls](#calls) | ``` stages.creatorId = calls.userId ```  ``` stages.updaterId = calls.userId ``` |
| [content\_categories](#content-categories) | ``` stages.creatorId = content_categories.creatorId ```  ``` stages.updaterId = content_categories.creatorId ``` |
| [mailboxes](#mailboxes) | ``` stages.creatorId = mailboxes.creatorId ```  ``` stages.updaterId = mailboxes.creatorId ```  ``` stages.creatorId = mailboxes.updaterId ```  ``` stages.updaterId = mailboxes.updaterId ```  ``` stages.creatorId = mailboxes.userId ```  ``` stages.updaterId = mailboxes.userId ``` |
| [sequence\_states](#sequence-states) | ``` stages.creatorId = sequence_states.creatorId ```  ``` stages.updaterId = sequence_states.creatorId ``` |
| [sequence\_steps](#sequence-steps) | ``` stages.creatorId = sequence_steps.creatorId ```  ``` stages.updaterId = sequence_steps.creatorId ```  ``` stages.creatorId = sequence_steps.updaterId ```  ``` stages.updaterId = sequence_steps.updaterId ``` |
| [sequence\_templates](#sequence-templates) | ``` stages.creatorId = sequence_templates.creatorId ```  ``` stages.updaterId = sequence_templates.creatorId ```  ``` stages.creatorId = sequence_templates.updaterId ```  ``` stages.updaterId = sequence_templates.updaterId ``` |
| [sequences](#sequences) | ``` stages.creatorId = sequences.creatorId ```  ``` stages.updaterId = sequences.creatorId ```  ``` stages.creatorId = sequences.ownerId ```  ``` stages.updaterId = sequences.ownerId ```  ``` stages.creatorId = sequences.updaterId ```  ``` stages.updaterId = sequences.updaterId ``` |
| [tasks](#tasks) | ``` stages.creatorId = tasks.creatorId ```  ``` stages.updaterId = tasks.creatorId ```  ``` stages.creatorId = tasks.completerId ```  ``` stages.updaterId = tasks.completerId ``` |
| [users](#users) | ``` stages.creatorId = users.creatorId ```  ``` stages.updaterId = users.creatorId ```  ``` stages.creatorId = users.id ```  ``` stages.updaterId = users.id ```  ``` stages.creatorId = users.updaterId ```  ``` stages.updaterId = users.updaterId ``` |

stages table schema

|  |
| --- |
| **color**  STRING |
| **createdAt**  DATE-TIME |
| **creatorId**  INTEGER |
| **id**  INTEGER |
| **name**  STRING |
| **order**  INTEGER |
| **updatedAt**  DATE-TIME |
| **updaterId**  INTEGER |

### tasks

The `tasks` table contains information about items that require action in Outreach.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [Outreach API method](https://api.outreach.io/api/v2/docs#task "Opens in new tab: Outreach API method") |

tasks table foreign keys

| Join tasks with | on |
| --- | --- |
| [accounts](#accounts) | ``` tasks.id = accounts.id ```  ``` tasks.creatorId = accounts.creatorId ```  ``` tasks.completerId = accounts.creatorId ```  ``` tasks.creatorId = accounts.ownerId ```  ``` tasks.completerId = accounts.ownerId ```  ``` tasks.creatorId = accounts.updaterId ```  ``` tasks.completerId = accounts.updaterId ``` |
| [opportunities](#opportunities) | ``` tasks.id = opportunities.id ```  ``` tasks.opportunityId = opportunities.id ```  ``` tasks.creatorId = opportunities.creatorId ```  ``` tasks.completerId = opportunities.creatorId ```  ``` tasks.creatorId = opportunities.ownerId ```  ``` tasks.completerId = opportunities.ownerId ``` |
| [prospects](#prospects) | ``` tasks.id = prospects.id ```  ``` tasks.prospectId = prospects.id ```  ``` tasks.creatorId = prospects.creatorId ```  ``` tasks.completerId = prospects.creatorId ```  ``` tasks.creatorId = prospects.updaterId ```  ``` tasks.completerId = prospects.updaterId ``` |
| [sequence\_states](#sequence-states) | ``` tasks.id = sequence_states.id ```  ``` tasks.prospectId = sequence_states.prospectId ```  ``` tasks.sequenceId = sequence_states.sequenceId ```  ``` tasks.sequenceStateId = sequence_states.id ```  ``` tasks.creatorId = sequence_states.creatorId ```  ``` tasks.completerId = sequence_states.creatorId ``` |
| [calls](#calls) | ``` tasks.callId = calls.id ```  ``` tasks.opportunityId = calls.opportunityId ```  ``` tasks.prospectId = calls.prospectId ```  ``` tasks.sequenceId = calls.sequenceId ```  ``` tasks.sequenceStateId = calls.sequenceStateId ```  ``` tasks.sequenceStepId = calls.sequenceStepId ```  ``` tasks.id = calls.id ```  ``` tasks.creatorId = calls.userId ```  ``` tasks.completerId = calls.userId ``` |
| [events](#events) | ``` tasks.mailingId = events.mailingId ```  ``` tasks.prospectId = events.prospectId ``` |
| [mailings](#mailings) | ``` tasks.mailingId = mailings.id ```  ``` tasks.opportunityId = mailings.opportunityId ```  ``` tasks.prospectId = mailings.prospectId ```  ``` tasks.sequenceId = mailings.sequenceId ```  ``` tasks.sequenceStateId = mailings.sequenceStateId ```  ``` tasks.sequenceStepId = mailings.sequenceStepId ```  ``` tasks.id = mailings.id ``` |
| [sequence\_steps](#sequence-steps) | ``` tasks.sequenceId = sequence_steps.sequenceId ```  ``` tasks.sequenceStepId = sequence_steps.id ```  ``` tasks.creatorId = sequence_steps.creatorId ```  ``` tasks.completerId = sequence_steps.creatorId ```  ``` tasks.creatorId = sequence_steps.updaterId ```  ``` tasks.completerId = sequence_steps.updaterId ``` |
| [call\_dispositions](#call-dispositions) | ``` tasks.creatorId = call_dispositions.creatorId ```  ``` tasks.completerId = call_dispositions.creatorId ``` |
| [call\_purposes](#call-purposes) | ``` tasks.creatorId = call_purposes.creatorId ```  ``` tasks.completerId = call_purposes.creatorId ``` |
| [content\_categories](#content-categories) | ``` tasks.creatorId = content_categories.creatorId ```  ``` tasks.completerId = content_categories.creatorId ``` |
| [mailboxes](#mailboxes) | ``` tasks.creatorId = mailboxes.creatorId ```  ``` tasks.completerId = mailboxes.creatorId ```  ``` tasks.creatorId = mailboxes.updaterId ```  ``` tasks.completerId = mailboxes.updaterId ```  ``` tasks.creatorId = mailboxes.userId ```  ``` tasks.completerId = mailboxes.userId ``` |
| [sequence\_templates](#sequence-templates) | ``` tasks.creatorId = sequence_templates.creatorId ```  ``` tasks.completerId = sequence_templates.creatorId ```  ``` tasks.creatorId = sequence_templates.updaterId ```  ``` tasks.completerId = sequence_templates.updaterId ``` |
| [sequences](#sequences) | ``` tasks.creatorId = sequences.creatorId ```  ``` tasks.completerId = sequences.creatorId ```  ``` tasks.creatorId = sequences.ownerId ```  ``` tasks.completerId = sequences.ownerId ```  ``` tasks.creatorId = sequences.updaterId ```  ``` tasks.completerId = sequences.updaterId ``` |
| [stages](#stages) | ``` tasks.creatorId = stages.creatorId ```  ``` tasks.completerId = stages.creatorId ```  ``` tasks.creatorId = stages.updaterId ```  ``` tasks.completerId = stages.updaterId ``` |
| [users](#users) | ``` tasks.creatorId = users.creatorId ```  ``` tasks.completerId = users.creatorId ```  ``` tasks.creatorId = users.id ```  ``` tasks.completerId = users.id ```  ``` tasks.creatorId = users.updaterId ```  ``` tasks.completerId = users.updaterId ``` |

tasks table schema

|  |
| --- |
| **accountId**  INTEGER |
| **action**  STRING |
| **autoskipAt**  DATE-TIME |
| **callId**  INTEGER |
| **compiledSequenceTemplateHtml**  STRING |
| **completed**  BOOLEAN |
| **completedAt**  DATE-TIME |
| **completerId**  INTEGER |
| **createdAt**  DATE-TIME |
| **creatorId**  INTEGER |
| **dueAt**  DATE-TIME |
| **id**  INTEGER |
| **mailingId**  INTEGER |
| **note**  STRING |
| **opportunityAssociation**  STRING |
| **opportunityId**  INTEGER |
| **ownerId**  INTEGER |
| **prospectId**  INTEGER |
| **scheduledAt**  DATE-TIME |
| **sequenceId**  INTEGER |
| **sequenceStateId**  INTEGER |
| **sequenceStepId**  INTEGER |
| **sequenceTemplateId**  INTEGER |
| **state**  STRING |
| **stateChangedAt**  DATE-TIME |
| **subjectId**  INTEGER |
| **taskPriorityId**  INTEGER |
| **taskThemeId**  INTEGER |
| **taskType**  STRING |
| **templateId**  INTEGER |
| **updatedAt**  DATE-TIME |

### teams

The `teams` table contains information about groups of users in Outreach.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [Outreach API method](https://api.outreach.io/api/v2/docs#team "Opens in new tab: Outreach API method") |

teams table schema

|  |
| --- |
| **color**  STRING |
| **createdAt**  DATE-TIME |
| **creatorId**  INTEGER |
| **id**  INTEGER |
| **name**  STRING |
| **scimExternalId**  STRING |
| **scimSource**  STRING |
| **updatedAt**  DATE-TIME |
| **updaterId**  INTEGER |

### users

The `users` table contains information about individual users that use the Outreach app.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [Outreach API method](https://api.outreach.io/api/v2/docs#user "Opens in new tab: Outreach API method") |

users table foreign keys

| Join users with | on |
| --- | --- |
| [duties](#duties) | ``` users.duties.id = duties.id ``` |
| [mailboxes](#mailboxes) | ``` users.mailboxId = mailboxes.id ```  ``` users.creatorId = mailboxes.creatorId ```  ``` users.id = mailboxes.creatorId ```  ``` users.updaterId = mailboxes.creatorId ```  ``` users.creatorId = mailboxes.updaterId ```  ``` users.id = mailboxes.updaterId ```  ``` users.updaterId = mailboxes.updaterId ```  ``` users.creatorId = mailboxes.userId ```  ``` users.id = mailboxes.userId ```  ``` users.updaterId = mailboxes.userId ``` |
| [mailings](#mailings) | ``` users.mailboxId = mailings.mailboxId ``` |
| [accounts](#accounts) | ``` users.creatorId = accounts.creatorId ```  ``` users.id = accounts.creatorId ```  ``` users.updaterId = accounts.creatorId ```  ``` users.creatorId = accounts.ownerId ```  ``` users.id = accounts.ownerId ```  ``` users.updaterId = accounts.ownerId ```  ``` users.creatorId = accounts.updaterId ```  ``` users.id = accounts.updaterId ```  ``` users.updaterId = accounts.updaterId ``` |
| [call\_dispositions](#call-dispositions) | ``` users.creatorId = call_dispositions.creatorId ```  ``` users.id = call_dispositions.creatorId ```  ``` users.updaterId = call_dispositions.creatorId ``` |
| [call\_purposes](#call-purposes) | ``` users.creatorId = call_purposes.creatorId ```  ``` users.id = call_purposes.creatorId ```  ``` users.updaterId = call_purposes.creatorId ``` |
| [calls](#calls) | ``` users.creatorId = calls.userId ```  ``` users.id = calls.userId ```  ``` users.updaterId = calls.userId ``` |
| [content\_categories](#content-categories) | ``` users.creatorId = content_categories.creatorId ```  ``` users.id = content_categories.creatorId ```  ``` users.updaterId = content_categories.creatorId ``` |
| [opportunities](#opportunities) | ``` users.creatorId = opportunities.creatorId ```  ``` users.id = opportunities.creatorId ```  ``` users.updaterId = opportunities.creatorId ```  ``` users.creatorId = opportunities.ownerId ```  ``` users.id = opportunities.ownerId ```  ``` users.updaterId = opportunities.ownerId ``` |
| [prospects](#prospects) | ``` users.creatorId = prospects.creatorId ```  ``` users.id = prospects.creatorId ```  ``` users.updaterId = prospects.creatorId ```  ``` users.creatorId = prospects.updaterId ```  ``` users.id = prospects.updaterId ```  ``` users.updaterId = prospects.updaterId ``` |
| [sequence\_states](#sequence-states) | ``` users.creatorId = sequence_states.creatorId ```  ``` users.id = sequence_states.creatorId ```  ``` users.updaterId = sequence_states.creatorId ``` |
| [sequence\_steps](#sequence-steps) | ``` users.creatorId = sequence_steps.creatorId ```  ``` users.id = sequence_steps.creatorId ```  ``` users.updaterId = sequence_steps.creatorId ```  ``` users.creatorId = sequence_steps.updaterId ```  ``` users.id = sequence_steps.updaterId ```  ``` users.updaterId = sequence_steps.updaterId ``` |
| [sequence\_templates](#sequence-templates) | ``` users.creatorId = sequence_templates.creatorId ```  ``` users.id = sequence_templates.creatorId ```  ``` users.updaterId = sequence_templates.creatorId ```  ``` users.creatorId = sequence_templates.updaterId ```  ``` users.id = sequence_templates.updaterId ```  ``` users.updaterId = sequence_templates.updaterId ``` |
| [sequences](#sequences) | ``` users.creatorId = sequences.creatorId ```  ``` users.id = sequences.creatorId ```  ``` users.updaterId = sequences.creatorId ```  ``` users.creatorId = sequences.ownerId ```  ``` users.id = sequences.ownerId ```  ``` users.updaterId = sequences.ownerId ```  ``` users.creatorId = sequences.updaterId ```  ``` users.id = sequences.updaterId ```  ``` users.updaterId = sequences.updaterId ``` |
| [stages](#stages) | ``` users.creatorId = stages.creatorId ```  ``` users.id = stages.creatorId ```  ``` users.updaterId = stages.creatorId ```  ``` users.creatorId = stages.updaterId ```  ``` users.id = stages.updaterId ```  ``` users.updaterId = stages.updaterId ``` |
| [tasks](#tasks) | ``` users.creatorId = tasks.creatorId ```  ``` users.id = tasks.creatorId ```  ``` users.updaterId = tasks.creatorId ```  ``` users.creatorId = tasks.completerId ```  ``` users.id = tasks.completerId ```  ``` users.updaterId = tasks.completerId ``` |

users table schema

|  |
| --- |
| **accountsViewId**  INTEGER |
| **activityNotificationsDisabled**  BOOLEAN |
| **bounceWarningEmailEnabled**  BOOLEAN |
| **bridgePhone**  STRING |
| **bridgePhoneExtension**  STRING |
| **callsViewId**  INTEGER |
| **controlledTabDefault**  STRING |
| **createdAt**  DATE-TIME |
| **creatorId**  INTEGER |
| **currentSignInAt**  DATE-TIME |
| **custom1**  STRING |
| **custom2**  STRING |
| **custom3**  STRING |
| **custom4**  STRING |
| **custom5**  STRING |
| **dailyDigestEmailEnabled**  BOOLEAN |
| **duties**  ARRAY This is a nested data structure:   - duty\_type: STRING - id: INTEGER - name: STRING |
| **email**  STRING |
| **enableVoiceRecordings**  BOOLEAN |
| **engagementEmailsEnabled**  BOOLEAN |
| **firstName**  STRING |
| **id**  INTEGER |
| **inboundBridgePhone**  STRING |
| **inboundBridgePhoneExtension**  STRING |
| **inboundCallBehavior**  STRING |
| **inboundPhoneType**  STRING |
| **inboundVoicemailCustomMessageText**  STRING |
| **inboundVoicemailMessageTextVoice**  STRING |
| **inboundVoicemailPromptType**  STRING |
| **kaiaRecordingsViewId**  INTEGER |
| **keepBridgePhoneConnected**  BOOLEAN |
| **lastName**  STRING |
| **lastSignInAt**  DATE-TIME |
| **locked**  BOOLEAN |
| **mailboxErrorEmailEnabled**  BOOLEAN |
| **mailboxId**  INTEGER |
| **meetingEngagementNotificationEnabled**  BOOLEAN |
| **name**  STRING |
| **notificationsEnabled**  BOOLEAN |
| **oceClickToDialEverywhere**  BOOLEAN |
| **oceGmailToolbar**  BOOLEAN |
| **oceGmailTrackingState**  STRING |
| **oceSalesforceEmailDecorating**  BOOLEAN |
| **oceSalesforcePhoneDecorating**  BOOLEAN |
| **oceUniversalTaskFlow**  BOOLEAN |
| **oceWindowMode**  BOOLEAN |
| **opportunitiesViewId**  INTEGER |
| **passwordExpiresAt**  DATE-TIME |
| **phoneCountryCode**  STRING |
| **phoneNumber**  STRING |
| **phoneType**  STRING |
| **pluginAlertNotificationEnabled**  BOOLEAN |
| **preferredVoiceRegion**  STRING |
| **prefersLocalPresence**  BOOLEAN |
| **primaryTimezone**  STRING |
| **profileId**  INTEGER |
| **prospectsViewId**  INTEGER |
| **reportsTeamPerfViewId**  INTEGER |
| **reportsViewId**  INTEGER |
| **roleId**  INTEGER |
| **scimExternalId**  STRING |
| **scimSource**  STRING |
| **secondaryTimezone**  STRING |
| **senderNotificationsExcluded**  STRING |
| **tasksViewId**  INTEGER |
| **teamsViewId**  INTEGER |
| **tertiaryTimezone**  STRING |
| **textingEmailNotifications**  BOOLEAN |
| **title**  STRING |
| **unknownReplyEmailEnabled**  BOOLEAN |
| **updatedAt**  DATE-TIME |
| **updaterId**  INTEGER |
| **userGuid**  STRING |
| **username**  STRING |
| **usersViewId**  INTEGER |
| **voicemailNotificationEnabled**  BOOLEAN |
| **weeklyDigestEmailEnabled**  BOOLEAN |
