---
title: "Selecting the best model for you"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/best-models.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Working with experiments", "Reviewing models", "Analyzing models"]
---

# Selecting the best model for you

When analyzing the results of your experiment, it is important to look for models with specific characteristics that are important for your use case. For example, in addition to consistently accurate predictions, you might also require models that can deliver predictions quickly. In the Models tab in your experiment, models are recommended to you based on several angles of analysis.

Analyzing the top models for an experiment

![The 'Model metrics' table in an ML experiment, with the top models presented as recommendations](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_top-models.png "Click to view full size")

Based on your filters, recommended models are presented to help you consider several different quality perspectives. A single model might be considered a top model in more than one way. The top model types are:

- ![Trophy](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_trophy.svg) [*Best model*](#Best)
- ![Target](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_target.svg) [*Most accurate*](#MostAccurate)
- ![Lightning bolt](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_optimize.svg) [*Fastest model*](#Fastest)

## Viewing the top models in the user interface

For information about finding and exploring the top models for your experiment, see [*Analyzing the model metrics tables*](analyze-models-quick.htm#Analyzing).

## Best model

Based on your filters, the best model is automatically selected for analysis. The best model is highlighted with a ![Trophy](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_trophy.svg) icon.

In Qlik Predict, the best model is determined from a balanced calculation that takes accuracy metrics and prediction speed into account.

To determine the best model, the following process is automatically performed:

1. Select the model with the highest score for the predictive performance metric determined by the model type. The metrics used are:

   - Binary classification: F1
   - Multiclass classification: F1 Macro
   - Regression: R2
   - Time series: MASE (or MAE if MASE is not available)
2. Using the performance scores from step 1, select all models that are within five percent of the score of the highest scoring model.
3. Out of all models selected, select the model with the fastest prediction speed (see [*Prediction speed*](#PredictionSpeed)). This model is the best model.

## Most accurate

It is important that your model is able to generate predictions with high accuracy on a consistent basis. Although F1, F1 Macro, and R2 provide balanced scoring that comprehensively reflect model accuracy, you might also have an interest in the raw accuracy and precision metrics for your models.

The most accurate model is highlighted with a ![Target](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_target.svg) icon. To determine the most accurate model, the following process is automatically performed:

1. Select the model with the highest score for the predictive performance metric determined by the model type. The metrics used are:

   - Binary classification: [*F1*](scoring-binary-classification.htm#F1)
   - Multiclass classification: [*F1 Macro*](scoring-multiclass-classification.htm#F1Macro)
   - Regression: [*R2*](scoring-regression.htm#R2)
   - Time series: [*MASE*](scoring-time-series.htm#MASE) (if MASE not available, select model with lowest [*MAE*](scoring-time-series.htm#MAE))
2. Using the performance scores from step 1, select all models that are within ten percent of the score of the highest scoring model.
3. One of the following two pathways are used depending on the model type:

   1. Binary classification:

      - If the training dataset is balanced, select the model with the highest accuracy score. This is the most accurate model. For information about the specific metric used, see [*Accuracy*](scoring-binary-classification.htm#Accuracy).
      - If the training dataset is imbalanced, select the model with the highest precision score. For information about the specific metric used, see [*Precision*](scoring-binary-classification.htm#Precision).
   2. Multiclass classification or regression:

      - Select the model with the highest accuracy score. The following accuracy metrics are used:

        - Multiclass classification: [*Accuracy*](scoring-multiclass-classification.htm#Accuracy)
        - Regression: [*MAE*](scoring-regression.htm#MAE)
   3. Time series: Select the model with the best (lowest) [*MAE*](scoring-time-series.htm#MAE) score.

## Fastest model

When choosing a model, you might want to place value on how fast the model can deliver predictions. The fastest model is highlighted with a ![Lightning bolt](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_optimize.svg) icon.

Prediction speed determines which model is the fastest. However, the models' predictive accuracy is still considered. This is because a model might be able to generate predictions quickly, but it must also be able to predict with reasonable accuracy as well.

To determine the fastest model, the following process is automatically performed:

1. Select the model with the highest score for the predictive performance metric determined by the model type. The metrics used are:

   - Binary classification: [*F1*](scoring-binary-classification.htm#F1)
   - Multiclass classification: [*F1 Macro*](scoring-multiclass-classification.htm#F1Macro)
   - Regression: [*R2*](scoring-regression.htm#R2)
   - Time series: [*MASE*](scoring-time-series.htm#MASE) (if MASE not available, select model with lowest [*MAE*](scoring-time-series.htm#MAE))
2. One of the following pathways are used depending on the model type:

   1. Binary classification:

      - If the training dataset is balanced, select all models that have an accuracy score within ten percent of the accuracy score of the model selected in step 1. For information about the specific metric used, see [*Accuracy*](scoring-binary-classification.htm#Accuracy).
      - If the training dataset is imbalanced, select all models that are within ten percent of the score of the highest scoring model from step 1. The metrics from step 1 are used.
   2. Multiclass classification or regression:

      - Select all models that have an accuracy score within ten percent of the accuracy score of the model from step 1. The following accuracy metrics are used:

        - Multiclass classification: [*Accuracy*](scoring-multiclass-classification.htm#Accuracy)
        - Regression: [*MAE*](scoring-regression.htm#MAE)
   3. Time series: Select all models within ten percent of the [*MAE*](scoring-time-series.htm#MAE) score of the model from step 1.
3. Out of all models selected, select the model with the fastest prediction speed (see [*Prediction speed*](#PredictionSpeed)). This model is the fastest model.

## Prediction speed

Prediction speed is a model metric that applies to all model types: binary classification, multiclass classification, regression, and time series. Prediction speed measures how fast a machine learning model is able to generate predictions.

In Qlik Predict, prediction speed is calculated using the combined feature computing time and test dataset prediction time. It is displayed in rows per second.

Prediction speed can be analyzed in the Model metrics table after running your experiment version. You can also view prediction speed data when analyzing models with embedded analytics. For more information, see:

- [*Analyzing the model metrics tables*](analyze-models-quick.htm#Analyzing)
- [*Comparing models*](analyze-models-compare.htm)

### Considerations

The measured prediction speed is based on the size of the training dataset rather than the data on which predictions are made. After deploying a model, you might notice differences between how fast predictions are created if training and prediction data differ greatly in size, or when creating real-time predictions on one or a handful of data rows.

## Overfitting

Overfitting occurs when a model's predictive behavior is too closely mapped to the training dataset. When a model is overfitted, it has likely only memorized patterns in the training dataset, and will not be able to accurately predict future values.

Overfitting can have several causes, including issues related to training algorithms and overly short or complex training datasets.

In Qlik Predict, overfitting is automatically identified through an analysis of [test-train results](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/holdout-crossvalidation.htm) for all metrics used in the process for top model selection, except prediction speed:

- Binary classification models: [*F1*](scoring-binary-classification.htm#F1), [*Accuracy*](scoring-binary-classification.htm#Accuracy) (balanced data), [*Precision*](scoring-binary-classification.htm#Precision) (imbalanced data)
- Multiclass classification models: [*F1 Macro*](scoring-multiclass-classification.htm#F1Macro), [*Accuracy*](scoring-multiclass-classification.htm#Accuracy)
- Regression models: [*R2*](scoring-regression.htm#R2), [*MAE*](scoring-regression.htm#MAE)

If there is a greater than ten percent difference between any of these metrics when comparing the testing and training results, the model is suspected of being overfitted.

If a model is suspected of being overfitted, it is never presented as a recommended model, even if it scores well. The model is marked with a warning ![Warning](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_warning_triangle.svg) in the Model metrics table.

If all models shown in your filters are suspected to be overfitted, models recommendations are not provided.

### Addressing overfitting

You can address overfitting by:

- Not deploying models suspected of overfitting.
- If you suspect an issue with your training dataset, see [*Getting your dataset ready for training*](dataset-preparation.htm) to learn about how you can prepare your training data to avoid overfitting.
