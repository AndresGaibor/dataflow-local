---
title: "Azure OpenAI"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/LLMConnections/connecting-azure-openAI.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections for knowledge marts", "Connecting  to LLM connections"]
---

# Azure OpenAI

Azure OpenAI offers coding and language AI models that you can fine-tune to your needs.

You must install Qlik Data Gateway - Data Movement. For more information, see [*Setting up Qlik Data Gateway - Data Movement for knowledge marts*](../../Gateways/gateways-for-knowledge-mart.htm).

## Preparing for authentication

To access your Azure OpenAI data, you need to authenticate the connection with your account credentials.

## Creating the connection

1. Fill in the required connection properties.
2. Provide a name for the connection in Name.
3. Click Test connection to verify the configuration.
4. When the test is successful, click Create.

Connection settings

| Setting | Description |
| --- | --- |
| Data gateway | You need a customer-managed data gateway. For more information, see [*Setting up Qlik Data Gateway - Data Movement for knowledge marts*](../../Gateways/gateways-for-knowledge-mart.htm). |
| Azure OpenAI endpoint | Your OpenAI API base URL. |
| API version | The OpenAI API version. |
| API Key | The OpenAI API key. |
