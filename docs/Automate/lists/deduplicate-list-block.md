---
title: "Deduplicate list block"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/lists/deduplicate-list-block.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Blocks", "List blocks"]
---

# Deduplicate list block

The deduplicate list block removes duplicate items from a list. If the list contains three identical items, the block will leave one instance of that item. Items are compared based on a defined key.

![deduplicate list block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/deduplicate-list-block.png)

A deduplicate list block is commonly used in the following situations:

- When an automation merges lists resulting in duplicate items.
- When an automation requires user input resulting in duplicate items in a list.

## Configuring a deduplicate list block

Configure the deduplicate list block to compare items within a single list.

Information note

List blocks do not use iterators. This means that lists are loaded in memory before doing the processing of any data. If your automation contains large lists, the automation might fail with an out-of-memory error. Instead, use a [loop block](../basic/loop-block.htm) to iterate through large lists.

### Inputs

The deduplicate list block requires a list and a key. A list is an array of objects. The list can be a field mapped list from a preceding block. The key should be a unique key that appears in the list.

Deduplicate list block input fields

![deduplicate list block inputs](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/deduplicate-list-block-inputs.png)

#### Example list

```
[
      {"email": "sven@acme.com", "name": "Sven Doe"},
      {"email": "svenja@acme.com", "name": "Svenja Doe"}
]
```

### Settings

Select the Compare value case-insensitive checkbox if you want to ignore case when removing duplicates.

## Example of removing duplicates

Input list:

```
[
      {"email": "john@doe.com", "name": "John Doe"},
      {"email": "bill@acme.com", "name": "Bill Davis"},
      {"email": "john@doe.com", "name": "John"},
]
```

With the key `email`, the output of the deduplicate list block is the following list:

```
[
      {"email": "john@doe.com", "name": "John Doe"},
      {"email": "bill@acme.com", "name": "Bill Davis"}
]
```

The block searches for items in the list that matches the unique key `email`, then removes all but the first match of that item.
