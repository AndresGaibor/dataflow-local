---
title: "Example - Highly formatted table with sub-bands"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/PixelPerfect/pixelperfect-sub-bands-example.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates", "Designing PixelPerfect report templates", "Adding content to your PixelPerfect report template", "Visualizing application data in your report"]
---

# Example - Highly formatted table with sub-bands

In this example, we create a highly formatted table and use sub-bands to create different versions of this table, each with different filtering. For more information about sub-bands, see [*Working with sub-bands in PixelPerfect reporting*](pixelperfect-sub-bands.htm).

## Preparations

Refer to the example application sources here: [*Examples - In-application reporting*](../../InAppGeneral/reporting-example-material.htm). Upload the application and data files into a space, and then reload the application. You are ready to complete the example.

## Step 1: Create data bindings

Do the following:

1. Create a new PixelPerfect template.
2. Open the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu available from the right-side panel in the designer.

   Field List menu in the PixelPerfect designer

   ![The 'Field List' menu expanded from the right side panel in the PixelPerfect designer](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-gen-field-list.png "Click to view full size")
3. Hover your cursor over Levels, and then click ![Plus](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg).
4. Expand the Sales Tables sheet. Next to Yearly Regional Sales, click ![Plus](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg).
5. You are brought back to the main menu in the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List. Hover your cursor over Levels again, and then click ![Plus](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg).
6. Expand Fields. Click ![Plus](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) next to OrderYear. The data binding is created.

## Step 2: Create the banded structure

Do the following:

1. On the design surface, right-click anywhere within the Detail1 band and click Insert Band > DetailReport.

   A new DetailReport band is inserted below Detail1.
2. Right-click the Detail2 band within the DetailReport band you just created. Click Insert Band > DetailReport.

   A new DetailReport band is inserted and nested within the first DetailReport band you created.
3. Right-click the Detail3 band within the second DetailReport band you just created. Click Insert Band > GroupHeader.

   The band is inserted above the Detail3 band.
4. Right-click the GroupHeader1 band you just created, and select Insert Sub-Band. The sub-band band is inserted within the parent GroupHeader1 band. Repeat this process two more times, so that there are three sub-bands nested within GroupHeader1.
5. Select the GroupHeader1 band. Move your cursor into the yellow vertical ruler, and position it at the top of the first sub-band. Click and drag so that the space above the first sub-band is much smaller.

   Using the cursor to resize the space above the first sub-band

   ![Image showing the location in the designer where you can drag to resize part of the GroupHeader band](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-sub-band-drag-resize.png "Click to view full size")

## Step 3: Bind the content to the data sources

Do the following:

1. Select the outermost DetailReport band in the structure (DetailReport1).
2. Click the gear icon at the edge of the design surface.

   Clicking the gear icon

   ![Close-up of the side of the design surface with a band selected, and the gear icon clicked, showing a popup menu for different settings](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-format-table-cog.png "Click to view full size")
3. In the menu, select the OrderYear level as the Data Member. This creates a separate table for each region in the application. However, we will be using sub-bands to only show three of the regions in the application.

   Tip noteAlternatively, click ![Cog wheel](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) at the far right of the designer. Add the Data Member under Detail Report Tasks.
4. Next, select the DetailReport2 band, and again click the gear icon at the edge of the design surface.
5. In the menu, select the Yearly Regional Sales level as the Data Member. This binds the table structure to the chart's source data.
6. Open the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu, and expand Levels.
7. Within the Yearly Regional Sales level, drag the Region and Sales fields onto the Detail3 band that is located below the sub-bands.
8. Arrange the field items on the band so they resemble two adjacent rows in a table.

   Tip note

   To align objects precisely with the grid, resize them manually until they are as close to grid lines as possible. Then, right-click each object and select Layout > Size to Grid. You can also open the ![Cog wheel](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) Properties menu and adjust their size values numerically under Layout > Size.

   For more information, see [*Arranging content in your PixelPerfect report template*](pixelperfect-arrange-content.htm).
9. We need to format the Sales values as currency figures. Click the Sales label, and then click the gear icon that appears next to it.
10. In the popout menu, click the ellipsis (three dots) menu under Text Format String.
11. The Format String Editor dialog opens. Choose Currency, and adjust the decimal points. Click OK.
12. Resize the Detail3 band, shrinking it so that it is only as small as the items in it.

## Step 4: Add conditions to the sub-bands

We need to configure each of the sub-bands so that it only appears when a particular value in the Region level cycle is present.

Do the following:

1. Select SubBand1.
2. Click ![Formula](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) on the right side panel to expand the Expressions menu.
3. In the menu, click the three-dot icon next to Visible.

   The Expression Editor opens.
4. In the Expression Editor, enter the following expression:

   ```
   Iif( [OrderYear] == 2021, True, False )
   ```
5. Repeat this process for the other sub-bands, but add the following expressions for each:

   - SubBand2:

     ```
     Iif( [OrderYear] == 2022, True, False )
     ```
   - SubBand3:

     ```
     Iif( [OrderYear] == 2023, True, False )
     ```

## Step 5: Add titles and column headers

Do the following:

1. Let's add a title for the level controlling the creation of separate tables. Open the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu, and expand Levels.
2. Expand the OrderYear level, and drag the OrderYear field within it onto the Detail2 band.
3. Customize font properties in the ![Cog wheel](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) Properties menu under Appearance > Font.
4. Resize the object as desired and then change the band size so that the objects take up the entire band height.
5. Next, let's add column headers for the sub-bands. From the toolbox on the left side of the designer, drag two ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_text.svg) Label objects (one for Region, one for Sales) onto SubBand1.
6. Arrange the labels at the top of SubBand1, or as desired.
7. Double-click each label and insert your own custom fixed text. In this case, you can use the field names.
8. Customize font as desired. For example, you might want columns headers to stand out, so you could make them bold.
9. Copy the two labels and paste them onto SubBand2 and SubBand3.

Your template should look something like the following.

Report template for example with sub-bands

![Report template showing the structure of bands and sub-bands, as well as the label objects,  that will create the output](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-sub-bands-example-template.png "Click to view full size")

Click Save template, and then click Preview report. Download the report and open it.

Report preview

![Generated report showing the highly formatted tables created from sub-bands](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-sub-bands-example-preview.png "Click to view full size")
