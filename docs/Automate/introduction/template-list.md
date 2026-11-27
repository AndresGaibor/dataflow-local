---
title: "All templates"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/introduction/template-list.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Getting started", "Using templates"]
---

# All templates

Qlik Automate templates allow you to automate a variety of tasks and workflows. The templates are preconfigured, easily customizable and quick to implement. This topic provides an overview on the available templates and areas in which they can be used.

Some of the common business workflows that templates are used for include:

- Automatically reload your apps.
- Trigger alerts and messages on common communication platforms.
- Manage your master items across apps.
- React to reload failures.
- Backup apps to external storage locations.
- Build customized, multi-page reports based on app sheets.

Information note

To see how the Qlik Community is using automation templates, see [Qlik Automate](https://community.qlik.com/t5/tag/Automation%20template/tg-p/board-id/qlik-support-knowledge-base).

Information noteThe usage of third-party blocks in an automation run may incur additional costs depending on your type of subscription. Blocks for Qlik apps and services are not considered third-party blocks. For more information, see [Managing Automations](../../Sense_Hub/Admin/mc-monitoring-automations.htm#third-party-blocks).

## App Installers

Automate app installation.

- Qlik Data Capacity Reporting App Deployer
  - This template can be scheduled to deploy the Data Capacity Reporting App to a Qlik Cloud tenant. The Data Capacity Reporting App provides detailed usage information for your Qlik Cloud capacity-based subscriptions. Refreshed data is available once per day in the morning, Central European time. Requires the Tenant Admin role to run.

    - To learn more, see this Qlik [Community article](https://community.qlik.com/t5/Official-Support-Articles/Automate-deployment-of-the-Data-Capacity-Reporting-app-with-Qlik/ta-p/2529176).
- Qlik Cloud Monitoring Apps Deployer
  - This template is an automated installer and maintainer for the Qlik Cloud Monitoring Applications, such as the App Analyzer, Reload Analyzer, and Automation Analyzer. Use this template to easily install and update your monitoring apps and their dependencies. This template replaces the deprecated Qlik Cloud Monitoring Apps Installer and Qlik Cloud Monitoring Apps API Key Rotator templates.

    - To learn more, see this Qlik[Community article](https://community.qlik.com/t5/Official-Support-Articles/Qlik-Cloud-Monitoring-Apps-Workflow-Guide/ta-p/2134140).
- Qlik Snowflake Monitoring Apps Installer
  - This automation template is a fully guided installer/updater for the Qlik Snowflake Monitoring application. Leverage this automation template to quickly and easily install and update this application, and follow the community guide to complete configuration.

    The applications themselves are community supported, however, they are provided through Qlik's Open-Source Software GitHub and thus are subject to Qlik's open-source guidelines and policies.

    - To learn more, see this Qlik [Community article](https://community.qlik.com/t5/Official-Support-Articles/Installing-the-Qlik-Snowflake-Monitoring-application-in-Qlik/ta-p/2455224).
    - Visit Qlik's open-source organization on [GitHub](https://github.com/qlik-oss).
    - Refer to [this repository](https://github.com/qlik-oss/qlik-snowflake-monitor) for license information.
    - Support varies per component:

      - The installer automation is supported by Qlik Support.
      - The application is supported by the community, and not by Qlik. For support information, see [here](https://github.com/qlik-oss/qlik-snowflake-monitor).

## Agentic Actions

Automate agentic actions triggered from Qlik experiences.

- Send a Message to a Slack Channel as an Action

## AI Assisted

Automate AI-assisted troubleshooting workflows.

- Diagnose failed analytics app reloads with AI and notify your team on Slack

## Alerting

Automate alerts and notifications.

- Alert API key owners about API key expiration within x number of days
- Alert app owners about apps that haven't been accessed in the last 28 days
- Alert app owners about apps without reloads in the past X days
- Alert app owners and Tenant Admins about orphaned data connections
- Create a Slack channel when Jira tickets update
- Diagnose failed analytics app reloads with AI and notify your team on Slack
- Notify your team on Microsoft Teams based on a measure
- Notify your team on Microsoft Teams with data from multiple apps
- Notify your team on Slack on app reload finished webhook
- Reload an app and notify your team on Slack
- Send email with attachment from Dropbox
- Send straight table data to email as a table
- Send straight table data to Microsoft Teams as a message
- Send straight table data to Microsoft Teams as a table
- Update a variable with data from a URL

## Analytics Data Pipeline

Automate Qlik Sense task notifications, app reloads, and improvements to your QVD data loads.

- Copy and update data from a Qlik Sense straight table to an Excel sheet
- Copy data from a Qlik Sense straight table to an Excel sheet
- Create a ServiceNow incident when reload fails
- Notify your team on Slack on app reload finished webhook
- Notify your team with a link to an app with active selections
- Reload an app and notify your team on Slack
- Reload app and retry if reload fails
- Reload apps as a task chain
- Reload apps in parallel
- Send straight table data to email as a table
- Split QVDs to improve reloads

## App to App Integration

Create automated integrations for third-party apps.

- Create a Slack channel when Jira tickets update
- Send email with attachment from Dropbox
- Sync HubSpot contacts to Salesforce

## Change Control

Automate change and version control tasks.

- Commit an app to GitHub
- Do app evaluation and publish app
- Export an app to a shared space a s a backup
- Export automation to GitHub
- Import an app from a file on Amazon S3
- Import an app from GitHub
- Import automation from GitHub
- Recover a soft-deleted analytics application
- Scheduled app export to an Amazon S3 bucket (without data)
- Set load script in Qlik Sense app from merged GitHub pull request
- Store a straight table as a .csv file on Amazon S3
- Verify load script in Qlik Sense app from new GitHub pull request

## Data Integration

Automate moving Data Integration tasks.

- Start Data Integration tasks and wait for completion
- Schedule data quality computations

## Insights to Action

Automate Write Table extraction tasks.

- Extract Change Store Data to a MySQL Database
- Extract Change Store Data to a MySQL Database in Bulk

## Machine Learning

Predict churn, deal probability, and analyze support tickets.

- Predict customer churn risk with Qlik Predict
- Predict deal win probability with Qlik Predict

## Master Item Management

Easily import, export and distribute master items.

- Distribute measures from one app to all apps in a space
- Export master items to an Excel workbook
- Import master items from an Excel workbook

## Migration to Qlik Cloud

Automate moving data from QlikView or Qlik Sense

- Generate dynamic QVDs from QlikView or Qlik Sense on Windows apps

## Reporting

Automate report creation and distribution.

- Embed a chart image in an email
- Send a burst report to email recipients from a straight table
- Send a burst report to email recipients from an Excel file
- Send a chart image to Slack
- Send a simple multi-page report by email
- Store a simple multi-page PowerPoint report to Microsoft SharePoint
- Store a report with a cover sheet and cycled pages in Dropbox
- Store cycled reports in Dropbox
- Store cycled reports in SharePoint
- Store multi-app report to Microsoft SharePoint

## Tenant Administration

Keep track of automations, logs, and expiring server licenses.

- Alert API key owners about API key expiration within x number of days
- Alert app owners about apps without reloads in the past X days
- Alert app owners and Tenant Admins about orphaned data connections
- Alert app owners about apps that haven't been accessed in the last 28 days
- Alert on automations without runs in the last X days
- Alert on failed automation in the last X days
- Alert Qlik Talend Data Integration server license expiring within X days
- Incrementally export audit trail logs from Qlik Enterprise Manager to Splunk
- Qlik Cloud Monitoring Apps API Key Rotator
- Qlik Cloud Monitoring Apps Installer
- Recover a soft-deleted analytics application
