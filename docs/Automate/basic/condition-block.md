---
title: "Condition block"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/basic/condition-block.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Blocks", "Basic blocks"]
---

# Condition block

The condition block sets a condition on the automation flow. The outcome of the condition determines the subsequent flow of the automation.

![alt text](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/condition-block.png)

A condition block is commonly used in following situations:

- When an automation should continue only if the output of the preceding block is not empty.
- When an automation adds a new record only if it does not already exist.
- When an automation has alternative outcomes depending on a preceding block.

Tip note

The condition block is identical to an `if-else` statement in a programming language.

## Configuring a condition block

Configure the condition block to set up alternative outcomes based on preceding blocks.

### Inputs

The condition functions as an `if-else` statement. If the condition block is evaluated to be true, the automation has one outcome, if false, it has a different outcome.

#### Conditions

The If field requires a field mapping from a previous block and a conditional operator.

Condition block inputs

![condition block inputs](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/condition-block-input.png)

You can use one of the following operators:

- equals
- does not equal
- is greater than
- is greater than or equal
- is less than
- is less that or equal
- is empty
- is not empty
- is text
- is not text
- is number
- is not number
- is object
- is not object
- is list
- is not list
- is email
- is not email
- is phone
- is not phone
- contains
- does not contain
- is true
- is false

You can add more than one condition to the condition block if you want to create `AND` or `OR` conditions. Create a second condition, then toggle the When all/some conditions are met switch to create an `AND` or `OR` condition.

Condition block with two conditions as inputs

![Multiple conditions on condition block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/condition-block-and.png)

#### How to use a condition block

When you add a condition block to the canvas, there are YES and NO branches below the block. Optionally add blocks to these branches if they need to be executed when the condition is true or false.

An automation with a condition block

![Condition example showing QCS reload and slack messages](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/condition-block-example.png)
