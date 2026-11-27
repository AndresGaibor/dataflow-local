---
title: "Working with loops"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/working-with-automations/working-with-loops.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Working with automations"]
---

# Working with loops

This section shows you how to use loop blocks in your automation. Loops are useful when processing data in a list.

There are two types of loop blocks. The [loop block](../basic/loop-block.htm) is a general loop block that lets you process list data. This is helpful for user generated lists and other list data that might be retrieved from web URLs. Some connector blocks are also loop blocks because they retrieve list data from their data source. If you add a connector block that includes a loop function, you don't need to add a general loop block.

## Loop blocks

Loops blocks include a loop function, which is depicted by a loop attached to the block. The image below shows a Qlik Cloud loop block and the general loop block. The only difference is that the Qlik Cloud loop block receives input from Qlik Cloud whereas the general loop block can receive input from other sources.

Loop blocks

![showing two loop blocks](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/loop-block-show.png)

### Example loop

In this example automation, the goal is to get a list of Qlik Cloud users by their ID. To do this, a List Users block is used to retrieve user information from Qlik Cloud in the form of a JSON array, which is essentially a list. Included in the list is the user ID for each user.

```
[
    {
    "id": "BLYLYomLgPwzf-hQCtWO_",
    "tenantId": "xqFQ0k66vSR8f9G7J-v",
    "status": "active",
    "name": "",
    "email": "",
    "links": {
      "self": {
        "href": "https://qcs.us.qlik.com/api/v1/users/BLYLYomLgPwzf-hQCtWO_"
      }
    }
  },
  {
    "id": "5cGmylXFwqPGtUdmKFljPH4H",
    "tenantId": "xqFQ0k66vSR8f9G7J-v",
    "status": "active",
    "name": "",
    "email": "",
    "zoneinfo": "America/Los_Angeles",
    "locale": "",
    "links": {
      "self": {
        "href": "https://qcs.us.qlik.com/api/v1/users/BLYLYomLgPwzf-hQCtWO_"
      }
      ...
]
```

Another way to view this data is in a table format.

Table viewer

![the table view of a list block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/table_view.png)

The example automation needs to go through this list of user information and access just the ID field for each row. To do this for the current example, a Get User block is added to the List Users loop. The input to this block is `{$.listUsers.item.id}`, which specifies only the `id` value of the list. Because it is inside the loop, it will retrieve the `id` for each row until there are no more rows. The Output block prints the IDs to the Output section. The second Output block outside of the loop prints a message when the loop is finished.

Automation with loop

![Loop block example fetchedQlik Sensecloud users by ID](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/loop-block-example.png)

When an automation containing a loop is executed, you can see how the blocks are processed by looking at the output chronologically. In the image below, the List Users block runs one time to get the complete list of users. Next, the Get User and Output blocks run in a loop until there are no more list items. Finally, the Output block outside of the loop runs once.

Chronological output

![loop block output shown chronologically](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/loop-block-chron.png)

## Looping a fixed number of times

You can force the loop to run *x* number of times by using a variable block and a general loop block. The variable must be set to a list type, and the loop must receive the variable as input.

### Example fixed loop

In this example automation, the goal is to execute a loop a fixed number of times. To do this, start with a variable block with a list type and add a new item for each iteration. The example below shows a list variable with four items.

Variable block as a counter

![automation with variable block set to counter list](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/loop-counter.png)

The variable, which is a list with four items, is the input to the general loop block. An output block inside the loop shows the actual value of the counter for each iteration.

Automation with a variable and loop

![Automation loop with variable as counter and output inside loop](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/loop-counter-full.png)

When this automation is executed, the Output section shows the value of the counter for each iteration.

Automation output

![loop counter output showing counter values](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/loop-counter-output.png)
