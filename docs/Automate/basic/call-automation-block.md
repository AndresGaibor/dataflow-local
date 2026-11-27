---
title: "Call automation block"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/basic/call-automation-block.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Blocks", "Basic blocks"]
---

# Call automation block

The call automation block calls another automation.

![The call automation block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/call-automation-block.png)

A call Automation block is commonly used in following situations:

- When an automation needs input from another automation.
- When an automation should be executed only when another automation is executed.

Information note

To send data to another automation, the automation receiving the data must have an [input block](input-block.htm). To receive data from another automation, the automation sending data must have an [output block](output-block.htm).

## Configuring a call automation block

Configure the call automation block to call another automation.

### Inputs

The call automation block requires another automation as input. The Automation to call field has a lookup function to show you the available automations.
