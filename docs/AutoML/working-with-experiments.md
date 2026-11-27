---
title: "Working with experiments"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/working-with-experiments.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict"]
---

# Working with experiments

Load historical data into an automated machine learning experiment and train a model to analyze and predict a business problem.

You can create and edit experiments in personal or shared spaces.

## Workflow

Before you create an automated machine learning experiment in Qlik Cloud Analytics, you need to have a well-defined machine learning question and a suitable training dataset available in Catalog. For more information, see [*Defining machine learning questions*](machine-learning-framework.htm) and [*Getting your dataset ready for training*](dataset-preparation.htm).

The following steps describe an experiment workflow.

1. Create your experiment

   Create a new experiment in Qlik Cloud. Add it to a shared space if you want to work collaboratively.

   [*Creating experiments*](creating-experiments.htm)
2. Configure your experiment

   Select a target to make predictions on and features to support the prediction.

   [*Configuring experiments*](configuring-experiments.htm)
3. Start the training

   Start the training of your first experiment version.

   [*Training experiments*](training-experiments.htm)
4. Review recommended models

   Review how the model training went and assess the models that have been recommended to you. Use the built-in tools to analyze training summaries and embedded analytics, which offer insights at the experiment, version, and model level.

   [*Reviewing models*](reviewing-experiments.htm)

   If further refinement is needed, you can configure subsequent versions of the experiment. Adjust parameters such as features and algorithms and retrain new versions of the experiment until you have a good model.

   [*Refining models*](refining-models.htm)
5. Deploy the model

   When you have a good model, it’s time to deploy it and start making predictions.

   [*Working with ML deployments*](working-with-deployments.htm)

## Requirements and permissions

For information about the required space roles for working with ML experiments in shared spaces, see:

- [*Shared space permissions for Professional and capacity-based subscription users*](../Spaces/permissions-shared-space-prof-full.htm)
- [*Shared space permissions for administrators*](../Spaces/permissions-shared-space-admin.htm)

If you are an administrator, see [*Who can work with Qlik Predict*](who-can-work-with-automl.htm) for a comprehensive overview of the required user permissions for working with ML experiments.

## Viewing lineage and impact analysis

Using the Lineage and Impact analysis tools in Qlik Cloud, you can analyze:

- The origins of an ML experiment and the data used to train each model.

  [*Analyzing lineage for machine learning content*](../Catalog/lineage.htm#MLLineage)
- How the ML experiment and its outputs are being used in downstream content across Qlik Cloud.

  [*Impact analysis for machine learning content*](../Catalog/impact-analysis2.htm#MLImpact)
