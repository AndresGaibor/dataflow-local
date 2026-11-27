---
title: "Using the write table for delivery status management"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/WriteTable/Stories/manage-delivery.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations", "Creating write tables", "Use cases for write tables"]
---

# Using the write table for delivery status management

This topic presents a use case for how the write table can be used for delivery status management.

A company’s logistics division uses Qlik to analyze the status of their deliveries. When a delivery is at risk of being delayed, the customer support team must reach out to the customer in real-time.

With write table, analysts can update delivery records in real-time by flagging delays, adding notes, and suggesting next steps for their customer support team such as informing customers about delay times or rescheduling delivery dates.

Every 5 minutes, a scheduled automation exports the latest updates from the write table and sends them to the customer’s support portal, ensuring the team always has the most recent information.

## Try it yourself

1. [Create a write table](../Create/create.htm) with these columns.

   Write table for delivery status management.

   ![Write table visualization that has been created for real-time delivery status management.](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/write-table_delivery-management_chart.png "Click to view full size")
2. [Create a scheduled automation.](/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/working-with-automations/working-with-schedules.htm)
3. [Configure the automation to pick up new updates from the change store.](../Create/create.htm#ExampleAutomate1)

   Diagram outlining the scheduled automation.

   ![Diagram showing the scheduled automation for picking up write table change store changes and then sending them to a support portal](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/write-table_scheduled-automation-delivery-management.png "Click to view full size")
4. Test it: Edit a few rows in the write table, click Save, and then manually run the automation to pick up new changes.

## Learn more

- [*Write table*](../Analyze/write-table.htm)
- [*Creating write tables*](../Create/create.htm)
