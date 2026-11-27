---
title: "Limit list block"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/lists/limit-block.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Blocks", "List blocks"]
---

# Limit list block

The limit list block limits the number of items in a list to a set number of items.

![limit list block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/limit-list-block.png)

A limit list block is commonly used in the following situations:

- When an automation displays list data but you only need some items for testing.
- When an automation contains a large list and you only need the most recent items.

## Configuring a limit list block

Configure the limit list block to reduce the number of items within a single list.

### Inputs

The limit list block requires a list and a limit number. The list can be a field mapped list from a preceding block. The number must be an integer.

Limit list block input fields

![limit list block inputs](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/limit-list-block-input.png)
