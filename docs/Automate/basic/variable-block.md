---
title: "Variable block"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/basic/variable-block.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Blocks", "Basic blocks"]
---

# Variable block

The variable block is a variable that can be used in your automation. It has a name and type, and it can store data when the automation is running.

![Variable block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/variable-block.png)

A variable block is commonly used in following situation:

- When an automation needs to temporarily store and transform data during its execution.

Information note

The variable is not stored in a database. When the automation stops, the variable data is erased.

## Configuring a variable block

Configure the variable block to a new or existing variable that can be used in the automation.

### Inputs

A variable block only requires a variable. However, to set the variable, you first have to create one.

#### Variable

When you add a variable block to the canvas for the first time, it will detect that you have no variables. You need to create one to use the variable block.

Variable block inputs

![variable block input](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/variable-block-input.png)

#### Manage variables

Create a new variable and select the variable type from the dropdown menu. When you save it, it will be available in the Variable field on the variable block.

Manage variables window

![manage variable](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/variable-block-create.png)

#### Variable types

Variables have a name and a type. The type defines the type of data it can hold. The following types are available:

- **String**

  Alphanumeric characters as text: `this is a string`
- **List**

  A list of items: `[ { "id": 123 }, { "id": "356" }, "abc" ]`
- **Table**

  A list of lists: `[ [ "item 1", "item 2", "item 3"], [ "item 4", "item 5", "item 6"] ]`
- **Object**

  A JSON object: `{ "name": "Bill", "id": 123 }`
- **Number**

  A numeral: `976429`

  Information note

  The variable type cannot be changed after it has been created.

#### Operations on variables

Once the variable is set, you select how the variable is used. The operation differs for each variable type.

##### String

Table showing the string operations

| Operation | Description |
| --- | --- |
| Empty | Make the variable empty (set it equal to an empty text). |
| Set the value of | Set the value of the variable (a text). |
| Append to | Add extra text at the end of the variable. |

##### List

Table showing the list operations

| Operation | Description |
| --- | --- |
| Empty | Make the list empty. |
| Add item to | Add an item (e.g. a record = object) to the list. |
| Merge other list into | Add all the items of another list to the current list. |

##### Table

Table showing the table operations

| Operation | Description |
| --- | --- |
| Empty | Make the table empty. |
| Add row to | Add a row to the table. The input should be a list of items (e.g. a list of strings). |

##### Object

Table showing the object operations

| Operation | Description |
| --- | --- |
| Empty | Make the object empty. |
| Set equal to object | Set the object equal to any other object (JSON structure). |
| Set key/values of | Set individual keys and their value. (The value can be any other JSON structure, such as object, text, or list.) |
| Merge other object into | Merge another object into the current object. If the same key exists in both objects, a conflict exists. You can configure the On conflict behavior: Either ignore the conflicting key (this means it will not be merged into the current object) or rename keys (this means a new key key\_1 will be added into the current object). |
| Rename key in | Rename a key in the object. |
| Remove key/value in | Remove a key in the object. |

##### Number

Table showing the number operations

| Operation | Description |
| --- | --- |
| Set value of | Set the value of the variable (a number). |
| Add to | Add to the value of the variable. |
| Subtract from | Subtract from the value of the variable. |
| Multiply from | Multiply the value of the variable. |
| Divide from | Divide the value of the variable. |
