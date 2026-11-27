---
title: "Understanding model algorithms"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/algorithms.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Working with experiments", "Reviewing models", "Understanding model review concepts"]
---

# Understanding model algorithms

An algorithm is a mathematical recipe that produces a model. It takes an input—your dataset—and produces an output—the model. Each algorithm has different strengths and weaknesses.

When you choose a target, Qlik Predict automatically selects the best algorithms for the use case. The target determines what kind of algorithms to use.

Algorithms that work best with binary and multiclass classification problems are used when:

- The target has only two unique values, as in "Will a customer cancel their subscription?"—Yes or No.
- The target is a string value with between three and ten unique values. For example, determining the optimal campaign mix with the target being one of "red", "blue", "green", or "yellow".

Algorithms that work best with regression problems are used if the target is a numerical column. Forecasting how much a customer will purchase is an example of a regression problem.

## Algorithms for binary and multiclass classification problems

Qlik Predict uses the following algorithms for binary and multiclass classification problems:

- CatBoost Classification
- Elastic Net Regression
- Gaussian Naive Bayes
- Lasso Regression
- LightGBM Classification
- Logistic Regression
- Random Forest Classification
- XGBoost Classification

## Algorithms for regression problems

Qlik Predict uses the following algorithms for regression problems:

- CatBoost Regression
- LightGBM Regression
- Linear Regression
- Random Forest Regression
- SGD Regression
- XGBoost Regression

## Algorithms for time series problems

Qlik Predict uses the following algorithms for time series problems:

- Time-series DeepAR
- Time-series Mixer
- Time-series Dense Encoder

## Different types of models

The model types can be divided into regression models, ensembles, time series models, and other types of machine learning models.

### Regression models

Regression models, or general linear models, are models that look for trends along the domain of each variable independently of one another. Like the algebraic equation y = mx+b, the algorithm is looking to choose an m and a b that will produce the highest accuracy, on average, for each x and y value. It is generally the same concept when there are more than one variable. Linear regression and logistic regression are examples of regression models for regression problems and classification problems, respectively.

For classification problems, the regression model output is the probability that the sample is the positive class. This means that y equals the probability and not an actual value.

Regressions are good at finding linear trends in data, but sometimes there is a relationship that isn’t linear. For a regression to be able to fit well to a non-linear pattern, data transformation is needed before training the model. The benefit of the strong understanding of linear relationships is that linear relationships generally do the best with [extrapolation](extrapolation-interpolation.htm). The table lists pros and cons for regression models.

| Pros | Cons |
| --- | --- |
| - Good at extrapolating - Good at finding linear trends to independent variables - Good with large data from the same population - Simple to understand | - Poor at exploiting patterns between variables - Poor at fitting non-linear trends - Sometimes too simplistic |

### Ensemble models

Ensembles are when multiple models are combined. This could be compared to a group of people with different backgrounds voting and using the average vote to decide. Random Forest and XGBoost are examples of ensemble models.

Ensembles can solve both regression problems and classification problems. They are good at finding non-linear relationships and at finding out how interactions between variables affect the target. Although ensembles are good at learning the patterns within the range of data on which they are trained, they perform poorly at predicting for values outside of the range they have seen. The table lists pros and cons for ensemble models.

| Pros | Cons |
| --- | --- |
| - Good at exploiting patterns between variables - Good at finding non-linear trends - Good with large data from the same population | - Poor at extrapolating - Not as easy to interpret |

### Time series models

Time series models are trained with deep learning algorithms that use GPU acceleration and neural network-based methods. These models are trained to produce predictions corresponding to specific dates and times. Time series models support predictions involving multivariate targets, as well as static, past, and future covariates.

Time series models require large amounts of computing power.

### Other model types

Other model types include all other model types. Examples include Nearest Neighbors and Gaussian Naive Bayes. These types of models are generally trying to create a new spatial representation of the data, often doing this by creating some type of distance metric that measures how different two records are. They can be good at handling non-linear trends but are computationally much more expensive as the dataset size increases. The table lists pros and cons for other models.

| Pros | Cons |
| --- | --- |
| - Good at exploiting patterns between variables - Good at finding non-linear trends | - Poor at extrapolating - Computationally more expensive on larger datasets |
