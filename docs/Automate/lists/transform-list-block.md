---
title: "Transform list"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/lists/transform-list-block.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Blocks", "List blocks"]
---

# Transform list

A transform list block takes a list and transforms it to another list by mapping existing values to new fields.

![transform list block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/transformlist-block.png)

A transform list block is commonly used in the following situation:

- When an automation contains a list, and you want to add new fields to the items in that list.

## Configuring a transform list block

Configure the transform list block to transform the output of one list to another list.

Information note

List blocks do not use iterators. This means that lists are loaded in memory before doing the processing of any data. If your automation contains large lists, the automation might fail with an out-of-memory error. Instead, use a [loop block](../basic/loop-block.htm) to iterate through large lists.

### Inputs

The transform list block requires a list and a field. The list can be a field mapped list from a preceding block. The field is the new key that the existing value is mapped to. Enter the new field name, then field map the list value you want to transform.

## Example of transforming a list

Input list:

```
[
      {"email": "john@doe.com", "name": "John Doe"},
      {"email": "bill@acme.com", "name": "Bill Davis"}
]
```

The list above is the input list. It contains two objects with two key-value pairs. The new field name is `fullname` and all values `{$.inputs.name}` are mapped to the new field name.

Transform list block input fields

![Transform list block inputs](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/transformlist-block-inputs.png)

The transform list block produces the following list:

```
[
      {"fullname": "John Doe"},
      {"fullname": "Bill Davis"}
]
```
