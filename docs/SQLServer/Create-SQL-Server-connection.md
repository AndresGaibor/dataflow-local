---
title: "Create a Microsoft SQL Server connection"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/ODBC_Connector_help/Content/Connectors_ODBC/SQLServer/Create-SQL-Server-connection.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "ODBC databases", "Microsoft SQL Server"]
---

# Create a Microsoft SQL Server connection

To access your data stored on a Microsoft SQL Server database, you will need to know the server and database name that you want to connect to, and you must have access credentials. Once you have created a connection to a Microsoft SQL Server database, you can select data from the available tables and then load that data into your application or document.

Information noteAn internet connection is required to access the Microsoft SQL Server database.

In Qlik Sense, you connect to a Microsoft SQL Server database through the Add data dialog or the Data load editor.

## Before you start

To work with data connections, your tenant administrator needs to assign you the required permissions for Data connections. For more information, see [Assigning permissions for users to work with data connections](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-data-connections.htm#Permissions).

## Setting up the database properties

Database properties that can be configured

| Database property | Description | Required |
| --- | --- | --- |
| Direct Gateway | This field will only appear if you selected the "via Direct Access gateway" data connection. Select the data gateway (or [gateway pool](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/direct-access-gateway-managing-console.htm#Pools)) through which you need to connect to your data source.  Information noteUsers that need to leverage gateway-enabled data connections must have the Can Consume Data permission for the space in which the gateway resides. | Yes |
| Server | Host name to identify the location of the Microsoft SQL Server database. If you are using AWS RDS, the server name is the database instance, such as <db.instance>.<region>.rds.amazon.com | Yes |
| Port | Server port for the Microsoft SQL Server database | Yes |
| Database | The name of the Microsoft SQL Server database | Yes |
| Encrypt | Select to use encrypted communication with the database server. | No |
| Minimum  TLS | Selects the minimum version of Transport Layer Security supported by the Microsoft SQL Server. Select a lower or equal number to what the server runs. | Yes.  Information note TLS 1.3 is only functional when both the Qlik Sense Enterprise on Windows version and the hosting environment support TLS 1.3. |
| CA Certificate | Path to file system location of the root CA certificate | Yes, when Encrypt is selected |
| Trust Server Certificate | Rely on the CA certificate provided by the server to verify secure data transfer. | No |

## Authentication properties

To use Single Sign-On, both the Microsoft SQL Server and the Qlik Sense engine must be running under a service account and they must have SPNs (Service Principal Names) assigned to them.

The ODBC Connector Package's Microsoft SQL Server Connector does not support single sign-on (SSO) in:

- Qlik Sense Desktop
- Qlik Cloud

The authentication properties differ, depending on whether you are using the Direct Access gateway connector or the regular Qlik Cloud connector.

### Microsoft SQL Server authentication properties when not using Direct Access gateway

Authentication properties that can be configured

| Authentication property | Description | Required |
| --- | --- | --- |
| Use Trusted Connection | Use the authentication service specified in the Server SPN field for secure data transfer. SPN cannot be used if NTLM is used for authentication. | No |
| Use NTLM | Use the NTLM (NT LAN Manager) security protocol for authentication. | Required when the user is registered with NTLM for authentication on the database server. Cannot be used if the user's credentials are not registered with NTLM on the database server. |
| Server SPN | The service principal name (SPN) to use for the Microsoft SQL Server. | Yes, when Use Trusted Connection is selected |
| Username | User name for the Microsoft SQL Server connection. | Yes |
| Password | Password for the Microsoft SQL Server connection. | Yes |

### Microsoft SQL Server authentication properties when using Direct Access gateway

Information noteRequires Direct Access gateway 1.7.13 or later.

Authentication properties

| Authentication property | Description | Required |
| --- | --- | --- |
| Use Trusted Connection | Use the authentication service specified in the Server SPN field for secure data transfer. SPN cannot be used if NTLM is used for authentication. | No |
| Use NTLM | Use the NTLM (NT LAN Manager) security protocol for authentication.  Information noteNTLM cannot be used when Use Trusted Connection is selected. | Required when the user is registered with NTLM for authentication on the database server. Cannot be used if the user's credentials are not registered with NTLM on the database server. |
| Server SPN | The service principal name (SPN) for the Microsoft SQL Server. | Yes, when Use Trusted Connection is selected. |
| Delegation UID | The user ID to use for scheduled, automatic reloads. If a Delegation UID is specified, it is also used to test the connection when it is created or edited. The ID must be entered in the format domain\username.  Information noteManual reloads always use the ID of the user who is logged into Qlik Sense, not the Delegation UID. | No, but the ID can be provided when Use Trusted Connection is selected.  Information noteBecause scheduled reloads are performed under a system account instead of a real user, enabling the Use Trusted Connection option may not be necessary, The scheduled reloads can be performed using predefined NTLM authentication. |
| User name | User name for the Microsoft SQL Server connection. | Yes, when Use Trusted Connection is not selected. |
| Password | Password for the Microsoft SQL Server connection.  Information noteWhen Use Trusted Connection is selected, the password is for the user identified with the Delegation UID. If Use Trusted Connection is selected, and a user is not specified in the Delegation UID property, then the Password property must be left blank. | Yes, when Use Trusted Connection is not selected. |
| Name | Name of the Microsoft SQL Server connection. The default name will be used if you do not enter a name. | Yes |

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

Information noteWhen you connect to a Microsoft SQL Server database with the Data load editor, Test Connection enables you to test the connection before you attempt to create it.
