---
title: "Creating new feature columns"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/feature-engineering.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Understanding machine learning", "Getting your dataset ready for training"]
---

# Creating new feature columns

Feature engineering is the process of creating new feature columns from current ones. It can help you gain additional predictive power from the source data that you have collected to answer a business question.

For example, a customer’s address would be excluded from the training data due to high cardinality. Instead of using the address, we could feature engineer a distance column. If we know the customer address together with various store locations, the distances to the stores can be calculated. The new columns will have a numerical value that can be used to uncover measurable patterns in the data.

You can perform feature engineering on your dataset in preparation for use in Qlik Predict. Additionally, Qlik Predict suggests new features which can be generated automatically from existing features.

New columns for distances to different stores

![Table with sample data.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/AutomatedMachineLearning/feature-engineering-distance-table.png "Click to view full size")

Review the features in your dataset to determine possible issues that might exist or improvements that can be made. Engineering good features requires skill and business experience. You want features expressed in a way that directly ties to the target column.

Things to consider:

- Should time factor into the feature?
- Does rate of change matter?
- Should a feature be normalized to account for differences across subsets of data?
- Do null values mean something?

## Auto-engineered features

With automatic feature engineering, new features are automatically created from existing ones.

Qlik Predict generates auto-engineered features from columns which contain date and time information. These new features separate each component of the column values into their own features.

In addition, special processing can be applied to columns containing free text. The original free text features are transformed into new features to improve model training.

Auto-engineered features improve the predictive and analytical value of your models as you train them. For more information, see [*Automatic feature engineering*](automatic-feature-engineering.htm).

## Examples: Engineering features

Use the following examples to begin brainstorming around how to engineer features that can enhance the predictive nature in your data.

### Will a sales opportunity close?

The target column is whether the sales opportunity closed (Yes or No).

- Original feature: Number of meetings
- Alternative features: Meetings per month or number of meetings in a specific stage

Transforming the measure to meeting frequency better accounts for change. Measuring meetings at a specific stage in the sales process better expresses sales momentum and accounts for cycle.

### Predict a future transaction amount

The target column is the amount of the next transaction.

- Original feature: Amount of last order
- Alternative features: The average order amount or the percentage change in order amount

The average amount gives you a broader account of order behavior. The change in buying pattern provides a normalized value.

### Will a customer churn?

The target column is whether the customer will churn (Yes or No).

- Original feature: Customer sentiment
- Alternative features: Change in customer sentiment or number of days with the current sentiment

Measuring the change in sentiment is more likely to lead to action. The number of days gives the duration of the current state.

### Will an employee voluntarily term?

The target column is whether an employee will terminate (Yes or No).

- Original feature: Salary
- Alternative features: Salary compared to peers or salary compared to the industry average

Comparing the salary to peers better aligns to the employee’s experience or sentiment. The comparison with the average salary for the industry better aligns to the employee’s opportunity cost.

### Will a lead convert to an opportunity?

The target column is whether a lead is converted (Yes or No).

- Original feature: How did you find us?
- Alternative features: Answered (Yes or No)

The action is what matters here and not what the answer was. Note that in this case, nulls mean something: inaction.

### Dates

With Qlik Predict's automatic feature engineering functionality, the components of dates and timestamps are automatically parsed into separate columns.

Dates can also be engineered in many other ways to create several features in one dataset, such as:

- Aggregate dates into seasons, quarters, or semesters.
- Calculate date difference, for example, number of days since the last purchase.
