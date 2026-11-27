---
title: "Categorical encoding"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/categorical-encoding.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Working with experiments", "Configuring experiments", "Automatic data preparation and transformation"]
---

# Categorical encoding

Most machine learning algorithms require the variables to be numeric. Because a categorical value does not have a clearly measurable relationship with the other values in that same column, it must first get converted into a numeric representation to be measured by math. Qlik Predict uses categorical encoding to transform categorical values in feature columns into numeric values that machine learning algorithms can understand.

Qlik Predict uses three encoding methods: impact encoding, one-hot encoding, and ordinal encoding. The method used on a particular feature depends on the data characteristics, the number of unique categorical values, and the [experiment type](#glossary-0 "Glossary term").

- For classification and regression problems:

  - For datasets with 100 or fewer columns:

    - Categorical features with 13 or fewer unique values are one-hot encoded.
    - Categorical features with more than 13 unique values are impact encoded.
  - For datasets with more than 100 columns, all categorical columns are impact encoded.
- For time series problems, categorical columns are encoded using ordinal encoding.

You can see which features in your dataset are being processed using categorical encoding by consulting the schema view when configuring your ML experiment. For more information, see [*Configuring experiments*](configuring-experiments.htm).

## How does categorical encoding work

A common technique for giving mathematical representation to a category is one-hot encoding. One-hot encoding pivots the categorical column into n number of columns, where n is equal to the number of unique values in the column. The number 1 is assigned to the appropriate column for each row and 0 to the other columns that were generated for the category. Categorical encoding allows each unique variable to be evaluated independently of the others, unlike a numerical value that is evaluated in relative terms to the other values in the column.

The example in the table shows how the categorical column MarketingSource has been one-hot encoded. The result is four new columns—one for each unique marketing source. On the first row, Person\_1 has marketing source "Facebook". This is represented by 1 in the new Facebook column, and 0 in the other columns.

Categorical encoding of the column MarketingSource

![Table with sample data. The table has four new columns: Facebook, Google Paid Search, Orgenic Search, and Customer referral.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/AutomatedMachineLearning/categorical-encoding-table-1.png "Click to view full size")

Related learning:

- [Introduction to Qlik Predict](/lnk/Introduction_Qlik_AutoML)
