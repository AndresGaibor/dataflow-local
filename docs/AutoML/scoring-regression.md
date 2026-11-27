---
title: "Scoring regression models"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/scoring-regression.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Working with experiments", "Reviewing models", "Understanding model review concepts", "Interpreting model scores"]
---

# Scoring regression models

Regression models predict outcomes as a number, indicating the model’s best estimate of the target variable. Several metrics are generated for you to evaluate regressions models.

## R2

R squared (R2) is a unitless measure of correlation of the features to the target. It can be expressed as: what percent closer to perfect are the model’s predictions compared to using the average value of the target?

R2 ranges from negative infinity to 1. The closer to 1, the more the variance in the target value can be explained by the feature variables. In other words, the more likely it is that you have feature important variables that would lead to accurate predictions.

The charts show an example of height plotted against age. Height is more closely correlated to age in the first chart, where R2 is 0.97, than in the second chart, where R2 is 0.56.

Two charts plotting height versus age with different R2 values

![Two graphs with different R2 values.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/AutomatedMachineLearning/r-squared.png "Click to view full size")

Note that a lower R2 value doesn't necessarily mean that it is a bad model. How you interpret R2 depends on the use case and the data. When considering regression model scoring, it's important to remember that a linear relationship isn't always critical. If linear regression is producing poor results while other algorithms have better performance, it might simply mean that your data can't be modeled well enough by a linear relationship.

## RMSE

Root mean squared error (RMSE) can be interpreted as the average +/- difference expected between a predicted value and the actual value. It is the standard deviation of residuals (the difference between the observed value and the predicted value for a feature). RMSE is measured in the same unit as the target value.

As an example, say that our target is to predict contract value and we get RMSE = 1250. This means that, on average, the predicted value differs +/- $1,250 from the actual value.

## MSE

Mean squared error (MSE) can be interpreted as the squared +/- difference between the predicted value and the actual value that we would expect to see on average. It is measured in the same unit as the target value squared.

In the example with contract value prediction, an MSE value of 1562500 would mean that model is off by +/- 1,562,500 $2. Note that the unit is dollars squared.

## MAE

The mean absolute error (MAE) is the average of all absolute prediction errors, where the prediction error is the difference between the actual and the predicted value. Using the absolute value of prediction errors prevents +/- errors from canceling each other out. MAE is measured in the same unit as the target value.

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
