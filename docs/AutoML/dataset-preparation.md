---
title: "Getting your dataset ready for training"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/dataset-preparation.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Understanding machine learning"]
---

# Getting your dataset ready for training

You train a dataset to answer your machine learning question. The training dataset includes a column for each feature as well as a column that contains the target. The machine learning algorithms learn general patterns from these rows of data to generate a model that can predict the target.

To get the dataset machine learning-ready, you need to understand your data and collect the necessary data points. You might also need to transform some of the data and remove data that is not relevant to your use case.

## What data should you collect?

Define your machine learning question precisely and decide exactly what needs to be aggregated to approach that question:

- If you want to predict which customers will churn, you need to aggregate a dataset where each row represents a customer, each feature column represents a feature that describes that customer, and the target column is whether that customer churned in a certain time period.
- If you want to predict what the sales will be for a given month and region, you need to aggregate a dataset where each row represents a given month for a given region, each feature column represents a feature that describes that month’s business in that region, and the target column is the sales revenue for that region in that month.

Try to figure out which things could influence the target and see if that data can be gathered. Remember that the predictive algorithms can only identify patterns that are there to be found. Maybe you need to collect or create additional features to extract additional information?

You must also determine how much data you need to accumulate before you can accurately predict. How long does it take before the event becomes representative? Consider the following examples:

- Customers need to have been a member for 60 days before you can predict if they will leave by day 90.
- The cost of insurance claims won’t be known for a few months, so you can exclude claims less than six months old.

Distinguish between time variant and non-time variant data. With time variant data, is the data timestamped to be aggregated appropriately?

## Will the data be available at the time of prediction?

Make sure that all the features you include in the training dataset will be available also for future predictions. It is a common mistake to train the model on features that you have available for historical data, but that will not be available at the time you make a prediction in the future. When making predictions on new data, the machine learning algorithm must have values for all the features that were available in the training dataset.

## Is more data better?

### Sample size

A larger volume of data tends to produce more reliable models. Any additional relevant data points will help, whether those are new or historical observations.

### Number of features

It can be tempting to include all possible variables into the model no matter the relevance to the targeted outcome. Simpler is typically better. It is generally better to use a smaller number of features in the model.

When there are more features, there can be more risk for potentially covering up the true underlying relationship that you want to uncover. The predictive model can use all the features to come up with a series of complicated rules that perform well against the data used to train the model. But the predicted target might actually only be influenced by one or two features. The model might not be good at generalizing to data outside of what was used in the training, which would result in poor predictive performance when applied to new data.

### Overfitting

Overfitting means that a model is overly complex and, as a result, is unreliable for predicting new data. Overfitting tends to happen when there are too many features relative to the number of data points available. For example, you might only have 50 rows of data and 100 feature columns in the dataset.

## Is your training data relevant?

A machine learning algorithm finds patterns in the data you feed it and uses those patterns to make predictions on data in the future. When you make predictions on new data, you assume that it is similar to the training data. For this reason, it is important that the training dataset statistically resembles the data you will make predictions on.

If the market or business has changed significantly from what your training dataset describes, you are probably using an outdated dataset that will lead to inaccurate predictions. You might need to create a new training dataset and only use data that is gathered after the change occurred.

Consider the example about sales predictions in [*Understanding machine learning*](machine-learning-basics.htm). Let's say that we fed data into our algorithm that represented advertisement spend on television, radio, and newspaper, as well as sales revenue for historic business quarters. However, the data was collected in the 1980’s. Now we no longer advertise that product on the radio and we almost exclusively advertise the product online. Our trained algorithm would perform poorly in predicting sales for the current business quarter because the training data is not representative of the current business.

## Explore the data

Use your business knowledge to understand and validate the data. If the data doesn’t align with your assumptions, could it mean data issues or could it mean that your assumptions are off?

### Remove unreliable features

Consider excluding columns from the dataset where:

- There is a high concentration of one value (low cardinality). For example, a column with the values "red", "green", "blue" where 90 percent of the values are "red".
- The values are highly unique (high cardinality).
- Most of the values are null.

### Address correlated features

Remove redundant features such as highly correlated features that provide the same or very similar information. Consider selecting a single feature from groups that appear to capture the same behaviors in the data. Try to determine if there is one feature that is driving the other.

### Replace null values

Explore your data to find out if there are missing values in key data points such as the target or key features. To use values from a sparse column, you can replace null values with "other" or "unknown". Or maybe you need to reassess the data collection.

### Target range

Look at the distribution of the data. If the distribution of your target data is too spread out relative to your sample size, it might be hard to find any pattern in your data.

What is the range of data values? There are some challenges with predicting data values outside of the range. Read more in [*Extrapolation and interpolation*](extrapolation-interpolation.htm).

Are there abnormalities in the distribution? Skew, tails, and multi-modal shapes in your data might require additional data transformation or further [feature engineering](feature-engineering.htm). Try to group low-volume categories and round or remove tails in numeric features.

### Eliminate outliers

Consider removing observations with outlier values in the feature columns. Outliers can impede an algorithm’s ability to discern general patterns in the data. It might be better to look at a smaller subset of data that has a tighter spread in the target column.

### Data grouping

You might improve your results by splitting the data into different datasets and use them to train separate models. Base the data grouping on one or more features.

### Data leakage

Data leakage means that the data used to train a machine learning algorithm includes the information you are trying to predict.

Related learning:

- [What is Qlik Predict](/lnk/What_is_AutoML)
