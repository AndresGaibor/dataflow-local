---
title: "Interpreting model scores"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/scoring-models.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Working with experiments", "Reviewing models", "Understanding model review concepts"]
---

# Interpreting model scores

Model scores are technical measures of how well your models are able to predict the training data. In addition to feature importance, model scores are a key aspect of model analysis.

## Model scoring metrics

The key metrics to use for model scoring varies according to the problem type. The problem type can be binary classification, multiclass classification, or regression. For more information, see the following help topics:

- Binary classification problems: [*Scoring binary classification models*](scoring-binary-classification.htm)
- Multiclass classification problems: [*Scoring multiclass classification models*](scoring-multiclass-classification.htm)
- Regression problems: [*Scoring regression models*](scoring-regression.htm)
- Time series problems: [*Scoring time series models*](scoring-time-series.htm)

## Why model scoring is important

The purpose of the different model scores is to understand the strengths of the model. This will increase your confidence in the usability of the model and show what improvements can be made. If scoring is very high or very low, it could indicate that there is an issue with the data being fed to the model.

Scoring a model is a challenging task because there are several metrics that describe different things about the model. To know if it is a good model, you need to combine business domain knowledge with an understanding of the various scoring metrics and data that the model was trained with. What could look like a terrible score in one use case, might be a great score and generate a high return on investment in another use case.

### The most important metric: A car analogy

Which metric is most important? That depends on how you plan to use the model. There is not a single metric that can tell you everything you want to know.

As an analogy, think about buying a car. There are a lot of different metrics to consider such as fuel efficiency, horsepower, torque, weight, and acceleration. We might want them all to be great, but we must make trade-offs depending on how we plan to use the car. A commuter might want a car with high fuel efficiency even if it means low torque, while a boat owner might choose high torque even if it means lower fuel efficiency.

A model can be thought of the same way. We want all of the metrics to be high—and we might be able to improve them with more data and better features—but there are always constraints and trade-offs to be made. Some scores matter more depending on what you intend to do with the model.

## Is the model a good fit?

Determining if a model is a good fit for the use case and good to be put into production, ultimately boils down to the question: "Is the model accurate enough to make a positive return on investment without unacceptable consequences?" The following four questions can help you to break it down.

### Is the model informing a human decision or automating it?

The required accuracy depends on whether you will use the model to automate or inform decisions. For example, a model can be trained to determine how much money employees should make. In this case, accuracy will probably need to be higher if the model is automating the decision compared to if it's only informing a decision. If managers use it to discover whether an employee is underpaid or overpaid, they can then use their own discretion to determine if the model is in error or not.

### Is there a quantifiable cost to a false positive or a false negative?

Are you able to quantify the cost of a false outcome? Take that cost into account when you determine the level of accuracy required to consider the model a good fit.

Using the same example as above, say that the model is simply informing. However, the manager trusts the model and doesn’t give an employee a pay raise because the model outputs that the employee would be overpaid if a raise was given. The employee then resigns to work elsewhere. What was the cost of losing that employee? If the reverse happened, what would the cost have been of falsely giving a raise?

### How much better is the model than random?

For regression problems, determine what the error would be if you always assumed the average value of the target column. How much better is the model compared to that?

For classification problems, take the rate of the positive class squared and add it to the rate of the negative class squared to get random accuracy. How much better is the model accuracy than that?

### Is the model better than making an ultimatum?

Depending on if there is a cost associated with errors, consider whether the model is better than an ultimatum. For example, say that a firm is doing free consultations that are expensive and time consuming ($6,000) but makes good money when a deal closes ($60,000). The firm currently operates under the assumption that 100 percent of consultations will close. However, they would make better profit if they could determine which consultations they should do and which they shouldn’t do. What does the model accuracy need to be in order for the firm to use the model output instead of the ultimatum that 100 percent of the deals will close?

## Feature importance

While feature importance values are not technically considered model scores, they are key metrics for evaluating the predictive performance of your models. Evaluating feature importance can also help identify issues with your experiment configuration and training data, such as [data leakage](#glossary-0 "Glossary term").

For more information, see [*Understanding feature importance*](feature-importance.htm).
