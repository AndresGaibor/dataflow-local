---
title: "RingCentral"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-RingCentral-v2.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# RingCentral

RingCentral is a cloud-based telephony platform. You can land analytics data from RingCentral as a data source when landing or replicating data.

A high-level look at RingCentral, including useful links, and the supported features.

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To retrieve your client ID and client secret:

1. Log into your [RingCentral Developer](https://login.ringcentral.com/?responseType=code&clientId=dqlOs9GHQEyyb9zBKOreTw&brandId=1210&state=&localeId=en_US&endpointId=&session=-5086812983269887808&display=page&prompt=login%20sso&scope=&appUrlScheme=https%3A%2F%2Fdevelopers.ringcentral.com%2Fapi%2Fsignup%2Fthree_legged_oauth%2Foauthredirect&ui_options=hide_logo%20hide_tos%20external_popup%20hide_consent&code_challenge=&code_challenge_method=&hideNavigationBar=true&response_hint=remember_me&v=26.1.2#/enterCredential) account.
2. Navigate to Register App > REST API App.
3. Enter a name and description for the app.
4. In the Auth section, select 3-legged OAuth flow authorization code, and then select Server-side web app.
5. In OAuth Redirect URL, enter https://connector.qlik.com/auth/oauth/v3.htm.
6. For Issue refresh tokens?, select Yes.
7. In the Security section, select the following scopes: Read Accounts, Read Call Log, Read Messages.
8. For Who will be authorized to access your app?, select Private.
9. Click Create.
10. Copy and paste your client ID, client secret, and the URL for creating connections into a secured file.

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
| API Url | API URL. |
| Client ID | Client ID. |
| Client Secret | Client secret. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### call\_log

The `call_log` contains info about your call logs.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [RingCentral API method](https://developers.ringcentral.com/api-reference/Call-Log/readUserCallLog "Opens in new tab: RingCentral API method") |

call\_log table schema

|  |
| --- |
| **\_contact\_id**  INTEGER |
| **action**  STRING |
| **direction**  STRING |
| **duration**  INTEGER |
| **extension**  OBJECT This is a nested data structure:   - id: INTEGER - uri: STRING |
| **from**  OBJECT This is a nested data structure:   - extensionId: STRING - location: STRING - name: STRING - phoneNumber: STRING |
| **id**  STRING |
| **result**  STRING |
| **sessionId**  STRING |
| **startTime**  DATE-TIME |
| **to**  OBJECT This is a nested data structure:   - extensionId: STRING - location: STRING - name: STRING - phoneNumber: STRING |
| **type**  STRING |
| **uri**  STRING |

### company\_call\_log

The `company_call_log` contains info about company call log records.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [RingCentral API method](https://developers.ringcentral.com/api-reference#Call-Log-loadCompanyCallLog "Opens in new tab: RingCentral API method") |

company\_call\_log table schema

|  |
| --- |
| **\_contact\_id**  INTEGER |
| **action**  STRING |
| **direction**  STRING |
| **duration**  INTEGER |
| **extension**  OBJECT This is a nested data structure:   - id: INTEGER - uri: STRING |
| **from**  OBJECT This is a nested data structure:   - location: STRING - name: STRING - phoneNumber: STRING |
| **id**  STRING |
| **result**  STRING |
| **sessionId**  STRING |
| **startTime**  DATE-TIME |
| **to**  OBJECT This is a nested data structure:   - location: STRING - name: STRING - phoneNumber: STRING |
| **type**  STRING |
| **uri**  STRING |

### contacts

The `contacts` contains info about corporate users of federated accounts.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [RingCentral API method](https://developers.ringcentral.com/api-reference/Internal-Contacts/readDirectoryEntry "Opens in new tab: RingCentral API method") |

contacts table schema

|  |
| --- |
| **account**  OBJECT This is a nested data structure:   - id: INTEGER |
| **email**  STRING |
| **extensionNumber**  INTEGER |
| **firstName**  STRING |
| **id**  INTEGER |
| **jobTitle**  STRING |
| **lastName**  STRING |
| **name**  STRING |
| **phoneNumbers**  ARRAY This is a nested data structure:   - phoneNumber: STRING - type: STRING - usageType: STRING |
| **status**  STRING |
| **type**  STRING |

### messages

The `messages` contains info about an extension mailbox’s messages.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | id  conversationId |
| **Useful links** | [RingCentral API method](https://developers.ringcentral.com/api-reference/Message-Store/listMessages "Opens in new tab: RingCentral API method") |

messages table schema

|  |
| --- |
| **\_contact\_id**  INTEGER |
| **availability**  STRING |
| **coverIndex**  INTEGER |
| **creationTime**  DATE-TIME |
| **direction**  STRING |
| **faxPageCount**  INTEGER |
| **faxResolution**  STRING |
| **id**  STRING |
| **lastModifiedTime**  DATE-TIME |
| **messageStatus**  STRING |
| **priority**  STRING |
| **readStatus**  STRING |
| **type**  STRING |
| **uri**  STRING |
