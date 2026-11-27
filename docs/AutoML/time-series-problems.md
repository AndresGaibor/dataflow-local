---
title: "Time series problems"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/time-series-problems.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Understanding machine learning", "Defining machine learning questions"]
---

# Time series problems

Time series machine learning problems involve leveraging historical data to forecast numerical metrics for specific dates and times.

## Comparing regression and time series problems

Regression problems are similar to time series problems in both the target variable and the real-world use cases they involve. There are also several differences between these two problem types.

For more information about regression problems, see [*Regression problems*](regression-problems.htm).

### Similarities

- Both involve a numerical target column.
- Both are commonly used in financial use cases involving sales and monetary forecasting.

### Differences

- Time series problems support grouped targets, while regression problems do not (see [*Components of a time series problem*](machine-learning-framework-time-series.htm#Components)). Grouped scenarios can still be addressed for regression problems by training multiple different models, at the cost of global learning across groups.
- Time series problems support scenarios where you know certain feature variables ahead of time—for example, weather-related forecasts, planned promotional discounts, and whether dates fall on week days, weekends, and holidays. These feature variables are known as [*Future features*](machine-learning-framework-time-series.htm#FutureFeatures).
- For time series problems, data must be indexed by date or datetime on a fixed time interval. Also, different data content is expected and generated during training and predictions (see [*Preparing a training dataset*](machine-learning-framework-time-series.htm#TrainPrepare) and [*Preparing an apply dataset*](machine-learning-framework-time-series.htm#ApplyPrepare)).
- In time series problems, predicted values explicitly correspond to specific dates and times. In regression problems, predicted values may or may not correspond to specific dates and times, but if they do, this association is implied rather than explicitly denoted in output.
- Different algorithms are used (see [*Understanding model algorithms*](algorithms.htm)).

## Time series example: Future sales

This example presents a high-level of the data you need to collect and provide for a time series problem. To learn more about developing frameworks for time series problems, see [*Working with multivariate time series forecasting*](machine-learning-framework-time-series.htm).

In this example, the goal is to forecast daily sales for the next four days. In addition, it has been requested that daily sales totals are predicted for each region and product group. With the need for sales by region and product group, a multivariate time series problem has been established.

To start, data is collected and aggregated to train the model. The requirement is that a total sales amount, per region and product group, is presented for each day within a specific time range. In addition, it is desired to provide how many products are available on promotion per day for each region and product group.

Sample of collected data

| Date | Products on Promotion | Region | Product Group | Sales |
| --- | --- | --- | --- | --- |
| 2025-01-01 | 100 | North America | Grocery | 99642.10 |
| 2025-01-01 | 31 | South America | Product | 34660.34 |
| 2025-01-01 | 11 | North America | Deli | 60345.44 |
| 2025-01-01 | 14 | South America | Grocery | 44603.33 |
| 2025-01-01 | 76 | North America | Product | 105844.44 |
| 2025-01-01 | 133 | South America | Deli | 150385.44 |
| 2025-01-02 | 17 | North America | Grocery | 80195.22 |
| 2025-01-02 | 35 | South America | Product | 61051.13 |
| 2025-01-02 | 24 | North America | Deli | 55938.38 |
| 2025-01-02 | 118 | South America | Grocery | 104823.33 |
| 2025-01-02 | 40 | North America | Product | 11111.12 |
| 2025-01-02 | 73 | South America | Deli | 15493.33 |

Suppose the last date for which historical data is available is 2025-10-09. Theoretically, after training, deploying, and predicting with a time series model for this use case, you could expect the following predictions.

Sample of predicted data

| Date | Products on Promotion | Region | Product Group | Sales |
| --- | --- | --- | --- | --- |
| 2025-10-10 | 0 | North America | Grocery | 193803.15 |
| 2025-10-10 | 14 | South America | Product | 76666.66 |
| 2025-10-10 | 55 | North America | Deli | 30593.55 |
| 2025-10-10 | 2 | South America | Grocery | 10549.33 |
| 2025-10-10 | 1341 | North America | Product | 100003.33 |
| 2025-10-11 | 0 | South America | Deli | 70001.87 |
| 2025-10-11 | 0 | North America | Grocery | 39522.11 |
| 2025-10-11 | 150 | South America | Product | 91859.30 |
| 2025-10-11 | 65 | North America | Deli | 19583.55 |
| 2025-10-11 | 12 | South America | Grocery | 194863.00 |
| 2025-10-11 | 70 | North America | Product | 140244.13 |
| 2025-10-11 | 15 | South America | Deli | 76666.66 |
| 2025-10-12 | 20 | North America | Grocery | 30593.55 |
| 2025-10-12 | 20 | South America | Product | 10549.33 |
| 2025-10-12 | 39 | North America | Deli | 100003.33 |
| 2025-10-12 | 109 | South America | Grocery | 105893.99 |
| 2025-10-12 | 37 | North America | Product | 80195.22 |
| 2025-10-13 | 75 | South America | Deli | 61051.13 |
| 2025-10-13 | 190 | North America | Grocery | 55938.38 |
| 2025-10-13 | 0 | South America | Product | 104823.33 |
| 2025-10-13 | 0 | North America | Deli | 99105.99 |
| 2025-10-13 | 100 | South America | Grocery | 130533.31 |
| 2025-10-13 | 0 | North America | Product | 67676.73 |
| 2025-10-13 | 14 | South America | Deli | 100474.24 |

## Learn more

- [*Working with multivariate time series forecasting*](machine-learning-framework-time-series.htm)
- [*Working with time series experiments*](time-series-experiment.htm)
