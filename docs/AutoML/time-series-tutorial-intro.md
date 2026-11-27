---
title: "Tutorial – Predicting sales with multivariate time series forecasting"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/time-series-tutorial-intro.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict"]
---

# Tutorial – Predicting sales with multivariate time series forecasting

In this tutorial, you will learn how to train and use a time series model to create time-specific sales forecasts. In particular you will use historical data to configure, train, and deploy a multivariate time series model, and use it to predict and visualize daily sales by store and product family.

## Who should complete this tutorial

This tutorial is designed for users who want to know how to forecast metrics, such as sales, for specific time ranges into the future. Some knowledge of machine learning and Qlik Sense is helpful but not required.

To complete this tutorial, you need the proper permissions in the Qlik Cloud tenant, and in the spaces where you will be working. Some of these are assigned by administrators. If you encounter permissions errors during the tutorial, contact your tenant administrator. You need permissions for the following:

- Creating and working with ML experiments

  [*Creation, use, and management of ML experiments*](who-can-work-with-automl.htm#CreateUseExp)
- Creating and working with ML deployments

  [*Model deployment and creation of ML deployments*](who-can-work-with-automl.htm#ModelDeployment)

  [*Management of ML deployments*](who-can-work-with-automl.htm#ManagementMLDeploy)

  [*Running batch predictions*](who-can-work-with-automl.htm#RunningBatch)
- Activating deployed models

  [*Model approval*](who-can-work-with-automl.htm#ModelApproval)
- Working with scripts and analytics applications

## What you need to do before you start

First, you need to download the tutorial materials linked below.

When you have downloaded your desired materials, unzip them on your desktop.

[MLTimeSeriesTutorialData](/en-US/cloud-services/tutorials/MLTimeSeriesTutorialData.zip)

The [training dataset](#glossary-0 "Glossary term") contains historical data for sales, tracked daily for individual stores and product families.

The [apply dataset](#glossary-1 "Glossary term") contains the required historical data for generating predictions, in addition to data for a future feature.

Do the following:

1. Open the Analytics [activity center](#glossary-2 "Glossary term").
2. Go to the Create page, select Dataset, and then select Upload data file.
3. Drag the  ML - Multivariate forecasting - training.csv file to the upload dialog.
4. Next, drag the  ML - Multivariate forecasting - apply.csv file to the upload dialog.
5. Select a space. It can be your personal space or a shared space if you want other users to be able to access this data.
6. Click Upload.

Now that your datasets are uploaded, you can proceed to creating an experiment.

## Lessons in this tutorial

The topics in this tutorial are designed to be completed in sequence. However, you can step away and return at any time.

## Further reading and resources

- [Qlik](http://www.qlik.com/) offers a wide variety of resources when you want to learn more.
- [Qlik online help](http://help.qlik.com/) is available.
- Training, including free online courses, is available on [Qlik Learning](https://learning.qlik.com/).
- Discussion forums, blogs, and more can be found in [Qlik Community](http://community.qlik.com/).

## Your opinion matters

We appreciate any feedback that you may have. Please use the section below to let us know how we're doing.
