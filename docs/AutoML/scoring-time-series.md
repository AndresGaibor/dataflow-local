---
title: "Scoring time series models"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/scoring-time-series.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Working with experiments", "Reviewing models", "Understanding model review concepts", "Interpreting model scores"]
---

# Scoring time series models

Time models predict outcomes as numbers corresponding to specific future dates. Several metrics are generated for you to evaluate time series models.

## MASE

MASE stands for mean absolute scaled error. MASE is one of the key metrics used to score and recommend time series models in Qlik Predict.

In Qlik Predict, MASE is determined by comparing the mean absolute error ([*MAE*](#MAE)) of a forecast to the MAE of a naive forecast. The naive forecast uses the last available value as the forecasted value for all future steps.

## MAE

MAE stands for mean absolute error. Along with [*MASE*](#MASE), MAE is one of the key metrics used to score and recommend time series models in Qlik Predict. MAE measures model quality by calculating the rate of error within forecasts created by the model.

## MAPE

MAPE stands for mean absolute percentage error.

## WMAPE

WMAPE stands for weighted mean absolute percentage error.

## RMSE

Root mean squared error (RMSE) can be interpreted as the average +/- difference expected between a predicted value and the actual value. It is the standard deviation of residuals (the difference between the observed value and the predicted value for a feature). RMSE is measured in the same unit as the target value.

As an example, say that our target is to predict contract value and we get RMSE = 1250. This means that, on average, the predicted value differs +/- $1,250 from the actual value.

## MSE

MSE stands for mean squared error.

## SMAPE

SMAPE stands for symmetric mean absolute percentage error.

## MDAPE

MDAPE stands for Median absolute percentage error.

## MNRMSE

MNRMSE stands for mean root mean squared error.

## MDNRMSE

MDNRMSE stands for median root mean squared error.

## Prediction speed

Prediction speed is a model metric that applies to all model types: binary classification, multiclass classification, regression, and time series. Prediction speed measures how fast a machine learning model is able to generate predictions.

In Qlik Predict, prediction speed is calculated using the combined feature computing time and test dataset prediction time. It is displayed in rows per second.

Prediction speed can be analyzed in the Model metrics table after running your experiment version. You can also view prediction speed data when analyzing models with embedded analytics. For more information, see:

- [*Analyzing the model metrics tables*](analyze-models-quick.htm#Analyzing)
- [*Comparing models*](analyze-models-compare.htm)

### Considerations

The measured prediction speed is based on the size of the training dataset rather than the data on which predictions are made. After deploying a model, you might notice differences between how fast predictions are created if training and prediction data differ greatly in size, or when creating real-time predictions on one or a handful of data rows.
