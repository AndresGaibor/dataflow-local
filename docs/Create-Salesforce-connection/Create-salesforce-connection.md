---
title: "Create a Salesforce connection"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Salesforce_Connector_help/Content/Connectors_Salesforce/Create-Salesforce-connection/Create-salesforce-connection.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "Salesforce"]
---

# Create a Salesforce connection

You must have a Salesforce.com account with current access credentials to create a connection. The validity of the access credentials is verified before the connection is created. You can also set properties that affect the way data is loaded from your Salesforce.com account and change the default proxy for the Salesforce Connector to use when accessing your account.

## Connecting to Salesforce

In Qlik Cloud you can select Add data from an application or add as a data source in a space. You can also use the Data load editor.

| Property | Description |
| --- | --- |
| Production | Select this option if you are connecting to a production environment. |
| Sandbox | Select this option if you are connecting to a sandbox environment. |
| My Domain | Select this option if you want to use a specific subdomain, and then enter the subdomain in the Domain name box. It should be in format mydomainname.my.salesforce.com where mydomainname is your environment domain name. |
| API version (optional) | Input your API version. Different API versions offer different sets of fields for data extraction. If you leave it blank, then the default version (52.0) is used. The default API version is the most stable. |

### Authentication

There are two types of authentication available:

- Username and password: The default setting. Authentication information is stored in Qlik Sense.
- Salesforce OAuth: User information will not be stored in Qlik Sense.

  To use Salesforce OAuth, you must create a connected app in Salesforce with the following settings:

  - Callback URL: https://connector.qlik.com/auth/oauth/v2.htm
  - OAuth Scopes:

    - Access the identity URL service (id, profile, email, address, phone)
    - Manage user data via APIs (api)
    - Perform requests at any time (refresh\_token, offline\_access)
  - Security:

    - Require secret for Web Server Flow
    - Require secret for Refresh Token Flow
    - Require Proof Key for Code Exchange (PKCE) extension for Supported Authorization Flows

To authenticate via OAuth, you need an authentication pin:

Do the following:

1. Under Authentication, select Salesforce OAuth from the drop-down.

   New form fields appear.
2. Fill in all fields. Under Account properties > Credentials, click the Authenticate button.

   A new window opens.
3. Fill in the Salesforce login fields. Click Login.

   A new window opens.
4. Copy the Authentication code. Go back to the connection creation dialog.
5. Under Complete authentication with the code provided by the source, paste the authentication pin. Click Verify.

Information noteWhen using OAuth authentication, if you edit any of the connection properties after a connection has been authenticated, you must explicitly re-authenticate. This re-authentication will not be initiated automatically. If you do not re-authenticate in this situation, the connection will stop working.

Authentication properties that can be configured

| Authentication property | Description |
| --- | --- |
| Username and password | Select this drop-down option to authenticate via username and password. |
| Salesforce OAuth | Select this drop-down option to authenticate via OAuth. |
| Client Id | The client id when configuring the OAuth authorization server. |
| Client Secret | The client secret when configuring the OAuth authorization server. This needs to be inputted every time the connection needs to be re-authenticated. |

### Credentials

Credentials are used to prove that a user is allowed to access the data in a connection.

There are two types of credentials that can be used when making a connection in Qlik Cloud. If you leave the User defined credentials check box deselected, then only one set of credentials will be used for the connection. These credentials belong to the connection and will be used by anyone who can access it. For example, if the connection is in a shared space, every user in the space will be able to use these credentials. This one-to-one mapping is the default setting.

If you select User defined credentials, then every user who wants to access this connection will need to input their own credentials before selecting tables or loading data. These credentials belong to a user, not a connection. User defined credentials can be saved and used in multiple connections of the same connector type.

In the Data load editor, you can click the ![Primary key](../_images/en-US/cloud-services/Subsystems/Salesforce_Connector_help/Content/Resources/Images/Icons/ic_key.svg) underneath the connection to edit your credentials. In spaces or Data manager, you can edit credentials by right-clicking on the connection and selecting Edit Credentials.

See which authentication type applies on each connector's page.

Fields available to be configured

| Field | Description | Note |
| --- | --- | --- |
| User defined credentials | Select this check box if you want users that access this connection to have to input their own credentials. Deselect this check box if credentials can be shared with anyone who has access to this connection. | Only available in Qlik Cloud. |
| New credentials | Drop-down menu item that appears if User defined credentials is selected. | Select this if you need to make a new set of user defined credentials. Click Delete to remove selected credentials. |
| Existing credentials | If User defined credentials is selected, existing credentials will be listed in drop-down menu. | Select a set of user defined credentials created previously. |
| User name | User name for the Salesforce account. | Salesforce user names are email addresses. If you intend to connect to a sandbox, you must append the name of the sandbox to your user name. For example, john.smith@XYZ.com.mysandbox. |
| Password | Password for the Salesforce account. | N/a |
| Security token | Security token that is assigned to the Salesforce account. | If you connect to Salesforce.com from an IP address that is in the Trusted IP Ranges in Salesforce, the security token is not required. |
| Credentials name | Name given to a set of user defined credentials. | Provided credentials are stored as private collateral and reused by you only during sequential requests. |
| Interface type | The API that is used to connect to the Salesforce data source. | When choosing between SOAP and Bulk APIs, you must know whether or not you need to load multiple Salesforce objects with a relationship query. To create relationship queries, you must use SOAP API. Bulk API is used to increase the processing speed when loading large data sets. Warning noteThe version of the Salesforce API affects which data types are supported. For example, if you use a data type such as Geolocation, which is supported by API version 30.0 or later, and then set the API to an earlier version, fields with that data type will not be accessible. |

