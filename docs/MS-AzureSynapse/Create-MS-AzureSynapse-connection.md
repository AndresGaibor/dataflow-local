---
title: "Create an Azure Synapse Analytics connection"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/ODBC_Connector_help/Content/Connectors_ODBC/MS-AzureSynapse/Create-MS-AzureSynapse-connection.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "ODBC databases", "Azure Synapse Analytics"]
---

# Create an Azure Synapse Analytics connection

To access your data stored on Azure Synapse Analytics, you will need to know the server and database name that you want to connect to, and you must have access credentials. Once you have created a connection to Azure Synapse Analytics, you can select data from the available tables and then load that data into your application or document.

In Qlik Sense and Qlik Cloud Analytics Services, you connect to Azure Synapse Analytics through the Add data dialog or the Data load editor.

In Qlik Cloud Data Servicesyou connect to an Azure Synapse Analytics database when onboarding data.

## Before you start

To work with data connections, your tenant administrator needs to assign you the required permissions for Data connections. For more information, see [Assigning permissions for users to work with data connections](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-data-connections.htm#Permissions).

## Setting up the database properties

Database properties that can be configured

| Database property | Description | Required |
| --- | --- | --- |
| Direct Gateway | This field will only appear if you selected the "via Direct Access gateway" data connection. Select the data gateway (or [gateway pool](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/direct-access-gateway-managing-console.htm#Pools)) through which you need to connect to your data source.  Information noteUsers that need to leverage gateway-enabled data connections must have the Can Consume Data permission for the space in which the gateway resides. | Yes |
| Server | Host name to identify the location of the Azure Synapse database. | Yes |
| Port | TCP server port for the Azure Synapse database. | Yes |
| Database | The name of the Azure Synapse database. | Yes |

## Authenticating the driver

Information noteThe Azure Synapse Analytics connector does not support NTLM authentication. For that reason, the Windows integrated security option is not available.

You have the following options to authenticate the driver:

- Azure Synapse Analytics credentials
- Azure OAuth
- Microsoft Entra ID

Warning note
Microsoft Entra MFA is not supported.

Information noteWhen using Direct Access gateway, Azure OAuth and Microsoft Entra ID authentication require Direct Access gateway 1.6.6 or later.

### Azure Synapse Analytics credentials authentication

Authentication properties that can be configured

| Authentication property | Description | Required |
| --- | --- | --- |
| Authentication mechanism | Select SQL Server Authentication. | Yes |
| User name | User name for the Azure Synapse Analytics connection. | Yes |
| Password | Password for the Azure Synapse Analytics connection. | Yes |

### Azure OAuth authentication

You can authenticate using OAuth 2.0. You need an authentication pin to authenticate via OAuth:

Do the following:

1. Under Authentication, select Azure OAuth.
2. Fill in Tenant ID, Client ID, and Client Secret.
3. Click the Authenticate button in the Credentials section under Account properties. A new window opens.
4. Copy the Authentication code. Go back to the connection creation dialog.
5. Under Complete authentication with the code provided by the source, paste the authentication pin. Click Verify.

Information noteWhen using OAuth authentication, if you edit any of the connection properties after a connection has been authenticated, you must explicitly re-authenticate. This re-authentication will not be initiated automatically. If you do not re-authenticate in this situation, the connection will stop working.

Authentication properties that can be configured

| Authentication property | Description | Required |
| --- | --- | --- |
| Authentication Mechanism | Select Azure OAuth.  Information noteWhen using Direct Access gateway, Azure OAuth authentication require Direct Access gateway 1.6.6 or later. | Yes |
| Tenant ID | The Azure AD tenant to use for authentication. It is also referred to as the directory ID. | Yes |
| Client ID | The client ID when configuring the Azure AD OAuth authorization server. | Yes |
| Client Secret | The client secret when configuring the Azure AD OAuth authorization server. This needs to be inputted every time the connection needs to be re-authenticated. | Yes |

#### Azure Synapse Analytics configuration for OAuth

Your Azure Synapse Analytics database must be configured to use OAuth. The process is described in Microsoft documentation:

[Quickstart: Register an application with the Microsoft identity platform](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app)

When configuring the OAuth authorization server, the redirect\_uri must be set to: https://connector.qlik.com/auth/oauth/v2.htm

### Microsoft Entra ID authentication

You can authenticate using Microsoft Entra ID.

Information noteMicrosoft Entra ID requires a minimum .NET 6.0 installation.

Authentication properties that can be configured

| Authentication property | Description | Required |
| --- | --- | --- |
| Authentication mechanism | Select Microsoft Entra ID.  Information noteWhen using Direct Access gateway, Microsoft Entra ID authentication requires Direct Access gateway 1.6.6 or later. | Yes |
| User name | User name in Microsoft Entra ID. | Yes |
| Password | Password in Microsoft Entra ID. | Yes |

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

Information noteWhen you connect to Azure Synapse Analytics with the Data load editor dialog, Test Connection enables you to test the connection before you attempt to create it.
