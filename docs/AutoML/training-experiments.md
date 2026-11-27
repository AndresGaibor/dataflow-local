---
title: "Training experiments"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/training-experiments.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Working with experiments"]
---

# Training experiments

Training machine learning models means to feed data to algorithms and let them learn patterns in the data. After the initial training on the data, you will learn a lot about the models from the generated metrics. Expect it to take many iterations of refinement and retraining before you have a model that is good enough to deploy.

## Requirements and permissions

To learn more about the user requirements for working with ML experiments, see [*Working with experiments*](working-with-experiments.htm).

## Running experiment training

Do the following:

1. Create and configure a new experiment or open an experiment from the catalog.
2. Click Run experiment to start the training.

   (For the following versions, the button will say Run v2, Run v3, and so on.)

When the training is finished, the model metrics become available. You are now ready to review and refine the models. For more information, see [*Reviewing models*](reviewing-experiments.htm) and [*Refining models*](refining-models.htm).

## Managing training jobs

Tenant admins can stop or cancel experiment training jobs from the Administration activity center.
For more information, see [*Administering Qlik Predict*](../Admin/mc-managing-experiments-deployments.htm).

## Configuring notifications

You can receive notifications when the training of a single model is completed and when the training of all the models in an experiment version is completed. For more information, see [*Configuring notifications for Qlik Predict*](automl-customize-experience.htm#Configur).

## Handling failed experiment versions

If a version fails during training, it is listed in the Failed versions table in the Models tab. You can:

- View the error details to understand why training failed.
- Delete the failed version from the list.

For more information, see [*Viewing failed versions*](analyze-models-quick.htm#ViewingFailed).
