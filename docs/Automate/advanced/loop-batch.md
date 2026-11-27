---
title: "Loop batch block"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/advanced/loop-batch.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Blocks", "Advanced blocks"]
---

# Loop batch block

The loop batch block loops over items in a list to process items in batch.

![loop batch block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/loop-batch-block.png)

Information note

The loop block also loops over items in a list, but the loop block only processes a single item at a time.

A loop batch block is commonly used in the following situations:

- When your automation has large lists that need to be processed.
- When your automation needs to send items in batch to another destination.

## Configuring a loop batch block

Configure the block to loop over items in a list and processes them in batch.

### Inputs

The loop batch block requires a list and a specified batch size (number of items in a batch). The list can be field mapped from a preceding block. The number of items per batch should be an integer.

Loop batch input fields

![Loop batch block inputs](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/loop-batch-block-inputs.png)
