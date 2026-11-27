---
title: "Example - Creating a profit and loss table with vertical bands"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/PixelPerfect/pixelperfect-vertical-bands-example.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates", "Designing PixelPerfect report templates", "Adding content to your PixelPerfect report template", "Visualizing application data in your report"]
---

# Example - Creating a profit and loss table with vertical bands

In this example, you will use vertical bands to create a profit and loss report outlining the total sales and profit for each year in the application.

## Background

Vertical bands allow you to arrange report content differently than horizontal bands. Rather than a standard relational table, vertical bands form a structure where each column corresponds to a single value from a dimension in your application—for example, a year, month, or category dimension. Other columns of interest are organized as rows rather than columns. The classic example of vertical bands is the profit and loss report, where the profit and loss fields are listed as rows in the table, and each column in the table represents a single year, quarter, or month value.

For more information about vertical bands, see [*Working with vertical bands in PixelPerfect reporting*](pixelperfect-vertical-bands.htm).

## Preparations

Refer to the example application sources here: [*Examples - In-application reporting*](../../InAppGeneral/reporting-example-material.htm). Upload the application and data files into a space, and then reload the application. You are ready to complete the example.

## Step 1: Create data binding

Do the following:

1. Create a new PixelPerfect template.
2. Open the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu available from the right-side panel in the designer.

   Field List menu in the PixelPerfect designer

   ![The 'Field List' menu expanded from the right side panel in the PixelPerfect designer](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-gen-field-list.png "Click to view full size")
3. Hover your cursor over Levels, and then click ![Plus](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg).
4. Expand the Sales Tables sheet. Next to P&L by Year, click ![Plus](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg).

   The data binding is created.

## Step 2: Create the banded structure

Do the following:

1. On the design surface, right-click anywhere within the Detail1 band and click Insert Band > DetailReport.

   A new DetailReport band is inserted below Detail1.
2. Right-click the DetailReport band. Click Insert Vertical Band > VerticalHeader.

   VerticalHeader and VerticalDetail bands are added.
3. Right-click the DetailReport band again. Click Insert Vertical Band > VerticalTotal.

   A VerticalTotal band is added.

You can reduce the width of the bands to save space.

## Step 3: Connect the structure to data binding

Do the following:

1. Select the DetailReport band that contains the vertical bands.
2. Click the gear icon at the edge of the design surface.

   Clicking the gear icon

   ![Close-up of the side of the design surface with a band selected, and the gear icon clicked, showing a popup menu for different settings](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-format-table-cog.png "Click to view full size")
3. In the menu, select the P&L by Year level as the Data Member.

   Tip noteAlternatively, click ![Cog wheel](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) at the far right of the designer. Add the Data Member under Detail Report Tasks.

## Step 4: Add headers

Do the following:

1. From the toolbox on the left side of the designer, drag three ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_text.svg) Label objects onto the VerticalHeader1 band, stacking them horizontally as a series of three rows.
2. Double-click each label and give them the following fixed text, respectively:

   - Year
   - Total Sales
   - Total Profit
3. From the toolbox on the left side of the designer, drag a ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_text.svg) Label object onto the top of VerticalTotal1, arranging it so it is parallel with the Year label. Double-click the label and give it the following fixed text: All Time

## Step 5: Add data to template

Do the following:

1. Open the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu, and expand Levels.
2. Within the P&L by Year level, drag the following fields onto the VerticalDetail1 band, stacking them horizontally as a series of three rows. They should be in this order:

   - OrderYear
   - Sales
   - Profit
3. Select the Sales field you just added.
4. Click the gear icon at the edge of the design surface.
5. In the popout menu, click the ellipsis (three dots) menu under Text Format String.
6. The Format String Editor dialog opens. Choose Currency, and adjust the decimal points. Click OK.
7. Repeat this process for the Profit field.
8. Copy the Sales and Profit fields, and paste them onto the VerticalTotal1 band so that the pasted fields are parallel to the original fields.

## Step 6: Configure the total calculations

We need to configure the newly pasted Sales and Profit fields to summarize all data from the table columns.

Do the following:

1. Select the Sales field you pasted within the VerticalTotal1 band.
2. Open the ![Cog wheel](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) Properties menu from the right-side panel. Expand Data, and then expand Summary.
3. Set Running to Report.
4. Return to the design surface. Click the bold f icon near the selected Sales field to open the Expression Editor.
5. In the Expression Editor, enter the following expression:

   ```
   sumSum([P&L by Year (P&L by Year_Level).Sales])
   ```
6. Repeat this entire process for the Profit field you pasted within the VerticalTotal1 band, but instead use this expression:

   ```
   sumSum([P&L by Year (P&L by Year_Level).Profit])
   ```

Customize font properties in the ![Cog wheel](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) Properties menu under Appearance > Font.

Report template for profit and loss table

![Report template showing the structure defining the profit and loss table. The structure consists of a DetailReport band, within which there are 3 vertical bands side-by-side](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-p-l-table-template.png "Click to view full size")

Click Save template, and then click Preview report. Download the report and open it.

Report preview

![Generated report showing the profit and loss table. The table details the profit vs. sales for each of the three years in the app data](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-p-l-table-report.png "Click to view full size")
