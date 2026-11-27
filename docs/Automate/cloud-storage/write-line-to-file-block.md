---
title: "Write line to file block"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/cloud-storage/write-line-to-file-block.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Blocks", "Cloud storage blocks"]
---

# Write line to file block

The write line to file block writes data to a file.

![write line to file block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/write-line-file-block.png)

A write line to file block is commonly used in the following situation:

- When you create a file during an automation and need to add data to it.

Information noteAs a best practice, use the Save and close file block after the Write line to file block to ensure the content is written to the file when exported to the cloud storage platform.

## Configuring a write line to file block

Configure the block to write data to an existing file.

## Inputs

The write line to file block requires a file to write the line to and the data to write. The File field is automatically filled by the Create file block, and the Data field can accept user-entered or field mapped data.

Information note

This block is used with the Create file block.

Write line to file inputs

![Write line to file inputs with fields filled in](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/write-line-file-block-inputs.png)

## Settings

The Settings tab is where you choose what the block does if it encounters an error.

Block settings tab

![General settings for all cloud storage blocks](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/cloud-storage-general-settings.png)

## Connection

The Connection tab is where you can authenticate your cloud storage provider. Once you select the storage provider on the Inputs tab, a Connect button appears here which opens up an authentication window. You must authenticate the connection to use this block.

Block connection tab

![Check if file exists block with Connect your dropbox shown](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/cloud-storage-general-connection.png)
