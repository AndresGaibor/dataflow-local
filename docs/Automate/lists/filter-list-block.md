---
title: "Filter list block"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/lists/filter-list-block.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Blocks", "List blocks"]
---

# Filter list block

The filter list block filters a list of objects based on one or more conditions. The output of the block is a list with a subset of objects from the input list.

![filter list block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/filter-list-block.png)

A filter list block is commonly used in the following situations:

- When an automation contains a list that contains unnecessary items.
- When an automation contains a large list but only a subset of that list is required.

## Configuring a filter list block

Configure the filter list block to filter items within a single list.

Information note

List blocks do not use iterators. This means that lists are loaded in memory before doing the processing of any data. If your automation contains large lists, the automation might fail with an out-of-memory error. Instead, use a [loop block](../basic/loop-block.htm) to iterate through large lists.

### Inputs

The filter list block requires an input list and a condition. The list can be a field mapped list from a proceeding block. The input condition accepts keys, for example **email**, or a nested key like **profile.email**.

Filter list block input fields

![Filter list block inputs](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/filter-list-block-inputs.png)

## Example of filtering a list

If you configure the filter list block to filter a list on the condition that `email` is not empty, then the block removes any list item where the `email` key is empty.

Input list:

```
[
      {"email": "john@doe.com", "name": "John Doe"},
      {"email": "", "name": "Bill Davis"}
]
```

Output list:

```
[
      {"email": "john@doe.com", "name": "John Doe"},
]
```
