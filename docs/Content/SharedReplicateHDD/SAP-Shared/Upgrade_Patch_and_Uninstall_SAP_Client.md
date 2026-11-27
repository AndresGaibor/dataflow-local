---
title: "Upgrading/patching and uninstalling the Replicate  SAP Client"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/Content/SharedReplicateHDD/SAP-Shared/Upgrade_Patch_and_Uninstall_SAP_Client.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SAP sources", "SAP (Application)", "Prerequisites", "Install the Replicate for SAP Client on the SAP machine"]
---

# Upgrading/patching and uninstalling the Replicate SAP Client

The following instructions explain how to upgrade/patch, and uninstall the Replicate SAP Client.

Information note

If you are applying a patch or upgrading the Replicate for SAP Client, you should only install the main transport and the ECC-specific transport (if upgrading on an ECC system). Do not install the configuration transport again, or any customizations made to the configuration will be lost.

To upgrade or patch the Replicate SAP Client on ECC Systems

1. Apply the new main transport (InstallCode.zip).
2. Apply the new ECC-specific transport (InstallCodeECC.zip).

To upgrade or patch the Replicate SAP Client on non-ECC systems

- Apply the new main transport (InstallCode.zip).

To uninstall the Replicate SAP Client

1. Apply the "Delete Main" transport (DeleteCode.zip).
2. Apply the "Delete Package" transport (DeletePackage.zip).

   Information note

   Do not apply items 3 and 4 if you are also running Qlik Gold Client Solution.
3. Apply the “Delete Common” transport (DeleteCodeCommon.zip)
4. Apply the “Delete Common Package” transport (DeletePackageCommon.zip)
