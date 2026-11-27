---
title: "Reviewing models"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/reviewing-experiments.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Working with experiments"]
---

# Reviewing models

In order to evaluate your machine learning models, you need to be able to make sense of the model scores and metrics. In some cases, understanding how each field and value influences the predicted outcome—why something happens—might be more important than making predictions.

## Workflow

When reviewing models, complete this step-by-step workflow for best results.

### Step 1: Understand the concepts

It can be helpful to have a basic understanding of the underlying concepts before you start reviewing your model metrics. In Qlik Predict, the model metrics are generally classified as:

- Model scores

  [*Interpreting model scores*](scoring-models.htm)
- Feature importance metrics

  [*Understanding feature importance*](feature-importance.htm)

In addition, there are a number of different algorithms available to train your models. For more information, see [*Understanding model algorithms*](algorithms.htm).

### Step 2: Use the interface to perform analysis

The next step is to use Qlik Predict to assess the results of the training. You can switch between the various tabs in the experiment interface to do the following:

- Review recommended models
- Inspect the training data to see how it was preprocessed during training
- View a summary of how Qlik Predict optimized your models by altering feature selection
- Perform high-level analysis of core model metrics
- Dig deeper with in-depth comparison and analysis of individual models

For full details, refer to the following guides:

- [*Selecting the best model for you*](best-models.htm)
- [*Performing quick model analysis*](analyze-models-quick.htm)
- [*Comparing models*](analyze-models-compare.htm)
- [*Performing detailed model analysis*](analyze-models-detailed.htm)

### Step 3: Refine the models as needed

After you have analyzed the models, you might want to deploy one of the recommended top-performing models. If further refinement is needed, you can create subsequent versions to improve upon the results.

Intelligent model optimization is activated by default in your experiment. This capability automatically refines models for you by excluding features which could impact model performance. Assuming you have a well-prepared dataset, the recommendations should be ready, or almost ready, for deployment.

You can alternatively start training without intelligent optimization, or turn it off after running one or more versions with it. This is useful if you need more control over the training process.

Additional refinement might be needed before or after model deployment. For example, you might need to retrain models after changing or refreshing the training data.

To learn more about how to refine models, see [*Refining models*](refining-models.htm).

After you have completed the refinement process, you are ready to deploy your preferred model.
