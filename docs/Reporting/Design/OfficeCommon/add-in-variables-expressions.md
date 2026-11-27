---
title: "Using variables and expressions in report templates with Qlik add-ins for Microsoft Office"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/OfficeCommon/add-in-variables-expressions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates", "Designing report templates with Qlik add-ins for Microsoft Office", "Adding content to report templates with Qlik add-ins for Microsoft Office"]
---

# Using variables and expressions in report templates with Qlik add-ins for Microsoft Office

Add variables and expressions as report objects in your Excel, PowerPoint, or Word[report template](#glossary-0 "Glossary term"). You can use a variable or expression to dynamically store a value or calculation that can be centrally modified and re-used across a report.

## Applies to

This content applies to the following types of Qlik Cloud report templates:

- Excel

  [*Qlik add-in for Microsoft Excel*](reporting-add-ins.htm#Excel)
- PowerPoint

  [*Qlik add-in for Microsoft PowerPoint*](reporting-add-ins.htm#PowerPoint)
- Word

  [*Qlik add-in for Microsoft Word*](reporting-add-ins.htm#Word)

## Variables

You can insert [variables](#glossary-1 "Glossary term") from Qlik Sense into the template. Like other template objects you create, a variable is added as an object in the template configuration, and is accessible from the add-in window. Add an instance of the variable object as a variable tag.

You can add both scripted variables and variables defined in sheet view.

### Adding a variable

Do the following:

1. Click the ![Variables](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_variables_outline.svg) icon on the top toolbar of the add-in.
2. Click Add variable. A list of available variables appears.

   Variables and expressions tab in an add-in, allowing you to add a new variable or revisit a variable you have already added

   !['Variables and expressions' tab in an add-in, from which you can add/modify existing variable objects you have added, or add a new variable](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ExcelAddIn_AddVariable.png "Click to view full size")
3. Click the ![Plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) icon to the right of an existing application variable to add it.

   Select a variable you want to add to the template

   ![Select the variable to add to the template from the available list](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ExcelAddIn_AddVariableInstance.png "Click to view full size")
4. The variable tag is inserted. The settings page for the variable appears. Under Expression, you can view a Preview of the current variable value.

   It is recommended to provide a unique Name to the variable so you can identify it in the add-in if you later need to change its settings.
5. Adjust any other parameters as needed.

Revisit any variable you have added at any point for modifications to its configuration, to locate it in the Excel, PowerPoint, or Word file, or to add another instance of it. Click the ![Variables](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_variables_outline.svg) icon in the add-in to open the Variables and expressions landing page, and click ![Right-directional arrow](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_direction_right.svg) to navigate to the area where it is inserted. Adjust any settings as needed in the add-in.

For information on other important actions you need to complete with variables, see the following:

- [*Formatting a variable or expression*](#Formatti)
- [*Removing a variable or expression*](#Removing)

## Expressions

Add expressions as objects using Qlik Sense syntax and functions. Like other template objects you create, an expression is added as an object in the template configuration, and is accessible from the add-in window. Add an instance of the expression object as an expression tag.

Popular expressions you might want to add include:

- =Count(distinct <your dimension field>): returns the number of unique values for a dimension field you define in the expression (for example, Customer or Product).
- =today(): returns the current date.
- =year(now): returns the current year.

### Adding an expression

1. Click the ![Variables](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_variables_outline.svg) icon on the top toolbar of the add-in.
2. Click Add expression. A list of available expressions appears.

   Variables and expressions tab in an add-in, allowing you to add a new expression or revisit an expression you have already added

   !['Variables and expressions' tab in an add-in, from which you can add/modify existing or new expressions](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ExcelAddIn_AddExpression.png "Click to view full size")
3. Click the ![Plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) icon to the right of an existing expression to add it. Follow the same steps for adding an existing variable: [*Adding a variable*](#Adding).
4. If you need to create a new expression instead, click Create expression.
5. Configure the new expression by adding a Name and Description (optional), and then define the Expression.

   Select a variable you want to add to the template

   ![Create an expression using an add-in, defining a Name, description, and expression (calculation)](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ExcelAddIn_CreateExpression.png "Click to view full size")
6. Check the Preview value under the Expression field to make sure you have configured the expression correctly, and click Create.

The expression object is created and will be available in the add-in window. The expression tag is also inserted at the selected location.

Revisit any expression you have added at any point for modifications to its configuration, to locate it in the Excel, PowerPoint, or Word file, or to add another instance of it. Click the ![Variables](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_variables_outline.svg) icon in the add-in to open the Variables and expressions landing page, and click ![Right-directional arrow](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_direction_right.svg) to navigate to the area where it is inserted. Adjust any settings as needed in the add-in.

For information on other important actions you need to complete with variables, see the following:

- [*Formatting a variable or expression*](#Formatti)
- [*Removing a variable or expression*](#Removing)

## Formatting a variable or expression

Apply native Excel, PowerPoint, or Word formatting to your variable and expression tags. This can include font styling, number formatting, and other customizations. The formatting is applied to the report output.

## Removing a variable or expression

You can remove a variable or expression from the report template, and from the list of that object type in the add-in pane.

Do the following:

1. Select the area where the object is added.
2. Click Delete in the bottom of the add-in window.

This removes the tags and the object from the corresponding object list.

If you instead use Microsoft Office features to delete an object, it will not be inserted in the generated report. However, the object will still appear in the list of added objects. This means you can easily re-add the object later.

## Learn more

- [*Adding content to report templates with Qlik add-ins for Microsoft Office*](add-in-content.htm)
- [*Working with levels and pages in tabular report templates*](../Excel/add-in-excel-levels-pages.htm)
- [*Using variables in expressions*](../../../Variables/work-with-variables.htm)
- [*Working with variables in the data load editor*](../../../Scripting/work-with-variables-in-data-load-editor.htm)
