---
title: "Save and close file block"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/cloud-storage/save-close-block.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Blocks", "Cloud storage blocks"]
---

# Save and close file block

The save and close file block saves a file that has been opened during the execution of an automation and then closes it.

![save and close file block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/save-close-file.png)

A save and close file block is commonly used in the following situation:

- When you open a file in an automation to read or write data to it.

Information noteAs a best practice, use the Save and close file block after the Write line to file block to ensure the content is written to the file when exported to the cloud storage platform.

## Configuring a save and close file block

Configure the block to safely save and close an open file.

## Inputs

The save and close a file block requires a file from a preceding block. The File field is automatically populated with any open files in your automation from preceding blocks.

Save and close file block inputs

![save and close file block with file selected](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/save-close-file-input.png)

## Settings

The Settings tab is where you choose what the block does if it encounters an error.

Block settings tab

![General settings for all cloud storage blocks](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/cloud-storage-general-settings.png)

## Connection

The Connection tab is where you can authenticate your cloud storage provider. Once you select the storage provider on the Inputs tab, a Connect button appears here which opens up an authentication window. You must authenticate the connection to use this block.

Block connection tab

![Check if file exists block with Connect your dropbox shown](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/cloud-storage-general-connection.png)