Information noteWhen you connect to Salesforce using the Data load editor, Test Connection enables you to test the connection before you attempt to create it.

## Specify data load properties with SOAP API

SOAP API is optimized for loading small data sets or a few records at a time, and it supports selecting data with relationship queries.

Fields available to be configured

| Field | Description | Note |
| --- | --- | --- |
| QueryALL | Reads all records including those that have been marked as deleted | N/a |
| Query | Reads all records excluding those that have been marked as deleted | N/a |
| Timeout | Sets the time that the connector to waits for a response for Salesforce.com when requesting a batch of data. | The default timeout period is 100 seconds. The timeout period applies to loading each batch of data. It does not apply to the time it takes to parse, convert, and write the data to Qlik Sense. |
| Batch size | Sets the number of rows that are written to the data target in one batch. | The default batch size is set to 500. The batch size must be within a range from 1-2000. |
| Plain queries only | Limits the connector's queries to one table. | When this option is selected, the connector does not make relationship queries. The connector also does not rename fields with a full path to the field. Field names remain the same as they are in the Salesforce object. |
| Convert SQL dates | Converts dates entered in the format YYYY-MM-DD hh:mm:ss to a Salesforce SOQL format. | The SQL date-time data type is often used in WHERE clauses, but that data type format does not match date-times in a Salesforce object. If the Convert SQL dates box is selected, date-time values entered in the YYYY-MM-DD hh:mm:ss format are automatically converted to the SOQL format used for the date-time data type.  Information note WHERE clauses can only be entered in the Qlik Sense Data load editor.  If Convert SQL dates is not selected, date-time values submitted to Salesforce.com in SQL format would not match any date-time values in the Salesforce.com object database. |
| Boolean as strings | Return Boolean values as “true” or “false” strings. | If Boolean as strings is not selected, Boolean values are returned as “1” or “0.” |
| Convert UTC to local time | Converts date-time values returned by the connector to the local time of the computer the connector is running on. | If Convert UTC to local time is not selected, the connector returns date-time values from Salesforce.com in Coordinated Universal Time (UTC). |
| Name | Name the Salesforce connection. | The default name will be used if you do not enter a name. |

## Specify data load properties with Bulk API

Bulk API is optimized for loading large data sets. To use Bulk API, the Salesforce Bulk API must be enabled for the account that is reading the data on Salesforce.com.

Information noteThe Bulk API does not support aggregation functions or grouping.

Fields available to be configured

| Field | Description | Note |
| --- | --- | --- |
| Convert SQL dates | Converts dates entered in the format YYYY-MM-DD hh:mm:ss to a Salesforce SOQL format. | The SQL date-time data type is often used in WHERE clauses, but that data type format does not match date-times in a Salesforce object. If the Convert SQL dates box is selected, date-time values entered in the YYYY-MM-DD hh:mm:ss format are automatically converted to the SOQL format used for the date-time data type.  Information note WHERE clauses can only be entered in the Qlik Sense Data load editor.  If Convert SQL dates is not selected, date-time values submitted to Salesforce.com in SQL format would not match any date-time values in the Salesforce.com object database. |
| Boolean as strings | Return Boolean values as “true” or “false” strings. | If Boolean as strings is not selected, Boolean values are returned as “1” or “0.” |
| Convert UTC to local time | Converts date-time values returned by the connector to the local time of the computer the connector is running on. | If Convert UTC to local time is not selected, the connector returns date-time values from Salesforce.com in Coordinated Universal Time (UTC). |
| PK Chunking | Splits large queries into small chunks that are processed concurrently in a thread pool. | Use PK Chunking if Bulk API is running slowly or if you experience timeout errors. |
| Chunk size | Sets the size of each PK chunk. | The default chunk size is 100,000 records. You can set the chunk size to a maximum of 250,000 records.  This option is available only when PK Chunking is selected. |
| Number of threads | Sets the number of threads to run in the thread pool. | The default number of threads is set to 2, but you can set the thread count from 1 to 10. The efficiency of running multiple threads will depend on your system resources. |
| Status calls interval | Sets the timeout between API calls. | The options are set in seconds. The Auto option will increase the timeout between calls on every subsequent call. |
| Name | Name the Salesforce connection. | The default name will be used if you do not enter a name. |
