---
title: "Adding variables and expressions to HTML report templates"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/HTML/html-report-variables-expressions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates", "Designing HTML report templates", "Adding content to your HTML report template"]
---

# Adding variables and expressions to HTML report templates

Add variables and expressions to your HTML [report template](#glossary-0 "Glossary term") as objects. You can use a variable or expression to dynamically store a value or calculation that can be centrally modified and re-used across a report.

## Variables

You can insert [variables](#glossary-1 "Glossary term") from the application into the template. Like other template objects you create, a variable is added as an object in the template configuration, and is accessible from the objects panel. Add an instance of the variable object as a variable tag.

You can add both scripted variables and variables defined in sheet view.

Do the following:

1. In the HTML designer, place your cursor at the location in the code at which you want to insert the variable.
2. Click ![Variables](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_variables_outline.svg) in the objects panel.

   Variables and expressions menu in the objects panel within the HTML designer

   !['Variables and expressions' menu in HTML designer, from which you can modify existing variables you have added, or add a new variables](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_html-add-variable-objects-panel.png "Click to view full size")
3. Click Add variable. A list of available application variables appears.
4. Click the ![Plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) icon to the right of an existing variable to add it.

   Select a variable you want to add to the template

   ![Selecting a variable to add as an HTML report object](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_html-add-variable-select-variable.png "Click to view full size")
5. The variable tag is inserted at your current location in the template code. The settings page for the variable appears. Under Expression, you can view a Preview of the current variable value.

   Template design surface with variable added as a tag

   ![Tag representing a variable shown in the HTML template](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_html-add-variable-resulting-tag.png "Click to view full size")
6. In the objects panel, provide a unique Name to the variable so you can identify it later.
7. Adjust any other parameters as needed.
8. You can re-use the variable object at any time. Open ![Variables](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_variables_outline.svg) in the objects panel, and click ![Right-directional arrow](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_direction_right.svg) to open the object. Click Add variable tag to add the variable again.

For information on other important actions you need to complete with variables, see the following:

- [*Formatting a variable or expression*](#Formatti)
- [*Removing content from an HTML report template*](html-report-remove-content.htm)

## Expressions

Add expressions as objects using the same syntax and functions that are available in analytics applications. Like other template objects you create, an expression is added as an object in the template configuration, and is accessible from the objects panel. Add an instance of the expression object as an expression tag.

Popular expressions you might want to add include:

- =Count(distinct <your dimension field>): returns the number of unique values for a dimension field you define in the expression (for example, Customer or Product).
- =today(): returns the current date.
- =year(now): returns the current year.

### Adding an expression

1. In the HTML designer, place your cursor at the location in the code at which you want to insert the table.
2. Click ![Variables](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_variables_outline.svg) in the objects panel.

   Variables and expressions menu in the objects panel within the HTML designer

   !['Variables and expressions' menu in HTML designer, from which you can modify existing expressions you have added, or add a new expression](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_html-add-expression-objects-panel.png "Click to view full size")
3. Click Add expression.
4. Configure the new expression by adding a Name and Description (optional), and then define the Expression.

   Define the expression you want to use in the template

   ![Create an expression using the HTML designer, defining a Name, description, and expression (calculation)](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_html-add-expression-enter-expression.png "Click to view full size")
5. Check the Preview value under the Expression field to make sure you have configured the expression correctly, and click Create.
6. The expression tag is inserted at your current location in the template code. The settings page for the expression appears. Under Expression, you can view a Preview of the current variable value.

   Template design surface with expression added as a tag

   ![Tag representing an expression report object shown in the HTML template](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_html-add-expression-result.png "Click to view full size")
7. In the objects panel, provide a unique Name to the variable so you can identify it later.
8. You can re-use the expression object at any time. Open ![Variables](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_variables_outline.svg) in the objects panel, and click ![Right-directional arrow](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_direction_right.svg) to open the object. Click Add expression tag to add the expression again.

For information on other important actions you need to complete with expressions, see the following:

- [*Formatting a variable or expression*](#Formatti)
- [*Removing content from an HTML report template*](html-report-remove-content.htm)

## Formatting a variable or expression

Style and format the variable to meet your requirements using HTML code. Possible customizations include font styling, number formatting, and using the variable in natural language in your report. The formatting is applied to the report output.
