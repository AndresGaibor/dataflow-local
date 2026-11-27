---
title: "Configuring SSO for the Teradata connector"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/ODBC_Connector_help/Content/Connectors_ODBC/Teradata/Setting-up-SSO-for-Teradata.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "ODBC databases", "Teradata"]
---

# Configuring SSO for the Teradata connector

Information noteWhen using Qlik Cloud Analytics, this section is only relevant if you are using Direct Access gateway 1.7.13 or later and have selected the Single Sign-On authentication mechanism.

If you intend to use single sign-on (SSO) to access a Teradata database with the Teradata (via Direct Access gateway) connector, you must configure the host server to enable SSO. Single sign-on permits clients to use one Windows authenticated login to access data in shared files.

A Windows domain administrator must do the following to configure SSO for the ODBC Connector Package's Teradata connector:

- Create service accounts in Microsoft Active Directory.
- Create service principal names (SPN) in Active Directory.
- Run ktpass to create the Kerberos keys.
- Create user on the Teradata database with NULL password.
- Configure delegation for the Direct Access gateway services administrator account.
- Configure the Direct Access gateway server for SSO.
- Configure the Teradata connector for SSO

Warning noteThe same Direct Access gateway services administrator account used during the Direct Access gateway (central node) installation must be used. If a different account is used, the Direct Access gateway services administrator account must own the HTTP service principal. For more information, see [User accounts](/en-US/sense-admin/November2026/Subsystems/DeployAdministerQSE/Content/Sense_DeployAdminister/QSEoW/Deploy_QSEoW/User-accounts.htm).

## Creating service accounts in Microsoft Active Directory

The service accounts created for SSO are used to authenticate connections to the host systems on which the services run. Two service accounts are required:

- Direct Access gateway server.
- Server where Teradata is running.
- Create user in Active Directory for each Teradata node.

## Creating service principal names (SPN) in Active Directory

A service principal name (SPN) is a unique identifier of a service instance. SPNs are used during authentication to associate a service instance with a service logon account. This allows a client application to request that a service authenticate an account even if the client does not have the account name. An SPN always includes the name of the host computer on which the service instance is running, so a service instance might register an SPN for each name or alias of its host.

Before the authentication service can use an SPN to authenticate a service, the SPN must be registered on the account object that the service instance uses to log on. A given SPN can be registered on only one account. For Win32 services, a service installer specifies the logon account when an instance of the service is installed. The installer then composes the SPNs and writes them as a property of the account object in Active Directory Domain Services. If the account of a service instance changes, the SPNs must be re-registered under the new account.

When a client connects to a service, it locates an instance of the service, composes an SPN for that instance, connects to the service, and presents the SPN for the service to authenticate.

To set up SSO for Teradata, you must create SPNs for the Direct Access gateway services administrator account.

Do the following:

1. Open an elevated command prompt with domain administrator credentials.
2. Enter the following to create an SPN:

   setspn -A TERADATA/<Teradata\_Host\_Name>@<domain> <domain>\<user>

   Information noteThe <Teradata\_Host\_Name> must be entered as the fully qualified domain name of the Teradata node.

   Information noteThe <user> is the user created in Active Directory for Teradata node.
3. Enter the following commands to verify the result of your SPN setup: setspn -L <domain>\<user>

   Information noteThe <user> is the user created in Active Directory for Teradata node.

## Running ktpass to create Kerberos keys

Do the following:

1. Use the ktpass command to create the key for the Teradata database node in the domain controller: ktpass -princ SPN -mapuser <teradata node\_name> -pass password -ptype KRB5\_NT\_PRINCIPAL -out keytab\_filename
2. Copy the keytab file to the Teradata server. It needs to be merged with any existing keytab file on the Teradata server.

