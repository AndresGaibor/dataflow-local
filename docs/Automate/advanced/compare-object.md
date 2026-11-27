---
title: "Compare object block"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/advanced/compare-object.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Blocks", "Advanced blocks"]
---

# Compare object block

The compare object block compares two objects. The output is either the identical or unique key-value pairs from the two objects.

![compare object block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/compare-object-block.png)

Make sure to reference an actual object for each input, not just one field.

A compare object block is commonly used in the following situations:

- When your automation needs to evaluate two different inputs to find common objects.
- When your automation needs to evaluate two different inputs to find unique objects.

## Configuring a compare object block

Configure the block to compare two objects.

### Inputs

The compare object block requires two objects as input that are to be compared. The objects can be field mapped objects from preceding blocks.

Compare object block input fields

![Compare object block input showing two variable to compare](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/compare-object-block-input.png)

### Settings

The Settings tab is where you choose what the compare object block is looking for: similar objects or different objects.

- Return key/values that are the same in both objects returns key-value pairs inside the object that are the same.
- Return key/values that are different in both objects returns key-value pairs inside the object that are different.

  - Choose whether to ignore keys that are not in both objects.

Compare object block settings

![Compare object block settings with output mode and ignore fields](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/compare-object-block-settings.png)
