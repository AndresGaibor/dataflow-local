---
title: "Create a Google BigQuery Connection"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/ODBC_Connector_help/Content/Connectors_ODBC/GoogleBigQuery/Create-GBQ-Connection.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "ODBC databases", "Google BigQuery"]
---

# Create a Google BigQuery Connection

To access your data stored on a Google BigQuery database, you will need to know the server and database name that you want to connect to, and you must have access credentials. Once you have created a connection to a Google BigQuery database, you can select data from the available tables and then load that data into your application or document.

In Qlik Sense, you connect to a Google BigQuery database through the Add data dialog or the Data load editor.

## Before you start

To work with data connections, your tenant administrator needs to assign you the required permissions for Data connections. For more information, see [Assigning permissions for users to work with data connections](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-data-connections.htm#Permissions).

## Authenticating the Google account

The first step is to authenticate your Google account using the account properties below.

Account properties that can be configured

| Account property | Description | Required |
| --- | --- | --- |
| Direct Gateway | This field will only appear if you selected the "via Direct Access gateway" data connection. Select the data gateway (or [gateway pool](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/direct-access-gateway-managing-console.htm#Pools)) through which you need to connect to your data source.  Information noteUsers that need to leverage gateway-enabled data connections must have the Can Consume Data permission for the space in which the gateway resides. | Yes |
| OAuth Mechanism | Select User Authentication, Service Authentication, or Application Default Credentials mechanisms.  For Service Authentication, the Google service account must be BigQuery Job User for connections to multiple catalogs, or BigQuery Data Viewer for connections to a single catalog. Read more about how to configure permissions for the Google service account in the [Google documentation](https://cloud.google.com/bigquery/docs/access-control).  For Application Default Credentials you must create an Environment Variable in your Windows System Properties. Read more about how to set up the GOOGLE\_APPLICATION\_CREDENTIALS environment variable in the [Google authentication documentation](https://cloud.google.com/docs/authentication/application-default-credentials#GAC).  Information note The Application Default Credentials option is only supported with the following Qlik products:   - Qlik Sense - Direct Access gateway 1.7.9 or later using the Google BigQuery (via Direct Access gateway) connector. | Yes |
| Sign In | Redirects to a Google sign-in page where you can obtain a confirmation code. | Yes, when User Authentication is selected. |
| Confirmation Code | The code obtained from the Google sign-in page. | Yes, when User Authentication is selected. |
| Email | The service account email. | Yes, when Service Authentication is selected. |
| Key File | The uploaded key file. | Yes, when Service Authentication is selected. |
| File | Click to upload a key file. | Yes, when Service Authentication is selected. |
| Validate | Validates the confirmation code or the key. | Yes |
| P12 Password | This option allows you to use a P12 private key file with a non-standard password. The specified value is the password your key file is encrypted with.  Information noteP12 private key file support is deprecated. You can use JSON private key files instead. | No |
| Catalog (Project) | The name of your BigQuery project. This project is the default project the Google BigQuery Connector queries against. The Google BigQuery Connector supports multiple catalogs, the equivalent of Google BigQuery projects.  Information noteWhen accessing Google BigQuery via Direct Access gateway, Direct Access gateway 1.7.1 or later is required. | Yes |
| Minimum  TLS | Selects the minimum version of Transport Layer Security supported by the server. Select a lower or equal number to what the server runs. | Yes.  Information note TLS 1.3 is only functional when both the Qlik Sense Enterprise on Windows version and the hosting environment support TLS 1.3. |

## Account properties

### Credentials

Credentials are used to prove that a user is allowed to access the data in a connection.

There are two types of credentials that can be used when making a connection in Qlik Cloud. If you leave the User defined credentials check box deselected, then only one set of credentials will be used for the connection. These credentials belong to the connection and will be used by anyone who can access it. For example, if the connection is in a shared space, every user in the space will be able to use these credentials. This one-to-one mapping is the default setting.

If you select User defined credentials, then every user who wants to access this connection will need to input their own credentials before selecting tables or loading data. These credentials belong to a user, not a connection. User defined credentials can be saved and used in multiple connections of the same connector type.

Information noteMake sure that you use credentials that match the OAuth mechanism. For example, credentials that are created for Service Authentication cannot be used to authenticate a connection with User Authentication.

#### Creating new credentials

1. Click Authenticate.

   A page with an authentication code will open.
2. Click Copy to clipboard to copy the authentication code.
3. Return to the connection dialog and paste the authentication code.
4. Click Verify to check that the authentication is successful.
5. Set a name for the credentials in Credentials name.
6. Click Get Catalogs to populate Catalogs with the catalogs that you have access to.

#### Editing credentials

In the Data load editor, you can click the ![Primary key](../_images/en-US/cloud-services/Subsystems/ODBC_Connector_help/Content/Resources/Images/Icons/ic_key.svg) underneath the connection to edit your credentials. In the hub or Data manager, you can edit credentials by right-clicking on the connection and selecting Edit Credentials.

## Additional options

Additional properties that can be configured

| Property | Description |
| --- | --- |
| Language Dialect | Use this dropdown to select Standard SQL or Legacy SQL.  Standard SQL: is compliant with the SQL 2011 standard. It supports querying nested and repeated data. For more information, see [SQL Reference](https://cloud.google.com/bigquery/docs/reference/standard-sql/).  Legacy SQL: Non-standard SQL dialect previously named BigQuery SQL. Legacy SQL was used prior to Google BigQuery 2.0. For more information, see [Query Reference](https://cloud.google.com/bigquery/docs/reference/legacy-sql). |
| Rows Per Block | Sets the maximum number of rows to fetch for each data request. |
| Default String Column Length | Sets the maximum number of characters that can be contained in string columns. |

## Large Results Options

Result set properties that can be configured

| Property | Description | Required |
| --- | --- | --- |
| Allow Large Result Sets | This option specifies the connector's response to query results larger than 128MB when using Legacy SQL. | No |
| Dataset Name For Large Result Sets | The ID of the existing BigQuery dataset that you want to use to store temporary tables for large result sets. Only specify a value for this option if you want to enable support for large result sets. | No |

## High-Throughput API options

Result set properties that can be configured

| Property | Description | Required |
| --- | --- | --- |
| Enable High-Throughput API | Enables High-Throughput API (HTAPI). | No |
| Minimum Query Results Size for HTAPI | Sets the minimum number of table rows required to activate HTAPI (default value is '1000'). | No |
| Ratio of Results to Rows Per Block | Sets the minimum ratio of total rows to rows in the first page, which are required to to activate reading through HTAPI (default value is '3').  If set to 0, then HTAPI is used for all query results that meet the minimum results size specified by HTAPI\_MinResultsSize. | No |

Information noteWhen you connect to a Google BigQuery database with the Data load editor or the Edit Script dialog, Test Connection enables you to test the connection before you attempt to create it.

## Miscellaneous properties

Miscellaneous properties and options that can be configured

| Property | Description |
| --- | --- |
| Allow non-SELECT queries | Specifies whether the connector allows non-Select queries. Default state is turned off.  [How to load without SELECT](../How-to-load-without-SELECT.htm) |
| Query timeout | Amount of time before a data load query times out. Can be set from 30 seconds to 65535 seconds. Default is 30 seconds. |
| Retry timeout | The length of time, in seconds, for which the connector retries a failed API call before timing out. The specified value must be an integer. A value of 0 indicates no timeout. Default value is 300. |

## Load optimization

Load properties that can be configured

| Property | Description | Required |
| --- | --- | --- |
| Max String Length | Maximum length of string fields. This can be set from 256 to 16384 characters. The default value is 4096. Setting this value close to the maximum length may improve load times, as it limits the need to allocate unnecessary resources. If a string is longer than the set value, it will be truncated, and the exceeding characters will not be loaded. | No |

## Advanced options

Information noteThis section is for advanced users who want to add their own custom connection parameters that are not displayed above.

Advanced options

| Property | Description | Required |
| --- | --- | --- |
| Name | Name of the custom property. You can add additional properties by clicking the Plus sign icon. | No |
| Value | Value of the property. | No |
