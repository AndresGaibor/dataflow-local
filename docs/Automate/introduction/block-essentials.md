---
title: "Block essentials"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/introduction/block-essentials.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Blocks"]
---

# Block essentials

Some of the configuration options are common to all blocks, and the way you configure and edit blocks is generally the same.

## Connecting blocks

Every automation begins with a start block, which is already placed on the automation canvas by default. Creating the automation workflow is as easy as dragging a new block onto the canvas. When you add a new block, the connection points are highlighted on the blocks already placed on the canvas.

Connecting blocks on the canvas

![Canvas showing new block added](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/block-add-to-canvas.png)

## General block options

Each block has the same general options menu. Once you drag a block onto the editor, click ![vertical 3 dots icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/Icons/ic_more_vertical.svg) to open the options menu.

General block options menu

![Block actions menu](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/block-actions-menu.png)

The options menu lets you manually trigger a test run, turn the block off and on, add comments about the block, and copy it.

In addition, you can also click Trace data on any block to see where the block's data originated. A new window appears identifying the data source, or sources, of the block.

### Test run

From the general block options menu, click Test Run to manually start an execution. A test run executes the automation from the Start block to the test run block. Test runs let you retrieve data for that block without running the entire automation. The block output from a test run can then be used to field map inputs in other blocks.

Information note

A test run executes an API call, but it does not retrieve all data from the data source.

### Comments

Comments are helpful when you want to provide information about each block in an automation. Add or edit comments from the Edit comment option from the general options menu.

Automation blocks with comments

![Automation showing comments](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/block-basic-comment.png)

Warning note

Block comments are used as input when generating AI descriptions for automations. Do not include personal data or sensitive information in block comments.

### Renaming blocks

You can assign a custom display name to any block type. Renaming a block changes only its displayed name and its internal `name` identifier remains unchanged. Formulas and field mappings continue to use the internal identifier.

The original block name remains visible in the Settings pane for reference.

To rename a block, do the following:

1. Right-click the block on the canvas.
2. Select Rename block.
3. Enter a custom display name. For example, rename Raw API Request to Look up user by ID.
4. Click Save.

Block names can contain any Unicode characters. Leading and trailing whitespace is removed when you save the name.

If another block in the same automation has the same display name, ignoring capitalization and leading or trailing whitespace, a warning appears. You can still save the name.

To restore the default name, clear the custom display name and click Save.

## Block configuration options

Each block can be configured from the right-hand block configuration pane. Not all blocks have the same options, but the basics are the same.

### Formula parsing

Formula parsing is enabled for all blocks by default. To turn formula parsing off, click on the parsing icon on the top-right corner of the block editing pane. To turn formula parsing on click on the icon again.

When formula parsing is off, you can see the raw formula and you can manually edit the formula.

Toggle button to show formula parsing off

![Formula parser toggled on](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/block-toggle-parsing-off.png)

Toggle button to show formula parsing on

![Formula parser toggled on](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/block-toggle-parsing-on_878x433.png)

You can toggle formula parsing on or off. When you turn formula parsing off, the configuration fields show the raw input values. You can manually edit the formula when the formula parser is turned off.

### Inputs

The Inputs section is available for most blocks. Inputs are data passed to the block from somewhere else, either from a preceding block or from user input. When you click inside an input field, you are automatically shown fields from preceding blocks that can be field mapped to the current block. You also have the option to add a formula.

Block inputs section

![The inputs section](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/inputs.png)

### Settings

The Settings section is available for some blocks. Settings are additional configuration values specific to the block and to the type of input it receives. Settings often determine how a block is executed, what it does after it executes, how it handles errors, or how it handles the input from another block.

Block settings section

![Settings section for the input block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/settings.png)

### History

The History section is available to all blocks, except for the start and stop blocks. It shows information about the block for each time it is executed in an automation. Here, you see the input and output for each execution, and the time it took for this block to execute.

- ![view icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/Icons/ic_view.svg) Show hidden fields
- ![code icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/Icons/ic_code.svg) Show raw format
- ![copy icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/Icons/ic_clipboard.svg) Copy data to clipboard
- ![expand icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/Icons/ic_expand.svg) Open data in a new window

Block history section

![The history section for the input block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/history.png)
