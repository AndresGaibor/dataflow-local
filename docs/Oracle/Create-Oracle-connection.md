---
title: "Create an Oracle connection"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/ODBC_Connector_help/Content/Connectors_ODBC/Oracle/Create-Oracle-connection.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "ODBC databases", "Oracle"]
---

# Create an Oracle connection

To access your data stored on an Oracle database, you will need to know the server and database name that you want to connect to, and you must have access credentials. Once you have created a connection to an Oracle database, you can select data from the available tables and then load that data into your application.

In Qlik Sense, you connect to an Oracle database through the Add data dialog or the Data load editor.

## Before you start

To work with data connections, your tenant administrator needs to assign you the required permissions for Data connections. For more information, see [Assigning permissions for users to work with data connections](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-data-connections.htm#Permissions).

## Setting database properties

There are two connection types: Basic and Oracle Wallets.

### Basic connection

If you are using the Oracle (via Direct Access gateway) connector, using the TNS service requires additional configuration. The following two TNS files must be modified for the Oracle environment. You can get these files from your Oracle configuration.

- tnsnames.ora: set the host addresses and ports for the TNS service.

  Information noteYou must set the TNS\_ADMIN environment variable on the Direct Access gateway machine, and specify the directory where the tnsnames.ora file is located.
- sqlnet.ora: set the location of the Oracle wallet.

Database properties that can be configured for basic connections

| Database property | Description | Required |
| --- | --- | --- |
| Direct Gateway | This field will only appear if you selected the "via Direct Access gateway" data connection. Select the data gateway (or [gateway pool](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/direct-access-gateway-managing-console.htm#Pools)) through which you need to connect to your data source.  Information noteUsers that need to leverage gateway-enabled data connections must have the Can Consume Data permission for the space in which the gateway resides. | Yes |
| Host name | Host name to identify the location of the Oracle database. If you are using AWS RDS, the server name is the database instance, such as <db.instance>.<region>.rds.amazon.com | Yes |
| Port | Server port for the Oracle database. | Yes |
| Service name | The alias name for the TNS service. | Yes |
| TNS Name | The TNS name defined in the tnsnames.ora file.  Information note This option only appears in the Oracle (via Direct Access gateway) connector.  Requires Direct Access gateway 1.7.6 or later. | No |

### Oracle Wallet connection

Your Oracle wallet-file must be in zip format. The maximum file size is 500 KB. The zip file must contain the following files:

- An .sso file
- tnsnames.ora

Database properties that can be configured for Oracle Wallet connections

| Database property | Description | Required |
| --- | --- | --- |
| Configuration File | The Oracle wallet-file in zip format. After you add the file, click Validate. | Yes |
| Service | This dropdown will be populated with your service options once you validate your wallet-file. | Yes |

## Authenticating the driver

Information noteThe Oracle Connector does not support NTLM authentication in version 4.0. For that reason, the Windows integrated security option is not available.

### Qlik Sense: Oracle authentication properties

Authentication properties that can be configured

| Authentication property | Description |
| --- | --- |
| Username | User name for the Oracle connection. |
| Password | Password for the Oracle connection. |
| Name | Name of the Oracle connection.  The default name will be used if you do not enter a name. |

## Account properties

### Credentials

Credentials are used to prove that a user is allowed to access the data in a connection.

There are two types of credentials that can be used when making a connection in Qlik Cloud. If you leave the User defined credentials check box deselected, then only one set of credentials will be used for the connection. These credentials belong to the connection and will be used by anyone who can access it. For example, if the connection is in a shared space, every user in the space will be able to use these credentials. This one-to-one mapping is the default setting.

If you select User defined credentials, then every user who wants to access this connection will need to input their own credentials before selecting tables or loading data. These credentials belong to a user, not a connection. User defined credentials can be saved and used in multiple connections of the same connector type.

In the Data load editor, you can click the ![Primary key](../_images/en-US/cloud-services/Subsystems/ODBC_Connector_help/Content/Resources/Images/Icons/ic_key.svg) underneath the connection to edit your credentials. In spaces or Data manager, you can edit credentials by right-clicking on the connection and selecting Edit Credentials.

See which authentication type applies on each connector's page.

Account properties

| Account property | Description |
| --- | --- |
| User defined credentials | Select this check box if you want users that access this connection to have to input their own credentials. Deselect this check box if credentials can be shared with anyone who has access to this connection. |
| New credentials | Drop-down menu item that appears if User defined credentials is selected. |
| Existing credentials | Drop-down menu item that appears if User defined credentials is selected. |
| User | User name for the connection. |
| Password | Password for the connection. |
| Credentials name | Name given to a set of user defined credentials. |

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

## Advanced options

Information noteThis section is for advanced users who want to add their own custom connection parameters that are not displayed above.

Advanced options

| Property | Description | Required |
| --- | --- | --- |
| Name | Name of the custom property. You can add additional properties by clicking the Plus sign icon. | No |
| Value | Value of the property. | No |

Information noteWhen you connect to an Oracle database with the Data load editor Test Connection enables you to test the connection before you attempt to create it.
