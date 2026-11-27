---
title: "Azure OpenAI analytics source"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/ac-azure-openai-overview.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics"]
---

# Azure OpenAI analytics source

Use the Azure OpenAI analytics connector to communicate with Microsoft's Azure OpenAI service, available within Azure's Cognitive Services. With this connector, you can enrich your Qlik Sense applications with contextual and analytical depth from generative AI models, such as those which power ChatGPT.

With the Azure OpenAI analytics connector, you can send data from your application's data model to the Azure OpenAI service. You can connect to this analytics source from the Create page of the Analytics [activity center](#glossary-0 "Glossary term") or within an application.

[What is Azure OpenAI Service?](https://learn.microsoft.com/en-us/azure/ai-services/openai/overview)

## Enabling ML endpoints in Qlik Cloud

To work with this connector, machine learning endpoints must be enabled in the Administration activity center. The switch is located under Feature control in the Settings section.

For more information, see [*Enabling analytic connections for machine learning endpoints*](load-data-from-advanced-analytic-connections.htm#Enabling).

## Limitations

- The APIs accessed through this connector enforce an endpoint quota and rate limiting, which are subject to the individual terms of your Microsoft Azure services.
- Usage of the Azure OpenAI analytics connector will impact and limit performance in the Qlik Sense reload and chart responsiveness. The degree to which this performance is affected depends on your use case.
- The different configurations of this connector send data to the endpoint service with the following limits:

  - OpenAI Completions API: Request limit of 25 rows per request, with a maximum batch size of 20 rows being sent at a time.
  - OpenAI Chat Completions API: Request limit of 25 rows per request, with a maximum batch size of one row being sent at a time.
- In a scenario where an application is regularly reloaded, it is best practice to cache the predictions using a QVD file and only send the new rows to the prediction endpoint. This will improve the performance of the Qlik Sense application reload and reduce the load on the endpoint.
- If you are using a relative connection name, and if you decide to move you application from a shared space to another shared space, or if you move your application from a shared space to your private space, then it will take some time for the analytic connection to be updated to reflect the new space location.
- You cannot create and manage connections to this connector in Data manager within an analytics application.
