---
title: "Understanding feature importance"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/feature-importance.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Working with experiments", "Reviewing models", "Understanding model review concepts"]
---

# Understanding feature importance

Feature importance measures how much impact each [feature](machine-learning-framework.htm) has on the target. It can help you identify dataset issues and improve the model. Feature importance is comprised of two distinct visualizations: permutation importance and SHAP importance.

The simplistic interpretation of feature importance is that changing the most feature important variable will change the target variable more than by changing any other variable. Changing two of the most feature important variables will likely have a greater impact than only changing one, but the principle is that something with very low feature importance probably doesn’t have much predictive power. Controlling or changing it might not make a difference.

## Using feature importance

Feature importance can be helpful in identifying problems with the data being used to train the model. For example, let's say we are trying to predict whether or not a sales opportunity will close, and we forget to exclude a column containing the sale's closing date. That would probably be the most predictive column and therefore have the highest feature importance. Including it would cause the model to perform better than it would in real life, because when we try to predict the binary outcome of whether a sale closes or not, we will not have access to the closing date.

Feature importance can also help you find ways to make a model iteratively better. The most feature important values can sometimes be a good base to segment on. As an example, maybe an autopay flag is very feature important. We could use this feature to segment the data and train one model on customers that are set up for autopay and another model on customers without autopay. The two models might be able to do a better job than our first model.

In other cases, you might be able to capture or engineer features that better represent what a more feature important variable describes—without adding redundancy. For example, a very feature important variable might be the product family that a business is producing. Breaking the product family into a few more descriptive features about the products could be more significant.

## Comparing permutation importance and SHAP importance

Permutation importance and SHAP importance are alternative ways of measuring feature importance. The main difference is that permutation importance is based on the decrease in model performance, while SHAP importance is based on magnitude of feature attributions.

### How to use the values

Permutation importance can be used to:

- Understand which features to keep and which to exclude.
- Check for data leakage.
- Understand what features are most important to model accuracy.
- Guide additional feature engineering.

SHAP importance can be used to:

- Understand which features most influence the predicted outcome.
- Dive into a feature and understand how the different values of that feature affect the prediction.
- Understand what is most influential on individual rows or subsets within the data.

### Data level

Permutation importance is calculated on the entire dataset. Specifically, how much the accuracy of the whole dataset changes by eliminating a feature. It cannot be used to understand influence on individual rows.

SHAP importance is calculated on row level and can be used to understand what is important to a specific row. The values represent how a feature influences the prediction of a single row relative to the average outcome in the dataset.

### Influence of feature values

Permutation importance cannot be used to understand which values within a feature are most important.

SHAP importance values can be used to understand how the values within a specific feature influence the outcome.

### Direction

Permutation importance does not include a direction.

SHAP importance values are directional. They can be positive or negative depending on which direction they influenced the predicted outcome.

### Magnitude

The magnitude of permutation importance measures how important the feature is to the overall prediction of the model.

The magnitude of the SHAP importance is how much a specific feature influences a row's prediction to be different from the average prediction for the dataset.
