---
title: "Working with date features in predictions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/date-features-predictions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Working with ML predictions"]
---

# Working with date features in predictions

When running predictions from an ML deployment trained with auto-engineered date features, there are requirements for how you specify dates and times in the apply data. These requirements and considerations are slightly different depending on whether you are running batch predictions, real-time predictions, or using the Qlik Predict analytics connector.

## Automatic date feature engineering

Automatic feature engineering is a data preparation step that is performed in an ML experiment during model training. With this process, new features are created from the training dataset, and then used to train the model. For date feature columns, this process is performed automatically by default. Users can opt out of date feature engineering. However, in most cases, it is recommended to use this capability.

For more information, see [*Date feature engineering*](date-feature-engineering.htm).

## Requirements for batch predictions

Auto-engineered date features are generated when using the training dataset to create a model, which is deployed and used as an ML deployment to make predictions on new data (for [batch predictions](#glossary-0 "Glossary term"), this is the [apply dataset](#glossary-1 "Glossary term")).

When a model trained with auto-engineered date features is deployed for making predictions, the apply dataset on which you are generating predictions does not need to include the auto-engineered date features. Qlik Predict generates the auto-engineered features for the apply dataset before predicting. However, the apply dataset must include the parent date feature (from which the date parts were derived), and the column you are using must have the Date, Datetime, Timestamp, or Time data type.

The prediction datasets created by an ML deployment, including SHAP and apply datasets, will include the auto-engineered date features.

## Requirements for real-time and connector-based predictions

When running [real-time predictions](#glossary-2 "Glossary term") and predictions from the Qlik Predict analytics connector, there are requirements for date features in the apply data you provide to Qlik Predict. For these types of predictions, the apply data is specified in a small JSON payload rather than as an apply dataset. For both real-time and connector-based predictions, you are sending the JSON payload to the real-time prediction endpoint in the Machine Learning API.

For the real-time prediction endpoint in the Machine Learning API to be able to process your date and timestamps fields, the JSON payload you send to the endpoint must follow the requirements below:

- Date and datetime values must be strings formatted in accordance with ISO 8601 standards. Examples:

  - 2020-01-14
  - 2020-01-14T00:00:00.000Z
- The parent date—the feature from which the date parts were derived—must be included in its entirety. For example, your model might only use a Year feature but you still need to provide the date in ISO 8601-compliant format.
- Data within each column needs to be of the same time zone.

The above requirements:

- Only apply for features trained with date feature engineering. If the feature type is manually changed to the categorical feature type, these requirements do not apply. If the feature type has been changed to categorical, provide the column, in the date format in which it was originally used for training, in the apply data.
- Do not apply to time series models.

Information noteThe data you use to train your model do not have to follow these requirements.

Information note

The real-time predictions API is deprecated and replaced by the real-time prediction endpoint in the [Machine Learning API](https://qlik.dev/apis/rest/ml/). The functionality itself is not being deprecated. For future real-time predictions, use the real-time prediction endpoint in the Machine Learning API. For help with migrating from the real-time predictions API to the Machine Learning API, refer to [the migration guide on the Qlik Cloud developer portal](https://qlik.dev/apis/rest/automl-deployments/#migrate-from-the-automl-real-time-predictions-api-to-the-machine-learning-api).

## Learn more

- [*Automatic feature engineering*](automatic-feature-engineering.htm)
- [*Date feature engineering*](date-feature-engineering.htm)
- [*Qlik Predict analytics source*](../LoadData/ac-qlik-automl-connector-overview.htm)
