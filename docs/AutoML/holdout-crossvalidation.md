---
title: "Holdout data and cross-validation"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/holdout-crossvalidation.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Working with experiments", "Configuring experiments", "Automatic data preparation and transformation"]
---

# Holdout data and cross-validation

One of the biggest challenges in predictive analytics is to know how a trained model will perform on data that it has never seen before. Put in another way, how well the model has learned true patterns versus having simply memorized the training data. Holdout data and cross-validation are effective techniques to make sure that your model isn’t just memorizing but is actually learning generalized patterns.

When configuring your experiment, you can choose whether the training data and holdout data are split randomly or with a special method used to create time-aware models.

## Testing models for memorization versus generalization

Asking how well a model will perform in the real world is equivalent to asking whether the model memorizes or generalizes. Memorization is the ability to remember perfectly what happened in the past. While a model that memorizes might have high scores when initially trained, the predictive accuracy will drop significantly when applied to new data. Instead, we want a model that generalizes. Generalization is the ability to learn and apply general patterns. By learning the true broader patterns from training data, a generalized model will be able to make the same quality predictions on new data that it has not seen before.

## Automatic holdout data

A holdout is data that is "hidden" from the model while it is training and then used to score the model. The holdout simulates how the model will perform on future predictions by generating accuracy metrics on data that was not used in training. It is as though we built a model, deployed it, and are monitoring its predictions relative to what actually happened—without having to wait to observe those predictions.

In Qlik Predict, there are two methods of selecting the holdout data: the default method, and the time-based method.

### Default method of selecting holdout data

Unless you turn on time-aware model training, holdout data is selected randomly before model training starts.

By default, the dataset is split randomly into training data and holdout data

![Ratio of training data and holdout data in the default method of holdout and cross validation](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/AutomatedMachineLearning/holdout-data-default.png "Click to view full size")

### Time-based method of selecting holdout data

With the time-based method, the entire training dataset is first sorted according to a date index column that you select. After sorting, the holdout data is separated from the rest of the training data. This holdout data contains the most recent data with respect to your selected index.

The time-based method is used when training time-aware models and time series models. For more information about these model options, see [*Creating time-aware models*](time-aware-models.htm) and [*Working with time series experiments*](time-series-experiment.htm).

In the time-based method, the dataset is split into training data and holdout data in the same proportions as the default method. However, in this method, the data is also sorted prior to the split.

![Ratio of training data and holdout data in the default method of holdout and cross validation. Additionally, the diagram shows that the entire dataset is sorted along the selected date index and this affects which data is separated as the holdout set](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/AutomatedMachineLearning/holdout-data-time-based.png "Click to view full size")

## Cross-validation

Cross-validation is a process that tests how well a machine learning model can predict future values for data it has not yet seen. In cross-validation, the training data for a model is split into a number of segments, called folds. During each iteration of the training, the model is trained on one or more folds, with at least one of the folds always prevented from being used for training. After each iteration, the performance is evaluated using one of the folds that was prevented from use in training.

The outcome of cross-validation is a set of test metrics that give a reasonable forecast of how accurately the trained model will be able to predict on data that it has never seen before.

In Qlik Predict, there are two methods of cross-validation: the default method and the time-based method.

## Default cross-validation

Unless you configure the training to use time-based cross-validation, Qlik Predict uses the default method of cross-validation. The default method of cross-validation is suitable for models that do not rely on a time series dimension – that is, you do not need the model to predict with consideration to a specific time-based column in the training data.

In the default method of cross-validation, the dataset is randomly split into a number of even segments, called folds. The machine learning algorithm trains the model on all but one fold. Cross-validation then tests each fold against a model trained on all of the other folds. This means that each trained model is tested on a segment of the data that it has never seen before. The process is repeated with a different fold being hidden during training and then tested until all folds have been used exactly once as a test and been trained on during every other iteration.

### Automatic holdout and default cross-validation

By default, Qlik Predict uses five-fold cross-validation during the model training to simulate model performance. The model is then tested against a separate holdout of the training data. This generates scoring metrics to let you evaluate and compare how well different algorithms perform.

