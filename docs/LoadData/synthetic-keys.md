---
title: "Synthetic keys"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/synthetic-keys.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Tutorial - Scripting for beginners"]
---

# Synthetic keys

When two or more internal tables have two or more fields in common, this implies a composite key relationship. Applications handle this through synthetic keys. These keys are anonymous fields that represent all occurring combinations of the composite key.

An increased number of composite keys can result in elevated memory usage, and can affect performance. This may also depend on data amounts, table structure, and other factors. Whenever there are several synthetic keys that are dependent on each other, it is good practice to remove them.

Now it is time to load our final set of data.

Do the following:

1. Open the Data load editor in the Scripting Tutorial application.
2. Click ![Create new section](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) to add a new script section.
3. Name the section Customers.
4. Under DataFiles in the right menu, click Select data.
5. Upload and then select Customers.xlsx. Click Continue. The data preview window opens.
6. Select Sheet1.
7. Click Add.
8. Click Load data.

Now you can see in the data load progress window that a synthetic keys was created.

Data load progress window with synthetic key warning

![Data load progress window with synthetic key warning.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-load-progress-synthetic-key.png "Click to view full size")9. Open the Data model viewer.

We can see that a synthetic key has been created by seeing that a new table, $Syn 1 Table, has been created. It contains all the fields, Region and Region code, that the connected tables Sheet1 and Region have in common. In this case it makes the connections a bit confusing and misleading, so it is not desirable to keep.

Data model viewer showing synthetic key

![Data model viewer showing synthetic key.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-data-model-synthetic-key.png "Click to view full size")

## Resolving synthetic keys

The easiest way to eliminate synthetic keys is to rename one or more fields in the tables. This can be done when loading the data. Now we will go through the steps of how to remove a synthetic key.

Do the following:

1. Open the Data load editor.
2. Click the section Customers and delete the row in the LOAD statement saying:

Region,

3. Click Load data.
4. Open the Data model viewer.

The synthetic key is has been removed.

Data model viewer showing that synthetic key has been removed

![Data model viewer showing that synthetic key has been removed.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-data-model-synthetic-key-fixed.png "Click to view full size")
