---
title: "Activate the extractors for Data Movement gateway"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/Content/SharedReplicateHDD/SAP-Extractor/extractor_SAP_activating_transports.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SAP sources", "SAP Extractor", "Prerequisites"]
---

# Activate the extractors for Data Movement gateway

After importing the transports, you need to activate them before configuring the Data Movement gateway SAP Extractor connector.

Information note

As the transport installations are not automatically validated by Data Movement gateway, it is strongly recommended to validate the installations before running tasks with the SAP Extractor connector.

To do this:

1. Open the Data Movement gateway for SAP Extractors launch pad through transaction /QTQVC/EXTREP.

   ![The Qlik Talend Data Integration for SAP Extractors launch pad. It contains four sections: Configuration, containing the Target Logical System, Activate Extractors, and Manage Extractors commands; Delta Settings, containing the Delete Delta Init command; Data Extract, containing the Set Filter Criteria, Schedule Extractor, and Delete Extract commands; and Reports/Logs, containing the View Extract Logs and View Job Status commands.](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/sap_activate1.png)
2. Create a logical system for the Extractor solution to use as follows:

   Information note

   This should be separate from any other Logical System present in the system.

   1. In the Configuration section, click the Target Logical System button.
   2. In the Target Logical system field, enter a technical name for the Logical System and then click Create.

      ![The Define Logical System tab. Contains fields for the Source Logical system, Target Logical system, and RFC Server name.](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/sap_extract2.png)

      This will create the Logical System and setup its associated RFC connections for use by the Qlik Talend Data Integration connector.

      The following confirmation should be shown:

      Successfully created logical system.
3. Activate the extractors to associate them with the Logical System as follows:
   1. In the Configuration section, click the Activate Extractors button.
   2. Using the Logical System created earlier, select the extractor (also known as DataSource) you wish to activate from the list of available extractors.

      Information note
      - An extractor may be missing from the list if it has not yet been activated in the ECC system in transaction RSA5.
      - Activated extractors will be recorded in the ROOSPRMSC and ROOSPRMSF tables associated with the Logical System.

      ![The Activate Extractor tab. Contains fields for Target Logical System, DataSource, Transfer Method, and Language.](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/sap_extract3.png)
   3. Click Activate to start the activation process.

      You should see a confirmation message at the bottom of your screen.
   4. Repeat steps b-c for any additional extractors you wish to activate.
   5. To confirm successful activation of the extractors, click Manage Extractors.

      The Manage Extractors window opens.

      ![The Manage Extractors window.](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/sap_extract4.png)

      In the Manage Extractors window, you can verify which extractors have been activated for your Logical System and manage their use.

Once you have confirmed that the required extractors have been activated, you can then configure the SAP Extractor connector settings in Data Movement gateway.
