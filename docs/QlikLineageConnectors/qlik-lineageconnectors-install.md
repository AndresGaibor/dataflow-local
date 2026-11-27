---
title: "Installing Qlik Lineage Connectors"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikLineageConnectors/qlik-lineageconnectors-install.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Delivering data and lineage for analytics", "Extracting lineage data with Qlik Lineage Connectors"]
---

# Installing Qlik Lineage Connectors

Expand/Collapse all

# Installing Qlik Lineage Connectors

Qlik Lineage Connectors
 are installed locally and accessed as a service on your web browser.

## Qlik Lineage Connectors requirements

Qlik Lineage Connectors can coexist with your BI tools on the same server. What Qlik Lineage Connectors need in terms of a memory footprint is linear to the number of objects and files in the environment you intend to cover. Since Qlik Lineage Connectors only use metadata surrounding your solution, they generally consume significantly less resources than the systems they connect to.

Qlik Lineage Connectors requirements

|  |  |
| --- | --- |
| Platforms | Windows 10 or Windows Server (with .NET 4.7.2 or higher) |
| Processors (CPUs) | dual-core 1.6 GHz |
| Memory (RAM) | 2 GB  Memory requirements are directly related to the amount of data being analyzed. |
| Disk space | 2 GB  Qlik Lineage Connectors have light storage requirements; parsed application logs and graph result sets are saved to disk then streamed to Qlik Cloud. |
| PowerShell | 5.1 is installed by default on Windows 10 with automatic updates enabled. |
| TLS | 1.2 or higher  By default, Qlik Lineage Connectors use TLS1.2 on port 4114. If NTLM authentication is used, 4115 is also used. When communicating with external systems, Qlik Lineage Connectors default to TLS 1.2, but will downgrade to TLS 1.0/1.1 if required by the server. |
| System cryptography | Qlik Cloud Government supports using Qlik Lineage Connectors only when Windows is configured to run in a FIPS 140-2 approved mode of operation (FIPS mode). To turn on FIPS mode, enable the Windows policy: [System cryptography: Use FIPS compliant algorithms for encryption, hashing, and signing](https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/system-cryptography-use-fips-compliant-algorithms-for-encryption-hashing-and-signing). For more information, see step 3 of the procedure [Using Windows in a FIPS 140-2 approved mode of operation](https://learn.microsoft.com/en-us/windows/security/threat-protection/fips-140-validation#using-windows-in-a-fips-140-2-approved-mode-of-operation).  Information noteNo additional modules need to be installed (step 1 and 2). Qlik Lineage Connectors use only the modules already provided by Windows and included in the [list of validated modules](https://learn.microsoft.com/en-us/windows/security/threat-protection/fips-140-validation#microsoft-fips-140-2-validated-cryptographic-modules). Qlik Lineage Connectors enforce the use of only FIPS-validated cryptographic algorithms through .NET Runtime (step 4). |

## Qlik Lineage Connectors installer

Installation of Qlik Lineage Connectors is done by running the installer. To download the installation package, click your user profile menu, select Settings, and go to Tools. Locate the Qlik Lineage Connector and click Download. By default, it will be installed into your C:/ drive Program Files folder and data and logs will be stored under the common ProgramData folder.

Do the following:

1. Save the installation package locally and run setup.exe to start the installation.
2. Select Next to continue.

![Qlik Lineage Connector wizard welcome](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_QlikLineageConnector_Install1.png)

3. Review the license agreement for the Qlik Lineage Connectors software package; select  I Agree and Next to continue the installation.

![Review the Qlik Lineage Connectors license agreement + select I Agree to continue the installation](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_QlikLineageConnector_Install2.png)

4. Keep the default install folder (C:\ProgramFiles\Qlik\LineageConnector\) or select a different location and select Next.

![Select the folder in which to save the Qlik Lineage Connector software package](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_QlikLineageConnector_Install3.png)

5. Select Next to begin the installation of Qlik Lineage Connectors.

Confirm installation of Qlik Lineage Connectors.

![Confirm Qlik Lineage Connector installation](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_QlikLineageConnector_Install4.png)

6. A console output window registers installation processes. Enter service account Username and Password credentials to run the Qlik Lineage Connectors in the dialog window. Passwords require at least 7 alpha-numeric characters and at least one special character (example, ! @ # ?).

   These are the server account credentials for the service account that will be running Qlik Lineage Connectors. Select Ok.

   Information noteThe service account is used to access files and logs used in the BI solution. For example, this service account in QlikView or QlikSense must have the same or higher access rights as the service account running the QlikView Publisher service or the Qlik Sense services. It is recommended to use the same service account credentials as the credentials that are running Qlik services. During the reload of Qlik Lineage Connectors these files will be accessed to retrieve metadata or to extract lineage information. A sufficiently high level of access is needed in order to retrieve this information.

![Credentials for service account](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_QlikLineageConnector_Install_QLCService.png)

7. Create a root password for Qlik Lineage Connectors settings.

![Create a root password for QLC settings](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_QlikLineageConnector_Install_RootPW.png)

8. Create an internal Qlik Lineage Connectors admin account and select Ok. These credentials will be used to access Qlik Lineage Connectors at the login screen. (See [*Sign in with the admin credentials you created upon installation*](#Sign_in_with_admin_credentials))

![create Qlik Lineage Connectors admin account by entering admin credentials](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_QlikLineageConnector_Install_QLCAdminAcct.png)

9. Select Close when the installation is complete.

![Qlik lineage connector screen install complete](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_QlikLineageConnector_InstallComplete.png)

## Accessing and running Qlik Lineage Connectors

Installing Qlik Lineage Connectors extracts the program files into the installation root directory and creates the service called Qlik Lineage Connector Service. The service runs with the default account Local System. You can find this under Services in Windows. The Qlik Lineage Connectors service is now installed and runs with the default account Local System.

Information noteThe Qlik Lineage Connectors service account needs to be a local admin on the server where it is installed, and it must have read access to all the files and file shares used by any of the monitored systems. Qlik Lineage Connectors are by default set up to use the Local System account as the running account. This needs to be changed under Microsoft Services if the default does not have read access to your file environment. In addition to the service account, different connectors may require special rights to be able to extract all available metadata. For more information, see [*Additional system access for Qlik Lineage Connectors*](#Addition)

Qlik Lineage Connectors
 can now be accessed by:

- Using a web browser and the URL: https://localhost:4114 or http://<servername>:4114
- Using the Windows program shortcut on the installed machine: Qlik Lineage Connector

You should now be presented with the Sign In page for Qlik Lineage Connectors, indicating a successful installation.

Do the following:

- Sign in with the admin credentials you created upon installation

![sign into Qlik Lineage Connectors webpage with admin credentials](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_QlikLineageConnector_Install_WebpageSignin.png)

## Communication and port settings

Qlik Lineage Connectors
 run as a web service on the installed machine. Port 4114 is the default port but the port can be changed in a config file. Users must be able to access this port from their machines. For more information, see [*Editing server configuration*](#Server)

For outbound communication, Qlik Lineage Connectors need to be able to communicate with the different ports that each separate system uses. Refer to documentation provided by the BI tools and source systems. Service Message Block (SMB) also needs to be enabled to access any folders using shared Universal Naming Convention (UNC) paths.

Inbound communications depend on whether Qlik Lineage Connectors should be accessed from users outside of the server or not. The default port is 4114, and if you plan to use Windows NT LAN Manager (NTLM) authentication, a separate endpoint is running behind the scenes on port 4115 as default.

The ports can be modified to any ports preferred. If the server is dedicated to Qlik Lineage Connectors, then 80/8080 or 443/4443 can be used instead.

If you are using email [notifications](#glossary-0 "Glossary term"), access to a Simple Mail Transfer Protocol (SMTP) server is required. If you are using Slack hooks, Qlik Lineage Connectors need to be able to communicate with slack.com over the internet.

## Editing server configuration

Qlik Lineage Connectors
 default ports and settings can be configured by editing the configuration file.

The service configuration file is a JSON structure. The default placement for the service configuration file is in the install root directory: C:\ProgramData\Qlik\LineageConnector\ svc.configThe following is an example service configuration with default values:

- Prior to any editing, be sure the service is stopped.

The configuration file is an XML file and provides a pointer to the directory and password for the services file. The following is an example configuration:

```
<configuration>
...
<appSettings>
	<DataDirectory value="" />
	<DbPassword value="" />
<appSettings>
<configuration>
```

Server configuration attributes

What do these attributes do?

| Attribute | Parameter | Note |
| --- | --- | --- |
| DataDirectory | A valid file path on a local resource. | Decides the data folder for the Qlik Lineage Connectors service. Defaults to C:\ProgramData\Qlik\LineageConnectors. Used to change post-installation where the server configuration lies. |
| DbPassword | Database password | The encrypted root password provided during the installation of Qlik Lineage Connectors. If a non-encrypted value is entered, this will be detected and replaced during service startup. All encrypted databases will be unreadable if this is removed/altered. Changing service account post-installation also requires an unencrypted password entry as this is tied to the service account. |

```
{
"Host": "*",
"Port": 4114,
"UseTLS": true,
"AuditLog": false,
"AuditLogLevel": "Full",
"Authentication": "Internal",
"HeaderUser": "x-nod-user",
"HeaderGroup": "x-nod-group",
"HeaderResolveADGroups": true,
"NtlmUrl": "https://localhost:4115/ntlm/token",
"NtlmPort": 4115,
"DisableScheduler": false
}
```

Service configuration attributes

What do these attributes do?

| Attribute | Parameter | Note |
| --- | --- | --- |
| Host | \* , localhost, \*.domain.com, servername | This configures allowed host calls. Allows blocking of requests aimed to localhost for example, or only allow calls where domain is specified: Wildcard-pattern match. |
| Port | Any non-reserved port | Change default port of your Qlik Lineage Connectors landing point. |
| UseTLS | true or false | Set this to true to enforce https calls. You must bind a certificate to the port. This attribute is not specific to Qlik Lineage Connectors. See Microsoft Documentation, [MSDN - Configuring SSL and Certificates](https://docs.microsoft.com/en-us/dotnet/framework/wcf/feature-details/how-to-configure-a-port-with-an-ssl-certificate). |
| AuditLog | true or false | Enables audit logging. |
| AuditLogLevel | Full or Limited | If enabled, this attribute sets the detail level of audit logging. |
| Authentication | None, Internal, NTLM, Header, SAML | Configured authentication mode. |
| HeaderUser | x-nod-user (Default header field name, can be any custom value.) | When using Header as authentication mode, this header field should be added by proxy in request. Example value for AD users: Domain\User. |
| HeaderGroup | x-nod-group (Default header field name, can be any custom value.) | When using Header as authentication mode for AD users, this header field could be added by proxy to map AD groups to user specified in HeaderUser. Example values for AD groups using a comma separated list:  Domain\GroupName1, Domain\GroupName2. |
| HeaderResolveADGroups | true or false | When using Header as authentication mode for AD users, Qlik Lineage Connectors will try to connect to AD and resolve AD groups for user specified in HeaderUser if true. The LDAP server to be used for lookups then needs to be specified under general Qlik Lineage Connectors settings. |
| NtlmUrl | http(s)://localhost:4115/ntml/token , http(s)://servername.domain.com:4115/ntml/token | Endpoint accessible from end user browsers to Qlik Lineage Connectors for NTLM resolving. Depending on your proxy, user call setup, or multi-AD setup, adjust for environment. |
| NtlmPort | Any non-reserved port. | Reserved port for NTLM resolution endpoint if adjusted for NtlmUrl. |
| DisableScheduler | true or false | Disables all scheduled tasks and only operates on manual triggers. |

## Qlik Lineage Connectors service configuration

Communication with Qlik Cloud might be hindered by local network settings. If your network uses proxies or other local limitations, editing the Qlik Lineage Connectors service configuration might be need to properly communicate with the Qlik Cloud tenant.

The configuration file is an XML file and its default location is C:\Program Files\Qlik\LineageConnector\QLCService.exe.config.

This is the default configuration:

<?xml version="1.0" encoding="utf-8"?>
<configuration>
<startup>
<supportedRuntime version="v4.0" sku=".NETFramework,Version=v4.7.2" />
</startup>
<runtime>
. . .
</runtime>
<system.serviceModel>
. . .
</system.serviceModel>
<!-- Uncomment proxy settings below to use default proxy on machine. -->
<!--
<system.net>
<defaultProxy enabled="true" useDefaultCredentials="true">
<proxy usesystemdefault="true" />
</defaultProxy>
</system.net>
-->
<appSettings>
<add key="DbPassword" value="" />
</appSettings>
</configuration>

To use the default network configuration as instructed by the Global Policy/Windows policy, uncomment the <system.net> proxy settings. If you still have communication issues after making these changes, contact your network administrator for proxy configurations and other network-specific limitations.

## Additional system access for Qlik Lineage Connectors

Additional configuration steps may be required to ensure access to BI tools and data source environments to extract all available metadata.

### QlikView

No extra access is required.

### Qlik Sense

An exported trust certificate from the Qlik Management Console (QMC) will be required by Qlik Lineage Connectors for API calls to be allowed. The service account also needs to be RootAdmin to ensure full rights during API calls. For this reason, it is best to run Qlik Lineage Connectors with the same service account as Qlik services use by adding it to the local admin group on the server.

### Qlik NPrinting

Access to Qlik NPrinting is configured by a connection string to Qlik NPrinting's underlying PostgreSQL database. In addition to the account credentials, Qlik Lineage Connectors' system DNS/IP must be placed on Qlik NPrinting's host configuration allowlist. For production, a separate Postgres user should be set up for Qlik Lineage Connectors use.

#### Open POSTGRES for External Connections

If Qlik Lineage Connectors and Qlik NPrinting servers are installed on different machines, the Qlik NPrinting PostgreSQL instance needs to be configured to accept external connections.

The configuration files are located on the Qlik NPrinting server under: %ProgramData%\NPrinting\data\

In the file postgresql.conf: file uncomment or add listen\_address with an \* asterisk value:

Listen\_address on postgresql.conf

![The Listen addresses, found below the Connection and Authentication label.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/NodeGraph/ui-NodeGraphTD-115.png "Click to view full size")

In the pg\_hba.conf file, add a host entry to add the Qlik Lineage Connectors server IP to the allowlist:

Allowlisting Qlik Lineage Connectors server IP

![The host entry, with fields for the database, user, address, and method.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/NodeGraph/ui-NodeGraphTD-116.png "Click to view full size")

### Tableau

During the connector setup, a Tableau user is specified, either by using the credentials directly or by specifying a Personal Access Token. The Tableau user specified needs to be Site Administrator or have similar rights for content extraction.

### Snowflake

The Snowflake account needs to be AccountAdmin for the databases intended to be read by Qlik Lineage Connectors. Authentication on the Snowflake account is configured by user/password in the connector configuration fields.

### MS SQL

The account used to connect to the MS SQL server needs to be sysadmin. During the connector setup in Qlik Lineage Connectors, a connection string needs to be entered. This makes it possible for the Qlik Lineage Connectors admin to decide whether internal authentication with the Qlik Lineage Connectors service account should be used, or if a specific database user should be specified.

### Oracle

The account used to connect to the Oracle server does not have to have the role of sysadmin but the detectable database objects are limited by the user [permissions](#glossary-1 "Glossary term"). When configuring an Oracle connector, a connection string is entered. At this time it is possible for the admin to decide whether internal authentication with the service account should be used, or whether a specific database user should be specified.

## Upgrading Qlik Lineage Connectors

Qlik Lineage Connectors can be upgraded on the Windows machine it is installed on.

Information noteYou must uninstall the existing version of Qlik Lineage Connectors before installing new patches and versions.

Do the following:

1. Open and sign into Qlik Lineage Connectors with your Admin credentials.
2. Select the ![About icon](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_info.svg) icon to open About Qlik Lineage Connectors. A notification on the information icon will indicate that a newer version is available. A box opens with Current version information. If you are not on the most current version, an option to Download latest version: x.x.x displays. Select the link to download the latest version.
3. Select the Windows key, Windows + S shortcut, or click in the search box on the taskbar, find “add or remove programs”.
4. Select Qlik Lineage Connectors in the list of installed apps and select Uninstall.
5. Select the downloaded QlikLineageConnectorSetup.msi file and follow the setup screens entering Service credentials Admin password when prompted. The upgrade installs automatically and configured projects and connectors are preserved.

## Uninstalling Qlik Lineage Connectors

Qlik Lineage Connectors can be uninstalled on the Windows machine through the Add or Remove Programs utility.

Do the following:

1. Select the Windows key, Windows + S shortcut, or click in the search box on the taskbar, enter “add or remove programs” or “apps & features”, and add or remove programs.
2. Select Qlik Lineage Connectors in the list of installed apps and select Uninstall.
