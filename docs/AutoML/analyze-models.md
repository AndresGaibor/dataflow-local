---
title: "Analyzing models"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/analyze-models.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Working with experiments", "Reviewing models"]
---

# Analyzing models

Qlik Predict provides a rich visual experience for analyzing the models you train in your experiment. You can analyze key model metrics using a simple interface that includes auto-generated recommendations, summaries, and visualizations. For more detailed analysis and comparisons, you can use embedded analytics.

## Before you start

Before analyzing models, it can be helpful to have a basic understanding of the model review concepts. This includes the model scores, feature importance, and algorithms.

For information, see [*Understanding model review concepts*](model-review-concepts.htm).

## Quick analysis

With quick analysis, you can quickly gain understanding about how the model training went, and about the quality of the resulting models. You can also review which models are recommended to you based on common requirements.

Before diving into the analysis, it is recommended that you open the Training data tab to see how the training data was handled. This can be important, since features may have been found to be unusable in the version.

Open the Models tab in the experiment for an overview of the training results. You can quickly compare the models and identify the top performers. The information you see in this tab depends on whether you are using Intelligent model optimization, as well as the problem type for your experiment.

For more information, see:

- [*Performing quick model analysis*](analyze-models-quick.htm)
- [*Selecting the best model for you*](best-models.htm)

## Model comparison

Use embedded analytics to perform interactive, in-depth comparison of your models. You can perform these comparisons in the Compare tab.

During model comparison, you can:

- Compare all available model metrics for all models.
- View and compare training and holdout scores for all models.
- Compare hyperparameter values across all models.

For a comprehensive guide, see [*Comparing models*](analyze-models-compare.htm).

## Detailed analysis

In the Analyze tab of the experiment, perform detailed analysis of a specific model. Detailed analysis is performed with embedded analytics. You can interactively filter the data to gain a better understanding of model performance for specific clusters of data.

With detailed model analysis, you can identify issues caused by training data and learn more about a model's strengths and weaknesses.

For a comprehensive guide, see [*Performing detailed model analysis*](analyze-models-detailed.htm).

## Downloading training reports

For additional details, you can download training reports for models in your experiment. A training report provides an in-depth summary of how a model was trained, providing comprehensive details about preprocessing, feature transformations, experiment versioning, and model metrics. Training reports are exported directly to your local machine.

For more information, see [*Downloading ML training reports*](training-report.htm).

## Next steps

Your next steps can depend on how you are optimizing your models.

Intelligent model optimization ideally creates a model that is ready to deploy with minimal or no further refinement. The quality of the models still depends on the quality of your training data, experiment configuration, and any requirements specific to your predictive use case. After you have analyzed the models and addressed any other issues with data quality or experiment configuration, you are ready to deploy the model that is best suited to your requirements.

If you identify further issues after running intelligent model optimization, or if you have turned off intelligent model optimization from the start, you can manually configure new versions of the experiment to improve the resulting models.

Examples of refinement steps include:

- Turning on intelligent optimization after starting without it.
- Turning off intelligent optimization after running a version with it. This allows you to make tweaks to the configuration as needed.
- Changing or refreshing the training data.
- Changing the included features.
- Changing the handling of feature data (for example, changing the feature type of a feature).

When you have achieved the desired results, deploy one or more models. For more information, see:

- [*Refining models*](refining-models.htm)
- [*Deploying models*](deploying-models.htm)
