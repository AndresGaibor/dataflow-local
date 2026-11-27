---
title: "Read data from file block"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/cloud-storage/read-data-block.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Blocks", "Cloud storage blocks"]
---

# Read data from file block

The read data from file block reads data from a file that is opened with the [open file block](open-file-block.htm).

![read data from file block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/read-data-block.png)

A read data from file block is commonly used in the following situations:

- When you need to read the data in an opened file to use as input for other blocks.
- When you need to read the data in an opened file to update other files.

## Configuring a read data from file block

Configure the block to read data from a file.

## Inputs

The read data from file block requires a file as input. The file must come from the [open file block](open-file-block.htm). If you do not have this block, the File field is empty.

Once you select a file, you can choose the mode for reading the file.

Read data from file inputs

![read data from file block showing the available modes](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/read-data-block-mode.png)

### Mode

The Automatic mode detects the data format of the file and takes the appropriate actions.

Select the CSV mode for CSV files. When you select this mode, you can specify the delimiter, the encoding type, and whether the file has headers. You can also specify which columns should be read. If this field is left empty, all columns are read.

Read data from file block mode selection

![read dat from file block with csv mode selected](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/read-data-block-mode-csv.png)

Select the JSON mode for JSON files. There are no additional configuration options for JSON.

Select the Raw (line-by-line) mode for other files types that might not work with automatic mode. You can optionally set the encoding type.

## Settings

The Settings tab is where you choose what the block does if it encounters an error.

Block settings tab

![General settings for all cloud storage blocks](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/cloud-storage-general-settings.png)

## Connection

The Connection tab is where you can authenticate your cloud storage provider. Once you select the storage provider on the Inputs tab, a Connect button appears here which opens up an authentication window. You must authenticate the connection to use this block.

Block connection tab

![Check if file exists block with Connect your dropbox shown](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/cloud-storage-general-connection.png)
