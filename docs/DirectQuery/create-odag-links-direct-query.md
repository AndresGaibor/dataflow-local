---
title: "Creating ODAG links in Direct Query applications"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DirectQuery/create-odag-links-direct-query.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Accessing cloud databases directly with Direct Query"]
---

# Creating ODAG links in Direct Query applications

You can link your Direct Query application to an on-demand template application. Creating these On-Demand Application Generation (ODAG) links enables you to generate in-memory applications directly from your Direct Query application. This allows you to quickly extract data slices into Qlik Cloud for deeper analysis. For more information about generating an on-demand template application, see [*Exporting Direct Query application settings to a template application*](export-to-template-app-direct-query.htm).

## Creating an ODAG link

Do the following:

1. In the sheet editor, select App navigation links from the assets panel and click Create new.
2. In the window that appears, fill out the following fields:
   - Name

     The name of your application navigation link.
   - Template app

     Select your on-demand template application from the drop-down list.
   - Expression

     The expression for the [dimension](#glossary-1 "Glossary term") used in your filter when you generated the on-demand template application.
   - Maximum row count

     The maximum number of rows allowed for the link to function.
3. Check the box Overwrite generated apps.
4. Set Default view when opened to App overview to view your generated application or My new sheet to go to the sheet editor.
5. Click Create.

## Using an ODAG link

Once you have created an ODAG link, you must now create an interface to use it from your Direct Query application.

Do the following:

1. In the sheet editor in your Direct Query application, create a button. For more information, see Adding visualizations in [*Creating a Direct Query application*](create-direct-query-app.htm).

   Information noteYou can access the link by dragging it from the assets panel and dropping it on the sheet, but creating a button is recommended for ease of use.
2. Select your button and, in the [properties](#glossary-2 "Glossary term") panel, click Actions and navigation.
3. In the Navigation drop-down list, select On-demand app.
4. In the On-demand drop-down list, select your ODAG link.
5. Click Enable chart.
6. Set Condition to enable chart to ON.
7. Set the condition so the button is only enabled when your filter dimension = 1.

In the sheet view, your button will now be able to automatically generate a new on-demand in-memory application based on your selected dimension as long as you have selected exactly one value for your filter dimension. The generated application will have the same settings as your Direct Query application and will overwrite any previously generated on-demand applications.

## Limitations

Generated on-demand applications with Direct Query applications have the following limitations:

- Row data fetch limits in the Direct Query SQL query impact the generated on-demand applications. For more information, see [*Direct Query limitations*](limitations-direct-query.htm).
