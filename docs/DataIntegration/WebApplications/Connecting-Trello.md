---
title: "Trello"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Trello.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Trello

Trello is a web-based, kanban-style, list-making application developed by Atlassian.

Trello integration replicates data using the [Trello REST API](https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

You need administrator permissions in your Trello account.

To generate your API key and API token:

1. Log into your [Trello](https://trello.com/power-ups/admin) account.
2. Click New in the upper-right corner.
3. Configure your app:
   - Name: Enter a name for your app.
   - Workspace: Select the Trello workspace that owns the app.
   - Email: Enter an email address to contact you about this app.
   - Support Email: Enter the email address that users and the platform team can use to contact you about your app or platform changes.
   - Author: Enter the author name to display in the directory and on authorization screens.
4. Click Create.
5. Go to API Key and click Generate a new API Key.
6. Copy and paste your API key into a secured file.
7. Click Token next to your Trello API key.
8. When prompted, select Allow to grant all requested permissions.
9. Copy and paste your API token into a secured file.

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
| API Key | API key. |
| API Token | API token. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### actions

The actions table contains information about the actions within each board the [authorizing user](#data-replication-board-membership) is a member of.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | board id |
| **Useful links** | [Trello API method](https://developer.atlassian.com/cloud/trello/rest/#api-boards-boardId-actions-get "Opens in new tab: Trello API method") |

actions table foreign keys

| Join actions with | on |
| --- | --- |
| [boards](#boards) | ``` actions.data.board.id = boards.id ```  ``` actions.data.organization.id = boards.idOrganization ```  ``` actions.idMemberCreator = boards.memberships.idMember ```  ``` actions.data.idMember = boards.memberships.idMember ```  ``` actions.data.idMemberAdded = boards.memberships.idMember ```  ``` actions.data.idMemberInviter = boards.memberships.idMember ```  ``` actions.data.card.idMembers = boards.memberships.idMember ```  ``` actions.data.member.id = boards.memberships.idMember ```  ``` actions.data.old.idMembers = boards.memberships.idMember ```  ``` actions.member.id = boards.memberships.idMember ```  ``` actions.memberCreator.id = boards.memberships.idMember ``` |
| [cards](#cards) | ``` actions.data.board.id = cards.idBoard ```  ``` actions.data.board.id = cards.labels.idBoard ```  ``` actions.data.card.id = cards.id ```  ``` actions.data.card.idList = cards.idList ```  ``` actions.data.list.id = cards.idList ```  ``` actions.data.listAfter.id = cards.idList ```  ``` actions.data.listBefore.id = cards.idList ```  ``` actions.data.old.idList = cards.idList ```  ``` actions.idMemberCreator = cards.idMembers ```  ``` actions.data.idMember = cards.idMembers ```  ``` actions.data.idMemberAdded = cards.idMembers ```  ``` actions.data.idMemberInviter = cards.idMembers ```  ``` actions.data.card.idMembers = cards.idMembers ```  ``` actions.data.member.id = cards.idMembers ```  ``` actions.data.old.idMembers = cards.idMembers ```  ``` actions.member.id = cards.idMembers ```  ``` actions.memberCreator.id = cards.idMembers ```  ``` actions.idMemberCreator = cards.idMembersVoted ```  ``` actions.data.idMember = cards.idMembersVoted ```  ``` actions.data.idMemberAdded = cards.idMembersVoted ```  ``` actions.data.idMemberInviter = cards.idMembersVoted ```  ``` actions.data.card.idMembers = cards.idMembersVoted ```  ``` actions.data.member.id = cards.idMembersVoted ```  ``` actions.data.old.idMembers = cards.idMembersVoted ```  ``` actions.member.id = cards.idMembersVoted ```  ``` actions.memberCreator.id = cards.idMembersVoted ``` |
| [checklists](#checklists) | ``` actions.data.board.id = checklists.data.board.id ```  ``` actions.data.board.id = checklists.idBoard ```  ``` actions.data.card.id = checklists.idCard ```  ``` actions.data.card.id = checklists.data.card.id ```  ``` actions.data.card.idList = checklists.idList ```  ``` actions.data.list.id = checklists.idList ```  ``` actions.data.listAfter.id = checklists.idList ```  ``` actions.data.listBefore.id = checklists.idList ```  ``` actions.data.old.idList = checklists.idList ```  ``` actions.data.card.idList = checklists.data.list.id ```  ``` actions.data.list.id = checklists.data.list.id ```  ``` actions.data.listAfter.id = checklists.data.list.id ```  ``` actions.data.listBefore.id = checklists.data.list.id ```  ``` actions.data.old.idList = checklists.data.list.id ```  ``` actions.data.organization.id = checklists.idOrganization ```  ``` actions.data.organization.id = checklists.data.organization.id ```  ``` actions.idMemberCreator = checklists.checkItems.idMember ```  ``` actions.data.idMember = checklists.checkItems.idMember ```  ``` actions.data.idMemberAdded = checklists.checkItems.idMember ```  ``` actions.data.idMemberInviter = checklists.checkItems.idMember ```  ``` actions.data.card.idMembers = checklists.checkItems.idMember ```  ``` actions.data.member.id = checklists.checkItems.idMember ```  ``` actions.data.old.idMembers = checklists.checkItems.idMember ```  ``` actions.member.id = checklists.checkItems.idMember ```  ``` actions.memberCreator.id = checklists.checkItems.idMember ```  ``` actions.idMemberCreator = checklists.idMemberCreator ```  ``` actions.data.idMember = checklists.idMemberCreator ```  ``` actions.data.idMemberAdded = checklists.idMemberCreator ```  ``` actions.data.idMemberInviter = checklists.idMemberCreator ```  ``` actions.data.card.idMembers = checklists.idMemberCreator ```  ``` actions.data.member.id = checklists.idMemberCreator ```  ``` actions.data.old.idMembers = checklists.idMemberCreator ```  ``` actions.member.id = checklists.idMemberCreator ```  ``` actions.memberCreator.id = checklists.idMemberCreator ```  ``` actions.idMemberCreator = checklists.memberCreator.id ```  ``` actions.data.idMember = checklists.memberCreator.id ```  ``` actions.data.idMemberAdded = checklists.memberCreator.id ```  ``` actions.data.idMemberInviter = checklists.memberCreator.id ```  ``` actions.data.card.idMembers = checklists.memberCreator.id ```  ``` actions.data.member.id = checklists.memberCreator.id ```  ``` actions.data.old.idMembers = checklists.memberCreator.id ```  ``` actions.member.id = checklists.memberCreator.id ```  ``` actions.memberCreator.id = checklists.memberCreator.id ```  ``` actions.idMemberCreator = checklists.memberships.idMember ```  ``` actions.data.idMember = checklists.memberships.idMember ```  ``` actions.data.idMemberAdded = checklists.memberships.idMember ```  ``` actions.data.idMemberInviter = checklists.memberships.idMember ```  ``` actions.data.card.idMembers = checklists.memberships.idMember ```  ``` actions.data.member.id = checklists.memberships.idMember ```  ``` actions.data.old.idMembers = checklists.memberships.idMember ```  ``` actions.member.id = checklists.memberships.idMember ```  ``` actions.memberCreator.id = checklists.memberships.idMember ``` |
| [lists](#lists) | ``` actions.data.board.id = lists.idBoard ```  ``` actions.data.card.idList = lists.id ```  ``` actions.data.list.id = lists.id ```  ``` actions.data.listAfter.id = lists.id ```  ``` actions.data.listBefore.id = lists.id ```  ``` actions.data.old.idList = lists.id ``` |
| [users](#users) | ``` actions.data.board.id = users.boardId ```  ``` actions.idMemberCreator = users.id ```  ``` actions.data.idMember = users.id ```  ``` actions.data.idMemberAdded = users.id ```  ``` actions.data.idMemberInviter = users.id ```  ``` actions.data.card.idMembers = users.id ```  ``` actions.data.member.id = users.id ```  ``` actions.data.old.idMembers = users.id ```  ``` actions.member.id = users.id ```  ``` actions.memberCreator.id = users.id ``` |

actions table schema

|  |
| --- |
| **data**  OBJECT This is a nested data structure:   - board: OBJECT, which is also a nested data structure.   - id: STRING   - name: STRING   - prefs: OBJECT, which is also a nested data structure.     - background: STRING   - shortLink: STRING - card: OBJECT, which is also a nested data structure.   - closed: BOOLEAN   - desc: STRING   - id: STRING   - idList: STRING   - idMembers: ARRAY, which is also a nested data structure.   - idShort: INTEGER   - name: STRING   - pos: NUMBER   - shortLink: STRING - cardSource: OBJECT, which is also a nested data structure.   - id: STRING   - idShort: INTEGER   - name: STRING   - shortLink: STRING - deactivated: BOOLEAN - idMember: STRING - idMemberAdded: STRING - idMemberInviter: STRING - list: OBJECT, which is also a nested data structure.   - closed: BOOLEAN   - id: STRING   - name: STRING   - pos: NUMBER - listAfter: OBJECT, which is also a nested data structure.   - id: STRING   - name: STRING - listBefore: OBJECT, which is also a nested data structure.   - id: STRING   - name: STRING - member: OBJECT, which is also a nested data structure.   - id: STRING   - name: STRING - memberType: STRING - method: STRING - old: OBJECT, which is also a nested data structure.   - closed: BOOLEAN   - desc: STRING   - id: STRING   - idList: STRING   - idMembers: ARRAY, which is also a nested data structure.   - idShort: INTEGER   - name: STRING   - pos: NUMBER   - prefs: OBJECT, which is also a nested data structure.     - background: STRING - organization: OBJECT, which is also a nested data structure.   - id: STRING   - name: STRING - text: STRING |
| **date**  STRING |
| **id**  STRING |
| **idMemberCreator**  STRING |
| **limits**  OBJECT This is a nested data structure:   - reactions: OBJECT, which is also a nested data structure.   - perAction: OBJECT, which is also a nested data structure.     - disableAt: INTEGER     - status: STRING     - warnAt: INTEGER   - uniquePerAction: OBJECT, which is also a nested data structure.     - disableAt: INTEGER     - status: STRING     - warnAt: INTEGER |
| **member**  OBJECT This is a nested data structure:   - activityBlocked: BOOLEAN - avatarHash: STRING - avatarUrl: STRING - fullName: STRING - id: STRING - idMemberReferrer: STRING - initials: STRING - nonPublicAvailable: BOOLEAN - username: STRING |
| **memberCreator**  OBJECT This is a nested data structure:   - activityBlocked: BOOLEAN - avatarHash: STRING - avatarUrl: STRING - fullName: STRING - id: STRING - idMemberReferrer: STRING - initials: STRING - nonPublicAvailable: BOOLEAN - username: STRING |
| **type**  STRING |

### boards

The boards table contains info about the boards that the [authorizing user](#data-replication-board-membership) is a member of.

#### Custom field support

Custom fields are supported for this table.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Trello API method](https://developer.atlassian.com/cloud/trello/rest/api-group-members/#api-members-id-boards-get "Opens in new tab: Trello API method") |

boards table foreign keys

| Join boards with | on |
| --- | --- |
| [actions](#actions) | ``` boards.id = actions.data.board.id ```  ``` boards.idOrganization = actions.data.organization.id ```  ``` boards.memberships.idMember = actions.idMemberCreator ```  ``` boards.memberships.idMember = actions.data.idMember ```  ``` boards.memberships.idMember = actions.data.idMemberAdded ```  ``` boards.memberships.idMember = actions.data.idMemberInviter ```  ``` boards.memberships.idMember = actions.data.card.idMembers ```  ``` boards.memberships.idMember = actions.data.member.id ```  ``` boards.memberships.idMember = actions.data.old.idMembers ```  ``` boards.memberships.idMember = actions.member.id ```  ``` boards.memberships.idMember = actions.memberCreator.id ``` |
| [cards](#cards) | ``` boards.id = cards.idBoard ```  ``` boards.id = cards.labels.idBoard ```  ``` boards.memberships.idMember = cards.idMembers ```  ``` boards.memberships.idMember = cards.idMembersVoted ``` |
| [checklists](#checklists) | ``` boards.id = checklists.data.board.id ```  ``` boards.id = checklists.idBoard ```  ``` boards.idOrganization = checklists.idOrganization ```  ``` boards.idOrganization = checklists.data.organization.id ```  ``` boards.memberships.idMember = checklists.checkItems.idMember ```  ``` boards.memberships.idMember = checklists.idMemberCreator ```  ``` boards.memberships.idMember = checklists.memberCreator.id ```  ``` boards.memberships.idMember = checklists.memberships.idMember ``` |
| [lists](#lists) | ``` boards.id = lists.idBoard ``` |
| [users](#users) | ``` boards.id = users.boardId ```  ``` boards.memberships.idMember = users.id ``` |

boards table schema

|  |
| --- |
| **closed**  BOOLEAN |
| **creationMethod**  STRING |
| **dateLastActivity**  DATE-TIME |
| **dateLastView**  DATE-TIME |
| **datePluginDisable**  DATE-TIME |
| **desc**  STRING |
| **descData**  STRING |
| **enterpriseOwned**  BOOLEAN |
| **id**  STRING |
| **idBoardSource**  STRING |
| **idEnterprise**  STRING |
| **idOrganization**  STRING |
| **idTags**  ARRAY This is a nested data structure. |
| **ixUpdate**  INTEGER |
| **labelNames**  OBJECT This is a nested data structure:   - black: STRING - blue: STRING - green: STRING - lime: STRING - orange: STRING - pink: STRING - purple: STRING - red: STRING - sky: STRING - yellow: STRING |
| **limits**  OBJECT This is a nested data structure:   - attachments: OBJECT, which is also a nested data structure.   - perBoard: OBJECT, which is also a nested data structure.     - disableAt: INTEGER     - status: STRING     - warnAt: INTEGER |
| **memberships**  ARRAY This is a nested data structure:   - deactivated: BOOLEAN - id: STRING - idMember: STRING - memberType: STRING - unconfirmed: BOOLEAN |
| **name**  STRING |
| **pinned**  BOOLEAN |
| **powerUps**  ARRAY This is a nested data structure. |
| **prefs**  OBJECT This is a nested data structure:   - background: STRING - backgroundBottomColor: STRING - backgroundBrightness: STRING - backgroundImage: STRING - backgroundImageScaled: ARRAY, which is also a nested data structure.   - height: INTEGER   - url: STRING   - width: INTEGER - backgroundTile: BOOLEAN - backgroundTopColor: STRING - calendarFeedEnabled: BOOLEAN - canBeEnterprise: BOOLEAN - canBeOrg: BOOLEAN - canBePrivate: BOOLEAN - canBePublic: BOOLEAN - canInvite: BOOLEAN - cardAging: STRING - cardCovers: BOOLEAN - comments: STRING - hideVotes: BOOLEAN - invitations: STRING - isTemplate: BOOLEAN - permissionLevel: STRING - selfJoin: BOOLEAN - voting: STRING |
| **premiumFeatures**  ARRAY This is a nested data structure. |
| **shortLink**  STRING |
| **shortUrl**  STRING |
| **starred**  BOOLEAN |
| **subscribed**  BOOLEAN |
| **templateGallery**  STRING |
| **url**  STRING |

### cards

The cards table contains info about all of the cards on boards that [authorizing user](#data-replication-board-membership) is a member of.

#### Custom field support

Custom fields are supported for this table.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Trello API method](https://developer.atlassian.com/cloud/trello/rest/api-group-boards/#api-boards-id-cards-filter-get "Opens in new tab: Trello API method") |

cards table foreign keys

| Join cards with | on |
| --- | --- |
| [boards](#boards) | ``` cards.idBoard = boards.id ```  ``` cards.labels.idBoard = boards.id ```  ``` cards.idMembers = boards.memberships.idMember ```  ``` cards.idMembersVoted = boards.memberships.idMember ``` |
| [actions](#actions) | ``` cards.idBoard = actions.data.board.id ```  ``` cards.labels.idBoard = actions.data.board.id ```  ``` cards.id = actions.data.card.id ```  ``` cards.idList = actions.data.card.idList ```  ``` cards.idList = actions.data.list.id ```  ``` cards.idList = actions.data.listAfter.id ```  ``` cards.idList = actions.data.listBefore.id ```  ``` cards.idList = actions.data.old.idList ```  ``` cards.idMembers = actions.idMemberCreator ```  ``` cards.idMembersVoted = actions.idMemberCreator ```  ``` cards.idMembers = actions.data.idMember ```  ``` cards.idMembersVoted = actions.data.idMember ```  ``` cards.idMembers = actions.data.idMemberAdded ```  ``` cards.idMembersVoted = actions.data.idMemberAdded ```  ``` cards.idMembers = actions.data.idMemberInviter ```  ``` cards.idMembersVoted = actions.data.idMemberInviter ```  ``` cards.idMembers = actions.data.card.idMembers ```  ``` cards.idMembersVoted = actions.data.card.idMembers ```  ``` cards.idMembers = actions.data.member.id ```  ``` cards.idMembersVoted = actions.data.member.id ```  ``` cards.idMembers = actions.data.old.idMembers ```  ``` cards.idMembersVoted = actions.data.old.idMembers ```  ``` cards.idMembers = actions.member.id ```  ``` cards.idMembersVoted = actions.member.id ```  ``` cards.idMembers = actions.memberCreator.id ```  ``` cards.idMembersVoted = actions.memberCreator.id ``` |
| [checklists](#checklists) | ``` cards.idBoard = checklists.data.board.id ```  ``` cards.labels.idBoard = checklists.data.board.id ```  ``` cards.idBoard = checklists.idBoard ```  ``` cards.labels.idBoard = checklists.idBoard ```  ``` cards.id = checklists.idCard ```  ``` cards.id = checklists.data.card.id ```  ``` cards.idChecklists = checklists.id ```  ``` cards.idChecklists = checklists.checkItems.idChecklist ```  ``` cards.idChecklists = checklists.data.checklist.id ```  ``` cards.idList = checklists.idList ```  ``` cards.idList = checklists.data.list.id ```  ``` cards.idMembers = checklists.checkItems.idMember ```  ``` cards.idMembersVoted = checklists.checkItems.idMember ```  ``` cards.idMembers = checklists.idMemberCreator ```  ``` cards.idMembersVoted = checklists.idMemberCreator ```  ``` cards.idMembers = checklists.memberCreator.id ```  ``` cards.idMembersVoted = checklists.memberCreator.id ```  ``` cards.idMembers = checklists.memberships.idMember ```  ``` cards.idMembersVoted = checklists.memberships.idMember ``` |
| [lists](#lists) | ``` cards.idBoard = lists.idBoard ```  ``` cards.labels.idBoard = lists.idBoard ```  ``` cards.idList = lists.id ``` |
| [users](#users) | ``` cards.idBoard = users.boardId ```  ``` cards.labels.idBoard = users.boardId ```  ``` cards.idMembers = users.id ```  ``` cards.idMembersVoted = users.id ``` |

cards table schema

|  |
| --- |
| **badges**  OBJECT This is a nested data structure:   - attachments: INTEGER - attachmentsByType: OBJECT, which is also a nested data structure.   - trello: OBJECT, which is also a nested data structure.     - board: INTEGER     - card: INTEGER - checkItems: INTEGER - checkItemsChecked: INTEGER - checkItemsEarliestDue: DATE-TIME - comments: INTEGER - description: BOOLEAN - due: DATE-TIME - dueComplete: BOOLEAN - fogbugz: STRING - location: BOOLEAN - subscribed: BOOLEAN - viewingMemberVoted: BOOLEAN - votes: INTEGER |
| **checkItemStates**  ARRAY This is a nested data structure. |
| **closed**  BOOLEAN |
| **cover**  OBJECT This is a nested data structure. |
| **customFieldItems**  ARRAY This is a nested data structure:   - id: STRING - idCustomField: STRING - idModel: STRING - idValue: STRING - modelType: STRING - value: OBJECT, which is also a nested data structure.   - checked: STRING   - date: STRING   - number: STRING   - option: STRING   - text: STRING |
| **dateLastActivity**  DATE-TIME |
| **desc**  STRING |
| **descData**  OBJECT This is a nested data structure:   - emoji: OBJECT, which is also a nested data structure. |
| **due**  DATE-TIME |
| **dueComplete**  BOOLEAN |
| **dueReminder**  STRING |
| **id**  STRING |
| **idAttachmentCover**  STRING |
| **idBoard**  STRING |
| **idChecklists**  ARRAY This is a nested data structure:   - id: STRING |
| **idLabels**  ARRAY This is a nested data structure. |
| **idList**  STRING |
| **idMembers**  ARRAY This is a nested data structure. |
| **idMembersVoted**  ARRAY This is a nested data structure. |
| **idShort**  INTEGER |
| **isTemplate**  BOOLEAN |
| **labels**  ARRAY This is a nested data structure:   - color: STRING - id: STRING - idBoard: STRING - name: STRING |
| **manualCoverAttachment**  BOOLEAN |
| **name**  STRING |
| **pos**  NUMBER |
| **shortLink**  STRING |
| **shortUrl**  STRING |
| **start**  STRING |
| **subscribed**  BOOLEAN |
| **url**  STRING |

### checklists

The checklists table contains info about checklists on boards that the [authorizing user](#data-replication-board-membership) is a member of.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Trello API method](https://developer.atlassian.com/cloud/trello/rest/api-group-boards/#api-boards-id-checklists-get "Opens in new tab: Trello API method") |

checklists table foreign keys

| Join checklists with | on |
| --- | --- |
| [boards](#boards) | ``` checklists.data.board.id = boards.id ```  ``` checklists.idBoard = boards.id ```  ``` checklists.idOrganization = boards.idOrganization ```  ``` checklists.data.organization.id = boards.idOrganization ```  ``` checklists.checkItems.idMember = boards.memberships.idMember ```  ``` checklists.idMemberCreator = boards.memberships.idMember ```  ``` checklists.memberCreator.id = boards.memberships.idMember ```  ``` checklists.memberships.idMember = boards.memberships.idMember ``` |
| [actions](#actions) | ``` checklists.data.board.id = actions.data.board.id ```  ``` checklists.idBoard = actions.data.board.id ```  ``` checklists.idCard = actions.data.card.id ```  ``` checklists.data.card.id = actions.data.card.id ```  ``` checklists.idList = actions.data.card.idList ```  ``` checklists.data.list.id = actions.data.card.idList ```  ``` checklists.idList = actions.data.list.id ```  ``` checklists.data.list.id = actions.data.list.id ```  ``` checklists.idList = actions.data.listAfter.id ```  ``` checklists.data.list.id = actions.data.listAfter.id ```  ``` checklists.idList = actions.data.listBefore.id ```  ``` checklists.data.list.id = actions.data.listBefore.id ```  ``` checklists.idList = actions.data.old.idList ```  ``` checklists.data.list.id = actions.data.old.idList ```  ``` checklists.idOrganization = actions.data.organization.id ```  ``` checklists.data.organization.id = actions.data.organization.id ```  ``` checklists.checkItems.idMember = actions.idMemberCreator ```  ``` checklists.idMemberCreator = actions.idMemberCreator ```  ``` checklists.memberCreator.id = actions.idMemberCreator ```  ``` checklists.memberships.idMember = actions.idMemberCreator ```  ``` checklists.checkItems.idMember = actions.data.idMember ```  ``` checklists.idMemberCreator = actions.data.idMember ```  ``` checklists.memberCreator.id = actions.data.idMember ```  ``` checklists.memberships.idMember = actions.data.idMember ```  ``` checklists.checkItems.idMember = actions.data.idMemberAdded ```  ``` checklists.idMemberCreator = actions.data.idMemberAdded ```  ``` checklists.memberCreator.id = actions.data.idMemberAdded ```  ``` checklists.memberships.idMember = actions.data.idMemberAdded ```  ``` checklists.checkItems.idMember = actions.data.idMemberInviter ```  ``` checklists.idMemberCreator = actions.data.idMemberInviter ```  ``` checklists.memberCreator.id = actions.data.idMemberInviter ```  ``` checklists.memberships.idMember = actions.data.idMemberInviter ```  ``` checklists.checkItems.idMember = actions.data.card.idMembers ```  ``` checklists.idMemberCreator = actions.data.card.idMembers ```  ``` checklists.memberCreator.id = actions.data.card.idMembers ```  ``` checklists.memberships.idMember = actions.data.card.idMembers ```  ``` checklists.checkItems.idMember = actions.data.member.id ```  ``` checklists.idMemberCreator = actions.data.member.id ```  ``` checklists.memberCreator.id = actions.data.member.id ```  ``` checklists.memberships.idMember = actions.data.member.id ```  ``` checklists.checkItems.idMember = actions.data.old.idMembers ```  ``` checklists.idMemberCreator = actions.data.old.idMembers ```  ``` checklists.memberCreator.id = actions.data.old.idMembers ```  ``` checklists.memberships.idMember = actions.data.old.idMembers ```  ``` checklists.checkItems.idMember = actions.member.id ```  ``` checklists.idMemberCreator = actions.member.id ```  ``` checklists.memberCreator.id = actions.member.id ```  ``` checklists.memberships.idMember = actions.member.id ```  ``` checklists.checkItems.idMember = actions.memberCreator.id ```  ``` checklists.idMemberCreator = actions.memberCreator.id ```  ``` checklists.memberCreator.id = actions.memberCreator.id ```  ``` checklists.memberships.idMember = actions.memberCreator.id ``` |
| [cards](#cards) | ``` checklists.data.board.id = cards.idBoard ```  ``` checklists.idBoard = cards.idBoard ```  ``` checklists.data.board.id = cards.labels.idBoard ```  ``` checklists.idBoard = cards.labels.idBoard ```  ``` checklists.idCard = cards.id ```  ``` checklists.data.card.id = cards.id ```  ``` checklists.id = cards.idChecklists ```  ``` checklists.checkItems.idChecklist = cards.idChecklists ```  ``` checklists.data.checklist.id = cards.idChecklists ```  ``` checklists.idList = cards.idList ```  ``` checklists.data.list.id = cards.idList ```  ``` checklists.checkItems.idMember = cards.idMembers ```  ``` checklists.idMemberCreator = cards.idMembers ```  ``` checklists.memberCreator.id = cards.idMembers ```  ``` checklists.memberships.idMember = cards.idMembers ```  ``` checklists.checkItems.idMember = cards.idMembersVoted ```  ``` checklists.idMemberCreator = cards.idMembersVoted ```  ``` checklists.memberCreator.id = cards.idMembersVoted ```  ``` checklists.memberships.idMember = cards.idMembersVoted ``` |
| [lists](#lists) | ``` checklists.data.board.id = lists.idBoard ```  ``` checklists.idBoard = lists.idBoard ```  ``` checklists.idList = lists.id ```  ``` checklists.data.list.id = lists.id ``` |
| [users](#users) | ``` checklists.data.board.id = users.boardId ```  ``` checklists.idBoard = users.boardId ```  ``` checklists.checkItems.idMember = users.id ```  ``` checklists.idMemberCreator = users.id ```  ``` checklists.memberCreator.id = users.id ```  ``` checklists.memberships.idMember = users.id ``` |

checklists table schema

|  |
| --- |
| **badges**  OBJECT This is a nested data structure:   - attachments: INTEGER - attachmentsByType: OBJECT, which is also a nested data structure.   - trello: OBJECT, which is also a nested data structure.     - board: INTEGER     - card: INTEGER - checkItems: INTEGER - checkItemsChecked: INTEGER - checkItemsEarliestDue: STRING - comments: INTEGER - description: BOOLEAN - due: STRING - dueComplete: BOOLEAN - fogbugz: STRING - location: BOOLEAN - subscribed: BOOLEAN - viewingMemberVoted: BOOLEAN - votes: INTEGER |
| **checkItemStates**  STRING |
| **checkItems**  ARRAY This is a nested data structure:   - creationMethod: STRING - due: STRING - id: STRING - idChecklist: STRING - idMember: STRING - name: STRING - nameData: STRING - pos: NUMBER - state: STRING - type: STRING |
| **closed**  BOOLEAN |
| **cover**  OBJECT This is a nested data structure. |
| **creationMethod**  STRING |
| **data**  OBJECT This is a nested data structure:   - board: OBJECT, which is also a nested data structure.   - id: STRING   - name: STRING   - prefs: OBJECT, which is also a nested data structure.     - permissionLevel: STRING     - selfJoin: BOOLEAN   - shortLink: STRING - card: OBJECT, which is also a nested data structure.   - closed: BOOLEAN   - due: STRING   - dueComplete: BOOLEAN   - id: STRING   - idShort: INTEGER   - name: STRING   - shortLink: STRING - checklist: OBJECT, which is also a nested data structure.   - id: STRING   - name: STRING - creationMethod: STRING - list: OBJECT, which is also a nested data structure.   - id: STRING   - name: STRING - old: OBJECT, which is also a nested data structure.   - closed: BOOLEAN   - due: STRING   - dueComplete: BOOLEAN   - name: STRING   - prefs: OBJECT, which is also a nested data structure.     - permissionLevel: STRING     - selfJoin: BOOLEAN - organization: OBJECT, which is also a nested data structure.   - id: STRING   - name: STRING |
| **date**  STRING |
| **dateLastActivity**  STRING |
| **dateLastView**  STRING |
| **datePluginDisable**  STRING |
| **desc**  STRING |
| **descData**  STRING |
| **due**  STRING |
| **dueComplete**  BOOLEAN |
| **dueReminder**  STRING |
| **enterpriseOwned**  BOOLEAN |
| **fullName**  STRING |
| **id**  STRING |
| **idAttachmentCover**  STRING |
| **idBoard**  STRING |
| **idBoardSource**  STRING |
| **idCard**  STRING |
| **idChecklists**  ARRAY This is a nested data structure. |
| **idEnterprise**  STRING |
| **idList**  STRING |
| **idMemberCreator**  STRING |
| **idOrganization**  STRING |
| **idShort**  INTEGER |
| **isTemplate**  BOOLEAN |
| **ixUpdate**  STRING |
| **labelNames**  OBJECT This is a nested data structure:   - black: STRING - blue: STRING - green: STRING - lime: STRING - orange: STRING - pink: STRING - purple: STRING - red: STRING - sky: STRING - yellow: STRING |
| **limits**  OBJECT This is a nested data structure:   - checkItems: OBJECT, which is also a nested data structure.   - perChecklist: OBJECT, which is also a nested data structure.     - disableAt: INTEGER     - status: STRING     - warnAt: INTEGER |
| **manualCoverAttachment**  BOOLEAN |
| **memberCreator**  OBJECT This is a nested data structure:   - activityBlocked: BOOLEAN - avatarHash: STRING - avatarUrl: STRING - fullName: STRING - id: STRING - idMemberReferrer: STRING - initials: STRING - nonPublicAvailable: BOOLEAN - username: STRING |
| **memberships**  ARRAY This is a nested data structure:   - deactivated: BOOLEAN - id: STRING - idMember: STRING - memberType: STRING - unconfirmed: BOOLEAN |
| **name**  STRING |
| **pinned**  STRING |
| **pos**  NUMBER |
| **prefs**  OBJECT This is a nested data structure:   - background: STRING - backgroundBottomColor: STRING - backgroundBrightness: STRING - backgroundColor: STRING - backgroundImage: STRING - backgroundImageScaled: ARRAY, which is also a nested data structure.   - height: INTEGER   - url: STRING   - width: INTEGER - backgroundTile: BOOLEAN - backgroundTopColor: STRING - calendarFeedEnabled: BOOLEAN - canBeEnterprise: BOOLEAN - canBeOrg: BOOLEAN - canBePrivate: BOOLEAN - canBePublic: BOOLEAN - canInvite: BOOLEAN - cardAging: STRING - cardCovers: BOOLEAN - comments: STRING - hideVotes: BOOLEAN - invitations: STRING - isTemplate: BOOLEAN - permissionLevel: STRING - selfJoin: BOOLEAN - voting: STRING |
| **shortLink**  STRING |
| **shortUrl**  STRING |
| **softLimit**  STRING |
| **starred**  BOOLEAN |
| **subscribed**  BOOLEAN |
| **templateGallery**  STRING |
| **type**  STRING |
| **url**  STRING |
| **username**  STRING |

### lists

The lists table contains info about lists on boards that the [authorizing user](#data-replication-board-membership) is a member of.

**Note**: To replicate this table, the [boards](#boards) table must be set to replicate.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Trello API method](https://developer.atlassian.com/cloud/trello/rest/api-group-boards/#api-boards-id-lists-get "Opens in new tab: Trello API method") |

lists table foreign keys

| Join lists with | on |
| --- | --- |
| [boards](#boards) | ``` lists.idBoard = boards.id ``` |
| [actions](#actions) | ``` lists.idBoard = actions.data.board.id ```  ``` lists.id = actions.data.card.idList ```  ``` lists.id = actions.data.list.id ```  ``` lists.id = actions.data.listAfter.id ```  ``` lists.id = actions.data.listBefore.id ```  ``` lists.id = actions.data.old.idList ``` |
| [cards](#cards) | ``` lists.idBoard = cards.idBoard ```  ``` lists.idBoard = cards.labels.idBoard ```  ``` lists.id = cards.idList ``` |
| [checklists](#checklists) | ``` lists.idBoard = checklists.data.board.id ```  ``` lists.idBoard = checklists.idBoard ```  ``` lists.id = checklists.idList ```  ``` lists.id = checklists.data.list.id ``` |
| [users](#users) | ``` lists.idBoard = users.boardId ``` |

lists table schema

|  |
| --- |
| **closed**  BOOLEAN |
| **id**  STRING |
| **idBoard**  STRING |
| **name**  STRING |
| **pos**  NUMBER |
| **softLimit**  INTEGER |
| **subscribed**  BOOLEAN |

### board\_memberships

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | id  boardId |
| **Useful links** | [Trello API method](https://developer.atlassian.com/cloud/trello/rest/api-group-boards/#api-boards-id-memberships-get "Opens in new tab: Trello API method") |

### board\_custom\_fields

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | id  boardId |
| **Useful links** | [Trello API method](https://developer.atlassian.com/cloud/trello/rest/api-group-boards/#api-boards-id-customfields-get "Opens in new tab: Trello API method") |

### board\_labels

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | id  boardId |
| **Useful links** | [Trello API method](https://developer.atlassian.com/cloud/trello/rest/api-group-boards/#api-boards-id-labels-get "Opens in new tab: Trello API method") |

### card\_attachments

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | id  card\_id |
| **Useful links** | [Trello API method](https://developer.atlassian.com/cloud/trello/rest/api-group-cards/#api-cards-id-attachments-get "Opens in new tab: Trello API method") |

### card\_custom\_field\_items

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | id  card\_id |
| **Useful links** | [Trello API method](https://developer.atlassian.com/cloud/trello/rest/api-group-cards/#api-cards-id-customfielditems-get "Opens in new tab: Trello API method") |

### members

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | id |
| **Useful links** | [Trello API method](https://developer.atlassian.com/cloud/trello/rest/api-group-members/#api-members-id-get "Opens in new tab: Trello API method") |

### organizations

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | id |
| **Useful links** | [Trello API method](https://developer.atlassian.com/cloud/trello/rest/api-group-organizations/#api-organizations-id-get "Opens in new tab: Trello API method") |

### organization\_actions

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | id  organization\_id |
| **Useful links** | [Trello API method](https://developer.atlassian.com/cloud/trello/rest/api-group-organizations/#api-organizations-id-actions-get "Opens in new tab: Trello API method") |

### organization\_members

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | id  organization\_id |
| **Useful links** | [Trello API method](https://developer.atlassian.com/cloud/trello/rest/api-group-organizations/#api-organizations-id-members-get "Opens in new tab: Trello API method") |

### organization\_memberships

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | id  organization\_id |
| **Useful links** | [Trello API method](https://developer.atlassian.com/cloud/trello/rest/api-group-organizations/#api-organizations-id-memberships-get "Opens in new tab: Trello API method") |

### users

The users table contains information about users who are members of boards that the [authorizing user](#data-replication-board-membership) is also a member of.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | id  board id |
| **Useful links** | [Trello API method](https://developer.atlassian.com/cloud/trello/rest/api-group-boards/#api-boards-id-members-get "Opens in new tab: Trello API method") |

users table foreign keys

| Join users with | on |
| --- | --- |
| [boards](#boards) | ``` users.boardId = boards.id ```  ``` users.id = boards.memberships.idMember ``` |
| [actions](#actions) | ``` users.boardId = actions.data.board.id ```  ``` users.id = actions.idMemberCreator ```  ``` users.id = actions.data.idMember ```  ``` users.id = actions.data.idMemberAdded ```  ``` users.id = actions.data.idMemberInviter ```  ``` users.id = actions.data.card.idMembers ```  ``` users.id = actions.data.member.id ```  ``` users.id = actions.data.old.idMembers ```  ``` users.id = actions.member.id ```  ``` users.id = actions.memberCreator.id ``` |
| [cards](#cards) | ``` users.boardId = cards.idBoard ```  ``` users.boardId = cards.labels.idBoard ```  ``` users.id = cards.idMembers ```  ``` users.id = cards.idMembersVoted ``` |
| [checklists](#checklists) | ``` users.boardId = checklists.data.board.id ```  ``` users.boardId = checklists.idBoard ```  ``` users.id = checklists.checkItems.idMember ```  ``` users.id = checklists.idMemberCreator ```  ``` users.id = checklists.memberCreator.id ```  ``` users.id = checklists.memberships.idMember ``` |
| [lists](#lists) | ``` users.boardId = lists.idBoard ``` |

users table schema

|  |
| --- |
| **boardId**  STRING |
| **fullName**  STRING |
| **id**  STRING |
| **username**  STRING |
