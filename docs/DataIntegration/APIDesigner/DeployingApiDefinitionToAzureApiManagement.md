---
title: "Deploying an API definition to Azure API Management"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/APIDesigner/DeployingApiDefinitionToAzureApiManagement.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing API contracts", "API Contracts Examples"]
---

# Deploying an API definition to Azure API Management

Use the API Contracts public
API to automatically update your API to Azure API Management.

This example explains how to import a new API definition or update an existing
one in Azure API Management from API Contracts.

![Diagram of the process where the API definition is fetched by the CI/CD pipeline from Qlik Talend Cloud and then pushed to Azure API Management.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/azure_api_management.png)

To do this, you must first fetch your API from Qlik Talend Cloud, then you
need to deploy it to Azure API Management using a command line script or a CI/CD
pipeline.

The following procedures use Microsoft PowerShell, but you can also use the Azure API
Management REST API.

For more information, see the following resources:

- [*Fetching an API definition for Azure API Management*](FetchingApiDefinitionForAzureApiManagement.htm)
- [Azure API Management documentation](https://docs.microsoft.com/en-us/azure/api-management/)
- [Microsoft PowerShell documentation](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-6)
- [Azure PowerShell API Management
  documentation](https://docs.microsoft.com/en-us/powershell/module/az.apimanagement/?view=azps-2.4.0#api_management)
- [Azure API Management REST API Reference](https://docs.microsoft.com/en-us/rest/api/apimanagement/)
