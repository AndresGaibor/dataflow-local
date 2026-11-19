---
title: "Scripting in the data load editor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/introduction-to-data-loading.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Tutorial - Scripting for beginners"]
---
# Scripting in the data load editor

Applications use a [data load script](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/introduction-to-data-loading.htm#glossary-0 "Glossary term"), which is managed in the [Data load editor](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/introduction-to-data-loading.htm#glossary-1 "Glossary term"), to connect
to and retrieve data from various data sources. A data source can be a data file, for example an Excel file or a .csv file. A data source can also be a database, for example a Google BigQuery or Salesforce database.

You can also load data using the [Data manager](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/introduction-to-data-loading.htm#glossary-2 "Glossary term"), but when you want to create, edit and run a data load script you use the data load editor.

In the script, the fields and tables to load are specified. Scripting is often used to specify what data to load from your data sources. You can also manipulate the data structure by using script statements.

During the data load, Qlik Sense identifies
common [fields](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/introduction-to-data-loading.htm#glossary-3 "Glossary term") from different tables (key fields) to associate the data. The resulting data structure of the data in the application can be monitored
in the data model viewer. Changes to the data structure can be achieved by renaming fields to obtain different associations between tables.

After the data has been loaded into an application, it is stored in the application.

## Data load editor

You can create scripts to load data in [Data load editor](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/introduction-to-data-loading.htm#glossary-4 "Glossary term"). The editor is available from the drop-down menu in the application.

When you open the data load editor, the script editor appears in the middle of your screen. Script sections are shown as tabs in the left menu. The application automatically creates the **Main** section. [Data connections](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/introduction-to-data-loading.htm#glossary-5 "Glossary term") are shown in the right menu.

The script must be written using the Qlik Sense script syntax. Qlik Sense syntax keywords are highlighted in blue.

Data load editor

![Data load editor.](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial_data_load_editor-cloud-rev2.png)

## Script editor

There are a number of functions available in the editor to assist you in developing the load script.

### Accessing syntax help for commands and functions

There are several ways to access syntax help for a Qlik Sense syntax keyword.

#### Accessing the help portal

You can access detailed help in the Qlik helpsite in two different ways.

- Click ![Help](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_help_outline.svg) in the toolbar to enter syntax help mode.
  In syntax help mode you can click on a syntax keyword (marked in blue and underlined) to access syntax help.
- Place the cursor inside or at the end of the keyword and press Ctrl+H.
- > **Note:** You cannot edit the script in syntax help mode.

#### Using the autocomplete function

If you start to type a Qlik Sense script keyword, you get an autocomplete list of matching keywords to select from. The list is narrowed down as you continue to type, and you can select from templates with suggested syntax and parameters. A tooltip displays the syntax of the function, including parameters and additional statements, as well as a link to the help portal description of the statement or function.

You can turn the autocomplete hints off or on by clicking ![Autocomplete hints on](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_autocomplete_on_outline.svg) or ![Autocomplete hints off](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_autocomplete_off_outline.svg).

> **Tip:** You can also use the keyboard shortcut Ctrl+Space to show the keyword list, and Ctrl+Shift+Space to show a tooltip.

### Commenting in the script

You can insert comments in the script code, or deactivate parts of the script code by using comment marks. All text on a line that follows to the right of // (two forward slashes) will be considered a comment and will not be executed when the script is run.

The data load editor toolbar contains a shortcut for commenting or uncommenting code. Click ![Comment / Uncomment](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_comment_outline.svg), or press Ctrl + K to comment or uncomment code.

### Indenting code

You can indent the code to increase readability. Click ![Indent](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_indent_outline.svg) to indent the text (increase indentation) or, click ![Undent](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_undent_outline.svg) to outdent the text (decrease indentation).

### Inserting a prepared test script

You can insert a prepared test script that will load a set of inline data fields. You can use this to quickly create a data set for test purposes. Press Ctrl + 00 to insert the test script.

## Script history

You can view the history of the different versions of your load script in **History**.
