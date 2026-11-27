---
title: "Working with versions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/working-with-automations/working-with-versions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Working with automations"]
---

# Working with versions

Each time the the automation is executed, a version of the automation is saved to the changelog.

Access the changelog from the Overview section. The changelog is available from the ![vertical three dots icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/Icons/ic_more_vertical.svg) button.

Automation changelog

![the changelog option on overview section](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/changelog.png)

## The changelog

The changelog shows a list of automation executions and when they were executed. Each entry is saved as a JSON object that represents the automation.

Information note

The changelog does not save the output of each block in an automation. Instead it saves the automation as a JSON object that you can use to restore previous versions.

Automation changelog view

![changelog view showing a single saved execution](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/changelog-view.png)

## Restore a previous version

To restore a previous version, copy the automation and paste it onto the automation canvas. Then replace the current automation with the previous version.

Here is an example using a simple automation:

Simple automation

![A simple automation with input and output block](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/automation-simple.png)

1. Copy the previous version using the ![clipboard icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/Icons/ic_clipboard.svg) on the changelog page.
2. Go to the Editor section.
3. Right-click the canvas, then click Paste blocks.

   ![Canvas with two versions of the automation shown](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/automation-restore.png)

   Information note

   The restored blocks are incremented with a number and they are not attached to a start block.
4. Replace the current blocks with the restored blocks.

   ![An automation with the restored blocks](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/automation-restore-replace.png)
