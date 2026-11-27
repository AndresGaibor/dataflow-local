---
title: "Install the Replicate for SAP Client on the SAP machine"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/Content/SharedReplicateHDD/SAP-Shared/Install_Replicate_for_SAP_Client_on_the_SAP_Machine.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SAP sources", "SAP (Application)", "Prerequisites"]
---

# Install the Replicate for SAP Client on the SAP machine

This section describes how to install the transports that make up the Replicate for SAP Client (R4SAP).

1. Go to [Product Downloads](https://community.qlik.com/t5/Downloads/tkb-p/Downloads).
2. Select Qlik Data Integration.
3. In the Product list, select Qlik Replicate.
4. In the Release list, select the Qlik Replicate version that corresponds to the release date (year and month) of your Data Movement gateway version. For example, if your Data Movement gateway version is 2024.5.54 (Year.Month.Build), select May 2024.
5. In the Release Number list, select Initial Release.
6. In the Download Link column, click the QlikReplicate\_<version>\_R4SAP.zip link to start your download.

There are eight transports in total, which are provided in the following folders:

- DeleteCode
  - Required for uninstalling the Replicate for SAP Client.
- DeletePackage
  - Required for uninstalling the Replicate for SAP Client.
- DeleteCodeCommon - Required for uninstalling the Replicate for SAP Client.
- DeletePackageCommon - Required for uninstalling the Replicate for SAP Client.
- InstallCode
  - The main transport.
- InstallCodeQRI - An install transport required when working with Qlik Talend Data Integration.
- InstallCodeECC
  - A transport with additional logic for ECC SAP systems .
- InstallConfig
   - The configuration transport.

## The installation procedure

Information note

- The transports must be installed in the order they appear below. Installing the transports in the incorrect order or omitting/skipping any of the transports will result in unexpected issues with data tasks.
- When installing the Replicate for SAP client, do not chose the "overwrite" option if Gold Client is already installed on the Data Movement gateway server machine. Otherwise, the Gold Client software will stop working.

To install the transports on ECC systems:

1. Install the main transport file (InstallCode).
2. Install the ECC-specific transport (InstallCodeECC).
3. Install the configuration transport (InstallConfig).

To install the transports on non-ECC systems (e.g. CRM):

1. Install the main transport file (InstallCode).
2. Install the configuration transport (InstallConfig).

To create the table /QTQVC/QRI:

- Import transport InstallCodeQRI from the installation package (QlikReplicate\_<version>\_R4SAP).

To create the record in the table:

1. Run transaction SE38.
2. Execute report /HTG/QLIK\_RESOURCE\_IDENTIFIER.

Information note

If you are [applying a patch or upgrading](Upgrade_Patch_and_Uninstall_SAP_Client.htm) Replicate for SAP Client, you should only install the main transport and the ECC-specific transport (if upgrading on an ECC system). Do not install the configuration transport again, or any customizations made to the configuration will be lost.
