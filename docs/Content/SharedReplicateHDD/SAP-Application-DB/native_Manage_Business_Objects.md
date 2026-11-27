---
title: "Managing business groups and tables"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/Content/SharedReplicateHDD/SAP-Application-DB/native_Manage_Business_Objects.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SAP sources", "SAP (Application)", "Prerequisites"]
---

# Managing business groups and tables

This prerequisite is only necessary if you want to edit the default Business Groups and/or tables before moving them.

Before you can manage business groups and tables, you first need to launch the SAP Client UI.

To launch the SAP Client user interface:

1. Open your SAP client console.
2. Double-click one of the SAP Application (DB) Sources.

   You will be prompted for your user name and password.
3. Enter your credentials for logging in to the selected SAP Application (DB) Source.
4. Enter /nzr4sap in the drop-down list at the top of the console and then press [Enter].
5. Click the Business Groups Configuration button.

   A list of Business Groups is displayed in the left pane.

## Managing business groups

To add a new Business Group

1. Click the Create toolbar button.

   The Create Business Group dialog box opens.
2. Enter a name for your Business Group and then press [Enter].

   The new Business Group is added to the Business Groups list in the left pane.

To duplicate a Business Group

1. Click the Copy toolbar button.

   The Business Group Configuration dialog box opens.
2. In the New Bus Object field, enter a name for the new Business Group and then press [Enter].

   The duplicated Business Group is added to the Business Groups list in the left pane.

To delete a Business Group

- Select the Business Group you want to delete and then click the Delete toolbar button.

  The Business Group is deleted.

## Managing tables

To add a new table to a Business Group

1. In the left pane, expand the desired Business Group.
2. Double-click the Tables icon.

   A list of tables is shown in the right pane.
3. Click the ![Edit](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/pencil.png) button above the table list to enter Edit mode.
4. Click the ![Add Table](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/sapclient_add_table_bg.png) button that appears to the right of the ![Edit](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/pencil.png) button.

   An empty row is added to the tables list.
5. Enter the Table Name (i.e. the virtual ABAP table) and the name of the corresponding Source Table (i.e. the physical table).
6. To save your changes click the Save button in the main toolbar.

To remove a table from a Business Group

1. In the left pane, expand the desired Business Group.
2. Double-click the Tables icon.

   A list of tables is shown in the right pane.
3. Click the ![Edit](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/pencil.png) button above the table list to enter Edit mode.
4. Select the table you want to delete.
5. Click the ![Delete Table](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/sapclient_delete_table_bg.png) button that appears to the right of the ![Edit](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Replicate/pencil.png) button.

   The table is deleted.
6. To save your changes click the Save button in the main toolbar.

## Accessing tables with a non-English language

To enable moving of non-English SAP tables, add them to the configuration as follows:

1. From the zr4sap transaction, click the Metadata Language Configuration button.
2. Click the Add button and select the appropriate language.
3. Click Save.

To remove a previously configured language, select the desired row and click the Delete button.
