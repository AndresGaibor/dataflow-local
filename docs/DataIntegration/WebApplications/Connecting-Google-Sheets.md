---
title: "Google Sheets"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Google-Sheets.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Google Sheets

Google Sheets is a web-based application that enables users to create and update spreadsheets in real time.

Google Sheets integration will generate tables containing data related to metadata and the individual sheets within a spreadsheet.

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

You need administrator permissions in your Google Search Console account.

To enable Google Sheets API:

1. Log into your [Google Search Console](https://console.developers.google.com) account.
2. Create or select a project.
3. Navigate to APIs & Services > + Enable APIs and Services.
4. Search for Google Sheets API.
5. Click Enable.

To retrieve your client ID and secret:

1. Log into your [Google Search Console](https://console.developers.google.com) account.
2. Create or select a project.
3. Navigate to APIs & Services > Credentials.
4. Select your OAuth app in the OAuth 2.0 Client IDs section. The client ID and secret are displayed.
5. Make sure Authorized Redirect URIs is set to https://connector.qlik.com/auth/oauth/v3.htm.
6. To create a new client ID, click Create Credentials.
7. In the Data Access section, click Add or remove scopes.
8. Select the following scopes:
   - .../auth/userinfo.profile
   - .../auth/spreadsheets.readonly
   - .../auth/drive.metadata.readonly
9. Click Update.
10. Click Save
11. In the Audience section, set User types to Internal.

    Set up your OAuth 2.0 app in Google Cloud Platform for internal use. If you set the audience to external, you may need to submit the OAuth 2.0 app for verification by Google.

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
| Spreadsheet ID | The part of the URL when viewing or editing a Google sheet. Example: `https://docs.google.com/spreadsheets/d/SPREADSHEET_ID/edit?gid=SHEET_ID#gid=SHEET_ID`  For more information, see the [Google documentation](https://developers.google.com/workspace/sheets/api/guides/concepts). |
| Client ID | Client ID. |
| Client Secret | Client secret. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### sheet\_metadata

The `sheet_metadata` table contains metadata about the sheets within the spreadsheet defined in the integration’s settings.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | sheetId |
| **Useful links** | [Google Sheets documentation](https://developers.google.com/sheets/api/reference/rest)  [Google Sheets API method](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/sheets#top_of_page "Opens in new tab: Google Sheets API method") |

sheet\_metadata table schema

|  |
| --- |
| **columns**  ARRAY  This is a nested data structure:   - **columnIndex**: INTEGER - **columnLetter**: STRING - **columnName**: STRING - **columnSkipped**: BOOLEAN - **columnType**: STRING - **format**: STRING - **type**: ARRAY, which is also a nested data structure. |
| **gridProperties**  OBJECT  This is a nested data structure:   - **columnCount**: INTEGER - **frozenColumnCount**: INTEGER - **frozenRowCount**: INTEGER - **rowCount**: INTEGER |
| **index**  INTEGER |
| **sheetId**  INTEGER |
| **sheetType**  STRING |
| **sheetUrl**  STRING |
| **spreadsheetId**  STRING |
| **title**  STRING |

### sheets\_loaded

The `sheets_loaded` table contains metadata about individual sheets loaded to your destination.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Keys** | sheetId  spreadsheetId  loadDate |
| **Useful links** | [Google Sheets documentation](https://developers.google.com/sheets/api/reference/rest)  [Google Sheets API method](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/sheets#top_of_page "Opens in new tab: Google Sheets API method") |

sheets\_loaded table schema

|  |
| --- |
| **lastRowNumber**  INTEGER |
| **loadDate**  DATE-TIME |
| **sheetId**  INTEGER |
| **spreadsheetId**  STRING |
| **title**  STRING |

### spreadsheet\_metadata

The `spreadsheet_metadata` table contains metadata about the spreadsheet defined in the integration’s settings.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | spreadsheetId |
| **Useful links** | [Google Sheets documentation](https://developers.google.com/sheets/api/reference/rest)  [Google Sheets API method](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/sheets#top_of_page "Opens in new tab: Google Sheets API method") |

spreadsheet\_metadata table schema

|  |
| --- |
| **properties**  OBJECT  This is a nested data structure:   - **autoRecalc**: STRING - **locale**: STRING - **timeZone**: STRING - **title**: STRING |
| **spreadsheetId**  STRING |
| **spreadsheetUrl**  STRING |
