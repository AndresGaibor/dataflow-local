---
title: "Connector blocks"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/connector-blocks/connectors-intro.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Blocks"]
---

# Connector blocks

Connectors let you access external data sources to integrate into your automation. Connectors are similar to the other automation blocks except that they require you to authenticate the connection. Each connector block makes a unique API call to the data source connector.

Information noteThe usage of third-party blocks in an automation run may incur additional costs depending on your type of subscription. Blocks for Qlik apps and services are not considered third-party blocks. For more information, see [Managing Automations](../../Sense_Hub/Admin/mc-monitoring-automations.htm#third-party-blocks).

In the Automation tab you can make use of the Third-party filter to show automations that includes third-party blocks while in the Runs tab you can use the Third-party filter to see automation runs that actually have used a third-party block while executing the automation workflow.

## Authenticating connectors

All connectors are available for all Qlik Automate, however, to use the connector in your automation you must be able to log in to authenticate it. There are two ways to authenticate.

On the [Create page](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikCloudNavigation/Analytics-activity-center.htm#anchor-2) in the Analytics Activity center, select the Automation Connection tile in the Data and Upload section to create a new connection. Alternatively, navigate to the Qlik Automate Connections page, select the connector and click Add new connection.

After you authenticate the connector, it is listed under Connections with a check mark that indicates the connector is authenticated. Connectors that are not yet authenticated are indicated with a cross mark.

Warning noteEditing an existing connection will trigger a reauthentication for connectors that use a password field for authentication, such as API keys or username and password.

Connections page

![Image of the Connections page showing a list of connectors. Authenticated connectors are indicated with a check mark. Unauthenticated connectors are indicated with a cross mark.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/connections.png)

From the Editor section, when you add a block to the canvas, there is a Connection tab on the block configuration pane that is highlighted in red. On this section, click Connect your connector button to authenticate.

Connecting a data source

![Connection section of configurator showing the connect your connector button](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/connections-canvas.png)

## Connectors

All of the connectors are available from the block selector pane. Connectors that are available are listed under Other Connectors. Authenticated connectors are listed under My Connectors. Connectors that are part of your current automation are listed under Connectors in use. Just like other blocks, drag a connector block onto the canvas and configure it from the block configuration pane.

The block selector pane

![The block selector pane showing the connectors sections](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/block-selector-pane-connectors.png)

Each connector includes many connector blocks, and each connector block corresponds to an API endpoint. When you add a connector block to the canvas, you can click Show API endpoint to see the method and URL this connector block uses to call the API server. Connector blocks are configured just like regular blocks. See [Block essentials](../introduction/block-essentials.htm) for details.

Tip note

For guides, tutorials, connector ideation, and connector troubleshooting, see [Qlik Community for Qlik Automate](https://community.qlik.com/t5/Qlik-Application-Automation/bd-p/qlik-application-automation-discussions).

## Qlik Cloud connector

The Qlik Cloud connector provides native Qlik Cloud integration to your automation. The connector blocks let you build powerful workflows with Qlik Cloud connectivity to do things like trigger reloads, create spaces, and publish apps.

Automation with Qlik Cloud blocks

![QCS automation example showing a reload task chain](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/QCS-automation.png)

## Qlik Reporting connector

The Qlik Reporting connector provides native Qlik reporting integration to your automation to create multi-sheet and customized reports. The Qlik Reporting connector blocks can be combined to build automations that generate reports based on sheets from apps. You can customize the report by applying different selections to specific sheets, or by configuring sheets to show alternate states. The report is generated as a PDF document, which you can distribute in a number of ways using other connector blocks.

Information note**Multi App Reports**

Use these blocks to create reports using data from multiple apps:

- Create Multi App Report
- Add Sheet to Multi App Report
- Add Selection to Sheet
- Generate Report

An automation that creates and generates a report

![Automation consisting of only reporting blocks](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/reporting.png)

Information note

Once a report is created using an automation, you can share the PDF document with anyone. This means you could potentially share data from an app that is not available to all users. Before creating and sending reports, make sure you understand the security implications of the app and data used to create the report.

To see more information about limitations, features, and use cases for reporting, see [Multi-sheet PDF reports via Qlik Automate](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Reports-with-application-automations.htm).

## Demo connectors

The set of available connectors includes two demo connectors. These connectors require authentication with a dummy API key, and they can be used for sample data or testing your workflow.

Automation with demo connector blocks

![CRM automation example with condition](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/crm-automation.png)
