---
title: "Automatic data preparation and transformation"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/preprocessing-steps.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Working with experiments", "Configuring experiments"]
---

# Automatic data preparation and transformation

The dataset you have selected for your experiment is automatically preprocessed to prepare it for model training. The preprocessing steps include data preparation and transformation. This increases the quality of the data to give you a model that produces accurate results.

A variety of data science techniques are used to preprocess the data. Most of the steps are performed by default and work well in many use cases. Knowing what these default steps are—along with the underlying concepts—can help you understand what you need to do with the data for your specific use case before using it to train a model.

## Experiment setup

Before preprocessing begins, Qlik Predict performs several preparatory steps and offers a preview of how your data will be handled. Some steps depend on your experiment type and other factors. The following steps may apply:

1. Classify columns in the dataset as having a categorical, numeric, date, or free text feature type.

   - Float, double, and decimal data types are always considered numeric.
   - Columns with a string data type, containing an average of less than 50 characters, are classified as categorical.
   - Columns with a string data type, containing an average of 50 or more characters, are classified as free text. However, at this stage, these columns are not guaranteed to be usable as free text features. Additional requirements are checked during preprocessing. See [*Preprocessing steps*](#Preproce).
   - Integer data types are always considered numeric.
   - Date and timestamp data types are always considered to have the date feature type. During experiment setup, Qlik Predict previews the auto-engineered features that could possibly be derived from the parent date feature.
2. Check each column for sparsity, constants, and high cardinality. Exclude the column if:

   - The column is 50 percent null or more. Deleting records that contain a null value for a feature can lead to throwing away otherwise useful training examples. Alternatively, imputing values can save the example, but the record becomes only an approximation of reality. Therefore, it is often better to exclude features with a high number (over 50 percent) of null values. Note that 0 is never considered null.
   - The column has the same value in every row (constant). In other words, the column has low cardinality. Features with only one single value have no predictive value.
   - The column is categorical and has 90 percent or more unique values (high cardinality). Too many unique values makes it difficult for the model to generalize beyond the training dataset.

Adjustments might be made to how the data is handled once preprocessing has begun.

## Preprocessing steps

After you have selected a target column, the next steps depend on the experiment type. For classification and regression experiments, rows where the target value is null are identified and separated, leaving rows where the target is known as the training set. For time series experiments, missing target values are interpolated.

Only data from the training dataset is used for making the decisions in the following steps. The steps, together with metadata, will be saved and applied to any new data for the model to make predictions on.

Preprocessing is performed on included features whenever you run a new experiment version. Some steps depend on your experiment type and other factors.

1. Calculate and save the mean for numerical values and the mode for categorical values.
2. Impute missing values. For more information, see [*Imputation of nulls*](null-imputation.htm).
3. Encode categorical variables.
4. For time series models, a number of steps are performed to validate user-configured experiment properties and to provide additional information to the user after training finishes:

   - The maximum forecast window is determined.
   - The time step of the date index is confirmed.
   - User-selected target groupings are validated or, if not specified, are identified if present from the included categorical features.
5. Generate new features from existing columns in the dataset. These new auto-engineered features can improve the performance and predictive capability of the models you create.

   Columns identified as possible free text are checked for average word length. If the column has an average word length of greater than five words, it can be encoded as a free text feature using automatic feature engineering. If not, a warning is shown. If not usable as free text, the feature should be deselected if it has high cardinality.
6. Calculate and save summary statistics for each column to use for feature scaling.
7. Standardize each column with feature scaling.
8. Perform analysis on features that have been selected for bias detection, returning data bias metrics and corresponding insights. For more information, see [*Detecting bias in machine learning models*](bias-detection.htm).
9. Use automatic holdout of training data and five-fold cross-validation. For more information, see [*Holdout data and cross-validation*](holdout-crossvalidation.htm).
10. Calculate various statistics about the dataset with increased certainty. For example, new information may become available about dataset size, row and cell counts, and proportions of null values. For more information, see [*Training dataset and profiling limitations*](ml-limitations-capacities.htm#DatasetSizeCapacities).

## Learn more

- [*Automatic feature engineering*](automatic-feature-engineering.htm)
