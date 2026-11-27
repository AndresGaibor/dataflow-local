---
title: "Meta (Amazon Bedrock) analytics source"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/ac-bedrock-meta-overview.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics", "Amazon Bedrock analytics sources"]
---

# Meta (Amazon Bedrock) analytics source

Use the Meta (Amazon Bedrock) analytics connector to communicate with Meta, enriching your Qlik Sense applications with contextual and analytical depth from generative AI and large language model (LLM) technology.

Information note

The Amazon Bedrock - Converse API connector allows you to connect to Amazon Bedrock's universal API for text generation models, including one or more models available through this connector. Consider replacing Anthropic (Amazon Bedrock) connections with Amazon Bedrock - Converse API connections for more advanced functionality. For more information, see [*Amazon Bedrock - Converse API analytics source*](ac-bedrock-converse-api-overview.htm).

With the Meta (Amazon Bedrock) analytics connector, you can send data from application consumer input, or from data loaded in your script, to Meta. You can connect to this analytics source from the Create page in the Analytics activity center, the Script, or within an application.

[Introducing  Llama](https://ai.meta.com/llama/)

## Prerequisites

To work with this connector, you must be an AWS user with an Access Key and Secret Key. You must also have the bedrock:invokemodel permission.

## Enabling ML endpoints in Qlik Cloud

To work with this connector, machine learning endpoints must be enabled in the Administration activity center. The switch is located under Feature control in the Settings section.

For more information, see [*Enabling analytic connections for machine learning endpoints*](load-data-from-advanced-analytic-connections.htm#Enabling).

## Limitations

- This connector has a request limit of 25 rows per request, with a maximum batch size of one row being sent at a time.
- The resources available on the services where the model has been deployed will impact and limit performance in the Qlik Sense reload and [chart](#glossary-0 "Glossary term") responsiveness.
- In a scenario where an application is regularly reloaded, it is best practice to cache the machine learning predictions using a [QVD](#glossary-1 "Glossary term") file and only send the new rows to the endpoint. This will improve the performance of the Qlik Sense application reload and reduce the load on the model endpoint.
- If you are using a relative connection name, and if you decide to move your application from a [shared space](#glossary-3 "Glossary term") to another shared space, or if you move your application from a shared space to your private space, then it will take some time for the analytic connection to be updated to reflect the new space location.
- You cannot create and manage connections to this connector in Data manager within an analytics application.

## Learn more

- [What is Amazon Bedrock?](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html)
