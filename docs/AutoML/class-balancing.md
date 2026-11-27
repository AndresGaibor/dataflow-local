---
title: "Class balancing"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/class-balancing.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Understanding machine learning", "Getting your dataset ready for training"]
---

# Class balancing

In a binary classification problem, there might be more data collected for one of the two classes. This uneven balance between the classes leads to the model learning more about the majority class than the minority class. You can use class balancing to improve the model.

## What is class balance

In a dataset for binary classification there are two classes. Class balance is the relative frequency of those classes.

If you flipped a perfectly random coin enough times, you would get a perfectly balanced set of two classes (heads and tails). The average class value is 0.5 in a perfectly balanced case (where one class is 1 and the other class is 0).

Two perfectly balanced classes

![Bar chart with two balanced classes.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/AutomatedMachineLearning/class-balancing-1.png "Click to view full size")

In many cases the class balance will not be equal. This could lead to the model learning more about the majority class than the minority class.

Examples of classes with unequal balance

![Bar chart with classes that are unequally balanced.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/AutomatedMachineLearning/class-balancing-2.png "Click to view full size")

## Proportional bias

A model can be very accurate by guessing the majority class in unbalanced data. For example, if 95 percent of website visitors don’t make a purchase, a model can be 95 percent accurate by saying that no one will purchase. The model learns about the majority class, but it's often more important to learn about the minority class. For example, why do the other 5 percent of the visitors to the website make purchases?

## Effects from class balancing

By performing class balancing on your data, you might get a model that is more feature-focused and that has learned more about the minority class. Potential effects on the model include:

- Higher F1 score because the weight of the minority class has increased.
- Marginally lower overall accuracy score because it is not relying on proportional bias as much.
- A more informative model because it is relying more on the features and how to distinguish the classes as being separate. The SHAP values might be more informative in a class-balanced model.

Note that in small datasets, class balancing could cause a loss of feature data. Also, by changing the proportions in the dataset, some information might be lost, which could bias model predictions.

## How to class balance

To class balance the data, you first need to find out what the ideal balance is for your specific business case. Anywhere from 80/20 to 50/50 could be needed. Balance just enough to get what you need because over-tuning of class balancing could lead to an overfit model. Then test the model with manual holdouts.

### Oversampling

Oversampling is often needed when your minority class does not have enough data.

With oversampling, data records are added to represent the minority class. Specifically, it involves taking multiple samples of the minority class and adding them to the original dataset.

The result is a dataset in which the majority and minority classes are more well-balanced.

Oversampling of the minority class (blue) to get an equal balance with the majority class (green)

![Illustration of oversampling.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/machine-learning_oversampling.png "Click to view full size")

### Undersampling

Use undersampling when you have too much data, particularly for the majority class.

With undersampling, the majority class is randomly sampled so that it comes into better balance with the minority class. The figure illustrates how samples are taken from the majority class in the original dataset to get a dataset with balanced classes.

Undersampling of the majority class (blue) to get an equal balance with the minority class (green)

![Illustration of undersampling.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/machine-learning_undersampling.png "Click to view full size")

## Automatic class balancing in Qlik Predict

This help topic mainly outlines how you can manually perform class balancing if needed. If you are training models using [intelligent model optimization](#glossary-0 "Glossary term") (activated by default in new [ML experiments](#glossary-1 "Glossary term")), Qlik Predict automatically performs class balancing during the training process.

For more information about imbalance detection and the specific processing used, see [*Class balancing*](intelligent-model-optimization.htm#ClassBal).
