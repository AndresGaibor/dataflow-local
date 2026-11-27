---
title: "GitHub"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-GitHub-v2.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# GitHub

GitHub is a platform and cloud-based service for software development and version control using Git. You can use GitHub as a data source when landing or replicating data.

GitHub integration replicates data using the [GitHub REST API v3](https://developer.github.com/v3/).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To create a Personal Access Token, follow the steps outlined in the
[GitHub documentation](https://docs.github.com/en/enterprise-cloud@latest/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

You can choose to generate either a fine-grained token or a classic token:

- Fine-grained token: When creating a fine-grained token, make sure to select the specific repository you want to replicate data from.
- Classic token: For classic tokens, select at least the repo scope to allow replication and set an appropriate expiration date.

Your token will be displayed only once, immediately after you generate it. Copy and paste it into a secured file.

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
| Github Repository Name | Github repository name including organization name. For example: qlikorganization/the-repo-name. |
| Access token | Access token. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### assignees

The `assignees` table contains info about the available assignees for issues in the repositories specified for the integration.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [GitHub documentation](https://developer.github.com/v3/issues/assignees/)  [GitHub API method](https://docs.github.com/en/rest/reference/issues#list-assignees "Opens in new tab: GitHub API method") |

assignees table schema

|  |
| --- |
| **\_sdc\_repository**  STRING |
| **avatar\_url**  STRING |
| **email**  STRING |
| **events\_url**  STRING |
| **followers\_url**  STRING |
| **following\_url**  STRING |
| **gists\_url**  STRING |
| **gravatar\_id**  STRING |
| **html\_url**  STRING |
| **id**  INTEGER |
| **login**  STRING |
| **name**  STRING |
| **node\_id**  STRING |
| **organizations\_url**  STRING |
| **received\_events\_url**  STRING |
| **repos\_url**  STRING |
| **site\_admin**  BOOLEAN |
| **starred\_at**  STRING |
| **starred\_url**  STRING |
| **subscriptions\_url**  STRING |
| **type**  STRING |
| **url**  STRING |

### collaborators

The `collaborators` table contains info about the users who contribute to the repositories specified for the integration.

For organization-owned repositories, this will include outside collaborators, organization owners, organization members that are direct collaborators, who have access through team memberships, or have access through default organization permissions.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [GitHub API method](https://docs.github.com/en/rest/reference/repos#list-repository-collaborators "Opens in new tab: GitHub API method") |

collaborators table foreign keys

| Join collaborators with | on |
| --- | --- |
| [pull\_requests](#pull-requests) | ``` collaborators.id = pull_requests.user.id ``` |
| [reviews](#reviews) | ``` collaborators.id = reviews.user.id ``` |

collaborators table schema

|  |
| --- |
| **\_sdc\_repository**  STRING |
| **avatar\_url**  STRING |
| **email**  STRING |
| **events\_url**  STRING |
| **followers\_url**  STRING |
| **following\_url**  STRING |
| **gists\_url**  STRING |
| **gravatar\_id**  STRING |
| **html\_url**  STRING |
| **id**  INTEGER |
| **login**  STRING |
| **name**  STRING |
| **node\_id**  STRING |
| **organizations\_url**  STRING |
| **permissions**  OBJECT This is a nested data structure:   - admin: BOOLEAN - maintain: BOOLEAN - pull: BOOLEAN - push: BOOLEAN - triage: BOOLEAN |
| **received\_events\_url**  STRING |
| **repos\_url**  STRING |
| **role\_name**  STRING |
| **site\_admin**  BOOLEAN |
| **starred\_url**  STRING |
| **subscriptions\_url**  STRING |
| **type**  STRING |
| **url**  STRING |

### comments

The `comments` table contains info about comments made on issues in the repositories specified for the integration.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [GitHub documentation](https://developer.github.com/v3/comments/)  [GitHub API method](https://docs.github.com/en/rest/reference/issues#list-issue-comments-for-a-repository "Opens in new tab: GitHub API method") |

comments table schema

|  |
| --- |
| **\_sdc\_repository**  STRING |
| **author\_association**  STRING |
| **body**  STRING |
| **body\_html**  STRING |
| **body\_text**  STRING |
| **created\_at**  DATE-TIME |
| **home\_url**  STRING |
| **html\_url**  STRING |
| **id**  INTEGER |
| **issue\_url**  STRING |
| **node\_id**  STRING |
| **performed\_via\_github\_app**  OBJECT This is a nested data structure:   - client\_id: STRING - client\_secret: STRING - created\_at: DATE-TIME - description: STRING - events: ARRAY, which is also a nested data structure. - external\_url: STRING - html\_url: STRING - id: INTEGER - installations\_count: INTEGER - name: STRING - node\_id: STRING - owner: OBJECT, which is also a nested data structure.   - avatar\_url: STRING   - email: STRING   - events\_url: STRING   - followers\_url: STRING   - following\_url: STRING   - gists\_url: STRING   - gravatar\_id: STRING   - html\_url: STRING   - id: INTEGER   - login: STRING   - name: STRING   - node\_id: STRING   - organizations\_url: STRING   - received\_events\_url: STRING   - repos\_url: STRING   - site\_admin: BOOLEAN   - starred\_at: STRING   - starred\_url: STRING   - subscriptions\_url: STRING   - type: STRING   - url: STRING - pem: STRING - permissions: OBJECT, which is also a nested data structure.   - checks: STRING   - contents: STRING   - deployments: STRING   - issues: STRING   - metadata: STRING - slug: STRING - updated\_at: DATE-TIME - webhook\_secret: STRING |
| **reactions**  OBJECT This is a nested data structure:   - +1: INTEGER - -1: INTEGER - confused: INTEGER - eyes: INTEGER - heart: INTEGER - hooray: INTEGER - laugh: INTEGER - rocket: INTEGER - total\_count: INTEGER - url: STRING |
| **updated\_at**  DATE-TIME |
| **url**  STRING |
| **user**  OBJECT This is a nested data structure:   - avatar\_url: STRING - email: STRING - events\_url: STRING - followers\_url: STRING - following\_url: STRING - gists\_url: STRING - gravatar\_id: STRING - html\_url: STRING - id: INTEGER - login: STRING - name: STRING - node\_id: STRING - organizations\_url: STRING - received\_events\_url: STRING - repos\_url: STRING - site\_admin: BOOLEAN - starred\_at: STRING - starred\_url: STRING - subscriptions\_url: STRING - type: STRING - url: STRING |

### commit\_comments

The `commit_comments` table contains info about the commit comments in the repositories specified for the integration.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [GitHub API method](https://docs.github.com/en/rest/reference/repos#list-commit-comments-for-a-repository "Opens in new tab: GitHub API method") |

commit\_comments table schema

|  |
| --- |
| **author\_association**  STRING |
| **body**  STRING |
| **commit\_id**  STRING |
| **created\_at**  DATE-TIME |
| **html\_url**  STRING |
| **id**  NUMBER |
| **line**  NUMBER |
| **node\_id**  STRING |
| **path**  STRING |
| **position**  NUMBER |
| **reactions**  OBJECT This is a nested data structure:   - +1: INTEGER - -1: INTEGER - confused: INTEGER - eyes: INTEGER - heart: INTEGER - hooray: INTEGER - laugh: INTEGER - rocket: INTEGER - total\_count: INTEGER - url: STRING |
| **updated\_at**  DATE-TIME |
| **url**  STRING |
| **user**  OBJECT This is a nested data structure:   - avatar\_url: STRING - email: STRING - events\_url: STRING - followers\_url: STRING - following\_url: STRING - gists\_url: STRING - gravatar\_id: STRING - html\_url: STRING - id: INTEGER - login: STRING - name: STRING - node\_id: STRING - organizations\_url: STRING - received\_events\_url: STRING - repos\_url: STRING - site\_admin: BOOLEAN - starred\_at: STRING - starred\_url: STRING - subscriptions\_url: STRING - type: STRING - url: STRING |

### commits

The `commits` table contains info about repository commits in a project.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | sha |
| **Useful links** | GitHub documentation  [GitHub API method](https://docs.github.com/en/rest/reference/repos#list-commits "Opens in new tab: GitHub API method") |

commits table foreign keys

| Join commits with | on |
| --- | --- |
| [issue\_events](#issue-events) | ``` commits.id = issue_events.commit_id ``` |
| [reviews](#reviews) | ``` commits.id = reviews.commit_id ``` |
| [review\_comments](#review-comments) | ``` commits.id = review_comments.commit_id ```  ``` commits.id = review_comments.original_commit_id ``` |
| [events](#events) | ``` commits.sha = events.payload.commits.sha ``` |
| [pr\_commits](#pr-commits) | ``` commits.sha = pr_commits.sha ``` |

commits table schema

|  |
| --- |
| **\_sdc\_repository**  STRING |
| **author**  OBJECT This is a nested data structure:   - avatar\_url: STRING - email: STRING - events\_url: STRING - followers\_url: STRING - following\_url: STRING - gists\_url: STRING - gravatar\_id: STRING - html\_url: STRING - id: INTEGER - login: STRING - name: STRING - node\_id: STRING - organizations\_url: STRING - received\_events\_url: STRING - repos\_url: STRING - site\_admin: BOOLEAN - starred\_at: STRING - starred\_url: STRING - subscriptions\_url: STRING - type: STRING - url: STRING |
| **comments\_url**  STRING |
| **commit**  OBJECT This is a nested data structure:   - author: OBJECT, which is also a nested data structure.   - avatar\_url: STRING   - email: STRING   - events\_url: STRING   - followers\_url: STRING   - following\_url: STRING   - gists\_url: STRING   - gravatar\_id: STRING   - html\_url: STRING   - id: INTEGER   - login: STRING   - name: STRING   - node\_id: STRING   - organizations\_url: STRING   - received\_events\_url: STRING   - repos\_url: STRING   - site\_admin: BOOLEAN   - starred\_at: STRING   - starred\_url: STRING   - subscriptions\_url: STRING   - type: STRING   - url: STRING - comment\_count: INTEGER - committer: OBJECT, which is also a nested data structure.   - avatar\_url: STRING   - email: STRING   - events\_url: STRING   - followers\_url: STRING   - following\_url: STRING   - gists\_url: STRING   - gravatar\_id: STRING   - html\_url: STRING   - id: INTEGER   - login: STRING   - name: STRING   - node\_id: STRING   - organizations\_url: STRING   - received\_events\_url: STRING   - repos\_url: STRING   - site\_admin: BOOLEAN   - starred\_at: STRING   - starred\_url: STRING   - subscriptions\_url: STRING   - type: STRING   - url: STRING - message: STRING - tree: OBJECT, which is also a nested data structure.   - sha: STRING   - url: STRING - url: STRING |
| **committer**  OBJECT This is a nested data structure:   - avatar\_url: STRING - email: STRING - events\_url: STRING - followers\_url: STRING - following\_url: STRING - gists\_url: STRING - gravatar\_id: STRING - html\_url: STRING - id: INTEGER - login: STRING - name: STRING - node\_id: STRING - organizations\_url: STRING - received\_events\_url: STRING - repos\_url: STRING - site\_admin: BOOLEAN - starred\_at: STRING - starred\_url: STRING - subscriptions\_url: STRING - type: STRING - url: STRING |
| **html\_url**  STRING |
| **id**  STRING |
| **node\_id**  STRING |
| **parents**  ARRAY This is a nested data structure:   - html\_url: STRING - sha: STRING - url: STRING |
| **pr\_id**  STRING |
| **pr\_number**  INTEGER |
| **sha**  STRING |
| **updated\_at**  DATE-TIME |
| **url**  STRING |

### events

The `events` table contains information about events in the repositories specified for the integration.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [GitHub documentation](https://developer.github.com/v3/activity/events/)  [GitHub API method](https://docs.github.com/en/rest/activity/events#list-repository-events "Opens in new tab: GitHub API method") |

events table foreign keys

| Join events with | on |
| --- | --- |
| [commits](#commits) | ``` events.payload.commits.sha = commits.sha ``` |
| [pr\_commits](#pr-commits) | ``` events.payload.commits.sha = pr_commits.sha ``` |

events table schema

|  |
| --- |
| **\_sdc\_repository**  STRING |
| **actor**  OBJECT This is a nested data structure:   - avatar\_url: STRING - display\_login: STRING - gravatar\_id: STRING - id: STRING - login: STRING - url: STRING |
| **created\_at**  STRING |
| **distinct\_size**  NUMBER |
| **head**  STRING |
| **id**  NUMBER |
| **org**  OBJECT This is a nested data structure:   - avatar\_url: STRING - display\_login: STRING - gravatar\_id: STRING - id: STRING - login: STRING - url: STRING |
| **payload**  OBJECT This is a nested data structure:   - action: STRING - before: STRING - comment: OBJECT, STRING, which is also a nested data structure.   - author\_association: STRING   - body: STRING   - body\_html: STRING   - body\_text: STRING   - created\_at: DATE-TIME   - html\_url: STRING   - id: INTEGER   - issue\_url: STRING   - node\_id: STRING   - performed\_via\_github\_app: OBJECT, which is also a nested data structure.     - client\_id: STRING     - client\_secret: STRING     - created\_at: DATE-TIME     - description: STRING     - events: ARRAY, which is also a nested data structure.     - external\_url: STRING     - html\_url: STRING     - id: INTEGER     - installations\_count: INTEGER     - name: STRING     - node\_id: STRING     - owner: OBJECT, which is also a nested data structure.       - avatar\_url: STRING       - email: STRING       - events\_url: STRING       - followers\_url: STRING       - following\_url: STRING       - gists\_url: STRING       - gravatar\_id: STRING       - html\_url: STRING       - id: INTEGER       - login: STRING       - name: STRING       - node\_id: STRING       - organizations\_url: STRING       - received\_events\_url: STRING       - repos\_url: STRING       - site\_admin: BOOLEAN       - starred\_at: STRING       - starred\_url: STRING       - subscriptions\_url: STRING       - type: STRING       - url: STRING     - pem: STRING     - permissions: OBJECT, which is also a nested data structure.       - checks: STRING       - contents: STRING       - deployments: STRING       - issues: STRING       - metadata: STRING     - slug: STRING     - updated\_at: DATE-TIME     - webhook\_secret: STRING   - reactions: OBJECT, which is also a nested data structure.     - +1: INTEGER     - -1: INTEGER     - confused: INTEGER     - eyes: INTEGER     - heart: INTEGER     - hooray: INTEGER     - laugh: INTEGER     - rocket: INTEGER     - total\_count: INTEGER     - url: STRING   - updated\_at: DATE-TIME   - url: STRING   - user: OBJECT, which is also a nested data structure.     - avatar\_url: STRING     - email: STRING     - events\_url: STRING     - followers\_url: STRING     - following\_url: STRING     - gists\_url: STRING     - gravatar\_id: STRING     - html\_url: STRING     - id: INTEGER     - login: STRING     - name: STRING     - node\_id: STRING     - organizations\_url: STRING     - received\_events\_url: STRING     - repos\_url: STRING     - site\_admin: BOOLEAN     - starred\_at: STRING     - starred\_url: STRING     - subscriptions\_url: STRING     - type: STRING     - url: STRING - commits: ARRAY, which is also a nested data structure.   - author: OBJECT, which is also a nested data structure.     - email: STRING     - name: STRING   - distinct: BOOLEAN   - message: STRING   - sha: STRING   - url: STRING - description: STRING - issue: OBJECT, STRING, which is also a nested data structure.   - body: STRING   - comments\_url: STRING   - events\_url: STRING   - html\_url: STRING   - id: INTEGER   - labels: OBJECT, which is also a nested data structure.     - active\_lock\_reason: STRING     - assignee: OBJECT, which is also a nested data structure.       - avatar\_url: STRING       - email: STRING       - events\_url: STRING       - followers\_url: STRING       - following\_url: STRING       - gists\_url: STRING       - gravatar\_id: STRING       - html\_url: STRING       - id: INTEGER       - login: STRING       - name: STRING       - node\_id: STRING       - organizations\_url: STRING       - received\_events\_url: STRING       - repos\_url: STRING       - site\_admin: BOOLEAN       - starred\_at: STRING       - starred\_url: STRING       - subscriptions\_url: STRING       - type: STRING       - url: STRING     - assignees: ARRAY, which is also a nested data structure.     - author\_association: STRING     - body\_html: STRING     - body\_text: STRING     - closed\_at: DATE-TIME     - closed\_by: OBJECT, which is also a nested data structure.       - avatar\_url: STRING       - email: STRING       - events\_url: STRING       - followers\_url: STRING       - following\_url: STRING       - gists\_url: STRING       - gravatar\_id: STRING       - html\_url: STRING       - id: INTEGER       - login: STRING       - name: STRING       - node\_id: STRING       - organizations\_url: STRING       - received\_events\_url: STRING       - repos\_url: STRING       - site\_admin: BOOLEAN       - starred\_at: STRING       - starred\_url: STRING       - subscriptions\_url: STRING       - type: STRING       - url: STRING     - comments: INTEGER     - created\_at: DATE-TIME     - draft: BOOLEAN     - items: OBJECT, which is also a nested data structure.       - color: STRING       - default: BOOLEAN       - description: STRING       - id: INTEGER       - name: STRING       - node\_id: STRING       - url: STRING     - locked: BOOLEAN     - milestone: OBJECT, which is also a nested data structure.       - closed\_at: DATE-TIME       - closed\_issues: INTEGER       - created\_at: DATE-TIME       - creator: OBJECT, which is also a nested data structure.         - avatar\_url: STRING         - email: STRING         - events\_url: STRING         - followers\_url: STRING         - following\_url: STRING         - gists\_url: STRING         - gravatar\_id: STRING         - html\_url: STRING         - id: INTEGER         - login: STRING         - name: STRING         - node\_id: STRING         - organizations\_url: STRING         - received\_events\_url: STRING         - repos\_url: STRING         - site\_admin: BOOLEAN         - starred\_at: STRING         - starred\_url: STRING         - subscriptions\_url: STRING         - type: STRING         - url: STRING       - description: STRING       - due\_on: DATE-TIME       - html\_url: STRING       - id: INTEGER       - labels\_url: STRING       - node\_id: STRING       - number: INTEGER       - open\_issues: INTEGER       - state: STRING       - title: STRING       - updated\_at: DATE-TIME       - url: STRING     - performed\_via\_github\_app: OBJECT, which is also a nested data structure.       - client\_id: STRING       - client\_secret: STRING       - created\_at: DATE-TIME       - description: STRING       - events: ARRAY, which is also a nested data structure.       - external\_url: STRING       - html\_url: STRING       - id: INTEGER       - installations\_count: INTEGER       - name: STRING       - node\_id: STRING       - owner: OBJECT, which is also a nested data structure.         - avatar\_url: STRING         - email: STRING         - events\_url: STRING         - followers\_url: STRING         - following\_url: STRING         - gists\_url: STRING         - gravatar\_id: STRING         - html\_url: STRING         - id: INTEGER         - login: STRING         - name: STRING         - node\_id: STRING         - organizations\_url: STRING         - received\_events\_url: STRING         - repos\_url: STRING         - site\_admin: BOOLEAN         - starred\_at: STRING         - starred\_url: STRING         - subscriptions\_url: STRING         - type: STRING         - url: STRING       - pem: STRING       - permissions: OBJECT, which is also a nested data structure.         - checks: STRING         - contents: STRING         - deployments: STRING         - issues: STRING         - metadata: STRING       - slug: STRING       - updated\_at: DATE-TIME       - webhook\_secret: STRING     - pull\_request: OBJECT, which is also a nested data structure.       - diff\_url: STRING       - html\_url: STRING       - merged\_at: DATE-TIME       - patch\_url: STRING       - url: STRING     - reactions: OBJECT, which is also a nested data structure.       - +1: INTEGER       - -1: INTEGER       - confused: INTEGER       - eyes: INTEGER       - heart: INTEGER       - hooray: INTEGER       - laugh: INTEGER       - rocket: INTEGER       - total\_count: INTEGER       - url: STRING     - repository: OBJECT, which is also a nested data structure.     - timeline\_url: STRING     - updated\_at: DATE-TIME   - labels\_url: STRING   - node\_id: STRING   - number: INTEGER   - repository\_url: STRING   - state: STRING   - state\_reason: STRING   - title: STRING   - url: STRING   - user: OBJECT, which is also a nested data structure.     - avatar\_url: STRING     - email: STRING     - events\_url: STRING     - followers\_url: STRING     - following\_url: STRING     - gists\_url: STRING     - gravatar\_id: STRING     - html\_url: STRING     - id: INTEGER     - login: STRING     - name: STRING     - node\_id: STRING     - organizations\_url: STRING     - received\_events\_url: STRING     - repos\_url: STRING     - site\_admin: BOOLEAN     - starred\_at: STRING     - starred\_url: STRING     - subscriptions\_url: STRING     - type: STRING     - url: STRING - master\_branch: STRING - pages: ARRAY, which is also a nested data structure.   - action: STRING   - html\_url: STRING   - page\_name: STRING   - sha: STRING   - summary: STRING   - title: STRING - pusher\_type: STRING - ref: STRING - ref\_type: STRING |
| **public**  BOOLEAN |
| **push\_id**  NUMBER |
| **ref**  STRING |
| **repo**  OBJECT This is a nested data structure:   - id: NUMBER - name: STRING - url: STRING |
| **size**  NUMBER |
| **type**  STRING |

### issue\_events

The `issue_events` table contains info about issue events in the repositories specified for the integration.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [GitHub API method](https://docs.github.com/en/rest/reference/issues#list-issue-events-for-a-repository "Opens in new tab: GitHub API method") |

issue\_events table foreign keys

| Join issue\_events with | on |
| --- | --- |
| [commits](#commits) | ``` issue_events.commit_id = commits.id ``` |
| [reviews](#reviews) | ``` issue_events.commit_id = reviews.commit_id ``` |
| [review\_comments](#review-comments) | ``` issue_events.commit_id = review_comments.commit_id ```  ``` issue_events.commit_id = review_comments.original_commit_id ``` |
| [issues](#issues) | ``` issue_events.id = issues.id ``` |
| [pull\_requests](#pull-requests) | ``` issue_events.id = pull_requests.id ``` |

issue\_events table schema

|  |
| --- |
| **\_sdc\_repository**  STRING |
| **actor**  OBJECT This is a nested data structure:   - avatar\_url: STRING - email: STRING - events\_url: STRING - followers\_url: STRING - following\_url: STRING - gists\_url: STRING - gravatar\_id: STRING - html\_url: STRING - id: INTEGER - login: STRING - name: STRING - node\_id: STRING - organizations\_url: STRING - received\_events\_url: STRING - repos\_url: STRING - site\_admin: BOOLEAN - starred\_at: STRING - starred\_url: STRING - subscriptions\_url: STRING - type: STRING - url: STRING |
| **assignee**  OBJECT This is a nested data structure:   - avatar\_url: STRING - email: STRING - events\_url: STRING - followers\_url: STRING - following\_url: STRING - gists\_url: STRING - gravatar\_id: STRING - html\_url: STRING - id: INTEGER - login: STRING - name: STRING - node\_id: STRING - organizations\_url: STRING - received\_events\_url: STRING - repos\_url: STRING - site\_admin: BOOLEAN - starred\_at: STRING - starred\_url: STRING - subscriptions\_url: STRING - type: STRING - url: STRING |
| **assigner**  OBJECT This is a nested data structure:   - avatar\_url: STRING - email: STRING - events\_url: STRING - followers\_url: STRING - following\_url: STRING - gists\_url: STRING - gravatar\_id: STRING - html\_url: STRING - id: INTEGER - login: STRING - name: STRING - node\_id: STRING - organizations\_url: STRING - received\_events\_url: STRING - repos\_url: STRING - site\_admin: BOOLEAN - starred\_at: STRING - starred\_url: STRING - subscriptions\_url: STRING - type: STRING - url: STRING |
| **author\_association**  STRING |
| **commit\_id**  STRING |
| **commit\_url**  STRING |
| **created\_at**  DATE-TIME |
| **dismissed\_review**  OBJECT This is a nested data structure:   - dismissal\_commit\_id: STRING - dismissal\_message: STRING - review\_id: INTEGER - state: STRING |
| **draft**  BOOLEAN |
| **event**  STRING |
| **id**  INTEGER |
| **issue**  OBJECT This is a nested data structure:   - active\_lock\_reason: STRING - assignee: OBJECT, which is also a nested data structure.   - avatar\_url: STRING   - email: STRING   - events\_url: STRING   - followers\_url: STRING   - following\_url: STRING   - gists\_url: STRING   - gravatar\_id: STRING   - html\_url: STRING   - id: INTEGER   - login: STRING   - name: STRING   - node\_id: STRING   - organizations\_url: STRING   - received\_events\_url: STRING   - repos\_url: STRING   - site\_admin: BOOLEAN   - starred\_at: STRING   - starred\_url: STRING   - subscriptions\_url: STRING   - type: STRING   - url: STRING - assignees: ARRAY, which is also a nested data structure. - author\_association: STRING - body: STRING - closed\_at: DATE-TIME - closed\_by: OBJECT, which is also a nested data structure.   - avatar\_url: STRING   - email: STRING   - events\_url: STRING   - followers\_url: STRING   - following\_url: STRING   - gists\_url: STRING   - gravatar\_id: STRING   - html\_url: STRING   - id: INTEGER   - login: STRING   - name: STRING   - node\_id: STRING   - organizations\_url: STRING   - received\_events\_url: STRING   - repos\_url: STRING   - site\_admin: BOOLEAN   - starred\_at: STRING   - starred\_url: STRING   - subscriptions\_url: STRING   - type: STRING   - url: STRING - comments: INTEGER - comments\_url: STRING - created\_at: DATE-TIME - events\_url: STRING - html\_url: STRING - id: INTEGER - labels: ARRAY, which is also a nested data structure.   - color: STRING   - default: BOOLEAN   - description: STRING   - id: INTEGER   - name: STRING   - node\_id: STRING   - url: STRING - labels\_url: STRING - locked: BOOLEAN - milestone: OBJECT, which is also a nested data structure.   - closed\_at: DATE-TIME   - closed\_issues: INTEGER   - created\_at: DATE-TIME   - creator: OBJECT, which is also a nested data structure.     - avatar\_url: STRING     - email: STRING     - events\_url: STRING     - followers\_url: STRING     - following\_url: STRING     - gists\_url: STRING     - gravatar\_id: STRING     - html\_url: STRING     - id: INTEGER     - login: STRING     - name: STRING     - node\_id: STRING     - organizations\_url: STRING     - received\_events\_url: STRING     - repos\_url: STRING     - site\_admin: BOOLEAN     - starred\_at: STRING     - starred\_url: STRING     - subscriptions\_url: STRING     - type: STRING     - url: STRING   - description: STRING   - due\_on: DATE-TIME   - html\_url: STRING   - id: INTEGER   - labels\_url: STRING   - node\_id: STRING   - number: INTEGER   - open\_issues: INTEGER   - state: STRING   - title: STRING   - updated\_at: DATE-TIME   - url: STRING - node\_id: STRING - number: INTEGER - performed\_via\_github\_app: OBJECT, which is also a nested data structure.   - client\_id: STRING   - client\_secret: STRING   - created\_at: DATE-TIME   - description: STRING   - events: ARRAY, which is also a nested data structure.   - external\_url: STRING   - html\_url: STRING   - id: INTEGER   - installations\_count: INTEGER   - name: STRING   - node\_id: STRING   - owner: OBJECT, which is also a nested data structure.     - avatar\_url: STRING     - email: STRING     - events\_url: STRING     - followers\_url: STRING     - following\_url: STRING     - gists\_url: STRING     - gravatar\_id: STRING     - html\_url: STRING     - id: INTEGER     - login: STRING     - name: STRING     - node\_id: STRING     - organizations\_url: STRING     - received\_events\_url: STRING     - repos\_url: STRING     - site\_admin: BOOLEAN     - starred\_at: STRING     - starred\_url: STRING     - subscriptions\_url: STRING     - type: STRING     - url: STRING   - pem: STRING   - permissions: OBJECT, which is also a nested data structure.     - checks: STRING     - contents: STRING     - deployments: STRING     - issues: STRING     - metadata: STRING   - slug: STRING   - updated\_at: DATE-TIME   - webhook\_secret: STRING - pull\_request: OBJECT, which is also a nested data structure.   - diff\_url: STRING   - html\_url: STRING   - merged\_at: DATE-TIME   - patch\_url: STRING   - url: STRING - reactions: OBJECT, which is also a nested data structure.   - +1: INTEGER   - -1: INTEGER   - confused: INTEGER   - eyes: INTEGER   - heart: INTEGER   - hooray: INTEGER   - laugh: INTEGER   - rocket: INTEGER   - total\_count: INTEGER   - url: STRING - repository: OBJECT, which is also a nested data structure. - repository\_url: STRING - state: STRING - title: STRING - updated\_at: DATE-TIME - url: STRING - user: OBJECT, which is also a nested data structure.   - avatar\_url: STRING   - email: STRING   - events\_url: STRING   - followers\_url: STRING   - following\_url: STRING   - gists\_url: STRING   - gravatar\_id: STRING   - html\_url: STRING   - id: INTEGER   - login: STRING   - name: STRING   - node\_id: STRING   - organizations\_url: STRING   - received\_events\_url: STRING   - repos\_url: STRING   - site\_admin: BOOLEAN   - starred\_at: STRING   - starred\_url: STRING   - subscriptions\_url: STRING   - type: STRING   - url: STRING |
| **label**  OBJECT This is a nested data structure:   - color: STRING - name: STRING |
| **lock\_reason**  STRING |
| **milestone**  OBJECT This is a nested data structure:   - title: STRING |
| **node\_id**  STRING |
| **performed\_via\_github\_app**  OBJECT This is a nested data structure:   - client\_id: STRING - client\_secret: STRING - created\_at: DATE-TIME - description: STRING - events: ARRAY, which is also a nested data structure. - external\_url: STRING - html\_url: STRING - id: INTEGER - installations\_count: INTEGER - name: STRING - node\_id: STRING - owner: OBJECT, which is also a nested data structure.   - avatar\_url: STRING   - email: STRING   - events\_url: STRING   - followers\_url: STRING   - following\_url: STRING   - gists\_url: STRING   - gravatar\_id: STRING   - html\_url: STRING   - id: INTEGER   - login: STRING   - name: STRING   - node\_id: STRING   - organizations\_url: STRING   - received\_events\_url: STRING   - repos\_url: STRING   - site\_admin: BOOLEAN   - starred\_at: STRING   - starred\_url: STRING   - subscriptions\_url: STRING   - type: STRING   - url: STRING - pem: STRING - permissions: OBJECT, which is also a nested data structure.   - checks: STRING   - contents: STRING   - deployments: STRING   - issues: STRING   - metadata: STRING - slug: STRING - updated\_at: DATE-TIME - webhook\_secret: STRING |
| **project\_card**  OBJECT This is a nested data structure:   - column\_name: STRING - id: INTEGER - previous\_column\_name: STRING - project\_id: INTEGER - project\_url: STRING - url: STRING |
| **rename**  OBJECT This is a nested data structure:   - from: STRING - to: STRING |
| **requested\_reviewer**  OBJECT This is a nested data structure:   - avatar\_url: STRING - email: STRING - events\_url: STRING - followers\_url: STRING - following\_url: STRING - gists\_url: STRING - gravatar\_id: STRING - html\_url: STRING - id: INTEGER - login: STRING - name: STRING - node\_id: STRING - organizations\_url: STRING - received\_events\_url: STRING - repos\_url: STRING - site\_admin: BOOLEAN - starred\_at: STRING - starred\_url: STRING - subscriptions\_url: STRING - type: STRING - url: STRING |
| **requested\_team**  OBJECT This is a nested data structure:   - description: STRING - html\_url: STRING - id: INTEGER - members\_url: STRING - name: STRING - node\_id: STRING - parent: OBJECT, which is also a nested data structure.   - description: STRING   - html\_url: STRING   - id: INTEGER   - ldap\_dn: STRING   - members\_url: STRING   - name: STRING   - node\_id: STRING   - permission: STRING   - privacy: STRING   - repositories\_url: STRING   - slug: STRING   - url: STRING - permission: STRING - permissions: OBJECT, which is also a nested data structure.   - admin: BOOLEAN   - maintain: BOOLEAN   - pull: BOOLEAN   - push: BOOLEAN   - triage: BOOLEAN - privacy: STRING - repositories\_url: STRING - slug: STRING - url: STRING |
| **review\_requester**  OBJECT This is a nested data structure:   - avatar\_url: STRING - email: STRING - events\_url: STRING - followers\_url: STRING - following\_url: STRING - gists\_url: STRING - gravatar\_id: STRING - html\_url: STRING - id: INTEGER - login: STRING - name: STRING - node\_id: STRING - organizations\_url: STRING - received\_events\_url: STRING - repos\_url: STRING - site\_admin: BOOLEAN - starred\_at: STRING - starred\_url: STRING - subscriptions\_url: STRING - type: STRING - url: STRING |
| **url**  STRING |

### issue\_labels

The `issue_labels` table contains info about issue labels in the repositories specified for the integration.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [GitHub API method](https://docs.github.com/en/rest/reference/issues#list-labels-for-a-repository "Opens in new tab: GitHub API method") |

issue\_labels table foreign keys

| Join issue\_labels with | on |
| --- | --- |
| [issues](#issues) | ``` issue_labels.id = issues.labels.id ``` |
| [pull\_requests](#pull-requests) | ``` issue_labels.id = pull_requests.labels.id ``` |

issue\_labels table schema

|  |
| --- |
| **\_sdc\_repository**  STRING |
| **color**  STRING |
| **default**  BOOLEAN |
| **description**  STRING |
| **id**  NUMBER |
| **name**  STRING |
| **node\_id**  STRING |
| **url**  STRING |

### issue\_milestones

The `issue_milestones` table contains info about issue milestones in the repositories specified for the integration.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [GitHub API method](https://docs.github.com/en/rest/reference/issues#list-milestones "Opens in new tab: GitHub API method") |

issue\_milestones table schema

|  |
| --- |
| **\_sdc\_repository**  STRING |
| **closed\_at**  DATE-TIME |
| **closed\_issues**  NUMBER |
| **created\_at**  DATE-TIME |
| **creator**  OBJECT This is a nested data structure:   - avatar\_url: STRING - email: STRING - events\_url: STRING - followers\_url: STRING - following\_url: STRING - gists\_url: STRING - gravatar\_id: STRING - html\_url: STRING - id: INTEGER - login: STRING - name: STRING - node\_id: STRING - organizations\_url: STRING - received\_events\_url: STRING - repos\_url: STRING - site\_admin: BOOLEAN - starred\_at: STRING - starred\_url: STRING - subscriptions\_url: STRING - type: STRING - url: STRING |
| **description**  STRING |
| **due\_on**  DATE-TIME |
| **html\_url**  STRING |
| **id**  NUMBER |
| **labels\_url**  STRING |
| **node\_id**  STRING |
| **number**  NUMBER |
| **open\_issues**  NUMBER |
| **state**  STRING |
| **title**  STRING |
| **updated\_at**  DATE-TIME |
| **url**  STRING |

### issues

The `issues` table contains info about issues in the repositories specified for the integration.

#### Issues and pull requests

GitHub’s API considers every pull request an issue, but not every issue may be a pull request. Therefore, this table may contain both issues and pull requests.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [GitHub documentation](https://developer.github.com/v3/issues/)  [GitHub API method](https://docs.github.com/en/rest/reference/issues#list-repository-issues "Opens in new tab: GitHub API method") |

issues table foreign keys

| Join issues with | on |
| --- | --- |
| [issue\_events](#issue-events) | ``` issues.id = issue_events.id ``` |
| [pull\_requests](#pull-requests) | ``` issues.id = pull_requests.id ```  ``` issues.labels.id = pull_requests.labels.id ``` |
| [issue\_labels](#issue-labels) | ``` issues.labels.id = issue_labels.id ``` |
| [pr\_commits](#pr-commits) | ``` issues.id = pr_commits.pr_id ``` |

issues table schema

|  |
| --- |
| **\_sdc\_repository**  STRING |
| **active\_lock\_reason**  STRING |
| **assignee**  OBJECT This is a nested data structure:   - avatar\_url: STRING - email: STRING - events\_url: STRING - followers\_url: STRING - following\_url: STRING - gists\_url: STRING - gravatar\_id: STRING - html\_url: STRING - id: INTEGER - login: STRING - name: STRING - node\_id: STRING - organizations\_url: STRING - received\_events\_url: STRING - repos\_url: STRING - site\_admin: BOOLEAN - starred\_at: STRING - starred\_url: STRING - subscriptions\_url: STRING - type: STRING - url: STRING |
| **assignees**  ARRAY This is a nested data structure. |
| **author\_association**  STRING |
| **body**  STRING |
| **body\_html**  STRING |
| **body\_text**  STRING |
| **closed\_at**  DATE-TIME |
| **closed\_by**  OBJECT This is a nested data structure:   - avatar\_url: STRING - email: STRING - events\_url: STRING - followers\_url: STRING - following\_url: STRING - gists\_url: STRING - gravatar\_id: STRING - html\_url: STRING - id: INTEGER - login: STRING - name: STRING - node\_id: STRING - organizations\_url: STRING - received\_events\_url: STRING - repos\_url: STRING - site\_admin: BOOLEAN - starred\_at: STRING - starred\_url: STRING - subscriptions\_url: STRING - type: STRING - url: STRING |
| **comments**  INTEGER |
| **comments\_url**  STRING |
| **created\_at**  DATE-TIME |
| **draft**  BOOLEAN |
| **events\_url**  STRING |
| **html\_url**  STRING |
| **id**  INTEGER |
| **labels**  ARRAY This is a nested data structure:   - color: STRING - default: BOOLEAN - description: STRING - id: INTEGER - name: STRING - node\_id: STRING - url: STRING |
| **labels\_url**  STRING |
| **locked**  BOOLEAN |
| **milestone**  OBJECT This is a nested data structure:   - closed\_at: DATE-TIME - closed\_issues: INTEGER - created\_at: DATE-TIME - creator: OBJECT, which is also a nested data structure.   - avatar\_url: STRING   - email: STRING   - events\_url: STRING   - followers\_url: STRING   - following\_url: STRING   - gists\_url: STRING   - gravatar\_id: STRING   - html\_url: STRING   - id: INTEGER   - login: STRING   - name: STRING   - node\_id: STRING   - organizations\_url: STRING   - received\_events\_url: STRING   - repos\_url: STRING   - site\_admin: BOOLEAN   - starred\_at: STRING   - starred\_url: STRING   - subscriptions\_url: STRING   - type: STRING   - url: STRING - description: STRING - due\_on: DATE-TIME - html\_url: STRING - id: INTEGER - labels\_url: STRING - node\_id: STRING - number: INTEGER - open\_issues: INTEGER - state: STRING - title: STRING - updated\_at: DATE-TIME - url: STRING |
| **node\_id**  STRING |
| **number**  INTEGER |
| **performed\_via\_github\_app**  OBJECT This is a nested data structure:   - client\_id: STRING - client\_secret: STRING - created\_at: DATE-TIME - description: STRING - events: ARRAY, which is also a nested data structure. - external\_url: STRING - html\_url: STRING - id: INTEGER - installations\_count: INTEGER - name: STRING - node\_id: STRING - owner: OBJECT, which is also a nested data structure.   - avatar\_url: STRING   - email: STRING   - events\_url: STRING   - followers\_url: STRING   - following\_url: STRING   - gists\_url: STRING   - gravatar\_id: STRING   - html\_url: STRING   - id: INTEGER   - login: STRING   - name: STRING   - node\_id: STRING   - organizations\_url: STRING   - received\_events\_url: STRING   - repos\_url: STRING   - site\_admin: BOOLEAN   - starred\_at: STRING   - starred\_url: STRING   - subscriptions\_url: STRING   - type: STRING   - url: STRING - pem: STRING - permissions: OBJECT, which is also a nested data structure.   - checks: STRING   - contents: STRING   - deployments: STRING   - issues: STRING   - metadata: STRING - slug: STRING - updated\_at: DATE-TIME - webhook\_secret: STRING |
| **pull\_request**  OBJECT This is a nested data structure:   - diff\_url: STRING - html\_url: STRING - merged\_at: DATE-TIME - patch\_url: STRING - url: STRING |
| **reactions**  OBJECT This is a nested data structure:   - +1: INTEGER - -1: INTEGER - confused: INTEGER - eyes: INTEGER - heart: INTEGER - hooray: INTEGER - laugh: INTEGER - rocket: INTEGER - total\_count: INTEGER - url: STRING |
| **repository\_url**  STRING |
| **state**  STRING |
| **state\_reason**  STRING |
| **timeline\_url**  STRING |
| **title**  STRING |
| **updated\_at**  DATE-TIME |
| **url**  STRING |
| **user**  OBJECT This is a nested data structure:   - avatar\_url: STRING - email: STRING - events\_url: STRING - followers\_url: STRING - following\_url: STRING - gists\_url: STRING - gravatar\_id: STRING - html\_url: STRING - id: INTEGER - login: STRING - name: STRING - node\_id: STRING - organizations\_url: STRING - received\_events\_url: STRING - repos\_url: STRING - site\_admin: BOOLEAN - starred\_at: STRING - starred\_url: STRING - subscriptions\_url: STRING - type: STRING - url: STRING |

### pr\_commits

The `pr_commits` table contains info about pull request commits and is a slight variation of the [`commits`](#commits) table. This allows you to associate commits to pull requests that are squash merged.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | pr\_commits schema on GitHub  [GitHub API method](https://docs.github.com/en/rest/reference/pulls#list-commits-on-a-pull-request "Opens in new tab: GitHub API method") |

pr\_commits table foreign keys

| Join pr\_commits with | on |
| --- | --- |
| [issues](#issues) | ``` pr_commits.pr_id = issues.id ``` |
| [pull\_requests](#pull-requests) | ``` pr_commits.pr_id = pull_requests.id ``` |
| [commits](#commits) | ``` pr_commits.sha = commits.sha ``` |
| [events](#events) | ``` pr_commits.sha = events.payload.commits.sha ``` |

pr\_commits table schema

|  |
| --- |
| **\_sdc\_repository**  STRING |
| **author**  OBJECT This is a nested data structure:   - avatar\_url: STRING - email: STRING - events\_url: STRING - followers\_url: STRING - following\_url: STRING - gists\_url: STRING - gravatar\_id: STRING - html\_url: STRING - id: INTEGER - login: STRING - name: STRING - node\_id: STRING - organizations\_url: STRING - received\_events\_url: STRING - repos\_url: STRING - site\_admin: BOOLEAN - starred\_at: STRING - starred\_url: STRING - subscriptions\_url: STRING - type: STRING - url: STRING |
| **comments\_url**  STRING |
| **commit**  OBJECT This is a nested data structure:   - author: OBJECT, which is also a nested data structure.   - avatar\_url: STRING   - email: STRING   - events\_url: STRING   - followers\_url: STRING   - following\_url: STRING   - gists\_url: STRING   - gravatar\_id: STRING   - html\_url: STRING   - id: INTEGER   - login: STRING   - name: STRING   - node\_id: STRING   - organizations\_url: STRING   - received\_events\_url: STRING   - repos\_url: STRING   - site\_admin: BOOLEAN   - starred\_at: STRING   - starred\_url: STRING   - subscriptions\_url: STRING   - type: STRING   - url: STRING - comment\_count: INTEGER - committer: OBJECT, which is also a nested data structure.   - date: DATE-TIME   - email: STRING   - login: STRING   - name: STRING - message: STRING - tree: OBJECT, which is also a nested data structure.   - sha: STRING   - url: STRING - url: STRING - verification: OBJECT, which is also a nested data structure.   - payload: STRING   - reason: STRING   - signature: STRING   - verified: BOOLEAN |
| **committer**  OBJECT This is a nested data structure:   - avatar\_url: STRING - email: STRING - events\_url: STRING - followers\_url: STRING - following\_url: STRING - gists\_url: STRING - gravatar\_id: STRING - html\_url: STRING - id: INTEGER - login: STRING - name: STRING - node\_id: STRING - organizations\_url: STRING - received\_events\_url: STRING - repos\_url: STRING - site\_admin: BOOLEAN - starred\_at: STRING - starred\_url: STRING - subscriptions\_url: STRING - type: STRING - url: STRING |
| **html\_url**  STRING |
| **id**  STRING |
| **node\_id**  STRING |
| **parents**  ARRAY This is a nested data structure:   - html\_url: STRING - sha: STRING - url: STRING |
| **pr\_id**  STRING |
| **pr\_number**  INTEGER |
| **sha**  STRING |
| **updated\_at**  DATE-TIME |
| **url**  STRING |

### project\_cards

The `project_cards` table contains information about project cards in the repositories specified for the integration.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [GitHub documentation](https://docs.github.com/en/rest/reference/projects#cards)  [GitHub API method](https://docs.github.com/en/rest/reference/projects#list-project-cards "Opens in new tab: GitHub API method") |

project\_cards table schema

|  |
| --- |
| **\_sdc\_repository**  STRING |
| **archived**  BOOLEAN |
| **cards\_url**  STRING |
| **column\_name**  STRING |
| **column\_url**  STRING |
| **content\_url**  STRING |
| **created\_at**  DATE-TIME |
| **creator**  OBJECT This is a nested data structure:   - avatar\_url: STRING - email: STRING - events\_url: STRING - followers\_url: STRING - following\_url: STRING - gists\_url: STRING - gravatar\_id: STRING - html\_url: STRING - id: INTEGER - login: STRING - name: STRING - node\_id: STRING - organizations\_url: STRING - received\_events\_url: STRING - repos\_url: STRING - site\_admin: BOOLEAN - starred\_at: STRING - starred\_url: STRING - subscriptions\_url: STRING - type: STRING - url: STRING |
| **id**  NUMBER |
| **name**  STRING |
| **node\_id**  STRING |
| **note**  STRING |
| **project\_id**  STRING |
| **project\_url**  STRING |
| **updated\_at**  DATE-TIME |
| **url**  STRING |

### project\_columns

The `project_columns` table contains info about the columns of projects in the repositories specified for the integration.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [GitHub API method](https://docs.github.com/en/rest/reference/projects#list-project-columns "Opens in new tab: GitHub API method") |

project\_columns table schema

|  |
| --- |
| **\_sdc\_repository**  STRING |
| **cards\_url**  STRING |
| **created\_at**  DATE-TIME |
| **id**  NUMBER |
| **name**  STRING |
| **node\_id**  STRING |
| **project\_url**  STRING |
| **updated\_at**  DATE-TIME |
| **url**  STRING |

### projects

The `projects` table contains info about projects in the repositories specified for the integration.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [GitHub API method](https://docs.github.com/en/rest/reference/projects#list-repository-projects "Opens in new tab: GitHub API method") |

projects table schema

|  |
| --- |
| **body**  STRING |
| **columns\_url**  STRING |
| **created\_at**  DATE-TIME |
| **creator**  OBJECT This is a nested data structure:   - avatar\_url: STRING - email: STRING - events\_url: STRING - followers\_url: STRING - following\_url: STRING - gists\_url: STRING - gravatar\_id: STRING - html\_url: STRING - id: INTEGER - login: STRING - name: STRING - node\_id: STRING - organizations\_url: STRING - received\_events\_url: STRING - repos\_url: STRING - site\_admin: BOOLEAN - starred\_at: STRING - starred\_url: STRING - subscriptions\_url: STRING - type: STRING - url: STRING |
| **html\_url**  STRING |
| **id**  NUMBER |
| **name**  STRING |
| **node\_id**  STRING |
| **number**  NUMBER |
| **organization\_permission**  STRING |
| **owner\_url**  STRING |
| **private**  BOOLEAN |
| **state**  STRING |
| **updated\_at**  DATE-TIME |
| **url**  STRING |

### pull\_requests

The `pull_requests` table contains info about pull requests made against the repositories specified for the integration.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [GitHub documentation](https://developer.github.com/v3/pulls/)  [GitHub API method](https://docs.github.com/en/rest/reference/pulls#list-pull-requests "Opens in new tab: GitHub API method") |

pull\_requests table foreign keys

| Join pull\_requests with | on |
| --- | --- |
| [collaborators](#collaborators) | ``` pull_requests.user.id = collaborators.id ``` |
| [reviews](#reviews) | ``` pull_requests.user.id = reviews.user.id ``` |
| [issues](#issues) | ``` pull_requests.id = issues.id ```  ``` pull_requests.labels.id = issues.labels.id ``` |
| [issue\_events](#issue-events) | ``` pull_requests.id = issue_events.id ``` |
| [issue\_labels](#issue-labels) | ``` pull_requests.labels.id = issue_labels.id ``` |
| [pr\_commits](#pr-commits) | ``` pull_requests.id = pr_commits.pr_id ``` |

pull\_requests table schema

|  |
| --- |
| **\_links**  OBJECT This is a nested data structure:   - comments: OBJECT, which is also a nested data structure.   - href: STRING - commits: OBJECT, which is also a nested data structure.   - href: STRING - html: OBJECT, which is also a nested data structure.   - href: STRING - issue: OBJECT, which is also a nested data structure.   - href: STRING - review\_comment: OBJECT, which is also a nested data structure.   - href: STRING - review\_comments: OBJECT, which is also a nested data structure.   - href: STRING - self: OBJECT, which is also a nested data structure.   - href: STRING - statuses: OBJECT, which is also a nested data structure.   - href: STRING |
| **\_sdc\_repository**  STRING |
| **active\_lock\_reason**  STRING |
| **assignee**  OBJECT This is a nested data structure:   - avatar\_url: STRING - email: STRING - events\_url: STRING - followers\_url: STRING - following\_url: STRING - gists\_url: STRING - gravatar\_id: STRING - html\_url: STRING - id: INTEGER - login: STRING - name: STRING - node\_id: STRING - organizations\_url: STRING - received\_events\_url: STRING - repos\_url: STRING - site\_admin: BOOLEAN - starred\_at: STRING - starred\_url: STRING - subscriptions\_url: STRING - type: STRING - url: STRING |
| **assignees**  ARRAY This is a nested data structure. |
| **author\_association**  STRING |
| **auto\_merge**  OBJECT This is a nested data structure:   - commit\_message: STRING - commit\_title: STRING - enabled\_by: OBJECT, which is also a nested data structure.   - avatar\_url: STRING   - email: STRING   - events\_url: STRING   - followers\_url: STRING   - following\_url: STRING   - gists\_url: STRING   - gravatar\_id: STRING   - html\_url: STRING   - id: INTEGER   - login: STRING   - name: STRING   - node\_id: STRING   - organizations\_url: STRING   - received\_events\_url: STRING   - repos\_url: STRING   - site\_admin: BOOLEAN   - starred\_at: STRING   - starred\_url: STRING   - subscriptions\_url: STRING   - type: STRING   - url: STRING - merge\_method: STRING |
| **base**  OBJECT This is a nested data structure:   - label: STRING - ref: STRING - repo: OBJECT, which is also a nested data structure. - sha: STRING - user: OBJECT, which is also a nested data structure.   - avatar\_url: STRING   - email: STRING   - events\_url: STRING   - followers\_url: STRING   - following\_url: STRING   - gists\_url: STRING   - gravatar\_id: STRING   - html\_url: STRING   - id: INTEGER   - login: STRING   - name: STRING   - node\_id: STRING   - organizations\_url: STRING   - received\_events\_url: STRING   - repos\_url: STRING   - site\_admin: BOOLEAN   - starred\_at: STRING   - starred\_url: STRING   - subscriptions\_url: STRING   - type: STRING   - url: STRING |
| **body**  STRING |
| **closed\_at**  DATE-TIME |
| **comments\_url**  STRING |
| **commits\_url**  STRING |
| **created\_at**  DATE-TIME |
| **diff\_url**  STRING |
| **draft**  BOOLEAN |
| **head**  OBJECT This is a nested data structure:   - label: STRING - ref: STRING - repo: OBJECT, which is also a nested data structure. - sha: STRING - user: OBJECT, which is also a nested data structure.   - avatar\_url: STRING   - email: STRING   - events\_url: STRING   - followers\_url: STRING   - following\_url: STRING   - gists\_url: STRING   - gravatar\_id: STRING   - html\_url: STRING   - id: INTEGER   - login: STRING   - name: STRING   - node\_id: STRING   - organizations\_url: STRING   - received\_events\_url: STRING   - repos\_url: STRING   - site\_admin: BOOLEAN   - starred\_at: STRING   - starred\_url: STRING   - subscriptions\_url: STRING   - type: STRING   - url: STRING |
| **html\_url**  STRING |
| **id**  STRING |
| **issues\_url**  STRING |
| **labels**  ARRAY This is a nested data structure:   - color: STRING - default: BOOLEAN - description: STRING - id: INTEGER - name: STRING - node\_id: STRING - url: STRING |
| **locked**  BOOLEAN |
| **merge\_commit\_sha**  STRING |
| **merged\_at**  DATE-TIME |
| **milestone**  OBJECT This is a nested data structure:   - closed\_at: DATE-TIME - closed\_issues: INTEGER - created\_at: DATE-TIME - creator: OBJECT, which is also a nested data structure.   - avatar\_url: STRING   - email: STRING   - events\_url: STRING   - followers\_url: STRING   - following\_url: STRING   - gists\_url: STRING   - gravatar\_id: STRING   - html\_url: STRING   - id: INTEGER   - login: STRING   - name: STRING   - node\_id: STRING   - organizations\_url: STRING   - received\_events\_url: STRING   - repos\_url: STRING   - site\_admin: BOOLEAN   - starred\_at: STRING   - starred\_url: STRING   - subscriptions\_url: STRING   - type: STRING   - url: STRING - description: STRING - due\_on: DATE-TIME - html\_url: STRING - id: INTEGER - labels\_url: STRING - node\_id: STRING - number: INTEGER - open\_issues: INTEGER - state: STRING - title: STRING - updated\_at: DATE-TIME - url: STRING |
| **node\_id**  STRING |
| **number**  INTEGER |
| **patch\_url**  STRING |
| **requested\_reviewers**  ARRAY This is a nested data structure:   - avatar\_url: STRING - email: STRING - events\_url: STRING - followers\_url: STRING - following\_url: STRING - gists\_url: STRING - gravatar\_id: STRING - html\_url: STRING - id: INTEGER - login: STRING - name: STRING - node\_id: STRING - organizations\_url: STRING - received\_events\_url: STRING - repos\_url: STRING - site\_admin: BOOLEAN - starred\_at: STRING - starred\_url: STRING - subscriptions\_url: STRING - type: STRING - url: STRING |
| **requested\_teams**  ARRAY This is a nested data structure:   - description: STRING - html\_url: STRING - id: INTEGER - members\_url: STRING - name: STRING - node\_id: STRING - parent: OBJECT, which is also a nested data structure.   - description: STRING   - html\_url: STRING   - id: INTEGER   - ldap\_dn: STRING   - members\_url: STRING   - name: STRING   - node\_id: STRING   - permission: STRING   - privacy: STRING   - repositories\_url: STRING   - slug: STRING   - url: STRING - permission: STRING - permissions: OBJECT, which is also a nested data structure.   - admin: BOOLEAN   - maintain: BOOLEAN   - pull: BOOLEAN   - push: BOOLEAN   - triage: BOOLEAN - privacy: STRING - repositories\_url: STRING - slug: STRING - url: STRING |
| **review\_comments\_url**  STRING |
| **state**  STRING |
| **statuses\_url**  STRING |
| **title**  STRING |
| **updated\_at**  DATE-TIME |
| **url**  STRING |
| **user**  OBJECT This is a nested data structure:   - avatar\_url: STRING - email: STRING - events\_url: STRING - followers\_url: STRING - following\_url: STRING - gists\_url: STRING - gravatar\_id: STRING - html\_url: STRING - id: INTEGER - login: STRING - name: STRING - node\_id: STRING - organizations\_url: STRING - received\_events\_url: STRING - repos\_url: STRING - site\_admin: BOOLEAN - starred\_at: STRING - starred\_url: STRING - subscriptions\_url: STRING - type: STRING - url: STRING |

### releases

The `releases` table contains info about releases in the repositories specified for the integration.

**Note**: GitHub doesn’t include regular Git tags that haven’t been associated with a release.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [GitHub API method](https://docs.github.com/en/rest/reference/repos#list-releases "Opens in new tab: GitHub API method") |

releases table schema

|  |
| --- |
| **\_sdc\_repository**  STRING |
| **assets**  ARRAY This is a nested data structure. |
| **assets\_url**  STRING |
| **author**  OBJECT This is a nested data structure:   - avatar\_url: STRING - email: STRING - events\_url: STRING - followers\_url: STRING - following\_url: STRING - gists\_url: STRING - gravatar\_id: STRING - html\_url: STRING - id: INTEGER - login: STRING - name: STRING - node\_id: STRING - organizations\_url: STRING - received\_events\_url: STRING - repos\_url: STRING - site\_admin: BOOLEAN - starred\_at: STRING - starred\_url: STRING - subscriptions\_url: STRING - type: STRING - url: STRING |
| **body**  STRING |
| **body\_html**  STRING |
| **body\_text**  STRING |
| **created\_at**  DATE-TIME |
| **discussion\_url**  STRING |
| **draft**  BOOLEAN |
| **html\_url**  STRING |
| **id**  STRING |
| **mentions\_count**  INTEGER |
| **name**  STRING |
| **node\_id**  STRING |
| **prerelease**  BOOLEAN |
| **published\_at**  DATE-TIME |
| **reactions**  OBJECT This is a nested data structure:   - +1: INTEGER - -1: INTEGER - confused: INTEGER - eyes: INTEGER - heart: INTEGER - hooray: INTEGER - laugh: INTEGER - rocket: INTEGER - total\_count: INTEGER - url: STRING |
| **tag\_name**  STRING |
| **tarball\_url**  STRING |
| **target\_commitish**  STRING |
| **upload\_url**  STRING |
| **url**  STRING |
| **zipball\_url**  STRING |

### review\_comments

The `review_comments` table contains info about comments made on pull request reviews in the repositories specified for the integration.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [GitHub API method](https://docs.github.com/en/rest/reference/pulls#list-review-comments-on-a-pull-request "Opens in new tab: GitHub API method") |

review\_comments table foreign keys

| Join review\_comments with | on |
| --- | --- |
| [commits](#commits) | ``` review_comments.commit_id = commits.id ```  ``` review_comments.original_commit_id = commits.id ``` |
| [issue\_events](#issue-events) | ``` review_comments.commit_id = issue_events.commit_id ```  ``` review_comments.original_commit_id = issue_events.commit_id ``` |
| [reviews](#reviews) | ``` review_comments.commit_id = reviews.commit_id ```  ``` review_comments.original_commit_id = reviews.commit_id ```  ``` review_comments.pull_request_review_id = reviews.id ``` |

review\_comments table schema

|  |
| --- |
| **\_links**  OBJECT This is a nested data structure:   - html: OBJECT, which is also a nested data structure.   - href: STRING - pull\_request: OBJECT, which is also a nested data structure.   - href: STRING - self: OBJECT, which is also a nested data structure.   - href: STRING |
| **\_sdc\_repository**  STRING |
| **assignee**  STRING |
| **assignees**  STRING |
| **author\_association**  STRING |
| **base**  STRING |
| **body**  STRING |
| **body\_html**  STRING |
| **body\_text**  STRING |
| **comments\_url**  STRING |
| **commit\_id**  STRING |
| **commits\_url**  STRING |
| **created\_at**  DATE-TIME |
| **diff\_hunk**  STRING |
| **diff\_url**  STRING |
| **head**  STRING |
| **html\_url**  STRING |
| **id**  INTEGER |
| **in\_reply\_to\_id**  INTEGER |
| **issue\_url**  STRING |
| **labels**  STRING |
| **line**  INTEGER |
| **locked**  STRING |
| **merge\_commit\_sha**  STRING |
| **milestone**  STRING |
| **node\_id**  STRING |
| **original\_commit\_id**  STRING |
| **original\_line**  INTEGER |
| **original\_position**  INTEGER |
| **original\_start\_line**  INTEGER |
| **patch\_url**  STRING |
| **path**  STRING |
| **position**  INTEGER |
| **pr\_id**  STRING |
| **pull\_request\_review\_id**  INTEGER |
| **pull\_request\_url**  STRING |
| **reactions**  OBJECT This is a nested data structure:   - +1: INTEGER - -1: INTEGER - confused: INTEGER - eyes: INTEGER - heart: INTEGER - hooray: INTEGER - laugh: INTEGER - rocket: INTEGER - total\_count: INTEGER - url: STRING |
| **requested\_reviewers**  STRING |
| **requested\_teams**  STRING |
| **review\_comment\_url**  STRING |
| **review\_comments\_url**  STRING |
| **side**  STRING |
| **start\_line**  INTEGER |
| **start\_side**  STRING |
| **statuses\_url**  STRING |
| **updated\_at**  DATE-TIME |
| **url**  STRING |
| **user**  OBJECT This is a nested data structure:   - avatar\_url: STRING - email: STRING - events\_url: STRING - followers\_url: STRING - following\_url: STRING - gists\_url: STRING - gravatar\_id: STRING - html\_url: STRING - id: INTEGER - login: STRING - name: STRING - node\_id: STRING - organizations\_url: STRING - received\_events\_url: STRING - repos\_url: STRING - site\_admin: BOOLEAN - starred\_at: STRING - starred\_url: STRING - subscriptions\_url: STRING - type: STRING - url: STRING |

### reviews

The `reviews` table contains info about pull request reviews in the repositories specified for the integration. A pull request review is a group of comments on a pull request.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [GitHub documentation](https://developer.github.com/v3/pulls/reviews/)  [GitHub API method](https://docs.github.com/en/rest/reference/pulls#list-reviews-for-a-pull-request "Opens in new tab: GitHub API method") |

reviews table foreign keys

| Join reviews with | on |
| --- | --- |
| [collaborators](#collaborators) | ``` reviews.user.id = collaborators.id ``` |
| [pull\_requests](#pull-requests) | ``` reviews.user.id = pull_requests.user.id ``` |
| [commits](#commits) | ``` reviews.commit_id = commits.id ``` |
| [issue\_events](#issue-events) | ``` reviews.commit_id = issue_events.commit_id ``` |
| [review\_comments](#review-comments) | ``` reviews.commit_id = review_comments.commit_id ```  ``` reviews.commit_id = review_comments.original_commit_id ```  ``` reviews.id = review_comments.pull_request_review_id ``` |

reviews table schema

|  |
| --- |
| **\_links**  OBJECT This is a nested data structure:   - html: OBJECT, which is also a nested data structure.   - href: STRING - pull\_request: OBJECT, which is also a nested data structure.   - href: STRING |
| **\_sdc\_repository**  STRING |
| **author\_association**  STRING |
| **body**  STRING |
| **body\_html**  STRING |
| **body\_text**  STRING |
| **commit\_id**  STRING |
| **html\_url**  STRING |
| **id**  INTEGER |
| **node\_id**  STRING |
| **pr\_id**  STRING |
| **pull\_request\_url**  STRING |
| **state**  STRING |
| **submitted\_at**  DATE-TIME |
| **user**  OBJECT This is a nested data structure:   - avatar\_url: STRING - email: STRING - events\_url: STRING - followers\_url: STRING - following\_url: STRING - gists\_url: STRING - gravatar\_id: STRING - html\_url: STRING - id: INTEGER - login: STRING - name: STRING - node\_id: STRING - organizations\_url: STRING - received\_events\_url: STRING - repos\_url: STRING - site\_admin: BOOLEAN - starred\_at: STRING - starred\_url: STRING - subscriptions\_url: STRING - type: STRING - url: STRING |

### stargazers

The `stargazers` table contains info about users who have starred the repositories specified for the integration.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | user\_id |
| **Useful links** | [GitHub API method](https://docs.github.com/en/rest/reference/activity#list-stargazers "Opens in new tab: GitHub API method") |

stargazers table schema

|  |
| --- |
| **\_sdc\_repository**  STRING |
| **starred\_at**  DATE-TIME |
| **user**  OBJECT This is a nested data structure:   - avatar\_url: STRING - email: STRING - events\_url: STRING - followers\_url: STRING - following\_url: STRING - gists\_url: STRING - gravatar\_id: STRING - html\_url: STRING - id: INTEGER - login: STRING - name: STRING - node\_id: STRING - organizations\_url: STRING - received\_events\_url: STRING - repos\_url: STRING - site\_admin: BOOLEAN - starred\_at: STRING - starred\_url: STRING - subscriptions\_url: STRING - type: STRING - url: STRING |
| **user\_id**  INTEGER |

### team\_members

The `team_members` table contains info about members of organization teams that are visible to the user who authorized the integration.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [GitHub API method](https://docs.github.com/en/rest/reference/teams#list-team-members "Opens in new tab: GitHub API method") |

team\_members table schema

|  |
| --- |
| **\_sdc\_repository**  STRING |
| **avatar\_url**  STRING |
| **email**  STRING |
| **events\_url**  STRING |
| **followers\_url**  STRING |
| **following\_url**  STRING |
| **gists\_url**  STRING |
| **gravatar\_id**  STRING |
| **html\_url**  STRING |
| **id**  NUMBER |
| **login**  STRING |
| **name**  STRING |
| **node\_id**  STRING |
| **organizations\_url**  STRING |
| **received\_events\_url**  STRING |
| **repos\_url**  STRING |
| **site\_admin**  BOOLEAN |
| **starred\_at**  STRING |
| **starred\_url**  STRING |
| **subscriptions\_url**  STRING |
| **team\_slug**  STRING |
| **type**  STRING |
| **url**  STRING |

### team\_memberships

The `team_memberships` table contains info about membership of users in of organization teams that are visible to the user who authorized the integration.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | url |
| **Useful links** | [GitHub API method](https://docs.github.com/en/rest/reference/teams#get-team-membership-for-a-user "Opens in new tab: GitHub API method") |

team\_memberships table schema

|  |
| --- |
| **\_sdc\_repository**  STRING |
| **login**  STRING |
| **role**  STRING |
| **state**  STRING |
| **url**  STRING |

### teams

The `teams` table contains info about the teams in an organization. Only teams that are visible to the user who authorized the integration in Stitch will be replicated.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [GitHub API method](https://docs.github.com/en/rest/reference/teams#list-teams "Opens in new tab: GitHub API method") |

teams table schema

|  |
| --- |
| **\_sdc\_repository**  STRING |
| **description**  STRING |
| **html\_url**  STRING |
| **id**  NUMBER |
| **members\_url**  STRING |
| **name**  STRING |
| **node\_id**  STRING |
| **parent**  OBJECT, STRING This is a nested data structure. |
| **permission**  STRING |
| **permissions**  OBJECT This is a nested data structure:   - admin: BOOLEAN - maintain: BOOLEAN - pull: BOOLEAN - push: BOOLEAN - triage: BOOLEAN |
| **privacy**  STRING |
| **repositories\_url**  STRING |
| **slug**  STRING |
| **url**  STRING |
