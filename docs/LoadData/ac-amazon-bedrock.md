---
title: "Amazon Bedrock analytics sources"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/ac-amazon-bedrock.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics"]
---

# Amazon Bedrock analytics sources

There are a number of analytic connectors in Qlik Sense for interacting with generative AI models available through the Amazon Bedrock platform. Use these connectors to load response data into your applications and scripts, or use them to configure chart expressions for real-time interaction with the models in a Qlik Sense sheet.

Information note

The Amazon Bedrock - Converse API connector allows you to connect to Amazon Bedrock's universal API for text generation models, including one or more models available through other Amazon Bedrock analytics connectors. For more advanced functionality, consider replacing existing connections with Amazon Bedrock - Converse API connections:

- AI21 Labs (Amazon Bedrock): All configurations
- Amazon Titan (Amazon Bedrock): Amazon - Titan Text G1 - Express configuration
- Anthropic (Amazon Bedrock): All configurations
- Cohere (Amazon Bedrock): Cohere - Generate configuration
- Meta (Amazon Bedrock): All configurations

For more information, see [*Amazon Bedrock - Converse API analytics source*](ac-bedrock-converse-api-overview.htm).

Amazon Bedrock is a platform hosted by Amazon Web Services which offers access to foundational models developed by Amazon and other external model providers.

[Amazon Bedrock](https://aws.amazon.com/bedrock/)

[What is Amazon Bedrock?](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html)

## Prerequisites

To work with these connectors, you must be an AWS user with an Access Key and Secret Key. You must also have the bedrock:invokemodel permission.

## Available connectors

The following analytic connectors are available for interactions with Amazon Bedrock. Each connector has its own documentation outlining connection parameters, limitations, and usage guidelines.

- [*AI21 Labs (Amazon Bedrock) analytics source*](ac-bedrock-ai21-overview.htm)
- [*Amazon Bedrock - Converse API analytics source*](ac-bedrock-converse-api-overview.htm)
- [*Amazon Titan (Amazon Bedrock) analytics source*](ac-bedrock-amazon-titan-overview.htm)
- [*Anthropic (Amazon Bedrock) analytics source*](ac-bedrock-anthropic-overview.htm)
- [*Cohere (Amazon Bedrock) analytics source*](ac-bedrock-cohere-overview.htm)
- [*Meta (Amazon Bedrock) analytics source*](ac-bedrock-meta-overview.htm)
