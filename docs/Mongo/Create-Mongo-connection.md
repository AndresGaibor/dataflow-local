---
title: "Create a MongoDB connection"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/ODBC_Connector_help/Content/Connectors_ODBC/Mongo/Create-Mongo-connection.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "ODBC databases", "MongoDB"]
---

# Create a MongoDB connection

You will need to know the server and database name that you want to connect to, and you must have access credentials. Once you have created a connection to a MongoDB database, you can select data from the available tables and then load that data into your application or document.

In Qlik Sense, you connect to a MongoDB database through the Add data dialog or the Data load editor.

## Before you start

To work with data connections, your tenant administrator needs to assign you the required permissions for Data connections. For more information, see [Assigning permissions for users to work with data connections](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-data-connections.htm#Permissions).

## Setting up the database properties

Database properties that can be configured

| Database property | Description | Required |
| --- | --- | --- |
| Direct Gateway | This field will only appear if you selected the "via Direct Access gateway" data connection. Select the data gateway (or [gateway pool](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/direct-access-gateway-managing-console.htm#Pools)) through which you need to connect to your data source.  Information noteUsers that need to leverage gateway-enabled data connections must have the Can Consume Data permission for the space in which the gateway resides. | Yes |
| Server | The IP address or host name of the server that is running the MongoDB database. | Yes |
| Port | Server port for the MongoDB database. Default value is 27017. | Yes |
| Database | The name of the MongoDB database. | Yes |

## Authenticating the driver

### Qlik Sense: MongoDB authentication properties

Authentication properties that can be configured

| Property | Description | Required |
| --- | --- | --- |
| Mechanism | The authentication mechanism used. Options are No Authentication, MongoDB User Name and Password, SCRAM-SHA-256, or LDAP.  Information noteWhen using Direct Access gateway, SCRAM-SHA-256 and LDAP authentication require Direct Access gateway 1.6.6 or later. | No |
| User name | User name for the MongoDB connection. | Yes, if Mechanism is not set to No Authentication |
| Password | Password for the MongoDB connection. | Yes, if Mechanism is not set to No Authentication |

## Account properties

### Credentials

Credentials are used to prove that a user is allowed to access the data in a connection.

There are two types of credentials that can be used when making a connection in Qlik Cloud. If you leave the User defined credentials check box deselected, then only one set of credentials will be used for the connection. These credentials belong to the connection and will be used by anyone who can access it. For example, if the connection is in a shared space, every user in the space will be able to use these credentials. This one-to-one mapping is the default setting.

If you select User defined credentials, then every user who wants to access this connection will need to input their own credentials before selecting tables or loading data. These credentials belong to a user, not a connection. User defined credentials can be saved and used in multiple connections of the same connector type.

In the Data load editor, you can click the ![Primary key](../_images/en-US/cloud-services/Subsystems/ODBC_Connector_help/Content/Resources/Images/Icons/ic_key.svg) underneath the connection to edit your credentials. In spaces or Data manager, you can edit credentials by right-clicking on the connection and selecting Edit Credentials.

See which authentication type applies on each connector's page.

## SSL Options

SSL options that can be configured

| Property | Description | Required |
| --- | --- | --- |
| Enable SSL | This option specifies whether the driver uses SSL to connect to the server. | No |
| Trusted Certificate (.pem) | The full path of the .pem file that you use to verify the server. | No |
| Allow Self-signed Server Certificate | This option specifies whether the driver allows self-signed SSL certificates from the server. | No |
| KeyFile (.pem) | The full path of the .pem file containing the certificate for verifying the client. | No |
| KeyFile Password | The password of the client certificate file that is specified in the Full Path of Mutual .pem Certificate field. | No |

## Replica Set

Replica set properties that can be configured

| Property | Description | Required |
| --- | --- | --- |
| Connect to Replica Set | Specifies whether the driver can access replica sets in your MongoDB implementation. | No |
| Replica Set Name | The name of the replica set accessed by the driver. | Yes, if connecting to a replica set. |
| Secondary Servers | A comma-separated list of the servers that you need to use when connecting to a replica set. You can indicate the TCP port that the server is using to listen for client connections by appending a colon (:) and the port number to the server name or IP address. | No |
| Read Preference | Specify how the driver routes read operations to the members of a replica set. The following values are possible: Primary (default), Primary preferred, Secondary, Secondary preferred, Nearest. | No |

## Sampling

Sampling properties that can be configured

| Property | Description | Required |
| --- | --- | --- |
| Sampling Method | This option specifies how the driver samples data when generating a temporary schema definition. Forward: (default) The driver samples data starting from the first record in the database, then samples the next record, and so on. Backwards: The driver samples data starting from the last record in the database, then samples the preceding record, and so on. Random: The driver selects sample records from the data source at random until the sampling limit is reached. | No |
| Sampling Count | The maximum number of records that the driver can sample to generate a temporary schema definition. When this option is set to 0, the driver samples every document in the database. Default value is 100. | No |
| Sampling Interval | The interval at which the driver samples records when scanning the database to generate a temporary schema definition. For example, if you set this option to 2, then the driver samples every second record in the database. If the Sampling Method is set to Random, this setting is ignored. Default value is 1. | No |

## Miscellaneous properties

Miscellaneous properties that can be configured

| Property | Description | Required |
| --- | --- | --- |
| Allow non-SELECT queries | Specifies whether the connector allows non-Select queries. Default state is disabled. Not available in QlikView. | No |
| Persist Metadata | Specifies whether metadata is stored. The following values are possible: Do not persist (default), Persist but do not overwrite, Persist and overwrite. | No |
| Query timeout | Amount of time before a data load query times out. Can be set from 30 seconds to 65535 seconds. Default value is 30. | No |
| Enable Double-Buffering | Specifies whether the connector retrieves the data using double-buffering. Default state is enabled. | No |
| Documents to Fetch Per Block | The maximum number of documents that a query returns at a time. Also determines the buffer size used when Enable Double-Buffering is enabled. Default value is 4096 | No |
| Expose strings as WVARCHAR | When enabled the String data type is mapped to WVARCHAR, when disabled it is mapped to VARCHAR. Default state is enabled. | No |
| String Column Size | The maximum number of characters contained in STRING columns. The maximum value is 2147483647, default value is 255. | No |
| Expose binary as LONGVARBINARY | When enabled the connector returns Binary columns as LONGVARBINARY data, when disabled it returns the columns as VARBINARY data. Default status is enabled. | No |
| Binary Column Size | The maximum data length for Binary columns. The maximum value is 2147483647, default value is 32767. | No |
| Enable JSON Read/Write Mode | When enabled the connector reports a special column named DocumentAsJson that retrieves or stores whole documents as JSON-formatted strings. Default status is disabled. | No |
| JSON Column Size | Sets the default column length for JSON fields. Default value is 1023. | No |
| Enable Passdown | When enabled the connector optimizes joins between virtual tables, passes filtering and aggregation optimizations to the MongoDB database for handling. Default state is enabled. | No |
| Enable Mixed Type Filter | When enabled the connector retrieves all values that match a specified filter term, even if the values are stored as a different data type than the filter term. When disabled the retrieved values match the data type of the specified filter term. | No |
| Enable Temporary Table Compression | This option specifies whether the SQL Engine compresses the temporary tables generated from executing nested select queries. | No |

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

Information noteWhen you connect to a MongoDB database with the Data load editor or the Edit Script dialog, Test Connection enables you to test the connection before you attempt to create it.
