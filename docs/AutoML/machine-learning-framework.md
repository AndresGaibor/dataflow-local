---
title: "Defining machine learning questions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/machine-learning-framework.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Understanding machine learning"]
---

# Defining machine learning questions

Turning a business use case into a specific and actionable machine learning question can be challenging. Follow a structured framework to avoid common pitfalls and generate a good predictive model.

The framework describes how to define a machine learning question and how to collect a well-structured dataset that is ready to be used. For more information about preparing a dataset, see [*Getting your dataset ready for training*](dataset-preparation.htm).

The framework consists of four parts:

- Event trigger
- Target
- Features
- Prediction point

Information noteThis framework describes how to define a machine learning question for classification and regression problems. To define machine learning questions for time series forecasting problems, see [*Working with multivariate time series forecasting*](machine-learning-framework-time-series.htm).

## Event trigger

The event trigger is an action or event that triggers the creation of new predictions. Each event trigger corresponds to a single row of data.

## Target

The target is the value that you are trying to predict. It must be specific both in how you define the value—the outcome—and the time frame by which the value is determined—the horizon. Defining the outcome and the horizon depends on the business context as well as the available data. Make sure that the target is relevant to the business context and think about what action you want to take with the predicted values.

The target is represented in a single column in the dataset that you use to train the machine learning algorithms.

## Features

The features are the other columns in your dataset that are used to predict a target value. They are your hypotheses about which variables will influence the target. Machine learning algorithms use the features to learn general patterns during training and to make predictions for new rows of data.

The feature columns make up most of the training dataset, where each feature is represented as a single column. Features must be aggregated to the event trigger level or higher.

Features can be fixed, which means that they are known at or before the event trigger, or window-dependent, which means that the data is collected after the event trigger but prior to the prediction point.

## Prediction point

The prediction point is the designated time when you stop collecting data for features and predict the target for each row. Deciding where the prediction point should fall is a balance between accuracy—predicting late enough to have collected quality feature data—and actionability—predicting early enough to take action to affect the outcome.

The time between the event trigger and the prediction point is the data accumulation window. This is the time used to collect feature data. The time between the prediction point and the horizon is the action window, which is the time used to act on what has been predicted. The prediction point can fall anywhere between the event trigger and the target horizon.

## Examples: Structured framework

The following examples show how the structured framework can be used on different business use cases. For an in-depth example where the framework is applied step by step, see [*Applying the structured framework: Customer churn example*](customer-churn-example.htm).

### Customer lifetime value

- Event trigger: A customer places their first order
- Target: Total order amount for the first three years

  - Numeric outcome: Dollar amount
  - The horizon is based on average customer life cycle length
- Features: Lead source, First order amount, Discount used on first order (Yes or No), Shipping state, Shipping region, Number of products in the first order
- Prediction point: Three months after the first order
- Machine learning question: "Predicting three months after a customer’s first order, what will their total order dollars be over the next 33 months"

### Customer repurchase

- Event trigger: A customer places an order
- Target: Another order is placed within six months

  - Binary outcome: Yes or No
  - The horizon determined by the data that 90 percent of customers who repurchase do so in six months or less
- Features: Traffic source, Number of previous orders, Discount used, Shipping state, Shipping region, Number of products ordered, Opened shipping notification email (Yes or No), Returned to site within 10 days, Signed-up for marketing emails (Yes or No)
- Prediction point: One week after order
- Machine learning question: "Predicting one week after a customer places an order, will they order again within six months"

### Sales lead conversion

- Event trigger: A sales lead is created
- Target: Converts to closed win within 12 months from creation

  - Binary outcome: Yes or No
  - The horizon based on the historical length of the sales cycle
- Features: Lead source, Industry, Company size, Number of touch points the first 30 days, Meeting scheduled within 30 days (Yes or No), Accurate phone number (Yes or No)
- Prediction point: 30 days after the lead is created
- Machine learning question: "Predicting 30 days after a lead is created, will that lead convert to a closed won opportunity within the next 11 months"

### Student graduation

- Event trigger: A student is accepted
- Target: Student graduates within six years from the program start

  - Binary outcome: Yes or No
  - The horizon is based on the historical length of the time to graduate
- Features: High school type, High school GPA, SAT/ACT score, Placement exam scores, Distance from high school to enrolled campus, Scholarship level, Parents' education level, First semester GPA, Number of credits first semester
- Prediction point: End of first enrolled semester
- Machine learning question: "Predicting at the end of their first semester, will a student graduate by the end of the sixth year"

### Sales by month

- Event trigger: First day of the month
- Target: Sales in units during the month

  - Numeric outcome: Number of units sold
  - The horizon is based on the calendar month
- Features: Product type, Month name, Quarter, Last year sales the same month, Two years prior sales the same month, Previous month sales, Average discount %, Marketing spend
- Prediction point: First day of the month
- Machine learning question: "Predicting on the first day of the month, what will total unit sales be by the end of the month"

Related learning:

- [What is Qlik Predict](/lnk/What_is_AutoML)
