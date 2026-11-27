---
title: "Setting up Data Movement gateway"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/dm-gateway-setting-up.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Qlik Data Gateway - Data Movement"]
---

# Setting up Data Movement gateway

Setting up Data Movement gateway involves procedures that need to be performed both in Administration and on the Data Movement gateway server.

Information note

- All CLI commands must be run on the Data Movement gateway server.
- Installation (RPM) and service commands must be run as sudo or as root.
- Data Movement gateway procedures that need to be performed in Administration require tenant admin permission.

  See also: [*Considerations when associating the data gateway with a space*](#Consider)

If you want to use knowledge marts, see [*Setting up Qlik Data Gateway - Data Movement for knowledge marts*](gateways-for-knowledge-mart.htm).

## Stage one: Download the Data Movement gateway

1. To access data gateways, select Administration from the launcher menu (![Launcher menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_grid_menu.svg)), and then Data gateways.

   All existing data gateways will be listed in [a table showing basic information about each gateway](dm-gateway-managing-console.htm#gateprop).
2. Click the Deploy toolbar button.
3. Select Data Gateway - Data Movement, accept the Qlik Customer Agreement, and click Download.

   The Data Movement gateway RPM (qlik-data-gateway-data-movement.rpm) will be downloaded to your machine.

## Stage two: Install and set up Data Movement gateway

This stage involves installing Data Movement gateway, setting the Qlik Cloud URL, and generating a registration key. You will need to copy the key to the Data Movement gateway settings in Administration (in stage three below). The key is used to establish an authenticated connection between Data Movement gateway and the Qlik Cloud tenant.

Warning noteWhen installing Data Movement gateway on a system with SELinux enabled, best practice is to use the default installation path. If you want to use a different path, please contact [Qlik Support](https://community.qlik.com/t5/Support/ct-p/qlikSupport).

1. Once the download is complete, copy the RPM file to the Linux machine where you want to install Data Movement gateway. Make sure the machine is behind your firewall, and can communicate with your data sources and Qlik Cloud.
2. Open a shell prompt and change the working directory to the directory containing the RPM:

   Example:

   /qlik/GatewayRPM/
3. Run the following command to install Data Movement gateway.

   Syntax:

   QLIK\_CUSTOMER\_AGREEMENT\_ACCEPT=yes rpm -ivh gateway-rpm

   Example:

   sudo QLIK\_CUSTOMER\_AGREEMENT\_ACCEPT=yes rpm -ivh qlik-data-gateway-data-movement.rpm

   You can view the Qlik Customer Agreement here: <https://www.qlik.com/us/-/media/files/legal/license-agreements/qlik/qlik-customer-agreement-english.pdf>
4. After the installation completes, change the working directory to:

   /opt/qlik/gateway/movement/bin

   Then, run the following commands:

   ### Setting the Qlik Cloud tenant and a proxy server

   Information note

   If you need to connect to your cloud data warehouse or storage via a proxy, make sure the relevant options are turned on in the landing settings:

   - Use proxy to connect to cloud data warehouse
   - Use proxy to connect to storage

   If neither of these options are turned on, the proxy connection will be to Qlik Cloud only.

   For more information on these options, see [*Landing data from data sources*](../DataIntegration/Landing/Landing-data-data-sources.htm).

   Run the following command to set the Qlik Cloud tenant URL and, optionally, your proxy server URL:

   Command for setting the Qlik Cloud tenant URL without a proxy server:

   Syntax:

   ./agentctl qcs set\_config --tenant\_url URL

   Example:

   ./agentctl qcs set\_config --tenant\_url mytenant.us.qlikcloud.com

   Command for setting the Qlik Cloud tenant URL and the proxy server URL:

   Syntax:

   ./agentctl qcs set\_config --tenant\_url your-qlik-cloud-tenant-url --proxy\_url https|http://host:port
   --proxy\_username username --proxy\_password password

   Example:

   ./agentctl qcs set\_config --tenant\_url mytenant.us.qlikcloud.com --proxy\_url https://myproxy:1212
   --proxy\_username admin --proxy\_password f56weqs@

   See also: [*Managing the Data Movement gateway server*](dm-gateway-managing.htm)

   ### Setting the CA bundle

   The CA bundle authenticates the identity of the Qlik Cloud tenant, thereby ensuring a trusted connection.

   Who needs to set the CA bundle?

   The CA bundle only needs to be set if you are:

   - A Qlik Cloud Government customer
   - A Qlik Cloud commercial customer using a security appliance that acts as a proxy and replaces the certificate information received from the Internet with its own CA root certificates

   Which bundle should I use?

   Customers should either use the Qlik CA bundle or bring their own CA bundle, as follows:

   - Qlik provides the CA bundle: Should be used by Qlik Cloud Government customers with a standard environment. A standard environment is an environment that does not have a security appliance that acts as a proxy and replaces the certificate information received from the Internet with its own CA root certificates.

     Information noteYou can rename the CA bundle file, but make sure that it has a .pem extension (for example, qlikcerts.pem). Then, run the command(s) described below.
   - Customers bring their own CA bundle: Should be used if the customer's environment is using a security appliance that acts as a proxy and replaces the certificate information received from the Internet with its own CA root certificates. If those certificates are self-signed, then in addition to the command for setting the CA bundle, you also need to run the command for allowing the CA bundle. Both of these commands are described below. This applies to both Qlik Cloud Government customers and Qlik Cloud commercial customers alike.

   Command for setting the CA bundle

   Run the following command to set the CA certificate bundle:

   Syntax:

   ./agentctl qcs set\_config --ca\_bundle\_path path-to-ca-bundle-file

   Example:

   ./agentctl qcs set\_config --ca\_bundle\_path /etc/ssl/certs/cacerts.pem

   Command for allowing the CA bundle

   Some environments use a security appliance that acts as a proxy and replaces the certificate information received from the Internet with its own CA root certificates. This command only needs to be run if the security appliance itself uses a self-signed certificate. In such a case, the CA bundle might not be trusted unless you run the following command:

   ./agentctl qcs set\_config --ca\_bundle\_allow\_invalid\_certs true

   Information noteIf you are not sure whether your environment is using such a security appliance, please contact your IT administrator.

   ### Generating and showing the registration key

   The key is used to establish an authenticated connection between the Data Movement gateway and the Qlik Cloud tenant.

   Run the following command to generate and show the key:

   ./agentctl qcs get\_registration

   The key is shown:

   ![Image of Data Movement registration key](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/dm_reg_key.png)
5. Copy the entire key as shown in the example above. You will need to paste it into Administration in the next stage.

## Stage three: Return to Administration and register Data Movement gateway

1. To access data gateways, select Administration from the launcher menu (![Launcher menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_grid_menu.svg)), and then Data gateways.

   All existing data gateways will be listed in [a table showing basic information about each gateway](dm-gateway-managing-console.htm#gateprop).
2. Click Create.

   The Create data gateway dialog opens.

   ![Image of the dialog for creating a data gateway ](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_dm-gate-create.png)
3. Specify a name for Data Movement gateway.
4. Optionally, provide a description for Data Movement gateway.
5. From the Gateway type drop-down list, select Data Movement.
6. From the Associated space drop-down list, select a space. See also [*Considerations when associating the data gateway with a space*](#Consider).
7. Paste the registration key you generated earlier into the Key field.
8. Click Create.

   Data Movement gateway is added enabled to the Data gateways list.

## Stage four: Start the Data Movement gateway service on the Data Movement gateway server

1. Run the following command:

   sudo systemctl start repagent
2. Check that the service has started by running the following command:

   sudo systemctl status repagent

   The status should be as follows:

   Active: active (running) since <timestamp> ago

Warning noteAfter starting the gateway service, you must refresh your browser to see the updated data gateway status (Connected) in Administration.

## Stage five: Use Data Movement gateway data sources in your data projects

1. To access data gateways, select Administration from the launcher menu (![Launcher menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_grid_menu.svg)), and then Data gateways.

   All existing data gateways will be listed in [a table showing basic information about each gateway](dm-gateway-managing-console.htm#gateprop).
2. Refresh your browser to make sure that the Data gateways table is up-to-date.
3. Locate your gateway in the Data gateways table and verify that its State is “Connected”.

Once you have verified in Administration that the Data Movement gateway is "Connected", you can use it to access your data sources and supported targets.

For more information, see [*Setting up connections to data sources*](../DataIntegration/Landing/connecting-data-2.htm) and [*Setting up connections to targets*](../DataIntegration/TargetConnections/data-project-connections.htm#top).

## Working with Data Movement gateway

When working with Qlik Data Gateway - Data Movement, the flow should be as follows:

1. Set up Data Movement gateway on at least one machine (depending on your [use case](replication-gateway.htm#Common)) and configure connectivity to your Qlik Cloud tenant, as described above.
2. Install the driver required for your data source and fulfill any other prerequisites, as described in [*Setting up connections to data sources*](../DataIntegration/Landing/connecting-data-2.htm). The driver might need to be installed on a Data Movement gateway server deployed close to your source, depending on your [use case](replication-gateway.htm#Common).
3. Install the driver required for your target platform and fulfill any other prerequisites, as described in [*Setting up connections to targets*](../DataIntegration/TargetConnections/data-project-connections.htm#top). The driver might also need to be installed on a Data Movement gateway server deployed close to your target, depending on your [use case](replication-gateway.htm#Common).
4. Configure the connector for your data source, as described in [*Setting up connections to data sources*](../DataIntegration/Landing/connecting-data-2.htm).
5. Configure the connector for your target platform, as described in [*Setting up connections to targets*](../DataIntegration/TargetConnections/data-project-connections.htm#top).
6. Create a project and run the required tasks, as described in [*Creating and managing data pipeline projects*](../DataIntegration/Introduction/Data-projects.htm).

## Considerations when associating the data gateway with a space

When associating the Data Movement gateway with a space (see Step 3 above), be aware of the following:

- Data gateways can be created in data spaces only.
- To create a connection in one space that uses a data gateway from another space, you must have the Can consume data role in the data gateway space.
- To create a data gateway, you must be a space owner or have the Can manage role. For user-based subscriptions, you also need a Professional entitlement. For more information, see [*Managing user entitlements*](../Admin/SaaS-user-allocations.htm).
- Data gateways can be associated with a single space only.

Related learning:

- [Qlik Data Gateway - Data Movement overview](/lnk/Introduction_data_gateway_movement)
