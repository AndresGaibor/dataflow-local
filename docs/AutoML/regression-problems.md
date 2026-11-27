---
title: "Regression problems"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/regression-problems.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Understanding machine learning", "Defining machine learning questions"]
---

# Regression problems

Regression problems are machine learning problems with a numerical target column. The following example will show you how to frame a business question in a precise way, and then aggregate a training dataset where all features are on equal footing. This provides a good basis for generating a predictive regression model.

## Regression example: Customer lifetime value

We start by assuming that a machine learning model trained on historical customers will learn to predict customer lifetime value using several features that influence that prediction. We collect a dataset with historical information about all past and present customers. There is one row for each customer and the columns represent features describing the customer: customer ID, gender, age, the date when they became a customer, zip code, the number of purchases they have made, and their total monetary spend.

Sample of collected data

![Table with a sample of training data.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/AutomatedMachineLearning/regression-problem-table-1.png "Click to view full size")

We could define customer lifetime value as the total monetary spend, feed the dataset to a machine learning algorithm, and have it learn to predict total monetary spend. As new customers are acquired in the future, we could use the trained algorithm to predict how much monetary value they will provide during their customer life. However, there are several problems with this approach:

- The dataset might include people who have been customers for one day, one month, or one year. The value for total monetary spend doesn’t reflect how much a customer will spend, but instead the total they have spent to-date.
- A customer whose account is one day old might have the characteristics of a customer with a high return. But because they just became a customer yesterday, they have only made one purchase and have not spent a lot of money. By including them in the training dataset, we are incorrectly teaching the machine learning algorithm that they are the type of customer who doesn’t bring in much money.
- We might have a new customer who in their first month has been ordering products three times a week, totaling 12 purchases. Someone else who has been a customer for one year and purchased once per month might have spent the same amount of money. The machine learning algorithm would put these two customers on equal footing in terms of customer lifetime value, when in reality the one-month-old customer might be significantly more valuable in the long run.

To avoid these pitfalls, we need to be precise about how to define customer lifetime value and about how to prepare a dataset for the problem. A good way to achieve this is to include time as a factor in the problem definition.

## Including a time factor

To include a time factor, we start by defining first-year value as the total money a customer spends in their first year as a customer. We could then use a customer’s behavior during their first three months as features to predict their total spend over their first year. First year value is a precise definition of a metric of interest that incorporates a time frame. The advantage of creating such a precisely defined metric is that it puts all examples from our training dataset on equal footing.

Note that since we are now looking at the total money people spent during their first year as customers, we must limit the training dataset to customers that have been around for at least one year. We could prepare a dataset like this:

Dataset including a time factor

![Table with a sample of training data.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/AutomatedMachineLearning/regression-problem-table-2.png "Click to view full size")

Here, each row represents a person who has been a customer for at least a year. The columns include features that describe the customer at the time when they became a customer as well as features that represent the customer’s activity during the chosen time frame.

The activity is measured by the number of purchases made in the first three months and the total monetary spend in the first three months. The target column represents the total money spent in the first year. That is the first year value that we will teach the machine learning algorithm to predict.

Notice how we are now asking a very precise question that is defined within a time frame: "Predict how much money a customer will bring in during their first year, based on their behavior during their first three months."

## Comparing regression and time series problems

Regression problems are similar to time series problems in both the target variable and the real-world use cases they involve. There are also several differences between these two problem types.

For more information about time series problems, see [*Time series problems*](time-series-problems.htm).

### Similarities

- Both involve a numerical target column.
- Both are commonly used in financial use cases involving sales and monetary forecasting.

### Differences

- Time series problems support grouped targets, while regression problems do not (see [*Components of a time series problem*](machine-learning-framework-time-series.htm#Components)). Grouped scenarios can still be addressed for regression problems by training multiple different models, at the cost of global learning across groups.
- Time series problems support scenarios where you know certain feature variables ahead of time—for example, weather-related forecasts, planned promotional discounts, and whether dates fall on week days, weekends, and holidays. These feature variables are known as [*Future features*](machine-learning-framework-time-series.htm#FutureFeatures).
- For time series problems, data must be indexed by date or datetime on a fixed time interval. Also, different data content is expected and generated during training and predictions (see [*Preparing a training dataset*](machine-learning-framework-time-series.htm#TrainPrepare) and [*Preparing an apply dataset*](machine-learning-framework-time-series.htm#ApplyPrepare)).
- In time series problems, predicted values explicitly correspond to specific dates and times. In regression problems, predicted values may or may not correspond to specific dates and times, but if they do, this association is implied rather than explicitly denoted in output.
- Different algorithms are used (see [*Understanding model algorithms*](algorithms.htm)).

## Learn more

- [*Time series problems*](time-series-problems.htm)
- [Introduction to Qlik Predict](/lnk/Introduction_Qlik_AutoML)
- [What is Qlik Predict](/lnk/What_is_AutoML)

Related learning:

- [Introduction to Qlik Predict](/lnk/Introduction_Qlik_AutoML)
- [What is Qlik Predict](/lnk/What_is_AutoML)
