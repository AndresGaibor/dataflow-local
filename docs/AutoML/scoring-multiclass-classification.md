---
title: "Scoring multiclass classification models"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/scoring-multiclass-classification.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Working with experiments", "Reviewing models", "Understanding model review concepts", "Interpreting model scores"]
---

# Scoring multiclass classification models

Multiclass classification is when you are trying to predict a single discrete outcome as in binary classification, but with more than two classes. Multiclass classification models are scored by different averages of [F1](scoring-binary-classification.htm#F1).

## F1 Macro

F1 Macro is the averaged F1 value for each class without weighting, that is, all classes are treated equally.

## Micro F1

Micro F1 is the F1 value calculated across the entire confusion matrix. The total true positives, false negatives, and false positives are counted. Calculating the Micro F1 score is equivalent to calculating the global precision or the global recall.

## Weighted F1

Weighted F1 corresponds to the binary classification F1. It is calculated for each class and then combined as a weighted average taking into account the number of records for each class.

## Accuracy

Accuracy measures how often the model made a correct prediction on average. It is calculated as the number of exactly matching predictions divided by the number of samples.

## Prediction speed

Prediction speed is a model metric that applies to all model types: binary classification, multiclass classification, regression, and time series. Prediction speed measures how fast a machine learning model is able to generate predictions.

In Qlik Predict, prediction speed is calculated using the combined feature computing time and test dataset prediction time. It is displayed in rows per second.

Prediction speed can be analyzed in the Model metrics table after running your experiment version. You can also view prediction speed data when analyzing models with embedded analytics. For more information, see:

- [*Analyzing the model metrics tables*](analyze-models-quick.htm#Analyzing)
- [*Comparing models*](analyze-models-compare.htm)

### Considerations

The measured prediction speed is based on the size of the training dataset rather than the data on which predictions are made. After deploying a model, you might notice differences between how fast predictions are created if training and prediction data differ greatly in size, or when creating real-time predictions on one or a handful of data rows.

## Bias metrics

In addition to these metrics, a number of bias metrics are also available for features on which you run bias detection. Some of these metrics are specific to the model type you are training. For more information, see [*Detecting bias in machine learning models*](bias-detection.htm).
