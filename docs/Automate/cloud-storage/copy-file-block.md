---
title: "Copy file block"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/cloud-storage/copy-file-block.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Blocks", "Cloud storage blocks"]
---

# Copy file block

The copy file block copies a file and adds it to a cloud storage provider.

![copy file block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/copy-file-block.png)

A copy file block is commonly used in the following situations:

- When you open a file from one location and want to add it to another.
- When you want to create a backup of files generated during an automation.

## Configuring a copy file block

Configure the block to copy a source file and add it to another location.

## Inputs

The copy file blocks requires a source file and a destination. The block also requires a preceding [open file block](open-file-block.htm). The Source file field is automatically populated with the field mapping from the open file block. The destination is a cloud storage location, and it requires an authenticated connection.

Copy file block inputs

![Copy file block with source http, dropbox, and destination path shown](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/copy-file-block-inputs.png)

## Settings

The Settings tab is where you choose what the block does if it encounters an error.

Block settings tab

![General settings for all cloud storage blocks](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/cloud-storage-general-settings.png)

## Connection

The Connection tab is where you can authenticate your cloud storage provider. Once you select the storage provider on the Inputs tab, a Connect button appears here which opens up an authentication window. You must authenticate the connection to use this block.

Block connection tab

![Check if file exists block with Connect your dropbox shown](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/cloud-storage-general-connection.png)
