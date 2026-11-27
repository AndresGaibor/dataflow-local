---
title: "Create file block"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/cloud-storage/create-file-block.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Blocks", "Cloud storage blocks"]
---

# Create file block

The create file block creates a new file.

![create file block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/create-file-block.png)

A create file block is commonly used in the following situation:

- When you want to create a new file to store output data from the automation.

## Configuring a create file block

Configure the block to create a file by entering a file name and optionally a path to an existing folder or bucket.

## Inputs

The create file block requires an authenticated connection to a cloud storage provider and a path for the new file. The cloud storage providers are available from the drop-down menu. You manually add the file path to the Path field.

Information noteWhen an automation calls out to an external server where SSL verification is required, the server should provide the complete chain certificates. If the complete chain certificate is not provided the verification may fail.

Information note

This block is used with the Write line to file block.

Create file block inputs

![create file block inputs with connector and path shown](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/create-file-block-input.png)

## Settings

The Settings tab is where you choose what the block does if it encounters an error.

Block settings tab

![General settings for all cloud storage blocks](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/cloud-storage-general-settings.png)

## Connection

The Connection tab is where you can authenticate your cloud storage provider. Once you select the storage provider on the Inputs tab, a Connect button appears here which opens up an authentication window. You must authenticate the connection to use this block.

Block connection tab

![Check if file exists block with Connect your dropbox shown](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/cloud-storage-general-connection.png)
