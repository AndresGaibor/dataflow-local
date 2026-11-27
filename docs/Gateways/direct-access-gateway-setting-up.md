---
title: "Setting up Qlik Data Gateway - Direct Access"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/direct-access-gateway-setting-up.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Qlik Data Gateway - Direct Access"]
---

# Setting up Qlik Data Gateway - Direct Access

You can set up Qlik Data Gateway - Direct Access either on a Windows server or in a containerized environment. For successful setup, ensure you are familiar with the prerequisites, installation instructions, limitations, and considerations for your specific setup workflow.

Information note

For the AWS PrivateLink pattern for Qlik Data Gateway - Direct Access, see [*Configuring AWS PrivateLink for Qlik Data Gateway - Direct Access*](direct-access-gateway-aws-privatelink.htm). The pattern does not replace the standard prerequisites and network requirements in this topic.

## Setup workflows

Choose one of the following workflows:

- [Setting up Qlik Data Gateway - Direct Access on a Windows server](direct-access-gateway-setup-win.htm)
- [Setting up Qlik Data Gateway - Direct Access in a container](direct-access-gateway-setup-container.htm)

## System prerequisites

### Software requirements

Refer to one of the following depending on your setup method:

- Windows server: [*Software prerequisites*](direct-access-gateway-setup-win.htm#Software)
- Containerized: [*Software requirements*](direct-access-gateway-setup-container.htm#SoftwareReq)

### Common requirements

These requirements are applicable to both Windows server and containerized installations.

#### Required ports and protocols

The following section lists the required ports.

#### Outbound ports

HTTPS/TCP-443 should be opened for outbound communication to <tenant-id>.<region>.qlikcloud.com.

#### Internal ports

Below is a list of ports used for communication by internal data gateway processes. If any of these ports is being used by another application, reconfigure the other application or uninstall it.

General ports

- 5050 (Connector Agent REST API)
- 9027 (DCAAS REST API)

ODBC ports

- 3005 (ODBC Connector REST API)
- 50260 (ODBC Connector gRPC)

SAP ports

- 3015 (SAP BW Connector REST API)
- 50270 (SAP BW Connector gRPC)
- 3025 (SAP SQL Connector REST API)
- 50280 (SAP SQL Connector gRPC)
- 3035 (SAP ODP Connector REST API)
- 50290 (SAP ODP Connector gRPC)
- 3035 (SAP Package Connector REST API)
- 50290 (SAP Package Connector gRPC)

REST ports

- 3055 (REST Connector REST API)
- 50310 (REST Connector gRPC)

File ports

- 3045 (File Connector REST API)
- 50300 (File Connector gRPC)

#### WSS protocol

In addition to HTTPS, Direct Access gateway also uses WSS (WebSocket Secure) protocol. Therefore, make sure that your firewall and proxy server (if you intend to use one) are set up to allow outbound WSS connections.

### Recommended hardware

Refer to one of the following depending on your setup method:

- Windows server: [*Recommended hardware*](direct-access-gateway-setup-win.htm#RecHardware)
- Containerized: [*Recommended hardware*](direct-access-gateway-setup-container.htm#RecHardware)

### System crytography (Windows server installation only)

See [*System cryptography*](direct-access-gateway-setup-win.htm#System).

## Installing Qlik Data Gateway - Direct Access

### Stage one: Download Qlik Data Gateway - Direct Access

Refer to one of the following depending on your setup method:

- Windows server: [*Stage one: Download Qlik Data Gateway - Direct Access*](direct-access-gateway-setup-win.htm#Stage5)
- Containerized: [*Stage one: Download Qlik Data Gateway - Direct Access*](direct-access-gateway-setup-container.htm#Stage1)

### Stage two: Install or deploy Direct Access gateway

Refer to one of the following depending on your setup method:

- Windows server: [*Stage two: Install Direct Access gateway on a server behind the firewall protecting your data sources*](direct-access-gateway-setup-win.htm#Stage4)
- Containerized: [*Stage two: Start the deployment by running the Docker Compose file*](direct-access-gateway-setup-container.htm#Stage2)

### Stage three: Set up Direct Access gateway

This stage includes setting your Qlik Cloud tenant URL, optionally setting a proxy server, and generating a registration key. You will need to copy the key to the data gateway settings in the Administration activity center (in stage three below). The key is used to establish an authenticated connection between the Direct Access gateway and the Qlik Cloud tenant.

Information note

Connecting to a Qlik Anonymous tenant (Sweden region) is not supported.

Starting from Direct Access gateway 1.7.16, Canada region is now supported. Select the Canada region during deployment in the Administration activity center when deploying the gateway setup file.

On the Direct Access gateway machine, do one of the following depending on your installation workflow:

- Windows server: Open a Command Prompt as an administrator and change the working directory to the ConnectorAgent subfolder (C:\Program Files\Qlik\ConnectorAgent\ConnectorAgent with a default installation).
- Containerized: Open a console inside the direct-access-agent container.

Then, continue as described below.

#### Setting the Qlik Cloud tenant

Set which Qlik Cloud tenant to connect to. To connect to the tenant via a proxy server, add the relevant parameters to the command as shown below.

Commands for setting the Qlik Cloud tenant without a proxy server:

- Windows server installation

  - Syntax: connectoragent qcs set\_config --tenant\_url your-qlik-cloud-tenant-url
  - Example: connectoragent qcs set\_config --tenant\_url mytenant.us.qlikcloud.com
- Containerized installation

  - Syntax: dotnet ConnectorAgent.dll qcs set\_config --tenant\_url your-qlik-cloud-tenant-url
  - Example: dotnet ConnectorAgent.dll qcs set\_config --tenant\_url mytenant.us.qlikcloud.com

Commands for setting the Qlik Cloud tenant with a proxy server:

- Windows server installation

  - Syntax: connectoragent qcs set\_config --tenant\_url your-qlik-cloud-tenant-url --proxy\_url http://host:port
    --proxy\_username username --proxy\_password password
  - Example: connectoragent qcs set\_config --tenant\_url mytenant.us.qlikcloud.com --proxy\_url http://myproxy:1212
    --proxy\_username admin --proxy\_password f56weqs@
- Containerized installation

  - Syntax: dotnet ConnectorAgent.dll qcs set\_config --tenant\_url your-qlik-cloud-tenant-url --proxy\_url http://host:port
    --proxy\_username username --proxy\_password password
  - Example: dotnet ConnectorAgent.dll qcs set\_config --tenant\_url mytenant.us.qlikcloud.com --proxy\_url http://myproxy:1212
    --proxy\_username admin --proxy\_password f56weqs@

For information on proxy limitations, see [*Connecting to Qlik Cloud via a proxy server*](direct-access-gateway-managing.htm#Connecti).

#### Setting the CA bundle

The CA bundle authenticates the identity of the Qlik Cloud tenant, thereby ensuring a trusted connection.

Who needs to set the CA bundle?

The CA bundle only needs to be set if you are:

- A Qlik Cloud Government customer
- A Qlik Cloud commercial customer using a security appliance that acts as a proxy and replaces the certificate information received from the Internet with its own CA root certificates

Which bundle should I use?

Customers should either use the Qlik CA bundle or bring their own CA bundle, as follows:

- Qlik provides the CA bundle: Should be used by Qlik Cloud Government customers with a standard environment. A standard environment is an environment that does not have a security appliance that acts as a proxy and replaces the certificate information received from the Internet with its own CA root certificates.

  In a default Direct Access gateway installation, the CA bundle file can be found in the following location:

  - Windows server installation: C:\Program Files\Qlik\ConnectorAgent\caBundle\qcg\_ca\_bundle.pem
  - Containerized installation: /usr/share/Qlik/Gateway/ssl/qcg\_ca\_bundle.pem

  Information noteYou can rename the CA bundle file, but make sure that it has a .pem extension (for example, qlikcerts.pem). Then, run the command(s) described below.
- Customers bring their own CA bundle: Should be used if the customer's environment is using a security appliance that acts as a proxy and replaces the certificate information received from the Internet with its own CA root certificates. If those certificates are self-signed, then in addition to the command for setting the CA bundle, you also need to run the command for allowing the CA bundle. Both of these commands are described below. This applies to both Qlik Cloud Government customers and Qlik Cloud commercial customers alike.

Command for setting the CA bundle

Run the following command to set the CA certificate bundle:

Syntax (Windows server installation):

connectoragent qcs set\_config --ca\_bundle\_path path-to-ca-bundle-file

Syntax (containerized installation):

dotnet ConnectorAgent.dll qcs set\_config --ca\_bundle\_path path-to-ca-bundle-file

Example (Windows server installation):

connectoragent qcs qcs set\_config --ca\_bundle\_path c:\ca\cacerts.pem

Example (containerized installation):

dotnet ConnectorAgent.dll qcs set\_config --ca\_bundle\_path c:\ca\cacerts.pem

Command for allowing the CA bundle

Some environments use a security appliance that acts as a proxy and replaces the certificate information received from the Internet with its own CA root certificates. This command only needs to be run if the security appliance itself uses a self-signed certificate. In such a case, the CA bundle might not be trusted unless you run the following command:

- Windows server installation:

  connectoragent qcs set\_config --ca\_bundle\_allow\_invalid\_certs true
- Containerized installation:

  dotnet ConnectorAgent.dll qcs set\_config --ca\_bundle\_allow\_invalid\_certs true

Information noteIf you are not sure whether your environment is using such a security appliance, please contact your IT administrator.

#### Generating and showing the registration key

The key is used to establish an authenticated connection between the Direct Access gateway and the Qlik Cloud tenant.

Commands for generating the registration key

- Windows server installation:

  connectoragent qcs generate\_keys
- Containerized installation:

  dotnet ConnectorAgent.dll qcs generate\_keys

Commands for showing the registration key

dotnet ConnectorAgent.dll qcs get\_registration

- Windows server installation:

  connectoragent qcs get\_registration
- Containerized installation:

  dotnet ConnectorAgent.dll qcs get\_registration

The key is shown.

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/da_reg_key.png)

Copy the entire key as shown in the example above. You will need to paste it into the Administration activity center in the next stage.

### Stage four: Register the data gateway

The next step is to register the data gateway. This can be done either through the Administration activity center or on the command line.

Option 1: Via the Administration activity center

Warning noteRegistering a Direct Access gateway automatically creates an Identify provider (Multi-cloud) entry in the Administration activity center, for secure gateway-to-tenant communication. The Identity provider description includes the gateway ID (issuer gateway\_id), which allows you easily locate the associated gateway in the Data gateways section (of the Administration activity center). Deleting the gateway Identity provider will disconnect the gateway so you should only do this if you are absolutely sure the gateway is no longer required. If you accidentally deleted the Identity provider, restarting the Direct Access gateway will restore the entry and reconnect the gateway.

1. In the Administration activity center, select Data gateways.

   Any existing data gateways will be listed in [a table showing basic information about each gateway](direct-access-gateway-managing-console.htm#gateprop).
2. Click the Create toolbar button.

   The Create data gateway dialog opens.

   ![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_da-gate-create.png)
3. Specify a name for the data gateway.
4. Optionally, provide a description for the data gateway.
5. Optionally, in the Pool field, select an existing gateway pool name or type a new one to create a pool that includes this gateway.

   For more information about load balancing with gateway pools, see [*Configuring load balancing with gateway pools*](direct-access-gateway-managing-console.htm#Pools).
6. From the data gateway type drop-down list, select Direct Access.
7. From the Associated space drop-down list, select a space.

   When associating the Direct Access gateway with a space, you should be aware of the following:

   - Data gateways can be created in shared or managed spaces only
   - To create a data connection in one space that uses a data gateway from another space, you must have the Can consume data role in the data gateway space.
   - To create a data gateway, you must be a space owner or have the Can manage role. For user-based subscriptions, you also need a Professional entitlement. For more information, see [*Managing user entitlements*](../Admin/SaaS-user-allocations.htm).
   - Data gateways can be associated with a single space only.
8. Paste the registration key you generated earlier into the Key field.
9. Click Create.

   The data gateway is added enabled to the Data gateways list.

Option 2: Automatic registration using the command line

You can also register Direct Access gateway automatically from the command line, without using the Administration activity center.

Information note

To automatically register and remove automatically registered gateways, you need the following permissions:

- Automatic registration: You need the Register Direct Access gateway admin permission set to Allowed.
- Removing automatically registered gateways: You need the Register Direct Access gateway admin permission set to Allowed.

For more information about permissions, see [*Default permissions and custom roles*](../Admin/permissions-scopes-capacity-model.htm).

For instructions, see one of the following depending on your installation workflow:

- Windows server installation: [*Option 2: Automatic registration using the command line*](direct-access-gateway-setup-win.htm#StageAuto)
- Containerized installation: [*Option 2: Automatic registration using the command line*](direct-access-gateway-setup-container.htm#StageAuto)

### Stage five: Start the Qlik Data Gateway - Direct Access service on the Direct Access gateway server

Next, you need to start the Qlik Data Gateway - Direct Access service.

Refer to one of the following depending on your setup method:

- Windows server installation: [*Stage five: Start the Qlik Data Gateway - Direct Access service on the Direct Access gateway server*](direct-access-gateway-setup-win.htm#Stage3)
- Containerized installation: [*Stage five: Start the Qlik Data Gateway - Direct Access service on the Direct Access gateway server*](direct-access-gateway-setup-container.htm#Stage5)

### Stage six: Add a connection to your data source

Locate your gateway in the Data gateways list and verify that its State is “Connected” (you might need to refresh your browser to see the current status). You can then proceed to add a connection to your data source.

There are several ways you can load data from data sources:

- [Adding and managing data sources from spaces](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/managing-data-resources-spaces.htm)
- [Loading and managing data with Data Manager](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/managing-data.htm)
- [Loading and transforming data with scripting](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/introduction-data-modeling.htm)

The list of available data sources will contain duplicate entries for those data sources that support gateway connectivity. Gateway-compliant data sources can be identified by the words "via Direct Access gateway”, which appear in parenthesis after the source type.

Gateway-compliant source connection example

![Gateway-compliant source connection example](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/da-source-example.png "Click to view full size")

Information noteThe Add data connection dialog for Gateway-compliant data sources has an extra Direct Access gateway field that allows you to select which gateway to use.

## General limitations and considerations

- Direct Access gateway can connect to a single tenant only.
- If, for any reason, the Direct Access gateway server is rebooted during a Qlik application reload, the reload will fail. Restart the Qlik application reload to refresh the data.
- Reload script queries cannot exceed 500,000 characters.

  For information on reloading scripts, see [*Running scripts*](../ScriptEditor/reloading-scripts.htm).
