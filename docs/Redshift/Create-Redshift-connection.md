---
title: "Create an Amazon Redshift connection"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/ODBC_Connector_help/Content/Connectors_ODBC/Redshift/Create-Redshift-connection.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "ODBC databases", "Amazon Redshift"]
---

# Create an Amazon Redshift connection

To access your data stored on an Amazon Redshift database, you will need to know the server and database name that you want to connect to, and you must have access credentials. Once you have created a connection to an Amazon Redshift database, you can select data from the available tables and then load that data into your application or document.

Information note

This connector appears twice in the Add data connection dialog. Once with just the data source name and once with the data source name followed by (via Direct Access gateway). Qlik Data Gateway - Direct Access eliminates the need to open inbound firewall ports, allowing Qlik Cloud applications to securely access firewalled data. If your enterprise data source is located behind a firewall, it is strongly recommended to connect to it via the Direct Access gateway.

For more information on Qlik Data Gateway - Direct Access, see [*Data gateways*](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/direct-access-gateway.htm).

In Qlik Sense, you connect to an Amazon Redshift database through the Add data dialog or the Data load editor. In Qlik Cloud Data Servicesyou connect to an Amazon Redshift database when onboarding data.

## Before you start

To work with data connections, your tenant administrator needs to assign you the required permissions for Data connections. For more information, see [Assigning permissions for users to work with data connections](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-data-connections.htm#Permissions).

## Setting up the database properties

Database properties that can be configured

| Database property | Description | Required |
| --- | --- | --- |
| Direct Gateway | This field will only appear if you selected the "via Direct Access gateway" data connection. Select the data gateway (or [gateway pool](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/direct-access-gateway-managing-console.htm#Pools)) through which you need to connect to your data source.  Information noteUsers that need to leverage gateway-enabled data connections must have the Can Consume Data permission for the space in which the gateway resides. | Yes |
| Host name | Host name to identify the location of the Amazon Redshift database | Yes |
| Port | Server port for the Amazon Redshift database | Yes |
| Database | The name of the Amazon Redshift database | Yes |

## Authenticating the driver

### Qlik Sense: Amazon Redshift authentication properties

#### Username and password

Authentication properties that can be configured

| Authentication property | Description |
| --- | --- |
| Auth Type | Drop-down that specifies the authentication method. Select Standard to authenticate with username and password. |
| Username | User name for the Amazon Redshift connection |
| Password | Password for the Amazon Redshift connection |
| Name | Name of the Amazon Redshift connection. The default name will be used if you do not enter a name. |

#### IAM credentials

Authentication properties that can be configured

| Authentication property | Description |
| --- | --- |
| Auth Type | Drop-down that specifies the authentication method. Select  AWS IAM Credentials to authenticate with IAM. You must have ODBC driver v1.4.35.1000 or later. |
| Cluster ID | The Amazon Redshift cluster you are connecting to. |
| Region | The AWS region your cluster is in. |
| DbUser | The user name you use to access the Amazon Redshift server. |
| CA file | The file path to the CA certificate file used for IAM/IDP authentication. |
| User AutoCreate | This option specifies whether the connector causes a new user to be created when the specified user does not exist. |
| DbGroups | A comma-separated list of existing database group names that the DbUser joins for the current session. If not specified, the default is: PUBLIC. |
| Force Lowercase | This option specifies whether the connector lowercases all DbGroups sent from the identity provider to Amazon Redshift when using SSO authentication. |

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

### IAM

Account properties that can be configured

| Account property | Description |
| --- | --- |
| User defined credentials | Select this check box if you want users that access this connection to have to input their own credentials. Deselect this check box if credentials can be shared with anyone who has access to this connection. |
| New credentials | Drop-down menu item that appears if User defined credentials is selected. |
| Existing credentials | Drop-down menu item that appears if User defined credentials is selected. |
| Access Key ID | The access key provided by your AWS account. |
| Secret Access Key | The secret key provided by your AWS account. |
| Session token | The temporary session token generated by the AWS Security Token Service. |

## Selecting SSL settings

SSL support in Amazon Redshift is strictly for encrypting the connection between your client and your cluster. It does not include the server-side certificate authentication. You must ensure when establishing a connection to the Redshift data source that the host name and IP address of the data source is complete and accurate.

Information noteSSL options for Redshift are explained further in Amazon's Redshift documentation.

[Configure Security Options for Connections](https://docs.aws.amazon.com/redshift/latest/mgmt/connecting-ssl-support.html)

SSL options that can be configured

| SSL Authentication setting | Description |
| --- | --- |
| verify-full | SSL is required, the server certificate must be verified, and the host name must match the host-name attribute on the server certificate. |
| verify-ca | SSL is required and the server certificate must be verified. |
| require | SSL is required. |
| prefer | SSL is used whenever the server supports it. |
| allow | SSL is used if the server requires it. |
| disable | SSL is disabled and the connection is not encrypted. |

### Specifying certificate location

Certificate settings that can be configured

| Certificate storage | Description |
| --- | --- |
| Trusted Certificate | The full path to the SSL certificate if it is not stored in the standard system location. This property can be selected only when SSL is enabled. |

Information noteIf you are using IAM authentication, your SSL settings must be set to: verify-full, verify-ca, or require.You must also provide a Trusted Certificate file.

## Additional options

Additional options that can be configured

| Additional option | Description |
| --- | --- |
| Query Processing Modes | Specifies how database is queried. |
| Single Row Mode | This option specifies whether the driver uses Single Row Mode and returns query results one row at a time. Enable this option if you plan to query large results and do not want to retrieve the entire result into memory. Disabling this option increases performance, but can result in out-of-memory errors. |
| Use Declare Fetch | This option specifies whether the driver uses Declare/Fetch Mode and returns a specific number of rows at a time. |

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

Information noteWhen you connect to an Amazon Redshift database with the Data load editor or the Edit script dialog, Test Connection enables you to test the connection before you attempt to create it.
