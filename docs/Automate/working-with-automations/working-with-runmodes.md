---
title: "Working with run modes"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/working-with-automations/working-with-runmodes.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Working with automations"]
---

# Working with run modes

Runs modes refer to how the automation starts. The run mode option is only available on the start block. Each run mode is explained in this topic.

## The start block

The start block is the first block in any automation. The run mode is the only configuration required on this block.

The four run modes are:

- [Manual](#manual)
- [Scheduled](#scheduled)
- [Triggered](#triggered)
- [Webhook](#webhook)

Run modes

![Start block run modes drop-down menu](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/start-block.png)

## Manual

When you set the start block to manual, the automation is only executed when you click Run. Manual run mode is used most often for testing. If the automation contains an input block, a modal appears when you run it from outside the automation editor, offering you the choice to stay on your current page or navigate to the history view to provide the required input values. For details, see [Working with inputs](working-with-inputs.htm).

## Scheduled

When you set the start block to Scheduled, the automation runs based on the schedule you define.

Configure the schedule with the following options:

- Based on: Select the recurrence pattern—Per minute, Hourly, Daily, Weekly, Monthly, or Yearly.
- Times per day: Select how often the automation runs within a day—Once, Every hour, Every 2 hours, Every 3 hours, Every 4 hours, Every 6 hours, or Every 12 hours.
- Timezone: Select the time zone for the schedule (for example, GMT+1:00, GMT+2:00).
- Time of day: Choose the hour and minute for execution.
- Run this schedule: Choose when the schedule is active—Continuously, From start date, Until end date, or Between start and end dates. Date fields appear when you select an option that requires date boundaries.

Run mode inputs

![Start block configured in Scheduled run mode](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/ui_QA_startBlock_Schedule2.png)

## Triggered

When you set the start block to triggered, you can use the automation webhook URL to trigger the automation. For details, see [Triggered webhooks](working-with-webhooks.htm#triggered-webhooks).

Information note

For triggered automations, the Run asynchronously setting in the Start block determines the maximum execution time for all triggered runs.

When this setting is cleared (`async = false`), the maximum execution time is configurable from 10 seconds up to 5 minutes (default: 55 seconds). When selected (`async = true`), the maximum execution time is 4 hours. The setting is configured per automation and is not selected per trigger request.

If the service is temporarily unavailable, a triggered request can be accepted for later processing instead of running immediately.

## Webhook

When you set the start block to webhook, the automation is triggered by an event from a connector block. This option is only available for some connectors, which are prepopulated in the Connector field. For details, see [Native webhooks](working-with-webhooks.htm#native-webhooks).
