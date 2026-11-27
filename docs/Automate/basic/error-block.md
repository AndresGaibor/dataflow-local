---
title: "Error block"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/basic/error-block.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Blocks", "Basic blocks"]
---

# Error block

The error block throws an error message and it will cause the current execution run to be in a `failed` or `warning` state.

![Error block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/error-block.png)

An error block is commonly used in following situation:

- When you want your automation to throw an error so the current run will have a `failed` or `warning` state.

## Configuring an error block

Configure the error block to set up what happens when your automation has an error.

### Inputs

The inputs for an error block are a required error message and an action to take.

#### Message

Enter a custom error message that is displayed when this block is executed.

#### Action

Choose to continue the automation or stop the execution when this block is executed.
