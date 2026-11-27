---
title: "Enabling cross-region inference"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/cross-region-data-processing.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Configuring features and integrations"]
---

# Enabling cross-region inference

Expand/Collapse all

# Enabling cross-region inference

To provide the latest high-performing AI capabilities and help optimize performance, some Qlik Cloud AI features use models that are available only through cross-region inference. Enabling cross-region inference gives you access to AI features that may require inference processing in other regions.

## Overview

Each Qlik Cloud tenant is assigned to a specific geographic region. By default, your data is processed and stored within that region.

Enabling cross-region inference allows Qlik Cloud to temporarily send an inference request required for processing to the AWS region where the service is available, process the request there, and return the results. The request is only sent outside your designated tenant region if capacity is constrained or the model is not available in your tenant region. This gives you access to the latest AI capabilities and helps support a reliable user experience. Processing is transient and does not store or cache data in the processing region.

Warning noteEnabling cross-region inference allows your request to be temporarily sent outside your tenant region. By opting in, you confirm that you are authorized to enable this feature.

## Data protection

Although data may move between regions, it remains within the strict security and compliance boundaries of AWS. Cross-region inference uses encryption in transit and is governed by AWS security controls.

Your data will never be used to train third-party large language models (LLMs), and enabling cross-region inference does not give Qlik or AWS access to your data.

Qlik Cloud Government noteFor customers with tenants in the EU, an EU cross-region inference profile will always be selected. For Qlik Cloud Government and Qlik Cloud Government - DoD, all cross-region inference processing remains within AWS GovCloud (US) boundaries.

## Capabilities that require cross-region inference

The following features are only available when cross-region inference is enabled:

- Qlik Answers

  - The agentic experience requires cross-region inference. It includes:

    - Help Specialist
    - Qlik Answers for structured and unstructured analysis.
    - Tools for automated machine learning workflows with Qlik Predict.
    - Data governance tools for managing data products, glossaries, and data quality.

    For more information, see [*Qlik Answers*](../QlikAnswers/Qlik-Answers.htm).
  - You can continue to use the legacy Qlik Answers experience (the Q&A chatbot for unstructured data) within your tenant region without enabling cross-region inference.
    For more information, see [*Working with legacy assistants*](../QlikAnswers/Legacy/legacy-assistants.htm).
- Qlik Automate

  - AI-generated automation descriptions

    For more information, see [*AI-generated automation descriptions*](../../Sense_QlikAutomation/introduction/ai-generated-automation-descriptions.htm).
- Pipelines

  - AI SQL assistant

    For more information, see [*Generating a SQL transformation from a text prompt*](../DataIntegration/Transformation/Generating-SQL-from-text-prompt.htm).
  - AI model recommendations

    For more information, see [*Creating a data model*](../DataIntegration/Transformation/Create-data-model.htm).
  - AI suggested primary keys in SQL transformations

    For more information, see [*Adding SQL transformations*](../DataIntegration/Transformation/Adding-SQL-based-tables.htm).
- Data stewardship

  - Data remediation

    For more information, see [*Reviewing AI fixes in a resolution sprint*](../DataIntegration/DataStewardship/Reviewing-AI-suggestions.htm).
