---
title: "Delete file block"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/cloud-storage/delete-file-block.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Blocks", "Cloud storage blocks"]
---

# Delete file block

The delete file block deletes a file from a cloud storage location.

![Delete file block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/delete-file-block.png)

A delete file block is commonly used in the following situation:

- When you want to delete an existing file on a cloud storage location when an automation is executed.

## Configuring a delete file block

Configure the block to delete a source file from a location on a cloud storage location.

## Inputs

The delete file block requires an authenticated connector and a path to a file on the cloud storage location. The path can include field mapped values from preceding blocks.

Delete file block inputs

![delete file block inputs with dropbox connection and path to file shown](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/delete-file-block-inputs.png)

## Settings

The Settings tab is where you choose what the block does if it encounters an error.

Block settings tab

![General settings for all cloud storage blocks](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/cloud-storage-general-settings.png)

## Connection

The Connection tab is where you can authenticate your cloud storage provider. Once you select the storage provider on the Inputs tab, a Connect button appears here which opens up an authentication window. You must authenticate the connection to use this block.

Block connection tab

![Check if file exists block with Connect your dropbox shown](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/cloud-storage-general-connection.png)
