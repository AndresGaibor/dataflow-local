---
title: "Tutorial – Generating and visualizing prediction data"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/tutorial-machine-learning.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict"]
---

# Tutorial – Generating and visualizing prediction data

This tutorial teaches you how to use Qlik Predict to train and deploy a machine learning model for making predictions. It also teaches you how you can visualize the prediction data in a Qlik Sense application.

We will consider the scenario of customer churn, a classic example of a binary classification problem. The goal is to be able to reliably predict whether a customer will cancel their subscription or remain a subscriber to a service. There are only two outcomes in this type of problem: true or false (churned, or not churned).

To approach this machine learning problem, we will start by processing a set of data for which we already know the outcome, then apply statistical modeling created from that data to new data for which we would like to predict the outcomes.

You will begin this tutorial by creating an experiment. From there, you will train models and deploy one of them into an ML deployment. This ML deployment will be used to create predictions, which can be visualized in a Qlik Sense application.

## What you will learn

Once you have completed this tutorial, you will understand the different steps involved in creating and configuring an experiment. You will also learn how to interpret model scores. Finally, you will be able to deploy a machine learning model and will understand how your predictions data can be used to generate compelling Qlik Sense visualizations in Qlik Cloud Analytics.

By default, Qlik Predict trains your models with intelligent model optimization. With intelligent optimization, automatic refinement is performed during training. This increases the likelihood that your models will be ready to deploy after a single version with minimal further iteration needed.

## Who should complete this tutorial

This tutorial is designed for users who want an introduction to automated machine learning and data visualization in Qlik Cloud Analytics. Some basic knowledge of machine learning and Qlik Sense is helpful, but not required.

To complete this tutorial, you need the proper permissions in the Qlik Cloud tenant, and in the spaces where you will be working. Some of these are assigned by administrators. If you encounter permissions errors during the tutorial, contact your tenant administrator. You need permissions for the following:

- Creating and working with ML experiments

  [*Creation, use, and management of ML experiments*](who-can-work-with-automl.htm#CreateUseExp)
- Creating and working with ML deployments

  [*Model deployment and creation of ML deployments*](who-can-work-with-automl.htm#ModelDeployment)

  [*Management of ML deployments*](who-can-work-with-automl.htm#ManagementMLDeploy)

  [*Running batch predictions*](who-can-work-with-automl.htm#RunningBatch)
- Activating deployed models

  [*Model approval*](who-can-work-with-automl.htm#ModelApproval)
- Working with analytics applications

## What you need to do before you start

First, you need to download the tutorial materials linked below. Choose between the CSV and QVD workflows. Downloading the pre-configured application is optional.

When you have downloaded your desired materials, unzip them on your desktop.

- [MLTutorialDataCSV](/en-US/cloud-services/tutorials/MLTutorialDataCSV.zip): Contains tutorial data in CSV format. This option is easier for getting started quickly.
- [MLTutorialDataQVF](/en-US/cloud-services/tutorials/MLTutorialDataQVF.zip): Contains tutorial data in the format of .qvf scripts that can be run to create QVDs. This option takes a bit longer than CSV but is helpful in introducing you to working with Qlik data formats and scripting.
- [MLTutorialPreConfiguredApp](/en-US/cloud-services/tutorials/MLTutorialPreConfiguredApp.zip): This item is optional. It is a sample copy of the Qlik Sense application that you will build during the tutorial. This allows you to skip past the training and deployment stages for quicker hands-on experience with predictive application development.

  For more information, see [*Alternative workflow: Upload pre-configured application*](tutorial-predictions-app.htm#Alternat).

The [training dataset](#glossary-1 "Glossary term") contains information about customers whose deadline for renewal has passed, and have made the decision to churn or remain subscribed to the service.

The [apply dataset](#glossary-2 "Glossary term") contains details about a new set of customers whose renewal date has not yet passed. It has not yet been determined whether or not these customers will cancel their service. The goal, with this tutorial, is to predict what this set of customers will do, with the hope that we can decrease the likelihood that they will churn.

### Option 1: Qlik Predict tutorial datasets (CSV)

Do the following:

1. Open the Analytics [activity center](#glossary-3 "Glossary term").
2. Go to the Create page, select Dataset, and then select Upload data file.
3. Drag the  ML - Churn data - training.csv file to the upload dialog.
4. Next, drag the  ML - Churn data - apply.csv file to the upload dialog.
5. Select a space. It can be your personal space or a shared space if you want other users to be able to access this data.
6. Click Upload.

Now that your datasets are uploaded, you can proceed to creating an experiment.

### Option 2: Qlik Predict tutorial datasets (QVD)

Do the following:

1. Open the Analytics activity center.
2. Go to the Create page, select Upload, and then select Script.
3. Drag these files to the upload dialog:

   - ML - Churn data - training.qvf
   - ML - Churn data - apply.qvf
4. Select a space. It can be your personal space, or a shared space if you want other users to be able to access this data.
5. Click Upload.
6. For each uploaded script, do the following:

   1. Open the script and switch to the Editor tab.
   2. In Editor, Click Export data.

   The [QVD](#glossary-4 "Glossary term") dataset is created in the same space where you uploaded the script.

Now that your datasets are created, you can proceed to creating an experiment.

## Lessons in this tutorial

The topics in this tutorial are designed to be completed in sequence. However, you can step away and return at any time.

## Further reading and resources

- [Qlik](http://www.qlik.com/) offers a wide variety of resources when you want to learn more.
- [Qlik online help](http://help.qlik.com/) is available.
- Training, including free online courses, is available on [Qlik Learning](https://learning.qlik.com/).
- Discussion forums, blogs, and more can be found in [Qlik Community](http://community.qlik.com/).

## Your opinion matters

We appreciate any feedback that you may have. Please use the section below to let us know how we're doing.
