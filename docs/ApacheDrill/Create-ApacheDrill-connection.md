---
title: "Create an Apache Drill connection"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/ODBC_Connector_help/Content/Connectors_ODBC/ApacheDrill/Create-ApacheDrill-connection.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "ODBC databases", "Apache Drill"]
---

# Create an Apache Drill connection

To access your data in an Apache Drill data store, you will need to know the Drill server you want to connect through. Once you have created a connection to an Apache Drill data store, you can select data from the available tables and then load that data into your application or document.

In Qlik Sense, you connect to an Apache Drill database through the Add data dialog or the Data load editor.

## Before you start

To work with data connections, your tenant administrator needs to assign you the required permissions for Data connections. For more information, see [Assigning permissions for users to work with data connections](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-data-connections.htm#Permissions).

## Setting up the database properties

Database properties that can be configured

| Database properties | Description | Required |
| --- | --- | --- |
| Direct Gateway | This field will only appear if you selected the "via Direct Access gateway" data connection. Select the data gateway (or [gateway pool](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/direct-access-gateway-managing-console.htm#Pools)) through which you need to connect to your data source.  Information noteUsers that need to leverage gateway-enabled data connections must have the Can Consume Data permission for the space in which the gateway resides. | Yes |
| Connection Type | Specifies whether the driver connects to a single server or a ZooKeeper cluster.Direct to Drillbit connects to a single Drill server. ZooKeeper Quorum connects to a ZooKeeper cluster. | Yes |
| Host | The IP address or host name of the Apache Drill server. | Yes |
| Port | The number of the TCP port that the Drill server uses to listen for client connections. | Yes, if the connection type is Direct to Drillbit. |
| Catalog | The default catalog name specified in ODBC driver's .did file. Typically, the name is DRILL. | No |
| Quorum | The server or servers in your ZooKeeper cluster. Separate multiple servers using a comma(,). | Yes, if the connection type is ZooKeeper Quorum. |
| Cluster Id | The name of the ZooKeeper cluster that the driver connects to. | Yes, if the connection type is ZooKeeper Quorum. |

## Authenticating the driver

### Qlik Sense: Apache Drill authentication properties

Authentication properties that can be configured

| Property | Description | Required |
| --- | --- | --- |
| Authentication Type | Specifies how the driver authenticates the connection to Drill,by choosing No Authentication or Plain. Plain is basic authentication that uses a user name and a password from Drill. Selecting Plain gives you the option to set up [*Account properties*](#Account). | Yes |
| Username | The user name that you use to access the Drill server. | Yes, if Authentication Type is set to Plain. |
| Password | The password corresponding to the Username. | Yes, if Authentication Type is set to Plain. |
| Name | Name of the Apache Drill connection. | No, the default name will be used if you do not enter a name. |

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

## SSL Options

SSL options that can be configured

| Property | Description | Required |
| --- | --- | --- |
| Enable SSL | Set whether SSL authentication is required when connecting to the Drill server. | No |
| Trusted Certificate | The full path to the SSL certificate. | Yes, if certificate is not stored in the standard system location. |
| Disable Host Verification | Disables verification that the host name in the SSL certificate is the host being connected to. | No |
| Disable Certificate Verification | Specifies whether the driver verifies the host certificate against the trust store. | No |
| Minimum  TLS | Selects the minimum version of Transport Layer Security supported by the Drill server. Select a lower or equal number to what the server runs. | Yes.  Information note TLS 1.3 is only functional when both the Qlik Sense Enterprise on Windows version and the hosting environment support TLS 1.3. |

## Miscellaneous settings

Miscellaneous options that can be configured

| Property | Description | Required |
| --- | --- | --- |
| Allow non-SELECT queries | Specifies whether the connector allows non-Select queries. Default state is turned off. | No |
| Query timeout | Amount of time before a data load query times out. Can be set from 0 seconds to 65535 seconds. Default = 180 seconds. If this property is set to 0, the connector does not stop queries. | Yes |

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

Information noteWhen you connect to an Apache Drill data source with the Data load editor or the Edit Script dialog, Test Connection enables you to test the connection before you attempt to create it.
