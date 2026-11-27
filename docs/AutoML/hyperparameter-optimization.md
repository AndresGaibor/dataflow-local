---
title: "Hyperparameter optimization"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/hyperparameter-optimization.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Working with experiments", "Configuring experiments", "Working with model optimization"]
---

# Hyperparameter optimization

Machine learning models require different constraints, weights, or learning rates to generalize different data patterns. These measures are called hyperparameters and are used to control the learning process. The hyperparameters need to be tuned so that the model can optimally solve the machine learning problem.

By default, Qlik Predict uses a predefined set of hyperparameter values for each algorithm used in model training. These are the standard, optimized values that are generally accepted by the data science community. The top-performing combination of hyperparameter values are automatically selected.

However, in some cases, you might want to fine-tune the model for optimal predictive results. This can be done using hyperparameter optimization (HPO).

Qlik Predict runs hyperparameter optimization only for the best algorithm of the set you selected in the experiment configuration. First, a random search is run, and then a grid search to find the best hyperparameters for the algorithm.

There are a few important things to consider before using hyperparameter optimization:

- Don't use hyperparameter optimization the first time you train a model. It is designed to be used after you have trained your model and are content with the results. That process often requires repeated refinement and retraining.
- Hyperparameter optimization adds considerable time. If the training process for your model takes five minutes using the standard predefined hyperparameter values, training that same model with hyperparameter optimization enabled could take hours.

## Algorithms used in hyperparameter optimization

Hyperparameter optimization is limited to specific algorithms and model types. It is specifically designed to work with the following model types and algorithms:

- Binary Classification models

  - CatBoost Classification
  - Elastic Net Regression
  - Lasso Regression
  - LightGBM Classification
  - Logistic Regression
  - Random Forest Classification
  - XGBoost Classification
- Regression models

  - CatBoost Regression
  - LightGBM Regression
  - Random Forest Regression
  - XGBoost Regression

Information noteHyperparameter optimization is not available for time series experiments.

## Enabling hyperparameter optimization

Do the following:

1. In an experiment, click View configuration.

   The experiment configuration panel opens.
2. If needed, click Create new version to configure the next version.
3. In the panel, expand Model optimization.
4. Switch from Intelligent to Manual.

   Hyperparameter optimization is not available with intelligent model optimization.
5. Click the check box for Hyperparameter optimization.

## Viewing hyperparameter values

View hyperparameter values in the Compare tab during detailed model analysis. For more information, see [*Performing detailed model analysis*](analyze-models-detailed.htm#Comparin).

## Learn more

- [*Understanding model algorithms*](algorithms.htm)
