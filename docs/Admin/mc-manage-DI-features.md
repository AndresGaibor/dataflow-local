---
title: "Configuring Data Integration features"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-manage-DI-features.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Configuring features and integrations"]
---

# Configuring Data Integration features

You can enable features in Data Integration as a [tenant admin](#glossary-0 "Glossary term").

All settings are available in the Administration activity center, on the Feature control tab of the Settings page.

## Viewing data in Data Integration

You can enable viewing data to be able to preview the results of Data Integration pipeline tasks. When enabled, only users with the relevant roles in a data space can view data in that data space.

## Generative AI-based assistant in Data Integration

You can activate generative AI-based assistants to have your dataset metadata details processed by a third-party GenAI model. Your data will not be used for training the model. For more details on features, use cases and metadata used, see:

- [*Generating a SQL transformation from a text prompt*](../DataIntegration/Transformation/Generating-SQL-from-text-prompt.htm)
- [*Creating a data model*](../DataIntegration/Transformation/Create-data-model.htm)

Information note

To use generative AI-based assistants, you must opt in to cross-region inference. This allows Qlik Cloud to send inference requests outside your tenant region.

For details and the latest information about inference processing locations, see [*Enabling cross-region inference*](cross-region-data-processing.htm).

AI model recommendations

### Availability

The GenAI model is hosted on AWS Bedrock Anthropic in the same region as the Qlik Cloud tenant. Generative AI-based assistants are available on tenants in the following Qlik regions:

- US East (North Virginia)
- Asia Pacific (Mumbai)
- Asia Pacific (Singapore)
- Asia Pacific (Sydney)
- Asia Pacific (Tokyo)
- Europe (Frankfurt)
- Europe (Ireland)
- Europe (London)

Govnote-not-inNot supported in Qlik Cloud Government.

### Information that is shared

Text prompts and dataset information are sent to a third party generative AI (GenAI) model. The information is treated as customer data and will not be used to train Qlik Cloud or the GenAI model on AWS Bedrock.

The following information is shared with the Generative AI model:

- Text prompts
- Additional generation instructions to adapt the query to your target data platform.

  Example: Generate a SQL query in a Snowflake-compatible syntax
- Dataset names and descriptions.
- Column names, data types and sizes.
- Primary key columns(unique identifiers).
- Relationships between datasets

  Example: "order\_detail" is attached to "order" using the "order\_id" key.

## Generative AI-based description assistant

You can activate generative AI-based description assistant to have your dataset and data product description processed by a third-party GenAI model. Your data will not be used for training the model. For more information, see [*Generating an AI-based description*](../DataIntegration/DataProducts/Generating-AI-based-description.htm).

Govnote-not-inNot supported in Qlik Cloud Government.
