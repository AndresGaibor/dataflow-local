---
title: "OpenAI analytics source"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/ac-openai-overview.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics"]
---

# OpenAI analytics source

Use the OpenAI analytics connector to communicate with the interactive OpenAI platform, enriching your Qlik Sense applications with contextual and analytical depth from generative AI models, such as those which power ChatGPT.

With the OpenAI analytics connector, you can send data from application consumer input, or from data loaded in your script, to OpenAI. You can connect to this analytics source from the Create page in the Analytics activity center, the Script, or within an application.

[OpenAI](https://openai.com/product)

## Getting started with the OpenAI platform

Before you can use the OpenAI analytics connector in your Qlik Sense applications, you must complete the following preparatory steps. You must also enable machine learning endpoints in Qlik Cloud. See [*Enabling ML endpoints in Qlik Cloud*](#Enabling2).

Once you have completed these steps, you are ready to create a connection to the OpenAI analytics connector. For more information, see [*Creating an OpenAI connection*](ac-openai-create.htm).

### Creating a platform account

To use the OpenAI connector, you must have an OpenAI platform account. To create an OpenAI platform account, see [Welcome to the OpenAI platform](https://platform.openai.com). Note that this account is different from the ChatGPT account offered by OpenAI, and the two services, including billing, are separate.

Currently, accounts are provided with time-limited credit. After you use this credit, a paid account is required to use the OpenAI services. This commercial relationship is between you and OpenAI. Qlik simply facilitates the use of the APIs from within Qlik Cloud.

The use of the OpenAI API and the models provided from it are subject to the terms and conditions outlined by OpenAI. It is also important to consider the stability, accuracy, and safety best practices related to these services, many of which are documented on the OpenAI website.

### Generating an OpenAI API key

Once you have set up an OpenAI account, you need to generate an API key on their platform. To create and manage API keys for the OpenAI platform, see [API keys](https://platform.openai.com/account/api-keys).

The secret key that you generate will only be visible once, so it’s important to make a note of the key securely once it has been generated.

## Enabling ML endpoints in Qlik Cloud

To work with this connector, machine learning endpoints must be enabled in the Administration activity center. The switch is located under Feature control in the Settings section.

For more information, see [*Enabling analytic connections for machine learning endpoints*](load-data-from-advanced-analytic-connections.htm#Enabling).

## Limitations

- The OpenAI API enforces an endpoint quota and rate limiting, which are subject to the individual terms of your OpenAI account. More information can be found in the OpenAI API reference documentation. See [API reference](https://platform.openai.com/docs/api-reference).
- Usage of the OpenAI analytics connector will impact and limit performance in the Qlik Sense reload and chart responsiveness. The degree to which this performance is affected depends on your use case.
- The different configurations of this connector send data to the endpoint service with the following limits:

  - OpenAI Chat Completions API: Request limit of 25 rows per request, with a maximum batch size of one row being sent at a time.
  - OpenAI Embeddings: Request limit of 100k rows per request, with a maximum batch size of 1000 rows being sent at a time.
- In a scenario where an application is regularly reloaded, it is best practice to cache the machine learning predictions using a [QVD](#glossary-0 "Glossary term") file and only send the new rows to the endpoint. This will improve the performance of the Qlik Sense application reload and reduce the load on the model endpoint.
- If you are using a relative connection name, and if you decide to move your application from a [shared space](#glossary-2 "Glossary term") to another shared space, or if you move your application from a shared space to your personal space, then it will take some time for the analytic connection to be updated to reflect the new space location.
- You cannot create and manage connections to this connector in Data manager within an analytics application.

## Detailed examples

For examples of how to work with the OpenAI analytics connector, see [*Quick examples*](ac-openai-use.htm#Quick) and [*Tutorial – Using the OpenAI analytics connector in Qlik Cloud*](ac-openai-tutorial.htm).
