---
title: "Installing Qlik DataTransfer"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikDataTransfer/install-Qlik-DataTransfer.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Managing data governance and transfers"]
---

# Installing Qlik DataTransfer

Qlik DataTransfer is a lightweight Windows application that lets you upload data from on-premises data sources to a Qlik Cloud [tenant](#glossary-0 "Glossary term") without firewall tunneling.
The service account owner (SAO) or [tenant administrator](#glossary-1 "Glossary term") generates an API key from the tenant, which is then used to authenticate Qlik DataTransfer. Once authenticated, you can schedule automatic data reloads or upload data manually.

Tip noteQlik recommends using the Qlik Data Gateway - Direct Access to load data from on premises into a Qlik Cloud tenant. The supported databases and the Generic ODBC Connector Package, together with the support for loading on premises files, can allow you to decommission Qlik DataTransfer servers (and potentially repurpose them for gateways).

New users are encouraged to use the File connector via Direct Access gateway and only use Qlik DataTransfer if absolutely necessary. For more information, see [Qlik Data Gateway - Direct Access](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/direct-access-gateway.htm) and [File (via Direct Access gateway)](/en-US/cloud-services/Subsystems/Web_Storage_Provider_Connectors_help/Content/Connectors_StorageProvider/Storage%20provider%20connectors/File-DG-storage-provider-connector.htm).

Qlik Cloud Government noteQlik DataTransfer supports encrypted communications but is not FIPS compliant (Federal Information Processing Standards). Qlik Cloud Government users can use it in their implementation pending their own risk review.

Qlik DataTransfer works with the following kinds of data sources:

- Application data
- Connection data
- Folders

For information on data types that are available with Qlik DataTransfer, see [*Uploading on-premises data with Qlik DataTransfer*](qlik-datatransfer.htm).

An installation of Qlik DataTransfer can only be associated to a single Qlik Cloud tenant.

## Qlik DataTransfer system requirements

Qlik DataTransfer requirements

|  |  |
| --- | --- |
| Platforms | - Microsoft Windows Server 2016 - Microsoft Windows Server 2019 - Microsoft Windows Server 2022 - Microsoft Windows Server 2025   For development and testing purposes only:   - Microsoft Windows 10 (64-bit version only)   Information noteThese operating systems are supported by Qlik Sense. Third-party software may require service packs to be installed. |
| Processors (CPUs) | Multi-core x64 compatible processors. We recommend a minimum of 4 cores. |
| Memory | 8 GB minimum  The memory requirements for the Qlik Sense products are directly related to the amount of data being analyzed. |
| Disk space | 2 GB minimum |
| Storage | Sufficient storage is required for the volume of applications and content used in the deployment. |
| PowerShell | 5.1 or higher |
| TLS | 1.2 |

## Before you begin

Before you download and run the Qlik DataTransfer installer, make sure you meet the following requirements:

Qlik Cloud and user permissions

- Access to a Qlik Cloud tenant.
- Professional user entitlement (applies only to user-based subscriptions).
- Manage API keys permission, assigned through a custom role or the default permissions. For information, see [*Managing API keys*](../Admin/mc-generate-api-keys.htm).
- Access to all spaces where you will upload data from Qlik DataTransfer. For more information, see [*Managing spaces*](../Admin/mc-administer-spaces.htm).

Access and permissions on your Windows machine

- Administrator permission on a Windows machine with access to on-premises data sources.
- A Windows machine that meets the system requirements. For details, see [System requirements for Qlik DataTransfer](/en-US/sense-admin/November2026/Subsystems/DeployAdministerQSE/Content/Sense_DeployAdminister/Common/system-requirements.htm#QDT).
- The policy SSL Configuration Settings set to support only IANA-format ciphers.
- Permission to execute PowerShell scripts with the RemoteSigned execution policy.

TLS and cipher requirements (Windows Server 2012 R2)

If installing or upgrading to Qlik DataTransfer May 2021 or later on Windows Server 2012 R2:

- Update the TLS Cipher Suite. Default ciphers in Windows Server 2012 R2 are not supported. Required ciphers:

  - TLS\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384
  - TLS\_ECDHE\_RSA\_WITH\_CHACHA20\_POLY1305\_SHA256
  - TLS\_ECDHE\_RSA\_WITH\_AES\_128\_GCM\_SHA256
  - TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA384
  - TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA256
- For instructions, see [Qlik Community: Adding Cipher Suite for Qlik Data Transfer on Windows 2012 R2](https://community.qlik.com/t5/Knowledge/Adding-Cipher-Suite-for-Qlik-Data-Transfer-on-Windows-2012-R2/ta-p/1819406).

Service account requirements

- Qlik DataTransfer requires a Windows user account. A dedicated user account with administrator privileges is recommended to run the service.
- If the dedicated user is an administrator, log in as that user to install Qlik DataTransfer. If not, use an administrator account.
- On a Windows server with Qlik Sense Enterprise on Windows installed, Qlik DataTransfer must be installed with the Qlik Sense services user used in the Qlik Sense installation.
- If you change the service log-on account after configuring Qlik DataTransfer, reconfigure the tenant and [connections](#glossary-2 "Glossary term"), delete token.json in %ProgramData%/Qlik/DataTransfer/DataUpload/storage, and restart the Qlik DataTransfer service.

Additional recommendations

- For February 2021 SR1, it is recommended to install Qlik DataTransfer on a separate server from Qlik Sense Enterprise on Windows or QlikView Server. Installing on the same server, Qlik DataTransfer runs using the Local System user account. If you change the service user account, it will stop either Qlik DataTransfer or the Qlik Sense Service Dispatcher.

Tip noteThe Qlik DataTransfer installer includes an instance of the Qlik associative engine, ODBC connectors, and the Qlik DataTransfer agent. When launched, it consumes additional memory and processing resources which must be considered if your server is sharing resources with other applications. For a production environment, we recommend that you install Qlik DataTransfer on its own server.

## Confirming the installation user account execution policy

The user account installing Qlik DataTransfer must have permission to execute PowerShell scripts with the RemoteSigned execution policy. If you do not have permission to assign the user account permissions, contact your administrator to give the installation user account these permissions.

Do the following:

1. Open PowerShell in administrator mode.
2. Run Get-ExecutionPolicy. It should be RemoteSigned. If it is Restricted or Disabled, continue to the next step.
3. Run Set-ExecutionPolicy RemoteSigned.
4. Select Y.

## Download and run the installer

Information note

If you are installing or upgrading Qlik DataTransfer on a Windows server with Qlik Sense Enterprise on Windows installed, Qlik DataTransfer must be installed with the Qlik Sense services user used in the Qlik Sense installation.

Do the following:

1. Download the Qlik DataTransfer.exe file from either:

   - [Product Downloads](https://community.qlik.com/t5/Downloads/tkb-p/Downloads)

     For more information, see [*Downloading tools and installation files*](../Introduction/Download_install_files.htm).
   - Qlik Cloud

     Click your profile icon in the top right-hand corner, then click Settings. Under Other, click Tools.

     Qlik Cloud Government noteThis option is not available in Qlik Cloud Government.
2. Run the installer and accept the Qlik User License Agreement. The default installation path is %Program Files%\Qlik\DataTransfer. When entering the service credentials , the username must be in the form domain\username.

   Information note

   If you enter a username that is more than 20 characters long, it must be in User Principal Name (UPN) format, and must include the full domain name. For example, longusername@full.domain.name.

   Information note

   If you have a Qlik Sense Desktop or another Qlik platform installed on the same server, you must shut down them down and stop the Qlik services before you can install Qlik DataTransfer .

   ![Qlik dataTransfer installer screen](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Qlik-DataTransfer-Installer.jpg)

   Once installed, restart the Qlik services in the following order:

   1. Qlik Sense Service Dispatcher
   2. Qlik Logging Service
   3. Qlik Sense Repository Service
   4. Qlik Sense Proxy Service
   5. Qlik Sense Engine Service
   6. Qlik Sense Scheduler Service
   7. Qlik Sense Printing Service
3. On the Service Credentials window, enter username and password for the account that you want use to run the Qlik DataTransfer services.
4. See [Configuring Qlik DataTransfer](configure-Qlik-DataTransfer.htm) to customize additional settings in the services.config file.

The installer creates a desktop shortcut to launch Qlik DataTransfer application.

## Generate an API key

API keys expire. The default expiration times might not be appropriate for your business needs. Before generating an API key, consider changing the maximum token expiration in the Administration activity center settings. For information, see [*Managing API keys*](../Admin/mc-generate-api-keys.htm#Enabling).

Information noteA license is required in order to generate an API key.

Do the following:

1. Log in to your Qlik Cloud tenant.
2. From your [activity center](#glossary-3 "Glossary term"), click your profile icon in the top right-hand corner, then click Settings.
3. Select API Keys.
4. Select Generate new key.

   ![Cloud hub settings menu, generate API key](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Generate-API-Key.png)
5. Enter a name for the API key and select the Expires in time.
6. Click Generate.

   ![Generate new API key screen](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/create-API-key.png)
7. Click Copy and close to copy the API to your clipboard.

   Information noteMake sure to save the API key. You need this key to authenticate Qlik DataTransfer .

   ![API key summary screen](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/New-API-Key.png)

   Now that you have an API key, you can create a secure connection between Qlik DataTransfer and your Qlik Cloud tenant.
   The API key is used to authenticate Qlik DataTransfer when uploading data to the tenant. Since the API has an expiry time, you need to create a new API key and reauthenticate Qlik DataTransfer when this key expires. You do not need to recreate your data connections if the API key expires.

## Authenticate Qlik DataTransfer

Do the following:

1. Open Qlik DataTransfer .

   The first time you open Qlik DataTransfer , the Setup Qlik DataTransfer  authentication screen appears.

   ![Qlik dataTransfer API key connection screen](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Qlik-DataTransfer-auth-tenant.png)
2. Enter a name for the connection.
3. Enter the URL to the Qlik Cloud tenant.
4. Paste the API key you generated from the tenant.
5. Click Apply to validate the tenant.
6. When your API key expires, or to authenticate Qlik DataTransfer against another tenant, click ![Settings](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel.svg) to enter a new API key, then click Confirm.

   ![Image of Qlik DataTransfer API key](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Qlik-DataTransfer-API-key.png)

Once Qlik DataTransfer is authenticated, you can upload your on-premises data to your Qlik Cloud tenant.
For information on how to use the Qlik DataTransfer , see [*Uploading on-premises data with Qlik DataTransfer*](qlik-datatransfer.htm).

Information note If you change the service log on account after configuring Qlik DataTransfer with your tenant, you must reconfigure the tenant and connections to ODBC data sources.

## Upgrading Qlik DataTransfer

Qlik DataTransfer displays a notification banner when new versions are available. Qlik DataTransfer does not automatically upgrade to newer versions.

Warning note

If you chose a different location for storing configuration files or chose different ports to run Qlik DataTransfer from the configuration file Service.conf, the upgrade will override it. Back up your Service.conf file prior to the upgrade and copy it to the default configuration folder after the upgrade is completed to keep your settings.

If the Qlik DataTransfer is using the Local System account, it will not prompt you for service user credentials and continue using Local System.

![Qlik DataTransfer upgrade banner](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Qlik-DataTransfer-upgradeBanner.png)

Do the following:

1. Download the new version of Qlik DataTransfer from the in-application banner or from [Product Downloads](https://community.qlik.com/t5/Downloads/tkb-p/Downloads).
2. Close your current version of Qlik DataTransfer .
3. Run the Qlik DataTransfer installer.

   Information note

   If you are upgrading Qlik DataTransfer on a Windows server with Qlik Sense Enterprise on Windows installed, Qlik DataTransfer must be upgraded with the Qlik Sense services user used in the Qlik Sense installation.
4. Click Upgrade.

   ![Upgrade QlikDataTransfer window](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Qlik-DataTransfer-upgrade.png)

## Uninstalling Qlik DataTransfer

Information noteWhen uninstalling Qlik DataTransfer , the installer removes all the Qlik DataTransfer files and folders. You should save any files or folders you want to keep to a new location.

Do the following:

1. Run the Qlik DataTransfer installer.

   Information note

   If you have a Qlik platform installed on the same server, you must stop the other Qlik services before you can uninstall Qlik DataTransfer .
2. Click Uninstall.
3. Once uninstalled, if applicable, restart the Qlik services in the following order:

   1. Qlik Sense Service Dispatcher
   2. Qlik Logging Service
   3. Qlik Sense Repository Service
   4. Qlik Sense Proxy Service
   5. Qlik Sense Engine Service
   6. Qlik Sense Scheduler Service
   7. Qlik Sense Printing Service

## Decommissioning Qlik DataTransfer

The Qlik Data Gateway - Direct Access allows you to securely access behind-the-firewall data sources, over a strictly outbound, encrypted, and mutually authenticated connection. With the addition of access to on premises data sources via the gateway, Qlik DataTransfer servers are recommended to be decommissioned when possible.

For more information, see [Qlik Data Gateway - Direct Access](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/direct-access-gateway.htm) and [File (via Direct Access gateway)](/en-US/cloud-services/Subsystems/Web_Storage_Provider_Connectors_help/Content/Connectors_StorageProvider/Storage%20provider%20connectors/File-DG-storage-provider-connector.htm).

## Limitations

Qlik DataTransfer has the following limitations:

- When upgrading from October 2020 or later, the location for storing configuration files and the ports used for running Qlik DataTransfer are changed to the default in the configuration file Service.conf. If you did not use the default location for storing configuration files or default ports for running Qlik DataTransfer, you will lose these settings. To keep your settings, backup Service.conf before the upgrade and redo the settings in Service.conf from the backed up file after the upgade is complete.
- If you did not use the default location for storing configuration files in Service.conf, you will need to manually delete the files in the folder you selected.
- If you use proxies, you must add a bypass for Qlik DataTransfer to your firewalls using the Qlik Cloud tenant URL. Without a bypass, Qlik DataTransfer will not be able to connect to Qlik Cloud.
- Qlik DataTransfer should be installed on a dedicated Window Server as stipulated in [*Qlik DataTransfer system requirements*](#Qlik). Do not install it on the actual data source server or on a server that has Qlik Data Gateway - Direct Access installed on it.
