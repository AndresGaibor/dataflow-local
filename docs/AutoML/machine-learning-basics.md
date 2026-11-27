---
title: "Understanding machine learning"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/machine-learning-basics.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict"]
---

# Understanding machine learning

Machine learning is the practice of using mathematical algorithms to recognize patterns in data and then use those patterns to make predictions.

## A simple example: Predicting sales

To better understand machine learning, let’s look at a simple example that predicts the sales of a product over the next quarter. We might know that sales of this product are affected by how much money is spent advertising the product. By looking at the data from previous quarters we know:

- How much money is spent (in thousands of dollars) advertising the product on television.
- What the sales were (in millions of dollars).

When we plot the data, it is obvious that the more money that is spent advertising our product on television, the more we sell.

Plot of sales versus television ad spend

![Plot of sales versus television ad spend.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/AutomatedMachineLearning/simple-example-1.png "Click to view full size")

To predict the sales revenue during the next business quarter, we can fit a function to the historical data:

A linear function is fit to the data

![Plot of sales versus television ad spend with a linear function.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/AutomatedMachineLearning/simple-example-2.png "Click to view full size")

Based on the amount of money we have budgeted to spend in television advertising during the next business quarter, we can evaluate the function at the value corresponding to this amount. Say that we are planning on spending $225,000 in television advertising next quarter. Evaluating the function at 225 gives us 17.7, and we can forecast $17.7 million in sales for the next quarter.

The function is evaluated to forecast sales for a specific amount spent on advertising

![Plot of sales versus television ad spend evaluating a point on a linear function.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/AutomatedMachineLearning/simple-example-3.png "Click to view full size")

To further improve the accuracy of our prediction, we can try to find a function that better fits the historical data—as shown in the figure—and make predictions based on this function.

A function that is a better fit to the data

![Plot of sales versus television ad spend with a non-linear function.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/AutomatedMachineLearning/simple-example-4.png "Click to view full size")

In this example, we have only looked at the amount of money spent on television advertising. We could also consider other factors that influence future sales. Instead of having sales as a function of television ad spend alone, we could, for example, have sales as a function of the three variables television ad spend, radio ad spend, and newspaper ad spend. We can use as many variables as we want, but the general idea is the same.

## Machine learning concepts

From a data perspective, the machine learning problem is reduced to compiling a table with historical data. We have one column in the table representing what we want to predict, which in our previous example was sales. In the language of machine learning, this column is called the target. The other columns are called features and are used to predict the value of the target column. The features are variables that can potentially contribute to the target outcome. The fundamental idea behind machine learning is:

Given a dataset, we find a function that fits that data so that we can predict what the value for the target column will be given the values for the feature columns.

Several sophisticated machine learning algorithms have been developed to solve different kinds of machine learning problems. When we feed data to a machine learning algorithm and let it learn patterns, we say that we are training a machine learning algorithm.

In Qlik Predict, machine learning problems are divided into classification, regression, or time series problems, depending on:

- If the target to predict is a categorical or numerical value. See examples in [*Classification problems*](classification-problems.htm) and [*Regression problems*](regression-problems.htm).
- If you need to predict data for specific future time periods. See an example in [*Time series problems*](time-series-problems.htm).

## Automated machine learning

With automated machine learning, the best fitting functions are found automatically during the training on your historical data. You can easily upload a dataset, select a target, and then start the training at the push of a button.

However, you will only get a good predictive output if you have good input. A machine learning experiment needs a well-defined machine learning question and a dataset designed to answer that question. To get started with your first experiment, follow these steps:

1. Define a machine learning question

   Turn your business use case into a specific question using a structured framework.

   [*Defining machine learning questions*](machine-learning-framework.htm)
2. Prepare your training dataset

   Collect good-quality data that is relevant for your use case.

   [*Getting your dataset ready for training*](dataset-preparation.htm)
3. Create an automated machine learning experiment

   When the preparations are done, you can start experimenting.

   [*Working with experiments*](working-with-experiments.htm)

Related learning:

- [What is Qlik Predict](/lnk/What_is_AutoML)
