---
title: "Jira"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Jira-v2.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Jira

Jira is a cloud-based platform that allows bug tracking and agile project management.

Jira integration replicates data from a Jira Cloud instance using the [Jira Cloud REST API v2](https://developer.atlassian.com/cloud/jira/platform/rest/v2/intro/#about).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To set up a Jira connection in Qlik Talend Cloud, you need:

- **Jira permissions**

  Qlik Talend Cloud can replicate only the Jira data that you can access (for example, issues, projects, and worklogs). If you cannot access specific records, Qlik Talend Cloud cannot replicate them. For more information, see
  [Jira permission schemes](https://support.atlassian.com/jira-cloud-administration/docs/what-are-permission-schemes-in-jira/#Managingprojectpermissions-permission_schemes).
- **Supported date locales**

  Records that use date formats from the following locales are skipped:

  - Hungarian (Hungary): Magyar
  - Italian (Italy): Italiano
  - Japanese (Japan): 日本語 (日本)
  - Korean (South Korea): 한국어 (대한민국)
  - Polish (Poland): Polski
  - Thai (Thailand): ภาษาไทย
  - Turkish (Turkey): Türkçe
  - Chinese (China): 中文 (简体)
  - Chinese (Taiwan): 中文 (繁體)
  - Portuguese (Brazil): português (Brasil)
  - Portuguese (Portugal): Português (Portugal)
  - Vietnamese (Vietnam): Tiếng Việt

To generate your API token:

1. Log into your [Jira](https://id.atlassian.com/login) account.
2. Navigate to User menu > Account settings > Security > Create and manage API tokens.
3. Click Create API token.
4. Enter a name for your new API token.
5. Click Create.
6. Copy and paste your API token into a secured file.

Before connecting to a self-managed (hosted) Jira instance, verify the following.

- Your Jira server must use `HTTPS`. Qlik Talend Cloud does not support HTTP for security reasons. If the Jira base URL you enter in Qlik Talend Cloud does not use HTTPS, the connection will fail.
- If your Jira instance is behind a firewall, allowlist Qlik Talend Cloud IP addresses so Qlik Talend Cloud can access the instance. For the current list, see
  [Allowlisting domains and IP addresses](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/qlik-cloud-dns-ip.htm).

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
| Base URL | The base URL is the main address of your Jira instance. Enter the URL you use to open Jira in a browser, for example https://yourcompany.atlassian.net. |
| Username or Email | Enter your email or username. |
| Password or Token | Enter your password or your generated token. When your Jira instance is cloud-hosted, use an API token. |
| Groups | Optional. User groups to include in replication. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### changelogs

The `changelogs` table contains info about the changelogs associated with an issue.

**Note**: Due to a Jira limitation in the endpoint this connector uses to replicate changelogs, only the 100 most recent changelogs for any individual issue can be replicated. Refer to [Jira documentation](https://confluence.atlassian.com/jirakb/jira-cloud-rest-api-limits-the-number-of-changelogs-returned-938840277.html) for more info.

#### Replication requirements

To replicate this data:

1. The [`issues`](#issues) table must also be set to replicate. **Note**: When an issue is updated, all available changelogs for that issue will also be replicated.
2. The `Browse Projects` [project Jira permission](https://confluence.atlassian.com/adminjiracloud/managing-project-permissions-776636362.html) is required.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Jira API method](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/#api-rest-api-3-issue-issueidorkey-changelog-get "Opens in new tab: Jira API method") |

changelogs table foreign keys

| Join changelogs with | on |
| --- | --- |
| [issue\_comments](#issue-comments) | ``` changelogs.issueId = issue_comments.issueId ```  ``` changelogs.author.accountId = issue_comments.author.accountId ```  ``` changelogs.author.accountId = issue_comments.updateAuthor.accountId ``` |
| [issue\_transitions](#issue-transitions) | ``` changelogs.issueId = issue_transitions.issueId ``` |
| [issues](#issues) | ``` changelogs.issueId = issues.id ```  ``` changelogs.author.accountId = issues.fields.attachment.author.accountId ``` |
| [worklogs](#worklogs) | ``` changelogs.issueId = worklogs.issueId ```  ``` changelogs.author.accountId = worklogs.author.accountId ```  ``` changelogs.author.accountId = worklogs.updateAuthor.accountId ``` |
| [components](#components) | ``` changelogs.author.accountId = components.assignee.accountId ```  ``` changelogs.author.accountId = components.componentBean.assignee.accountId ```  ``` changelogs.author.accountId = components.componentBean.lead.accountId ```  ``` changelogs.author.accountId = components.componentBean.realAssignee.accountId ```  ``` changelogs.author.accountId = components.lead.accountId ```  ``` changelogs.author.accountId = components.realAssignee.accountId ``` |
| [projects](#projects) | ``` changelogs.author.accountId = projects.components.assignee.accountId ```  ``` changelogs.author.accountId = projects.components.lead.accountId ```  ``` changelogs.author.accountId = projects.components.realAssignee.accountId ```  ``` changelogs.author.accountId = projects.lead.accountId ``` |
| [users](#users) | ``` changelogs.author.accountId = users.accountId ``` |

changelogs table schema

|  |
| --- |
| **author**  OBJECT This is a nested data structure:   - accountId: STRING - active: BOOLEAN - avatarUrls: OBJECT, which is also a nested data structure. - displayName: STRING - emailAddress: STRING - key: STRING - name: STRING - self: STRING - timeZone: STRING |
| **created**  DATE-TIME |
| **historyMetadata**  OBJECT This is a nested data structure:   - activityDescription: STRING - activityDescriptionKey: STRING - actor: OBJECT, which is also a nested data structure.   - avatarUrl: STRING   - displayName: STRING   - displayNameKey: STRING   - id: STRING   - type: STRING   - url: STRING - cause: OBJECT, which is also a nested data structure.   - avatarUrl: STRING   - displayName: STRING   - displayNameKey: STRING   - id: STRING   - type: STRING   - url: STRING - description: STRING - descriptionKey: STRING - emailDescription: STRING - emailDescriptionKey: STRING - extraData: OBJECT, which is also a nested data structure. - generator: OBJECT, which is also a nested data structure.   - avatarUrl: STRING   - displayName: STRING   - displayNameKey: STRING   - id: STRING   - type: STRING   - url: STRING - type: STRING |
| **id**  STRING |
| **issueId**  STRING |
| **items**  ARRAY This is a nested data structure:   - field: STRING - fieldId: STRING - fieldtype: STRING - from: STRING - fromString: STRING - to: STRING - toString: STRING |

### components

The `components` table contains info about components in projects in your JIRA account.

#### Replication requirements

**Note**: To replicate this data:

1. The [`projects`](#projects) table must also be set to replicate, and
2. The `Browse Projects` [project Jira permission](https://confluence.atlassian.com/adminjiracloud/managing-project-permissions-776636362.html) is required.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [JIRA API method](https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-project-components/#api-rest-api-2-project-projectidorkey-component-get "Opens in new tab: JIRA API method") |

components table foreign keys

| Join components with | on |
| --- | --- |
| [projects](#projects) | ``` components.componentBean.projectId = projects.id ```  ``` components.projectId = projects.id ```  ``` components.assignee.accountId = projects.components.assignee.accountId ```  ``` components.componentBean.assignee.accountId = projects.components.assignee.accountId ```  ``` components.componentBean.lead.accountId = projects.components.assignee.accountId ```  ``` components.componentBean.realAssignee.accountId = projects.components.assignee.accountId ```  ``` components.lead.accountId = projects.components.assignee.accountId ```  ``` components.realAssignee.accountId = projects.components.assignee.accountId ```  ``` components.assignee.accountId = projects.components.lead.accountId ```  ``` components.componentBean.assignee.accountId = projects.components.lead.accountId ```  ``` components.componentBean.lead.accountId = projects.components.lead.accountId ```  ``` components.componentBean.realAssignee.accountId = projects.components.lead.accountId ```  ``` components.lead.accountId = projects.components.lead.accountId ```  ``` components.realAssignee.accountId = projects.components.lead.accountId ```  ``` components.assignee.accountId = projects.components.realAssignee.accountId ```  ``` components.componentBean.assignee.accountId = projects.components.realAssignee.accountId ```  ``` components.componentBean.lead.accountId = projects.components.realAssignee.accountId ```  ``` components.componentBean.realAssignee.accountId = projects.components.realAssignee.accountId ```  ``` components.lead.accountId = projects.components.realAssignee.accountId ```  ``` components.realAssignee.accountId = projects.components.realAssignee.accountId ```  ``` components.assignee.accountId = projects.lead.accountId ```  ``` components.componentBean.assignee.accountId = projects.lead.accountId ```  ``` components.componentBean.lead.accountId = projects.lead.accountId ```  ``` components.componentBean.realAssignee.accountId = projects.lead.accountId ```  ``` components.lead.accountId = projects.lead.accountId ```  ``` components.realAssignee.accountId = projects.lead.accountId ``` |
| [versions](#versions) | ``` components.componentBean.projectId = versions.projectId ```  ``` components.projectId = versions.projectId ``` |
| [changelogs](#changelogs) | ``` components.assignee.accountId = changelogs.author.accountId ```  ``` components.componentBean.assignee.accountId = changelogs.author.accountId ```  ``` components.componentBean.lead.accountId = changelogs.author.accountId ```  ``` components.componentBean.realAssignee.accountId = changelogs.author.accountId ```  ``` components.lead.accountId = changelogs.author.accountId ```  ``` components.realAssignee.accountId = changelogs.author.accountId ``` |
| [issue\_comments](#issue-comments) | ``` components.assignee.accountId = issue_comments.author.accountId ```  ``` components.componentBean.assignee.accountId = issue_comments.author.accountId ```  ``` components.componentBean.lead.accountId = issue_comments.author.accountId ```  ``` components.componentBean.realAssignee.accountId = issue_comments.author.accountId ```  ``` components.lead.accountId = issue_comments.author.accountId ```  ``` components.realAssignee.accountId = issue_comments.author.accountId ```  ``` components.assignee.accountId = issue_comments.updateAuthor.accountId ```  ``` components.componentBean.assignee.accountId = issue_comments.updateAuthor.accountId ```  ``` components.componentBean.lead.accountId = issue_comments.updateAuthor.accountId ```  ``` components.componentBean.realAssignee.accountId = issue_comments.updateAuthor.accountId ```  ``` components.lead.accountId = issue_comments.updateAuthor.accountId ```  ``` components.realAssignee.accountId = issue_comments.updateAuthor.accountId ``` |
| [issues](#issues) | ``` components.assignee.accountId = issues.fields.attachment.author.accountId ```  ``` components.componentBean.assignee.accountId = issues.fields.attachment.author.accountId ```  ``` components.componentBean.lead.accountId = issues.fields.attachment.author.accountId ```  ``` components.componentBean.realAssignee.accountId = issues.fields.attachment.author.accountId ```  ``` components.lead.accountId = issues.fields.attachment.author.accountId ```  ``` components.realAssignee.accountId = issues.fields.attachment.author.accountId ``` |
| [users](#users) | ``` components.assignee.accountId = users.accountId ```  ``` components.componentBean.assignee.accountId = users.accountId ```  ``` components.componentBean.lead.accountId = users.accountId ```  ``` components.componentBean.realAssignee.accountId = users.accountId ```  ``` components.lead.accountId = users.accountId ```  ``` components.realAssignee.accountId = users.accountId ``` |
| [worklogs](#worklogs) | ``` components.assignee.accountId = worklogs.author.accountId ```  ``` components.componentBean.assignee.accountId = worklogs.author.accountId ```  ``` components.componentBean.lead.accountId = worklogs.author.accountId ```  ``` components.componentBean.realAssignee.accountId = worklogs.author.accountId ```  ``` components.lead.accountId = worklogs.author.accountId ```  ``` components.realAssignee.accountId = worklogs.author.accountId ```  ``` components.assignee.accountId = worklogs.updateAuthor.accountId ```  ``` components.componentBean.assignee.accountId = worklogs.updateAuthor.accountId ```  ``` components.componentBean.lead.accountId = worklogs.updateAuthor.accountId ```  ``` components.componentBean.realAssignee.accountId = worklogs.updateAuthor.accountId ```  ``` components.lead.accountId = worklogs.updateAuthor.accountId ```  ``` components.realAssignee.accountId = worklogs.updateAuthor.accountId ``` |

components table schema

|  |
| --- |
| **assignee**  OBJECT This is a nested data structure:   - accountId: STRING - active: BOOLEAN - avatarUrls: OBJECT, which is also a nested data structure.   - 16x16: STRING   - 24x24: STRING   - 32x32: STRING   - 48x48: STRING - displayName: STRING - self: STRING |
| **assigneeType**  STRING |
| **componentBean**  OBJECT This is a nested data structure:   - assignee: OBJECT, which is also a nested data structure.   - accountId: STRING   - active: BOOLEAN   - avatarUrls: OBJECT, which is also a nested data structure.     - 16x16: STRING     - 24x24: STRING     - 32x32: STRING     - 48x48: STRING   - displayName: STRING   - self: STRING - assigneeType: STRING - description: STRING - id: STRING - isAssigneeTypeValid: BOOLEAN - lead: OBJECT, which is also a nested data structure.   - accountId: STRING   - active: BOOLEAN   - avatarUrls: OBJECT, which is also a nested data structure.     - 16x16: STRING     - 24x24: STRING     - 32x32: STRING     - 48x48: STRING   - displayName: STRING   - self: STRING - name: STRING - project: STRING - projectId: INTEGER - realAssignee: OBJECT, which is also a nested data structure.   - accountId: STRING   - active: BOOLEAN   - avatarUrls: OBJECT, which is also a nested data structure.     - 16x16: STRING     - 24x24: STRING     - 32x32: STRING     - 48x48: STRING   - displayName: STRING   - self: STRING - realAssigneeType: STRING - self: STRING |
| **description**  STRING |
| **id**  STRING |
| **isAssigneeTypeValid**  BOOLEAN |
| **issueCount**  INTEGER |
| **lead**  OBJECT This is a nested data structure:   - accountId: STRING - active: BOOLEAN - avatarUrls: OBJECT, which is also a nested data structure.   - 16x16: STRING   - 24x24: STRING   - 32x32: STRING   - 48x48: STRING - displayName: STRING - self: STRING |
| **name**  STRING |
| **project**  STRING |
| **projectId**  INTEGER |
| **realAssignee**  OBJECT This is a nested data structure:   - accountId: STRING - active: BOOLEAN - avatarUrls: OBJECT, which is also a nested data structure.   - 16x16: STRING   - 24x24: STRING   - 32x32: STRING   - 48x48: STRING - displayName: STRING - self: STRING |
| **realAssigneeType**  STRING |
| **self**  STRING |

### group\_users

The `group_users` table contains the list of all users in a group. Users are ordered by username. Due to privacy reasons, the Jira API does not return the username in the results.

#### Replication requirements

**Note**: To replicate this data:

1. The [`groups`](#groups) table must also be set to replicate.
2. The `Browse users and groups` [global Jira permission](https://confluence.atlassian.com/adminjiracloud/managing-global-permissions-776636359.html) is required.
3. The `Administer Jira` [global Jira permission](https://confluence.atlassian.com/adminjiracloud/managing-global-permissions-776636359.html) is required.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | groupId, accountId |
| **Useful links** | [JIRA API method](https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-groups/#api-rest-api-2-group-member-get "Opens in new tab: JIRA API method") |

### groups

The `groups` table contains the list of groups found in your JIRA account.

**Note**: To replicate this data, the `Browse users and groups` [global Jira permission](https://confluence.atlassian.com/adminjiracloud/managing-global-permissions-776636359.html) is required.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | groupId |
| **Useful links** | [JIRA API method](https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-groups/#api-rest-api-2-group-bulk-get "Opens in new tab: JIRA API method") |

### issue\_comments

The `issue_comments` table contains info about comments made on issues.

#### Replication requirements

To replicate this data:

1. The [`issues`](#issues) table must also be set to replicate. **Note**: When an issue is updated, all the comments for that issue will also be replicated.
2. The `Browse Projects` [project Jira permission](https://confluence.atlassian.com/adminjiracloud/managing-project-permissions-776636362.html) is required.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [JIRA API method](https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-issue-comments/#api-group-issue-comments "Opens in new tab: JIRA API method") |

issue\_comments table foreign keys

| Join issue\_comments with | on |
| --- | --- |
| [changelogs](#changelogs) | ``` issue_comments.issueId = changelogs.issueId ```  ``` issue_comments.author.accountId = changelogs.author.accountId ```  ``` issue_comments.updateAuthor.accountId = changelogs.author.accountId ``` |
| [issue\_transitions](#issue-transitions) | ``` issue_comments.issueId = issue_transitions.issueId ``` |
| [issues](#issues) | ``` issue_comments.issueId = issues.id ```  ``` issue_comments.author.accountId = issues.fields.attachment.author.accountId ```  ``` issue_comments.updateAuthor.accountId = issues.fields.attachment.author.accountId ``` |
| [worklogs](#worklogs) | ``` issue_comments.issueId = worklogs.issueId ```  ``` issue_comments.author.accountId = worklogs.author.accountId ```  ``` issue_comments.updateAuthor.accountId = worklogs.author.accountId ```  ``` issue_comments.author.accountId = worklogs.updateAuthor.accountId ```  ``` issue_comments.updateAuthor.accountId = worklogs.updateAuthor.accountId ``` |
| [components](#components) | ``` issue_comments.author.accountId = components.assignee.accountId ```  ``` issue_comments.updateAuthor.accountId = components.assignee.accountId ```  ``` issue_comments.author.accountId = components.componentBean.assignee.accountId ```  ``` issue_comments.updateAuthor.accountId = components.componentBean.assignee.accountId ```  ``` issue_comments.author.accountId = components.componentBean.lead.accountId ```  ``` issue_comments.updateAuthor.accountId = components.componentBean.lead.accountId ```  ``` issue_comments.author.accountId = components.componentBean.realAssignee.accountId ```  ``` issue_comments.updateAuthor.accountId = components.componentBean.realAssignee.accountId ```  ``` issue_comments.author.accountId = components.lead.accountId ```  ``` issue_comments.updateAuthor.accountId = components.lead.accountId ```  ``` issue_comments.author.accountId = components.realAssignee.accountId ```  ``` issue_comments.updateAuthor.accountId = components.realAssignee.accountId ``` |
| [projects](#projects) | ``` issue_comments.author.accountId = projects.components.assignee.accountId ```  ``` issue_comments.updateAuthor.accountId = projects.components.assignee.accountId ```  ``` issue_comments.author.accountId = projects.components.lead.accountId ```  ``` issue_comments.updateAuthor.accountId = projects.components.lead.accountId ```  ``` issue_comments.author.accountId = projects.components.realAssignee.accountId ```  ``` issue_comments.updateAuthor.accountId = projects.components.realAssignee.accountId ```  ``` issue_comments.author.accountId = projects.lead.accountId ```  ``` issue_comments.updateAuthor.accountId = projects.lead.accountId ``` |
| [users](#users) | ``` issue_comments.author.accountId = users.accountId ```  ``` issue_comments.updateAuthor.accountId = users.accountId ``` |

issue\_comments table schema

|  |
| --- |
| **author**  OBJECT This is a nested data structure:   - accountId: STRING - active: BOOLEAN - avatarUrls: OBJECT, which is also a nested data structure. - displayName: STRING - emailAddress: STRING - key: STRING - name: STRING - self: STRING - timeZone: STRING |
| **body**  STRING |
| **created**  DATE-TIME |
| **id**  STRING |
| **issueId**  STRING |
| **jsdPublic**  BOOLEAN |
| **properties**  ARRAY This is a nested data structure:   - key: STRING |
| **renderedBody**  STRING |
| **self**  STRING |
| **updateAuthor**  OBJECT This is a nested data structure:   - accountId: STRING - active: BOOLEAN - avatarUrls: OBJECT, which is also a nested data structure. - displayName: STRING - emailAddress: STRING - key: STRING - name: STRING - self: STRING - timeZone: STRING |
| **updated**  DATE-TIME |
| **visibility**  OBJECT This is a nested data structure:   - type: STRING - value: STRING |

### issue\_transitions

The `issue_transitions` table contains info about issue transitions.

#### Replication requirements

To replicate this data:

1. The [`issues`](#issues) table must also be set to replicate. **Note**: When an issue is updated, all the transitions for that issue will also be replicated.
2. The `Browse Projects` [project Jira permission](https://confluence.atlassian.com/adminjiracloud/managing-project-permissions-776636362.html) is required.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Loading Behavior** | Append-Only |
| **Primary Key** | id |
| **Useful links** | [JIRA API method](https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-issues/#api-rest-api-2-issue-issueidorkey-transitions-get "Opens in new tab: JIRA API method") |

issue\_transitions table foreign keys

| Join issue\_transitions with | on |
| --- | --- |
| [changelogs](#changelogs) | ``` issue_transitions.issueId = changelogs.issueId ``` |
| [issue\_comments](#issue-comments) | ``` issue_transitions.issueId = issue_comments.issueId ``` |
| [issues](#issues) | ``` issue_transitions.issueId = issues.id ``` |
| [worklogs](#worklogs) | ``` issue_transitions.issueId = worklogs.issueId ``` |

issue\_transitions table schema

|  |
| --- |
| **expand**  STRING |
| **fields**  OBJECT This is a nested data structure. |
| **hasScreen**  BOOLEAN |
| **id**  STRING |
| **isConditional**  BOOLEAN |
| **isGlobal**  BOOLEAN |
| **isInitial**  BOOLEAN |
| **issueId**  STRING |
| **name**  STRING |
| **to**  OBJECT This is a nested data structure:   - description: STRING - iconUrl: STRING - id: STRING - name: STRING - self: STRING - statusCategory: OBJECT, which is also a nested data structure.   - colorName: STRING   - id: INTEGER   - key: STRING   - name: STRING   - self: STRING - statusColor: STRING |

### issues

The `issues` table contains info about the issues in your JIRA instance. This table only contains core issue data - some data is located in other tables, such as [`changelogs`](#changelogs), [`issue_comments`](#issue_comments), and [`issue_transitions`](#issue_transitions).

**Note**: To replicate this data, the `Browse projects` [project Jira permission](https://confluence.atlassian.com/adminjiracloud/managing-project-permissions-776636362.html) for the project that the issue is in is required.

#### Identifying deleted issues

When an issue is hard-deleted in JIRA, the record for the issue will remain in your destination. Currently, Jira’s API doesn’t include a way to identify deleted issues.

To identify deleted issues, [Atlassian’s suggested workaround](https://answers.atlassian.com/questions/75537/how-do-i-find-if-an-issue-has-been-deleted) is:

1. Create a status in JIRA that will be applied to issues you want to delete.
2. Before deleting the issue, apply the status.
3. Allow Qlik Talend Cloud to extract and load the updated data into your destination.
4. Delete the issue.
5. After Qlik Talend Cloud finishes loading the data, use the `fields__status__name` field in your queries to filter issues with the deleted status you applied in step 2.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [JIRA documentation](https://docs.atlassian.com/jira/REST/ondemand/#api/2/issue-getIssue)  [JIRA API method](https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-issues/#api-rest-api-2-issue-issueidorkey-get "Opens in new tab: JIRA API method") |

issues table foreign keys

| Join issues with | on |
| --- | --- |
| [changelogs](#changelogs) | ``` issues.id = changelogs.issueId ```  ``` issues.fields.attachment.author.accountId = changelogs.author.accountId ``` |
| [issue\_comments](#issue-comments) | ``` issues.id = issue_comments.issueId ```  ``` issues.fields.attachment.author.accountId = issue_comments.author.accountId ```  ``` issues.fields.attachment.author.accountId = issue_comments.updateAuthor.accountId ``` |
| [issue\_transitions](#issue-transitions) | ``` issues.id = issue_transitions.issueId ``` |
| [worklogs](#worklogs) | ``` issues.id = worklogs.issueId ```  ``` issues.fields.attachment.author.accountId = worklogs.author.accountId ```  ``` issues.fields.attachment.author.accountId = worklogs.updateAuthor.accountId ``` |
| [components](#components) | ``` issues.fields.attachment.author.accountId = components.assignee.accountId ```  ``` issues.fields.attachment.author.accountId = components.componentBean.assignee.accountId ```  ``` issues.fields.attachment.author.accountId = components.componentBean.lead.accountId ```  ``` issues.fields.attachment.author.accountId = components.componentBean.realAssignee.accountId ```  ``` issues.fields.attachment.author.accountId = components.lead.accountId ```  ``` issues.fields.attachment.author.accountId = components.realAssignee.accountId ``` |
| [projects](#projects) | ``` issues.fields.attachment.author.accountId = projects.components.assignee.accountId ```  ``` issues.fields.attachment.author.accountId = projects.components.lead.accountId ```  ``` issues.fields.attachment.author.accountId = projects.components.realAssignee.accountId ```  ``` issues.fields.attachment.author.accountId = projects.lead.accountId ``` |
| [users](#users) | ``` issues.fields.attachment.author.accountId = users.accountId ``` |

issues table schema

|  |
| --- |
| **editmeta**  OBJECT This is a nested data structure:   - fields: OBJECT, which is also a nested data structure. |
| **expand**  STRING |
| **fields**  OBJECT This is a nested data structure:   - attachment: ARRAY, which is also a nested data structure. - created: DATE-TIME - lastViewed: DATE-TIME - updated: DATE-TIME |
| **fieldsToInclude**  OBJECT This is a nested data structure. |
| **id**  STRING |
| **key**  STRING |
| **names**  OBJECT This is a nested data structure. |
| **properties**  OBJECT This is a nested data structure:   - properties: OBJECT, which is also a nested data structure. |
| **renderedFields**  OBJECT This is a nested data structure. |
| **schema**  OBJECT This is a nested data structure. |
| **self**  STRING |
| **versionedRepresentations**  OBJECT This is a nested data structure. |

### project\_categories

The `project_categories` table contains info about project categories.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [JIRA API method](https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-project-categories/#api-group-project-categories "Opens in new tab: JIRA API method") |

project\_categories table foreign keys

| Join project\_categories with | on |
| --- | --- |
| [projects](#projects) | ``` project_categories.id = projects.projectCategory.id ``` |

project\_categories table schema

|  |
| --- |
| **description**  STRING |
| **id**  STRING |
| **name**  STRING |
| **self**  STRING |

### project\_types

The `project_types` table contains info about project types.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | key |
| **Useful links** | [JIRA API method](https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-project-types/#api-group-project-types "Opens in new tab: JIRA API method") |

project\_types table schema

|  |
| --- |
| **color**  STRING |
| **descriptionI18nKey**  STRING |
| **formattedKey**  STRING |
| **icon**  STRING |
| **key**  STRING |

### projects

The `projects` table contains info about projects in your JIRA account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [JIRA documentation](https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-projects/#api-group-projects) |

projects table foreign keys

| Join projects with | on |
| --- | --- |
| [project\_categories](#project-categories) | ``` projects.projectCategory.id = project_categories.id ``` |
| [components](#components) | ``` projects.id = components.componentBean.projectId ```  ``` projects.id = components.projectId ```  ``` projects.components.assignee.accountId = components.assignee.accountId ```  ``` projects.components.lead.accountId = components.assignee.accountId ```  ``` projects.components.realAssignee.accountId = components.assignee.accountId ```  ``` projects.lead.accountId = components.assignee.accountId ```  ``` projects.components.assignee.accountId = components.componentBean.assignee.accountId ```  ``` projects.components.lead.accountId = components.componentBean.assignee.accountId ```  ``` projects.components.realAssignee.accountId = components.componentBean.assignee.accountId ```  ``` projects.lead.accountId = components.componentBean.assignee.accountId ```  ``` projects.components.assignee.accountId = components.componentBean.lead.accountId ```  ``` projects.components.lead.accountId = components.componentBean.lead.accountId ```  ``` projects.components.realAssignee.accountId = components.componentBean.lead.accountId ```  ``` projects.lead.accountId = components.componentBean.lead.accountId ```  ``` projects.components.assignee.accountId = components.componentBean.realAssignee.accountId ```  ``` projects.components.lead.accountId = components.componentBean.realAssignee.accountId ```  ``` projects.components.realAssignee.accountId = components.componentBean.realAssignee.accountId ```  ``` projects.lead.accountId = components.componentBean.realAssignee.accountId ```  ``` projects.components.assignee.accountId = components.lead.accountId ```  ``` projects.components.lead.accountId = components.lead.accountId ```  ``` projects.components.realAssignee.accountId = components.lead.accountId ```  ``` projects.lead.accountId = components.lead.accountId ```  ``` projects.components.assignee.accountId = components.realAssignee.accountId ```  ``` projects.components.lead.accountId = components.realAssignee.accountId ```  ``` projects.components.realAssignee.accountId = components.realAssignee.accountId ```  ``` projects.lead.accountId = components.realAssignee.accountId ``` |
| [versions](#versions) | ``` projects.id = versions.projectId ``` |
| [changelogs](#changelogs) | ``` projects.components.assignee.accountId = changelogs.author.accountId ```  ``` projects.components.lead.accountId = changelogs.author.accountId ```  ``` projects.components.realAssignee.accountId = changelogs.author.accountId ```  ``` projects.lead.accountId = changelogs.author.accountId ``` |
| [issue\_comments](#issue-comments) | ``` projects.components.assignee.accountId = issue_comments.author.accountId ```  ``` projects.components.lead.accountId = issue_comments.author.accountId ```  ``` projects.components.realAssignee.accountId = issue_comments.author.accountId ```  ``` projects.lead.accountId = issue_comments.author.accountId ```  ``` projects.components.assignee.accountId = issue_comments.updateAuthor.accountId ```  ``` projects.components.lead.accountId = issue_comments.updateAuthor.accountId ```  ``` projects.components.realAssignee.accountId = issue_comments.updateAuthor.accountId ```  ``` projects.lead.accountId = issue_comments.updateAuthor.accountId ``` |
| [issues](#issues) | ``` projects.components.assignee.accountId = issues.fields.attachment.author.accountId ```  ``` projects.components.lead.accountId = issues.fields.attachment.author.accountId ```  ``` projects.components.realAssignee.accountId = issues.fields.attachment.author.accountId ```  ``` projects.lead.accountId = issues.fields.attachment.author.accountId ``` |
| [users](#users) | ``` projects.components.assignee.accountId = users.accountId ```  ``` projects.components.lead.accountId = users.accountId ```  ``` projects.components.realAssignee.accountId = users.accountId ```  ``` projects.lead.accountId = users.accountId ``` |
| [worklogs](#worklogs) | ``` projects.components.assignee.accountId = worklogs.author.accountId ```  ``` projects.components.lead.accountId = worklogs.author.accountId ```  ``` projects.components.realAssignee.accountId = worklogs.author.accountId ```  ``` projects.lead.accountId = worklogs.author.accountId ```  ``` projects.components.assignee.accountId = worklogs.updateAuthor.accountId ```  ``` projects.components.lead.accountId = worklogs.updateAuthor.accountId ```  ``` projects.components.realAssignee.accountId = worklogs.updateAuthor.accountId ```  ``` projects.lead.accountId = worklogs.updateAuthor.accountId ``` |

projects table schema

|  |
| --- |
| **assigneeType**  STRING |
| **avatarUrls**  OBJECT This is a nested data structure. |
| **components**  ARRAY This is a nested data structure:   - assignee: OBJECT, which is also a nested data structure.   - accountId: STRING   - active: BOOLEAN   - applicationRoles: OBJECT, which is also a nested data structure.   - avatarUrls: OBJECT, which is also a nested data structure.   - displayName: STRING   - emailAddress: STRING   - expand: STRING   - groups: OBJECT, which is also a nested data structure.   - key: STRING   - locale: STRING   - name: STRING   - self: STRING   - timeZone: STRING - assigneeType: STRING - description: STRING - id: STRING - isAssigneeTypeValid: BOOLEAN - lead: OBJECT, which is also a nested data structure.   - accountId: STRING   - active: BOOLEAN   - applicationRoles: OBJECT, which is also a nested data structure.   - avatarUrls: OBJECT, which is also a nested data structure.   - displayName: STRING   - emailAddress: STRING   - expand: STRING   - groups: OBJECT, which is also a nested data structure.   - key: STRING   - locale: STRING   - name: STRING   - self: STRING   - timeZone: STRING - leadUserName: STRING - name: STRING - project: STRING - projectId: INTEGER - realAssignee: OBJECT, which is also a nested data structure.   - accountId: STRING   - active: BOOLEAN   - applicationRoles: OBJECT, which is also a nested data structure.   - avatarUrls: OBJECT, which is also a nested data structure.   - displayName: STRING   - emailAddress: STRING   - expand: STRING   - groups: OBJECT, which is also a nested data structure.   - key: STRING   - locale: STRING   - name: STRING   - self: STRING   - timeZone: STRING - realAssigneeType: STRING - self: STRING |
| **description**  STRING |
| **email**  STRING |
| **expand**  STRING |
| **id**  STRING |
| **issueTypes**  ARRAY This is a nested data structure:   - avatarId: INTEGER - description: STRING - iconUrl: STRING - id: STRING - name: STRING - self: STRING - subtask: BOOLEAN |
| **key**  STRING |
| **lead**  OBJECT This is a nested data structure:   - accountId: STRING - active: BOOLEAN - applicationRoles: OBJECT, which is also a nested data structure. - avatarUrls: OBJECT, which is also a nested data structure. - displayName: STRING - emailAddress: STRING - expand: STRING - groups: OBJECT, which is also a nested data structure. - key: STRING - locale: STRING - name: STRING - self: STRING - timeZone: STRING |
| **name**  STRING |
| **projectCategory**  OBJECT This is a nested data structure:   - description: STRING - id: STRING - name: STRING - self: STRING |
| **projectKeys**  ARRAY This is a nested data structure. |
| **projectTypeKey**  STRING |
| **roles**  OBJECT This is a nested data structure. |
| **self**  STRING |
| **simplified**  BOOLEAN |
| **url**  STRING |

### resolutions

The `resolutions` table contains info about issue resolutions.

**Note**: To replicate this data, the `Administer Jira` [global Jira permission](https://confluence.atlassian.com/adminjiracloud/managing-global-permissions-776636359.html) is required.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [JIRA API method](https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-issue-resolutions/#api-group-issue-resolutions "Opens in new tab: JIRA API method") |

resolutions table schema

|  |
| --- |
| **description**  STRING |
| **iconUrl**  STRING |
| **id**  STRING |
| **name**  STRING |
| **self**  STRING |

### roles

The `roles` table contains info about the project roles in your JIRA account.

**Note**: To replicate this data, the `Administer Jira` [global Jira permission](https://confluence.atlassian.com/adminjiracloud/managing-global-permissions-776636359.html) is required.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [JIRA API method](https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-project-roles/#api-rest-api-2-role-get "Opens in new tab: JIRA API method") |

roles table schema

|  |
| --- |
| **actors**  ARRAY This is a nested data structure:   - avatarUrl: STRING - displayName: STRING - id: INTEGER - name: STRING - type: STRING |
| **description**  STRING |
| **id**  INTEGER |
| **name**  STRING |
| **self**  STRING |

### users

The `users` table contains info about the users in your JIRA account.

**Note**: To replicate this data, the `Administer Jira` [global Jira permission](https://confluence.atlassian.com/adminjiracloud/managing-global-permissions-776636359.html) is required.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [JIRA API method](https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-users/#api-rest-api-2-user-get "Opens in new tab: JIRA API method") |

users table foreign keys

| Join users with | on |
| --- | --- |
| [changelogs](#changelogs) | ``` users.accountId = changelogs.author.accountId ``` |
| [components](#components) | ``` users.accountId = components.assignee.accountId ```  ``` users.accountId = components.componentBean.assignee.accountId ```  ``` users.accountId = components.componentBean.lead.accountId ```  ``` users.accountId = components.componentBean.realAssignee.accountId ```  ``` users.accountId = components.lead.accountId ```  ``` users.accountId = components.realAssignee.accountId ``` |
| [issue\_comments](#issue-comments) | ``` users.accountId = issue_comments.author.accountId ```  ``` users.accountId = issue_comments.updateAuthor.accountId ``` |
| [issues](#issues) | ``` users.accountId = issues.fields.attachment.author.accountId ``` |
| [projects](#projects) | ``` users.accountId = projects.components.assignee.accountId ```  ``` users.accountId = projects.components.lead.accountId ```  ``` users.accountId = projects.components.realAssignee.accountId ```  ``` users.accountId = projects.lead.accountId ``` |
| [worklogs](#worklogs) | ``` users.accountId = worklogs.author.accountId ```  ``` users.accountId = worklogs.updateAuthor.accountId ``` |

users table schema

|  |
| --- |
| **accountId**  STRING |
| **accountType**  STRING |
| **active**  BOOLEAN |
| **avatarUrls**  OBJECT This is a nested data structure. |
| **displayName**  STRING |
| **emailAddress**  STRING |
| **expand**  STRING |
| **key**  STRING |
| **name**  STRING |
| **self**  STRING |
| **timeZone**  STRING |

### versions

The `versions` table contains info about versions in your JIRA account.

#### Replication requirements

**Note**: To replicate this data:

1. The [`projects`](#projects) table must also be set to replicate, and
2. The `Browse Projects` [project Jira permission](https://confluence.atlassian.com/adminjiracloud/managing-project-permissions-776636362.html) is required.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [JIRA API method](https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-project-versions/#api-rest-api-2-project-projectidorkey-versions-get "Opens in new tab: JIRA API method") |

versions table foreign keys

| Join versions with | on |
| --- | --- |
| [components](#components) | ``` versions.projectId = components.componentBean.projectId ```  ``` versions.projectId = components.projectId ``` |
| [projects](#projects) | ``` versions.projectId = projects.id ``` |

versions table schema

|  |
| --- |
| **archived**  BOOLEAN |
| **description**  STRING |
| **expand**  STRING |
| **id**  STRING |
| **moveUnfixedIssuesTo**  STRING |
| **name**  STRING |
| **operations**  ARRAY This is a nested data structure:   - href: STRING - iconClass: STRING - id: STRING - label: STRING - styleClass: STRING - title: STRING - weight: INTEGER |
| **overdue**  BOOLEAN |
| **project**  STRING |
| **projectId**  INTEGER |
| **releaseDate**  DATE-TIME |
| **released**  BOOLEAN |
| **remotelinks**  ARRAY This is a nested data structure:   - name: STRING - self: STRING |
| **self**  STRING |
| **startDate**  DATE-TIME |
| **userReleaseDate**  DATE-TIME |
| **userStartDate**  DATE-TIME |

### worklogs

The `worklogs` table contains info about the worklogs in your JIRA account.

**Note**: For a worklog to be replicated, it must be set as `Viewable by All Users`, or the integration authenticating user (visible in the integration’s Integration Settings page), must be a member of the project role/group with permission to view the worklog.

If you’re missing worklogs, verify that you have the required permissions to access the worklog.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [JIRA API method](https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-issue-worklogs/#api-rest-api-2-worklog-updated-get "Opens in new tab: JIRA API method") |

worklogs table foreign keys

| Join worklogs with | on |
| --- | --- |
| [changelogs](#changelogs) | ``` worklogs.issueId = changelogs.issueId ```  ``` worklogs.author.accountId = changelogs.author.accountId ```  ``` worklogs.updateAuthor.accountId = changelogs.author.accountId ``` |
| [issue\_comments](#issue-comments) | ``` worklogs.issueId = issue_comments.issueId ```  ``` worklogs.author.accountId = issue_comments.author.accountId ```  ``` worklogs.updateAuthor.accountId = issue_comments.author.accountId ```  ``` worklogs.author.accountId = issue_comments.updateAuthor.accountId ```  ``` worklogs.updateAuthor.accountId = issue_comments.updateAuthor.accountId ``` |
| [issue\_transitions](#issue-transitions) | ``` worklogs.issueId = issue_transitions.issueId ``` |
| [issues](#issues) | ``` worklogs.issueId = issues.id ```  ``` worklogs.author.accountId = issues.fields.attachment.author.accountId ```  ``` worklogs.updateAuthor.accountId = issues.fields.attachment.author.accountId ``` |
| [components](#components) | ``` worklogs.author.accountId = components.assignee.accountId ```  ``` worklogs.updateAuthor.accountId = components.assignee.accountId ```  ``` worklogs.author.accountId = components.componentBean.assignee.accountId ```  ``` worklogs.updateAuthor.accountId = components.componentBean.assignee.accountId ```  ``` worklogs.author.accountId = components.componentBean.lead.accountId ```  ``` worklogs.updateAuthor.accountId = components.componentBean.lead.accountId ```  ``` worklogs.author.accountId = components.componentBean.realAssignee.accountId ```  ``` worklogs.updateAuthor.accountId = components.componentBean.realAssignee.accountId ```  ``` worklogs.author.accountId = components.lead.accountId ```  ``` worklogs.updateAuthor.accountId = components.lead.accountId ```  ``` worklogs.author.accountId = components.realAssignee.accountId ```  ``` worklogs.updateAuthor.accountId = components.realAssignee.accountId ``` |
| [projects](#projects) | ``` worklogs.author.accountId = projects.components.assignee.accountId ```  ``` worklogs.updateAuthor.accountId = projects.components.assignee.accountId ```  ``` worklogs.author.accountId = projects.components.lead.accountId ```  ``` worklogs.updateAuthor.accountId = projects.components.lead.accountId ```  ``` worklogs.author.accountId = projects.components.realAssignee.accountId ```  ``` worklogs.updateAuthor.accountId = projects.components.realAssignee.accountId ```  ``` worklogs.author.accountId = projects.lead.accountId ```  ``` worklogs.updateAuthor.accountId = projects.lead.accountId ``` |
| [users](#users) | ``` worklogs.author.accountId = users.accountId ```  ``` worklogs.updateAuthor.accountId = users.accountId ``` |

worklogs table schema

|  |
| --- |
| **author**  OBJECT This is a nested data structure:   - accountId: STRING - active: BOOLEAN - avatarUrls: OBJECT, which is also a nested data structure. - displayName: STRING - emailAddress: STRING - key: STRING - name: STRING - self: STRING - timeZone: STRING |
| **comment**  STRING |
| **created**  DATE-TIME |
| **id**  STRING |
| **issueId**  STRING |
| **properties**  ARRAY This is a nested data structure:   - key: STRING |
| **self**  STRING |
| **started**  DATE-TIME |
| **timeSpent**  STRING |
| **timeSpentSeconds**  INTEGER |
| **updateAuthor**  OBJECT This is a nested data structure:   - accountId: STRING - active: BOOLEAN - avatarUrls: OBJECT, which is also a nested data structure. - displayName: STRING - emailAddress: STRING - key: STRING - name: STRING - self: STRING - timeZone: STRING |
| **updated**  DATE-TIME |
| **visibility**  OBJECT This is a nested data structure:   - type: STRING - value: STRING |
