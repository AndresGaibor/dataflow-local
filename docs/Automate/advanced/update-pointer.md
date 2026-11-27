---
title: "Update pointer block"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/advanced/update-pointer.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Blocks", "Advanced blocks"]
---

# Update pointer block

The update pointer block sets the pointer for an incremental block.

![update pointer block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/update-pointer-block.png)

Incremental blocks are blocks that retrieve data incrementally on each automation run. The pointer is typically represented as timestamp. On the first run the pointer starts at 0. Once the data is retrieved, then the pointer is set to the current timestamp. The next time the block runs, only data that was added or updated between the pointer timestamp and the current timestamp is retrieved, and the pointer is then increased to the current timestamp.

An update pointer block is commonly used in the following situation:

- When your automation has an incremental block and you need to reset the pointer to a value in the past to retrieve and process data once again.
