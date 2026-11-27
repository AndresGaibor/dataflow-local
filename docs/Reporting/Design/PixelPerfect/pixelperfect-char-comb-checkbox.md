---
title: "Creating character combs and check boxes"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/PixelPerfect/pixelperfect-char-comb-checkbox.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates", "Designing PixelPerfect report templates", "Adding content to your PixelPerfect report template", "Visualizing application data in your report"]
---

# Creating character combs and check boxes

The ![Character comb](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_character_comb_outline.svg) Character comb and ![Check](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_checks.svg) Check box objects in PixelPerfect reporting allow you to style text in section headers using input from the Qlik Sense app. They can also be used to generate interactive reports that can be used as forms.

Character comb and check box in PixelPerfect report

![Character comb and check box objects in a PixelPerfect report](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-char-comb-checkbox.png "Click to view full size")

## Adding a character comb

With the ![Character comb](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_character_comb_outline.svg) Character comb, you can style app data values as a series of cells, one for each letter. This can be used, for example, to add emphasis for section headers.

Do the following:

1. From the toolbox panel on the left side of the designer, drag a ![Character comb](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_character_comb_outline.svg) Character comb onto the design surface.

   Consider placing it on a DetailReport band if you plan on looping the object with a level.
2. To use app data in the character comb, go to the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List and create a data binding to use as the source. It can be a level or table data binding.

   See [*Data binding*](pixelperfect-data-binding.htm).
3. Select the character comb and click ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) in the right-side panel.
4. Click the button to edit the Text property expression.

   The Expression Editor opens.
5. Expand Fields and double-click the field you want to use, or type the field name enclosed in square brackets.
6. Click OK.
7. For best results, open ![Gear](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) Properties and turn on Auto Width under Character Comb Tasks.

## Adding a check box

With the ![Check](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_checks.svg) Check box, you can add text data from the app into check box elements, and use conditions to check or uncheck the boxes. This can be used to style section headers or to make the report resemble a form.

Do the following:

1. From the toolbox panel on the left side of the designer, drag a ![Check](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_checks.svg) Check box onto the design surface.

   Consider placing it on a DetailReport band if you plan on looping the object with a level.
2. To use app data in the check box, go the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List and create a data binding to use as the source. It can be a level or table data binding.

   See [*Data binding*](pixelperfect-data-binding.htm).
3. Select the check box and click ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) in the right-side panel.
4. Click the button to edit the Text property expression.

   The Expression Editor opens.
5. Expand Fields and double-click the field you want to use, or type the field name enclosed in square brackets.
6. Click OK.
7. Customize the check box as needed with the following:

   - All check boxes inherit the default state you set in the object properties. You can define a condition so that the check box only appears in a state for certain field values. For example:

     ```
     Iif( [Country (Country_Level).Country] == 'Argentina', True  , False  )
     ```

     This setting is configured in the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) Expressions panel under Check Box State.
   - Open ![Gear](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) Properties and set custom symbols and sizes under Check Box Tasks > Glyph Options.

## Example - Character combs and check boxes

Refer to the example application sources here: [*Examples - In-application reporting*](../../InAppGeneral/reporting-example-material.htm). Upload the application and data files into a space, and then reload the application. You are ready to complete the example.

In this example, we create character combs and check boxes and loop them over a level.

### Part 1: Add data binding

Do the following:

1. Create a new PixelPerfect template.
2. Open the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu available from the right-side panel in the designer.

   Field List menu in the PixelPerfect designer

   ![The 'Field List' menu expanded from the right side panel in the PixelPerfect designer](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-gen-field-list.png "Click to view full size")
3. Click the plus icon next to Levels.
4. Expand Fields, and click the ![Plus](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) icon next to Region.

   The data binding is added.

### Part 2: Add DetailReport band and connect it with data binding

You need to create a DetailReport band to use a level.

Do the following:

1. Right-click the Detail1 band, and then click Insert Band > DetailReport.
2. To bind the DetailReport1 band to the level, select the band and then open the ![Gear](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) Properties menu. Under Detail Report Tasks > Data Member, select the Region level.

### Part 3: Add a character comb and check box

Do the following:

1. From the toolbox panel on the left side of the designer, drag a ![Character comb](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_character_comb_outline.svg) Character comb onto the DetailReport1 band.
2. Resize the character comb so that its cells are on a single line.
3. From the same panel, drag a ![Check](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_checks.svg) Check box onto the DetailReport1 band. Place it to the right side of the character comb.
4. Select the character comb and click ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) Expressions in the right-side panel.
5. For the Text property expression, open the Expression Editor, and type the field [Region] as the expression.
6. Click OK.
7. Open ![Gear](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) Properties and turn on Auto Width under Character Comb Tasks.
8. Select the check box and click ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) Expressions in the right-side panel.
9. For the Text property expression, open the Expression Editor, and type the field [Region] as the expression.
10. Click OK.
11. For the Check Box State property expression, open the Expression Editor and paste the following expression:

    ```
    Iif( [Region] == 'Spain', True  , False  )
    ```
12. Click OK.

    Character comb and check box added to template

    ![](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-char-comb-checkbox-blank.png "Click to view full size")
13. In the top right corner, click Save template.
14. Click Preview report. Download the report and open it.

    Result

    ![](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-char-comb-checkbox.png "Click to view full size")
