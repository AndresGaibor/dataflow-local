---
title: "Lever"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Lever.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Lever

Lever is a cloud-based applicant tracking system (ATS) and candidate relationship management (CRM) platform.

Lever integration replicates data using the [Lever API (v1)](https://hire.lever.co/developer/documentation).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To create the token:

1. Log into your [Lever](https://hire.lever.co/auth/login?continue=%2F) account.
2. Click your profile icon in the upper-right corner.
3. Go to Settings > API Credentials.
4. Locate the Generate New Key link in the Lever API credentials section.
5. If you want your key to access confidential information, turn the Allow access to confidential data toggle on. If not, skip to the next step.
6. Click Done.
7. Copy and paste your token into a secured file.

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
| Token | Token. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### archive\_reasons

The `archive_reasons` table contains info about the reasons candidates have exited your active hiring pipeline. Refer to [Lever’s documentation](https://help.lever.co/hc/articles/204502125) for more info.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Lever documentation](https://hire.lever.co/developer/documentation#archive-reasons)  [Lever API method](https://hire.lever.co/developer/documentation#list-all-archive-reasons "Opens in new tab: Lever API method") |

archive\_reasons table foreign keys

| Join archive\_reasons with | on |
| --- | --- |
| [candidate\_applications](#candidate-applications) | ``` archive_reasons.id = candidate_applications.archived.reason ``` |
| [candidates](#candidates) | ``` archive_reasons.id = candidates.archived.reason ``` |
| [opportunity\_applications](#opportunity-applications) | ``` archive_reasons.id = opportunity_applications.archived.reason ``` |
| [opportunities](#opportunities) | ``` archive_reasons.id = opportunities.archived.reason ``` |

archive\_reasons table schema

|  |
| --- |
| **id**  STRING |
| **text**  STRING |

### candidate\_applications

The `candidate_applications` table contains info about candidate applications in your Lever account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Lever documentation](https://hire.lever.co/developer/documentation#applications)  [Lever API method](https://hire.lever.co/developer/documentation#list-all-applications "Opens in new tab: Lever API method") |

candidate\_applications table foreign keys

| Join candidate\_applications with | on |
| --- | --- |
| [archive\_reasons](#archive-reasons) | ``` candidate_applications.archived.reason = archive_reasons.id ``` |
| [candidates](#candidates) | ``` candidate_applications.archived.reason = candidates.archived.reason ```  ``` candidate_applications.id = candidates.applications ```  ``` candidate_applications.candidateId = candidates.id ```  ``` candidate_applications.postingHiringManager = candidates.followers ```  ``` candidate_applications.postingOwner = candidates.followers ```  ``` candidate_applications.requisitionForHire.hiringManagerOnHire = candidates.followers ```  ``` candidate_applications.user = candidates.followers ```  ``` candidate_applications.postingHiringManager = candidates.owner ```  ``` candidate_applications.postingOwner = candidates.owner ```  ``` candidate_applications.requisitionForHire.hiringManagerOnHire = candidates.owner ```  ``` candidate_applications.user = candidates.owner ```  ``` candidate_applications.postingHiringManager = candidates.stageChanges.userId ```  ``` candidate_applications.postingOwner = candidates.stageChanges.userId ```  ``` candidate_applications.requisitionForHire.hiringManagerOnHire = candidates.stageChanges.userId ```  ``` candidate_applications.user = candidates.stageChanges.userId ``` |
| [opportunity\_applications](#opportunity-applications) | ``` candidate_applications.archived.reason = opportunity_applications.archived.reason ```  ``` candidate_applications.id = opportunity_applications.id ```  ``` candidate_applications.candidateId = opportunity_applications.candidateId ```  ``` candidate_applications.posting = opportunity_applications.posting ```  ``` candidate_applications.requisitionForHire.id = opportunity_applications.requisitionForHire.id ```  ``` candidate_applications.postingHiringManager = opportunity_applications.postingHiringManager ```  ``` candidate_applications.postingOwner = opportunity_applications.postingHiringManager ```  ``` candidate_applications.requisitionForHire.hiringManagerOnHire = opportunity_applications.postingHiringManager ```  ``` candidate_applications.user = opportunity_applications.postingHiringManager ```  ``` candidate_applications.postingHiringManager = opportunity_applications.postingOwner ```  ``` candidate_applications.postingOwner = opportunity_applications.postingOwner ```  ``` candidate_applications.requisitionForHire.hiringManagerOnHire = opportunity_applications.postingOwner ```  ``` candidate_applications.user = opportunity_applications.postingOwner ```  ``` candidate_applications.postingHiringManager = opportunity_applications.requisitionForHire.hiringManagerOnHire ```  ``` candidate_applications.postingOwner = opportunity_applications.requisitionForHire.hiringManagerOnHire ```  ``` candidate_applications.requisitionForHire.hiringManagerOnHire = opportunity_applications.requisitionForHire.hiringManagerOnHire ```  ``` candidate_applications.user = opportunity_applications.requisitionForHire.hiringManagerOnHire ```  ``` candidate_applications.postingHiringManager = opportunity_applications.user ```  ``` candidate_applications.postingOwner = opportunity_applications.user ```  ``` candidate_applications.requisitionForHire.hiringManagerOnHire = opportunity_applications.user ```  ``` candidate_applications.user = opportunity_applications.user ``` |
| [opportunities](#opportunities) | ``` candidate_applications.archived.reason = opportunities.archived.reason ```  ``` candidate_applications.id = opportunities.applications ```  ``` candidate_applications.candidateId = opportunities.id ```  ``` candidate_applications.postingHiringManager = opportunities.followers ```  ``` candidate_applications.postingOwner = opportunities.followers ```  ``` candidate_applications.requisitionForHire.hiringManagerOnHire = opportunities.followers ```  ``` candidate_applications.user = opportunities.followers ```  ``` candidate_applications.postingHiringManager = opportunities.owner ```  ``` candidate_applications.postingOwner = opportunities.owner ```  ``` candidate_applications.requisitionForHire.hiringManagerOnHire = opportunities.owner ```  ``` candidate_applications.user = opportunities.owner ```  ``` candidate_applications.postingHiringManager = opportunities.stageChanges.userId ```  ``` candidate_applications.postingOwner = opportunities.stageChanges.userId ```  ``` candidate_applications.requisitionForHire.hiringManagerOnHire = opportunities.stageChanges.userId ```  ``` candidate_applications.user = opportunities.stageChanges.userId ``` |
| [opportunity\_offers](#opportunity-offers) | ``` candidate_applications.candidateId = opportunity_offers.opportunityId ```  ``` candidate_applications.posting = opportunity_offers.posting ```  ``` candidate_applications.postingHiringManager = opportunity_offers.creator ```  ``` candidate_applications.postingOwner = opportunity_offers.creator ```  ``` candidate_applications.requisitionForHire.hiringManagerOnHire = opportunity_offers.creator ```  ``` candidate_applications.user = opportunity_offers.creator ``` |
| [postings](#postings) | ``` candidate_applications.posting = postings.id ```  ``` candidate_applications.postingHiringManager = postings.followers ```  ``` candidate_applications.postingOwner = postings.followers ```  ``` candidate_applications.requisitionForHire.hiringManagerOnHire = postings.followers ```  ``` candidate_applications.user = postings.followers ```  ``` candidate_applications.postingHiringManager = postings.hiringManager ```  ``` candidate_applications.postingOwner = postings.hiringManager ```  ``` candidate_applications.requisitionForHire.hiringManagerOnHire = postings.hiringManager ```  ``` candidate_applications.user = postings.hiringManager ```  ``` candidate_applications.postingHiringManager = postings.owner ```  ``` candidate_applications.postingOwner = postings.owner ```  ``` candidate_applications.requisitionForHire.hiringManagerOnHire = postings.owner ```  ``` candidate_applications.user = postings.owner ```  ``` candidate_applications.postingHiringManager = postings.user ```  ``` candidate_applications.postingOwner = postings.user ```  ``` candidate_applications.requisitionForHire.hiringManagerOnHire = postings.user ```  ``` candidate_applications.user = postings.user ``` |
| [requisitions](#requisitions) | ``` candidate_applications.posting = requisitions.postings ```  ``` candidate_applications.requisitionForHire.id = requisitions.id ```  ``` candidate_applications.postingHiringManager = requisitions.creator ```  ``` candidate_applications.postingOwner = requisitions.creator ```  ``` candidate_applications.requisitionForHire.hiringManagerOnHire = requisitions.creator ```  ``` candidate_applications.user = requisitions.creator ```  ``` candidate_applications.postingHiringManager = requisitions.hiringManager ```  ``` candidate_applications.postingOwner = requisitions.hiringManager ```  ``` candidate_applications.requisitionForHire.hiringManagerOnHire = requisitions.hiringManager ```  ``` candidate_applications.user = requisitions.hiringManager ```  ``` candidate_applications.postingHiringManager = requisitions.owner ```  ``` candidate_applications.postingOwner = requisitions.owner ```  ``` candidate_applications.requisitionForHire.hiringManagerOnHire = requisitions.owner ```  ``` candidate_applications.user = requisitions.owner ``` |
| [candidate\_offers](#candidate-offers) | ``` candidate_applications.postingHiringManager = candidate_offers.creator ```  ``` candidate_applications.postingOwner = candidate_offers.creator ```  ``` candidate_applications.requisitionForHire.hiringManagerOnHire = candidate_offers.creator ```  ``` candidate_applications.user = candidate_offers.creator ``` |
| [candidate\_referrals](#candidate-referrals) | ``` candidate_applications.postingHiringManager = candidate_referrals.referrer ```  ``` candidate_applications.postingOwner = candidate_referrals.referrer ```  ``` candidate_applications.requisitionForHire.hiringManagerOnHire = candidate_referrals.referrer ```  ``` candidate_applications.user = candidate_referrals.referrer ```  ``` candidate_applications.postingHiringManager = candidate_referrals.user ```  ``` candidate_applications.postingOwner = candidate_referrals.user ```  ``` candidate_applications.requisitionForHire.hiringManagerOnHire = candidate_referrals.user ```  ``` candidate_applications.user = candidate_referrals.user ``` |
| [opportunity\_referrals](#opportunity-referrals) | ``` candidate_applications.postingHiringManager = opportunity_referrals.referrer ```  ``` candidate_applications.postingOwner = opportunity_referrals.referrer ```  ``` candidate_applications.requisitionForHire.hiringManagerOnHire = opportunity_referrals.referrer ```  ``` candidate_applications.user = opportunity_referrals.referrer ```  ``` candidate_applications.postingHiringManager = opportunity_referrals.user ```  ``` candidate_applications.postingOwner = opportunity_referrals.user ```  ``` candidate_applications.requisitionForHire.hiringManagerOnHire = opportunity_referrals.user ```  ``` candidate_applications.user = opportunity_referrals.user ``` |

candidate\_applications table schema

|  |
| --- |
| **candidateId**  STRING |
| **createdAt**  NUMBER |
| **email**  STRING |
| **id**  STRING |
| **name**  STRING |
| **posting**  STRING |
| **type**  STRING |
| **user**  STRING |

### candidate\_offers

The `candidate_offers` table contains data sent to candidates about [`opportunities`](#opportunities) via Lever’s Offers feature.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Lever documentation](https://hire.lever.co/developer/documentation#offers)  [Lever API method](https://hire.lever.co/developer/documentation#list-all-offers "Opens in new tab: Lever API method") |

candidate\_offers table foreign keys

| Join candidate\_offers with | on |
| --- | --- |
| [opportunity\_offers](#opportunity-offers) | ``` candidate_offers.id = opportunity_offers.id ```  ``` candidate_offers.creator = opportunity_offers.creator ``` |
| [requisitions](#requisitions) | ``` candidate_offers.id = requisitions.offerIds ```  ``` candidate_offers.creator = requisitions.creator ```  ``` candidate_offers.creator = requisitions.hiringManager ```  ``` candidate_offers.creator = requisitions.owner ``` |
| [candidate\_applications](#candidate-applications) | ``` candidate_offers.creator = candidate_applications.postingHiringManager ```  ``` candidate_offers.creator = candidate_applications.postingOwner ```  ``` candidate_offers.creator = candidate_applications.requisitionForHire.hiringManagerOnHire ```  ``` candidate_offers.creator = candidate_applications.user ``` |
| [candidate\_referrals](#candidate-referrals) | ``` candidate_offers.creator = candidate_referrals.referrer ```  ``` candidate_offers.creator = candidate_referrals.user ``` |
| [candidates](#candidates) | ``` candidate_offers.creator = candidates.followers ```  ``` candidate_offers.creator = candidates.owner ```  ``` candidate_offers.creator = candidates.stageChanges.userId ``` |
| [opportunities](#opportunities) | ``` candidate_offers.creator = opportunities.followers ```  ``` candidate_offers.creator = opportunities.owner ```  ``` candidate_offers.creator = opportunities.stageChanges.userId ``` |
| [opportunity\_applications](#opportunity-applications) | ``` candidate_offers.creator = opportunity_applications.postingHiringManager ```  ``` candidate_offers.creator = opportunity_applications.postingOwner ```  ``` candidate_offers.creator = opportunity_applications.requisitionForHire.hiringManagerOnHire ```  ``` candidate_offers.creator = opportunity_applications.user ``` |
| [opportunity\_referrals](#opportunity-referrals) | ``` candidate_offers.creator = opportunity_referrals.referrer ```  ``` candidate_offers.creator = opportunity_referrals.user ``` |
| [postings](#postings) | ``` candidate_offers.creator = postings.followers ```  ``` candidate_offers.creator = postings.hiringManager ```  ``` candidate_offers.creator = postings.owner ```  ``` candidate_offers.creator = postings.user ``` |

candidate\_offers table schema

|  |
| --- |
| **approvedAt**  DATE-TIME |
| **createdAt**  DATE-TIME |
| **creator**  STRING |
| **fields**  ARRAY This is a nested data structure:   - identifier: STRING - text: STRING - value: STRING |
| **id**  STRING |
| **sentAt**  DATE-TIME |
| **signatures**  OBJECT This is a nested data structure:   - email: STRING - firstOpenedAt: DATE-TIME - lastOpenedAt: DATE-TIME - name: STRING - role: STRING - signed: BOOLEAN - signedAt: DATE-TIME |
| **status**  STRING |

### candidate\_referrals

The `candidate_referrals` table contains info about the referrals in your Lever account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Lever documentation](https://hire.lever.co/developer/documentation#referrals)  [Lever API method](https://hire.lever.co/developer/documentation#list-all-referrals "Opens in new tab: Lever API method") |

candidate\_referrals table foreign keys

| Join candidate\_referrals with | on |
| --- | --- |
| [opportunity\_referrals](#opportunity-referrals) | ``` candidate_referrals.id = opportunity_referrals.id ```  ``` candidate_referrals.referrer = opportunity_referrals.referrer ```  ``` candidate_referrals.user = opportunity_referrals.referrer ```  ``` candidate_referrals.referrer = opportunity_referrals.user ```  ``` candidate_referrals.user = opportunity_referrals.user ``` |
| [candidate\_applications](#candidate-applications) | ``` candidate_referrals.referrer = candidate_applications.postingHiringManager ```  ``` candidate_referrals.user = candidate_applications.postingHiringManager ```  ``` candidate_referrals.referrer = candidate_applications.postingOwner ```  ``` candidate_referrals.user = candidate_applications.postingOwner ```  ``` candidate_referrals.referrer = candidate_applications.requisitionForHire.hiringManagerOnHire ```  ``` candidate_referrals.user = candidate_applications.requisitionForHire.hiringManagerOnHire ```  ``` candidate_referrals.referrer = candidate_applications.user ```  ``` candidate_referrals.user = candidate_applications.user ``` |
| [candidate\_offers](#candidate-offers) | ``` candidate_referrals.referrer = candidate_offers.creator ```  ``` candidate_referrals.user = candidate_offers.creator ``` |
| [candidates](#candidates) | ``` candidate_referrals.referrer = candidates.followers ```  ``` candidate_referrals.user = candidates.followers ```  ``` candidate_referrals.referrer = candidates.owner ```  ``` candidate_referrals.user = candidates.owner ```  ``` candidate_referrals.referrer = candidates.stageChanges.userId ```  ``` candidate_referrals.user = candidates.stageChanges.userId ``` |
| [opportunities](#opportunities) | ``` candidate_referrals.referrer = opportunities.followers ```  ``` candidate_referrals.user = opportunities.followers ```  ``` candidate_referrals.referrer = opportunities.owner ```  ``` candidate_referrals.user = opportunities.owner ```  ``` candidate_referrals.referrer = opportunities.stageChanges.userId ```  ``` candidate_referrals.user = opportunities.stageChanges.userId ``` |
| [opportunity\_applications](#opportunity-applications) | ``` candidate_referrals.referrer = opportunity_applications.postingHiringManager ```  ``` candidate_referrals.user = opportunity_applications.postingHiringManager ```  ``` candidate_referrals.referrer = opportunity_applications.postingOwner ```  ``` candidate_referrals.user = opportunity_applications.postingOwner ```  ``` candidate_referrals.referrer = opportunity_applications.requisitionForHire.hiringManagerOnHire ```  ``` candidate_referrals.user = opportunity_applications.requisitionForHire.hiringManagerOnHire ```  ``` candidate_referrals.referrer = opportunity_applications.user ```  ``` candidate_referrals.user = opportunity_applications.user ``` |
| [opportunity\_offers](#opportunity-offers) | ``` candidate_referrals.referrer = opportunity_offers.creator ```  ``` candidate_referrals.user = opportunity_offers.creator ``` |
| [postings](#postings) | ``` candidate_referrals.referrer = postings.followers ```  ``` candidate_referrals.user = postings.followers ```  ``` candidate_referrals.referrer = postings.hiringManager ```  ``` candidate_referrals.user = postings.hiringManager ```  ``` candidate_referrals.referrer = postings.owner ```  ``` candidate_referrals.user = postings.owner ```  ``` candidate_referrals.referrer = postings.user ```  ``` candidate_referrals.user = postings.user ``` |
| [requisitions](#requisitions) | ``` candidate_referrals.referrer = requisitions.creator ```  ``` candidate_referrals.user = requisitions.creator ```  ``` candidate_referrals.referrer = requisitions.hiringManager ```  ``` candidate_referrals.user = requisitions.hiringManager ```  ``` candidate_referrals.referrer = requisitions.owner ```  ``` candidate_referrals.user = requisitions.owner ``` |

candidate\_referrals table schema

|  |
| --- |
| **baseTemplateId**  STRING |
| **completedAt**  DATE-TIME |
| **createdAt**  DATE-TIME |
| **fields**  ARRAY This is a nested data structure:   - description: STRING - options: ARRAY, which is also a nested data structure.   - text: STRING - prompt: STRING - required: BOOLEAN - text: STRING - type: STRING - value: STRING |
| **id**  STRING |
| **instructions**  STRING |
| **referrer**  STRING |
| **stage**  STRING |
| **text**  STRING |
| **type**  STRING |
| **user**  STRING |

### candidate\_resumes

The `candidate_resumes` table contains info about candidate resumes.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Lever documentation](https://hire.lever.co/developer/documentation#resumes)  [Lever API method](https://hire.lever.co/developer/documentation#list-all-resumes "Opens in new tab: Lever API method") |

candidate\_resumes table foreign keys

| Join candidate\_resumes with | on |
| --- | --- |
| [opportunity\_resumes](#opportunity-resumes) | ``` candidate_resumes.id = opportunity_resumes.id ``` |

candidate\_resumes table schema

|  |
| --- |
| **createdAt**  DATE-TIME |
| **file**  OBJECT This is a nested data structure. |
| **id**  STRING |
| **parsedData**  OBJECT This is a nested data structure. |

### candidates

The `candidates` table contains info about candidates, or individuals who’ve been added to your Lever account as potential fits for job opportunities.

**Note**: This table must be set to replicate in order to replicate the `candidate_applications`, `candidate_offers`, `candidate_referrals`, and `candidate_resumes` tables.

During Extraction, this table will be replicated before any other selected `candidate_*` tables. Then, for every candidate, Stitch will query for every candidate’s applications, offers, referrals, and resumes.

For example: During Extraction, Stitch replicates a candidate with `id: 12345` from Lever’s `/candidates` endpoint.

Using `id: 12345`, Stitch will then query for the rest of the candidate’s data:

- `/candidates/12345/applications`
- `/candidates/12345/offers`
- `/candidates/12345/referrals`
- `/candidates/12345/resumes`

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Lever documentation](https://hire.lever.co/developer/documentation#candidates)  [Lever API method](https://hire.lever.co/developer/documentation#list-all-candidates "Opens in new tab: Lever API method") |

candidates table foreign keys

| Join candidates with | on |
| --- | --- |
| [archive\_reasons](#archive-reasons) | ``` candidates.archived.reason = archive_reasons.id ``` |
| [candidate\_applications](#candidate-applications) | ``` candidates.archived.reason = candidate_applications.archived.reason ```  ``` candidates.applications = candidate_applications.id ```  ``` candidates.id = candidate_applications.candidateId ```  ``` candidates.followers = candidate_applications.postingHiringManager ```  ``` candidates.owner = candidate_applications.postingHiringManager ```  ``` candidates.stageChanges.userId = candidate_applications.postingHiringManager ```  ``` candidates.followers = candidate_applications.postingOwner ```  ``` candidates.owner = candidate_applications.postingOwner ```  ``` candidates.stageChanges.userId = candidate_applications.postingOwner ```  ``` candidates.followers = candidate_applications.requisitionForHire.hiringManagerOnHire ```  ``` candidates.owner = candidate_applications.requisitionForHire.hiringManagerOnHire ```  ``` candidates.stageChanges.userId = candidate_applications.requisitionForHire.hiringManagerOnHire ```  ``` candidates.followers = candidate_applications.user ```  ``` candidates.owner = candidate_applications.user ```  ``` candidates.stageChanges.userId = candidate_applications.user ``` |
| [opportunity\_applications](#opportunity-applications) | ``` candidates.archived.reason = opportunity_applications.archived.reason ```  ``` candidates.applications = opportunity_applications.id ```  ``` candidates.id = opportunity_applications.candidateId ```  ``` candidates.followers = opportunity_applications.postingHiringManager ```  ``` candidates.owner = opportunity_applications.postingHiringManager ```  ``` candidates.stageChanges.userId = opportunity_applications.postingHiringManager ```  ``` candidates.followers = opportunity_applications.postingOwner ```  ``` candidates.owner = opportunity_applications.postingOwner ```  ``` candidates.stageChanges.userId = opportunity_applications.postingOwner ```  ``` candidates.followers = opportunity_applications.requisitionForHire.hiringManagerOnHire ```  ``` candidates.owner = opportunity_applications.requisitionForHire.hiringManagerOnHire ```  ``` candidates.stageChanges.userId = opportunity_applications.requisitionForHire.hiringManagerOnHire ```  ``` candidates.followers = opportunity_applications.user ```  ``` candidates.owner = opportunity_applications.user ```  ``` candidates.stageChanges.userId = opportunity_applications.user ``` |
| [opportunities](#opportunities) | ``` candidates.archived.reason = opportunities.archived.reason ```  ``` candidates.applications = opportunities.applications ```  ``` candidates.contact = opportunities.contact ```  ``` candidates.id = opportunities.id ```  ``` candidates.stage = opportunities.stage ```  ``` candidates.stageChanges.toStageId = opportunities.stage ```  ``` candidates.stage = opportunities.stageChanges.toStageId ```  ``` candidates.stageChanges.toStageId = opportunities.stageChanges.toStageId ```  ``` candidates.followers = opportunities.followers ```  ``` candidates.owner = opportunities.followers ```  ``` candidates.stageChanges.userId = opportunities.followers ```  ``` candidates.followers = opportunities.owner ```  ``` candidates.owner = opportunities.owner ```  ``` candidates.stageChanges.userId = opportunities.owner ```  ``` candidates.followers = opportunities.stageChanges.userId ```  ``` candidates.owner = opportunities.stageChanges.userId ```  ``` candidates.stageChanges.userId = opportunities.stageChanges.userId ``` |
| [opportunity\_offers](#opportunity-offers) | ``` candidates.id = opportunity_offers.opportunityId ```  ``` candidates.followers = opportunity_offers.creator ```  ``` candidates.owner = opportunity_offers.creator ```  ``` candidates.stageChanges.userId = opportunity_offers.creator ``` |
| [stages](#stages) | ``` candidates.stage = stages.id ```  ``` candidates.stageChanges.toStageId = stages.id ``` |
| [candidate\_offers](#candidate-offers) | ``` candidates.followers = candidate_offers.creator ```  ``` candidates.owner = candidate_offers.creator ```  ``` candidates.stageChanges.userId = candidate_offers.creator ``` |
| [candidate\_referrals](#candidate-referrals) | ``` candidates.followers = candidate_referrals.referrer ```  ``` candidates.owner = candidate_referrals.referrer ```  ``` candidates.stageChanges.userId = candidate_referrals.referrer ```  ``` candidates.followers = candidate_referrals.user ```  ``` candidates.owner = candidate_referrals.user ```  ``` candidates.stageChanges.userId = candidate_referrals.user ``` |
| [opportunity\_referrals](#opportunity-referrals) | ``` candidates.followers = opportunity_referrals.referrer ```  ``` candidates.owner = opportunity_referrals.referrer ```  ``` candidates.stageChanges.userId = opportunity_referrals.referrer ```  ``` candidates.followers = opportunity_referrals.user ```  ``` candidates.owner = opportunity_referrals.user ```  ``` candidates.stageChanges.userId = opportunity_referrals.user ``` |
| [postings](#postings) | ``` candidates.followers = postings.followers ```  ``` candidates.owner = postings.followers ```  ``` candidates.stageChanges.userId = postings.followers ```  ``` candidates.followers = postings.hiringManager ```  ``` candidates.owner = postings.hiringManager ```  ``` candidates.stageChanges.userId = postings.hiringManager ```  ``` candidates.followers = postings.owner ```  ``` candidates.owner = postings.owner ```  ``` candidates.stageChanges.userId = postings.owner ```  ``` candidates.followers = postings.user ```  ``` candidates.owner = postings.user ```  ``` candidates.stageChanges.userId = postings.user ``` |
| [requisitions](#requisitions) | ``` candidates.followers = requisitions.creator ```  ``` candidates.owner = requisitions.creator ```  ``` candidates.stageChanges.userId = requisitions.creator ```  ``` candidates.followers = requisitions.hiringManager ```  ``` candidates.owner = requisitions.hiringManager ```  ``` candidates.stageChanges.userId = requisitions.hiringManager ```  ``` candidates.followers = requisitions.owner ```  ``` candidates.owner = requisitions.owner ```  ``` candidates.stageChanges.userId = requisitions.owner ``` |

candidates table schema

|  |
| --- |
| **applications**  ARRAY This is a nested data structure. |
| **archived**  OBJECT This is a nested data structure:   - archivedAt: DATE-TIME - reason: STRING |
| **contact**  STRING |
| **createdAt**  DATE-TIME |
| **dataProtection**  OBJECT This is a nested data structure. |
| **emails**  ARRAY This is a nested data structure. |
| **followers**  ARRAY This is a nested data structure. |
| **headline**  STRING |
| **id**  STRING |
| **isAnonymized**  BOOLEAN |
| **lastAdvancedAt**  DATE-TIME |
| **lastInteractionAt**  DATE-TIME |
| **links**  ARRAY This is a nested data structure. |
| **location**  STRING |
| **name**  STRING |
| **origin**  STRING |
| **owner**  STRING |
| **phones**  ARRAY This is a nested data structure:   - type: STRING - value: STRING |
| **resume**  OBJECT This is a nested data structure. |
| **snoozedUntil**  DATE-TIME |
| **sources**  ARRAY This is a nested data structure. |
| **stage**  STRING |
| **stageChanges**  ARRAY This is a nested data structure. |
| **tags**  ARRAY This is a nested data structure. |
| **urls**  OBJECT This is a nested data structure. |

### opportunities

The `opportunities` table contains info about opportunities. In Lever, an opportunity represents each of an individual candidate’s unique candidacies or journeys through your hiring pipeline for a position. A candidate can be associated with multiple opportunities.

**Note**: This table must be set to replicate in order to replicate the `opportunity_applications`, `opportunity_offers`, `opportunity_referrals`, and `opportunity_resumes` tables.

During Extraction, this table will be replicated before any other selected `opportunity_*` tables. Then, for every opportunity, Stitch will query for every opportunity’s applications, offers, referrals, and resumes.

For example: During Extraction, Stitch replicates an opportunity with `id: 12345` from Lever’s `/opportunities` endpoint.

Using `id: 12345`, Stitch will then query for the rest of the opportunity’s data:

- `/opportunities/12345/applications`
- `/opportunities/12345/offers`
- `/opportunities/12345/referrals`
- `/opportunities/12345/resumes`

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Lever documentation](https://hire.lever.co/developer/documentation#opportunities)  [Lever API method](https://hire.lever.co/developer/documentation#list-all-opportunities "Opens in new tab: Lever API method") |

opportunities table foreign keys

| Join opportunities with | on |
| --- | --- |
| [archive\_reasons](#archive-reasons) | ``` opportunities.archived.reason = archive_reasons.id ``` |
| [candidate\_applications](#candidate-applications) | ``` opportunities.archived.reason = candidate_applications.archived.reason ```  ``` opportunities.applications = candidate_applications.id ```  ``` opportunities.id = candidate_applications.candidateId ```  ``` opportunities.followers = candidate_applications.postingHiringManager ```  ``` opportunities.owner = candidate_applications.postingHiringManager ```  ``` opportunities.stageChanges.userId = candidate_applications.postingHiringManager ```  ``` opportunities.followers = candidate_applications.postingOwner ```  ``` opportunities.owner = candidate_applications.postingOwner ```  ``` opportunities.stageChanges.userId = candidate_applications.postingOwner ```  ``` opportunities.followers = candidate_applications.requisitionForHire.hiringManagerOnHire ```  ``` opportunities.owner = candidate_applications.requisitionForHire.hiringManagerOnHire ```  ``` opportunities.stageChanges.userId = candidate_applications.requisitionForHire.hiringManagerOnHire ```  ``` opportunities.followers = candidate_applications.user ```  ``` opportunities.owner = candidate_applications.user ```  ``` opportunities.stageChanges.userId = candidate_applications.user ``` |
| [candidates](#candidates) | ``` opportunities.archived.reason = candidates.archived.reason ```  ``` opportunities.applications = candidates.applications ```  ``` opportunities.contact = candidates.contact ```  ``` opportunities.id = candidates.id ```  ``` opportunities.stage = candidates.stage ```  ``` opportunities.stageChanges.toStageId = candidates.stage ```  ``` opportunities.stage = candidates.stageChanges.toStageId ```  ``` opportunities.stageChanges.toStageId = candidates.stageChanges.toStageId ```  ``` opportunities.followers = candidates.followers ```  ``` opportunities.owner = candidates.followers ```  ``` opportunities.stageChanges.userId = candidates.followers ```  ``` opportunities.followers = candidates.owner ```  ``` opportunities.owner = candidates.owner ```  ``` opportunities.stageChanges.userId = candidates.owner ```  ``` opportunities.followers = candidates.stageChanges.userId ```  ``` opportunities.owner = candidates.stageChanges.userId ```  ``` opportunities.stageChanges.userId = candidates.stageChanges.userId ``` |
| [opportunity\_applications](#opportunity-applications) | ``` opportunities.archived.reason = opportunity_applications.archived.reason ```  ``` opportunities.applications = opportunity_applications.id ```  ``` opportunities.id = opportunity_applications.candidateId ```  ``` opportunities.followers = opportunity_applications.postingHiringManager ```  ``` opportunities.owner = opportunity_applications.postingHiringManager ```  ``` opportunities.stageChanges.userId = opportunity_applications.postingHiringManager ```  ``` opportunities.followers = opportunity_applications.postingOwner ```  ``` opportunities.owner = opportunity_applications.postingOwner ```  ``` opportunities.stageChanges.userId = opportunity_applications.postingOwner ```  ``` opportunities.followers = opportunity_applications.requisitionForHire.hiringManagerOnHire ```  ``` opportunities.owner = opportunity_applications.requisitionForHire.hiringManagerOnHire ```  ``` opportunities.stageChanges.userId = opportunity_applications.requisitionForHire.hiringManagerOnHire ```  ``` opportunities.followers = opportunity_applications.user ```  ``` opportunities.owner = opportunity_applications.user ```  ``` opportunities.stageChanges.userId = opportunity_applications.user ``` |
| [opportunity\_offers](#opportunity-offers) | ``` opportunities.id = opportunity_offers.opportunityId ```  ``` opportunities.followers = opportunity_offers.creator ```  ``` opportunities.owner = opportunity_offers.creator ```  ``` opportunities.stageChanges.userId = opportunity_offers.creator ``` |
| [stages](#stages) | ``` opportunities.stage = stages.id ```  ``` opportunities.stageChanges.toStageId = stages.id ``` |
| [candidate\_offers](#candidate-offers) | ``` opportunities.followers = candidate_offers.creator ```  ``` opportunities.owner = candidate_offers.creator ```  ``` opportunities.stageChanges.userId = candidate_offers.creator ``` |
| [candidate\_referrals](#candidate-referrals) | ``` opportunities.followers = candidate_referrals.referrer ```  ``` opportunities.owner = candidate_referrals.referrer ```  ``` opportunities.stageChanges.userId = candidate_referrals.referrer ```  ``` opportunities.followers = candidate_referrals.user ```  ``` opportunities.owner = candidate_referrals.user ```  ``` opportunities.stageChanges.userId = candidate_referrals.user ``` |
| [opportunity\_referrals](#opportunity-referrals) | ``` opportunities.followers = opportunity_referrals.referrer ```  ``` opportunities.owner = opportunity_referrals.referrer ```  ``` opportunities.stageChanges.userId = opportunity_referrals.referrer ```  ``` opportunities.followers = opportunity_referrals.user ```  ``` opportunities.owner = opportunity_referrals.user ```  ``` opportunities.stageChanges.userId = opportunity_referrals.user ``` |
| [postings](#postings) | ``` opportunities.followers = postings.followers ```  ``` opportunities.owner = postings.followers ```  ``` opportunities.stageChanges.userId = postings.followers ```  ``` opportunities.followers = postings.hiringManager ```  ``` opportunities.owner = postings.hiringManager ```  ``` opportunities.stageChanges.userId = postings.hiringManager ```  ``` opportunities.followers = postings.owner ```  ``` opportunities.owner = postings.owner ```  ``` opportunities.stageChanges.userId = postings.owner ```  ``` opportunities.followers = postings.user ```  ``` opportunities.owner = postings.user ```  ``` opportunities.stageChanges.userId = postings.user ``` |
| [requisitions](#requisitions) | ``` opportunities.followers = requisitions.creator ```  ``` opportunities.owner = requisitions.creator ```  ``` opportunities.stageChanges.userId = requisitions.creator ```  ``` opportunities.followers = requisitions.hiringManager ```  ``` opportunities.owner = requisitions.hiringManager ```  ``` opportunities.stageChanges.userId = requisitions.hiringManager ```  ``` opportunities.followers = requisitions.owner ```  ``` opportunities.owner = requisitions.owner ```  ``` opportunities.stageChanges.userId = requisitions.owner ``` |

opportunities table schema

|  |
| --- |
| **applications**  ARRAY This is a nested data structure. |
| **archived**  OBJECT This is a nested data structure:   - archivedAt: DATE-TIME - reason: STRING |
| **contact**  STRING |
| **createdAt**  DATE-TIME |
| **dataProtection**  OBJECT This is a nested data structure.  This is a nested data structure. |
| **emails**  ARRAY This is a nested data structure. |
| **followers**  ARRAY This is a nested data structure. |
| **headline**  STRING |
| **id**  STRING |
| **isAnonymized**  BOOLEAN |
| **lastAdvancedAt**  DATE-TIME |
| **lastInteractionAt**  DATE-TIME |
| **links**  ARRAY This is a nested data structure. |
| **location**  STRING |
| **name**  STRING |
| **origin**  STRING |
| **owner**  STRING |
| **phones**  ARRAY This is a nested data structure:   - type: STRING - value: STRING |
| **snoozedUntil**  DATE-TIME |
| **sources**  ARRAY This is a nested data structure. |
| **stage**  STRING |
| **stageChanges**  ARRAY This is a nested data structure. |
| **tags**  ARRAY This is a nested data structure. |
| **urls**  OBJECT This is a nested data structure. |

### opportunity\_applications

The `opportunity_applications` table contains info about candidate applications in your Lever account.

**Note**: To replicate this table, the [`opportunities`](#opportunities) table must be set to replicate.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Lever API method](https://hire.lever.co/developer/documentation#list-all-opportunities "Opens in new tab: Lever API method") |

opportunity\_applications table foreign keys

| Join opportunity\_applications with | on |
| --- | --- |
| [archive\_reasons](#archive-reasons) | ``` opportunity_applications.archived.reason = archive_reasons.id ``` |
| [candidate\_applications](#candidate-applications) | ``` opportunity_applications.archived.reason = candidate_applications.archived.reason ```  ``` opportunity_applications.id = candidate_applications.id ```  ``` opportunity_applications.candidateId = candidate_applications.candidateId ```  ``` opportunity_applications.posting = candidate_applications.posting ```  ``` opportunity_applications.requisitionForHire.id = candidate_applications.requisitionForHire.id ```  ``` opportunity_applications.postingHiringManager = candidate_applications.postingHiringManager ```  ``` opportunity_applications.postingOwner = candidate_applications.postingHiringManager ```  ``` opportunity_applications.requisitionForHire.hiringManagerOnHire = candidate_applications.postingHiringManager ```  ``` opportunity_applications.user = candidate_applications.postingHiringManager ```  ``` opportunity_applications.postingHiringManager = candidate_applications.postingOwner ```  ``` opportunity_applications.postingOwner = candidate_applications.postingOwner ```  ``` opportunity_applications.requisitionForHire.hiringManagerOnHire = candidate_applications.postingOwner ```  ``` opportunity_applications.user = candidate_applications.postingOwner ```  ``` opportunity_applications.postingHiringManager = candidate_applications.requisitionForHire.hiringManagerOnHire ```  ``` opportunity_applications.postingOwner = candidate_applications.requisitionForHire.hiringManagerOnHire ```  ``` opportunity_applications.requisitionForHire.hiringManagerOnHire = candidate_applications.requisitionForHire.hiringManagerOnHire ```  ``` opportunity_applications.user = candidate_applications.requisitionForHire.hiringManagerOnHire ```  ``` opportunity_applications.postingHiringManager = candidate_applications.user ```  ``` opportunity_applications.postingOwner = candidate_applications.user ```  ``` opportunity_applications.requisitionForHire.hiringManagerOnHire = candidate_applications.user ```  ``` opportunity_applications.user = candidate_applications.user ``` |
| [candidates](#candidates) | ``` opportunity_applications.archived.reason = candidates.archived.reason ```  ``` opportunity_applications.id = candidates.applications ```  ``` opportunity_applications.candidateId = candidates.id ```  ``` opportunity_applications.postingHiringManager = candidates.followers ```  ``` opportunity_applications.postingOwner = candidates.followers ```  ``` opportunity_applications.requisitionForHire.hiringManagerOnHire = candidates.followers ```  ``` opportunity_applications.user = candidates.followers ```  ``` opportunity_applications.postingHiringManager = candidates.owner ```  ``` opportunity_applications.postingOwner = candidates.owner ```  ``` opportunity_applications.requisitionForHire.hiringManagerOnHire = candidates.owner ```  ``` opportunity_applications.user = candidates.owner ```  ``` opportunity_applications.postingHiringManager = candidates.stageChanges.userId ```  ``` opportunity_applications.postingOwner = candidates.stageChanges.userId ```  ``` opportunity_applications.requisitionForHire.hiringManagerOnHire = candidates.stageChanges.userId ```  ``` opportunity_applications.user = candidates.stageChanges.userId ``` |
| [opportunities](#opportunities) | ``` opportunity_applications.archived.reason = opportunities.archived.reason ```  ``` opportunity_applications.id = opportunities.applications ```  ``` opportunity_applications.candidateId = opportunities.id ```  ``` opportunity_applications.postingHiringManager = opportunities.followers ```  ``` opportunity_applications.postingOwner = opportunities.followers ```  ``` opportunity_applications.requisitionForHire.hiringManagerOnHire = opportunities.followers ```  ``` opportunity_applications.user = opportunities.followers ```  ``` opportunity_applications.postingHiringManager = opportunities.owner ```  ``` opportunity_applications.postingOwner = opportunities.owner ```  ``` opportunity_applications.requisitionForHire.hiringManagerOnHire = opportunities.owner ```  ``` opportunity_applications.user = opportunities.owner ```  ``` opportunity_applications.postingHiringManager = opportunities.stageChanges.userId ```  ``` opportunity_applications.postingOwner = opportunities.stageChanges.userId ```  ``` opportunity_applications.requisitionForHire.hiringManagerOnHire = opportunities.stageChanges.userId ```  ``` opportunity_applications.user = opportunities.stageChanges.userId ``` |
| [opportunity\_offers](#opportunity-offers) | ``` opportunity_applications.candidateId = opportunity_offers.opportunityId ```  ``` opportunity_applications.posting = opportunity_offers.posting ```  ``` opportunity_applications.postingHiringManager = opportunity_offers.creator ```  ``` opportunity_applications.postingOwner = opportunity_offers.creator ```  ``` opportunity_applications.requisitionForHire.hiringManagerOnHire = opportunity_offers.creator ```  ``` opportunity_applications.user = opportunity_offers.creator ``` |
| [postings](#postings) | ``` opportunity_applications.posting = postings.id ```  ``` opportunity_applications.postingHiringManager = postings.followers ```  ``` opportunity_applications.postingOwner = postings.followers ```  ``` opportunity_applications.requisitionForHire.hiringManagerOnHire = postings.followers ```  ``` opportunity_applications.user = postings.followers ```  ``` opportunity_applications.postingHiringManager = postings.hiringManager ```  ``` opportunity_applications.postingOwner = postings.hiringManager ```  ``` opportunity_applications.requisitionForHire.hiringManagerOnHire = postings.hiringManager ```  ``` opportunity_applications.user = postings.hiringManager ```  ``` opportunity_applications.postingHiringManager = postings.owner ```  ``` opportunity_applications.postingOwner = postings.owner ```  ``` opportunity_applications.requisitionForHire.hiringManagerOnHire = postings.owner ```  ``` opportunity_applications.user = postings.owner ```  ``` opportunity_applications.postingHiringManager = postings.user ```  ``` opportunity_applications.postingOwner = postings.user ```  ``` opportunity_applications.requisitionForHire.hiringManagerOnHire = postings.user ```  ``` opportunity_applications.user = postings.user ``` |
| [requisitions](#requisitions) | ``` opportunity_applications.posting = requisitions.postings ```  ``` opportunity_applications.requisitionForHire.id = requisitions.id ```  ``` opportunity_applications.postingHiringManager = requisitions.creator ```  ``` opportunity_applications.postingOwner = requisitions.creator ```  ``` opportunity_applications.requisitionForHire.hiringManagerOnHire = requisitions.creator ```  ``` opportunity_applications.user = requisitions.creator ```  ``` opportunity_applications.postingHiringManager = requisitions.hiringManager ```  ``` opportunity_applications.postingOwner = requisitions.hiringManager ```  ``` opportunity_applications.requisitionForHire.hiringManagerOnHire = requisitions.hiringManager ```  ``` opportunity_applications.user = requisitions.hiringManager ```  ``` opportunity_applications.postingHiringManager = requisitions.owner ```  ``` opportunity_applications.postingOwner = requisitions.owner ```  ``` opportunity_applications.requisitionForHire.hiringManagerOnHire = requisitions.owner ```  ``` opportunity_applications.user = requisitions.owner ``` |
| [candidate\_offers](#candidate-offers) | ``` opportunity_applications.postingHiringManager = candidate_offers.creator ```  ``` opportunity_applications.postingOwner = candidate_offers.creator ```  ``` opportunity_applications.requisitionForHire.hiringManagerOnHire = candidate_offers.creator ```  ``` opportunity_applications.user = candidate_offers.creator ``` |
| [candidate\_referrals](#candidate-referrals) | ``` opportunity_applications.postingHiringManager = candidate_referrals.referrer ```  ``` opportunity_applications.postingOwner = candidate_referrals.referrer ```  ``` opportunity_applications.requisitionForHire.hiringManagerOnHire = candidate_referrals.referrer ```  ``` opportunity_applications.user = candidate_referrals.referrer ```  ``` opportunity_applications.postingHiringManager = candidate_referrals.user ```  ``` opportunity_applications.postingOwner = candidate_referrals.user ```  ``` opportunity_applications.requisitionForHire.hiringManagerOnHire = candidate_referrals.user ```  ``` opportunity_applications.user = candidate_referrals.user ``` |
| [opportunity\_referrals](#opportunity-referrals) | ``` opportunity_applications.postingHiringManager = opportunity_referrals.referrer ```  ``` opportunity_applications.postingOwner = opportunity_referrals.referrer ```  ``` opportunity_applications.requisitionForHire.hiringManagerOnHire = opportunity_referrals.referrer ```  ``` opportunity_applications.user = opportunity_referrals.referrer ```  ``` opportunity_applications.postingHiringManager = opportunity_referrals.user ```  ``` opportunity_applications.postingOwner = opportunity_referrals.user ```  ``` opportunity_applications.requisitionForHire.hiringManagerOnHire = opportunity_referrals.user ```  ``` opportunity_applications.user = opportunity_referrals.user ``` |

opportunity\_applications table schema

|  |
| --- |
| **candidateId**  STRING |
| **createdAt**  NUMBER |
| **email**  STRING |
| **id**  STRING |
| **name**  STRING |
| **posting**  STRING |
| **type**  STRING |
| **user**  STRING |

### opportunity\_offers

The `opportunity_offers` table contains info about

**Note**: To replicate this table, the [`opportunities`](#opportunities) table must be set to replicate.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Useful links** | [Lever documentation](https://hire.lever.co/developer/documentation#opportunities)  [Lever API method](https://hire.lever.co/developer/documentation#list-all-opportunities "Opens in new tab: Lever API method") |

opportunity\_offers table foreign keys

| Join opportunity\_offers with | on |
| --- | --- |
| [candidate\_offers](#candidate-offers) | ``` opportunity_offers.id = candidate_offers.id ```  ``` opportunity_offers.creator = candidate_offers.creator ``` |
| [requisitions](#requisitions) | ``` opportunity_offers.id = requisitions.offerIds ```  ``` opportunity_offers.posting = requisitions.postings ```  ``` opportunity_offers.creator = requisitions.creator ```  ``` opportunity_offers.creator = requisitions.hiringManager ```  ``` opportunity_offers.creator = requisitions.owner ``` |
| [candidate\_applications](#candidate-applications) | ``` opportunity_offers.opportunityId = candidate_applications.candidateId ```  ``` opportunity_offers.posting = candidate_applications.posting ```  ``` opportunity_offers.creator = candidate_applications.postingHiringManager ```  ``` opportunity_offers.creator = candidate_applications.postingOwner ```  ``` opportunity_offers.creator = candidate_applications.requisitionForHire.hiringManagerOnHire ```  ``` opportunity_offers.creator = candidate_applications.user ``` |
| [candidates](#candidates) | ``` opportunity_offers.opportunityId = candidates.id ```  ``` opportunity_offers.creator = candidates.followers ```  ``` opportunity_offers.creator = candidates.owner ```  ``` opportunity_offers.creator = candidates.stageChanges.userId ``` |
| [opportunity\_applications](#opportunity-applications) | ``` opportunity_offers.opportunityId = opportunity_applications.candidateId ```  ``` opportunity_offers.posting = opportunity_applications.posting ```  ``` opportunity_offers.creator = opportunity_applications.postingHiringManager ```  ``` opportunity_offers.creator = opportunity_applications.postingOwner ```  ``` opportunity_offers.creator = opportunity_applications.requisitionForHire.hiringManagerOnHire ```  ``` opportunity_offers.creator = opportunity_applications.user ``` |
| [opportunities](#opportunities) | ``` opportunity_offers.opportunityId = opportunities.id ```  ``` opportunity_offers.creator = opportunities.followers ```  ``` opportunity_offers.creator = opportunities.owner ```  ``` opportunity_offers.creator = opportunities.stageChanges.userId ``` |
| [postings](#postings) | ``` opportunity_offers.posting = postings.id ```  ``` opportunity_offers.creator = postings.followers ```  ``` opportunity_offers.creator = postings.hiringManager ```  ``` opportunity_offers.creator = postings.owner ```  ``` opportunity_offers.creator = postings.user ``` |
| [candidate\_referrals](#candidate-referrals) | ``` opportunity_offers.creator = candidate_referrals.referrer ```  ``` opportunity_offers.creator = candidate_referrals.user ``` |
| [opportunity\_referrals](#opportunity-referrals) | ``` opportunity_offers.creator = opportunity_referrals.referrer ```  ``` opportunity_offers.creator = opportunity_referrals.user ``` |

opportunity\_offers table schema

|  |
| --- |
| **approved**  BOOLEAN |
| **approvedAt**  DATE-TIME |
| **createdAt**  DATE-TIME |
| **creator**  STRING |
| **fields**  ARRAY This is a nested data structure:   - identifier: STRING - text: STRING - value: STRING |
| **id**  STRING |
| **opportunityId**  STRING |
| **posting**  STRING |
| **sentAt**  DATE-TIME |
| **sentDocument**  OBJECT This is a nested data structure:   - downloadUrl: STRING - fileName: STRING - uploadedAt: DATE-TIME |
| **signatures**  OBJECT This is a nested data structure:   - candidate: OBJECT, which is also a nested data structure.   - email: STRING   - firstOpenedAt: DATE-TIME   - lastOpenedAt: DATE-TIME   - name: STRING   - role: STRING   - signed: BOOLEAN   - signedAt: DATE-TIME - email: STRING - firstOpenedAt: DATE-TIME - lastOpenedAt: DATE-TIME - name: STRING - role: STRING - signed: BOOLEAN - signedAt: DATE-TIME |
| **signedDocument**  OBJECT This is a nested data structure:   - downloadUrl: STRING - fileName: STRING - uploadedAt: DATE-TIME |
| **status**  STRING |

### opportunity\_referrals

The `opportunity_referrals` table contains info about the referrals in your Lever account.

**Note**: To replicate this table, the [`opportunities`](#opportunities) table must be set to replicate.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Lever documentation](https://hire.lever.co/developer/documentation#opportunities)  [Lever API method](https://hire.lever.co/developer/documentation#list-all-opportunities "Opens in new tab: Lever API method") |

opportunity\_referrals table foreign keys

| Join opportunity\_referrals with | on |
| --- | --- |
| [candidate\_referrals](#candidate-referrals) | ``` opportunity_referrals.id = candidate_referrals.id ```  ``` opportunity_referrals.referrer = candidate_referrals.referrer ```  ``` opportunity_referrals.user = candidate_referrals.referrer ```  ``` opportunity_referrals.referrer = candidate_referrals.user ```  ``` opportunity_referrals.user = candidate_referrals.user ``` |
| [candidate\_applications](#candidate-applications) | ``` opportunity_referrals.referrer = candidate_applications.postingHiringManager ```  ``` opportunity_referrals.user = candidate_applications.postingHiringManager ```  ``` opportunity_referrals.referrer = candidate_applications.postingOwner ```  ``` opportunity_referrals.user = candidate_applications.postingOwner ```  ``` opportunity_referrals.referrer = candidate_applications.requisitionForHire.hiringManagerOnHire ```  ``` opportunity_referrals.user = candidate_applications.requisitionForHire.hiringManagerOnHire ```  ``` opportunity_referrals.referrer = candidate_applications.user ```  ``` opportunity_referrals.user = candidate_applications.user ``` |
| [candidate\_offers](#candidate-offers) | ``` opportunity_referrals.referrer = candidate_offers.creator ```  ``` opportunity_referrals.user = candidate_offers.creator ``` |
| [candidates](#candidates) | ``` opportunity_referrals.referrer = candidates.followers ```  ``` opportunity_referrals.user = candidates.followers ```  ``` opportunity_referrals.referrer = candidates.owner ```  ``` opportunity_referrals.user = candidates.owner ```  ``` opportunity_referrals.referrer = candidates.stageChanges.userId ```  ``` opportunity_referrals.user = candidates.stageChanges.userId ``` |
| [opportunities](#opportunities) | ``` opportunity_referrals.referrer = opportunities.followers ```  ``` opportunity_referrals.user = opportunities.followers ```  ``` opportunity_referrals.referrer = opportunities.owner ```  ``` opportunity_referrals.user = opportunities.owner ```  ``` opportunity_referrals.referrer = opportunities.stageChanges.userId ```  ``` opportunity_referrals.user = opportunities.stageChanges.userId ``` |
| [opportunity\_applications](#opportunity-applications) | ``` opportunity_referrals.referrer = opportunity_applications.postingHiringManager ```  ``` opportunity_referrals.user = opportunity_applications.postingHiringManager ```  ``` opportunity_referrals.referrer = opportunity_applications.postingOwner ```  ``` opportunity_referrals.user = opportunity_applications.postingOwner ```  ``` opportunity_referrals.referrer = opportunity_applications.requisitionForHire.hiringManagerOnHire ```  ``` opportunity_referrals.user = opportunity_applications.requisitionForHire.hiringManagerOnHire ```  ``` opportunity_referrals.referrer = opportunity_applications.user ```  ``` opportunity_referrals.user = opportunity_applications.user ``` |
| [opportunity\_offers](#opportunity-offers) | ``` opportunity_referrals.referrer = opportunity_offers.creator ```  ``` opportunity_referrals.user = opportunity_offers.creator ``` |
| [postings](#postings) | ``` opportunity_referrals.referrer = postings.followers ```  ``` opportunity_referrals.user = postings.followers ```  ``` opportunity_referrals.referrer = postings.hiringManager ```  ``` opportunity_referrals.user = postings.hiringManager ```  ``` opportunity_referrals.referrer = postings.owner ```  ``` opportunity_referrals.user = postings.owner ```  ``` opportunity_referrals.referrer = postings.user ```  ``` opportunity_referrals.user = postings.user ``` |
| [requisitions](#requisitions) | ``` opportunity_referrals.referrer = requisitions.creator ```  ``` opportunity_referrals.user = requisitions.creator ```  ``` opportunity_referrals.referrer = requisitions.hiringManager ```  ``` opportunity_referrals.user = requisitions.hiringManager ```  ``` opportunity_referrals.referrer = requisitions.owner ```  ``` opportunity_referrals.user = requisitions.owner ``` |

opportunity\_referrals table schema

|  |
| --- |
| **baseTemplateId**  STRING |
| **completedAt**  DATE-TIME |
| **createdAt**  DATE-TIME |
| **fields**  ARRAY This is a nested data structure:   - description: STRING - options: ARRAY, which is also a nested data structure.   - text: STRING - prompt: STRING - required: BOOLEAN - text: STRING - type: STRING - value: STRING |
| **id**  STRING |
| **instructions**  STRING |
| **referrer**  STRING |
| **stage**  STRING |
| **text**  STRING |
| **type**  STRING |
| **user**  STRING |

### opportunity\_resumes

The `opportunity_resumes` table contains info about candidate resumes.

**Note**: To replicate this table, the [`opportunities`](#opportunities) table must be set to replicate.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Lever documentation](https://hire.lever.co/developer/documentation#opportunities)  [Lever API method](https://hire.lever.co/developer/documentation#list-all-opportunities "Opens in new tab: Lever API method") |

opportunity\_resumes table foreign keys

| Join opportunity\_resumes with | on |
| --- | --- |
| [candidate\_resumes](#candidate-resumes) | ``` opportunity_resumes.id = candidate_resumes.id ``` |

opportunity\_resumes table schema

|  |
| --- |
| **createdAt**  DATE-TIME |
| **file**  OBJECT This is a nested data structure. |
| **id**  STRING |
| **parsedData**  OBJECT This is a nested data structure. |

### postings

The `postings` table contains info about job postings in your Lever account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [Lever documentation](https://hire.lever.co/developer/documentation#postings)  [Lever API method](https://hire.lever.co/developer/documentation#list-all-postings "Opens in new tab: Lever API method") |

postings table foreign keys

| Join postings with | on |
| --- | --- |
| [candidate\_applications](#candidate-applications) | ``` postings.id = candidate_applications.posting ```  ``` postings.followers = candidate_applications.postingHiringManager ```  ``` postings.hiringManager = candidate_applications.postingHiringManager ```  ``` postings.owner = candidate_applications.postingHiringManager ```  ``` postings.user = candidate_applications.postingHiringManager ```  ``` postings.followers = candidate_applications.postingOwner ```  ``` postings.hiringManager = candidate_applications.postingOwner ```  ``` postings.owner = candidate_applications.postingOwner ```  ``` postings.user = candidate_applications.postingOwner ```  ``` postings.followers = candidate_applications.requisitionForHire.hiringManagerOnHire ```  ``` postings.hiringManager = candidate_applications.requisitionForHire.hiringManagerOnHire ```  ``` postings.owner = candidate_applications.requisitionForHire.hiringManagerOnHire ```  ``` postings.user = candidate_applications.requisitionForHire.hiringManagerOnHire ```  ``` postings.followers = candidate_applications.user ```  ``` postings.hiringManager = candidate_applications.user ```  ``` postings.owner = candidate_applications.user ```  ``` postings.user = candidate_applications.user ``` |
| [opportunity\_applications](#opportunity-applications) | ``` postings.id = opportunity_applications.posting ```  ``` postings.followers = opportunity_applications.postingHiringManager ```  ``` postings.hiringManager = opportunity_applications.postingHiringManager ```  ``` postings.owner = opportunity_applications.postingHiringManager ```  ``` postings.user = opportunity_applications.postingHiringManager ```  ``` postings.followers = opportunity_applications.postingOwner ```  ``` postings.hiringManager = opportunity_applications.postingOwner ```  ``` postings.owner = opportunity_applications.postingOwner ```  ``` postings.user = opportunity_applications.postingOwner ```  ``` postings.followers = opportunity_applications.requisitionForHire.hiringManagerOnHire ```  ``` postings.hiringManager = opportunity_applications.requisitionForHire.hiringManagerOnHire ```  ``` postings.owner = opportunity_applications.requisitionForHire.hiringManagerOnHire ```  ``` postings.user = opportunity_applications.requisitionForHire.hiringManagerOnHire ```  ``` postings.followers = opportunity_applications.user ```  ``` postings.hiringManager = opportunity_applications.user ```  ``` postings.owner = opportunity_applications.user ```  ``` postings.user = opportunity_applications.user ``` |
| [opportunity\_offers](#opportunity-offers) | ``` postings.id = opportunity_offers.posting ```  ``` postings.followers = opportunity_offers.creator ```  ``` postings.hiringManager = opportunity_offers.creator ```  ``` postings.owner = opportunity_offers.creator ```  ``` postings.user = opportunity_offers.creator ``` |
| [requisitions](#requisitions) | ``` postings.id = requisitions.postings ```  ``` postings.followers = requisitions.creator ```  ``` postings.hiringManager = requisitions.creator ```  ``` postings.owner = requisitions.creator ```  ``` postings.user = requisitions.creator ```  ``` postings.followers = requisitions.hiringManager ```  ``` postings.hiringManager = requisitions.hiringManager ```  ``` postings.owner = requisitions.hiringManager ```  ``` postings.user = requisitions.hiringManager ```  ``` postings.followers = requisitions.owner ```  ``` postings.hiringManager = requisitions.owner ```  ``` postings.owner = requisitions.owner ```  ``` postings.user = requisitions.owner ``` |
| [candidate\_offers](#candidate-offers) | ``` postings.followers = candidate_offers.creator ```  ``` postings.hiringManager = candidate_offers.creator ```  ``` postings.owner = candidate_offers.creator ```  ``` postings.user = candidate_offers.creator ``` |
| [candidate\_referrals](#candidate-referrals) | ``` postings.followers = candidate_referrals.referrer ```  ``` postings.hiringManager = candidate_referrals.referrer ```  ``` postings.owner = candidate_referrals.referrer ```  ``` postings.user = candidate_referrals.referrer ```  ``` postings.followers = candidate_referrals.user ```  ``` postings.hiringManager = candidate_referrals.user ```  ``` postings.owner = candidate_referrals.user ```  ``` postings.user = candidate_referrals.user ``` |
| [candidates](#candidates) | ``` postings.followers = candidates.followers ```  ``` postings.hiringManager = candidates.followers ```  ``` postings.owner = candidates.followers ```  ``` postings.user = candidates.followers ```  ``` postings.followers = candidates.owner ```  ``` postings.hiringManager = candidates.owner ```  ``` postings.owner = candidates.owner ```  ``` postings.user = candidates.owner ```  ``` postings.followers = candidates.stageChanges.userId ```  ``` postings.hiringManager = candidates.stageChanges.userId ```  ``` postings.owner = candidates.stageChanges.userId ```  ``` postings.user = candidates.stageChanges.userId ``` |
| [opportunities](#opportunities) | ``` postings.followers = opportunities.followers ```  ``` postings.hiringManager = opportunities.followers ```  ``` postings.owner = opportunities.followers ```  ``` postings.user = opportunities.followers ```  ``` postings.followers = opportunities.owner ```  ``` postings.hiringManager = opportunities.owner ```  ``` postings.owner = opportunities.owner ```  ``` postings.user = opportunities.owner ```  ``` postings.followers = opportunities.stageChanges.userId ```  ``` postings.hiringManager = opportunities.stageChanges.userId ```  ``` postings.owner = opportunities.stageChanges.userId ```  ``` postings.user = opportunities.stageChanges.userId ``` |
| [opportunity\_referrals](#opportunity-referrals) | ``` postings.followers = opportunity_referrals.referrer ```  ``` postings.hiringManager = opportunity_referrals.referrer ```  ``` postings.owner = opportunity_referrals.referrer ```  ``` postings.user = opportunity_referrals.referrer ```  ``` postings.followers = opportunity_referrals.user ```  ``` postings.hiringManager = opportunity_referrals.user ```  ``` postings.owner = opportunity_referrals.user ```  ``` postings.user = opportunity_referrals.user ``` |

postings table schema

|  |
| --- |
| **categories**  OBJECT This is a nested data structure:   - commitment: STRING - department: STRING - level: STRING - location: STRING - team: STRING |
| **content**  OBJECT This is a nested data structure:   - closing: STRING - customQuestions: ARRAY, which is also a nested data structure. - description: STRING - lists: ARRAY, which is also a nested data structure.   - content: STRING   - text: STRING |
| **createdAt**  DATE-TIME |
| **distributionChannels**  ARRAY This is a nested data structure. |
| **followers**  STRING |
| **hiringManager**  STRING |
| **id**  STRING |
| **owner**  STRING |
| **reqCode**  STRING |
| **state**  STRING |
| **tags**  ARRAY This is a nested data structure. |
| **text**  STRING |
| **updatedAt**  DATE-TIME |
| **urls**  OBJECT This is a nested data structure:   - apply: STRING - list: STRING - show: STRING |
| **user**  STRING |

### requisitions

The `requisitions` table contains info about requisitions in your Lever account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | createdAt |
| **Useful links** | [Lever documentation](https://hire.lever.co/developer/documentation#requisitions)  [Lever API method](https://hire.lever.co/developer/documentation#list-all-requisitions "Opens in new tab: Lever API method") |

requisitions table foreign keys

| Join requisitions with | on |
| --- | --- |
| [candidate\_offers](#candidate-offers) | ``` requisitions.offerIds = candidate_offers.id ```  ``` requisitions.creator = candidate_offers.creator ```  ``` requisitions.hiringManager = candidate_offers.creator ```  ``` requisitions.owner = candidate_offers.creator ``` |
| [opportunity\_offers](#opportunity-offers) | ``` requisitions.offerIds = opportunity_offers.id ```  ``` requisitions.postings = opportunity_offers.posting ```  ``` requisitions.creator = opportunity_offers.creator ```  ``` requisitions.hiringManager = opportunity_offers.creator ```  ``` requisitions.owner = opportunity_offers.creator ``` |
| [candidate\_applications](#candidate-applications) | ``` requisitions.postings = candidate_applications.posting ```  ``` requisitions.id = candidate_applications.requisitionForHire.id ```  ``` requisitions.creator = candidate_applications.postingHiringManager ```  ``` requisitions.hiringManager = candidate_applications.postingHiringManager ```  ``` requisitions.owner = candidate_applications.postingHiringManager ```  ``` requisitions.creator = candidate_applications.postingOwner ```  ``` requisitions.hiringManager = candidate_applications.postingOwner ```  ``` requisitions.owner = candidate_applications.postingOwner ```  ``` requisitions.creator = candidate_applications.requisitionForHire.hiringManagerOnHire ```  ``` requisitions.hiringManager = candidate_applications.requisitionForHire.hiringManagerOnHire ```  ``` requisitions.owner = candidate_applications.requisitionForHire.hiringManagerOnHire ```  ``` requisitions.creator = candidate_applications.user ```  ``` requisitions.hiringManager = candidate_applications.user ```  ``` requisitions.owner = candidate_applications.user ``` |
| [opportunity\_applications](#opportunity-applications) | ``` requisitions.postings = opportunity_applications.posting ```  ``` requisitions.id = opportunity_applications.requisitionForHire.id ```  ``` requisitions.creator = opportunity_applications.postingHiringManager ```  ``` requisitions.hiringManager = opportunity_applications.postingHiringManager ```  ``` requisitions.owner = opportunity_applications.postingHiringManager ```  ``` requisitions.creator = opportunity_applications.postingOwner ```  ``` requisitions.hiringManager = opportunity_applications.postingOwner ```  ``` requisitions.owner = opportunity_applications.postingOwner ```  ``` requisitions.creator = opportunity_applications.requisitionForHire.hiringManagerOnHire ```  ``` requisitions.hiringManager = opportunity_applications.requisitionForHire.hiringManagerOnHire ```  ``` requisitions.owner = opportunity_applications.requisitionForHire.hiringManagerOnHire ```  ``` requisitions.creator = opportunity_applications.user ```  ``` requisitions.hiringManager = opportunity_applications.user ```  ``` requisitions.owner = opportunity_applications.user ``` |
| [postings](#postings) | ``` requisitions.postings = postings.id ```  ``` requisitions.creator = postings.followers ```  ``` requisitions.hiringManager = postings.followers ```  ``` requisitions.owner = postings.followers ```  ``` requisitions.creator = postings.hiringManager ```  ``` requisitions.hiringManager = postings.hiringManager ```  ``` requisitions.owner = postings.hiringManager ```  ``` requisitions.creator = postings.owner ```  ``` requisitions.hiringManager = postings.owner ```  ``` requisitions.owner = postings.owner ```  ``` requisitions.creator = postings.user ```  ``` requisitions.hiringManager = postings.user ```  ``` requisitions.owner = postings.user ``` |
| [candidate\_referrals](#candidate-referrals) | ``` requisitions.creator = candidate_referrals.referrer ```  ``` requisitions.hiringManager = candidate_referrals.referrer ```  ``` requisitions.owner = candidate_referrals.referrer ```  ``` requisitions.creator = candidate_referrals.user ```  ``` requisitions.hiringManager = candidate_referrals.user ```  ``` requisitions.owner = candidate_referrals.user ``` |
| [candidates](#candidates) | ``` requisitions.creator = candidates.followers ```  ``` requisitions.hiringManager = candidates.followers ```  ``` requisitions.owner = candidates.followers ```  ``` requisitions.creator = candidates.owner ```  ``` requisitions.hiringManager = candidates.owner ```  ``` requisitions.owner = candidates.owner ```  ``` requisitions.creator = candidates.stageChanges.userId ```  ``` requisitions.hiringManager = candidates.stageChanges.userId ```  ``` requisitions.owner = candidates.stageChanges.userId ``` |
| [opportunities](#opportunities) | ``` requisitions.creator = opportunities.followers ```  ``` requisitions.hiringManager = opportunities.followers ```  ``` requisitions.owner = opportunities.followers ```  ``` requisitions.creator = opportunities.owner ```  ``` requisitions.hiringManager = opportunities.owner ```  ``` requisitions.owner = opportunities.owner ```  ``` requisitions.creator = opportunities.stageChanges.userId ```  ``` requisitions.hiringManager = opportunities.stageChanges.userId ```  ``` requisitions.owner = opportunities.stageChanges.userId ``` |
| [opportunity\_referrals](#opportunity-referrals) | ``` requisitions.creator = opportunity_referrals.referrer ```  ``` requisitions.hiringManager = opportunity_referrals.referrer ```  ``` requisitions.owner = opportunity_referrals.referrer ```  ``` requisitions.creator = opportunity_referrals.user ```  ``` requisitions.hiringManager = opportunity_referrals.user ```  ``` requisitions.owner = opportunity_referrals.user ``` |

requisitions table schema

|  |
| --- |
| **backfill**  BOOLEAN |
| **createdAt**  DATE-TIME |
| **creator**  STRING |
| **department**  STRING |
| **employmentStatus**  STRING |
| **headcountHired**  INTEGER |
| **headcountTotal**  STRING |
| **hiringManager**  STRING |
| **id**  STRING |
| **internalNotes**  STRING |
| **location**  STRING |
| **name**  STRING |
| **offerIds**  ARRAY This is a nested data structure. |
| **owner**  STRING |
| **postings**  ARRAY This is a nested data structure. |
| **requisitionCode**  STRING |
| **status**  STRING |
| **team**  STRING |

### sources

The `sources` table contains info about sources, or the ways that candidates enter into your Lever account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | text |
| **Useful links** | [Lever documentation](https://hire.lever.co/developer/documentation#sources)  [Lever API method](https://hire.lever.co/developer/documentation#list-all-sources "Opens in new tab: Lever API method") |

sources table schema

|  |
| --- |
| **count**  INTEGER |
| **text**  STRING |

### stages

The `stages` table contains info about stages, or the steps in the recruiting workflow in your hiring pipeline.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Lever documentation](https://hire.lever.co/developer/documentation#stages)  [Lever API method](https://hire.lever.co/developer/documentation#list-all-stages "Opens in new tab: Lever API method") |

stages table foreign keys

| Join stages with | on |
| --- | --- |
| [candidates](#candidates) | ``` stages.id = candidates.stage ```  ``` stages.id = candidates.stageChanges.toStageId ``` |
| [opportunities](#opportunities) | ``` stages.id = opportunities.stage ```  ``` stages.id = opportunities.stageChanges.toStageId ``` |

stages table schema

|  |
| --- |
| **id**  STRING |
| **text**  STRING |

### users

The `users` table contains info about the users in your Lever account. A user includes anyone who has been invited to Lever to collaborate on recruiting efforts.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Lever documentation](https://hire.lever.co/developer/documentation#users)  [Lever API method](https://hire.lever.co/developer/documentation#list-all-users "Opens in new tab: Lever API method") |

users table schema

|  |
| --- |
| **accessRole**  STRING |
| **createdAt**  DATE-TIME |
| **deactivatedAt**  DATE-TIME |
| **email**  STRING |
| **externalDirectoryId**  STRING |
| **id**  STRING |
| **name**  STRING |
| **photo**  STRING |
| **username**  STRING |
