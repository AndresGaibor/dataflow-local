---
title: "List functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/working-with-automations/list-functions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Working with automations", "Working with formulas"]
---

# List functions

You can manipulate list data using the available text functions in Qlik Automate.

## Count

Counts the number of items in a list.

`{$.getContacts}` = [{"name":"John Doe},{"name":"Jane Doe"}]

`{count:{$.getContacts}}` = 2

## Get keys

Returns a list of keys from key-value pairs in an object.

`{$.contact}` = {"name":"John Doe", "email":"jd@email.com"}

`{getkeys:$.contact}` = ["name","email"]

## Implode

Converts a list of items into a comma-separated string. You can change the delimiter as a parameter.

`{$.contacts[*].name}` = ["John","Jane","Bill","Barb"]

`{implode:{$.contacts[*].name}}` = John,Jane,Bill,Barb

With a linebreak as the delimiter:

`{implode:{$.contacts[*].name}, "{linebreak}"}` = John</br>Jane</br>Bill</br>Barb

## Sort

Sorts a list ascending. For lists of object, add a parameter to sort the objects by key name. Use `sortdecs` to sort a list descending.

`{$.contacts[*].name}` = ["John","Jane","Bill","Barb"]

`{sort:{$.contacts[*].name}}` = ["Barb","Bill","Jane","John"]

With a key name as a parameter:

`{$.contacts[*].name}`=

```
[
  {
    "name":"John",
    "id":"100"
  },
  {
    "name":"Bill",
    "id":"4"
  },
  {
    "name":"Barb",
    "id":"17"
  },
  {
    "name":"Jane",
    "id":"1"
  }
]
```

`{sort:{$.contacts[*].name}, "id"}` =

```
[
  {
    "name":"Jane",
    "id":"1"
  },
  {
    "name":"Bill",
    "id":"4"
  },
  {
    "name":"Barb",
    "id":"17"
  },
  {
    "name":"John",
    "id":"100"
  }
]
```

Information note

The algorithm applies a natural sort order, not an alphanumeric sort order. Change the algorithm as needed.

The sort order options

![The sort order algorithm list for the sort function](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/sort-order.png)
