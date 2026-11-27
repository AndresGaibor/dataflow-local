---
title: "Replace Field Names In List"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/lists/replace-field-names-in-list-block.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Blocks", "List blocks"]
---

# Replace Field Names In List

The replace field names in list block replaces the field names used in a list with another field name.

![replace filed names in list block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/replace-field-name-block.png)

A replace field names in list block is commonly used in the following situation:

- When an automation contains a list, and you want to change one or more of the field names.

## Configuring a replace field names in list block

Configure the replace filed names in list block to replace existing field names with new field names.

Information note

List blocks do not use iterators. This means that lists are loaded in memory before doing the processing of any data. If your automation contains large lists, the automation might fail with an out-of-memory error. Instead, use a [loop block](../basic/loop-block.htm) to iterate through large lists.

### Inputs

The replace field names in list block requires a list and a field name to replace. The list can be field mapped from a preceding block. Enter the field name to replace and the new field name.

### Settings

The Settings tab is where you can tell the block to either keep or remove the all other field names in the list. If you choose to remove them, the new list only contains the items for field names you replaced.

Replace field names in list block settings

![replace field names in list settings](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/replace-field-name-block-settings.png)

## Example of replacing field names in a list

Input list:

```
[
      {"mail": "john@doe.com", "fname": "John", "lname": "Doe"},
      {"mail": "bill@acme.com", "fname": "Bill", "lname": "Davis" }
]
```

The list above is the input list. It contains two objects with three key-value pairs. The new field name is `email` and all values `{$.inputs.mail}` are replaced with the new field name.

Replace field names in list input fields

![replace field names in list input](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/replace-field-name-block-input.png)

The replace field names in list block produces the following list:

```
[
      {"email": "john@doe.com", "fname": "John", "lname": "Doe"},
      {"email": "bill@acme.com", "fname": "Bill", "lname": "Davis" }
]
```