1. Before the training of your experiment starts, all data in your dataset that has a non-null target is randomly shuffled. 20 percent of your dataset is extracted as holdout data. The remaining 80 percent of the dataset is used to train the model with cross-validation.
2. To prepare for cross-validation, the dataset is split into five pieces—folds—at random. The model is then trained five times, each time "hiding" a different fifth of the data to test how the model performs. Training metrics are generated during the cross-validation and is the average of the computed values.
3. After the training, the model is applied to the holdout data. Because the holdout data has not been seen by the model during training—unlike cross-validation data—it's ideal for validating the model training performance. Holdout metrics are generated during this final model evaluation.

For more information about metrics used to analyze model performance, see [*Reviewing models*](reviewing-experiments.htm).

In the default method, the training data is used during a five-fold cross-validation to generate a model. After the training, the model is evaluated using the holdout data.

![Diagram showing the default method of holdout and cross-validation, highlighting a five-fold process. Training data is used for cross validation and holdout data for final model evaluation.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/AutomatedMachineLearning/holdout-cross-validation-default.png "Click to view full size")

## Time-based cross-validation

Time-based cross-validation is suitable for training your model to predict data along a time series dimension. For example, you want to predict your company's sales for the next month, given a dataset containing past sales data. To use time-based cross-validation, there has to be a column in your training data that contains date or timestamp information.

Time-based cross-validation is used to create time-aware models. You activate time-aware training under Model optimization in the experiment configuration panel. For more information, see [*Configuring experiments*](configuring-experiments.htm).

With time-based cross-validation, models are trained to better understand that they are predicting data for future dates.

Like the default method, time-based cross-validation involves separating the training data into folds that are used for both training and testing. In both methods, models are also trained over a number of iterations. However, the time-based method has several differences from the default method:

- Training data is sorted and organized into folds along the date index you pick. By contrast, default cross-validation randomly selects which rows are included in any given fold.
- The number of folds being used as training data increases gradually with each iteration of the training. This means that during the first iteration, only the first (oldest) fold might be used, with subsequent iterations gradually containing a larger volume of training data, including more recent data. The fold being used as test data varies with each iteration.

  This contrasts with the default cross-validation method, which uses a fixed volume of data for train and test splits in each iteration (that is, four folds for training and one fold for testing).
- Because the entire training dataset is sorted along your selected index, the data being used to test the trained model is always more recent – or equally as recent – than the data used to train the model. The automatic holdout data that is used to perform the final performance tests on the model is always more recent – or equally as recent – than the rest of the training dataset.

  By contrast, the default cross-validation can result in models being tested on data that is older than the training data, resulting in data leakage.

### Automatic holdout and time-based cross-validation

This procedure shows how time-aware models are trained. The process has differences and similarities compared to the [default cross-validation process](#Default).

1. All data in your dataset is sorted along the date index you have selected. This includes the training data and holdout data.
2. Before the training of your experiment starts, 20 percent of your dataset is extracted as holdout data. This holdout data is the more recent, or equally as recent, as the rest of the dataset. The remaining 80 percent of the dataset is used to train the model with cross-validation.
3. To prepare for cross-validation, the sorted training data is split into a number of folds. With respect to the date index you select, the first fold would contain the oldest records and the last fold would contain the most recent records.
4. The model is then trained over five iterations. In each iteration, the amount of training data is gradually increased. With each iteration, the recentness of the included training data is also increased. Training metrics are generated during the cross-validation and is the average of the computed values.
5. After the training, the model is applied to the holdout data. Because the holdout data has not been seen by the model during training, it's ideal for validating the model training performance. Holdout metrics are generated during this final model evaluation.

In the time-based method, the sorted training data is used to generate and test a time-aware model. After the training, the model is evaluated using the holdout data.

![Diagram showing the default method of holdout and cross-validation, highlighting a five-fold process. Training data is used for cross validation and holdout data for final model evaluation.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/AutomatedMachineLearning/holdout-cross-validation-time-based.png "Click to view full size")

## Holdout and cross-validation for time series models

A time series model is a specific type of model that performs time-specific forecasts. The training process for these models has some similarities and differences when compared to other models:

- As with other models, the training dataset is still split into 80 percent (train) and 20 percent (test). The [time-based splitting method](#TimeBasedSplit) is used.

  The test set is used to evaluate model performance. This set is surfaced in the Analyze tab in the experiment, where you can explore how well the model generalizes beyond its training window.
- Five-fold cross-validation is not used. Some validation is performed during the training process itself, as the data is run through a neural network.

For more information about time series forecasting with Qlik Predict, see [*Working with time series experiments*](time-series-experiment.htm).
