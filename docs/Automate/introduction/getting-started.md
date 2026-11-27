---
title: "Getting started"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/introduction/getting-started.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate"]
---

# Getting started

You don't need to configure or download anything to get started with Qlik Automate, but you need to authenticate the data connections you want to integrate to your workflow.

## How do automations work

An automation is a workflow made up of blocks. Some blocks run small basic processes, like receiving user input, printing output to the screen, or sending an email. Other blocks handle more advanced or specialized actions, like comparing lists or running batch loops. Data connector blocks send or receive data to and from cloud applications and data sources. Building an automation is as simple as ordering blocks into a logical workflow and configuring what each block does. Qlik Automate provides an easy-to-use visual layer to what is essentially a compiled script that makes API calls. When the automation is executed, it makes API calls for each block.

[Navigating the user interface](navigating-UI.htm)

## Who are automations for

Users with the Automation Creator role can create automations. Users can access their personal automations by selecting Analytics or Data Integration from the navigation menu ![Launcher menu](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_grid_menu.svg) and clicking Automations. Analytics admins and tenant admins can manage automations from the Administration activity center.

[Managing automations](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-managing-automations.htm)

## Where are automations created

The automation editor is available from the Analytics or Qlik Talend Data Integration [activity centers](#glossary-0 "Glossary term") by clicking **Automation** and then clicking Create automation.
The automation editor is the only place to create automations.

[Creating automations](creating-automation.htm)

## How to connect data sources

The benefit of automations is that you can create workflows that integrate multiple data sources. Many data source connectors are included with Qlik Automate, including the Qlik Cloud connector to integrate data directly from your analytics environment.

[Connector blocks](../connector-blocks/connectors-intro.htm)

## How to start automations

Automations can be started in different ways: manually, scheduled, triggered, or by a webhook. The run mode of the automation can be selected on the automation's Start block.

During service downtime, some triggered requests can be accepted for later processing.

[Working with run modes](../working-with-automations/working-with-runmodes.htm)

## Tutorials

If you want to get started right away, click the tutorials link below to see end-to-end example of the most common use cases for automations. These use cases are helpful if you want to implement out-of-the-box automations, or if you want to go through the steps of creating an automation.

[Tutorials](../tutorials/tutorials.htm)
