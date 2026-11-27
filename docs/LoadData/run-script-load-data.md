---
title: "Running load scripts to load data in applications"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/run-script-load-data.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Scripting to load or export data"]
---

# Running load scripts to load data in applications

Click ![load data](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_play_2_outline.svg) Load data in the toolbar to run the script and reload data in the application. The application is automatically saved before loading the data.

The Data load progress dialog is displayed, and you can Abort the load. When the data load has completed, the dialog is updated with status (Finished successfully or Data load failed) and a summary of possible errors and warnings, such as for synthetic keys. The summary is also displayed in Output, if you want to view it after the dialog is closed.

You can preview the loaded data and view profiling information by clicking the Preview button.

Information noteIf you want the Data load progress dialog to always close automatically after a successful execution, select Close when successfully finished.

Information noteWhen you create a new application, its size is initially unknown. To avoid any issues, run your first reload via the Reload now option from your [activity center](#glossary-0 "Glossary term"). This will accurately determine the size of your application and ensure it is routed to the appropriate engine based on its size.
