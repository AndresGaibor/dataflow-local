---
title: "Managing the Data Movement gateway server"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/dm-gateway-managing.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Qlik Data Gateway - Data Movement"]
---

# Managing the Data Movement gateway server

This topic describes the various connectivity and management options that are available after you have installed Data Movement gateway.

## Updating the Qlik Cloud tenant URL

You can change the Qlik Cloud tenant URL as needed.

To do this:

1. Run the following command to stop the Data Movement gateway service:

   sudo systemctl stop repagent
2. Check that the service has stopped by running the following command:

   sudo systemctl status repagent

   The status should be as follows:

   Active: inactive (dead) since <timestamp> ago
3. Change the working directory to:

   /opt/qlik/gateway/movement/bin

   Then run the following command to set the Qlik Cloud tenant URL:

   Syntax:

   ./agentctl qcs set\_config --tenant\_url URL

   Example:

   ./agentctl qcs set\_config --tenant\_url mytenant.us.qlikcloud.com
4. Run the following command to start the Data Movement gateway service:

   sudo systemctl start repagent
5. Check that the service has started by running the following command:

   sudo systemctl status repagent

   The status should be as follows:

   Active: active (running) since <timestamp> ago

Information noteUpdating the Qlik Cloud tenant URL also requires you to generate a new registration key and register it in Administration > Data gateways. For details, see [*Stage two: Install and set up Data Gateway - Data Movement on a server behind the firewall protecting your data sources*](dm-gateway-setting-up.htm#Stage4), and [*Stage three: Return to Administration and register Data Gateway - Data Movement*](dm-gateway-setting-up.htm#Stage2)).

## Connecting to cloud data warehouses via a proxy server

You can configure the Data Movement gateway to connect to your cloud data warehouses via a proxy server. You can also disable proxy server connectivity should it no longer be required.

Information noteThis proxy is only used for the connection between Data Movement gateway server and your cloud data warehouses.

### Enabling or editing proxy server connectivity

You can enable or edit proxy server connectivity as follows:

1. On the Data Movement gateway server, open a shell prompt and change the working directory to:

   /opt/qlik/gateway/movement/bin
2. Run the following command to stop the Data Movement gateway service:

   sudo systemctl stop repagent
3. Check that the service has stopped by running the following command:

   sudo systemctl status repagent

   The status should be as follows:

   Active: inactive (dead) since <timestamp> ago
4. Run the following command to set the proxy:

   Syntax:

   ./agentctl qcs set\_config --proxy\_url https|http://host:port
   --proxy\_username username --proxy\_password password

   Example:

   ./agentctl qcs set\_config --proxy\_url https://myproxy:1212
   --proxy\_username admin --proxy\_password f56weqs@
5. Run the following command to start the Data Movement gateway service:

   sudo systemctl start repagent
6. Check that the service has started by running the following command:

   sudo systemctl status repagent

   The status should be as follows:

   Active: active (running) since <timestamp> ago

### Disabling proxy server connectivity

You can turn off proxy server connectivity as follows:

1. On the Data Movement gateway server, open a shell prompt and change the working directory to:

   /opt/qlik/gateway/movement/bin
2. Run the following command to stop the Data Movement gateway service:

   sudo systemctl stop repagent
3. Check that the service has stopped by running the following command:

   sudo systemctl status repagent

   The status should be as follows:

   Active: inactive (dead) since <timestamp> ago
4. Run the following command:

   ./agentctl qcs set\_config --proxy\_url ""
5. Run the following command to start the Data Movement gateway service:

   sudo systemctl start repagent
6. Check that the service has started by running the following command:

   sudo systemctl status repagent

   The status should be as follows:

   Active: active (running) since <timestamp> ago

## Viewing the current settings

You can view the current Data Movement gateway settings (for example, Qlik Cloud tenant URL, proxy URL, and so on).

To do this:

1. Open a shell prompt and change the working directory to:

   /opt/qlik/gateway/movement/bin
2. Run the following command:

   ./agentctl qcs show\_config

   Your current settings will be shown.

   Example:

   ```
   [qlik@gatewayhost bin]# ./agentctl qcs show_config
   --tenant_url “tenant.qlik.com”
   --proxy_url “”
   --proxy_username “”
   --connection_mode “DATA_GATEWAY”
   --listening_address “localhost”
   --listening_port “443"
   ReplicateAgent Control Program completed successfully.
   ```

## Data Movement gateway service commands

Before changing a setting on the Data Movement gateway server, you need to stop the Data Movement gateway service, and then start it once the setting has been changed.

### Stopping the service

1. Run the following command to stop the Data Movement gateway service:

   sudo systemctl stop repagent
2. Check that the service has stopped by running the following command:

   sudo systemctl status repagent

   The status should be as follows:

   Active: inactive (dead) since <timestamp> ago

### Starting the service

1. Run the following command:

   sudo systemctl start repagent
2. Check that the service has started by running the following command:

   sudo systemctl status repagent

   The status should be as follows:

   Active: active (running) since <timestamp> ago

### Restarting the service

1. Run the following command:

   sudo systemctl restart repagent
2. Check that the service has started by running the following command:

   sudo systemctl status repagent

   The status should be as follows:

   Active: active (running) since <timestamp> ago

Warning noteAfter starting the gateway service, you must refresh your browser to see the updated data gateway status (Connected) in Administration > Data gateways.
