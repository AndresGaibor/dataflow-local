---
title: "Configuring SSO for the Microsoft SQL Server connector"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/ODBC_Connector_help/Content/Connectors_ODBC/SQLServer/Setting-up-SSO-for-MSSQL.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "ODBC databases", "Microsoft SQL Server"]
---

# Configuring SSO for the Microsoft SQL Server connector

Information noteWhen using Qlik Cloud Analytics, this section is only relevant if you are using Direct Access gateway 1.7.13 or later and have selected the Single Sign-On authentication mechanism.

If you intend to use single sign-on (SSO) to access a Microsoft SQL Server with the Microsoft SQL Server (via Direct Access gateway) connector, you must configure the host server to enable SSO. Single sign-on permits clients to use one Windows authenticated login to access data in shared files.

To configure SSO for the Microsoft SQL Server connector (via Direct Access gateway) connector, a Windows domain administrator must do the following:

- Create service accounts in Microsoft Active Directory.
- Create service principal names (SPN) in Active Directory.
- Configure delegation for the Direct Access gateway services administrator account.
- Configure the Direct Access gateway server for SSO.
- Configure the Microsoft SQL Server connector for SSO
- Configure the Microsoft SQL Server for SSO.

Warning noteThe same Direct Access gateway services administrator account used during the Direct Access gateway (central node) installation must be used. If a different account is used, the Direct Access gateway services administrator account must own the HTTP service principal. For more information, see [User accounts](/en-US/sense-admin/November2026/Subsystems/DeployAdministerQSE/Content/Sense_DeployAdminister/QSEoW/Deploy_QSEoW/User-accounts.htm).

## Creating service accounts in Microsoft Active Directory

The service accounts created for SSO are used to authenticate connections to the host systems on which the services run. Two service accounts are required:

- Direct Access gateway server.
- Server where MS SQL Server is running.

## Creating service principal names (SPN) in Active Directory

A service principal name (SPN) is a unique identifier of a service instance. SPNs are used during authentication to associate a service instance with a service logon account. This allows a client application to request that a service authenticate an account even if the client does not have the account name. An SPN always includes the name of the host computer on which the service instance is running, so a service instance might register an SPN for each name or alias of its host.

Before the authentication service can use an SPN to authenticate a service, the SPN must be registered on the account object that the service instance uses to log on. A given SPN can be registered on only one account. For Win32 services, a service installer specifies the logon account when an instance of the service is installed. The installer then composes the SPNs and writes them as a property of the account object in Active Directory Domain Services. If the account of a service instance changes, the SPNs must be re-registered under the new account.

When a client connects to a service, it locates an instance of the service, composes an SPN for that instance, connects to the service, and presents the SPN for the service to authenticate.

To set up SSO for Microsoft SQL server, you must create SPNs for the Direct Access gateway services administrator account.

Do the following:

1. Open an elevated command prompt with domain administrator credentials.
2. Enter the following to create an SPN for the Direct Access gateway services administrator:

   setspn -A HTTP/<Direct Access gateway\_server>:<port> <domain>\<Qlik\_Sense\_services\_administrator>

   Information noteThe <Direct Access gateway\_server> must be entered as the fully qualified domain name of the server.

   Information noteThe <Direct Access gateway\_server> is the machine where the Direct Access gateway service is running.
3. Enter the following to create an SPN for the MS SQL Server services administrator:

   setspn -A MSSQLSvc/<server\_name>:<port> <domain>\<services\_administrator>

   Information noteThe <server\_name> must be entered as the fully qualified domain name of the server.
4. Enter the following commands to verify the result of your SPN setup:
   1. setspn -L <domain>\<Qlik\_Sense\_services\_administrator> to verify the Direct Access gateway services administrator.
   2. setspn -L <domain>\<MS\_Sql \_server\_services\_administrator> to verify the MS SQL Server services administrator.

## Configuring delegation for the Direct Access gateway services administrator account

Delegation allows a front-end service to forward client requests to a back-end service so that the back-end service can also impersonate the client. Impersonation is used to check whether a client is authorized to perform a particular action, while delegation is a way of flowing impersonation capabilities, along with the client’s identity, to a back-end service.

To configure SSO for Microsoft SQL Server, you must set up delegation rights to the Microsoft SQL Server service for the Direct Access gateway services administrator.

A Windows domain administrator can change the delegation tab on the Direct Access gateway services administrator account properties page.

Do the following:

1. Open the Active Directory Users and Computers management tool with Windows domain administrator credentials.
2. Right click on your Direct Access gateway services administrator account and click Properties.
3. Go to the Delegation tab, and select Trust this user for delegation to specified services only, then select  Use any authentication protocol.
4. Click Add....
5. On the Add Services window, click Users or Computers....
6. On the Select Users or Computers window, enter the domain and user name of the Microsoft SQL Server services administrator and click OK.
7. On the Add Services window, select the Microsoft SQL Server service and click OK.

You can verify your delegation configuration on the Delegation tab. The MS SQL Server service should now be set as the service to which the Direct Access gateway services administrator can present delegation credentials.

## Configuring the Direct Access gateway server for SSO

To configure the Direct Access gateway server for SSO with Microsoft SQL Server, you must:

- Add the Direct Access gateway services administrator to the Administrator group on the Direct Access gateway server if it is not already part of that group.
- Add Direct Access gateway services administrator as part of the Act as part of the operating system role in the Local Security Policy.

Do the following:

1. Log on to the Direct Access gateway server as an administrator.
2. Open Local Security Policy, and go to Security Settings > Local Policies > User Rights Assignment.
3. Under Policy, right click on Act as part of the operating system and select Properties.
4. On the Local Security Setting tab, click Add User or Group....
5. Add the Direct Access gateway services administrator account, and click OK.

## Configuring the MS SQL Server connector for SSO

To configure the Microsoft SQL Server connector (via Direct Access gateway) connector for SSO, you must be logged in as an administrator to the Direct Access gateway server. If you logged in for the previous configuration steps on the Direct Access gateway server, you can simply continue with the following steps:

Do the following:

1. Open Local Security Policy, and go to Security Settings > Local Policies > User Rights Assignment.
2. Under Policy, right click on Impersonate a client after authentication and select Properties.
3. On the Local Security Setting tab, click Add User or Group....
4. Add the Direct Access gateway services administrator account, and click OK.
5. Restart the Direct Access gateway server.

   The server must be restarted for the policy changes to take effect.

## Configuring Microsoft SQL Server for SSO

To configure the Microsoft SQL Server for SSO, you must ensure that the Microsoft SQL Server service runs as the Microsoft SQL Server services administrator.

Do the following:

1. Log on to the Microsoft SQL Server as an administrator.
2. Open the Sql Server Configuration Manager.
3. Select SQL Server Services.
4. Select SQL Server in the right pane and verify that the Log On As column is populated with your Microsoft SQL Server services administrator account.

Information noteYou must reboot after making changes to remove the SQL self-registration of the SPN under machine account and register the SPN manually on the domain account.
