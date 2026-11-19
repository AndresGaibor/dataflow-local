---
title: "Fork processor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataFlow/data-flow-processor-fork.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and preparing data with Data flow", "Data flow processors"]
---
# Fork processor

Duplicates the data into two identical outputs.

The **Fork** processor can be used to duplicate the input flow and output up to ten identical output flows that can be processed in a different way according to your needs.

## Usage

The **Fork** processor requires one input flow and at least two output flows.

## Properties

The Fork processor does not require any configuration.

To rename the processor or edit its description, point your mouse over the name or description to change in the **Properties** panel and click the ![Edit](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) **Edit** icon.

## Example: Exporting an intermediary state of the data flow

In this example, you have a flow that cleans and normalizes raw sales data. You want to save the cleaned data at an intermediary step as a file, while the rest of the flow continues through further processors such as an aggregation.

![Data flow with a Fork processor branching into an intermediary target and a continuing flow](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Dataflow/fork_example_1.png)

1. In the data flow editor, add a **Fork** processor after the last processor that produces the intermediary state you want to export.
2. Connect one output of the **Fork** processor to a target node and configure it to save the intermediary data as a file, for example clean\_sales\_data.qvd.
3. Connect the second output to the next processor in your main flow, for example an **Aggregate** processor, and continue adding processors and a target to complete the flow.
4. Click **Run flow**.

## Example: Exporting a data flow to two different output formats

In this example, you want to export the same dataset as a .qvd file for use in Qlik analytics apps, and as a .csv file to share with external stakeholders.

![Data flow with a Fork processor connected to two targets in different output formats](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Dataflow/fork_example_2.png)

1. In the data flow editor, add a **Fork** processor after the last processor in your flow.
2. Connect one output of the **Fork** processor to a **Data Files** target. Configure it to export as a .qvd file.
3. Connect the second output to another **Data Files** target. Configure it to export as a .csv file.
4. Click **Run flow**.
