---
title: "Compare lists block"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/lists/compare-lists-block.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Blocks", "List blocks"]
---

# Compare lists block

The compare lists block compares lists to find common and unique items between them.

![compare lists block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/compare-list-block.png)

A compare lists block is commonly used in the following situations:

- When an automation needs to find identical items across lists.
- When an automation needs to find unique items across lists.

## Configuring a compare lists block

Configure the compare lists block to compare the items in two lists.

Information note

List blocks do not use iterators. This means that lists are loaded in memory before doing the processing of any data. If your automation contains large lists, the automation might fail with an out-of-memory error. Instead, use a [loop block](../basic/loop-block.htm) to iterate through large lists.

### Inputs

The compare lists block requires two lists and a key as inputs. A list is an array of objects. The lists can be field mapped from a preceding block. The key should be a unique key that appears in the list.

Compare lists block input fields

![The input fields for the compare list block showing field mapped values for each list](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/compare-list-block-inputs.png)

#### Example list

```
[
      {"email": "john@doe.com", "name": "John Doe"},
      {"email": "bill@acme.com", "name": "Bill Davis"}
]
```

### Settings

The Settings tab is where you specify what you want to compare between lists. In the List unique key fields, enter the keys for each list that you want to compare. They can be the same or different, depending on the keys used in each list.

The settings options for the compare list block

![compare list block settings](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/compare-list-block-settings.png)

In the Compare results field, you choose whether you want to intersect the lists or compare list 1 to list 2.

- **Intersect**

  Finds all items in list 1 and list 2 that match the unique keys you defined in the settings.
- **Unique in list 1**

  Finds items in list 1 that match the unique key for list 1 that are do not match items in list 2 with the unique key for list 2.

In the Results field, you choose to merge the results from both lists or show only the results from list 1.

Compare results and Results fields

![compare list block compare fields](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/compare-list-block-compare.png)

## Examples of comparing lists based on keys

List 1:

```
[
      {"email": "john@doe.com", "name": "John Doe"},
      {"email": "bill@acme.com", "name": "Bill Davis"}
]
```

List 2:

```
[
      {"email": "john@doe.com", "city": "NY"},
      {"email": "ann@acme.com", "city: "Paris"}
]
```

If you compare the results as Unique in list 1 (all items in list 1 that do not exist in list 2), a unique key: `email`, and set the results to Items from list1, the block produces the following list:

```
[
      {"email": "bill@acme.com", "name": "Bill Davis"}
]
```

The block searches for items in both lists that match the unique key `email`, then searches for items that exist only in list 1.

If you compare the results as Intersect (all items that exist in both list 1 and list 2), a unique key: `email`, and set the results to Items from list1, the block produces the following list:

```
[
      {"email": "john@doe.com", "name": "John Doe"}
]
```

Tip note

If you want to combine the objects from both lists, select Merged items from list 1 and list 2 to . This option will match items based on the key, but it will merge the items from each list into a single object.

```
[
      {"email": "john@doe.com", "name": "John Doe",  "city": "NY"}
]
```
