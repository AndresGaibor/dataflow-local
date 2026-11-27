---
title: "List pointers block"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/advanced/list-pointer.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Blocks", "Advanced blocks"]
---

# List pointers block

The list pointers block lists all the pointers associated with an incremental block.

![list pointers block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/list-pointers-block.png)

Incremental blocks are blocks that retrieve data incrementally on each automation run. The pointer is typically represented as timestamp. On the first run the pointer starts at 0. Once the data is retrieved, then the pointer is set to the current timestamp. The next time the block runs, only data that was added or updated between the pointer timestamp and the current timestamp is retrieved, and the pointer is then increased to the current timestamp.

An incremental block can have multiple pointers associated to it if the block has an input. In this case a pointer is created for each input value that is used. For example, a List companies incrementally block might have an input organization ID. In this example a pointer will be stored for each organization ID that is used to retrieve data.

A list pointers block is commonly used in the following situation:

- When your automation has an incremental block and you need a list of pointers associated with it in order to delete them one by one to process historic data once again.
