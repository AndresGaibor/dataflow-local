---
title: "Sleep block"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/basic/sleep-block.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Blocks", "Basic blocks"]
---

# Sleep block

The sleep block pauses the automation for a defined amount of time. When the sleep block is executed, the automation continues processing data from previous blocks after the wait time has passed.

![Sleep block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/sleep-block.png)

A sleep block is commonly used in following situation:

- When you have a call URL block inside a loop, and the automation might exceed the rate limit of the API.

Information note

The automation continues to run when sleep block is executed. This means the automation still takes up a slot of concurrent executions in your tenant.

## Configuring a sleep block

Configure the sleep block to sleep for a set duration.

## Inputs

The only input required is the sleep duration.

### Time

Enter the number of seconds you want the automation to sleep for when it reaches the sleep block.
