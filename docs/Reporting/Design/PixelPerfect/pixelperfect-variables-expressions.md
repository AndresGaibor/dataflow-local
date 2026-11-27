---
title: "Working with variables and expressions in your PixelPerfect template"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/PixelPerfect/pixelperfect-variables-expressions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates", "Designing PixelPerfect report templates", "Adding content to your PixelPerfect report template", "Visualizing application data in your report"]
---

# Working with variables and expressions in your PixelPerfect template

You can add [variables](#glossary-0 "Glossary term") from the Qlik Sense application to your PixelPerfect template to create dynamic content. Expressions using Qlik Sense syntax can be added directly, allowing you to store and use individual calculations in reports.

Variables and expressions can be added as usable data bindings from the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu.

## When to use them

Variables and expressions are useful to add to your report. Here are some examples:

- Use a scripted variable to store the date of the last time the application was reloaded. This could be inserted on the front page of the report.
- Add an expression to calculate a key metric, such as total sales. Then, combine the expression into native PixelPerfect text to represent data using natural language and PixelPerfect formatting.

## Adding a variable

You can add a variable that exists in the Qlik Sense application as a data binding.

Do the following:

1. Open the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu available from the right-side panel in the designer.
2. Click the plus icon next to Variables.
3. Select the Qlik Sense variable you want to add. Click the ![Plus](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) icon next to it.

   The data binding is added.

## Adding an expression

You can add Qlik Sense expressions directly as data bindings.

Do the following:

1. Open the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu available from the right-side panel in the designer.
2. Click the plus icon next to Expressions.
3. Select the Qlik Sense variable you want to add. Click the ![Plus](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) icon next to it.

   The data binding is added.

## Example - Using a variable to display date of last application reload

Refer to the example application sources here: [*Examples - In-application reporting*](../../InAppGeneral/reporting-example-material.htm). Upload the application and data files into a space, and then reload the application. You are ready to complete the example.

In this example, we use Qlik Sense variables to compose a text string representing the date on which the application data was last reloaded.

Do the following:

1. Create a new PixelPerfect template.
2. Open the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List in the designer.

   Field List menu in the PixelPerfect designer

   ![The 'Field List' menu expanded from the right side panel in the PixelPerfect designer](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-gen-field-list.png "Click to view full size")
3. Expand Variables. Click the plus icon to add a new variable.
4. Click the plus icon next to Variables.
5. Click the plus icon next to vLastReloadYear. This is a scripted variable from the application. The variable contains the expression =year(now()) and is only updated when the application reloads.
6. You are brought back to the main ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu. Click the plus icon next to Variables.
7. Click the plus icon next to vLastReloadMonth. This is a scripted variable from the application. The variable contains the expression =month(now()) and is only updated when the application reloads.
8. You are brought back to the main ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu. Click the plus icon next to Variables.
9. Click the plus icon next to vLastReloadDay. This is a scripted variable from the application. The variable contains the expression =day(now()) and is only updated when the application reloads.
10. From the toolbox panel on the left side of the designer, drag a ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_text.svg) Label object onto the TopMargin1 band in your template.
11. Select the label. Click the bold f icon near the label to open the Expression Editor.
12. In the Expression Editor, enter the following expression:

    ```
    Concat('Application last reloaded: ', [vLastReloadYear], '-', [vLastReloadMonth], '-', [vLastReloadDay])
    ```
13. Increase the width of the label so that all text can be displayed on a single line.

    Label containing string composition with variables, added to template. The image also shows the data sources that were used in the label expression.

    ![Report template with a label containing text and a variable value, added in the top margin](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-variable-blank.png "Click to view full size")
14. Customize and style the label properties if desired.
15. In the top right corner, click Save template.
16. Click Preview report. Download the report and open it.

Report preview

![Generated report showing the variable value and concatenated text. In this case, the complete string displays the time at which the app was last reloaded](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-variable-example.png "Click to view full size")

## Learn more

- [*Variables dialog*](../../../Sheets/variables-dialog.htm)
- [*Working with variables in the data load editor*](../../../Scripting/work-with-variables-in-data-load-editor.htm)
