---
title: "Using the write table for real-time inventory management"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/WriteTable/Stories/manage-inventory.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations", "Creating write tables", "Use cases for write tables"]
---

# Using the write table for real-time inventory management

This example shows how the write table can be used in real-time inventory management.

A company sells physical products and uses Qlik to analyze inventory and orders. When demand suddenly spikes, new orders can exceed stock, slowing order fulfillment.

With the write table, analysts can see products, warehouse quantities, and outstanding orders. When demand surges, they can quickly update how many units to reorder, set priorities, and add notes for the purchasing team. Clicking Place order runs an automation that collects updates, generates a purchase order, and emails it, helping the team respond faster to changing demand.

## Try it yourself

1. [Create a write table](../Create/create.htm) with these columns.

   Write table for real-time inventory management.

   ![Write table visualization that has been created for real-time inventory management.](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/write-table_inventory-management_chart.png "Click to view full size")
2. [Add a button to trigger an automation](../../Button/create-buttons.htm#Execute).
3. Configure the automation and link it to the button. See:

   - [Learn how to configure an automation to connect to the change-stores API.](../Create/create.htm#ExampleAutomateMain)
   - [Learn how to run an automation with custom parameters through the Qlik Sense button.](https://community.qlik.com/t5/Official-Support-Articles/How-to-run-an-automation-with-custom-parameters-through-the-Qlik/ta-p/2496485)
4. Test it: Edit a few rows, click Save, then click the button to see the workflow in action.

Real-time inventory management with the write table.

![Diagram showing how a company can use the write table for inventory management](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/write-table_inventory-management.png "Click to view full size")

## Learn more

- [*Write table*](../Analyze/write-table.htm)
- [*Creating write tables*](../Create/create.htm)
