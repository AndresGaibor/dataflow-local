---
title: "Tutorial - Creating a set expression"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/SetAnalysis/set-analysis-tutorial.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Chart expressions", "Set analysis"]
---

# Tutorial - Creating a set expression

You can build set expressions in Qlik Sense to support data analysis. In this context, the analysis is often referred to as [set analysis](#glossary-0 "Glossary term"). Set analysis offers a way of defining a scope that is different from the set of records defined by the current selection in an app.

## What you will learn

This tutorial provides the data and chart expressions to build set expressions using set modifiers, identifiers and operators.

## Who should complete this tutorial

This tutorial is for app developers who are comfortable working with the script editor and chart expressions.

## What you need to do before you start

If you have a user-based subscription, you need Professional user entitlement. To find out what type of user you have, contact your tenant administrator. For more information, see [*Managing user entitlements*](../../Admin/SaaS-user-allocations.htm).

## Further reading and resources

- The [*Set analysis*](set-analysis-expressions.htm) topics in the help provide an overview of set analysis, detailed description of the set expression elements, and examples.
- [Qlik](http://www.qlik.com/) offers a wide variety of resources when you want to learn more.
- Training, including free online courses, is available on [Qlik Learning](https://learning.qlik.com/).
- Discussion forums, blogs, and more can be found in [Qlik Community](http://community.qlik.com/).

### Videos

The following videos complement this tutorial.

The first video shows basic set expressions that are similar to those that are described in this tutorial. The second video demonstrates more complex set expressions.

- [Set Analysis Part 1: Beginners' Introduction](https://play.vidyard.com/emzQVRFpAhM5LLwXcKNU8u)
- [Set Analysis Part 2](https://play.vidyard.com/U86Emuu4vymytxsQBCPmTh)

## Elements in a set expression

Set expressions are enclosed in an [aggregation](#glossary-2 "Glossary term") function, such as Sum(), Max(), Min(), Avg(), or Count(). Set expressions are constructed from building blocks known as elements. These elements are set modifiers, identifiers, and operators.

Elements in a set expression

![Elements in a set expression.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_setanalysis_callout.png "Click to view full size")

The set expression above, for example, is built from the aggregation Sum(Sales). The set expression is enclosed in the outer curly brackets: { }

The first operand in the expression is: $<Year={2021}>

This operand returns sales for the year 2021 for the current selection. The modifier, <Year={2021}>, contains the selection of the year 2021. The $ set identifier indicates that the set expression is based on current selection.

The second operand in the expression is: 1<Country={'Sweden'}>

This operand returns Sales for Sweden. The modifier, <Country={'Sweden'}>, contains the selection of the country Sweden. The 1 set identifier indicates that [selections](#glossary-3 "Glossary term") made in the app will be ignored.

Finally, the + set operator indicates that the expression returns a set consisting of the records that belongs to any of the two set operands.

For more information, see:

- [*Set modifiers*](set-modifiers.htm)
- [*Set identifiers*](set-identifiers.htm)
- [*Set operators*](set-operators.htm)

## Creating a set expression tutorial

Complete the following procedures to create the set expressions shown in this tutorial.

### Create a new app and load data

Do the following:

1. Create a new app.
2. Click Script editor. Alternatively, open the app navigation menu and select Data load editor.
3. Create a new section in the Data load editor.
4. Copy the following data and paste it into the new section: [*Set expression tutorial data*](#SetExpressionData)
5. Click Load data. The data is loaded as an inline load.

For more information about using inline loads, see [*Using inline loads to load data*](../../Scripting/inline-loads-qs.htm).

### Create set expressions with modifiers

The set modifier consists of one or more [field](#glossary-4 "Glossary term") names, each followed by a selection that should be made on the field. The modifier is enclosed by angled brackets. For example, in this set expression:

Sum ( {<Year = {2015}>} Sales )

The modifier is:

<Year = {2015}>

This modifier specifies that data from the year 2015 will be selected. The curly brackets in which the modifier is enclosed indicate a set expression.

Do the following:

1. In a [sheet](#glossary-5 "Glossary term"), open the Assets panel from the navigation bar, and then click Charts.

   ![KPIs using set modifiers.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_set_tutorial_chart2.png "Click to view full size")
2. Under Visualizations, drag a KPI onto the sheet, and then click Add measure.

   ![KPIs using set modifiers.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_set_tutorial_add_measure.png "Click to view full size")
3. Click Sales, and then select Sum(Sales) for the aggregation.

   ![KPIs using set modifiers.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_set_tutorial_sum_sales.png "Click to view full size")

   The KPI shows the sum of sales for all years.

   ![KPIs using set modifiers.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_set_tutorial_kpi_sum_sales.png "Click to view full size")
4. Copy and paste the KPI to create a new KPI.
5. Click the new KPI, click Sales under Measures, and then click Open Expression editor.

   ![KPIs using set modifiers.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_set_tutorial_kpi_expression_editor.png "Click to view full size")

   The expression editor opens with the aggregation Sum(Sales).

   ![KPIs using set modifiers.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_set_tutorial_kpi_editor_sum_sales.png "Click to view full size")
6. In the expression editor, create an expression to sum Sales for 2015 only:

   - Add curly brackets to indicate a set expression: Sum({}Sales)

   1. Add angle brackets to indicate a set modifier: Sum({<>}Sales)
   2. In the angle brackets, add the field to be selected, in this case the field is Year, followed by an equal sign. Next, enclose 2015 in another set of curly brackets. The resulting set modifier is: {<Year={2015}>}.

      The entire expression is:

      ```
      Sum({<Year={2015}>}Sales)
      ```

      ![KPIs using set modifiers.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_set_tutorial_kpi_editor_sum_sales_year.png "Click to view full size")
   3. Click Apply to save the expression and to close the expression editor. The sum of Sales for 2015 is shown in the KPI.

      ![KPIs using set modifiers.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_set_tutorial_kpi_sum_sales_year.png "Click to view full size")
7. Create two more KPIs with the following expressions:

   ```
   Sum({<Year={2015,2016}>}Sales)
   ```

   The modifier in the above is <Year={2015,2016}>. The expression will return the sum of Sales for 2015 and 2016.

   ```
   Sum({<Year={2015},Country={'Germany'}>} Sales)
   ```

   The modifier in the above is <Year={2015}, Country={'Germany'}>. The expression will return the sum of Sales for 2015, where 2015 intersects with Germany.

   KPIs using set modifiers

   ![KPIs using set modifiers.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_kpi_set_modfier.png "Click to view full size")

### Add set identifiers

The set expressions above will use current selections as base, because an identifier was not used. Next, add identifiers to specify the behavior when selections are made.

Do the following:

On your sheet, build or copy the following set expressions:

```
Sum({$<Year={"2015"}>}Sales)
```

The $ identifier will base the set expression on the current selections made in the data. This is also the default behavior when an identifier is not used.

```
Sum({1<Year={"2015"}>}Sales)
```

The 1 identifier will cause the aggregation of Sum(Sales) on 2015 to ignore the current selection. The value of the aggregation will not change when the user makes other selections. For example, when Germany is selected below, the value for the aggregate sum of 2015 does not change.

KPIs using set modifiers and identifiers

![KPIs using set modifiers and identifiers.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_kpi_set_identifier.png "Click to view full size")

### Add operators

Set operators are used to include, exclude, or intersect data sets. All operators use sets as operands and return a set as result.

You can use set operators in two different situations:

- To perform a set operation on set identifiers, representing sets of records in data.
- To perform a set operation on the element sets, on the field values, or inside a set modifier.

Do the following:

On your sheet, build or copy the following set expression:

```
Sum({$<Year={2015}>+1<Country={'Germany'}>}Sales)
```

The plus sign (+) operator produces a union of the data sets for 2015 and Germany. As explained with set identifiers above, the dollar sign ($) identifier means current selections will be used for the first operand, <Year={2015}>, will be respected. The 1 identifier means selection will be ignored for the second operand, <Country={'Germany'}>.

KPI using plus sign (+) operator

![KPIs using set modifiers and identifiers.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_set_tutorial_plus_operator.png "Click to view full size")

Alternatively, use a minus sign (-) to return a data set that consists of the records that belong to 2015 but not Germany. Or, use an asterisk (\*) to return a set consisting of the records that belong to both sets.

```
Sum({$<Year={2015}>-1<Country={'Germany'}>}Sales)
```

```
Sum({$<Year={2015}>*1<Country={'Germany'}>}Sales)
```

KPIs using operators

![KPIs using set modifiers and identifiers.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_set_tutorial_minus_operator.png "Click to view full size")

## Set expression tutorial data

Load script

Load the following data as an inline load and then create the chart expressions in the tutorial.

For more information about using inline loads, see [*Using inline loads to load data*](../../Scripting/inline-loads-qs.htm).

```
//Create table SalesByCountry
SalesByCountry:
Load * Inline [
Country, Year, Sales
Argentina, 2016, 66295.03
Argentina, 2015, 140037.89
Austria, 2016, 54166.09
Austria, 2015, 182739.87
Belgium, 2016, 182766.87
Belgium, 2015, 178042.33
Brazil, 2016, 174492.67
Brazil, 2015, 2104.22
Canada, 2016, 101801.33
Canada, 2015, 40288.25
Denmark, 2016, 45273.25
Denmark, 2015, 106938.41
Finland, 2016, 107565.55
Finland, 2015, 30583.44
France, 2016, 115644.26
France, 2015, 30696.98
Germany, 2016, 8775.18
Germany, 2015, 77185.68
];
```
