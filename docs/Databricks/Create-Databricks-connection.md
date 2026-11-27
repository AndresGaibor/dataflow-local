---
title: "Create a Databricks connection"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/ODBC_Connector_help/Content/Connectors_ODBC/Databricks/Create-Databricks-connection.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "ODBC databases", "Databricks"]
---

# Create a Databricks connection

You need to know the Databricks server and schema name to create a connection. You must also have access credentials. Once you have created a connection to your Databricks schema, you can select data from the available tables and load that data into your application.

In Qlik Sense and Qlik Cloud Analytics Services, you connect to Databricks through the Data manager or the Data load editor.

## Before you start

To work with data connections, your tenant administrator needs to assign you the required permissions for Data connections. For more information, see [Assigning permissions for users to work with data connections](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-data-connections.htm#Permissions).

### Configuring Databricks for OAuth

Your Databricks workspace must be configured to use OAuth.

#### Configuring Azure Databricks

Do the following:

1. Register an OAuth application in Microsoft Entra ID (formerly Azure AD).

   For more information, see [Configure an OpenID Connect OAuth application from Azure AD app gallery](https://learn.microsoft.com/en-us/entra/identity/saas-apps/openidoauth-tutorial).
2. Assign the API permission <https://azuredatabricks.net/user_impersonation> to the OAuth application.
3. Use the Client ID and Client Secret of the registered Microsoft Entra ID application when configuring the connection.

#### Configuring AWS Databricks

Do the following:

1. In the Databricks Account Console, under Settings > App connections, create a custom OAuth application.
2. Configure the redirect URL <https://connector.qlik.com/auth/oauth/v3.htm>.
3. Request the scopes sql offline\_access.
4. Generate a Client Secret.
5. Use the generated Client ID and Client Secret when configuring the connection.

## Setting up the connection properties

### Qlik Cloud Analytics Services database properties

Connection properties that can be configured

| Database property | Description | Required |
| --- | --- | --- |
| Direct Gateway | This field will only appear if you selected the "via Direct Access gateway" data connection. Select the data gateway (or [gateway pool](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/direct-access-gateway-managing-console.htm#Pools)) through which you need to connect to your data source.  Information noteUsers that need to leverage gateway-enabled data connections must have the Can Consume Data permission for the space in which the gateway resides. | Yes |
| Host name | The IP address or host name of the Databricks server. | Yes |
| Port | Server port for the Databricks connection. | Yes |
| Catalog | If your Databricks host supports Unity Catalog, specify the catalog name. Otherwise, leave this field empty.  Information noteThe catalog name is case sensitive.  Information noteIn some cases, the default catalog value may be set to hive\_metastore, even in workspaces where unity catalog is not enabled. In this scenario, the catalog name must be specified as hive\_metastore, otherwise the connection will fail. .  See [Set up and manage Unity Catalog](https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/get-started#---step-1-confirm-that-your-workspace-is-enabled-for-unity-catalog) to check if the workspace is enabled for unity catalogs. See [What are catalogs in Azure Databricks](https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/create-catalogs#--manage-the-default-catalog) to identify the catalog name that must be specified in the connection dialog. | Only if your Databricks host supports Unity Catalog. |
| Schema | The name of the Databricks schema. If you specified a catalog, you must specify a schema in that catalog. | Yes |
| HTTP Path | Databricks compute resources URL. | Yes |

## Authenticating the driver

Databricks connectors have the following authentication mechanisms:

- OAuth 2.0

  Information noteWhen using Direct Access gateway, OAuth 2.0 authentication requires Direct Access gateway 1.7.8 or later.
- Personal Access Token

### OAuth 2.0 authentication properties

Information noteWhen using Direct Access gateway, OAuth 2.0 authentication (Databricks OAuth) requires Direct Access gateway 1.7.8 or later.

These properties apply to authentication with these flows:

- Databricks OAuth (Service Principal)
- Databricks OAuth (User Account)
- Azure OAuth (legacy)

#### Databricks OAuth (Service Principal)

Authentication properties that can be configured for Databricks OAuth (Service Principal)

| Property | Description |
| --- | --- |
| Client ID | The client ID when configuring the OAuth authorization server. |
| Client Secret | The client secret when configuring the OAuth authorization server. This needs to be inputted every time the connection needs to be re-authenticated. |

#### Databricks OAuth (User Account)

Authentication properties that can be configured for Databricks OAuth (User Account)

| Property | Description |
| --- | --- |
| Client ID | The client ID when configuring the OAuth authorization server. |
| Client Secret | The client secret when configuring the OAuth authorization server. This needs to be inputted every time the connection needs to be re-authenticated. |

#### Microsoft Azure OAuth (legacy)

Microsoft Azure OAuth (legacy) is kept for backwards compatibility with existing connection definitions, but you are encouraged to migrate and use instead one of the new Databricks OAuth options.

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
| Client ID | Available when OAuth 2.0 is selected as the mechanism. The client ID for the connection. |
| Client Secret | Available when OAuth 2.0 is selected as the mechanism. The client secret for the connection. |
| Token | Available when Personal Access Token is selected as the mechanism. The token for authenticating the connection. |
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

Information noteWhen you connect to a Databricks schema in the Data load editor or the Edit Script dialog, you can click Test Connection before you create it.
