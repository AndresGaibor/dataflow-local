---
title: "Introducing automated machine learning"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/introduction.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict"]
---

# Introducing automated machine learning

Automate machine learning for your analytics team with Qlik Predict. With the simple code-free interface, you can easily create machine learning experiments to generate models and make predictions.

## What is machine learning

Machine learning is a branch of artificial intelligence and data science focused on recognizing patterns in historical data to predict future outcomes. Algorithms are trained on the data to build a predictive model without being explicitly programmed to do so. A machine learning model can help you answer questions like:

- Will a gym customer cancel their membership?
- What is the expected lifetime value for a given customer?

Read more about the basic concepts in [*Understanding machine learning*](machine-learning-basics.htm). You will also learn about the structured framework for defining machine learning questions and preparing datasets.

## What can you do with automated machine learning

Create automated machine learning experiments in Qlik Sense. In the Analytics [activity center](#glossary-0 "Glossary term"), you can collaborate on the experiment with other users and easily load data from Catalog to train the model.

Integrate your predictive analytics with Qlik Sense applications to share your findings. Explore further with visualizations and interactive what-if scenarios to understand how changing different parameters might affect your desired outcome.

You can make predictions for datasets stored in Catalog or make operational predictions in real-time using Qlik Sense APIs.

## How do experiments work

An experiment trains machine learning algorithms on a particular dataset with a particular target. The training generates machine learning models, which you can use to make predictions.

Most of the process is automated in automated machine learning. When you create an experiment and load a dataset, the dataset is automatically analyzed and the data is preprocessed to make it ready for machine learning. Statistics and other information about each column are displayed to help you select a target. When you start the training, several algorithms start searching for patterns in the data. For more information about creating and training experiments, see [*Working with experiments*](working-with-experiments.htm).

When the training is finished, scores and ranks let you evaluate the generated machine learning models. By changing parameters and iterating the training, you can generate a number of versions. Choose the best-performing model for your dataset and deploy it to start making predictions. For more information, see [*Working with ML deployments*](working-with-deployments.htm).

As the following image shows, an experiment can have multiple versions, each using one or more algorithms. The model with the best performing algorithm can be deployed to make predictions. This means that one experiment can result in several ML deployments.

![Overview of how experiments, versions, algorithms, models, and predictions are related.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/AutomatedMachineLearning/automl-process-diagram.png "Click to view full size")

## User access to Qlik Predict

For full details about how users can access Qlik Predict, see [*Who can work with Qlik Predict*](who-can-work-with-automl.htm).

## Limitations and capacities

For general Qlik Predict limitations and capacities, see [*Qlik Predict limitations and capacities*](ml-limitations-capacities.htm).

Qlik Predict is an additional paid-for capability. Some limited functionality is included in applicable subscriptions. Some specific capabilities and capacities are dependent on your subscription tier (see [*Qlik Predict subscription-governed capacities*](#Subscription)).

## Qlik Predict subscription-governed capacities

Access to Qlik Predict features is governed by the terms of your Qlik subscription. For details, see:

- [Qlik Pricing](https://www.qlik.com/us/pricing)
- [Qlik Cloud® Subscriptions](https://www.qlik.com/us/legal/product-terms) product description

Related learning:

- [What is Qlik Predict](/lnk/What_is_AutoML)
- [Introduction to Qlik Predict](/lnk/Introduction_Qlik_AutoML)
