---
title: "Output block"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/basic/output-block.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Blocks", "Basic blocks"]
---

# Output block

The output block shows output to the user during the execution of an automation. The output block can show the output from other blocks or some user-entered output.

![Output block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/output-block.png)

An output block is commonly used in following situations:

- When an automation is executed manually and the user needs to see the output.
- When an automation is executed through its REST API endpoint.
- When an automation is called from another automation.

Tip note

Blocks have inputs and outputs, which are limited to the scope of each execution of the automation. The output block, however, is the only block that can share data outside of its scope.

## Configuring an output block

Configure the output block to receive input and display output.

### Input

The Inputs tab is where you tell the output block what to display as output. You can combine plain text and field mappings in one output block. The desired output is displayed on the automations Output.

Output block inputs

![output block input](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/output-block-input.png)

#### Formatting output

The output block supports [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) to let you customize the output format. For example, you can add Markdown table markup to make the output more readable.

Output block inputs with Markdown formatting

![output block with Markdown formatting](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/outputBlock-format-output.png)

The output is formatted in a readable table.

Output table

![output block settings](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/output-block-output-table.png)

### Settings

The Settings tab is where you choose the Display Mode for the output.

#### Display modes

- Add this output to the list of outputs (default)

  Automations can have many output blocks, and they can be used in loops. Each output is added to the overall output of the automation.
- Use only this output (overwrites previous outputs)

  The output of the block will replace all previous outputs.
- Merge data with the existing output

  Output is concatenated into one output (string).

### Accessing the output block outside its scope

An automation can call another automation and access the output from the output block. When an automation is called from another automation, the output block defines which data is returned to the calling automation.

### Providing output in a REST API endpoint

When an automation is called from its REST API endpoint URL (Webhook URL), the JSON response of the API call is defined by the output block.

If you use the default display mode Add this output to the list of outputs the output of the API endpoint of the automation will be an array (list), where each item in the list is the JSON object of one output block.

Information note

Set the display mode to Use only this output. This prevents your output from being formatted as an array (list).
