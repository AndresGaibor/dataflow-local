---
title: "Merge lists block"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/lists/merge-lists-block.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Blocks", "List blocks"]
---

# Merge lists block

The merge lists block combines two lists into a new single list.

![merge lists block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/merge-lists-block.png)

A merge lists block is commonly used in the following situations:

- When an automation contains similar lists that can be combined.
- When an automation contains two lists such that one list can be nested in the other.

## Configure the merge lists block

Configure the merge lists block to combine two lists.

Information note

List blocks do not use iterators. This means that lists are loaded in memory before doing the processing of any data. If your automation contains large lists, the automation might fail with an out-of-memory error. Instead, use a [loop block](../basic/loop-block.htm) to iterate through large lists.

### Inputs

The merge lists blocks requires two input lists. The lists can be field mapped from preceding blocks.

Merge lists block input fields

![merge lists block inputs](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/merge-lists-block-inputs.png)

### Settings

The Settings tab is where you specify how to merge the two lists. You decide the merge strategy, the unique keys used for the merge strategy, and how to handle duplicate items.

#### Item merge strategy

The first option is **Merge list 1 item and list 2 item in one new item**. This strategy creates a new list that includes all key-value pairs from each list.

The second option is **Add list 2 items as children to list 1 items**. This strategy is used for lists that have a parent-child relationship. All items of list 2 are added as children of an object in list 1, based on a key.

#### Unique key

The unique key is used to compare items in the lists. For example `email` in one list and `profile.email` in the second. Objects are matched and merged based on the values matching these keys.

#### On duplicate keys

The first option is **Ignore item from list 2**. This option does not merge the duplicate item from list two into the new list.

The second option is **Merge item from list 2 into item from list 1**. This option merges the item from list 2 into the same item from list 1. Key-value pairs that are unique in list two are added to the duplicate item in list 1.

#### Merge values case-insensitive

Check this box to ignore case differences between lists.

## Examples of merging two lists

Below are examples of merging lists.

### Merging list 1 item and list 2 item in one new item

To merge items from list 1 and list 2 into a new list, select **Merging list 1 item and list 2 item in one new item** and enter the unique key for each list. Choose what to do for duplicate keys.

Merge lists block settings

![Merge settings matching same key](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/merge-lists-block-settings1.png)

Example list 1:

```
[
      {"email": "john@doe.com", "name": "John Doe"},
      {"email": "bill@acme.com", "name": "Bill Davis"}
]
```

Example list 2:

```
[
      {"email": "john@doe.com", "city": "NY"},
      {"email": "ann@acme.com", "city": "Paris"}
]
```

The merged list looks like this:

```
[
      {"email": "john@doe.com", "name": "John Doe", "city": "NY"}
      {"email": "bill@acme.com", "name": "Bill Davis"}
      {"email": "ann@acme.com", "city": "Paris"}
]
```

### Add list 2 items as children to list 1 items

To merge items from list 2 into list 1 as children for a specific item, select **Add list 2 items as children to list 1 items**, then enter the key that is the parent for the child items in list 2. Also, for each list, enter the unique keys that are used to match items between lists. Choose what to do for duplicate keys.

Merge lists block settings

![Merge settings parent child relationship](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/merge-lists-block-settings2.png)

Example list 1:

```
[
      {"email": "john@doe.com", "name": "John Doe"},
      {"email": "bill@acme.com", "name": "Bill Davis"}
]
```

Example list 2:

```
[
    {"id": 1, "price": 100, "email": "john@doe.com"},
    {"id": 2, "price": 200, "email": "john@doe.com"}
]
```

The first object in the merged list looks like this:

```
{
  "email": "john@doe.com",
  "name": "John Doe",
  "orders": [ {"id": 1, "price": 100}, {"id": 2, "price": 200} ]
}
```
