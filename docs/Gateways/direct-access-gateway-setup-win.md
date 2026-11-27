---
title: "Setting up Qlik Data Gateway - Direct Access on a Windows server"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/direct-access-gateway-setup-win.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Qlik Data Gateway - Direct Access", "Setting up Qlik Data Gateway - Direct Access"]
---

# Setting up Qlik Data Gateway - Direct Access on a Windows server

Expand/Collapse all

# Setting up Qlik Data Gateway - Direct Access on a Windows server

This topic outlines the how to set up Qlik Data Gateway - Direct Access on a Windows server. It provides prerequisites and installation instructions, and describes the limitations and considerations you should be aware of when working with Qlik Data Gateway - Direct Access on a Windows server.

## Best practices when using Qlik Data Gateway - Direct Access

For a successful experience when using Qlik Data Gateway - Direct Access, it is strongly recommended to adhere to the following best practices:

- Do not use the same Direct Access gateway for development, user acceptance testing, and production, as this will increase the risk of overloading the available resources and impact system stability. From a business perspective, the combination of insufficient resources and decreased stability, might result in delayed updates to production application data.
- For optimal performance, install the Direct Access gateway on a server that is as close as possible to your data source.
- Direct Access gateway should be installed on a dedicated Windows Server as stipulated in the system requirements below. Do not install it on the actual database server or alongside other Qlik products, including but not limited to, Qlik DataTransfer, Qlik Sense Desktop, and Qlik Sense Enterprise.

## System prerequisites

This section describes the software, ports, and hardware requirements for using Qlik Data Gateway - Direct Access on a Windows server.

### Software prerequisites

- The Direct Access gateway should be installed on a Windows Server machine behind your firewall. The server should be able to access your data source.

  Supported Windows Server editions:

  - 2016
  - 2019
  - 2022
  - 2025

    Windows Server 2025 Requires Qlik Data Gateway - Direct Access 1.7.0 or later.
- Three different .NET versions need to be installed. Install the following .NET versions only:

  - .NET 4.8: Required for the installation.
  - .NET 6.0.x Runtime (x64) and ASP.NET Core Runtime 6.0.x (x64) (latest patch)

    News noteFrom Direct Access gateway 1.6.8, .NET 6.0.x is no longer required.
  - .NET 10 Runtime (x64) and ASP.NET Core Runtime 10 (x64) (latest patch)

    The Direct Access gateway setup will prompt you to install .NET 10 if it detects that it is not currently installed.

  Information note
  - Installing .NET runtime versions higher than 10 is not supported.
  - Direct Access gateway 1.6.6 and 1.6.7 requires both versions - 6.0.x and 8.0.x - of the .NET and ASP.NET Core Runtimes.

  For instructions on how to verify the currently installed .NET version, see <https://docs.microsoft.com/en-us/dotnet/framework/migration-guide/how-to-determine-which-versions-are-installed>.
- Microsoft Visual C++ 2015-2022 Redistributable (x64). The Direct Access gateway setup will prompt you to install the redistributable if it detects that it is not currently installed.

#### Additional software prerequisites when using SAP data sources

