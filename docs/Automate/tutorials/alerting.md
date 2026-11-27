---
title: "Alerting and messaging"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/tutorials/alerting.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Tutorials"]
---

# Alerting and messaging

A significant benefit of Qlik Automate is that you create alerting workflows that send alerts and messages to almost anywhere your team is collaborating. In this tutorial, you'll learn how to use some of the Qlik Cloud connector blocks and the Slack connector blocks to create an alerting workflow to send information about a Qlik Sense app reload to your team through Slack. This tutorial walks through the different blocks needed to create the workflow, increasing the level of complexity as we move forward.

Information note

In addition to the method described below, you can also use Qlik's built-in alerts with your automations. For more information, see [Monitoring data with alerts](../../Sense_Hub/Alerting/monitoring-changes-with-alerts.htm) and [Personal settings](../../Sense_Hub/Introduction/profile-settings.htm). With automations, you can, for example, configure an alert to notify users when a scheduled automation fails. Note that only one alert is sent per six hours.

## Send a simple message to Slack

First, create an automation that sends a pre-defined message to a Slack channel.

1. Go to the Connections section of automations.
2. From the Explore menu, find Slack, then click Add.
3. When the authentication window opens, enter your login credentials and click Allow.
4. Go to the Editor.
5. From the block selector pane, under My connectors, select Slack. This opens all of the connector blocks available for the Slack connector.
6. Drag the Send Message block onto the canvas and attach it to the start block.

   ![Slack automation to send a message](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/slack.png)
7. In the block configuration pane, enter the following information:

   a. For the Channel field, enter the channel name, or use the `do lookup` function to find the channel.

   ![alt](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/slack-channel.png)

   b. Open Slack and invite the Qlik Automate app to the channel. You can do this with the `/invite` [slash command](https://slack.com/intl/en-ca/help/articles/201259356-Slash-commands-in-Slack), then select Add apps to this channel.

   c. Add a message to the Text field. This is the text that is sent to the channel. The text field accepts field mapped values. See [Working with field mapping](../working-with-automations/working-with-fieldmapping.htm) for information on field mapping input values.

   d. Optionally add an icon emoji or an icon URL.
8. Save the automation, then click Run.

If you want to reply to a thread rather than send a message to the main channel, you can specify the thread ID. The thread ID is the `ts` value returned from the send message block.

Thread Ts field on the Slack send message block

![Thread ID field](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/slack-channel-thread.png)

Slack thread

![Slack posting to a thread](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/slack-result-thread.png)

## Alert your team of a new app

As an app creator, you might want to let your team know that you've created a new app. Keeping the automation from above, modify it to send information about your new app.

1. Select the start block and change the Run mode to Webhook.
2. Set the Connector to Qlik Cloud Services.
3. Set the Event to App created.

   ![Alerting automation with the start block set as webhook](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/alerting-trigger2.png)
4. Select the Send message block and clear the text field.
5. Create a new message: "Hey team, check out this new app:".
6. Click the end of the text you just added and field map the app name from the start block output. In the output, the `name` value is under `attributes`. Save your automation.

   ![alt](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/alerting-message-json.png)
7. Go to the hub and create a new app. The moment the app is created, the automation posts the message to Slack.

   ![Slack message showing the automation message](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/alerting-message-app.png)

## Alert your team of a data update

As the app owner, you want to let your team know when you update the app data.

1. Select the start block from the previous example and change the Event to App Data Updated.

   ![Start block with app updated as webhook](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/alerting-trigger-data2.png)
2. Select the Send message block and clear the Text field.
3. Add some new text "Hey team, the app has some new data."
4. In the Text field, field map the `name` from the start block output so the Slack message includes the app name.

   ![Send message block showing the message output](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/alerting-trigger-message.png)
5. Go to your the data manager for your app and click Load data. The automation will be triggered and a Slack message will be sent.

   ![The Slack message from the automation bot after trigger from data reload](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/alerting-message-slack.png)
