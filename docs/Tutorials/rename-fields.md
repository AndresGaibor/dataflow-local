---
title: "Renaming fields"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Tutorials/rename-fields.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Tutorial - Scripting for beginners"]
---

# Renaming fields

In the previous topic, we showed you how to rename [fields](#glossary-0 "Glossary term") in the data preview window. In the heading of the data preview window, you renamed Invoice Date to Bill Date. When you inserted the [load script](#glossary-1 "Glossary term"), you could see that the field would be renamed using the keyword AS.

Load script window renaming Invoice Date as Bill Date

![Load script window renaming Invoice Date as Bill Date.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-load_rename_as-cloud-rev.png "Click to view full size")

We can also perform this action directly in the script.

Do the following:

1. Open the Data load editor in the Scripting Tutorial application.
2. Click the Sales tab.
3. In the load script, make the following changes. Note that you have to include parentheses around fields that contain a space.
   1. Change GrossSales, to:

   ```
   GrossSales AS "Gross Sales",
   ```

   2. Change "Item Desc", to:

   ```
   "Item Desc" AS "Item Description",
   ```

Your script should look like this:

Load script window with script to rename fields

![Load script window with script to rename fields.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-load_rename_fields-cloud-rev.png "Click to view full size")4. Click Load data. The data is loaded.
5. Open the Data model viewer. Confirm that the fields have been renamed.
6. You can also view all your fields in an application. Click the Analysis/Sheet tab in the top toolbar. The application opens in sheet view.
7. Click Edit sheet, and then click Fields in the assets panel. You can see the field names that you changed. You can use any of these fields in the visualizations that you create in your application.

Renamed fields in analysis view

![Renamed fields in analysis view.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-edit-sheet-renamed-fields-rev.png "Click to view full size")
