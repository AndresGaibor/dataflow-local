---
title: "Overriding task settings for individual datasets when publishing to Kafka"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/TargetConnections/kafka-dataset-settings.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Managing datasets"]
---

# Overriding task settings for individual datasets when publishing to Kafka

When publishing to Kafka, you can override the data message publishing and message format task settings for individual datasets.

To do this:

1. Open the task. In the Datasets tab, click the![More icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_catmore_vertical.svg)menu to the right of the dataset and select Settings.

   The Dataset settings: <dataset name> dialog opens.
2. To override the data message publishing settings, select the Data message publishing tab and continue as described in [*Overriding data message publishing settings*](#Overridi2) below.
3. To override the message format settings, select the Message format tab and continue as described in [*Overriding message format settings*](#Overridi) below.

## Overriding data message publishing settings

For each setting, the current task setting is indicated by the field Task setting: <setting> (for example, Task setting: Specific topic).

For a description of these settings, see [*Data message publishing*](../Replicating/replicating-settings.htm#Data3).

You can either retain the task setting or use the Expression Builder to specify a custom topic, message key, or partition key.

To use the Expression Builder:

1. Select the Custom topic, Custom message key, or Custom partition key field as appropriate, and click ![Expression icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression.svg).

   Information noteCustom topics must already exist or the broker must be configured to create them.

   The Expression Builder opens.
2. Build an expression.

   You can use columns in the dataset, functions, and operators to build the expression.

   Click ![Right arrow icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_right.svg) to move an item to the expression.

   You can also use all functions supported by Kafka in the expression.
3. Click Extract parameters.

   You can now add a test value to Value to test for all parameters.
4. Click Test expression.

   You should now see the result of the expression, using the test values.
5. When you are ready, click OK.

   The expression is added to the field.

### Building expressions

You need to build an expression that defines custom values. You can use:

- Columns

  All columns in the source dataset.
- Functions

  String functions, numeric functions, null check functions, data and time functions, and logical functions.
- Operators

  Mathematical and logical operators. Some operators are also available in the toolbar above the expression. This is also where you find the operator for string concatenation, ||.

Click ![Right arrrow icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_right.svg) to move an item to the expression.

You can also use all functions supported by Kafka in the expression.

## Overriding message format settings

To override the task message attributes for this dataset, enable Use custom settings, and then configure the settings as described in [*Message attributes*](../Replicating/replicating-settings.htm#Message).
