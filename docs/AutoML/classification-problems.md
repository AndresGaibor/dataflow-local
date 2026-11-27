---
title: "Classification problems"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/classification-problems.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Understanding machine learning", "Defining machine learning questions"]
---

# Classification problems

Problems where the target column is a categorical column are called classification problems. Binary classification problems have two possible categories, such as Yes or No, whereas multiclass classifications problems have more than two possible categories.

The following examples explain the two types of classification problems. They also discuss some of the considerations when defining a machine learning question.

## Binary classification example: Customer churn

In this example, a company offers a subscription-based model. Data has been collected about all past and current customers. Customers have been labeled as having canceled their subscription (churned) or not.

The following table shows the collected data. Each row represents a unique customer, and the columns represent different features describing that customer. The last column is our target. This is a binary column specifying if the customer has canceled their subscription (Yes or No).

Sample of collected data

![Table with a sample of training data.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/AutomatedMachineLearning/classification-problem-table-1.png "Click to view full size")

We could use this dataset to train a machine learning algorithm to predict if any given customer will churn. However, there are some problems with this approach:

- The dataset compares new and old customers, and there is no information about whether the customers that have not canceled yet will cancel down the road.
- Newly acquired customers might have characteristics that indicate they may churn (maybe we know that males in their twenties who don’t buy much in their first month tend to cancel their subscription soon after). However, as they are new and haven’t canceled yet, we are training the machine learning algorithm to associate those characteristics with a loyal customer that will not cancel.

Avoid these pitfalls by being precise about how you define churn and how you prepare a dataset for the problem. Getting a sense of how to ask business questions in a precise and appropriate way so that they can be tackled by machine learning is something that comes with practice. Seeing both good and bad examples of how to do this is helpful when getting started in machine learning for business applications. If you are unsure about how to frame your business questions for machine learning, consider incorporating a time frame into the definition of your business metrics. This strategy often goes a long way.

### Including a time factor

Let’s consider incorporating time into the question. We could study which customers are going to cancel their services within their first six months. For example, we could use their behavior during their first customer month to predict whether they will churn within the first six months. Now we have a precise way of defining customer churn, a way that incorporates a time frame. We could aggregate a dataset like this:

Dataset including a time factor

![Table with a sample of training data.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/AutomatedMachineLearning/classification-problem-table-2.png "Click to view full size")

Here, each row represents a customer, but now we only include customers that have historically lasted at least six months. For each of them, their number of purchases and total spend during the first month is used to predict whether they churned after six months. For the purposes of this question, it has become irrelevant whether they churned after their first six months. The target column only tells us whether they canceled their subscription within their first six months.

Now, we have a training dataset where the rows can be compared with each other. Once we train a model on this dataset, we can take any new customer that has subscribed for at least one month and use their behavior during their first month and our trained model to predict whether they will churn during their first six months.

## Multiclass classification example: Iris petals

In this example, we have data about a large sample of iris flowers. For each flower, we have recorded the length and width of their petals and sepals, as well as the kind of species of iris it belongs to. In the future, when we encounter a new iris flower, we would like to be able to predict what kind of iris species it is based on its sepal length, sepal width, petal length, and petal width.

Sample of collected data

![Table with a sample of training data.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/AutomatedMachineLearning/classification-problem-table-3.png "Click to view full size")

We can feed the collected data to a machine learning algorithm that fits a function to the historical data. Such a function would output a predicted species type based on values for the other four variables. The output is a category from a discrete set of categories.

Note that we work under the assumption that the data we make predictions on in the future will statistically resemble the data we trained the algorithm on. If there are only three different species of iris present in the training dataset, then we may only use this trained algorithm to make predictions on flowers of those species. We can't expect a machine learning algorithm to make predictions on patterns that it was not trained to recognize from the training dataset.

Related learning:

- [Introduction to Qlik Predict](/lnk/Introduction_Qlik_AutoML)
- [What is Qlik Predict](/lnk/What_is_AutoML)
