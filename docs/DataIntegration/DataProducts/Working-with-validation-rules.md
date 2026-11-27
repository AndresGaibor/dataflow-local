---
title: "Working with validation rules"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataProducts/Working-with-validation-rules.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Understanding your data with the catalog", "Assessing data quality"]
---

# Working with validation rules

A validation rule is a set of business requirements which helps you detect anomalies in datasets. It defines the values your data must comply with. A condition can be added to make the validation rule apply to some data only.

Information noteYou need one of the following subscriptions:

- Qlik Talend Cloud Enterprise
- Qlik Talend Cloud Premium
- Qlik Cloud Analytics Premium
- Qlik Cloud Analytics Enterprise
- Qlik Sense Enterprise SaaS

1. You create the validation rule as a standalone object. When you are defining the rule, you can use variables and specific values.

   As validation rules are generic, the variables let you adapt the rule to each dataset by associating variables to the fields of the dataset.

   Specific values let you use the same value in all datasets to which you applied the rule.
2. You apply the validation rule and adapt it to a field.

   You associate the variables of the validation rule with the fields. You can apply a rule to a field to validate data from other fields.
3. Before you apply the rule, a preview is displayed to show you how many values will be invalid. The invalid values are calculated from a sample of up to 100 records.
4. The validation rule validates your data by categorizing the values:
   - The values are valid. They fulfill all rule statements.
   - The values are not applicable. They do not fulfill the condition and no alternative validation expression (Else if or Else) has been defined.
   - The values are invalid. Either:
     - They fulfill the condition (If) but not the validation expression (Then).
     - They fulfill the condition (Else if) but not the corresponding validation expression (Then).
     - They fulfill neither the condition (If) nor the alternative validation expression (Else).

The following tables summarize the validation results:

Validation results with Then logic

| If | Then | Results |
| --- | --- | --- |
| Not defined | Fulfilled | Valid |
| Not defined | Not fulfilled | Invalid |

Validation results with If/Then/Else logic

| If | Then | Else | Results |
| --- | --- | --- | --- |
| Fulfilled | Fulfilled | Doesn't apply | Valid |
| Fulfilled | Not fulfilled | Doesn't apply | Invalid |
| Not fulfilled | Doesn't apply | Fulfilled | Valid |
| Not fulfilled | Doesn't apply | Not fulfilled | Invalid |
| Not fulfilled | Doesn't apply | Not defined | Not applicable |

Validation results with If/Then/Else if/Else logic

| If | Then | Else if | Then | Else | Results |
| --- | --- | --- | --- | --- | --- |
| Fulfilled | Fulfilled | Doesn't apply | Doesn't apply | Doesn't apply | Valid |
| Fulfilled | Not fulfilled | Doesn't apply | Doesn't apply | Doesn't apply | Invalid |
| Not fulfilled | Doesn't apply | Fulfilled | Fulfilled | Doesn't apply | Valid |
| Not fulfilled | Doesn't apply | Fulfilled | Not fulfilled | Doesn't apply | Invalid |
| Not fulfilled | Doesn't apply | Not fulfilled | Doesn't apply | Fulfilled | Valid |
| Not fulfilled | Doesn't apply | Not fulfilled | Doesn't apply | Not fulfilled | Invalid |
| Not fulfilled | Doesn't apply | Doesn't apply | Doesn't apply | Not defined | Not applicable |

You can apply the same validation rule to as many fields as necessary, even in the same dataset.

Information noteValidation rules depend on spaces. It means that the quality of a dataset on which you are working can be impacted by validation rules to which you do not have access.

The validation rules have effects on the quality of your dataset and the Qlik Trust Score™. For more information, see [Assessing data quality](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataProducts/Data-quality-and-data-discovery.htm) and [Qlik Trust Score™](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataProducts/Qlik-Trust-score.htm).

