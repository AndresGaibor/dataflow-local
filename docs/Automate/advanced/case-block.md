---
title: "Case block"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/advanced/case-block.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Blocks", "Advanced blocks"]
---

# Case block

The case block takes some type of input, evaluates whether it meets a condition, and executes different blocks depending on the value of that input and the condition.

![Case block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/case-block.png)

A case block is commonly used in the following situations:

- When your automation needs to evaluate the input before executing subsequent blocks.
- When your automation needs to evaluate the input before making a choice on which block to execute next.

## Configuring a case block

Configure the block to evaluate input before proceeding.

### Inputs

The case block requires an item to check as input and at least one case to evaluate. The item to check can be a field mapped item from a preceding block and the case must be a typed string or integer.

Case block input fields

![case block inputs showing input and case fiels](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/case-block-input.png)

The case block executes different subsequent blocks depending on the case evaluation.

Case block inside an automation

![case block with a case and a stop block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/case-block-withCase.png)
