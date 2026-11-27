---
title: "Data manager"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/data-management.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Understanding applications", "Navigating in the application interface"]
---

# Data manager

Add data from data sources in [Data manager](#glossary-0 "Glossary term") and then preview and associate the data. Perform other actions, such as add calculated fields. When you are done, load the data.

Click Data manager in the application navigation menu to open Data manager.

Associations is the default view. You can also select Tables view.

If you have not added data to your application, you are instead prompted to do so before you can associate the data.

In both views you can:

- Add data and load data. Add data to Qlik Sense to preview and perform actions on the data, and then load the data. You can also reload data. See: [*Adding data to the application from connections and new files*](adding-data.htm)
- Concatenate or join tables: See: [*Concatenating tables in Data manager*](concatenating-tables-in-data-manager.htm), [*Joining tables in Data manager*](join-keep-tables-in-data-manager.htm)

See also: [*Loading and managing data with Data Manager*](managing-data.htm)

## Associations view

View data tables represented as bubbles. The size of the bubble represents the amount of data in the table. The links between the bubbles represent the associations between tables. When two tables are associated, select the button in the link to view or edit the association.

Click Apply all or Apply to apply the recommended associations. Click the link between the bubbles to view the association in the data preview panel.

Select a table and then click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) to edit the table. Select a table and then click Show data preview to preview the data.

Associations view in data manager

![Associations view in data manager.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_data_manager_associations.png "Click to view full size")

You can also associate tables automatically according to Insight Advisor recommendations by clicking ![Effects](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_effects.svg), and add more tables to your application.

See:

- [*Managing data associations*](associating-data.htm)
- [*Editing a table*](editing-table.htm)

## Tables view

View data tables represented as tables.

Select a table and then click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) to edit the table. Select a table and then click Show data preview to preview the data.

Tables view in data manager

![Tables view in data manager.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_data_manager_tables.png "Click to view full size")

See: [*Editing a table*](editing-table.htm)

Data manager tools

| UI item | Description |
| --- | --- |
| Edit | Edit the selected table. |
| Reload | Reload the selected table. |
| Delete | Delete the selected table. |
| Clear filter | Clear data filters. |
| More | Concatenate the selected table or view table transformation details. |

Related learning:

- [Introduction to the data manager](/lnk/Intro_Data_Manager_QS)
