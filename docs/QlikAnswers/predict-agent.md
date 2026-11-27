---
title: "Working with machine learning in Qlik Answers"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/predict-agent.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Answers", "Using Qlik Answers and choosing your context"]
---

# Working with machine learning in Qlik Answers

You can work with Qlik Predict automated machine learning using the AI-powered technology of Qlik Answers.

In the agentic Qlik Answers experience, you can create and run machine learning workflows in natural language. You can explore datasets, configure and train experiments, and run predictions from the same chat experience.

This Qlik Answers experience is separate from accessing Qlik Predict capabilities through the Qlik MCP server in an external LLM client. For more information, see [*Qlik MCP server*](../QlikMCP/Qlik-MCP-server.htm).

Working with Predict in Qlik Answers

![Training ML experiment in agentic experience](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_answers_context_predict.png "Click to view full size")

Govnote-not-inNot supported in Qlik Cloud Government.

Govnote-not-inNot supported in Qlik Cloud Government - DoD.

## Before you begin

Prerequisites:

- Your [tenant](#glossary-0 "Glossary term") has cross-region inference turned on—that is, the tenant needs to be enabled for the agentic Qlik Answers experience.

  [*Enabling cross-region inference*](../Admin/cross-region-data-processing.htm)
- Your tenant and subscription have capacity for Qlik Answers and Qlik Predict.

  [*Qlik Answers capacity*](administering-qlik-answers.htm#Capacity)

  [*Monitoring Qlik Predict consumption for the subscription*](../Admin/mc-managing-experiments-deployments.htm#MonitorConsumption)
- You have access to the required datasets and Qlik Predict assets.

  [*Permissions*](#Permissions)

## Chatting with Qlik Predict in Qlik Answers

Do the following:

1. In the top bar, click Qlik Answers.

   The Qlik Answers chat opens.
2. In the dropdown menu, select Predict.

   Opening Predict

   ![Selecting the predict context in chat](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_answers-context-selector-predict.png "Click to view full size")
3. Select one of the available starter questions, or enter your own question.

   Information note

   Depending on your question, Qlik Answers may need to use a tool to generate the response, such as when running a prediction. Qlik Answers asks for approval the first time it needs to use a tool. You can choose to approve it once, approve it for all future requests, or deny the use of the tool.

   For more information, see [*Managing Qlik Answers tools*](qlik-answers-tools.htm).

## End-to-end workflows

Use the following workflows when working with Predict.

### Step 1: Dataset exploration and insights

Use dataset insights to understand data quality and candidate fields before training. Ask for insights and [target](#glossary-1 "Glossary term") recommendations.

You also do not need to know the exact name of the dataset you want to use—you can ask for a list of available datasets.

Example questions for dataset exploration and insights

| Action | Example questions | Notes |
| --- | --- | --- |
| Dataset selection | - Show me the available datasets for training - What datasets can I use for training? - List datasets | - |
| Dataset insights | - can you show me dataset insights for <dataset name> | Alternatively, you can first open the dataset in Qlik Cloud, and then ask questions such as:   - can you show me dataset insights for this dataset? - What features in this dataset have high cardinality |
| Target recommendation | - What column do you recommend to use as the target - What is your recommendation for the target - What column should the trained model predict | Useful as follow-up questions after selecting a dataset and exploring insights. |

### Step 2: Experiment training and monitoring

Describe your objective and let the agent configure and run an experiment. Regression, classification, and time series experiment types are supported. After you select a dataset and target, you are prompted to start training.

If you have already started a machine learning workflow previously, you can ask Predict to monitor existing experiments.

Example questions for experiment training and monitoring

| Action | Example questions | Notes |
| --- | --- | --- |
| Experiment training (with dataset already selected) | - I want to predict <column name> - Use <column name> as the target | Useful as follow-up questions after selecting a training dataset to use. |
| Experiment training (no dataset selected) | - Train models to predict <column name>; use <dataset name or a keyword> - Create an experiment with <dataset name or a keyword> data | These questions can help you get started directly without searching manually for datasets by name. |
| Experiment monitoring | - List my most recent experiments and their status - What is the status of my experiment | - |

### Step 3: Model interpretation and recommendations

After training completes, you can ask for plain-language interpretation of model behavior and recommendations based on model output. Charts are shown to help visualize model metrics and insights.

Example questions for model analysis

| Action | Example questions | Notes |
| --- | --- | --- |
| Model recommendations | - What is the best model in this experiment - I have the experiment <experiment name> open. What is the best model - I have the experiment <experiment name> open. Summarize the best model performance for a business audience | For best results, you need to either have the experiment open in your browser or reference the experiment name in the prompt. |
| Model metrics and insights | - What is the best model algorithm in this experiment - I have the experiment <experiment name> open. What are the metrics for the best model - Explore model insights and feature importance for this experiment - I have the experiment <experiment name> open. Which features have the strongest impact on this model? | For best results, you need to either have the experiment open in your browser or reference the experiment name in the prompt. |

### Step 4: Deployment, activation, and predictions

After training, you can deploy a model, creating an ML deployment. After you have asked to deploy a model, you are prompted to confirm the deployment.

You can also run [batch predictions](#glossary-2 "Glossary term") using the models you have deployed. The system searches for compatible [apply datasets](#glossary-3 "Glossary term") and lists them for you to choose. You can also use natural language prompts to select a specific apply dataset.

Deployed models are activated automatically as predictions are created, depending on the available capacity for the subscription.

Example questions for deployment and predictions

| Action | Example questions | Notes |
| --- | --- | --- |
| Model deployment and monitoring | - Deploy the best model for this experiment - I have the experiment <experiment name> open. View deployment details - Check deployment status for this experiment | Useful as follow-up questions directly after model analysis.  For best results, you need to either have the experiment open in your browser or reference the experiment name in the prompt. |
| Predictions—start the request | - Run predictions with this deployment - Run predictions with the deployment <deployment name> | For best results, you need to either have the deployment open in your browser or reference the deployment name in the prompt. |
| Predictions—selecting an apply dataset | - Use <apply dataset name> as the apply dataset for predictions with this deployment - I have the deployment <deployment name> open. Run predictions with <apply dataset name> dataset | For best results, you need to either have the deployment open in your browser or reference the deployment name in the prompt. |
| Predictions—monitor status | - Check batch prediction status for this deployment | For best results, you need to either have the deployment open in your browser or reference the deployment name in the prompt. |
| Predictions—explore prediction output | - I have the deployment <deployment name> open. Explore current prediction results - Show me my latest predictions for this deployment | For best results, you need to either have the deployment open in your browser or reference the deployment name in the prompt. |

## Best practices for asking questions

For best results when working with Qlik Predict in Qlik Answers, follow these general guidelines:

- If you are unsure of how to get started, ask Predict what it can do. Qlik Answers can provide a list of supported capabilities.
- Start a new conversation when changing topics, or if you are not getting the response you need.
- If you are not getting the required response, try providing more details and be specific about what you are looking to do. For example, referencing the exact names of datasets and other assets can better help Qlik Answers find them when starting training or running predictions.
- Rephrase your question if it does not return the response you need at first.

For more information, see [*Best practices for chatting with Qlik Answers*](best-practices-assistant-chat.htm).

## Permissions

You need both Qlik Answers and Qlik Predict permissions to complete end-to-end machine learning workflows.

Specifically, you need the following:

- Professional user entitlement (only applicable to user-based subscriptions)
- The required Agentic AI > Data analysis permission set to Allowed. This permission is assigned by a tenant admin.

  [*Managing user access to Qlik Answers*](administering-qlik-answers.htm#Access)
- The required Qlik Predict permissions for working with ML experiments and deployments, assigned to you by a tenant admin. See:

  - [*User access to ML experiments*](../AutoML/who-can-work-with-automl.htm#AccessExperiment)
  - [*User access to ML deployments and predictions*](../AutoML/who-can-work-with-automl.htm#AccessDeployment)
- Access to the spaces where the datasets, experiments, and deployments are located. See:

  - [*Shared space permissions for Professional and capacity-based subscription users*](../Spaces/permissions-shared-space-prof-full.htm)
  - [*Managed space permissions for Professional and capacity-based subscription users*](../Spaces/permissions-managed-space-prof-full.htm)

## Limitations

### Datasets

Updating and deleting datasets

You cannot upload or delete datasets from chat.

Changing datasets

The following are not possible in chat:

- Changing training datasets after running an experiment version.
- Running multiple predictions with different apply datasets within the same chat.

As a workaround, when you need to train experiments or run predictions using a different dataset, start a new chat first. If you are training experiments, this will also require creating a new experiment in the new chat.

For more information about starting new chats, see [*Chatting with Qlik Answers*](answering-questions-qlik-answers.htm#Chatting).

Large datasets

Chat does not support datasets that exceed any of the following limits for the Qlik Cloud tenant:

- Maximum dataset size (training datasets)
- Maximum dataset cell count (training datasets)
- Maximum number of included columns (training and apply datasets)

### Experiment features

The following experiment features are not supported when using Qlik Predict in Qlik Answers. They are still supported when using Qlik Predict through the user interface.

- Bias detection is not supported.
- It is not possible to analyze or download model training reports.
- It is not possible to access embedded analytics (Compare and Analyze tabs) for the experiment.
- All features and algorithms are selected for training when configuring the experiment. You cannot deselect features or algorithms. Further, intelligent model optimization is always used to train models—manual optimization is not supported.
- It is not possible to train second and subsequent versions of an experiment.

### Prediction types

Not available for [real-time](#glossary-4 "Glossary term") or connector-based predictions.

### ML model management

- You cannot replace an existing deployed model from chat.
- You cannot deploy multiple models from different experiment versions from chat.
- It is not possible to access embedded analytics (model operations and drift monitoring) for the deployment.

## Learn more

- [*Answering questions with Qlik Answers*](answering-questions-qlik-answers.htm)
- [*Machine learning with Qlik Predict*](../AutoML/home-automl.htm)
- [*Working with experiments*](../AutoML/working-with-experiments.htm)
- [*Working with ML deployments*](../AutoML/working-with-deployments.htm)
- [*Working with ML predictions*](../AutoML/working-with-predictions.htm)
- [*Using Qlik Answers and choosing your context*](choose-context.htm)
- [*Deploying and administering Qlik Answers*](administering-qlik-answers.htm)
- [*Enabling cross-region inference*](../Admin/cross-region-data-processing.htm)
