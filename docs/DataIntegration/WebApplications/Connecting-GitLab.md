---
title: "GitLab"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-GitLab.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# GitLab

GitLab is an all-in-one platform designed for software development and DevOps.

GitLab integration replicates data using the [GitLab REST API](https://docs.gitlab.com/ee/api/README.html).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To create a private token:

1. Log into your [GitLab](https://gitlab.com/users/sign_in?redirect_to_referer=yes) account.
2. In the upper-right corner, click your user icon.
3. Select Settings.
4. On the left sidebar, select Personal access tokens > Add new token.
5. In Token name, enter an identifiable name for the token.
6. In the Scopes section, check the api box.
7. Click Create personal access token.
8. Copy and paste your private token into a secured file, as it is displayed only once.

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
| API URL | API URL. |
| Private Token | Private token. |
| Projects to track | Enter the projects you want to track separated by spaces. |
| Groups to track | Enter the groups you want to track separated by spaces. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### branches

The `branches` table contains high-level info about repository branches in your projects.

**Note**: To replicate branch data, you must set this table and the [`projects`](#projects) table to replicate. Data for this table will only be replicated when the associated project (in the [`projects`](#projects) table) is also updated.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | project\_id  name |
| **Useful links** | [GitLab API method](https://gitlab.com/help/api/branches.html#list-repository-branches "Opens in new tab: GitLab API method") |

branches table foreign keys

| Join branches with | on |
| --- | --- |
| [commits](#commits) | ``` branches.project_id = commits.project_id ```  ``` branches.commit_id = commits.id ``` |
| [issues](#issues) | ``` branches.project_id = issues.project_id ``` |
| [milestones](#milestones) | ``` branches.project_id = milestones.project_id ``` |
| [projects](#projects) | ``` branches.project_id = projects.project_id ``` |

branches table schema

|  |
| --- |
| **commit\_id**  STRING |
| **developers\_can\_merge**  BOOLEAN |
| **developers\_can\_push**  BOOLEAN |
| **merged**  BOOLEAN |
| **name**  STRING |
| **project\_id**  INTEGER |
| **protected**  BOOLEAN |

### commits

The `commits` table contains info about repository commits in a project.

**Note**: To replicate commit data, you must set this table and the [`projects`](#projects) table to replicate. Data for this table will only be replicated when the associated project (in the [`projects`](#projects) table) is also updated.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [GitLab API method](https://gitlab.com/help/api/commits.md#list-repository-commits "Opens in new tab: GitLab API method") |

commits table foreign keys

| Join commits with | on |
| --- | --- |
| [branches](#branches) | ``` commits.project_id = branches.project_id ```  ``` commits.id = branches.commit_id ``` |
| [issues](#issues) | ``` commits.project_id = issues.project_id ``` |
| [milestones](#milestones) | ``` commits.project_id = milestones.project_id ``` |
| [projects](#projects) | ``` commits.project_id = projects.project_id ``` |

commits table schema

|  |
| --- |
| **allow\_failure**  BOOLEAN |
| **author\_email**  STRING |
| **author\_name**  STRING |
| **committer\_email**  STRING |
| **committer\_name**  STRING |
| **created\_at**  DATE-TIME |
| **id**  STRING |
| **message**  STRING |
| **project\_id**  INTEGER |
| **short\_id**  STRING |
| **title**  STRING |

### groups

The `groups` table contains info about the groups in your GitLab account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [GitLab API method](https://docs.gitlab.com/ee/api/groups.html#list-groups "Opens in new tab: GitLab API method") |

groups table schema

|  |
| --- |
| **avatar\_url**  STRING |
| **description**  STRING |
| **full\_name**  STRING |
| **full\_path**  STRING |
| **id**  INTEGER |
| **lfs\_enabled**  BOOLEAN |
| **name**  STRING |
| **path**  STRING |
| **projects**  ARRAY This is a nested data structure:   - id: INTEGER |
| **request\_access\_enabled**  BOOLEAN |
| **visibility\_level**  INTEGER |
| **web\_url**  STRING |

### issues

The `issues` table contains info about issues contained within projects.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [GitLab API method](https://gitlab.com/help/api/issues.md#list-project-issues "Opens in new tab: GitLab API method") |

issues table foreign keys

| Join issues with | on |
| --- | --- |
| [branches](#branches) | ``` issues.project_id = branches.project_id ``` |
| [commits](#commits) | ``` issues.project_id = commits.project_id ``` |
| [milestones](#milestones) | ``` issues.project_id = milestones.project_id ```  ``` issues.milestone_id = milestones.id ``` |
| [projects](#projects) | ``` issues.project_id = projects.project_id ``` |

issues table schema

|  |
| --- |
| **assignee\_id**  INTEGER |
| **author\_id**  INTEGER |
| **confidential**  BOOLEAN |
| **created\_at**  DATE-TIME |
| **description**  STRING |
| **due\_date**  STRING |
| **id**  INTEGER |
| **iid**  INTEGER |
| **labels**  ARRAY This is a nested data structure. |
| **milestone\_id**  INTEGER |
| **project\_id**  INTEGER |
| **state**  STRING |
| **subscribed**  BOOLEAN |
| **title**  STRING |
| **updated\_at**  DATE-TIME |
| **user\_notes\_count**  INTEGER |
| **web\_url**  STRING |

### milestones

The `milestones` table contains info about project milestones.

**Note**: To replicate milestone data, you must set this table and the [`projects`](#projects) table to replicate. Data for this table will only be replicated when the associated project (in the [`projects`](#projects) table) is also updated.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [GitLab API method](https://gitlab.com/help/api/milestones.md#list-project-milestones "Opens in new tab: GitLab API method") |

milestones table foreign keys

| Join milestones with | on |
| --- | --- |
| [branches](#branches) | ``` milestones.project_id = branches.project_id ``` |
| [commits](#commits) | ``` milestones.project_id = commits.project_id ``` |
| [issues](#issues) | ``` milestones.project_id = issues.project_id ```  ``` milestones.id = issues.milestone_id ``` |
| [projects](#projects) | ``` milestones.project_id = projects.project_id ``` |

milestones table schema

|  |
| --- |
| **created\_at**  DATE-TIME |
| **description**  STRING |
| **due\_date**  STRING |
| **group\_id**  INTEGER |
| **id**  INTEGER |
| **iid**  INTEGER |
| **project\_id**  INTEGER |
| **start\_date**  STRING |
| **state**  STRING |
| **title**  STRING |
| **updated\_at**  DATE-TIME |

### projects

The `projects` table contains info about specific projects.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | last\_activity\_at |
| **Useful links** | [GitLab API method](https://gitlab.com/help/api/projects.md#list-all-projects "Opens in new tab: GitLab API method") |

projects table foreign keys

| Join projects with | on |
| --- | --- |
| [branches](#branches) | ``` projects.project_id = branches.project_id ``` |
| [commits](#commits) | ``` projects.project_id = commits.project_id ``` |
| [issues](#issues) | ``` projects.project_id = issues.project_id ``` |
| [milestones](#milestones) | ``` projects.project_id = milestones.project_id ``` |
| [users](#users) | ``` projects.creator_id = users.id ``` |

projects table schema

|  |
| --- |
| **approvals\_before\_merge**  INTEGER |
| **archived**  BOOLEAN |
| **avatar\_url**  STRING |
| **builds\_enabled**  BOOLEAN |
| **container\_registry\_enabled**  BOOLEAN |
| **created\_at**  DATE-TIME |
| **creator\_id**  INTEGER |
| **default\_branch**  STRING |
| **description**  STRING |
| **forks\_count**  INTEGER |
| **http\_url\_to\_repo**  STRING |
| **id**  INTEGER |
| **issues\_enabled**  BOOLEAN |
| **last\_activity\_at**  DATE-TIME |
| **lfs\_enabled**  BOOLEAN |
| **merge\_requests\_enabled**  BOOLEAN |
| **name**  STRING |
| **name\_with\_namespace**  STRING |
| **namespace**  OBJECT This is a nested data structure:   - id: INTEGER - kind: STRING - name: STRING - path: STRING |
| **only\_allow\_merge\_if\_all\_discussions\_are\_resolved**  BOOLEAN |
| **only\_allow\_merge\_if\_build\_succeeds**  BOOLEAN |
| **open\_issues\_count**  INTEGER |
| **owner\_id**  INTEGER |
| **path**  STRING |
| **path\_with\_namespace**  STRING |
| **permissions**  OBJECT This is a nested data structure:   - group\_access: OBJECT, which is also a nested data structure. - project\_access: OBJECT, which is also a nested data structure. |
| **public**  BOOLEAN |
| **public\_builds**  BOOLEAN |
| **request\_access\_enabled**  BOOLEAN |
| **shared\_runners\_enabled**  BOOLEAN |
| **shared\_with\_groups**  ARRAY This is a nested data structure:   - group\_access\_level: INTEGER - group\_id: INTEGER - group\_name: STRING |
| **snippets\_enabled**  BOOLEAN |
| **ssh\_url\_to\_repo**  STRING |
| **star\_count**  INTEGER |
| **tag\_list**  ARRAY This is a nested data structure. |
| **visibility\_level**  INTEGER |
| **web\_url**  STRING |
| **wiki\_enabled**  BOOLEAN |

### users

The `users` table contains info about the users in your GitLab account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [GitLab API method](https://gitlab.com/help/api/users.md#list-users "Opens in new tab: GitLab API method") |

users table foreign keys

| Join users with | on |
| --- | --- |
| [projects](#projects) | ``` users.id = projects.creator_id ``` |

users table schema

|  |
| --- |
| **avatar\_url**  STRING |
| **id**  INTEGER |
| **name**  STRING |
| **state**  STRING |
| **username**  STRING |
| **web\_url**  STRING |
