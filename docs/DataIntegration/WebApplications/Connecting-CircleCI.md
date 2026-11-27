---
title: "CircleCI"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-CircleCI.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# CircleCI

CircleCI is a cloud-based continuous integration and continuous delivery (CI/CD) platform that automates software builds, tests, and deployments triggered by changes in source repositories.

CircleCI integration replicates data using the [CircleCI API v2](https://circleci.com/docs/api/v2/).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To set up your CircleCI account, you need:

- A CircleCI account with read access to the projects and organizations whose data you want to replicate.
- A CircleCI **Personal API Token**. Project API tokens are not supported by the CircleCI v2 API and cannot be used with this connector.
- One or more project slugs in the form `vcs-type/org-name/repo-name` (for example, gh/acme-org/web-app for a GitHub-hosted repository).

To create your API token:

1. Log into your [CircleCI](https://app.circleci.com/login) account.
2. Click your avatar in the lower-left corner and select User Settings.
3. Select Personal API Tokens.
4. Click Create New Token.
5. Enter a descriptive name, for example QlikDataIntegration, and click Add API Token.
6. Copy and paste your API token into a secured file.

To identify your project slugs:

- `vcs-type` — `gh` for repositories hosted on GitHub, or `bb` for repositories hosted on Bitbucket.
- `org-name` — the GitHub organization (or username) or Bitbucket workspace that owns the repository.
- `repo-name` — the repository name.

You can read the slug directly from a CircleCI pipeline URL. For example, the URL `https://app.circleci.com/pipelines/github/acme-org/web-app/123` corresponds to the slug gh/acme-org/web-app.

To replicate from multiple projects in one connection, enter all slugs in the Project Slugs field separated by spaces, for example: gh/my-org/repo-one gh/my-org/repo-two.

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
| Token | API token. |
| Project Slugs | Project slugs. |

## Limitations and considerations

- **Personal API Token only.** CircleCI Project API tokens are not supported by the v2 API. The token must belong to a user who has read access to the projects and organizations being replicated. If the token owner loses access (for example, leaves the organization), syncs that depended on that access will return empty results or fail.
- **`pipelines`, `workflows`, and `jobs` are scoped to Project Slugs.** Only the projects listed in the Project Slugs field are replicated for these three streams. Adding a project requires updating the field and re-saving the connection.
- **Organization-scoped streams replicate everything the token can see.** The `collaborations`, `context`, `groups`, `project`, `pipeline_definition`, `schedule`, `trigger`, and `deploy` streams replicate data for every organization and project visible to the Personal API Token. To limit what these streams return, restrict the access of the underlying CircleCI user.
- **`workflows` is replicated per pipeline.** The connector lists pipelines for each configured project, then issues one workflow request per pipeline. Projects with many historical pipelines produce many API calls for the `workflows` stream on the initial sync; subsequent syncs only fetch newer pipelines.
- **`jobs` is replicated per workflow.** Each workflow produces one or more job requests. Projects with many workflows per pipeline can produce a high API-call volume for the `jobs` stream.
- **`jobs` uses Full Table replication even though `pipelines` and `workflows` are incremental.** A workflow's job list is fully refreshed on every sync because the CircleCI jobs API does not expose a replication key. As pipeline and workflow bookmarks advance, the set of workflows re-fetched shrinks, but each retained workflow is re-fetched in full.
- Rate-limit responses (`HTTP 429`) include a `Retry-After` header; the connector waits for the specified duration before retrying, up to 6 attempts within a 60-second budget. Transient server errors (`5xx`) are retried with exponential backoff, up to 5 attempts.
- `HTTP 404 Not Found` responses for individual resources (for example, a deleted pipeline) are treated as empty responses and do not stop the sync. Authentication errors (`401`) and validation errors (`400`) are surfaced immediately and fail the sync.
- Start Date is honored only on the initial sync of each stream. Once a stream has a bookmark in state, subsequent syncs resume from that bookmark; changing Start Date in the connection settings does not retroactively affect already-replicated data.
- Interrupted syncs resume per-project. The connector records a `currently_syncing` marker for the project or pipeline in progress when a sync is interrupted, so the next sync resumes from that point.

## Schema

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### collaborations

The `collaborations` table contains information about the organizations the Personal API Token's user belongs to.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [CircleCI API reference](https://circleci.com/docs/api/v2/#operation/getCollaborations "Opens in new tab: CircleCI API reference") |

### context

The `context` table contains information about contexts (shared environment variable sets) defined in the organizations visible to the token.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id  organization\_id |
| **Useful links** | [CircleCI API reference](https://circleci.com/docs/api/v2/#operation/listContexts "Opens in new tab: CircleCI API reference") |

### deploy

The `deploy` table contains deployment metadata for the organizations visible to the token.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id  organization\_id |
| **Replication Key** | updated\_at |
| **Useful links** | [CircleCI API reference](https://circleci.com/docs/api/v2/ "Opens in new tab: CircleCI API reference") |

### groups

The `groups` table contains information about groups defined in the organizations visible to the token.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id  organization\_id |
| **Useful links** | [CircleCI API reference](https://circleci.com/docs/api/v2/ "Opens in new tab: CircleCI API reference") |

### jobs

The `jobs` table contains information about jobs from your CircleCI workflows. This is a child stream of [workflows](#workflows).

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id  \_workflow\_id |
| **Useful links** | [CircleCI API reference](https://circleci.com/docs/api/v2/#operation/listWorkflowJobs "Opens in new tab: CircleCI API reference") |

### pipeline\_definition

The `pipeline_definition` table contains pipeline definitions for the projects within organizations visible to the token.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id  project\_id  organization\_id |
| **Useful links** | [CircleCI API reference](https://circleci.com/docs/api/v2/ "Opens in new tab: CircleCI API reference") |

### pipelines

The `pipelines` table contains information about pipelines from your CircleCI projects. The [workflows](#workflows) and [jobs](#jobs) streams are children of this stream.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | [CircleCI API reference](https://circleci.com/docs/api/v2/#operation/listPipelinesForProject "Opens in new tab: CircleCI API reference") |

### project

The `project` table contains project metadata for the organizations visible to the token.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id  organization\_id |
| **Useful links** | [CircleCI API reference](https://circleci.com/docs/api/v2/#operation/getProjectBySlug "Opens in new tab: CircleCI API reference") |

### schedule

The `schedule` table contains scheduled pipeline configurations for projects within organizations visible to the token.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id  project-slug |
| **Replication Key** | updated-at |
| **Useful links** | [CircleCI API reference](https://circleci.com/docs/api/v2/#operation/listSchedulesForProject "Opens in new tab: CircleCI API reference") |

### trigger

The `trigger` table contains pipeline trigger configurations for projects within organizations visible to the token.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id  project\_id  pipeline\_definition\_id  organization\_id |
| **Useful links** | [CircleCI API reference](https://circleci.com/docs/api/v2/ "Opens in new tab: CircleCI API reference") |

### workflows

The `workflows` table contains information about workflows from your CircleCI pipelines. This is a child stream of [pipelines](#pipelines). The [jobs](#jobs) stream is a child of this stream.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | created\_at |
| **Useful links** | [CircleCI API reference](https://circleci.com/docs/api/v2/#operation/listWorkflowsByPipelineId "Opens in new tab: CircleCI API reference") |
