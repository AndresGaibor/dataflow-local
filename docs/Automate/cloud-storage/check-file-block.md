---
title: "Check if file exists block"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/cloud-storage/check-file-block.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Blocks", "Cloud storage blocks"]
---

# Check if file exists block

The check if file exists block connects to a cloud storage location and looks for a named file.

![Check if file exists block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/check-if-file-exists-block.png)

## Configuring a check if file exists block

Configure the block to connect to a cloud storage provider and search for a file.

## Inputs

The check if file exists block requires an authenticated cloud storage provider and a path to the file. The cloud storage providers are available from the drop-down menu. You manually add the file path to the Path field.

Check if file exists block inputs

![check if path exists input with dropbox selected as storage provider](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/check-if-file-exists-input.png)

## Settings

The Settings tab is where you choose what the block does if it encounters an error.

Block settings tab

![General settings for all cloud storage blocks](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/cloud-storage-general-settings.png)

## Connection

The Connection tab is where you can authenticate your cloud storage provider. Once you select the storage provider on the Inputs tab, a Connect button appears here which opens up an authentication window. You must authenticate the connection to use this block.

Block connection tab

![Check if file exists block with Connect your dropbox shown](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/cloud-storage-general-connection.png)
