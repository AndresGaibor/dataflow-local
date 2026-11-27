---
title: "Zoom"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Zoom.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Zoom

Zoom is a video conferencing platform.

Zoom integration replicates data using the [Zoom API](https://developers.zoom.us/docs/api/).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

Before connecting Zoom with QTC, ensure the following requirements are met:

- You must have a Zoom Pro plan or higher.
- For webinar use, your plan must include the Webinar Add-On, and the feature must be enabled in your Zoom instance.
- Your Zoom account has an admin role or higher.

To set up a Zoom App, choose one of the following:

- Internal App (Server-to-Server OAuth)
  1. Follow the instructions at
     [Zoom Internal Apps documentation](https://developers.zoom.us/docs/internal-apps/).
  2. In the app settings, add the required scopes listed below.
- OAuth App
  1. Follow the instructions at
     [Creating an OAuth App](https://developers.zoom.us/docs/integrations/create/).
  2. In the app settings, add the required scopes listed below.

For both app types, add the following scopes:

- `meeting:read:list_meetings:admin`
- `meeting:read:list_poll_results:admin`
- `meeting:read:list_polls:admin`
- `meeting:read:list_registrants:admin`
- `meeting:read:list_registration_questions:admin`
- `meeting:read:meeting:admin`
- `report:read:list_meeting_participants:admin`
- `report:read:list_webinar_participants:admin`
- `report:read:meeting:admin`
- `report:read:webinar:admin`
- `user:read:list_users:admin`
- `webinar:read:list_absentees:admin`
- `webinar:read:list_panelists:admin`
- `webinar:read:list_past_polls:admin`
- `webinar:read:list_polls:admin`
- `webinar:read:list_registrants:admin`
- `webinar:read:list_registration_questions:admin`
- `webinar:read:list_tracking_sources:admin`
- `webinar:read:list_webinars:admin`
- `webinar:read:past_qa:admin`
- `webinar:read:webinar:admin`

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
| Client ID | Client ID. |
| Client Secret | Client secret. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

The schema and info displayed below is for version 1.

Depending on your destination, table and column names may not appear as they are outlined below.

### meeting\_files

The `meeting_files` table contains information about files shared during meetings in your Zoom account.

**Note**:Zoom deletes these files 24 hours after completion of the meeting.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | meeting\_uuid  file\_name |
| **Useful links** | [Zoom API method](https://marketplace.zoom.us/Content/api-reference/zoom-api/meetings/listpastmeetingfiles "Opens in new tab: Zoom API method") |

meeting\_files table foreign keys

| Join meeting\_files with | on |
| --- | --- |
| [meeting\_poll\_results](#meeting-poll-results) | ``` meeting_files.meeting_uuid = meeting_poll_results.meeting_uuid ``` |
| [meetings](#meetings) | ``` meeting_files.meeting_uuid = meetings.uuid ``` |

meeting\_files table schema

|  |
| --- |
| **download\_url**  STRING |
| **file\_name**  STRING |
| **file\_size**  INTEGER |
| **meeting\_uuid**  STRING |

### meeting\_poll\_results

The `meeting_poll_results` table contains information about the results of polls from your Zoom meetings.

**Note**: As per Zoom’s docs, a Zoom Pro plan or higher is required to retrieve this data.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | email  meeting\_id |
| **Useful links** | [Zoom API method](https://developers.zoom.us/docs/api/meetings/#tag/polls/get/past_meetings/%7BmeetingId%7D/polls "Opens in new tab: Zoom API method") |

meeting\_poll\_results table foreign keys

| Join meeting\_poll\_results with | on |
| --- | --- |
| [meeting\_files](#meeting-files) | ``` meeting_poll_results.meeting_uuid = meeting_files.meeting_uuid ``` |
| [meetings](#meetings) | ``` meeting_poll_results.meeting_uuid = meetings.uuid ``` |

meeting\_poll\_results table schema

|  |
| --- |
| **email**  STRING |
| **meeting\_uuid**  STRING |
| **name**  STRING |
| **question\_details**  ARRAY This is a nested data structure:   - answer: STRING - question: STRING |

### meeting\_polls

The `meeting_polls` table contains information about the polls from your Zoom meetings.

**Note**: As per Zoom’s docs, a Zoom Pro plan or higher is required to retrieve this data.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | id  meeting\_id |
| **Useful links** | [Zoom API method](https://developers.zoom.us/docs/api/meetings/#tag/polls/get/meetings/%7BmeetingId%7D/polls "Opens in new tab: Zoom API method") |

meeting\_polls table foreign keys

| Join meeting\_polls with | on |
| --- | --- |
| [meeting\_questions](#meeting-questions) | ``` meeting_polls.meeting_id = meeting_questions.meeting_id ``` |
| [meeting\_registrants](#meeting-registrants) | ``` meeting_polls.meeting_id = meeting_registrants.meeting_id ``` |
| [meetings](#meetings) | ``` meeting_polls.meeting_id = meetings.meeting_id ``` |
| [report\_meeting\_participants](#report-meeting-participants) | ``` meeting_polls.meeting_id = report_meeting_participants.meeting_id ``` |
| [report\_meetings](#report-meetings) | ``` meeting_polls.meeting_id = report_meetings.meeting_id ``` |

meeting\_polls table schema

|  |
| --- |
| **id**  STRING |
| **meeting\_id**  STRING |
| **questions**  ARRAY This is a nested data structure:   - answers: ARRAY, which is also a nested data structure. - name: STRING - type: STRING |
| **status**  STRING |
| **title**  STRING |

### meeting\_questions

The `meeting_questions` table contains questions that users will see when registering for your Zoom meetings.

**Note**: As per Zoom’s docs, a Zoom Pro plan or higher is required to retrieve this data.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | meeting\_id |
| **Useful links** | [Zoom API method](https://developers.zoom.us/docs/api/meetings/#tag/invitation--registration/get/meetings/%7BmeetingId%7D/registrants/questions "Opens in new tab: Zoom API method") |

meeting\_questions table foreign keys

| Join meeting\_questions with | on |
| --- | --- |
| [meeting\_polls](#meeting-polls) | ``` meeting_questions.meeting_id = meeting_polls.meeting_id ``` |
| [meeting\_registrants](#meeting-registrants) | ``` meeting_questions.meeting_id = meeting_registrants.meeting_id ``` |
| [meetings](#meetings) | ``` meeting_questions.meeting_id = meetings.meeting_id ``` |
| [report\_meeting\_participants](#report-meeting-participants) | ``` meeting_questions.meeting_id = report_meeting_participants.meeting_id ``` |
| [report\_meetings](#report-meetings) | ``` meeting_questions.meeting_id = report_meetings.meeting_id ``` |

meeting\_questions table schema

|  |
| --- |
| **custom\_questions**  ARRAY This is a nested data structure:   - answers: ARRAY, which is also a nested data structure. - required: BOOLEAN - title: STRING - type: STRING |
| **meeting\_id**  STRING |
| **questions**  ARRAY This is a nested data structure:   - field\_name: STRING - required: BOOLEAN |

### meeting\_registrants

The `meeting_registrants` table contains the list of users who have registered for your Zoom meetings.

**Note**: As per Zoom’s docs, a Zoom Pro plan or higher is required to retrieve this data.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | id  meeting\_id |
| **Useful links** | [Zoom API method](https://developers.zoom.us/docs/api/meetings/#tag/invitation--registration "Opens in new tab: Zoom API method") |

meeting\_registrants table foreign keys

| Join meeting\_registrants with | on |
| --- | --- |
| [meeting\_polls](#meeting-polls) | ``` meeting_registrants.meeting_id = meeting_polls.meeting_id ``` |
| [meeting\_questions](#meeting-questions) | ``` meeting_registrants.meeting_id = meeting_questions.meeting_id ``` |
| [meetings](#meetings) | ``` meeting_registrants.meeting_id = meetings.meeting_id ``` |
| [report\_meeting\_participants](#report-meeting-participants) | ``` meeting_registrants.meeting_id = report_meeting_participants.meeting_id ``` |
| [report\_meetings](#report-meetings) | ``` meeting_registrants.meeting_id = report_meetings.meeting_id ``` |

meeting\_registrants table schema

|  |
| --- |
| **address**  STRING |
| **city**  STRING |
| **comments**  STRING |
| **county**  STRING |
| **create\_time**  DATE-TIME |
| **custom\_questions**  ARRAY This is a nested data structure:   - title: STRING - value: STRING |
| **email**  STRING |
| **first\_name**  STRING |
| **id**  STRING |
| **industry**  STRING |
| **job\_title**  STRING |
| **join\_url**  STRING |
| **last\_name**  STRING |
| **meeting\_id**  STRING |
| **no\_of\_employees**  STRING |
| **org**  STRING |
| **phone**  STRING |
| **purchasing\_time\_frame**  STRING |
| **role\_in\_purchase\_process**  STRING |
| **state**  STRING |
| **status**  STRING |
| **zip**  STRING |

### meetings

The `meetings` table contains information about instant, scheduled, and recurring meetings in your Zoom account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | uuid |
| **Useful links** | [Zoom API method](https://developers.zoom.us/docs/api/meetings/#tag/meetings/get/meetings/%7BmeetingId%7D "Opens in new tab: Zoom API method") |

meetings table foreign keys

| Join meetings with | on |
| --- | --- |
| [meeting\_poll\_results](#meeting-poll-results) | ``` meetings.uuid = meeting_poll_results.meeting_uuid ``` |
| [meeting\_files](#meeting-files) | ``` meetings.uuid = meeting_files.meeting_uuid ``` |
| [meeting\_polls](#meeting-polls) | ``` meetings.meeting_id = meeting_polls.meeting_id ``` |
| [meeting\_questions](#meeting-questions) | ``` meetings.meeting_id = meeting_questions.meeting_id ``` |
| [meeting\_registrants](#meeting-registrants) | ``` meetings.meeting_id = meeting_registrants.meeting_id ``` |
| [report\_meeting\_participants](#report-meeting-participants) | ``` meetings.meeting_id = report_meeting_participants.meeting_id ``` |
| [report\_meetings](#report-meetings) | ``` meetings.meeting_id = report_meetings.meeting_id ``` |

meetings table schema

|  |
| --- |
| **agenda**  STRING |
| **created\_at**  DATE-TIME |
| **duration**  INTEGER |
| **encrypted\_Password**  STRING |
| **h323\_password**  STRING |
| **host\_id**  STRING |
| **id**  INTEGER |
| **join\_url**  STRING |
| **meeting\_id**  STRING |
| **occurences**  ARRAY This is a nested data structure:   - duration: INTEGER - occurence\_id: STRING - start\_time: DATE-TIME - status: STRING |
| **password**  STRING |
| **pmi**  INTEGER |
| **recurrence**  OBJECT This is a nested data structure:   - end\_date\_time: DATE-TIME - end\_times: INTEGER - monthly\_day: INTEGER - monthly\_week: INTEGER - monthly\_week\_day: INTEGER - repeat\_interval: INTEGER - type: INTEGER - weekly\_days: INTEGER |
| **settings**  OBJECT This is a nested data structure:   - alternative\_hosts: STRING - approval\_type: INTEGER - audio: STRING - authentication\_domains: STRING - authentication\_option: STRING - auto\_recording: STRING - close\_registration: BOOLEAN - cn\_meeting: BOOLEAN - contact\_email: BOOLEAN - contact\_name: BOOLEAN - enforce\_login: BOOLEAN - enforce\_login\_domains: STRING - global\_dial\_in\_countries: ARRAY, which is also a nested data structure. - global\_dial\_in\_numbers: ARRAY, which is also a nested data structure.   - city: STRING   - country: STRING   - country\_name: STRING   - number: STRING   - type: STRING - host\_video: BOOLEAN - in\_meeting: BOOLEAN - join\_before\_host: BOOLEAN - meeting\_authentication: BOOLEAN - mute\_upon\_entry: BOOLEAN - participant\_video: BOOLEAN - registrants\_confirmation\_email: BOOLEAN - registrants\_email\_notification: BOOLEAN - registration\_type: INTEGER - use\_pmi: BOOLEAN - waiting\_room: BOOLEAN - watermark: BOOLEAN |
| **start\_time**  DATE-TIME |
| **start\_url**  STRING |
| **status**  STRING |
| **timezone**  STRING |
| **topic**  STRING |
| **tracking\_fields**  ARRAY This is a nested data structure:   - field: STRING - value: STRING |
| **type**  INTEGER |
| **uuid**  STRING |

### report\_meeting\_participants

The `report_meeting_participants` table contains information about your Zoom’s meeting participants.

**Note**: As per Zoom’s docs, a Zoom Pro plan or higher is required to retrieve this data.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | id  meeting\_id |
| **Useful links** | [Zoom API method](https://developers.zoom.us/docs/api/meetings/#tag/reports/get/report/meetings/%7BmeetingId%7D/participants "Opens in new tab: Zoom API method") |

report\_meeting\_participants table foreign keys

| Join report\_meeting\_participants with | on |
| --- | --- |
| [meeting\_polls](#meeting-polls) | ``` report_meeting_participants.meeting_id = meeting_polls.meeting_id ``` |
| [meeting\_questions](#meeting-questions) | ``` report_meeting_participants.meeting_id = meeting_questions.meeting_id ``` |
| [meeting\_registrants](#meeting-registrants) | ``` report_meeting_participants.meeting_id = meeting_registrants.meeting_id ``` |
| [meetings](#meetings) | ``` report_meeting_participants.meeting_id = meetings.meeting_id ``` |
| [report\_meetings](#report-meetings) | ``` report_meeting_participants.meeting_id = report_meetings.meeting_id ``` |
| [users](#users) | ``` report_meeting_participants.user_id = users.id ``` |
| [report\_webinar\_participants](#report-webinar-participants) | ``` report_meeting_participants.user_id = report_webinar_participants.user_id ``` |

report\_meeting\_participants table schema

|  |
| --- |
| **duration**  STRING |
| **id**  STRING |
| **join\_time**  DATE-TIME |
| **leave\_time**  DATE-TIME |
| **meeting\_id**  STRING |
| **name**  STRING |
| **user\_email**  STRING |
| **user\_id**  STRING |

### report\_meetings

The `report_meetings` table contains detailed reports about past Zoom meetings.

**Note**: As per Zoom’s docs, a Zoom Pro plan or higher is required to retrieve this data.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | meeting\_id |
| **Useful links** | [Zoom API method](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/reportMeetingDetails "Opens in new tab: Zoom API method") |

report\_meetings table foreign keys

| Join report\_meetings with | on |
| --- | --- |
| [meeting\_polls](#meeting-polls) | ``` report_meetings.meeting_id = meeting_polls.meeting_id ``` |
| [meeting\_questions](#meeting-questions) | ``` report_meetings.meeting_id = meeting_questions.meeting_id ``` |
| [meeting\_registrants](#meeting-registrants) | ``` report_meetings.meeting_id = meeting_registrants.meeting_id ``` |
| [meetings](#meetings) | ``` report_meetings.meeting_id = meetings.meeting_id ``` |
| [report\_meeting\_participants](#report-meeting-participants) | ``` report_meetings.meeting_id = report_meeting_participants.meeting_id ``` |

report\_meetings table schema

|  |
| --- |
| **dept**  STRING |
| **duration**  INTEGER |
| **end\_time**  DATE-TIME |
| **id**  INTEGER |
| **meeting\_id**  STRING |
| **participants\_count**  INTEGER |
| **start\_time**  DATE-TIME |
| **topic**  STRING |
| **total\_minutes**  INTEGER |
| **tracking\_fields**  ARRAY This is a nested data structure:   - field: STRING - value: STRING |
| **type**  INTEGER |
| **user\_email**  STRING |
| **user\_name**  STRING |
| **uuid**  STRING |

### report\_webinar\_participants

The `report_webinar_participants` table contains information about your Zoom’s webinar participants.

**Note**: As per Zoom’s docs, a Zoom Pro plan or higher with the webinar add-on enabled is required to retrieve this data.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | id  webinar\_id |
| **Useful links** | [Zoom API method](https://developers.zoom.us/docs/api/meetings/#tag/reports/get/report/webinars/%7BwebinarId%7D/participants "Opens in new tab: Zoom API method") |

report\_webinar\_participants table foreign keys

| Join report\_webinar\_participants with | on |
| --- | --- |
| [users](#users) | ``` report_webinar_participants.user_id = users.id ``` |
| [report\_meeting\_participants](#report-meeting-participants) | ``` report_webinar_participants.user_id = report_meeting_participants.user_id ``` |
| [report\_webinars](#report-webinars) | ``` report_webinar_participants.webinar_id = report_webinars.webinar_id ``` |
| [webinar\_panelists](#webinar-panelists) | ``` report_webinar_participants.webinar_id = webinar_panelists.webinar_id ``` |
| [webinar\_registrants](#webinar-registrants) | ``` report_webinar_participants.webinar_id = webinar_registrants.webinar_id ``` |
| [webinar\_polls](#webinar-polls) | ``` report_webinar_participants.webinar_id = webinar_polls.webinar_id ``` |
| [webinar\_questions](#webinar-questions) | ``` report_webinar_participants.webinar_id = webinar_questions.webinar_id ``` |
| [webinar\_tracking\_sources](#webinar-tracking-sources) | ``` report_webinar_participants.webinar_id = webinar_tracking_sources.webinar_id ``` |

report\_webinar\_participants table schema

|  |
| --- |
| **attentiveness\_score**  STRING |
| **duration**  STRING |
| **id**  STRING |
| **join\_time**  DATE-TIME |
| **leave\_time**  DATE-TIME |
| **name**  STRING |
| **user\_email**  STRING |
| **user\_id**  STRING |
| **webinar\_id**  STRING |

### report\_webinars

The `report_webinars` table contains information about past webinars in your Zoom account.

**Note**: As per Zoom’s docs, a Zoom Pro plan or higher with the webinar add-on enabled is required to retrieve this data.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Zoom API method](https://developers.zoom.us/docs/api/meetings/#tag/reports/get/report/webinars/%7BwebinarId%7D "Opens in new tab: Zoom API method") |

report\_webinars table foreign keys

| Join report\_webinars with | on |
| --- | --- |
| [report\_webinar\_participants](#report-webinar-participants) | ``` report_webinars.webinar_id = report_webinar_participants.webinar_id ``` |
| [webinar\_panelists](#webinar-panelists) | ``` report_webinars.webinar_id = webinar_panelists.webinar_id ``` |
| [webinar\_registrants](#webinar-registrants) | ``` report_webinars.webinar_id = webinar_registrants.webinar_id ``` |
| [webinar\_polls](#webinar-polls) | ``` report_webinars.webinar_id = webinar_polls.webinar_id ``` |
| [webinar\_questions](#webinar-questions) | ``` report_webinars.webinar_id = webinar_questions.webinar_id ``` |
| [webinar\_tracking\_sources](#webinar-tracking-sources) | ``` report_webinars.webinar_id = webinar_tracking_sources.webinar_id ``` |
| [webinar\_absentees](#webinar-absentees) | ``` report_webinars.uuid = webinar_absentees.webinar_uuid ``` |
| [webinar\_files](#webinar-files) | ``` report_webinars.uuid = webinar_files.webinar_uuid ``` |
| [webinar\_poll\_results](#webinar-poll-results) | ``` report_webinars.uuid = webinar_poll_results.webinar_uuid ``` |
| [webinar\_qna\_results](#webinar-qna-results) | ``` report_webinars.uuid = webinar_qna_results.webinar_uuid ``` |
| [webinars](#webinars) | ``` report_webinars.uuid = webinars.uuid ``` |

report\_webinars table schema

|  |
| --- |
| **dept**  STRING |
| **duration**  INTEGER |
| **end\_time**  DATE-TIME |
| **host\_id**  STRING |
| **id**  INTEGER |
| **participants\_count**  INTEGER |
| **start\_time**  DATE-TIME |
| **topic**  STRING |
| **total\_minutes**  INTEGER |
| **tracking\_fields**  ARRAY This is a nested data structure:   - field: STRING - value: STRING |
| **type**  INTEGER |
| **user\_email**  STRING |
| **user\_id**  STRING |
| **user\_name**  STRING |
| **uuid**  STRING |
| **webinar\_id**  STRING |

### users

The `users` table contains user data from your Zoom account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Zoom API method](https://developers.zoom.us/docs/api/users/#tag/users "Opens in new tab: Zoom API method") |

users table foreign keys

| Join users with | on |
| --- | --- |
| [report\_meeting\_participants](#report-meeting-participants) | ``` users.id = report_meeting_participants.user_id ``` |
| [report\_webinar\_participants](#report-webinar-participants) | ``` users.id = report_webinar_participants.user_id ``` |

users table schema

|  |
| --- |
| **created\_at**  DATE-TIME |
| **dept**  STRING |
| **email**  STRING |
| **first\_name**  STRING |
| **group\_ids**  ARRAY This is a nested data structure. |
| **id**  STRING |
| **im\_group\_ids**  ARRAY This is a nested data structure. |
| **last\_client\_version**  STRING |
| **last\_login\_time**  DATE-TIME |
| **last\_name**  STRING |
| **pmi**  INTEGER |
| **status**  STRING |
| **timezone**  STRING |
| **type**  INTEGER |
| **verified**  INTEGER |

### webinar\_absentees

The `webinar_absentees` table contains information about webinar absentees from your Zoom webinars.

**Note**: As per Zoom’s docs, a Zoom Pro plan or higher with the webinar add-on enabled is required to retrieve this data.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | id  webinar\_id |
| **Useful links** | [Zoom API method](https://developers.zoom.us/docs/api/meetings/#tag/webinars/get/past_webinars/%7BwebinarId%7D/absentees "Opens in new tab: Zoom API method") |

webinar\_absentees table foreign keys

| Join webinar\_absentees with | on |
| --- | --- |
| [report\_webinars](#report-webinars) | ``` webinar_absentees.webinar_uuid = report_webinars.uuid ``` |
| [webinar\_files](#webinar-files) | ``` webinar_absentees.webinar_uuid = webinar_files.webinar_uuid ``` |
| [webinar\_poll\_results](#webinar-poll-results) | ``` webinar_absentees.webinar_uuid = webinar_poll_results.webinar_uuid ``` |
| [webinar\_qna\_results](#webinar-qna-results) | ``` webinar_absentees.webinar_uuid = webinar_qna_results.webinar_uuid ``` |
| [webinars](#webinars) | ``` webinar_absentees.webinar_uuid = webinars.uuid ``` |

webinar\_absentees table schema

|  |
| --- |
| **address**  STRING |
| **city**  STRING |
| **comments**  STRING |
| **county**  STRING |
| **create\_time**  DATE-TIME |
| **custom\_questions**  ARRAY This is a nested data structure:   - title: STRING - value: STRING |
| **email**  STRING |
| **first\_name**  STRING |
| **id**  STRING |
| **industry**  STRING |
| **job\_title**  STRING |
| **join\_url**  STRING |
| **last\_name**  STRING |
| **no\_of\_employees**  STRING |
| **org**  STRING |
| **phone**  STRING |
| **purchasing\_time\_frame**  STRING |
| **role\_in\_purchase\_process**  STRING |
| **state**  STRING |
| **status**  STRING |
| **webinar\_uuid**  STRING |
| **zip**  STRING |

### webinar\_files

The `webinar_files` table contains information about files shared in-meeting in your Zoom account.

**Note**: Zoom deletes these files 24 hours after completion of the webinar.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | webinar\_uuid  file\_name |
| **Useful links** | [Zoom API method](https://marketplace.zoom.us/Content/api-reference/zoom-api/webinars/listpastwebinarfiles "Opens in new tab: Zoom API method") |

webinar\_files table foreign keys

| Join webinar\_files with | on |
| --- | --- |
| [report\_webinars](#report-webinars) | ``` webinar_files.webinar_uuid = report_webinars.uuid ``` |
| [webinar\_absentees](#webinar-absentees) | ``` webinar_files.webinar_uuid = webinar_absentees.webinar_uuid ``` |
| [webinar\_poll\_results](#webinar-poll-results) | ``` webinar_files.webinar_uuid = webinar_poll_results.webinar_uuid ``` |
| [webinar\_qna\_results](#webinar-qna-results) | ``` webinar_files.webinar_uuid = webinar_qna_results.webinar_uuid ``` |
| [webinars](#webinars) | ``` webinar_files.webinar_uuid = webinars.uuid ``` |

webinar\_files table schema

|  |
| --- |
| **download\_url**  STRING |
| **file\_name**  STRING |
| **file\_size**  INTEGER |
| **webinar\_uuid**  STRING |

### webinar\_panelists

The `webinar_panelists` table contains information about your Zoom webinar panelists.

**Note**: As per Zoom’s docs, a Zoom Pro plan or higher with the webinar add-on enabled is required to retrieve this data.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | id  webinar\_id |
| **Useful links** | [Zoom API method](https://developers.zoom.us/docs/api/meetings/#tag/webinars/get/webinars/%7BwebinarId%7D/panelists "Opens in new tab: Zoom API method") |

webinar\_panelists table foreign keys

| Join webinar\_panelists with | on |
| --- | --- |
| [report\_webinar\_participants](#report-webinar-participants) | ``` webinar_panelists.webinar_id = report_webinar_participants.webinar_id ``` |
| [report\_webinars](#report-webinars) | ``` webinar_panelists.webinar_id = report_webinars.webinar_id ``` |
| [webinar\_registrants](#webinar-registrants) | ``` webinar_panelists.webinar_id = webinar_registrants.webinar_id ``` |
| [webinar\_polls](#webinar-polls) | ``` webinar_panelists.webinar_id = webinar_polls.webinar_id ``` |
| [webinar\_questions](#webinar-questions) | ``` webinar_panelists.webinar_id = webinar_questions.webinar_id ``` |
| [webinar\_tracking\_sources](#webinar-tracking-sources) | ``` webinar_panelists.webinar_id = webinar_tracking_sources.webinar_id ``` |

webinar\_panelists table schema

|  |
| --- |
| **email**  STRING |
| **id**  STRING |
| **join\_url**  STRING |
| **name**  STRING |
| **webinar\_id**  STRING |

### webinar\_poll\_results

The `webinar_poll_results` data contains information about poll results from specific Zoom webinars.

**Note**: As per Zoom’s docs, the following requirements must be met to retrieve this data:

- A Zoom webinar license
- A Pro plan or higher

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | webinar\_id  email |
| **Useful links** | [Zoom API method](https://developers.zoom.us/docs/api/meetings/#tag/webinars/get/past_webinars/%7BwebinarId%7D/polls "Opens in new tab: Zoom API method") |

webinar\_poll\_results table foreign keys

| Join webinar\_poll\_results with | on |
| --- | --- |
| [report\_webinars](#report-webinars) | ``` webinar_poll_results.webinar_uuid = report_webinars.uuid ``` |
| [webinar\_absentees](#webinar-absentees) | ``` webinar_poll_results.webinar_uuid = webinar_absentees.webinar_uuid ``` |
| [webinar\_files](#webinar-files) | ``` webinar_poll_results.webinar_uuid = webinar_files.webinar_uuid ``` |
| [webinar\_qna\_results](#webinar-qna-results) | ``` webinar_poll_results.webinar_uuid = webinar_qna_results.webinar_uuid ``` |
| [webinars](#webinars) | ``` webinar_poll_results.webinar_uuid = webinars.uuid ``` |

webinar\_poll\_results table schema

|  |
| --- |
| **email**  STRING |
| **name**  STRING |
| **question\_details**  ARRAY This is a nested data structure:   - answer: STRING - question: STRING |
| **webinar\_uuid**  STRING |

### webinar\_polls

The `webinar_polls` table contains information about polls in your Zoom webinars.

**Note**: As per Zoom’s docs, a Zoom Pro plan or higher with the webinar add-on enabled is required to retrieve this data.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | id  webinar\_id |
| **Useful links** | [Zoom API method](https://developers.zoom.us/docs/api/meetings/#tag/webinars/get/webinars/%7BwebinarId%7D/polls "Opens in new tab: Zoom API method") |

webinar\_polls table foreign keys

| Join webinar\_polls with | on |
| --- | --- |
| [report\_webinar\_participants](#report-webinar-participants) | ``` webinar_polls.webinar_id = report_webinar_participants.webinar_id ``` |
| [report\_webinars](#report-webinars) | ``` webinar_polls.webinar_id = report_webinars.webinar_id ``` |
| [webinar\_panelists](#webinar-panelists) | ``` webinar_polls.webinar_id = webinar_panelists.webinar_id ``` |
| [webinar\_registrants](#webinar-registrants) | ``` webinar_polls.webinar_id = webinar_registrants.webinar_id ``` |
| [webinar\_questions](#webinar-questions) | ``` webinar_polls.webinar_id = webinar_questions.webinar_id ``` |
| [webinar\_tracking\_sources](#webinar-tracking-sources) | ``` webinar_polls.webinar_id = webinar_tracking_sources.webinar_id ``` |

webinar\_polls table schema

|  |
| --- |
| **id**  STRING |
| **questions**  ARRAY This is a nested data structure:   - answers: ARRAY, which is also a nested data structure. - name: STRING - type: STRING |
| **status**  STRING |
| **title**  STRING |
| **webinar\_id**  STRING |

### webinar\_qna\_results

The `webinar_qna_results` table contains information about about the questions and answers from specific Zoom webinars.

**Note**: As per Zoom’s docs, the following requirements must be met to retrieve this data:

- A Zoom webinar license
- A Pro plan or higher

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | webinar\_id  email |
| **Useful links** | [Zoom API method](https://developers.zoom.us/docs/api/meetings/#tag/webinars/get/past_webinars/%7BwebinarId%7D/qa "Opens in new tab: Zoom API method") |

webinar\_qna\_results table foreign keys

| Join webinar\_qna\_results with | on |
| --- | --- |
| [report\_webinars](#report-webinars) | ``` webinar_qna_results.webinar_uuid = report_webinars.uuid ``` |
| [webinar\_absentees](#webinar-absentees) | ``` webinar_qna_results.webinar_uuid = webinar_absentees.webinar_uuid ``` |
| [webinar\_files](#webinar-files) | ``` webinar_qna_results.webinar_uuid = webinar_files.webinar_uuid ``` |
| [webinar\_poll\_results](#webinar-poll-results) | ``` webinar_qna_results.webinar_uuid = webinar_poll_results.webinar_uuid ``` |
| [webinars](#webinars) | ``` webinar_qna_results.webinar_uuid = webinars.uuid ``` |

webinar\_qna\_results table schema

|  |
| --- |
| **email**  STRING |
| **name**  STRING |
| **question\_details**  ARRAY This is a nested data structure:   - answer: STRING - question: STRING |
| **webinar\_uuid**  STRING |

### webinar\_questions

The `webinar_questions` table contains information about your questions to be answered when registering for a Zoom webinar.

**Note**: As per Zoom’s docs, a Zoom Pro plan or higher with the webinar add-on enabled is required to retrieve this data.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | webinar\_id |
| **Useful links** | [Zoom API method](https://developers.zoom.us/docs/api/meetings/#tag/webinars/get/webinars/%7BwebinarId%7D/registrants/questions "Opens in new tab: Zoom API method") |

webinar\_questions table foreign keys

| Join webinar\_questions with | on |
| --- | --- |
| [report\_webinar\_participants](#report-webinar-participants) | ``` webinar_questions.webinar_id = report_webinar_participants.webinar_id ``` |
| [report\_webinars](#report-webinars) | ``` webinar_questions.webinar_id = report_webinars.webinar_id ``` |
| [webinar\_panelists](#webinar-panelists) | ``` webinar_questions.webinar_id = webinar_panelists.webinar_id ``` |
| [webinar\_registrants](#webinar-registrants) | ``` webinar_questions.webinar_id = webinar_registrants.webinar_id ``` |
| [webinar\_polls](#webinar-polls) | ``` webinar_questions.webinar_id = webinar_polls.webinar_id ``` |
| [webinar\_tracking\_sources](#webinar-tracking-sources) | ``` webinar_questions.webinar_id = webinar_tracking_sources.webinar_id ``` |

webinar\_questions table schema

|  |
| --- |
| **custom\_questions**  ARRAY This is a nested data structure:   - answers: ARRAY, which is also a nested data structure. - required: BOOLEAN - title: STRING - type: STRING |
| **questions**  ARRAY This is a nested data structure:   - field\_name: STRING - required: BOOLEAN |
| **webinar\_id**  STRING |

### webinar\_registrants

The `webinar_registrants` table contains information about the users registered for a webinar in your Zoom account. Only webinars where registration is required are included in this table.

**Note**: As per Zoom’s docs, a Zoom Pro plan or higher with the webinar add-on enabled is required to retrieve this data.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | webinar\_id  id |
| **Useful links** | [Zoom API method](https://developers.zoom.us/docs/api/meetings/#tag/webinars/get/webinars/%7BwebinarId%7D/registrants "Opens in new tab: Zoom API method") |

webinar\_registrants table foreign keys

| Join webinar\_registrants with | on |
| --- | --- |
| [report\_webinar\_participants](#report-webinar-participants) | ``` webinar_registrants.webinar_id = report_webinar_participants.webinar_id ``` |
| [report\_webinars](#report-webinars) | ``` webinar_registrants.webinar_id = report_webinars.webinar_id ``` |
| [webinar\_panelists](#webinar-panelists) | ``` webinar_registrants.webinar_id = webinar_panelists.webinar_id ``` |
| [webinar\_polls](#webinar-polls) | ``` webinar_registrants.webinar_id = webinar_polls.webinar_id ``` |
| [webinar\_questions](#webinar-questions) | ``` webinar_registrants.webinar_id = webinar_questions.webinar_id ``` |
| [webinar\_tracking\_sources](#webinar-tracking-sources) | ``` webinar_registrants.webinar_id = webinar_tracking_sources.webinar_id ``` |

webinar\_registrants table schema

|  |
| --- |
| **address**  STRING |
| **city**  STRING |
| **comments**  STRING |
| **county**  STRING |
| **create\_time**  DATE-TIME |
| **custom\_questions**  ARRAY This is a nested data structure:   - title: STRING - value: STRING |
| **email**  STRING |
| **first\_name**  STRING |
| **id**  STRING |
| **industry**  STRING |
| **job\_title**  STRING |
| **join\_url**  STRING |
| **last\_name**  STRING |
| **no\_of\_employees**  STRING |
| **org**  STRING |
| **phone**  STRING |
| **purchasing\_time\_frame**  STRING |
| **role\_in\_purchase\_process**  STRING |
| **state**  STRING |
| **status**  STRING |
| **webinar\_id**  STRING |
| **zip**  STRING |

### webinar\_tracking\_sources

The `webinar_tracking_sources` lists all information about tracking sources in your Zoom account. Only webinars where registration is required will be included in this table.

**Note**: As per Zoom’s docs, a Zoom Pro plan or higher with the webinar add-on enabled is required to retrieve this data.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | id  webinar\_id |
| **Useful links** | [Zoom API method](https://developers.zoom.us/docs/api/meetings/#tag/webinars/get/webinars/%7BwebinarId%7D/tracking_sources "Opens in new tab: Zoom API method") |

webinar\_tracking\_sources table foreign keys

| Join webinar\_tracking\_sources with | on |
| --- | --- |
| [report\_webinar\_participants](#report-webinar-participants) | ``` webinar_tracking_sources.webinar_id = report_webinar_participants.webinar_id ``` |
| [report\_webinars](#report-webinars) | ``` webinar_tracking_sources.webinar_id = report_webinars.webinar_id ``` |
| [webinar\_panelists](#webinar-panelists) | ``` webinar_tracking_sources.webinar_id = webinar_panelists.webinar_id ``` |
| [webinar\_registrants](#webinar-registrants) | ``` webinar_tracking_sources.webinar_id = webinar_registrants.webinar_id ``` |
| [webinar\_polls](#webinar-polls) | ``` webinar_tracking_sources.webinar_id = webinar_polls.webinar_id ``` |
| [webinar\_questions](#webinar-questions) | ``` webinar_tracking_sources.webinar_id = webinar_questions.webinar_id ``` |

webinar\_tracking\_sources table schema

|  |
| --- |
| **id**  STRING |
| **registration\_count**  INTEGER |
| **source\_name**  STRING |
| **tracking\_url**  STRING |
| **visitor\_count**  INTEGER |
| **webinar\_id**  STRING |

### webinars

The `webinars` table contains information bout webinars scheduled from your Zoom account.

**Note**: As per Zoom’s docs, a Zoom Pro plan or higher with the webinar add-on enabled is required to retrieve this data.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | uuid |
| **Useful links** | [Zoom API method](https://developers.zoom.us/docs/api/meetings/#tag/webinars/get/users/%7BuserId%7D/webinars "Opens in new tab: Zoom API method") |

webinars table foreign keys

| Join webinars with | on |
| --- | --- |
| [report\_webinars](#report-webinars) | ``` webinars.uuid = report_webinars.uuid ``` |
| [webinar\_absentees](#webinar-absentees) | ``` webinars.uuid = webinar_absentees.webinar_uuid ``` |
| [webinar\_files](#webinar-files) | ``` webinars.uuid = webinar_files.webinar_uuid ``` |
| [webinar\_poll\_results](#webinar-poll-results) | ``` webinars.uuid = webinar_poll_results.webinar_uuid ``` |
| [webinar\_qna\_results](#webinar-qna-results) | ``` webinars.uuid = webinar_qna_results.webinar_uuid ``` |

webinars table schema

|  |
| --- |
| **agenda**  STRING |
| **created\_at**  DATE-TIME |
| **duration**  INTEGER |
| **host\_id**  STRING |
| **id**  STRING |
| **join\_url**  STRING |
| **occurences**  ARRAY This is a nested data structure:   - duration: INTEGER - occurence\_id: STRING - start\_time: DATE-TIME - status: STRING |
| **recurrence**  OBJECT This is a nested data structure:   - end\_date\_time: DATE-TIME - end\_times: INTEGER - monthly\_day: INTEGER - monthly\_week: INTEGER - monthly\_week\_day: INTEGER - repeat\_interval: INTEGER - type: INTEGER - weekly\_days: INTEGER |
| **settings**  OBJECT This is a nested data structure:   - allow\_multiple\_devices: BOOLEAN - alternative\_hosts: STRING - approval\_type: INTEGER - audio: STRING - authentication\_domains: STRING - authentication\_option: STRING - auto\_recording: STRING - close\_registration: BOOLEAN - contact\_email: BOOLEAN - contact\_name: BOOLEAN - enforce\_login: BOOLEAN - enforce\_login\_domains: STRING - global\_dial\_in\_countries: ARRAY, which is also a nested data structure. - hd\_video: BOOLEAN - host\_video: BOOLEAN - meeting\_authentication: BOOLEAN - notify\_registrants: BOOLEAN - on\_demand: BOOLEAN - panelists\_video: BOOLEAN - post\_webinar\_survey: BOOLEAN - practice\_session: BOOLEAN - registrants\_confirmation\_email: BOOLEAN - registrants\_email\_notification: BOOLEAN - registrants\_restrict\_number: INTEGER - registration\_type: INTEGER - show\_share\_button: BOOLEAN - survey\_url: STRING |
| **start\_time**  DATE-TIME |
| **start\_url**  STRING |
| **timezone**  STRING |
| **topic**  STRING |
| **tracking\_fields**  ARRAY This is a nested data structure:   - field: STRING - value: STRING |
| **type**  INTEGER |
| **uuid**  STRING |
