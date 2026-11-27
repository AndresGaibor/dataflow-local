---
title: "Delete pointer block"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/advanced/delete-pointer.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Blocks", "Advanced blocks"]
---

# Delete pointer block

The delete pointer block deletes a pointer from an incremental block.

![delete pointer block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/delete-pointer-block.png)

Incremental blocks are blocks that retrieve data incrementally on each automation run. The pointer is typically represented as timestamp. On the first run the pointer starts at 0. Once the data is retrieved, then the pointer is set to the current timestamp. The next time the block runs, only data that was added or updated between the pointer timestamp and the current timestamp is retrieved, and the pointer is then increased to the current timestamp.

A delete pointer block is commonly used in the following situation:

- When your automation has an incremental block and you want to delete the pointer in order to retrieve all data once again.
