---
title: "Automating your data workflow"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Introduction/Automate-data-workflow.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data"]
---

# Automating your data workflow

You can create automations to create a data-driven workflow and rationalize your Qlik Talend Cloud deployment with Qlik Automate and the Data integration REST API.

- Orchestrate the tasks inside a pipeline project to give you more control over when particular tasks need to be run and allow you to insert other tasks based on conditions.
- Enable the scheduling of quality computations for datasets, streamlining data validation processes across your organization.
- Deploy pipeline projects across spaces.

For more information:

- [Qlik Automate](/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/introduction/home-automation.htm).
- [Data integration REST API](https://qlik.dev/apis/rest/di-projects/)

## Orchestrating tasks in a pipeline project

Create an automation in Qlik Automate using the Qlik Talend Data Integration connector. You can either start with a blank automation, or use the Start Data Integration tasks and wait for completion template.

[How to: Getting Started with the Qlik Talend Data Integration connector in Qlik Automate](https://customerportal.qlik.com/article/How-to-Getting-Started-with-the-Qlik-Talend-Data-Integration-connector-in-Qlik-Automate)

[Qlik Automate: Start multiple Qlik Talend Data Integration tasks and wait for their completion to start next task(s)](https://customerportal.qlik.com/article/Qlik-Automate-Start-multiple-Qlik-Talend-Data-Integration-tasks-and-wait-for-their-completion-to-start-next-task-s)

## Computing data quality

Create an automation in Qlik Automate using the Qlik Cloud Catalog connector. You can either start with a blank automation, or use the Schedule data quality computations template.

[How to get started with the Qlik Cloud Catalog connector in Qlik Automate](https://customerportal.qlik.com/article/How-to-get-started-with-the-Qlik-Cloud-Catalog-connector-in-Qlik-Application-Automation)

## Deploying a pipeline project

Deploy a pipeline project by exporting the project from a development data space and importing it into a production data space using the Data integration REST API .

[How to deploy Qlik Talend Cloud Pipelines across spaces using Qlik Automate](https://community.qlik.com/t5/Official-Support-Articles/How-to-deploy-Qlik-Talend-Cloud-Pipelines-across-spaces-using/ta-p/2531537)

[Data integration REST API: Deploy a data integration project](https://qlik.dev/manage/di-projects/deploy-di-project/)
