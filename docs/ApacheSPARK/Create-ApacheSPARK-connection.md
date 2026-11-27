---
title: "Create an Apache Spark connection"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/ODBC_Connector_help/Content/Connectors_ODBC/ApacheSPARK/Create-ApacheSPARK-connection.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "ODBC databases", "Apache Spark"]
---

# Create an Apache Spark connection

To access your data stored on an Apache Spark database, you will need to know the server and database name that you want to connect to, and you must have access credentials. Once you have created a connection to an Apache Spark database, you can select data from the available tables and then load that data into your application or document.

In Qlik Sense, you connect to an Apache Spark database through the Add data dialog or the Data load editor.

## Before you start

To work with data connections, your tenant administrator needs to assign you the required permissions for Data connections. For more information, see [Assigning permissions for users to work with data connections](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-data-connections.htm#Permissions).

## Setting up the database properties

Database properties that can be configured

| Database property | Description | Required |
| --- | --- | --- |
| Direct Gateway | This field will only appear if you selected the "via Direct Access gateway" data connection. Select the data gateway (or [gateway pool](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/direct-access-gateway-managing-console.htm#Pools)) through which you need to connect to your data source.  Information noteUsers that need to leverage gateway-enabled data connections must have the Can Consume Data permission for the space in which the gateway resides. | Yes |
| Spark Server Type | The type of Spark server can be Shark Server, Shark Server 2, or Spark Thrift Server. | yes |
| Host | The IP address or host name of the Apache Spark server. | yes |
| Port | Server port for the Apache Spark database. | yes |
| Database | The name of the Apache Spark database. | yes |

## Authenticating the driver

### Qlik Sense: Apache Spark authentication properties

Authentication properties that can be configured

| Property | Description |
| --- | --- |
| Mechanism | Authentication with user name only, with user name and password, or with no authentication. If the Spark Server Type is Shark Server, you must select No Authentication. If the Spark Server Type is Spark Thrift Server, most configurations require User Name authentication. Selecting User Name and Password or User Name gives you the option to set up [*Account properties*](#Account). |
| Username | User name for the Apache Spark connection. |
| Password | Password for the Apache Spark connection. |
| Name | Name of the Apache Spark connection.  The default name will be used if you do not enter a name. |

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

## Setting SSL options

SSL options that can be configured

| Property | Description | Required |
| --- | --- | --- |
| Trusted Certificate | The full path to the SSL certificate if it is not stored in the standard system location. | Yes, if certificate is not stored in the standard system location. |
| Allow Self-signed Server Certificate | Accept an SSL certificate from the server that is self-signed and not verified by a trusted authority. | No |
| Allow Common Name Host Name Mismatch | Allow a mismatch between the SSL certificate's common name and the name provided in Host name field. | No |

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

Information noteThis section is for advanced users who want to add additional connection parameters that are not displayed above.

Advanced options that can be configured

| Option | Description | Required |
| --- | --- | --- |
| Name | Name of the property. You can add additional properties by clicking the plus sign. | No |
| Value | Value of the property. | No |
| Thrift | Can be set to Binary, SASL, or HTTP. Default = SASL | Yes |

Information noteWhen you connect to an Apache Spark database with the Data load editor or the Edit Script dialog, Test Connection enables you to test the connection before you attempt to create it.
