---
title: "Using templates"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/introduction/templates.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Getting started"]
---

# Using templates

Templates are pre-built automations that are simple to configure and quick to implement. You can customize templates as much or as little as needed to meet your specific use case, and they are especially helpful for understanding the logical sequence in common workflows. This topic provides an overview of how to use templates. See [all templates](template-list.htm) for a list of templates you can use.

Tip note

For a visual demo on how to get started using templates, see [Creating automations from templates](https://share.vidyard.com/watch/VWNXe1SqdFxuY6KZ6YfpBN?).

Information noteThe usage of third-party blocks in an automation run may incur additional costs depending on your type of subscription. Blocks for Qlik apps and services are not considered third-party blocks. For more information, see [Managing Automations](../../Sense_Hub/Admin/mc-monitoring-automations.htm#third-party-blocks).

## Searching templates

Templates are available from the template window when you create a [new automation](creating-automation.htm). Use the category and connector filters to narrow down the templates you see. For example, you can search for templates that include the Slack connector by selecting the Slack connector tag. This filters the available templates to those that have a Slack connector block somewhere in the automation.

Filtered view of the template window

![A filtered view of the template window with the Slack connector selected](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/template-filter.png)

Most of the templates include connectors that integrate third-party cloud applications and services. To use those connectors, you must authentication the connection. See [connector blocks](../connector-blocks/connectors-intro.htm) to learn how to authenticate connectors.

## Customizing templates

When you add a template to the automation canvas, most blocks are preconfigured with field mapped inputs from the preceding blocks, however, you will want to verify and adjust each block as required. You can edit the automation by adding or removing blocks. For example, you might want to use a reporting template to send automatic reports to your team using Slack, but the template that is best suited for your business process is preconfigured in the Microsoft Teams block. You can swap the Microsoft Teams connector blocks for the appropriate Slack connector blocks. When you replace blocks, you'll need to adjust the [field mapping](../working-with-automations/working-with-fieldmapping.htm) between blocks, but using a template provides a good starting point for any automation.

Tip note

Tip: When adapting a template, give blocks descriptive custom display names so their purpose is clear on the canvas. For example, in the [parallel-reload workflow example](#template-example), you can name the blocks "Reload sales app" and "Reload inventory app".

Replacing a Microsoft Teams message block with a Slack message block

![MS Team messaging template showing a Slack block replacement](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/template-customize.png)

## Template example

This example shows you how to choose a template from the template window and how to configure it. Each template has a specific workflow and requires a unique configuration, but this example will help you understand how to walk through a template to adjust it to meet your needs. In this example, you'll configure a template to reload multiple apps in parallel.

Do the following:

1. In the Analytics or Qlik Talend Data Integration [activity center](#glossary-0 "Glossary term"), click Automation.
2. Click Create new automation.
3. Under Connectors, select Qlik.

   This filters templates that include the Qlik connector.
4. Hover over the Reload apps in parallel tile, then click Details.

   The details page provides a preview of what the automation looks like and gives you a short description on what it does.

   ![Details page for the reload apps in parallel template](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/template-details.png)
5. Click Use template.

   You can choose to rename the template, select a Space to save it in, and modify the description. After you save these changes, the template opens in the automation editor.
6. The template includes three Do reload blocks. Optionally add or remove these blocks as needed. For this example, remove one of the reload blocks.
7. On the Inputs section for each Do reload block, enter the app ID for the app you want to reload. Use the Do lookup function to find your app ID.
8. Select the Wait for reloads to complete block. The Reload Ids field is prefilled with the output from the Do reload blocks. If you added or removed blocks, adjust the inputs.

   In this example you removed a block, so adjust your formula to look like this:

   ```
   {$.DoReload.id}, {$.DoReload2.id}
   ```

   Information note

   Use the formula parsing toggle to see the input field as a raw json object.
9. Select the Condition block. The condition is preconfigured to watch for a status = `failed` returned from any of the reload blocks. You can adjust this condition as needed. For this example, leave the condition as is.
10. Select the Output block. This block is executed on the YES branch of the condition. This means that if one of the reload blocks fails, the output block is executed. It is preconfigured with a message. For this example, leave the output as is.
11. Select the Error block. This block is preconfigured to stop the automation if a reload fails. For this example, leave the error as is.
12. The NO branch of the condition is empty. Add an Output block to this branch.
13. Clear the Data to output field and enter a reload successful message.

    "Your app reloads were successful!"
14. Click Save, then click Run.

With the removal of the reload block and the addition of an output block on the YES branch, this automation now looks like this:

Customizes parallel app reload automation from a template

![Parallel app reload automation from a template with added blocks](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/template-alter.png)

As the automation executes, the Output section in the History tab opens. You should see the message that corresponds to the status of the parallel app reloads.

Automation output

![Output window for automation showing message](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/template-historytab-output.png)
