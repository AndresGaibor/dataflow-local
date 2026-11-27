---
title: "Hugging Face analytics source"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/ac-hugging-face-overview.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics"]
---

# Hugging Face analytics source

Use the Hugging Face analytics connector to communicate with Hugging Face, enriching your Qlik Sense applications with contextual and analytical depth from a large repository of machine learning models.

With the Hugging Face analytics connector, you can send data from application consumer input, or from data loaded in your script, to Hugging Face. You can connect to this analytics source from the Create page in the Analytics activity center, the Script, or within an application.

[Hugging Face](https://huggingface.co)

## Getting started with Hugging Face

Before you can use this analytics connector, you must complete the following preparatory steps.

### Create an account

Visit the official Hugging Face website to register for an account. After you have created the account, you can generate API keys and access other features on the platform.

### Generate an API token

To authenticate yourself on a Hugging Face connection, you must have an API token. To learn how to create and manage API tokens, refer to the Hugging Face website. You might need to do this through your account settings: [Access Tokens](https://huggingface.co/settings/tokens).

## Enabling ML endpoints in Qlik Cloud

To work with this connector, machine learning endpoints must be enabled in the Administration activity center. The switch is located under Feature control in the Settings section.

For more information, see [*Enabling analytic connections for machine learning endpoints*](load-data-from-advanced-analytic-connections.htm#Enabling).

## Limitations

- The different configurations of this connector send data to the endpoint service with the following limits:

  - Feature Extraction: Request limit of 40 rows per request, with a maximum batch size of 20 rows being sent at a time.
  - Question Answering: Request limit of 25 rows per request, with a maximum batch size of one row being sent at a time.
  - Summarization: Request limit of 40 rows per request, with a maximum batch size of 20 rows being sent at a time.
  - Sentence Similarity: Request limit of 10,000 rows per request, with a maximum batch size of 1000 rows being sent at a time.
  - Text Classification: Request limit of 40 rows per request, with a maximum batch size of 20 rows being sent at a time.
  - Text Generation: Request limit of 40 rows per request, with a maximum batch size of 20 rows being sent at a time.
  - Token Classification: Request limit of 40 rows per request, with a maximum batch size of 20 rows being sent at a time.
  - Translation: Request limit of 40 rows per request, with a maximum batch size of 20 rows being sent at a time.
- In a scenario where an application is regularly reloaded, it is best practice to cache the machine learning predictions using a [QVD](#glossary-0 "Glossary term") file and only send the new rows to the endpoint. This will improve the performance of the Qlik Sense application reload and reduce the load on the model endpoint.
- The resources available on the services where the model has been deployed will impact and limit performance in the Qlik Sense reload and [chart](#glossary-1 "Glossary term") responsiveness.
- When using Hugging Face connections in a chart expression it is recommended to provide the datatypes of the fields as the model needs to process these in the correct string/numeric format. A limitation of server side extensions in chart expressions is that the data types are not automatically detected as they are in the load script.
- If you are using a relative connection name, and if you decide to move your application from a [shared space](#glossary-3 "Glossary term") to another shared space, or if you move your application from a shared space to your private space, then it will take some time for the analytic connection to be updated to reflect the new space location.
- You cannot create and manage connections to this connector in Data manager within an analytics application.

## Learn more

- [Tasks](https://huggingface.co/tasks)
- [Models](https://huggingface.co/models)
