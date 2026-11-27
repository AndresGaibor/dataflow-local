---
title: "Handling of free text data"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/free-text-handling.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Working with experiments", "Configuring experiments", "Automatic data preparation and transformation", "Automatic feature engineering"]
---

# Handling of free text data

Free text (for example, textual string data entered into forms) requires special processing by machine learning algorithms to be useful in a model. In Qlik Predict, processing of free text is a form of automatic feature engineering. Technically speaking, this processing uses the TF-IDF (term frequency - inverse document frequency) method.

Qlik Predict supports separate processing for features with free text data in English.

If a column in your training data contains free text, it is assigned the free text feature type. It can also be used as a categorical feature, although this is strongly discouraged if it has high cardinality (too many unique values).

You can select a maximum of three columns to be used as free text features in an experiment.

Information noteIt is recommended that models trained before January 23, 2024 are re-trained if they use fields which consist of free text data.

## Requirements for free text encoding

For a column containing free text to be successfully encoded as free text, it must fulfill two requirements. These requirements are checked at different stages of experiment creation.

The requirements are:

- The column must have an average character length of 50 or more characters.
- The column must have an average word length of five or more words.

## Treating a feature as free text

The process of treating a feature as free text is as follows:

1. When you select your training data, Qlik Predictidentifies features that can possibly be processed as free text. They are marked with the Possible free text insight in schema view, and will have the free text feature type.
2. After you run v1 of the experiment, additional analysis is completed. At this point, features initially marked as possible free text might be found to be unusable as free text features.

   If the features which are unusable as free text have high cardinality, it is recommended that you deselect them from the experiment. These features, when treated as categorical, contribute no value to model performance.

   If the features which are unusable as free text do not have high cardinality, you can include them in your experiment by clicking Treat as categorical, or by switching their Feature type from free text to categorical. If you leave the feature type as free text, it will also internally be treated as categorical, and will be impact encoded.

For full details about preprocessing, see [*Automatic data preparation and transformation*](preprocessing-steps.htm).

For more information about each of the insights shown in schema view, see [*Viewing insights about your training data*](dataset-insights.htm).

## Using a free text feature as the experiment target

In rare cases, a free text feature can be selected as the target. If the feature meets all requirements for free text encoding, and contains between two and ten unique values, it can be used as the target. In these scenarios, the experiment is defined as a standard binary classification or multiclass classification problem.

## Free text features in predictions

To learn about the requirements for running predictions with a deployed model trained with free text features, see [*Working with free text features in predictions*](free-text-features-predictions.htm).

## Considerations

Including free text features in your experiment increases the complexity of the experiment and the processes required to run it. It is possible that Permutation importance charts will be unavailable for the resultant models if your free text data is complex enough.

## Troubleshooting

Using free text data to train a model can be a resource-intensive process. You might encounter an error when you include free text columns containing large numbers of unique words as features.

Here are some guidelines for resolving these errors:

- Reduce the data subset in your training dataset to include fewer rows of free text.
- Remove free text features you do not need to include in model training.
- Treat one or more free text columns as categorical, rather than free text, features. Note that this is not recommended if these free text features contain high cardinality.

## Limitations

- Automatic free text feature engineering is only available for training datasets within certain size limits. For more information, see [*Training dataset and profiling limitations*](ml-limitations-capacities.htm#DatasetSizeCapacities).
- Automatic free text feature engineering is not available for time series experiments.

## Learn more

- [*Automatic feature engineering*](automatic-feature-engineering.htm)
- [*Date feature engineering*](date-feature-engineering.htm)
