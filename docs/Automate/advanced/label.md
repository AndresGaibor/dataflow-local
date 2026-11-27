---
title: "Label block"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/advanced/label.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Blocks", "Advanced blocks"]
---

# Label block

The label block marks a place in the automation. They are equivalent to a `go to` statement. They are used in combination with go to label blocks.

![label block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/label-block.png)

A label block is commonly used in the following situations:

- When your automation contains sections that should be processed non-sequentially.
- When your automation is large and you want to organize your canvas into sections.
- When your automation has [go to label blocks](go-to-label.htm).

Information note

When an automation jumps to a label, the automation flow continues from that point in the automation. It does not return to the previous location. To create a function-like behavior in your automation, use the [call automation block](../basic/call-automation-block.htm).

## Configuring a label block

Configure the block to have a named label.

### Inputs

The label block requires a name, which can be either a string or an integer.

Label block input field

![label block with a name](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/label-block-input.png)
