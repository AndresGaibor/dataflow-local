---
title: "Open file block"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/cloud-storage/open-file-block.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Blocks", "Cloud storage blocks"]
---

# Open file block

The open file block opens a file from a cloud storage provider. This block is needed to use the [copy file block](copy-file-block.htm).

![open file block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/open-file-block.png)

An open file block is commonly used in the following situations:

- When you need to copy a file from a cloud storage location.
- When you need to read a file from a cloud storage location.

## Configuring an open file block

Configure the block to open a file.

## Inputs

The open file block is a read-only block. It requires an authenticated connector that can be a cloud storage provider or an HTTP connection.

### Cloud storage connector

Select the connector from the drop-down menu and enter the path to the file.

Open file block inputs

![open file block using Dropbox connection and showing path](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/open-file-block-cloud.png)

### HTTP

Select the HTTP connector from the drop-down menu and enter a URL to the file. You can optionally add required headers and parameters that are used for the HTTP call.

Open file block inputs menu

![Open file block using HTTP input showing URL](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/open-file-block-HTTP.png)

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
