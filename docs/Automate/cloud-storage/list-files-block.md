---
title: "List files block"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/cloud-storage/list-files-block.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Blocks", "Cloud storage blocks"]
---

# List files block

The list files block lists all the files located at a specified path on a cloud storage location.

![List files block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/list-files-block.png)

A list files block is commonly used in the following situations:

- When you want to get a list of files to use as input elsewhere in the automation.
- When you want to get a list of files before adding a new file to the path.

## Configuring a list files block

Configure the block to list the files from a cloud storage location.

## Inputs

The list files block requires an authenticated connector and a folder path on the cloud storage. The path can include field mapped values from preceding blocks.

List files block inputs

![list files block with dropbox connection and path shown](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/list-files-block-inputs.png)

## Settings

The Settings tab is where you choose what the block does if it encounters an error.

Block settings tab

![General settings for all cloud storage blocks](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/cloud-storage-general-settings.png)

## Connection

The Connection tab is where you can authenticate your cloud storage provider. Once you select the storage provider on the Inputs tab, a Connect button appears here which opens up an authentication window. You must authenticate the connection to use this block.

Block connection tab

![Check if file exists block with Connect your dropbox shown](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/cloud-storage-general-connection.png)

## Learn more

- [Qlik Community - How to use the cloud storage blocks in automations](https://community.qlik.com/t5/Official-Support-Articles/Qlik-Application-Automation-How-to-use-the-cloud-storage-blocks/ta-p/1928265).
