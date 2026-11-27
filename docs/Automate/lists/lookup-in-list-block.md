---
title: "Lookup item in list block"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/lists/lookup-in-list-block.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Blocks", "List blocks"]
---

# Lookup item in list block

The lookup item in list block searches for a specific item inside a list.

![lookup item in a list block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/lookup-item-list-block.png)

A lookup item in list block is commonly used in the following situation:

- When an automation needs a specific object from a list.

## Configuring a lookup item in list block

Configure the lookup item in list block to select a specified item within a single list.

Information note

List blocks do not use iterators. This means that lists are loaded in memory before doing the processing of any data. If your automation contains large lists, the automation might fail with an out-of-memory error. Instead, use a [loop block](../basic/loop-block.htm) to iterate through large lists.

### Inputs

The lookup item in list block requires a list and a condition. The list can be a field mapped list from a preceding block. The input condition accepts keys, for example **email**, or a nested key like **profile.email**.

Look up item in list block input fields

![lookup item in list block inputs](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/lookup-item-list-block-input.png)

## Example of looking up item in list

List:

```
[
      {"email": "john@doe.com", "name": "John Doe"},
      {"email": "bill@acme.com", "name": "Bill Davis"}
]
```

If the above list is the input list, and the condition is `email` equals *john@doe.com*, then the resulting list is:

```
{"email": "john@doe.com", "name": "John Doe"}
```