- Install the SAP NetWeaver RFC SDK on the Qlik Data Gateway - Direct Access machine, as described in [Installing SAP NetWeaver RFC SDK for Qlik Data Gateway - Direct Access](https://help.qlik.com/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Connectors_SAP/Installation/Installing-sap-connectors-for-direct-access-gw.htm).
- Install Microsoft Visual C++ 2013 Redistributable (x64) on the Qlik Data Gateway - Direct Access machine.

### Required ports and protocols

For required ports and protocols, see [*Required ports and protocols*](direct-access-gateway-setting-up.htm#Ports).

### Recommended hardware

- 8 cores
- 32 GB memory
- 100 GB storage

#### Minimum hardware

The minimum hardware is only suitable for specific scenarios using smaller dedicated server deployments (development, test, or production), with continuously low data volumes, and a limited number of concurrent reloads.

- 4 cores
- 8 GB memory
- 100 GB storage

More resources might be required to provide for consistent processing of increasing data volumes and higher counts of concurrent reloads.
The point at which the performance becomes unacceptable depends on the use case and configuration within each unique environment.

### System cryptography

Qlik Cloud Government supports using Qlik Data Gateway - Direct Access only when Windows is configured to run in a FIPS 140-2 approved mode of operation (FIPS mode). To turn on FIPS mode, enable the Windows policy: [System cryptography: Use FIPS compliant algorithms for encryption, hashing, and signing](https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/system-cryptography-use-fips-compliant-algorithms-for-encryption-hashing-and-signing). For more information, see step 3 of the procedure [Using Windows in a FIPS 140-2 approved mode of operation](https://learn.microsoft.com/en-us/windows/security/threat-protection/fips-140-validation#using-windows-in-a-fips-140-2-approved-mode-of-operation).

Information noteNo additional modules need to be installed. Qlik Data Gateway - Direct Access use only the modules already provided by Windows and included in the [list of validated modules](https://learn.microsoft.com/en-us/windows/security/threat-protection/fips-140-validation#microsoft-fips-140-2-validated-cryptographic-modules). Qlik Data Gateway - Direct Access enforce the use of only FIPS-validated cryptographic algorithms through .NET Runtime.

## Installing Qlik Data Gateway - Direct Access

Setting up the Direct Access gateway involves procedures that need to be performed both in the Administration activity center and on the Direct Access gateway server.

Information noteData gateway procedures that need to be performed in the Administration activity center require tenant admin permission.

Qlik Data Gateway - Direct Access setup steps — Installation on a Windows server

![Direct Access Gateway flow diagram - setup steps for setup on a Windows server.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/direct-access-gateway_setup.png "Click to view full size")

### Stage one: Download Qlik Data Gateway - Direct Access

1. In the Administration activity center, select Data gateways.

   Any existing data gateways will be listed in [a table showing basic information about each gateway](direct-access-gateway-managing-console.htm#gateprop).
2. Click the Deploy toolbar button.

   The Deploy Data Gateway dialog opens.
3. Select Data Gateway - Direct Access (Windows), accept the Qlik Customer Agreement, and click Download. The Direct Access gateway setup file (qlik-data-gateway-direct-access.exe) will be downloaded to your machine.

### Stage two: Install Direct Access gateway on a server behind the firewall protecting your data sources

This stage involves installing Direct Access gateway. You can either install Direct Access gateway interactively or silently.

Information noteUninstalling Direct Access gateway does not remove the configuration settings. In other words, if you uninstall one version of Direct Access gateway and then install a different version, the newly installed version will use the same configuration as the uninstalled version.

Information noteOverriding the default Windows service account requires Direct Access gateway 1.7.4 or later.

#### Interactively installing Direct Access gateway

1. When the download is complete, copy the setup file to a Windows Server machine behind the firewall. Make sure the machine can communicate with your data sources.
2. Open the qlik-data-gateway-direct-access.exe file to launch the Setup wizard.

   Information note
   - Direct Access gateway requires Microsoft .NET 10. If setup detects that an earlier version is installed, you will be prompted to install the required version. When the .NET installation completes, you will need to restart the Direct Access gateway machine and then run the Direct Access gateway setup again.
   - Setup will prompt you to install Microsoft Visual C++ 2015-2022 Redistributable (x64) if it detects that it is not currently installed.

   Information note
   - During setup, you can optionally override the following defaults:
     - The installation path (C:\Program Files\Qlik\ConnectorAgent).
     - The Windows service account under which Direct Access gateway will be installed (LocalSystem). The specified Service Account must have both the "Log on as a Service" right and "Write" permission on the Direct Access gateway installation folder.
3. Continue clicking Next until setup is complete.

#### Silently installing, upgrading, and uninstalling Direct Access gateway

Information noteSupported from Direct Access gateway 1.6.4.

Installing Direct Access gateway silently is useful, for example, if you need to install Direct Access gateway on several machines throughout your organization. If required, you can also override the default Windows service account (LocalSystem).

Prerequisites

Make sure to install the correct versions of all the [prerequisite software](#Software) before
beginning the silent installation as, unlike the interactive installation, this cannot be done during the installation.

Installing or upgrading Direct Access gateway

Open a CMD prompt as administrator and run the following command from the folder containing the Direct Access gateway executable:

qlik-data-gateway-direct-access.exe /S InstallPath="full-path" AcceptEula=yes

Where full-path should be replaced with the actual installation path in quotation marks, for example, "C:\TMP\Qlik".

Information noteSetting the AcceptEula parameter to "yes" is required. By setting the AcceptEula parameter to "yes", you agree to the terms of the [Qlik Customer Agreement](https://www.qlik.com/us/legal/legal-agreements).

Overriding the default Windows service account

By default, Direct Access gateway is installed under the LocalSystem Windows service account.

To install Direct Access gateway under a different account, include the following parameters in your command:

- ServiceAccount: The service account name.

  Information noteThe specified Service Account must have both the "Log on as a Service" right and "Write" permission on the Direct Access gateway installation folder.
- ServicePassword: The password for the specified service account.

Sample command with parameters for overriding the Windows service account

qlik-data-gateway-direct-access.exe /S InstallPath="C:\TMP\Qlik" AcceptEula=yes
ServiceAccount="qliktech.com\user" ServicePassword=kZmbkb8m8BGGz91

Uninstalling Direct Access gateway

Open a CMD prompt as administrator and run the following command from the folder containing the Direct Access gateway executable:

qlik-data-gateway-direct-access.exe /S /uninstall

#### Troubleshooting the installation

The installation log files can be useful for troubleshooting issues with the installation or upgrade:

From Direct Access gateway 1.7.7, the full path to the log files is:

<Direct Access gateway installation folder>\data\logs\Qlik Data Gateway - Direct Access\_<Timestamp>.log

If your Direct Access gateway version is earlier than 1.7.7, the full path to the log files is:

C:\Users\<user>\AppData\Local\Temp\Qlik Data Gateway - Direct Access\_<Timestamp>.log

### Stage three: Setting up Direct Access gateway

For detailed setup instructions, see [*Stage three: Set up Direct Access gateway*](direct-access-gateway-setting-up.htm#Stage3).

### Stage four: Register the data gateway

The next step is to register the data gateway. This can be done either through the Administration activity center or on the command line.

Option 1: Via the Administration activity center

You can register the gateway using the Administration activity center. See [*Option 1: Via the Administration activity center*](direct-access-gateway-setting-up.htm#StageConsole).

Option 2: Automatic registration using the command line

You can also register Direct Access gateway automatically from the command line, without using the Administration activity center. This method uses a short-lived session token generated from an OAuth client.

Information note

To automatically register and remove automatically registered gateways, you need the following permissions:

- Automatic registration: You need the Register Direct Access gateway admin permission set to Allowed.
- Removing automatically registered gateways: You need the Register Direct Access gateway admin permission set to Allowed.

For more information about permissions, see [*Default permissions and custom roles*](../Admin/permissions-scopes-capacity-model.htm).

Information noteAutomatic registration is supported through the command line only. A REST API for automatic gateway registration is not currently available.

Prerequisites

An API key with tenant admin permission to create and manage OAuth clients.

Registering the gateway with automatic registration

1. Generate a JSON Web Key (JWK) on the Direct Access gateway machine. This command creates private keys on the Direct Access gateway machine:

   ConnectorAgent.exe qcs generate\_jwk
2. Copy the JWK returned by the command.
3. Using the API key, create an OAuth client for the gateway through the tenant admin API, providing the JWK you copied in the previous step.

   curl "https://<tenant-url>/api/v1/oauth-clients" -X POST -H 'accept: application/json' -H 'content-type: application/json' -H 'authorization: Bearer <api-key>' -d '{"appType":"web","clientName":"<client-name>","description":"","allowedScopes":["admin.direct-access-gateways:register\_gateway","admin.direct-access-gateways:delete\_gateway"],"allowedAuthMethods":["private\_key\_jwt"],"publicKeys":[<jwk>],"allowedGrantTypes":["client\_credentials"]}'
4. Copy the client\_id value returned in the response.
5. Set the OAuth client's consent method to trusted.

   curl "https://<tenant-url>/api/v1/oauth-clients/<client-id>/connection-configs/me" -X PATCH -H 'accept: application/json' -H 'content-type: application/json' -H 'authorization: Bearer <api-key>' -d '[{"op":"replace","path":"/consentMethod","value":"trusted"}]'
6. Create a registration assertion on the Direct Access gateway machine:

   ConnectorAgent.exe qcs generate\_registration\_assertion --tenant\_url <tenant-url> --client-id <client-id>
7. Request an access token. This also triggers automatic creation of the bot user account used by the gateway.

   curl "https://<tenant-url>/oauth/token" -X POST -H 'content-type: application/x-www-form-urlencoded' -d "grant\_type=client\_credentials" -d "client\_id=<client-id>" -d "client\_assertion\_type=urn:ietf:params:oauth:client-assertion-type:jwt-bearer" -d "client\_assertion=<assertion>" -d "scope=admin.direct-access-gateways:register\_gateway admin.direct-access-gateways:delete\_gateway"
8. Look up the auto-created bot user.

   curl "https://<tenant-url>/api/v1/users" -H 'accept: application/json' -H 'authorization: Bearer <API-key>'
9. Copy the ID of my-bot-client.
10. Create a "DAG Registration" role.

    curl "https://<tenant-url>/api/v1/roles" -X POST -H 'accept: application/json' -H 'content-type: application/json' -H  'authorization: Bearer API-key' -d '{"name":"DAG Registration","description":"Role for registering a gateway","assignedScopes":["admin.direct-access-gateways:register\_gateway", "admin.direct-access-gateways:delete\_gateway"]}'
11. Assign tenant-level roles to the bot user.

    curl "https://<tenant-url>/api/v1/users/<bot-user-ID>" -X PATCH  -H 'accept: application/json' -H 'content-type: application/json' -H  'authorization: Bearer <API-key>' -d ' [ { "op": "replace", "path": "/assignedRoles", "value": [ { "name": "DAG Registration" } ] } ]'
12. Get the Direct Access Gateway space.

    curl "https://<tenant-url>/api/v1/spaces" -H  'authorization: Bearer <API-key>'
13. Copy the Direct Access Gateway space ID.
14. Add the bot user to the space with Can edit permission.

    curl "https://<tenant-url>/api/v1/spaces/<DAG-space-ID>/assignments" -X POST -H 'accept: application/json' -H 'content-type: application/json' -H  'authorization: Bearer <API-key>' -d '{"assigneeId": "<Bot-user-ID>","roles": ["consumer","dataconsumer","producer"], "type": "user"}'
15. In case the existing assertion has expired, generate a new one.

    ConnectorAgent.exe qcs generate\_registration\_assertion --tenant\_url <tenant-url> --client-id <client-ID>

    Follow the needed steps in the command prompt. Since the OAuth client is already created, there is a need to update JWK using this API call:

    curl "https://<tenant-url>/api/v1/oauth-clients/<client-ID>" -X PATCH -H 'accept: application/json' -H 'content-type: application/json' -H 'authorization: Bearer <API-key>' -d '[{"op":"replace","path":"/publicKeys/0/y","value":"<Y-value-from-JWK>"},{"op":"replace","path":"/publicKeys/0/x","value":"<X-value-from-JWK>"},{"op":"remove","path":"/publicKeys/0/use"},{"op":"replace","path":"/publicKeys/0/kid","value":"<kid-value-from-JWK>"}]'
16. Register the gateway:

    ConnectorAgent.exe qcs register\_gateway --tenant\_url <tenant-url> --gateway\_name <gateway-name> --gateway\_description <gateway-description> --space\_name <space-name> --client-id <client-ID> --assertion <assertion>

Removing an automatically registered gateway

Use the following steps to unregister a gateway that was registered using the automatic, session token-based method described above. These steps also remove the OAuth client, bot user, and role that were created for it.

1. Generate an assertion, as described in [step six of Automatic gateway registration using a session token](#AutoRegister). In case the existing assertion has expired, generate a new one using this command:

   ConnectorAgent.exe qcs generate\_registration\_assertion --tenant\_url <tenant-url> --client-id <client-ID>

   Follow the needed steps in the command prompt. Since the OAuth client is already created, there is a need to update JWK using this API call:

   curl "https://<tenant-url>/api/v1/oauth-clients/<client-ID>" -X PATCH -H 'accept: application/json' -H 'content-type: application/json' -H 'authorization: Bearer <API-key>' -d '[{"op":"replace","path":"/publicKeys/0/y","value":"<Y-value-from-JWK>"},{"op":"replace","path":"/publicKeys/0/x","value":"<X-value-from-JWK>"},{"op":"remove","path":"/publicKeys/0/use"},{"op":"replace","path":"/publicKeys/0/kid","value":"<kid-value-from-JWK>"}]'
2. Delete the gateway:

   ConnectorAgent.exe qcs delete\_gateway --tenant\_url <tenant-url> --gateway\_name <gateway-name> --client-id <client-ID> --assertion <assertion>
3. Delete the JWK.

   ConnectorAgent.exe qcs delete\_jwk
4. Look up the bot user account that was created for the gateway.

   curl "https://<tenant-url>/api/v1/users" -H 'accept: application/json' -H 'authorization: Bearer <api-key>'
5. Copy the bot ID.
6. Delete this bot user account.

   curl -X DELETE "https://<tenant-url>/api/v1/users/<bot-user-ID>" -H "Authorization: Bearer <api-key>"
7. Look up the “DAG Registration” role that was created for the gateway.

   curl "https://<tenant-url>/api/v1/roles?limit=1&filter=(name eq \"DAG Registration\")" -H "Authorization: Bearer <api-key>"
8. Copy the role ID.
9. Delete this role.

   curl -X DELETE "https://<tenant-url>/api/v1/roles/<role-ID>" -H "Authorization: Bearer <api-key>"
10. Delete the OAuth client.

    curl -X DELETE "https://<tenant-url>/api/v1/oauth-clients/<client-ID>" -H "qlik-confirm-delete: <client-ID>" -H "Authorization: Bearer <api-key>"

### Stage five: Start the Qlik Data Gateway - Direct Access service on the Direct Access gateway server

On the Direct Access gateway server, do one of the following to start the service:

- Open the Windows Services console and start the Qlik Data Gateway - Direct Access service.
- Open a Command Prompt as an administrator and change the working directory to the ConnectorAgent subfolder (C:\Program Files\Qlik\ConnectorAgent\ConnectorAgent with a default installation). Then, run the following command:

  connectoragent service start

  A confirmation that the service started successfully will be shown.

See also: [*Running the service under a different account*](direct-access-gateway-managing.htm#Running)

### Stage six: Add a connection to your data source

See [*Stage six: Add a connection to your data source*](#Stage6).

## Supported data sources

The following ODBC connectors are supported for Windows server installations:

- ODBC sources. For more information, see [ODBC databases ‒ Qlik Cloud](https://help.qlik.com/en-US/cloud-services/Subsystems/ODBC_Connector_help/Content/Connectors_ODBC/Introduction/ODBC-connector.htm).
- REST sources. For more information, see [REST sources ‒ Qlik Cloud](https://help.qlik.com/en-US/cloud-services/Subsystems/REST_Connector_help/Content/Connectors_REST/REST-connector.htm).
- SAP BW, SAP SQL, and SAP ODP sources. Requires Direct Access gateway 1.2.0 or later.

  For information on setting up connectivity to these sources, see [SAP NetWeaver](https://help.qlik.com/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Connectors_SAP/SAP-SQL-connector.htm).

## Learn more

- [*Setting up Qlik Data Gateway - Direct Access*](direct-access-gateway-setting-up.htm)
- [*Setting up Qlik Data Gateway - Direct Access in a container*](direct-access-gateway-setup-container.htm)