- API Designer

  - Generate contract

    For more information, see [Creating an API with AI Assistant](https://help.qlik.com/talend/en-US/api-designer-user-guide/Cloud/creating-a-new-api-with-ai-assistant) (Talend help).
- Data governance

  - AI data quality validation rule generation

    For more information, see [*Working with validation rules*](../DataIntegration/DataProducts/Working-with-validation-rules.htm).
  - AI-generated descriptions

    For more information, see [*Generating an AI-based description*](../DataIntegration/DataProducts/Generating-AI-based-description.htm).
- Discovery Agent

  - For more information, see [*Discovery Agent*](../DiscoveryAgent/discovery-agent.htm).
- Qlik Predict

  - AI recommendations for features on which to run bias detection (optional)

    Bias detection does not require cross-region inference. Using AI to recommend features is optional and performed before bias detection runs. You can still run bias detection without AI—that is, without cross-region inference—by manually selecting features on which to run bias detection.

    For more information, see [*Using generative AI to recommend features for bias detection*](../AutoML/bias-detection.htm#UsingAI).
  - Machine learning in Qlik Answers

    The agentic Qlik Answers experience supports training machine learning experiments, deploying models, and generating predictions.

    For more information, see [*Working with machine learning in Qlik Answers*](../QlikAnswers/predict-agent.htm#UsingAI).

The list of features that require cross-region inference may expand as new AI capabilities become available.

Information noteEnabling cross-region inference does not enable new AI features in your tenant. The AI features available in your tenant depend on your subscription and feature rollout in your tenant region.

## Inference processing locations

When processing inference requests for the capabilities listed above, multiple calls are made to AI models. These calls include inputs from the user, metadata, and data accessible within the tenant. Data transmitted to another region via cross-region inference does not persist. It is processed in real time and not stored in the processing region.

The tables below show inference processing locations for these calls for each tenant region. To receive notifications of updates, subscribe to the [Qlik Cross Region Inference](https://community.qlik.com/t5/Official-Support-Articles/Qlik-Cross-Region-Data-Processing/ta-p/2541184) article in Qlik Community.

### How to subscribe to the article in Qlik Community

Do the following:

1. Sign in to Qlik Community with your account.
2. Go to [Qlik Cross Region Inference](https://community.qlik.com/t5/Official-Support-Articles/Qlik-Cross-Region-Data-Processing/ta-p/2541184).
3. Click the vertical ellipsis (three dots) next to the article title.
4. Select Subscribe from the menu.

You will receive notifications when the article is updated.

### Qlik Answers inference processing locations

The following table lists the inference processing locations for Qlik Answers for each tenant region, along with the applicable time periods.

Qlik Answers inference processing locations

Processing locations and effective dates for Qlik Answers

| Qlik tenant region | Processing locations | Effective from | Effective to |
| --- | --- | --- | --- |
| **Australia**  ap.qlikcloud.com | Australia, India, Japan, South Korea, Singapore | 2/10/2026 | To be determined |
| **Brazil**  br.qlikcloud.com | United Arab Emirates, Australia, Bahrain, Brazil, Canada, Switzerland, United Kingdom, Hong Kong, Indonesia, Israel, India, Japan, South Korea, Mexico, Malaysia, New Zealand, Singapore, Thailand, Taiwan, South Africa, EU member states, United States of America | 5/26/2026 | To be determined |
| **Canada**  ca.qlikcloud.com | Canada, United States of America | 6/22/2026 | To be determined |
| **Germany**  de.qlikcloud.com | EU member states | 2/10/2026 | To be determined |
| **United Kingdom**  uk.qlikcloud.com | United Kingdom, EU member states | 2/10/2026 | To be determined |
| **Ireland**  eu.qlikcloud.com | EU member states | 2/10/2026 | To be determined |
| **India**  in.qlikcloud.com | Australia, India, Japan, South Korea, Singapore | 2/10/2026 | To be determined |
| **Japan**  jp.qlikcloud.com | Australia, India, Japan, South Korea, Singapore | 2/10/2026 | To be determined |
| **Singapore**  sg.qlikcloud.com | Australia, India, Japan, South Korea, Singapore | 2/10/2026 | To be determined |
| **United States of America**  us.qlikcloud.com | United States of America | 2/10/2026 | To be determined |

### Inference processing locations for Pipelines, Qlik Automate, API Designer, and Data governance

The following table lists the inference processing locations for Pipelines, Qlik Automate, API Designer, and Data governance AI for each tenant region, along with the applicable time periods.

Information noteAI-generated automation descriptions are currently not available for tenants in the `il-central-1` region.

Warning noteFor processing locations for data governance tools in Qlik Answers, refer to [*Qlik Answers inference processing locations*](#QlikAnswersLocations).

Inference processing locations for Pipelines, Qlik Automate, API Designer, and Data governance

Processing locations and effective dates for Pipelines, API Designer, and Data governance

| Qlik tenant region | Processing locations | Effective from | Effective to |
| --- | --- | --- | --- |
| **Australia**  ap.qlikcloud.com | Australia, India, Japan, South Korea, Singapore | 2/10/2026 | To be determined |
| **Brazil**  br.qlikcloud.com | United Arab Emirates, Australia, Bahrain, Brazil, Canada, Switzerland, United Kingdom, Hong Kong, Indonesia, Israel, India, Japan, South Korea, Mexico, Malaysia, New Zealand, Singapore, Thailand, Taiwan, South Africa, EU member states, United States of America | 5/26/2026 | To be determined |
| **Germany**  de.qlikcloud.com | EU member states | 2/10/2026 | To be determined |
| **France**  fr.qlikcloud.com | EU member states | 2/10/2026 | To be determined |
| **United Kingdom**  uk.qlikcloud.com | United Kingdom, EU member states | 2/10/2026 | To be determined |
| **Ireland**  eu.qlikcloud.com | EU member states | 2/10/2026 | To be determined |
| **India**  in.qlikcloud.com | Australia, India, Japan, South Korea, Singapore | 2/10/2026 | To be determined |
| **Japan**  jp.qlikcloud.com | Australia, India, Japan, South Korea, Singapore | 2/10/2026 | To be determined |
| **Singapore**  sg.qlikcloud.com | Australia, India, Japan, South Korea, Singapore | 2/10/2026 | To be determined |
| **United States of America**  us.qlikcloud.com | United States of America | 2/10/2026 | To be determined |

### Inference processing locations for Discovery Agent

The following table lists the inference processing locations for Discovery Agent for each tenant region, along with the applicable time periods.

Warning noteWhen using Qlik Answers to explore Discovery Agent insights, processing locations for Qlik Answers are also used. See [*Qlik Answers inference processing locations*](#QlikAnswersLocations).

Inference processing locations for Discovery Agent

Processing locations and effective dates for Discovery Agent

| Qlik tenant region | Processing locations | Effective from | Effective to |
| --- | --- | --- | --- |
| **Australia**  ap.qlikcloud.com | Australia, India, Japan, South Korea, Singapore | 2/10/2026 | To be determined |
| **Brazil**  br.qlikcloud.com | United Arab Emirates, Australia, Bahrain, Brazil, Canada, Switzerland, United Kingdom, Hong Kong, Indonesia, Israel, India, Japan, South Korea, Mexico, Malaysia, New Zealand, Singapore, Thailand, Taiwan, South Africa, EU member states, United States of America | 5/26/2026 | To be determined |
| **Canada**  ca.qlikcloud.com | Canada, United States of America | 6/22/2026 | To be determined |
| **Germany**  de.qlikcloud.com | EU member states | 2/10/2026 | To be determined |
| **United Kingdom**  uk.qlikcloud.com | United Kingdom, EU member states | 2/10/2026 | To be determined |
| **Ireland**  eu.qlikcloud.com | EU member states | 2/10/2026 | To be determined |
| **India**  in.qlikcloud.com | Australia, India, Japan, South Korea, Singapore | 2/10/2026 | To be determined |
| **Japan**  jp.qlikcloud.com | Australia, India, Japan, South Korea, Singapore | 2/10/2026 | To be determined |
| **Singapore**  sg.qlikcloud.com | Australia, India, Japan, South Korea, Singapore | 2/10/2026 | To be determined |
| **United States of America**  us.qlikcloud.com | United States of America | 2/10/2026 | To be determined |

### Inference processing locations for Qlik Predict

The following table lists locations where inference requests may be processed for optional usage of large language models (LLMs) during bias detection in ML experiments. The locations are listed for each tenant region, along with the applicable time periods.

Warning noteFor processing locations for Qlik Predict in Qlik Answers, refer to [*Qlik Answers inference processing locations*](#QlikAnswersLocations).

Inference processing locations for bias detection in Qlik Predict

Processing locations and effective dates—AI recommendations for Qlik Predict bias detection

| Qlik tenant region | Processing locations | Effective from | Effective to |
| --- | --- | --- | --- |
| **Australia**  ap.qlikcloud.com | Australia, India, Japan, South Korea, Singapore | 2/10/2026 | To be determined |
| **Brazil**  br.qlikcloud.com | United Arab Emirates, Australia, Bahrain, Brazil, Canada, Switzerland, United Kingdom, Hong Kong, Indonesia, Israel, India, Japan, South Korea, Mexico, Malaysia, New Zealand, Singapore, Thailand, Taiwan, South Africa, EU member states, United States of America | 5/26/2026 | To be determined |
| **Canada**  ca.qlikcloud.com | Canada, United States of America | 6/22/2026 | To be determined |
| **Germany**  de.qlikcloud.com | EU member states | 2/10/2026 | To be determined |
| **United Kingdom**  uk.qlikcloud.com | United Kingdom, EU member states | 2/10/2026 | To be determined |
| **Ireland**  eu.qlikcloud.com | EU member states | 2/10/2026 | To be determined |
| **India**  in.qlikcloud.com | Australia, India, Japan, South Korea, Singapore | 2/10/2026 | To be determined |
| **Japan**  jp.qlikcloud.com | Australia, India, Japan, South Korea, Singapore | 2/10/2026 | To be determined |
| **Singapore**  sg.qlikcloud.com | Australia, India, Japan, South Korea, Singapore | 2/10/2026 | To be determined |
| **United States of America**  us.qlikcloud.com | United States of America | 2/10/2026 | To be determined |

## Enabling cross-region inference

As a tenant administrator, you can turn cross-region inference on or off.

### What happens when you enable cross-region inference

When you enable cross-region inference, permission settings for AI features become visible and adjustable in the Administration activity center.

For the AI capabilities listed above that require cross-region inference, the following permissions are set to Not allowed by default:

- Data analysis: Analyze data and create charts with Qlik Answers.
- Qlik product help: Use Qlik Answers to find relevant product documentation.
- Data governance: Use Qlik Answers to work with data governance, including building glossaries, monitoring data quality, and managing data products.

Use default permissions and custom roles to configure these permissions under Features and actions > Agentic AI. You can control access to these features by adjusting the relevant permission settings.

Access to AI features in Pipelines, API Designer, and Data governance is controlled by the standard permissions for those areas, such as dataset permissions and pipeline build permissions.

### Prerequisite for enabling cross-region inference

Before you enable cross-region inference, make sure that the Data analysis and Data governance permission (under Agentic AI) are set to Not allowed in the following locations:

- Default permissions
- Any custom roles that include this permission

### Enable cross-region inference

Do the following:

1. In the Administration activity center, go to Settings > AI features.
2. Under AI features in Qlik, turn on Enable cross-region inference.
3. In the confirmation dialog, select the checkbox to confirm that you are authorized to enable cross-region inference, and then click Confirm.
4. On the next page, click Submit to apply the changes.

### Control access to AI features

After you enable cross-region inference, you can control which users have access to each AI feature. Access to AI features is controlled by manually configured user role permissions.

#### Controlling access for all users

To control access for all users in a tenant, set the default permissions.

1. In the Administration activity center, go to Manage users > Permissions, and click Manage default permissions.
2. Select Features and actions.
3. For access to Qlik Answers agentic AI, under the Agentic AI section, set the following permissions to Allowed:

   - Data analysis: This provides access to Qlik Answers to analyze data, create charts, and gather insights from documents.
   - Qlik product help: (Optional) This allows users to access Qlik Answers for product documentation guidance.
4. For access to generating AI-based descriptions and suggestions, under Data quality, set the following permissions to Allowed:

   - AI-based descriptions and suggestions: This allows users to create AI-based dataset descriptions to quickly add a precise description to a dataset.

#### Controlling access for specific users

To allow only specific users or groups to use an AI feature, use custom user roles. For more information, see [*Managing custom roles*](permissions-custom-roles-capacity-model.htm).

1. In the Administration activity center, go to Manage users > Permissions.
2. Select an existing custom role or create a new custom role.
3. Select Features and actions.
4. For access to Qlik Answers agentic AI, under the Agentic AI section, set the following permissions to Allowed:

   - Data analysis: This provides access to Qlik Answers to analyze data, create charts, and gather insights from documents.
   - Qlik product help: (Optional) This allows users to access Qlik Answers for product documentation guidance.
   - Data governance: This provides access to tools for working with data governance.
5. For access to generating AI-based descriptions and suggestions, under Data quality, set the following permissions to Allowed:

   - AI-based descriptions and suggestions: This allows users to create AI-based dataset descriptions to quickly add a precise description to a dataset.
6. Assign the role to the users or groups you want to allow.

### Turn off cross-region inference

Before you turn off cross-region inference, you must set all related AI feature permissions—such as Data analysis, Data governance, and Qlik product help—to Not allowed in the following locations:

- Default permissions
- Any custom roles that include these permissions

Alternatively, you can remove any custom roles that contain these permissions.
