---
title: "Create a Marketo connection"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/ODBC_Connector_help/Content/Connectors_ODBC/Marketo/Create-Marketo-connection.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "ODBC databases", "Marketo"]
---

# Create a Marketo connection

To access data stored on a Marketo database, you will need to know the server and database name that you want to connect to, and you must have access credentials. Once you have created a connection to a Marketo database, you can select data from the available tables and then load that data into your application or document.

In Qlik Sense, you connect to a DynamoDB database through the Add data dialog or the Data load editor.

## Before you start

To work with data connections, your tenant administrator needs to assign you the required permissions for Data connections. For more information, see [Assigning permissions for users to work with data connections](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-data-connections.htm#Permissions).

## Setting up the database properties

Database properties that can be configured

| Database property | Description | Required |
| --- | --- | --- |
| Host name | The IP address or host name of the Marketo server. | Yes |
| Port | Server port for the Marketo database. | Yes |

## Authentication

The Marketo connection can be authenticated with OAuth or with an Access Token.

Authentication properties that can be configured for OAuth

| Authentication property | Description | Required |
| --- | --- | --- |
| Scope | The scope for the OAuth request. | Yes |
| Client ID | The client ID associated with your Marketo service. | Yes |
| Client Secret | The client secret associated with your Marketo service. | Yes |

## Account properties

### Credentials

Credentials are used to prove that a user is allowed to access the data in a connection.

There are two types of credentials that can be used when making a connection in Qlik Cloud. If you leave the User defined credentials check box deselected, then only one set of credentials will be used for the connection. These credentials belong to the connection and will be used by anyone who can access it. For example, if the connection is in a shared space, every user in the space will be able to use these credentials. This one-to-one mapping is the default setting.

If you select User defined credentials, then every user who wants to access this connection will need to input their own credentials before selecting tables or loading data. These credentials belong to a user, not a connection. User defined credentials can be saved and used in multiple connections of the same connector type.

In the Data load editor, you can click the ![Primary key](../_images/en-US/cloud-services/Subsystems/ODBC_Connector_help/Content/Resources/Images/Icons/ic_key.svg) underneath the connection to edit your credentials. In spaces or Data manager, you can edit credentials by right-clicking on the connection and selecting Edit Credentials.

See which authentication type applies on each connector's page.

Account properties that can be configured

| Account property | Description |
| --- | --- |
| User defined credentials | Select this check box if you want users that access this connection to have to input their own credentials. Deselect this check box if credentials can be shared with anyone who has access to this connection. |
| New credentials | Drop-down menu item that appears if User defined credentials is selected. |
| Existing credentials | Drop-down menu item that appears if User defined credentials is selected. |
| Access Token | The access token for the OAuth 2.0 authentication. |
| Credentials name | Name given to a set of user defined credentials. |

## Setting SSL options

SSL options that can be configured

| Property | Description | Required |
| --- | --- | --- |
| Enable SSL | Require SSL authentication on the connection the Marketo server. | No |
| Trusted Certificate | The full path to the SSL certificate if it is not stored in the standard system location. | Yes, if certificate is not stored in the standard system location. Only available when SSL is enabled. |
| Use Host Verification | This option specifies whether the Marketo connector requires the host name in the server's certificate to match the host name of the server when connecting over SSL. | Yes, if certificate is not stored in the standard system location. Only available when SSL is enabled. |
| Use Peer Verification | This option specifies whether the Marketo connector verifies the identity of the server when connecting over SSL. | Yes, if certificate is not stored in the standard system location. Only available when SSL is enabled. |
| Minimum  TLS | Selects the minimum version of Transport Layer Security supported by the Marketo server. Select a lower or equal number to what the server runs. | Yes.  Information note TLS 1.3 is only functional when both the Qlik Sense Enterprise on Windows version and the hosting environment support TLS 1.3. |

## Miscellaneous settings

Miscellaneous properties that can be configured

| Property | Description | Required |
| --- | --- | --- |
| Allow non-SELECT queries | Specifies whether the connector allows non-Select queries. Default state is turned off. | No |
| Query timeout | Amount of time before a data load query times out. Can be set from 30 seconds to 65535 seconds. Default is 30. | No |

## Load optimization

Load properties that can be configured

| Property | Description | Required |
| --- | --- | --- |
| Max String Length | Maximum length of string fields. This can be set from 256 to 16384 characters. The default value is 4096. Setting this value close to the maximum length may improve load times, as it limits the need to allocate unnecessary resources. If a string is longer than the set value, it will be truncated, and the exceeding characters will not be loaded. | No |

### Advanced options

Information noteThis section is for advanced users who want to add their own custom connection parameters that are not displayed above.

Advanced options

| Property | Description | Required |
| --- | --- | --- |
| Name | Name of the custom property. You can add additional properties by clicking the Plus sign icon. | No |
| Value | Value of the property. | No |

Information noteWhen you connect to a Marketo database with the Data load editor or the Edit script dialog, Test Connection enables you to test the connection before you attempt to create it.
