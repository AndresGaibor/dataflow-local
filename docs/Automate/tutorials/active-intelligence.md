---
title: "Active intelligence"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/tutorials/active-intelligence.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Tutorials"]
---

# Active intelligence

Automations help you build out active intelligence workflows by bringing real-time information directly to those who need it. In this tutorial, you'll learn how to send data from your analytics app to your team with the click of a button. By the end of this tutorial, you'll be able to trigger an automation to send a Slack message that includes the value of a master item from a button object on a sheet.

## Context

This tutorial is general enough to apply the same principles to an app you currently have in development. The only requirements to follow along with this tutorial are that you have a personal app with at least one master item. If you need to create a master item in your app before you start this tutorial, see [master item](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Measures/create-master-measure-field.htm).

## Create the automation

The automation you create in this tutorial is a simple alerting automation that is executed from a button inside the app. The button creates a bookmark for the current selection and sends the app ID and bookmark ID to the automation. The automation retrieves some measure values based on the bookmark selection and sends a message to Slack.

The first step is to outline the automation without configuring it yet.

1. Starting with a blank automation, add the following blocks one after the other:

   - Inputs (basic)
   - Apply Bookmark (Qlik Cloud connector)
   - Get Measure value (Qlik Cloud connector)
   - Get Measure value (Qlik Cloud connector)
   - Send message (Slack connector)

   Your automation looks like this:

   ![Simple notificiation automation that is triggered from a button](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/active-intelligence_rev.png)
2. Save the automation.

   You'll configure the automation later.

## Create the button

Qlik Sense SaaS lets you add buttons to your sheet, which can be configured to execute automations. Open your app and add a button object to a sheet.

1. From the chart options in the assets panel, drag a button object to the sheet.
2. Under Actions and navigation in the properties panel, click Add action.
3. Under Action, select Execute automation.
4. Under Automation, select the automation you want to trigger as an action.

   The automations that are available appear in the drop-down menu.

   ![drop-down menu for automation action button](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/active-intelligence1.png)
5. Select the Include selections box.

   When you select this option, the button creates a bookmark for the current selection. The app ID and bookmark ID are used as inputs to the automation, and they are used to apply data selections when executing the automation.
6. Optionally, if you want other users with access to your app to be able to run your automation using the button, select Run mode: triggered.

   Warning noteWhen Execute automation uses Run mode: triggered, everyone with access to the sheet and the button can run the automation using the button. When the button is clicked, the automation's Execution Token is visible in the browser's network traffic in the browser developer console. This token can only be used to run that automation and has no use for other automations or other APIs. A user could use this token to run the automation with a different payload than the one created through the button however.
7. Click Copy input block.

   When pasted into your automation, it will add blocks for Input and Apply bookmark, passing the button information into your automation.

The button configuration looks like this:

Button configuration to run an automation

![Button configuration settings to execute automation action](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/button_config.png "Click to view full size")

Information note

You can [style](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/Button/button.htm#anchor-5) and label your button however you want.

## Configure the automation

In this part of the tutorial, you'll configure the automation that you created earlier.

1. Right-click in your automation and select Paste Block(s).

   An Inputs and Apply Bookmark block are automatically added to your automation.
2. Click and drag the Inputs and Apply Bookmark blocks after Start.

   Your automation should now look like this:

   ![The full automation, with Inputs and Apply Bookmark added.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/full-active-intelligence-automation.png)
3. Select the Get Measure Value block. Use the do lookup function to map the app ID and measure ID you want to use in this automation. Repeat this for the second Get Measure Value block.

   ![The do lookup field from a Get measure block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/do-lookup.png)
4. Select the Send Message block. The only required fields are Channel and Text. Once the Slack connection is authenticated, you can use the do lookup function to select a Slack channel.

   a. Open Slack and invite the Qlik Account app to the channel. You can do this with the `/invite` [slash command](https://slack.com/intl/en-ca/help/articles/201259356-Slash-commands-in-Slack), then select Add apps to this channel.

   b. In the block inputs text field, customize a message and include the output from the Get Measure Value blocks.

   ![alt](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/active-intelligence2.png)
5. Save the automation.

## Run the automation

1. Open your sheet containing the button.
2. Make some data selections.

   ![Button on a sheet with a data selection](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/button-click.png)
3. Click the button to send the Slack message. The values included in the message correspond to the data selections. You can test this by making different selections in the app and clicking the button.

   ![Resulting message from the button](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/slack-active.png)
