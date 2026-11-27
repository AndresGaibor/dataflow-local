---
title: "Loop block"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/basic/loop-block.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Blocks", "Basic blocks"]
---

# Loop block

The loop block iterates over items in a list. All of the blocks inside a loop are executed until the items in the list are finished, or some other condition stops the loop.

![alt text](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/loop-block.png)

A loop block is commonly used in the following situation:

- When an automation needs to process list items one by one.

Information note

Some connector blocks output a list and have built-in loop functions. You don't need to use a loop block for these connector blocks.

## Configuring a loop block

Configure the loop block to iterate over items in a list.

Tip note

- See [exit loop block](../advanced/exit-loop.htm) on how to use an exit loop block.
- See [Working with loops](../working-with-automations/working-with-loops.htm) on how to build loops in your automation.

### Input

The input for a loop block is a field mapping of a preceding block that contains a list.

#### Loop over items of list

Click the Loop over items of list field to show to available field mappings.

Loop block inputs

![iterate over items loop block settings](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/loop-block-iterate.png)

#### Placeholders to access the item in the loop and the index

The input of the loop block should be a list. Inside the loop you can use the placeholder { $.loop.item } to reference the current item from the list that is being used.

Information note

To see the raw formula for placeholders, see [Working with field mapping](../working-with-automations/working-with-fieldmapping.htm).

Loop inputs raw formula

![part of automation showing a loop and formula to access item](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/loop-block-item.png)

#### Index

The placeholder { $.loop.index } can be used to get the index of the current item, starting with 0 for the first item (0, 1, 2, 3...).

#### Iterate over keys of an object

You can iterate over the properties of an **object** with key value pairs. In this case the placeholder { $.loop.item } will give you the *value* of each property, and { $.loop.index } will give you the *key* of each property. These placeholders should only be used inside the loop.
