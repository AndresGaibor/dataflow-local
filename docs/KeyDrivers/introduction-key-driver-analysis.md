---
title: "Uncovering the key influencers behind your data using key driver analysis"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/KeyDrivers/introduction-key-driver-analysis.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data"]
---

# Uncovering the key influencers behind your data using key driver analysis

With [key driver analysis](#glossary-0 "Glossary term"), you can identify and compare the sources of specific trends in your data. A key driver analysis helps you visualize and rank the influence that a defined set of factors has on the current data for a specific target field. Use the insights you uncover to improve and enhance your organization's analytical and decision-making processes.

Key driver analysis is available in a Qlik Sense application. Perform key driver analysis in sheet view when in analysis mode.

Qlik Cloud Government noteKey driver analysis is not available in Qlik Cloud Government.

Information note

Key driver analysis is not available in Qlik Sense Business, Qlik Cloud Analytics Standard, or Qlik Anonymous Access.

Key driver analysis in a Qlik Sense application

![Key driver analysis in a Qlik Sense app](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_key-driver-analysis-rev.png "Click to view full size")

## What is key driver analysis?

[Key driver analysis](#glossary-2 "Glossary term") is a form of statistical data discovery that allows you to identify the degree to which various factors impact the outcome of a single target metric. The analysis is performed for both quantitative and qualitative data. The intention behind a key driver analysis is to find out exactly what is causing a certain trend in the data, and use these insights to take direct action or improve organizational awareness.

In business intelligence, common targets for which you would like to evaluate influencers are [fields](#glossary-3 "Glossary term") such as Sales, Customer Satisfaction, Margin, Churned, and Cost of Sale. Examples of factors (key drivers) include Product, Location, Store Number, and Manager.

The metrics evaluated in a key driver analysis differ for every organization and use case. The target metric, and the various factors influencing its outcomes, depend on the problem you are looking to solve, the available data, and other factors.

## Why use a key driver analysis?

Key driver analysis is useful in business intelligence because it can be applied in numerous ways to improve key performance indicators. You could use a key driver analysis to solve problems and gain insights related to product investment, revenue expansion, cost reduction, customer satisfaction, and many others.

In Qlik Sense, key driver analysis is integrated into the application consumer experience. Using the real-time data analysis capabilities native to Qlik Sense, you can run a new key driver analysis each time the application data changes. This allows you to continuously monitor your data for changes and quickly uncover emerging trends so you can take prompt and effective action where needed.

## How it works

Key driver analysis is centered around the idea of influence. In Qlik Sense, key driver analysis evaluates the influence that specific fields (features, or key drivers) have on a particular field of interest (the target).

### The data used in the analysis

A key driver analysis is a specific examination of a subset of your data. When you create the analysis, you select certain fields as the components of the analysis.

You need to choose the following building blocks for each analysis:

- Target
- Multiple features

After you have selected these components, a specific dataset is created from your data model using the target and features. The key driver analysis uses this dataset, not your entire data model, to determine the influence that the features are having on the target. Fields that you do not include in the configuration are not analyzed.

More information about each component is provided below.

### Calculating influence

In Qlik Sense, key driver analysis is performed by calculating the SHAP values for each feature data value in the subset of data you are analyzing. These SHAP values are generated from a model trained by Qlik Predict. Models use the random forest algorithm to generate the SHAP values.

The SHAP value is a calculation of the degree of impact a data value has on the corresponding target value, in relation to the other features in the dataset specifically created from your key driver analysis configuration. When you view the results of a key driver analysis, you are viewing aggregations of the SHAP values across all or a particular set of records in the dataset.

For more information about SHAP importance in Qlik Predict, see [*Understanding SHAP importance in experiment training*](../AutoML/shap-importance.htm).

### The target

The target is the field for which you want to analyze key drivers. For example, you might want to compare how certain factors are influencing your sales. In this case, you would select a sales measure as your target.

When selecting your target, time of data availability is important, particularly in relation to the features you choose to include in your analysis. For more information about the proper data collection time frames for your target and features, see [*Features*](#Features).

The number of unique values and type of data in the target determines the type of problem the analysis will solve. This, in turn, impacts the requirements your data has to meet. For more information, see [*Data requirements*](#Requirem).

Key driver analysis supports the following problem types:

- Regression
- Binary classification

#### Regression analyses

Regression analyses are used when the target contains a large number of unique numeric values. If you use a numeric calculation (measure) as your target, the key driver analysis will likely interpret the configuration as a regression problem.

When choosing a measure as your target, you can apply a basic aggregation directly to the field within the configuration, or select an existing master item if you want to use a more complex expression.

#### Binary classification analyses

If your target only includes two unique values (For example, yes or no), the key driver analysis interprets the configuration as a binary classification problem. Binary classification analyses are created by selecting a binary dimension as the target.

As a common example, if you have a Churned field in your application to track which customers have canceled a particular service, you could select the Churned field as the target to uncover what factors are driving those customer decisions.

### Features

The features are your key drivers. These are the fields that contain extractable information about what is influencing trends in the data. For example, when you create a key driver analysis to identify influencers behind sales, you might select [dimensions](#glossary-4 "Glossary term") like Location, Product Type, Store Number, and Sales Representative as features. Calculated [measures](#glossary-5 "Glossary term") can also be used as features.

You should only include features containing data that is recordable and collected before the point in time at which you collect your target data. If you include features containing data you would only know at time of data collection for the target, the analysis will be skewed and will not provide analytical value.

For example, if your target is Sales, you should not include features containing data directly derived from it. Likewise, if your target is a Churned field with a binary outcome (Yes or No), you should not include a feature containing the date on which the customer churned.

For more information about how to identify invalid analysis results, see [*Identifying invalid results*](key-driver-analysis-results.htm#Identify).

A feature is assigned one of the two following types:

- Categorical feature: one which contains data values based on distinct, recurring categories. An example of a categorical feature could be a Continent field, in which there are only a handful of possible values and these are not interpreted as raw numeric data, but instead as text. Numbers can be used as categories.
- Numeric feature: one in which the data values are purely numeric data and do not belong to categories.

All included features are specifically analyzed to determine how much influence each has on the current data in the target.

For more information about requirements for the target and included features, see [*Data requirements*](#Requirem).

### Application selections

The selections you make in the application are used in the key driver analysis. For example, you might want to discover key drivers for sales, but when including a Store Number dimension as a feature, you might only want to analyze the influence of five specific stores in your organization. To do this, you could select the values in the application, then configure the key driver analysis.

Because selections are basically filters applied to the data model, it is important to be aware that making selections in one field can affect the available data that can be used in the analysis.

## Considerations for the tenant subscription

Key driver analysis relies on Qlik Predict to calculate the influence of the features on the target. It does this by creating machine learning models which are used to calculate SHAP values for the data points corresponding to included features in the selected data subset.

Creating a key driver analysis consumes services metered by Qlik Predict. A certain amount of Qlik Predict usage is included with most Qlik Cloud subscriptions. If more capacity is needed, an upgrade to a paid tier of Qlik Predict is required.

Check with your [service account owner](#glossary-6 "Glossary term"), and consult the terms of the subscription you are using, to find out your capacity for usage of key driver analysis.

The following resources can provide additional details:

- [*Introducing automated machine learning*](../AutoML/introduction.htm#AutoML)
- The product description for [Qlik Cloud® Subscriptions](https://www.qlik.com/us/legal/product-terms)

## Data requirements

### Minimum data volume requirements

The dataset created from your target and features needs to have at least 400 cells. Otherwise, you cannot run the analysis.

### Other requirements

The following requirements apply to the dataset created from your analysis configuration:

- The target needs to contain at least two unique values.
- If the target contains between two and ten unique values, each unique value needs to appear in at least ten records in the dataset.

If you encounter errors when running a key driver analysis, it could be that the data you have selected for the analysis does not meet these requirements. For other problems you might encounter and a list of possible solutions, see [*Troubleshooting*](use-key-driver-analysis.htm#Troubles).

## Using key driver analysis in Qlik Sense

The following help topics can help you get started with creating and interpreting [key driver analyses](#glossary-7 "Glossary term") in Qlik Sense:

- [*Creating a key driver analysis in Qlik Sense*](use-key-driver-analysis.htm)
- [*Viewing and interpreting the results of a key driver analysis*](key-driver-analysis-results.htm)

### Limitations

A list of limitations for key driver analysis is provided below:

- Fields containing the date, time, or timestamp data types are not supported for use as the target or as features.

## Learn more

- [*Creating a key driver analysis in Qlik Sense*](use-key-driver-analysis.htm)
- [*Viewing and interpreting the results of a key driver analysis*](key-driver-analysis-results.htm)
