---
title: "Typeform"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Typeform.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Typeform

Typeform is a tool for collecting and organizing information. It is a web-based platform that you can use to create anything from surveys to apps.

For more information about the API, see the [Typeform Create](https://developer.typeform.com/create/) and [Responses](https://developer.typeform.com/responses/) APIs.

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To generate your client ID and secret:

1. Log into your [Typeform](https://admin.typeform.com/login) account.
2. Click your user avatar at the top right of the page and select Account/Your Settings.
3. Click the See admin settings link at the bottom left of the page.
4. In the Admin Settings page, click Developer Apps on the left navigation bar.
5. Click Edit App for the selected application. Your client ID is displayed.

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
| Forms | Enter the names separated by a comma. Example: FrZi6D,f8nzFm. To sync all the forms, leave the field empty. |
| Incremental Range | Select the range from the drop-down list. |
| Client ID | Client ID. |
| Client Secret | Client secret. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### answers

The `answers` table contains info about the answers submitted for the forms specified in the Integration Settings page.
**Note**: There is no replication key for this table, it uses the replication key `submitted_at` from its parent stream [`submitted_landings`](#submitted-landings).

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | landing\_id  question\_id |
| **Useful links** | [Typeform documentation](https://developer.typeform.com/responses/)  [Typeform API method](https://developer.typeform.com/responses/reference/retrieve-responses "Opens in new tab: Typeform API method") |

answers table foreign keys

| Join answers with | on |
| --- | --- |
| [submitted\_landings](#submitted-landings) | ``` answers.landing_id = submitted_landings.landing_id ``` |
| [unsubmitted\_landings](#unsubmitted-landings) | ``` answers.landing_id = unsubmitted_landings.landing_id ``` |
| [questions](#questions) | ``` answers.question_id = questions.question_id ``` |

answers table schema

|  |
| --- |
| **\_sdc\_form\_id**  STRING |
| **answer**  STRING |
| **data\_type**  STRING |
| **landing\_id**  STRING |
| **question\_id**  STRING |
| **ref**  STRING |
| **submitted\_at**  DATE-TIME |
| **type**  STRING |

### forms

The `forms` table contains info about the forms (public and private) that are accesible by the user who authorized the integration in Stitch.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | last\_updated\_at |
| **Useful links** | [Typeform documentation](https://developer.typeform.com/responses/)  [Typeform API method](https://developer.typeform.com/create/reference/retrieve-forms/ "Opens in new tab: Typeform API method") |

forms table foreign keys

| Join forms with | on |
| --- | --- |
| [questions](#questions) | ``` forms.id = questions.form_id ``` |

forms table schema

|  |
| --- |
| **\_links**  OBJECT This is a nested data structure:   - display: STRING |
| **created\_at**  DATE-TIME |
| **id**  STRING |
| **last\_updated\_at**  STRING |
| **self**  OBJECT This is a nested data structure:   - href: STRING |
| **settings**  OBJECT This is a nested data structure:   - is\_public: BOOLEAN - is\_trial: BOOLEAN |
| **theme**  OBJECT This is a nested data structure:   - href: STRING |
| **title**  STRING |
| **type**  STRING |

### questions

The `questions` table contains a list of question titles and IDs that can be used to link to [`answers`](#answers).

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | form\_id  question\_id |
| **Useful links** | [Typeform API method](https://developer.typeform.com/create/reference/retrieve-form/ "Opens in new tab: Typeform API method") |

questions table foreign keys

| Join questions with | on |
| --- | --- |
| [forms](#forms) | ``` questions.form_id = forms.id ``` |
| [answers](#answers) | ``` questions.question_id = answers.question_id ``` |

questions table schema

|  |
| --- |
| **attachment**  OBJECT This is a nested data structure:   - href: STRING - properties: OBJECT, which is also a nested data structure.   - description: STRING - scale: NUMBER - type: STRING |
| **field\_type**  STRING |
| **form\_id**  STRING |
| **id**  STRING |
| **layout**  OBJECT This is a nested data structure:   - attachment: OBJECT, which is also a nested data structure.   - href: STRING   - properties: OBJECT, which is also a nested data structure.     - description: STRING   - scale: NUMBER   - type: STRING - placement: STRING - type: STRING |
| **name**  STRING |
| **options**  ARRAY This is a nested data structure:   - label: STRING |
| **properties**  OBJECT This is a nested data structure:   - allow\_multiple\_selection: BOOLEAN - allow\_other\_choice: BOOLEAN - alphabetical\_order: BOOLEAN - button\_text: STRING - choices: ARRAY, which is also a nested data structure.   - attachment: OBJECT, which is also a nested data structure.     - href: STRING     - type: STRING   - label: STRING   - ref: STRING - currency: STRING - default\_country\_code: STRING - description: STRING - fields: ARRAY - hide\_marks: BOOLEAN - labels: OBJECT, which is also a nested data structure.   - center: STRING   - left: STRING   - right: STRING - price: OBJECT, which is also a nested data structure.   - type: STRING   - value: STRING - randomize: BOOLEAN - separator: STRING - shape: STRING |
| **question\_id**  STRING |
| **ref**  STRING |
| **required**  STRING |
| **sub\_questions**  ARRAY This is a nested data structure:   - question\_id: STRING - ref: STRING - title: STRING |
| **title**  STRING |
| **type**  STRING |
| **validations**  OBJECT This is a nested data structure:   - max\_length: INTEGER - max\_selection: INTEGER - max\_value: INTEGER - min\_selection: INTEGER - min\_value: INTEGER - required: BOOLEAN |

### submitted\_landings

The `submitted_landings` table contains info about submitted form landings.

**Note**: Data related to a form landing can be retrieved twice, once in `unsubmitted_landings` when it is unsubmitted and once in `submitted_landings` when it is submitted. In this case, they will have different bookmarks.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | landing\_id |
| **Replication Key** | submitted\_at |
| **Useful links** | [Typeform API method](https://developer.typeform.com/responses/reference/retrieve-responses "Opens in new tab: Typeform API method") |

submitted\_landings table foreign keys

| Join submitted\_landings with | on |
| --- | --- |
| [answers](#answers) | ``` submitted_landings.landing_id = answers.landing_id ``` |
| [unsubmitted\_landings](#unsubmitted-landings) | ``` submitted_landings.landing_id = unsubmitted_landings.landing_id ``` |

submitted\_landings table schema

|  |
| --- |
| **\_sdc\_form\_id**  STRING |
| **browser**  STRING |
| **hidden**  STRING |
| **landed\_at**  DATE-TIME |
| **landing\_id**  STRING |
| **network\_id**  STRING |
| **platform**  STRING |
| **referer**  STRING |
| **submitted\_at**  DATE-TIME |
| **tags**  ARRAY |
| **token**  STRING |
| **user\_agent**  STRING |

### unsubmitted\_landings

The `unsubmitted_landings` table contains info about unsubmitted form landings.

**Note**: Data related to a form landing can be retrieved twice, once in `unsubmitted_landings` when it is unsubmitted and once in `submitted_landings` when it is submitted. In this case, they will have different bookmarks.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | landing\_id |
| **Replication Key** | landed\_at |
| **Useful links** | [Typeform API method](https://developer.typeform.com/responses/reference/retrieve-responses "Opens in new tab: Typeform API method") |

unsubmitted\_landings table foreign keys

| Join unsubmitted\_landings with | on |
| --- | --- |
| [answers](#answers) | ``` unsubmitted_landings.landing_id = answers.landing_id ``` |
| [submitted\_landings](#submitted-landings) | ``` unsubmitted_landings.landing_id = submitted_landings.landing_id ``` |

unsubmitted\_landings table schema

|  |
| --- |
| **\_sdc\_form\_id**  STRING |
| **browser**  STRING |
| **landed\_at**  DATE-TIME |
| **landing\_id**  STRING |
| **network\_id**  STRING |
| **platform**  STRING |
| **referer**  STRING |
| **response\_id**  STRING |
| **token**  STRING |
| **user\_agent**  STRING |
