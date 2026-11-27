---
title: "Making preparations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/build-app.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Tutorial - Build an analytics application"]
---

# Making preparations

In this step, you will create a new analytics application, and add the data files from the BuildingAnAppFiles folder.

## Opening Qlik Cloud

Open Qlik Cloud by entering a web address in your browser, such as https://<your tenant address>. If a login window is opened in your browser, enter your user name and password. The exact address and credentials that you enter depend on how your organization has deployed Qlik Cloud.

## Placing tutorial source files in a new application

The BuildingAnAppFiles folder you downloaded contains the data files. Before you start creating [visualizations](#glossary-0 "Glossary term") you need to make a new application and add your data.

When you create a new application, put it in your [personal space](#glossary-1 "Glossary term"). Your personal space is your own private work area.

### Create a new application

Do the following:

1. Log in to Qlik Cloud.
2. Go to the Create page of the Analytics [activity center](#glossary-2 "Glossary term") and select Analytics app.
3. Type a Name for your application. For example: Building an app tutorial.
4. Choose a Space for your new application.

   The default option is your Personal space.
5. Click Create.

### Upload the tutorial source files

You need to upload the data files.

This section shows you to upload different types of files as data sources. Four files are in .xlsx (Excel) format, and one file is in CSV format. To teach you how to process different data sources, the CSV file has embedded field names. Adding a file with embedded field names to your data model requires additional configuration to ensure the field names are included.

#### Upload the Excel files

Do the following:

1. Open the application you created.

   You will see the application overview screen.
2. Select the four .xlsx data files from the BuildingAnAppFiles folder and drag them to the Files and other sources tile. These four files are:

   - Cities.xlsx
   - Customers.xlsx
   - Item master.xlsx
   - Sales.xlsx

   ![The view in an app with no data. There are 3 cards:Data catalog, Files and other sources, Data load editor.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_tutorial_adding_data_empty_app.png)

Information note

If you see a dialog box that says "Replace file? This file already exists", then you may have added these files to your personal space previously. Or you may have different data files with the same file names. You can choose to replace the existing files, or cancel the upload.

The data files are added to your personal data files.

#### Upload the CSV file

Do the following:

1. In the top left, click ![Add](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) Add data. Click Files and other sources.
2. Drag the Sales rep.csv file onto the Drop a file here or click to select a file tile.
3. You will see the data table. Make sure that the Field names drop-down is set to Embedded field names.
4. Click Next.

Information note

If you see a dialog box that says "Replace file? This file already exists", then you may have added these files to your personal space previously. Or you may have different data files with the same file names. You can choose to replace the existing files, or cancel the upload.

Data files in the Data manager

![Data tables in Data manager ready to be associated](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_tutorial_add-data.png "Click to view full size")

All required files have now been added to your personal data files. They are ready to be associated.

The next step is to associate and load the data.
