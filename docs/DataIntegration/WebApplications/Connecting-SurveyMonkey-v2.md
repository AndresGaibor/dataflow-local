---
title: "SurveyMonkey"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-SurveyMonkey-v2.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# SurveyMonkey

SurveyMonkey is an online survey tool used to create online surveys, polls, and quizzes. You can use SurveyMonkey as a data source when landing or replicating data. The SurveyMonkey account must be a paid subscription.

SurveyMonkey integration replicates data using the [SurveyMonkey REST API v3](https://developer.surveymonkey.com/api/v3/).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To retrieve the access token of an existing app:

1. Log in to https://developer.surveymonkey.com.
2. Click My Apps.
3. Click Settings on the app.
4. Copy Access Token to Access Token in the connection settings.

For more information about authentication, see [Authentication](https://www.surveymonkey.com/developer/api/v3/#authentication).

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
| Access Token | Access token for a private app in SurveyMonkey. |
| Survey ID | Survey ID. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### responses

This table contains information about your survey responses.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | date\_modified |
| **Useful links** | [SurveyMonkey documentation](https://developer.surveymonkey.com/api/v3/)  [SurveyMonkey API method](https://developer.surveymonkey.com/api/v3/#collectors-id-responses-id-details "Opens in new tab: SurveyMonkey API method") |

responses table foreign keys

| Join responses with | on |
| --- | --- |
| [simplified\_responses](#simplified-responses) | ``` responses.id = simplified_responses.id ```  ``` responses.survey_id = simplified_responses.survey_id ``` |
| [survey\_details](#survey-details) | ``` responses.survey_id = survey_details.id ``` |

responses table schema

|  |
| --- |
| **analyze\_url**  STRING |
| **collection\_mode**  STRING |
| **collector\_id**  STRING |
| **custom\_value**  STRING |
| **custom\_variables**  OBJECT This is a nested data structure. |
| **date\_created**  DATE-TIME |
| **date\_modified**  DATE-TIME |
| **edit\_url**  STRING |
| **email\_address**  STRING |
| **first\_name**  STRING |
| **href**  STRING |
| **id**  STRING |
| **ip\_address**  STRING |
| **last\_name**  STRING |
| **logic\_path**  OBJECT This is a nested data structure. |
| **metadata**  OBJECT This is a nested data structure. |
| **page\_path**  ARRAY This is a nested data structure. |
| **pages**  ARRAY This is a nested data structure:   - id: STRING - questions: ARRAY, which is also a nested data structure.   - answers: ARRAY, which is also a nested data structure.     - choice\_id: STRING     - col\_id: STRING     - image: STRING     - is\_correct: BOOLEAN     - other\_id: STRING     - row\_id: STRING     - score: INTEGER     - tag\_data: ARRAY, which is also a nested data structure.     - text: STRING   - id: STRING   - variable\_id: STRING |
| **quiz\_results**  OBJECT This is a nested data structure:   - correct: INTEGER - incorrect: INTEGER - partially\_correct: INTEGER - score: INTEGER - total\_questions: INTEGER - total\_score: INTEGER |
| **recipient\_id**  STRING |
| **response\_status**  STRING |
| **survey\_id**  STRING |
| **total\_time**  INTEGER |

### simplified\_responses

This table contains a simplified version of information about your survey responses.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | date\_modified |
| **Useful links** | [SurveyMonkey documentation](https://developer.surveymonkey.com/api/v3/)  [SurveyMonkey API method](https://developer.surveymonkey.com/api/v3/#collectors-id-responses-id-details "Opens in new tab: SurveyMonkey API method") |

simplified\_responses table foreign keys

| Join simplified\_responses with | on |
| --- | --- |
| [responses](#responses) | ``` simplified_responses.id = responses.id ```  ``` simplified_responses.survey_id = responses.survey_id ``` |
| [survey\_details](#survey-details) | ``` simplified_responses.survey_id = survey_details.id ``` |

simplified\_responses table schema

|  |
| --- |
| **analyze\_url**  STRING |
| **collection\_mode**  STRING |
| **collector\_id**  STRING |
| **custom\_value**  STRING |
| **custom\_variables**  OBJECT This is a nested data structure. |
| **date\_created**  DATE-TIME |
| **date\_modified**  DATE-TIME |
| **edit\_url**  STRING |
| **email\_address**  STRING |
| **first\_name**  STRING |
| **href**  STRING |
| **id**  STRING |
| **ip\_address**  STRING |
| **last\_name**  STRING |
| **logic\_path**  OBJECT This is a nested data structure. |
| **metadata**  OBJECT This is a nested data structure. |
| **page\_path**  ARRAY This is a nested data structure. |
| **pages**  ARRAY This is a nested data structure:   - id: STRING - questions: ARRAY, which is also a nested data structure.   - answers: ARRAY, which is also a nested data structure.     - choice\_id: STRING     - col\_id: STRING     - image: STRING     - is\_correct: BOOLEAN     - other\_id: STRING     - row\_id: STRING     - score: INTEGER     - simple\_text: STRING     - tag\_data: ARRAY, which is also a nested data structure.     - text: STRING   - family: STRING   - heading: STRING   - id: STRING   - subtype: STRING   - variable\_id: STRING |
| **quiz\_results**  OBJECT This is a nested data structure:   - correct: INTEGER - incorrect: INTEGER - partially\_correct: INTEGER - score: INTEGER - total\_questions: INTEGER - total\_score: INTEGER |
| **recipient\_id**  STRING |
| **response\_status**  STRING |
| **survey\_id**  STRING |
| **total\_time**  INTEGER |

### survey\_details

This table contains information about your survey details.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | date\_modified |
| **Useful links** | [SurveyMonkey documentation](https://developer.surveymonkey.com/api/v3/)  [SurveyMonkey API method](https://developer.surveymonkey.com/api/v3/#surveys "Opens in new tab: SurveyMonkey API method") |

survey\_details table foreign keys

| Join survey\_details with | on |
| --- | --- |
| [responses](#responses) | ``` survey_details.id = responses.survey_id ``` |
| [simplified\_responses](#simplified-responses) | ``` survey_details.id = simplified_responses.survey_id ``` |

survey\_details table schema

|  |
| --- |
| **analyze\_url**  STRING |
| **buttons\_text**  OBJECT This is a nested data structure:   - done\_button: STRING - exit\_button: STRING - next\_button: STRING - prev\_button: STRING |
| **category**  STRING |
| **collect\_url**  STRING |
| **custom\_variables**  OBJECT This is a nested data structure. |
| **date\_created**  DATE-TIME |
| **date\_modified**  DATE-TIME |
| **edit\_url**  STRING |
| **folder\_id**  STRING |
| **footer**  BOOLEAN |
| **href**  STRING |
| **id**  STRING |
| **is\_owner**  BOOLEAN |
| **language**  STRING |
| **nickname**  STRING |
| **page\_count**  INTEGER |
| **pages**  ARRAY This is a nested data structure:   - description: STRING - href: STRING - id: STRING - position: INTEGER - question\_count: INTEGER - questions: ARRAY, which is also a nested data structure.   - answers: OBJECT, which is also a nested data structure.     - choices: ARRAY, which is also a nested data structure.       - description: STRING       - id: STRING       - image: OBJECT, which is also a nested data structure.         - s3\_key: STRING         - url: STRING       - is\_na: BOOLEAN       - position: INTEGER       - quiz\_options: OBJECT, which is also a nested data structure.         - score: INTEGER       - text: STRING       - visible: BOOLEAN       - weight: INTEGER     - cols: ARRAY, which is also a nested data structure.     - other: OBJECT, which is also a nested data structure.     - rows: ARRAY, which is also a nested data structure.   - display\_options: OBJECT, which is also a nested data structure.     - show\_display\_number: BOOLEAN   - family: STRING   - forced\_ranking: BOOLEAN   - headings: ARRAY, which is also a nested data structure.     - description: STRING     - heading: STRING     - image: OBJECT, which is also a nested data structure.       - s3\_key: STRING       - url: STRING     - random\_assignment: OBJECT, which is also a nested data structure.       - description: STRING       - id: STRING       - percent: NUMBER       - position: INTEGER       - variable\_name: STRING   - href: STRING   - id: STRING   - layout: OBJECT, which is also a nested data structure.     - bottom\_spacing: NUMBER     - col\_width: NUMBER     - col\_width\_format: STRING     - left\_spacing: NUMBER     - num\_chars: NUMBER     - num\_lines: NUMBER     - position: STRING     - right\_spacing: NUMBER     - top\_spacing: NUMBER     - width: NUMBER     - width\_format: STRING   - nickname: STRING   - position: INTEGER   - quiz\_options: OBJECT, which is also a nested data structure.     - feedback: OBJECT, which is also a nested data structure.       - correct\_text: STRING       - incorrect\_text: STRING       - partial\_text: STRING     - scoring\_enabled: BOOLEAN   - required: OBJECT, which is also a nested data structure.     - amount: STRING     - text: STRING     - type: STRING   - sorting: OBJECT, which is also a nested data structure.     - ignore\_last: BOOLEAN     - type: STRING   - subtype: STRING   - validation: OBJECT, which is also a nested data structure.     - max: STRING     - min: STRING     - sum: INTEGER     - sum\_text: STRING     - text: STRING     - type: STRING   - visible: BOOLEAN - title: STRING |
| **preview**  STRING |
| **question\_count**  INTEGER |
| **quiz\_options**  OBJECT This is a nested data structure:   - feedback: OBJECT, which is also a nested data structure.   - ranges: ARRAY, which is also a nested data structure.     - max: STRING     - message: STRING     - min: STRING   - ranges\_type: STRING - is\_quiz\_mode: BOOLEAN - show\_results\_type: STRING |
| **response\_count**  INTEGER |
| **summary\_url**  STRING |
| **title**  STRING |

### surveys

This table contains information about your surveys.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | date\_modified |
| **Useful links** | [SurveyMonkey documentation](https://developer.surveymonkey.com/api/v3/) |

surveys table schema

|  |
| --- |
| **date\_created**  DATE-TIME |
| **date\_modified**  DATE-TIME |
| **id**  STRING |
| **language**  STRING |
| **nickname**  STRING |
| **question\_count**  INTEGER |
| **response\_count**  INTEGER |
| **title**  STRING |
