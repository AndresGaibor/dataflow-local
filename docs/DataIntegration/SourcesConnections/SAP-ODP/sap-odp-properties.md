---
title: "SAP ODP"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/SAP-ODP/sap-odp-properties.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SAP sources"]
---

# SAP ODP

Information noteThis connector is supported with a Qlik Talend Cloud Enterprise subscription only.

This topic explains how to set up a SAP ODP source in a data task. Before you start the data task, make sure that you have fulfilled the [*Prerequisites*](sap-odp-prereq.htm) and familiarized yourself with the [*Limitations and considerations*](sap-odp-limitations.htm).

Information note

SAP's current grace period for ODP access ends in December 2026. SAP HANA RFC is an Early Access alternative for table-based capture, but it does not cover every ODP use case and does not support CDS views or extractors. Existing SAP ODP connections and tasks are not converted automatically. To use SAP HANA RFC, create a new connection and reload the task. For details, see [*SAP HANA RFC*](../SAP-HANA-RFC/sap-hana-rfc-source.htm).

When using the SAP ODP connector, there is a fixed delta processing mode, which applies the actual changes that were performed on the source datasets (INSERT, UPDATE, or DELETE) to the corresponding target datasets.

Information note

- Changes operations are determined by the ODP source. Some operations might not be supported on the target.
- We recommend manually setting a Primary Key for ODP sources that are not set up to use the default Primary Key.
- Some UPDATEs are received as INSERTs. Therefore, to prevent conflicts on the target, set the Duplicate key when applying an INSERT Apply Conflicts handling policy to UPDATE the existing target record.

  For more information on this setting, see [*Apply conflicts*](../../Replicating/replicating-settings.htm#Apply2).

## Setting connection properties

This section describes how to set up connection parameters for a specific SAP Application server or for a SAP system using load balancing.

To open the connector, do the following:

1. In Connections, click Create connection.
2. Select the SAP ODP source connector and then provide the following settings:

### Data source

- Data gateway

  Select a Data Movement gateway to use for moving your data.

  For information on Data Movement gateway, see [*Qlik Data Gateway - Data Movement*](../../../Gateways/replication-gateway.htm).
- Connect to: Select one of the following according to your SAP ODP environment:

  - Application server - Then proceed from Connecting to a specific application server below.
  - Load balancing environment - Then proceed from Connecting to a load balancing environment below.

#### Connecting to a specific application server

1. After selecting Application server from the Connect to drop-down list, provide the following information:

   - Server name: The IP address of the Application Server on which the SAP ODP source is located.
   - Instance identifier: The instance number of your SAP ODP source.
   - Client identifier: The System ID of your SAP ODP source.
2. Complete the fields described in Account properties and Source properties below.

#### Connecting to a load balancing environment

1. After selecting Load balancing environment from the Connect to drop-down list, provide the following information:

   - Message server: The host name or IP address of the message server host.
   - Application servers group name: The name of the SAP server group. This is an optional group of application servers in a load balancing connection.
   - SAP system name: The SAP R/3 name.
   - Message server service: the name of the SAP message server service as specified in the following file:

     <system drive>:\WINDOWS\system32\drivers\etc\services

     If you do not specify a value, the Data Provider for SAP uses the following default name:

     sapms<R/3 system name>
   - Client identifier: The System ID of the SAP Application source you want to Move.
2. Complete the fields described in Account properties and Source properties below.

### Account properties

- User Name: Your user name for accessing the SAP ODP source. This should be password of the communication user created earlier in SAP.
- Password: Your password for accessing the SAP ODP source. This should be the user name of the communication user created earlier in SAP.

### Source properties

- ODP context: Choose one of the following:

  - ABAP Core Data Services (CDS) views: The context of the CDS views. This is the default ODP context.
  - SAP NetWeaver Business Warehouse: The context of the BW objects.
  - SAP DataSources/Extractors: The context of the data sources and extractors.
  - SAP HANA Information Views: The context of the HANA views.
  - SAP LT Replication (SLT): Required to work with a SAP Landscape Transformation Replication Server.

    See also: [*Setting up SLT on SAP*](sap-odp-prereq.htm#Setting)
- SLT alias: This field is only visible when the ODP context is set to SAP LT Replication (SLT). Specify the SLT alias as defined in the configuration created in [*Setting up SLT on SAP*](sap-odp-prereq.htm#Setting)
- Subscriber type: Choose one of the following:

  - SAP NetWeaver Business Warehouse: This is the default ODP subscriber type.
  - RODPS\_REPL\_TEST: Used mainly for testing and is not recommended to use for production.
  - Others: This will expose the field Other subscriber type, where you can specify a subscriber type that is not listed.
- Subscriber name: Specify the subscriber name. This will be the name shown in SAP for all subscriptions opened by this endpoint connection.
- Max package size: The size of the data package in bytes. This value can be adjusted according to your network and system capabilities.
.

### Security

In the Security settings, you can configure Secure Network Communication (SNC).

#### Prerequisites for working with SNC

Follow the steps below to install the Secure Network Communication (SNC) client on the Data Movement gateway machine.

What you need

- An exported certificate (.crt) of the SAP server
- SAPCAR.EXE
- SAP user (authorized customer)
- The version of the crypto library which is installed on the corresponding SAP server

Installing the SNC client

1. Create a workspace folder for the SAP SNC files and binaries (hereafter referred to as "your SNC folder"), for example: /opt/snc/
2. Copy the exported server certificate and SAPCAR.EXE to your SNC folder.
3. Go to <https://support.sap.com/en/my-support/software-downloads.html> and search for SAPCRYPTOLIB under Installations & Upgrades. Download the 64-bit .SAR to your SNC folder.
4. Open a command prompt and change the working directory to your SNC folder. Then run the following command to unpack the content of the .SAR to your SNC folder:

   sapcar -xvf LibName.sar

   Example:

   sapcar -xvf SAPCRYPTOLIBP\_8541-20011731\_32.SAR
5. Add system environment variables as follows:
   1. Add a system environment called SECUDIR with the path to your SNC folder as its value.
   2. Add a system environment variable called QLIK\_SNC\_LIB with the path to the sapcrypto.dll file as its value.
   3. Add the newly added environment variables to the "PATH" environment variable.
6. Determine the <PSE\_File\_Name> and choose a <PSE\_PIN> to protect it. You will need to provide this information in the next steps.

   Example:

   pseName: "CN=USR,OU=SAP,O=Qlik,C=IS" password: password123
7. Determine the <SNC\_NAME>. It should look something like this: CN=USR, OU=SAP, O=Qlik, C=IS

   See also [*Determining the server SNC name*](#Getting) below.
8. Make sure you have the required permissions to access and execute the files in the SECUDIR folder, and then run the following command to generate the PSE file:

   sapgenpse get\_pse -p <PSE\_File\_Name>.pse -x <PSE\_PIN> <SNC\_NAME>

   Example:

   sapgenpse get\_pse -p usr.pse -x password123 "CN=USR,OU=SAP,O=Qlik,C=IS"
9. Bind the PSE file with the OS user and create the CRED\_V2 file in the SECUDIR folder by running the following command on the Data Movement gateway machine:

   sapgenpse seclogin -p <PSE\_File\_Name>.pse -x <PSE\_PIN> -O <OS\_USER>

   Example:

   sapgenpse seclogin -p usr.pse -x password123 -O SYSTEM
10. Generate the CRT file by running the following command:

    sapgenpse export\_own\_cert -o <PSE\_File\_Name>.crt -p <PSE\_File\_Name>.pse -x <PSE\_PIN>

    Example:

    sapgenpse export\_own\_cert -o usr.crt -p usr.pse -x password123
11. Import the SAP Application Server Certificate (<SERVER\_CRT>) to the PSE by running the following command:

    sapgenpse maintain\_pk -a <SERVER\_CRT>.crt -p <PSE\_File\_Name>.pse -x <PSE\_PIN>

    Example:

    sapgenpse maintain\_pk -a sapsys.crt -p usr.pse -x password123
12. To verify that the DN of the SAP Server’s PSE was imported into the client, run the following command and then check the "subject" value:

    sapgenpse maintain\_pk -v -l -p <PSE\_File\_Name>.pse

    Example:

    sapgenpse maintain\_pk -v -l -p usr.pse

Importing the client certificate

1. Connect to the SAP Application Server and navigate to the "STRUST" transaction using an authorized user.
2. Double-click the SNC (SAPCryptolib) folder.
3. Click ![Display-chang button](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/change-button-sap.png) to switch to Change view.
4. Click ![Certificate import button](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/import-cert-sap.png) to import the certificate.
5. In the new dialog, enter the path to the .crt file that was created earlier, then click continue.
6. Verify the details of the certificate in the Certificate section.
7. Click Add to Certificate List to add the certificate to the list.
8. Save the changes.

Determining the server SNC name

There are two ways you can determine the server name:

- Method 1: Decrypt the server CRT file using the OpenSSL command. The server name will be part of the subject.
- Method 2: This method requires appropriate permissions. While connected to the system:
  1. Run the RZ10 transaction.
  2. Select the system profile.
  3. Select the Extended Maintenance option and then click Display.
  4. The value of the snc/identity/as parameter should be the SNC name.

Configuring the SNC connector settings

Configure the SNC settings in the SAP ODP connector as follows:

- Activate Secure Network Communication (SNC): Select to turn on SNC.
- SNC name: The SNC partner name.

  Example:

  p:CN=SYS, OU=SAP, O=Qlik, C=IS
- SNC quality of protection - Select one of the following:
  - Authentication only: Select to verify the identity of the SAP ODP machine. This is the minimum protection level offered by SNC.
  - Integrity protection: Select to detect any changes or manipulation of the data, which might have occurred between the Qlik Talend Data Integration machine and the SAP ODP machine.
  - Privacy protection: Select to encrypt the messages being transferred to prevent eavesdropping. Privacy protection also includes integrity protection. This is the maximum level of protection provided by SNC.
  - Maximum security available: The maximum level of data protection supported by the SAP ODP machine.

### Internal properties

Internal properties are for special use cases and are therefore not exposed in the dialog. You should only use them if instructed by Qlik Support.

Use the ![Create new](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) and ![Cancel](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin.svg) buttons to the right of the fields to add or remove properties as needed.

### Name

The display name for the source connection.

## Defining the metadata

After you have configured the connection properties, click OK. The Connection metadata view will open. Define the metadata for the connection as described in [*Connecting to SaaS applications*](../../Landing/connecting-web-applications.htm#Managing). You can edit the metadata later as needed by doing one of the following:

- Select Metadata from the ![Options menu for the data connection](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_catmore_vertical.svg)menu shown for the SAP ODP connection within your project.
- Select Metadata from the ![Options menu for the data connection](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_catmore.svg) menu shown for the SAP ODP connection in Connections view.
