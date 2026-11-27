---
title: "Working with field mapping"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/working-with-automations/working-with-fieldmapping.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Working with automations"]
---

# Working with field mapping

Field mapping refers to data from one block being mapped to a field in another block.

## Block input and output

Each block in an automation has some form of data input and output. The input and output are JSON objects, whose key names can be mapped to other fields. This means that the output from one block can be used to provide input for another block. The field mapping is simply a placeholder that receives the output from a preceding block.

Here is an example of a simple automation that fetches the list of users from a Qlik Sense SaaS tenant and prints the output to the automation output view.

Example automation with output

![Example automation with aQlik SenseList users block connected to an output block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/field-map-example.png)

The List Users block is configured to fetch the first five users of the Qlik Cloud tenant. The output for this block produces a JSON object.

```
[
  {
    "id": "c37iCQrY1p1C-8x-4WwQN11c",
    "tenantId": "xqFQ0k66vSR8f9G7J-vZtHZ",
    "status": "active",

    ...

]
```

The Output block is configured to print only the user IDs. This mean that you should map the `id` field to the Output block input field.

```
{
    "id": "c37iCQrY1p1C-8x-4WwQN11c"
}
```

## Field mapping

When you add a block to your automation, the input fields detect the JSON output from preceding fields. When you click the input field, you can select the field mapping from the preceding blocks.

Data to output field

![Showing the input field with auto populated field inputs from preceding block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/field-map-example-mapping.png)

Click the field mapping to show the full JSON object. Here, you can select the key name that you want to map to the input field.

JSON object from block output

![Showing the input field with auto populated field inputs from preceding block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/field-map-example-json.png)

When you select a key name, the input field shows the field mapping. Field mapping is simply a placeholder that references the `item.id` JSON path from the `$.listUsers` block. This is shown when you toggle [formula parsing](../introduction/block-essentials.htm#anchor-3).

Renaming a block changes only its displayed name. It does not change existing formulas or field mappings, which continue to reference the block's internal name, such as `$.listUsers` in this example.

```
{$.listUsers.item.id}
```

When the automation is executed, the List Users block fetches the users from the Qlik Cloud tenant. The input field for the Output block references the `item.id` JSON path from the output of the List Users block.

Output view

![The output section of the automation showing the field mapped IDs](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/field-map-example-output.png)