You can use the validation rules in Talend Studio. For more information, see [tDQRules properties](https://help.qlik.com/talend/en-US/components/8.0/validation/tdqrules).

## Creating a validation rule

You can create a rule from the Validation rules tab or when you apply a rule to a dataset. You can also create a rule from an AI-generated suggestion. For more information, see [Applying a validation rule to a dataset](#Applying-a-rule).

After you created the rule, you can apply it to datasets.

In this use case, a worker from a blood center needs to check that persons are marked as potential givers only when all donation criteria are met, and are marked as non-givers otherwise:

- Blood group is not empty and it ends with + or -.
- Age is greater or equal to 18 and less than 71.
- If age is outside the allowed range, use the If condition to validate non-givers. Use an Else if alternative for valid blood groups, and Else for all other cases.

1. Open Data quality and select the Validation rules tab.
2. If you have no validation rules, click Add. Otherwise, click Create validation rule.
3. Enter the name BloodDonation.
4. Select the space in which the rule must be stored.
5. Select the Critical severity and the Validity category. These settings let you adjust the impact of a rule on the dataset quality. For more information, see [Categories and levels of severity](#Categories-severity).
6. Enter a description. This is optional but recommended to describe the purpose of the validation rule.
7. To add conditions, toggle on Define conditions. The If, Else if, and Else sections are active.

   The Else if section is available only in pull-up mode.
8. In the If section:
   1. Enter the variable name age. You will associate this variable to a dataset field later.
   2. Select the logical operator Or.
   3. Add the conditions age < 18 and age >= 71.
9. In the first Then section:
   1. Enter the expression lower(trim($(cangive))) and select Text > = false.
10. In the Else if section:
    1. Enter the variable name bloodgroup.
    2. Select the operator Generic > Is not empty.
    3. Click Add group.
    4. Select the logical operator Or for the group and And for all conditions, at the top of the Else if section.
    5. For the group, repeat the previous steps to add the conditions on the rhesus:
       - bloodgroup Ends with +.
       - bloodgroup Ends with -.
11. In the second Then section (for Else if), enter cangive and select Text > = true.
12. In the Else section, enter the expression lower(trim($(cangive))) and select Text > = false.
13. Click Create.

## Applying a validation rule to a dataset

You can apply the same validation rule to different fields, even in the same dataset. You can also apply different rules to the same field.

1. Open a dataset.
2. Select the Data Preview tab.
3. Click a field. The right panel is displayed.
4. Click ![Apply validation rule icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add_20x20.png) from the Validation rules section.
5. Select the check box of the rule you want to apply and click Next.

   You can also create a rule from this window and apply it to the current dataset right away. You can also apply the rule to other datasets later.
6. Apply or create validation rules as follows:
   - To apply an existing rule: Select the check box of the rule you want to apply and click Next.
   - To create a rule using AI:

     Information note

     To use AI data quality validation rule generation, you must opt in to cross-region inference. This allows Qlik Cloud to send inference requests outside your tenant region.

     For details and the latest information about inference processing locations, see [*Enabling cross-region inference*](../../Admin/cross-region-data-processing.htm).
   - Use Suggest rules if you have not yet generated suggestions for this dataset.
   - Use View suggestions if rule suggestions have already been generated.
   - Click Create New and select Suggest new rules to generate new rule suggestions. The suggestions are based on up to five values from the sample to generate suggestions consistent with your data.

     The information is treated as customer data and will not be used to train Qlik Cloud or the GenAI model.

     Warning noteThis feature uses generative artificial intelligence (“GenAI”). It is the user’s responsibility to review and verify any GenAI output before using or sharing it, and to evaluate whether the use of it is appropriate for any particular use case and whether it complies with applicable laws.- To create a rule manually: You can also create a rule directly from this window and apply it to the current dataset right away.

   Information noteAny rule you directly create on a dataset will be available for you to apply to other datasets. You can find all the rules in Data quality > Validation rules.
7. Associate each variable to a field. In this use case:
   - bloodgroup associated to BloodGroup.
   - age associated to Age.
   - cangive associated to Giver.

   A preview of the rule results is displayed to let you know how many values will be invalid. The invalid values are calculated from a sample of up to 100 records.
8. To refresh the data quality automatically, select the Refresh quality check box.
9. Click Apply.
10. If you did not select Refresh quality, the rule is grayed out. Click Refresh above the right panel to apply your changes and refresh the data quality.

The rule is applied to the dataset and you can assess the quality of your dataset, and the quality of the fields to which a variable has been associated.

The icon ![validation rules](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_validation_rules_20x20.png) is displayed in the column header of the fields to which a rule applies. Hover over the icon to see how many rules apply to the field.

## Assessing the quality of the dataset and a field

You can see the percentage of invalid, non-applicable, and valid values in the quality bars. The percentage is calculated on all the data of the field, not on the sample only.

### Quality bar of the dataset

For more information on the quality of each field, do the following:

1. Open the dataset.
2. Select the Data Preview tab.
3. To open the rigth panel, click a field to which a rule is applied.

   An icon in the header helps you see when a rule applies to a field.
4. To display the percentage, hover over a color in the quality bar.
   You can see up to four colors:- Light red: Not executable values. The rule cannot be executed on those values. For example, a value is yes but the rule must validate that the value is greater than 18.
   - Red: Invalid values. Either:
     - They fulfill the condition (If) but not the validation expression (Then).
     - They fulfill the condition (Else if) but not the corresponding validation expression (Then).
     - They fulfill neither the condition (If) nor the alternative validation expression (Else).
   - Light green: Not applicable values. The values do not fulfill the condition (If) and no alternative validation expression (Else if or Else) has been defined.
   - Green: Valid values. They fulfill all rule statements.

   In this use case:

   - 21,1% of the values are invalid. For example, a person is marked as a giver but the blood group is empty.
   - 15,8% of the values are not executable. For example, the Giver value is empty for the record marked as non-executable..
   - 63,1% of the values are valid. Either:
     - The blood group is filled in, ends with + or - and the age is >= 18 < 71 and the person is marked as a giver.
     - The blood group is filled in, ends with + or - and the age is < 18 >= 71 and the person is not marked as a giver.![Quality bar of the dataset.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/validation-rule-quality-bar.png)

### Quality bar of a field

Information noteThe quality bar includes the results for the semantic types and the validation rules. For more information, see [Managing semantic types](Managing-semantic-types.htm).

1. Open the dataset.
2. Select the Data Preview tab.
3. To display the percentage, hover over a color in the quality bar.
   You can see up to three colors from left to right:- Red: Invalid values. This includes not executable values from rules.
   - Black: Empty or null values.
   - Green: Valid values. This includes not applicable values from rules.![Quality bar of a field.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/data-products-quality-bar.png)
4. For more details about each color, click it. The right panel opens and you can see the semantic type and the percentage for the validation rules.

The invalid values are marked with a red bar on the left.

![Invalid value marked in red.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/data-products-invalid-value.png)

For more details about the error, click the red bar. The error may come from a validation rule, the semantic type, or both.

## Preview of a rule

When you associate the variables to the fields, a preview of the rule results is displayed to let you test and adjust a rule before you apply it to your data. You can see how accurate and relevant the rule is.

This preview lets you know how many values will be invalid. The invalid values are calculated from a sample of up to 100 records and are displayed at the top of the results.

Using the toggles, you can filter the values you see:

- Invalid values only: You see only the values that are invalid against the rule.
- Logic fields only: You see only the fields that are used in the logic of the rule.

![Validation rule preview](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/validation-rule-preview.png)

## Using expressions in validation rules

Validation rule expressions use Qlik function syntax. For more information, see [*Script syntax and chart functions*](../../LoadData/script-syntax-functions.htm). Only some functions are supported in validation rules, you can see the list in the application.

You can use expressions in the If, Then, Else if, and Else sections when defining a rule.

Validation rules support date and time functions. All date and time functions are based on UTC. There is no timezone parameter.
Date and time results are rendered as full date/time values for consistent comparisons.

For arithmetic or numeric comparisons, use Date#(),
Time#(), Timestamp#(), or the Num() function.
The format parameter of Date#(), Time#(), and Timestamp#()
accepts both the standard patterns, such as DD/MM/YYYY and HH:mm:ss, and the Unix epoch patterns: unix-seconds, unix-millis, unix-micros,
and unix-nanos. For example, Timestamp#($(createdAt), 'unix-millis') interprets the value
as a Unix epoch in milliseconds: Timestamp#(1234567890000, 'unix-millis')

Information noteExpressions are available only in pull-up mode.

1. Open the rule from:
   - Data quality > Validation rules tab.
   - The dataset's Data preview tab, when you are applying a rule to a dataset.
2. In the rule definition, select Expression.
3. Enter your expression or click fx to open the expression editor, and see the available functions and how to use them.

   ![Expression editor for validation rules](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/validation-rules-expression.png)

   This editor lets you test your expression before you apply it to your data.
4. If you clicked fx:
   1. Type the expression or select the functions from the left menu. In this example, the value must be lowercase and with no extra spaces.
   2. Click Extract variables.
   3. Enter the value to test. For example,  True  with extra spaces before and after.
   4. Click Test expression. The value is returned in lowercase, and with no extra spaces.

      The dialog slightly varies if you have opened it from:

      - The Validation rules tab.

        ![Testing an expression from the Validation rules tab](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/validation-rules-test-expression.png)
      - The dataset's Data preview tab.

        ![Testing an expression from the dataset](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/validation-rules-test-expression-dataset.png)
5. Click Confirm.

When an expression cannot be evaluated for a value, that value is categorized as not executable.

For more information about the usage of the $ symbol, see [*Dollar-sign expansion using a variable*](../../Scripting/dollar-sign-expansion-using-variable.htm).

## Overview of the validation rules

Once you have created and applied rules to a dataset, you can get an overview of the quality:

- In the Overview tab. You can see what impacts the dataset quality the most. The four rules with the most negative impact on the quality are displayed. You can also see the rules types used in your dataset. For more information, see [Categories and levels of severity](#Categories-severity).

  The rules might be different from one user to another as they depend on the space access.

  ![Overview of the validation rules](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/validation-rules-overview.png)
- In the Validation rules tab: You can see the details of each validation rule applied to the dataset.

  ![Validation rules tab of a dataset](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/dataset-validation-rules.png)

## Editing a validation rule from a dataset

This procedure lets you only edit a validation rule from a dataset and change the fields to which the rule apply.

To edit the definition of the rule, see [Editing a validation rule](#Editing-rule).

1. Open a dataset.
2. Select the Data Preview tab.
3. Click the field to which the rule applies.
4. In the right panel, click ![Apply validation rule icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add_20x20.png) from the Validation rules section.
5. Edit the rule as needed.
6. To apply your changes and refresh the data quality automatically, select the Refresh quality check box.
7. Click Apply.
8. If you did not select Refresh quality, click Refresh above the right panel to apply your changes and refresh the data quality.

## Removing a validation rule from a dataset

This procedure lets you remove a rule from a dataset without deleting the rule from the space.

To delete the rule from the space, see [Deleting a validation rule](#Deleting-rule).

1. Open the dataset.
2. Select the Data Preview tab.
3. Click the field from which you want to remove the rule.
4. In the right panel, click ![Actions icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_horizontal.png) > Remove.
5. Confirm the removal.
6. Click Refresh above the right panel to apply your changes and refresh the data quality.

## Activating/Deactivating a validation rule

Instead of deleting or removing a validation rule from a dataset, you can deactivate it from two menus:

- From the Validation rules tab:
  1. Hover over the rule.
  2. On the right, click ![Actions icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_horizontal.png) > Deactivate.

     This deactivates the rule in all datasets to which the rule applies.
  3. Refresh the data quality in the impacted datasets.
- From the dataset:
  1. Click the field to which the rule you want to deactivate applies.
  2. In the right panel, click ![Actions icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_horizontal.png) > Deactivate.
  3. Click Refresh above the right panel to apply your changes and refresh the data quality.

     The rule is grayed out and the icon ![validation rules](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_validation_rules_20x20.png) is no longer displayed in the column header. You can activate it back at any time. If Activate is grayed out, it means that the rule is deactivated for all datasets.

     The rule is only deactivated for this dataset and you can still apply it to other datasets.

To activate a rule, follow the same procedure but click Activate.

## Editing a validation rule

This procedure lets you edit a validation rule and will impact all the datasets to which the rule applies.

To only edit the fields to which a rule applies, see [Editing a validation rule from a dataset](#Editing-rule-from-dataset).

You can only edit the rules that are in a space to which you have access.

1. Open Data quality and select the Validation rules tab.
2. From the list, click the rule or ![Actions icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_horizontal.png) > Edit.
3. Edit the rule as needed.

   Information noteWhen you change the category or the severity, it changes the impact of the rule on the dataset quality. For more information, see [Categories and levels of severity](#Categories-severity).
4. Click Save.
5. When the rule applies to datasets, open each dataset and refresh the quality.

## Deleting a validation rule

This procedure will impact all the datasets to which the rule applies.

To only remove a rule from a dataset, see [Removing a validation rule from a dataset](#Removing-rule).

You can only delete the rules that are in a space to which you have access.

1. Open Data quality and select the Validation rules tab.
2. From the list, click ![Actions icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_horizontal.png) > Delete.
3. Confirm the deletion.
4. When the rule applies to datasets, open each dataset and refresh the quality.

## Categories and levels of severity

The category and the severity let you adjust the impact of a rule on the dataset quality and the Qlik Trust Score™. Some levels of severity have more impact than the others.

### Categories

No category has more weight than another and all the categories impact the dataset quality and the Validity dimension of the Qlik Trust Score™.

When a rule is in the Accuracy category, it also impacts the Accuracy dimension.

For more information, see [Assessing data quality](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataProducts/Data-quality-and-data-discovery.htm) and [Qlik Trust Score™](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataProducts/Qlik-Trust-score.htm).

### Severity

A rule with a lower weight will impact less the dataset quality and the Qlik Trust Score™ than a rule with a higher weight: Critical > Major > Standard > Minor.

Example: A dataset with 55 invalid records against a rule with the severity set to Severity: Minor will less decrease the scores compared to the same rule set to Severity: Major.

## The operators

When you define the rule, you can select different operators to validate your data.

Tip noteYou can configure whether Text operators are case-sensitive.

| Category | Operator | Description | Type | Example |
| --- | --- | --- | --- | --- |
| Generic | is empty | Different from Text/is blank | All types | A null value and the value "" are considered empty, and therefore valid. |
| Generic | is not empty | Different from Text/is not blank | All types | A null value and the value "" are considered empty, and therefore invalid. |
| Text | is blank | Different from Generic/is empty | Text | A null value, the value "", and the value "    " are considered blank, and therefore valid. |
| Text | is not blank | Different from Generic/is not empty | Text | A null value, the value "", and the value "    " are considered blank, and therefore invalid. |
| Text | = | Equal to | Text | OrderID = ORD#10 |
| Text | != | Different from | Text | OrderID != ORD#10 |
| Text | Contains | N/A | Text | OrderID Contains ORD#10 |
| Text | Does not contain | N/A | Text | OrderID Does not contain ORD#10 |
| Text | Starts with | N/A | Text | OrderID Starts with ORD# |
| Text | Does not start with | N/A | Text | OrderID Does not start with ORD# |
| Text | Ends with | N/A | Text | OrderID Ends with \_XX |
| Text | Does not end with | N/A | Text | OrderID Does not end with \_XX |
| Text | is blank | N/A | Text | Shipment is blank |
| Text | is not blank | N/A | Text | Shipment is not blank |
| Text | Matches regex | For more information, see the [RE2/J documentation](https://github.com/google/re2j). | Text | PostalCode Matches regex ^[0-9]{5}(-[0-9]{4})?$ |
| Text | Does not match regex | For more information, see the [RE2/J documentation](https://github.com/google/re2j). | Text | PostalCode Does not match regex ^[0-9]{5}(-[0-9]{4})?$ |
| Text | Is one of | Select this operator when you need to use a restricted list of values, instead of a semantic type.  You can add up to 150 values, and each one can contain up to 200 characters. When you need more than 150 values, use a semantic type. | Text | Country Is one of USA France Canada China |
| Text | Is not one of | Select this operator when you need to use a restricted list of values, instead of a semantic type.  You can add up to 150 values, and each one can contain up to 200 characters. When you need more than 150 values, use a semantic type. | Text | Country Is not one of USA France Canada China |
| Number | = | Equal to | Number | Age = 21 |
| Number | != | Different from | Number | Age != 0 |
| Number | < | Less than | Number | Age < 21 |
| Number | <= | Less than or equal to | Number | Age <= 20 |
| Number | > | Greater than | Number | Age > 20 |
| Number | >= | Greater than or equal to | Number | Age >= 21 |
| Boolean | is true | N/A | Boolean | User deleted is true |
| Boolean | is false | N/A | Boolean | User activated is false |
| Boolean | = | Relationship between two boolean fields | Boolean | User deleted = Account deactivated |
| Boolean | != | Relationship between two boolean fields | Boolean | User activated != User deleted |
| Type | is of semantic type | The value is defined in the selected semantic type. | All types | Country is of semantic type Country Code ISO3 |
| Type | is not of semantic type | The value is not defined in the selected semantic type. | All types | Phone is not of semantic type US Phone |
| Date | Is in the last | Enter a positive integer and select the unit. | All types | Shipment Is in the last 4 Hours |
| Date | Is not in the last | Enter a positive integer and select the unit. | All types | Shipment Is not in the last 110 Minutes |
| Date | Is in the next | Enter a positive integer and select the unit. | All types | Shipment Is in the next 90 Seconds |
| Date | Is not in the next | Enter a positive integer and select the unit. | All types | Shipment Is not in the next 28 Days |
| Date | Is before | Open the calendar and select the date and time. You must select a date/time using the UTC+00 time zone. | All types | Birthdate Is before 1/1/2008 12:00 AM |
| Date | Is before or equal to | Open the calendar and select the date and time. You must select a date/time using the UTC+00 time zone. | All types | Birthdate Is before or equal to 1/1/2008 12:00 AM |
| Date | Is after | Open the calendar and select the date and time. You must select a date/time using the UTC+00 time zone. | All types | Birthdate Is after 1/1/2008 12:00 AM |
| Date | Is after or equal to | Open the calendar and select the date and time. You must select a date/time using the UTC+00 time zone. | All types | Birthdate Is after or equal to 1/1/2008 12:00 AM |
| Date | Is equal to | Open the calendar and select the date and time. You must select a date/time using the UTC+00 time zone. | All types | Birthdate Is equal to 1/1/2008 12:00 AM |
| Date | Is not equal to | Open the calendar and select the date and time. You must select a date/time using the UTC+00 time zone. | All types | Birthdate Is not equal to 1/1/2008 12:00 AM |
| Date | Is in the past | N/A | All types | Shipment Is in the past |
| Date | Is in the future | N/A | All types | Shipment Is in the future |
