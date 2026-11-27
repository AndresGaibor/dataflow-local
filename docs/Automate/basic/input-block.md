---
title: "Input block"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/basic/input-block.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Blocks", "Basic blocks"]
---

# Input block

The input block receives external input from a user or an external source, for example if the automation is executed through its REST API endpoint.

When a user runs an automation containing an input block from the Hub, Catalog, or other external location, a modal appears to guide them to provide the required input values. For details on how to provide inputs, see [Working with inputs](../working-with-automations/working-with-inputs.htm).

![input block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/input-block.png)

An input block is commonly used in following situations:

- When an automation needs input from a user.
- When an automation is executed through its REST API endpoint.
- When an automation is called from another automation.

Information note

Do not use input blocks for automations that are executed on a schedule because the automation cannot ask for user input when it is executed through a schedule.

Tip note

Blocks have inputs and outputs, which are limited to the scope of each execution of the automation. The input block, however, is the only block that can receive data from outside of its scope.

## Configuring an input block

Configure the input block to receive user input.

### Inputs

The input block can have one or more input fields. Each input field is made up of the following key value pairs.

- Label: The field name for the input.
- Help text: Text that is presented to the user.
- Input type: The type of input the user must enter or select.

Information note

For each input field, you can select whether it is required.

Input block inputs

![input block input field](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/input-block-input.png)

#### Input types

Input blocks can have different input types.

##### Single input line

Lets the user enter a single line of text.

##### Multiple input line

Lets the user to enter multiple lines of text.

##### Dropdown

Lets the user select a predefined item from a dropdown menu.

Information note

Defined as a comma-separated list or an array of {`id`-`name`} pairs. If you defined the options using an array, the name is presented to the user and the ID appears in the field mapping.

##### Multi select

Lets the user select one or more predefined items from a list of options.

Information note

Defined as a comma-separated list or an array of {`id`-`name`} pairs. If you defined the options using an array, the name is presented to the user and the ID appears in the field mapping.

The user input is saved as selected and unselected.

##### Button

Lets the user input information by clicking a button. Each input value is a button.
The user input is saved as an array of Boolean objects: [ {`button 1`: `true`} ].

##### Data

Lets the user add structured JSON data. The data input type is often used in automations that are triggered by their webhook URL to pass webhook parameters to the endpoint. In this case, add the input block directly below the start block.

Automation with input block

![Input block below a start block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/input-block-json.png)

The input parameters are automatically displayed in the example webhook URL of the automation.

See [Working with webhooks](../working-with-automations/working-with-webhooks.htm)

##### Key value pairs

Lets the user add key-value pair objects.

It is typically used in automations that are called by another automation.

##### Field mapping

Lets the user map fields from one system to another, enabling dynamic field name translation between different data sources.
