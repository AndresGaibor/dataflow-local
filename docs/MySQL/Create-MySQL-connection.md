---
title: "Create a MySQL Enterprise Edition connection"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/ODBC_Connector_help/Content/Connectors_ODBC/MySQL/Create-MySQL-connection.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "ODBC databases", "MySQL Enterprise Edition"]
---

# Create a MySQL Enterprise Edition connection

To access your data stored on a MySQL Enterprise Edition database, you will need to know the server and database name that you want to connect to, and you must have access credentials. Once you have created a connection to a MySQL Enterprise Edition database, you can select data from the available tables and then load that data into your application or document.

In Qlik Sense, you connect to a MySQL database through the Add data dialog or the Data load editor.

## Before you start

To work with data connections, your tenant administrator needs to assign you the required permissions for Data connections. For more information, see [Assigning permissions for users to work with data connections](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-data-connections.htm#Permissions).

## Setting up the database properties

Database properties that can be configured

| Database property | Description | Required |
| --- | --- | --- |
| Direct Gateway | This field will only appear if you selected the "via Direct Access gateway" data connection. Select the data gateway (or [gateway pool](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/direct-access-gateway-managing-console.htm#Pools)) through which you need to connect to your data source.  Information noteUsers that need to leverage gateway-enabled data connections must have the Can Consume Data permission for the space in which the gateway resides. | Yes |
| Host name | Host name to identify the location of the MySQL Enterprise Edition database. If you are using AWS RDS, the server name is the database instance, such as <db.instance>.<region>.rds.amazon.com | Yes |
| Port | Server port for the MySQL Enterprise Edition database. | Yes |
| Database | The name of the MySQL Enterprise Edition database. | Yes |

## Authenticating the driver

### Qlik Sense: MySQL Enterprise Edition authentication properties

Authentication properties that can be configured

| Authentication property | Description |
| --- | --- |
| Username | User name for the MySQL Enterprise Edition connection. |
| Password | Password for the MySQL Enterprise Edition connection. |
| Name | Name of the MySQL Enterprise Edition connection. The default name will be used if you do not enter a name. |

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

## Selecting SSL settings

SSL options that can be configured

| SSL Mode setting | Description |
| --- | --- |
| disabled | SSL is disabled and the connection is not encrypted. |
| preferred | SSL is used whenever the server supports it. |
| required | SSL is required. |
| verify\_ca | SSL is required and the server certificate must be verified. |
| verify\_identity | SSL is required, the server certificate must be verified, and the host name must match the host-name attribute on the server certificate. |

### Specifying certificate location

Certificate properties that can be configured

| Certificate storage | Description |
| --- | --- |
| Trusted Certificate | The .pem file containing trusted CA certificates, for verifying the server when using SSL. |
| Client Certificate | The .pem file containing the SSL certificate used for proving the identity of the client. |
| Client Certificate Key | The file containing the private key used for encrypting the client-side certificate during two-way SSL verification. |

## Miscellaneous properties

Miscellaneous properties and options that can be configured

| Property | Description |
| --- | --- |
| Query timeout | Amount of time before a data load query times out. Can be set from 30 seconds to 65535 seconds. Default is 30 seconds. |

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

Information noteWhen you connect to a MySQL Enterprise Edition database with the Data load editor or the Edit Script dialog, Test Connection enables you to test the connection before you attempt to create it.
