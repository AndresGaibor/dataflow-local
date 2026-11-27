---
title: "SAP Extractor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/SAP-Extractor/SAP-Extractor-source.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SAP sources"]
---

# SAP Extractor

This section explains how to set up a SAP Extractor source in a data task. Before you start the data task, make sure that you have fulfilled the [*Prerequisites*](../../../../Global_Common/Content/SharedReplicateHDD/SAP-Extractor/extractor_Prerequisites.htm) and familiarized yourself with the [*Limitations and considerations*](../../../../Global_Common/Content/SharedReplicateHDD/SAP-Extractor/extractor_Limitations_SAP_app.htm).

Information noteThis connector is supported with a Qlik Talend Cloud Enterprise subscription only.

## Setting connection properties

This section describes the available connection properties. All properties are required unless otherwise indicated.

To open the connector, do the following:

1. In Connections, click Create connection.
2. Select the SAP Extractor source connector and then provide the following settings:

### Connecting to a specific SAP Application server

#### Data source

- Data gateway

  Select a Data Movement gateway to use for moving your data.

  For information on Data Movement gateway, see [*Qlik Data Gateway - Data Movement*](../../../Gateways/replication-gateway.htm).
- Connect to: Select Application server.
- Server: The IP address of the Application Server on which the SAP Extractor source is located.
- Instance number: The instance number of the SAP Extractor data source.
- Client identifier: The System ID of the SAP Extractor data source.

#### Account properties

- User Name: The user name for accessing the SAP Extractor data source. This is the user name for the communication user created earlier in SAP.
- Password: The password for accessing the SAP Extractor data source. This is the password s for the communication user created earlier in SAP.

#### Security

See [*Security*](#Security) below.

#### CDC properties

Run extractor every (minutes): Specify how often to check for changes.

#### Name

The display name for the source connection.

### Connecting to a SAP system using load balancing

#### Data source

- Data gateway

Select a Data Movement gateway to use.

If you do not want to use Data Movement gateway, select None. For information on Data Movement gateway, see [*Qlik Data Gateway - Data Movement*](../../../Gateways/replication-gateway.htm).

Information noteThis field is not available with the Qlik Talend Cloud Starter subscription, as it does not support Data Movement gateway

- Connect to: Select Load balancing environment.
- Message server: The host name or IP address of the message server host.
- Application servers group name: The name of the SAP server group. This is an optional group of application servers in a load balancing connection.
- SAP system name: The SAP R/3 name.
- Message server service: The name of the SAP message server service as specified in the following file:

  <system drive>:\WINDOWS\system32\drivers\etc\services

  If you do not specify a value, the Data Provider for SAP uses the following default name:

  sapms<R/3 system name>
- Client identifier: The System ID of the SAP Extractor data source.

#### Account properties

- User Name: The user name for accessing the SAP Extractor data source. This is the user name for the communication user created earlier in SAP.
- Password: The password for accessing the SAP Extractor data source. This is the password s for the communication user created earlier in SAP.

#### Security

See [*Security*](#Security) below.

#### CDC properties

Run extractor every (minutes): Specify how often to check for changes.

#### Internal properties

Internal properties are for special use cases and are therefore not exposed in the dialog. You should only use them if instructed by Qlik Support.

Use the ![Create new](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) and ![Cancel](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin.svg) buttons to the right of the fields to add or remove properties as needed.

#### Name

The display name for the source connection.

## Security

In the Security settings, you can configure Secure Network Communication (SNC).

### Prerequisites for working with SNC

Follow the steps below to install the Secure Network Communication (SNC) client on the Data Movement gateway machine.

#### What you need:

- An exported certificate (.crt) of the SAP server. Export the certificate as follows:
  1. Log into the SAP system.
  2. Run STRUST transaction.
  3. Select SNC SAPCryptolib.
  4. Select the subject under Own Certificate.
  5. Click the Display > Change option, and select Export certificate.
  6. From the Certificate section, choose the type and save the file.
- SAPCAR.EXE
- SAP user (authorized customer)
- The version of the crypto library which is installed on the corresponding SAP server

#### Installing the SNC client

1. Create a workspace folder for the SAP SNC files and binaries (hereafter referred to as "your SNC folder"), for example: "C:\snc\"
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
9. Bind the PSE file with the OS user and create the CRED\_V2 file in SECUDIR folder as follows:
   1. Make a note of the OS user under which the Qlik replication server is running. To do this on Linux, run the ps aux command.
   2. Run the following command:

      sapgenpse seclogin -p <PSE\_File\_Name>.pse -x <PSE\_PIN> -O <OS\_USER>

      Example:

      sapgenpse seclogin -p usr.pse -x password123 -O SYSTEM
10. Generate the CRT file by executing the following command:

    sapgenpse export\_own\_cert -o <PSE\_File\_Name>.crt -p <PSE\_File\_Name>.pse -x <PSE\_PIN>

    Example:

    sapgenpse export\_own\_cert -o usr.crt -p usr.pse -x password123
11. Import the SAP Application Server Certificate (<SERVER\_CRT>) to the PSE by executing the following command:

    sapgenpse maintain\_pk -a <SERVER\_CRT>.crt -p <PSE\_File\_Name>.pse -x <PSE\_PIN>

    Example:

    sapgenpse maintain\_pk -a sapsys.crt -p usr.pse -x password123
12. To verify that the DN of the SAP Server’s PSE was imported into the client, run the following command and then check the "subject" value:

    sapgenpse maintain\_pk -v -l -p <PSE\_File\_Name>.pse

    Example:

    sapgenpse maintain\_pk -v -l -p usr.pse

#### Importing the client certificate

1. Connect to the SAP Application Server and navigate to the "STRUST" transaction using an authorized user.
2. Double-click the SNC (SAPCryptolib) folder.
3. Click ![Display-chang button](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/change-button-sap.png) to switch to Change view.
4. Click ![Certificate import button](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/import-cert-sap.png) to import the certificate.
5. In the new dialog, enter the path to the .crt file that was created earlier, then click continue.
6. Verify the details of the certificate in the Certificate section.
7. Click Add to Certificate List to add the certificate to the list.
8. Save the changes.

#### Determining the server SNC name

There are two ways you can determine the server name:

- Method 1: Decrypt the server CRT file using the OpenSSL command. The server name will be part of the subject.
- Method 2: This method requires appropriate permissions. While connected to the system:
  1. Run the RZ10 transaction.
  2. Select the system profile.
  3. Select the Extended Maintenance option and then click Display.
  4. The value of the snc/identity/as parameter should be the SNC name.

### Connection settings

Configure the SNC settings in the SAP Extractor connector as follows:

- Activate Secure Network Communication: Select to turn on SNC.
- SNC name: The SNC partner name.

  Example:

  p:CN=SYS, OU=SAP, O=Qlik, C=IS
- SNC quality of protection - Select one of the following:
  - Authentication only: Select to verify the identity of the SAP Extractor machine. This is the minimum protection level offered by SNC.
  - Integrity protection: Select to detect any changes or manipulation of the data, which might have occurred between the Data Movement gateway machine and the SAP Extractor machine.
  - Privacy protection: Select to encrypt the messages being transferred to prevent eavesdropping. Privacy protection also includes integrity protection. This is the maximum level of protection provided by SNC.
  - Maximum security available: The maximum level of data protection supported by the SAP Extractor machine.
