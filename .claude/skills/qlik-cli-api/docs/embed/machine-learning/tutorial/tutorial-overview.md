---
source: https://qlik.dev/embed/machine-learning/tutorial/tutorial-overview/
last_updated: 2026-03-18T16:49:43Z
---

# Automated machine learning tutorial overview

Automated machine learning finds patterns in your data and uses them to make predictions on future data.
In addition to making predictions, you can do an in-depth analysis of the key features that influence the predicted
outcome.

For an introduction to automated machine learning, see [Machine learning with Qlik Predict](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/home-automl.htm)
on Qlik Help.

**Example scenario**: You work at a company aiming to reduce churn, a classic example of a binary classification
problem. With limited resources, how can you identify customers likely to cancel their subscriptions?
The Machine Learning API enables you to train and deploy models without deep expertise in machine learning.

## What you'll learn

This tutorial shows you how to:

- Profile historical data.
- Create an experiment and train models.
- Evaluate and deploy the best-performing models.
- Generate predictions in real time or batches.

By the end of this tutorial, you'll know how to automate the machine learning workflow using the Machine Learning API
and gain valuable insights from your data.

## The automated machine learning workflow

The automated machine learning workflow is designed to simplify machine learning tasks by automating key processes.
Here's an overview of the workflow:

1. Create an experiment: Define the problem.
2. Profile your data: Gain insights into your dataset to prepare it for training.
3. Create an experiment version: Configure your experiment to generate and train machine learning models.
4. Evaluate models: Identify the best-performing model.
5. Deploy models: Make trained models available for real-time or batch predictions.
6. Generate predictions: Use the deployed models to infer outcomes from new data.

## Prerequisites

Ensure your dataset that contains historical data meets the following criteria:

- Avoid missing values, duplicates, and inconsistent formats.
- Include a target, which is a well-defined column representing the outcome you want to predict
  (for example, `Churned` for customer churn prediction).
- Include features, which are a range of independent variables that may influence the target.

For more information about preparing your dataset, see [Getting your dataset ready for training](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/dataset-preparation.htm)
on Qlik Help.

## Example data used in this tutorial

This tutorial uses the `AutoML Tutorial - Churn data - training.csv` dataset, which contains customer subscription data
and key features, such as:

- `HasRenewed`: Indicates whether the customer has renewed their subscription previously.
- `CustomerTenure`: The total time the customer has been with the company.

This tutorial also uses the `AutoML Tutorial - Churn data - apply.csv` dataset as the apply dataset for batch prediction
generation.

You can find these datasets in the [Generating and visualizing prediction data tutorial](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/tutorial-machine-learning.htm)
on Qlik Help.

## Next step

[Create your first experiment.](https://qlik.dev/embed/machine-learning/tutorial/tutorial-overview/create-experiment)
