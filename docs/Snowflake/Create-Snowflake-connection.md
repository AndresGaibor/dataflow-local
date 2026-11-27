---
title: "Create a Snowflake connection"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/ODBC_Connector_help/Content/Connectors_ODBC/Snowflake/Create-Snowflake-connection.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "ODBC databases", "Snowflake"]
---

# Create a Snowflake connection

You need to know the server and database name to create a Snowflake connection. You must have access credentials to access data stored on a Snowflake database. Once you have created a connection, you can select data from the available tables and then load that data into your application.

In Qlik Sense, you connect to a Snowflake database through the Add data dialog or the Data load editor.

## Before you start

To work with data connections, your tenant administrator needs to assign you the required permissions for Data connections. For more information, see [Assigning permissions for users to work with data connections](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-data-connections.htm#Permissions).

## Database properties

Database properties that can be configured

| Database property | Description | Required |
| --- | --- | --- |
| Direct Gateway | This field will only appear if you selected the "via Direct Access gateway" data connection. Select the data gateway (or [gateway pool](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/direct-access-gateway-managing-console.htm#Pools)) through which you need to connect to your data source.  Information noteUsers that need to leverage gateway-enabled data connections must have the Can Consume Data permission for the space in which the gateway resides. | Yes |
| Server | The full hostname for the Snowflake account, not prefixed with http:// or https:// | Yes |
| Port | The port on which the connector will listen for Snowflake communication. | Yes |
| Database | The default database to use for connection. | No |
| Schema | The default schema to use for connection. Default = public | No |
| Warehouse | Specifies the default warehouse to use for sessions initiated by the connector. | No |
| Role | Specifies the default role to use for the connection. The specified role should be the role assigned to the specified Snowflake user.  Warning note In Data manager and data flows, the Role attribute is ignored and not added to generated script.  If you want to use the Role attribute when loading data from a Snowflake connection in Data manager or data flows, do one of the following:   - Use the Snowflake connection with a script to create a QVD file, and then use that QVD in Data manager or data flows. - In an application, use the Snowflake connection in Data load editor to add the script and load the data, and then synchronize the scripted tables with Data manager. - In a data flow, use a script processor rather than a source node, to include the Snowflake connection. In a script processor, you can specify the role statement.  Qlik Cloud Government noteThe option to select a role other than the default is not available in Qlik Cloud Government. | No |

## Authentication

There are different ways of authenticating a connection:

- Username and password (the default setting)
- OAuth

  Information noteWhen using Direct Access gateway, OAuth authentication require Direct Access gateway 1.6.6 or later.
- Key pairing (not available in Qlik Cloud Government)

Qlik Cloud Government noteKey pairing is not available with Qlik Cloud Government.

### Username and password

Authentication properties that can be configured

| Authentication property | Description | Required |
| --- | --- | --- |
| Username and password | Select this drop-down option to authenticate via username and password. | Yes |

### OAuth

In Qlik Cloud, authentication data can be stored in different places:

- Username and password: The default setting. Authentication information is stored in Qlik Sense.
- OAuth: User information will not be stored in Qlik Sense.

You need an authentication pin to authenticate via OAuth:

Do the following:

1. Under Authentication, select OAuth from the drop-down. New form fields appear.
2. Fill in all fields. Click the Authenticate button in the Credentials section under Account properties. A new window opens.
3. Copy the Authentication code. Go back to the connection creation dialog.
4. Under Complete authentication with the PIN provided by the source, paste the authentication pin. Click Verify.

Information noteWhen using OAuth authentication, if you edit any of the connection properties after a connection has been authenticated, you must explicitly re-authenticate. This re-authentication will not be initiated automatically. If you do not re-authenticate in this situation, the connection will stop working.

Authentication properties that can be configured

| Authentication property | Description | Required |
| --- | --- | --- |
| OAuth | Select this drop-down option to authenticate via OAuth.  Information noteWhen using Direct Access gateway, OAuth authentication require Direct Access gateway 1.6.6 or later. | Yes |
| OAuth  Server (Authorize) | URL of the authorization server. | Yes |
| OAuth Server (Token) | URL of the token server. | Yes |
| Client Id | The client id when configuring the OAuth authorization server. | Yes |
| Client Secret | The client secret when configuring the OAuth authorization server. This needs to be inputted every time the connection needs to be re-authenticated. | Yes |
| Scope | If scope offers offline access, re-authentication is automatic. | No |

#### Snowflake configuration for OAuth

Your Snowflake database must be configured to use OAuth. The process is described in Snowflake documentation:

- [Configure Snowflake OAuth for Custom Clients](https://docs.snowflake.com/en/user-guide/oauth-custom.html)

  Information noteProof Key for Code Exchange (PKCE), as recommended by Snowflake, is enabled.
- [External OAuth](https://docs.snowflake.com/en/user-guide/oauth-external.html)

When configuring the OAuth authorization server, the redirect\_uri must be set to: https://connector.qlik.com/auth/oauth/v2.htm

### Key pairing

Qlik Cloud Government note

Qlik Cloud Government does not support Snowflake key pairing.

Authentication properties that can be configured

| Authentication property | Description | Required |
| --- | --- | --- |
| Key Pair | Select this drop-down option to authenticate via key pairing | Yes |

#### Snowflake configuration for key pairing

Your Snowflake database must be configured to use key pairing. The process is described in Snowflake documentation:

- [Configuring Key Pair Authentication](https://docs.snowflake.com/en/user-guide/key-pair-auth.html#configuring-key-pair-authentication)

## Account properties

### Credentials

Credentials are used to prove that a user is allowed to access the data in a connection.

There are two types of credentials that can be used when making a connection in Qlik Cloud. If you leave the User defined credentials check box deselected, then only one set of credentials will be used for the connection. These credentials belong to the connection and will be used by anyone who can access it. For example, if the connection is in a shared space, every user in the space will be able to use these credentials. This one-to-one mapping is the default setting.

If you select User defined credentials, then every user who wants to access this connection will need to input their own credentials before selecting tables or loading data. These credentials belong to a user, not a connection. User defined credentials can be saved and used in multiple connections of the same connector type.

In the Data load editor, you can click the ![Primary key](../_images/en-US/cloud-services/Subsystems/ODBC_Connector_help/Content/Resources/Images/Icons/ic_key.svg) underneath the connection to edit your credentials. In spaces or Data manager, you can edit credentials by right-clicking on the connection and selecting Edit Credentials.

See which authentication type applies on each connector's page.

### Username and password

Account properties

| Account property | Description |
| --- | --- |
| User defined credentials | Select this check box if you want users that access this connection to have to input their own credentials. Deselect this check box if credentials can be shared with anyone who has access to this connection. |
| New credentials | Drop-down menu item that appears if User defined credentials is selected. |
| Existing credentials | Drop-down menu item that appears if User defined credentials is selected. |
| User | User name for the connection. |
| Password | Password for the connection. |
| Credentials name | Name given to a set of user defined credentials. |

### OAuth

Account properties that can be configured

| Account property | Description |
| --- | --- |
| User defined credentials | Select this check box if you want users that access this connection to have to input their own credentials. Deselect this check box if credentials can be shared with anyone who has access to this connection. |
| New credentials | Drop-down menu item that appears if User defined credentials is selected. |
| Existing credentials | Drop-down menu item that appears if User defined credentials is selected. |
| Authenticate | Click this button to authenticate OAuth information inputted under Authentication section. |
| Credentials name | Name given to a set of user defined credentials. |

### Key pairing

Qlik Cloud Government note

Qlik Cloud Government does not support Snowflake key pairing.

Account properties that can be configured

| Account property | Description |
| --- | --- |
| User defined credentials | Select this check box if you want users that access this connection to have to input their own credentials. Deselect this check box if credentials can be shared with anyone who has access to this connection. |
| New credentials | Drop-down menu item that appears if User defined credentials is selected. |
| Existing credentials | Drop-down menu item that appears if User defined credentials is selected. |
| User | The login name of the Snowflake user. |
| Private Key File Path | The file path to your private key. |
| Private Key File Password | The password to your private key. |
| Credentials name | Name given to a set of user defined credentials. |

## Miscellaneous properties

Miscellaneous properties that can be configured

| Property | Description |
| --- | --- |
| Query timeout | Amount of time before a data load query times out. Can be set from 30 seconds to 65535 seconds (18 hours).  Default = 600 seconds (10 minutes). |

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

## Name

Connection name options

| Option | Description |
| --- | --- |
| Name | Name of the connection. The default name will be used if you do not enter a name. |

Information noteWhen you connect to a Snowflake database with the Data load editor or the Edit Script dialog, Test Connection enables you to test the connection before you attempt to create it.
