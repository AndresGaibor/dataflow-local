---
title: "Go to label block"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/advanced/go-to-label.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Blocks", "Advanced blocks"]
---

# Go to label block

The go to label block jumps to a named label block to process another section of the automation.

![go to label block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/go-to-label-block.png)

A go to label block is commonly used in the following situations:

- When your automation contains sections that should be processed non-sequentially.
- When your automation has [label blocks](label.htm).

## Configuring a go to label block

Configure the block to jump to a label block.

### Inputs

The go to label block requires a label as input. The automation must have a label block to use this block. Available labels are automatically populated in the input field.

Go to label block inputs

![go to label block with selected label shown](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/go-to-label-block-input.png)
