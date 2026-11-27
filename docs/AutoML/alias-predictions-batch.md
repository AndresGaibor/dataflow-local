---
title: "Configuring model aliases for batch predictions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/alias-predictions-batch.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Working with ML predictions", "Creating predictions on datasets"]
---

# Configuring model aliases for batch predictions

You can select a [model alias](#glossary-0 "Glossary term") to use for predictions when creating or editing a prediction configuration. Model aliases are configured in the Prediction configuration panel.

## About model aliases

Multiple models can be added to an ML deployment. A system of aliases is available so that you can dynamically change the models used in predictions with minimal need for manual updates. Model aliases allow for advanced use cases and flexibility when generating predictive insights.

For more information, see [*Using multiple models in your ML deployment*](ml-deployment-available-models.htm).

## Configuring the model alias to use in predictions

Unless you make specific changes to the Choose model alias setting in your configuration, predictions will use the default alias in the ML deployment.

For more information about configuring batch predictions, see [*Creating predictions on datasets*](creating-predictions.htm).

Do the following:

1. Open an ML deployment and click Create prediction.
2. Add an apply dataset to the configuration.
3. In the Prediction configuration panel on the right, expand Choose model alias.
4. Use the drop down menu to select the alias to use.

   Information noteOnly aliases that have a model assigned to them are available to select. Empty aliases do not appear in this menu.
5. Continue with the remaining setup steps, and save the prediction configuration.

## Changing the models used in aliases

For information about changing the machine learning models used in each alias in your ML deployment, see [*Working with aliases*](ml-deployment-available-models.htm#Working).