Refer to the [Teradata documentation](https://docs.teradata.com/r/ACm5X1AxfP9ltcSZbN8Gsw/BM4fuhrICwax4IJco73t7Q) for more information.

## Creating a user with null password

All users authenticated by Kerberos must have LOGON WITH NULL PASSWORD privileges defined in each database to which they can log on.

Do the following:

- Input:

  CREATE USER <user> AS PERM=1000, PASSWORD = <password>;

  GRANT LOGON ON ALL TO <user> WITH NULL PASSWORD;

See the following for more information:

- [Kerberos Authentication with Database Authorization](https://docs.teradata.com/reader/ACm5X1AxfP9ltcSZbN8Gsw/d46YuxR~p9aMyT6J7agkFg)
- [Grant Logon](https://docs.teradata.com/reader/Zab4857ITLP4IWlYEHeBBA/k9e7JxQaRvzaMxSbif_6Xg)

You should use the Basic Teradata Query Utility to validate the SSO connection:

c:\Program Files\Teradata\Client\17.00\bin> bteq

Teradata BTEQ 17.00.00.04 (64-bit) for WIN64. PID: 16344 Copyright 1984-2020 Teradata. All rights reserved.

Enter your logon or BTEQ command:

.set logonprompt off

\*\*\* Logon prompts disabled. Type .LOGONPROMPT ON; to re-enable.

Teradata BTEQ 17.00.00.04 (64-bit) for WIN64. Enter your logon or BTEQ command:

.logon <Teradata server>/,

\*\*\* Logon successfully completed.

\*\*\* Teradata Database Release is 16.20.32.23 \*\*\* Teradata Database Version is 16.20.32.23 \*\*\* Transaction Semantics are BTET.

\*\*\* Session Character Set Name is 'ASCII'.

\*\*\* Total elapsed time was 1 second.

BTEQ -- Enter your SQL request or BTEQ command:

select username from dbc.users;

\*\*\* Query completed. One row found. One column returned. \*\*\* Total elapsed time was 1 second.

UserName

------------------------------

<user>@<domain>

BTEQ -- Enter your SQL request or BTEQ command:

.quit;

## Configuring delegation for the Direct Access gateway services administrator account

Delegation allows a front-end service to forward client requests to a back-end service so that the back-end service can also impersonate the client. Impersonation is used to check whether a client is authorized to perform a particular action, while delegation is a way of flowing impersonation capabilities, along with the client’s identity, to a back-end service.

To configure SSO for Teradata, you must set up delegation rights to the Teradata service for the the Direct Access gateway services administrator.

A Windows domain administrator can change the delegation tab on the Direct Access gateway services administrator account properties page.

Do the following:

1. Open the Active Directory Users and Computers management tool with Windows domain administrator credentials.
2. Right click on your Direct Access gateway services administrator account and click Properties.
3. Go to the Delegation tab, and select Trust this user for delegation to specified services only, then select  Use any authentication protocol.
4. Click Add....
5. On the Add Services window, click Users or Computers....
6. On the Select Users or Computers window, enter the domain and user name of the Teradata services administrator and click OK.
7. On the Add Services window, select the Teradata service and click OK.

You can verify your delegation configuration on the Delegation tab. The Teradata service should now be set as the service to which the Direct Access gateway services administrator can present delegation credentials.

## Configuring the Direct Access gateway server for SSO

To configure the Qlik Sense server for SSO with Teradata, you must:

- Add the Direct Access gateway services administrator to the Administrator group on the Direct Access gateway server if it is not already part of that group.
- Add Direct Access gateway services administrator as part of the Act as part of the operating system role in the Local Security Policy.

Do the following:

1. Log on to the Direct Access gateway server as an administrator.
2. Open Local Security Policy, and go to Security Settings > Local Policies > User Rights Assignment.
3. Under Policy, right click on Act as part of the operating system and select Properties.
4. On the Local Security Setting tab, click Add User or Group....
5. Add the Direct Access gateway services administrator account, and click OK.

## Configuring the Teradata connector for SSO

To configure the Teradata (via Direct Access gateway) connector for SSO, you must be logged in as an administrator to the Direct Access gateway server. If you logged in for the previous configuration steps on the Direct Access gateway server, you can simply continue with the following steps:

Do the following:

1. Open Local Security Policy, and go to Security Settings > Local Policies > User Rights Assignment.
2. Under Policy, right click on Impersonate a client after authentication and select Properties.
3. On the Local Security Setting tab, click Add User or Group....
4. Add the Direct Access gateway services administrator account, and click OK.
5. Restart the Direct Access gateway server.

   The server must be restarted for the policy changes to take effect.
