---
title: "Managing the Qlik Data Gateway - Direct Access server"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/direct-access-gateway-managing.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Qlik Data Gateway - Direct Access"]
---

# Managing the Qlik Data Gateway - Direct Access server

This section describes the various connectivity and management options that are available after you have installed Qlik Data Gateway - Direct Access.

## Connecting to Qlik Cloud via a proxy server

If you did not configure proxy connectivity in the initial setup, you can do it later by running the commands described below. You can also run the same commands to edit existing proxy server settings.

### Limitations and considerations

- Only HTTP proxy schemas are supported.
- Proxy servers that are configured to intercept SSL connections (for the purposes of content inspection or other security measures) are not supported.
- In addition to HTTPS, Direct Access gateway also uses WSS (WebSocket Secure) protocol. Therefore, make sure that your firewall and proxy server (if you intend to use one) are set up to allow outbound WSS connections.

### Enabling proxy server connectivity

You can enable or edit proxy server connectivity as follows:

1. Do one of the following, depending on installation workflow:

   - Windows server installation:

     Open a Command Prompt as an administrator and change the working directory to the ConnectorAgent subfolder (C:\Program Files\Qlik\ConnectorAgent\ConnectorAgent with a default installation).
   - Containerized installation:

     Open a console inside the direct-access-agent container.
2. Run the following command:

   - Windows server installation:

     - Syntax: connectoragent qcs set\_config --proxy\_url http://host:port
       --proxy\_username username --proxy\_password password
     - Example: connectoragent qcs set\_config --proxy\_url http://myproxy:1212
       --proxy\_username admin --proxy\_password f56weqs@
   - Containerized installation:

     - Syntax: dotnet ConnectorAgent.dll qcs set\_config --proxy\_url http://host:port
       --proxy\_username username --proxy\_password password
     - Example: dotnet ConnectorAgent.dll qcs set\_config --proxy\_url http://myproxy:1212
       --proxy\_username admin --proxy\_password f56weqs@
3. Do one of the following, depending on installation workflow:

   - Windows server installation:

     Restart the Qlik Data Gateway - Direct Access service as described in [*Managing the Qlik Data Gateway - Direct Access service*](#Managing).
   - Containerized installation:

     Restart the direct-access-agent container.

### Disabling proxy server connectivity

You can turn off proxy server connectivity as follows:

1. Open a Command Prompt as an administrator and change the working directory to the ConnectorAgent subfolder (C:\Program Files\Qlik\ConnectorAgent\ConnectorAgent with a default installation).
2. Do one of the following, depending on installation workflow:

   - Windows server installation:

     Open a Command Prompt as an administrator and change the working directory to the ConnectorAgent subfolder (C:\Program Files\Qlik\ConnectorAgent\ConnectorAgent with a default installation).
   - Containerized installation:

     Open a console inside the direct-access-agent container.
3. Run the following command:

   connectoragent qcs set\_config --proxy\_url ""

   - Windows server installation:

     connectoragent qcs set\_config --proxy\_url ""
   - Containerized installation:

     dotnet ConnectorAgent.dll qcs set\_config --proxy\_url ""
4. Do one of the following, depending on installation workflow:

   - Windows server installation:

     Restart the Qlik Data Gateway - Direct Access service as described in [*Managing the Qlik Data Gateway - Direct Access service*](#Managing).
   - Containerized installation:

     Restart the direct-access-agent container.

## Updating the Qlik Cloud tenant URL

You can change the Qlik Cloud tenant URL as needed.

To do this:

1. On the Direct Access gateway server, open a Command Prompt as an administrator and change the working directory to the ConnectorAgent subfolder (C:\Program Files\Qlik\ConnectorAgent\ConnectorAgent with a default installation).
2. Run one of the following commands depending on your installation workflow:

   - Windows server installation:

     - Syntax: connectoragent qcs set\_config --tenant\_url URL
     - Example: connectoragent qcs set\_config --tenant\_url mytenant.us.qlikcloud.com
   - Containerized installation:

     - Syntax: dotnet ConnectorAgent.dll qcs set\_config --tenant\_url URL
     - Example: dotnet ConnectorAgent.dll qcs set\_config --tenant\_url mytenant.us.qlikcloud.com
3. Restart the Qlik Data Gateway - Direct Access service as described in [*Managing the Qlik Data Gateway - Direct Access service*](#Managing).

Information noteUpdating the Qlik Cloud tenant URL also requires you to generate a new registration key, as described in [*Stage two: Install or deploy Direct Access gateway*](direct-access-gateway-setting-up.htm#Install2) (and register it, as described in [*Stage four: Register the data gateway*](direct-access-gateway-setting-up.htm#Stage4)).

## Viewing the current Direct Access gateway server settings

You can view the current Direct Access gateway server settings.

To do this:

1. Do one of the following depending on your installation workflow:

   - Windows server installation:

     On the Direct Access gateway server, open a Command Prompt as an administrator and change the working directory to the ConnectorAgent subfolder (C:\Program Files\Qlik\ConnectorAgent\ConnectorAgent with a default installation).
   - Containerized installation:

     Open a console inside the direct-access-agent container.
2. Run one of the following commands depending on your installation workflow:

   - Windows server installation:

     connectoragent qcs set\_config --tenant\_url URL
   - Containerized installation:

     dotnet ConnectorAgent.dll qcs set\_config --tenant\_url URL

   Your current settings will be shown.

   Example:

   ```
   connector-agent starting....
   --tenant_url "elastic.example"
   --proxy_url ""
   --proxy_username ""
   DirectAccessAgent Control Program completed successfully.
   ```

## Managing the Qlik Data Gateway - Direct Access service

Information noteApplies to Windows server installations only.

After changing a setting on the Direct Access gateway server, you need to restart the Qlik Data Gateway - Direct Access service. You can also run the service under a different account.

### Starting, stopping, or restarting the service

On the Direct Access gateway server, do one of the following to stop, start, or restart the service:

- Open the Windows Services console and stop, start or restart the Qlik Data Gateway - Direct Access service as required.

- Open a Command Prompt as an administrator and change the working directory to the ConnectorAgent subfolder (C:\Program Files\Qlik\ConnectorAgent\ConnectorAgent with a default installation). Then, run the following commands:

  connectoragent service stop

  A confirmation that the service stopped successfully will be shown.

  connectoragent service start

  A confirmation that the service started successfully will be shown.

### Running the service under a different account

By default, the Qlik Data Gateway - Direct Access service runs under the Local System account. To run the service under a different account, right-click Qlik Data Gateway - Direct Access in the Windows Services console and select the Log On tab. Then select This account and enter the account details. When you're done, save your settings and restart the service.

## Available command categories

To see a list of available command categories:

1. Do one of the following depending on your installation workflow:

   - Windows server installation:

     Open a Command Prompt as an administrator and change the working directory to the ConnectorAgent subfolder (C:\Program Files\Qlik\ConnectorAgent\ConnectorAgent with a default installation.
   - Containerized installation:

     Open a console inside the direct-access-agent container.
2. Run one of the following commands depending on your installation workflow:

   - Windows server installation:

     connectoragent help
   - Containerized installation:

     dotnet ConnectorAgent.dll help

The following list will be displayed:

- service
  - See Managing the Qlik Data Gateway - Direct Access service above.
- qcs
  - Must precede all documented commands, except service commands.

  Example (Windows server installation):

  connectoragent qcs show\_config

  Example (Containerized installation):

  dotnet ConnectorAgent.dll qcs show\_config
- setup
  - For support use only.
- repository
  - For support use only.
- configuration - For support use only.
