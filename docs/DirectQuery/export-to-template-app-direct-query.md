---
title: "Exporting Direct Query application settings to a template application"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DirectQuery/export-to-template-app-direct-query.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Accessing cloud databases directly with Direct Query"]
---

# Exporting Direct Query application settings to a template application

You can export your Direct Query application directly into an on-demand template application. This allows you to make a deeper, more customizable analysis of your data than what is possible with Direct Query

## Generating a template application

The most important thing when generating an on-demand template application is the [dimension](#glossary-1 "Glossary term") to use as the filter when generating on-demand in-memory applications. The on-demand template application lets you to reuse your Direct Query settings in the on-demand applications, while only having to alter a single dimension.

Do the following:

1. In a dashboard, select values for one or more fields. Only the selected values will be displayed in the template application.
2. In the navigation bar, click the menu to left of the Prepare tab.
3. Select Generate template app from the drop-down list.
4. In the window that appears, enter a name for your application and select the space where you want it to be created and click Generate.
5. Once the application has been generated, click Open.

   Information noteThis will take you to the [Data load editor](#glossary-2 "Glossary term") of your newly generated on-demand template application.

   Tip noteThe template script is intended to be extended, edited and copied according to your needs. You will most likely want to be able to load other sources using the selection [field](#glossary-3 "Glossary term") and the ODAG bindings.
6. In the top right, click Load data.
7. Once the data has loaded, Click the Sheet button in the top left corner.
8. Build a new sheet.
9. Create your desired visualizations, see Adding visualizations in [*Creating a Direct Query application*](create-direct-query-app.htm). These are the visualizations that will be shown in the generated on-demand applications.

Once you have saved your changes, your on-demand template application will be available for use by creating an ODAG link in your Direct Query application. For more information, see [*Creating ODAG links in Direct Query applications*](create-odag-links-direct-query.htm).
